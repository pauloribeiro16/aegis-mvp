#!/usr/bin/env python3
"""Referential-integrity checker for the case pipeline (read-only, report-only).

Complements ``doc_lint.py``, which enforces document *hygiene* (R11/R12 + control
paths).  That lint cannot see the defect class where a requirement cites a Phase 2
objective that does not exist, a totals table that does not sum, or an Exit Gate
that certifies files which are absent.  Measured on Case_03 (2026-09-29):
``doc_lint --strict`` returned 0 findings while 23 objective IDs cited in the
delivered Doc01 resolved to nothing and 41 claimed carriers were absent from it.

Checks
------
  T1  ID resolution        every cited ``PO-/SO-/AG-/ORG-/RN/R<TC>`` resolves
                           against the case's own Phase 1/2/3 artefacts
  T2  Regulatory coherence  for every chain segment ``<law> -> <objective>``, the
                           regulation recorded for that objective in Phase 2
                           matches the cited law
  T3  Totals arithmetic     every ``| label | N |`` ledger row whose siblings share
                           a stated total; and every ``N/M covered``-style claim
                           does not exceed its own arithmetic ceiling
  T4  Gate evidence         every file cited as G1-G12 evidence exists
  T5  Driver symmetry       every driver the coverage matrix binds to a carrier is
                           cited back by that carrier; every driver without a
                           carrier carries an explicit verdict
  T7  Threat ledger         Part 2 reconciliation: every threat card reaches the
                           risk register (minus declared cross-lens merges), count
                           claims match measured files, risk-distribution claims
                           match the register, and every mitigating RN cited by a
                           card/register row is published on that row's own target
                           surface in the accepted Part 1 baseline

Scope: ``cases/Case_*/`` only — these are the artefacts that participate in the
chain.  Governance (``AGENTS.md``, ``docs/decisions/``) legitimately talks about
IDs generically and is out of scope.

Usage::

    python scripts/check_traceability.py                # human report, exit 0
    python scripts/check_traceability.py --strict       # exit 1 on any finding
    python scripts/check_traceability.py --case Case_03_OmniBank
    python scripts/check_traceability.py --report _traceability.md

Idempotent: reads the tree; writes nothing unless ``--report`` is given.
"""

from __future__ import annotations

import argparse
import io
import re
import sys
from pathlib import Path
from typing import Iterator

REPO = Path(__file__).resolve().parent.parent
CASES = REPO / "cases"

# ---------------------------------------------------------------- ID grammars

RE_OBJECTIVE = re.compile(r"\b(?:PO|SO)-D-\d\d\.\d-\d{3}\b")
RE_GOAL = re.compile(r"\bAG-D-\d\d\.\d-\d{3}\b")
RE_ORG = re.compile(r"\bORG-D-\d\d\.\d-\d{3}\b")
RE_PRINCIPLE = re.compile(r"\bPRIN-ENG-\d{2}\b")
RE_RN = re.compile(r"\bRN\d{1,3}\b")
RE_CARD = re.compile(r"(?<![A-Za-z0-9])R(\d{1,2})\.(\d{1,2})(?![0-9.])")
RE_UC = re.compile(r"\{U\.C\.\s*(\d{1,2})\.(\d{1,2})(?![0-9.])\}")
RE_SECTION = re.compile(r"^##\s+(.*)$")
HISTORY_SECTION = re.compile(r"version history|changelog|hist[oó]rico", re.IGNORECASE)

# Law tokens as they appear on the left of a chain arrow.  Ordered longest-first
# so "AI Act" wins over a bare "Act".
RE_LAW = re.compile(
    r"(?P<law>GDPR|CRA|NIS\s*2|AI\s*Act|DORA|NIS2|AI_Act)"
)
# A constraint may cite several laws jointly against a set of drivers —
#   `GDPR Art. 5(1)(f)` · `CRA Annex I (2)(f)` · `DORA Art. 9` → `PO-…-001`/`SO-…-003`
# which is legitimate.  A segment is a *run* of laws terminated by one arrow and
# one driver set; the check is set-based (every law needs a driver of its own
# regulation), never 1:1 per token.  A segment boundary is '|', '·' or '<'; a
# law with no arrow in its run governs nothing.  The driver set may be one
# backticked span (`A, B`) or several adjacent ones (`A`/`B`) — both are read.
RE_SEGMENT = re.compile(
    r"(?P<laws>(?:GDPR|CRA|NIS\s*2|AI[\s_]?Act|DORA)[^|·<]{0,70}?)+"
    r"(?:[→>]{1,2}|-->)"
    r"\s*(?P<objs>(?:`(?:PO|SO)-D-\d\d\.\d-\d{3}`[\s,/]*)+)"
)
RE_LAW_IN_RUN = re.compile(r"GDPR|CRA|NIS\s*2|AI[\s_]?Act|DORA")
RE_OBJ_IN_SET = re.compile(r"(?:PO|SO)-D-\d\d\.\d-\d{3}")

CANON_LAW = {
    "GDPR": "GDPR",
    "CRA": "CRA",
    "NIS 2": "NIS2",
    "NIS2": "NIS2",
    "AI Act": "AI_Act",
    "AI_Act": "AI_Act",
    "DORA": "DORA",
}
# Phase 2 writes the regulation column as a markdown-bold token.
RE_REG_CELL = re.compile(r"\*\*(GDPR|CRA|NIS\s*2|AI\s*Act|AI_Act|DORA)\*\*")

LEDGER_TOTAL = re.compile(r"\|\s*\**Total\w*\**\s*\|\s*\**(\d+)\**\s*\|", re.IGNORECASE)
# Only a *carried/covered* claim is bounded by the non-carrier rows.  "N/N placed"
# and "N/N objectives" describe mapping completeness, where N/N is correct and
# expected — matching those would flag every matrix in the repository.
CLAIM_N_OF_M = re.compile(
    r"\b(\d{1,4})\s*/\s*(\d{1,4})\b(?=[^0-9/]{0,40}\b(?:carried|covered)\b)", re.IGNORECASE
)

