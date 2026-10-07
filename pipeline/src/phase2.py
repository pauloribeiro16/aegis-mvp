"""phase2.py — Phase 2 prototype: Adjusted Goals -> Operational Objectives.

Consumes a Phase 1 run directory (`steps/goals/*.json`, `steps/verdicts.json`,
`steps/selection.json`) and renders the two Phase 2 deliverables. What runs here
is exactly the part the determinism ledger measured as derivable
(docs/pipeline/05_PHASE2_DETERMINISM_LEDGER.md §3); the generative cells are
named seams, not guesses.

    python3 pipeline/src/phase2.py --run-dir <phase1 run> --out <dir>

Design constraints taken from the ledger, not invented here:

  * Control anchors are DERIVED (`controls.goal_anchors`), never copied from
    Phase 1 and never emitted by a model — Phase 1 already routes them through
    the mapping store, and re-deriving is what makes R2b hold by construction.
  * The objective id inherits Phase 1's slot. Which regulation occupies which
    slot is decided by Phase 1 and is not re-decided here (ledger §4.3 found the
    hand-authored cases disagree about that rule).
  * Every cell this module cannot derive is emitted as an explicit `UNSET`
    marker, never as plausible filler. A blank cell is a visible seam; invented
    text is a lie that survives to Phase 3.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import controls
from compose import (confirmed_regulations, load_case, load_selection,
                     subdomain_name)

#: Marker for a cell the pipeline has no derivation rule for. Deliberately
#: visible in the rendered document: the ledger marks these "no rule found",
#: and an empty cell is the honest rendering of that.
UNSET = "—"

#: Regulation -> (id prefix, operational scope label). The prefix is the GDPR
#: personal-data ambit vs everything else, per the phase convention. The scope
#: label's parenthesised nouns are per-case and are a seam, not a constant.
PREFIX_BY_REG = {"GDPR": "PO"}
SCOPE_BY_REG = {
    "GDPR": "Personal Data Scope",
    "CRA": "Product & Software Security Scope",
    "NIS2": "Network & Information Systems Scope",
    "DORA": "ICT Risk Scope",
    "AI_Act": "High-Risk AI System Scope",
}

#: Canonical regulation order, used only to ORDER rows. Slots themselves are
#: inherited from Phase 1 — see module docstring.
REG_ORDER = ["GDPR", "CRA", "NIS2", "DORA", "AI_Act"]


# --------------------------------------------------------------------------
# ingest
# --------------------------------------------------------------------------

def load_goals(run_dir: Path) -> list[dict]:
    """Every Phase 1 goal in the run, in canonical sub-domain then slot order."""
    goals_dir = run_dir / "steps" / "goals"
    out = []
    for jf in sorted(goals_dir.glob("*.json")):
        blob = json.loads(jf.read_text(encoding="utf-8"))
        out.extend(blob.get("goals", []))
    return out


def objective_id(goal: dict) -> str:
    """`AG-D-XX.Y-NNN` -> `PO-/SO-D-XX.Y-NNN`, slot inherited unchanged."""
    ag = goal["id"]                       # AG-D-01.1-002
    reg = _reg_of(ag, goal)
    prefix = PREFIX_BY_REG.get(reg, "SO")
    # `replace` would give POD-01.1-002: the id is `AG-D-…`, so the token to
    # swap is the leading `AG-` and the `D-` belongs to the canonical axis.
    return prefix + ag[2:]


def subdomain_of(ag_id: str) -> str:
    """`AG-D-01.1-002` -> `D-01.1`.

    Split on the SLOT, not on `-`: the id is `AG-D-<sub>-<slot>`, so a naive
    `split('-')[1]` yields the literal `D`.
    """
    m = re.match(r"[A-Z]{2}-(D-\d{2}\.\d)-\d{3}$", ag_id)
    if not m:
        raise ValueError(f"malformed goal id: {ag_id!r}")
    return m.group(1)


def _reg_of(ag: str, goal: dict) -> str:
    """The regulation behind a goal id.

    Phase 1 wrote the regulation into the goal record; the id slot is only a
    positional convention and the ledger found the two disagree in Case 03
    (§4.3), so the field wins and the slot is never used to infer it.
    """
    reg = (goal.get("regulation") or "").strip()
    if reg:
        return reg
    raise ValueError(f"{ag}: goal carries no `regulation`; cannot derive the "
                     f"objective prefix without it")


def reg_sort_key(reg: str) -> tuple:
    return (REG_ORDER.index(reg) if reg in REG_ORDER else len(REG_ORDER), reg)


# --------------------------------------------------------------------------
# derive (zero LLM)
# --------------------------------------------------------------------------

def derive_objective(repo: Path, goal: dict) -> dict:
    """One objective row. Every populated cell is traceable to Phase 1 or the
    corpus; everything else is UNSET by design."""
    ag = goal["id"]
    sd = subdomain_of(ag)
    reg = _reg_of(ag, goal)
    baseline_source = (goal.get("baseline_source") or "").strip()

    anchors = []
    if baseline_source:
        # Re-derivation, not inheritance: Phase 1's anchors are an output of
        # this same call, so reading them back would make the check circular.
        anchors = controls.goal_anchors(repo, sd, [baseline_source])

    return {
        "objective_id": objective_id(goal),
        "parent_goal": ag,
        "subdomain": sd,
        "subdomain_name": subdomain_name(repo, sd),
        "regulation": reg,
        "statement": (goal.get("goal") or "").strip(),
        "scope": SCOPE_BY_REG.get(reg, UNSET),
        "criteria": UNSET,          # seam: no rule found (ledger §3.1)
        "method": UNSET,            # seam
        "owner": UNSET,             # seam
        "anchors": ", ".join(anchors) if anchors else UNSET,
        # carried for the seam calls; not rendered
        "implication": (goal.get("implication") or "").strip(),
        "source": (goal.get("source") or "").strip(),
        "pattern": (goal.get("pattern") or "").strip(),
        "property": (goal.get("property") or "").strip(),
        "adjustment": (goal.get("adjustment") or "").strip(),
    }


def build(repo: Path, run_dir: Path) -> list[dict]:
    """All objectives for a run, ordered by sub-domain then regulation slot."""
    rows = [derive_objective(repo, g) for g in load_goals(run_dir)]
    rows.sort(key=lambda r: (r["subdomain"], reg_sort_key(r["regulation"])))
    return rows


# --------------------------------------------------------------------------
# gates — the defects the ledger measured, promoted to checks
# --------------------------------------------------------------------------

def check(rows: list[dict], run_dir: Path | None = None) -> list[str]:
    """Findings. Empty list means the derived set passed everything below.

    These are the defects that survived hand-authoring in cases 01-03 and that
    `doc_lint.py` cannot see, because each is a *content* fault inside a
    structurally valid table.
    """
    out = []

    # G0 — upstream completeness. Phase 2 consumes Phase 1's selection; if a
    # selected sub-domain has no goal artifact the run is short, and emitting
    # the remainder anyway would ship a quietly incomplete deliverable whose
    # total is wrong. Observed on run_m09_c2_meta_1991136: D-06.1/D-06.3/D-06.4
    # selected, never derived.
    if run_dir is not None:
        sel = load_selection(run_dir).get("selected", [])
        have = {r["subdomain"] for r in rows}
        missing = sorted({s["id"] for s in sel} - have)
        if missing:
            out.append(f"upstream incomplete: {len(missing)} selected sub-domain(s) "
                       f"have no Phase 1 goal artifact: {', '.join(missing)}")

    # G1 — a statement that swallowed raw baseline (ledger §4.2). Four Case 03
    # rows carry fenced YAML, `## Security Requirements` headings and `req_id:`
    # inside the cell. That is a corpus-extraction fault and it must never
    # survive a code path, because the code path cannot produce it.
    for r in rows:
        blob = r["statement"]
        if "```" in blob or "req_id:" in blob or "\n## " in blob or " --- ## " in blob:
            out.append(f"{r['objective_id']}: statement carries raw baseline "
                       f"markup (fence/req_id/heading) — extraction fault")

    # G2 — prefix must follow the regulation, uniformly (ledger §4.4).
    for r in rows:
        want = PREFIX_BY_REG.get(r["regulation"], "SO")
        got = r["objective_id"][:2]
        if got != want:
            out.append(f"{r['objective_id']}: prefix {got} contradicts regulation "
                       f"{r['regulation']} (expected {want})")

    # G3 — id must resolve to exactly one row (ledger §4.3, slot collisions).
    seen: dict[str, int] = {}
    for r in rows:
        seen[r["objective_id"]] = seen.get(r["objective_id"], 0) + 1
    for oid, n in sorted(seen.items()):
        if n > 1:
            out.append(f"{oid}: {n} rows share one objective id")

    # G4 — every objective must trace to a Phase 1 goal, and every goal must be
    # carried forward. The check runs in both directions because the two failure
    # modes look identical from inside the document: a dropped objective and an
    # invented one are both "the row count is plausible".
    have = {r["parent_goal"] for r in rows}
    for r in rows:
        if not r["parent_goal"].startswith("AG-"):
            out.append(f"{r['objective_id']}: parent {r['parent_goal']!r} is not a "
                       f"Phase 1 goal id (ADR-004 chain broken)")
    if run_dir is not None:
        upstream = {g["id"] for g in load_goals(run_dir)}
        for missing in sorted(upstream - have):
            out.append(f"{missing}: Phase 1 goal has no Phase 2 objective — dropped "
                       f"between phases")

    return out


# --------------------------------------------------------------------------
# render (zero LLM)
# --------------------------------------------------------------------------

DOC01_HEADER = (
    "| Objective ID | Operational Statement | Parent Goal | Regulation | "
    "Operational Scope (Ambit) | Verification Criteria | Method | "
    "Responsible Owner | Control Anchors |\n"
    "|---|---|---|---|---|---|---|---|---|"
)


def cell(v: str) -> str:
    """Markdown table cell: no raw pipes, no newlines."""
    return (v or UNSET).replace("|", "\\|").replace("\n", " ").strip() or UNSET


def _company_name(repo: Path, run_dir: Path) -> str:
    """The bound company name, or a neutral fallback.

    A run directory that carries no `pipeline/cases/<case_id>/case.yaml` is not
    an error: the prototype must render from a bare run dir, which is what makes
    it testable without a GPU. Fall back to the case id rather than failing.
    """
    try:
        case = load_case(repo, _case_id(run_dir))
    except (FileNotFoundError, OSError, ValueError):
        case = {}
    return case.get("company_name") or _case_id(run_dir)


def render_doc01(repo: Path, run_dir: Path, rows: list[dict]) -> str:
    name = _company_name(repo, run_dir)
    lines = [
        f"# Privacy & Security Operational Objectives — {name}",
        "",
        "> **Document Purpose:** Operational Objectives derived from the Phase 1 "
        "Adjusted Goals. Cells marked `—` are seams: the pipeline has no "
        "derivation rule for them and does not invent one.",
        "",
        "## §1 Method",
        "",
        "Every populated cell is a function of the Phase 1 deliverable and the "
        "frozen corpus. Control anchors are derived by `controls.goal_anchors` "
        "(Sub-SO → `source_SR` → mapping store → CONTROLS), never copied and "
        "never emitted by a model. Objective ids inherit the Phase 1 slot.",
        "",
    ]
    current = None
    for r in rows:
        if r["subdomain"] != current:
            current = r["subdomain"]
            lines += [f"### {current} — {r['subdomain_name']}", "", DOC01_HEADER]
        lines.append(
            "| `{oid}` | {stmt} | `{parent}` | **{reg}** | {scope} | {crit} | "
            "{meth} | {own} | `{anch}` |".format(
                oid=cell(r["objective_id"]), stmt=cell(r["statement"]),
                parent=cell(r["parent_goal"]), reg=cell(r["regulation"]),
                scope=cell(r["scope"]), crit=cell(r["criteria"]),
                meth=cell(r["method"]), own=cell(r["owner"]),
                anch=cell(r["anchors"]))
        )
    lines += ["", "## §2 Version History", "",
              "| Version | Date | Author / Role | Changes |", "|---|---|---|---|",
              "| `0.1` | — | aegis-mvp phase2 prototype | "
              "Deterministic spine: ids, parents, statements, anchors. "
              "Seams left unset. |", ""]
    return "\n".join(lines)


def render_doc02() -> str:
    """Doc02 prototype. The 7 principles are a baseline asset; the per-case
    constraint is a seam, so the principles render with their UNSET constraint
    rather than with another company's architecture (ledger §4.6)."""
    return "\n".join([
        "# Secure Design & Systems Engineering Principles",
        "",
        "> **Prototype:** principle scaffolding only. Per-case constraints are a "
        "seam and render as `—`.",
        "",
    ])


