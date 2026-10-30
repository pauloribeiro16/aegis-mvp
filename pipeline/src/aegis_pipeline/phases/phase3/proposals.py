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

import json
import re
from pathlib import Path

from aegis_pipeline.guards.quality_gates import check_no_technology

RE_OBJECTIVE = re.compile(r"^(?:PO|SO)-D-\d{2}\.\d-\d{3}$")
RE_ANCHOR = re.compile(r"[A-Z]{2}\.[A-Z0-9-]+(?:-\d+)?")


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
    """Rows the verdict stage routed to the product lane.

    The selector reads the matrix's own Action column, a pure enum since
    Onda B (schemas.ACTIONS) — `PROPOSE_PRODUCT` is the whole contract. The
    old free-text column ("Propose for Round 2: …") is what this selector had
    to substring-mine, and the measured run routed 52 of 65 objectives
    around it. A row that names no enum action is not a target; the round
    can still add one by hand.
    """
    from aegis_pipeline.phases.phase3.schemas import ACTIONS

    targets = []
    for row in rows:
        action = (row.get("action") or "").replace("`", "").replace("*", "").strip().upper()
        if action == "PROPOSE_PRODUCT":
            targets.append(row)
        elif action and action not in ACTIONS:
            # A legacy run's stored free text is visible, never silently mined:
            # it does not select a target, and it says why.
            print(f"[p3a_propose] {row['id']}: action {row.get('action')!r} is not "
                  f"the enum — not a proposal target (re-run p3a_map for the enum column)",
                  flush=True)
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
        # Onda C L0: the acceptance bar is a black-box test — a mechanism name
        # in it pre-bakes the implementation the fit criterion exists to abstract.
        from aegis_pipeline.guards.quality_gates import check_fit_criterion_observable
        obs = check_fit_criterion_observable(fields["Fit criterion"])
        if obs:
            raise ValueError(f"proposals [{oid}]: {obs[0]}")
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


def with_part2_trigger(path: Path, item: dict) -> dict:
    """A rewritten proposal keeps the Part 2 rejection that opened it.

    The parser rebuilds the proposal from the model's answer, so the trigger
    does not survive on its own — and the trigger is what the exit gate reads
    to know that a rejection was absorbed.
    """
    stored = json.loads(path.read_text(encoding="utf-8"))
    trig = item.get("part2_trigger")
    if trig and not stored.get("part2_trigger"):
        stored["part2_trigger"] = trig
        path.write_text(json.dumps(stored, indent=1, ensure_ascii=False), encoding="utf-8")
    return stored


def part2_trigger_items(run_dir: Path, state: dict, round_no: int) -> list[dict]:
    """The rework items a Part 2 rejection opens (ADR-005 reverse loop).

    `p3b_risk_round` wrote `round<N>_triggers_from_part2.json` and NOTHING
    read it: the loop was open in name only, and the exit gate closed on a
    file the pipeline had written itself. Each rejection names the Part 1
    requirements the register cited as its mitigators — those are what Part 1
    has to rework, and the item carries the person's instruction so the
    rewrite knows which risk it is answering.
    """
    path = run_dir / "steps" / "phase3" / f"round{round_no}_triggers_from_part2.json"
    if not path.is_file():
        return []
    blob = json.loads(path.read_text(encoding="utf-8"))
    accepted = {round_key(p): p for p in (state.get("accepted") or [])}
    items: list[dict] = []
    for trig in blob.get("triggers", []):
        ids = {m.strip().strip("`")
               for m in (trig.get("suggested_carrier_context") or "").split(",")
               if m.strip().strip("`")}
        for key in sorted(ids):
            proposal = accepted.get(key)
            if proposal is None:
                # The mitigator is not an accepted proposal (an org card, or a
                # requirement that was never accepted): there is nothing here
                # to rework, and the rejection stays open.
                continue
            items.append({
                **proposal,
                "round_key": key,
                "part2_trigger": {
                    "threat": trig.get("threat"),
                    "instruction": trig.get("instruction", ""),
                },
            })
    return items


#: The verdicts a human may enter, and the functional-evolution operations the
#: verdicts file may register (R13 §3.4 taxonomy — Onda B).
ROUND_VERDICTS = ("Accept", "Reject", "Adjust")
FUNCTIONAL_CHANGES = ("D1", "D2", "D3", "D4")


