# To Do



!taskname = high importance task

##### Reminders

###### Bureaucracy & Chores
* [2026-07-15 19:00] Get Laptop From kim


###### General

###### HTBH




##### How to be Human

###### Producing




* !^Steam Page Setup
  Complete all admin and implementation steps to get HTBH's Steam store page live. Covers: partner onboarding, AppID creation, tax/banking setup, store page fields, graphical asset uploads (capsules, library hero, screenshots, trailer), content survey / Germany age rating, pricing + regional pricing, SteamPipe build upload, and the two-checklist release process. Done when store page is "Coming Soon" with build approved and the 2-week clock started.
* Market Research
* Target Audience Analysis
* Social media setup

* !Sprint planning: art & design
  Plan and assign sprint tasks for both the art track and the design track. Done when both tracks have a full, prioritised sprint backlog ready to execute.

* !Vertical slice roadmap & deliverables plan
  Define the milestone path to vertical slice: (1) a roadmap showing the phases and milestones needed to reach VS, and (2) a deliverables checklist scoped to VS. Done when both documents exist and tasks can be broken out from them.



###### Design

* Meditator Building: tier visual design
  Three-tier economy building. Tier 1 — "The Meditator": looks identical to the Flute Player but seated on a rock. Tier 2 — "The Shaman": seated on a partial temple structure, visibly levitating above it. Tier 3 — "The Sun Priest": god-like figure radiating sunlight with a giant temple beneath. Design all three art directions / sprites before implementation.

* ^Ideation: More Boss types
* ^Ideation: More Enemy types
* ^Ideation: More Economy Buildings
* ^Ideation: More Defence Buildings
* Ideation: life loss display
  Options: animate the base, or have the enemy path back out of the base
* Come up with more generic upgrades
* Booster Limits Explanations
* Economy Proximity Bonuses Ideation
* !^Enemy spawning and Pathfinding Ideation
* x !Boss rework



###### Claude Build











this should be toggleable in balancing gui
* Range and Building Preview on hover




tried to fix and now gives error: 
Traceback (most recent call last):
  File "main.py", line 20, in <module>
  File "src\core\game.py", line 185, in run
  File "src\core\game.py", line 205, in _handle_events
  File "src\core\game.py", line 236, in _handle_settings
  File "src\ui\settings_menu.py", line 55, in handle_event
  File "src\core\game.py", line 1937, in _apply_display_mode
pygame.error: Cannot set 0 sized SCALED display mode






* Display Updated Cost for construction on shift click, upgrade tiers on shift click
  When numeros items are shift clicked, the cost on the button should increase to reflect that, and there should be a 2x before the name, also on shift click one should be able to upgrade the tiers of buildings en masse as well
* x !Lighting and AOE hitboxes
  Should be elipses to seem like circles on the isometric ground, just like in the old prototype
* x !^Call Enemy Animations
* ^Loading Screen
  add a loading screen and the ability to import art for it
* x !Lightning Building
* !painter option greyout
  painter should be greyed out when the tile has already been built with a painter in building screen
* x !^Boss enemy rework
  Needs to have stages, and become stationary and become an enemy spawner
* ^Enemy tile stacking rework
* ^Tutorial
* ^Ploppable buildings
* zoom level should be higher at default
  Make the current max zoomed in be the default, and make one extra zoom level more zoomed in even than that
* x !Bush wall builder unlock broken
* Editable Projectile
* Fullscreen as default
* x Animated props
* !Time Speedup
* x !^Enemy Scaling Rework
* x !Boss Stuck on terrain
  Boss gets stuck randomly on water or mountain tiles, weird pathfinding overall, should reconfirm intent
* x !Fix Meditate and Bushwall Levelups
  Currently, when you unlock bushwall builder and meditator, they are not available to build, its because



###### Balancing

* Raider Scaling
  Seperate raider scaling in balancing GUI
* Fewer Water tiles
* Mortar more expensive
  Mortar/AOE base cost must be more expensive
* ^Game Still too hard at start?
* ^Game still outscalable?



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
* Leon Website



##### Admin

* Integrate dashboard calendar sync into morning routine
  Set up persistent 6:30am calendar → reminders sync: either configure Windows Task Scheduler to run sync-calendar-reminders.js (requires one-time Google OAuth token setup) or keep a Claude Code session open so the CronCreate job fires. Done when calendar events appear automatically in the dashboard Reminders sidebar every morning without any manual steps.
* Rework Morning Claude Routines
* Change Dashboard Logo



##### University





##### Bureaucracy \& Chores

* Get Laptop From kim







##### Reminders

###### Admin



##### Reminders

###### HTBH / Producing



##### HTBH / ART

* ^UI Rework
* Seasons Art
* Painter Art
* Enemy Art
* ^Cutscene - Meet Humans
* ^Make Map
* Intro Cutscene Rework
* Tile Conditions Art


##### HTBH Engin Changes

* Build Shipped balancing GUI
  A version of the editor which only carries the selector tree on the right, and the balancing values, and it says (BUILD VERSION, CANNOT BE PUSHED TO GIT), and it gets shipped with the Build
* Feature Toggle
  Every Feature in the game should be toggleable on or off in a feature toggle section of the GUI
* Balancing GUI: Hover tooltips for each value
  Every config field should show a tooltip on hover explaining what it controls, what effect changing it has, and any constraints. Tooltip content should live in a data file (not hardcoded). Done when all fields have accurate tooltips.
* x !^vfx editor in engine
  a way to import sprite sheets for different ingame vfx, a way to manipulate those vfx, and way for the engine to call them and delete them,
* x !^ui editor V1 in engine
  10L of migration plan, UI EDITOR, follow UI editor plan md
* redesign branch lock protocol
* !^Cutscene Integration
  Need the functionality to add cutscenes and import mp4s for them.
* x Map maker Keybinds
* x !^Scene Editor for Entities
  be able to set the position of a projectile origin point for def buildings or a projectile endpoint for enemies, or adjust the position of healthbars, directly in the editor
* default animation speed 6 frames
  default animation speed 6 frames per sec, should be editable via core balancing
* x Scrolling toolbrush in the Map maker
* !All tileweights balanceable
* !Font and Color editing broken in UI editor
* Setup bat should only have to be run once
* x !Scrolling changes anim speeds
  It should be impossible to change the values anywhere in the editor especially the animation speeds via mousewheel. the mousewheel is only there for navigation, not for editing values.
* x Tilepainting scrollable
* Execute plan buttons in agent dispatch
  Buttons which can hust execute the selected plan with an attached message in the summon robot screen
* Ai-free plan switching
  one should be able to switch the current plan in plan.md from the editor without  claude
* Worktree name in the Editor
* ^Sound Editor
* Flip horizontal and flip vertical  for any sprite editor


##### HTBH / Marketing

* Brand Creation
