"""Wave 6 — weave the accepted constraints, then run the exit gate.

`p3a_weave` (model): per accepted-constraint-bearing card, security
preconditions and exception extensions for the use case; the Doc01 injection
of the accepted constraint blocks is mechanical. `p3a_gate` (zero calls):
T1–T6 over the run's own outputs, doc_lint --strict, and the G1–G6 evaluation
with the two-state rule — a run whose round has open verdicts is PROPOSED, not
CONCLUDED, and the gate does not close.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

from aegis_pipeline.guards.quality_gates import check_no_technology

RE_CARD_ID = re.compile(r"^R\d+\.\d+$")
RE_SUFFICIENCY_ROW = re.compile(
    r"^-\s+\*\*(?P<reg>[A-Za-z0-9_][A-Za-z0-9_ ]*):\*\*\s+"
    r"(?P<full>\d+) fully covered,\s*(?P<partial>\d+) partial,\s*(?P<org>\d+) organizational",
    re.MULTILINE,
)
RE_STEP4_ROW = re.compile(r"^\|\s*`[^`]+`\s*\|")


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


def render_sufficiency(rows: list[dict], round_state: dict, regs: list[str] | None = None) -> str:
    """G5 evidence: compliance verdict per regulation + the explicit residue list.

    The counts are grouped by each objective's own regulation column. The
    previous renderer printed the whole-matrix total once per regulation, so
    GDPR and CRA came out byte-identical — and G5, being `is_file()`, passed it.
    """
    by_reg: dict[str, dict[str, int]] = {}
    for row in rows:
        reg = str(row.get("regulation") or "—").strip("*_ ")
        bucket = by_reg.setdefault(reg, {})
        bucket[row["verdict"]] = bucket.get(row["verdict"], 0) + 1
    totals: dict[str, int] = {}
    for row in rows:
        totals[row["verdict"]] = totals.get(row["verdict"], 0) + 1
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
    for reg in sorted(by_reg):
        bucket = by_reg[reg]
        n = sum(bucket.values())
        lines.append(f"- **{reg}:** {bucket.get('Fully covered (anchored)', 0)} fully covered, "
                     f"{bucket.get('Partially covered (functional leg + explicit carve-out)', 0)} partial, "
                     f"{bucket.get('No functional carrier (organizational)', 0)} organizational "
                     f"({n} objective(s) under this regulation)")
    lines += ["", "## Security verdict", "",
              f"- {totals.get('Fully covered (anchored)', 0)} of {len(rows)} objectives fully carried after the round;"
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


def gate_input_paths(run_dir: Path) -> list[Path]:
    """Every file whose content the verdict below depends on.

    The report carries a digest of these, so a reader can tell whether the
    verdict in front of them is still the verdict the run deserves. A gate
    verdict that outlives its inputs is worse than no gate: it was CONCLUDED at
    16:36 on run_p2enr_c1, `p3a_prin` and `p3a_round` later opened seven
    verdicts, and nothing said so.
    """
    paths = [
        run_dir / "outputs" / "phase2" / "Doc01_Operational_Objectives.md",
        run_dir / "outputs" / "phase3" / "synthesis_rounds" / "OBJECTIVE_MAPPING.md",
        run_dir / "outputs" / "phase3" / "synthesis_rounds" / "ROUND1_REGISTER.md",
        run_dir / "outputs" / "phase3" / "synthesis_rounds" / "SUFFICIENCY_ASSESSMENT.md",
        run_dir / "outputs" / "phase3" / "synthesis_rounds" / "STEP4_CONSTRAINT_ABSORPTION.md",
        run_dir / "steps" / "phase3" / "round1_state.json",
        run_dir / "steps" / "gates" / "G-P3-A.approved",
    ]
    paths += sorted((run_dir / "steps" / "phase3").glob("verdicts_*.json"))
    return paths


def inputs_digest(run_dir: Path) -> str:
    """Content-independent fingerprint: identity, mtime and size of every input."""
    h = hashlib.sha256()
    for path in gate_input_paths(run_dir):
        try:
            st = path.stat()
            h.update(f"{path}|{st.st_mtime_ns}|{st.st_size}\n".encode())
        except OSError:
            h.update(f"{path}|missing\n".encode())
    return h.hexdigest()[:16]


def _sufficiency_findings(path: Path, n_rows: int) -> list[str]:
    """G5 measured the verdict per regulation, not the existence of a file.

    The renderer relabelled the whole-matrix total once per regulation, so two
    regulations got byte-identical lines and the gate passed them.
    """
    if not path.is_file():
        return ["SUFFICIENCY_ASSESSMENT missing"]
    found = []
    triples = set()
    n_lines = 0
    for line in path.read_text(encoding="utf-8").splitlines():
        m = RE_SUFFICIENCY_ROW.match(line)
        if m:
            n_lines += 1
            triples.add((int(m["full"]), int(m["partial"]), int(m["org"])))
    if not n_lines:
        found.append("no per-regulation verdict line found")
    elif len(triples) == 1:
        found.append(
            f"all {n_lines} regulation lines carry the same counts {triples.pop()} — "
            "the whole-matrix total relabelled, not a per-regulation verdict"
        )
    elif n_rows and sum(sum(t) for t in triples) < n_rows:
        found.append(f"per-regulation counts sum below the {n_rows} matrix rows — a row has no regulation")
    return found


def _step4_findings(path: Path, n_accepted: int) -> list[str]:
    """G6 measured the existence of a file; it now measures the absorption itself."""
    if not path.is_file():
        return ["STEP4 absorption table missing (run p3a_weave)"]
    rows = sum(1 for line in path.read_text(encoding="utf-8").splitlines() if RE_STEP4_ROW.match(line))
    if rows != n_accepted:
        return [f"{rows} absorption row(s) for {n_accepted} accepted constraint(s)"]
    return []


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

    # G1 — the matrix AND the principle layer are placed (ADR-006: "every Phase 2
    # objective and every principle placed, zero silent/pending"). Reading only
    # the rows let a run pass with PRINCIPLE_MAPPING at "Bound 0 / Pending 7".
    unset = [r["id"] for r in rows if r.get("verdict") in (None, "—", "")]
    pending_principles = [o for o in round_state.get("open", []) if str(o).startswith("PRIN-")]
    g1_problems = []
    if not rows:
        g1_problems.append("empty matrix")
    if unset:
        g1_problems.append(f"{len(unset)} verdict(s) unset")
    if any(f.startswith("T-G1") for f in findings):
        g1_problems.append("skeleton findings")
    if pending_principles:
        g1_problems.append(
            f"{len(pending_principles)} principle(s) unplaced ({', '.join(pending_principles[:3])}"
            f"{'…' if len(pending_principles) > 3 else ''})"
        )
    gates["G1"] = "CLOSED" if not g1_problems else "OPEN — " + "; ".join(g1_problems)

    # G3 — accepted constraints cite published anchors
    g3_findings = [f for f in findings if f.startswith("T6")]
    gates["G3"] = "CLOSED" if not g3_findings else f"OPEN — {len(g3_findings)} anchor finding(s)"

    # G4 — doc_lint --strict over THIS run's deliverables. The lint walks the
    # repo scopes on its own, and output/<case>/phase3/ was empty, so the gate
    # was passing on the hand-written corpus while never reading the run.
    deliverables = run_dir / "outputs" / "phase3"
    if deliverables.is_dir():
        lint = subprocess.run(
            ["python3", str(repo / "scripts" / "doc_lint.py"), "--strict", str(deliverables)],
            capture_output=True, text=True, timeout=120,
        )
        gates["G4"] = "CLOSED" if lint.returncode == 0 else f"OPEN — doc_lint: {lint.stdout[-400:] or lint.stderr[-400:]}"
    else:
        gates["G4"] = f"OPEN — no deliverables at {deliverables} to lint"

    # G5 — a per-regulation verdict, not the existence of a file
    suff_findings = _sufficiency_findings(
        run_dir / "outputs" / "phase3" / "synthesis_rounds" / "SUFFICIENCY_ASSESSMENT.md", len(rows)
    )
    gates["G5"] = "CLOSED" if not suff_findings else "OPEN — " + suff_findings[0]

    # G6 — one absorption row per accepted constraint
    step4_findings = _step4_findings(
        run_dir / "outputs" / "phase3" / "synthesis_rounds" / "STEP4_CONSTRAINT_ABSORPTION.md",
        len(round_state.get("accepted", [])),
    )
    gates["G6"] = "CLOSED" if not step4_findings else "OPEN — " + step4_findings[0]

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
        "n_principles_pending": len(pending_principles),
        "inputs_digest": inputs_digest(run_dir),
    }


def previous_digest(run_dir: Path) -> str | None:
    """The digest the report on disk was written with, if any."""
    report = run_dir / "steps" / "phase3" / "gate_report.md"
    if not report.is_file():
        return None
    m = re.search(r"^inputs_digest:\s*(\S+)", report.read_text(encoding="utf-8"), re.MULTILINE)
    return m.group(1) if m else None


def render_gate_report(report: dict) -> str:
    lines = [
        "---",
        "title: 'Phase 3 Part 1 — exit gate report'",
        "generated_by: 'p3a_gate (wave 6)'",
        f"state: {report['state']}",
        f"inputs_digest: {report['inputs_digest']}",
        "---",
        "",
        f"# Exit gate — state: **{report['state']}**",
        "",
        "| Gate | Verdict |",
        "|---|---|",
    ]
    for gate in ("G1", "G2", "G3", "G4", "G5", "G6"):
        lines.append(f"| {gate} | {report['gates'].get(gate, '—')} |")
    lines += [
        "",
        f"Objectives in the matrix: {report['n_objectives']}.",
        f"Principles unplaced: {report.get('n_principles_pending', 0)}.",
        "",
        f"Judged inputs digest: `{report['inputs_digest']}`. A later stage that writes "
        "any gate input makes this verdict stale — re-run `p3a_gate`.",
    ]
    if report["findings"]:
        lines += ["", "## Findings", ""]
        lines += [f"- {f}" for f in report["findings"][:40]]
    lines.append("")
    return "\n".join(lines) + "\n"
