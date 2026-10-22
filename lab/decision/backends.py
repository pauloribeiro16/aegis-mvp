"""backends.py — two routes to the same decision-model contract.

    decide(state, questions, *, images=None, audio=None)
        -> {"ok": bool, "answers": {...}, "usage": {...}, "error": {...} | None}

HttpBackend    POST {base}/v1/systemone
               vLLM 0.32.0's LiquidStrategy (d1-3B). llama.cpp speaks the same
               contract. There is no OpenAI /v1/chat/completions for these
               models: a decision model does not write text, it returns typed
               answers, and the Decision Index is a top-level `questions` field.

InProcBackend  transformers AutoModel.from_pretrained(..., trust_remote_code=True)
               -> model.system_one(state, questions, images[, audio])
               The checkpoint's own code path: the tree-batched forward pass
               that the server reconstructs only approximately.

Both arms exist so the serving layer can be measured against the checkpoint
rather than assumed equivalent to it.

Stdlib only on the HTTP side (urllib) — the lane adds no dependency to the
project. The in-process side needs torch/transformers, which live in the
cluster venv, never in the pipeline venv.
"""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.request
from typing import Any

# The answer discriminants the Decision Index defines.
ANSWER_TYPES = ("noul", "choice", "score")

# The canonical question schema, as documented by Liquid for the decision
# models and confirmed in the checkpoints' own prompt.py:
#   noul   {type, instructions, criteria?: {true, false}}
#   choice {type, instructions, criteria: {name: description}}   (>= 2 options)
#   score  {type, instructions, criteria: [level, ...]}          (2..10 levels)


class BackendError(RuntimeError):
    """Raised only for problems the harness cannot record as a result."""


