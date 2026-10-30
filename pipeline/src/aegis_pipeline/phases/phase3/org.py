"""Wave 5 — the organizational lane: duties, not verdict rows.

The measured shape (Case 01 audit, 2026-10-10): 32 organizational verdict rows
collapse to 16 duties (17 ORG / 13 SCALE / 2 CARRIED dispositions) because the
taxonomy organises by sub-domain and the duties cut across it. The grouping key
is the audited duty assignment — a routing rule written from the matrix alone
would emit one requirement per row, which is exactly the 1:1 failure the audit
records (32 EARS cards for an 8-person company). The audit file is therefore a
deterministic INPUT here, parsed — never re-derived by a model.
"""

from __future__ import annotations

import re
from pathlib import Path

RE_DUTY_ROW = re.compile(
    r"^\|\s*`(?P<id>(?:PO|SO)-D-\d{2}\.\d-\d{3})`\s*\|(?P<duty>[^|]+)\|"
    r"\s*\*\*(?P<disposition>ORG|SCALE|CARRIED)\*\*\s*\|(?P<warrant>[^|]+)\|"
)

ORG_VERDICT = "No functional carrier (organizational)"
DISPOSITIONS = ("ORG", "SCALE", "CARRIED")


RE_OBJECTIVE_REF = re.compile(r"((?:PO|SO)-D-\d{2}\.\d-\d{3})")


def parse_duty_audit(path: Path) -> dict[str, dict]:
    """Parse the §3 audit table: objective → duty, disposition, warrant.

    The audit merges rows in PROSE ("Merges with `X`", "Third instance … (see
    `X`)"). The canonicalization unions rows connected by an explicit objective
    reference plus rows sharing an identical duty text — the measured result on
    the Case 01 audit is 26 duties, not the §4's 16: the remaining merges are
    prose-relative and stay a human input (recorded deviation, PREREG_P3_01).
    """
    out: dict[str, dict] = {}
    order: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = RE_DUTY_ROW.match(line.strip())
        if not m:
            continue
        if m["id"] in out:
            raise ValueError(f"duty audit: {m['id']} appears twice")
        out[m["id"]] = {
            "duty": m["duty"].strip(),
            "disposition": m["disposition"],
            "warrant": m["warrant"].strip(),
        }
        order.append(m["id"])
    if not out:
        raise ValueError(f"duty audit: no rows parsed from {path}")
    unknown = sorted(d for d in {v["disposition"] for v in out.values()} if d not in DISPOSITIONS)
    if unknown:
        raise ValueError(f"duty audit: dispositions outside {DISPOSITIONS}: {unknown}")

    # union-find: referências explícitas + texto de dever idêntico
    parent = {oid: oid for oid in order}

    def find(x: str) -> str:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: str, b: str) -> None:
        parent[find(a)] = find(b)

    for oid, value in out.items():
        for ref in RE_OBJECTIVE_REF.findall(value["duty"] + " " + value["warrant"]):
            if ref != oid and ref in out:
                union(oid, ref)
    by_text: dict[str, str] = {}
    for oid in order:
        key = out[oid]["duty"].lower()
        if key in by_text:
            union(oid, by_text[key])
        else:
            by_text[key] = oid

    canonical: dict[str, str] = {}
    for oid in order:
        root = find(oid)
        canonical.setdefault(root, out[oid]["duty"])
    for oid in order:
        out[oid]["duty"] = canonical[find(oid)]
    return out


# ---------------------------------------------------------------------------
# Onda B — Etapa 1.5: the model clusters the ROUTE_ORG rows into duties and
# proposes each duty's disposition; the audit file becomes the fallback.
# ---------------------------------------------------------------------------

RE_DUTY_PROPOSAL_ROW = re.compile(
    r"^\|\s*(?P<duty>[^|]+?)\s*\|\s*(?P<objectives>[^|]+)\|"
    r"\s*(?P<disposition>ORG|SCALE|CARRIED)\s*\|\s*(?P<scale_fact>[^|]*)\|"
    r"\s*(?P<warrant>[^|]*)\|"
)


