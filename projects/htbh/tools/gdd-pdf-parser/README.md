# GDD XP Card Parser

Parses a game design document PDF and outputs one TechXPCard markdown file per XP card, bundled as a ZIP.

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```bash
# Basic — outputs <gdd-name>_xpcards.zip
python parser.py my_gdd.pdf

# Specify output path
python parser.py my_gdd.pdf --output cards.zip

# Scan mode — lists all headings found in the PDF (use this if 0 cards detected)
python parser.py my_gdd.pdf --scan

# Debug mode — shows detected cards and extracted section content
python parser.py my_gdd.pdf --debug
```

## How to export the GDD from Google Docs

**Do this:** File → Download → PDF Document (.pdf)

**Not this:** Print → Print to PDF (converts text to vector paths — not parseable)

## How it works

1. Detects XP card chapter boundaries by finding headings followed by known GDD section labels (e.g. "Intention | Requirements", "Last Update", etc.)
2. Extracts the configured sections from each card
3. Maps them to the TechXPCard format:

| GDD section | → TechXPCard section |
|---|---|
| Intention \| Requirements | High Level Description |
| Mechanic Description | High Level Description (appended) |
| Player Interaction | Basic Requirements |
| World/Feature/Physics Interaction | Relates to |
| Balancing Variables | Designer Inputs / Balancing Inputs |

Skipped: Vision Statement, References, Required Feedback, Sketch, Last Update

Empty in output (fill manually): Glossary, Advanced Requirements, Up for discussion Requirements, Planning Poker

## Tuning

If 0 cards are detected, run `--scan` to see what heading sizes are in your PDF, then adjust `heading_min_size` in `config.yaml`.

All section names and mappings are configurable in `config.yaml`.
