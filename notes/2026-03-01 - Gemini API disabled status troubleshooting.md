# Gemini API disabled status troubleshooting
**Date:** 2026-03-01

---

**🧑 You:** I got it from bot telegram but all my preferences is good what it could be Gemini confused about

**🤖 Claude:** Your bot shows **Status: Disabled** for the Gemini API — this means the API key or billing is disabled on Google's side, not a connection issue (connection is healthy ✅).

**Most likely causes:**

1. **Free tier quota exhausted** — Gemini free API has daily/monthly limits
2. **Billing not enabled** on the Google Cloud project `gen-lang-client-0101592875`
3. **API not enabled** in that specific project

**Quick fix:** Go to [aistudio.google.com](https://aistudio.google.com) → check your API key status, or go to Google Cloud Console and enable billing for that project.

**🧑 You:** It was billing now its connected to billing but still disabled

**🤖 Claude:** Try these in order:

1. **Enable the Gemini API** in Google Cloud Console → APIs & Services → search "Gemini API" → click Enable
2. **Wait 5-10 minutes** after enabling billing — it doesn't activate instantly
3. **Regenerate your API key** — old keys sometimes don't pick up billing changes

The project `gen-lang-client` looks like it was auto-created by AI Studio, so go to [aistudio.google.com](https://aistudio.google.com) → Get API Key → make sure the key is linked to the now-billed project.

**🧑 You:** It was already enabled

**🤖 Claude:** Then try **regenerating the API key**:

1. Go to [aistudio.google.com](https://aistudio.google.com) → **Get API Key**
2. Create a **new key** linked to that same project
3. Update the key in your bot's config

Sometimes the key itself gets flagged/disabled even if the project is fine.

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
- [[2026-02-01 - Getting started with clawbot]]


## Same Day
- [[2026-03-01 - Setting up Claude remote access]]

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
- [[2026-02-05 - Getting access to Claude API]]
- [[2026-02-08 - Claude API pricing and costs]]
- [[2026-03-18 - Building with Anthropic_s Claude API]]
- [[2026-03-27 - Claude Haiku 4_5 API availability]]
- [[2026-03-27 - Claude network issue troubleshooting]]
- [[2026-04-04 - Setting up the Anthropic API environment]]