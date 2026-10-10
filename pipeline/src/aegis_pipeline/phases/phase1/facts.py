#!/usr/bin/env python3
"""aegis_pipeline.phases.phase1.facts — Stage P1 fact sheet extraction and validation."""

from __future__ import annotations

import sys
from pathlib import Path

# Ensure pipeline/src is importable
_src = Path(__file__).resolve().parents[3]
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

from compose import parse_simple_yaml
from aegis_pipeline.phases.phase1.common import extract_fenced

FACT_REQUIRED_FIELDS = [
    "company",
    "sector",
    "size_employees",
    "jurisdictions",
    "legal_form",
    "product_summary",
    "develops_software",
    "data_categories",
    "data_subjects",
    "hosting",
    "assumed_regulations",
    "open_questions",
]


def parse_p1(answer: str) -> dict:
    """Parse and validate stage P1 fact sheet answer."""
    yaml_text = extract_fenced(answer, "yaml")
    fact = parse_simple_yaml(yaml_text)
    missing = [k for k in FACT_REQUIRED_FIELDS if k not in fact]
    if missing:
        raise ValueError(f"fact sheet missing required fields: {missing}")
    if fact["develops_software"] not in ("true", "false", "unclear", True, False):
        raise ValueError(f"develops_software must be true|false|unclear, got {fact['develops_software']!r}")
    regs = fact.get("assumed_regulations")
    if not isinstance(regs, list) or not regs:
        raise ValueError("assumed_regulations must be a non-empty list (input §5)")
    if not isinstance(fact.get("jurisdictions"), list):
        raise ValueError("jurisdictions must be a list")
    return {"yaml_text": yaml_text, "fact": fact}
