import os
import logging
from datetime import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

TOKEN = os.environ.get("TELEGRAM_TOKEN")
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Obsidian bot is running!\nUse /topic <text> to save a topic.")

async def topic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /topic <topic name>")
        return
    
    text = " ".join(context.args)
    today = datetime.now().strftime("%Y-%m-%d")
    time_now = datetime.now().strftime("%H:%M")
    
    with open("topics.md", "a") as f:
        f.write(f"\n## {today}\n- {time_now} — {text}\n")
    
    await update.message.reply_text(f"✅ Saved: {text}")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("topic", topic))
app.run_webhook(
    listen="0.0.0.0",
    port=int(os.environ.get("PORT", 8080)),
    webhook_url=WEBHOOK_URL
)
