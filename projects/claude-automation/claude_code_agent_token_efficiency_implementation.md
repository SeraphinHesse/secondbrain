# Claude Code Token Efficiency Implementation Spec

> Purpose: Give a Claude Code agent a clear, low-token implementation plan for making this repo cheaper, faster, and easier to work on without changing game behavior.
>
> Primary outcome: Replace broad rereading with a small routing system, subsystem capsules, task-specific skills, and guardrails that prevent unnecessary file reads.

---

## 0. Operating Mandate For The Agent

You are implementing an **agent-efficiency layer** for this repository.

Your job is to add or refactor documentation/configuration that helps future Claude Code sessions avoid rereading the entire codebase.

Do **not** refactor gameplay, engine behavior, architecture, assets, or production code unless the user explicitly asks for that in a separate task.

### Non-Negotiable Rules

1. **Do not scan the whole repo blindly.**
2. **Do not read generated files, imported assets, binaries, build outputs, logs, or cache directories unless required.**
3. **Do not turn `CLAUDE.md` into a giant knowledge base.**
4. **Do not add session notes to root `CLAUDE.md`.**
5. **Do not use Obsidian or any external vault as always-loaded context.**
6. **Keep every always-loaded instruction file short.**
7. **Prefer links, maps, and retrieval instructions over pasted architecture explanations.**
8. **Preserve existing project-specific instructions. Compress them; do not delete important rules.**
9. **When uncertain, create a small placeholder with TODOs instead of inventing architecture.**
10. **End with a concise implementation report listing changed files and remaining TODOs.**

### Token Discipline While Implementing

Before reading files, identify the smallest useful information needed.

Allowed initial reads:

```txt
- root CLAUDE.md, if it exists
- existing .claude/ directory, if it exists
- top-level directory listing
- package/project config files only if needed to infer engine/framework
- existing docs/README files only if they are short
```

Use shell search/listing before opening files:

```bash
find . -maxdepth 3 -type f \
  ! -path './.git/*' \
  ! -path './.godot/*' \
  ! -path './build/*' \
  ! -path './dist/*' \
  ! -path './vendor/*' \
  ! -path './addons/*'
```

Prefer targeted search:

```bash
rg "class_name|extends|Grid|Enemy|Building|Economy|Wave|Save|UI" --glob '!*.import' --glob '!*.uid' --glob '!addons/**' --glob '!vendor/**'
```

Do not open large files unless directly needed. If a file is over 400 lines, inspect relevant sections only.

---

## 1. Implementation Goal

Create a structure like this, adapted to the actual repo:

```txt
repo/
  CLAUDE.md
  .claude/
    settings.json
    skills/
      add-building/SKILL.md
      add-enemy-type/SKILL.md
      debug-pathfinding/SKILL.md
      update-agent-docs/SKILL.md
      repo-orientation/SKILL.md
  docs/
    ai/
      INDEX.md
      decisions.md
      glossary.md
      capsule-template.md
      prompt-templates.md
      capsules/
        grid.md
        buildings.md
        enemies.md
        economy.md
        waves.md
        ui.md
        save-load.md
        rendering.md
```

If some systems do not exist, create only the relevant capsule files and keep missing ones as TODOs in `docs/ai/INDEX.md`.

---

## 2. Existing Instruction Audit

### Task

Inspect existing agent instruction files and classify them.

Look for:

```txt
CLAUDE.md
**/CLAUDE.md
.claude/**
docs/**
README.md
```

### Classify Existing Content Into Four Buckets

| Bucket | Belongs Where | Examples |
|---|---|---|
| Always-needed routing | root `CLAUDE.md` | repo map, how to choose subsystem, global safety rules |
| Subsystem-specific rules | local `CLAUDE.md` or capsule | grid invariants, building registration, enemy pathing |
| Reusable procedure | `.claude/skills/*/SKILL.md` | add building, debug pathfinding, update docs |
| Historical memory | `docs/ai/decisions.md` or Obsidian | old decisions, rationale, meeting notes |

