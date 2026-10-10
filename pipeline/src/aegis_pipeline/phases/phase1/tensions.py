#!/usr/bin/env python3
"""aegis_pipeline.phases.phase1.tensions — Stage P4t strategic tensions resolution and merge."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# Ensure pipeline/src is importable
_src = Path(__file__).resolve().parents[3]
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

from aegis_pipeline.phases.phase1.common import extract_fenced, parse_md_table

P4T_HEADER = "| ID | Sub-domains | Tension | Conflict | Resolution |"
P4T_SEPARATOR = "|---|---|---|---|---|"


def _cell(v: str) -> str:
    return " ".join(str(v).split())


def parse_p4t(answer: str, sd_id: str | None = None) -> dict:
    """Tension resolutions: a 5-column table, or the single line `None.`."""
    md = extract_fenced(answer, "markdown")
    if md.strip().lower().rstrip(".") == "none":
        return {"md": md, "tensions": []}
    tensions = []
    seq = 0
    for cells in parse_md_table(md):
        if not cells:
            continue
        idm = re.match(r"`?(T-\d{3})`?", cells[0].replace("*", "").strip())
        if not idm:
            continue
        if len(cells) != 5:
            raise ValueError(
                f"tension row {idm.group(1)} has {len(cells)} columns, "
                "expected 5 (ID | Sub-domains | Tension | Conflict | Resolution)"
            )
        seq += 1
        if idm.group(1) != f"T-{seq:03d}":
            raise ValueError(
                f"tension IDs must be sequential from T-001: got {idm.group(1)}"
                + (f" (sub-domain {sd_id})" if sd_id else "")
            )
        for i, name in ((2, "Tension"), (3, "Conflict"), (4, "Resolution")):
            if not cells[i].strip():
                raise ValueError(f"empty {name} cell on {idm.group(1)}")
        tensions.append({
            "id": idm.group(1),
            "subdomains": cells[1],
            "tension": cells[2],
            "conflict": cells[3],
            "resolution": cells[4],
        })
    if not tensions:
        raise ValueError(
            "no T-NNN rows and no `None.` marker in the p4t answer"
            + (f" (sub-domain {sd_id})" if sd_id else "")
        )
    return {"md": md, "tensions": tensions}


def merge_tensions(per_sd: list[dict]) -> dict:
    """Renumber per-sub-domain p4t answers into one unified `T-NNN` sequence."""
    rows: list[dict] = []
    for entry in per_sd:
        rows.extend(dict(t) for t in entry.get("tensions", []))
    for i, t in enumerate(rows, 1):
        t["id"] = f"T-{i:03d}"
    if not rows:
        md = "None."
    else:
        md = "\n".join([P4T_HEADER, P4T_SEPARATOR] + [
            f"| {t['id']} | {_cell(t['subdomains'])} | {_cell(t['tension'])} | "
            f"{_cell(t['conflict'])} | {_cell(t['resolution'])} |" for t in rows
        ])
    return {"md": md, "tensions": rows, "assumptions": []}


def p4t_extra_instruction(sd_id: str) -> str:
    """The p4t wrap instruction, scoped to one sub-domain (ADR-012 D1)."""
    return (
        f"Wrap your answer: return ONLY one ```markdown fenced block containing the "
        f"tension-resolution table `| ID | Sub-domains | Tension | Conflict | "
        f"Resolution |`, one row per tension of THIS sub-domain that activates on this "
        f"company, or ONLY the line `None.` inside the fence when none of them does. "
        f"SCOPE: this call resolves sub-domain {sd_id} alone — the attached pack carries "
        f"the Emergent-tensions sections of that sub-domain and no other, and every "
        f"selected sub-domain is resolved in its own call. Column rules: `Sub-domains` "
        f"cites the canonical id `{sd_id}` (R1); `ID` restarts at `T-001` and runs "
        f"sequentially, because the delivered table renumbers the whole set at merge — a "
        f"gap or a number above 001 here is a defect. `Tension` names the conflict "
        f"concisely, `Conflict` states which duties collide and on what operational "
        f"dimension (clock, recipient, scope, competence), `Resolution` adopts ONE "
        f"auditable binding rule for this company (e.g. strictest timeline binds per "
        f"recipient; parallel recipients keep their own clocks) — never `TBD`. Skip a "
        f"corpus tension whose triggering condition does not hold for this company: that "
        f"is not a silent drop, it does not activate. Technology-neutral (R5); no "
        f"obligation invented beyond the corpus tensions the pack quotes (R8). "
        f"Nothing else."
    )


def store_tension_slice(run_dir: Path, sd_id: str, parsed: dict) -> None:
    """One sub-domain's p4t answer slice."""
    d = run_dir / "steps" / "tensions"
    d.mkdir(exist_ok=True)
    (d / f"{sd_id}.md").write_text(parsed["md"] + "\n", encoding="utf-8")
    (d / f"{sd_id}.json").write_text(
        json.dumps({"subdomain": sd_id, "tensions": parsed["tensions"]},
                   indent=1, ensure_ascii=False), encoding="utf-8"
    )


def load_tension_slices(run_dir: Path, sd_ids: list[str]) -> list[dict]:
    """The per-sub-domain p4t slices in canonical sub-domain order."""
    d = run_dir / "steps" / "tensions"
    return [
        json.loads((d / f"{sd}.json").read_text(encoding="utf-8"))
        for sd in sd_ids if (d / f"{sd}.json").exists()
    ]
