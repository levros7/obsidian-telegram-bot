# Setting up Claude remote access
**Date:** 2026-03-01

---

**🧑 You:** How to use and setup Claude remote

**🤖 Claude:** ```
This block is not supported on your current device yet.
```

Could you clarify what you mean by "Claude remote"? There are a few possibilities:

- **Claude Code** running remotely (on a server/VPS)
- **Claude API** accessed remotely from your apps
- **Remote MCP servers** connected to Claude
- Something else?

**🧑 You:** Continue to work on iPhone after Claude code worked on Mac

**🤖 Claude:** You want to **continue Claude Code work on iPhone** after starting on Mac — let me check the current docs.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

This is **Claude Code Remote Control** — just released. Here's what you need to know:

**Requirements:**
- Claude **Pro or Max** plan (currently Max only, Pro coming soon)
- Latest Claude Code version (`claude update`)
- Claude app updated on iPhone

**Setup — 2 steps:**

**On your Mac (terminal):**
```bash
claude update          # make sure it's latest
claude remote-control  # or /rc from inside a session
```
It shows a QR code and session URL.

**On iPhone:**
Scan the QR code → opens in the Claude app under the **Code tab** as "Remote Control Session (Mac)".

**Key things to know:**
- Your Mac terminal **must stay open** — the session runs locally, not in the cloud
- 10-minute timeout if you lose network connection
- One session at a time per Claude Code instance
- You can approve/reject actions from iPhone
- To auto-enable for every session: run `/config` → set "Enable Remote Control for all sessions" to true

**Tip:** Wrap it in `tmux` so your session survives if the terminal app closes:
```bash
tmux new -s claude-rc
claude remote-control
# Detach: Ctrl+B, D
# Reconnect: tmux attach -t claude-rc
```

Do you have Pro or Max plan? That's the main gate right now.

## Related Notes
- [[.-minerd --url=stratum+tcp---earth.vircurpool.com-3333 --use]]
- [[10 лучших фильмов десятилетия по версии The Hollywood Report]]
- [[2023-11-24 - _ hello]]
- [[2024-04-06 - Good morning in Hebrew]]
- [[2024-04-06 - Meaning of omit in Hebrew]]
- [[2024-04-11 - Identifying an indoor palm plant]]
- [[2024-05-01 - Hebrew Word Meanings and Grammar]]
- [[2024-05-10 - Summarizing Content While Respecting Copyrights]]


## Same Day
- [[2026-03-01 - Gemini API disabled status troubleshooting]]

## Same Month
- [[2026-03-27 - Current time in Moscow]]
- [[2026-03-13 - כתיבת מייל על עיכוב בהפקת דוחות]]
- [[2026-03-02 - Managing your Gmail inbox]]
- [[2026-03-03 - בדיקת חריגות בנוהל והבקרה]]
- [[2026-03-22 - שער או שאר - הבדל במשמעות]]
- [[2026-03-31 - קישור מייל לתא באקסל]]
- [[2026-03-12 - Schedule image to Google Calendar agent]]
- [[2026-03-12 - הצגת 10 פקודות אחרונות בלינוקס]]

## Same Contact
- [[2024-04-06 - Good morning in Hebrew]]
- [[2024-04-06 - Meaning of omit in Hebrew]]
- [[2024-04-11 - Identifying an indoor palm plant]]
- [[2024-05-01 - Hebrew Word Meanings and Grammar]]
- [[2024-05-10 - Summarizing Content While Respecting Copyrights]]
- [[2025-05-15 - How to Ask a Man if He_s Gone Out]]
- [[2026-02-02 - P2271 oxygen sensor stuck rich]]
- [[2026-02-02 - תנאים לתוצאות טובות ולא טובות]]

## Same Phone
- [[$Ley00dr07]]
- [[.-minerd --url=stratum+tcp---earth.vircurpool.com-3333 --use]]
- [[01240906720080]]
- [[016733 מס עסקה דוד שמש]]
- [[03-9642231]]
- [[036133322]]
- [[039426648 נטנל  ביטוח לעומי]]
- [[039767909 גלית עד]]

## Same Russian
- [[.-minerd --url=stratum+tcp---earth.vircurpool.com-3333 --use]]
- [[01240906720080]]
- [[03-9642231]]
- [[036133322]]
- [[039767909 גלית עד]]
- [[10 лучших фильмов десятилетия по версии The Hollywood Report]]
- [[2026-01-20 - Getting the new version from your coworker]]
- [[2026-02-01 - Getting started with clawbot]]

## Related Topics
- [[2026-02-01 - Claude_s image generation capabilities]]
- [[2026-02-01 - Setting up Cowork]]
- [[2026-02-01 - Setting up productive conversation preferences]]
- [[2026-02-05 - Getting access to Claude API]]
- [[2026-02-07 - Installing Claude code on Mac]]
- [[2026-02-08 - Claude API pricing and costs]]
- [[2026-02-08 - Improving Claude code setup and performance]]
- [[2026-02-09 - Checking Claude usage limits]]