def parse_duty_proposals(answer: str, org_ids: set[str]) -> list[dict]:
    """L0 for the duty-clustering call: one table row per proposed duty.

    The contract is a partition: every organizational objective appears in
    exactly one duty, and no invented id passes. A `SCALE` disposition MUST
    cite the company fact it leans on (`scale_fact`) — a carve-out without a
    fact is a preference, and proportionality is measured against the intake.
    """
    from aegis_pipeline.phases.phase1.common import extract_fenced

    block = extract_fenced(answer, "markdown")
    proposals: list[dict] = []
    seen: set[str] = set()
    for line in block.splitlines():
        line = line.strip()
        if not line.startswith("|") or set(line) <= {"|", "-", " ", ":"}:
            continue
        m = RE_DUTY_PROPOSAL_ROW.match(line)
        if not m:
            continue
        duty = m["duty"].strip().strip("`*")
        if not duty:
            raise ValueError("duty proposals: a row carries an empty duty name")
        objectives = [
            oid.strip().strip("`*") for oid in m["objectives"].split(",") if oid.strip().strip("`*")
        ]
        bad = [o for o in objectives if o not in org_ids]
        if bad:
            raise ValueError(f"duty proposals: objectives not routed organizational: {bad[:6]}")
        dupes = sorted({o for o in objectives if o in seen})
        if dupes:
            raise ValueError(f"duty proposals: objectives assigned to more than one duty: {dupes[:6]}")
        seen.update(objectives)
        disposition = m["disposition"]
        scale_fact = m["scale_fact"].strip()
        if disposition == "SCALE" and len(scale_fact) < 15:
            raise ValueError(
                f"duty proposals [{duty}]: SCALE without a company scale fact "
                "(the carve-out must cite the intake)")
        proposals.append({
            "duty": duty,
            "objectives": objectives,
            "disposition": disposition,
            "scale_fact": scale_fact,
            "warrant": m["warrant"].strip(),
        })
    if not proposals:
        raise ValueError("duty proposals: no rows parsed")
    missing = sorted(org_ids - seen)
    if missing:
        raise ValueError(
            f"duty proposals: {len(missing)} organizational objective(s) not clustered: {missing[:8]}")
    return proposals


def apply_duty_overrides(proposals: list[dict], overrides: dict[str, str]) -> list[dict]:
    """The human's per-duty disposition from the round verdicts (`\"duties\"`).

    The model proposes; the human disposes. An override keyed by duty name
    replaces that duty's disposition — the model's proposal stays in the file
    as the record of what was proposed.
    """
    if not overrides:
        return proposals
    by_name = {p["duty"]: p for p in proposals}
    unknown = sorted(set(overrides) - set(by_name))
    if unknown:
        raise ValueError(f"duty overrides: no proposed duty named {unknown[:6]}")
    out = []
    for p in proposals:
        p = dict(p)
        if p["duty"] in overrides:
            override = overrides[p["duty"]]
            if override not in DISPOSITIONS:
                raise ValueError(
                    f"duty overrides: {p['duty']} -> {override!r} outside {DISPOSITIONS}")
            p["disposition"] = override
            p["overridden_by_human"] = True
        out.append(p)
    return out


def duty_proposal_map(proposals: list[dict]) -> dict[str, dict]:
    """The shape `group_duties` consumes, from the cluster stage's proposals."""
    duty_map: dict[str, dict] = {}
    for p in proposals:
        for oid in p["objectives"]:
            duty_map[oid] = {
                "duty": p["duty"],
                "disposition": p["disposition"],
                "warrant": p.get("warrant") or p.get("scale_fact", ""),
            }
    return duty_map


