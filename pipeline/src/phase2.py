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

Doc01 is fully deterministic. Doc02 is the opposite: its definitions are a
baseline asset and its `Constraint` column is the one genuinely generative cell
in Phase 2 (ledger §3.3). That column comes from the `p2d` step
(`docs/pipeline/prompts/PROM-P2-03_SYNTHESIZE_PRINCIPLES.md`) and is loaded from
`steps/principles.json`; with no such file every constraint renders as `UNSET`,
which is the honest rendering of "not yet synthesised".
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

#: The 7 universal engineering principles — a BASELINE ASSET (ADR-013 D2).
#: Copied, never regenerated: `Definition` is byte-identical across all three
#: hand-authored Doc02s for 5 of 7 (ledger §3.2). The per-case `Constraint` is
#: the only generative cell in Doc02 (ledger §3.3), and it is what `p2d` produces.
#:
#: The `PRIN-ENG-06` and `-07` definitions use the Case 02/03 wording, which is
#: the neutral one. Case 01 reads "strictly scoped DTOs" — an L4
#: technology-class term recorded at ledger §4.7, and the reason the fixture
#: selection is deliberate rather than arbitrary.
CATEGORIES = [
    {"n": 1, "title": "Architectural & Data Flow Modeling", "sec": "§2",
     "def_col": "Architectural Definition", "con_col": "Diagrammatic & Modeling Constraint",
     "domain": "System Architecture, Data Flow Diagrams (DFD), Component Topology, and Network Boundaries.",
     "lit": "Adam Shostack (2014, *Threat Modeling: Designing for Security*); Jerome Saltzer & Michael Schroeder (1975)."},
    {"n": 2, "title": "Core Systems & Access Security", "sec": "§3",
     "def_col": "Security Definition", "con_col": "Architectural & Operational Constraint",
     "domain": "System-wide access control, failure state handling, and resource isolation.",
     "lit": "Jerome Saltzer & Michael Schroeder (1975, *The Protection of Information in Computer Systems*); OWASP."},
    {"n": 3, "title": "Requirements Engineering & Verifiability", "sec": "§4",
     "def_col": "Requirements Engineering Definition", "con_col": "Specification Constraint",
     "domain": "Specification of system behaviors, verification criteria, and lifecycle traceability.",
     "lit": "ISO/IEC/IEEE 29148:2018; INCOSE Guide to Writing Requirements; EARS (Mavin et al., 2009)."},
    {"n": 4, "title": "Privacy by Design & Data Lifecycle", "sec": "§5",
     "def_col": "Privacy Engineering Definition", "con_col": "Operational & Diagrammatic Constraint",
     "domain": "Personal data lifecycle, data-subject sovereignty, and purpose-bound processing.",
     "lit": "Ann Cavoukian (2009, *Privacy by Design: 7 Foundational Principles*); GDPR Art. 5, 17, 25; ISO/IEC 27701:2019."},
]

