#!/usr/bin/env python3
"""aegis_pipeline.phases.phase1.assembly — Deterministic assembly of doc02_adjusted_goals.md."""

from __future__ import annotations

import datetime as _dt
import json
import sys
from pathlib import Path

# Ensure pipeline/src is importable
_src = Path(__file__).resolve().parents[3]
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

from compose import (
    REGULATIONS,
    confirmed_regulations,
    domain_dir,
    objective_paragraph,
    parse_simple_yaml,
    sub_so_objective,
)
from aegis_pipeline.guards.controls import (
    goal_anchors,
    parse_overrides,
    sd_control_sections,
    track_b_rows,
)
from aegis_pipeline.phases.phase1.goals import (
    PROPERTY_LONG,
    goal_table_header,
)


def _hl_goal(repo: Path, sd_id: str) -> str:
    """The regulation-neutral Baseline Goal paragraph, verbatim from the corpus."""
    return " ".join(objective_paragraph(domain_dir(repo, sd_id)).split())


def _cell(v: str) -> str:
    return " ".join(str(v).split())


def _run_identity(run_dir: Path) -> str:
    """run_id and mode of the run assembling this document."""
    mf = run_dir / "manifest.json"
    if not mf.exists():
        return run_dir.name
    try:
        m = json.loads(mf.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return run_dir.name
    return f"{m.get('run_id', run_dir.name)} ({m.get('mode', 'pipeline')})"


def assemble_doc(repo: Path, run_dir: Path, case: dict) -> str:
    """Deterministic assembly of doc02_adjusted_goals.md."""
    steps_dir = run_dir / "steps"
    fact = parse_simple_yaml((steps_dir / "fact_sheet.yaml").read_text(encoding="utf-8"))
    selection = json.loads((steps_dir / "selection.json").read_text(encoding="utf-8"))
    confirmed = confirmed_regulations(run_dir)
    sel_ids = sorted(s["id"] for s in selection["selected"])
    names = {s["id"]: s["name"] for s in selection["selected"]}
    framing = (steps_dir / "framing.md").read_text(encoding="utf-8").strip()
    tpath = steps_dir / "tensions.json"
    tensions = json.loads(tpath.read_text(encoding="utf-8")).get("tensions", []) if tpath.exists() else []
    overrides = parse_overrides(case.get("track_b_overrides"))

    today = _dt.date.today().isoformat()
    n_goals = 0
    goal_blocks: list[str] = []
    for sd in sel_ids:
        jf = steps_dir / "goals" / f"{sd.replace('.', '_')}.json"
        if not jf.exists():
            goal_blocks.append(
                f"### {sd} — {names[sd]}\n\n"
                f"**High-Level Security Goal (SO-{sd}.HL):** {_cell(_hl_goal(repo, sd))}\n\n"
                f"> **[UNVALIDATED_DRAFT: Stage P4 did not carry this sub-domain — L0 repair failed ({sd})]**\n"
            )
            continue
        data = json.loads(jf.read_text(encoding="utf-8"))
        gs = data["goals"]
        if not gs:
            goal_blocks.append(
                f"### {sd} — {names[sd]}\n\n"
                f"**High-Level Security Goal (SO-{sd}.HL):** {_cell(_hl_goal(repo, sd))}\n\n"
                "_None — no Sub-SO for the confirmed regulations in this module._"
            )
            continue
        regs_present = sorted({g["regulation"] for g in gs}, key=REGULATIONS.index)
        baselines = [
            f"**Regulation baseline — `SG-{sd}.{reg}` ({reg}):** {_cell(sub_so_objective(repo, sd, reg))}"
            for reg in regs_present
        ]
        rows = []
        for g in gs:
            anchors = goal_anchors(repo, sd, [g["baseline_source"]])
            rows.append(
                f"| `{g['id']}` | {_cell(g['goal'])} | {_cell(g['implication'])} | "
                f"{g['pattern']} | {PROPERTY_LONG[g['property']]} | {g['parent']} | "
                f"{g['regulation']} | {_cell(g['source'])} | "
                f"{', '.join(anchors) if anchors else '—'} | {_cell(g['adjustment'])} |"
            )
        n_goals += len(rows)
        goal_blocks.append(
            f"### {sd} — {names[sd]}\n\n"
            f"**High-Level Security Goal (SO-{sd}.HL):** {_cell(_hl_goal(repo, sd))}\n\n"
            + "\n\n".join(baselines) + "\n\n"
            + goal_table_header() + "\n"
            + "\n".join(rows)
        )

    if len(confirmed) >= 2 and tensions:
        t_parts = [
            f"### {t['id']} ({t['subdomains']}) — {_cell(t['tension'])}\n\n"
            f"**Conflict:** {_cell(t['conflict'])}\n\n"
            f"**Resolution:** {_cell(t['resolution'])}"
            for t in tensions
        ]
        s4 = "\n\n".join(t_parts)
    elif len(confirmed) >= 2:
        s4 = "None — the confirmed regulation pairing surfaces no strategic tension in the corpus."
    else:
        s4 = "None — single-regulation run."

    tb_rows = track_b_rows(fact, sel_ids, overrides)
    s5_table = (
        "| Sub-Domain | Scale | Inheritability | Priority | Tier | Rationale |\n"
        "|---|---|---|---|---|---|\n"
        + "\n".join(
            f"| {r['subdomain']} | {r['scale']} | {r['inheritability']} "
            f"| {r['priority']} | {r['tier']} | {_cell(r['rationale'])} |"
            for r in tb_rows
        )
    )

    s6_parts: list[str] = []
    for i, sd in enumerate(sel_ids, 1):
        secs = sd_control_sections(repo, sd, confirmed)
        body = [f"### §6.{i} {sd} — {names[sd]}\n\n_Applicable regulations: {', '.join(confirmed)}_"]
        for sec in secs:
            if not sec["rows"]:
                continue
            body.append(
                f"#### {sec['title']}\n\n"
                "| Function | Control ID | Description (1-liner) | Path |\n"
                "|---|---|---|---|\n"
                + "\n".join(
                    f"| {r['function']} | {r['id']} | {_cell(r['text'])} | {r['path']} |"
                    for r in sec["rows"]
                )
            )
        s6_parts.append("\n\n".join(body))

    doc_id = "MVP-P1-DOC02-001"
    parts = [
        f"---\ndocument_id: {doc_id}\ntitle: \"Adjusted Goals per Sub-Domain — {case['company_name']}\"\n"
        f"version: 0.1\ncreated: {today}\nstatus: DRAFT\n"
        f"input: pipeline/cases/{case['case_id']}/company_input.md\ncorpus: baseline\n"
        f"run_id: {_run_identity(run_dir)}\n---\n",
        f"# Adjusted Goals per Sub-Domain — {case['company_name']}",
        "## §0 Document Purpose",
        f"This document is the **Phase 1 Adjusted Goals layer** of the "
        f"{case['company_name']} run — the Fase 0 → Fase 1 exchange of the pipeline "
        f"I/O contract (ADR-004): the frozen corpus **Baseline Goals** (high-level "
        f"goal `SO-D-XX.Y.HL` + per-regulation Sub-SOs) restated against one "
        f"company. It binds every ACTIVE sub-domain to: 1. a **regulatory floor** — "
        f"the corpus Baseline Goals, consumed by reference (§1); 2. a **framing** — "
        f"the company context conditioning every goal (§2); 3. **Adjusted Goals** — "
        f"one company-proportional row per Sub-SO of each confirmed regulation, "
        f"with code-derived control anchors (§3); 4. **resolutions** for the "
        f"strategic tensions surfaced by the confirmed regulation pairings (§4); "
        f"5. a **Track B tier** per sub-domain from the deterministic matrix (§5); "
        f"6. the **NIST controls mapping** per sub-domain (§6).",
        "## §1 Regulatory Floor (corpus, by reference)",
        "The baseline floor for goals is consumed by reference from `baseline/domains/` "
        "and `baseline/MAPPINGS/` per rule R9. The only baseline text reproduced here "
        "is each sub-domain's High-Level Security Goal paragraph and each confirmed "
        "regulation's Sub-SO objective, both verbatim — the rest is by reference.",
        "## §2 Framing (company context conditioning every goal below)",
        framing,
        "## §3 Adjusted Goals",
        "### §3.0 Structure and Interpretation Guide",
        "Each active sub-domain presents:\n"
        "1. **High-Level Security Goal (`SO-D-XX.Y.HL`):** the regulation-neutral "
        "baseline objective, verbatim from the corpus module (`objective.md`).\n"
        "2. **Regulation baseline (`SG-D-XX.Y.<REG>`):** each confirmed regulation's "
        "Sub-SO objective, verbatim from the corpus module — the floor the adjusted goal restates.\n"
        "3. **Regulation-specific Adjusted Goals:** one row per Sub-SO of each "
        "confirmed regulation, in canonical order (slot 001 = GDPR, 002 = CRA, …), "
        "each with the **Company implication** — what the duty concretely means for this company.\n"
        "4. **Property:** one protected property per row (Confidentiality, "
        "Integrity, Availability, Privacy Right, Accountability).\n"
        "5. **Control Anchors:** NIST CSF 2.0 ids derived by code from the row's "
        "Baseline source (`source_SR` → mapping store); the full per-axis mapping lives in §6.\n"
        "6. **Adjustment (closed vocabulary):** `unchanged — fits as stated` | "
        "`narrowed: … — because …` | `flagged: …` — never silently relaxed (R3).",
    ]
    parts.extend(goal_blocks)
    parts.append("## §4 Tensions Resolved")
    parts.append(s4)
    parts.append(f"## §5 Track B Decision Trail ({len(tb_rows)} rows)")
    parts.append(s5_table)
    parts.append("## §6 NIST Controls Mapping")
    parts.extend(s6_parts)
    return "\n\n".join(parts) + "\n"


def build_run_notes(run_dir: Path) -> str:
    """Deterministic RUN_NOTES.md: run meta, §8 evidence plan, gate ledger."""
    manifest = json.loads((run_dir / "manifest.json").read_text(encoding="utf-8"))
    gates = (
        sorted((run_dir / "steps" / "gates").glob("G-P1-*.approved"))
        if (run_dir / "steps" / "gates").exists()
        else []
    )
    gate_rows = "\n".join(
        f"| {g.stem} | approved | {g.read_text(encoding='utf-8').strip().splitlines()[-1][:80]} |"
        for g in gates
    )
    n_calls = (
        sum(1 for l in (run_dir / "trace.jsonl").read_text().splitlines() if l.strip())
        if (run_dir / "trace.jsonl").exists()
        else 0
    )
    return f"""# RUN_NOTES — {manifest['run_id']}

## Run meta

| Field | Value |
|---|---|
| Case | {manifest['case_id']} |
| Model | {manifest['model']} |
| LLM calls (trace.jsonl) | {n_calls} |
| Fichas | {', '.join(f"{k}={v}" for k, v in manifest['ficha_versions'].items())} |
| Deliverable | doc02_adjusted_goals.md (DRAFT) |

## SPEC §8 evidence

| # | Item | How verified | Result |
|---|---|---|---|
| 1 | Input contract (5 sections) | validated at P1 (L0 stop condition) | PASS |
| 2 | Confirmed regulation set (§2 verdicts) | validate.py item 2 (verdicts.json) | run locally post-sync |
| 3 | §3 codes exist in corpus | validate.py item 3 | run locally post-sync |
| 4 | AG IDs unique, match selection | validate.py item 4 | run locally post-sync |
| 5 | Regulatory sources resolve (R2a) | validate.py item 5 | run locally post-sync |
| 6 | Control anchors resolve (R2b) | derived by controls.py + validate.py diff | PASS by construction |
| 7 | No statement without input trace | L0 parsers + gate review | human check |
| 8 | Frontmatter complete; DRAFT | assembly (deterministic) | PASS (DRAFT until G-P1-D) |
| 9 | Pattern/property/parent/baseline source/adjustment | validate.py item 9 | run locally post-sync |
| 10 | Document hygiene (R11/R12) | validate.py R12-hygiene + doc_lint scope note | run locally post-sync |

## Human gates

| Gate | State | Note |
|---|---|---|
{gate_rows or "| (none yet) | | |"}
"""
