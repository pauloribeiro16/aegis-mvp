#!/usr/bin/env python3
"""steps.py — Backward-compatible shim delegating to aegis_pipeline.phases.phase1."""

from __future__ import annotations

import sys
from pathlib import Path

# Ensure pipeline/src is importable
_src = Path(__file__).resolve().parent
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

from aegis_pipeline.phases.phase1 import (
    EXTRA_INSTRUCTION,
    FRAMING_DIMENSIONS,
    GOAL_COLUMNS_DOC,
    GOAL_COLUMNS_EMIT,
    NUM_CTX,
    NUM_PREDICT,
    P3_INSTRUCTION_VARIANTS,
    P4_ADJUSTMENT_BADGES,
    P4_ADJUSTMENT_MENU,
    P4_ADJUSTMENT_VARIANTS,
    P4_IMPLICATION_CONCRETE,
    P4_IMPLICATION_MARKER,
    P4_IMPLICATION_VARIANTS,
    P4_STYLE_MARKER,
    P4_STYLE_META,
    P4_STYLE_VARIANTS,
    P4T_HEADER,
    P4T_SEPARATOR,
    PARSERS,
    PATTERNS,
    PROPERTY_ALIASES,
    PROPERTY_LONG,
    StepRunner,
    _assert_wrap_instruction,
    _p4_instruction,
    assemble_doc,
    build_run_notes,
    canonical_reg,
    check_p4_quality,
    extract_fenced,
    goal_table_header,
    load_tension_slices,
    merge_tensions,
    one_reg,
    p4_extra_instruction,
    p4t_extra_instruction,
    parse_md_table,
    parse_p1,
    parse_p2,
    parse_p2d,
    parse_p2o,
    parse_p3,
    parse_p3f,
    parse_p4,
    parse_p4t,
    store_parsed,
    store_tension_slice,
)
from aegis_pipeline.phases.phase1.common import _REG_SPELLING
from aegis_pipeline.phases.phase1.assembly import _cell, _hl_goal, _run_identity

# Legacy private aliases for internal callers
_canonical_reg = canonical_reg
_one_reg = one_reg

__all__ = [
    "EXTRA_INSTRUCTION",
    "FRAMING_DIMENSIONS",
    "GOAL_COLUMNS_DOC",
    "GOAL_COLUMNS_EMIT",
    "NUM_CTX",
    "NUM_PREDICT",
    "P3_INSTRUCTION_VARIANTS",
    "P4_ADJUSTMENT_BADGES",
    "P4_ADJUSTMENT_MENU",
    "P4_ADJUSTMENT_VARIANTS",
    "P4_IMPLICATION_CONCRETE",
    "P4_IMPLICATION_MARKER",
    "P4_IMPLICATION_VARIANTS",
    "P4_STYLE_MARKER",
    "P4_STYLE_META",
    "P4_STYLE_VARIANTS",
    "P4T_HEADER",
    "P4T_SEPARATOR",
    "PARSERS",
    "PATTERNS",
    "PROPERTY_ALIASES",
    "PROPERTY_LONG",
    "StepRunner",
    "_assert_wrap_instruction",
    "_p4_instruction",
    "assemble_doc",
    "build_run_notes",
    "canonical_reg",
    "check_p4_quality",
    "extract_fenced",
    "goal_table_header",
    "load_tension_slices",
    "merge_tensions",
    "one_reg",
    "p4_extra_instruction",
    "p4t_extra_instruction",
    "parse_md_table",
    "parse_p1",
    "parse_p2",
    "parse_p2d",
    "parse_p2o",
    "parse_p3",
    "parse_p3f",
    "parse_p4",
    "parse_p4t",
    "store_parsed",
    "store_tension_slice",
    "_REG_SPELLING",
    "_cell",
    "_hl_goal",
    "_run_identity",
    "_canonical_reg",
    "_one_reg",
]
