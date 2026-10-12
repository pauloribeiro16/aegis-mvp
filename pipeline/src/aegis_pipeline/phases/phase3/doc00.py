"""Wave 5b — Doc00 is COMPOSED, not generated (doc 08 §wave 5).

A model rewriting company input restates it — the recorded failure is Case 03's
Phase 2 Doc02 carrying Case 02's architecture. Everything here is assembled
deterministically from the run's own artifacts: the Phase 1 fact sheet, the V0
card catalogue, and the trust-boundary (TB) verdict rows. Zero model calls.
"""

from __future__ import annotations

import json
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
    """Part I/II from the fact sheet, Part III from the card catalogue, TZ from TB rows."""

    def _fact(key: str, fallback: str = "—") -> str:
        value = fact_sheet.get(key)
        if isinstance(value, list):
            return ", ".join(str(v) for v in value) if value else fallback
        return str(value) if value else fallback

    lines = [
        "---",
        f"title: 'Doc00 — Process and Operational Workflows ({company})'",
        "generated_by: 'p3a_org (wave 5) — deterministic composition'",
        "---",
        "",
        f"# Doc00 — Business Context, Process Models & Product Use Cases — {company}",
        "",
        "## Part I — Scope and Organizational Context",
        "",
        f"- **Company:** {company}",
        f"- **Sector:** {_fact('sector')}",
        f"- **Size:** {_fact('size')}",
        f"- **Jurisdiction:** {_fact('jurisdiction')}",
        f"- **Products / services:** {_fact('products_services')}",
        f"- **Data handled:** {_fact('data_categories')}",
        f"- **Infrastructure:** {_fact('infrastructure')}",
        f"- **Assumed regulations:** {_fact('assumed_regulations')}",
        "",
        "## Part III — Product Use Case catalogue",
        "",
        "| PUC ID | Business Trigger | Primary Actor | System Operational Boundary | Deliverables & Outputs | Realizing Requirements |",
        "|---|---|---|---|---|---|",
    ]
    for card in cards:
        p = card["puc"]
        lines.append(
            f"| {p['puc_id']} | {p['trigger']} | {p['actor']} | {p['boundary']} | {p['outputs']} | {card['id']} |"
        )
    lines += [
        "",
        "## Part III.b — Security & Trust Zone annotations",
        "",
        "| Zone | Trust-boundary skill | Protected perimeter |",
        "|---|---|---|",
    ]
    if tb_rows:
        for row in tb_rows:
            lines.append(
                f"| TZ-{row.get('seq', '?')} | {row.get('skill', '—')} | {row.get('objective', '—')} — {row.get('summary', '')[:120]} |"
            )
    else:
        lines.append("| — | — | No TB-skill rows in the coverage matrix; the Part 2 Step 1 pass owns the trust-boundary model. |")
    lines.append("")
    return "\n".join(lines) + "\n"
