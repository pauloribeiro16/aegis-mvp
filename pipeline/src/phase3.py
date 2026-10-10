"""phase3.py — Phase 3 Part 1: the coverage skeleton.

Builds `OBJECTIVE_MAPPING.md` and `PRINCIPLE_MAPPING.md` from the Phase 2
deliverable, with every row present and every content column empty. No model
call happens here and none can: this module reads a file and writes two.

Why a skeleton is worth building first, rather than starting with the model:

  * **G1 stops being a judgement.** The gate asks for exhaustive mapping with
    zero silent objectives. When the rows are generated, a silent objective is
    not a decision someone forgot to make — it is a row the generator would have
    had to skip, and the check becomes a set comparison.
  * **The output schema is fixed before any prose exists**, which is what makes
    the later model stages parseable and the later gates meaningful.

What is deliberately absent. The ADR-007 D2 reconstruction test is not
implemented: all 62 Phase 2 Verification Criteria are one of two template
sentences with the objective's own name substituted (ADR-013 §3, measured), so
there is nothing object-specific to reconstruct against. The matrix says
`anchored` and does not claim a discharge it cannot perform.

    python3 pipeline/src/phase3.py --source <phase2 Doc01> --out <dir>
    python3 pipeline/src/phase3.py --case Case_01_TinyTask_SaaS --out <dir>

Reads either a Phase 2 deliverable produced by a run, or the hand-authored one
under `cases/<case>/02_PHASE2_RULES/` — the latter is how the golden comparison
runs.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import phase3_schemas as _s
from phase3_schemas import (MATRIX_COLUMNS, ORGANIZATIONAL as _ORG, UNSET,
                            VERDICTS, anchor_set, domain_of,
                            is_template_criterion, subdomain_of)

REPO = Path(__file__).resolve().parent.parent.parent

#: The seven engineering principles, in canonical order. Ids and names come from
#: the Phase 2 `Doc02_Secure_Design_Principles.md`; the pipeline states them
#: here so the skeleton does not need a second file to exist.
PRINCIPLES = (
    ("PRIN-ENG-01", "Explicit Trust Boundaries & Complete Mediation"),
    ("PRIN-ENG-02", "Attack Surface Minimization & Peripheral Resilience"),
    ("PRIN-ENG-03", "Least Privilege & Mechanism Isolation"),
    ("PRIN-ENG-04", "Fail-Safe Defaults & Closed Failure States"),
    ("PRIN-ENG-05", "Requirement Verifiability & Atomicity"),
    ("PRIN-ENG-06", "Proactive Data Minimization & Scoped Projection"),
    ("PRIN-ENG-07", "End-to-End Lifecycle Security & Irreversible Erasure"),
)

#: Phase 2 `Doc01_Operational_Objectives.md` column order. Index 8 is the
#: published anchor set, the same column `check_traceability.py` T6 reads —
#: reading the same surface is what keeps the two from drifting.
COL_ID, COL_STATEMENT, COL_PARENT, COL_REG, COL_SCOPE, COL_CRITERIA, COL_METHOD, COL_OWNER, COL_ANCHORS = range(9)


def load_objectives(path: Path) -> list[dict]:
    """Every objective row of a Phase 2 deliverable, in file order."""
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) < 9 or not re.match(r"`?(PO|SO)-D-\d{2}\.\d-\d{3}", cells[0]):
            continue
        oid = cells[0].strip("` ")
        rows.append({
            "id": oid,
            "statement": cells[COL_STATEMENT].strip("` "),
            "parent_goal": cells[COL_PARENT].strip("` "),
            "regulation": cells[COL_REG].strip("` "),
            "scope": cells[COL_SCOPE],
            "criterion": cells[COL_CRITERIA],
            "method": cells[COL_METHOD],
            "owner": cells[COL_OWNER],
            "anchors": anchor_set(cells[COL_ANCHORS]),
            "subdomain": subdomain_of(oid),
            "domain": domain_of(subdomain_of(oid)),
        })
    return rows


def build(rows: list[dict]) -> list[dict]:
    """The matrix skeleton: one row per objective, content columns empty.

    The Summary column carries the Phase 2 operational statement so a reader can
    tell the rows apart; every column that requires a judgement — carrier, skill,
    verdict, discharge, action — is `UNSET`.
    """
    return [{
        "id": r["id"],
        "summary": r["statement"],
        "carrier": UNSET,
        "skill": UNSET,
        "verdict": UNSET,
        "discharge": UNSET,
        "action": UNSET,
        "subdomain": r["subdomain"],
        "domain": r["domain"],
        "regulation": r["regulation"],
        "scope": r["scope"],
        "method": r["method"],
        "owner": r["owner"],
        "criterion": r["criterion"],
        "anchors": r["anchors"],
        "criterion_is_template": is_template_criterion(r["criterion"]),
    } for r in rows]


def check(rows: list[dict], objectives: list[dict]) -> list[str]:
    """The gates this stage can decide on its own. Empty list = pass.

    Anchor presence is deliberately **not** gated here. A contractual obligation
    carries no product control anchor by construction — measured: every
    unanchored objective across the three cases is a PROCESS-lane contract or
    procurement duty verified by `INSPECT`, and its anchor belongs in the
    organizational document. The skeleton does not yet know which rows those
    are, because the verdict is the next stage's job. `check_anchors` is the
    gate, and it runs after the verdicts land.
    """
    findings = []
    ids = [r["id"] for r in rows]
    expected = [o["id"] for o in objectives]

    missing = set(expected) - set(ids)
    if missing:
        findings.append(f"matrix drops {len(missing)} objective(s): {sorted(missing)[:5]}")
    extra = set(ids) - set(expected)
    if extra:
        findings.append(f"matrix invents {len(extra)} objective(s): {sorted(extra)[:5]}")
    if len(ids) != len(set(ids)):
        dupes = sorted({i for i in ids if ids.count(i) > 1})
        findings.append(f"matrix repeats {len(dupes)} objective id(s): {dupes[:5]}")

    return findings


def check_anchors(rows: list[dict]) -> list[str]:
    """Post-verdict gate: a row claiming a product carrier must carry anchors.

    An objective verdicted `No functional carrier (organizational)` is exempt —
    a process obligation has no product control anchor, and that is the correct
    state rather than a gap. Run this after the verdicts land, never before.
    """
    findings = []
    for r in rows:
        claiming = r["verdict"] not in (S_UNSET, ORGANIZATIONAL)
        if claiming and not r["anchors"]:
            findings.append(f"{r['id']} claims a functional carrier but carries no "
                            f"published anchor set")
        if not claiming and r["verdict"] == ORGANIZATIONAL and r["anchors"]:
            continue  # anchors on an organizational row are not an error
    return findings


#: Re-exported for `check_anchors` without importing the schemas module twice.
S_UNSET = UNSET
ORGANIZATIONAL = _ORG


def render_matrix(rows: list[dict], by_domain: dict[str, list[dict]],
                  domain_names: dict[str, str]) -> str:
    out = [
        "# Phase 2 Objective Mapping — Exhaustive Coverage Matrix",
        "",
        "> **SKELETON.** Every Phase 2 objective has a row; every column that "
        "requires a judgement is unset. The `Fully covered` verdict is "
        "*anchored*, not *discharge-verified*: the ADR-007 D2 reconstruction test "
        "is not executable on the current Phase 2 data, because all Verification "
        "Criteria are one of two template sentences with the objective's own name "
        "substituted (ADR-013 §3). The `VC discharge` column records which legs a "
        "carrier carries and which are carved out; it does not claim a "
        "reconstruction.",
        "",
        "## Verdict vocabulary (ADR-007 D4)",
        "",
    ]
    out += [f"- `{v}`" for v in VERDICTS]
    out += ["", "---", ""]

    for domain in sorted(by_domain):
        out += [f"## {domain} — {domain_names.get(domain, '')}".rstrip(" —"), ""]
        out += ["| " + " | ".join(MATRIX_COLUMNS) + " |",
                "|" + "|".join(["---"] * len(MATRIX_COLUMNS)) + "|"]
        for r in by_domain[domain]:
            out.append("| `" + r["id"] + "` | " + " | ".join(
                [r["summary"], r["carrier"], r["skill"], r["verdict"],
                 r["discharge"], r["action"]]) + " |")
        out += ["", "---", ""]

    out += ["## Coverage totals", "", "| Verdict | Count |", "|---|---|"]
    for v in VERDICTS:
        n = sum(1 for r in rows if r["verdict"] == v)
        out.append(f"| {v} | {n} |")
    out.append(f"| **Unset** | **{sum(1 for r in rows if r['verdict'] == UNSET)}** |")
    out.append(f"| **Total objectives** | **{len(rows)}** |")
    return "\n".join(out) + "\n"


def render_principles() -> str:
    out = ["# Engineering Principles — Mapping (skeleton)", "",
           "| Principle | Name | Where | Realization | RN | State |", "|---|---|---|---|---|---|"]
    for pid, name in PRINCIPLES:
        out.append(f"| `{pid}` | {name} | {UNSET} | {UNSET} | {UNSET} | {UNSET} |")
    out += ["", "---", "",
            "| Surface | Count |", "|---|---|",
            f"| Principles present | {len(PRINCIPLES)}/{len(PRINCIPLES)} |",
            f"| Bound | 0 |",
            f"| Pending | {len(PRINCIPLES)} |"]
    return "\n".join(out) + "\n"


def domain_names_from(index: Path) -> dict[str, str]:
    """Domain titles from `baseline/domains/index.md`, when the file is present.

    The index links each domain as `D-03_Access-Control`; the title is the part
    after the first underscore, with dashes turned back into spaces.
    """
    names = {}
    if not index.is_file():
        return names
    for line in index.read_text(encoding="utf-8").splitlines():
        m = re.search(r"\[(D-\d{2})_([^\]]+)\]\(", line)
        if m:
            names[m.group(1)] = m.group(2).replace("-", " ")
    return names


def resolve_source(args) -> Path:
    if args.source:
        return Path(args.source)
    if args.case:
        return (REPO / "cases" / args.case / "02_PHASE2_RULES"
                / "Doc01_Operational_Objectives.md")
    raise SystemExit("one of --source or --case is required")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--source", help="a Phase 2 Doc01_Operational_Objectives.md")
    ap.add_argument("--case", help="read the hand-authored deliverable of this case")
    ap.add_argument("--out", required=True, help="directory to write the skeleton into")
    args = ap.parse_args()

    source = resolve_source(args)
    if not source.is_file():
        print(f"no Phase 2 deliverable at {source}", file=sys.stderr)
        return 2

    objectives = load_objectives(source)
    if not objectives:
        print(f"no objective rows parsed from {source}", file=sys.stderr)
        return 2

    rows = build(objectives)
    findings = check(rows, objectives)
    if findings:
        for f in findings:
            print(f"  [FAIL] {f}", file=sys.stderr)
        print(f"{len(findings)} finding(s) — skeleton not written", file=sys.stderr)
        return 1

    by_domain: dict[str, list[dict]] = {}
    for r in rows:
        by_domain.setdefault(r["domain"], []).append(r)

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "OBJECTIVE_MAPPING.md").write_text(
        render_matrix(rows, by_domain, domain_names_from(REPO / "baseline/domains/index.md")),
        encoding="utf-8")
    (out / "PRINCIPLE_MAPPING.md").write_text(render_principles(), encoding="utf-8")

    sds = sorted({r["subdomain"] for r in rows})
    templated = sum(1 for r in rows if r["criterion_is_template"])
    anchored = sum(1 for r in rows if r["anchors"])
    unanchored = [r["id"] for r in rows if not r["anchors"]]
    print(f"skeleton: {len(rows)} objectives across {len(by_domain)} domains / {len(sds)} sub-domains")
    print(f"  published anchor set: {anchored}/{len(rows)}"
          + (f" — unanchored (process obligations): {', '.join(unanchored)}" if unanchored else ""))
    print(f"  Phase 2 criteria that are the generic template: {templated}/{len(rows)}")
    print(f"  wrote {out/'OBJECTIVE_MAPPING.md'}")
    print(f"  wrote {out/'PRINCIPLE_MAPPING.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# ---------------------------------------------------------------- verdicts

#: Marker for a judgement cell the model did not fill.
UNFILLED = UNSET

RE_TABLE_ROW = re.compile(r"^\|(?P<cells>.+)\|\s*$")


def parse_verdicts(answer: str) -> list[dict]:
    """Parse one sub-domain's verdict table. Raises on any structural defect.

    Structure only: seven columns, a well-formed objective id, and a verdict
    inside the ADR-007 D4 vocabulary. What it cannot decide — whether the
    carriers are real, whether the discharge says anything, whether the anchors
    belong to the objective — is `check_verdicts`'s, and that runs with the
    sub-domain's objectives in hand.
    """
    rows = {}
    for line in answer.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) < len(MATRIX_COLUMNS):
            continue
        oid = cells[0].strip("` ").split(" ")[0]
        if not re.match(r"^(PO|SO)-D-\d{2}\.\d-\d{3}$", oid):
            continue
        if oid in rows:
            raise ValueError(f"verdict table repeats {oid}")
        # The model wraps the verdict in backticks as often as in bold, and both
#        # were seen in one batch — strip the marks, not the wording.
        verdict = cells[4].replace("**", "").replace("`", "").strip()
        if verdict not in VERDICTS:
            raise ValueError(f"{oid}: verdict {verdict!r} is outside the ADR-007 D4 vocabulary")
        rows[oid] = {
            "id": oid,
            "summary": cells[1],
            "carrier": cells[2],
            "skill": cells[3],
            "verdict": verdict,
            "discharge": cells[5],
            "action": cells[6],
            "carriers_cited": sorted(set(re.findall(r"R\d+\.\d+", cells[2]))),
        }
    if not rows:
        raise ValueError("verdict table parsed to zero rows")
    return list(rows.values())


def check_verdicts(rows: list[dict], objectives: list[dict], pool: list[str]) -> list[str]:
    """Post-verdict gates. Empty list = pass.

    Two of these exist because the absence is silent in a way the eye skips: a
    `Fully covered` row with nothing in the discharge column reads as coverage
    and is not, and a `No functional carrier` row with nothing in it routes the
    objective without naming what it routed.
    """
    findings = []
    pub = {o["id"]: set(o["anchors"]) for o in objectives}
    known = set(pool)
    wanted = {o["id"] for o in objectives}
    seen = {x["id"] for x in rows}
    for oid in sorted(wanted - seen):
        findings.append(f"{oid}: no verdict row was parsed for this objective")
    for r in rows:
        if r["id"] not in wanted:
            findings.append(f"{r['id']}: row is not an objective of this sub-domain")
        stray_cards = set(r.get("carriers_cited", [])) - known
        if stray_cards:
            findings.append(f"{r['id']}: carrier {sorted(stray_cards)} is not in the candidate pool")
        oid, v, d = r["id"], r["verdict"], r["discharge"].strip()
        empty = (not d) or d in (UNSET, "-", "—", "n/a", "N/A")
        if v == VERDICTS[0] and empty:
            findings.append(f"{oid}: Fully covered with no discharge record")
        if v == ORGANIZATIONAL and empty:
            findings.append(f"{oid}: routed to the organizational lane without naming the obligation")
        if v == "N/A" and empty:
            findings.append(f"{oid}: N/A without a reason")
        if v in (UNSET, UNFILLED):
            findings.append(f"{oid}: no verdict recorded")
        if v not in VERDICTS and v != UNSET:
            findings.append(f"{oid}: verdict {v!r} is outside the vocabulary")
    findings.extend(anchor_findings(rows, pub))
    return findings


def anchor_findings(rows: list[dict], published: dict[str, set]) -> list[str]:
    """T6: a chain may only select anchors its objective publishes.

    The anchor ids themselves are Phase 2's, carried on the skeleton row, so the
    check is that the verdicted row kept them rather than replaced them.
    """
    findings = []
    for r in rows:
        allowed = published.get(r["id"], set())
        used = set(r.get("anchors_used", []))
        stray = used - allowed
        if stray:
            findings.append(f"{r['id']}: chain selects anchor(s) outside the published set: {sorted(stray)}")
    return findings


def apply_verdicts(skeleton: list[dict], verdicts: list[dict]) -> list[dict]:
    """Merge parsed verdicts onto the skeleton rows, preserving order."""
    by_id = {v["id"]: v for v in verdicts}
    merged = []
    for s in skeleton:
        v = by_id.get(s["id"])
        if v is None:
            merged.append(s)
            continue
        row = dict(s)
        for col in ("carrier", "skill", "verdict", "discharge", "action"):
            row[col] = v[col] if v[col] else s[col]
        row["carriers_cited"] = v.get("carriers_cited", [])
        row["anchors_used"] = s["anchors"]
        merged.append(row)
    return merged


def load_v0_cards(doc01: Path) -> list[dict]:
    """The candidate carrier pool, read from the frozen V0 deliverable.

    V0 is a human input and this module never writes it. Only the id, name and
    description are read, because that is all a verdict needs: whether a card can
    carry an objective. Constraints live in V1/V2 and are deliberately not shown —
    a verdict that can see the security constraints it is judging has already
    been anchored, and the question being asked is whether the functional card
    covers the obligation at all.
    """
    cards, current = [], None
    for line in doc01.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\|\s*\*\*ID:\*\*\s*(R\d+\.\d+)\s*\*\*Name:\*\*\s*(.+?)\s*\|", line)
        if m:
            current = {"id": m.group(1), "name": m.group(2), "description": ""}
            cards.append(current)
            continue
        if current is not None:
            d = re.match(r"^\|\s*\*\*Description:\*\*\s*(.+?)\s*\|", line)
            if d:
                current["description"] = d.group(1)
    return cards


def build_verdict_pack(rows: list[dict], cards: list[dict]) -> str:
    """The context one sub-domain's verdict call carries.

    Small by design. The objectives arrive with their published anchors already
    attached, the carrier pool is the frozen V0 card list, and the vocabulary
    states what each verdict means. Nothing here invites the model to invent a
    control, because every anchor it could name is already on the page.
    """
    out = ["# Coverage rows to verdict", ""]
    for r in rows:
        out += [f"## `{r['id']}`", "",
                f"- **Regulation:** {r['regulation']}",
                f"- **Objective:** {r['summary']}",
                f"- **Published control anchors:** "
                + (", ".join(f"`{a}`" for a in r["anchors"]) if r["anchors"]
                   else "_none — this obligation has no product control anchor; if it is "
                        "discharged by a card, say so explicitly_"),
                ""]

    out += ["---", "", "# Candidate functional cards (V0 — the whole carrier pool)", ""]
    for c in cards:
        out.append(f"- `{c['id']}` **{c['name']}** — {c['description']}")

    out += ["", "---", "", "# Verdicts", "",
            "One per objective, exactly one of:"]
    out += [f"- `{v}`" for v in VERDICTS]
    out += ["",
            "Emit a markdown table with exactly these columns:",
            "`Objective | Summary | Functional carrier | Skill | State | VC discharge | Action / Round`",
            ""]
    return "\n".join(out)
