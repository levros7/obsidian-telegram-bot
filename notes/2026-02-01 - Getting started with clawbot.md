# Getting started with clawbot
**Date:** 2026-02-01

---

**🧑 You:** i have installed clawbot hot to run it how to start to use

**🤖 Claude:** I'll fix your message first, then answer:

**Your corrected message:**
"I have installed Clawbot. How do I run it? How do I start to use it?"

**Why these matter:**
- Capital letters start sentences and proper names (Clawbot)
- Periods separate complete thoughts
- "how" appears twice - needed punctuation between them

---

**To run Clawbot:**

1. **Open your terminal/command prompt**
2. **Navigate to the Clawbot folder:**
   ```
   cd path/to/clawbot
   ```
3. **Run the start command** (usually):
   ```
   python clawbot.py
   ```
   OR
   ```
   npm start
   ```

**Need more details?** Tell me:
- Which Clawbot version did you install?
- What operating system are you using?

I can then give you the exact commands!

**🧑 You:** cd: no such file or directory: path/to/clawbot

**🤖 Claude:** That error means the folder doesn't exist at that location!

**Why:** I gave you an example path - you need YOUR actual path.

---

**Find where Clawbot is:**

1. **Where did you install it?** Check:
   - Downloads folder?
   - Desktop?
   - Specific project folder?

2. **Once you know, use that path:**
   ```
   cd ~/Downloads/clawbot
   ```
   OR
   ```
   cd ~/Desktop/clawbot
   ```

**Quick tip:** Type `cd ` (with space), then **drag the Clawbot folder** into the terminal - it auto-fills the path!

---

**Still stuck?** Tell me:
- How did you install Clawbot? (downloaded ZIP, git clone, etc.)
- What do you see when you type `ls` in terminal?

**🧑 You:** how to find where is it

**🤖 Claude:** **Quick ways to find Clawbot:**

**Option 1 - Search your computer:**
- **Mac:** Press `Cmd + Space`, type "clawbot"
- **Windows:** Press `Win`, type "clawbot"
- **Linux:** Press `Super`, type "clawbot"

**Option 2 - Check common locations:**
In terminal, try these commands one by one:

```bash
ls ~/Downloads
ls ~/Desktop
ls ~/Documents
```

Look for a folder named "clawbot" or similar.

**Option 3 - Remember how you installed:**
- Did you use `git clone`? It went to your current folder
- Downloaded a ZIP? Probably in Downloads
- Used an installer? Check Applications or Program Files

---

**Once you see it listed:**
If it shows up in `ls ~/Downloads`, then:
```
cd ~/Downloads/clawbot
```

**What did you find?** Tell me which command showed the clawbot folder!

**🤖 Claude:** **Great news! Clawdbot is already installed and running!**

**Why:** You successfully installed it with that `curl` command. It's a global command now - you don't need to find a folder!

---

**To start using Clawdbot:**

```bash
clawdbot gateway
```

This starts the main service.

**OR** if you want the interactive setup first:

```bash
clawdbot onboard
```

This guides you through setup (you canceled it earlier when it asked for OpenAI login).

---

**What happened:**
- ✓ Clawdbot installed globally
- ✓ You can run `clawdbot` from anywhere
- ✗ You canceled the OpenAI authentication (that's why setup didn't finish)

**Next step:** Run `clawdbot onboard` again and complete the OpenAI login when the browser opens!

Want me to explain any specific clawdbot command?

**🧑 You:** what does it mean (node:28651) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
(Use `node --trace-deprecation ...` to show where the warning was created)
Wrote ~/.clawdbot/clawdbot.json
Workspace OK: ~/clawd
Sessions OK: ~/.clawdbot/agents/main/sessions
levrosenblum@Mac ~ %

**🤖 Claude:** **Your corrected question:**
"What does this deprecation warning mean?"

**Why:** Added capital letter and question mark for proper sentence structure.

---

**What it means:**
It's just a **warning, not an error** - Clawdbot is working fine!

**Why it appeared:**
- Node.js is saying an old code library (`punycode`) will be removed in future versions
- Clawdbot uses it internally
- The developers need to update it eventually

