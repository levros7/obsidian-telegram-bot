# On-site and MP skills needed
**Date:** 2026-02-27

---

**🧑 You:** Look for on site skills mp skills that I could have been needed

**🤖 Claude:** ```
This block is not supported on your current device yet.
```

**Grammar fix:** "Look for on-site skills/MP skills that I could have needed" — "could have been needed" is a passive construction that sounds awkward; likely meant "could need" or "might be useful for me."

---

Here's what's available and relevant to your work:

**Public skills (most useful for you):**
- **docx** — Word document creation (NOC reports, shift summaries)
- **xlsx** — Excel/spreadsheet work (monitoring dashboards, schedules)
- **pptx** — PowerPoint presentations
- **pdf** — PDF creation/extraction
- **frontend-design** — Web UI/artifacts

**Example skills (more advanced):**
- **mcp-builder** — Build MCP servers (relevant to your Claude integrations!)
- **skill-creator** — Create custom skills
- **internal-comms** — Internal communication templates
- **doc-coauthoring** — Collaborative document writing

**Most relevant for your NOC/automation work:** `mcp-builder`, `xlsx`, `docx`

Want me to read any specific skill's details?

**🧑 You:** What do you think which agents do I need to

**🤖 Claude:** Good question! Let me ask a few things to give you a useful answer.
```
This block is not supported on your current device yet.
```

Let me know your answers and I'll suggest the right agent setup for you!

**🧑 You:** Q: What's the main goal you want agents to help with?
A: Obsidian note automation and Telegram bot workflows

Q: Where should agents run?
A: Claude Code, Railway (cloud), and Local Mac

**🤖 Claude:** Based on your setup, here's what I'd suggest:

**2-3 agents you actually need:**

**1. Telegram Intake Agent** (Railway — already partly built)
Receives messages, classifies them (NOC incident / Claude summary / personal note), and routes to the right place.

**2. Obsidian Writer Agent** (Local Mac / Claude Code)
Watches for new data (from Telegram or GitHub), formats it into proper Obsidian markdown with your NOC templates, and saves to iCloud vault.

**3. Orchestrator / Router Agent** (Claude Code)
The "brain" — decides what to do with each input. Calls the other two agents. This is what ties everything together.

---

**Why this structure?**
- Railway handles always-on receiving (Telegram)
- Local Mac handles file writing (Obsidian needs local iCloud access)
- Claude Code is best for the logic/orchestration layer

---

Want me to sketch out how these agents would talk to each other, or start building one of them?

**🧑 You:** sketch out how these agents would talk to each other

**🤖 Claude:** Here's the flow:

```
[You / Telegram]
       │
       ▼
┌─────────────────────┐
│  Telegram Intake    │  ← Railway (always on)
│  Agent              │
│  - Receives message │
│  - Tags type:       │
│    NOC / Summary /  │
│    Personal         │
└────────┬────────────┘
         │ HTTP POST (JSON payload)
         ▼
┌─────────────────────┐
│  Orchestrator Agent │  ← Claude Code (Mac)
│  - Reads tag        │
│  - Decides action   │
│  - Calls next agent │
└────┬────────────────┘
     │
     ├──── If NOC incident ──────────────────┐
     │                                       ▼
     │                            ┌─────────────────────┐
     │                            │  Obsidian Writer    │
     ├──── If Claude summary ───► │  Agent (Local Mac)  │
     │                            │  - Formats markdown │
     └──── If personal note ───►  │  - Saves to iCloud  │
                                  │    vault folder     │
                                  └─────────────────────┘
```

**How they talk:**

- **Telegram → Orchestrator:** Railway sends a webhook POST with `{type, content, timestamp}`
- **Orchestrator → Obsidian Writer:** Local function call or Unix socket (since both are on Mac)
- **Obsidian Writer → iCloud:** Direct file write to the vault path

---

**The JSON payload example:**
```json
{
  "type": "noc_incident",
  "content": "UC4 job failed - JOB_NAME",
  "timestamp": "2026-02-27T10:30:00",
  "source": "telegram"
}
```

---

Want me to start coding the Orchestrator agent first? That's the core piece.

## Related Notes
- [[1. ssh root@ваш ip номер]]
- [[10 лучших фильмов десятилетия по версии The Hollywood Report]]
- [[2023-11-24 - _ hello]]
- [[2024-04-06 - Good morning in Hebrew]]
- [[2024-04-06 - Meaning of omit in Hebrew]]
- [[2024-04-11 - Identifying an indoor palm plant]]
- [[2024-05-01 - Hebrew Word Meanings and Grammar]]
- [[2024-05-10 - Summarizing Content While Respecting Copyrights]]


## Same Day
- [[2026-02-27 - Claude Pro discount options]]
- [[2026-02-27]]
- [[2026-02-27 - Git repository not found error]]

## Same Month
- [[2026-02-07 - Installing Claude code on Mac]]
- [[2026-02-14 - Autocomplete in Google vs Visual Studio Code]]
- [[2026-02-26 - Railway mail management agent for Gmail]]
- [[2026-02-21 - How to run Claude code]]
- [[2026-02-13 - Changing font in VS Code]]
- [[2026-02-12 - גיבוי ושחזור מועדפים בChrome]]
- [[2026-02-01 - Setting up productive conversation preferences]]
- [[2026-02-15 - שינוי תאריך בחיפוש]]

## Same Contact
- [[2024-04-06 - Good morning in Hebrew]]
- [[2026-02-01 - Claude_s image generation capabilities]]
- [[2026-02-01 - Getting started with clawbot]]
- [[2026-02-01 - Memory and conversation continuity]]
- [[2026-02-01 - Setting up Cowork]]
- [[2026-02-01 - Setting up productive conversation preferences]]
- [[2026-02-01 - Writing correction clarification]]
- [[2026-02-02 - P2271 oxygen sensor stuck rich]]

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
- [[2026-04-04 - Remotion development skills roadmap]]