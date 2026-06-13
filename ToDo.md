# To Do



!taskname = high importance task

##### Reminders

###### Bureaucracy & Chores
* [2026-06-15 19:00] Get Laptop From kim


###### General
* [2026-06-13 22:00] Fly to Italy

###### HTBH
* [2026-06-11 17:00] Meet Johann




##### How to be Human

###### Producing

* WBS update
* WBS full tasks
* Taiga update



* x Vertical Slice Deliverables Internal Presentation
  Prepare and deliver an internal presentation covering the vertical slice deliverables — what they are, current status, and what done looks like. Done when the team has a shared, aligned picture of VS scope and next steps.
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


* shift click to select multiple tiles of the same type
  Shift-clicking a tile should add it to a multi-selection, but only within the same category (build tiles, buildable tiles, or combat tiles — no mixing). Selecting a build tile locks the selection to build tiles only; selecting a buildable tile locks to buildable tiles, etc. A valid multi-selection then lets the player upgrade, build, or unlock all selected tiles in one action simultaneously.

* Maybe make the mortar shoot where the enemies will go? maybe put this on a bool in balancing
  Instead of firing at an enemy's current position, the Mortar predicts the enemy's movement vector and leads the shot so the projectile lands where the enemy will be. Expose a balancing toggle (bool) and a lead-factor scalar in the balancing GUI so the behaviour can be tuned or disabled.

* Range Impacts the pathfinding of the enemies
  Every tile covered by the attack range of a non-Mortar defence building (e.g. Stone Thrower, Sunscorch) should have its pathfinding tile weight increased by a configurable amount, making enemies prefer routes that avoid those tiles. They will still walk through covered tiles if forced, but will route around them otherwise. Add a global on/off toggle and a weight-increase scalar to the balancing GUI under the building/pathfinding section.



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

* Add Meditator building
  Economy building that generates yield each turn like the Musician. Core mechanic: a streak counter tracks consecutive undisturbed turns — each uninterrupted turn the yield increases (compounding). If the building is attacked or disturbed, the streak resets. Ties into the three-tier design (Meditator → Shaman → Sun Priest). Done when the building is placeable, upgradeable, and the streak/yield logic works correctly.

* !Add wall building
  Add walls as a placeable structure. Walls should block or redirect enemy pathing by acting as impassable (or high-weight) tiles in the pathfinding system. Done when a wall tile can be built, integrates with the existing tile-weight/pathfinding system, and enemies route around it.

* Show died-last-round indicator
  In the per-creature damage stats, note whether it died last round
* See Attack speed in building stats
* Move Balancing GUI outside of balancing folder and cleanup root folder
* Boost building range visual representation
* !Add Blocker Building
  A high Hp building with (for now) the same pathfinding weight as econ building but significantly more hp. does nothing else, can be placed strategically to block the enemies path
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

* Keanu meeting plan — VC + agency consulting/IT role
  Prepare for the meeting with Cano covering two angles: (1) VC conversation — what we're raising, for what, and what we want from him; (2) potential role for Cano doing sales, consulting, and IT outsourcing for Addictive Media, with emphasis on consulting and IT. Done when there's a clear agenda and talking points for both topics.

* Tazio meeting plan — operations involvement
  Prep for meeting with Tatsu to explore him joining in an operations capacity. Define what the role could look like, what we'd need from him, and what we'd offer. Done when there's a clear agenda and a proposal outline ready.

* !Regain access to Google account
  Unlock or recover access to the agency Google account. Work through whatever the current blocker is (2FA, recovery, account suspension). Done when we're fully logged in and operational again.

* Regain access to Google account
  Unlock or recover access to the agency Google account. Work through whatever the current blocker is (2FA, recovery, account suspension). Done when we're fully logged in and operational again.
* Setup Addictive Task and Project Dashboard
* Tazio & Keanu Meeting
* Glasses Ideation
* Weib Automation and Pitch planning
* Github Repo

* Addictive OS — Phase 0: Foundation (IN PROGRESS)
  Turn the AddictiveMedia repo into a real OS: root CLAUDE.md (voice, services, pricing), folder structure, _Brain Obsidian vault, connector checks, .gitignore. Done when a fresh Claude session answers "what's our medium consulting price?" and "draft a line in our voice" straight from CLAUDE.md. (Covers the old "Github Repo" item.)
* Addictive OS — Phase 1: Agency Dashboard / OS
  Task/project/calendar management over the repo + onboard-client skill (one-command client setup). (Covers "Setup Addictive Task and Project Dashboard.")
* Addictive OS — Phase 2: Document & Reporting Engine
  Branded Templates + client-report skill wiring Windsor.ai data into on-brand PDF reports.
* Addictive OS — Phase 3: Outreach & Acquisition Engine
  Prospect research, outreach-draft + proposal skills, personalized micro-pitch generator.
* Addictive OS — Phase 4: Media-Buying & Optimization Automation
  weekly-sprint skill, scheduled ad-platform pulls, budget/anomaly alerts, case-study generator.
* Addictive OS — Phase 5: Productize & Expand
  Client websites, "convert your company to AI" consulting, Addictive OS as a productized service, Dashboard Stage 2 (server + mobile).
* !voice-guardian skill — tone deep-dive + anti-AI-slop research
  Deferred from Phase 0. Codify Addictive Media's real voice from the brand docs, then research anti-"AI-slop" techniques (banned phrases, burstiness, concrete-over-abstract, EN/DE register) so generated copy doesn't read as machine-written. Until done, founders approve all outward copy.
* Set up / authenticate Windsor.ai connector
  One-time auth for the Windsor.ai MCP (Meta/Google Ads data) so reporting + media automation can pull live ad data. Run authenticate → complete_authentication in a Claude session.



##### Claude Automation

* Research: Claude Code skills for frontend web design
  Survey and document useful Claude Code skills for frontend/web design work. Priority candidates: the built-in topic skill, the third-party "taste" skill (UI/UX Pro Max), and any library-focused skills. Done when there's a curated shortlist with install/use notes in `projects/claude-automation/`.

* Research: Cybersecurity for vibe coding
  Investigate security risks specific to AI-assisted rapid development (vibe coding). Cover common vulnerabilities in AI-generated code, relevant Claude Code skills or MCP tools for catching issues, and best practices for reviewing AI-generated code. Done when findings are documented in `projects/claude-automation/cybersecurity-vibe-coding-notes.md`.



##### Admin

* Dashboard for secondbrain
* Dashboard: Reminder System
* Integrate dashboard calendar sync into morning routine
  Set up persistent 6:30am calendar → reminders sync: either configure Windows Task Scheduler to run sync-calendar-reminders.js (requires one-time Google OAuth token setup) or keep a Claude Code session open so the CronCreate job fires. Done when calendar events appear automatically in the dashboard Reminders sidebar every morning without any manual steps.
* Dashboard: Click and drag movable tasks
* Rework Morning Claude Routine
* !Make Automation an addable Category



##### University





##### Bureaucracy \& Chores
* !Buy birthday present for Jacob
  Get a gift for Jacob's birthday. Done when a present is purchased and ready to give.

* Get Laptop From kim





