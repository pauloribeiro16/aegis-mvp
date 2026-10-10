"""aegis_pipeline.phases.phase3.schemas — the shapes Phase 3 Part 1 agrees on before anything runs.

Everything here is a decision that every later stage inherits: the matrix column
set, the verdict vocabulary, how an organizational requirement is identified, and
how identifiers are allocated. It is separated from `phase3.py` because a change
to any of these is a change to the artefact contract, and should be visible as
one file rather than scattered through the generators.
"""
from __future__ import annotations

import re

#: Marker for a cell the pipeline has no derivation rule for. Matches Phase 2's
#: convention: a blank cell is a visible seam, invented text is a lie that
#: survives to the next phase.
UNSET = "—"

#: The five verdicts of ADR-007 D4. A row carries exactly one; the matrix is a
#: pure enum, which is what R10b invariant 2 requires of a categorical field.
VERDICTS = (
    "Fully covered (anchored)",
    "Partially covered (functional leg + explicit carve-out)",
    "No functional carrier (organizational)",
    "Design guidance",
    "N/A",
)

#: Which verdicts route an objective out of the product lane. Only the second
#: kind carries substance to the organizational document.
ORGANIZATIONAL = "No functional carrier (organizational)"

#: The coverage matrix columns, in the order the case documents use them. The
#: order is load-bearing for `check_traceability.py` and for the totals table,
#: so it is declared once here rather than retyped per renderer.
MATRIX_COLUMNS = (
    "Objective",
    "Summary",
    "Functional carrier",
    "Skill",
    "State",
    "VC discharge",
    "Action / Round",
)

#: The seven analysis lenses in `baseline/skills/`. The codes are the ones the
#: corpus uses; the directory names are given so a reader can resolve one.
SKILLS = {
    "TB": "trust-boundary-analysis",
    "AS": "attack-surface-analysis",
    "LP": "least-privilege-analysis",
    "DM": "data-minimization-analysis",
    "FS": "fail-safe-defaults-analysis",
    "LE": "lifecycle-erasure-analysis",
    "V": "verifiability-analysis",
}

RE_OBJECTIVE = re.compile(r"^(PO|SO)-(D-\d{2}\.\d)-\d{3}$")
RE_ORG_ID = re.compile(r"^ORG-(D-\d{2}\.\d)-\d{3}$")
RE_CARD = re.compile(r"^R\d+\.\d+$")
RE_SUBDOMAIN = re.compile(r"^D-\d{2}\.\d$")


def subdomain_of(objective_id: str) -> str:
    """`SO-D-03.2-001` -> `D-03.2`. Raises on anything that is not an objective."""
    m = RE_OBJECTIVE.match(objective_id.strip())
    if not m:
        raise ValueError(f"not a Phase 2 objective id: {objective_id!r}")
    return m.group(2)


def domain_of(subdomain: str) -> str:
    """`D-03.2` -> `D-03`."""
    if not RE_SUBDOMAIN.match(subdomain):
        raise ValueError(f"not a sub-domain id: {subdomain!r}")
    return subdomain[:4]


def org_id(subdomain: str, seq: int) -> str:
    """Allocate `ORG-D-XX.Y-NNN`. Allocation is the pipeline's job, not the model's."""
    if not RE_SUBDOMAIN.match(subdomain):
        raise ValueError(f"not a sub-domain id: {subdomain!r}")
    return f"ORG-{subdomain}-{seq:03d}"


def anchor_set(anchor_cell: str) -> list[str]:
    """Split a published anchor cell into individual anchor ids.

    The cell is Phase 2's ninth column, read verbatim from the deliverable — the
    same surface `check_traceability.py` T6 reads, so the two cannot drift. The
    cell is backtick-wrapped as a whole (`` `PR.DS-01, PR.DS-10` ``) and the unset
    marker comes wrapped too (`` `—` ``), so the marks come off before either the
    unset test or the split.
    """
    cell = anchor_cell.strip().strip("`").strip()
    if not cell or cell == UNSET:
        return []
    out = []
    for part in re.split(r"[,;]", cell):
        # Some cells qualify an id in place — "GV.PO-01 (primary)" in Case 02.
        # The qualifier is not part of the id and would fail resolution.
        a = re.sub(r"\s*\([^)]*\)\s*$", "", part.strip().strip("`").strip()).strip()
        if a and a != UNSET:
            out.append(a)
    return out


def is_template_criterion(text: str) -> bool:
    """True when a Phase 2 Verification Criterion is the generic template.

    Measured: all 62 of Case 01's are one of two sentences with the objective's
    own name substituted. A criterion that is generic cannot be reconstructed
    against, so the discharge column must not pretend it was.
    """
    generic = (
        "Automated check or audit confirms",
        "Security verification confirms",
    )
    return any(text.strip().startswith(p) for p in generic)
