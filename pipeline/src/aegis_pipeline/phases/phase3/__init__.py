"""aegis_pipeline.phases.phase3 — Phase 3 Part 1: Coverage Mapping and Skeleton Package.
"""
from __future__ import annotations

from aegis_pipeline.phases.phase3.runner import (
    REPO,
    S_UNSET,
    check,
    check_anchors,
    main,
    resolve_source,
)
from aegis_pipeline.phases.phase3.schemas import (
    MATRIX_COLUMNS,
    ORGANIZATIONAL,
    RE_CARD,
    RE_OBJECTIVE,
    RE_ORG_ID,
    RE_SUBDOMAIN,
    SKILLS,
    UNSET,
    VERDICTS,
    anchor_set,
    domain_of,
    is_template_criterion,
    org_id,
    subdomain_of,
)
from aegis_pipeline.phases.phase3.skeleton import (
    COL_ANCHORS,
    COL_CRITERIA,
    COL_ID,
    COL_METHOD,
    COL_OWNER,
    COL_PARENT,
    COL_REG,
    COL_SCOPE,
    COL_STATEMENT,
    PRINCIPLES,
    build,
    domain_names_from,
    load_objectives,
    render_matrix,
    render_principles,
)
from aegis_pipeline.phases.phase3.v0_cards import load_v0_cards
from aegis_pipeline.phases.phase3.verdicts import (
    RE_TABLE_ROW,
    UNFILLED,
    anchor_findings,
    apply_verdicts,
    build_verdict_pack,
    check_verdicts,
    parse_verdicts,
)

__all__ = [
    # Schemas
    "UNSET",
    "VERDICTS",
    "ORGANIZATIONAL",
    "MATRIX_COLUMNS",
    "SKILLS",
    "RE_OBJECTIVE",
    "RE_ORG_ID",
    "RE_CARD",
    "RE_SUBDOMAIN",
    "subdomain_of",
    "domain_of",
    "org_id",
    "anchor_set",
    "is_template_criterion",
    # Skeleton
    "PRINCIPLES",
    "COL_ID",
    "COL_STATEMENT",
    "COL_PARENT",
    "COL_REG",
    "COL_SCOPE",
    "COL_CRITERIA",
    "COL_METHOD",
    "COL_OWNER",
    "COL_ANCHORS",
    "load_objectives",
    "build",
    "render_matrix",
    "render_principles",
    "domain_names_from",
    # Verdicts
    "UNFILLED",
    "RE_TABLE_ROW",
    "parse_verdicts",
    "check_verdicts",
    "anchor_findings",
    "apply_verdicts",
    "build_verdict_pack",
    # Cards
    "load_v0_cards",
    # Runner
    "REPO",
    "S_UNSET",
    "check",
    "check_anchors",
    "resolve_source",
    "main",
]
