# HTBH — Tile Conditions Ideation
*Generated 2026-06-09 — review at 12:30*

## Design Principle
Tile conditions should be **orthogonal to tile state** (BUILDABLE/COMBAT/SPAWNING are zone states; terrain is a separate property). A tile has both a zone state AND a terrain type. This keeps the existing unlock/pathfinding system intact.

Implementation hook: add `terrain_type: str` to `Tile` in `tile.py`. `Tile.pathfinding_weight` already queries the tile — terrain can stack a modifier on top. Buffs/debuffs for buildings read `tile.terrain_type` in `update_stats_from_tier` or at placement.

---

## Terrain Type Ideas

### 1. Elevated Ground (High Ground)
- **Effect on buildings:** +1 Chebyshev range for any building placed on it
- **Effect on enemies:** +25% movement cost through the tile (PF weight bump) — enemies don't love climbing
- **Strategic role:** Rare premium real estate. Forces a positioning choice: do you spend love to unlock the high ground tile, or build closer?
- **Theme:** "The stage above the crowd — music carries further from the heights"
- **Implementation:** Add `PF_WEIGHT_HIGH_GROUND` to map balancing. In `Tile.pathfinding_weight`, add terrain check. Range buff applied at placement via `tile.terrain_type` check in buildings.

### 2. Resonant Ground (Sacred/Echo Tiles)
- **Effect on economic buildings:** +50% yield
- **Effect on defence buildings:** +1 damage per attack
- **Placement:** Only 2–4 per map, scattered in the COMBAT zone — pre-determined at map gen or fixed positions
- **Visual cue:** Subtle glow/shimmer on the tile
- **Theme:** "Spots where human connection naturally amplifies — the campfire, the plaza, the old stage"
- **Implementation:** No PF weight change. Buff applied by checking `tile.terrain_type == 'resonant'` in `EconomicBuilding.update_stats_from_tier` and `DefenceBuilding.update_stats_from_tier`.

### 3. Dense Terrain / Overgrowth
- **Unbuildable** (like a COMBAT tile that can't host buildings)
- **Blocks movement:** Very high PF weight (8–9) — forces enemies to path around it, creating natural chokepoints
- **Can be cleared:** Pay a love cost to convert it to a standard BUILDABLE tile — like a mini-unlock
- **Theme:** "Untamed wilderness. Humanity must clear the chaos to make space for connection"
- **Implementation:** New tile state variant, or terrain type with `is_buildable = False`. `pathfinding_weight` returns high value. UI: right-click → "Clear Overgrowth (X love)"

### 4. Unstable Ground / Rubble
- **Buildings placed here:** -20% HP, but -30% placement cost (cheaper to build in the ruins)
- **Enemies:** Take 1 chip damage per tile they walk through it (environmental hazard)
- **Theme:** "Broken places — you can build here, but it costs you something"
- **Risk/reward:** Budget option with defensive upside. Especially interesting for painter (which doesn't fight anyway — lower HP is irrelevant)
- **Implementation:** Stat mod applied at placement. Enemy chip damage in `_update_enemy_phase` after each move step.

### 5. Open Plaza / Acoustic Stage
- **Effect on AOE buildings (Maw Mortar line):** +1 AOE radius
- **Effect on economic buildings:** +1 to `rounds_to_payout` reduction for Painter (pays out one round earlier)
- **No movement penalty for enemies**
- **Theme:** "Performance spaces — the open air amplifies the blast of art (and mortars)"
- **Implementation:** `AOEDefenceBuilding` reads `tile.terrain_type` when computing splash radius. Small scope change.

### 6. Scorched Earth (Dynamic Terrain)
- **Created by:** Enemy SiegeCannon impacts leave a scorched tile behind
- **Effect:** Slightly lower PF weight (enemies are drawn back to their own destruction — overconfident)
- **Healing:** Pay love to restore to normal — ties into the "humanity healing" theme
- **Strategic tension:** You might WANT some scorched tiles to funnel enemies, or you might want to heal them to reclaim building space
- **Theme:** "Destruction leaves a mark. Humanity must choose to heal it."
- **Implementation:** `SiegeCannon.on_impact()` sets target tile's `terrain_type = 'scorched'`. Dynamic terrain — the only mutable terrain type. Adds a new interaction layer to SiegeCannon.

### 7. Frozen Ground (Late-Game / Biome Variant)
- **Effect on enemies:** -30% move speed (high PF weight — they slow through it)
- **Effect on buildings:** -1 range (cold affects sight lines)
- **Could appear:** Only in later rounds / specific map regions
- **Theme:** "Emotional coldness — harder to reach people, harder for them to reach you"
- **Implementation:** Round-gated terrain type reveal. PF weight + range debuff.

---

## Implementation Priority Order
1. **Resonant Ground** — smallest scope, biggest thematic payoff, no PF changes needed
2. **Elevated Ground** — one PF weight + range buff, clear strategic depth
3. **Dense Terrain / Overgrowth** — adds chokepoint design and a love sink mechanic
4. **Scorched Earth** — most interesting dynamic loop, but requires SiegeCannon hook

---

## Domains Touched
| Feature | Primary Domain | Secondary Domain |
|---|---|---|
| Terrain type property on Tile | map | — |
| PF weight modifiers | map | — |
| Building stat buffs/debuffs | buildings | map (reads terrain) |
| Clearing overgrowth (UI) | ui | map |
| Scorched by SiegeCannon | enemies | map |
| Balancing new PF weights | map | — |

---

## Open Questions for Fabian/GDD
- Should terrain types be fixed at map gen, or can any tile become any terrain?
- Is there a thematic name system? ("Sacred Ground" → "Place of Gathering"? "Elevated" → "The Stage"?)
- Should terrain conditions be visible to the player before unlocking a tile? (preview in unlock mode)
- Scorched Earth: should it reset after N rounds automatically, or only on player action?
