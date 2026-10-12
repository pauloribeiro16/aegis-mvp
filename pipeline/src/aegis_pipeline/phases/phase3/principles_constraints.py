"""principles_constraints.py — the principle-seeded constraint synthesis.

Why this exists. The hand-written Case 01 derives its transversal constraints
from the engineering principles: RN24 (transport protection) is a PRIN-ENG-01
binding, RN18/RN26 are PRIN-ENG-07, RN13/RN17 are PRIN-ENG-02. The pipeline
skipped that step, so PRINCIPLE_MAPPING stayed a skeleton and every objective
that a principle should have carried — transport protection being the measured
example — routed to the organizational lane for having "no functional carrier".

The pass runs between the coverage matrix and the acceptance round: one call
per principle, proposing the constraint(s) that implement it at the company's
scale, keyed to the routed objectives they can discharge. The proposals enter
the SAME human round as the objective-driven ones and are stored in the same
`proposals_*.json` shape the round already collects — no round changes.

After the round, accepted principle constraints re-route their objectives in
the matrix (`organizational` -> `Partially covered` with the derived card as
carrier) and the matrix is re-rendered. That re-routing is what makes the
principles load-bearing rather than decorative.
"""
from __future__ import annotations

import re

def canonical_principles() -> list[dict]:
    """The seven principles with their academic definition — the phase 2 source.

    Reused rather than re-typed: a local tuple of id+name would drift from the
    referential, and the pack is where the definition has to arrive for the
    proposal to implement the principle instead of restating it.
    """
    from aegis_pipeline.phases.phase2.principles import PRINCIPLES
    return PRINCIPLES

FIELDS = ("Constraint (EARS)", "Fit criterion", "Risk addressed",
          "Chain anchors", "Proposed carrier", "Also carries")

RE_OBJECTIVE = re.compile(r"^(PO|SO)-D-\d{2}\.\d-\d{3}$")


def parse_principle_proposals(answer: str, principle: str,
                              routed: list[dict]) -> list[dict]:
    """L0 for the principle call: blocks keyed by a routed objective id.

    Structural only, same split as the objective-driven parser: the block ids
    must be objectives the matrix routed organizational, and the carrier must
    be `new` — a principle constraint has no existing card by construction.
    """
    from aegis_pipeline.phases.phase1.common import extract_fenced

    block = extract_fenced(answer, "markdown").strip()
    sections: dict[str, str] = {}
    current: str | None = None
    for line in block.splitlines():
        if line.startswith("###"):
            current = line.lstrip("#").strip().strip("`")
            if current in sections:
                raise ValueError(f"principles: objective {current} appears twice")
            sections[current] = ""
        elif current is not None:
            sections[current] += line + "\n"

    routed_ids = {r["id"] for r in routed}
    invented = [oid for oid in sections if oid not in routed_ids]
    if invented:
        raise ValueError(
            f"principals [{principle}]: block id(s) {invented[:4]} are not objectives "
            f"the matrix routed organizational — a principle constraint may only "
            f"discharge routed objectives")

    out: list[dict] = []
    for oid, body in sections.items():
        fields: dict[str, str] = {}
        current: str | None = None
        for line in body.splitlines():
            m = re.match(r"^\*\*(.+?):\*\*\s*(.*)$", line.strip())
            if m and m.group(1) in FIELDS:
                current = m.group(1)
                fields[current] = m.group(2).strip()
            elif current is not None and line.strip():
                # a wrapped field continues until the next bold label; without
                # this the constraint loses its second half and then has no SHALL
                fields[current] = (fields[current] + " " + line.strip()).strip()
        missing = [f for f in FIELDS[:5] if not fields.get(f)]
        if missing:
            raise ValueError(f"principles [{principle}] {oid}: missing field(s) {missing}")
        if not re.search(r"\bshall\b", fields["Constraint (EARS)"], re.IGNORECASE):
            raise ValueError(f"principles [{principle}] {oid}: constraint has no SHALL")
        carrier = fields["Proposed carrier"].strip().strip("`")
        if carrier != "new":
            raise ValueError(
                f"principles [{principle}] {oid}: carrier must be `new` — a principle "
                f"constraint creates its card, it does not borrow one")
        anchors = [a.strip().strip("`") for a in fields["Chain anchors"].split(",") if a.strip()]
        if not anchors:
            raise ValueError(f"principles [{principle}] {oid}: no chain anchors")
        also = [a.strip().strip("`") for a in fields.get("Also carries", "").split(",")
                if a.strip().strip("`")]
        stray = [a for a in also if not RE_OBJECTIVE.match(a)]
        if stray:
            raise ValueError(f"principles [{principle}] {oid}: also-carries {stray} not objective ids")
        m = re.match(r"^(?:PO|SO)-(D-\d{2}\.\d)-", oid)
        out.append({
            "objective": oid,
            "subdomain": m.group(1),
            "constraint": fields["Constraint (EARS)"],
            "fit_criterion": fields["Fit criterion"],
            "risk": fields["Risk addressed"],
            "anchors": anchors,
            "carrier": "new",
            "principle": principle,
            "also_carries": also,
        })
    return out


