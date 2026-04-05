# Current available plugins
**Date:** 2026-03-17

---

**🧑 You:** what plugins do you have reaght now

**🤖 Claude:** **Correction:** "reaght" → "right" — *gh* is silent in "right"; common dysgraphia swap.

---

Here's what I have access to right now:

**Built-in tools:**
- 🔍 Web search + web fetch
- 🖼️ Image search
- 🗺️ Places/maps
- 🌤️ Weather
- 🏈 Sports data
- 📅 Google Calendar (connected)
- 📧 Gmail (connected)
- 🗂️ Google Drive search
- 💾 Memory (read/write)
- 📁 File create/view/edit (bash, str_replace)
- 🎨 Visualizer (SVG/HTML widgets)
- 🔎 Past chat search

**Skills (file-based guides I can load):**
- docx, pdf, pptx, xlsx
- Frontend design, canvas design
- MCP builder, web artifacts builder
- Internal comms, doc co-authoring
- And a few more

Anything specific you want to use?

**🧑 You:** do you have plugin cli

**🤖 Claude:** **Correction:** "plugin" → no fix needed here, but context: you likely mean a **terminal/CLI tool** — just clarifying.

---

Yes — I have **bash_tool**, which is a full Linux terminal (Ubuntu 24).

I can run commands like:
```bash
python3, pip, node, npm, git, curl, etc.
```

**Limitations:**
- Network access is restricted to specific domains (GitHub, PyPI, npm, etc.)
- No access to your local Mac terminal — it's a sandboxed container
- Files reset between sessions

Want me to run something specific?

**🧑 You:** give list recomended plugins for claude code and for claude cowork

**🤖 Claude:** Let me check the actual current docs — I don't want to guess.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Here's what I found from official sources. No guessing.

---

**🖥️ Claude Code — Top recommended plugins**

From Anthropic's official plugin page at claude.com/plugins:

| Plugin | What it does |
|---|---|
| **GitHub MCP** | Manage repos, PRs, issues from Code |
| **Context7** | Pulls live, version-specific library docs into session |
| **Playwright MCP** | Browser automation & UI testing (by Microsoft) |
| **Firecrawl** | Converts websites to clean LLM-ready markdown |
| **Supabase MCP** | DB ops, auth, storage management |
| **/feature-dev** | 7-phase feature build workflow (most popular) |
| **/code-review** | Free, official code review plugin |
| **Simplify** | Cleans up code after changes |
| **Semantic LSP** | Code intelligence via language server |

---

**💼 Claude Cowork — Official Anthropic plugins**

Anthropic open-sourced 11 knowledge-work plugins on GitHub (`anthropics/knowledge-work-plugins`), installable directly from Cowork:

| Plugin | Who it's for |
|---|---|
| **Sales** | Call prep, pipeline, outreach |
| **Data analyst** | SQL queries, write-query commands |
| **Legal** | Research, drafting |
| **Finance** | DCF models, comparables |
| **Marketing** | Campaigns, copy |
| **HR / Recruiting** | Screening, onboarding |
| + 5 more roles | All customizable |

In February 2026, Anthropic also added 12 new MCP connectors to Cowork: Google Calendar, Google Drive, Gmail, DocuSign, Apollo, Clay, Outreach, Similarweb, MSCI, LegalZoom, FactSet, and WordPress.

---

**For your NOC work specifically** — GitHub MCP + Filesystem MCP + Memory plugin would be most useful in Claude Code. Want me to help set any of these up?

**🧑 You:** install for me please Supabase MCP

**🤖 Claude:** I can't install it directly on your Mac — my bash terminal is a sandboxed container, not your local machine.

You need to run this yourself in your Mac terminal:

```bash
claude mcp add --transport http supabase https://mcp.supabase.com/sse
```

Or if you prefer the npm version:
```bash
claude mcp add supabase -- npx -y @supabase/mcp-server-supabase@latest --access-token YOUR_TOKEN
```

Get your token at: **supabase.com → Account → Access Tokens**

Want step-by-step instructions?

**🧑 You:** yes

**🤖 Claude:** **Step-by-step: Supabase MCP for Claude Code**

---

