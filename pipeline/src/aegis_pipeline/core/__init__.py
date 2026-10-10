"""aegis_pipeline.core — Core runtime foundations (configuration, tracing, LLM client)."""

from aegis_pipeline.core.config import (
    CONFIG_NAME,
    DEFAULTS,
    SAMPLER_KEYS,
    config_path,
    describe,
    load,
    sampler_options,
    write,
)
from aegis_pipeline.core.llm_client import LLMError, OllamaClient
from aegis_pipeline.core.trace import Trace, count_calls, now_iso, update_manifest

__all__ = [
    "CONFIG_NAME",
    "DEFAULTS",
    "SAMPLER_KEYS",
    "config_path",
    "describe",
    "load",
    "sampler_options",
    "write",
    "LLMError",
    "OllamaClient",
    "Trace",
    "count_calls",
    "now_iso",
    "update_manifest",
]
