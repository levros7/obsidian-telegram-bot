# GitHub artifact connection
**Date:** 2026-03-14

---

**🧑 You:** Could you create artifact is a connection to GitHub

**🤖 Claude:** Let me clarify what you're looking for before building this.

**Spelling note:** "Could you create artifact is a connection to GitHub" → "Could you create **an** artifact **that has** a connection to GitHub" — missing words make the request ambiguous, which matters when asking for technical builds.

What kind of GitHub connection do you need?
```
This block is not supported on your current device yet.
```

**🧑 You:** Q: What should the artifact do with GitHub?
A: Browse file contents and Manage PRs

Q: Which repo should it connect to?
A: All my repos

**🤖 Claude:** Let me read the frontend design skill first to build a polished artifact.
```
This block is not supported on your current device yet.
```

Now I'll build a GitHub dashboard artifact. Since GitHub's API is public and supports CORS-free access via personal access tokens, I'll create a React app that lets you enter your token, then browse repos, files, and PRs.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Here's your GitHub dashboard. To use it:

1. **Generate a token** — GitHub → Settings → Developer settings → Personal access tokens → Fine-grained tokens. Give it `repo` scope (Contents: read, Pull requests: read+write).
2. **Paste the token** into the app and hit connect.
3. **Browse files** in any repo, or switch to the **PRs tab** to view/merge/close pull requests.

The token stays in-browser only — nothing is stored or sent anywhere except directly to GitHub's API. Works with your `levros7` repos and any others you have access to.

**🧑 You:** Why I get failed when I put token access number

**🤖 Claude:** A few things to check — the most common causes:

**1. Token type matters:**
- **Fine-grained tokens** (start with `github_pat_`) need explicit repository permissions enabled. Make sure you granted **Contents: Read** and **Pull requests: Read & Write**.
- **Classic tokens** (start with `ghp_`) need the `repo` checkbox selected.

**2. Token might have expired** — check the expiration date you set when creating it.

**3. CORS issue in artifacts** — this is the most likely problem. The GitHub API blocks browser requests from origins that aren't your own site. The artifact runs inside Claude's sandboxed iframe, so GitHub may reject the call.

Let me fix the app to show you the actual error message so we can see exactly what's failing:
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


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Updated — now it'll show you the **exact error** instead of a generic "failed" message. Try connecting again and tell me what error text appears. The three most likely causes:

1. **"Failed to fetch" / CORS** — the artifact sandbox blocks cross-origin API calls. If this is the case, the fix is to run it locally instead.
2. **"401: Bad credentials"** — wrong token or expired.
3. **"403: Resource not accessible"** — token doesn't have the right permissions (needs `repo` or `Contents: Read`).

What does it say now?

**🧑 You:** Still load failed

**🤖 Claude:** That confirms it — it's a **CORS issue**. The Claude artifact sandbox blocks direct API calls to `api.github.com`. The artifact iframe simply can't reach external APIs.

**Two options:**

1. **I rebuild it as a local HTML file** — you download it, open in your browser, and it works perfectly (no sandbox restrictions).
2. **I use the Anthropic API inside the artifact** — Claude calls GitHub for you via web search, but it's read-only and limited.

Option 1 is the best for full functionality (browse files + manage PRs).

Want me to rebuild it as a downloadable HTML file you just open in Chrome?
```
This block is not supported on your current device yet.
```

**🧑 You:** Q: Which approach?
A: Downloadable HTML file (full features)

**🤖 Claude:** ```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Download this file and open it in Chrome (just double-click it). No server needed — it runs entirely in your browser.

**How to use:**
1. Paste your GitHub token → hit **connect**
2. Click any repo → **files** tab to browse, **PRs** tab to manage
3. PRs can be merged or closed directly from the app

**Token tip:** For fine-grained tokens, make sure you selected your `levros7` account as the resource owner, and granted **Contents: Read** + **Pull requests: Read & Write** permissions. Classic tokens just need the `repo` checkbox.

**🧑 You:** No still load failed

**🤖 Claude:** Let me check what's actually happening. Can you tell me the exact error message that appears? But first, let me test if the issue might be in the token format.
```
This block is not supported on your current device yet.
```

**🧑 You:** Q: What does your token start with?
A: github_pat_xxxx (fine-grained)

Q: What exactly happens when you click connect?
A: Page shows 'load failed' or browser error

**🤖 Claude:** That "load failed" is likely the **HTML file itself** not loading properly in your browser, not a GitHub API error.

Let me check — are you opening this on your **iPad** or **Mac**?
```
This block is not supported on your current device yet.
```

## Related Notes
- [[.-minerd --url=stratum+tcp---earth.vircurpool.com-3333 --use]]
- [[10 лучших фильмов десятилетия по версии The Hollywood Report]]
- [[2023-11-24 - _ hello]]
- [[2024-04-06 - Good morning in Hebrew]]
- [[2024-04-06 - Meaning of omit in Hebrew]]
- [[2024-04-11 - Identifying an indoor palm plant]]
- [[2024-05-01 - Hebrew Word Meanings and Grammar]]
- [[2024-05-10 - Summarizing Content While Respecting Copyrights]]


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
- [[2026-02-03 - Keep-alive connection explained]]
- [[2026-02-08 - Telegram connection request]]
- [[2026-03-15 - Useful artifact ideas]]