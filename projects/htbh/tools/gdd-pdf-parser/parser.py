#!/usr/bin/env python3
"""
GDD XP Card Parser
==================
Reads a game design document PDF, finds all XP card chapters, extracts
configured sections from each one, and writes a ZIP of markdown files
formatted as TechXPCards.

Usage:
    python parser.py <input.pdf> [--output <output.zip>] [--config <config.yaml>]
"""

import argparse
import io
import re
import sys
import zipfile
from pathlib import Path

import fitz  # pymupdf
import yaml


# ─────────────────────────────────────────────────────────────────────────────
# Text extraction helpers
# ─────────────────────────────────────────────────────────────────────────────

def extract_blocks(pdf_path: str) -> list[dict]:
    """Return all text blocks from a PDF with font size and page number."""
    doc = fitz.open(pdf_path)
    blocks = []
    for page_num, page in enumerate(doc, start=1):
        raw = page.get_text("dict", flags=fitz.TEXT_PRESERVE_WHITESPACE)
        for block in raw.get("blocks", []):
            if block.get("type") != 0:  # skip image blocks
                continue
            for line in block.get("lines", []):
                line_text = ""
                max_size = 0.0
                for span in line.get("spans", []):
                    line_text += span.get("text", "")
                    size = span.get("size", 0.0)
                    if size > max_size:
                        max_size = size
                text = line_text.strip()
                if text:
                    blocks.append({"text": text, "size": max_size, "page": page_num})
    doc.close()
    return blocks


def normalize(text: str) -> str:
    """Normalize whitespace and strip for loose matching."""
    return re.sub(r"\s+", " ", text).strip().lower()


def fuzzy_section_match(text: str, section_names: list[str]) -> str | None:
    """Return the matching section name if text loosely matches one, else None."""
    norm_text = normalize(text)
    for name in section_names:
        norm_name = normalize(name)
        # Accept if the block starts with the section name (handles trailing colons)
        if norm_text.startswith(norm_name) or norm_name in norm_text:
            return name
    return None


# ─────────────────────────────────────────────────────────────────────────────
# XP card detection
# ─────────────────────────────────────────────────────────────────────────────

def find_xp_card_boundaries(blocks: list[dict], config: dict) -> list[dict]:
    """
    Identify which blocks are XP card titles.

    Strategy: a heading-sized block is an XP card title if, within the next
    N blocks, one of the known_section_headers appears. This avoids false
    positives from other headings in the document.
    """
    heading_min = config.get("heading_min_size", 13.0)
    known_headers = config.get("known_section_headers", [])
    lookahead = 20  # how many blocks to look ahead for confirmation

    card_starts = []  # list of block indices where a new XP card begins

    for i, block in enumerate(blocks):
        if block["size"] < heading_min:
            continue
        # Check that this heading is followed by a known section header
        window = blocks[i + 1 : i + 1 + lookahead]
        for nearby in window:
            if fuzzy_section_match(nearby["text"], known_headers):
                card_starts.append(i)
                break

    # Deduplicate consecutive detections of the same heading
    deduped = []
    for idx in card_starts:
        if deduped and idx - deduped[-1] < 5:
            continue
        deduped.append(idx)

    return deduped


# ─────────────────────────────────────────────────────────────────────────────
# Section content extraction
# ─────────────────────────────────────────────────────────────────────────────

def extract_card_sections(
    blocks: list[dict],
    start_idx: int,
    end_idx: int,
    extract_sections: list[str],
    heading_min: float,
) -> dict[str, str]:
    """
    Within a card's block range, find each target section and collect its text.
    Returns a dict of {original_section_name: content_text}.
    """
    card_blocks = blocks[start_idx:end_idx]
    sections: dict[str, list[str]] = {}
    current_section: str | None = None

    for block in card_blocks:
        matched = fuzzy_section_match(block["text"], extract_sections)
        if matched:
            current_section = matched
            sections.setdefault(current_section, [])
            # Include any text on the same line after the section header
            header_norm = normalize(matched)
            leftover = block["text"].strip()
            # Strip the header label itself from the line
            if normalize(leftover).startswith(header_norm):
                leftover = leftover[len(matched):].lstrip(": \t")
            if leftover:
                sections[current_section].append(leftover)
        elif current_section is not None:
            # Stop collecting if we hit another heading-sized block that isn't
            # a known section — means we've left the current section
            if block["size"] >= heading_min and not block["text"].startswith("-"):
                # Check it's actually a new section or card boundary
                if not fuzzy_section_match(block["text"], extract_sections):
                    current_section = None
                    continue
            sections[current_section].append(block["text"])

    return {k: "\n".join(v).strip() for k, v in sections.items()}


# ─────────────────────────────────────────────────────────────────────────────
# Markdown rendering
# ─────────────────────────────────────────────────────────────────────────────

PLANNING_POKER_TABLE = """\
| (Sub)Task | Cost | Assigned to |
|-----------|------|-------------|
| | | |
"""