**What you see:**
- ✓ `Wrote ~/.clawdbot/clawdbot.json` - Config created successfully
- ✓ `Workspace OK` - Everything is set up correctly
- ✓ `Sessions OK` - Ready to use

---

**Should you worry?** 
**No!** Clawdbot is working. You can safely ignore this warning.

**Your setup is complete!** Now you can:
```bash
clawdbot gateway
```

Ready to continue?

**🧑 You:** 🦞 Clawdbot 2026.1.24-3 (885167d)
   I'll do the boring stuff while you dramatically stare at the logs like it's cinema.

16:04:01 Gateway start blocked: set gateway.mode=local (current: unset) or pass --allow-unconfigured.
levrosenblum@Mac ~ %

**🤖 Claude:** **The error explained:**
Clawdbot needs you to choose a mode before starting.

**Why:** Security - it won't run until you configure how it should work.

---

**Fix it - choose ONE:**

**Option 1 - Set mode permanently:**
```bash
clawdbot config set gateway.mode local
```
Then:
```bash
clawdbot gateway
```

**Option 2 - Run once without saving:**
```bash
clawdbot gateway --allow-unconfigured
```

---

**What's the difference?**
- `local` mode = runs on your computer only
- `--allow-unconfigured` = temporary, one-time run

**Recommended:** Use Option 1 (set it permanently).

Try it now!

**🧑 You:** what do you recomend

**🤖 Claude:** **Your corrected question:**
"What do you recommend?"

**Why:** "Recommend" has two "m"s - common spelling mistake!

---

**I recommend Option 1:**

```bash
clawdbot config set gateway.mode local
```

**Why this is better:**
- You only configure it once
- More secure (saves your choice)
- Won't ask again every time
- Standard way to use Clawdbot

**Then start it:**
```bash
clawdbot gateway
```

This is the proper setup for personal use on your Mac!

**🧑 You:** 16:07:59 [canvas] host mounted at http://127.0.0.1:18789/__clawdbot__/canvas/ (root /Users/levrosenblum/clawd/canvas)
16:07:59 [heartbeat] started
16:07:59 [gateway] agent model: anthropic/claude-opus-4-5
16:07:59 [gateway] listening on ws://127.0.0.1:18789 (PID 28737)
16:07:59 [gateway] listening on ws://[::1]:18789
16:07:59 [gateway] log file: /tmp/clawdbot/clawdbot-2026-02-01.log
16:07:59 [browser/server] Browser control listening on http://127.0.0.1:18791/

**🤖 Claude:** **Perfect! Clawdbot is now running! 🎉**

**What you're seeing:**
- ✓ Gateway is **live** on port 18789
- ✓ Browser control ready on port 18791
- ✓ Using Claude Opus 4.5 model
- ✓ Logs saving to `/tmp/clawdbot/`

---

**What this means:**
Clawdbot is waiting for commands! The terminal will stay open showing activity logs.

**To use it:**
Open a **NEW terminal window** (keep this one running!) and try:

```bash
clawdbot status
```

OR visit the dashboard:
```bash
clawdbot dashboard
```

---

**Keep this terminal open** - it's the main service running. Use another terminal for commands!

Want to know what to do next?

**🧑 You:** yes pleas

**🤖 Claude:** **Your corrected message:**
"Yes, please."

**Why:** "Please" has an "e" at the end!

---

**Next steps to actually use Clawdbot:**

**1. Open a NEW terminal** (keep the gateway running in the old one)

**2. Try these commands:**

**Check status:**
```bash
clawdbot status
```

**Open the web dashboard:**
```bash
clawdbot dashboard
```

**Send a test message to the agent:**
```bash
clawdbot agent --message "Hello, introduce yourself"
```

**See available channels (WhatsApp, Slack, etc.):**
```bash
clawdbot channels
```

---

**What do you want to do?**
- Chat with the AI agent?
- Connect WhatsApp/Slack?
- Browse the dashboard?

Tell me and I'll give you the exact command!

**🧑 You:** Connect WhatsApp/Slack

