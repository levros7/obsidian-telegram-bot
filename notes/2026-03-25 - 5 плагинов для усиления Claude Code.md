# 5 плагинов для усиления Claude Code
**Date:** 2026-03-25

---

**🧑 You:** what do you think : 19:01 — ⚡️Инструкция 5 плагинов которые делают Claude Code в 10 раз сильнее Для установки нужен Claude Code CLI. Все команды выполняются в терминале. 1️⃣ Context7 — актуальная документация Подтягивает свежую документацию любой библиотеки прямо в контекст. Больше никаких устаревших ответов. npx ctx7 setup --claude Откроется браузер для авторизации. После этого всё работает автоматически. Исходники: github.com/upstash/context7 2️⃣ Claude-Mem — долгосрочная память Записывает контекст сессий и восстанавливает его в будущих разговорах. SQLite + векторный поиск. claude plugin marketplace add thedotmack/claude-mem claude plugin install claude-mem Исходники: github.com/thedotmack/claude-mem 3️⃣ Superpowers — методология разработки TDD, системный дебаг, планирование, параллельные агенты, code review. Claude работает как senior-разработчик. claude plugin install superpowers Исходники: github.com/obra/superpowers 4️⃣ Security Guidance — автоматическая проверка безопасности Хук от Anthropic. Проверяет каждый edit на уязвимости: XSS, command injection, eval, innerHTML. Блокирует опасный код. claude plugin install security-guidance Источник: официальный маркетплейс Anthropic (github.com/anthropics/claude-plugins-official) 5️⃣ Dev-Browser — браузер для Claude Claude может открыть страницу, проверить UI, кликать на элементы. Реальная проверка вместо слепого написания кода. claude plugin marketplace add sawyerhood/dev-browser claude plugin install dev-browser Исходники: github.com/SawyerHood/dev-browser 🧠 После установки перезапустите Claude Code чтобы плагины активировались. Весь официальный каталог плагинов: github.com/anthropics/claude-plugins-official

**🤖 Claude:** ```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

No spelling/grammar correction needed — your message was just a paste of someone else's text in Russian, no errors from you.

---

**My take: mostly legit, but with caveats.**

**What's real:**

- The `claude-plugins-official` repo is real — it's Anthropic's curated directory of high-quality Claude Code plugins.
- The `security-guidance` hook concept is real — it checks file edits for vulnerabilities like XSS, command injection, etc.
- The official marketplace is built into Claude Code — you access it via `/plugin` → Discover tab, not necessarily `claude plugin marketplace add`.

**What's suspicious:**

- **Context7** — real project (Upstash), but the install command `npx ctx7 setup --claude` looks off. It's normally an MCP server, not installed that way.
- **claude-mem, Superpowers, dev-browser** — these are community/third-party plugins. Anthropic warns: they don't control what MCP servers or software are included in third-party plugins and can't verify they'll work as intended.
- The install syntax `claude plugin marketplace add user/repo` + `claude plugin install name` is the correct pattern, so that part checks out.

**Bottom line:**

The post is mostly accurate but written in a hyped Telegram style. The 4 non-official plugins are community tools — they may work great or may break. Don't install blindly. The only one I'd trust immediately is `security-guidance` from Anthropic's official marketplace.

Want me to check if any of these are actually in the official catalog?

**🧑 You:** yes

**🤖 Claude:** ```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Here's the verdict for each plugin:

| Plugin | In Official Catalog? | Notes |
|---|---|---|
| **Context7** | ✅ Yes | Listed in `external_plugins/context7` in the official repo |
| **security-guidance** | ✅ Yes | Listed in `plugins/security-guidance` — Anthropic-built |
| **Superpowers** | ✅ Yes | In the marketplace catalog — but install via `/plugin install`, not the CLI command in the post |
| **claude-mem** | ❌ No | Not found in the official catalog — community only |
| **dev-browser** | ❌ No | Not found in the official catalog — community only |

**Summary:** 3 out of 5 are in the official Anthropic marketplace. Install those 3 safely. For `claude-mem` and `dev-browser` — they're third-party, trust at your own risk.

**Correct install for the safe ones:**
```
/plugin install context7@claude-plugins-official
/plugin install security-guidance@claude-plugins-official
/plugin install superpowers@claude-plugins-official
```

**🧑 You:** how to install this plugins

**🤖 Claude:** No grammar corrections needed.
```
This block is not supported on your current device yet.
```

Simple. Everything is done inside Claude Code using the `/plugin` command.

**Step 1 — Open Claude Code in your terminal:**
```bash
claude
```

**Step 2 — Install the 3 safe plugins** (type these inside Claude Code):
```
/plugin install context7@claude-plugins-official
/plugin install security-guidance@claude-plugins-official
/plugin install superpowers@claude-plugins-official
```

**Step 3 — Reload:**
```
/reload-plugins
```

That's it. The official marketplace `claude-plugins-official` is already built in — no need to add it manually.

---

**To browse what else is available:**
```
/plugin
```
Then go to the **Discover** tab.

**🧑 You:** is it mean i do9 not have any skillls : /reload-plugins                                                                                                                       
  ⎿  Reloaded: 3 plugins · 0 skills · 5 agents · 0 hooks · 2 plugin MCP servers · 1 plugin LSP server

**🤖 Claude:** No spelling correction needed ("do9" is just a typo, not a language error).

**No — it's good news.** Skills are loaded differently than plugins.

- **3 plugins** ✅ — your plugins are installed
- **0 skills** — means none of the installed plugins include skills (that's normal — Context7, security-guidance, and superpowers use **agents** and **MCP servers**, not skills)
- **5 agents** ✅ — those come from Superpowers
- **2 plugin MCP servers** ✅ — Context7 + one other is running

Skills are a separate thing — they're instruction files (SKILL.md) that teach Claude *when* to do something automatically. Most power-user plugins don't use them.

**Your setup looks correct.** Try typing `/superpowers` or `/context7` in Claude Code to confirm they work.

## Related Notes
- [[1. ssh root@ваш ip номер]]
- [[10 лучших фильмов десятилетия по версии The Hollywood Report]]
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
- [[2026-03-25 - Extract commands from screenshot]]
- [[2026-03-25 - Understanding retrieval-augmented generation]]

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
- [[2026-02-07 - Installing Claude code on Mac]]
- [[2026-03-24 - Installing Telegram plugin clarification]]
- [[Claude_Conversations]]

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
- [[2026-02-01 - Claude_s image generation capabilities]]
- [[2026-02-05 - Getting access to Claude API]]
- [[2026-02-07 - Installing Claude code on Mac]]
- [[2026-02-08 - Claude API pricing and costs]]
- [[2026-02-08 - Improving Claude code setup and performance]]
- [[2026-02-09 - Checking Claude usage limits]]
- [[2026-02-09 - Installing Claude Code CLI tool]]
- [[2026-02-13 - Changing font in VS Code]]