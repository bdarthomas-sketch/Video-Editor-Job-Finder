import os
import json
import time
import re
import feedparser
import pyfiglet
import requests
from datetime import datetime, timezone
from dotenv import load_dotenv
from colorama import init, Fore, Style
from keywords import (
    JOB_KEYWORDS, VIDEO_EDITING_KEYWORDS, REMOTE_KEYWORDS,
    PAY_KEYWORDS, SPANISH_INDICATORS, ENGLISH_BASIC_INDICATORS,
    VALID_LEVEL_KEYWORDS, EXCLUDE_LEVEL, EXCLUDE_TOPICS,
    NON_VIDEO_JOB_KEYWORDS, SCORE, MIN_SCORE
)

init(autoreset=True)

load_dotenv()

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
    print("❌ ERROR: Faltan variables de entorno TELEGRAM_TOKEN y/o TELEGRAM_CHAT_ID.")
    exit(1)

SUBREDDITS_EN = ["forhire", "VideoEditing", "HireAnEditor", "freelance_forhire", "DesignJobs", "RemoteJobs"]
SUBREDDITS_ES = ["empleos_AR", "TrabajoArgentina"]

SEEN_FILE = "seen_ids.json"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}


def load_seen():
    if os.path.exists(SEEN_FILE):
        with open(SEEN_FILE, "r") as f:
            return set(json.load(f))
    return set()


def save_seen(seen):
    with open(SEEN_FILE, "w") as f:
        json.dump(list(seen), f)


def send_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    resp = requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": text, "parse_mode": "HTML"})
    if not resp.ok:
        print(f"{Fore.RED}  ⚠ Telegram error {resp.status_code}: {resp.text}{Style.RESET_ALL}")


def score_post(title, body, is_english_sub):
    text = (title + " " + body).lower()
    score = 0
    matches = []

    categories = [
        ("job", JOB_KEYWORDS, SCORE["job"]),
        ("video_editing", VIDEO_EDITING_KEYWORDS, SCORE["video_editing"]),
        ("remote", REMOTE_KEYWORDS, SCORE["remote"]),
        ("pay", PAY_KEYWORDS, SCORE["pay"]),
        ("spanish", SPANISH_INDICATORS, SCORE["spanish"]),
        ("english", ENGLISH_BASIC_INDICATORS, SCORE["english"]),
        ("valid_level", VALID_LEVEL_KEYWORDS, SCORE["valid_level"]),
        ("exclude_level", EXCLUDE_LEVEL, SCORE["exclude_level"]),
        ("exclude_topic", EXCLUDE_TOPICS, SCORE["exclude_topic"]),
        ("non_video_job", NON_VIDEO_JOB_KEYWORDS, SCORE["non_video_job"]),
    ]

    for name, keywords, pts in categories:
        matched = next((kw for kw in keywords if kw in text), None)
        if matched:
            score += pts
            matches.append((pts, name, matched))

    if is_english_sub and not any(kw in text for kw in SPANISH_INDICATORS) and not any(kw in text for kw in ENGLISH_BASIC_INDICATORS):
        return 0

    # ponytail: debug temporal — quitar cuando no haga falta más
    if not is_english_sub and score < 0:
        for pts, name, kw in matches:
            sign = "+" if pts > 0 else ""
            print(f"  [DEBUG] {sign}{pts} {name}: \"{kw}\"")

    return score