GATE_ROW = re.compile(r"^\|\s*\**G(\d{1,2})\**\s*\|(.*)$")


class Finding:
    __slots__ = ("path", "line_no", "check", "text")

    def __init__(self, path: Path, line_no: int, check: str, text: str) -> None:
        self.path, self.line_no, self.check, self.text = path, line_no, check, text


def read(path: Path) -> list[str]:
    return io.open(path, encoding="utf-8", errors="replace").read().splitlines()


def rel(path: Path) -> str:
    return path.relative_to(REPO).as_posix()


# ------------------------------------------------------------ case discovery


class Case:
    """A case's artefact inventory, loaded once."""

    def __init__(self, root: Path) -> None:
        self.root = root
        self.name = root.name
        self.p1 = self._md("01_PHASE1_CONTEXT")
        self.p2 = self._md("02_PHASE2_RULES/Doc01_Operational_Objectives.md")
        # Part 1 lives under part1_security_privacy/ (ADR-006 two-part layout); fall back to
        # the flat layout so older cases keep resolving.
        self.p3_dir = root / "03_PHASE3_SPEC"
        self.part1 = self.p3_dir / "part1_security_privacy"
        self.p1_root = self.part1 if self.part1.is_dir() else self.p3_dir
        self.p3 = self._md("03_PHASE3_SPEC/part1_security_privacy/Doc01_Requirements_Specification.md") \
            or self._md("03_PHASE3_SPEC/part1_security_privacy/Doc01_Requirements_Elicitation_and_PUC.md") \
            or self._md("03_PHASE3_SPEC/Doc01_Requirements_Specification.md") \
            or self._md("03_PHASE3_SPEC/Doc01_Requirements_Elicitation_and_PUC.md")
        self.mapping = self._rglob_one("03_PHASE3_SPEC/part1_security_privacy/synthesis_rounds/OBJECTIVE_MAPPING.md") \
            or self._rglob_one("03_PHASE3_SPEC/synthesis_rounds/OBJECTIVE_MAPPING.md")
        # ID universes.
        p1_text = self._text(self.p1)
        p2_text = self._text(self.p2)
        self.goals = set(RE_GOAL.findall(p1_text))
        self.goals = {g for g in RE_GOAL.findall(p1_text)}
        self.objectives = set(RE_OBJECTIVE.findall(p2_text))
        # Regulation of each objective, as recorded in Phase 2's table.
        self.objective_reg: dict[str, str] = {}
        if self.p2:
            for line in read(self.p2):
                m = re.match(r"\|\s*`((?:PO|SO)-D-\d\d\.\d-\d{3})`\s*\|", line)
                if not m:
                    continue
                reg = RE_REG_CELL.search(line)
                if reg:
                    self.objective_reg[m.group(1)] = CANON_LAW[reg.group(1).replace("  ", " ")]
        # Deliverable-side ID universes (Phase 3).
        self.deliverables = [p for p in self._rglob("03_PHASE3_SPEC") if self._is_deliverable(p)]
        # The ACTIVE working copies only.  Version folders (v0_/v1_/v2_) are
        # historical snapshots: they legitimately carry IDs that an earlier
        # numbering produced, so asserting against them would either raise
        # phantom findings or — worse — mask a defect in the live baseline by
        # satisfying a lookup against a stale copy.
        self.active_deliverables = [
            p for p in self.deliverables if not self._is_versioned(p) and p != self.mapping
        ]
        if not self.active_deliverables and self.p3:
            self.active_deliverables = [self.p3]
        self.active_text = "\n".join(self._text(p) for p in self.active_deliverables)
        self.cards = set(RE_CARD.findall(self.active_text))
        self.rns = set(RE_RN.findall(self.active_text))
        self.ucs = set(RE_UC.findall(self.active_text))
        self.principles = set(RE_PRINCIPLE.findall(self._text(self._rglob_one("02_PHASE2_RULES/Doc02_Secure_Design_Principles.md"))))
        self.orgs = set(RE_ORG.findall(self.active_text))

    # -- helpers
    def _md(self, relative: str) -> Path | None:
        p = self.root / relative
        if p.is_file():
            return p
        if p.is_dir():
            docs = sorted(p.glob("Doc01*.md"))
            return docs[0] if docs else None
        return None

    def _rglob(self, relative: str) -> list[Path]:
        p = self.root / relative
        if p.is_file():
            return [p]
        return sorted(p.rglob("*.md")) if p.is_dir() else []

    def _rglob_one(self, relative: str) -> Path | None:
        found = self._rglob(relative)
        return found[0] if found else None

    def _text(self, path: Path | None) -> str:
        return "\n".join(read(path)) if path and path.is_file() else ""

    @staticmethod
    def _is_versioned(path: Path) -> bool:
        parts = path.parts
        return any(p.startswith(("v0_", "v1_", "v2_", "v3_")) for p in parts)

    @staticmethod
    def _is_deliverable(path: Path) -> bool:
        parts = path.as_posix()
        if "filtered_corpus" in parts:
            return False
        return path.name.startswith(("Doc01", "Doc02", "Doc03")) or path.name == "OBJECTIVE_MAPPING.md"


def discover_cases(only: str | None) -> list[Case]:
    if not CASES.is_dir():
        return []
    roots = sorted(p for p in CASES.iterdir() if p.is_dir())
    out = []
    for root in roots:
        if only and only not in root.name:
            continue
        out.append(Case(root))
    return out


# ------------------------------------------------------------------- T1 / T2


