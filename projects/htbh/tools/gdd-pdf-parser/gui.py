#!/usr/bin/env python3
"""
GDD XP Card Parser — GUI
Single-file app: parser logic + tkinter GUI.
Build to EXE on Windows:  build_exe.bat
"""

import io
import re
import sys
import threading
import zipfile
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, scrolledtext, ttk

# ─────────────────────────────────────────────────────────────────────────────
# Default config (embedded so the EXE is self-contained)
# ─────────────────────────────────────────────────────────────────────────────

DEFAULT_CONFIG = {
    "known_section_headers": [
        "Intention | Requirements",
        "Intention|Requirements",
        "Intention | Requirements:",
        "Player Interaction",
        "Player Interaction:",
        "World/ Feature/ Physics Interaction",
        "World/ Feature/ Physics Interaction:",
        "World/Feature/Physics Interaction",
        "Vision Statement",
        "Vision Statement (Feel)",
        "Balancing Variables",
        "Balancing Variables:",
        "Mechanic Description",
        "Mechanic Description:",
        "Required Feedback",
        "Last Update",
        "Last Update:",
    ],
    "extract_sections": [
        "Intention | Requirements",
        "Intention | Requirements:",
        "Player Interaction",
        "Player Interaction:",
        "World/ Feature/ Physics Interaction",
        "World/ Feature/ Physics Interaction:",
        "Balancing Variables",
        "Balancing Variables:",
        "Mechanic Description",
        "Mechanic Description:",
    ],
    "section_mapping": {
        "Intention | Requirements":    "High Level Description",
        "Intention | Requirements:":   "High Level Description",
        "Player Interaction":          "Basic Requirements",
        "Player Interaction:":         "Basic Requirements",
        "World/ Feature/ Physics Interaction":  "Relates to",
        "World/ Feature/ Physics Interaction:": "Relates to",
        "Balancing Variables":         "Designer Inputs / Balancing Inputs",
        "Balancing Variables:":        "Designer Inputs / Balancing Inputs",
        "Mechanic Description":        "High Level Description",
        "Mechanic Description:":       "High Level Description",
    },
    "contacts": ["FABIAN KRÜGER", "SERPH"],
    "heading_min_size": 13.0,
}

# ─────────────────────────────────────────────────────────────────────────────
# Parser core
# ─────────────────────────────────────────────────────────────────────────────

def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def fuzzy_match(text: str, names: list) -> str | None:
    # Strip trailing colons before comparing so "Foo:" matches "Foo" and vice versa
    norm = normalize(text).rstrip(":")
    for name in names:
        norm_name = normalize(name).rstrip(":")
        if norm.startswith(norm_name) or norm_name in norm:
            return name
    return None


def extract_blocks(pdf_path: str) -> list:
    import fitz
    doc = fitz.open(pdf_path)
    blocks = []
    for page_num, page in enumerate(doc, start=1):
        raw = page.get_text("dict", flags=fitz.TEXT_PRESERVE_WHITESPACE)
        for block in raw.get("blocks", []):
            if block.get("type") != 0:
                continue
            for line in block.get("lines", []):
                text = ""
                max_size = 0.0
                for span in line.get("spans", []):
                    text += span.get("text", "")
                    size = span.get("size", 0.0)
                    if size > max_size:
                        max_size = size
                text = text.strip()
                if text:
                    blocks.append({"text": text, "size": max_size, "page": page_num})
    doc.close()
    return blocks


def find_card_boundaries(blocks: list, config: dict) -> list:
    heading_min = config.get("heading_min_size", 13.0)
    known = config.get("known_section_headers", [])
    lookahead = 20
    starts = []
    for i, block in enumerate(blocks):
        if block["size"] < heading_min:
            continue
        window = blocks[i + 1: i + 1 + lookahead]
        for nearby in window:
            if fuzzy_match(nearby["text"], known):
                starts.append(i)
                break
    deduped = []
    for idx in starts:
        if deduped and idx - deduped[-1] < 5:
            continue
        deduped.append(idx)
    return deduped


def extract_card_sections(blocks: list, start: int, end: int, extract: list, heading_min: float) -> dict:
    sections: dict[str, list] = {}
    current = None
    for block in blocks[start:end]:
        matched = fuzzy_match(block["text"], extract)
        if matched:
            current = matched
            sections.setdefault(current, [])
            leftover = block["text"].strip()
            if normalize(leftover).startswith(normalize(matched)):
                leftover = leftover[len(matched):].lstrip(": \t")
            if leftover:
                sections[current].append(leftover)
        elif current is not None:
            if block["size"] >= heading_min and not block["text"].startswith("-"):
                if not fuzzy_match(block["text"], extract):
                    current = None
                    continue
            sections[current].append(block["text"])
    return {k: "\n".join(v).strip() for k, v in sections.items()}


