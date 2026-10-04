#!/usr/bin/env python3
"""Per-run sampler configuration (the reproducibility carrier).

Before this module a run's sampling configuration lived in three places at
once: the literal ``0.2`` written into every trace record, the default argument
of ``llm.chat``, and nothing at all for seed. Those agree today only by
coincidence — changing the call site without the record would make the trace
lie about what the model received.

``config.json`` in the run directory is now the single declaration, written by
``run_pipeline.py new-run`` and read by both the pipeline and agent arms. It is
echoed into ``manifest.json`` so the run survives ``sync_down`` and remains
self-describing: every number needed to reproduce or refute it travels with
the artefacts.

Stdlib only (no pip egress on compute nodes), like the rest of pipeline/src.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

CONFIG_NAME = "config.json"

#: Sampler keys forwarded to the Ollama ``options`` block. ``None`` means
#: "do not send" — which is NOT the same as sending a default, because Ollama's
#: documented defaults have contradicted each other across its own docs
#: (see docs/research/01_PIPELINE_PATTERNS.md PP-012). An unsent key is a
#: recorded fact; an inherited default is not.
SAMPLER_KEYS = ("temperature", "seed", "top_p", "top_k")

DEFAULTS: dict[str, Any] = {
    # SEEDED BY DEFAULT — measured, not assumed. EXP-02 (2026-10-03/04, 45
    # runs) established that with a fixed seed the whole pipeline is
    # bit-reproducible: the 15 seeded runs produced byte-identical goal sets
    # (retention sd = 0.0000; assembled deliverables differing only in the run
    # id), and the pipeline's entire run-to-run variance is sampling-driven —
    # zero residual from the serving layer, contrary to the vendor's own
    # nondeterminism warning. Unseeded runs also ABORT at ~40% on the R6
    # grounding gate, which seeded runs never trip. Seeding is therefore a
    # correctness property for an unattended pipeline, not a nicety.
    #
    # Running UNSEEDED now requires saying so explicitly (--seed none); the
    # "unset means whatever the server defaults to" state is no longer
    # reachable by omission. Temperature stays at 0.2: EXP-02 showed greedy
    # (0.0) adds no determinism once the seed is fixed and costs a little
    # retention (0.7159 vs 0.7171), so lowering it buys nothing.
    "temperature": 0.2,
    "seed": 42,
    "top_p": None,
    "top_k": None,
    # experimental bookkeeping: an arm label and repeat index let the aggregator
    # group runs without parsing run-id strings, and let the pre-registration
    # state the design in the same file the runs carry
    "arm": None,
    "repeat": None,
    "preapprove_gates": False,
    # control factors held fixed across an experiment; recorded, not enforced
    "case": None,
    "ficha_overrides": {},
}


def config_path(run_dir: Path) -> Path:
    return Path(run_dir) / CONFIG_NAME


def load(run_dir: Path) -> dict[str, Any]:
    """Return the run's config merged over DEFAULTS.

    A missing config.json is not an error: a run created before this module
    still has to be readable, and its missing config is itself evidence (the
    run predates per-run configuration and cannot be reproduced by construction).
    """
    cfg = dict(DEFAULTS)
    path = config_path(run_dir)
    if path.is_file():
        try:
            stored = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return cfg
        if isinstance(stored, dict):
            cfg.update(stored)
    return cfg


def write(run_dir: Path, cfg: dict[str, Any]) -> Path:
    path = config_path(run_dir)
    path.write_text(json.dumps(cfg, indent=1, sort_keys=True, ensure_ascii=False),
                    encoding="utf-8")
    return path


def sampler_options(cfg: dict[str, Any]) -> dict[str, Any]:
    """The subset of the config that goes into the Ollama ``options`` block.

    Keys set to None are dropped rather than sent as null: Ollama rejects a
    null in the options block, and sending an explicit default would silently
    turn "we did not set this" into "we set this".
    """
    return {k: cfg[k] for k in SAMPLER_KEYS if cfg.get(k) is not None}


def describe(cfg: dict[str, Any]) -> str:
    """One-line human summary for logs and the run's stdout banner."""
    bits = [f"{k}={cfg.get(k)}" for k in SAMPLER_KEYS]
    if cfg.get("arm"):
        bits.append(f"arm={cfg['arm']}")
    if cfg.get("repeat") is not None:
        bits.append(f"repeat={cfg['repeat']}")
    return " ".join(bits)