**🤖 Claude:** **Your corrected message:**
"Connect WhatsApp/Slack."

**Why:** Added period - complete sentence needs punctuation!

---

**To connect messaging apps:**

**For WhatsApp:**
```bash
clawdbot channels login
```
This shows a QR code - scan it with WhatsApp on your phone!

**For Slack:**
```bash
clawdbot channels login --channel slack
```
This opens your browser to authorize Slack.

---

**See all available channels:**
```bash
clawdbot channels
```

**Which one do you want to connect first?**
- WhatsApp (easiest - just scan QR)
- Slack (needs workspace access)
- Something else?

## Related Notes
- [[.-minerd --url=stratum+tcp---earth.vircurpool.com-3333 --use]]
- [[1. ssh root@ваш ip номер]]
- [[10 лучших фильмов десятилетия по версии The Hollywood Report]]
- [[2023-11-24 - _ hello]]
- [[2024-04-06 - Good morning in Hebrew]]
- [[2024-04-06 - Meaning of omit in Hebrew]]
- [[2024-04-11 - Identifying an indoor palm plant]]
- [[2024-05-01 - Hebrew Word Meanings and Grammar]]


## Related Keys & Serials
- [[2026-02-07 - Installing Claude code on Mac]]
- [[2026-03-02 - Managing your Gmail inbox]]
- [[2026-02-26 - Railway mail management agent for Gmail]]
- [[2026-02-13 - Changing font in VS Code]]
- [[2026-03-07 - RAG engine explained]]
- [[2026-03-24 - Installing Telegram plugin clarification]]
- [[Claude_Conversations]]
- [[2026-03-01 - Gemini API disabled status troubleshooting]]


## Same Day
- [[2026-02-01 - Setting up productive conversation preferences]]
- [[2026-02-01 - Memory and conversation continuity]]
- [[2026-02-01 - Writing correction clarification]]
- [[2026-02-01 - Claude_s image generation capabilities]]
- [[2026-02-01 - Setting up Cowork]]

## Same Month
- [[2026-02-07 - Installing Claude code on Mac]]
- [[2026-02-14 - Autocomplete in Google vs Visual Studio Code]]
- [[2026-02-26 - Railway mail management agent for Gmail]]
- [[2026-02-21 - How to run Claude code]]
- [[2026-02-13 - Changing font in VS Code]]
- [[2026-02-12 - גיבוי ושחזור מועדפים בChrome]]
- [[2026-02-01 - Setting up productive conversation preferences]]
- [[2026-02-15 - שינוי תאריך בחיפוש]]

## Same Token
- [[2026-02-05 - Getting access to Claude API]]

## Same Contact
- [[2024-04-06 - Good morning in Hebrew]]
- [[2026-02-01 - Claude_s image generation capabilities]]
- [[2026-02-01 - Memory and conversation continuity]]
- [[2026-02-01 - Setting up Cowork]]
- [[2026-02-01 - Setting up productive conversation preferences]]
- [[2026-02-01 - Writing correction clarification]]
- [[2026-02-02 - P2271 oxygen sensor stuck rich]]
- [[2026-02-02 - Unidentifiable Hebrew phrase]]

## Same Email
- [[$Ley00dr07]]
- [[.-minerd --url=stratum+tcp---earth.vircurpool.com-3333 --use]]
- [[01240906720080]]
- [[016733 מס עסקה דוד שמש]]
- [[03-9642231]]
- [[036133322]]
- [[039767909 גלית עד]]
- [[08.01 ביטוח בריאות קולקטיב]]

## Same Russian
- [[$Ley00dr07]]
- [[.-minerd --url=stratum+tcp---earth.vircurpool.com-3333 --use]]
- [[01240906720080]]
- [[016733 מס עסקה דוד שמש]]
- [[03-9642231]]
- [[036133322]]
- [[039767909 גלית עד]]
- [[08.01 ביטוח בריאות קולקטיב]]

## Related Topics
- [[2026-01-20 - Getting the new version from your coworker]]
- [[2026-02-05 - Getting access to Claude API]]
- [[2026-03-20 - Getting a certificate from Claude AI]]