### Output Of Audit

Before editing, write a short internal plan:

```txt
Existing instruction files found:
- ...

Content to preserve:
- ...

Content to move:
- ...

Files to create/update:
- ...
```

Then implement directly. Do not ask for confirmation unless there is risk of deleting important user-authored instructions.

---

## 3. Root `CLAUDE.md` Target

### Goal

Make root `CLAUDE.md` a **thin router**, not a project encyclopedia.

Hard limit: **200 lines maximum**.

Preferred target: **80-150 lines**.

### Root `CLAUDE.md` Template

Adapt this template to the actual repo.

```md
# Claude Code Router

This file is a routing layer for Claude Code. Keep it short.
Do not add session notes, implementation logs, or long architecture explanations here.

## Core Rule

Before editing, identify the smallest relevant subsystem and read only the minimum needed files.

Default read order:
1. This file.
2. The closest subsystem `CLAUDE.md`, if present.
3. The relevant `docs/ai/capsules/*.md` file.
4. Directly relevant source files.

Do not scan the whole repo unless the task explicitly crosses systems.

## Repo Map

Update this list to match the actual project:

- `engine/` — reusable engine/runtime systems.
- `game/` — game-specific buildings, enemies, economy, waves, levels.
- `ui/` — menus, HUD, overlays, interface logic.
- `assets/` — art/audio/imported files. Do not read unless task is asset-related.
- `docs/ai/` — compressed agent-readable project memory.
- `.claude/skills/` — task-specific procedures loaded only when needed.

## Agent Memory Structure

- Use `docs/ai/INDEX.md` for the map of agent-readable docs.
- Use `docs/ai/capsules/*.md` for subsystem summaries.
- Use `docs/ai/decisions.md` for durable decisions only.
- Use `docs/ai/glossary.md` for project terms.
- Use `.claude/skills/*/SKILL.md` for workflows.

## Token Discipline

- Prefer `rg`, `find`, and symbol search before opening files.
- Read no more than 5 source files before forming a plan.
- If more files are needed, state why.
- Do not read generated files, imports, binaries, caches, build output, or logs.
- Do not open images/audio unless the task is explicitly visual/audio.

## Editing Rules

- Make the smallest change that satisfies the task.
- Preserve existing architecture unless the task asks for architecture changes.
- Prefer updating one subsystem at a time.
- Do not duplicate logic across systems.
- Update the relevant capsule only when a durable invariant, file path, or workflow changes.

## Verification

Use the narrowest available verification:
- subsystem test
- targeted scene/run check
- type/lint/build check
- manual checklist from the relevant capsule

If no verification exists, say what was checked and what could not be checked.

## Documentation Update Rule

After meaningful changes:
1. Update the relevant capsule in `docs/ai/capsules/`.
2. Add durable architecture decisions to `docs/ai/decisions.md`.
3. Do not add temporary notes to this file.

## Obsidian / External Vault Rule

Do not read an Obsidian vault by default.
Use external memory only when the user asks for historical reasoning or when the repo docs explicitly point to one relevant note.
Never bulk-read session notes.
```

### Important

If the existing `CLAUDE.md` has critical project-specific instructions, preserve them by compressing them into:

```txt
- root CLAUDE.md, if global and always needed
- subsystem CLAUDE.md, if local
- docs/ai/capsules/*.md, if explanatory
- .claude/skills/*/SKILL.md, if procedural
```

---

## 4. `docs/ai/` Structure

Create `docs/ai/` as the compressed agent memory layer.

### 4.1 `docs/ai/INDEX.md`

