#!/usr/bin/env python3
"""llm.py — Backward-compatible shim delegating to aegis_pipeline.core.llm_client."""

from __future__ import annotations

import sys
from pathlib import Path

# Ensure package root is in sys.path
_src = Path(__file__).resolve().parent
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

from aegis_pipeline.core.llm_client import LLMError, OllamaClient

__all__ = [
    "LLMError",
    "OllamaClient",
]
