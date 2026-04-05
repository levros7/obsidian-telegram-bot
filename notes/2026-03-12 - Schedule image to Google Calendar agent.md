# Schedule image to Google Calendar agent
**Date:** 2026-03-12

---

**🧑 You:** Coul you create agent from this project when I just put picture and that’s it

**🤖 Claude:** ```
This block is not supported on your current device yet.
```

Now I'll build the agent — a React artifact that lets you upload a schedule image, sends it to Claude API, extracts your shifts, and adds them to Google Calendar automatically.
```
This block is not supported on your current device yet.
```

Now let me build the agent artifact:
```
This block is not supported on your current device yet.
```

Here's your Schedule Agent! 🎉

The artifact below works like this:

**How to use it:**
1. **Drag & drop** or click to upload a schedule photo
2. Click **"נתח משמרות"** → Claude AI reads the image, finds all your "לב" shifts
3. Click **"שמור בלוח שנה"** → events go straight to Google Calendar

**What it knows:**
- בוקר = 06:30–15:00
- צהריים = 14:30–23:00
- לילה = 22:30–07:00 (next day)
- Handles paired names like "ראם לב", "לב גבריאל" — finds לב in all of them

> ⚠️ **One limitation:** The artifact runs in your browser, and Google Calendar MCP authorization happens at the Claude level. The image analysis via Anthropic API will work, but the calendar-creation step may need to be done by me directly (as I do now). Want me to add a "Send to Claude" button that shows you the shifts and you paste them back to me to create events? Or does this flow work for you?

**🧑 You:** Yes

**🤖 Claude:** Looking at image 5 (the most current week: 15/03/2026–21/03/2026), let me find your shifts first.

Scanning carefully for "לב" only:

- **16/03 (ב)** — בוקר: "ראם **לב**" → **לב** is there ✅
- **17/03 (ג)** — לילה: "**לב** גבריאל" → **לב** is there ✅
- **18/03 (ד)** — צהריים: "**לב** ראם" → **לב** is there ✅
- **19/03 (ה)** — לילה: "**לב** ראם" → **לב** is there ✅

Now creating all 4 events:
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

✅ כל 4 המשמרות נוצרו בלוח השנה!

| תאריך | משמרת | שעות |
|-------|--------|------|
| 16/03 (ב') | בוקר | 06:30–15:00 |
| 17/03 (ג') | לילה | 22:30–07:00 |
| 18/03 (ד') | צהריים | 14:30–23:00 |
| 19/03 (ה') | לילה | 22:30–07:00 |

---

לגבי הסוכן — הבעיה היא שאירטיפקט לא יכול לגשת ישירות ל-Google Calendar שלך (דורש הרשאות שרק לי יש). הפתרון הכי פשוט: **פשוט שלח לי את התמונה כאן** ואני עושה הכל אוטומטית תוך שניות — בדיוק כמו עכשיו. 😊

**🧑 You:** Still you have problem with 15/3 there’s לב too

**🧑 You:** ?

**🤖 Claude:** Sorry! Looking again at 15/03 — בוקר column shows "לב עוז" — that's לב paired with עוז, so לב IS there! ✅

Adding it now:
```
This block is not supported on your current device yet.
```

✅ נוסף! **15/03 (א') — בוקר 06:30–15:00**

עכשיו השבוע המלא:

| תאריך | משמרת | שעות |
|-------|--------|------|
| 15/03 א' | בוקר | 06:30–15:00 ✅ |
| 16/03 ב' | בוקר | 06:30–15:00 ✅ |
| 17/03 ג' | לילה | 22:30–07:00 ✅ |
| 18/03 ד' | צהריים | 14:30–23:00 ✅ |
| 19/03 ה' | לילה | 22:30–07:00 ✅ |

סליחה על הפספוס! אני אזכור — כל תא עם "לב" בתוכו, גם אם מחובר לשם אחר.

**🧑 You:** Now you did it twice please remove one

**🤖 Claude:** I'll delete the duplicate 15/03 בוקר event — the one created second:
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Let me find both 15/03 events first:
```
This block is not supported on your current device yet.
```

Found both. Deleting the duplicate (the first one, "עבודה - בוקר"):
```
This block is not supported on your current device yet.
```

✅ הכפל נמחק! נשאר רק אחד ב-15/03 בוקר 06:30–15:00. השבוע מסודר עכשיו! 🎉

**🧑 You:** Check out all duplication for a next week

**🤖 Claude:** Let me pull all עבודה events for next week (15–21/03):
```
This block is not supported on your current device yet.
```

Found 4 duplicates! Deleting them all now:
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

✅ מנוקה! מחקתי 4 כפולות. השבוע עכשיו נקי:

| תאריך | משמרת | שעות |
|-------|--------|------|
| 15/03 א' | בוקר | 06:30–15:00 |
| 16/03 ב' | בוקר | 06:30–15:00 |
| 17/03 ג' | לילה | 22:30–07:00 |
| 18/03 ד' | צהריים | 14:30–23:00 |
| 19/03 ה' | לילה | 22:30–07:00 |

כל אחד מופיע פעם אחת בדיוק. 🎯

**🧑 You:** מעולה

**🤖 Claude:** תודה! 🎉 הכל מסודר עכשיו. שבוע טוב בעבודה! 💪

## Related Notes
- [[.-minerd --url=stratum+tcp---earth.vircurpool.com-3333 --use]]
- [[1. ssh root@ваш ip номер]]
- [[10 лучших фильмов десятилетия по версии The Hollywood Report]]
- [[2023-11-24 - _ hello]]
- [[2024-04-06 - Good morning in Hebrew]]
- [[2024-04-06 - Meaning of omit in Hebrew]]
- [[2024-04-11 - Identifying an indoor palm plant]]
- [[2024-05-01 - Hebrew Word Meanings and Grammar]]


## Same Day
- [[2026-03-12 - הצגת 10 פקודות אחרונות בלינוקס]]
- [[2026-03-12 - הוספת שידור עבודה לקלנדר]]

## Same Month
- [[2026-03-27 - Current time in Moscow]]
- [[2026-03-13 - כתיבת מייל על עיכוב בהפקת דוחות]]
- [[2026-03-02 - Managing your Gmail inbox]]
- [[2026-03-03 - בדיקת חריגות בנוהל והבקרה]]
- [[2026-03-22 - שער או שאר - הבדל במשמעות]]
- [[2026-03-31 - קישור מייל לתא באקסל]]
- [[2026-03-12 - הצגת 10 פקודות אחרונות בלינוקס]]
- [[2026-03-30 - DWH_SCHEDULE reload אחרי 19_00]]

## Same Contact
- [[03-9642231]]
- [[2024-04-06 - Good morning in Hebrew]]
- [[2024-04-06 - Meaning of omit in Hebrew]]
- [[2024-04-11 - Identifying an indoor palm plant]]
- [[2024-05-01 - Hebrew Word Meanings and Grammar]]
- [[2024-05-10 - Summarizing Content While Respecting Copyrights]]
- [[2025-05-15 - How to Ask a Man if He_s Gone Out]]
- [[2026-02-01 - Claude_s image generation capabilities]]

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
- [[2026-02-07 - Creating a test agent from scratch]]
- [[2026-02-14 - Autocomplete in Google vs Visual Studio Code]]
- [[2026-02-14 - Comparing antigravity tools in Google vs VS Code]]
- [[2026-02-24 - Obsidian data update agent]]
- [[2026-02-26 - Railway mail management agent for Gmail]]
- [[2026-03-30 - DWH_SCHEDULE reload אחרי 19_00]]
- [[2026-04-01 - Building a BI dashboard for Google Drive]]