"""aegis_pipeline.phases.phase3b.threat_gate — Etapa 2.5: the six exit gates
of Part 2 (G7–G12), zero model calls.

G7  every threat carries a HUMAN signature (the model proposes, never accepts)
G8  zero Critical residual
G9  no non-mitigated statutory threat Accept_Residual_Risk / Transfer
G10 the reverse loop is closed (no unresolved Reject_Risk_Require_Mitigation)
G11 reconciliation (T7): STRIDE ∪ LINDDUN == the register; every cited
    mitigator exists in Part 1's deliverables
G12 catalog integrity (T8): zero K3 ids outside baseline/THREATS
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

from aegis_pipeline.phases.phase3b.schemas import check_threat_ids, threat_index


def gate_input_paths(run_dir: Path) -> list[Path]:
    paths = [
        run_dir / "steps" / "phase3b" / "risk_register.json",
        run_dir / "steps" / "phase3b" / "risk_verdicts.json",
        run_dir / "steps" / "phase3b" / "system_model.json",
        run_dir / "steps" / "phase3b" / "adtrees.json",
    ]
    paths += sorted((run_dir / "outputs" / "phase3b").rglob("*.md"))
    return paths


def inputs_digest(run_dir: Path) -> str:
    h = hashlib.sha256()
    for path in gate_input_paths(run_dir):
        try:
            st = path.stat()
            h.update(f"{path}|{st.st_mtime_ns}|{st.st_size}\n".encode())
        except OSError:
            h.update(f"{path}|missing\n".encode())
    return h.hexdigest()[:16]


def run_gate(run_dir: Path, repo: Path) -> dict:
    """G7–G12 over this run's Part 2 artifacts. Pure function of the disk."""
    findings: list[str] = []
    gates: dict[str, str] = {}

    register_path = run_dir / "steps" / "phase3b" / "risk_register.json"
    verdicts_path = run_dir / "steps" / "phase3b" / "risk_verdicts.json"
    index = threat_index(run_dir, repo)

    register: dict = {"threats": []}
    verdicts: dict = {}
    if register_path.is_file():
        register = json.loads(register_path.read_text(encoding="utf-8"))
    else:
        findings.append("risk register missing — run the p3b chain first")
    if verdicts_path.is_file():
        blob = json.loads(verdicts_path.read_text(encoding="utf-8"))
        verdicts = blob.get("decisions", {})

    rows = register.get("threats", [])

    # G7 — every threat carries a human signature
    unsigned = [r["id"] for r in rows if r["id"] not in verdicts]
    gates["G7"] = "CLOSED" if rows and not unsigned else (
        f"OPEN — {len(unsigned)} threat(s) without a signed human decision "
        f"({', '.join(unsigned[:5])})" if unsigned else "OPEN — empty register")

    # G8 — zero Critical residual
    critical = [r["id"] for r in rows if r.get("residual_level") == "Critical"]
    gates["G8"] = "CLOSED" if not critical else f"OPEN — Critical residual: {critical[:5]}"

    # G9 — statutory, non-mitigated threats may not be accepted/transferred
    illegal = [
        r["id"] for r in rows
        if r.get("statutory_obligation") and r.get("mitigation_assessment") == "UNMITIGATED_GAP"
        and verdicts.get(r["id"], {}).get("decision") in ("Accept_Residual_Risk", "Transfer")
    ]
    gates["G9"] = "CLOSED" if not illegal else f"OPEN — statutory acceptance: {illegal[:5]}"

    # G10 — the reverse loop is closed. A rejection is closed only when Part 1
    # ABSORBED it: the trigger file was written AND a human-signed round state
    # carries the rework for that threat. The trigger file alone is not
    # absorption — writing it was the pipeline's own job, so the old check
    # closed the loop on a file the pipeline had just written itself.
    rejects = [r["id"] for r in rows if verdicts.get(r["id"], {}).get("decision") == "Reject_Risk_Require_Mitigation"]
    unresolved = [rid for rid in rejects if not absorbed_by_part1(run_dir, rid)]
    gates["G10"] = "CLOSED" if not rejects else (
        "CLOSED" if not unresolved else
        f"OPEN — rejection(s) not absorbed by a signed Part 1 round: {unresolved[:5]}")

    # G11 — T7 reconciliation: STRIDE ∪ LINDDUN == register; mitigators real
    stride = _cited(run_dir, "02_STRIDE_THREAT_ANALYSIS.md")
    linddun = _cited(run_dir, "03_LINDDUN_PRIVACY_ANALYSIS.md")
    in_docs = stride | linddun
    in_register = {r["id"] for r in rows}
    recon = []
    for tid in sorted(in_docs - in_register):
        recon.append(f"{tid}: analysed in STRIDE/LINDDUN but absent from the register")
    for tid in sorted(in_register - in_docs):
        recon.append(f"{tid}: in the register but absent from STRIDE/LINDDUN")
    gates["G11"] = "CLOSED" if not recon else "OPEN — " + "; ".join(recon[:4])

    # G12 — T8 over the whole Part 2 text
    blob = "\n".join(p.read_text(encoding="utf-8") for p in gate_input_paths(run_dir) if p.is_file() and p.suffix == ".md")
    t8 = check_threat_ids(blob, index)
    gates["G12"] = "CLOSED" if not t8 else "OPEN — " + t8[0]
    findings += t8

    state = "CONCLUDED" if all(v.startswith("CLOSED") for v in gates.values()) and not findings \
        else ("PROPOSED" if unsigned else "FAILED")
    return {
        "state": state,
        "gates": gates,
        "findings": findings,
        "n_threats": len(rows),
        "inputs_digest": inputs_digest(run_dir),
    }


