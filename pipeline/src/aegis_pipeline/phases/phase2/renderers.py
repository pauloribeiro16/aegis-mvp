#!/usr/bin/env python3
"""aegis_pipeline.phases.phase2.renderers — Markdown renderers for Phase 2 Doc01 and Doc02."""

from __future__ import annotations

import json
import sys
from pathlib import Path

# Ensure pipeline/src is importable
_src = Path(__file__).resolve().parents[3]
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

from compose import load_case
from aegis_pipeline.phases.phase2.principles import (
    CATEGORIES,
    PRINCIPLES,
)
from aegis_pipeline.phases.phase2.parsers import (
    _ops_by_slot,
    _slot_of,
    load_operationalizations,
    load_tensions,
)

DOC01_HEADER = (
    "| Objective ID | Operational Statement | Parent Goal | Regulation | "
    "Operational Scope (Ambit) | Verification Criteria | Method | "
    "Responsible Owner | Control Anchors |\n"
    "|---|---|---|---|---|---|---|---|---|"
)


def cell(v: str) -> str:
    return " ".join(str(v).split())


def _case_id(run_dir: Path) -> str:
    return json.loads((run_dir / "manifest.json").read_text(encoding="utf-8"))["case_id"]


def _company_name(repo: Path, run_dir: Path) -> str:
    try:
        case = load_case(repo, _case_id(run_dir))
    except (FileNotFoundError, OSError, ValueError):
        case = {}
    return case.get("company_name") or _case_id(run_dir)


def _fact_sheet(run_dir: Path) -> str:
    f = run_dir / "steps" / "fact_sheet.yaml"
    return f.read_text(encoding="utf-8") if f.exists() else ""


def render_doc01(repo: Path, run_dir: Path, rows: list[dict]) -> str:
    name = _company_name(repo, run_dir)
    tensions = load_tensions(run_dir)
    op_map = load_operationalizations(run_dir)

    lines = [
        f"# Privacy & Security Operational Objectives — {name}",
        "",
        "> **Document Purpose:** Defines the Operational Objectives across all active "
        "sub-domains, separating the distinct operational scopes of applicable regulations, "
        "establishing empirical verification methods (ISO 29148 / INCOSE), and formalizing "
        "testable operational engineering rules (`RULE-*`). Cells marked `—` are seams: "
        "the pipeline has no derivation rule for them and does not invent one.",
        "",
        "## §1 Governance & Structure Guide",
        "",
        "### 1.1 Separation of Regulatory Ambits",
        "Where multiple regulations apply to the same sub-domain, they bind distinct operational "
        "ambits and cannot be conflated into a single objective (e.g. GDPR binds personal data, "
        "CRA binds product security, NIS 2 binds entity risk management, AI Act binds high-risk AI).",
        "",
        "### 1.2 Empirical Verification Methods (ISO 29148 / INCOSE)",
        "Every operational objective is evaluated via one of four empirical methods:",
        "- `TEST`: Automated assertion, CI/CD pipeline test, or runtime security probe.",
        "- `INSPECT`: Systematic review of configuration (IaC), process artefacts, or audit records.",
        "- `DEMONSTRATE`: Walkthrough or observable execution of an end-to-end operational flow.",
        "- `ANALYZE`: Systematic risk examination, architectural boundary review, or threat model.",
        "",
    ]

    if tensions:
        lines += [
            "## §2 Harmonisation of Strategic Tensions",
            "",
            "When multiple regulations apply, operational tensions are harmonized as follows:",
            "",
            "| Tension ID | Sub-Domains | Tension | Conflict | Resolution Strategy |",
            "|---|---|---|---|---|",
        ]
        for t in tensions:
            lines.append(
                f"| `{cell(t.get('id', ''))}` | `{cell(t.get('subdomains', ''))}` | "
                f"**{cell(t.get('tension', ''))}** | {cell(t.get('conflict', ''))} | "
                f"{cell(t.get('resolution', ''))} |"
            )
        lines.append("")

    sec_num = "§3" if tensions else "§2"
    lines += [f"## {sec_num} Operational Objectives by Domain", ""]

    current = None
    all_rules_in_subdomain: list[dict] = []

    for r in rows:
        sd = r["subdomain"]
        if sd != current:
            if current is not None:
                if all_rules_in_subdomain:
                    lines += [
                        "",
                        f"#### Operational Engineering Rules (`RULE-*`) — {current}",
                        "",
                        "| Rule ID | Operational Statement | Method | Parent Objective |",
                        "|---|---|---|---|",
                    ]
                    for rl in all_rules_in_subdomain:
                        lines.append(
                            f"| `{cell(rl.get('rule_id', ''))}` | {cell(rl.get('statement', ''))} | "
                            f"`{cell(rl.get('verification_target', ''))}` | `{cell(rl.get('parent_obj', ''))}` |"
                        )
                lines.append("")
                all_rules_in_subdomain = []

            current = sd
            lines.append(f"### {current} — {r['subdomain_name']}")
            lines.append("")

            op_data = op_map.get(current, {})
            op_trans = op_data.get("operational_translation")
            if op_trans:
                lines.append(f"**Operational Translation ({name} Context):** {op_trans}")
                lines.append("")

            lines += [DOC01_HEADER]

        op_data = op_map.get(current, {})
        om = _ops_by_slot(op_data).get(_slot_of(r["objective_id"]))
        if om:
            crit = om.get("criteria") or r["criteria"]
            meth = om.get("method") or r["method"]
            own = om.get("owner") or r["owner"]
            for ritem in om.get("rules", []):
                ritem_copy = dict(ritem)
                ritem_copy["parent_obj"] = r["objective_id"]
                all_rules_in_subdomain.append(ritem_copy)
        else:
            crit = r["criteria"]
            meth = r["method"]
            own = r["owner"]

        lines.append(
            "| `{oid}` | {stmt} | `{parent}` | **{reg}** | {scope} | {crit} | "
            "{meth} | {own} | `{anch}` |".format(
                oid=cell(r["objective_id"]),
                stmt=cell(r["statement"]),
                parent=cell(r["parent_goal"]),
                reg=cell(r["regulation"]),
                scope=cell(r["scope"]),
                crit=cell(crit),
                meth=cell(meth),
                own=cell(own),
                anch=cell(r["anchors"]),
            )
        )

    if all_rules_in_subdomain:
        lines += [
            "",
            f"#### Operational Engineering Rules (`RULE-*`) — {current}",
            "",
            "| Rule ID | Operational Statement | Method | Parent Objective |",
            "|---|---|---|---|",
        ]
        for rl in all_rules_in_subdomain:
            lines.append(
                f"| `{cell(rl.get('rule_id', ''))}` | {cell(rl.get('statement', ''))} | "
                f"`{cell(rl.get('verification_target', ''))}` | `{cell(rl.get('parent_obj', ''))}` |"
            )
        lines.append("")

    ver_sec = "§4" if tensions else "§3"
    lines += [
        "",
        f"## {ver_sec} Version History",
        "",
        "| Version | Date | Author / Role | Changes |",
        "|---|---|---|---|",
        "| `0.2` | — | aegis-mvp Phase 2 (enriched) | "
        "Operational translation, ISO 29148 methods, criteria, and RULE-* catalogue. |",
        "",
    ]
    return "\n".join(lines)


