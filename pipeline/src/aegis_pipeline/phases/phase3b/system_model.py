"""aegis_pipeline.phases.phase3b.system_model — Etapa 2.1: the attack target.

Decomposes the approved Part 1 package into assets (AST), data flows (DF) and
trust boundaries (TB), and allocates every accepted requirement to what it
protects. Fidelity rules: zero invented components (R6 — everything traces to
the fact sheet or the Part 1 deliverables), and 100% of the accepted
requirements allocated (a control protecting nothing is an orphan).
"""
from __future__ import annotations

import re

from aegis_pipeline.guards.quality_gates import check_no_technology

RE_AST = re.compile(r"^AST-\d{2,}$")
RE_DF = re.compile(r"^DF-\d{2,}$")
RE_TB = re.compile(r"^TB-\d{2,}$")

TABLES = ("Assets", "Data flows", "Trust boundaries", "Control allocation")


def _rows(block: str, title: str, ncols: int) -> list[list[str]]:
    rows = []
    in_section = False
    for line in block.splitlines():
        s = line.strip()
        if s.startswith("####"):
            in_section = s.lstrip("#").strip().lower().startswith(title.lower())
            continue
        if not in_section or not s.startswith("|") or set(s) <= {"|", "-", " ", ":"}:
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) == ncols:
            if cells[0].strip("`*") in ("ID", "Control"):
                continue  # the header row — a data row's first cell is an id
            rows.append(cells)
    return rows


def parse_system_model(answer: str, accepted_ids: list[str]) -> dict:
    """L0 for the model call. `accepted_ids` = the REQ/R-ORG ids Part 1 accepted."""
    from aegis_pipeline.phases.phase1.common import extract_fenced

    block = extract_fenced(answer, "markdown")
    assets, flows, boundaries, allocation = (
        _rows(block, t, 2 if t == "Control allocation" else 5) for t in TABLES)
    if not assets:
        raise ValueError("system model: no Assets rows")
    if not flows:
        raise ValueError("system model: no Data flow rows")
    if not boundaries:
        raise ValueError("system model: no Trust boundary rows")

    ast_ids = {r[0].strip("`") for r in assets}
    bad = [a for a in ast_ids if not RE_AST.match(a)]
    if bad:
        raise ValueError(f"system model: asset id(s) {bad[:4]} outside the AST-nn shape")
    tb_ids = {r[0].strip("`") for r in boundaries}
    bad = [t for t in tb_ids if not RE_TB.match(t)]
    if bad:
        raise ValueError(f"system model: trust boundary id(s) {bad[:4]} outside the TB-nn shape")

    flows_out = []
    for r in flows:
        df_id, source, dest, carried, boundary = (c.strip() for c in r)
        if not RE_DF.match(df_id.strip("`")):
            raise ValueError(f"system model: flow id {df_id!r} outside the DF-nn shape")
        carried_ids = [a.strip().strip("`") for a in carried.split(",") if a.strip().strip("`")]
        unknown_assets = [a for a in carried_ids if a not in ast_ids]
        if unknown_assets:
            raise ValueError(f"system model [{df_id}]: carries unknown asset(s) {unknown_assets[:4]}")
        if boundary.strip("`") not in tb_ids:
            raise ValueError(f"system model [{df_id}]: names trust boundary {boundary!r} that is not declared")
        tech = check_no_technology(source, dest, carried, boundary)
        if tech:
            raise ValueError(f"system model [{df_id}]: {tech[0]}")
        flows_out.append({"id": df_id.strip("`"), "source": source, "destination": dest,
                          "assets_carried": carried_ids,
                          "trust_boundary": boundary.strip("`")})

    alloc: dict[str, list[str]] = {}
    for r in allocation:
        control = r[0].strip("`")
        targets = [t.strip().strip("`") for t in r[1].split(",") if t.strip().strip("`")]
        unknown = [t for t in targets if t not in ast_ids and t not in tb_ids
                   and not RE_DF.match(t)]
        if unknown:
            raise ValueError(f"system model: allocation for {control!r} names unknown target(s) {unknown[:4]}")
        alloc.setdefault(control, []).extend(targets)
    missing = [oid for oid in accepted_ids if oid not in alloc]
    if missing:
        raise ValueError(
            f"system model: {len(missing)} accepted requirement(s) not allocated to any "
            f"asset/flow/boundary: {missing[:8]}")

    return {
        "assets": [{"id": r[0].strip("`"), "name": r[1], "kind": r[2], "sensitivity": r[3],
                    "rationale": r[4]} for r in assets],
        "trust_boundaries": [{"id": r[0].strip("`"), "name": r[1],
                              "privilege_change": r[2], "controls": r[3], "rationale": r[4]}
                             for r in boundaries],
        "flows": flows_out,
        "allocation": alloc,
    }


def render_system_model(model: dict, company: str, accepted: list[dict]) -> str:
    """01_SYSTEM_MODEL_AND_FOUNDATIONS — the deliverable."""
    lines = [
        "---",
        f"title: '01 — System Model, Assets and Trust Boundaries ({company})'",
        "generated_by: 'p3b_model (onda D)'",
        "---",
        "",
        "## §1 Assets",
        "",
        "| ID | Asset | Kind | Sensitivity | Rationale |",
        "|---|---|---|---|---|",
    ]
    for a in model["assets"]:
        lines.append(f"| `{a['id']}` | {a['name']} | {a['kind']} | {a['sensitivity']} | {a['rationale']} |")
    lines += ["", "## §2 Trust boundaries", "",
              "| ID | Boundary | Privilege change | Controls at the crossing | Rationale |",
              "|---|---|---|---|---|"]
    for t in model["trust_boundaries"]:
        lines.append(f"| `{t['id']}` | {t['name']} | {t['privilege_change']} | {t['controls']} | {t['rationale']} |")
    lines += ["", "## §3 Data flows", "",
              "| ID | Source | Destination | Assets carried | Trust boundary |",
              "|---|---|---|---|---|"]
    for f in model["flows"]:
        lines.append(f"| `{f['id']}` | {f['source']} | {f['destination']} "
                     f"| {', '.join(f'`{a}`' for a in f['assets_carried'])} | `{f['trust_boundary']}` |")
    by_oid = {p["objective"]: p for p in accepted if isinstance(accepted, list)}
    lines += ["", "## §4 Control allocation (every accepted requirement protects something)", "",
              "| Control | Requirement | Protects |", "|---|---|---|"]
    for control, targets in sorted(model["allocation"].items()):
        p = by_oid.get(control, {})
        lines.append(f"| `{control}` | {p.get('constraint', control)[:120]} "
                     f"| {', '.join(f'`{t}`' for t in targets)} |")
    lines.append("")
    return "\n".join(lines) + "\n"
