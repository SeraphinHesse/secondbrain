# ToDo List Format Conventions

## Task Entry Format

```
* Task name
  Description — what needs to happen, why it matters, what done looks like.
```

- The `* ` prefix marks a task item.
- The description is on the **immediately following line**, indented with 2 spaces.
- Description is optional but should be added whenever the task is not self-evident.
- Use `* !` prefix for high-importance tasks.
- Use `^` for major tasks (big, multi-session work). Unmarked tasks are minor.
- Canonical flag order: `* x !^Task text` (done marker, then `!`, then `^`). The parser accepts `!`/`^` in either order but always writes this order.

## Section Structure

```
##### Category Name

###### Sub-Category

* Task name
  Description of the task.

* !High importance task
  Why this is urgent and what it requires.
```

## Category Hierarchy

- `#####` = top-level category (e.g. `##### How to be Human`)
- `######` = sub-category (e.g. `###### Claude Build`)
- Task bullets live under the nearest sub-category (or directly under a category if no sub exists)

## Reminder Format

Reminders use a timestamp prefix and live under `##### Reminders`:

```
* [YYYY-MM-DD HH:MM] Reminder text
  Optional description or context.
```

## Rules

1. Never add duplicate tasks — scan the section before adding.
2. `!` prefix = high priority (rendered in red on the dashboard).
3. `^` prefix = major task (rendered in the collapsible "Major" group on the dashboard; unmarked = "Minor"). Independent of `!`.
4. Descriptions are file-backed — they appear in `ToDo.md` and sync to the dashboard.
5. The dashboard server (`TODO list/todo-server.js`) reads and writes this file directly.