def fetch_subreddit_new(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/search.rss"
    params = {"q": "video+editor", "sort": "new", "restrict_sr": "on", "limit": "25"}
    resp = requests.get(url, headers=HEADERS, params=params, timeout=15)
    if resp.status_code == 429:
        time.sleep(30)
        resp = requests.get(url, headers=HEADERS, params=params, timeout=15)
    resp.raise_for_status()
    feed = feedparser.parse(resp.text)
    results = []
    for entry in feed.entries:
        title = entry.get("title", "")
        summary = entry.get("summary", "")
        post_id = entry.get("id", entry.get("link", ""))
        results.append({
            "id": post_id,
            "title": title,
            "link": entry.get("link", ""),
            "summary": summary,
            "published": entry.get("published", ""),
            "subreddit": subreddit,
        })
    return results


def fetch_global_search(keyword):
    url = "https://www.reddit.com/r/all/search.rss"
    params = {"q": keyword, "sort": "new", "restrict_sr": "on", "limit": "25"}
    resp = requests.get(url, headers=HEADERS, params=params, timeout=15)
    if resp.status_code == 429:
        time.sleep(30)
        resp = requests.get(url, headers=HEADERS, params=params, timeout=15)
    resp.raise_for_status()
    feed = feedparser.parse(resp.text)
    results = []
    for entry in feed.entries:
        title = entry.get("title", "")
        summary = entry.get("summary", "")
        post_id = entry.get("id", entry.get("link", ""))
        results.append({
            "id": post_id,
            "title": title,
            "link": entry.get("link", ""),
            "summary": summary,
            "published": entry.get("published", ""),
            "subreddit": "r/all",
        })
    return results


def format_post(post):
    try:
        created = datetime.strptime(post["published"], "%a, %d %b %Y %H:%M:%S %z").strftime("%d/%m/%Y")
    except (ValueError, KeyError):
        created = "?"
    body = re.sub(r"<[^>]+>", " ", post.get("summary", ""))[:300]
    body = " ".join(body.split())
    title = post["title"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    body = body.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return (
        f"<b>{title}</b>\n"
        f"r/{post['subreddit']} · {created}\n"
        f"{body}\n\n"
        f"<a href=\"{post['link']}\">Ver post</a>"
    )


def run_cycle(seen):
    sent_count = 0
    all_subs = [(s, True) for s in SUBREDDITS_EN] + [(s, False) for s in SUBREDDITS_ES]

    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f"\n{Fore.CYAN}🔍 Búsqueda iniciada — {now}{Style.RESET_ALL}\n")

    for sub, is_en in all_subs:
        print(f"{Fore.YELLOW}📡 Revisando r/{sub}...{Style.RESET_ALL}")
        try:
            posts = fetch_subreddit_new(sub)
            for p in posts:
                pid = p["id"]
                if pid in seen:
                    print(f"  ❌ {p['title'][:60]} — ya visto")
                    continue
                s = score_post(p["title"], p["summary"], is_en)
                if s < MIN_SCORE:
                    print(f"  ❌ Score {s}: {p['title'][:60]} — descartado")
                    continue
                print(f"  {Fore.GREEN}✅ Score {s}: {p['title'][:60]}{Style.RESET_ALL}")
                seen.add(pid)
                send_telegram(format_post(p))
                sent_count += 1
                time.sleep(0.5)
        except Exception as e:
            print(f"{Fore.RED}Error en r/{sub}: {e}{Style.RESET_ALL}")
        time.sleep(15)

    global_keywords = ["video editor", "video editing", "editor de video"]
    for kw in global_keywords:
        print(f"{Fore.YELLOW}📡 Buscando en r/all: {kw}...{Style.RESET_ALL}")
        try:
            posts = fetch_global_search(kw)
            for p in posts:
                pid = p["id"]
                if pid in seen:
                    print(f"  ❌ {p['title'][:60]} — ya visto")
                    continue
                s = score_post(p["title"], p["summary"], True)
                if s < MIN_SCORE:
                    print(f"  ❌ Score {s}: {p['title'][:60]} — descartado")
                    continue
                print(f"  {Fore.GREEN}✅ Score {s}: {p['title'][:60]}{Style.RESET_ALL}")
                seen.add(pid)
                send_telegram(format_post(p))
                sent_count += 1
                time.sleep(0.5)
        except Exception as e:
            print(f"{Fore.RED}Error en búsqueda global '{kw}': {e}{Style.RESET_ALL}")
        time.sleep(15)

    save_seen(seen)

    if sent_count == 0:
        send_telegram("✅ Búsqueda completada. Sin nuevos posts.")
    else:
        send_telegram(f"✅ Búsqueda completada. {sent_count} posts enviados.")

    print(f"\n✔ Búsqueda completada. {sent_count} posts enviados.")
    return sent_count


def main():
    banner = pyfiglet.figlet_format("Video Job Finder", font="slant")
    print(f"\033[38;5;208m{banner}\033[0m")

    seen = load_seen()
    in_github = os.environ.get("GITHUB_ACTIONS") == "true"

    try:
        if in_github:
            run_cycle(seen)
        else:
            while True:
                run_cycle(seen)
                print(f"\n⏳ Próxima búsqueda en 60 minutos...")
                time.sleep(3600)
    except KeyboardInterrupt:
        print(f"\n👋 Bot detenido.")


if __name__ == "__main__":
    main()
