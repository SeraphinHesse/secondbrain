# To Do



!taskname = high importance task

##### Reminders

###### Bureaucracy & Chores


###### General
* [2026-06-11 18:00] Meeting with Kim
* [2026-06-13 22:00] Fly to Italy

###### HTBH
* [2026-06-11 17:00] Meet Johann
* [2026-06-09 23:38] Check if First Levelup Glitch fix ran
  (AOE_DEF_UNLOCK_MIN_VILLAGE_LEVEL: 2→1)




##### 

##### How to be Human

###### Producing

* WBS update
* WBS full tasks
* Taiga update
* Call Johann

* x !Sprint planning: art & tech
  Plan and assign sprint tasks for both the art team and for tech. Done when both teams have a full, prioritised sprint backlog ready to execute.

* x !Vertical slice roadmap & deliverables plan
  Define the milestone path to vertical slice: (1) a roadmap showing the phases and milestones needed to reach VS, and (2) a deliverables checklist scoped to VS. Done when both documents exist and tasks can be broken out from them.
* x !Agenda Planning

* Vertical Slice Deliverables Internal Presentation
  Prepare and deliver an internal presentation covering the vertical slice deliverables — what they are, current status, and what done looks like. Done when the team has a shared, aligned picture of VS scope and next steps.
* x !Internal Vert Slice Delivs Slides
  Make Slides presentation in the template to
* Steam Page Setup



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
* Come up with more generic upgrades
* Booster Limits Explanations
* Traps Ideation



###### Claude Build

* x !Range of building should update visually immediately on upgrade, not on the next select
  When upgrading a building, the range indicator stays at the old value until the building is deselected and reselected. Fix it so the range visualisation refreshes in-place the moment the upgrade is confirmed — especially important when range increases on upgrade.

* shift click to select multiple tiles of the same type
  Shift-clicking a tile should add it to a multi-selection, but only within the same category (build tiles, buildable tiles, or combat tiles — no mixing). Selecting a build tile locks the selection to build tiles only; selecting a buildable tile locks to buildable tiles, etc. A valid multi-selection then lets the player upgrade, build, or unlock all selected tiles in one action simultaneously.

* Maybe make the mortar shoot where the enemies will go? maybe put this on a bool in balancing
  Instead of firing at an enemy's current position, the Mortar predicts the enemy's movement vector and leads the shot so the projectile lands where the enemy will be. Expose a balancing toggle (bool) and a lead-factor scalar in the balancing GUI so the behaviour can be tuned or disabled.

* Range Impacts the pathfinding of the enemies
  Every tile covered by the attack range of a non-Mortar defence building (e.g. Stone Thrower, Sunscorch) should have its pathfinding tile weight increased by a configurable amount, making enemies prefer routes that avoid those tiles. They will still walk through covered tiles if forced, but will route around them otherwise. Add a global on/off toggle and a weight-increase scalar to the balancing GUI under the building/pathfinding section.


* x !First Levelup Glitch: First levelup only painter even though mortar should be available
  At the very first level-up (after round 0), only the Painter appears as an unlock option — the Mortar never shows up even though it should be available from round 0 onward. Investigate the unlock-pool logic that populates the three choices and fix whatever is filtering the Mortar out.

* x !Hole HP upgrade not available in lives mode
  The HP/hole-upgrade technology card is meaningless in lives mode (lives are tracked differently). Remove it from the upgrade pool when the game is running in lives mode so it never appears as a level-up option.
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
  https://docs.google.com/document/d/1KszfyyrXJBXUo8kMW9GGmMaiDflqj5JNKP8BPM0Cvow/edit?tab=t.0#heading=h.w6ikow374bm6

* Add Meditator building
  Economy building that generates yield each turn like the Musician. Core mechanic: a streak counter tracks consecutive undisturbed turns — each uninterrupted turn the yield increases (compounding). If the building is attacked or disturbed, the streak resets. Ties into the three-tier design (Meditator → Shaman → Sun Priest). Done when the building is placeable, upgradeable, and the streak/yield logic works correctly.

* !Add wall building
  Add walls as a placeable structure. Walls should block or redirect enemy pathing by acting as impassable (or high-weight) tiles in the pathfinding system. Done when a wall tile can be built, integrates with the existing tile-weight/pathfinding system, and enemies route around it.

