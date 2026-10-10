#!/usr/bin/env python3
"""run_pipeline.py — Stage driver for the AEGIS-MVP Phase 1 pipeline.

Stages (each normally one SLURM job, stopped at its human gate):
  p1   extract facts                       -> steps/fact_sheet.yaml      (gate G-P1-A)
  p2   confirm regulations                 -> steps/verdicts.*           (gate G-P1-B)
  p3   select sub-domain subset            -> steps/selection.*          (gate G-P1-C)
  p3f  build the §2 framing table          -> steps/framing.md
  p4   derive adjusted goals (1 call/sub-domain; anchors code-derived)
  p4t  resolve strategic tensions          -> steps/tensions.* (multi-reg only)
  p5   zero-LLM assembly + validate        -> doc02_adjusted_goals.md, RUN_NOTES.md (gate G-P1-D)

State lives on disk (ADR-010 D5): each stage re-enters from the run
directory's recorded predecessors.
"""
from __future__ import annotations

import sys
from pathlib import Path

# Ensure src root is in sys.path
_src = Path(__file__).resolve().parent
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

from aegis_pipeline.cli import REPO_DEFAULT, cmd_new_run, cmd_run, main

__all__ = ["cmd_new_run", "cmd_run", "main", "REPO_DEFAULT"]

if __name__ == "__main__":
    try:
        sys.exit(main())
    except (SystemExit,):
        raise
    except Exception as e:
        print(f"STAGE ABORTED: {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(1)
