"""phase3.py — backward-compatible shim.

Re-exports all symbols from `aegis_pipeline.phases.phase3`.
"""
from __future__ import annotations

import sys
from pathlib import Path

# Ensure src root is in sys.path
_src = Path(__file__).resolve().parent
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

from aegis_pipeline.phases.phase3 import (
    COL_ANCHORS,
    COL_CRITERIA,
    COL_ID,
    COL_METHOD,
    COL_OWNER,
    COL_PARENT,
    COL_REG,
    COL_SCOPE,
    COL_STATEMENT,
    MATRIX_COLUMNS,
    ORGANIZATIONAL,
    PRINCIPLES,
    RE_CARD,
    RE_OBJECTIVE,
    RE_ORG_ID,
    RE_SUBDOMAIN,
    RE_TABLE_ROW,
    REPO,
    S_UNSET,
    SKILLS,
    UNFILLED,
    UNSET,
    VERDICTS,
    anchor_findings,
    anchor_set,
    apply_verdicts,
    build,
    build_verdict_pack,
    check,
    check_anchors,
    check_verdicts,
    domain_names_from,
    domain_of,
    is_template_criterion,
    load_objectives,
    load_v0_cards,
    main,
    org_id,
    parse_verdicts,
    render_matrix,
    render_principles,
    resolve_source,
    subdomain_of,
)

if __name__ == "__main__":
    sys.exit(main())
