import os
import logging
import base64
import requests
from datetime import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import anthropic

logging.basicConfig(level=logging.INFO)

TOKEN = os.environ.get("TELEGRAM_TOKEN")
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")
GITHUB_TOKEN = os.environ.get("GH_TOKEN")
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
GITHUB_USER = "Levros7"
GITHUB_REPO = "obsidian-telegram-bot"
NOTES_REPO = os.environ.get("NOTES_REPO", "obsidian-notes-private")
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
        content += f"\n## {today}\n"
    content += f"- {time_now} — {topic}\n"

    url = f"https://api.github.com/repos/{GITHUB_USER}/{GITHUB_REPO}/contents/{FILE_PATH}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    encoded = base64.b64encode(content.encode("utf-8")).decode("utf-8")

    payload = {"message": f"Add topic: {topic}", "content": encoded}
    if sha:
        payload["sha"] = sha

    r = requests.put(url, json=payload, headers=headers)
    return r.status_code in (200, 201)

def save_lasttopic_to_github(text):
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M")
    day_str = now.strftime("%A")

    # 1. Create a new file per topic
    safe_text = text.replace("/", "-").replace("\\", "-").strip()
    topic_filename = f"{date_str} {safe_text}.md"
    topic_content = (
        f"# {safe_text}\n\n"
        f"📅 {day_str}, {date_str} — {time_str}\n\n"
        f"💬 {text}\n"
    )
    topic_url = f"https://api.github.com/repos/{GITHUB_USER}/{GITHUB_REPO}/contents/{topic_filename}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    encoded_topic = base64.b64encode(topic_content.encode("utf-8")).decode("utf-8")
    payload_topic = {"message": f"New topic: {text}", "content": encoded_topic}
    r1 = requests.put(topic_url, json=payload_topic, headers=headers)

    # 2. Append a wikilink to the index file (Claude_Conversations.md)
    content, sha = get_file()
    if f"## {date_str}" not in content:
        content += f"\n## {date_str}\n"
    content += f"- {time_str} — [[{date_str} {safe_text}]]\n"

    index_url = f"https://api.github.com/repos/{GITHUB_USER}/{GITHUB_REPO}/contents/{FILE_PATH}"
    encoded_index = base64.b64encode(content.encode("utf-8")).decode("utf-8")
    payload_index = {"message": f"Index: {text}", "content": encoded_index}
    if sha:
        payload_index["sha"] = sha
    r2 = requests.put(index_url, json=payload_index, headers=headers)

    return r1.status_code in (200, 201) and r2.status_code in (200, 201)

def ask_claude(question, context_text):
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=500,
        system="You are a helpful assistant. Answer using ONLY the notes provided. If the answer isn't in the notes, say so clearly.",
        messages=[{
            "role": "user",
            "content": f"Notes:\n{context_text}\n\nQuestion: {question}"
        }]
    )
    return response.content[0].text


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Obsidian bot running!\n"
        "Commands:\n"
        "/topic <text> — save a topic entry\n"
        "/lasttopic <text> — record the last Claude conversation topic\n"
        "/ask <question> — ask a question about your Obsidian notes"
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
            "✅ Saved to Obsidian:\n"
            f"📅 {now.strftime('%A, %Y-%m-%d')} — {now.strftime('%H:%M')}\n"
            f"💬 {text}"
        )
    else:
        await update.message.reply_text("❌ Failed to save")


def get_all_notes():
    """Fetch all .md files from private notes repo"""
    url = f"https://api.github.com/repos/{GITHUB_USER}/{NOTES_REPO}/contents/"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        return ""
    files = r.json()
    all_text = ""
    for f in files[:30]:  # limit to 30 files per request
        if f["name"].endswith(".md"):
            fr = requests.get(f["download_url"], headers=headers)
            if fr.status_code == 200:
                all_text += f"\n\n--- {f['name']} ---\n{fr.text}"
    return all_text

async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /ask <your question>")
        return
    question = " ".join(context.args)
    await update.message.reply_text("🔍 Searching your notes...")
    notes = get_all_notes()
    if not notes:
        await update.message.reply_text("❌ Could not fetch notes from GitHub")
        return
    answer = ask_claude(question, notes)
    await update.message.reply_text(f"💬 {answer}")


app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", topic))
app.add_handler(CommandHandler("topic", topic))
app.add_handler(CommandHandler("lasttopic", lasttopic))
app.add_handler(CommandHandler("ask", ask))
app.run_webhook(
    listen="0.0.0.0",
    port=int(os.environ.get("PORT", 8080)),
    webhook_url=WEBHOOK_URL
)
# This line is just a marker - we'll edit main.py next
# This line intentionally left blank
