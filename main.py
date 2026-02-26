import os
import logging
import base64
import requests
from datetime import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

TOKEN = os.environ.get("TELEGRAM_TOKEN")
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")
GITHUB_TOKEN = os.environ.get("GH_TOKEN")
GITHUB_USER = "Levros7"
GITHUB_REPO = "obsidian-telegram-bot"
FILE_PATH = "Claude_Conversations.md"


def get_file():
    url = f"https://api.github.com/repos/{GITHUB_USER}/{GITHUB_REPO}/contents/{FILE_PATH}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        data = r.json()
        content = base64.b64decode(data["content"]).decode("utf-8")
        return content, data["sha"]
    return "", None

def save_to_github(topic):
    today = datetime.now().strftime("%Y-%m-%d")
    time_now = datetime.now().strftime("%H:%M")
    content, sha = get_file()

    if f"## {today}" not in content:
        content += f"
## {today}
"
    content += f"- {time_now} — {topic}
"

    url = f"https://api.github.com/repos/{GITHUB_USER}/{GITHUB_REPO}/contents/{FILE_PATH}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    encoded = base64.b64encode(content.encode("utf-8")).decode("utf-8")

    payload = {"message": f"Add topic: {topic}", "content": encoded}
    if sha:
        payload["sha"] = sha

    r = requests.put(url, json=payload, headers=headers)
    return r.status_code == 200 or r.status_code == 201

def save_lasttopic_to_github(text):
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M")
    day_str = now.strftime("%A")
    content, sha = get_file()

    entry = (
        f"
---
"
        f"**Last Claude Topic**
"
        f"📅 {day_str}, {date_str} — {time_str}
"
        f"💬 {text}
"
    )

    content += entry

    url = f"https://api.github.com/repos/{GITHUB_USER}/{GITHUB_REPO}/contents/{FILE_PATH}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    encoded = base64.b64encode(content.encode("utf-8")).decode("utf-8")

    payload = {"message": f"Last topic: {text}", "content": encoded}
    if sha:
        payload["sha"] = sha

    r = requests.put(url, json=payload, headers=headers)
    return r.status_code == 200 or r.status_code == 201

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Obsidian bot running!
"
        "Commands:
"
        "/topic <text> — save a topic entry
"
        "/lasttopic <text> — record the last Claude conversation topic"
    )

async def topic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /topic <topic name>")
        return
    text = " ".join(context.args)
    success = save_to_github(text)
    if success:
        await update.message.reply_text(f"✅ Saved to Obsidian: {text}")
    else:
        await update.message.reply_text("❌ Failed to save")

async def lasttopic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /lasttopic <topic text>")
        return
    text = " ".join(context.args)
    success = save_lasttopic_to_github(text)
    if success:
        now = datetime.now()
        await update.message.reply_text(
            f"✅ Saved to Obsidian:
"
            f"📅 {now.strftime('%A, %Y-%m-%d')} — {now.strftime('%H:%M')}
"
            f"💬 {text}"
        )
    else:
        await update.message.reply_text("❌ Failed to save")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("topic", topic))
app.add_handler(CommandHandler("lasttopic", lasttopic))
app.run_webhook(
    listen="0.0.0.0",
    port=int(os.environ.get("PORT", 8080)),
    webhook_url=WEBHOOK_URL
)