PRINCIPLES = [
    {"id": "PRIN-ENG-01", "category": 1, "skill": "trust-boundary-analysis",
     "name": "Explicit Trust Boundaries & Complete Mediation",
     "source": "Shostack (2014) / Saltzer & Schroeder (1975)",
     "definition": "Every interface separating zones of differing privilege must be visually demarcated, and every crossing flow must be authenticated and validated with zero unmediated bypasses."},
    {"id": "PRIN-ENG-02", "category": 1, "skill": "attack-surface-analysis",
     "name": "Attack Surface Minimization & Peripheral Resilience",
     "source": "Howard & LeBlanc (2003) / Schneier (2000)",
     "definition": "Accessible entry points, communication channels, and active interfaces must be reduced to the minimum necessary, and auxiliary ingress hooks must match core security intensity."},
    {"id": "PRIN-ENG-03", "category": 2, "skill": "least-privilege-analysis",
     "name": "Least Privilege & Mechanism Isolation",
     "source": "Saltzer & Schroeder (1975)",
     "definition": "Every principal (user, service, background worker) must operate with the minimum privileges necessary, and distinct tenants or sensitivity levels must not share unisolated execution mechanisms."},
    {"id": "PRIN-ENG-04", "category": 2, "skill": "fail-safe-defaults-analysis",
     "name": "Fail-Safe Defaults & Closed Failure States",
     "source": "Saltzer & Schroeder (1975) / OWASP",
     "definition": "Access decisions and state transitions must default to refusal, and unexpected failures or exceptions must terminate in a secure closed state without state corruption or data leakage."},
    {"id": "PRIN-ENG-05", "category": 3, "skill": "verifiability-analysis",
     "name": "Requirement Verifiability & Atomicity",
     "source": "ISO/IEC/IEEE 29148:2018 / EARS (2009)",
     "definition": "Every security and privacy requirement must be atomic (one single condition and response) and possess a deterministic, automated pass/fail verification method."},
    {"id": "PRIN-ENG-06", "category": 4, "skill": "data-minimization-analysis",
     "name": "Proactive Data Minimization & Scoped Projection",
     "source": "Cavoukian (2009) / GDPR Art. 5(1)(c)",
     "definition": "Only data strictly indispensable for fulfilling the declared service purpose may be collected, transmitted, or retained, and egress models must project strictly scoped data views."},
    {"id": "PRIN-ENG-07", "category": 4, "skill": "lifecycle-erasure-analysis",
     "name": "End-to-End Lifecycle Security & Irreversible Erasure",
     "source": "Cavoukian (2009) / GDPR Art. 17",
     "definition": "Protection covers the entire data lifecycle; data subject to erasure must be permanently destroyed across edge caches, primary stores, archives, and disaster-recovery copies."},
]

PRINCIPLE_IDS = [p["id"] for p in PRINCIPLES]

