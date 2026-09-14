# Reddit Video Editor Bot

Busca posts de trabajo de edición de video en Reddit y los envía a Telegram.

## Setup

1. Ir a **Settings > Secrets and variables > Actions** en tu repo
2. Crear dos secrets:
   - `TELEGRAM_TOKEN` — token del bot de BotFather
   - `TELEGRAM_CHAT_ID` — ID del chat o grupo donde recibir los mensajes

## Ejecución

1. Ir a **Actions > Reddit Video Editor Bot**
2. Hacer clic en **Run workflow**

## Agregar subreddits en español

Editar la lista `SUBREDDITS_ES` en `bot.py`:

```python
SUBREDDITS_ES = ["subreddit1", "subreddit2"]
```

El bot ya busca "editor de video" en español, solo falta agregar los subreddits.
