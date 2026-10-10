#!/usr/bin/env python3
"""validate.py — Backward-compatible shim delegating to aegis_pipeline.guards.l1_validation."""

from __future__ import annotations

import sys
from pathlib import Path

_src = Path(__file__).resolve().parent
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

from aegis_pipeline.guards.l1_validation import (
    PROPERTY_LONG,
    REPO_DEFAULT,
    check,
    doc_sections,
    main,
    md_table_defects,
    md_table_rows,
    resolve_control_anchor,
    resolve_reg_source,
    validate_run,
    warn,
)

__all__ = [
    "PROPERTY_LONG",
    "REPO_DEFAULT",
    "check",
    "doc_sections",
    "main",
    "md_table_defects",
    "md_table_rows",
    "resolve_control_anchor",
    "resolve_reg_source",
    "validate_run",
    "warn",
]

if __name__ == "__main__":
    sys.exit(main())
