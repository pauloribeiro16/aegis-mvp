#!/usr/bin/env python3
"""aegis_pipeline.phases.phase1.selection — Stage P3 sub-domain subset selection."""

from __future__ import annotations

import re
import sys
from pathlib import Path

# Ensure pipeline/src is importable
_src = Path(__file__).resolve().parents[3]
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

from compose import SD_RE
from aegis_pipeline.phases.phase1.common import extract_fenced, parse_md_table


def parse_p3(answer: str, candidates: list[str]) -> dict:
    """Parse and validate stage P3 sub-domain selection table."""
    md = extract_fenced(answer, "markdown")
    rows = parse_md_table(md)
    selected, seen = [], set()
    for cells in rows:
        if not cells:
            continue
        m = SD_RE.match(cells[0].replace("`", "").strip())
        if m:
            if len(cells) < 3 or not cells[1] or not cells[2]:
                raise ValueError(f"selection row incomplete for {cells[0]}: {cells}")
            sid = cells[0].replace("`", "").strip()
            if sid in seen:
                raise ValueError(f"duplicate selection row: {sid}")
            if sid not in candidates:
                raise ValueError(f"selected sub-domain {sid} is not in the candidate set")
            seen.add(sid)
            selected.append({"id": sid, "name": cells[1], "rationale": cells[2]})
    exc_match = re.search(r"Excluded candidates:?\s*(.*)$", md, re.S | re.I)
    excluded, exc_seen = [], set()
    if exc_match:
        for line in exc_match.group(1).splitlines():
            line = line.strip().lstrip("-").strip()
            m = re.match(r"`?(D-\d{2}\.\d)`?\s*[—:-]\s*(.+)", line)
            if m:
                sid, why = m.group(1), m.group(2).strip()
                if sid in exc_seen:
                    raise ValueError(f"duplicate exclusion: {sid}")
                if sid in seen:
                    raise ValueError(f"sub-domain {sid} appears both selected and excluded")
                if sid not in candidates:
                    raise ValueError(f"excluded sub-domain {sid} is not in the candidate set")
                exc_seen.add(sid)
                excluded.append({"id": sid, "why": why})
    got = seen | exc_seen
    missing = sorted(set(candidates) - got)
    if missing:
        raise ValueError(f"candidates neither selected nor excluded (silent drop): {missing}")
    if not selected:
        raise ValueError("empty selection — the pipeline cannot continue")
    return {"md": md, "selected": selected, "excluded": excluded}