PLANNING_TABLE = "| (Sub)Task | Cost | Assigned to |\n|-----------|------|-------------|\n| | | |\n"


def render_card(title: str, sections: dict, config: dict) -> str:
    mapping = config.get("section_mapping", {})
    contacts = config.get("contacts", [])

    out: dict[str, list] = {}
    for gdd_sec, content in sections.items():
        out_key = None
        for k, v in mapping.items():
            if normalize(gdd_sec) == normalize(k):
                out_key = v
                break
        if out_key and content:
            out.setdefault(out_key, []).append(content)

    def get(key):
        parts = out.get(key, [])
        return "\n\n".join(parts) if parts else "*[to be filled]*"

    contact_lines = "\n".join(f"{i}. {n}" for i, n in enumerate(contacts, 1))

    return f"""# XP-Card: {title}

## Glossary

*[Insert terms that are not clear]*

---

## High Level Description

{get("High Level Description")}

---

## Requirements

*[Any information needed here — e.g. what is not done / unclear / up for discussion]*

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

{contact_lines}

---

## Planning Poker — Programmers

{PLANNING_TABLE}
""".strip() + "\n"


def safe_filename(title: str) -> str:
    name = re.sub(r"[^\w\s\-]", "", title)
    name = re.sub(r"\s+", "_", name.strip())
    return name[:80] or "xp_card"


def run_parser(pdf_path: str, config: dict, log) -> tuple[bytes, int]:
    """Returns (zip_bytes, card_count). Calls log(msg) for progress."""
    blocks = extract_blocks(pdf_path)
    log(f"Extracted {len(blocks)} text blocks from PDF.")

    if not blocks:
        raise ValueError(
            "No text found in this PDF.\n\n"
            "Export from Google Docs using:\n"
            "  File → Download → PDF Document (.pdf)\n"
            "(NOT via Print → Save as PDF)"
        )

    boundaries = find_card_boundaries(blocks, config)
    log(f"Detected {len(boundaries)} XP card(s).")

    if not boundaries:
        raise ValueError(
            "No XP cards detected.\n\n"
            "The parser looks for heading-level text followed by known GDD section labels.\n"
            "If your GDD structure differs, adjust config.yaml next to gui.exe."
        )

    heading_min = config.get("heading_min_size", 13.0)
    extract = config.get("extract_sections", [])

    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        for i, start_idx in enumerate(boundaries):
            end_idx = boundaries[i + 1] if i + 1 < len(boundaries) else len(blocks)
            title = blocks[start_idx]["text"].strip()
            log(f"  [{i+1}/{len(boundaries)}] {title}")
            card_secs = extract_card_sections(blocks, start_idx + 1, end_idx, extract, heading_min)
            md = render_card(title, card_secs, config)
            fname = f"{i+1:02d}_{safe_filename(title)}.md"
            zf.writestr(fname, md)

    return buf.getvalue(), len(boundaries)


# ─────────────────────────────────────────────────────────────────────────────
# Load optional external config.yaml (next to the exe/script)
# ─────────────────────────────────────────────────────────────────────────────

def load_config() -> dict:
    exe_dir = Path(sys.executable).parent if getattr(sys, "frozen", False) else Path(__file__).parent
    config_path = exe_dir / "config.yaml"
    if config_path.exists():
        try:
            import yaml
            with open(config_path, "r", encoding="utf-8") as f:
                return yaml.safe_load(f)
        except Exception:
            pass
    return DEFAULT_CONFIG


