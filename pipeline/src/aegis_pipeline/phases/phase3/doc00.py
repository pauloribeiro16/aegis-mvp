"""Wave 5b — Doc00 is COMPOSED, not generated (doc 08 §wave 5).

A model rewriting company input restates it — the recorded failure is Case 03's
Phase 2 Doc02 carrying Case 02's architecture. Everything here is assembled
deterministically from the run's own artifacts: the Phase 1 fact sheet, the V0
card catalogue, and the trust-boundary (TB) verdict rows. Zero model calls.
"""

from __future__ import annotations

import json
import re
from pathlib import Path


def load_fact_sheet(run_dir: Path) -> dict:
    """Read the fact sheet with the reader that owns its dialect.

    The fact sheet is the flat YAML subset `parse_simple_yaml` documents — top
    level `key: value`, inline lists, block lists, folded continuations — and
    `parse_p1` validates it with exactly that reader. `yaml.safe_load` was used
    here instead and rejected the file: a scalar containing `: ` (the product
    summary does) is a nested mapping to a strict parser and a plain string to
    ours. Two readers over one artefact is the hazard; this is now the one
    reader, and Doc00 gets the same dict Phase 1 validated.

    The dialect splits an inline list on commas, so a list value containing a
    comma arrives split. That reading is Phase 1's too — it is not introduced
    here — and the fix belongs with the producer, not with the reader.
    """
    from compose import parse_simple_yaml

    path = run_dir / "steps" / "fact_sheet.yaml"
    data = parse_simple_yaml(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not data:
        raise ValueError(f"fact sheet {path} did not parse to a mapping")
    return data


def load_cards(run_dir: Path) -> list[dict]:
    """The accepted V0 catalogue — run-generated when present, else the case's frozen V0 via steps/."""
    cards_dir = run_dir / "steps" / "phase3" / "cards"
    cards: list[dict] = []
    for path in sorted(cards_dir.glob("R*.json")):
        cards.append(json.loads(path.read_text(encoding="utf-8"))["card"])
    return cards


def render_doc00(
    company: str,
    fact_sheet: dict,
    cards: list[dict],
    tb_rows: list[dict],
) -> str:
    """Parts I–IV: fact sheet, actors from the card catalogue, PUCs, trust zones.

    Two rules the earlier renderer broke. It asked the fact sheet for field
    names that do not exist in the Phase 1 schema (`size`, `jurisdiction`,
    `products_services`, `infrastructure`), so four bullets always read `—`
    while the data sat in the file under `size_employees`, `jurisdictions`,
    `product_summary` and `hosting`. And it dropped the fields it did not ask
    for, including `open_questions` — where the honest "the intake does not
    say" lives.
    """

    def fact(*keys: str, fallback: str = "—") -> str:
        """First non-empty value among `keys`.

        A name that does not resolve must not read as a fact that does not
        exist, so every caller passes the spellings that can carry the fact.
        """
        for key in keys:
            value = fact_sheet.get(key)
            if isinstance(value, list):
                joined = ", ".join(str(v) for v in value if v)
                if joined:
                    return joined
            elif value not in (None, "", [], {}):
                return str(value)
        return fallback

    def yes_no(value: str) -> str:
        return {"true": "yes", "false": "no"}.get(value.strip().lower(), value)

    # Not every card is functional: the constraint-absorption cards the weave
    # stage allocates (carrier `new`) carry an objective and a constraint, not a
    # product use case. Reading `card["puc"]` unguarded crashed the renderer
    # whenever p3a_org ran after p3a_weave.
    puc_cards = [c for c in cards if isinstance(c.get("puc"), dict)]

    actors: dict[str, dict[str, list[str]]] = {}
    for card in puc_cards:
        puc = card["puc"]
        actor = str(puc.get("actor") or "—").strip()
        entry = actors.setdefault(actor, {"pucs": [], "cards": []})
        if puc.get("puc_id"):
            entry["pucs"].append(str(puc["puc_id"]))
        if card.get("id"):
            entry["cards"].append(str(card["id"]))

    lines = [
        "---",
        f"title: 'Doc00 — Process and Operational Workflows ({company})'",
        "generated_by: 'p3a_org (wave 5) — deterministic composition'",
        "---",
        "",
        f"# Doc00 — Business Context, Process Models & Product Use Cases — {company}",
        "",
        "## Scope",
        "",
        "This document carries the company context the requirements were derived from, the",
        "operational actors those requirements bind, the product use case catalogue, and the",
        "security and trust zones recorded in the coverage matrix.",
        "",
        "It does not carry the As-Is operational model — roles in context before the tool, the",
        "current manual workflow, or an inefficiency register. No artifact of the pipeline",
        "encodes that state: the intake records what the company handles, not how work is done",
        "today. It is absent rather than estimated.",
        "",
        "## Part I — Scope and Organizational Context",
        "",
        f"- **Company:** {company}",
        f"- **Sector:** {fact('sector')}",
        f"- **Size (employees):** {fact('size_employees', 'size')}",
        f"- **Jurisdiction:** {fact('jurisdictions', 'jurisdiction')}",
        f"- **Legal form:** {fact('legal_form')}",
        f"- **Develops the software itself:** {yes_no(fact('develops_software'))}",
        f"- **Products / services:** {fact('product_summary', 'products_services')}",
        "",
        "### Data handled",
        "",
        f"- **Data categories:** {fact('data_categories')}",
        f"- **Data subjects:** {fact('data_subjects')}",
        f"- **Sensitive data:** {fact('sensitive_data', fallback='none declared')}",
        f"- **Data scale:** {fact('data_scale')}",
        "",
        "### Operating model",
        "",
        f"- **Hosting:** {fact('hosting')}",
        f"- **Access model:** {fact('access_model')}",
        f"- **Third-party processing:** {fact('third_party_processing', fallback='none declared')}",
        "",
        "### Assumed regulations",
        "",
    ]
    regulations = fact_sheet.get("assumed_regulations") or []
    if isinstance(regulations, list) and regulations:
        lines += [f"- {r}" for r in regulations]
    else:
        lines.append(f"- {fact('assumed_regulations')}")

    open_questions = fact_sheet.get("open_questions") or []
    if isinstance(open_questions, list) and open_questions:
        lines += [
            "",
            "### What the intake does not say",
            "",
            "Stated rather than resolved — an estimate here would be an invention.",
            "",
        ]
        lines += [f"- {q}" for q in open_questions]

    lines += [
        "",
        "## Part II — Operational Actors and Interaction Model",
        "",
        "Actors derived from the requirement cards. The category column of the reference",
        "deliverable (internal user / external user / external system) is not derivable from a",
        "card and is therefore not asserted here.",
        "",
        "| Actor | Use cases triggered | Realizing requirements |",
        "|---|---|---|",
    ]
    for actor in sorted(actors):
        entry = actors[actor]
        lines.append(
            f"| {actor} | {', '.join(entry['pucs']) or '—'} | {', '.join(entry['cards']) or '—'} |"
        )
    if not actors:
        lines.append("| — | — | No product use case cards were produced for this run. |")

    if actors:
        lines += ["", "```mermaid", "flowchart LR"]
        for index, actor in enumerate(sorted(actors), start=1):
            lines.append(f'  A{index}["{actor.replace(chr(34), chr(39))}"]')
        for index, actor in enumerate(sorted(actors), start=1):
            for puc_id in actors[actor]["pucs"]:
                node = re.sub(r"[^A-Za-z0-9]", "_", puc_id) or "PUC"
                lines.append(f'  A{index} --> {node}["{puc_id}"]')
        lines.append("```")

    lines += [
        "",
        "## Part III — Product Use Case Catalogue",
        "",
        "| PUC ID | Business Trigger | Primary Actor | System Operational Boundary | Deliverables & Outputs | Realizing Requirements |",
        "|---|---|---|---|---|---|",
    ]
    for card in puc_cards:
        p = card["puc"]
        lines.append(
            f"| {p['puc_id']} | {p['trigger']} | {p['actor']} | {p['boundary']} | {p['outputs']} | {card['id']} |"
        )
    if not puc_cards:
        lines.append("| — | — | — | — | — | No product use case cards were produced for this run. |")

    lines += [
        "",
        "## Part IV — Security & Trust Zone Annotations",
        "",
        "| Zone | Trust-boundary skill | Protected perimeter |",
        "|---|---|---|",
    ]
    if tb_rows:
        for row in tb_rows:
            lines.append(
                f"| TZ-{row.get('seq', '—')} | {row.get('skill', '—')} | {row.get('objective', '—')} — {row.get('summary', '')[:120]} |"
            )
    else:
        lines.append("| — | — | No trust-boundary rows in the coverage matrix; the Part 2 threat pass owns the trust-boundary model. |")
    lines.append("")
    return "\n".join(lines) + "\n"