def render_duty_clustering(proposals: list[dict], org_rows: list[dict]) -> str:
    """The DUTY_CLUSTERING deliverable: proposals side by side with the rows."""
    summary = {r["id"]: (r.get("summary") or "—") for r in org_rows}
    lines = [
        "---",
        "title: 'DUTY_CLUSTERING — organizational duties proposed (Etapa 1.5)'",
        "generated_by: 'p3a_org_cluster (onda B)'",
        "status: PROPOSED — the human round may override dispositions",
        "---",
        "",
        "## §1 Duty proposals",
        "",
        "| Duty | Objectives | Disposition | Scale fact | Warrant |",
        "|---|---|---|---|---|",
    ]
    for p in proposals:
        lines.append(
            f"| {p['duty']} | {', '.join(f'`{o}`' for o in p['objectives'])} "
            f"| {p['disposition']} | {p.get('scale_fact') or '—'} "
            f"| {p.get('warrant') or '—'} |"
        )
    lines += ["", "## §2 The rows each duty carries", ""]
    for p in proposals:
        lines.append(f"### {p['duty']}")
        lines.append("")
        for oid in p["objectives"]:
            lines.append(f"- `{oid}` — {summary.get(oid, '—')}")
        lines.append("")
    return "\n".join(lines) + "\n"


def group_duties(rows: list[dict], duty_map: dict[str, dict]) -> list[dict]:
    """Collapse organizational verdict rows into duties.

    Every organizational row must be covered by the duty map; a row the audit
    does not know about is a finding, not a silent drop. Returns one entry per
    distinct duty with its objectives and the disposition split.
    """
    duties: dict[str, dict] = {}
    uncovered: list[str] = []
    for row in rows:
        if row.get("verdict") != ORG_VERDICT:
            continue
        assignment = duty_map.get(row["id"])
        if assignment is None:
            uncovered.append(row["id"])
            continue
        duty = duties.setdefault(
            assignment["duty"],
            {"duty": assignment["duty"], "objectives": [], "dispositions": {}, "warrants": []},
        )
        duty["objectives"].append(row["id"])
        duty["dispositions"][assignment["disposition"]] = (
            duty["dispositions"].get(assignment["disposition"], 0) + 1
        )
        if assignment["warrant"] and assignment["warrant"] not in duty["warrants"]:
            duty["warrants"].append(assignment["warrant"])
    if uncovered:
        raise ValueError(f"duty grouping: {len(uncovered)} organizational rows not in the duty map: {uncovered[:8]}")
    ordered = sorted(duties.values(), key=lambda d: (min(d["objectives"]), d["duty"]))
    for duty in ordered:
        # `PO-D-01.2-001`.split("-")[1] is "D", not the sub-domain — one duty
        # rendered every card as ORG-D-NNN and the canonical ORG-D-XX.Y-NNN shape
        # was unreachable. Duties cut across sub-domains (one card routed four
        # objectives from D-02 and D-10), so the id names the sub-domain of the
        # FIRST objective, which is the allocation rule the renderer documents.
        duty["subdomain"] = re.match(r"^(?:PO|SO)-(D-\d{2}\.\d)-", duty["objectives"][0]).group(1)
    return ordered


def count_dispositions(duties: list[dict]) -> dict[str, int]:
    totals = {d: 0 for d in DISPOSITIONS}
    for duty in duties:
        for disposition, n in duty["dispositions"].items():
            totals[disposition] += n
    return totals


# ---------------------------------------------------------------------------
# The ORG card call — the model writes the EARS card, the code allocates ids.
# ---------------------------------------------------------------------------

ORG_FIELDS = ("Statement (EARS)", "Requirement Origin", "Fit Criterion", "Verification Method", "Chain", "Control Anchors", "Dependencies", "Priority")
ORG_METHODS = ("TEST", "INSPECT", "DEMONSTRATE", "ANALYZE")
RE_EARS = re.compile(r"\bshall\b", re.IGNORECASE)


