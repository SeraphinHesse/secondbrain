# Backlog

## Cleared 2026-06-11 12:19

### HTBH / Producing

* !Sprint planning: art & tech
  Plan and assign sprint tasks for both the art team and for tech. Done when both teams have a full, prioritised sprint backlog ready to execute.
* !Vertical slice roadmap & deliverables plan
  Define the milestone path to vertical slice: (1) a roadmap showing the phases and milestones needed to reach VS, and (2) a deliverables checklist scoped to VS. Done when both documents exist and tasks can be broken out from them.
* !Agenda Planning
* !Internal Vert Slice Delivs Slides
  Make Slides presentation in the template to

### HTBH / Claude Build

* !Range of building should update visually immediately on upgrade, not on the next select
  When upgrading a building, the range indicator stays at the old value until the building is deselected and reselected. Fix it so the range visualisation refreshes in-place the moment the upgrade is confirmed — especially important when range increases on upgrade.
* !First Levelup Glitch: First levelup only painter even though mortar should be available
  At the very first level-up (after round 0), only the Painter appears as an unlock option — the Mortar never shows up even though it should be available from round 0 onward. Investigate the unlock-pool logic that populates the three choices and fix whatever is filtering the Mortar out.
* !Hole HP upgrade not available in lives mode
  The HP/hole-upgrade technology card is meaningless in lives mode (lives are tracked differently). Remove it from the upgrade pool when the game is running in lives mode so it never appears as a level-up option.
* !Add Boost buildings (4 aura support buildings)
  Four new support buildings that each emit a passive aura buffing all defense buildings in adjacent/surrounding tiles. One per stat: (1) Attack range boost, (2) HP boost, (3) Damage boost, (4) Attack speed boost. Buff values should be configurable in the balancing GUI. Done when all four are placeable, their auras apply correctly to nearby defense buildings, and buffs update dynamically when buildings are added/removed from range.
* !infinte money and unlock all tech cheat

### Admin

* !Finish Dashboard Task Completion MD sync


## Cleared 2026-06-11 13:24

### Reminders / HTBH

* [2026-06-09 23:38] Check if First Levelup Glitch fix ran
  (AOE_DEF_UNLOCK_MIN_VILLAGE_LEVEL: 2→1)

### HTBH / Producing

* Call Johann

### Addictive Media Agency

* !Meet Simona

### Reminders / Addictive Media Agency

* ![2026-06-11 13:30] Meet Simona


## Cleared 2026-06-11 13:27

### HTBH / Claude Build

* !Boss Enemy
  https://docs.google.com/document/d/1KszfyyrXJBXUo8kMW9GGmMaiDflqj5JNKP8BPM0Cvow/edit?tab=t.0#heading=h.w6ikow374bm6


## Cleared 2026-06-16 10:00

### Reminders / General

* [2026-06-13 22:00] Fly to Italy

### Reminders / HTBH

* [2026-06-11 17:00] Meet Johann

### HTBH / Producing

* Vertical Slice Deliverables Internal Presentation
  Prepare and deliver an internal presentation covering the vertical slice deliverables — what they are, current status, and what done looks like. Done when the team has a shared, aligned picture of VS scope and next steps.

### HTBH / Claude Build

* shift click to select multiple tiles of the same type
  Shift-clicking a tile should add it to a multi-selection, but only within the same category (build tiles, buildable tiles, or combat tiles — no mixing). Selecting a build tile locks the selection to build tiles only; selecting a buildable tile locks to buildable tiles, etc. A valid multi-selection then lets the player upgrade, build, or unlock all selected tiles in one action simultaneously.
* Maybe make the mortar shoot where the enemies will go? maybe put this on a bool in balancing
  Instead of firing at an enemy's current position, the Mortar predicts the enemy's movement vector and leads the shot so the projectile lands where the enemy will be. Expose a balancing toggle (bool) and a lead-factor scalar in the balancing GUI so the behaviour can be tuned or disabled.
* Range Impacts the pathfinding of the enemies
  Every tile covered by the attack range of a non-Mortar defence building (e.g. Stone Thrower, Sunscorch) should have its pathfinding tile weight increased by a configurable amount, making enemies prefer routes that avoid those tiles. They will still walk through covered tiles if forced, but will route around them otherwise. Add a global on/off toggle and a weight-increase scalar to the balancing GUI under the building/pathfinding section.
* Switch Button to Confirm construction with cancel
  WHen building buildings in the stat confirm window, Confirm should be on the right, cancel should be on the left switch these, then put a book into UIbalancing defaulted to true that is ConfirmOnRightSide
* Lives in base building UI
  Clicking the base building should show current lives in its info UI panel
* Tile weight reduction by damage
  After ~round 10, top 3 damage-dealing buildings reduce tile weights on their tiles; enemies more likely to path over them (feels like enemies target whoever hurt them most)
* Sunscorch beam scales visually
  Beam gets fatter each level; at laser beam tier it should be very fat and red
* Add Meditator building
  Economy building that generates yield each turn like the Musician. Core mechanic: a streak counter tracks consecutive undisturbed turns — each uninterrupted turn the yield increases (compounding). If the building is attacked or disturbed, the streak resets. Ties into the three-tier design (Meditator → Shaman → Sun Priest). Done when the building is placeable, upgradeable, and the streak/yield logic works correctly.
* !Add wall building
  Add walls as a placeable structure. Walls should block or redirect enemy pathing by acting as impassable (or high-weight) tiles in the pathfinding system. Done when a wall tile can be built, integrates with the existing tile-weight/pathfinding system, and enemies route around it.
* Show died-last-round indicator
  In the per-creature damage stats, note whether it died last round
* Boost building range visual representation
* !Add Blocker Building
  A high Hp building with (for now) the same pathfinding weight as econ building but significantly more hp. does nothing else, can be placed strategically to block the enemies path
* Painter Death Tile Blocking
  When the painter dies, the tile he was on becomes unusable
* Scrollable list of buildable buildings
* Boss healthbar needs to disappear
  When the boss isnt killed, but the round ends, (i.e. via cheating or via losing the round) the bosses healthbar remains on screen, this should disappear FOR SURE
* Map Mode: Building Range
  toggled by a button on the HUD, all ranges of all defence buildings should become visible at the same time
* Map Mode: Enemy heatmap
  toggled by a button on the HUD, a heatmap of enemy locations will be shown

### HTBH / Balancing

* Early game slightly too difficult (double check this?)
* Slinger too strong
* First levelup should be slightly later
* Flute player needs more HP
  Currently only has two hit points, needs a bump
* Musicians too strong
  Overall generating too much gold/income
* Harp too cheap/strong
  Harp player is either too cheap to build or generates too much yield (or both)
* Raise all building upkeep
  Upkeep across the board is too low
* Blocker too much HP

### Admin

* Dashboard for secondbrain
* !Make Automation an addable Category
* Call Jakob

### Reminders / Admin

* [2026-06-15 13:00] Call Jakob

