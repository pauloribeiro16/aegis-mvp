"""Wave 5 — the organizational lane: duties, not verdict rows.

The measured shape (Case 01 audit, 2026-10-10): 32 organizational verdict rows
collapse to 16 duties (17 ORG / 13 SCALE / 2 CARRIED dispositions) because the
taxonomy organises by sub-domain and the duties cut across it. The grouping key
is the audited duty assignment — a routing rule written from the matrix alone
would emit one requirement per row, which is exactly the 1:1 failure the audit
records (32 EARS cards for an 8-person company). The audit file is therefore a
deterministic INPUT here, parsed — never re-derived by a model.
"""

from __future__ import annotations

import re
from pathlib import Path

RE_DUTY_ROW = re.compile(
    r"^\|\s*`(?P<id>(?:PO|SO)-D-\d{2}\.\d-\d{3})`\s*\|(?P<duty>[^|]+)\|"
    r"\s*\*\*(?P<disposition>ORG|SCALE|CARRIED)\*\*\s*\|(?P<warrant>[^|]+)\|"
)

ORG_VERDICT = "No functional carrier (organizational)"
DISPOSITIONS = ("ORG", "SCALE", "CARRIED")


def parse_duty_audit(path: Path) -> dict[str, dict]:
    """Parse the §3 audit table: objective → duty, disposition, warrant."""
    out: dict[str, dict] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = RE_DUTY_ROW.match(line.strip())
        if not m:
            continue
        if m["id"] in out:
            raise ValueError(f"duty audit: {m['id']} appears twice")
        out[m["id"]] = {
            "duty": m["duty"].strip(),
            "disposition": m["disposition"],
            "warrant": m["warrant"].strip(),
        }
    if not out:
        raise ValueError(f"duty audit: no rows parsed from {path}")
    unknown = sorted(d for d in {v["disposition"] for v in out.values()} if d not in DISPOSITIONS)
    if unknown:
        raise ValueError(f"duty audit: dispositions outside {DISPOSITIONS}: {unknown}")
    return out


def group_duties(rows: list[dict], duty_map: dict[str, dict]) -> list[dict]:
    """Collapse organizational verdict rows into duties.

    Every organizational row must be covered by the duty map; a row the audit
    does not know about is a finding, not a silent drop. Returns one entry per
    distinct duty with its objectives and the disposition split.
    """
    duties: dict[str, dict] = {}
    uncovered: list[str] = []
    for row in rows:
        if row.get("verdict") != ORG_VERDICT:
            continue
        assignment = duty_map.get(row["id"])
        if assignment is None:
            uncovered.append(row["id"])
            continue
        duty = duties.setdefault(
            assignment["duty"],
            {"duty": assignment["duty"], "objectives": [], "dispositions": {}, "warrants": []},
        )
        duty["objectives"].append(row["id"])
        duty["dispositions"][assignment["disposition"]] = (
            duty["dispositions"].get(assignment["disposition"], 0) + 1
        )
        if assignment["warrant"] and assignment["warrant"] not in duty["warrants"]:
            duty["warrants"].append(assignment["warrant"])
    if uncovered:
        raise ValueError(f"duty grouping: {len(uncovered)} organizational rows not in the duty map: {uncovered[:8]}")
    ordered = sorted(duties.values(), key=lambda d: (min(d["objectives"]), d["duty"]))
    for duty in ordered:
        duty["subdomain"] = duty["objectives"][0].split("-")[1]  # D-XX.Y do 1.º objectivo
    return ordered


def count_dispositions(duties: list[dict]) -> dict[str, int]:
    totals = {d: 0 for d in DISPOSITIONS}
    for duty in duties:
        for disposition, n in duty["dispositions"].items():
            totals[disposition] += n
    return totals


# ---------------------------------------------------------------------------
# The ORG card call — the model writes the EARS card, the code allocates ids.
# ---------------------------------------------------------------------------

ORG_FIELDS = ("Statement (EARS)", "Requirement Origin", "Fit Criterion", "Verification Method", "Chain", "Control Anchors", "Dependencies", "Priority")
ORG_METHODS = ("TEST", "INSPECT", "DEMONSTRATE", "ANALYZE")
RE_EARS = re.compile(r"\bshall\b", re.IGNORECASE)