```md
# Agent Documentation Index

This directory contains compressed context for Claude Code agents.
Read only the files relevant to the current task.

## Read Order

1. Root `CLAUDE.md`
2. Closest subsystem `CLAUDE.md`, if present
3. One relevant capsule from `docs/ai/capsules/`
4. Directly relevant source files

## Capsules

- `capsules/grid.md` — grid, tiles, placement, occupancy, unlock rules.
- `capsules/buildings.md` — building types, registration, placement behavior, upgrades.
- `capsules/enemies.md` — enemy types, pathing, stats, spawn behavior.
- `capsules/economy.md` — currency, production, XP/progression, costs.
- `capsules/waves.md` — rounds/waves/spawning/progression timing.
- `capsules/ui.md` — HUD, menus, overlays, player feedback.
- `capsules/save-load.md` — persistence, serialization, migration rules.
- `capsules/rendering.md` — sprites, tilemaps, visual conventions.

## Durable Memory

- `decisions.md` — lasting architecture/design decisions and rationale.
- `glossary.md` — project-specific terms.
- `prompt-templates.md` — reusable low-token user prompts.

## Maintenance Rule

When changing a subsystem, update only the matching capsule.
Do not expand capsules into full documentation.
Each capsule should remain skimmable.
```

### 4.2 `docs/ai/capsule-template.md`

```md
# Capsule Template

> Keep this file short. Target 60-120 lines.
> This is compressed agent context, not full documentation.

## Purpose

What this subsystem owns.

## Key Files

- `path/to/file` — why it matters.
- `path/to/file` — why it matters.

## Data Flow

1. Step one.
2. Step two.
3. Step three.

## Invariants

- Rule that must not be broken.
- Rule that must not be duplicated elsewhere.
- Rule about ownership or boundaries.

## Common Tasks

### Task Name

Read:
- `path/to/file`

Edit:
- `path/to/file`

Verify:
- command or manual check

## Common Mistakes

- Mistake to avoid.
- Mistake to avoid.

## Verification

- Narrowest automated check.
- Manual check if no automated test exists.

## Last Updated

- YYYY-MM-DD — reason for update.
```

### 4.3 Example Capsule: `docs/ai/capsules/grid.md`

Create this file if the repo appears to have a grid/tile/placement system. Adapt paths to actual files.

```md
# Grid Capsule

## Purpose

Owns tile coordinates, grid state, occupancy, placement validation, combat/build/spawn zones, and unlock expansion rules.

## Key Files

TODO: Replace with actual paths after inspecting the repo.

- `TODO` — authoritative grid state.
- `TODO` — tile/cell data.
- `TODO` — placement flow.
- `TODO` — unlock or expansion behavior.

## Data Flow

TODO: Fill from actual code.

Expected shape:
1. Map/grid initializes tile data.
2. Placement system asks grid whether a tile/area is valid.
3. Building/enemy systems consume grid position/path data.
4. Unlock logic mutates tile zone states.

## Invariants

- Do not duplicate coordinate conversion logic outside the grid owner.
- Do not bypass the authoritative occupancy/placement check.
- Keep buildable/base rules separate from spawn/combat/background rules.
- If map dimensions change, update pathing, placement, and UI assumptions together.

## Common Tasks

### Change unlock behavior

Read:
- this capsule
- actual grid owner file
- actual unlock/progression file
- placement validation file

Verify:
- place a building
- unlock a section
- confirm converted zones are correct
- confirm enemy pathing still works

### Change placement validation

Read:
- grid owner
- placement controller
- building base class or registry

Verify:
- valid placement accepted
- invalid placement rejected
- occupied tile rejected

## Common Mistakes

- Hardcoding dimensions in unrelated systems.
- Updating visuals but not authoritative tile data.
- Updating tile data but not pathing/navigation.
- Letting building scripts decide global placement rules.

## Verification

TODO: Add project-specific command or manual check.

## Last Updated

- TODO — created by agent-efficiency setup.
```

### 4.4 Example Capsule: `docs/ai/capsules/buildings.md`

