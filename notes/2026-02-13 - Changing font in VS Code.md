# Changing font in VS Code
**Date:** 2026-02-13

---

**🧑 You:** how to change font in vs code

**🤖 Claude:** # Font Change in VS Code

**Settings approach (easiest):**

1. Open Settings: `Ctrl+,` (Windows/Linux) or `Cmd+,` (Mac)
2. Search: `font family`
3. Paste your font name in the box (e.g., `Fira Code`, `Courier New`, `Monaco`)

**JSON approach:**

Open settings.json (`Ctrl+Shift+P` → "Preferences: Open Settings JSON") and add:

```json
"editor.fontFamily": "Fira Code",
"editor.fontSize": 14
```

**Popular fonts for coding:**
- Fira Code (has ligatures)
- JetBrains Mono
- Cascadia Code
- Courier New (default-like)

Need help installing a custom font first, or changing font size/weight?

**🧑 You:** actioly idlike to change just color of font

**🤖 Claude:** # Font Color in VS Code

**Quick way:**

1. Open Settings: `Ctrl+,`
2. Search: `editor.tokenColorCustomizations`
3. Click "Edit in settings.json"

**Add this:**

```json
"editor.tokenColorCustomizations": {
  "comments": "#90EE90",
  "strings": "#FF6B6B",
  "keywords": "#4A90E2",
  "variables": "#FFD700"
}
```

**Easier way - use a theme:**

1. `Ctrl+Shift+P` → type `color theme`
2. Pick a theme (One Dark Pro, Dracula, Nord, etc.)

This changes ALL colors at once instead of manually tweaking each one.

---

**Spelling fix:** "actioly" → "actually" (mix of letters, happens with dysgraphia—rearrange mentally: act-u-al-ly)

Which approach—custom colors or just pick a new theme?

**🧑 You:** what is better to use terminal in macbook or vs code

**🤖 Claude:** # Terminal vs VS Code Terminal

**VS Code terminal is better for you because:**
- Everything in one window (code + terminal together)
- Faster workflow—no switching between apps
- You can run commands while editing
- Perfect for NOC work (monitoring + commands side-by-side)

**Use native Terminal only if:**
- You need multiple terminal windows open
- Running long processes (let them run while you code elsewhere)
- Working with multiple projects at once

**For your NOC work specifically:**
VS Code terminal wins. You can:
- Monitor logs in terminal
- Edit scripts in editor
- Run UC4 commands without leaving VS Code

---

**Spelling fix:** No errors—good!

Recommendation: Use VS Code terminal as your main one. Open native Terminal only when you need it separate.

**🧑 You:** i just want to change color yellow font black screen

**🤖 Claude:** # Change Font Color to Yellow on Black

**Quick way:**

1. Open Settings: `Cmd+,`
2. Search: `tokenColorCustomizations`
3. Click "Edit in settings.json"

**Paste this:**

```json
"editor.tokenColorCustomizations": {
  "textMateRules": [
    {
      "scope": "source",
      "settings": {
        "foreground": "#FFFF00"
      }
    }
  ]
},
"editor.background": "#000000"
```

This makes ALL text yellow on black background.

**Or simpler - use a theme:**
1. `Cmd+Shift+P` → `color theme`
2. Search "dark" or "black" themes
3. Pick one, then adjust if needed

---

**Spelling fix:** "i" → "I" (always capitalize "I" in English—it's a rule, helps readability)

Done?

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
- [[2026-03-07 - RAG engine explained]]
- [[2026-03-24 - Installing Telegram plugin clarification]]
- [[Claude_Conversations]]
- [[2026-03-01 - Gemini API disabled status troubleshooting]]
- [[2026-02-01 - Getting started with clawbot]]


## Same Day
- [[2026-02-13 - סידור עבודה שבועי ללב]]
- [[2026-02-13 - Fat and S_P 500 correlation]]
- [[2026-02-13 - שימו לב להודעה]]

## Same Month
- [[2026-02-07 - Installing Claude code on Mac]]
- [[2026-02-14 - Autocomplete in Google vs Visual Studio Code]]
- [[2026-02-26 - Railway mail management agent for Gmail]]
- [[2026-02-21 - How to run Claude code]]
- [[2026-02-12 - גיבוי ושחזור מועדפים בChrome]]
- [[2026-02-01 - Setting up productive conversation preferences]]
- [[2026-02-15 - שינוי תאריך בחיפוש]]
- [[2026-02-27 - On-site and MP skills needed]]

## Same Contact
- [[03-9642231]]
- [[2024-04-06 - Good morning in Hebrew]]
- [[2026-02-01 - Claude_s image generation capabilities]]
- [[2026-02-01 - Getting started with clawbot]]
- [[2026-02-01 - Memory and conversation continuity]]
- [[2026-02-01 - Setting up Cowork]]
- [[2026-02-01 - Setting up productive conversation preferences]]
- [[2026-02-01 - Writing correction clarification]]

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
- [[2026-02-07 - Installing Claude code on Mac]]
- [[2026-02-08 - Improving Claude code setup and performance]]
- [[2026-02-09 - Installing Claude Code CLI tool]]
- [[2026-02-14 - Autocomplete in Google vs Visual Studio Code]]
- [[2026-02-14 - Comparing antigravity tools in Google vs VS Code]]
- [[2026-02-18 - Claude code beginner_s guide]]
- [[2026-02-21 - How to run Claude code]]
- [[2026-03-03 - P0138 code_ downstream O2 sensor voltage high]]