def check_principle_proposals(proposals: list[dict], routed: list[dict]) -> list[str]:
    """Post-parse gates. Empty = pass.

    Two anchors disciplines at once: every anchor must belong to the published
    set of SOME routed objective (R2 — the principle itself publishes nothing),
    and every also-carries objective must be one the matrix routed
    organizational, because re-routing anything else would silently upgrade a
    verdict the round never saw.
    """
    findings: list[str] = []
    published: dict[str, set] = {}
    for r in routed:
        published[r["id"]] = set(r.get("anchors") or [])
    union = set().union(*published.values()) if published else set()
    routed_ids = {r["id"] for r in routed}
    for p in proposals:
        stray = {a for a in p["anchors"] if a not in union}
        if stray:
            findings.append(f"{p['principle']} {p['objective']}: anchor(s) {sorted(stray)} "
                            f"belong to no routed objective's published set (R2)")
        for oid in p.get("also_carries", []):
            if oid not in routed_ids:
                findings.append(f"{p['principle']} {p['objective']}: also-carries {oid} "
                                f"was not routed organizational — re-routing it would "
                                f"upgrade a verdict the round never saw")
    return findings


def build_principle_pack(principle: dict, routed: list[dict],
                         cards: list[dict], fact_sheet: str) -> str:
    """The pack one principle call carries.

    The routed objectives arrive WITH their published anchors — the same R2
    discipline as every other pack: every anchor the model could name is on the
    page, so it has nothing to invent. The V0 card names are there so the
    constraint can name what it constrains without re-describing the product.
    """
    pid = principle["id"]
    out = [f"# Principle to implement: `{pid}` — {principle['name']}", "",
           f"**Definition:** {principle['definition']}", "",
           f"**Academic source:** {principle['source']}", "",
           f"**Skill:** `{principle['skill']}`", "",
           "The coverage matrix routed these objectives to the organizational "
           "lane for want of a functional carrier. If THIS principle demands a "
           "product-side control the company must build — at the company's own "
           "scale — propose the constraint that implements it. If the principle "
           "genuinely adds nothing for these objectives, return an empty fenced "
           "block; silence is a valid answer and the round will never see it.",
           ""]
    for r in routed:
        out += [f"## `{r['id']}`",
                f"- **Objective:** {r.get('summary', '')}",
                f"- **Published control anchors:** "
                + (", ".join(f"`{a}`" for a in (r.get("anchors") or []))
                   or "_none_"),
                ""]
    out += ["---", "", "# The functional cards that exist (do NOT re-describe them)",
            ""]
    for c in cards:
        # cards on disk come in two shapes: the generated card (`name`) and the
        # legacy proposal record that `allocate_new_cards` replaced but which
        # survived in older runs. Fall back rather than KeyError on the whole
        # stage — one stale card must not kill seven calls.
        label = c.get("name") or c.get("constraint") or c.get("description", "")
        out.append(f"- `{c.get('id', '?')}` **{label[:160]}**")
    out += ["", "---", "", "# Company fact sheet", "", fact_sheet, "",
            "One block per constraint, keyed by the routed objective it "
            "PRIMARILY discharges; objectives it also carries go in `Also "
            "carries`. Anchors come only from the published sets above.",
            ""]
    return "\n".join(out)


def reroute_objectives(rows: list[dict], accepted: list[dict]) -> tuple[list[dict], int]:
    """Flip routed objectives to Partially covered under an accepted constraint.

    Runs after the round. A principle proposal's primary objective and its
    `also_carries` both move from `No functional carrier (organizational)` to
    `Partially covered (functional leg + explicit carve-out)`, the carrier
    naming the derived card and the discharge recording the principle binding —
    the same row shape the hand-written matrix gives its RN24 chains.
    """
    by_objective = {}
    for p in accepted:
        by_objective[p["objective"]] = p
        for oid in p.get("also_carries", []):
            by_objective.setdefault(oid, p)
    moved = 0
    for row in rows:
        p = by_objective.get(row["id"])
        if p is None or row["verdict"] != "No functional carrier (organizational)":
            continue
        row["verdict"] = "Partially covered (functional leg + explicit carve-out)"
        row["carrier"] = f"`{p.get('allocated_card', 'new')}`"
        row["discharge"] = (f"{p['principle']} binding — constraint accepted in "
                            f"Round 1; see STEP4_CONSTRAINT_ABSORPTION")
        moved += 1
    return rows, moved


def render_principle_mapping(rows: list[dict], accepted: list[dict]) -> str:
    """PRINCIPLE_MAPPING filled from the accepted bindings, not a skeleton.

    The previous renderer emitted "Bound 0 / Pending 7" unconditionally. This
    one reports what the round actually accepted, and names the principles that
    contributed nothing — a principle that adds nothing is a finding, not a
    blank to hide.
    """
    from aegis_pipeline.phases.phase3.skeleton import render_principles

    bindings: dict[str, list[dict]] = {}
    for p in accepted:
        if p.get("principle"):
            bindings.setdefault(p["principle"], []).append(p)
    # Replace the skeleton rather than append to it: the skeleton carries its own
    # "Bound 0 / Pending 7" footer, and two contradicting footers in one document
    # is worse than none.
    lines = [render_principles().split("## Coverage Totals")[0].rstrip(),
             "", "## Coverage totals (filled by `p3a_weave`)", ""]
    lines += ["| Principle | Objectives discharged | Constraint count | State |",
              "|---|---|---|---|"]
    for p in canonical_principles():
        got = bindings.get(p["id"], [])
        objs = sorted({o for g in got for o in [g["objective"], *g.get("also_carries", [])]})
        lines.append(
            f"| `{p['id']}` {p['name']} | "
            + (", ".join(f"`{o}`" for o in objs) if objs else "—")
            + f" | {len(got)} | "
            + ("Bound" if got else "Pending — no constraint proposed"))
    bound = sum(1 for p in canonical_principles() if bindings.get(p["id"]))
    lines += ["", f"**Principles bound: {bound}/{len(canonical_principles())}**"]
    return "\n".join(lines) + "\n"
