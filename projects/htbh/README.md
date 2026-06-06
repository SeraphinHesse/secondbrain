# Project: How To Be Human (HTBH)

**Status**: active
**Type**: game
**Engine**: pygame-ce (Python 3)

## What it is
An isometric tower-defense where you spend *love* (the currency) to unlock tiles and place musicians/defenders that protect "the hole" (your base) from waves of enemies. Napoleonic-soldier enemy aesthetic, procedurally generated sprites.

## Run / build
- `py main.py` from the project root
- `pip install -r requirements.txt`
- `build.bat` for a PyInstaller `.exe` → `dist/`

## Repo
<!-- Add GitHub URL when known -->

## Core architecture
- `src/game.py` — god-object, start here for gameplay changes
- `balancing.py` / `balancing.json` — ALL numeric tuning (JSON wins at runtime)
- `src/constants.py` — enums, grid dims, screen sizes
- `src/buildings/` — building hierarchy
- `src/enemies/` — raider, siege cannon
- `src/ui/` — HUD, construct panel, levelup window

See the project's own `CLAUDE.md` for the full architecture reference.

## Current phase
<!-- Prototype / vertical slice / alpha / beta -->

## Open tasks
- [ ]

## Devlog
<!-- Append after each session: date + what happened + what's next -->
