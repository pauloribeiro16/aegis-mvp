"""aegis_pipeline.observability — Logging, metrics, and execution telemetry."""

from aegis_pipeline.observability.logging import (
    ConsoleFormatter,
    StructuredJsonFormatter,
    bind_context,
    ctx_case,
    ctx_phase,
    ctx_run_id,
    ctx_stage,
    ctx_subdomain,
    get_logger,
    setup_logging,
)
from aegis_pipeline.observability.metrics import StageMetrics

__all__ = [
    "ConsoleFormatter",
    "StructuredJsonFormatter",
    "bind_context",
    "ctx_case",
    "ctx_phase",
    "ctx_run_id",
    "ctx_stage",
    "ctx_subdomain",
    "get_logger",
    "setup_logging",
    "StageMetrics",
]