* x !Add Boost buildings (4 aura support buildings)
  Four new support buildings that each emit a passive aura buffing all defense buildings in adjacent/surrounding tiles. One per stat: (1) Attack range boost, (2) HP boost, (3) Damage boost, (4) Attack speed boost. Buff values should be configurable in the balancing GUI. Done when all four are placeable, their auras apply correctly to nearby defense buildings, and buffs update dynamically when buildings are added/removed from range.
* Show died-last-round indicator
  In the per-creature damage stats, note whether it died last round
* See Attack speed in building stats
* Move Balancing GUI outside of balancing folder and cleanup root folder
* Boost building range visual representation
* !Add Blocker Building
  A high Hp building with (for now) the same pathfinding weight as econ building but significantly more hp. does nothing else, can be placed strategically to block the enemies path
* x !infinte money and unlock all tech cheat
* Make Balancing Config history get cloned to the build version
* FIx Boost Range
* Split Boost into 3 techs
* Painter Death Tile Blocking
  When the painter dies, the tile he was on becomes unusable
* Traps



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
* !Meet Simona
* !Meet Simona

* Research: Automate potential client list creation
  Investigate tools, APIs, and approaches for automatically generating qualified potential client lists for the agency. Could include LinkedIn scraping, Apollo/Hunter APIs, domain enrichment, etc. Done when there's a clear shortlist of viable approaches with pros/cons.

* Build: Client list automation tool
  Build the automation software based on the research above. Should output a structured list of potential clients (company, contact, fit score or similar). Done when the tool can run and produce a usable lead list with minimal manual input.

* Drunkin' Donuts: rebrand plan
  Create a full rebrand strategy document for the client currently operating under the name "Drunkin' Donuts." Cover new name options, visual identity direction, positioning, and rollout approach. Done when there's a concrete rebrand proposal ready to present.

* Drunkin' Donuts: How to be Human release roadmap & advertising plan
  Build a release roadmap and advertising strategy for Gio's (Drunkin' Donuts) "How to be Human" release. Cover pre-release, launch, and post-launch phases — channels, content, timelines, budget buckets. Done when there's a doc we can brief the client with.

* Sign Gio (Drunkin' Donuts) — brand agreement
  Figure out the right structure to sign Gio the rapper as a client and get a brand agreement in place. Define what the deal looks like — services, exclusivity, rev share or retainer — and what the approach is for getting him to sign. Done when we have a proposed deal structure and an outreach/signing plan.

* Cano meeting plan — VC + agency consulting/IT role
  Prepare for the meeting with Cano covering two angles: (1) VC conversation — what we're raising, for what, and what we want from him; (2) potential role for Cano doing sales, consulting, and IT outsourcing for Addictive Media, with emphasis on consulting and IT. Done when there's a clear agenda and talking points for both topics.

* Tatsu meeting plan — operations involvement
  Prep for meeting with Tatsu to explore him joining in an operations capacity. Define what the role could look like, what we'd need from him, and what we'd offer. Done when there's a clear agenda and a proposal outline ready.

* !Pay Chelsea for the website
  Invoice or direct payment to Chelsea for work done on the website. Confirm the amount owed, settle it, and keep a record. Done when Chelsea is paid and payment is documented.

* Regain access to Google account
  Unlock or recover access to the agency Google account. Work through whatever the current blocker is (2FA, recovery, account suspension). Done when we're fully logged in and operational again.



##### Admin

* Dashboard for secondbrain
* Dashboard: Reminder System
* Integrate dashboard calendar sync into morning routine
  Set up persistent 6:30am calendar → reminders sync: either configure Windows Task Scheduler to run sync-calendar-reminders.js (requires one-time Google OAuth token setup) or keep a Claude Code session open so the CronCreate job fires. Done when calendar events appear automatically in the dashboard Reminders sidebar every morning without any manual steps.
* Dashboard: Click and drag movable tasks
* Rework Morning Claude Routine
* x !Finish Dashboard Task Completion MD sync
* j



##### University





##### Bureaucracy \& Chores




##### Reminders

###### Admin



##### Reminders

###### Addictive Media Agency
* ![2026-06-11 13:30] Meet Simona