def check_id_resolution(case: Case) -> list[Finding]:
    """T1: every objective/goal/ORG id cited in the ACTIVE deliverable must exist
    in that case's own Phase 1/2 artefacts.  Version folders are historical
    snapshots and are not asserted against."""
    findings: list[Finding] = []
    for path in case.active_deliverables:
        section = ""
        for line_no, line in enumerate(read(path), 1):
            heading = RE_SECTION.match(line)
            if heading:
                section = heading.group(1)
            # A Version History / CHANGELOG row legitimately *names* the ids it
            # corrected; that is the record of a fix, not a live citation.
            if HISTORY_SECTION.search(section):
                continue
            for oid in sorted(set(RE_OBJECTIVE.findall(line))):
                if oid not in case.objectives:
                    findings.append(
                        Finding(path, line_no, "T1 unresolved objective", f"{oid}  (absent from Phase 2)")
                    )
            for gid in sorted(set(RE_GOAL.findall(line))):
                if gid not in case.goals:
                    findings.append(
                        Finding(path, line_no, "T1 unresolved goal", f"{gid}  (absent from Phase 1)")
                    )
    return findings


def check_regulatory_coherence(case: Case) -> list[Finding]:
    """T2: the law on the left of a chain arrow must match the regulation Phase 2
    records for each objective it points at."""
    findings: list[Finding] = []
    if not case.objective_reg:
        return findings
    for path in case.active_deliverables:
        for line_no, line in enumerate(read(path), 1):
            for seg in RE_SEGMENT.finditer(line):
                laws = {
                    CANON_LAW[m.group(0).replace("  ", " ")]
                    for m in RE_LAW_IN_RUN.finditer(seg.group("laws"))
                }
                objs = set(RE_OBJ_IN_SET.findall(seg.group("objs")))
                regs = {case.objective_reg[o] for o in objs if o in case.objective_reg}
                if not objs or not regs:
                    continue
                unmatched_laws = laws - regs
                if unmatched_laws:
                    findings.append(
                        Finding(
                            path,
                            line_no,
                            "T2 law with no driver of its regulation",
                            f"{sorted(unmatched_laws)} cited but the driver set is {sorted(objs)} ({sorted(regs)})",
                        )
                    )
    return findings


# ----------------------------------------------------------------------- T3


def check_totals(case: Case) -> list[Finding]:
    """T3: a markdown totals table must sum to its own declared Total row.

    Only a single, self-contained table counts: a header row, a separator, a run of
    rows whose count column is purely numeric, and a closing Total row.  Anything
    else in the file (mixed-type tables, a "Total" word in prose) is left alone —
    a totals checker that fires on incidental shapes trains its readers to ignore it.
    """
    findings: list[Finding] = []
    for path in case._rglob("03_PHASE3_SPEC") + case._rglob("02_PHASE2_RULES"):
        lines = read(path)
        for start in range(len(lines)):
            if not re.match(r"^\s*\|[-: |]+\|\s*$", lines[start]) or start < 1:
                continue  # need a separator, and a header above it
            header = [c.strip() for c in lines[start - 1].split("|")[1:-1]]
            if len(header) < 2:
                continue
            # Collect the contiguous run of rows that follow the separator.
            run: list[tuple[int, int]] = []  # (line_no, count)
            idx = start + 1
            while idx < len(lines):
                cells = [c.strip() for c in lines[idx].split("|")[1:-1]]
                if not lines[idx].lstrip().startswith("|"):
                    break
                if len(cells) != len(header):
                    break
                m = re.fullmatch(r"\**(\d+)\**", cells[1] or "")
                if not m:
                    break
                run.append((idx + 1, int(m.group(1))))
                idx += 1
            if len(run) < 2:
                continue
            last_cells = [c.strip() for c in lines[run[-1][0] - 1].split("|")[1:-1]]
            if not LEDGER_TOTAL.search(lines[run[-1][0] - 1]):
                continue
            declared = int(re.fullmatch(r"\**(\d+)\**", last_cells[1] or "").group(1))
            body = [n for _, n in run[:-1]]
            if sum(body) != declared:
                findings.append(
                    Finding(
                        path,
                        run[-1][0],
                        "T3 totals do not sum",
                        f"declared total {declared}, column sums to {sum(body)} ({body})",
                    )
                )
    # A ratio can never exceed its denominator.
    for path in case._rglob("03_PHASE3_SPEC"):
        for line_no, line in enumerate(read(path), 1):
            for m in CLAIM_N_OF_M.finditer(line):
                if int(m.group(1)) > int(m.group(2)):
                    findings.append(
                        Finding(path, line_no, "T3 impossible ratio", m.group(0))
                    )
    return findings


def _case_noncarrier_total(case: Case) -> int | None:
    """Sum of the matrix's explicitly non-carried rows (N/A + organizational)."""
    if not case.mapping:
        return None
    total = 0
    seen = False
    for line in read(case.mapping):
        low = line.lower()
        if not line.startswith("| `"):
            continue
        if "**n/a**" in low or "no functional carrier" in low:
            total += 1
            seen = True
    return total if seen else None


def check_ratio_claims(case: Case) -> list[Finding]:
    """T3b: a 'N/M carried' claim may not exceed M minus the matrix's own
    non-carried rows — the defect where 95/100 was asserted over a 92/100 table."""
    findings: list[Finding] = []
    noncarrier = _case_noncarrier_total(case)
    if noncarrier is None:
        return findings
    ceiling_total = len(case.objectives)
    ceiling_carried = ceiling_total - noncarrier
    for path in case._rglob("03_PHASE3_SPEC"):
        for line_no, line in enumerate(read(path), 1):
            for m in CLAIM_N_OF_M.finditer(line):
                num, den = int(m.group(1)), int(m.group(2))
                if den != ceiling_total:
                    continue
                if num > ceiling_carried:
                    findings.append(
                        Finding(
                            path,
                            line_no,
                            "T3 covered count exceeds matrix arithmetic",
                            f"{num}/{den} claimed, but only {ceiling_carried}/{ceiling_total} are non-N/A/non-organizational in the matrix",
                        )
                    )
    return findings


# ----------------------------------------------------------------------- T4


