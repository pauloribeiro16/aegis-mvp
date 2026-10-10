#!/usr/bin/env python3
"""runconfig.py — Backward-compatible shim delegating to aegis_pipeline.core.config."""

from __future__ import annotations

import sys
from pathlib import Path

# Ensure package root is in sys.path
_src = Path(__file__).resolve().parent
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

from aegis_pipeline.core.config import (
    CONFIG_NAME,
    DEFAULTS,
    SAMPLER_KEYS,
    config_path,
    describe,
    load,
    sampler_options,
    write,
)

__all__ = [
    "CONFIG_NAME",
    "DEFAULTS",
    "SAMPLER_KEYS",
    "config_path",
    "describe",
    "load",
    "sampler_options",
    "write",
]
