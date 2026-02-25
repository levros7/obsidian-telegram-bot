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
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GITHUB_USER = "Levros7"
GITHUB_REPO = "obsidian-telegram-bot"
FILE_PATH = "Claude Conversations.md"

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
        content += f"\n## {today}\n"
    content += f"- {time_now} — {topic}\n"
    
    url = f"https://api.github.com/repos/{GITHUB_USER}/{GITHUB_REPO}/contents/{FILE_PATH}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    encoded = base64.b64encode(content.encode("utf-8")).decode("utf-8")
    
    payload = {"message": f"Add topic: {topic}", "content": encoded}
    if sha:
        payload["sha"] = sha
    
    r = requests.put(url, json=payload, headers=headers)
    return r.status_code == 200 or r.status_code == 201

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Obsidian bot running!\nUse /topic <text>")

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

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("topic", topic))
app.run_webhook(
    listen="0.0.0.0",
    port=int(os.environ.get("PORT", 8080)),
    webhook_url=WEBHOOK_URL
)
