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
from aegis_pipeline.phases.phase3.proposals import latest_round

RE_CARD_ID = re.compile(r"^R\d+\.\d+$")
RE_SUFFICIENCY_ROW = re.compile(
    r"^-\s+\*\*(?P<reg>[A-Za-z0-9_][A-Za-z0-9_ ]*):\*\*\s+"
    r"(?P<full>\d+) fully covered,\s*(?P<partial>\d+) partial,\s*(?P<org>\d+) organizational"
    r"(?:,\s*(?P<guidance>\d+) design guidance)?"
    r"(?:,\s*(?P<na>\d+) N/A)?"
    r"(?:\s*\((?P<total>\d+) objective)?",
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
    slot = leftover_slot(fields)
    if slot:
        raise ValueError(
            f"weave [{card_id}]: unfilled template slot {slot!r} — name the "
            "constraint or the behaviour instead of leaving a placeholder "
            "(the exit gate's doc_lint refuses it: R12)")
    return {"card_id": card_id, **fields}


#: An unfilled template slot in a woven use case. The rule is the doc_lint's
#: own (R12), so L0 and the gate agree on what a leftover is: multi-token
#: lowercase ("accepted constraint") or SHOUTY ("YYYY-MM-DD"). Single short
#: tokens (<REG>, <id>) are path/field notation, and slots inside code spans
#: are notation too.
RE_TEMPLATE_SLOT = re.compile(r"<([A-Za-z][A-Za-z0-9 _.\-]{0,30})>")


def _is_leftover_slot(inner: str) -> bool:
    if re.fullmatch(r"[a-z]+(?:[ _\-][a-z0-9]+)+", inner):
        return True
    return bool(re.fullmatch(r"[A-Z]{4,}[A-Z0-9\-]*", inner))


def leftover_slot(fields: dict[str, str]) -> str | None:
    """The first unfilled template slot in the woven fields, if any.

    The model emitted one in run_p302_muse_c1 ("... an observable record
    generation capability is available per <accepted constraint>"), and the
    exit gate's doc_lint refused the deliverable (G4 OPEN). The defect has to
    be caught at L0, where the repair round can ask the model to name the
    constraint, instead of failing the gate on the disk.
    """
    for value in fields.values():
        prose = re.sub(r"`[^`]*`", "", value or "")
        for match in RE_TEMPLATE_SLOT.finditer(prose):
            if _is_leftover_slot(match.group(1)):
                return match.group(0)
    return None


def accepted_constraint_ids(round_state: dict) -> set[str]:
    """Objectives whose proposals the round accepted — the weave's input set."""
    return {p["objective"] for p in round_state.get("accepted", [])}


def uc_of_carrier(cards: list[dict], carrier: str) -> str:
    """The use case that carries this constraint, or "—" when there is none.

    A card allocated from an accepted `new` proposal has NO use case: it is a
    requirement card, not a V0 use case. The lookup used to hard-access
    `c["usecase"]["uc_id"]` and the whole weave stage died with
    `KeyError: 'usecase'` (job 2166550) on the first post-round run that
    reached it.
    """
    for card in cards:
        if card.get("id") != carrier:
            continue
        uc = card.get("usecase") or {}
        return uc.get("uc_id", "—")
    return "—"


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
        lines.append(
            f"- **{reg}:** {bucket.get('Fully covered (anchored)', 0)} fully covered, "
            f"{bucket.get('Partially covered (functional leg + explicit carve-out)', 0)} partial, "
            f"{bucket.get('No functional carrier (organizational)', 0)} organizational, "
            f"{bucket.get('Design guidance', 0)} design guidance, "
            f"{bucket.get('N/A', 0)} N/A "
            f"({n} objective(s) under this regulation)"
        )
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

    The set has to cover what the gates *read*, not what looks related. G4
    lints the whole `outputs/phase3/` tree and G6 judges a deliverable inside
    it, so those files are inputs; a digest that skipped them would miss the
    very mutation that matters. The case's frozen V0 baseline and the human
    duty audit live in the repository, not in the run, so no run-scoped
    fingerprint can cover them.
    """
    paths = [
        run_dir / "outputs" / "phase2" / "Doc01_Operational_Objectives.md",
        run_dir / "steps" / "gates" / "G-P3-A.approved",
        run_dir / "steps" / "phase3" / "duty_proposals.json",
        run_dir / "steps" / "phase3" / "duties.json",
        run_dir / "steps" / "phase3" / "duty_audit.md",
    ]
    # every round the run actually has — the digest must move when a later
    # round's state lands, and a round file the run does not have is no input
    for pattern in ("round*_state.json", "round*_verdicts.json", "round*_proposals.json"):
        paths += sorted((run_dir / "steps" / "phase3").glob(pattern))
    # every deliverable the gate lints or judges
    paths += sorted((run_dir / "outputs" / "phase3").rglob("*.md"))
    # every state file the verdict is derived from
    paths += sorted((run_dir / "steps" / "phase3").glob("verdicts_*.json"))
    paths += sorted((run_dir / "steps" / "phase3").glob("proposals_*.json"))
    for sub in ("cards", "org", "weave"):
        paths += sorted((run_dir / "steps" / "phase3" / sub).glob("*.json"))
    seen: set[Path] = set()
    unique: list[Path] = []
    for p in paths:
        if p not in seen:
            seen.add(p)
            unique.append(p)
    return unique


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

    Three defects are guarded here, all measured on real runs:

    * the renderer relabelling the whole-matrix total once per regulation, so
      two regulations got byte-identical lines (S7) — but only when there ARE
      at least two regulations, or a GDPR-only case fails forever;
    * a line whose own buckets do not sum to the total it declares;
    * the buckets across regulations summing below the matrix rows, which
      means a row's regulation column collapsed into one the renderer does
      not print (S8 — and a `Design guidance`/`N/A` row is exactly the kind
      the three-bucket renderer used to drop on the floor).
    """
    if not path.is_file():
        return ["SUFFICIENCY_ASSESSMENT missing"]
    found = []
    lines_by_reg: dict[str, dict[str, int]] = {}
    declared: dict[str, int] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = RE_SUFFICIENCY_ROW.match(line)
        if m:
            counts = {k: int(m[k] or 0) for k in ("full", "partial", "org", "guidance", "na")}
            lines_by_reg[m["reg"]] = counts
            if m["total"] is not None:
                declared[m["reg"]] = int(m["total"])
    if not lines_by_reg:
        found.append("no per-regulation verdict line found")
        return found
    if len(lines_by_reg) > 1 and len({tuple(v.values()) for v in lines_by_reg.values()}) == 1:
        sample_counts = next(iter(lines_by_reg.values()))
        found.append(
            f"all {len(lines_by_reg)} regulation lines carry the same counts {sample_counts} — "
            "the whole-matrix total relabelled, not a per-regulation verdict"
        )
    for reg, counts in lines_by_reg.items():
        if reg in declared and sum(counts.values()) != declared[reg]:
            found.append(
                f"{reg}: buckets sum to {sum(counts.values())} but the line declares "
                f"{declared[reg]} objectives"
            )
    counted = sum(sum(v.values()) for v in lines_by_reg.values())
    if n_rows and counted < n_rows:
        found.append(
            f"per-regulation buckets sum to {counted}, below the {n_rows} matrix rows "
            "— a row has no regulation the renderer prints"
        )
    return found


def _step4_findings(path: Path, n_accepted: int) -> list[str]:
    """G6 measured the existence of a file; it now measures the absorption itself."""
    if not path.is_file():
        return ["STEP4 absorption table missing (run p3a_weave)"]
    rows = sum(1 for line in path.read_text(encoding="utf-8").splitlines() if RE_STEP4_ROW.match(line))
    if rows != n_accepted:
        return [f"{rows} absorption row(s) for {n_accepted} accepted constraint(s)"]
    return []


def traceability_findings(run_dir: Path, repo: Path) -> list[str]:
    """The R12b referential-integrity layer, run over THIS run.

    `scripts/check_traceability.py` was rooted at the case corpus, so the
    pipeline never ran it: this gate's own docstring claimed it ran T1–T6
    and it did not. The script can now be pointed at a run directory, and
    pointed at run_p2enr_c1 it finds what the gate reported as CLOSED — two
    chains citing a law their driver does not carry, and thirteen objectives
    the matrix declares covered that no deliverable cites.

    R12b says the chains must be re-anchored "before any coverage verdict is
    credible", so these findings block CONCLUDED rather than decorating the
    report.
    """
    import subprocess
    import sys

    script = repo / "scripts" / "check_traceability.py"
    if not script.is_file():
        return []
    try:
        proc = subprocess.run(
            [sys.executable, str(script), "--run-dir", str(run_dir), "--json"],
            capture_output=True, text=True, timeout=180,
        )
    except (OSError, subprocess.SubprocessError):
        return ["referential-integrity layer could not be run — its verdict is unknown"]
    try:
        rows = json.loads(proc.stdout or "[]")
    except json.JSONDecodeError:
        return ["referential-integrity layer produced no readable verdict"]
    return [
        f"{r.get('check', 'T?')}: {Path(r.get('path', '')).name}:{r.get('line', 0)} — {r.get('text', '')}"
        for r in rows
    ]


def run_gate(run_dir: Path, repo: Path) -> dict:
    """The R12b referential-integrity layer (T1–T6 over this run) + doc_lint
    --strict + G1–G6 with the two-state rule."""
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
        case_id = json.loads((run_dir / "manifest.json").read_text()).get("case_id") if (run_dir / "manifest.json").is_file() else None
        pool = p3.ensure_v0_pool(run_dir, repo, case_id, source=p3.v0_source(run_dir), seed=False)
        pool_ids = [c["id"] for c in pool]
        findings += [f"T-matrix: {f}" for f in p3.check_verdicts(rows, objectives, pool_ids)]
        findings += [f"T6: {f}" for f in p3.check_anchors(rows)]
    else:
        findings.append("T-G1: coverage matrix or Phase 2 deliverable missing — run the earlier stages")

    # G2 / two-state rule — over the LATEST round (onda B): a round-2 ledger
    # open means the run is PROPOSED even if round 1 converged long ago.
    n_round = latest_round(run_dir)
    register = run_dir / "outputs" / "phase3" / "synthesis_rounds" / f"ROUND{n_round}_REGISTER.md"
    state_path = run_dir / "steps" / "phase3" / f"round{n_round}_state.json"
    marker = run_dir / "steps" / "gates" / "G-P3-A.approved"
    round_state: dict = {"converged": False, "open": ["(no round artifacts)"]}
    if state_path.is_file():
        round_state = json.loads(state_path.read_text(encoding="utf-8"))
    n_proposals = len(round_state.get("accepted", [])) + len(round_state.get("rejected", [])) + len(round_state.get("adjusted", [])) + len(round_state.get("open", []))
    n_pending = len(round_state.get("pending_adjustment", []))
    if not register.is_file():
        gates["G2"] = "OPEN — no round register (stage p3a_propose not run)"
    elif not marker.is_file():
        gates["G2"] = "OPEN — proposals recorded but no human marker (G-P3-A)"
    elif not round_state.get("converged"):
        if n_pending:
            gates["G2"] = (f"OPEN — round {n_round}: {n_pending} adjusted item(s) awaiting "
                           f"the round-{n_round + 1} repropose")
        else:
            gates["G2"] = (f"OPEN — round {n_round} proposed, not concluded: "
                           f"{len(round_state.get('open', []))} verdict(s) missing")
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
    chain_findings = traceability_findings(run_dir, repo)
    all_closed = all(v.startswith("CLOSED") for v in gates.values())
    if proposed:
        state = "PROPOSED"
    elif all_closed and not findings and not chain_findings:
        state = "CONCLUDED"
    else:
        state = "FAILED"
    live = inputs_digest(run_dir)
    prior = previous_digest(run_dir)
    return {
        "state": state,
        "gates": gates,
        "findings": findings,
        "chain_findings": chain_findings,
        "n_objectives": len(rows),
        "n_principles_pending": len(pending_principles),
        "inputs_digest": live,
        # The verdict that was on disk before this run, and whether it had
        # already been overtaken when this run started.
        "previous_digest": prior,
        "previous_verdict_stale": prior is not None and prior != live,
    }


def previous_digest(run_dir: Path) -> str | None:
    """The digest the report on disk was written with, if any."""
    report = run_dir / "steps" / "phase3" / "gate_report.md"
    if not report.is_file():
        return None
    m = re.search(r"^inputs_digest:\s*(\S+)", report.read_text(encoding="utf-8"), re.MULTILINE)
    return m.group(1) if m else None


def gate_report_is_stale(run_dir: Path) -> bool:
    """True when the report on disk no longer describes the run as it stands.

    The reader-side check. `run_gate` says what the verdict *is*; this says
    whether the verdict *in front of the reader* is still the one the run
    deserves. A report with no digest at all cannot be verified, so it is
    treated as stale rather than trusted.
    """
    prior = previous_digest(run_dir)
    if prior is None:
        return False
    return prior != inputs_digest(run_dir)


def invalidate_gate_report(run_dir: Path, since: str) -> bool:
    """Mark the report on disk as overtaken. Returns True if it was marked.

    Called when a stage writes after the gate ran. The report keeps the
    digest of the inputs it judged — that is the record of what it was a
    verdict about — and its `state:` becomes STALE, so a reader who opens the
    file alone cannot read it as a current certification.
    """
    report = run_dir / "steps" / "phase3" / "gate_report.md"
    if not report.is_file():
        return False
    text = report.read_text(encoding="utf-8")
    if re.search(r"^state:\s*STALE\s*$", text, re.MULTILINE):
        return False
    text = re.sub(r"^state:\s*\S+\s*$", "state: STALE", text, count=1, flags=re.MULTILINE)
    text = re.sub(r"^(inputs_digest:.*)$", r"\1\nstale_since: " + since, text,
                  count=1, flags=re.MULTILINE)
    text = text.replace(
        "# Exit gate — state: **",
        "# Exit gate — state: **STALE** (this verdict was overtaken; re-run `p3a_gate`) — ",
        1,
    )
    report.write_text(text, encoding="utf-8")
    return True


def export_deliverables(run_dir: Path, repo: Path, company: str, run_id: str) -> Path:
    """Copy the Part 1 notebooks into `<repo>/output/<company>/phase3/<run_id>/`.

    The one place the deliverable leaves the run directory. Doc00..Doc03 live
    in up to three mirrors inside the run (`part1_security_privacy/`, the
    `v2_*` roots, `synthesis_rounds/`) and the export flattens them, with the
    gate report and the round register alongside — a reader of the exported
    folder sees the specification AND the verdict that closed it.
    """
    export_dir = repo / "output" / company / "phase3" / run_id
    export_dir.mkdir(parents=True, exist_ok=True)
    import shutil
    for src_dir in (
        run_dir / "outputs" / "phase3" / "part1_security_privacy" / "v2_security_privacy_synthesis",
        run_dir / "outputs" / "phase3" / "v2_security_privacy_synthesis",
        run_dir / "outputs" / "phase3" / "part1_security_privacy",
        run_dir / "outputs" / "phase3" / "synthesis_rounds",
        run_dir / "steps" / "phase3",
    ):
        if src_dir.is_dir():
            for f in src_dir.glob("*.md"):
                shutil.copy2(f, export_dir / f.name)
    return export_dir


def render_gate_report(report: dict) -> str:
    lines = [
        "---",
        "title: 'Phase 3 Part 1 — exit gate report'",
        "generated_by: 'p3a_gate (wave 6)'",
        f"state: {report['state']}",
        f"inputs_digest: {report['inputs_digest']}",
    ]
    if report.get("previous_digest"):
        lines.append(f"superseded_digest: {report['previous_digest']}")
    if report.get("previous_verdict_stale"):
        lines.append("superseded_verdict: stale — the verdict this report replaces "
                     "had already been overtaken when it was written")
    lines += [
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
        f"Judged inputs digest: `{report['inputs_digest']}`. This verdict describes the "
        "run as of that fingerprint. A later write to any gate input makes it stale, "
        "and the report is then marked `state: STALE` — re-run `p3a_gate`.",
    ]
    if report["findings"]:
        lines += ["", "## Findings", ""]
        lines += [f"- {f}" for f in report["findings"][:40]]
    if report.get("chain_findings"):
        lines += ["", "## Referential integrity (R12b, over this run)", ""]
        lines += [f"- {f}" for f in report["chain_findings"][:40]]
        if len(report["chain_findings"]) > 40:
            lines.append(f"- … and {len(report['chain_findings']) - 40} more")
    lines.append("")
    return "\n".join(lines) + "\n"
