#!/usr/bin/env python3
"""aegis_pipeline.phases.phase2.derivation — Derivation rules and gates for Operational Objectives."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# Ensure pipeline/src is importable
_src = Path(__file__).resolve().parents[3]
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

from compose import load_selection, subdomain_name
from aegis_pipeline.guards import controls
import quality
from aegis_pipeline.phases.phase2.principles import (
    PREFIX_BY_REG,
    PRINCIPLES,
    PRINCIPLE_IDS,
    REG_ORDER,
    SCOPE_BY_REG,
    STOPWORDS,
    UNSET,
)
from aegis_pipeline.phases.phase2.parsers import METHOD_VOCAB


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
    ag = goal["id"]
    reg = _reg_of(ag, goal)
    prefix = PREFIX_BY_REG.get(reg, "SO")
    return prefix + ag[2:]


def subdomain_of(ag_id: str) -> str:
    """`AG-D-01.1-002` -> `D-01.1`."""
    m = re.match(r"[A-Z]{2}-(D-\d{2}\.\d)-\d{3}$", ag_id)
    if not m:
        raise ValueError(f"malformed goal id: {ag_id!r}")
    return m.group(1)


def _reg_of(ag: str, goal: dict) -> str:
    reg = (goal.get("regulation") or "").strip()
    if reg:
        return reg
    raise ValueError(f"{ag}: goal carries no `regulation`; cannot derive the objective prefix without it")


def reg_sort_key(reg: str) -> tuple:
    return (REG_ORDER.index(reg) if reg in REG_ORDER else len(REG_ORDER), reg)


def derive_objective(repo: Path, goal: dict) -> dict:
    """One objective row."""
    ag = goal["id"]
    sd = subdomain_of(ag)
    reg = _reg_of(ag, goal)
    baseline_source = (goal.get("baseline_source") or "").strip()

    anchors = []
    if baseline_source:
        anchors = controls.goal_anchors(repo, sd, [baseline_source])

    return {
        "objective_id": objective_id(goal),
        "parent_goal": ag,
        "subdomain": sd,
        "subdomain_name": subdomain_name(repo, sd),
        "regulation": reg,
        "statement": (goal.get("goal") or "").strip(),
        "scope": SCOPE_BY_REG.get(reg, UNSET),
        "criteria": UNSET,
        "method": UNSET,
        "owner": UNSET,
        "anchors": ", ".join(anchors) if anchors else UNSET,
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


def check(rows: list[dict], run_dir: Path | None = None) -> list[str]:
    """Doc01 findings."""
    out = []

    if run_dir is not None:
        sel = load_selection(run_dir).get("selected", [])
        have = {r["subdomain"] for r in rows}
        missing = sorted({s["id"] for s in sel} - have)
        if missing:
            out.append(
                f"upstream incomplete: {len(missing)} selected sub-domain(s) "
                f"have no Phase 1 goal artifact: {', '.join(missing)}"
            )

    for r in rows:
        blob = r["statement"]
        if "```" in blob or "req_id:" in blob or "\n## " in blob or " --- ## " in blob:
            out.append(f"{r['objective_id']}: statement carries raw baseline markup (fence/req_id/heading) — extraction fault")

    for r in rows:
        want = PREFIX_BY_REG.get(r["regulation"], "SO")
        got = r["objective_id"][:2]
        if got != want:
            out.append(f"{r['objective_id']}: prefix {got} contradicts regulation {r['regulation']} (expected {want})")

    seen: dict[str, int] = {}
    for r in rows:
        seen[r["objective_id"]] = seen.get(r["objective_id"], 0) + 1
    for oid, n in sorted(seen.items()):
        if n > 1:
            out.append(f"{oid}: {n} rows share one objective id")

    have = {r["parent_goal"] for r in rows}
    for r in rows:
        if not r["parent_goal"].startswith("AG-"):
            out.append(f"{r['objective_id']}: parent {r['parent_goal']!r} is not a Phase 1 goal id (ADR-004 chain broken)")
    if run_dir is not None:
        upstream = {g["id"] for g in load_goals(run_dir)}
        for missing in sorted(upstream - have):
            out.append(f"{missing}: Phase 1 goal has no Phase 2 objective — dropped between phases")

    return out


def _other_case_intakes(repo: Path) -> list[str]:
    out: list[str] = []
    for intake in sorted((repo / "cases").glob("Case_*/01_PHASE1_CONTEXT/Doc01_INTAKE_FORM.md")):
        try:
            out.append(intake.read_text(encoding="utf-8"))
        except OSError:
            continue
    return out


def _foreign_vocab(repo: Path) -> frozenset[str]:
    shared = set()
    for p in PRINCIPLES:
        shared |= set(re.findall(r"[a-z]{5,}", p["definition"].lower()))
    vocab: set[str] = set()
    for text in _other_case_intakes(repo):
        vocab |= set(re.findall(r"[a-z]{5,}", text.lower()))
    return frozenset(vocab - shared - STOPWORDS)


_NAME_RE = re.compile(r"\b[a-z]+[A-Z][A-Za-z]*\b|\b[A-Z]{3,}\b|\b(?<![.!?]\s)[A-Z][a-z]{2,}\b")


def check_doc02(repo: Path, run_dir: Path, principles: list[dict]) -> list[str]:
    """Doc02 findings: G5 completeness, G6 technology neutrality, G7 grounding."""
    out: list[str] = []
    by_id = {p["id"]: p for p in principles}

    for pid in PRINCIPLE_IDS:
        if pid not in by_id:
            out.append(f"{pid}: Doc02 has no row for this principle")
    for pid, row in sorted(by_id.items()):
        if pid not in PRINCIPLE_IDS:
            out.append(f"{pid}: Doc02 carries an unknown principle id")

    fact_file = run_dir / "steps" / "fact_sheet.yaml"
    fact = fact_file.read_text(encoding="utf-8") if fact_file.exists() else ""
    declared = set(re.findall(r"[a-z]{5,}", fact.lower())) if fact else set()
    foreign = _foreign_vocab(repo) - declared
    for pid in PRINCIPLE_IDS:
        row = by_id.get(pid)
        if row is None:
            continue
        constraint = str(row.get("constraint", "") or "")
        if not constraint.strip() or constraint == UNSET:
            continue
        out += [
            f"{pid}: {f}"
            for f in quality.check_no_technology(
                constraint, str(row.get("method_lead", "")), str(row.get("eval_scope", ""))
            )
        ]
        names = {m.group(0).lower() for m in _NAME_RE.finditer(constraint)}
        hits = sorted(n for n in names & foreign if n not in declared)
        if hits:
            out.append(
                f"{pid}: constraint names {', '.join(hits)} — an asset of another case, absent from this run's fact sheet (ledger §4.6)"
            )

        method = str(row.get("method_lead", "") or "").strip()
        if method and method != UNSET:
            head = method.split(":")[0].split("(")[0].strip().strip("`").upper()
            if head and head not in METHOD_VOCAB:
                out.append(f"{pid}: method_lead {head!r} is outside the published vocabulary {sorted(METHOD_VOCAB)}")

    return out