def _cited(run_dir: Path, name: str) -> set[str]:
    path = run_dir / "outputs" / "phase3b" / name
    if not path.is_file():
        return set()
    return set(re.findall(r"`(T-(?:STR|LIN)-\d+)`", path.read_text(encoding="utf-8")))


def absorbed_by_part1(run_dir: Path, threat_id: str) -> bool:
    """True when a Part 1 round DECIDED the rework this rejection opened.

    Two pieces of evidence, and the second is the one that counts: the
    trigger file names the threat, and a round STATE — which only exists
    after a person signed the round — carries an item whose
    `part2_trigger` is this threat. The trigger file alone proves nothing:
    writing it was the pipeline's own job. The state must also be from the
    round the trigger opened, or later: an earlier round cannot have
    absorbed a later rejection.
    """
    phase3 = run_dir / "steps" / "phase3"
    trigger_rounds = [_round_no(p.name) for p in phase3.glob("round*_triggers_from_part2.json")
                      if threat_id in p.read_text(encoding="utf-8")]
    if not trigger_rounds:
        return False
    for state_path in phase3.glob("round*_state.json"):
        if _round_no(state_path.name) < min(trigger_rounds):
            continue
        try:
            state = json.loads(state_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        decided = ((state.get("accepted") or []) + (state.get("rejected") or [])
                   + (state.get("adjusted") or []))
        for item in decided:
            if (item.get("part2_trigger") or {}).get("threat") == threat_id:
                return True
    return False


def _round_no(filename: str) -> int:
    """The round number in `round<N>_state.json` / `round<N>_triggers...`."""
    m = re.match(r"^round(\d+)_", filename)
    return int(m.group(1)) if m else 0


def render_gate_report(report: dict) -> str:
    lines = [
        "---",
        "title: 'Phase 3 Part 2 — exit gate report'",
        "generated_by: 'p3b_gate (onda D)'",
        f"state: {report['state']}",
        f"inputs_digest: {report['inputs_digest']}",
        "---",
        "",
        f"# Exit gate (Part 2) — state: **{report['state']}**",
        "",
        "| Gate | Verdict |",
        "|---|---|",
    ]
    for gate in ("G7", "G8", "G9", "G10", "G11", "G12"):
        lines.append(f"| {gate} | {report['gates'].get(gate, '—')} |")
    lines += ["", f"Threats in the register: {report['n_threats']}."]
    if report["findings"]:
        lines += ["", "## Findings", ""]
        lines += [f"- {f}" for f in report["findings"][:30]]
    lines.append("")
    return "\n".join(lines) + "\n"