def check_gate_evidence(case: Case) -> list[Finding]:
    """T4: every file path cited as G1-G6 evidence must exist.

    Evidence is cited from three different vantage points in practice — relative to
    the citing file, relative to the case's Phase 3 folder, or bare (implying the
    synthesis_rounds folder).  All three are accepted; only a token that resolves
    under none of them is a finding.
    """
    findings: list[Finding] = []
    path_token = re.compile(r"`([A-Za-z0-9_./-]+\.md)`")
    roots = [case.p3_dir, case.p1_root / "synthesis_rounds", case.p1_root / "analysis_v0_to_v1", case.p1_root / "analysis_v1_to_v2"]
    for path in case._rglob("03_PHASE3_SPEC"):
        for line_no, line in enumerate(read(path), 1):
            m = GATE_ROW.match(line)
            if not m or int(m.group(1)) > 12:
                continue
            for token in path_token.findall(line):
                if token.startswith("../") or token.startswith("./"):
                    candidates = [path.parent / token]
                else:
                    candidates = [path.parent / token] + [base / token for base in roots]
                if not any(c.resolve().exists() for c in candidates):
                    findings.append(Finding(path, line_no, "T4 gate evidence file missing", token))
    return findings


# ----------------------------------------------------------------------- T5


# Case-insensitive: the row state is lower-cased before matching, so an
# uppercase-only pattern would never fire and every row would read as "silent".
CARRIER_TOKENS = re.compile(
    r"\bRN\d{1,3}\b|\bR\d{1,2}\.\d{1,2}\b|\bchain row\b|\btransversal\b|\bcovered\b",
    re.IGNORECASE,
)
RE_MATRIX_ROW = re.compile(r"^\|\s*" + r"`((?:PO|SO)-D-\d\d\.\d-\d{3})`\s*\|")


def check_driver_symmetry(case: Case) -> list[Finding]:
    """T5: a driver the matrix binds to a carrier must actually be cited by the
    ACTIVE deliverable; a driver with no carrier must say so explicitly.

    The lookup deliberately excludes the matrix itself and the version folders —
    asserting a driver against a stale snapshot would hide a live defect.
    """
    findings: list[Finding] = []
    if not case.mapping:
        return findings
    delivered = set(RE_OBJECTIVE.findall(case.active_text))
    for line_no, line in enumerate(read(case.mapping), 1):
        m = RE_MATRIX_ROW.match(line)
        if not m:
            continue
        oid = m.group(1)
        cells = [c.strip() for c in line.split("|")[1:-1]]
        state = " ".join(cells[1:]).lower()
        # A non-coverage verdict (N/A, organizational, design guidance) means the
        # row claims no product carrier at all — even when the note column happens
        # to mention an RN ("supported by RN18 logs" on an ops row).
        non_cover = any(
            k in state for k in ("**n/a**", "no functional carrier", "design guidance")
        )
        cover_verdict = any(k in state for k in ("fully covered", "partially covered"))
        claims_carrier = (not non_cover) and bool(CARRIER_TOKENS.search(state))
        # ADR-007 D3: a carrier serving an objective *transversally* is recorded
        # as a cross-reference in the matrix, not stamped on every slice card.
        # The matrix is therefore authoritative for such rows and no card
        # citation is required.
        transversal = "transversal" in cells[2].lower() if len(cells) > 2 else False
        if transversal:
            continue
        if claims_carrier and oid not in delivered:
            findings.append(
                Finding(
                    case.mapping,
                    line_no,
                    "T5 claimed carrier does not cite the driver",
                    f"{oid} declared covered here but cited by no active deliverable",
                )
            )
        elif not claims_carrier and not cover_verdict and not non_cover:
            findings.append(
                Finding(case.mapping, line_no, "T5 driver with neither carrier nor verdict", oid)
            )
    return findings


# ----------------------------------------------------------------------- T6

# The anchor list follows the driver set (`→ PRIN-ENG-01 → CSF ...`), so it sits
# *after* the segment match and must be read from the line, not from the match.
# PF ids (`PR.DS-P1`) ride the same published sets as CSF since the anchor
# column carries both axes (R8 — PF accompanies GDPR-derived obligations).
RE_ANCHOR_RUN = re.compile(r"CSF\s+((?:[A-Z]{2}\.[A-Z]{2}-(?:\d{2}|P\d+)(?:\s*,\s*)?)+)")
RE_ANCHOR_ID = re.compile(r"\b[A-Z]{2}\.[A-Z]{2}-(?:\d{2}|P\d+)\b")
RE_ANCHOR_PF = re.compile(r"^([A-Z]{2}\.[A-Z]{2}-P\d+)$")


def check_anchor_provenance(case: Case) -> list[Finding]:
    """T6: every control anchor a chain selects must belong to the published
    anchor set of an objective that chain cites (R2 / ADR-005 Step 4). An
    out-of-set anchor is a derivation defect, not a wording preference."""
    findings: list[Finding] = []
    published: dict[str, set[str]] = {}
    for line in read(case.p2):
        m = RE_MATRIX_ROW.match(line)
        if not m:
            continue
        cells = [c.strip() for c in line.split("|")[1:-1]]
        if len(cells) >= 9:
            published[m.group(1)] = set(RE_ANCHOR_ID.findall(cells[8]))
    if not published:
        return findings
    for path in case.active_deliverables:
        for line_no, line in enumerate(read(path), 1):
            # A cell packs several constraints separated by <br>; each carries its
            # own driver set AND its own anchor run. Scope both to one constraint,
            # or a later constraint's anchors are charged to an earlier chain.
            for piece in line.split("<br>"):
              # Only the LAST segment of a constraint owns the anchor run: earlier
              # segments' tails run into the following segments' drivers, which
              # would charge one chain's anchors to another.
              segs = list(RE_SEGMENT.finditer(piece))
              for seg in segs[-1:]:
                # The anchor run belongs to the WHOLE constraint, not to the last
                # regulation leg: a multi-regulation chain carries one driver per
                # regulation inside one <br>-piece, and R2 is satisfied when an
                # anchor belongs to the published set of ANY driver that piece
                # cites. Scoping to the last leg would charge a GDPR leg's anchor
                # to the CRA/NIS 2 leg that happens to close the chain.
                objs = {o for s in segs for o in RE_OBJ_IN_SET.findall(s.group("objs"))}
                if not objs:
                    continue
                tail = piece[seg.end():]  # the anchor run starts past the drivers
                am = RE_ANCHOR_RUN.search(tail)
                if not am:
                    continue
                allowed: set[str] = set()
                for o in objs:
                    allowed |= published.get(o, set())
                if not allowed:
                    continue  # drivers publish no set — recorded, not checkable
                for anchor in sorted(set(RE_ANCHOR_ID.findall(am.group(1))) - allowed):
                    findings.append(
                        Finding(
                            path,
                            line_no,
                            "T6 anchor outside the cited drivers' published set",
                            f"{anchor} not published by any of {sorted(objs)}",
                        )
                    )
    return findings


