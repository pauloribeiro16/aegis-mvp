#!/usr/bin/env python3
"""llm.py — minimal Ollama HTTP client for the Phase 1 pipeline.

Talks to a local `ollama serve` on the compute node (127.0.0.1:$PORT).
Stdlib only (no pip egress on compute nodes). Every call returns the raw
JSON response so the trace can store exactly what the model produced.
"""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.request


class LLMError(RuntimeError):
    pass


class OllamaClient:
    def __init__(self, base: str, timeout_connect: int = 30, timeout_read: int = 3600):
        self.base = base.rstrip("/")
        self.timeout_connect = timeout_connect
        self.timeout_read = timeout_read

    def _request(self, path: str, payload: dict | None, timeout: int) -> bytes:
        url = f"{self.base}{path}"
        data = json.dumps(payload).encode("utf-8") if payload is not None else None
        req = urllib.request.Request(url, data=data, method="POST" if data else "GET",
                                     headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except urllib.error.HTTPError as e:
            raise LLMError(f"HTTP {e.code} from {url}: {e.read()[:500].decode('utf-8', 'replace')}") from e
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            raise LLMError(f"connection error to {url}: {e}") from e

    def tags(self) -> dict:
        return json.loads(self._request("/api/tags", None, self.timeout_connect).decode("utf-8"))

    def wait_until_up(self, retries: int = 30, delay_s: int = 10) -> bool:
        for _ in range(retries):
            try:
                self.tags()
                return True
            except LLMError:
                time.sleep(delay_s)
        return False

    def ensure_model_cached(self, model: str) -> None:
        names = [m.get("name", "") for m in self.tags().get("models", [])]
        if not any(n == model or (n.split(":")[0] == model.split(":")[0]
                                   and n.endswith(model.split(":")[-1])) for n in names):
            raise LLMError(
                f"model '{model}' not present in the local Ollama cache (available: {names[:12]}...). "
                "Compute nodes have no egress — pull it on the login node first."
            )

    def warm_up(self, model: str, num_ctx: int, retries: int = 5, timeout_s: int = 180) -> float:
        """Load the model into VRAM before the real call. Returns seconds taken."""
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": "ping"}],
            "stream": False,
            "options": {"num_ctx": num_ctx, "num_predict": 1},
        }
        start = time.time()
        last: Exception | None = None
        for _ in range(retries):
            try:
                self._request("/api/chat", payload, timeout_s)
                return time.time() - start
            except LLMError as e:
                last = e
                time.sleep(5)
        raise LLMError(f"warm-up failed after {retries} attempts: {last}")

    def chat(self, model: str, system: str, user: str, num_ctx: int,
             temperature: float = 0.2, timeout_s: int | None = None,
             num_predict: int = 8192, sampler: dict | None = None) -> dict:
        """One chat completion. Returns the full JSON response (stream=False).

        num_predict explicit: a silent default cap truncates mid-answer and the
        content arrives empty (seen on qwen3.8 with done_reason=length).

        think=false: qwen3.8 emits a `thinking` block that shares the same
        num_predict budget as the answer — a pack that fills the context could
        spend the whole budget reasoning and return content="" (job 1963648,
        seq 24: 2285 eval tokens, empty content). The pipeline has no use for
        the reasoning trace; disabling it makes num_predict mean the answer.

        sampler: seed / top_p / top_k from the run's config.json. A key set to
        None is omitted rather than sent as null, so "we did not set it" stays
        distinguishable from "we set it to the default" — the distinction the
        determinism experiment depends on (docs/experiments/PREREG_01.md)."""
        options = {"num_ctx": num_ctx, "temperature": temperature,
                   "num_predict": num_predict}
        options.update(sampler or {})
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "stream": False,
            "think": False,
            "options": options,
        }
        raw = self._request("/api/chat", payload, timeout_s or self.timeout_read)
        try:
            return json.loads(raw.decode("utf-8"))
        except json.JSONDecodeError as e:
            # a truncated body is a transport failure, not a crash: let the
            # caller's retry loop see it and record it in the trace
            raise LLMError(f"malformed JSON in response from {self.base}/api/chat "
                           f"({len(raw)} bytes): {e}") from e

    def chat_messages(self, model: str, messages: list[dict], num_ctx: int,
                      temperature: float = 0.2, timeout_s: int | None = None,
                      num_predict: int = 8192, tools: list[dict] | None = None,
                      sampler: dict | None = None) -> dict:
        """Multi-turn completion (agent loop). `messages` is any role sequence;
        when `tools` is given, Ollama may answer with message.tool_calls instead
        of content. Same truncation/JSON guards and same sampler handling as
        chat()."""
        options = {"num_ctx": num_ctx, "temperature": temperature,
                   "num_predict": num_predict}
        options.update(sampler or {})
        payload = {
            "model": model,
            "messages": messages,
            "stream": False,
            "think": False,
            "options": options,
        }
        if tools:
            payload["tools"] = tools
        raw = self._request("/api/chat", payload, timeout_s or self.timeout_read)
        try:
            return json.loads(raw.decode("utf-8"))
        except json.JSONDecodeError as e:
            raise LLMError(f"malformed JSON in response from {self.base}/api/chat "
                           f"({len(raw)} bytes): {e}") from e