def render_doc02(repo: Path, run_dir: Path, principles: list[dict]) -> str:
    by_id = {p["id"]: p for p in principles}
    lines = [
        f"# Secure Design & Systems Engineering Principles — {_company_name(repo, run_dir)}",
        "",
        "> **Document Purpose:** establishes the 7 technology-agnostic engineering "
        "principles that constrain this company's solution space before "
        "technologies are chosen in Phase 3. The definitions are a baseline "
        "asset; the `Constraint` column is this company's own architecture. A "
        "`—` cell is a seam — the pipeline has no derivation for it — not a "
        "guess.",
        "",
        "## §1 The engineering spine",
        "",
        "Phase 2 runs on two non-overlapping pillars. **Doc01** carries the "
        "regulatory spine: what the law proportionally requires, as verifiable "
        "operational objectives. **Doc02** carries the engineering spine: 7 "
        "universal principles bound to this company's architecture. Per "
        "ISO/IEC/IEEE 29148:2018 clause 5.2.4 these state *verifiable "
        "architectural constraints* — what boundaries, invariants and failure "
        "modes must hold — without prescribing concrete database engines, "
        "frameworks, protocols or libraries, which belong to Phase 3.",
        "",
    ]
    for cat in CATEGORIES:
        lines += [
            f"## {cat['sec']} Principles Category {cat['n']} — {cat['title']}",
            "",
            f"> **Governing Domain:** {cat['domain']}  ",
            f"> **Foundational Literature:** {cat['lit']}",
            "",
            f"| Principle ID | Principle Name | Academic Source | {cat['def_col']} | "
            f"{cat['con_col']} | Verification Method & Lead |",
            "|---|---|---|---|---|---|",
        ]
        for p in PRINCIPLES:
            if p["category"] != cat["n"]:
                continue
            row = by_id.get(p["id"], {})
            lines.append(
                f"| `{p['id']}` | **{p['name']}** | {p['source']} | {p['definition']} | "
                f"{cell(row.get('constraint', ''))} | {cell(row.get('method_lead', ''))} |"
            )
        lines.append("")

    lines += [
        "## §6 Operationalization via Specialized Agentic Skills (1:1 symmetry)",
        "",
        "| Principle ID | Principle Name | Specialized Autonomous Skill | Path in Repository | Primary Evaluation Scope |",
        "|---|---|---|---|---|",
    ]
    for p in PRINCIPLES:
        row = by_id.get(p["id"], {})
        lines.append(
            f"| `{p['id']}` | {p['name']} | `{p['skill']}` | "
            f"[`baseline/skills/{p['skill']}/`](baseline/skills/{p['skill']}/) | "
            f"{cell(row.get('eval_scope', ''))} |"
        )
    lines += [
        "",
        "## §7 Version History",
        "",
        "| Version | Date | Author / Role | Changes |",
        "|---|---|---|---|",
        "| `0.1` | — | aegis-mvp phase2 | Definitions from the baseline; constraints per company. |",
        "",
    ]
    return "\n".join(lines)
