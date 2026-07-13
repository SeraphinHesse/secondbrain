# TODO List — Dashboard & Server Guide

## Overview

This folder contains the dashboard GUI and its backend server. `ToDo.md` lives one level up in the repo root and is the single source of truth — users edit it directly, and the dashboard reads/writes it via the server.

```
secondbrain/
├── ToDo.md                  ← source of truth, edited daily by the user
└── TODO list/
    ├── todo-dashboard.html  ← single-page dashboard GUI
    ├── todo-server.js       ← Node.js server (primary, no npm needed)
    ├── todo-server.py       ← Python fallback server
    ├── launch-dashboard.bat ← start server if not running, open browser
    ├── restart-dashboard.bat← kill + restart server, open browser
    ├── setup-autostart.bat  ← register server in Windows startup
    ├── Todolistconventions.md
    └── CLAUDE.md            ← this file
```

## Architecture

- **Server** (`todo-server.js`): Pure Node stdlib HTTP server on `localhost:8765`. Reads/writes `../ToDo.md`. No build step, no npm.
- **Client** (`todo-dashboard.html`): Vanilla JS, single HTML file, served by the server at `/`. Fetches `localhost:8765/api/tasks` for all data operations.
- **Data format**: `ToDo.md` is the authoritative store. Descriptions are stored as indented lines (`  description`) directly after their `* task` line.

## API

| Method | Endpoint    | Body fields                               | Returns        |
|--------|-------------|-------------------------------------------|----------------|
| GET    | /api/tasks  | —                                         | Task[]         |
| POST   | /api/tasks  | `text, cat, high, major, desc`            | Task[]         |
| PATCH  | /api/tasks  | `id, text, cat, high, major, desc, done`  | Task[]         |
| DELETE | /api/tasks  | `id`                                      | Task[]         |
| DELETE | /api/category | `name` (display name, e.g. `"HTBH / Design"`) | `{ removed, tasks }` |

Task object shape: `{ id, cat, text, high, major, done, reminder, desc }`

`DELETE /api/category` removes every matching section (duplicates included) and all tasks inside it from `ToDo.md`. Rejects `name: "Reminders"` with 400. Reminders under `Reminders / <cat>` are not touched. `CAT_MAP` stays intact, so adding a task to a deleted built-in category recreates its section.

Task line markers in `ToDo.md`: `x ` = done, `!` = high priority, `^` = major (unmarked = minor). Canonical write order: `* x !^Task text`.

## Task Description Convention

Tasks can have an optional description stored as an indented line in `ToDo.md`:

```markdown
* Task name
  Description — context, why, acceptance criteria.
```

- The description line must be indented with 2+ spaces.
- It must be the line **immediately after** the `* task` line.
- The parser uses this to read/write the `desc` field.
- No blank line between task and description.

## Branching Rules — CRITICAL

GUI/server changes **must** go on a separate branch. `ToDo.md` must never be modified by a dashboard feature branch — all user task data stays on `main`.

**Correct workflow:**
```
git checkout -b claude/dashboard-<feature>
# Edit only files in "TODO list/"
# Do NOT touch ToDo.md
git push origin claude/dashboard-<feature>
# PR → merge to main
```

**Why this matters:** The user edits `ToDo.md` daily on `main`. If a dashboard branch touches `ToDo.md`, merging will cause conflicts with the user's live data.

**Rule:** Feature branches for this folder must only contain changes to files inside `TODO list/`. If a change requires adding a new category mapping, add it to `todo-server.js`'s `CAT_MAP` — never by pre-populating `ToDo.md`.

## CAT_MAP — Adding Categories

`CAT_MAP` in `todo-server.js` maps dashboard display names to markdown section headers in `ToDo.md`. When adding a new top-level category:

1. Add entry to `CAT_MAP` in `todo-server.js`
2. Add matching entry to `DEFAULT_CAT_META` in `todo-dashboard.html` (icon + color)
3. Mirror the Reminders sub-category if applicable
4. **Do not** pre-create the section in `ToDo.md` — the server creates it on first task add

## Running the Server

```bat
cd "TODO list"
node todo-server.js
```

Or double-click `launch-dashboard.bat`. Server port: **8765**.

## Editing the Dashboard

The dashboard is a single self-contained HTML file. No build tooling. Keep it that way.

- All state that needs to survive browser restarts goes in `ToDo.md` (via the server), not `localStorage`.
- `localStorage` is used only for UI state: collapse states (`sb-collapsed`, `sb-group-col`, `sb-urgent-col`, `sb-rem-col`, `sb-rem-zone`), category order (`sb-cat-order`), hidden built-in categories (`sb-hidden-cats`), custom categories (`sb-custom-cats`), reminder pairs (`sb-rem-pairs`).
- Never store task descriptions in `localStorage` — they live in `ToDo.md`.
- Drag & drop (tasks between groups/categories, category reorder) is mouse-only HTML5 DnD; on touch devices use the modal's category dropdown instead.

## Testing Changes

After making changes:
1. Kill existing server: `restart-dashboard.bat`
2. Open `http://localhost:8765`
3. Verify: add a task with description, confirm it appears in `ToDo.md` as an indented line
4. Verify: edit a description in the modal, confirm `ToDo.md` updates
5. Verify: delete a task, confirm its description line is also removed
6. Verify: no regressions in reminder rendering, urgent zone, backlog
