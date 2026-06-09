# CONTEXT FOR CLAUDE CODE â€” HOW TO BE HUMAN PROJECT MANAGEMENT

> **You are operating inside the Secondbrain repo, which serves as the project management,
> planning, and idea-collection layer for the game "How to Be Human" (HTBH).**
>
> Your role here is NOT to write game code â€” that lives in the HowToBeHuman repo.
> Your role here is to help with:
> - **Project planning & task tracking** (milestones, WBS, sprints, scope)
> - **Game design documentation** (mechanics, systems, balancing, design decisions)
> - **Idea capture & processing** (inbox routing, structured notes, ideation)
> - **Producer-level oversight** (what needs doing, what's blocked, what's next)
>
> The CLAUDE.md files below are sourced directly from the HowToBeHuman game repo.
> They describe the architecture, conventions, and current state of the codebase
> so you have full context when discussing or planning work on it.
>
> **Never edit game source files from here. Always work via the HowToBeHuman repo for code.**

---
## Root CLAUDE.md

# CLAUDE.md — Router

First-read router for agents on **How To Be Human** (isometric tower-defence; you
spend *love* to unlock tiles and place musicians/defenders that protect "the
hole" from enemy waves). This file stays slim: it routes you to ONE domain doc.
Deep dive → `AI_REFERENCE.md`. Original full reference → `docs/legacy/CLAUDE_original.md`.

## Project Identity & Fast Start
- **Engine:** pygame-ce (Python 3). **Run:** `py main.py` (from this dir;
  `main.py` resolves paths then calls `src.core.game.Game().run()`).
- **Deps:** `pip install -r requirements.txt`. **Build exe:** `build.bat`
  (PyInstaller via `HowToBeHuman.spec`; output in `dist/`).
- **No formal test suite.** Verify with the headless smoke test below.

## Headless Smoke Test (run after every Python/JSON edit)
Forces SDL dummy drivers so the game boots with no window:
```
$env:SDL_VIDEODRIVER='dummy'; $env:SDL_AUDIODRIVER='dummy'; py -c "import balancing as B; import src.core.game as g; game = g.Game(); print('OK', B.STARTING_CURRENCY)"
```
Confirms imports resolve, all 5 `Balancing_*.json` overrides load, and `Game()`
constructs. **State what you actually verified** — if you only ran the smoke
test (not a live GUI round) or only read code statically, say so.

## Step 1 — Classify the task, then read ONE domain doc
Classify by **domain** (buildings / enemies / map / ui / core) and **task type**
(visual / bug fix / tweak / new feature). Then read ONLY that domain's doc and
edit ONLY that domain's file scope:

| Domain    | Read this doc            | May edit (file scope)                                                                                          |
|-----------|--------------------------|----------------------------------------------------------------------------------------------------------------|
| buildings | `src/buildings/CLAUDE.md`| `src/buildings/**`, `balancing/balancing_buildings.py`, `balancing/Balancing_Buildings.json`, named building regions of `game.py`/`building_ui.py` |
| enemies   | `src/enemies/CLAUDE.md`  | `src/enemies/**`, `balancing/balancing_enemies.py`, `balancing/Balancing_Enemies.json`, named spawn/scale regions of `game.py`      |
| map       | `src/map/CLAUDE.md`      | `src/map/**` (tile.py, tile_map.py, pathfinder.py, camera.py), `balancing/balancing_map.py`, `balancing/Balancing_Map.json`        |
| ui        | `src/ui/CLAUDE.md`       | `src/ui/**`, `src/effects.py`, `balancing/balancing_ui.py`, `balancing/Balancing_UI.json`                                           |
| core      | `src/core/CLAUDE.md`     | `src/core/**` (game.py, constants.py, sprite_gen.py), `balancing/balancing_core.py`, `balancing/Balancing_Core.json`               |

`game.py` is genuinely shared (placement, spawning, phase logic live there). The
scope hook enforces **file** scope, not region scope — so each domain doc names
the exact `game.py` functions/sections that domain may touch; do not edit other
regions. **If a task truly spans two domains, tell the user** — they decide
whether you read both docs.
Branch + Lock Protocol: every task should follow branch lock protocol based on the classification of the task

## Balance source of truth (read before quoting/editing balance)
Each `Balancing_<Domain>.json` **overrides** its `balancing_<domain>.py` at
runtime. Read the JSON for the authoritative live value. Change a value in
**both** the domain `.py` and the same-domain `.json` (override only applies to
keys already defined in the `.py`). `import balancing as B` (the frozen
aggregator) still exposes every name. ×10 HP/DMG combat scale still applies
(BASE_HP is the exception, stays 10).

## Step 2 — Universal exit gate (identical for every domain)
1. Run the smoke test → report exactly what you verified.
2. If balance changed: diff the domain `.py` vs its `.json`, report agreement.
3. If anything architectural changed: update **the domain CLAUDE.md** — NOT this
   router, NOT another domain's doc (this is how we avoid doc merge conflicts).
4. On the user's confirmation: commit (brief msg) → push → open PR.

## Branch + lock protocol (full detail in `.claude/commands/`)
- Default session start = `/start-domain <domain>`: pull `claudeprototype`, set
  that domain's `Balancing_*.json` `_lock` → `"LOCKED"`, push, create/switch
  `feature<Domain>`, write `.claude/active_domain`.
- `/resume-domain <domain>` just switches to the existing feature branch.
- `/finish-domain` runs the gate then (on confirm) commits/pushes/opens the PR.
- `/merge-domain <domain>` is the ONLY place the lock clears (`_lock` →
  `"UNLOCKED"`) — at merge time.
- **Invariant:** while a `feature<Domain>` branch exists, that domain's JSON
  `_lock` stays `"LOCKED"`.
- **Never run destructive git on uncommitted work** (also deny-listed): no
  `git reset --hard`, `git clean`, `git checkout -- <file>`, force-push.


---

## src/buildings/CLAUDE.md

# CLAUDE.md — BUILDINGS domain

Self-contained guide for the **buildings** domain. You reached here from the root
router after classifying the task. Edit only this domain's file scope.

**When you change buildings architecture/conventions, update THIS doc** (not the
root router, not another domain's doc).

## File scope you may edit
- `src/buildings/**`
- `balancing/balancing_buildings.py` + `balancing/Balancing_Buildings.json` (this domain's balance pair)
- Named building regions of `src/core/game.py` and `src/ui/building_ui.py` (below)

## Balance ownership & rules
- This domain owns: all `*_BUILDING_TIERS` (defence/economic/aoe/painter/sun_scorcher),
  their flat seed/shim constants (`AOE_DEF_*`, `PAINTER_*`, `SUN_SCORCHER_*`,
  `DEFENCE_MIN_ATTACK_SPEED`, `*_COST` shims, `building_tiers()`), and `RANDOM_NAMES`
  + `add_random_name` / `_save_random_names` (building renaming).
- `balancing/Balancing_Buildings.json` **overrides** `balancing/balancing_buildings.py` at runtime —
  read the JSON for the live value. Change values in **both** and keep them in sync
  (override only applies to keys already defined in the `.py`).
- **×10 combat scale:** all building HP/DMG values are ×10 (a "1 HP/1 DMG" unit
  reads as 10). NOT scaled: yields, payouts, costs, upkeep, speeds, ranges, radii.
- Derived shims (`DEFENCE_COST` etc.) read tier-1 `build_cost` **after** the JSON
  load, so overrides flow through. `building_tiers(type)` is the accessor.

## Building system conventions
- Base class `src/buildings/building.py` (`Building`): tier/level logic (`upgrade`,
  `advance_tier`, `at_tier_max`, `has_next_tier`), the `IS_COMBAT` flag, `upkeep()`.
- Expected methods on a building type: `update_stats_from_tier`, `current_stats()`,
  `stats_preview()`, `_render_alive(surf, sprites, tx, ty)` (override; `render`
  handles the destroyed sprite), `_sprite_key`, `upgrade_cost()`, and
  `update(dt, enemies, tilemap)` ONLY for combat buildings (no-op by default).
- **Placement must go through `game.py:Game.place_building()`** — never set
  `tile.building` directly. It is the single source of truth for type-unlock gating
  (returns `False` if the type is locked).
- `upkeep()` is duck-typed (love drained per income phase; 0 = free). Income is
  duck-typed too: any alive building with positive `yield_amount` is paid.

### Add a new building (pattern)
1. Subclass `Building` (`building_type = "<key>"`, `_default_type_name`).
2. Implement the expected methods above (+ `update` if combat → set `IS_COMBAT=True`).
3. Add a tier list in `balancing/balancing_buildings.py`, wire into `building_tiers()`; mirror
   in `balancing/Balancing_Buildings.json`.
4. Construct it in `Game.place_building` (the only legal placement path).
5. Add a CONSTRUCT spec/handling in `src/ui/building_ui.py` (`_CONSTRUCT_SPECS`,
   `_construct_availability`, `open_construct`/`_handle_construct`/`_draw_construct`).
6. Add a pathfinding weight (that lives in the **map** domain — coordinate if the
   enemy must treat its tile specially) and a branch in `Tile.pathfinding_weight`.
7. Update THIS doc.

## Current building keys (`building_type`)
- `base` — `BaseBuilding` ("The Hole"); not buildable/upgradeable, pathfinder goal.
  Lives-mode display logic + win/loss tuning is **core**, not buildings.
- `economic` — `EconomicBuilding`; **Flute Player → Harp Player → Trio**.
- `defence` — `DefenceBuilding`; **Stone Thrower → Slinger → Pistoleer**.
- `aoe_defence` — `AOEDefenceBuilding` ("Maw Mortar → Maw Catapult → Maw Cannon").
  **Locked at start**; level-up reward "Unlock Maw Mortar". Arcing shell to a fixed
  ground point, splashes `aoe_radius`. `IS_COMBAT=True`.
- `painter` — `PainterBuilding` ("Cave Painter → Maestro → Art Factory"). **Locked.**
  Risky economy: `yield_amount=0`, accrues `progress` per surviving round-end, pays a
  lump sum at `rounds_to_payout`, removes itself + frees the tile (added to
  `Game.used_painter_tiles`, never re-hostable). Dying before payout resets progress.
  Progress/payout logic = `game.py:_process_painters` (in `_begin_income_phase`,
  BEFORE the revive sweep).
- `sun_scorcher` — `SunScorcherBuilding` ("Sun Scorcher → Radiant Beam → Laser Beam").
  Subclasses `DefenceBuilding` (`IS_COMBAT=True`). **Locked + ERA-gated** (tier-1
  `era_unlock_round=15`). Ramping instant-damage beam (own `_MIN_TICK` floor, NOT
  `DEFENCE_MIN_ATTACK_SPEED`); ramp grows on same target, resets on any target change.
  Targets highest-HP enemy in Chebyshev range. Drawn via `render_projectiles` hook.

## The three stacking gates (locked content must be gated in BOTH UI and logic)
1. **Type-unlock:** `Game.unlocked_buildings` gates whether a type can be built —
   enforced in `Game.place_building` (single source of truth) AND `building_ui`
   (disabled construct button). `kind='unlock_building'` level-up reward flips it.
2. **Era gate (round-based, type-level):** tier-1 `era_unlock_round` excludes the
   whole type from the level-up pool until `round_num >= era_unlock_round`. PRIMARY
   gate in `Game._roll_levelup_options`; `building_ui._construct_availability` mirrors
   it as a safeguard. Read via `Game._era_unlock_round(btype)`.
3. **Per-tier round gate:** each tier's `unlock_min_round` keeps the tier out of the
   pool (and fully hidden in the upgrade panel: `NEXT TIER LOCKED`) until
   `round_num >= unlock_min_round`. `Game._tier_offerable`; `building_ui._upgrade_state`
   modes: `in_tier`/`tier_upgrade`/`tier_locked`/`tier_hidden`/`max_tier`.
Tier research is also gated globally per type (`defence_tiers_unlocked` etc.) on
levelup, read via `Game.tiers_unlocked_for`. These gates stack.

## game.py regions this domain may touch
`place_building`, `_process_painters`, the building branches of `_roll_levelup_options`
/ `_apply_levelup_option` / `_resolve_levelup`, per-type tier counters
(`*_tiers_unlocked`), and building-construct hooks. Do NOT edit phase-loop,
enemy-spawn, income-sweep ordering, or render orchestration (those are core).

## Verify before finishing
Smoke test (router). Confirm `Game.place_building()` still constructs new types;
construct/upgrade UI in `building_ui.py`; locked content gated in BOTH UI + logic;
`balancing/balancing_buildings.py` and `balancing/Balancing_Buildings.json` agree on changed keys.


---

## src/core/CLAUDE.md

# CLAUDE.md — CORE domain

Self-contained guide for the **core** domain — the game loop, phase logic, income,
levelup, render orchestration, procedural art, geometry constants, and any service
to the other pillars. You reached here from the root router. Edit only this scope.

**When you change core architecture/conventions, update THIS doc** (not the root
router, not another domain's doc).

## File scope you may edit
- `src/core/**` — `game.py` (the `Game` god-object), `constants.py` (geometry/enums/
  colors), `sprite_gen.py` (procedural sprites).
- `balancing/balancing_core.py` + `balancing/Balancing_Core.json` (this domain's balance pair)

(These three files were moved from loose `src/` into `src/core/`; imports are
`from src.core.<mod>`. `main.py` calls `src.core.game.Game().run()`.)

NOTE: `game.py` is genuinely shared. Buildings/enemies/ui docs name the specific
`game.py` regions those domains may touch. As the core domain you own the rest:
phase transitions, the main loop, income/payday, levelup roll/apply, render
orchestration, combat sweep, and the base/Hole win-loss logic.

## Balance ownership & rules
- This domain owns: `STARTING_CURRENCY`, `GAME_SCALE_ROUNDS`, `SPEED_*_MIN_ROUND`,
  phase timers (`ROUND_END_DELAY`, `INCOME_PHASE_DURATION`), all XP/village keys,
  `LEVELUP_LOVE_REWARD`, and the base/Hole keys (`BASE_HP`, `BASE_INCOME`,
  `BASE_KILLS_ENEMIES`, `BASE_LIVES_MODE`, `BASE_LIVES`, `BUILDING_REVIVE`).
- `balancing/Balancing_Core.json` **overrides** `balancing/balancing_core.py` at runtime — read the JSON
  for the live value; change both and keep in sync.
- **×10 combat scale** applies to combat HP/DMG generally; `BASE_HP` is the
  deliberate exception (the Hole stays 10, NOT scaled). Yields/costs/timers unscaled.

## Geometry & constants (`constants.py`)
ONE coordinate system everywhere (shared with the map domain). All geometry is driven
by constants here: `MAP_COLS/ROWS`, `BASE_COL/ROW`, tile pitch (`TILE_W/H/HW/HH`),
zone ring maxima (`COMBAT_RING_MAX`, `SPAWN_RING_MAX`), screen sizes, colors, and the
`GameState`/`GamePhase`/`TileState` enums. **Change the constants, not the logic** —
nothing geometric is hardcoded outside this file.

## Phases (`GamePhase`; transitions in `Game._update_gameplay`)
- **BUILDING** — player-driven, no timer. Tile click → `_handle_tile_click` → opens
  `building_ui`. End via HUD "end turn" → `_begin_enemy_phase`.
- **ENEMY** — `_update_enemy_phase`: spawns from `_spawn_queue`, moves enemies, runs
  combat-building `update`, awards XP per kill, ends when queue + enemies empty →
  `_begin_round_end`. **Base hit:** HP mode → Hole takes `e.dmg`, game-over at 0;
  **lives mode** (`BASE_LIVES_MODE`, default on) → costs ONE life (`Game.base_lives`),
  instantly clears all enemies + queue and ends the round; game-over at 0 lives.
- **ROUND_END** — short `ROUND_END_DELAY`. Pending levelup → `_begin_levelup`; else →
  `_begin_income_phase`.
- **LEVELUP** — fully modal (`levelup_window` owns input). `_resolve_levelup` applies
  the choice, advances village level, proceeds to income.
- **INCOME ("PAYDAY")** — `_begin_income_phase`, ordering matters:
  stat-snapshot → income (yields) → upkeep → `_process_painters` → **revive**
  (`BUILDING_REVIVE` rebuilds non-base buildings) → clear splatters → `round_num++`.
  Painters run BEFORE revive so a Painter that died this round isn't credited.

Key hooks: income/upkeep = `_begin_income_phase`; tower attacks =
`DefenceBuilding.update` (called in `_update_enemy_phase`); rebuild/heal =
`Building.rebuild()` (round end only); placement = `Game.place_building`.

## Combat speed control
ENEMY phase only. `Game.COMBAT_SPEEDS = (1.0, 1.5, 2.0, 0.0)` indexed by
`combat_speed_idx` (keys 1/2/3 or HUD `SpeedButton`s in ui). Index 3 = in-combat
pause (distinct from the Esc pause menu). The multiplier scales `dt` into
`_update_enemy_phase` only (UI/HUD use raw dt). `combat_speed_idx` persists across
waves (reset only in `_start_new_game`). 1.5×/2× gated by `SPEED_*_MIN_ROUND`.

## Combat conventions (core sweep)
`_update_enemy_phase` sweeps built tiles by the **`IS_COMBAT` class flag**, NOT by
hardcoding `building_type`. New combat types only need `IS_COMBAT=True` + an
`update(dt, enemies, tilemap)`. Range highlighting (`Game._highlight_range`) is gated
on `hasattr(building, 'range_tiles')` — type-agnostic, Chebyshev distance. Projectiles
render via the duck-typed `render_projectiles` hook; AOE shells lock onto a fixed
ground point at fire time (target dying mid-flight cannot crash).

## XP / levelup (core)
XP per kill via `_xp_for_enemy` (`XP_PER_*`); village thresholds from
`VILLAGE_XP_*`. Options rolled in `_roll_levelup_options` and applied in
`_apply_levelup_option`. Rewards unlock content only **when selected**. The three
stacking content gates (type-unlock / era / per-tier round) are described in the
buildings doc but enforced PRIMARILY here in `_roll_levelup_options`.

## Rendering / sprites (`sprite_gen.py`)
All sprites procedurally generated at startup into `Game.sprites` (string keys).
Tier keys `f"{prefix}_t{tier+1}_lvl{level}"`; animated GIF units load via
`_load_gif_frames` into `*_frames`. Background art sliced/loaded here too. Lives-mode
faces `_life_face(state)` → `life_face_{happy,determined,angry,crashout,lost}`. Enemy
collection sliced by `_slice_collection` into `enemy_stages`/`raider_stages`. Match
the existing pixel/iso style; avoid heavy asset-loading systems unless asked.

## Verify before finishing
Smoke test (router) — `Game()` exercises construct, phases setup, and sprite_gen.
For phase/income/levelup changes, prefer a live `py main.py` round and say so.
Confirm `balancing/balancing_core.py` and `balancing/Balancing_Core.json` agree on changed keys; state
whether you ran the smoke test, a live GUI round, or only checked statically.


---

## src/enemies/CLAUDE.md

# CLAUDE.md — ENEMIES domain

Self-contained guide for the **enemies** domain. You reached here from the root
router after classifying the task. Edit only this domain's file scope.

**When you change enemy architecture/conventions, update THIS doc** (not the root
router, not another domain's doc).

## File scope you may edit
- `src/enemies/**` — `enemy.py` (base), `raider.py`, `siege_cannon.py`
- `balancing/balancing_enemies.py` + `balancing/Balancing_Enemies.json` (this domain's balance pair)
- Named spawn/scale regions of `src/core/game.py` (below)

## Balance ownership & rules
- This domain owns: `ENEMY_*`, `RAIDER_*`, `SIEGE_*`, `BASE_ENEMY_COUNT`,
  `ENEMIES_PER_ROUND`, `ENEMY_SPAWN_INTERVAL`, `SPAWN_RAMP_*`,
  `ENEMY_SCALE_EVERY_N_LEVELS`, `ENEMY_SCALE_TIERS`.
- `balancing/Balancing_Enemies.json` **overrides** `balancing/balancing_enemies.py` at runtime — read the
  JSON for the live value; change both and keep them in sync.
- **×10 combat scale:** all enemy HP/DMG (incl. `ENEMY_SCALE_TIERS` `hp`/`dmg`) are
  ×10. NOT scaled: speeds, ranges, spawn intervals, counts.

## Enemy conventions
- Base class `enemy.py:Enemy`. Each enemy computes its path **once at spawn**
  (`find_path` in `__init__`, from the **map** domain's `pathfinder.py`); weights are
  read live, so building/tile changes are reflected next wave. There is **no global
  path cache** — if you change geometry mid-wave, recompute per-enemy paths yourself.
- Variants exist: `find_path_to_nearest_economic` (raiders) /
  `find_path_to_nearest_defence` (siege) target buildings before the base.
- **Base hit** is handled in `game.py:_update_enemy_phase` (lives vs HP mode) — that
  is core logic; this domain defines the enemy that deals the hit, not the response.

### Enemy scaling / stage / tier
- An enemy's tier = sprite stage = `(round_num-1) // ENEMY_SCALE_EVERY_N_LEVELS`
  (currently every 7–8 rounds), passed to all enemy types in `_update_enemy_phase`.
- Stat bonuses come from `ENEMY_SCALE_TIERS` (cumulative flat deltas; 5 entries —
  one per sprite-stage step). **Stats cap at the last tier** while the sprite stage
  keeps advancing to its max. Raiders also scale by tier.
- `Enemy._stage_idx = min(tier, _num_stages-1)`. Sprite stages 1 & 4 have two colour
  variants picked 50/50 via `Enemy._variant` (see Rendering in core/ui).

### Add a new enemy (pattern)
1. Subclass `Enemy` in `src/enemies/`.
2. Add stats to `balancing/balancing_enemies.py` (count/start-round/HP/dmg/speed) + JSON mirror.
3. Queue it in `game.py:_begin_enemy_phase` and instantiate in `_update_enemy_phase`.
4. Add an XP value (`XP_PER_*`, which lives in **core** balance) + a branch in
   `Game._xp_for_enemy` — coordinate that XP value with the core domain.
5. Sprites: set a `_stage_key` into a collection (`enemy_stages`/`raider_stages`) or
   set `_stage_key=None` and use a procedural `_sprite_key` (sprite_gen is **core**).

## Current enemy types
- standard `Enemy` — `enemy_stages` (6 stages).
- `Raider` — fast/fragile; `_stage_key="raider_stages"` (5 stages); targets economy
  buildings first. Starts at `RAIDER_START_ROUND`.
- `SiegeCannon` — slow/heavy; `_stage_key=None` (keeps procedural sprite); targets
  defence buildings first. Lead-spawned at the queue front (`SIEGE_QUEUE_LEAD_COUNT`),
  then mixed in (`SIEGE_MIX_RATIO`).

## game.py regions this domain may touch
`_begin_enemy_phase` (spawn queue: standard + raiders + leading siege cannons,
tier-scaled), the enemy-instantiation/scaling parts of `_update_enemy_phase`, and
`_xp_for_enemy`. Do NOT edit income/payday, levelup, placement, or render
orchestration (core), nor pathfinding weights (map).

## Verify before finishing
Smoke test (router). Confirm the spawn queue still builds and enemies instantiate;
`balancing/balancing_enemies.py` and `balancing/Balancing_Enemies.json` agree on changed keys; state
whether you ran the smoke test or only checked statically.


---

## src/map/CLAUDE.md

# CLAUDE.md — MAP domain

Self-contained guide for the **map** domain. You reached here from the root router
after classifying the task. Edit only this domain's file scope.

**When you change map architecture/conventions, update THIS doc** (not the root
router, not another domain's doc).

## File scope you may edit
- `src/map/**` — `tile.py`, `tile_map.py`, `pathfinder.py`, `camera.py`
- `balancing/balancing_map.py` + `balancing/Balancing_Map.json` (this domain's balance pair)

(These four files were moved from loose `src/` into `src/map/` during the context
restructure; all imports are `from src.map.<mod>`.)

## Balance ownership & rules
- This domain owns: `BASE_UNLOCK_COST`, `UNLOCK_COST_DISTANCE_MOD`,
  `ADJACENT_UNLOCK_ONLY`, all `PF_WEIGHT_*`.
- `balancing/Balancing_Map.json` **overrides** `balancing/balancing_map.py` at runtime — read the JSON
  for the live value; change both and keep them in sync.
- Geometry (grid dims, zone ring maxima, tile pitch) lives in `src/core/constants.py`
  (the **core** domain), NOT here. Change the constants, not the logic.

## One coordinate system everywhere
Grid arrays, pathfinding, spawning, rendering, and mouse-picking ALL use the same
`(col, row)`. `tile.world_center()` and the inverse projection
(`DefenceBuilding._world_to_tile`) are the canonical transforms.
- Grid `MAP_COLS × MAP_ROWS` = 20×20. Base at `(BASE_COL, BASE_ROW)=(1,1)` (the
  pathfinder goal). Col 0 / row 0 are BACKGROUND. Both axes increase away from base.
- Playfield cols 1..19, rows 1..19; outside = BACKGROUND (impassable).

## Zones — nested square rings (`initial_tile_state` in `tile.py`)
Keyed on the Chebyshev ring `max(col,row)` from the base corner:
- BUILDABLE starting pocket cols 1–2/rows 1–2 (base tile is BUILT).
- **COMBAT** = inner square `ring <= COMBAT_RING_MAX (9)` minus the pocket.
- **SPAWNING** = 4-deep band `9 < ring <= SPAWN_RING_MAX (13)`.
- **BACKGROUND** = `ring > 13`. To resize, change `COMBAT_RING_MAX`/`SPAWN_RING_MAX`
  in core `constants.py` only.

## Zones recede dynamically (`tile_map.py`)
`do_unlock` converts a clicked 2×2 chunk COMBAT→BUILDABLE, then
`_recede_spawn_after_unlock` pushes the spawn band one 2×2 section outward: nearest
2×2 SPAWNING→COMBAT, then nearest 2×2 BACKGROUND behind it →SPAWNING. Never overwrites
BUILDABLE/BUILT/BASE. Degrades gracefully near the map edge (logs `[zone] …`, no
crash). Spawn tiles read live each wave (`spawning_tiles()`); enemies recompute paths
at spawn, so there is no cache to invalidate.

## Unlocking
- `TileMap.do_unlock` converts COMBAT→BUILDABLE in 2×2 chunks only; `can_unlock`
  enforces `ADJACENT_UNLOCK_ONLY`. Unlock never creates SPAWNING tiles.
- **Unlock cost** (`TileMap.unlock_cost`, mirrored by `building_ui._unlock_cost`):
  `BASE_UNLOCK_COST + (col_section + row_section) * UNLOCK_COST_DISTANCE_MOD` —
  Manhattan distance in 2×2 sections from the base pocket section `(0,0)`. Sections
  are `((col-1)//2, (row-1)//2)`.

## Pathfinding (`pathfinder.py`)
- Dijkstra to the base goal; variants `find_path_to_nearest_economic` /
  `find_path_to_nearest_defence` target a building before the base.
- Weights are resolved per-tile by `Tile.pathfinding_weight` (reads `PF_WEIGHT_*`
  live): economic tile = `PF_WEIGHT_ECONOMIC_BUILDING` (1), defence = 2, base = 0
  (goal), impassable = 999. Range/targeting uses **Chebyshev** distance
  (`max(|Δcol|,|Δrow|)`).
- If you add a building type that enemies must treat specially, add a branch in
  `Tile.pathfinding_weight` and a `PF_WEIGHT_*` here — coordinate with the buildings
  domain (which owns the building itself).

## camera.py
`camera.py` centres on the base; world-locked offsets pan the background. The zoom
switch (`GAME_SCALE_ROUNDS`) is core balance.

## Verify before finishing
Smoke test (router) — `Game()` builds the `_grid`, base placement, and zones at
construct time, so a clean boot exercises this domain. Confirm `balancing/balancing_map.py`
and `balancing/Balancing_Map.json` agree on changed keys; state whether you ran the smoke test
or only checked statically.


---

## src/ui/CLAUDE.md

# CLAUDE.md — UI domain

Self-contained guide for the **ui** domain. You reached here from the root router
after classifying the task. Edit only this domain's file scope.

**When you change ui architecture/conventions, update THIS doc** (not the root
router, not another domain's doc).

## File scope you may edit
- `src/ui/**` — `building_ui.py`, `hud.py`, `levelup_window.py`, menus
  (`main_menu`, `pause_menu`, `settings_menu`, `credits_menu`, `add_name_menu`,
  `cheat_menu`), `game_log.py`, `game_over_screen.py`, `fonts.py`.
- `src/effects.py` — world-space visual effects (floaters). Effects ARE part of ui.
- `balancing/balancing_ui.py` + `balancing/Balancing_UI.json` (this domain's balance pair)

## Balance ownership & rules
- This domain owns: `NOT_ENOUGH_LOVE_DURATION`, `CONSTRUCT_SHOW_CANCEL`,
  `GORE_ENABLED`, `BG_ART_*`.
- `balancing/Balancing_UI.json` **overrides** `balancing/balancing_ui.py` at runtime — read the JSON for
  the live value; change both and keep them in sync.
- These are visual/timing toggles, not combat numbers — no ×10 scaling applies here.

## UI conventions
- **Construct/upgrade panel** = `building_ui.py`. It is **data-driven** from
  `BuildingUI._CONSTRUCT_SPECS`; `_construct_availability(btype, tile)` returns
  `(enabled, short_tag, hint)` so per-type gates (lock / used-tile / future era)
  show a disabled button + hint without bespoke code. Upgrade modes live in
  `_upgrade_state`: `in_tier`/`tier_upgrade`/`tier_locked`/`tier_hidden`/`max_tier`.
  When you add a buildable type, append a `_CONSTRUCT_SPECS` entry (the buildings
  domain owns the `place_building` branch — coordinate).
- **HUD** = `hud.py`: currency, round, end-turn, the four `SpeedButton`s (combat
  speed, ENEMY phase only; play/fast-forward/pause vector icons, gold highlight),
  and the top-left base display. In lives mode the HP bar is replaced by `BASE_LIVES`
  munchkin life-faces (mood by village level; see sprite keys below).
- **Levelup window** = `levelup_window.py`: fully modal, owns its own input; pulls
  names/explanations/costs out of `balancing`. It only presents — option rolling
  (`_roll_levelup_options`) and applying (`_apply_levelup_option`/`_resolve_levelup`)
  are **core** game logic.
- **Floaters/effects** (`effects.py`): `IncomeFloater`, `XPFloater`,
  `PainterMessageFloater` — store camera-independent world coords, add the camera
  offset at render time (drawn on the GAME surface so they scale with zoom).
- **Settings menu** shows the Gore ON/OFF toggle **only when `GORE_ENABLED` is true**
  (master off ⇒ no gore, no toggle). `Game` sets `Enemy.gore_enabled = GORE_ENABLED
  and settings_menu.gore_on` each render.
- **Add-name window** uses `B.add_random_name` (that fn + `RANDOM_NAMES` are owned by
  the **buildings** domain balance; the UI just calls it).

## Sprite/render notes relevant to UI
- Sprites are procedurally generated at startup (sprite_gen is **core**); UI looks
  them up by string key. Life-face keys: `life_face_{happy,determined,angry,crashout,
  lost}` (used by the Hole's lives display + HUD).
- Background artwork (`BG_ART_*`) is drawn in `tile_map.py:render` (map domain) but
  its enable/file/offset toggles are UI balance.

## Cross-domain note
`building_ui.py` is shared with the buildings domain (it mirrors building gates as a
safeguard). Edit construct/HUD/menu/effects presentation here; do not change
placement legality, gate logic, or income/levelup rules (those are buildings/core).

## Verify before finishing
Smoke test (router) boots the UI subsystems at construct time. For visual changes
that need a live window, run `py main.py` and say so. Confirm `balancing/balancing_ui.py` and
`balancing/Balancing_UI.json` agree on changed keys; state whether you ran the smoke test, a
live GUI round, or only checked statically.


---


