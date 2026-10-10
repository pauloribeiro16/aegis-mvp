#!/usr/bin/env python3
"""phase2.py — Backward-compatible shim delegating to aegis_pipeline.phases.phase2."""

from __future__ import annotations

import sys
from pathlib import Path

# Ensure pipeline/src is importable
_src = Path(__file__).resolve().parent
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

from aegis_pipeline.phases.phase2 import (
    CATEGORIES,
    DOC01_HEADER,
    METHOD_VOCAB,
    PREFIX_BY_REG,
    PRINCIPLES,
    PRINCIPLE_IDS,
    REG_ORDER,
    SCOPE_BY_REG,
    STOPWORDS,
    UNSET,
    build,
    cell,
    check,
    check_doc02,
    derive_objective,
    grounding_ratio,
    load_goals,
    load_operationalizations,
    load_tensions,
    main,
    method_distribution,
    method_diversity_findings,
    objective_id,
    parse_p2o,
    principles_for,
    reg_sort_key,
    render_doc01,
    render_doc02,
    seam_fill,
    subdomain_of,
)
from aegis_pipeline.phases.phase2.derivation import (
    _foreign_vocab,
    _NAME_RE,
    _other_case_intakes,
    _reg_of,
)
from aegis_pipeline.phases.phase2.parsers import (
    _ops_by_slot,
    _slot_of,
)
from aegis_pipeline.phases.phase2.renderers import (
    _case_id,
    _company_name,
    _fact_sheet,
)
from aegis_pipeline.phases.phase2.runner import _confirmed

__all__ = [
    "CATEGORIES",
    "DOC01_HEADER",
    "METHOD_VOCAB",
    "PREFIX_BY_REG",
    "PRINCIPLES",
    "PRINCIPLE_IDS",
    "REG_ORDER",
    "SCOPE_BY_REG",
    "STOPWORDS",
    "UNSET",
    "build",
    "cell",
    "check",
    "check_doc02",
    "derive_objective",
    "grounding_ratio",
    "load_goals",
    "load_operationalizations",
    "load_tensions",
    "main",
    "method_distribution",
    "method_diversity_findings",
    "objective_id",
    "parse_p2o",
    "principles_for",
    "reg_sort_key",
    "render_doc01",
    "render_doc02",
    "seam_fill",
    "subdomain_of",
    "_NAME_RE",
    "_case_id",
    "_company_name",
    "_confirmed",
    "_fact_sheet",
    "_foreign_vocab",
    "_ops_by_slot",
    "_other_case_intakes",
    "_reg_of",
    "_slot_of",
]

if __name__ == "__main__":
    raise SystemExit(main())