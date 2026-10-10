"""aegis_pipeline.phases.phase3.skeleton — matrix and principles skeleton builders and renderers.

Builds OBJECTIVE_MAPPING.md and PRINCIPLE_MAPPING.md skeletons from Phase 2
deliverables, with every row present and every content column unset.
"""
from __future__ import annotations

import re
from pathlib import Path

from aegis_pipeline.phases.phase3.schemas import (
    MATRIX_COLUMNS,
    UNSET,
    VERDICTS,
    anchor_set,
    domain_of,
    is_template_criterion,
    subdomain_of,
)

#: The seven engineering principles, in canonical order.
PRINCIPLES = (
    ("PRIN-ENG-01", "Explicit Trust Boundaries & Complete Mediation"),
    ("PRIN-ENG-02", "Attack Surface Minimization & Peripheral Resilience"),
    ("PRIN-ENG-03", "Least Privilege & Mechanism Isolation"),
    ("PRIN-ENG-04", "Fail-Safe Defaults & Closed Failure States"),
    ("PRIN-ENG-05", "Requirement Verifiability & Atomicity"),
    ("PRIN-ENG-06", "Proactive Data Minimization & Scoped Projection"),
    ("PRIN-ENG-07", "End-to-End Lifecycle Security & Irreversible Erasure"),
)

#: Phase 2 Doc01_Operational_Objectives.md column order.
COL_ID, COL_STATEMENT, COL_PARENT, COL_REG, COL_SCOPE, COL_CRITERIA, COL_METHOD, COL_OWNER, COL_ANCHORS = range(9)


def load_objectives(path: Path) -> list[dict]:
    """Every objective row of a Phase 2 deliverable, in file order."""
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) < 9 or not re.match(r"`?(PO|SO)-D-\d{2}\.\d-\d{3}", cells[0]):
            continue
        oid = cells[0].strip("` ")
        rows.append({
            "id": oid,
            "statement": cells[COL_STATEMENT].strip("` "),
            "parent_goal": cells[COL_PARENT].strip("` "),
            "regulation": cells[COL_REG].strip("` "),
            "scope": cells[COL_SCOPE],
            "criterion": cells[COL_CRITERIA],
            "method": cells[COL_METHOD],
            "owner": cells[COL_OWNER],
            "anchors": anchor_set(cells[COL_ANCHORS]),
            "subdomain": subdomain_of(oid),
            "domain": domain_of(subdomain_of(oid)),
        })
    return rows


def build(rows: list[dict]) -> list[dict]:
    """The matrix skeleton: one row per objective, content columns empty."""
    return [{
        "id": r["id"],
        "summary": r["statement"],
        "carrier": UNSET,
        "skill": UNSET,
        "verdict": UNSET,
        "discharge": UNSET,
        "action": UNSET,
        "subdomain": r["subdomain"],
        "domain": r["domain"],
        "regulation": r["regulation"],
        "scope": r["scope"],
        "method": r["method"],
        "owner": r["owner"],
        "criterion": r["criterion"],
        "anchors": r["anchors"],
        "criterion_is_template": is_template_criterion(r["criterion"]),
    } for r in rows]


def render_matrix(
    rows: list[dict],
    by_domain: dict[str, list[dict]],
    domain_names: dict[str, str],
) -> str:
    out = [
        "# Phase 2 Objective Mapping — Exhaustive Coverage Matrix",
        "",
        "> **SKELETON.** Every Phase 2 objective has a row; every column that "
        "requires a judgement is unset. The `Fully covered` verdict is "
        "*anchored*, not *discharge-verified*: the ADR-007 D2 reconstruction test "
        "is not executable on the current Phase 2 data, because all Verification "
        "Criteria are one of two template sentences with the objective's own name "
        "substituted (ADR-013 §3). The `VC discharge` column records which legs a "
        "carrier carries and which are carved out; it does not claim a "
        "reconstruction.",
        "",
        "## Verdict vocabulary (ADR-007 D4)",
        "",
    ]
    out += [f"- `{v}`" for v in VERDICTS]
    out += ["", "---", ""]

    for domain in sorted(by_domain):
        out += [f"## {domain} — {domain_names.get(domain, '')}".rstrip(" —"), ""]
        out += ["| " + " | ".join(MATRIX_COLUMNS) + " |",
                "|" + "|".join(["---"] * len(MATRIX_COLUMNS)) + "|"]
        for r in by_domain[domain]:
            out.append("| `" + r["id"] + "` | " + " | ".join(
                [r["summary"], r["carrier"], r["skill"], r["verdict"],
                 r["discharge"], r["action"]]) + " |")
        out += ["", "---", ""]

    out += ["## Coverage totals", "", "| Verdict | Count |", "|---|---|"]
    for v in VERDICTS:
        n = sum(1 for r in rows if r["verdict"] == v)
        out.append(f"| {v} | {n} |")
    out.append(f"| **Unset** | **{sum(1 for r in rows if r['verdict'] == UNSET)}** |")
    out.append(f"| **Total objectives** | **{len(rows)}** |")
    return "\n".join(out) + "\n"


def render_principles() -> str:
    out = ["# Engineering Principles — Mapping (skeleton)", "",
           "| Principle | Name | Where | Realization | RN | State |", "|---|---|---|---|---|---|"]
    for pid, name in PRINCIPLES:
        out.append(f"| `{pid}` | {name} | {UNSET} | {UNSET} | {UNSET} | {UNSET} |")
    out += ["", "---", "",
            "| Surface | Count |", "|---|---|",
            f"| Principles present | {len(PRINCIPLES)}/{len(PRINCIPLES)} |",
            f"| Bound | 0 |",
            f"| Pending | {len(PRINCIPLES)} |"]
    return "\n".join(out) + "\n"


def domain_names_from(index: Path) -> dict[str, str]:
    """Domain titles from baseline/domains/index.md, when the file is present."""
    names = {}
    if not index.is_file():
        return names
    for line in index.read_text(encoding="utf-8").splitlines():
        m = re.search(r"\[(D-\d{2})_([^\]]+)\]\(", line)
        if m:
            names[m.group(1)] = m.group(2).replace("-", " ")
    return names
