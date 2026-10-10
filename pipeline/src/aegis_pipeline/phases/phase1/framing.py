#!/usr/bin/env python3
"""aegis_pipeline.phases.phase1.framing — Stage P3f context framing table synthesis."""

from __future__ import annotations

import sys
from pathlib import Path

# Ensure pipeline/src is importable
_src = Path(__file__).resolve().parents[3]
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

from aegis_pipeline.phases.phase1.common import extract_fenced, parse_md_table

FRAMING_DIMENSIONS = [
    "Size",
    "Area of operation",
    "Regulatory roles",
    "Inherited capabilities",
]


def parse_p3f(answer: str) -> dict:
    """§2 Framing: a 2-column table with exactly the four canonical dimensions."""
    md = extract_fenced(answer, "markdown")
    rows = parse_md_table(md)
    dims: dict[str, str] = {}
    for cells in rows:
        if len(cells) != 2:
            raise ValueError(f"framing table row must have 2 columns: {cells}")
        key = " ".join(cells[0].split()).lower().rstrip(":")
        if key == "dimension":
            continue
        dims[key] = cells[1]
    missing = [d for d in FRAMING_DIMENSIONS
               if d.lower() not in dims or not dims[d.lower()].strip()]
    if missing:
        raise ValueError(
            f"framing table missing or empty dimension(s): {missing} "
            f"(expected exactly: {', '.join(FRAMING_DIMENSIONS)})"
        )
    extra = [k for k in dims if k not in [d.lower() for d in FRAMING_DIMENSIONS]]
    if extra:
        raise ValueError(f"framing table has unexpected dimension(s): {extra}")
    return {"framing": md.strip()}