# ─────────────────────────────────────────────────────────────────────────────
# GUI
# ─────────────────────────────────────────────────────────────────────────────

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GDD XP Card Parser")
        self.resizable(True, True)
        self.minsize(560, 400)
        self.configure(bg="#1e1e2e")
        self._config = load_config()
        self._build_ui()
        self._center()

    def _center(self):
        self.update_idletasks()
        w, h = 620, 480
        x = (self.winfo_screenwidth() - w) // 2
        y = (self.winfo_screenheight() - h) // 2
        self.geometry(f"{w}x{h}+{x}+{y}")

    def _build_ui(self):
        BG   = "#1e1e2e"
        CARD = "#2a2a3e"
        ACC  = "#7c6af7"
        FG   = "#cdd6f4"
        MUTED = "#6c7086"

        self.configure(bg=BG)

        # Title
        tk.Label(self, text="GDD XP Card Parser", font=("Segoe UI", 16, "bold"),
                 bg=BG, fg=FG).pack(pady=(20, 4))
        tk.Label(self, text="Converts GDD PDF → TechXPCard markdown files (ZIP)",
                 font=("Segoe UI", 9), bg=BG, fg=MUTED).pack(pady=(0, 16))

        # Input row
        frame = tk.Frame(self, bg=BG)
        frame.pack(fill="x", padx=24)

        tk.Label(frame, text="GDD PDF:", font=("Segoe UI", 9), bg=BG, fg=FG, width=10, anchor="w").grid(row=0, column=0, sticky="w")
        self.pdf_var = tk.StringVar()
        tk.Entry(frame, textvariable=self.pdf_var, font=("Segoe UI", 9),
                 bg=CARD, fg=FG, insertbackground=FG, relief="flat",
                 highlightthickness=1, highlightbackground=MUTED, highlightcolor=ACC
                 ).grid(row=0, column=1, sticky="ew", padx=(6, 6))
        tk.Button(frame, text="Browse…", font=("Segoe UI", 9), bg=ACC, fg="white",
                  activebackground="#9d8fff", relief="flat", padx=10,
                  command=self._browse_pdf).grid(row=0, column=2)

        # Output row
        tk.Label(frame, text="Output ZIP:", font=("Segoe UI", 9), bg=BG, fg=FG, width=10, anchor="w").grid(row=1, column=0, sticky="w", pady=(8, 0))
        self.zip_var = tk.StringVar()
        tk.Entry(frame, textvariable=self.zip_var, font=("Segoe UI", 9),
                 bg=CARD, fg=FG, insertbackground=FG, relief="flat",
                 highlightthickness=1, highlightbackground=MUTED, highlightcolor=ACC
                 ).grid(row=1, column=1, sticky="ew", padx=(6, 6), pady=(8, 0))
        tk.Button(frame, text="Browse…", font=("Segoe UI", 9), bg=CARD, fg=FG,
                  activebackground=ACC, relief="flat", padx=10,
                  command=self._browse_zip).grid(row=1, column=2, pady=(8, 0))

        frame.columnconfigure(1, weight=1)

        # Convert button
        self.btn = tk.Button(self, text="Convert", font=("Segoe UI", 11, "bold"),
                             bg=ACC, fg="white", activebackground="#9d8fff",
                             relief="flat", padx=24, pady=8, command=self._convert)
        self.btn.pack(pady=18)

        # Log area
        log_frame = tk.Frame(self, bg=CARD, padx=2, pady=2)
        log_frame.pack(fill="both", expand=True, padx=24, pady=(0, 20))

        self.log = scrolledtext.ScrolledText(log_frame, font=("Consolas", 9),
                                             bg=CARD, fg=FG, insertbackground=FG,
                                             relief="flat", wrap="word",
                                             state="disabled")
        self.log.pack(fill="both", expand=True)

        # Status bar
        self.status_var = tk.StringVar(value="Ready")
        tk.Label(self, textvariable=self.status_var, font=("Segoe UI", 8),
                 bg=BG, fg=MUTED, anchor="w").pack(fill="x", padx=24, pady=(0, 8))

    def _browse_pdf(self):
        path = filedialog.askopenfilename(
            title="Select GDD PDF",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        if path:
            self.pdf_var.set(path)
            stem = Path(path).stem
            default_zip = str(Path(path).parent / f"{stem}_xpcards.zip")
            self.zip_var.set(default_zip)
            self._log_clear()
            self._log(f"Selected: {path}")

    def _browse_zip(self):
        path = filedialog.asksaveasfilename(
            title="Save ZIP as",
            defaultextension=".zip",
            filetypes=[("ZIP files", "*.zip")]
        )
        if path:
            self.zip_var.set(path)

    def _convert(self):
        pdf = self.pdf_var.get().strip()
        out = self.zip_var.get().strip()
        if not pdf:
            self._log("ERROR: Please select a PDF first.", color="red")
            return
        if not out:
            self._log("ERROR: Please specify an output ZIP path.", color="red")
            return
        self.btn.configure(state="disabled", text="Converting…")
        self.status_var.set("Converting…")
        self._log_clear()
        threading.Thread(target=self._worker, args=(pdf, out), daemon=True).start()

    def _worker(self, pdf: str, out: str):
        try:
            zip_bytes, count = run_parser(pdf, self._config, self._log)
            with open(out, "wb") as f:
                f.write(zip_bytes)
            self._log(f"\nDone! {count} card(s) written to:\n{out}", color="green")
            self.status_var.set(f"Done — {count} cards → {Path(out).name}")
        except Exception as e:
            self._log(f"\nERROR: {e}", color="red")
            self.status_var.set("Failed — see log")
        finally:
            self.btn.configure(state="normal", text="Convert")

    def _log(self, msg: str, color: str | None = None):
        def _do():
            self.log.configure(state="normal")
            tag = color or "normal"
            self.log.tag_configure("red",   foreground="#f38ba8")
            self.log.tag_configure("green", foreground="#a6e3a1")
            self.log.insert("end", msg + "\n", tag)
            self.log.see("end")
            self.log.configure(state="disabled")
        self.after(0, _do)

    def _log_clear(self):
        def _do():
            self.log.configure(state="normal")
            self.log.delete("1.0", "end")
            self.log.configure(state="disabled")
        self.after(0, _do)


if __name__ == "__main__":
    App().mainloop()
