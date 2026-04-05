# OAuth token expiration and login requirement
**Date:** 2026-02-21

---

**🧑 You:** API Error: 401 {"type":"error","error":{"type":"authentication_error","message":"OAuth token has expired. Please obtain a new token or refresh your existing token."},"request_id":"req_011CYLpHXZbemrTU84PoqGii"} · Please run /login

**🤖 Claude:** Your OAuth token expired. Run `/login` to get a new one.

**🧑 You:** and what i have to do after

**🤖 Claude:** After `/login`:

1. It will open a browser auth page
2. You log in / approve access
3. A new token is saved automatically
4. Re-run your original command

That's it — no manual token copying needed.

**🧑 You:** i need to do it evre time

**🤖 Claude:** No, tokens usually last a long time. If yours expires every session, it means it's **not being saved** between sessions.

Quick fix: check if there's a config file storing the token (like `~/.config/...` or `.env`). If it resets every time, the token isn't persisting — likely a file permission or missing config issue.

Which tool is this for? (Claude Code, n8n, something else?)

**🧑 You:** Claude Code

**🤖 Claude:** Claude Code tokens expire after **~hours of inactivity** by default — this is known behavior.

Fix: run `/login` once, then keep a Claude Code session alive (or just re-login when needed — it's fast).

There's no "stay logged in forever" option currently in Claude Code. It uses OAuth which has expiry by design.

If it bothers you, check if `~/.claude` has a stored token — sometimes deleting and re-logging fixes repeated expiry issues.

## Related Notes
- [[.-minerd --url=stratum+tcp---earth.vircurpool.com-3333 --use]]
- [[1. ssh root@ваш ip номер]]
- [[2023-11-24 - _ hello]]
- [[2024-04-06 - Good morning in Hebrew]]
- [[2024-04-06 - Meaning of omit in Hebrew]]
- [[2024-04-11 - Identifying an indoor palm plant]]
- [[2024-05-01 - Hebrew Word Meanings and Grammar]]
- [[2024-05-10 - Summarizing Content While Respecting Copyrights]]


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
- [[2026-02-21 - How to run Claude code]]

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