# ----------------------------------------------------------------------- T7

# The Part 2 dossiers are invisible to T1-T6 (which scan only Doc01/Doc02/Doc03/
# OBJECTIVE_MAPPING deliverables), so a threat dossier written against a phantom
# baseline — wrong RN numbering, UC ids that no longer exist, cards that silently
# vanish between dossier and register — passes every gate.  T7 reconciles the
# Part 2 corpus against itself and against the accepted Part 1 baseline.

RE_TM_ID = re.compile(r"TM-D-\d\d\.\d-\d{3}")
RE_TM_CARD = re.compile(r"^#{4}\s+((?:TM|AT)-D-?\S*)")  # card heading, id first token
RE_TM_CARD_STRICT = re.compile(r"^####\s+(TM-D-\d\d\.\d-\d{3})\s*:")
RE_REGISTER_ROW = re.compile(r"^\|\s*\d{1,3}\s*\|\s*`?(TM-D-\d\d\.\d-\d{3})`?\s*\|")
RE_HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
RE_CARD5 = re.compile(r"^#####\s+R(\d{1,2})\.(\d{1,2})\b")
RE_UC4 = re.compile(r"^#{4,5}\s+\{U\.C\.\s*(\d{1,2})\.(\d{1,2})(?:\.(\d{1,2}))?\}")
RE_TABLE1_ROW = re.compile(r"^\|\s*\**R(\d{1,2})\.(\d{1,2})\**\s*\|\s*\**PUC")
RE_TABLE7_ROW = re.compile(r"^\|\s*\**(RN\d{1,3})\**\s*\|")
RE_NFR_TOKEN = re.compile(r"NFR-(RN\d{1,3})\b")
RE_BACKTICK = re.compile(r"`([^`]+)`")
RE_RN_IN_SPAN = re.compile(r"(?:NFR-)?RN\d{1,3}")
RE_BARE_RN = re.compile(r"\bRN\d{1,3}\b")
RE_RN_RANGE = re.compile(r"RN\d{1,3}\s*[-–]\s*RN?\d{0,3}")
RE_KPI_COUNTS = re.compile(r"(\d{1,3})\s+threats?\s*\(\s*(\d{1,3})\s*STRIDE\s*\+\s*(\d{1,3})\s*LINDDUN\s*\)", re.IGNORECASE)
RE_THREAT_CARD_CLAIM = re.compile(r"(?<![\d.])(\d{1,3})\s+(?:exhaustive\s+|standardized\s+|technical\s+|privacy\s+)*threat cards\b", re.IGNORECASE)
RE_IDENTIFIED_N = re.compile(r"\b(\d{1,3})\s*/\s*(\d{1,3})\s+identified threats\b", re.IGNORECASE)
RE_ALL_CRITICAL = re.compile(r"All\s+(\d{1,3})\s+Critical\s+inherent", re.IGNORECASE)
RE_PRIVACY_DIST = re.compile(r"All\s+(\d{1,3})\s+Critical\s+inherent\s+privacy\s+risks\s+and\s+(\d{1,3})\s+High\s+inherent", re.IGNORECASE)
RE_KPI_LEVEL_ROW = re.compile(
    r"^\|\s*\**(?P<band>Critical|High|Medium|Low)\s+Risk\s+Threats[^|]*\**\s*\|\s*\**(?P<inh>\d{1,3})\s+threats?[^|]*\**\s*\|\s*\**(?P<res>\d{1,3})\s+threats?", re.IGNORECASE
)

BAND_TOKENS = (("crit", "Crit"), ("🔴", "Crit"), ("alto", "High"), ("🟠", "High"),
               ("méd", "Med"), ("🟡", "Med"), ("baixo", "Low"), ("🟢", "Low"),
               ("critical", "Crit"), ("high", "High"), ("medium", "Med"), ("low", "Low"))


def _risk_band(cell: str) -> str | None:
    low = cell.lower()
    for token, band in BAND_TOKENS:
        if token in low:
            return band
    return None


def _rn_ids_in_text(text: str) -> set[str]:
    """RN ids inside backticked spans only; whole-span ranges (`RN1`–`RN30`) skipped."""
    out: set[str] = set()
    for span in RE_BACKTICK.findall(text):
        if RE_RN_RANGE.search(span):
            continue
        for m in RE_RN_IN_SPAN.finditer(span):
            out.add(m.group(0).replace("NFR-", ""))
    return out


def _accepted_baseline(case: Case) -> tuple[Path | None, Path | None]:
    """The accepted (active) Doc01/Doc02: top-level copies first, then the v2 folder."""
    p1 = case.part1
    doc01 = p1 / "Doc01_Requirements_Specification.md"
    if not doc01.is_file():
        doc01 = p1 / "Doc01_Requirements_Elicitation_and_PUC.md"
    doc02 = p1 / "Doc02_System_Use_Cases.md"
    v2 = p1 / "v2_security_privacy_synthesis"
    if not doc01.is_file():
        doc01 = v2 / "Doc01_Requirements_Specification.md"
        if not doc01.is_file():
            doc01 = v2 / "Doc01_Requirements_Elicitation_and_PUC.md"
    if not doc02.is_file():
        doc02 = v2 / "Doc02_System_Use_Cases.md"
    return (doc01 if doc01.is_file() else None, doc02 if doc02.is_file() else None)


