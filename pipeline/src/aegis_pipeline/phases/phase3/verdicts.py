"""aegis_pipeline.phases.phase3.verdicts — verdict parsing, verification gates, and prompt packs.

Handles parsing of model-produced verdict tables, checking them against published
control anchors and candidate cards, and merging verdicts back onto the skeleton.
"""
from __future__ import annotations

import re

from aegis_pipeline.phases.phase3.schemas import (
    ACTIONS,
    MATRIX_COLUMNS,
    ORGANIZATIONAL,
    UNSET,
    VERDICTS,
)

#: Marker for a judgement cell the model did not fill.
UNFILLED = UNSET

RE_TABLE_ROW = re.compile(r"^\|(?P<cells>.+)\|\s*$")

#: The shape of a control anchor as the model cites it in prose (`GV.RR-02`).
#: One pattern, three readers: the parser, the merge and the fallback re-derive
#: the same citation set, so a disagreement between them cannot be silent.
RE_ANCHOR_CITE = re.compile(r"`?([A-Z]{2}\.[A-Z]{2}-(?:\d+|P\d+|[A-Z0-9]+))`?")


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
        discharge = cells[5]
        # The Action column is a pure enum (R10b inv. 2): the routing decision
        # is a category, the justification lives in the discharge. Free text
        # here is what the proposal selector had to substring-mine.
        action = cells[6].replace("**", "").replace("`", "").strip()
        if action not in ACTIONS:
            raise ValueError(f"{oid}: action {action!r} is outside the routing enum {ACTIONS}")
        # S5/S6: what the model actually cited, in the summary AND the
        # discharge. Scanning only the discharge let a chain that names its
        # anchor in the summary pass T3 with an invented one, and the old
        # `anchors_used = s["anchors"]` merge handed every silent row the full
        # published set — the one assignment that can never fail a check.
        anchors_cited = sorted(set(
            RE_ANCHOR_CITE.findall(f"{cells[1]} {discharge}")))
        rows[oid] = {
            "id": oid,
            "summary": cells[1],
            "carrier": cells[2],
            "skill": cells[3],
            "verdict": verdict,
            "discharge": discharge,
            "action": action,
            "carriers_cited": sorted(set(re.findall(r"R\d+\.\d+", cells[2]))),
            "anchors_cited": anchors_cited,
        }
    if not rows:
        raise ValueError("verdict table parsed to zero rows")
    return list(rows.values())


def verdict_defects(rows: list[dict], objectives: list[dict], pool: list[str]) -> list[str]:
    """The per-call defects an L0 repair round may fix.

    These are the checks that used to run only AFTER the call returned, so a
    row that named no anchor cost the whole sub-domain: the stage caught the
    finding, dropped the sub-domain, and 11 objectives went to the matrix with
    no verdict at all. A defect the model can repair belongs in `_validate`,
    where the repair round lives.
    """
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
        if v == VERDICTS[0] and not empty and pub.get(oid) and not r.get("anchors_cited"):
            findings.append(
                f"{oid}: fully covered but cites no anchor — the objective publishes "
                f"{len(pub[oid])}; a discharge that names none is unverifiable (T3)"
            )
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


def check_verdicts(rows: list[dict], objectives: list[dict], pool: list[str]) -> list[str]:
    """The batch gate: the repairable defects plus the mode-collapse alert."""
    findings = verdict_defects(rows, objectives, pool)
    # Onda C L1 — the mode-collapse alert (M-26, registered in METRICS.md).
    # The measured run pushed 52 of 65 objectives into the organizational
    # lane; a batch where the technical domains D-02..D-07 route >65%
    # organizational is that failure recurring, and it says so instead of
    # passing silently.
    #
    # The scope D-02..D-07 was checked against the data before it was trusted:
    # the collapsed arms of the calibration measure 68–78% in this scope (the
    # alert fires) and the healthy arms 12–21% (it stays quiet). A narrower
    # "product domains" scope (D-01, D-03, D-05, D-07) was measured too and
    # measured WORSE — 50–59% on the collapsed arms, because D-03 held at
    # 25%/0% while D-01 collapsed to 62–75% — so it was not adopted.
    tech = [r for r in rows if str(r.get("subdomain", ""))[:4] in {f"D-0{n}" for n in range(2, 8)}]
    if len(tech) >= 5:
        org_share = sum(1 for r in tech if r["verdict"] == ORGANIZATIONAL) / len(tech)
        if org_share > 0.65:
            findings.append(
                f"mode collapse: {org_share:.0%} of the {len(tech)} technical-domain "
                f"objectives (D-02..D-07) route organizational — above the 65% alert; "
                "a software product carries most of these, re-read the carriers")
    return findings


def anchor_findings(rows: list[dict], published: dict[str, set]) -> list[str]:
    """T6/T3: a chain may only select anchors its objective publishes.

    Reads the merged row's `anchors_used` and falls back to the parser's
    `anchors_cited`, so the check also runs on rows straight out of
    `parse_verdicts` — the citation set the model produced is the source of
    truth in either shape.
    """
    findings = []
    for r in rows:
        allowed = published.get(r["id"], set())
        used = set(r.get("anchors_used") or r.get("anchors_cited") or [])
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
        cited = v.get("anchors_cited")
        if cited is None:
            cited = sorted(set(RE_ANCHOR_CITE.findall(v.get("discharge", ""))))
        # What the row cites, and nothing else. Inheriting the published set
        # here made `anchors_used` a tautology: T3 compared the objective's own
        # anchors with themselves and could never find an invention.
        row["anchors_used"] = cited
        merged.append(row)
    return merged


def build_verdict_pack(rows: list[dict], cards: list[dict],
                       rules: dict[str, list[dict]] | None = None) -> str:
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
        for rule in (rules or {}).get(r["id"], []):
            out += [f"  - **Phase 2 rule `{rule['rule_id']}`** — {rule.get('statement', '')}"
                    + (f" (verify: `{rule['verification_target']}`)"
                       if rule.get("verification_target") else ""),
                    ""]

    out += ["---", "", "# Candidate functional cards (V0 — the whole carrier pool)", ""]
    for c in cards:
        out.append(f"- `{c['id']}` **{c['name']}** — {c['description']}")

    out += ["", "---", "", "# Verdicts", "",
            "One verdict per objective, exactly one of:"]
    out += [f"- `{v}`" for v in VERDICTS]
    out += ["",
            "The Action column is a pure enum, exactly one of:"]
    out += [f"- `{a}`" for a in ACTIONS]
    out += ["",
            "Emit a markdown table with exactly these columns:",
            "`Objective | Summary | Functional carrier | Skill | State | VC discharge | Action`",
            ""]
    return "\n".join(out)
