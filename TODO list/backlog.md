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


## Cleared 2026-06-22 17:01

### Reminders / Bureaucracy & Chores

* [2026-06-16 16:40] Fly Home
* [2026-06-19 18:00] Dinner with parents

### HTBH / Producing

* Taiga update
* Call Fabian
  Guide: https://docs.google.com/document/d/1eC3m6qhfyt6CbJOwM38a8IP-FTneCkUwsVBTBO5-Nlg/edit

### HTBH / Design

* !Ideation: Tile conditions
* Traps Ideation

### HTBH / Claude Build

* See Attack speed in building stats
* GDD converter

### Addictive Media Agency

* Github Repo
* Addictive OS — Phase 0: Foundation
  Turn the AddictiveMedia repo into a real OS: root CLAUDE.md (voice, services, pricing), folder structure, _Brain Obsidian vault, connector checks, .gitignore. Done when a fresh Claude session answers "what's our medium consulting price?" and "draft a line in our voice" straight from CLAUDE.md. (Covers the old "Github Repo" item.)

### Admin

* Dashboard: Reminder System
* Call Jakob

### Bureaucracy & Chores

* !Buy birthday present for Jacob
  Get a gift for Jacob's birthday. Done when a present is purchased and ready to give.
* Fly Home

### Reminders / HTBH / Producing

* [2026-06-16 18:55] Call Fabian
* [2026-06-16 18:45] Call Jakob
* [2026-06-16 19:00] call Hendrik


## Cleared 2026-06-23 12:56

### HTBH / Design

* !XP cards: Finish GDD

### HTBH / Claude Build

* !Implement Tile Conditions
* !FIx Boost Range
  Boost buildings should be able to be placed anywhere, except in the area of effect of another boost building
* !Wall HP upgrade
  Upgrading the Wall Builder building from level 1 to 2 or 2 to 3 currently only increases the building's own HP. It should also upgrade the HP of all walls it manages. Make wall HP scale with the building's level and not only scale with the tier. Done when upgrading the Wall Builder visibly increases wall HP, displayed also in green on hover just like all other stats.
* !Active Abilities
* !bloodstains only get cleared on end turn
  Blood stains left by dead enemies are currently cleared at the end of the combat phase. Change this so they persist and are only cleared at the end of the following turn when the player presses End Turn — so they carry over into the next round and players can see where enemies fell. Done when blood stains survive into the next round and disappear only on the subsequent End Turn press.
* !Xp from dead buildings
  When a building is destroyed, it should grant the player XP. The amount should be balanceable per building type, with a default of 1 XP per building. Done when buildings drop XP on death and the per-building XP value is exposed in the balancing config.
* !Story Upgrades
* !Blank Cutscenes
* !Xp from lost rounds
  When a round is lost, any enemies that were in the queue but never spawned should still award XP as if they had entered and died — so losing a round does not put the player at an XP disadvantage. Done when the rule is implemented and the XP amount matches what would have been awarded normally.
* !Meditator unlockable and Balanceable
  The meditator needs to be added to the unlock system and to the balancing gui in the same way as all the other buildings
* !Scaling Blocker
  The Blocker should be scaleable with tiers just like any other building it should start with 500 HP and then should scale Hp with upgrades
* !hover income
  Update inome from story upgrades, hover income  to show sources by building type
* Meditator bug
* Blocker Crash

### HTBH / Balancing

* !Higher wall hp
* !Adjust Unlock Pool Levels
  Adjust Unlock Pool Levels for All tiers of all buildings


## Cleared 2026-06-23 20:01

### HTBH / Claude Build

* Balancing GUI: Left panel category tree
  Replace the flat category list on the left with a hierarchical tree: top level = category (e.g. Buildings), second = sub-type (e.g. Defense/Economy), third = individual building names. Clicking a leaf scrolls/filters to that building. Done when the full tree is rendered and navigable.
* Make Balancing Config history get cloned to the build version
* Scale Base Income Per XPLevel
  Scale the basic 5 income the player gets by 2 each level each time the player levels up
* !Fix Damage and yield Update from boss Upgrades
  A bunch of Boss Upgrades are broken, they both dont visually show the effect in the UI nor is the effect in game for Upgrade Boss1A, Boss2AandB, but it is working for:Boss3A+B
* !UI Rework
  Make the placeholder rendered UI look exactly like the Provided mocks. Analyse the pixels. follow the exact colors, also make sure it is legible and understandable
* !Lightning strike AOE feedback
  Give AOE feedback exactly like the mortar
* !Blocker Unlockable
* !Moving background
  The background moves a bit in relation to the tiles when you move the camera,
* !Range Visual Not displayed when placed on mountain
  The defence buildings Range Visual is Not being displayed when placed on mountain
* !Boss Bar Bug
  Doesnt Go away if the boss isnt killed - needs to be cleared in payday phase
* !Enemy Attack FX
* !Asset Integrator

### HTBH / Balancing

* Sunscorch nerf + pricier upgrade
  Sunscorch generally too strong; upgrade cost needs to go up