def parse_org_card(answer: str, duty: str) -> dict:
    """L0 for one duty's organizational requirement card."""
    from aegis_pipeline.phases.phase1.common import extract_fenced

    block = extract_fenced(answer, "markdown").strip()
    fields: dict[str, str] = {}
    for field in ORG_FIELDS:
        m = re.search(rf"\*\*{re.escape(field)}:?\*\*\s*(.+)", block)
        if not m:
            raise ValueError(f"org card [{duty}]: missing field {field!r}")
        fields[field] = m.group(1).strip()
    statement = fields["Statement (EARS)"]
    if not RE_EARS.search(statement):
        raise ValueError(f"org card [{duty}]: statement is not EARS — no 'shall'")
    if not statement.rstrip(".").endswith(tuple("abcdefghijklmnopqrstuvwxyz)")) and len(statement) < 40:
        raise ValueError(f"org card [{duty}]: statement too short to be a requirement")
    if fields["Verification Method"] not in ORG_METHODS:
        raise ValueError(f"org card [{duty}]: Verification Method {fields['Verification Method']!r} not in {ORG_METHODS}")
    if not fields["Fit Criterion"]:
        raise ValueError(f"org card [{duty}]: empty fit criterion (Volere binary required)")
    anchors = [a.strip().strip("`") for a in fields["Control Anchors"].split(",") if a.strip()]
    if not anchors:
        raise ValueError(f"org card [{duty}]: no control anchors (NIST CSF GOVERN required)")
    if fields["Priority"] not in ("Must", "Should"):
        raise ValueError(f"org card [{duty}]: Priority {fields['Priority']!r} not Must/Should")
    return {"duty": duty, **fields, "_anchor_list": anchors}


def check_org_anchor_files(repo: Path, parsed: dict) -> None:
    """Every cited anchor must exist as a JSON under baseline/CONTROLS (R2)."""
    from aegis_pipeline.guards.quality_gates import check_no_technology

    findings = check_no_technology(parsed["Statement (EARS)"], parsed["Fit Criterion"])
    if findings:
        raise ValueError(f"org card [{parsed['duty']}]: technology vocabulary (R5): {findings}")
    controls_root = repo / "baseline" / "CONTROLS"
    for anchor in parsed["_anchor_list"]:
        hits = list(controls_root.rglob(f"{anchor}.json"))
        if not hits:
            raise ValueError(
                f"org card [{parsed['duty']}]: anchor {anchor!r} resolves to no file under baseline/CONTROLS (R2)"
            )


def render_doc03(
    duties: list[dict],
    cards: list[dict],
    company: str,
    confirmed_regs: list[str],
) -> str:
    """Compose the organizational deliverable in the hand-written Doc03's structure."""
    lines = [
        "---",
        f"title: 'Doc03 — Organizational Requirements ({company})'",
        "generated_by: 'p3a_org (wave 5)'",
        "status: PROPOSED — routed duties until the acceptance round",
        "---",
        "",
        f"# Doc03 — Organizational Requirements — {company}",
        "",
        "## §1 Derivation contract",
        "",
        "EARS with an organizational subject (`The organization shall …`), one atomic",
        "requirement per duty, binary Volere fit criterion, verification method, and a",
        "chain `regulation article → Phase 2 objective → organizational control anchor`",
        "(NIST CSF 2.0 GOVERN + advisory surfaces, R2b). IDs are allocated by the",
        "pipeline per duty, never per verdict row (ADR-008 D4).",
        "",
        "## §3 Requirements",
        "",
    ]
    for index, (duty, card) in enumerate(zip(duties, cards), start=1):
        org_id = f"ORG-{duty['subdomain']}-{index:03d}"
        lines += [
            f"### {org_id} — {duty['duty']}",
            "",
            f"**Statement (EARS):** {card['Statement (EARS)']}",
            "",
            f"**Requirement Origin:** {card['Requirement Origin']}",
            "",
            f"**Fit Criterion:** {card['Fit Criterion']}",
            "",
            f"**Verification Method:** {card['Verification Method']}",
            "",
            f"**Chain:** {card['Chain']}",
            "",
            f"**Control Anchors:** {card['Control Anchors']}",
            "",
            f"**Dependencies:** {card['Dependencies']}",
            "",
            f"**Priority:** {card['Priority']}",
            "",
            f"**Objectives routed:** {', '.join(f'`{o}`' for o in duty['objectives'])}",
            "",
        ]
    pending = [d for d in duties if "SCALE" in d["dispositions"]]
    lines += ["## §5 Objectives routed but not yet specified (SCALE)", ""]
    if pending:
        for duty in pending:
            lines.append(f"- {duty['duty']} — objectives: {', '.join(f'`{o}`' for o in duty['objectives'])} — pending the proportionality decision (G-c)")
    else:
        lines.append("None.")
    lines.append("")
    lines.append(f"Confirmed regulations: {', '.join(confirmed_regs)}.")
    return "\n".join(lines) + "\n"
