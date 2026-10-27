"""Wave 4 — constraint proposal and the acceptance round.

The first `p3a_map` run measured the failure this stage exists to fix: the
model pushed 52 of 65 objectives to `No functional carrier (organizational)`
because the V0 pool has no security cards. The corrective route is a proposal
per objective — an EARS constraint with a binary fit criterion, the risk it
addresses, and a chain whose anchors stay inside the objective's published set
— which the human round then Accepts / Rejects (explicit risk acceptance) /
Adjusts, item by item (ADR-005).
"""

from __future__ import annotations

import re
from pathlib import Path

from aegis_pipeline.guards.quality_gates import check_no_technology

RE_OBJECTIVE = re.compile(r"^(?:PO|SO)-D-\d{2}\.\d-\d{3}$")
RE_ANCHOR = re.compile(r"[A-Z]{2}\.[A-Z0-9-]+(?:-\d+)?")
PROPOSAL_ACTIONS = ("propose", "round 2")


def load_rule_catalogue(run_dir: Path) -> dict[str, list[dict]]:
    """{objective_id: [rule, ...]} from the Phase 2 operationalization store.

    The `RULE-*` tail is the only artefact Phase 2 produces that Phase 1 does
    not, and until now nothing read it: Phase 3 loaded the Phase 2 document
    through a 9-cell row filter keyed on `PO-/SO-` ids, and the RULE rows have
    4 cells, so they were structurally invisible. This is the catalogue a
    proposal cites when it says which rule it discharges.

    The store is `steps/phase2/*.json`, not the rendered markdown: the parent
    objective is recoverable from the `objectives[].rules[]` nesting there,
    while the rendered row loses it.
    """
    from aegis_pipeline.phases.phase2.parsers import load_operationalizations

    out: dict[str, list[dict]] = {}
    for blob in load_operationalizations(run_dir).values():
        for o in blob.get("objectives") or []:
            oid = str(o.get("objective_id") or "")
            rules = [r for r in (o.get("rules") or []) if r.get("rule_id")]
            if oid and rules:
                out[oid] = rules
    return out


def select_proposal_targets(rows: list[dict]) -> list[dict]:
    """Rows the model itself flagged for a proposal.

    The selector reads the matrix's own `Action / Round` column (`Propose for
    Round 2: …`), written by the verdict stage — no second judgement here. A
    row that names no action and no pending-proposal discharge is not a target;
    the round can still add one by hand.
    """
    targets = []
    for row in rows:
        action = (row.get("action") or "").lower()
        discharge = (row.get("discharge") or "").lower()
        if any(marker in action for marker in PROPOSAL_ACTIONS) or "pending proposal" in discharge:
            targets.append(row)
    return targets


def parse_proposals(answer: str, targets: list[dict],
                     rules: dict[str, list[dict]] | None = None) -> list[dict]:
    """L0 for the proposal call: one `### <objective-id>` block per target."""
    from aegis_pipeline.phases.phase1.common import extract_fenced

    block = extract_fenced(answer, "markdown").strip()
    sections: dict[str, str] = {}
    current: str | None = None
    for line in block.splitlines():
        if line.startswith("###"):
            current = line.lstrip("#").strip().strip("`")
            if current in sections:
                raise ValueError(f"proposals: objective {current} appears twice")
            sections[current] = ""
        elif current is not None:
            sections[current] += line + "\n"

    expected = [t["id"] for t in targets]
    missing = [oid for oid in expected if oid not in sections]
    if missing:
        raise ValueError(f"proposals: no block for {len(missing)} target(s): {missing[:6]}")
    invented = [oid for oid in sections if oid not in expected]
    if invented:
        raise ValueError(f"proposals: blocks for non-target objectives: {invented[:6]}")

    out: list[dict] = []
    for oid in expected:
        body = sections[oid]
        fields: dict[str, str] = {}
        for field in ("Constraint (EARS)", "Fit criterion", "Risk addressed", "Chain anchors", "Proposed carrier"):
            m = re.search(rf"\*\*{re.escape(field)}:?\*\*\s*(.+)", body)
            if not m:
                raise ValueError(f"proposals [{oid}]: missing field {field!r}")
            fields[field] = m.group(1).strip()
        if not re.search(r"\bshall\b", fields["Constraint (EARS)"], re.IGNORECASE):
            raise ValueError(f"proposals [{oid}]: constraint is not EARS — no 'shall'")
        if not fields["Fit criterion"]:
            raise ValueError(f"proposals [{oid}]: empty fit criterion")
        if not fields["Risk addressed"]:
            raise ValueError(f"proposals [{oid}]: empty risk")
        anchors = [a.strip().strip("`") for a in fields["Chain anchors"].split(",") if a.strip()]
        if not anchors:
            raise ValueError(f"proposals [{oid}]: no chain anchors")
        # `Rules discharged` is REQUIRED when the objective carries Phase 2
        # rules. Measured 2026-10-22 on the cluster: with the field merely
        # permitted, 18 of 18 proposals omitted it — the model does not use a
        # field it is not required to, and the tail stayed an orphan with a
        # consumer that never fired. When the objective has no rule there is
        # nothing to discharge and the field is absent.
        rm = re.search(r"\*\*Rules discharged:?\*\*\s*(.+)", body)
        cited = [r.strip().strip("`") for r in rm.group(1).split(",") if r.strip()] if rm else []
        owned = {str(r.get("rule_id")) for r in (rules or {}).get(oid, [])}
        if owned and not cited:
            raise ValueError(
                f"proposals [{oid}]: no rule cited, but the objective carries "
                f"{len(owned)} Phase 2 rule(s) ({', '.join(sorted(owned))})"
            )
        out.append({
            "objective": oid,
            # `PO-D-01.2-001`.split("-")[1] is "D" — the same truncation org.py
            # shipped, and it survives into the accepted round state, where the
            # weave routes on it.
            "subdomain": re.match(r"^(?:PO|SO)-(D-\d{2}\.\d)-", oid).group(1),
            "constraint": fields["Constraint (EARS)"],
            "fit_criterion": fields["Fit criterion"],
            "risk": fields["Risk addressed"],
            "anchors": anchors,
            "rules": cited,
            "carrier": fields["Proposed carrier"],
        })
    return {"proposals": out}