**Step 1 — Get your Supabase token**
1. Go to [supabase.com](https://supabase.com) → log in
2. Click your avatar (top right) → **Account**
3. Go to **Access Tokens** → **Generate new token**
4. Name it "Claude Code" → copy the token

---

**Step 2 — Add to Claude Code**

Open Terminal on your Mac and run:

```bash
claude mcp add supabase -- npx -y @supabase/mcp-server-supabase@latest --access-token YOUR_TOKEN_HERE
```

Replace `YOUR_TOKEN_HERE` with the token you copied.

---

**Step 3 — Verify it worked**

```bash
claude mcp list
```

You should see `supabase` in the list.

---

**Step 4 — Restart Claude Code**

Close and reopen Claude Code — MCP servers only load on restart.

---

After that, you can say things like:
> "Show me all tables in my Supabase project"
> "Run this SQL query on my database"

Do you have a Supabase account already, or need help creating one?

**🧑 You:** what do you think most plugin do i need\

**🤖 Claude:** **Correction:** "what do you think most plugin do i need" → "What plugins do you think I need most?" — *word order* and *subject-verb agreement* matter for clarity.

---

Based on your NOC work + automation setup, here's my honest take:

**🔴 High priority (fits your work directly)**

| Plugin | Why you need it |
|---|---|
| **GitHub MCP** | You already use `levros7` repos — manage PRs, commits from Claude Code |
| **Memory MCP** | Persistent context across sessions — huge for ADHD workflow |
| **Filesystem MCP** | Read/write local files — useful for your Obsidian iCloud sync scripts |

**🟡 Medium priority (your automation projects)**

| Plugin | Why |
|---|---|
| **Context7** | When building Python/Flask/N8N — gets live docs instead of outdated training data |
| **/feature-dev** | Structured workflow when building your NOC monitoring tools |

**🟢 Lower priority for now**

| Plugin | Why to skip for now |
|---|---|
| Supabase MCP | Only useful if you start using Supabase DB — you don't yet |
| Playwright | Browser testing — not relevant to NOC work |
| Firecrawl | Web scraping — not your use case |

---

**My actual recommendation:** Start with just **GitHub MCP + Filesystem MCP**. Those two directly support what you're already building.

Want to install GitHub MCP next?

**🧑 You:** lets start from this : Memory MCP

**🤖 Claude:** Good choice — most useful for ADHD workflow.

---

**Step 1 — Install the Memory MCP**

In your Mac Terminal:

```bash
claude mcp add memory -- npx -y @modelcontextprotocol/server-memory
```

---

**Step 2 — Verify**

```bash
claude mcp list
```

Should show `memory` in the list.

---

**Step 3 — Restart Claude Code**

Close and reopen completely.

---

**Step 4 — Test it**

In Claude Code, say:
> "Remember that I work in a NOC and use UC4 and Actimize"

Then next session:
> "What do you know about my work?"

It should remember. ✅

---

That's it — no token needed for this one, it's fully local.

Ready to do **GitHub MCP** next?

**🧑 You:** how to get in claude code

**🤖 Claude:** **Correction:** "how to get in claude code" → "How do I get into Claude Code?" — missing subject and preposition.

---

Two ways depending on what you have:

---

**Option 1 — Terminal (you already have this)**
```bash
claude
```
Just type `claude` in your Mac Terminal. If installed, it opens.

---

**Option 2 — VS Code**
Install the **Claude Code extension** from the VS Code marketplace → it adds a sidebar panel.

---

**Not installed yet?**
```bash
npm install -g @anthropic-ai/claude-code
```
Then run `claude` to start.

---

**Check if it's already installed:**
```bash
claude --version
```

Do you have it installed already, or starting fresh?

**🧑 You:** ❯ remember i have adhd                                                                                                                      
  ⎿  API Error: 401 {"type":"error","error":{"type":"authentication_error","message":"OAuth token has expired. Please obtain a new token or 
     refresh your existing token."},"request_id":"req_011CZ8uKPpaQEzj1sx4MwyDQ"} · Please run /login

**🤖 Claude:** Got it — your Claude Code session token expired. Easy fix:

---

**Run this in Terminal:**
```bash
claude
```

Then inside Claude Code:
```
/login
```

It will open a browser to re-authenticate. After that you're back in.

---

After login, try the memory command again. Want me to remind you what to test first?

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
- [[2026-03-17 - קבלת סרטיפיקט Claude 101]]
- [[2026-03-17 - Document review request]]

## Same Month
- [[2026-03-27 - Current time in Moscow]]
- [[2026-03-13 - כתיבת מייל על עיכוב בהפקת דוחות]]
- [[2026-03-02 - Managing your Gmail inbox]]
- [[2026-03-03 - בדיקת חריגות בנוהל והבקרה]]
- [[2026-03-22 - שער או שאר - הבדל במשמעות]]
- [[2026-03-31 - קישור מייל לתא באקסל]]
- [[2026-03-12 - Schedule image to Google Calendar agent]]
- [[2026-03-12 - הצגת 10 פקודות אחרונות בלינוקס]]

## Same Token
- [[2026-02-08 - Telegram connection request]]
- [[2026-02-08 - Using skill beeper-mcp]]

## Same Contact
- [[2024-04-06 - Good morning in Hebrew]]
- [[2024-04-06 - Meaning of omit in Hebrew]]
- [[2024-04-11 - Identifying an indoor palm plant]]
- [[2024-05-01 - Hebrew Word Meanings and Grammar]]
- [[2024-05-10 - Summarizing Content While Respecting Copyrights]]
- [[2025-05-15 - How to Ask a Man if He_s Gone Out]]
- [[2026-02-02 - P2271 oxygen sensor stuck rich]]
- [[2026-02-02 - תנאים לתוצאות טובות ולא טובות]]

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
- [[2026-03-27 - Current time in Moscow]]