class _Surface:
    """RN publication sets extracted from the accepted Part 1 baseline."""

    def __init__(self, case: Case) -> None:
        self.card_rns: dict[str, set[str]] = {}
        self.card_anchors: dict[str, set[str]] = {}
        self.uc_rns: dict[str, set[str]] = {}
        self.bound_rns: dict[str, set[str]] = {}
        self.table7: set[str] = set()
        self.ok = False
        doc01, doc02 = _accepted_baseline(case)
        if doc01:
            self._load_doc01(doc01)
            self.ok = True
        if doc02:
            self._load_doc02(doc02)
            self.ok = self.ok or bool(self.uc_rns or self.bound_rns)

    def _load_doc01(self, path: Path) -> None:
        current: str | None = None
        for line in read(path):
            m = RE_CARD5.match(line)
            if m:
                current = f"R{m.group(1)}.{m.group(2)}"
                self.card_rns.setdefault(current, set())
                continue
            t7 = RE_TABLE7_ROW.match(line)
            if t7:
                self.table7.add(t7.group(1))
                am = RE_ANCHOR_RUN.search(line)
                if am:
                    self.card_anchors.setdefault(t7.group(1), set()).update(RE_ANCHOR_ID.findall(am.group(1)))
                continue
            if current is None:
                continue
            if RE_HEADING.match(line):
                current = None
                continue
            rns = set(RE_NFR_TOKEN.findall(line))
            if rns:
                self.card_rns[current] |= {r.replace("NFR-", "") for r in rns}
                # per-constraint anchor run: everything after the LAST NFR token
                # on the piece belongs to that constraint's chain
                for piece in line.split("<br>"):
                    toks = list(RE_NFR_TOKEN.finditer(piece))
                    if not toks:
                        continue
                    rid = toks[-1].group(1).replace("NFR-", "")
                    tail = piece[toks[-1].end():]
                    am = RE_ANCHOR_RUN.search(tail)
                    if am:
                        self.card_anchors.setdefault(rid, set()).update(RE_ANCHOR_ID.findall(am.group(1)))

    def _load_doc02(self, path: Path) -> None:
        current_uc: str | None = None
        for line in read(path):
            m = RE_UC4.match(line)
            if m:
                current_uc = f"U{m.group(1)}.{m.group(2)}"
                self.uc_rns.setdefault(current_uc, set())
                continue
            if current_uc is not None:
                h = RE_HEADING.match(line)
                if h:
                    current_uc = None
                    # Table 1 rows may follow a heading; keep scanning
                else:
                    if not RE_RN_RANGE.search(line):
                        self.uc_rns[current_uc] |= set(RE_BARE_RN.findall(line))
                    continue
            m = RE_TABLE1_ROW.match(line)
            if m:
                self.bound_rns[f"R{m.group(1)}.{m.group(2)}"] = {
                    r.replace("NFR-", "") for r in RE_NFR_TOKEN.findall(line)
                }

    def allowed_for(self, cards: set[str], ucs: set[str]) -> set[str]:
        out: set[str] = set(self.table7)
        for c in cards:
            out |= self.bound_rns.get(c, set()) | self.card_rns.get(c, set())
        for u in ucs:
            out |= self.uc_rns.get(u, set())
        return out

    def anchors_for(self, rns: set[str]) -> set[str]:
        out: set[str] = set()
        for r in rns:
            out |= self.card_anchors.get(r, set())
        return out


def _parse_threat_card(line_iter: list[tuple[int, str]], start: int) -> tuple[str, list[tuple[int, str]], int]:
    """Return (tm_id, body lines, next index) for a `#### TM-D-...` card."""
    tm_id = RE_TM_CARD_STRICT.match(line_iter[start][1]).group(1)
    body: list[tuple[int, str]] = []
    i = start + 1
    while i < len(line_iter):
        if RE_TM_CARD_STRICT.match(line_iter[i][1]) or (RE_HEADING.match(line_iter[i][1]) and not RE_TM_CARD_STRICT.match(line_iter[i][1]) and len(RE_HEADING.match(line_iter[i][1]).group(1)) <= 4):
            break
        body.append(line_iter[i])
        i += 1
    return tm_id, body, i


def _targets_of(body: list[tuple[int, str]]) -> tuple[set[str], set[str]]:
    text = "\n".join(l for _, l in body)
    cards = {f"R{a}.{b}" for a, b in re.findall(r"\bR(\d{1,2})\.(\d{1,2})\b", text) if not re.match(r"^0", a)}
    ucs = {f"U{a}.{b}" for a, b in re.findall(r"\{U\.C\.\s*(\d{1,2})\.(\d{1,2})(?![0-9.])\}", text)}
    return cards, ucs