def check_proposals(
    proposals: list[dict],
    rows: list[dict],
    objectives: list[dict],
    rules: dict[str, list[dict]] | None = None,
) -> list[str]:
    """Semantic gates: published anchors only (T6), technology ban, ids real."""
    findings: list[str] = []
    published: dict[str, set[str]] = {}
    for o in objectives:
        raw_val = o.get("anchors_raw", o.get("anchors", ""))
        if isinstance(raw_val, (list, set)):
            published[o["id"]] = {str(a).strip("` ") for a in raw_val if str(a).strip("` ")}
        elif isinstance(raw_val, str):
            published[o["id"]] = {a.strip("` ") for a in re.findall(r"`?([A-Za-z0-9._-]+)`?", raw_val) if a.strip("` ")}
        else:
            published[o["id"]] = set()
    known = {row["id"] for row in rows}
    for proposal in proposals:
        oid = proposal["objective"]
        if oid not in known:
            findings.append(f"{oid}: proposal for an objective that is not in the matrix")
            continue
        tech = check_no_technology(proposal["constraint"], proposal["fit_criterion"])
        if tech:
            findings.append(f"{oid}: technology vocabulary (R5/L4): {tech}")
        allowed_anchors = published.get(oid, set())
        for anchor in proposal["anchors"]:
            clean_anchor = anchor.strip("` ")
            if clean_anchor and clean_anchor not in allowed_anchors:
                findings.append(
                    f"{oid}: anchor {anchor!r} is not in the objective's published set (T6)"
                )
        allowed = {str(r.get("rule_id")) for r in (rules or {}).get(oid, [])}
        for rule in proposal.get("rules") or []:
            if rule not in allowed:
                findings.append(
                    f"{oid}: rule {rule!r} is not a Phase 2 rule of this objective"
                )
    return findings


def round_key(proposal: dict) -> str:
    """The id a verdict is entered under.

    Objective-driven proposals are keyed by objective. A principle-derived
    constraint is keyed by the PRINCIPLE, because it is a different artefact
    discharging the same objective: `SO-D-07.2-001` has both an objective-driven
    card and the PRIN-ENG-02 constraint, and one verdict cannot govern two
    constraints. The plan recorded the opposite decision ("principle proposals
    are not distinguished in the round") and the run falsified it.
    """
    return proposal.get("principle") or proposal["objective"]


def apply_round_verdicts(
    proposals: list[dict],
    verdicts: dict[str, str],
) -> dict:
    """Split proposals by the human round verdict. Reject = explicit, recorded."""
    allowed = {"Accept", "Reject", "Adjust"}
    accepted, rejected, adjusted, open_items = [], [], [], []
    for proposal in proposals:
        key = round_key(proposal)
        verdict = verdicts.get(key)
        if verdict is None:
            open_items.append(key)
        elif verdict not in allowed:
            raise ValueError(
                f"round: verdict {verdict!r} for {key} not in {sorted(allowed)}"
            )
        elif verdict == "Accept":
            accepted.append(proposal)
        elif verdict == "Reject":
            rejected.append(proposal)
        else:
            adjusted.append(proposal)
    return {
        "accepted": accepted,
        "rejected": rejected,
        "adjusted": adjusted,
        "open": open_items,
        "converged": not open_items,
    }