```md
# Buildings Capsule

## Purpose

Owns building definitions, placement behavior, upgrades, production/combat effects, and registration/factory logic.

## Key Files

TODO: Replace with actual paths after inspecting the repo.

- `TODO` — base building class.
- `TODO` — building registry/factory.
- `TODO` — placement integration.
- `TODO` — upgrade/progression definitions.

## Invariants

- New buildings must be registered in the central registry/factory if one exists.
- Shared building behavior belongs in the base building class or component, not copied into each building.
- Economy buildings and defense buildings should not duplicate placement validation.
- Upgrade data should be data-driven if the repo already uses data tables/resources/configs.

## Common Tasks

### Add a new building

Read:
- this capsule
- base building class
- closest similar building
- registry/factory
- relevant data/resource/config file

Edit:
- new building script/resource
- registry/factory
- tests or sample scene if applicable

Verify:
- building appears in selection/build menu if applicable
- placement works
- cost/effect applies
- no duplicate registration

## Common Mistakes

- Adding a building script but forgetting registration.
- Duplicating placement rules.
- Hardcoding cost/effect values in UI and gameplay separately.
- Updating visuals but not data.

## Verification

TODO: Add project-specific command or manual check.

## Last Updated

- TODO — created by agent-efficiency setup.
```

### 4.5 Create Other Capsules As Short TODO Files

Create short placeholders for systems that exist:

```txt
docs/ai/capsules/enemies.md
docs/ai/capsules/economy.md
docs/ai/capsules/waves.md
docs/ai/capsules/ui.md
docs/ai/capsules/save-load.md
docs/ai/capsules/rendering.md
```

Each should follow the capsule template and contain actual paths only when known.

Do not invent file paths.

---

## 5. Durable Memory Files

### 5.1 `docs/ai/decisions.md`

```md
# Durable Decisions

Use this file for decisions that should survive across Claude Code sessions.
Do not use it for temporary task notes.

Format:

```txt
YYYY-MM-DD — Decision title
Decision: ...
Rationale: ...
Implications: ...
Related files: ...
```

## Decisions

TODO: Add existing durable decisions only if found in current docs or source comments.
```

### 5.2 `docs/ai/glossary.md`

```md
# Project Glossary

Use this file for project-specific terms that future agents should understand.
Keep entries short.

## Terms

- **Buildable zone** — TODO.
- **Combat zone** — TODO.
- **Spawn zone** — TODO.
- **Background zone** — TODO.
- **Base** — TODO.
- **Love points** — TODO, if this is the current currency term.
- **Determination points** — TODO, if this is the current XP/progression term.
```

Only include terms that actually match the current repo/design docs.

### 5.3 `docs/ai/prompt-templates.md`

```md
# Low-Token Prompt Templates

Use these when starting Claude Code tasks.

## Local Bug Fix

```txt
Task: Fix [specific bug].

Scope:
- Relevant subsystem: [name]
- Start in folder: [path]
- Expected files: [paths if known]
- Do not touch: [systems/folders]

Token discipline:
- Do not scan the repo.
- Read the relevant capsule first.
- Read at most 5 source files before proposing a plan.
- Use rg/find before opening files.

Acceptance:
- [expected behavior]
- [test/manual check]
```

## Add Building

```txt
Task: Add a new building: [name].

Building type: [defense/economy/boost/special]
Expected behavior: [behavior]
Expected files to inspect:
- docs/ai/capsules/buildings.md
- closest similar building
- building registry/factory
- placement integration

Do not scan unrelated enemy, UI, save/load, or asset folders unless required.

Acceptance:
- building can be placed
- cost is applied
- effect works
- registry/menu updated if applicable
- relevant capsule updated only if a durable rule changed
```

## Debug Pathfinding

```txt
Task: Debug pathfinding issue: [symptom].

Scope:
- Read docs/ai/capsules/grid.md
- Read docs/ai/capsules/enemies.md
- Inspect only pathfinding/grid files first

Do not modify building/economy/UI unless the cause is proven there.

Acceptance:
- reproduce or explain likely cause
- minimal fix
- narrow verification
```

## End-Of-Task Capsule Update

```txt
Before finishing, update only the relevant docs/ai capsule if this task changed:
- subsystem ownership
- key file paths
- invariants
- common workflow
- verification method

