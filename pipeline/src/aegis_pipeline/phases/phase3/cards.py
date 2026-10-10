"""Wave 2 — the V0 functional baseline, one card at a time.

The stage (`p3a_cards`) makes one inventory call and one call per card; each
card call returns the 7-row requirement card, its PUC table row and its
Level-1 use case. This module owns the L0 contract: what a card, a PUC and a
use case must look like to be accepted, and the deterministic composition of
the V0 deliverables from the accepted cards.
"""

from __future__ import annotations

import re

from aegis_pipeline.guards.quality_gates import check_no_technology

RE_CARD_ID = re.compile(r"^R\d+\.\d+$")
RE_PUC_ID = re.compile(r"^PUC\s+\d+\.\d+$")
RE_UC_ID = re.compile(r"^\{U\.C\.\s*\d+\.\d+\}$")

# R13 anti-pattern 7 — "User Account Management" instead of "Manage User
# Accounts". Heuristic, not the altitude instrument: it rejects the canonical
# nominalizations, the L2 scorer judges the rest.
NOMINAL_SUFFIXES = (
    "management",
    "handling",
    "administration",
    "provisioning",
    "monitoring",
    "processing",
    "lifecycle",
    "tracking",
)

CARD_ROWS = ("ID", "Description", "Requirement Origin", "Interfaces", "Dependencies", "Identified Problems", "Priority")
PRIORITIES = ("Must", "Should", "Could", "Won't")
UC_FIELDS = ("Traceability", "Primary Actor", "Preconditions", "Trigger", "Main Success Scenario", "Extensions", "Success Guarantees", "Minimal Guarantees")


def _fenced_markdown(answer: str) -> str:
    from aegis_pipeline.phases.phase1.common import extract_fenced

    return extract_fenced(answer, "markdown").strip()


def _split_sections(block: str) -> dict[str, str]:
    sections: dict[str, str] = {}
    current: str | None = None
    for line in block.splitlines():
        if line.startswith("####"):
            current = line.lstrip("#").strip()
            sections[current] = ""
        elif current is not None:
            sections[current] += line + "\n"
    return sections


def parse_inventory(answer: str) -> dict:
    """L0 for the inventory call: a table `| Card | Name | Business basis |`."""
    block = _fenced_markdown(answer)
    rows: list[dict] = []
    seen: set[str] = set()
    for line in block.splitlines():
        line = line.strip()
        if not line.startswith("|") or set(line) <= {"|", "-", " ", ":"}:
            continue
        cells = [c.strip().strip("`") for c in line.strip("|").split("|")]
        if len(cells) != 3 or cells[0] in ("Card", "Card ID"):
            continue
        if not RE_CARD_ID.match(cells[0]):
            raise ValueError(f"inventory: card id {cells[0]!r} is not `R<n>.<m>`")
        if cells[0] in seen:
            raise ValueError(f"inventory: card {cells[0]} appears more than once")
        if not cells[1]:
            raise ValueError(f"inventory: card {cells[0]} has an empty Name")
        if not cells[2]:
            raise ValueError(f"inventory: card {cells[0]} has an empty Business basis")
        seen.add(cells[0])
        rows.append({"id": cells[0], "name": cells[1], "basis": cells[2]})
    if len(rows) < 5:
        raise ValueError(f"inventory: only {len(rows)} cards parsed — a product has more than that")
    return {"cards": rows}


