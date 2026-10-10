#!/usr/bin/env python3
"""aegis_pipeline.observability.metrics — Pipeline execution metrics and telemetry."""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Any


@dataclass
class StageMetrics:
    stage_name: str
    start_time: float = field(default_factory=time.time)
    end_time: float | None = None
    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_calls: int = 0
    retries: int = 0
    custom_metrics: dict[str, Any] = field(default_factory=dict)

    def finish(self) -> None:
        if self.end_time is None:
            self.end_time = time.time()

    @property
    def duration_seconds(self) -> float:
        end = self.end_time if self.end_time is not None else time.time()
        return max(0.0, end - self.start_time)

    @property
    def tokens_per_second(self) -> float:
        dur = self.duration_seconds
        if dur <= 0:
            return 0.0
        return self.completion_tokens / dur

    def record_call(self, prompt_tokens: int, completion_tokens: int, retries: int = 0) -> None:
        self.prompt_tokens += prompt_tokens
        self.completion_tokens += completion_tokens
        self.total_calls += 1
        self.retries += retries

    def to_dict(self) -> dict[str, Any]:
        return {
            "stage": self.stage_name,
            "duration_s": round(self.duration_seconds, 3),
            "prompt_tokens": self.prompt_tokens,
            "completion_tokens": self.completion_tokens,
            "total_calls": self.total_calls,
            "retries": self.retries,
            "tokens_per_second": round(self.tokens_per_second, 2),
            **self.custom_metrics,
        }
