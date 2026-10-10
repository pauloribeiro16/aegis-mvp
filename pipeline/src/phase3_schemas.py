"""phase3_schemas.py — backward-compatible shim.

Re-exports all symbols from `aegis_pipeline.phases.phase3.schemas`.
"""
from __future__ import annotations

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

__all__ = [
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
]