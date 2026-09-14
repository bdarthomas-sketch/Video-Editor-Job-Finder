import os
import json
import time
import feedparser
import pyfiglet
import requests
from datetime import datetime, timezone
from dotenv import load_dotenv
from colorama import init, Fore, Style

init(autoreset=True)

load_dotenv()

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

SUBREDDITS_EN = ["forhire", "VideoEditing", "editors", "HireAnEditor", "freelance_forhire", "DesignJobs", "RemoteJobs"]
SUBREDDITS_ES = ["empleos_AR", "TrabajoArgentina", "argentina", "AskArgentina"]

KEYWORDS = ["video editor", "video editing", "editor de video"]

EXCLUDE_LEVEL = ["senior", "expert", "advanced", "avanzado"]
REMOTE_KEYWORDS = ["remote", "remoto", "work from home", "online"]
PAY_KEYWORDS = ["usd", "crypto", "bitcoin", "eth", "usdt", "$"]

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
    requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": text, "parse_mode": "Markdown"})


def passes_filters(title, body, is_en):
    text = (title + " " + body).lower()

    if is_en and not any(w in text for w in ["spanish", "español"]):
        return "sub EN sin 'spanish'/'español'"

    if not any(kw in text for kw in KEYWORDS):
        return "sin keyword relevante"

    if not any(w in text for w in REMOTE_KEYWORDS):
        return "sin keyword remoto"

    if not any(w in text for w in PAY_KEYWORDS):
        return "sin mención de pago"

    if any(w in text for w in EXCLUDE_LEVEL):
        return "nivel excluido"

    if title.lower().startswith("[for hire]") or title.lower().startswith("[available]"):
        return "post [For Hire]"

    return None


def fetch_subreddit_new(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/new.rss"
    params = {"limit": "50"}
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
    url = "https://www.reddit.com/search.rss"
    params = {"q": keyword, "sort": "new", "limit": "50"}
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
            "subreddit": "global",
        })
    return results


def format_post(post):
    try:
        created = datetime.strptime(post["published"], "%a, %d %b %Y %H:%M:%S %z").strftime("%d/%m/%Y")
    except (ValueError, KeyError):
        created = "?"
    body = post.get("summary", "")[:300].replace("\n", " ")
    title = post["title"].replace("[", "\\[").replace("]", "\\]")
    body = body.replace("[", "\\[").replace("]", "\\]")
    return (
        f"*{title}*\n"
        f"r/{post['subreddit']} · {created}\n"
        f"{body}\n\n"
        f"[Ver post]({post['link']})"
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
                reason = passes_filters(p["title"], p["summary"], is_en)
                if reason:
                    print(f"  ❌ {p['title'][:60]} — {reason}")
                    continue
                print(f"  {Fore.GREEN}✅ Encontrado: {p['title'][:60]}{Style.RESET_ALL}")
                seen.add(pid)
                send_telegram(format_post(p))
                sent_count += 1
                time.sleep(0.5)
        except Exception as e:
            print(f"{Fore.RED}Error en r/{sub}: {e}{Style.RESET_ALL}")
        time.sleep(15)

    for kw in KEYWORDS:
        print(f"{Fore.YELLOW}📡 Revisando búsqueda global: {kw}...{Style.RESET_ALL}")
        try:
            posts = fetch_global_search(kw)
            for p in posts:
                pid = p["id"]
                if pid in seen:
                    print(f"  ❌ {p['title'][:60]} — ya visto")
                    continue
                reason = passes_filters(p["title"], p["summary"], True)
                if reason:
                    print(f"  ❌ {p['title'][:60]} — {reason}")
                    continue
                print(f"  {Fore.GREEN}✅ Encontrado: {p['title'][:60]}{Style.RESET_ALL}")
                seen.add(pid)
                send_telegram(format_post(p))
                sent_count += 1
                time.sleep(0.5)
        except Exception as e:
            print(f"{Fore.RED}Error en búsqueda global '{kw}': {e}{Style.RESET_ALL}")
        time.sleep(15)

    save_seen(seen)
    print(f"\n✔ Búsqueda completada. {sent_count} posts enviados.")
    return sent_count


def main():
    banner = pyfiglet.figlet_format("V1d30Edit0r Job Finder", font="slant")
    print(f"\033[38;5;208m{banner}\033[0m")

    seen = load_seen()

    try:
        while True:
            run_cycle(seen)
            print(f"\n⏳ Próxima búsqueda en 60 minutos...")
            time.sleep(3600)
    except KeyboardInterrupt:
        print(f"\n👋 Bot detenido.")


if __name__ == "__main__":
    main()
