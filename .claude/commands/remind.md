Handle a reminder request from: $ARGUMENTS

Parse the arguments to extract:
- The reminder message (required)
- When to remind: parse any time reference ("at 3pm", "tomorrow at 10", "in 2 hours", "Monday", etc.) relative to today's date in Europe/Berlin timezone. If no time is given, default to 3 hours from now, rounded to the nearest 15 minutes.
- Category (infer from keywords, default "General"):
  - "HTBH" — game dev, prototype, HTBH, WBS, Taiga, mechanics, design, Johann, balancing
  - "Agency" — client, lead, marketing, agency, campaign, outreach
  - "Admin" — admin, tax, invoice, paperwork, government, bureaucracy
  - "Bureaucracy & Chores" — Pfand, bottles, recycling, chores, cleaning, laundry, groceries, shopping, household, errands
  - "General" — everything else

Then do all three steps in order:

**Step 1 — Create Google Calendar event**
Use `mcp__claude_ai_Google_Calendar__create_event` with:
- summary: "🔔 [reminder message]"
- start: ISO 8601 datetime in Europe/Berlin (e.g. "2026-06-09T15:00:00+02:00")
- end: 15 minutes after start
- description: "[reminder message]\n\n→ Dashboard: http://localhost:8765"
- Use the primary calendar

**Step 2 — Add to ToDo.md**
File path: `C:\Users\serap\OneDrive\Documents\GitHub\secondbrain\ToDo.md`

Find the `##### Reminders` section, then find or create the `###### [category]` subsection under it. Insert after the last `* ` item in that subsection (or right after the header if empty):
```
* [YYYY-MM-DD HH:MM] [reminder message]
```
Use the exact reminder time in the brackets. If the `###### [category]` subsection doesn't exist yet, add it under `##### Reminders` before inserting the item.

**Step 3 — Confirm**
Reply with exactly one line:
"Reminder set for [human-readable time, e.g. 'Today at 15:00' or 'Tomorrow at 10:00']: [message]"