* !slightly higher stone thrower hp
* Make Lightning weaker
* !Fabian - Less Enemies with Bosses
* !Fabian - Less enemy scaling
* !Fabian - More enemy scaling in later eras


## Cleared 2026-06-24 01:59

### HTBH / Producing

* !WBS update
  Check if the WBS still matches the planned scope of the game
* !WBS full tasks
* !HtbH Vert Slice Presentation
* !HtbH Vert Slice Delivs Zip

### HTBH / Claude Build

* Hover TileConditions in UpgradeUi
  in the upgrade Ui, hovering the tileconditions should show what they do
* !Tiles Art
* !Flute Player Art
* !Mortar Art
* !Walls thicker and color represented
  Walls should become thicker with each upgrade and meaningfully thicker on the levelups, they should always be behind buildings, they should also match the color of the type of wall they have
* !Boosters percentages
  Boosters should be percentage based, giving 1% more dmg or whatever per turn rather than 1 damage
* !Stats Should be visible in UI
  Right now the Building Ui is too bright for the text, make the text darker so you can read it
* !Building Placement FX
  Everytime you place a building, make a a little golden highlight on the tile and somesparks. also sparks when it levels up, more when it levels up a second time, and then full building vfx with the tile gold highlight when the tier is upgraded.
* !Building Death FX
  WHen a building dies, it needs purple rubble to fall apart and then disappear
* !Hide HP Bars
  HP bars should be hidden until the HP is under 100
* !Fix Buildings Pausing
  Buildings pause at the end of combat phase


## Cleared 2026-07-13 08:27

### HTBH / Producing

* !WBS content Timeline
* !Art Plan

### HTBH / Claude Build

* Balancing GUI: Fix build/editor version label
  The GUI currently misidentifies the editor version as a build version. Find the version detection logic and correct it. Done when the label accurately shows "Editor" in Godot editor and "Build" in exported builds.
* Balancing GUI: Collapsible items within categories
  Buildings and entries inside each category should be individually collapsible/expandable so you can focus on one at a time. State persists within session. Done when each entry can be collapsed to its header and re-expanded.
* Balancing GUI: Visual polish
  General UI refresh — spacing, typography, color palette, card styling, hover states. Current look is too raw. Done when it looks like a tool you'd actually want to use.
* Balancing GUI: Value categories within each building
  Group each building's config values into logical sub-categories (e.g. Combat, Economy, Visual, Costs) instead of one flat list. Done when all building values are organized into named groups with visual separators.
* Balancing GUI cleanup
* !New Repo
* !Engine
* !Editor
* !migrate game to drunkenrobot engine - phase 9, First playable
* balancing session history in editor
* !Tile Unlock Lag
  Tile Unlock Lag
* Enemy Spawning Lag
  Lag for each enemy towards the end of the spawn queue after round 12
* Bug: Tile Unlock Cost
  Tile costs increase as they get further away from the base, if its in the wrong direction
* Bug: Enemies walk on background tiles

### HTBH / Balancing

* Levelling too Fast: Sheets Predictions not accurate

### Addictive Media Agency

* Organize Tazio & Keanu Meeting

### Bureaucracy & Chores

* Dinner with parents

### HTBH / Claude Visuals

* Background Art


## Cleared 2026-07-14 08:16

### HTBH / Claude Build

* Fullscreen Mode
  Full screen mode is currently broken on various resolutions. Fix it so the game runs correctly at any screen resolution without layout issues, clipping, or scaling errors. Done when full screen works reliably across all tested resolutions.
* !^migrate game to drunkenrobot engine - phase 10, feature layering
  follow migration plan, phase 10
* !buttons behind construction screen
  the pause and the end turn button should be BEHIND the building construction/tileunlocking/building upgrade UI screen, but it is not, those buttons should disappear and not be clickable when those screens are open
* !Lightning Does no Damage
* Enemy HP bars
* !^Enemy Grouping

### Admin

* Dashboard: Click and drag movable tasks
* Be able to change time on the reminders
* !Major Big Tasks and minor tasks
* !Seperate HtbH Engine and HtbH Claude Art Categories


## Cleared 2026-07-15 11:06

### HTBH / Claude Build

* !Close Screens with Right Click
  Must be able to close the build / unlock tile / upgrade screen by right clicking anywhere
* !Boss pathfinding fix
  Enemy Boss gets stuck on water tiles or mountains, and walks weird
* !^Enemy rework
* block underleveled buildings
  If a player unlocks a higher tier of a building, they can no longer place the now underleveled building and must pay a upfront cost for the higher tier version immediately. So if you unlock slinger, you can no longer place a stone thrower, but he immediately spawns as a slinger for a higher upfront cost which should be balanceable, then make the cost in the levelup screen always be the upfront purchase cost of building if it is a higher tier, or the initial purchase cost if it is lower tier
* reduce enemy height/ fix position of hp bars etc

### HTBH Engin Changes

* !^Redesign Test Suite
* !^Redesign Skills and Agents
* Plan doc org
* Functionality to Reuse Sprites
* Tickbox to turn off animations, so they revert to the first frame
* Make Balanceable if a building is unlocked at the start, and set a minimum pool time
* Engine Settings