Do not add temporary session notes.
```
```

---

## 6. Claude Skills

Create reusable Claude Code skills for common workflows.

Skills should be specific and short.

### 6.1 `.claude/skills/repo-orientation/SKILL.md`

```md
---
description: Use for first-pass orientation in this repo without wasting tokens on broad rereading.
---

# Repo Orientation Skill

Goal: Identify the smallest relevant subsystem for the user's task.

Steps:
1. Read root `CLAUDE.md`.
2. Read `docs/ai/INDEX.md`.
3. Use `find` or `rg` to locate likely subsystem files.
4. Read only one relevant capsule.
5. Read at most 5 source files before proposing a plan.

Do not:
- scan the whole repo
- read generated/imported/binary files
- open unrelated systems
- summarize the entire architecture

Return:
- relevant subsystem
- files likely needed
- files intentionally avoided
- proposed next step
```

### 6.2 `.claude/skills/add-building/SKILL.md`

```md
---
description: Use when adding or modifying a building, tower, economy producer, boost building, or upgradeable structure.
---

# Add Or Modify Building Skill

Steps:
1. Read `docs/ai/capsules/buildings.md`.
2. Locate the closest similar building.
3. Locate the building base class and registry/factory.
4. Inspect placement integration only if placement behavior changes.
5. Make the smallest change.
6. Update registry/data/menu only if required.
7. Run the narrowest verification.
8. Update the buildings capsule only if a durable rule, path, or workflow changed.

Avoid:
- reading enemy/pathfinding systems unless this building affects them
- duplicating placement validation
- hardcoding cost/effect in multiple places
- editing unrelated UI unless the building must appear in UI

Final report:
- changed files
- behavior added/changed
- verification performed
- capsule updated or not, with reason
```

### 6.3 `.claude/skills/add-enemy-type/SKILL.md`

```md
---
description: Use when adding or modifying an enemy type, enemy stats, spawn behavior, or pathing interaction.
---

# Add Or Modify Enemy Type Skill

Steps:
1. Read `docs/ai/capsules/enemies.md`.
2. Read `docs/ai/capsules/waves.md` if spawning/waves are involved.
3. Locate the closest similar enemy.
4. Locate enemy base class and enemy registry/spawner.
5. Make the smallest change.
6. Verify spawn, movement/pathing, damage/death behavior, and wave integration if applicable.
7. Update the enemy or waves capsule only if a durable rule, path, or workflow changed.

Avoid:
- changing grid logic unless pathing requires it
- changing building logic unless enemy interactions require it
- duplicating stats in UI and gameplay separately

Final report:
- changed files
- behavior added/changed
- verification performed
- capsule updated or not, with reason
```

### 6.4 `.claude/skills/debug-pathfinding/SKILL.md`

```md
---
description: Use when enemies do not move correctly, paths are blocked unexpectedly, spawn/combat zones behave incorrectly, or placement breaks navigation.
---

# Debug Pathfinding Skill

Steps:
1. Read `docs/ai/capsules/grid.md`.
2. Read `docs/ai/capsules/enemies.md`.
3. Identify whether the issue is grid data, zone conversion, navigation/pathfinding, enemy movement, or placement blocking.
4. Use targeted search for path/grid APIs.
5. Inspect only directly relevant files.
6. Reproduce or describe the most likely failure path.
7. Make the smallest fix.
8. Verify with a narrow manual or automated check.

Avoid:
- broad architecture rewrites
- changing building/economy/UI before proving the bug is there
- hardcoding paths or dimensions

Final report:
- root cause
- changed files
- verification
- remaining risks
```

### 6.5 `.claude/skills/update-agent-docs/SKILL.md`

