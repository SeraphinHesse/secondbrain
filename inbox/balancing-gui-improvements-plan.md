# Balancing GUI Improvements — Plan

**Date:** 2026-06-16  
**Project:** HTBH  
**Section:** Claude Build

---

## Tasks

### 1. Fix Build / Editor Version Label (Bug — do first)
The GUI currently misidentifies the editor version as a build version. Find the version detection logic and invert/correct the condition so the label accurately reflects which environment is running.

**Done when:** The label correctly shows "Editor" in Godot editor and "Build" in exported builds.

---

### 2. Collapsible Items Within Categories
Buildings (and other entries) inside each category should be individually collapsible/expandable so the user can focus on one item at a time without scrolling through everything.

**Done when:** Each row/entry in a category can be collapsed to just its header, and re-expanded. State should persist within a session.

---

### 3. Left Panel: Category Tree Navigation
Replace the flat category list on the left with a hierarchical tree:
- Top level: category (e.g. "Buildings")
- Second level: sub-type (e.g. "Defense", "Economy")
- Third level: individual building names

Clicking a leaf node scrolls/filters to that building directly.

**Done when:** Full tree is rendered on the left, clicking any node navigates to the correct entry in the main panel.

---

### 4. Visual Polish / Nicer Look
General UI refresh — better spacing, typography, color usage, visual hierarchy. Current look is too raw/utilitarian.

**Scope:** Fonts, padding, card styling, color palette, hover states, overall feel.

**Done when:** It looks like a tool you'd actually want to use.

---

### 5. Hover Tooltips for Each Value
Every numerical/config field should show a tooltip on hover explaining:
- What the value controls in-game
- What effect increasing/decreasing it has
- Any known constraints or gotchas

**Done when:** Hovering any field shows a relevant, accurate tooltip. Tooltips should be authored in a data file (not hardcoded inline) so they're easy to update.

---

### 6. Value Categories Within Each Building
Inside each building's expanded view, group its config values into logical sub-categories (e.g. "Combat", "Economy", "Visual", "Costs") so the list of values is scannable rather than one long dump.

**Done when:** Each building's values are organized into named groups with visual separators.

---

## Order of Attack

1. **Fix version label** (quick bug, do first — unblocks accurate testing)
2. **Collapsible items** (biggest UX win, low visual risk)
3. **Tree navigation** (requires knowing the category structure — do after collapsibles are working)
4. **Value categories within buildings** (schema/data work, pairs with tree nav)
5. **Hover tooltips** (needs tooltip data file — can be done in parallel with #4)
6. **Visual polish** (do last, once structure is locked in)
