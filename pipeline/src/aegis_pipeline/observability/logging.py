#!/usr/bin/env python3
"""aegis_pipeline.observability.logging — Structured logging with contextual correlation."""

from __future__ import annotations

import contextlib
import contextvars
import json
import logging
import sys
from datetime import datetime, timezone
from typing import Any, Generator

# Context variables propagated across stages and tasks
ctx_run_id: contextvars.ContextVar[str | None] = contextvars.ContextVar("run_id", default=None)
ctx_case: contextvars.ContextVar[str | None] = contextvars.ContextVar("case", default=None)
ctx_phase: contextvars.ContextVar[str | None] = contextvars.ContextVar("phase", default=None)
ctx_stage: contextvars.ContextVar[str | None] = contextvars.ContextVar("stage", default=None)
ctx_subdomain: contextvars.ContextVar[str | None] = contextvars.ContextVar("subdomain", default=None)


@contextlib.contextmanager
def bind_context(
    run_id: str | None = None,
    case: str | None = None,
    phase: str | None = None,
    stage: str | None = None,
    subdomain: str | None = None,
) -> Generator[None, None, None]:
    """Temporarily bind contextual variables for logging correlation."""
    tokens = []
    if run_id is not None:
        tokens.append((ctx_run_id, ctx_run_id.set(run_id)))
    if case is not None:
        tokens.append((ctx_case, ctx_case.set(case)))
    if phase is not None:
        tokens.append((ctx_phase, ctx_phase.set(phase)))
    if stage is not None:
        tokens.append((ctx_stage, ctx_stage.set(stage)))
    if subdomain is not None:
        tokens.append((ctx_subdomain, ctx_subdomain.set(subdomain)))
    try:
        yield
    finally:
        for var, token in reversed(tokens):
            var.reset(token)


class StructuredJsonFormatter(logging.Formatter):
    """Outputs machine-readable single-line JSON records for cluster/file logging."""

    def format(self, record: logging.LogRecord) -> str:
        payload: dict[str, Any] = {
            "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "run_id": ctx_run_id.get(),
            "case": ctx_case.get(),
            "phase": ctx_phase.get(),
            "stage": ctx_stage.get(),
            "subdomain": ctx_subdomain.get(),
        }
        if hasattr(record, "metrics") and isinstance(record.metrics, dict):
            payload["metrics"] = record.metrics
        if record.exc_info:
            payload["exception"] = self.formatException(record.exc_info)
        return json.dumps(payload, ensure_ascii=False)


class ConsoleFormatter(logging.Formatter):
    """Clean, human-readable terminal formatter."""

    def format(self, record: logging.LogRecord) -> str:
        stage = ctx_stage.get()
        sub = ctx_subdomain.get()
        prefix = f"[{stage}]" if stage else "[aegis]"
        if sub:
            prefix += f"[{sub}]"
        lvl = f"[{record.levelname}]" if record.levelno != logging.INFO else ""
        parts = [p for p in (prefix, lvl, record.getMessage()) if p]
        out = " ".join(parts)
        if record.exc_info:
            out += "\n" + self.formatException(record.exc_info)
        return out


def setup_logging(json_mode: bool = False, level: int = logging.INFO) -> None:
    """Configure the root logger with either JSON or console formatting."""
    root = logging.getLogger("aegis")
    root.setLevel(level)
    root.handlers.clear()

    handler = logging.StreamHandler(sys.stderr)
    handler.setLevel(level)
    if json_mode:
        handler.setFormatter(StructuredJsonFormatter())
    else:
        handler.setFormatter(ConsoleFormatter())
    root.addHandler(handler)


def get_logger(name: str) -> logging.Logger:
    """Return a namespaced logger under the 'aegis' hierarchy."""
    if name.startswith("aegis."):
        return logging.getLogger(name)
    return logging.getLogger(f"aegis.{name}")
