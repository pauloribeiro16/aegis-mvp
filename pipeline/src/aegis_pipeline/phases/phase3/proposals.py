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

from aegis_pipeline.guards.quality_gates import check_no_technology

RE_OBJECTIVE = re.compile(r"^(?:PO|SO)-D-\d{2}\.\d-\d{3}$")
RE_ANCHOR = re.compile(r"[A-Z]{2}\.[A-Z0-9-]+(?:-\d+)?")
PROPOSAL_ACTIONS = ("propose", "round 2")


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


def parse_proposals(answer: str, targets: list[dict]) -> list[dict]:
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
            "carrier": fields["Proposed carrier"],
        })
    return {"proposals": out}


def check_proposals(
    proposals: list[dict],
    rows: list[dict],
    objectives: list[dict],
) -> list[str]:
    """Semantic gates: published anchors only (T6), technology ban, ids real."""
    findings: list[str] = []
    published = {o["id"]: o.get("anchors_raw", o.get("anchors", "")) for o in objectives}
    known = {row["id"] for row in rows}
    for proposal in proposals:
        oid = proposal["objective"]
        if oid not in known:
            findings.append(f"{oid}: proposal for an objective that is not in the matrix")
            continue
        tech = check_no_technology(proposal["constraint"], proposal["fit_criterion"])
        if tech:
            findings.append(f"{oid}: technology vocabulary (R5/L4): {tech}")
        raw = str(published.get(oid, ""))
        for anchor in proposal["anchors"]:
            if anchor and anchor not in raw:
                findings.append(
                    f"{oid}: anchor {anchor!r} is not in the objective's published set (T6)"
                )
    return findings


def apply_round_verdicts(
    proposals: list[dict],
    verdicts: dict[str, str],
) -> dict:
    """Split proposals by the human round verdict. Reject = explicit, recorded."""
    allowed = {"Accept", "Reject", "Adjust"}
    accepted, rejected, adjusted, open_items = [], [], [], []
    for proposal in proposals:
        verdict = verdicts.get(proposal["objective"])
        if verdict is None:
            open_items.append(proposal["objective"])
        elif verdict not in allowed:
            raise ValueError(
                f"round: verdict {verdict!r} for {proposal['objective']} not in {sorted(allowed)}"
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
        "| Item | Objective | Proposed constraint | Verdict |",
        "|---|---|---|---|",
    ]
    for index, proposal in enumerate(proposals, start=1):
        verdict = verdict_map.get(proposal["objective"], "**pending**")
        lines.append(
            f"| P-{index:02d} | `{proposal['objective']}` | {proposal['constraint'][:140]} | {verdict} |"
        )
    lines += [
        "",
        "## §2 How to close this round",
        "",
        "1. Enter one verdict per item — `Accept`, `Reject` (= explicit risk acceptance,",
        "   recorded, never silent) or `Adjust` — in `steps/phase3/round1_verdicts.json`",
        "   under `\"verdicts\": {\"<objective-id>\": \"Accept|Reject|Adjust\"}`.",
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