def check_threat_ledger(case: Case) -> list[Finding]:
    """T7: Part 2 threat-dossier reconciliation (see module docstring)."""
    findings: list[Finding] = []
    p2 = case.p3_dir / "part2_threat_risk"
    if not p2.is_dir():
        return findings
    files = {p.name: p for p in sorted(p2.glob("*.md"))}
    f02, f03, f05 = files.get("02_TECHNICAL_THREATS_STRIDE.md"), files.get("03_PRIVACY_THREATS_LINDDUN.md"), files.get("05_RISK_REGISTER_AND_GOVERNANCE.md")
    if not (f02 and f05):
        return findings  # Part 2 not launched (stub README only)

    surface = _Surface(case)

    def cards_of(path: Path) -> list[tuple[str, int, list[tuple[int, str]]]]:
        lines = read(path)
        out = []
        i = 0
        numbered = list(enumerate(lines, 1))
        idx = 0
        while idx < len(numbered):
            if RE_TM_CARD_STRICT.match(numbered[idx][1]):
                tm_id, body, nxt = _parse_threat_card(numbered, idx)
                out.append((tm_id, numbered[idx][0], body))
                idx = nxt
            else:
                idx += 1
        return out

    stride_cards = cards_of(f02) if f02 else []
    linddun_cards = cards_of(f03) if f03 else []
    all_cards = stride_cards + linddun_cards

    # Register rows: header-indexed so schema changes (extra columns) survive.
    reg_rows: list[tuple[int, dict[str, str]]] = []
    reg_header: list[str] = []
    for line_no, line in enumerate(read(f05), 1):
        if line.startswith("|") and "Threat ID" in line and not reg_header:
            reg_header = [c.strip() for c in line.split("|")[1:-1]]
            continue
        m = RE_REGISTER_ROW.match(line)
        if m and reg_header:
            cells = [c.strip() for c in line.split("|")[1:-1]]
            if len(cells) == len(reg_header):
                row = dict(zip(reg_header, cells))
                row["_tm"] = m.group(1)
                reg_rows.append((line_no, row))

    def col(row: dict[str, str], *patterns: str) -> str:
        for name, val in row.items():
            if name == "_tm":
                continue
            if all(re.search(p, name, re.IGNORECASE) for p in patterns):
                return val
        return ""

    # Declared cross-lens merges (05_, any heading mentioning a merge).
    merged: set[str] = set()
    in_merge = False
    for line_no, line in enumerate(read(f05), 1):
        h = RE_HEADING.match(line)
        if h:
            in_merge = bool(re.search(r"merge", h.group(2), re.IGNORECASE))
            continue
        if in_merge:
            merged |= set(RE_TM_ID.findall(line))

    # -- T7a: card <-> register bidirectional coverage
    card_ids = [tid for tid, _, _ in all_cards]
    reg_ids = [row["_tm"] for _, row in reg_rows]
    carried = set(card_ids) - merged
    for tid, ln, _ in all_cards:
        if tid not in reg_ids and tid not in merged:
            findings.append(Finding(f02 if tid in {c for c, _, _ in stride_cards} else f03, ln, "T7a threat card absent from register", tid))
    for ln, row in reg_rows:
        if row["_tm"] not in card_ids:
            findings.append(Finding(f05, ln, "T7a register row has no threat card", row["_tm"]))

    # -- T7d: duplicate card ids without a declared merge
    seen: dict[str, int] = {}
    for path, lst in ((f02, stride_cards), (f03, linddun_cards)):
        for tid, ln, _ in lst:
            if tid in seen and tid not in merged:
                findings.append(Finding(path, ln, "T7d duplicate threat id without declared merge", tid))
            seen[tid] = ln

    # -- T7b: count claims vs measured files
    n_stride, n_lind = len(stride_cards), len(linddun_cards)
    n_reg = len(reg_rows)
    n_expect = n_stride + n_lind - len(merged & set(card_ids))
    for path in files.values():
        for line_no, line in enumerate(read(path), 1):
            for m in RE_KPI_COUNTS.finditer(line):
                total, x, y = (int(g) for g in m.groups())
                if x != n_stride or y != n_lind:
                    findings.append(Finding(path, line_no, "T7b STRIDE/LINDDUN count claim vs files", f"claimed {x} STRIDE + {y} LINDDUN, files hold {n_stride} + {n_lind}"))
                if total != n_expect:
                    findings.append(Finding(path, line_no, "T7b total threats claim vs cards-merges", f"claimed {total}, cards {n_stride}+{n_lind} minus {len(merged & set(card_ids))} merge(s) = {n_expect}"))
            for m in RE_THREAT_CARD_CLAIM.finditer(line):
                claimed = int(m.group(1))
                local = n_stride if "STRIDE" in path.name or "02_" in path.name else n_lind if "03_" in path.name else None
                if local is not None and claimed != local:
                    findings.append(Finding(path, line_no, "T7b threat-card count claim vs file", f"claimed {claimed}, file holds {local}"))
            for m in RE_IDENTIFIED_N.finditer(line):
                if int(m.group(2)) != n_reg or int(m.group(1)) != n_reg:
                    findings.append(Finding(path, line_no, "T7b identified-threats ratio vs register rows", m.group(0)))

    # -- T7c: risk-distribution claims
    dist_inh: dict[str, int] = {"Crit": 0, "High": 0, "Med": 0, "Low": 0}
    dist_res: dict[str, int] = {"Crit": 0, "High": 0, "Med": 0, "Low": 0}
    for _, row in reg_rows:
        b = _risk_band(col(row, r"inh", r"risk"))
        if b:
            dist_inh[b] += 1
        b = _risk_band(col(row, r"res", r"risk"))
        if b:
            dist_res[b] += 1
    for path in files.values():
        for line_no, line in enumerate(read(path), 1):
            m = RE_KPI_LEVEL_ROW.match(line)
            if m:
                band = {"Critical": "Crit", "High": "High", "Medium": "Med", "Low": "Low"}[m.group("band").capitalize()]
                if int(m.group("inh")) != dist_inh.get(band):
                    findings.append(Finding(path, line_no, "T7c KPI inherent distribution vs register", f"{band}: claimed {m.group('inh')}, register holds {dist_inh.get(band)}"))
                if int(m.group("res")) != dist_res.get(band):
                    findings.append(Finding(path, line_no, "T7c KPI residual distribution vs register", f"{band}: claimed {m.group('res')}, register holds {dist_res.get(band)}"))
            m = RE_ALL_CRITICAL.search(line)
            if m and path == f02:
                matrix_crit = _matrix_band_count(f02, "Crit")
                if int(m.group(1)) != matrix_crit:
                    findings.append(Finding(path, line_no, "T7c Critical-inherent claim vs summary matrix", f"claimed {m.group(1)}, matrix holds {matrix_crit}"))
            m = RE_PRIVACY_DIST.search(line)
            if m and path == f03:
                crit, high = _matrix_band_count(f03, "Crit"), _matrix_band_count(f03, "High")
                if int(m.group(1)) != crit or int(m.group(2)) != high:
                    findings.append(Finding(path, line_no, "T7c privacy distribution claim vs summary matrix", f"claimed {m.group(1)} Crit / {m.group(2)} High, matrix holds {crit} / {high}"))

    # -- T7e: mitigating RNs must be published on the row's own target surface
    if surface.ok:
        for path, lst in ((f02, stride_cards), (f03, linddun_cards)):
            for tid, ln, body in lst:
                cards, ucs = _targets_of(body)
                if not cards and not ucs:
                    continue
                cited = _rn_ids_in_text("\n".join(l for _, l in body))
                allowed = surface.allowed_for(cards, ucs)
                for rn in sorted(cited - allowed):
                    findings.append(Finding(path, ln, "T7e mitigating RN not published on target surface", f"{tid} cites {rn}; not bound to {sorted(cards) or '—'} / {sorted(ucs) or '—'} in the accepted baseline"))
        for ln, row in reg_rows:
            cards = {f"R{a}.{b}" for a, b in re.findall(r"\bR(\d{1,2})\.(\d{1,2})\b", col(row, r"cards", r"ucs") + " " + col(row, r"threat title"))}
            ucs = {f"U{a}.{b}" for a, b in re.findall(r"\{U\.C\.\s*(\d{1,2})\.(\d{1,2})\}", col(row, r"cards", r"ucs"))}
            if not cards and not ucs:
                continue
            cited = _rn_ids_in_text(col(row, r"mitigat"))
            allowed = surface.allowed_for(cards, ucs)
            for rn in sorted(cited - allowed):
                findings.append(Finding(f05, ln, "T7e register RN not published on target surface", f"{row['_tm']} cites {rn}; not bound to {sorted(cards) or '—'} / {sorted(ucs) or '—'} in the accepted baseline"))
        # -- T7f: register CSF anchors ⊆ union of the cited RNs' published anchors
        for ln, row in reg_rows:
            anchor_cell = col(row, r"CSF")
            if not anchor_cell or anchor_cell.strip() in {"—", "-"}:
                continue
            rns = _rn_ids_in_text(col(row, r"mitigat"))
            allowed = surface.anchors_for(rns)
            if not allowed:
                continue
            for anchor in sorted(set(RE_ANCHOR_ID.findall(anchor_cell)) - allowed):
                findings.append(Finding(f05, ln, "T7f register anchor outside cited RNs' published set", f"{anchor} not published for {sorted(rns)}"))
    return findings