#: Function words excluded from the grounding ratio. A constraint's tokens that
#: appear in the fact sheet and in NO principle definition are the company-
#: specific content. Deliberately a MEASUREMENT, not a gate (ficha PROM-P2-03,
#: Guard hooks): M11 established that demanding a named artefact does not make
#: a column more company-specific, so gating on it would reject a 7-row
#: document into uselessness while teaching nothing.
STOPWORDS = {"the", "and", "for", "with", "that", "this", "from", "every",
             "must", "may", "its", "any", "all", "not", "are", "their",
             "each", "which", "when", "where", "only", "into", "than", "then"}


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
    """Doc01 findings. Empty list means the derived set passed everything below.

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


#: The four empirical verification methods the Doc01 §1.3 publishes. A
#: `method_lead` outside this vocabulary is not a rule, it is a new one.
METHOD_VOCAB = {"TEST", "INSPECT", "DEMONSTRATE", "ANALYZE"}


def _other_case_intakes(repo: Path) -> list[str]:
    """Every OTHER case's intake form, as flat text.

    The intake form is where a company declares its own nouns — `eGate`,
    `traveller`, `kiosk`, `OmniScore`. That makes it the right source for a
    contamination vocabulary, and an earlier version of this gate read the
    Doc02 constraints instead and flagged `boundary`, `including`, `flows` and
    `within` — ordinary English, on the first real run of Phase 2 (jobs
    1996356/1996357). A gate that fires on the language is not a gate.

    Returns `[]` when the corpus is absent, so the check degrades to silence
    rather than to a false accusation.
    """
    out: list[str] = []
    for intake in sorted((repo / "cases").glob(
            "Case_*/01_PHASE1_CONTEXT/Doc01_INTAKE_FORM.md")):
        try:
            out.append(intake.read_text(encoding="utf-8"))
        except OSError:
            continue
    return out


def _foreign_vocab(repo: Path) -> frozenset[str]:
    """Content words that name SOME OTHER company's own assets.

    G7 compares a constraint against this vocabulary rather than against a
    capitalisation heuristic. A "does it look like a proper noun" regex cannot
    see `eGate` — the capital is mid-word, so no word boundary precedes it —
    which is precisely the token the ledger's §4.6 defect is made of. Reading
    the other cases' intake forms catches the recorded defect by name without
    a capitalisation blind spot, and because an intake states a company's own
    assets rather than the register they are described in, it does not pull in
    the surrounding English.
    """
    shared = set()
    for p in PRINCIPLES:
        shared |= set(re.findall(r"[a-z]{5,}", p["definition"].lower()))
    vocab: set[str] = set()
    for text in _other_case_intakes(repo):
        vocab |= set(re.findall(r"[a-z]{5,}", text.lower()))
    return frozenset(vocab - shared - STOPWORDS)


#: A token shaped like a NAME rather than a word: CamelCase (`eGate`,
#: `OmniScore`), ALLCAPS (`SPOC`), or capitalised and not sentence-initial.
#: The intersection of "looks like a name" and "appears in another case's
#: intake" is what separates an asset from the English around it: `eGate` is
#: both, `boundary` is in the intake too but is neither.
_NAME_RE = re.compile(r"\b[a-z]+[A-Z][A-Za-z]*\b|\b[A-Z]{3,}\b|\b(?<![.!?]\s)[A-Z][a-z]{2,}\b")


def check_doc02(repo: Path, run_dir: Path, principles: list[dict]) -> list[str]:
    """Doc02 findings: G5 completeness, G6 technology neutrality, G7 grounding.

    G7 mechanises ledger §4.6 — Case 03's Doc02 carrying Case 02's eGate
    architecture — as a checkable property instead of a reviewer's memory.
    The check is one-directional on purpose. A constraint that says nothing
    company-specific is a weak document (reported by `grounding_ratio`), not a
    defect, so it is measured rather than failed.
    """
    import quality  # noqa: PLC0415 — local: quality imports nothing from here

    out: list[str] = []
    by_id = {p["id"]: p for p in principles}

    # G5 — every canonical principle exactly once. A dropped row and a duplicated
    # row both leave a structurally valid table, which is why the check is
    # bidirectional rather than a count.
    for pid in PRINCIPLE_IDS:
        if pid not in by_id:
            out.append(f"{pid}: Doc02 has no row for this principle")
    for pid, row in sorted(by_id.items()):
        if pid not in PRINCIPLE_IDS:
            out.append(f"{pid}: Doc02 carries an unknown principle id")

    fact = _fact_sheet(run_dir)
    declared = set(re.findall(r"[a-z]{5,}", fact.lower())) if fact else set()
    foreign = _foreign_vocab(repo) - declared
    for pid in PRINCIPLE_IDS:
        row = by_id.get(pid)
        if row is None:
            continue
        constraint = str(row.get("constraint", "") or "")
        if not constraint.strip() or constraint == UNSET:
            continue  # a declared seam is honest; an invented cell is not
        # G6 — R5/R13 technology neutrality, reusing the Phase 1 gate.
        out += [f"{pid}: {f}" for f in quality.check_no_technology(
            constraint, str(row.get("method_lead", "")), str(row.get("eval_scope", "")))]
        # G7 — another company's architecture, by name.
        names = {m.group(0).lower() for m in _NAME_RE.finditer(constraint)}
        hits = sorted(n for n in names & foreign if n not in declared)
        if hits:
            out.append(f"{pid}: constraint names {', '.join(hits)} — an asset of "
                       f"another case, absent from this run's fact sheet (ledger §4.6)")

        method = str(row.get("method_lead", "") or "").strip()
        if method and method != UNSET:
            head = method.split(":")[0].split("(")[0].strip().strip("`").upper()
            if head and head not in METHOD_VOCAB:
                out.append(f"{pid}: method_lead {head!r} is outside the published "
                           f"vocabulary {sorted(METHOD_VOCAB)}")

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


def load_tensions(run_dir: Path) -> list[dict]:
    tfile = run_dir / "steps" / "tensions.json"
    if tfile.exists():
        try:
            return json.loads(tfile.read_text(encoding="utf-8")).get("tensions", [])
        except (OSError, ValueError):
            return []
    return []


def load_operationalizations(run_dir: Path) -> dict[str, dict]:
    """Load per-subdomain operationalization data from steps/phase2/*.json."""
    p2_dir = run_dir / "steps" / "phase2"
    if not p2_dir.is_dir():
        return {}
    out: dict[str, dict] = {}
    for jf in sorted(p2_dir.glob("*.json")):
        try:
            blob = json.loads(jf.read_text(encoding="utf-8"))
            sd = blob.get("subdomain")
            if sd:
                out[sd] = blob
        except (OSError, ValueError):
            continue
    return out


def _slot_of(objective_id: str) -> str | None:
    """`SO-D-06.3-002` -> `D-06.3-002`. The regulation prefix is positional.

    Matching operationalization data by FULL id would silently drop a row
    whose model answer wrote `SO-` where Phase 1 derived `PO-` (GDPR slot):
    the seams would stay `—` with nothing to point at. The slot is the
    identity the two sides share by construction.
    """
    m = re.search(r"(D-\d{2}\.\d-\d{3})$", objective_id or "")
    return m.group(1) if m else None


def _ops_by_slot(op_data: dict) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for o in op_data.get("objectives", []):
        s = _slot_of(str(o.get("objective_id", "")))
        if s:
            out[s] = o
    return out


def seam_fill(rows: list[dict], op_map: dict[str, dict]) -> tuple[int, int]:
    """(objectives whose method/criteria/owner came through, total objectives).

    Measured, not gated: a p2o sub-domain that failed must surface as a
    number in the stage result, not as silent `—` cells in the document.
    """
    by_slot: dict[str, dict] = {}
    for blob in op_map.values():
        by_slot.update(_ops_by_slot(blob))
    filled = sum(1 for r in rows
                 if by_slot.get(_slot_of(r["objective_id"]), {}).get("criteria"))
    return filled, len(rows)


def method_distribution(op_map: dict[str, dict]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for blob in op_map.values():
        for o in blob.get("objectives", []):
            m = str(o.get("method", ""))
            counts[m] = counts.get(m, 0) + 1
    return dict(sorted(counts.items()))


def method_diversity_findings(dist: dict[str, int]) -> list[str]:
    """R10b invariant 3: a default exceeding 60% of the batch is mode collapse.

    The four ISO 29148 methods are the vocabulary the ficha offers; a batch
    where one of them swallows the rest is the model picking a default, not
    classifying — the same distribution ceiling the Phase 1 adjustment badge
    was measured against.
    """
    total = sum(dist.values())
    if total < 4:
        return []
    return [f"method {m}: {n}/{total} objectives ({n / total:.0%}) exceeds the "
            f"60% mode-collapse ceiling (R10b) — the batch is collapsing to "
            f"one default verification method"
            for m, n in dist.items() if n / total > 0.60]


def parse_p2o(answer: str, subdomain: str | None = None) -> dict:
    """Parse and validate one sub-domain's operationalization answer."""
    import quality
    from steps import extract_fenced

    raw = extract_fenced(answer, "json").strip()
    data = json.loads(raw)
    if not isinstance(data, dict):
        raise ValueError("p2o: expected a JSON object")
    sd_raw = str(data.get("subdomain", "")).strip()
    m_sd_field = re.match(r"^[Dd][-_.]?(\d{2})[-_.](\d)$", sd_raw)
    sd = f"D-{m_sd_field.group(1)}.{m_sd_field.group(2)}" if m_sd_field else sd_raw.upper()
    if subdomain and sd != subdomain:
        raise ValueError(f"p2o: expected subdomain {subdomain!r}, got {sd!r}")
    data["subdomain"] = sd or subdomain   # the blob is indexed by this key downstream
    op_trans = str(data.get("operational_translation", "")).strip()
    if not op_trans:
        raise ValueError("p2o: operational_translation cannot be empty")
    objs = data.get("objectives", [])
    if not isinstance(objs, list) or len(objs) == 0:
        raise ValueError("p2o: expected non-empty list under 'objectives'")

    normalized_objs = []
    seen_criteria: dict[str, str] = {}
    rule_seq = 0    # per CALL, not per objective: rule ids are unique across
                    # the whole sub-domain, and two objectives in one call
                    # must never both emit RULE-D-XX.Y-001
    for idx, o in enumerate(objs):
        if not isinstance(o, dict):
            raise ValueError(f"p2o: objective {idx} is not an object")
        oid = str(o.get("objective_id") or o.get("id") or "").strip().upper()
        if oid.startswith("OBJ-"):
            oid = "SO-" + oid[4:]
        m_oid = re.match(r"^(?:PO|SO)-(D-\d{2}\.\d)-\d{3}$", oid)
        if not m_oid:
            raise ValueError(f"p2o: objective {idx} id {oid!r} is not a "
                             f"PO-/SO-D-XX.Y-NNN id")
        if subdomain and m_oid.group(1) != subdomain:
            raise ValueError(f"p2o: {oid} belongs to {m_oid.group(1)}, not to "
                             f"this sub-domain ({subdomain})")
        meth = str(o.get("method", "")).strip().upper()
        if meth not in METHOD_VOCAB:
            raise ValueError(f"p2o: {oid} invalid method {meth!r}, must be one of {sorted(METHOD_VOCAB)}")
        crit = str(o.get("criteria", "")).strip()
        if len(crit.split()) < 8:
            raise ValueError(f"p2o: {oid} criteria too thin to be falsifiable "
                             f"({len(crit.split())} words) — name the verification "
                             f"artifact or test condition")
        crit_key = re.sub(r"\W+", " ", crit.lower()).strip()
        if crit_key in seen_criteria:
            raise ValueError(f"p2o: {oid} criteria duplicates {seen_criteria[crit_key]}'s "
                             f"— a repeated template is not a per-objective criterion")
        seen_criteria[crit_key] = oid
        own = str(o.get("owner", "")).strip()
        if not own:
            raise ValueError(f"p2o: {oid} owner cannot be empty")
        raw_rules = o.get("rules", [])
        if not isinstance(raw_rules, list) or len(raw_rules) == 0:
            # the RULE-* tail is the phase's bridge to Phase 3 (SPEC §6): an
            # objective with no operational rule contributes nothing to the
            # catalogue and must not pass as operationalized
            raise ValueError(f"p2o: {oid} must carry at least one RULE-* rule")
        norm_rules = []
        for r in raw_rules:
            if isinstance(r, str):
                parts = r.split(":", 1)
                rid = parts[0].strip()
                stmt = parts[1].strip() if len(parts) > 1 else r.strip()
                r_dict = {"rule_id": rid, "statement": stmt, "verification_target": meth}
            elif isinstance(r, dict):
                vt = str(r.get("verification_target") or meth).strip().upper()
                r_dict = {
                    "rule_id": str(r.get("rule_id") or r.get("id") or "").strip(),
                    "statement": str(r.get("statement") or r.get("description") or r.get("rule") or "").strip(),
                    "verification_target": vt if vt in METHOD_VOCAB else meth,
                }
            else:
                raise ValueError(f"p2o: {oid} rule must be string or object")

            # Every rule leaves with a CANONICAL id numbered across the whole
            # call: the model's own numbering restarts per objective and takes
            # variants (RULE-D-06.3-1, RULE_D_06_3_001, bare prose). The slot
            # the rule names is honoured; the sequence is ours.
            rule_seq += 1
            m_sd = re.search(r"D[-_.](\d{2})[-_.](\d)", r_dict["rule_id"],
                             re.IGNORECASE)
            sd_norm = (f"D-{m_sd.group(1)}.{m_sd.group(2)}" if m_sd
                       else m_oid.group(1))
            r_dict["rule_id"] = f"RULE-{sd_norm}-{rule_seq:03d}"
            stmt = r_dict["statement"]
            if not ("SHALL" in stmt.upper() or "MUST" in stmt.upper()):
                raise ValueError(f"p2o: {r_dict['rule_id']} statement must contain SHALL or MUST (EARS/RFC2119)")
            tech_hits = quality.check_no_technology(stmt)
            if tech_hits:
                raise ValueError(f"p2o: {r_dict['rule_id']} {tech_hits[0]}")
            norm_rules.append(r_dict)

        normalized_objs.append({
            "objective_id": oid,
            "method": meth,
            "criteria": crit,
            "owner": own,
            "rules": norm_rules,
        })

    data["objectives"] = normalized_objs
    return data


def render_doc01(repo: Path, run_dir: Path, rows: list[dict]) -> str:
    name = _company_name(repo, run_dir)
    tensions = load_tensions(run_dir)
    op_map = load_operationalizations(run_dir)

    lines = [
        f"# Privacy & Security Operational Objectives — {name}",
        "",
        "> **Document Purpose:** Defines the Operational Objectives across all active "
        "sub-domains, separating the distinct operational scopes of applicable regulations, "
        "establishing empirical verification methods (ISO 29148 / INCOSE), and formalizing "
        "testable operational engineering rules (`RULE-*`). Cells marked `—` are seams: "
        "the pipeline has no derivation rule for them and does not invent one.",
        "",
        "## §1 Governance & Structure Guide",
        "",
        "### 1.1 Separation of Regulatory Ambits",
        "Where multiple regulations apply to the same sub-domain, they bind distinct operational "
        "ambits and cannot be conflated into a single objective (e.g. GDPR binds personal data, "
        "CRA binds product security, NIS 2 binds entity risk management, AI Act binds high-risk AI).",
        "",
        "### 1.2 Empirical Verification Methods (ISO 29148 / INCOSE)",
        "Every operational objective is evaluated via one of four empirical methods:",
        "- `TEST`: Automated assertion, CI/CD pipeline test, or runtime security probe.",
        "- `INSPECT`: Systematic review of configuration (IaC), process artefacts, or audit records.",
        "- `DEMONSTRATE`: Walkthrough or observable execution of an end-to-end operational flow.",
        "- `ANALYZE`: Systematic risk examination, architectural boundary review, or threat model.",
        "",
    ]

    if tensions:
        lines += [
            "## §2 Harmonisation of Strategic Tensions",
            "",
            "When multiple regulations apply, operational tensions are harmonized as follows:",
            "",
            "| Tension ID | Sub-Domains | Tension | Conflict | Resolution Strategy |",
            "|---|---|---|---|---|",
        ]
        for t in tensions:
            lines.append(
                f"| `{cell(t.get('id', ''))}` | `{cell(t.get('subdomains', ''))}` | "
                f"**{cell(t.get('tension', ''))}** | {cell(t.get('conflict', ''))} | "
                f"{cell(t.get('resolution', ''))} |"
            )
        lines.append("")

    sec_num = "§3" if tensions else "§2"
    lines += [f"## {sec_num} Operational Objectives by Domain", ""]

    current = None
    all_rules_in_subdomain: list[dict] = []

    for r in rows:
        sd = r["subdomain"]
        if sd != current:
            if current is not None:
                if all_rules_in_subdomain:
                    lines += [
                        "",
                        f"#### Operational Engineering Rules (`RULE-*`) — {current}",
                        "",
                        "| Rule ID | Operational Statement | Method | Parent Objective |",
                        "|---|---|---|---|",
                    ]
                    for rl in all_rules_in_subdomain:
                        lines.append(
                            f"| `{cell(rl.get('rule_id', ''))}` | {cell(rl.get('statement', ''))} | "
                            f"`{cell(rl.get('verification_target', ''))}` | `{cell(rl.get('parent_obj', ''))}` |"
                        )
                # A sub-domain with no RULE block ends at its objectives table;
                # the next heading still needs its blank separator, or the table
                # and the `###` header end up on adjacent lines (run_p2c3,
                # D-03.3 — the one sub-domain whose p2o call failed).
                lines.append("")
                all_rules_in_subdomain = []

            current = sd
            lines.append(f"### {current} — {r['subdomain_name']}")
            lines.append("")

            op_data = op_map.get(current, {})
            op_trans = op_data.get("operational_translation")
            if op_trans:
                lines.append(f"**Operational Translation ({name} Context):** {op_trans}")
                lines.append("")

            lines += [DOC01_HEADER]

        op_data = op_map.get(current, {})
        om = _ops_by_slot(op_data).get(_slot_of(r["objective_id"]))
        if om:
            crit = om.get("criteria") or r["criteria"]
            meth = om.get("method") or r["method"]
            own = om.get("owner") or r["owner"]
            for ritem in om.get("rules", []):
                ritem_copy = dict(ritem)
                ritem_copy["parent_obj"] = r["objective_id"]
                all_rules_in_subdomain.append(ritem_copy)
        else:
            crit = r["criteria"]
            meth = r["method"]
            own = r["owner"]

        lines.append(
            "| `{oid}` | {stmt} | `{parent}` | **{reg}** | {scope} | {crit} | "
            "{meth} | {own} | `{anch}` |".format(
                oid=cell(r["objective_id"]), stmt=cell(r["statement"]),
                parent=cell(r["parent_goal"]), reg=cell(r["regulation"]),
                scope=cell(r["scope"]), crit=cell(crit),
                meth=cell(meth), own=cell(own),
                anch=cell(r["anchors"]))
        )

    if all_rules_in_subdomain:
        lines += [
            "",
            f"#### Operational Engineering Rules (`RULE-*`) — {current}",
            "",
            "| Rule ID | Operational Statement | Method | Parent Objective |",
            "|---|---|---|---|",
        ]
        for rl in all_rules_in_subdomain:
            lines.append(
                f"| `{cell(rl.get('rule_id', ''))}` | {cell(rl.get('statement', ''))} | "
                f"`{cell(rl.get('verification_target', ''))}` | `{cell(rl.get('parent_obj', ''))}` |"
            )
        lines.append("")

    ver_sec = "§4" if tensions else "§3"
    lines += ["", f"## {ver_sec} Version History", "",
              "| Version | Date | Author / Role | Changes |", "|---|---|---|---|",
              "| `0.2` | — | aegis-mvp Phase 2 (enriched) | "
              "Operational translation, ISO 29148 methods, criteria, and RULE-* catalogue. |", ""]
    return "\n".join(lines)


def principles_for(run_dir: Path) -> list[dict]:
    """The per-case `Constraint` / `Method & Lead` / `Evaluation Scope` triples.

    Read from `steps/principles.json` when the `p2d` step ran; otherwise every
    generative cell renders as `UNSET`. The fallback is deliberate and loud —
    rendering another company's architecture here is the defect the ledger
    records at §4.6, and a seam is the honest alternative to it.
    """
    by_id: dict[str, dict] = {}
    f = run_dir / "steps" / "principles.json"
    if f.exists():
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
            for p in data.get("principles", []):
                if isinstance(p, dict) and p.get("id") in PRINCIPLE_IDS:
                    by_id[p["id"]] = p
        except (OSError, ValueError):
            by_id = {}
    return [dict(by_id.get(p["id"], {}), **p) for p in PRINCIPLES]


def grounding_ratio(principles: list[dict], fact_sheet: str) -> float:
    """Share of constraints carrying content absent from the definitions.

    A constraint is counted as grounded when it contains at least one token
    that appears in the company's fact sheet and in NO principle definition —
    i.e. content that could only come from this company. A constraint that is
    only the definition restated scores 0. Reported, never gated (see
    `STOPWORDS`).
    """
    generic = set()
    for p in PRINCIPLES:
        generic |= set(re.findall(r"[a-z]{3,}", p["definition"].lower()))
    company = set(re.findall(r"[a-z]{3,}", fact_sheet.lower())) - generic - STOPWORDS
    if not company:
        return 0.0
    hit = 0
    for p in principles:
        con = str(p.get("constraint", "") or "").lower()
        if con and any(t in company for t in set(re.findall(r"[a-z]{3,}", con))):
            hit += 1
    return round(hit / len(principles), 3) if principles else 0.0


def _fact_sheet(run_dir: Path) -> str:
    f = run_dir / "steps" / "fact_sheet.yaml"
    return f.read_text(encoding="utf-8") if f.exists() else ""


def render_doc02(repo: Path, run_dir: Path, principles: list[dict]) -> str:
    """Doc02 — the engineering spine. Four category tables plus the §6 skill map.

    The `Definition` column is a baseline asset copied from `PRINCIPLES`
    (ADR-013 D2); the `Constraint` column is the per-case work `p2d` produces
    (ledger §3.3). §6 emits REPO-RELATIVE paths: the absolute
    `file:///c:/Users/…` links the hand-authored deliverables carry resolve only
    on the author's machine (ledger §4.5).
    """
    by_id = {p["id"]: p for p in principles}
    lines = [
        f"# Secure Design & Systems Engineering Principles — {_company_name(repo, run_dir)}",
        "",
        "> **Document Purpose:** establishes the 7 technology-agnostic engineering "
        "principles that constrain this company's solution space before "
        "technologies are chosen in Phase 3. The definitions are a baseline "
        "asset; the `Constraint` column is this company's own architecture. A "
        "`—` cell is a seam — the pipeline has no derivation for it — not a "
        "guess.",
        "",
        "## §1 The engineering spine",
        "",
        "Phase 2 runs on two non-overlapping pillars. **Doc01** carries the "
        "regulatory spine: what the law proportionally requires, as verifiable "
        "operational objectives. **Doc02** carries the engineering spine: 7 "
        "universal principles bound to this company's architecture. Per "
        "ISO/IEC/IEEE 29148:2018 clause 5.2.4 these state *verifiable "
        "architectural constraints* — what boundaries, invariants and failure "
        "modes must hold — without prescribing concrete database engines, "
        "frameworks, protocols or libraries, which belong to Phase 3.",
        "",
    ]
    for cat in CATEGORIES:
        lines += [
            f"## {cat['sec']} Principles Category {cat['n']} — {cat['title']}",
            "",
            f"> **Governing Domain:** {cat['domain']}  ",
            f"> **Foundational Literature:** {cat['lit']}",
            "",
            f"| Principle ID | Principle Name | Academic Source | {cat['def_col']} | "
            f"{cat['con_col']} | Verification Method & Lead |",
            "|---|---|---|---|---|---|",
        ]
        for p in PRINCIPLES:
            if p["category"] != cat["n"]:
                continue
            row = by_id.get(p["id"], {})
            lines.append(
                f"| `{p['id']}` | **{p['name']}** | {p['source']} | {p['definition']} | "
                f"{cell(row.get('constraint', ''))} | {cell(row.get('method_lead', ''))} |")
        lines.append("")

    lines += [
        "## §6 Operationalization via Specialized Agentic Skills (1:1 symmetry)",
        "",
        "| Principle ID | Principle Name | Specialized Autonomous Skill | Path in Repository | Primary Evaluation Scope |",
        "|---|---|---|---|---|",
    ]
    for p in PRINCIPLES:
        row = by_id.get(p["id"], {})
        lines.append(
            f"| `{p['id']}` | {p['name']} | `{p['skill']}` | "
            f"[`baseline/skills/{p['skill']}/`](baseline/skills/{p['skill']}/) | "
            f"{cell(row.get('eval_scope', ''))} |")
    lines += ["", "## §7 Version History", "",
              "| Version | Date | Author / Role | Changes |", "|---|---|---|---|",
              "| `0.1` | — | aegis-mvp phase2 | Definitions from the baseline; "
              "constraints per company. |", ""]
    return "\n".join(lines)


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

    principles = principles_for(run_dir)
    findings += check_doc02(repo, run_dir, principles)
    ratio = grounding_ratio(principles, _fact_sheet(run_dir))

    if args.json:
        print(json.dumps({"objectives": rows, "principles": principles,
                          "grounding_ratio": ratio}, indent=1, ensure_ascii=False))
        return 1 if findings else 0

    if args.out:
        args.out.mkdir(parents=True, exist_ok=True)
        (args.out / "Doc01_Operational_Objectives.md").write_text(
            render_doc01(repo, run_dir, rows), encoding="utf-8")
        (args.out / "Doc02_Secure_Design_Principles.md").write_text(
            render_doc02(repo, run_dir, principles), encoding="utf-8")

    seams = {c: sum(1 for r in rows if r[c] == UNSET)
             for c in ("scope", "criteria", "method", "owner", "anchors")}
    unseamed_prin = sum(1 for p in principles
                        if str(p.get("constraint", "")) in ("", UNSET))
    print(f"objectives: {len(rows)}   sub-domains: {len({r['subdomain'] for r in rows})}")
    print(f"confirmed regulations: {_confirmed(run_dir) or 'not recorded in this run'}")
    print(f"unseamed cells: {seams}")
    print(f"doc02 constraints unseamed: {unseamed_prin}/7   grounding_ratio: {ratio}")
    if findings:
        print(f"GATE FAIL ({len(findings)}):")
        for f in findings[:20]:
            print(f"  - {f}")
        return 1
    print("gates: pass")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())