def parse_org_card(answer: str, duty: str) -> dict:
    """L0 for one duty's organizational requirement card."""
    from aegis_pipeline.phases.phase1.common import extract_fenced

    block = extract_fenced(answer, "markdown").strip()
    fields: dict[str, str] = {}
    for field in ORG_FIELDS:
        m = re.search(rf"\*\*{re.escape(field)}:?\*\*\s*(.+)", block)
        if not m:
            raise ValueError(f"org card [{duty}]: missing field {field!r}")
        fields[field] = m.group(1).strip()
    statement = fields["Statement (EARS)"]
    if not RE_EARS.search(statement):
        raise ValueError(f"org card [{duty}]: statement is not EARS — no 'shall'")
    if not statement.rstrip(".").endswith(tuple("abcdefghijklmnopqrstuvwxyz)")) and len(statement) < 40:
        raise ValueError(f"org card [{duty}]: statement too short to be a requirement")
    if fields["Verification Method"] not in ORG_METHODS:
        raise ValueError(f"org card [{duty}]: Verification Method {fields['Verification Method']!r} not in {ORG_METHODS}")
    if not fields["Fit Criterion"]:
        raise ValueError(f"org card [{duty}]: empty fit criterion (Volere binary required)")
    anchors = [a.strip().strip("`") for a in fields["Control Anchors"].split(",") if a.strip()]
    if not anchors:
        raise ValueError(f"org card [{duty}]: no control anchors (NIST CSF GOVERN required)")
    if fields["Priority"] not in ("Must", "Should"):
        raise ValueError(f"org card [{duty}]: Priority {fields['Priority']!r} not Must/Should")
    return {"duty": duty, **fields, "_anchor_list": anchors}


def check_org_chain_laws(parsed: dict, regs: set[str]) -> None:
    """Every law the chain names has a driver of its own regulation (T2).

    The chain format is `<law> Art. n -> <objective> -> <anchors>`; the law on
    the left must belong to a regulation that at least one of the duty's merged
    objectives carries. The model proved it will not obey this as prose
    (ficha v1.3.0; job 2168120 re-derived and cited CRA with GDPR-only drivers
    again) — as an L0 refusal it enters the repair cycle with a message that
    teaches the rule. `regs` empty (no context set) checks nothing: the guard
    refuses only when it can name the duty's own regulations.
    """
    if not regs:
        return
    chain = parsed.get("Chain", "")
    laws = set(re.findall(r"\b(GDPR|CRA|NIS2|DORA|AI[\s_-]?Act|AI_Act)\b", chain))
    cited = {"AI_Act" if "Act" in law else law for law in laws}
    stray = sorted(cited - regs)
    if stray:
        raise ValueError(
            f"chain-law rule: {stray} cited but the duty's objectives carry only "
            f"{sorted(regs)} — every law on the left of a chain arrow needs a "
            "driver of its own regulation among the merged objectives; drop the "
            "stray law or the duty needs an objective of that regulation")


def resolve_anchor(controls_root: Path, anchor: str) -> str | None:
    """Resolve one anchor id to a file under `baseline/CONTROLS`, tolerantly.

    The corpus is the authority. NIST CSF 2.0 writes every numeric suffix with a
    leading zero, and the model writes `GV.RR-2` for `GV.RR-02` often enough to
    be a format habit rather than a fabrication — the same habit the
    objective-id spelling normalisation already handles.

    The tolerance is a *lookup*, never a guess: a single-digit suffix is padded
    only when the padded form resolves to a real file. `GV.RR-2` therefore
    resolves and `PR.IP-1` does not — CSF 1.1's `PR.IP` has no CSF 2.0
    counterpart, so padding it would dress a wrong-framework id as a typo and
    let it past R2. Returns the id that resolved, or None.
    """
    if list(controls_root.rglob(f"{anchor}.json")):
        return anchor
    m = re.fullmatch(r"(.*?[0-9A-Za-z])-(\d)", anchor)
    if m and list(controls_root.rglob(f"{m.group(1)}-0{m.group(2)}.json")):
        return f"{m.group(1)}-0{m.group(2)}"
    return None