# ---------------------------------------------------------------------------
# Round bookkeeping — the multi-round engine (Etapa 1.6 / 1.6.b, Onda B).
# ---------------------------------------------------------------------------

def _round_glob(run_dir: Path, kind: str) -> list[Path]:
    return sorted((run_dir / "steps" / "phase3").glob(f"round*_{kind}.json"))


def latest_round(run_dir: Path) -> int:
    """The highest round that has verdicts or state on disk; round 1 otherwise."""
    rounds = [int(p.stem.split("_")[0][len("round"):])
              for p in _round_glob(run_dir, "verdicts") + _round_glob(run_dir, "state")]
    return max(rounds) if rounds else 1


def latest_applied_round(run_dir: Path) -> int:
    """The highest round that has an APPLIED state (`round<N>_state.json`).

    `latest_round` counts every round file — including the verdicts SCAFFOLD
    that `p3a_repropose` itself writes for the human to fill. So a resumed
    repropose resolved to the NEXT round and died with "round N+1 has no
    applied state" (job 2166543). The stage needs the round whose items were
    applied, not the round whose paperwork exists.
    """
    rounds = [int(p.stem.split("_")[0][len("round"):])
              for p in _round_glob(run_dir, "state")]
    return max(rounds) if rounds else 1


def round_verdicts_path(run_dir: Path, n: int) -> Path:
    return run_dir / "steps" / "phase3" / f"round{n}_verdicts.json"


def round_state_path(run_dir: Path, n: int) -> Path:
    return run_dir / "steps" / "phase3" / f"round{n}_state.json"


def round_proposals_path(run_dir: Path, n: int) -> Path:
    return run_dir / "steps" / "phase3" / f"round{n}_proposals.json"


def scaffold_verdicts_file(n: int) -> dict:
    """The empty verdicts file: what the human fills, and in what vocabulary."""
    return {
        "verdicts": {},
        "notes": {},
        "instructions": (
            "enter Accept|Reject|Adjust per verdict key — the objective id for an "
            "objective-driven proposal, the principle id (PRIN-ENG-nn) for a "
            "constraint derived from a principle; one objective can carry two "
            "constraints, so the two keys are distinct verdicts. An Adjust verdict "
            "MUST carry its instruction under \"notes\" (the next round's repropose "
            "obeys it). Optional: \"functional_changes\" "
            "({\"item\", \"kind\": \"D1|D2|D3|D4\", \"target\", \"note\"}) and per-duty "
            "disposition overrides under \"duties\"."),
    }


