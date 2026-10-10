"""aegis_pipeline.phases.phase3.verdicts — verdict parsing, verification gates, and prompt packs.

Handles parsing of model-produced verdict tables, checking them against published
control anchors and candidate cards, and merging verdicts back onto the skeleton.
"""
from __future__ import annotations

import re

from aegis_pipeline.phases.phase3.schemas import (
    MATRIX_COLUMNS,
    ORGANIZATIONAL,
    UNSET,
    VERDICTS,
)

#: Marker for a judgement cell the model did not fill.
UNFILLED = UNSET

RE_TABLE_ROW = re.compile(r"^\|(?P<cells>.+)\|\s*$")


def parse_verdicts(answer: str) -> list[dict]:
    """Parse one sub-domain's verdict table. Raises on any structural defect.

    Structure only: seven columns, a well-formed objective id, and a verdict
    inside the ADR-007 D4 vocabulary.
    """
    rows = {}
    for line in answer.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) < len(MATRIX_COLUMNS):
            continue
        oid = cells[0].strip("` ").split(" ")[0]
        if not re.match(r"^(PO|SO)-D-\d{2}\.\d-\d{3}$", oid):
            continue
        if oid in rows:
            raise ValueError(f"verdict table repeats {oid}")
        # Strip backticks and bold marks
        verdict = cells[4].replace("**", "").replace("`", "").strip()
        if verdict not in VERDICTS:
            raise ValueError(f"{oid}: verdict {verdict!r} is outside the ADR-007 D4 vocabulary")
        rows[oid] = {
            "id": oid,
            "summary": cells[1],
            "carrier": cells[2],
            "skill": cells[3],
            "verdict": verdict,
            "discharge": cells[5],
            "action": cells[6],
            "carriers_cited": sorted(set(re.findall(r"R\d+\.\d+", cells[2]))),
        }
    if not rows:
        raise ValueError("verdict table parsed to zero rows")
    return list(rows.values())


def check_verdicts(rows: list[dict], objectives: list[dict], pool: list[str]) -> list[str]:
    """Post-verdict gates. Empty list = pass."""
    findings = []
    pub = {o["id"]: set(o["anchors"]) for o in objectives}
    known = set(pool)
    wanted = {o["id"] for o in objectives}
    seen = {x["id"] for x in rows}
    for oid in sorted(wanted - seen):
        findings.append(f"{oid}: no verdict row was parsed for this objective")
    for r in rows:
        if r["id"] not in wanted:
            findings.append(f"{r['id']}: row is not an objective of this sub-domain")
        stray_cards = set(r.get("carriers_cited", [])) - known
        if stray_cards:
            findings.append(f"{r['id']}: carrier {sorted(stray_cards)} is not in the candidate pool")
        oid, v, d = r["id"], r["verdict"], r["discharge"].strip()
        empty = (not d) or d in (UNSET, "-", "—", "n/a", "N/A")
        if v == VERDICTS[0] and empty:
            findings.append(f"{oid}: Fully covered with no discharge record")
        if v == ORGANIZATIONAL and empty:
            findings.append(f"{oid}: routed to the organizational lane without naming the obligation")
        if v == "N/A" and empty:
            findings.append(f"{oid}: N/A without a reason")
        if v in (UNSET, UNFILLED):
            findings.append(f"{oid}: no verdict recorded")
        if v not in VERDICTS and v != UNSET:
            findings.append(f"{oid}: verdict {v!r} is outside the vocabulary")
    findings.extend(anchor_findings(rows, pub))
    return findings


def anchor_findings(rows: list[dict], published: dict[str, set]) -> list[str]:
    """T6: a chain may only select anchors its objective publishes."""
    findings = []
    for r in rows:
        allowed = published.get(r["id"], set())
        used = set(r.get("anchors_used", []))
        stray = used - allowed
        if stray:
            findings.append(f"{r['id']}: chain selects anchor(s) outside the published set: {sorted(stray)}")
    return findings


def apply_verdicts(skeleton: list[dict], verdicts: list[dict]) -> list[dict]:
    """Merge parsed verdicts onto the skeleton rows, preserving order."""
    by_id = {v["id"]: v for v in verdicts}
    merged = []
    for s in skeleton:
        v = by_id.get(s["id"])
        if v is None:
            merged.append(s)
            continue
        row = dict(s)
        for col in ("carrier", "skill", "verdict", "discharge", "action"):
            row[col] = v[col] if v[col] else s[col]
        row["carriers_cited"] = v.get("carriers_cited", [])
        row["anchors_used"] = s["anchors"]
        merged.append(row)
    return merged


def build_verdict_pack(rows: list[dict], cards: list[dict]) -> str:
    """The context one sub-domain's verdict call carries."""
    out = ["# Coverage rows to verdict", ""]
    for r in rows:
        out += [f"## `{r['id']}`", "",
                f"- **Regulation:** {r['regulation']}",
                f"- **Objective:** {r['summary']}",
                f"- **Published control anchors:** "
                + (", ".join(f"`{a}`" for a in r["anchors"]) if r["anchors"]
                   else "_none — this obligation has no product control anchor; if it is "
                        "discharged by a card, say so explicitly_"),
                ""]

    out += ["---", "", "# Candidate functional cards (V0 — the whole carrier pool)", ""]
    for c in cards:
        out.append(f"- `{c['id']}` **{c['name']}** — {c['description']}")

    out += ["", "---", "", "# Verdicts", "",
            "One per objective, exactly one of:"]
    out += [f"- `{v}`" for v in VERDICTS]
    out += ["",
            "Emit a markdown table with exactly these columns:",
            "`Objective | Summary | Functional carrier | Skill | State | VC discharge | Action / Round`",
            ""]
    return "\n".join(out)
