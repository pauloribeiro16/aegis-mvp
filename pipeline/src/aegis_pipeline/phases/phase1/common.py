#!/usr/bin/env python3
"""aegis_pipeline.phases.phase1.common — Common parsing, table, and formatting helpers."""

from __future__ import annotations

import re
import sys
from pathlib import Path

# Ensure pipeline/src is importable
_src = Path(__file__).resolve().parents[3]
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

from compose import REGULATIONS

# Spelling normalization map for inline regulation tokens
_REG_SPELLING = {
    "aiact": "AI_Act",
    "aiacts": "AI_Act",
    "ai act": "AI_Act",
    "ai-act": "AI_Act",
    "aia": "AI_Act",
    "ai": "AI_Act",
    "nis2": "NIS2",
    "nis 2": "NIS2",
    "nis-2": "NIS2",
    "nisii": "NIS2",
    "gdpr": "GDPR",
    "cra": "CRA",
    "dora": "DORA",
    "doraia": "DORA",
}


def extract_fenced(text: str, lang: str | None = None) -> str:
    """Extract first fenced code block (optionally with a language tag)."""
    pattern = rf"```{lang}[^\n]*\n(.*?)```" if lang else r"```[^\n]*\n(.*?)```"
    m = re.search(pattern, text, re.S)
    if not m:
        raise ValueError(f"no {'```' + lang + ' ' if lang else ''}fenced block found in answer")
    return m.group(1)


def parse_md_table(text: str) -> list[list[str]]:
    """Parse a markdown table into rows of cells (separator rows dropped)."""
    rows: list[list[str]] = []
    for line in text.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
            continue
        rows.append(cells)
    return rows


def canonical_reg(token: str) -> str:
    """Canonical regulation token, or '' when spelling is unrecognisable."""
    t = token.strip().strip("` ").strip()
    if t in REGULATIONS:
        return t
    return _REG_SPELLING.get(re.sub(r"[\s\-_]+", "", t).lower(), "")


def one_reg(bs: str, sd_id: str) -> str:
    """The single regulation a Baseline source cites (SG-D-XX.Y.<REG>)."""
    raw = bs.strip("` ")
    m = re.fullmatch(rf"SG-{re.escape(sd_id)}\.(\S+)", raw)
    if not m:
        raise ValueError(
            f"Baseline source {bs!r} must cite exactly one Sub-SO id SG-{sd_id}.<REG> (one regulation per goal row)"
        )
    reg = canonical_reg(m.group(1))
    if not reg:
        raise ValueError(
            f"Baseline source {bs!r} has regulation {m.group(1)!r}, which is not one of {'/'.join(REGULATIONS)}"
        )
    return reg