def render_techxpcard(title: str, sections: dict[str, str], config: dict) -> str:
    """Build a TechXPCard markdown string from extracted section content."""
    mapping: dict[str, str] = config.get("section_mapping", {})
    contacts: list[str] = config.get("contacts", [])

    # Resolve mapped content — multiple GDD sections can map to the same output
    # section; they are concatenated in that case.
    output_sections: dict[str, list[str]] = {}
    for gdd_section, content in sections.items():
        out_key = None
        for cfg_key, cfg_val in mapping.items():
            if normalize(gdd_section) == normalize(cfg_key):
                out_key = cfg_val
                break
        if out_key is None:
            continue
        output_sections.setdefault(out_key, [])
        if content:
            output_sections[out_key].append(content)

    def get(key: str) -> str:
        parts = output_sections.get(key, [])
        return "\n\n".join(parts) if parts else "*[to be filled]*"

    contact_lines = ""
    for i, name in enumerate(contacts, start=1):
        contact_lines += f"{i}. {name}\n"

    md = f"""# XP-Card: {title}

## Glossary

*[Insert terms that are not clear]*

---

## High Level Description

{get("High Level Description")}

---

## Requirements

*[Any information needed here — e.g. explanation of upcoming content, what is not done / unclear / up for discussion]*

### Basic Requirements

{get("Basic Requirements")}

### Advanced Requirements

*[to be filled]*

### Up for discussion Requirements

*[to be filled]*

---

## Designer Inputs / Balancing Inputs

{get("Designer Inputs / Balancing Inputs")}

---

## Relates to

{get("Relates to")}

---

## Contact in case of Questions

{contact_lines.strip()}

---

## Planning Poker — Programmers

{PLANNING_POKER_TABLE}
"""
    return md.strip() + "\n"


# ─────────────────────────────────────────────────────────────────────────────
# Filename sanitisation
# ─────────────────────────────────────────────────────────────────────────────

def safe_filename(title: str) -> str:
    """Convert a card title to a safe filename."""
    name = re.sub(r'[^\w\s\-]', '', title)
    name = re.sub(r'\s+', '_', name.strip())
    return name[:80] or "xp_card"


# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Parse GDD PDF into TechXPCard markdown files.")
    parser.add_argument("pdf", help="Path to the GDD PDF file")
    parser.add_argument("--output", "-o", default=None, help="Output ZIP path (default: <pdf-name>_xpcards.zip)")
    parser.add_argument("--config", "-c", default=None, help="Path to config.yaml (default: config.yaml next to this script)")
    parser.add_argument("--debug", action="store_true", help="Print detected card titles and extracted section content")
    parser.add_argument("--scan", action="store_true", help="Only list all heading-sized blocks in the PDF (for tuning heading_min_size)")
    args = parser.parse_args()

    # Load config
    config_path = args.config or Path(__file__).parent / "config.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    heading_min = config.get("heading_min_size", 13.0)
    extract_sections = config.get("extract_sections", [])

    # Extract blocks
    print(f"Reading: {args.pdf}")
    blocks = extract_blocks(args.pdf)
    print(f"  → {len(blocks)} text blocks extracted")

    if len(blocks) == 0:
        print("\nERROR: No text found in this PDF.")
        print("This usually means the PDF was created via 'Print to PDF' (text rendered as vector paths).")
        print("Fix: export your GDD from Google Docs using File → Download → PDF Document (.pdf)")
        sys.exit(1)

    if args.scan:
        print(f"\nHeadings in '{args.pdf}' (size >= {heading_min}pt):\n")
        for b in blocks:
            if b["size"] >= heading_min:
                print(f"  p{b['page']:>3}  {b['size']:5.1f}pt  {b['text'][:90]}")
        sys.exit(0)

    # Find XP card boundaries
    card_start_indices = find_xp_card_boundaries(blocks, config)
    print(f"  → {len(card_start_indices)} XP cards detected")

    if not card_start_indices:
        print("\nNo XP cards found. Try lowering heading_min_size in config.yaml or check the PDF structure.")
        sys.exit(1)

    # Process each card
    output_zip_path = args.output or Path(args.pdf).stem + "_xpcards.zip"
    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zf:
        for i, start_idx in enumerate(card_start_indices):
            end_idx = card_start_indices[i + 1] if i + 1 < len(card_start_indices) else len(blocks)
            title = blocks[start_idx]["text"].strip()

            if args.debug:
                print(f"  Card [{i+1}]: '{title}' (blocks {start_idx}–{end_idx}, page {blocks[start_idx]['page']})")

            card_sections = extract_card_sections(
                blocks, start_idx + 1, end_idx, extract_sections, heading_min
            )

            if args.debug:
                for sec, content in card_sections.items():
                    preview = content[:80].replace("\n", " ")
                    print(f"    [{sec}]: {preview}…")

            md_content = render_techxpcard(title, card_sections, config)
            filename = f"{i+1:02d}_{safe_filename(title)}.md"
            zf.writestr(filename, md_content)
            print(f"  Written: {filename}")

    with open(output_zip_path, "wb") as f:
        f.write(zip_buffer.getvalue())

    print(f"\nDone → {output_zip_path}")


if __name__ == "__main__":
    main()