def parse_card(answer: str) -> dict:
    """L0 for one card call: `#### Card`, `#### PUC`, `#### Use case` sections."""
    block = _fenced_markdown(answer)
    sections = _split_sections(block)
    card_sec = next((v for k, v in sections.items() if k.lower().startswith("card")), None)
    puc_sec = next((v for k, v in sections.items() if k.lower().startswith("puc")), None)
    uc_sec = next((v for k, v in sections.items() if k.lower().startswith("use case")), None)
    if not (card_sec and puc_sec and uc_sec):
        raise ValueError(
            "card call: expected three `####` sections — Card, PUC, Use case — "
            f"got {sorted(sections)!r}"
        )

    # Card: the 7-row table, `| <n> | <Row label> | <content> |`
    rows: dict[str, str] = {}
    for line in card_sec.splitlines():
        line = line.strip()
        if not line.startswith("|") or set(line) <= {"|", "-", " ", ":"}:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) != 3 or not cells[1].strip():
            continue
        label = cells[1].strip().strip("*").rstrip(":").strip()
        if label in CARD_ROWS:
            rows[label] = cells[2].strip().strip("`")
    missing = [row for row in CARD_ROWS if row not in rows]
    if missing:
        raise ValueError(f"card: missing rows {missing}")
    for row in ("ID", "Description", "Requirement Origin", "Priority"):
        if not rows[row].strip():
            raise ValueError(f"card: row {row!r} is empty")
    m = re.match(r"^(R\d+\.\d+)\s*[—–-]\s*(.+)$", rows["ID"])
    if not m:
        raise ValueError(f"card: ID row {rows['ID']!r} must be `R<n>.<m> — <Active verb name>`")
    card_id, name = m.group(1), m.group(2).strip()
    if name.lower().rstrip(".").endswith(NOMINAL_SUFFIXES):
        raise ValueError(
            f"card: name {name!r} is a nominalization (R13) — use the active verb form"
        )
    if rows["Priority"] not in PRIORITIES:
        raise ValueError(f"card: Priority {rows['Priority']!r} not in {PRIORITIES}")

    # PUC: one 5-column row under the header
    puc_cells: list[str] = []
    for line in puc_sec.splitlines():
        line = line.strip()
        if not line.startswith("|") or set(line) <= {"|", "-", " ", ":"}:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) == 5 and RE_PUC_ID.match(cells[0]):
            puc_cells = cells
            break
    if not puc_cells:
        raise ValueError("card: no PUC row with 5 columns (`PUC <n>.<m>` first cell)")

    # Use case: the fully-dressed fields
    uc_id_match = re.search(r"\{U\.C\.\s*\d+\.\d+\}", uc_sec)
    if not uc_id_match:
        raise ValueError("card: use case has no `{U.C. n.m}` id")
    fields: dict[str, str] = {}
    for field in UC_FIELDS:
        m = re.search(rf"\*\*{re.escape(field)}:?\*\*\s*(.+)", uc_sec)
        if not m:
            raise ValueError(f"card: use case missing {field!r}")
        fields[field] = m.group(1).strip()
    scenario = fields["Main Success Scenario"]
    steps = re.findall(r"(?:^|\s)(\d+)\.\s+", scenario)
    if len(steps) < 3:
        raise ValueError("card: Main Success Scenario needs ≥3 numbered actor/system steps")
    if card_id not in fields["Traceability"]:
        raise ValueError(
            f"card: use case traceability {fields['Traceability']!r} does not cite {card_id}"
        )

    card = {
        "id": card_id,
        "name": name,
        "description": rows["Description"],
        "origin": rows["Requirement Origin"],
        "interfaces": rows["Interfaces"],
        "dependencies": rows["Dependencies"],
        "problems": rows["Identified Problems"],
        "priority": rows["Priority"],
        "puc": dict(zip(("puc_id", "trigger", "actor", "boundary", "outputs"), puc_cells)),
        "usecase": {"uc_id": uc_id_match.group(0), **fields},
    }
    return {"card": card}


def check_card_quality(parsed: dict) -> dict:
    """Content gates over one parsed card — raises like `check_p4_quality`."""
    card = parsed["card"]
    texts = (card["name"], card["description"], card["origin"], card["interfaces"], card["dependencies"])
    findings = check_no_technology(*texts)
    if findings:
        raise ValueError(f"card {card['id']}: technology vocabulary (R5/L4): {findings}")
    return parsed


# ---------------------------------------------------------------------------
# Deterministic composition — the V0 deliverables from the accepted cards.
# ---------------------------------------------------------------------------


def render_v0_doc01(cards: list[dict], company: str) -> str:
    groups: dict[str, list[dict]] = {}
    for card in cards:
        groups.setdefault(card["id"].split(".")[0], []).append(card)
    lines = [
        "---",
        f"title: 'Doc01 — Requirements Elicitation and PUC ({company})'",
        "generated_by: 'p3a_cards (wave 2)'",
        "status: PROPOSED — V0 until the acceptance round",
        "---",
        "",
        f"# Doc01 — Requirements Elicitation and PUC — {company}",
        "",
        "## Part I — Requirements by package",
        "",
    ]
    for group in sorted(groups):
        lines.append(f"### Package R{group}")
        lines.append("")
        for card in groups[group]:
            lines.append(f"#### Card {card['id']} — {card['name']}")
            lines.append("")
            lines.append("| # | Row | Content |")
            lines.append("|---|---|---|")
            lines.append(f"| 1 | ID | {card['id']} — {card['name']} |")
            lines.append(f"| 2 | Description | {card['description']} |")
            lines.append(f"| 3 | Requirement Origin | {card['origin']} |")
            lines.append(f"| 4 | Interfaces | {card['interfaces']} |")
            lines.append(f"| 5 | Dependencies | {card['dependencies']} |")
            lines.append(f"| 6 | Identified Problems | {card['problems'] or '—'} |")
            lines.append(f"| 7 | Priority | {card['priority']} |")
            lines.append("")
    lines += ["## Part II — Product Use Case catalogue", "", "| PUC ID | Business Trigger | Primary Actor | System Operational Boundary | Deliverables & Outputs |", "|---|---|---|---|---|"]
    for card in cards:
        p = card["puc"]
        lines.append(f"| {p['puc_id']} | {p['trigger']} | {p['actor']} | {p['boundary']} | {p['outputs']} |")
    lines.append("")
    return "\n".join(lines) + "\n"


def render_v0_doc02(cards: list[dict], company: str) -> str:
    lines = [
        "---",
        f"title: 'Doc02 — System Use Cases ({company})'",
        "generated_by: 'p3a_cards (wave 2)'",
        "status: PROPOSED — V0 until the acceptance round",
        "---",
        "",
        f"# Doc02 — System Use Cases — {company}",
        "",
    ]
    for card in cards:
        uc = card["usecase"]
        lines.append(f"## {uc['uc_id']} — {card['name']}")
        lines.append("")
        for field in UC_FIELDS:
            lines.append(f"**{field}:** {uc[field]}")
            lines.append("")
    return "\n".join(lines) + "\n"
