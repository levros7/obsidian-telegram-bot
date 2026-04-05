# Remotion development skills roadmap
**Date:** 2026-04-04

---

**🧑 You:** give me plan map hot to use remotion-dev skiils

**🤖 Claude:** ```
This block is not supported on your current device yet.
```

No "remotion-dev" skill exists in the skills library. The available skills are listed above.

**Quick correction:** "hot to" → "how to" (missing 'w' — common dysgraphia slip, easy to miss).

---

Did you mean one of these?

| What you might mean | Skill to use |
|---|---|
| Animated GIFs | `slack-gif-creator` |
| Generative / code-based art | `algorithmic-art` |
| Video-like slides/presentations | `pptx` or `canvas-design` |
| Web UI with animations | `web-artifacts-builder` |

**Remotion** (the React video framework) isn't a built-in skill here — it runs locally on your Mac, not in Claude's sandbox.

Want me to help you use one of the skills above, or walk you through Remotion locally on your M4?

**🧑 You:** it dose exist check netwotk

**🤖 Claude:** **Corrections:** "dose" → "does", "netwotk" → "network" (transposition — letters swapped, classic dysgraphia pattern).

---
```
This block is not supported on your current device yet.
```

No remotion-dev skill found via network search either. It doesn't exist in your connected tool set.

What **does** exist for video/animation-type work:
- `slack-gif-creator` — animated GIFs
- `algorithmic-art` — generative animations (p5.js)
- `canvas-design` — static visuals

**Remotion** is a local npm tool — it runs on your M4, not inside Claude's environment. Want me to give you a quick setup plan for Remotion locally instead?

**🧑 You:** Source: https://github.com/remotion-dev/skills.git

**🤖 Claude:** Got it, let me clone and read it.
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

Got it — it's real and loaded. Here's your plan map:

---
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

The skill has **6 layers** — click any box to go deep on that topic. The learning order:

1. **Compositions** → define your video canvas
2. **Timing** → `spring()`, `interpolate()`, easing curves
3. **Sequencing** → delay/trim/overlap clips
4. **Media** → images, video, audio, fonts
5. **Advanced** → transitions, captions, charts, 3D
6. **Render** → FFmpeg export

Want me to start with any specific box?

**🧑 You:** Explain Remotion compositions and how to define them

**🤖 Claude:** ```
This block is not supported on your current device yet.
```

Here's a clean breakdown from the actual skill file:

---

**Compositions** are defined in `src/Root.tsx`. They're the "video blueprint" — they tell Remotion the size, frame rate, duration, and which React component to render.

**Basic structure:**
```tsx
<Composition
  id="MyVideo"
  component={MyComponent}
  durationInFrames={150}  // 5 seconds at 30fps
  fps={30}
  width={1920}
  height={1080}
/>
```

**4 key concepts:**

| Concept | What it does | When to use |
|---|---|---|
| `defaultProps` | Sets initial prop values | Any dynamic content |
| `<Still>` | Single-frame image, no fps/duration needed | Thumbnails, posters |
| `<Folder>` | Groups compositions in the sidebar | Multi-project repos |
| `calculateMetadata` | Makes duration/size dynamic from API data | Data-driven videos |

**`calculateMetadata` is the power move** — it lets you fetch data before rendering and set duration based on real content (e.g., audio length from ElevenLabs).

**Nesting compositions** uses `<Sequence width={} height={}>` wrapper — not another `<Composition>` tag.

---

Want me to go deeper on any of these, or move to the next topic (timing & animations)?

## Related Notes
- [[.-minerd --url=stratum+tcp---earth.vircurpool.com-3333 --use]]
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
- [[2026-04-04 - סריקת לוח שמירות לשבוע 05-11 באפריל]]
- [[2026-04-04 - Setting up the Anthropic API environment]]
- [[2026-04-04 - Using Obsidian for RAG systems]]

## Same Month
- [[2026-04-01 - Google Drive BI dashboard monitoring]]
- [[2026-04-03 - Новое в iOS 26_5 для iPhone]]
- [[2026-04-01 - Building a BI dashboard for Google Drive]]
- [[2026-04-04 - סריקת לוח שמירות לשבוע 05-11 באפריל]]
- [[2026-04-02 - Invoice translation clarification]]
- [[2026-04-01 - ברכה על מצה בפסח]]
- [[2026-04-04 - Setting up the Anthropic API environment]]
- [[2026-04-02 - Analyzing a JavaScript-rendered website]]

## Same Contact
- [[2024-04-06 - Good morning in Hebrew]]
- [[2024-04-06 - Meaning of omit in Hebrew]]
- [[2024-05-10 - Summarizing Content While Respecting Copyrights]]
- [[2025-05-15 - How to Ask a Man if He_s Gone Out]]
- [[2026-02-02 - P2271 oxygen sensor stuck rich]]
- [[2026-02-04 - שמירת session בדפדפן]]
- [[2026-02-04 - תיקון ותשובת מייל]]
- [[2026-02-07 - תיקון כתיב עברי]]

## Same Phone
- [[$Ley00dr07]]
- [[.-minerd --url=stratum+tcp---earth.vircurpool.com-3333 --use]]
- [[01240906720080]]
- [[016733 מס עסקה דוד שמש]]
- [[03-9642231]]
- [[036133322]]
- [[039767909 גלית עד]]
- [[08.01 ביטוח בריאות קולקטיב]]

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
- [[2026-02-27 - On-site and MP skills needed]]