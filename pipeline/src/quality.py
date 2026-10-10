#!/usr/bin/env python3
"""quality.py — Backward-compatible shim delegating to aegis_pipeline.guards.quality_gates."""

from __future__ import annotations

import sys
from pathlib import Path

_src = Path(__file__).resolve().parent
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

from aegis_pipeline.guards.quality_gates import (
    ADJ_PREFIXES,
    IMPLICATION_DUP_LIMIT,
    L4_TERMS,
    NEAR_VERBATIM_LIMIT,
    RETENTION_FLOOR,
    STOP,
    adjustment_kind,
    cached_ratio,
    check_adjustment_vocab,
    check_grounded,
    check_implication_specific,
    check_no_technology,
    check_obligation_retention,
    check_subso_coverage,
    max_peer_similarity,
    near_verbatim_similarity,
    norm,
    retention_ratio,
    run_all,
    run_row,
    score_row,
    score_run,
    tokens,
)

__all__ = [
    "ADJ_PREFIXES",
    "IMPLICATION_DUP_LIMIT",
    "L4_TERMS",
    "NEAR_VERBATIM_LIMIT",
    "RETENTION_FLOOR",
    "STOP",
    "adjustment_kind",
    "cached_ratio",
    "check_adjustment_vocab",
    "check_grounded",
    "check_implication_specific",
    "check_no_technology",
    "check_obligation_retention",
    "check_subso_coverage",
    "max_peer_similarity",
    "near_verbatim_similarity",
    "norm",
    "retention_ratio",
    "run_all",
    "run_row",
    "score_row",
    "score_run",
    "tokens",
]
