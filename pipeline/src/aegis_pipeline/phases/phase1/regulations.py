#!/usr/bin/env python3
"""aegis_pipeline.phases.phase1.regulations — Stage P2 regulation scope confirmation."""

from __future__ import annotations

import sys
from pathlib import Path

# Ensure pipeline/src is importable
_src = Path(__file__).resolve().parents[3]
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

from compose import REGULATIONS
from aegis_pipeline.phases.phase1.common import extract_fenced, parse_md_table


def parse_p2(answer: str) -> dict:
    """Parse and validate stage P2 regulation scope verdicts."""
    md = extract_fenced(answer, "markdown")
    rows = parse_md_table(md)
    if not rows:
        raise ValueError("no table found in P2 answer")
    body = rows[1:] if rows[0] and rows[0][0].lower().startswith("regulation") else rows
    verdicts = []
    for cells in body:
        if len(cells) < 3:
            raise ValueError(f"P2 table row has {len(cells)} columns, expected >=3: {cells}")
        reg = cells[0].replace("*", "").replace("`", "").strip()
        verdict = cells[1].replace("*", "").replace("`", "").strip().lower()
        if verdict not in ("applies", "does not apply", "flagged"):
            raise ValueError(f"invalid verdict {verdict!r} for {reg}")
        if reg not in REGULATIONS:
            raise ValueError(f"non-canonical regulation id: {reg!r}")
        verdicts.append({"regulation": reg, "verdict": verdict, "rationale": cells[2]})
    got = [v["regulation"] for v in verdicts]
    if sorted(got) != sorted(REGULATIONS):
        raise ValueError(f"§2 must cover exactly the 5 candidate regulations; got {got}")
    return {"md": md, "verdicts": verdicts}