```md
---
description: Use after meaningful code changes to update compressed agent docs without bloating context.
---

# Update Agent Docs Skill

Goal: Keep future Claude Code sessions cheap and accurate.

Update only durable, reusable information.

Update a capsule if any of these changed:
- subsystem ownership
- key files
- data flow
- invariants
- common workflow
- verification method
- repeated mistakes to avoid

Add to `docs/ai/decisions.md` only if a lasting design or architecture decision was made.

Do not add:
- temporary TODOs unrelated to future work
- session logs
- full implementation summaries
- long explanations
- copied code
- chat transcripts

Hard limits:
- Capsules should target 60-120 lines.
- Root `CLAUDE.md` should stay under 200 lines.
- Prefer replacing stale text over appending.
```

---

## 7. Optional `.claude/settings.json` Read Deny Rules

If `.claude/settings.json` already exists, merge carefully and preserve existing settings.

If it does not exist, create it.

Use the deny list only for paths that are safe to block in this repo.

```json
{
  "permissions": {
    "deny": [
      "Read(./.git/**)",
      "Read(./.godot/**)",
      "Read(./build/**)",
      "Read(./dist/**)",
      "Read(./exports/**)",
      "Read(./logs/**)",
      "Read(./tmp/**)",
      "Read(./cache/**)",
      "Read(./**/*.import)",
      "Read(./**/*.uid)",
      "Read(./**/*.png)",
      "Read(./**/*.jpg)",
      "Read(./**/*.jpeg)",
      "Read(./**/*.webp)",
      "Read(./**/*.wav)",
      "Read(./**/*.mp3)",
      "Read(./**/*.ogg)",
      "Read(./**/*.blend)",
      "Read(./**/*.fbx)",
      "Read(./**/*.glb)",
      "Read(./**/*.gltf)"
    ]
  }
}
```

### Warning

Do not deny `addons/**`, `vendor/**`, or plugin directories if this project contains editable gameplay/plugin code there.

If in doubt, add a comment in the final report instead of blocking those paths.

---

## 8. Local Subsystem `CLAUDE.md` Files

If the repo has clear subsystem folders, add short local `CLAUDE.md` files.

Examples:

```txt
engine/CLAUDE.md
game/CLAUDE.md
ui/CLAUDE.md
```

Each should be under 80 lines.

### Template

```md
# Local Claude Instructions: [Subsystem]

Read this only when working inside this subsystem.

## Scope

This subsystem owns:
- TODO
- TODO

This subsystem does not own:
- TODO
- TODO

## Read First

- `docs/ai/capsules/[matching-capsule].md`
- TODO key local file

## Rules

- TODO invariant.
- TODO invariant.
- Do not duplicate logic owned by another subsystem.

## Verification

- TODO command/manual check.
```

Do not duplicate root instructions here.

---

## 9. Obsidian Guidance

Do not add an Obsidian vault to the repo unless the user explicitly asks.

If an Obsidian vault already exists in or near the repo:

1. Do not bulk-read it.
2. Create or update only a small `Index.md` if asked.
3. Use it as historical memory, not default context.
4. Distill durable facts into `docs/ai/capsules/*.md` or `docs/ai/decisions.md`.
5. Never import the whole vault from root `CLAUDE.md`.

Recommended rule for root `CLAUDE.md`:

```md
## Obsidian / External Vault Rule

Do not read an Obsidian vault by default.
Use it only when the user asks for historical reasoning or when repo docs point to one specific relevant note.
Never bulk-read session notes.
```

---

## 10. Implementation Sequence

Follow this order:

### Phase 1 — Audit

- Find existing instruction files.
- Read existing root `CLAUDE.md`.
- Identify important project-specific instructions to preserve.
- Identify obvious subsystems from directory names and source search.

### Phase 2 — Create Agent Docs

- Create `docs/ai/INDEX.md`.
- Create `docs/ai/capsule-template.md`.
- Create `docs/ai/decisions.md`.
- Create `docs/ai/glossary.md`.
- Create `docs/ai/prompt-templates.md`.
- Create relevant `docs/ai/capsules/*.md` files.

### Phase 3 — Refactor Root `CLAUDE.md`

