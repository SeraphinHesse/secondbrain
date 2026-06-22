# To Do



!taskname = high importance task

##### Reminders

###### Bureaucracy & Chores
* [2026-06-16 19:00] Get Laptop From kim


###### General

###### HTBH




##### How to be Human

###### Producing

* !WBS update
  Check if the WBS still matches the planned scope of the game
* !WBS full tasks



* Steam Page Setup
  Complete all admin and implementation steps to get HTBH's Steam store page live. Covers: partner onboarding, AppID creation, tax/banking setup, store page fields, graphical asset uploads (capsules, library hero, screenshots, trailer), content survey / Germany age rating, pricing + regional pricing, SteamPipe build upload, and the two-checklist release process. Done when store page is "Coming Soon" with build approved and the 2-week clock started.



###### Design

* Meditator Building: tier visual design
  Three-tier economy building. Tier 1 — "The Meditator": looks identical to the Flute Player but seated on a rock. Tier 2 — "The Shaman": seated on a partial temple structure, visibly levitating above it. Tier 3 — "The Sun Priest": god-like figure radiating sunlight with a giant temple beneath. Design all three art directions / sprites before implementation.

* x !XP cards: Finish GDD
* Ideation: More Boss types
* Ideation: More Enemy types
* Ideation: More Economy Buildings
* Ideation: More Defence Buildings
* Ideation: life loss display
  Options: animate the base, or have the enemy path back out of the base
* Come up with more generic upgrades
* Booster Limits Explanations
* Economy Proximity Bonuses Ideation



###### Claude Build

* Balancing GUI: Fix build/editor version label
  The GUI currently misidentifies the editor version as a build version. Find the version detection logic and correct it. Done when the label accurately shows "Editor" in Godot editor and "Build" in exported builds.

* Balancing GUI: Collapsible items within categories
  Buildings and entries inside each category should be individually collapsible/expandable so you can focus on one at a time. State persists within session. Done when each entry can be collapsed to its header and re-expanded.

* Balancing GUI: Left panel category tree
  Replace the flat category list on the left with a hierarchical tree: top level = category (e.g. Buildings), second = sub-type (e.g. Defense/Economy), third = individual building names. Clicking a leaf scrolls/filters to that building. Done when the full tree is rendered and navigable.

* Balancing GUI: Visual polish
  General UI refresh — spacing, typography, color palette, card styling, hover states. Current look is too raw. Done when it looks like a tool you'd actually want to use.

* Balancing GUI: Hover tooltips for each value
  Every config field should show a tooltip on hover explaining what it controls, what effect changing it has, and any constraints. Tooltip content should live in a data file (not hardcoded). Done when all fields have accurate tooltips.

* Balancing GUI: Value categories within each building
  Group each building's config values into logical sub-categories (e.g. Combat, Economy, Visual, Costs) instead of one flat list. Done when all building values are organized into named groups with visual separators.





this should be toggleable in balancing gui
* Range and Building Preview on hover
* x !Implement Tile Conditions



* Move Balancing GUI outside of balancing folder and cleanup root folder
* Make Balancing Config history get cloned to the build version
* FIx Boost Range
* Split Boost into 3 techs
* All tileweights balanceable
* Economy Proximity Bonuses
* !Fullscreen Mode
  Full screen mode is currently broken on various resolutions. Fix it so the game runs correctly at any screen resolution without layout issues, clipping, or scaling errors. Done when full screen works reliably across all tested resolutions.

* !Wall HP upgrade
  Upgrading the Wall Builder building currently only increases the building's own HP. It should also upgrade the HP of all walls it manages. Make wall HP scale with the building's upgrade tier. Done when upgrading the Wall Builder visibly increases wall HP.

* x !Active Abilities

* !bloodstains only get cleared on end turn
  Blood stains left by dead enemies are currently cleared at the end of the combat phase. Change this so they persist and are only cleared at the end of the following turn when the player presses End Turn — so they carry over into the next round and players can see where enemies fell. Done when blood stains survive into the next round and disappear only on the subsequent End Turn press.

* !Xp from dead buildings
  When a building is destroyed, it should grant the player XP. The amount should be balanceable per building type, with a default of 1 XP per building. Done when buildings drop XP on death and the per-building XP value is exposed in the balancing config.

* !Story Upgrades
* !Blank Cutscenes
* !Cutscene Integration

* !Xp from lost rounds
  When a round is lost, any enemies that were in the queue but never spawned should still award XP as if they had entered and died — so losing a round does not put the player at an XP disadvantage. Done when the rule is implemented and the XP amount matches what would have been awarded normally.
* !Meditator unlockable and Balanceable
  The meditator needs to be added to the unlock system and to the balancing gui in the same way as all the other buildings
* !Scaling Blocker
  The Blocker should be scaleable with tiers just like any other building it should start with 500 HP and then should scale Hp with upgrades



###### Godot Implementation

* Add the Stone Thrower
  Implement the Stone Thrower unit in Godot. Done when it is functional in-game with correct behaviour, animations, and balancing config wired up.

* Add the Meditator
  Implement the Meditator building in Godot (Tier 1 of the economy building). Done when it is placeable, produces the correct resource output, and hooks into the existing balancing config.



###### Balancing

* Levelling too Fast: Sheets Predictions not accurate
* Sunscorch nerf + pricier upgrade
  Sunscorch generally too strong; upgrade cost needs to go up
* Higher wall hp
* slightly higher stone thrower hp



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
* Organize Tazio & Keanu Meeting
* Glasses Ideation
* Weib Automation and Pitch planning

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
* Set up Meta Ads account + activate Meta Ads MCP
  Create a Meta Business account and Meta Ads account, then sign up at pipeboard.co to get a Pipeboard token. Add PIPEBOARD_TOKEN to .claude/settings.local.json in the AddictiveMedia repo to activate the Meta Ads MCP (meta-ads server is already configured in .mcp.json — just needs the token).

* Set up / authenticate Windsor.ai connector
  One-time auth for the Windsor.ai MCP (Meta/Google Ads data) so reporting + media automation can pull live ad data. Run authenticate → complete_authentication in a Claude session.
* !Pay chelsea for website



##### Claude Automation

* Research: Claude Code skills for frontend web design
  Survey and document useful Claude Code skills for frontend/web design work. Priority candidates: the built-in topic skill, the third-party "taste" skill (UI/UX Pro Max), and any library-focused skills. Done when there's a curated shortlist with install/use notes in `projects/claude-automation/`.

* Research: Cybersecurity for vibe coding
  Investigate security risks specific to AI-assisted rapid development (vibe coding). Cover common vulnerabilities in AI-generated code, relevant Claude Code skills or MCP tools for catching issues, and best practices for reviewing AI-generated code. Done when findings are documented in `projects/claude-automation/cybersecurity-vibe-coding-notes.md`.



##### Admin

* Integrate dashboard calendar sync into morning routine
  Set up persistent 6:30am calendar → reminders sync: either configure Windows Task Scheduler to run sync-calendar-reminders.js (requires one-time Google OAuth token setup) or keep a Claude Code session open so the CronCreate job fires. Done when calendar events appear automatically in the dashboard Reminders sidebar every morning without any manual steps.
* Dashboard: Click and drag movable tasks
* Rework Morning Claude Routines
* Be able to change time on the reminders
* Big Tasks and small tasks
* Change Dashboard Logo



##### University





##### Bureaucracy \& Chores

* Get Laptop From kim
* Dinner with parents







##### Reminders

###### Admin



##### Reminders

###### HTBH / Producing