def render_proposal_derivation(proposals: list[dict]) -> str:
    """The STEP2-style derivation table (gabarito: Case 01 analysis_v1_to_v2)."""
    lines = [
        "---",
        "title: 'STEP2 — Round 1 proposal derivation'",
        "generated_by: 'p3a_propose (wave 4)'",
        "---",
        "",
        "| Item | Objective | Proposed constraint (L2, EARS) | Chain | Risk addressed |",
        "|---|---|---|---|---|",
    ]
    for index, proposal in enumerate(proposals, start=1):
        chain = " + ".join(proposal["anchors"])
        lines.append(
            f"| P-{index:02d} | `{proposal['objective']}` | {proposal['constraint']} "
            f"**Fit:** {proposal['fit_criterion']} | {chain} | {proposal['risk']} |"
        )
    lines.append("")
    return "\n".join(lines) + "\n"


def render_round_register(
    proposals: list[dict],
    verdict_map: dict[str, str],
    converged: bool,
) -> str:
    """The ROUND<n>_REGISTER scaffold/final: §1 verdict ledger over the proposals."""
    lines = [
        "---",
        "title: 'ROUND1_REGISTER — acceptance round (generated scaffold; verdicts are human)'",
        "generated_by: 'p3a_propose (wave 4) + p3a_round (wave 4)'",
        "---",
        "",
        "## §1 Verdict ledger",
        "",
        "| Item | Verdict key | Discharges | Proposed constraint | Verdict |",
        "|---|---|---|---|---|",
    ]
    for index, proposal in enumerate(proposals, start=1):
        key = round_key(proposal)
        verdict = verdict_map.get(key, "**pending**")
        lines.append(
            f"| P-{index:02d} | `{key}` | `{proposal['objective']}` | "
            f"{proposal['constraint'][:140]} | {verdict} |"
        )
    lines += [
        "",
        "## §2 How to close this round",
        "",
        "1. Enter one verdict per item — `Accept`, `Reject` (= explicit risk acceptance,",
        "   recorded, never silent) or `Adjust` — in `steps/phase3/round1_verdicts.json`",
        "   under `\"verdicts\": {\"<verdict-key>\": \"Accept|Reject|Adjust\"}`. The key is the",
        "   objective id, or the principle id for a constraint derived from a principle —",
        "   a principle id is separate because one objective can carry two constraints.",
        "2. Create `steps/gates/G-P3-A.approved` with the review note (≥200 chars).",
        "3. Re-run `--stage p3a_round`: the gate evaluates only on the CONCLUDED state.",
        "",
        f"Round state: **{'CONVERGED' if converged else 'OPEN'}**.",
        "",
    ]
    return "\n".join(lines) + "\n"


def allocate_new_cards(
    accepted: list[dict], existing: list[str], start_seq: int = 9
) -> list[dict]:
    """Derive one new functional card per accepted proposal whose carrier is `new`.

    The proposal already carries everything a card needs — the EARS constraint
    is the description, the fit criterion is the acceptance bar, the risk is the
    origin — so this is allocation, not generation, and needs no model call.
    This is the D1 path the hand-written Round 1 used for `R8.3`.

    Cards group by the proposal's sub-domain root (R9.x under a D-XX.Y with two
    duties gets R9.1, R9.2). The returned cards carry `dispositions` because the
    weave and the stage result read it.
    """
    by_sub: dict[str, int] = {}
    out = []
    for proposal in accepted:
        if (proposal.get("carrier") or "").strip("`") != "new":
            continue
        sub = proposal["subdomain"]
        n = by_sub.get(sub, 0) + 1
        by_sub[sub] = n
        card = {
            "id": f"R{start_seq}.{n}",
            "name": f"Apply the {sub} security constraint",
            "description": proposal["constraint"].rstrip("."),
            "origin": f"Round 1 accepted proposal for `{proposal['objective']}` — {proposal['risk'][:140]}",
            "constraints": [
                {
                    "id": f"RN-{proposal['objective']}",
                    "text": proposal["constraint"],
                    "fit_criterion": proposal["fit_criterion"],
                    "chain": proposal["anchors"],
                }
            ],
            "priority": "Must",
            "objectives": [proposal["objective"]],
            "subdomain": sub,
        }
        out.append(card)
    used = set(existing)
    for card in out:
        while card["id"] in used:
            card["id"] = f"R{int(card['id'][1:].split('.')[0]) + 1}.{card['id'].split('.')[1]}"
        used.add(card["id"])
    return out
