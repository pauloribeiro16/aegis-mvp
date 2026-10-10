#!/usr/bin/env python3
"""controls.py — Backward-compatible shim delegating to aegis_pipeline.guards.controls."""

from __future__ import annotations

import sys
from pathlib import Path

_src = Path(__file__).resolve().parent
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

from aegis_pipeline.guards.controls import (
    DESC_MAX,
    PATH_ALIAS,
    REF_DIRS,
    TRACK_B_MATRIX,
    control_meta,
    goal_anchors,
    parse_overrides,
    sd_control_sections,
    sources_of,
    track_b_rows,
)

__all__ = [
    "DESC_MAX",
    "PATH_ALIAS",
    "REF_DIRS",
    "TRACK_B_MATRIX",
    "control_meta",
    "goal_anchors",
    "parse_overrides",
    "sd_control_sections",
    "sources_of",
    "track_b_rows",
]