def _matrix_band_count(path: Path, band: str) -> int:
    """Count summary-matrix rows whose Inherent Risk column carries `band`."""
    lines = read(path)
    header: list[str] = []
    idx_inh = -1
    count = 0
    for line in lines:
        if line.startswith("|") and "Threat ID" in line:
            header = [c.strip() for c in line.split("|")[1:-1]]
            idx_inh = next((i for i, h in enumerate(header) if re.search(r"inh", h, re.IGNORECASE) and re.search(r"risk", h, re.IGNORECASE)), -1)
            continue
        if idx_inh < 0 or not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.split("|")[1:-1]]
        if len(cells) != len(header) or not RE_TM_ID.search(cells[0]):
            continue
        if _risk_band(cells[idx_inh]) == band:
            count += 1
    return count


# ---------------------------------------------------------------------- main


CHECKS = {
    "T1": ("ID resolution", check_id_resolution),
    "T2": ("Regulatory coherence", check_regulatory_coherence),
    "T3": ("Totals arithmetic", check_totals),
    "T3b": ("Ratio ceiling", check_ratio_claims),
    "T4": ("Gate evidence", check_gate_evidence),
    "T5": ("Driver symmetry", check_driver_symmetry),
    "T6": ("Anchor provenance", check_anchor_provenance),
    "T7": ("Threat ledger reconciliation", check_threat_ledger),
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--strict", action="store_true", help="exit 1 on any finding")
    parser.add_argument("--case", help="restrict to one case directory name")
    parser.add_argument("--report", type=Path, help="write findings to this markdown ledger")
    args = parser.parse_args()

    findings: list[Finding] = []
    cases = discover_cases(args.case)
    if not cases:
        print("no cases found under cases/")
        return 0

    for case in cases:
        print(f"\n=== {case.name} ===")
        print(
            f"    universe: {len(case.objectives)} objectives (Phase 2) · "
            f"{len(case.goals)} goals (Phase 1) · {len(case.cards)} cards · "
            f"{len(case.rns)} RNs · {len(case.ucs)} UCs · {len(case.orgs)} ORG"
        )
        for key, (_label, fn) in CHECKS.items():
            results = fn(case)
            findings.extend(results)
            flag = "OK " if not results else "FAIL"
            print(f"    [{flag}] {key} {_label}: {len(results)} finding(s)")
    findings.sort(key=lambda f: (str(f.path), f.line_no))

    if findings:
        print("\n--- findings ---")
    for finding in findings:
        text = finding.text if len(finding.text) <= 130 else finding.text[:127] + "..."
        print(f"{rel(finding.path)}:{finding.line_no}: [{finding.check}] {text}")
    print(f"\n{len(findings)} findings across {len(cases)} case(s)")

    if args.report:
        rows = "\n".join(
            f"| `{rel(f.path)}:{f.line_no}` | {f.check} | `{f.text.strip()[:100]}` |"
            for f in findings
        ) or "| — | — | — |"
        args.report.write_text(
            "# Referential-integrity report\n\n"
            f"Findings: {len(findings)} across {len(cases)} case(s).\n\n"
            "| Location | Check | Detail |\n|---|---|---|\n" + rows + "\n",
            encoding="utf-8",
        )
        print(f"report written: {args.report}")
    return 1 if args.strict and findings else 0


if __name__ == "__main__":
    sys.exit(main())
