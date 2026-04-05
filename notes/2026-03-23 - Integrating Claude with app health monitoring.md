# Integrating Claude with app health monitoring
**Date:** 2026-03-23

---

**🧑 You:** Connect Claude to app health

**🤖 Claude:** Lev, I want to make sure I understand what you're asking before jumping in. "Connect Claude to app health" could mean a few different things:

Are you looking to monitor the health of one of your running services (like the Railway bot, NOC Agent on port 5001, etc.) from within Claude? Or something else?

Let me ask a quick clarifying question:
```
This block is not supported on your current device yet.
```

**🧑 You:** Q: What do you mean by 'Connect Claude to app health'?
A: Something else (I'll explain)

**🤖 Claude:** Got it — go ahead and explain what you have in mind!

**🧑 You:** I mean app health on iPhone

**🤖 Claude:** Ah, you want to connect **Claude** (the app) to the **Apple Health** app on your iPhone — so Claude can read your health data (steps, sleep, heart rate, etc.).

**Short answer:** This isn't currently possible. Claude (iOS app) doesn't have Apple HealthKit integration. There's no way to grant Claude access to Health data right now.

**Possible workarounds:**

1. **Shortcuts + manual paste** — Use Apple Shortcuts to pull Health data into text, then paste it into Claude
2. **Export Health data** — Export a CSV/XML from the Health app and upload it to Claude
3. **Wait for official support** — Anthropic may add integrations like this in the future

Would you like me to help you build an Apple Shortcut that pulls your health stats so you can easily share them with Claude?

**🧑 You:** Yes

**🤖 Claude:** Let me build you a simple Apple Shortcut workflow. Since I can't create `.shortcut` files directly, I'll give you step-by-step instructions to build it yourself.

**Apple Shortcut: "Health Stats for Claude"**

Open the **Shortcuts** app on your iPhone and tap **+** to create a new one.

**Add these actions in order:**

1. **Find Health Samples** → Type: Steps, Start Date: Today
2. **Calculate Statistics** → Operation: Sum
3. **Set Variable** → Name: `steps`
4. **Find Health Samples** → Type: Heart Rate, Sort: Latest, Limit: 1
5. **Set Variable** → Name: `hr`
6. **Find Health Samples** → Type: Sleep Analysis, Start Date: Yesterday
7. **Set Variable** → Name: `sleep`
8. **Text** → Type this template:
   ```
   Health Update:
   Steps today: [steps]
   Heart rate (latest): [hr] bpm
   Sleep last night: [sleep]
   ```
9. **Copy to Clipboard**

Then just open Claude and paste it.

**Tips:**
- You can add more data types (weight, calories, etc.) using the same pattern
- Add the shortcut to your Home Screen for one-tap access
- You can also add **"Open App → Claude"** as a final step so it jumps straight there

Want me to help you add more health metrics to this, or build an N8N workflow that automates sending health data somewhere?

**🤖 Claude:** Nice, I see you're already in Apple Shortcuts and found the **"Log Health Sample"** action. That one is for **writing** data to Health (logging a new sample).

For **reading** data from Health to send to Claude, you need a different action:

**Use "Find Health Samples" instead** — search for it in the "Search Actions" bar at the bottom.

**Steps:**

1. Delete the current "Log Health Sample" action (tap the **X**)
2. Search for **"Find Health Samples"**
3. Set **Type** → whatever you want (Steps, Heart Rate, Sleep, etc.)
4. Set **Sort by** → Start Date, **Order** → Latest First
5. Set **Limit** → e.g. 1 (for latest reading)

Then after that action, add a **"Text"** action to format the result, and finally **"Copy to Clipboard"** so you can paste it into Claude.

Want me to walk you through the full shortcut action-by-action with screenshots descriptions?

**🤖 Claude:** Looking good! You've got **Find Health Samples** set up correctly — Heart Rate, last 7 days, count/min.

**Now tweak these two settings:**

1. **Sort by** → tap "None" → change to **Start Date**, then set order to **Latest First**
2. **Limit** → toggle it **ON** → set to **1** (so you get just the most recent reading)

**Then add the next actions below it:**

3. Search for **"Text"** action → type something like:
   ```
   Heart Rate: [Health Samples] bpm
   ```
   (Tap where you want the value and select the "Health Samples" variable)

4. Search for **"Copy to Clipboard"** action → add it after the Text

**To test:** Tap the **▶** (play button) at the bottom right. Then open Claude and paste — you should see your latest heart rate.

Once this works, we can duplicate the pattern to add steps, sleep, and more into one shortcut. Want to try running it?

**🧑 You:** No something like

**🤖 Claude:** I see — you're searching for "Heart" in the actions search but getting no results. That's because you're searching for a **new** action to add.

You don't need to search for a new action here. Go back and edit the **existing** "Find Health Samples" action you already set up:

1. Tap **Cancel** to close this search
2. Scroll up to your **Find Health Samples** action
3. Tap on **"None"** next to **Sort by** → select **Start Date**
4. A new option will appear for order → select **Latest First**
5. Toggle **Limit** ON → set to **1**

Those settings are inside the same action you already have — no need to add a new one.

After that, **then** use the search bar to add a **"Text"** action (search for "Text") below it.

Give it a try!

**🧑 You:** Where is it

**🤖 Claude:** You're almost there! **Sort by: Start Date** and **Order: Latest First** are set.

Now scroll down a little — **Limit** should be just below "Order". It's likely just off-screen at the bottom. Swipe up on the action card to reveal it, then toggle it ON and set it to **1**.

After that, tap **"Search Actions"** at the bottom and type **"Text"** to add the next action.

**🤖 Claude:** This is set up perfectly. Heart Rate, last 7 days, sorted by Start Date, Latest First, Limit ON, Get 1 Health sample.

**Next step:** Tap **"Search Actions"** at the bottom and type **"Text"**. Add the **Text** action.

Inside it, type:

```
Heart Rate: 
```

Then tap right after the colon and look for a button to insert a **variable** — it should show **"Health Samples"** as an option (from the previous action). Tap it to insert it. Then add **bpm** after it.

The result should look like: `Heart Rate: [Health Samples] bpm`

After that, add one more action: search for **"Copy to Clipboard"** and add it.

Then hit **▶** to test!

**🧑 You:** Correct?

**🤖 Claude:** Yes! You can see the **"Health S..."** variable button right there above the keyboard. Now:

1. Tap on **"Health S..."** (the pink heart icon button) — it will insert the variable after "Heart Rate:"
2. Then type **` bpm`** after it

So it reads: `Heart Rate: [Health Samples] bpm`

Then close the keyboard, search for **"Copy to Clipboard"** and add that action below.

You're almost done!

**🧑 You:** Right?

**🤖 Claude:** I see — you tapped on the Health Samples variable and it opened its details view. That's fine, no changes needed here.

Tap **"Return"** (bottom right blue button) to go back to the Text action.

Your Text field should now show: `Heart Rate: [Health Samples] bpm`

If the "bpm after it" text ended up in the variable name field by accident, tap **Return** first, then check what the Text action looks like. If it doesn't look right, screenshot it and send me — we'll fix it.

**🧑 You:** I don’t understand

**🤖 Claude:** No worries, this is simpler than it looks. This screen lets you choose **what property** of the Health Sample to insert. 

**"Value"** is already checked (the blue checkmark) — that's exactly what you want. It will output the heart rate number.

Now just tap **"Return"** (the blue keyboard button at top right) to go back to the Text action.

Then type **` bpm`** after the variable in the text field.

That's it for this part!

**🧑 You:** Where?

**🤖 Claude:** This looks great! The Text action shows:

```
Heart Rate:
🩷 Health Samples
```

You can add "bpm" later if you want — it's optional. The value will still come through.

**Now the last step:** Tap **"Search Actions"** at the bottom and type **"Copy to Clipboard"**. Add that action below the Text.

Then hit **▶** (play button, bottom right) to test it! After it runs, open Claude and paste — you should see your heart rate.

**🧑 You:** No I want to finish it no veritable there are

**🤖 Claude:** I think you're saying there's no variable showing — the **Health Samples** variable isn't inserting the actual value?

Let me clarify: the blue **"Health Samples"** text you see in the Text action IS the variable. It looks like text now, but when you **run** the shortcut (▶), it will be replaced with your actual heart rate number.

So what you have is already correct! It will output something like `Heart Rate: 72` when it runs.

Now just:

1. Tap **"Search Actions"**
2. Type **"Copy to Clipboard"**
3. Add it
4. Hit **▶** to test

Want to try running it?

**🧑 You:** Yes

**🤖 Claude:** Go for it! Add **"Copy to Clipboard"** and hit **▶**.

After it runs, come back to this chat and **long-press → Paste**. I'll confirm if it worked.

**🧑 You:** Heart Rate: 
72.14508819580078

**🤖 Claude:** It works! Your latest heart rate reading is **72 bpm** — that's a healthy resting rate.

Now you have a working shortcut. Want to expand it? We can add more health data in the same shortcut, like:

- **Steps today**
- **Sleep last night**
- **Active calories**

Just duplicate the same pattern (Find Health Samples → add to the Text block) for each metric. Want me to walk you through adding steps next?

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
- [[2026-03-23 - ספר חרבות וכלכלה]]
- [[2026-03-23 - Reading PDF content from disk]]

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
- [[2026-02-01 - Claude_s image generation capabilities]]
- [[2026-02-05 - Getting access to Claude API]]
- [[2026-02-07 - Installing Claude code on Mac]]
- [[2026-02-08 - Claude API pricing and costs]]
- [[2026-02-08 - Improving Claude code setup and performance]]
- [[2026-02-09 - Checking Claude usage limits]]
- [[2026-02-09 - Installing Claude Code CLI tool]]
- [[2026-02-18 - Claude code beginner_s guide]]