def apply_round_verdicts(
    proposals: list[dict],
    verdicts: dict[str, str],
    notes: dict[str, str] | None = None,
    functional_changes: list[dict] | None = None,
) -> dict:
    """Split proposals by the human round verdict. Reject = explicit, recorded.

    Onda B: an `Adjust` verdict is NOT a quiet acceptance. The item enters
    `pending_adjustment[]` carrying the human's note, and the round does not
    converge while that list is non-empty — `p3a_repropose` rewrites exactly
    those items for the next round. The measured defect this closes: an
    all-Adjust round counted as converged and the weave absorbed proposals no
    human ever approved.

    `functional_changes` (D1 split / D2 merge / D3 retire / D4 new card) is
    validated against the round's items and recorded in the state; a D3 on an
    item retires it — the item moves to `retired[]` and gets no repropose.
    """
    allowed = set(ROUND_VERDICTS)
    notes = notes or {}
    changes = list(functional_changes or [])
    retired_keys = {c.get("item") for c in changes if c.get("kind") == "D3"}
    for c in changes:
        if c.get("kind") not in FUNCTIONAL_CHANGES:
            raise ValueError(
                f"round: functional change kind {c.get('kind')!r} outside {FUNCTIONAL_CHANGES}")
        if c.get("item") not in {round_key(p) for p in proposals}:
            raise ValueError(
                f"round: functional change on {c.get('item')!r}, which is not an item of this round")
    accepted, rejected, adjusted, pending, open_items, retired = [], [], [], [], [], []
    for proposal in proposals:
        key = round_key(proposal)
        verdict = verdicts.get(key)
        if verdict is None:
            open_items.append(key)
        elif verdict not in allowed:
            raise ValueError(
                f"round: verdict {verdict!r} for {key} not in {sorted(allowed)}")
        elif key in retired_keys:
            retired.append({**proposal, "retire_note": notes.get(key, "")})
        elif verdict == "Accept":
            accepted.append(proposal)
        elif verdict == "Reject":
            rejected.append({**proposal, "reject_note": notes.get(key, "")})
        else:
            adjusted.append(proposal)
            pending.append({**proposal, "adjust_note": notes.get(key, "")})
    return {
        "accepted": accepted,
        "rejected": rejected,
        "adjusted": adjusted,
        "pending_adjustment": pending,
        "retired": retired,
        "open": open_items,
        "functional_changes": changes,
        "converged": not open_items and not pending,
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
    round_no: int = 1,
    notes: dict[str, str] | None = None,
    functional_changes: list[dict] | None = None,
    duty_proposals: list[dict] | None = None,
    carried: dict[str, list[dict]] | None = None,
) -> str:
    """The ROUND<n>_REGISTER scaffold/final: §1 verdict ledger over the proposals."""
    notes = notes or {}
    lines = [
        "---",
        f"title: 'ROUND{round_no}_REGISTER — acceptance round (generated scaffold; verdicts are human)'",
        "generated_by: 'p3a_propose (wave 4) + p3a_round + p3a_repropose (onda B)'",
        "---",
        "",
        "## §1 Verdict ledger",
        "",
        "| Item | Verdict key | Discharges | Proposed constraint | Verdict | Note |",
        "|---|---|---|---|---|---|",
    ]
    for index, proposal in enumerate(proposals, start=1):
        key = round_key(proposal)
        verdict = verdict_map.get(key, "**pending**")
        note = notes.get(key, "—")
        lines.append(
            f"| P-{index:02d} | `{key}` | `{proposal['objective']}` | "
            f"{proposal['constraint'][:140]} | {verdict} | {note} |"
        )
    if carried:
        for kind in ("accepted", "rejected"):
            for proposal in carried.get(kind, []):
                lines.append(
                    f"| — | `{round_key(proposal)}` | `{proposal['objective']}` | "
                    f"{proposal['constraint'][:140]} | {kind.capitalize()} (carried) | — |"
                )
    if functional_changes:
        lines += ["", "## §2 Functional change register (D1–D4)", "",
                  "| Item | Kind | Target | Note |", "|---|---|---|---|"]
        for change in functional_changes:
            lines.append(
                f"| `{change.get('item', '—')}` | {change.get('kind', '—')} "
                f"| {change.get('target', '—')} | {change.get('note', '—')} |"
            )
    if duty_proposals:
        lines += ["", "## §3 Duty dispositions (p3a_org_cluster — human may override in "
                  "the verdicts file under `\"duties\"`)", "",
                  "| Duty | Objectives | Disposition | Scale fact |", "|---|---|---|---|"]
        for d in duty_proposals:
            lines.append(
                f"| {d['duty']} | {', '.join(f'`{o}`' for o in d['objectives'])} "
                f"| {d['disposition']} | {d.get('scale_fact', '—')} |"
            )
    section = "§3" if not duty_proposals else "§4"
    lines += [
        "",
        f"## {section} How to close this round",
        "",
        "1. Enter one verdict per item — `Accept`, `Reject` (= explicit risk acceptance,",
        "   recorded, never silent) or `Adjust` — in `steps/phase3/round"
        f"{round_no}_verdicts.json`",
        "   under `\"verdicts\": {\"<verdict-key>\": \"Accept|Reject|Adjust\"}`. The key is the",
        "   objective id, or the principle id for a constraint derived from a principle —",
        "   a principle id is separate because one objective can carry two constraints.",
        "   An `Adjust` verdict MUST carry a note under `\"notes\"` — it is the instruction",
        "   the next round's repropose obeys.",
        "2. Optional: register functional evolution under `\"functional_changes\"` —",
        "   `{\"item\": \"<key>\", \"kind\": \"D1|D2|D3|D4\", \"target\": \"R<n>.<m>\", \"note\": \"…\"}`",
        "   (D1 split, D2 merge, D3 retire, D4 new card). A D3 retires the item.",
        "3. Create `steps/gates/G-P3-A.approved` with the review note (≥200 chars).",
        "4. Re-run `--stage p3a_round`; with `Adjust` items, then run `--stage p3a_repropose`",
        "   for the next round.",
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
