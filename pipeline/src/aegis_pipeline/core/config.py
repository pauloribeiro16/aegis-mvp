#!/usr/bin/env python3
"""aegis_pipeline.core.config — per-run sampler configuration and reproducibility."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

CONFIG_NAME = "config.json"

SAMPLER_KEYS = ("temperature", "seed", "top_p", "top_k")

DEFAULTS: dict[str, Any] = {
    "temperature": 0.2,
    "seed": 42,
    "top_p": None,
    "top_k": None,
    "arm": None,
    "repeat": None,
    "preapprove_gates": False,
    "case": None,
    "ficha_overrides": {},
}


def config_path(run_dir: Path) -> Path:
    return Path(run_dir) / CONFIG_NAME


def load(run_dir: Path) -> dict[str, Any]:
    """Return the run's config merged over DEFAULTS."""
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
    """Subset of config forwarded to Ollama options block."""
    return {k: cfg[k] for k in SAMPLER_KEYS if cfg.get(k) is not None}


def describe(cfg: dict[str, Any]) -> str:
    """One-line human summary for logs and stdout banner."""
    bits = [f"{k}={cfg.get(k)}" for k in SAMPLER_KEYS]
    if cfg.get("arm"):
        bits.append(f"arm={cfg['arm']}")
    if cfg.get("repeat") is not None:
        bits.append(f"repeat={cfg['repeat']}")
    return " ".join(bits)
