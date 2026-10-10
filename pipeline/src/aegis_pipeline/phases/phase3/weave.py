"""Wave 6 — weave the accepted constraints, then run the exit gate.

`p3a_weave` (model): per accepted-constraint-bearing card, security
preconditions and exception extensions for the use case; the Doc01 injection
of the accepted constraint blocks is mechanical. `p3a_gate` (zero calls):
T1–T6 over the run's own outputs, doc_lint --strict, and the G1–G6 evaluation
with the two-state rule — a run whose round has open verdicts is PROPOSED, not
CONCLUDED, and the gate does not close.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from aegis_pipeline.guards.quality_gates import check_no_technology

RE_CARD_ID = re.compile(r"^R\d+\.\d+$")


def parse_weave(answer: str) -> dict:
    """L0 for one weave call: `#### Card R<n>.<m>` + precondition/extension fields."""
    from aegis_pipeline.phases.phase1.common import extract_fenced

    block = extract_fenced(answer, "markdown").strip()
    m = re.search(r"####\s*Card\s+(R\d+\.\d+)", block)
    if not m:
        raise ValueError("weave: no `#### Card R<n>.<m>` header")
    card_id = m.group(1)
    fields: dict[str, str] = {}
    for field in ("Preconditions", "Extensions", "Constraints absorbed"):
        m = re.search(rf"\*\*{re.escape(field)}:?\*\*\s*(.+?)(?=\n\*\*|\Z)", block, re.DOTALL)
        if not m:
            raise ValueError(f"weave [{card_id}]: missing field {field!r}")
        fields[field] = m.group(1).strip()
    tech = check_no_technology(fields["Preconditions"], fields["Extensions"])
    if tech:
        raise ValueError(f"weave [{card_id}]: technology vocabulary (R5): {tech}")
    return {"card_id": card_id, **fields}


def accepted_constraint_ids(round_state: dict) -> set[str]:
    """Objectives whose proposals the round accepted — the weave's input set."""
    return {p["objective"] for p in round_state.get("accepted", [])}


def render_step4(accepted: list[dict], cards: list[dict]) -> str:
    """STEP4 — absorption weaving: which accepted constraint lands on which card."""
    card_ids = {c["id"] for c in cards}
    lines = [
        "---",
        "title: 'STEP4 — Constraint absorption (weave)'",
        "generated_by: 'p3a_weave (wave 6)'",
        "---",
        "",
        "| Objective | Constraint | Carrier card | In pool? |",
        "|---|---|---|---|",
    ]
    for proposal in accepted:
        carrier = proposal.get("carrier", "—")
        in_pool = "yes" if carrier in card_ids else "NEW"
        lines.append(f"| `{proposal['objective']}` | {proposal['constraint'][:160]} | {carrier} | {in_pool} |")
    lines.append("")
    return "\n".join(lines) + "\n"


def render_sufficiency(rows: list[dict], round_state: dict, regs: list[str]) -> str:
    """G5 evidence: compliance verdict per regulation + the explicit residue list."""
    counts: dict[str, int] = {}
    for row in rows:
        counts[row["verdict"]] = counts.get(row["verdict"], 0) + 1
    residues = [
        f"`{p['objective']}` — risk accepted: {p['risk']}"
        for p in round_state.get("rejected", [])
    ]
    lines = [
        "---",
        "title: 'SUFFICIENCY_ASSESSMENT'",
        "generated_by: 'p3a_weave (wave 6) — computed from the matrix and the round'",
        "---",
        "",
        "## Compliance verdict per regulation",
        "",
    ]
    for reg in regs:
        lines.append(f"- **{reg}:** {counts.get('Fully covered (anchored)', 0)} fully covered, "
                     f"{counts.get('Partially covered (functional leg + explicit carve-out)', 0)} partial, "
                     f"{counts.get('No functional carrier (organizational)', 0)} organizational "
                     "(counts span the whole matrix; per-objective regulation lives in the Fase 2 doc)")
    lines += ["", "## Security verdict", "",
              f"- {sum(1 for r in rows if r['verdict'] == 'Fully covered (anchored)')} of {len(rows)} objectives fully carried after the round;"
              f" {len(round_state.get('accepted', []))} constraints accepted and woven."]
    lines += ["", "## Residues (explicit)", ""]
    if residues:
        lines += [f"- {r}" for r in residues]
    else:
        lines += ["- None — no rejection recorded."]
    if round_state.get("open"):
        lines += [f"- OPEN (round not converged): {', '.join(f'`{o}`' for o in round_state['open'])}"]
    lines.append("")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# The exit gate — zero model calls.
# ---------------------------------------------------------------------------