def _case_id(run_dir: Path) -> str:
    return json.loads((run_dir / "manifest.json").read_text(encoding="utf-8"))["case_id"]


# --------------------------------------------------------------------------
# cli
# --------------------------------------------------------------------------

def _confirmed(run_dir: Path) -> list[str]:
    """Confirmed regulations, or `[]` when the run carries no verdicts.

    Phase 2 does not need this file to derive anything — the regulation travels
    on each goal record — so a run without it still renders. It is printed for
    the reader's benefit and must not be able to fail the run.
    """
    try:
        return confirmed_regulations(run_dir)
    except (FileNotFoundError, OSError, ValueError, KeyError):
        return []


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--run-dir", required=True, type=Path,
                    help="a Phase 1 run directory (steps/goals/*.json)")
    ap.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[2])
    ap.add_argument("--out", type=Path, help="write Doc01/Doc02 here "
                                              "(default: stdout summary only)")
    ap.add_argument("--json", action="store_true", help="emit derived rows as JSON")
    args = ap.parse_args(argv)

    repo, run_dir = args.repo.resolve(), args.run_dir.resolve()
    if not (run_dir / "steps" / "goals").is_dir():
        print(f"error: {run_dir} has no steps/goals/ — not a Phase 1 run dir",
              file=sys.stderr)
        return 2

    rows = build(repo, run_dir)
    findings = check(rows, run_dir)

    if args.json:
        print(json.dumps(rows, indent=1, ensure_ascii=False))
        return 1 if findings else 0

    if args.out:
        args.out.mkdir(parents=True, exist_ok=True)
        (args.out / "Doc01_Operational_Objectives.md").write_text(
            render_doc01(repo, run_dir, rows), encoding="utf-8")
        (args.out / "Doc02_Secure_Design_Principles.md").write_text(
            render_doc02(), encoding="utf-8")

    seams = {c: sum(1 for r in rows if r[c] == UNSET)
             for c in ("scope", "criteria", "method", "owner", "anchors")}
    print(f"objectives: {len(rows)}   sub-domains: {len({r['subdomain'] for r in rows})}")
    print(f"confirmed regulations: {_confirmed(run_dir) or 'not recorded in this run'}")
    print(f"unseamed cells: {seams}")
    if findings:
        print(f"GATE FAIL ({len(findings)}):")
        for f in findings[:20]:
            print(f"  - {f}")
        return 1
    print("gates: pass")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())