def check_org_anchor_files(repo: Path, parsed: dict) -> None:
    """Every cited anchor must exist as a JSON under baseline/CONTROLS (R2)."""
    from aegis_pipeline.guards.quality_gates import check_no_technology

    findings = check_no_technology(parsed["Statement (EARS)"], parsed["Fit Criterion"])
    if findings:
        raise ValueError(f"org card [{parsed['duty']}]: technology vocabulary (R5): {findings}")
    controls_root = repo / "baseline" / "CONTROLS"
    resolved = []
    for anchor in parsed["_anchor_list"]:
        hit = resolve_anchor(controls_root, anchor)
        if hit is None:
            raise ValueError(
                f"org card [{parsed['duty']}]: anchor {anchor!r} resolves to no file under baseline/CONTROLS (R2)"
            )
        resolved.append(hit)
    parsed["_anchor_list"] = resolved
    parsed["Control Anchors"] = ", ".join(f"`{a}`" for a in resolved)


def render_doc03(
    duties: list[dict],
    cards: list[dict],
    company: str,
    confirmed_regs: list[str],
) -> str:
    """Compose the organizational deliverable in the hand-written Doc03's structure."""
    lines = [
        "---",
        f"title: 'Doc03 — Organizational Requirements ({company})'",
        "generated_by: 'p3a_org (wave 5)'",
        "status: PROPOSED — routed duties until the acceptance round",
        "---",
        "",
        f"# Doc03 — Organizational Requirements — {company}",
        "",
        "## §1 Derivation contract",
        "",
        "EARS with an organizational subject (`The organization shall …`), one atomic",
        "requirement per duty, binary Volere fit criterion, verification method, and a",
        "chain `regulation article → Phase 2 objective → organizational control anchor`",
        "(NIST CSF 2.0 GOVERN + advisory surfaces, R2b). IDs are allocated by the",
        "pipeline per duty, never per verdict row (ADR-008 D4).",
        "",
        "## §3 Requirements",
        "",
    ]
    # The card's `duty` field holds the call slug (S20): join on it explicitly.
    # A positional zip rendered duty N with card N+1's statement whenever one
    # call failed — a deliverable that asserts the wrong duty is worse than one
    # that names the gap.
    cards_by_duty = {c.get("duty"): c for c in cards if isinstance(c, dict) and c.get("duty")}
    pairs: list[tuple[dict, dict]] = []
    unspec: list[dict] = []
    for d in duties:
        c = cards_by_duty.get(d["slug"])
        if c is None:
            unspec.append(d)
        else:
            pairs.append((d, c))

    for index, (duty, card) in enumerate(pairs, start=1):
        org_id = f"ORG-{duty['subdomain']}-{index:03d}"
        lines += [
            f"### {org_id} — {duty['duty']}",
            "",
            f"**Statement (EARS):** {card['Statement (EARS)']}",
            "",
            f"**Requirement Origin:** {card['Requirement Origin']}",
            "",
            f"**Fit Criterion:** {card['Fit Criterion']}",
            "",
            f"**Verification Method:** {card['Verification Method']}",
            "",
            f"**Chain:** {card['Chain']}",
            "",
            f"**Control Anchors:** {card['Control Anchors']}",
            "",
            f"**Dependencies:** {card['Dependencies']}",
            "",
            f"**Priority:** {card['Priority']}",
            "",
            f"**Objectives routed:** {', '.join(f'`{o}`' for o in duty['objectives'])}",
            "",
        ]
    pending = [d for d in duties if "SCALE" in d["dispositions"]]
    lines += ["## §5 Objectives routed but not yet specified (SCALE)", ""]
    if pending:
        for duty in pending:
            lines.append(f"- {duty['duty']} — objectives: {', '.join(f'`{o}`' for o in duty['objectives'])} — pending the proportionality decision (G-c)")
    else:
        lines.append("None.")
    if unspec:
        lines += ["", "## §6 Duties whose card call failed", ""]
        for duty in unspec:
            lines.append(
                f"- `{duty['slug']}` — {duty['duty']} — objectives: "
                f"{', '.join(f'`{o}`' for o in duty['objectives'])} — no card stored; re-run p3a_org"
            )
    lines.append("")
    lines.append(f"Confirmed regulations: {', '.join(confirmed_regs)}.")
    return "\n".join(lines) + "\n"
