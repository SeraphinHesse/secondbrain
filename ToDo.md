# To Do



!taskname = high importance task

##### Reminders

###### Bureaucracy & Chores


###### HTBH




##### 

##### How to be Human

###### Producing

* WBS update
* WBS full tasks
* Taiga update
* Call Johann



###### Design

* Meditator Building: tier visual design
  Three-tier economy building. Tier 1 — "The Meditator": looks identical to the Flute Player but seated on a rock. Tier 2 — "The Shaman": seated on a partial temple structure, visibly levitating above it. Tier 3 — "The Sun Priest": god-like figure radiating sunlight with a giant temple beneath. Design all three art directions / sprites before implementation.

* XP cards: Finish GDD
* !Ideation: Tile conditions
* Ideation: More Boss types
* Ideation: More Enemy types
* Ideation: More Economy Buildings
* Ideation: More Defence Buildings
* Life loss feedback unclear
  When a life is lost nothing makes it clear; needs a fix
* Ideation: life loss display
  Options: animate the base, or have the enemy path back out of the base
* Show died-last-round indicator
  In the per-creature damage stats, note whether it died last round
* Move Balancing GUI outside of balancing folder and cleanup root folder



###### Claude Build

* !Update .gitignore for HTBH prototype section
* Range of building should update visually immediately on upgrade, not on the next select
  When upgrading a building, the range indicator stays at the old value until the building is deselected and reselected. Fix it so the range visualisation refreshes in-place the moment the upgrade is confirmed — especially important when range increases on upgrade.

* shift click to select multiple tiles of the same type
  Shift-clicking a tile should add it to a multi-selection, but only within the same category (build tiles, buildable tiles, or combat tiles — no mixing). Selecting a build tile locks the selection to build tiles only; selecting a buildable tile locks to buildable tiles, etc. A valid multi-selection then lets the player upgrade, build, or unlock all selected tiles in one action simultaneously.

* Maybe make the mortar shoot where the enemies will go? maybe put this on a bool in balancing
  Instead of firing at an enemy's current position, the Mortar predicts the enemy's movement vector and leads the shot so the projectile lands where the enemy will be. Expose a balancing toggle (bool) and a lead-factor scalar in the balancing GUI so the behaviour can be tuned or disabled.

* !Range Impacts the pathfinding of the enemies
  Every tile covered by the attack range of a non-Mortar defence building (e.g. Stone Thrower, Sunscorch) should have its pathfinding tile weight increased by a configurable amount, making enemies prefer routes that avoid those tiles. They will still walk through covered tiles if forced, but will route around them otherwise. Add a global on/off toggle and a weight-increase scalar to the balancing GUI under the building/pathfinding section.

* Infinite money cheat, unlock all tech cheat
  Add two entries to the cheats menu: one that gives the player infinite gold (or a very large lump sum), and one that unlocks all technology immediately. Both should be accessible from the existing cheats UI.

* !First Levelup Glitch: First levelup only painter even though mortar should be available
  At the very first level-up (after round 0), only the Painter appears as an unlock option — the Mortar never shows up even though it should be available from round 0 onward. Investigate the unlock-pool logic that populates the three choices and fix whatever is filtering the Mortar out.

* Hole HP upgrade not available in lives mode
  The HP/hole-upgrade technology card is meaningless in lives mode (lives are tracked differently). Remove it from the upgrade pool when the game is running in lives mode so it never appears as a level-up option.
* Come up with more generic upgrades
* Switch Button to Confirm construction with cancel
  WHen building buildings in the stat confirm window, Confirm should be on the right, cancel should be on the left switch these, then put a book into UIbalancing defaulted to true that is ConfirmOnRightSide
this should be toggleable in balancing gui
* Range and Building Preview on hover
* !Implement Tile Conditions
* Lives in base building UI
  Clicking the base building should show current lives in its info UI panel
* Tile weight reduction by damage
  After ~round 10, top 3 damage-dealing buildings reduce tile weights on their tiles; enemies more likely to path over them (feels like enemies target whoever hurt them most)
* Sunscorch beam scales visually
  Beam gets fatter each level; at laser beam tier it should be very fat and red
* !Boss Enemy

* Add Meditator building
  Economy building that generates yield each turn like the Musician. Core mechanic: a streak counter tracks consecutive undisturbed turns — each uninterrupted turn the yield increases (compounding). If the building is attacked or disturbed, the streak resets. Ties into the three-tier design (Meditator → Shaman → Sun Priest). Done when the building is placeable, upgradeable, and the streak/yield logic works correctly.

* Add wall building
  Add walls as a placeable structure. Walls should block or redirect enemy pathing by acting as impassable (or high-weight) tiles in the pathfinding system. Done when a wall tile can be built, integrates with the existing tile-weight/pathfinding system, and enemies route around it.



###### Balancing

* Early game slightly too difficult (double check this?)
* Slinger too strong
* Levelling too Fast: Sheets Predictions not accurate
* First levelup should be slightly later
* Flute player needs more HP
  Currently only has two hit points, needs a bump
* Musicians too strong
  Overall generating too much gold/income
* Harp too cheap/strong
  Harp player is either too cheap to build or generates too much yield (or both)
* Sunscorch nerf + pricier upgrade
  Sunscorch generally too strong; upgrade cost needs to go up
* Raise all building upkeep
  Upkeep across the board is too low



##### Addictive Media Agency





##### Admin

* Dashboard for secondbrain
* Dashboard: Reminder System
* Integrate dashboard calendar sync into morning routine
  Set up persistent 6:30am calendar → reminders sync: either configure Windows Task Scheduler to run sync-calendar-reminders.js (requires one-time Google OAuth token setup) or keep a Claude Code session open so the CronCreate job fires. Done when calendar events appear automatically in the dashboard Reminders sidebar every morning without any manual steps.



##### University





##### Bureaucracy \& Chores