- Backup existing important content mentally while editing.
- Replace bloated content with a thin router.
- Move subsystem details to capsules.
- Move procedures to skills.
- Keep root under 200 lines.

### Phase 4 — Add Skills

Create:

```txt
.claude/skills/repo-orientation/SKILL.md
.claude/skills/add-building/SKILL.md
.claude/skills/add-enemy-type/SKILL.md
.claude/skills/debug-pathfinding/SKILL.md
.claude/skills/update-agent-docs/SKILL.md
```

Adjust names if the repo uses different concepts.

### Phase 5 — Add Optional Deny Rules

- Create or merge `.claude/settings.json`.
- Deny generated/assets/cache reads only where safe.
- Avoid blocking editable plugin/vendor code unless clearly generated or third-party.

### Phase 6 — Add Local `CLAUDE.md` Files

Only add local files for major folders where they reduce repeated explanation.

Keep them short.

### Phase 7 — Final Verification

Check:

```bash
find . -name 'CLAUDE.md' -o -path './.claude/skills/*/SKILL.md' -o -path './docs/ai/*' -o -path './docs/ai/capsules/*'
```

Check line counts:

```bash
wc -l CLAUDE.md docs/ai/*.md docs/ai/capsules/*.md .claude/skills/*/SKILL.md 2>/dev/null
```

Root `CLAUDE.md` must be under 200 lines.

Capsules should preferably be under 120 lines each unless the subsystem genuinely needs more.

---

## 11. Acceptance Criteria

Implementation is complete when:

- [ ] Root `CLAUDE.md` is a router, not a giant architecture doc.
- [ ] Root `CLAUDE.md` is under 200 lines.
- [ ] `docs/ai/INDEX.md` exists.
- [ ] `docs/ai/capsule-template.md` exists.
- [ ] At least 3 relevant subsystem capsules exist.
- [ ] `docs/ai/decisions.md` exists.
- [ ] `docs/ai/glossary.md` exists.
- [ ] `docs/ai/prompt-templates.md` exists.
- [ ] At least 3 relevant skills exist in `.claude/skills/`.
- [ ] Existing project-specific instructions were preserved in the correct place.
- [ ] No gameplay/engine behavior was changed.
- [ ] Generated/imported/asset/cache read-deny rules were added or explicitly skipped with reason.
- [ ] Final report explains how to use the new setup.

---

## 12. Final Report Format

When finished, respond with:

```txt
Implemented Claude Code token-efficiency layer.

Changed files:
- path — what changed
- path — what changed

Preserved instructions:
- ...

New workflow:
- Start Claude from the smallest relevant folder when possible.
- Read root CLAUDE.md, then the matching capsule.
- Use skills for repeated workflows.
- Update capsules only when durable rules change.

Verification:
- Root CLAUDE.md line count: X
- Capsules created: X
- Skills created: X
- Deny rules added/skipped: ...

No gameplay or engine behavior was changed.

Remaining TODOs:
- ...
```

---

## 13. Important Anti-Patterns To Avoid

Do not do these:

```txt
- Add a 1,000-line CLAUDE.md.
- Import every architecture doc into CLAUDE.md.
- Create an Obsidian vault and force Claude to read all notes.
- Add every session summary to permanent docs.
- Summarize the whole repo every task.
- Spawn many exploratory agents by default.
- Read image/audio/assets for code tasks.
- Rewrite production architecture while setting up docs.
- Put volatile task notes into durable memory.
```

Preferred pattern:

```txt
Thin router -> one capsule -> few source files -> narrow edit -> narrow verification -> capsule update only if durable.
```

---

## 14. Optional User-Facing Prompt After Setup

After this implementation, the user can start future tasks with:

```txt
Use the new token-efficient workflow.
Read only the relevant CLAUDE.md and docs/ai capsule.
Do not scan the repo.
Read at most 5 source files before proposing a plan.
Use the relevant skill if one applies.
Make the smallest change and update the capsule only if durable behavior changed.
```