class HttpBackend:
    """The decision endpoint over HTTP (vLLM's /v1/systemone)."""

    def __init__(self, base: str, model: str | None = None, timeout: int = 900):
        self.base = base.rstrip("/")
        self.model = model
        self.timeout = timeout
        self._needs_model_field = model is not None
        self.calls = 0

    # -- transport ----------------------------------------------------------
    def _post(self, payload: dict) -> tuple[int, dict | str]:
        req = urllib.request.Request(
            f"{self.base}/v1/systemone",
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                return resp.status, json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            raw = exc.read().decode("utf-8", "replace")
            try:
                return exc.code, json.loads(raw)
            except json.JSONDecodeError:
                return exc.code, raw

    def _body(self, state: Any, questions: dict, images, audio) -> dict:
        payload: dict[str, Any] = {"state": state, "questions": questions}
        if self.model:
            payload["model"] = self.model
        if images:
            payload["images"] = list(images)
        if audio:
            payload["files"] = list(audio)
        return payload

    # -- contract -----------------------------------------------------------
    def decide(self, state: Any, questions: dict, *, images=None, audio=None) -> dict:
        payload = self._body(state, questions, images, audio)
        t0 = time.perf_counter()
        status, body = self._post(payload)
        self.calls += 1

        # One-shot repair: some OpenAI-style routes require a `model` field.
        # Detect it from the error rather than guessing up front, and remember
        # the answer for the rest of the run.
        if status >= 400 and not self._needs_model_field and self.model is None:
            text = json.dumps(body) if not isinstance(body, str) else body
            if "model" in text.lower():
                self._needs_model_field = True
                self.model = self._fallback_model_name()
                payload = self._body(state, questions, images, audio)
                t0 = time.perf_counter()
                status, body = self._post(payload)
                self.calls += 1

        latency_ms = (time.perf_counter() - t0) * 1000.0
        if status >= 400:
            return {
                "ok": False,
                "answers": {},
                "usage": {},
                "error": {"kind": "http", "status": status, "detail": body},
                "latency_ms": latency_ms,
            }
        return {
            "ok": True,
            "answers": body.get("answers", {}),
            "usage": body.get("usage", {}),
            "error": None,
            "latency_ms": latency_ms,
        }

    def _fallback_model_name(self) -> str:
        try:
            req = urllib.request.Request(f"{self.base}/v1/models")
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            ids = [m.get("id") for m in data.get("data", []) if m.get("id")]
            if ids:
                return ids[0]
        except Exception:  # noqa: BLE001
            pass
        return "d1"

    def decide_batch(self, requests: list) -> dict:
        """Not available: the decision endpoint is one request per state."""
        raise NotImplementedError("the /v1/systemone endpoint has no batch route")


class InProcBackend:
    """The checkpoint's own code path, loaded in-process with transformers."""

    def __init__(
        self,
        checkpoint: str,
        dtype: str = "bfloat16",
        device: str = "cuda",
        audio_capable: bool = False,
        compile_model: bool = False,
    ):
        import torch
        from transformers import AutoModel

        self.checkpoint = checkpoint
        self.audio_capable = audio_capable
        torch_dtype = {
            "float32": torch.float32,
            "float16": torch.float16,
            "bfloat16": torch.bfloat16,
        }[dtype]
        self.dtype = dtype

        kwargs: dict[str, Any] = {"trust_remote_code": True, "dtype": torch_dtype}
        try:
            model = AutoModel.from_pretrained(checkpoint, attn_implementation="sdpa", **kwargs)
        except (TypeError, ValueError) as exc:
            # d1-omni-600M refuses the sdpa attention implementation
            # ("D1OmniModel does not support an attention implementation
            # through torch.nn.functional.scaled_dot_product_attention"),
            # and transformers raises ValueError for that, not TypeError.
            model = AutoModel.from_pretrained(checkpoint, **kwargs)
            print(f"[backend] {checkpoint}: sdpa unavailable ({type(exc).__name__}), "
                  f"fell back to the default attention implementation")
        self.model = model.eval().to(device)
        self.device = device

        import inspect
        sig = inspect.signature(self.model.system_one)
        positional = [p for p in sig.parameters.values()
                      if p.kind in (p.POSITIONAL_ONLY, p.POSITIONAL_OR_KEYWORD)]
        accepts_audio = len(positional) >= 4
        if audio_capable and not accepts_audio:
            raise SystemExit(
                f"--audio-capable but {checkpoint} exposes system_one with "
                f"{len(positional)} positional arguments; it takes no audio. "
                f"Loading the wrong checkpoint here measures nothing.")
        if not audio_capable and accepts_audio:
            print(f"[backend] {checkpoint} takes an audio argument; "
                  f"this arm will not use it.")
        self.accepts_audio = accepts_audio

        if compile_model:
            # README: on NVIDIA this runs single questions as CUDA graphs, and
            # "the first call with a new shape pays for kernel selection".
            self.model.compile(mode="reduce-overhead")

        self.calls = 0

    def decide(self, state: Any, questions: dict, *, images=None, audio=None) -> dict:
        t0 = time.perf_counter()
        try:
            if self.audio_capable:
                result = self.model.system_one(state, questions, images, audio)
            else:
                result = self.model.system_one(state, questions, images)
        except Exception as exc:  # noqa: BLE001 -- an error IS a result here
            return {
                "ok": False,
                "answers": {},
                "usage": {},
                "error": {"kind": "exception", "type": type(exc).__name__, "detail": str(exc)},
                "latency_ms": (time.perf_counter() - t0) * 1000.0,
            }
        self.calls += 1
        return {
            "ok": True,
            "answers": result.get("answers", {}),
            "usage": result.get("usage", {}),
            "error": None,
            "latency_ms": (time.perf_counter() - t0) * 1000.0,
        }

    def decide_batch(self, requests: list) -> dict:
        """`system_one_batch`: the tree-batched forward pass.

        The d1-3B runner notes "in bf16 the kernels differ by batch shape",
        so this is where a batch-shape sensitivity effect would show up.
        """
        t0 = time.perf_counter()
        try:
            if self.audio_capable:
                results = self.model.system_one_batch(requests)
            else:
                results = self.model.system_one_batch([(s, q, i) if i is not None else (s, q)
                                                       for s, q, i in requests])
        except Exception as exc:  # noqa: BLE001
            return {
                "ok": False,
                "answers": {},
                "usage": {},
                "error": {"kind": "exception", "type": type(exc).__name__, "detail": str(exc)},
                "latency_ms": (time.perf_counter() - t0) * 1000.0,
            }
        self.calls += len(requests)
        return {
            "ok": True,
            "answers": [r.get("answers", {}) for r in results],
            "usage": [r.get("usage", {}) for r in results],
            "error": None,
            "latency_ms": (time.perf_counter() - t0) * 1000.0,
        }


def warmup(backend, questions: dict | None = None) -> dict:
    """One throwaway call so the first measured case is not paying for
    kernel selection, graph capture or lazy import."""
    questions = questions or {
        "warmup": {"type": "noul", "instructions": "Is this text non-empty?"}
    }
    result = backend.decide("A short state used only to warm the model up.", questions)
    return result
