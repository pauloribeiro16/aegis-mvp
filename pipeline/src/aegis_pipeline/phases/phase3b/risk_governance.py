"""aegis_pipeline.phases.phase3b.risk_governance — Etapa 2.4: the golden rule.

The model composes the risk register in state PROPOSED; ONLY A PERSON decides.
`risk_verdicts.json` is human-exclusive — the pipeline writes the scaffold,
never a decision. A `Reject_Risk_Require_Mitigation` reopens Part 1 (the
ADR-005 reverse loop) with the person's instruction attached.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from aegis_pipeline.phases.phase3b.schemas import (
    RISK_DECISIONS,
    STATUTORY_FORBIDDEN,
)

REQUIRED_SIGNATURE = ("decision", "accepted_by_person", "person_role", "justification", "review_signpost")


def compose_risk_register(threats: list[dict], trees: list[dict]) -> dict:
    """The PROPOSED register: one row per threat, residual from the code."""
    unbroken = {t["threat"] for t in trees if t.get("unbroken_attack_path")}
    rows = []
    for t in threats:
        rows.append({
            "id": t["id"], "method": t["method"], "target": t["target"],
            "category": t["category"], "threat": t["threat"],
            "inherent": f"{t['l_inh']}x{t['i_inh']}={t['inherent_score']} ({t['inherent_level']})",
            "mitigating_requirements": t["mitigating_requirements"],
            "mitigation_assessment": t["mitigation_assessment"],
            "defense": t["defense"],
            # The statutory flag travels with the row. It used to be dropped
            # here, and both G9 checks read the ROW: `row.get("statutory_
            # obligation")` was always None, so a non-mitigated statutory
            # threat could be accepted or transferred with nothing firing.
            "statutory_obligation": bool(t.get("statutory_obligation")),
            "residual": f"{t['l_res']}x{t['i_res']}={t['residual_score']} ({t['residual_level']})",
            "residual_level": t["residual_level"],
            "unbroken_attack_path": t["id"] in unbroken,
            "state": "PROPOSED",
        })
    return {"state": "PROPOSED", "threats": rows}


def scaffold_risk_verdicts(register: dict) -> dict:
    """The empty verdicts file: what the person fills, in what vocabulary."""
    return {
        "decisions": {},
        "instructions": (
            "ONE decision per threat id, written by a PERSON — the model never "
            "touches this file. Each entry: {\"decision\": \"Accept_Mitigated|"
            "Accept_Residual_Risk|Transfer|Avoid|Reject_Risk_Require_Mitigation\", "
            "\"accepted_by_person\": \"<name>\", \"person_role\": \"<role>\", "
            "\"justification\": \"<why>\", \"review_signpost\": \"<the condition that "
            "reopens this decision>\"}. A Reject_Risk_Require_Mitigation carries the "
            "mitigation instruction in \"justification\" and reopens Part 1."),
    }


def apply_risk_verdicts(register: dict, verdicts: dict[str, dict]) -> dict:
    """Validate the person's signatures; raise on anything unsigned or illegal."""
    rows = register["threats"]
    decisions = {}
    for row in rows:
        tid = row["id"]
        v = verdicts.get(tid)
        if not isinstance(v, dict):
            raise ValueError(f"risk verdicts: threat {tid} has no signed decision "
                             "(the gate does not close over an unsigned register)")
        missing = [k for k in REQUIRED_SIGNATURE if not str(v.get(k, "")).strip()]
        if missing:
            raise ValueError(f"risk verdicts [{tid}]: unsigned field(s) {missing}")
        decision = v["decision"]
        if decision not in RISK_DECISIONS:
            raise ValueError(f"risk verdicts [{tid}]: decision {decision!r} outside {RISK_DECISIONS}")
        if row["unbroken_attack_path"] and row["residual_level"] == "Low":
            raise ValueError(f"risk verdicts [{tid}]: the tree proves an open path — "
                             "this row may not read Low (run p3b_trees)")
        if decision in STATUTORY_FORBIDDEN and row.get("statutory_obligation") \
                and row["mitigation_assessment"] == "UNMITIGATED_GAP":
            raise ValueError(
                f"risk verdicts [{tid}]: a non-mitigated statutory obligation may not be "
                f"{decision} (G9) — mitigate it in Part 1")
        decisions[tid] = v
        row["decision"] = decision
        row["accepted_by_person"] = v["accepted_by_person"]
        row["person_role"] = v["person_role"]
        row["justification"] = v["justification"]
        row["review_signpost"] = v["review_signpost"]
        row["state"] = "DECIDED"
    register["decisions"] = decisions
    return register


def rejection_triggers(register: dict) -> list[dict]:
    """The reverse-loop payload: one instruction per rejected risk."""
    return [
        {"threat": row["id"], "target": row["target"],
         "instruction": row["justification"],
         "suggested_carrier_context": ", ".join(row["mitigating_requirements"]) or "—"}
        for row in register["threats"]
        if row.get("decision") == "Reject_Risk_Require_Mitigation"
    ]


def write_round_trigger(run_dir: Path, triggers: list[dict]) -> Path | None:
    """`round<N+1>_triggers_from_part2.json` — the file Part 1's repropose reads."""
    if not triggers:
        return None
    from aegis_pipeline.phases.phase3.proposals import latest_round

    n = latest_round(run_dir) + 1
    path = run_dir / "steps" / "phase3" / f"round{n}_triggers_from_part2.json"
    path.write_text(json.dumps({"from": "part2", "triggers": triggers},
                               indent=1, ensure_ascii=False), encoding="utf-8")
    return path


def render_risk_register(register: dict, company: str) -> str:
    """05_RISK_REGISTER_AND_GOVERNANCE — the deliverable with the signatures."""
    lines = [
        "---",
        f"title: '05 — Risk Register and Governance ({company})'",
        "generated_by: 'p3b_risk_round (onda D) — register PROPOSED by the model, "
        "decisions signed by a person'",
        "---",
        "",
        "| ID | Method | Target | Threat | Inherent | Mitigation | Residual | Decision | Signed by | Signpost |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    for row in register["threats"]:
        lines.append(
            f"| `{row['id']}` | {row['method']} | `{row['target']}` | {row['threat'][:120]} "
            f"| {row['inherent']} | {row['mitigation_assessment']} | {row['residual']} "
            f"| {row.get('decision', '**pending**')} "
            f"| {row.get('accepted_by_person', '—')} ({row.get('person_role', '—')}) "
            f"| {row.get('review_signpost', '—')} |")
    lines += ["", "## Rejections that reopen Part 1 (ADR-005 reverse loop)", ""]
    rejects = [r for r in register["threats"] if r.get("decision") == "Reject_Risk_Require_Mitigation"]
    if rejects:
        for r in rejects:
            lines.append(f"- `{r['id']}` — {r['justification']}")
    else:
        lines.append("- None.")
    if register.get("state") == "PROPOSED":
        lines += ["", "**The register is PROPOSED: no risk is accepted until a person "
                  "signs `steps/phase3b/risk_verdicts.json`.**", ""]
    lines.append("")
    return "\n".join(lines) + "\n"