def run_gate(run_dir: Path, repo: Path) -> dict:
    """T1–T6 (Part 1 scope) + doc_lint --strict + G1–G6 with the two-state rule."""
    import subprocess

    import phase3 as p3

    findings: list[str] = []
    gates: dict[str, str] = {}

    matrix_path = run_dir / "outputs" / "phase3" / "synthesis_rounds" / "OBJECTIVE_MAPPING.md"
    phase2_doc = run_dir / "outputs" / "phase2" / "Doc01_Operational_Objectives.md"

    rows: list[dict] = []
    objectives: list[dict] = []
    if matrix_path.is_file() and phase2_doc.is_file():
        objectives = p3.load_objectives(phase2_doc)
        # The rendered matrix is the merged skeleton+verdicts; read the steps store instead.
        verdict_rows: list[dict] = []
        for path in sorted((run_dir / "steps" / "phase3").glob("verdicts_*.json")):
            verdict_rows.extend(json.loads(path.read_text(encoding="utf-8")))
        rows = p3.apply_verdicts(p3.build(objectives), verdict_rows) if verdict_rows else []
        skeleton_findings = p3.check(rows, objectives)
        findings += [f"T-G1: {f}" for f in skeleton_findings]
        pool_ids = [c["id"] for c in p3.load_v0_cards(
            repo / "cases" / json.loads((run_dir / "manifest.json").read_text())["case_id"]
            / "03_PHASE3_SPEC" / "part1_security_privacy" / "v0_functional_baseline"
            / "Doc01_Requirements_Elicitation_and_PUC.md"
        )]
        findings += [f"T-matrix: {f}" for f in p3.check_verdicts(rows, objectives, pool_ids)]
        findings += [f"T6: {f}" for f in p3.check_anchors(rows)]
    else:
        findings.append("T-G1: coverage matrix or Phase 2 deliverable missing — run the earlier stages")

    # G2 / two-state rule
    register = run_dir / "outputs" / "phase3" / "synthesis_rounds" / "ROUND1_REGISTER.md"
    state_path = run_dir / "steps" / "phase3" / "round1_state.json"
    marker = run_dir / "steps" / "gates" / "G-P3-A.approved"
    round_state: dict = {"converged": False, "open": ["(no round artifacts)"]}
    if state_path.is_file():
        round_state = json.loads(state_path.read_text(encoding="utf-8"))
    n_proposals = len(round_state.get("accepted", [])) + len(round_state.get("rejected", [])) + len(round_state.get("adjusted", [])) + len(round_state.get("open", []))
    if not register.is_file():
        gates["G2"] = "OPEN — no round register (stage p3a_propose not run)"
    elif not marker.is_file():
        gates["G2"] = "OPEN — proposals recorded but no human marker (G-P3-A)"
    elif not round_state.get("converged"):
        gates["G2"] = f"OPEN — proposed, not concluded: {len(round_state.get('open', []))} verdict(s) missing"
    elif n_proposals == 0:
        gates["G2"] = "OPEN — a converged register with zero items closes nothing (§two states)"
    else:
        gates["G2"] = "CLOSED"
    proposed = not gates["G2"].startswith("CLOSED")

    # G1
    unset = [r["id"] for r in rows if r.get("verdict") in (None, "—", "")]
    gates["G1"] = "CLOSED" if rows and not unset and not any(f.startswith("T-G1") for f in findings) \
        else f"OPEN — {len(unset)} verdict(s) unset or skeleton findings"

    # G3 — accepted constraints cite published anchors
    g3_findings = [f for f in findings if f.startswith("T6")]
    gates["G3"] = "CLOSED" if not g3_findings else f"OPEN — {len(g3_findings)} anchor finding(s)"

    # G4 — doc_lint --strict over the produced markdown
    lint = subprocess.run(
        ["python3", str(repo / "scripts" / "doc_lint.py"), "--strict", str(run_dir / "outputs" / "phase3")],
        capture_output=True, text=True, timeout=120,
    )
    gates["G4"] = "CLOSED" if lint.returncode == 0 else f"OPEN — doc_lint: {lint.stdout[-400:] or lint.stderr[-400:]}"

    # G5 — sufficiency assessment exists
    gates["G5"] = "CLOSED" if (run_dir / "outputs" / "phase3" / "synthesis_rounds" / "SUFFICIENCY_ASSESSMENT.md").is_file() \
        else "OPEN — SUFFICIENCY_ASSESSMENT missing"

    # G6 — the v0→v1 transition dossier
    gates["G6"] = "CLOSED" if (run_dir / "outputs" / "phase3" / "synthesis_rounds" / "STEP4_CONSTRAINT_ABSORPTION.md").is_file() \
        else "OPEN — STEP4 absorption table missing (run p3a_weave)"

    # CONCLUDED exige TODOS os gates fechados; com a ronda aberta é PROPOSED
    # mesmo com gates fechados — é a regra dos dois estados (doc 08).
    all_closed = all(v.startswith("CLOSED") for v in gates.values())
    if proposed:
        state = "PROPOSED"
    elif all_closed and not findings:
        state = "CONCLUDED"
    else:
        state = "FAILED"
    return {
        "state": state,
        "gates": gates,
        "findings": findings,
        "n_objectives": len(rows),
    }


def render_gate_report(report: dict) -> str:
    lines = [
        "---",
        "title: 'Phase 3 Part 1 — exit gate report'",
        "generated_by: 'p3a_gate (wave 6)'",
        f"state: {report['state']}",
        "---",
        "",
        f"# Exit gate — state: **{report['state']}**",
        "",
        "| Gate | Verdict |",
        "|---|---|",
    ]
    for gate in ("G1", "G2", "G3", "G4", "G5", "G6"):
        lines.append(f"| {gate} | {report['gates'].get(gate, '—')} |")
    lines += ["", f"Objectives in the matrix: {report['n_objectives']}."]
    if report["findings"]:
        lines += ["", "## Findings", ""]
        lines += [f"- {f}" for f in report["findings"][:40]]
    lines.append("")
    return "\n".join(lines) + "\n"
