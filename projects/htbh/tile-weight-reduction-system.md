# Idea: Tile Weight Reduction System

## Domain
Game dev — HTBH

## Raw Idea
After a threshold round (e.g. round 10), enemy pathfinding tile weights get reduced based on which buildings dealt the most damage that round.

- Top 3 damage-dealing buildings reduce the tile weights of the tiles they occupy/cover
- Lower tile weight = more likely for enemies to path over that tile
- Creates a soft feedback loop: high-performing towers attract more enemies over time

## Questions to Resolve
- Does the weight reduction reset each round, or accumulate?
- Is the reduction a flat value or percentage?
- Does this apply to the building's tile only, or a radius around it?
- What round does it kick in? (mentioned: ~round 10)
- Visual feedback needed? (e.g. highlight tiles with reduced weight)

## Potential Mechanic Name
"Threat Magnetism" / "Aggro Weighting"
