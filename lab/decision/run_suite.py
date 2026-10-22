#!/usr/bin/env python3
"""run_suite.py — run one arm of the d1 decision-model suite.

    python3 run_suite.py --backend http --base http://127.0.0.1:8000 \
        --cases cases_protocol.json --out results/A2_protocol.jsonl --arm A2

    python3 run_suite.py --backend inproc --checkpoint /path/to/LiquidAI_d1-3B \
        --dtype bfloat16 --cases cases_protocol.json --out results/A1_protocol.jsonl --arm A1

Output: JSONL, one record per (case, repeat). An error is a RESULT, not a
crash — the interesting divergences between the two checkpoints are exactly
the places where one raises and the other answers.

Case file format:
{
  "cases": [
    {"id": "...", "state": "...", "questions": {"n": {"type": "...", ...}},
     "expect": {"answer_type": "noul", "labels": {"n": true}},
     "expect_error": false, "repeat": 1, "tags": ["L1"]}
  ],
  "batches": [
    {"id": "robust.batch_shape", "members": ["case.a", "case.b"], "focus": "case.a"}
  ]
}
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from backends import HttpBackend, InProcBackend, warmup  # noqa: E402


def load_cases(path: Path) -> tuple[list[dict], list[dict]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return data.get("cases", []), data.get("batches", [])


def case_state(case: dict):
    """The state of a case.

    `state_template` + `state_repeat` builds a long state without carrying a
    40 k-token string in the JSON -- the ceiling cases need a state that is
    genuinely above the model's context limit, not a description of one.
    """
    if "state_template" in case:
        return case["state_template"] * int(case.get("state_repeat", 1))
    return case.get("state")


def record(arm: str, backend_name: str, model: str, dtype: str,
           case: dict, result: dict, index: int) -> dict:
    return {
        "arm": arm,
        "backend": backend_name,
        "model": model,
        "dtype": dtype,
        "case_id": case.get("id", "?"),
        "repeat": index,
        "tags": case.get("tags", []),
        "questions": case.get("questions", {}),
        "state_chars": len(str(case_state(case) or "")),
        "expect": case.get("expect", {}),
        "expect_error": case.get("expect_error"),
        "ok": result.get("ok", False),
        "answers": result.get("answers", {}),
        "usage": result.get("usage", {}),
        "error": result.get("error"),
        "latency_ms": result.get("latency_ms", 0.0),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--backend", choices=["http", "inproc"], required=True)
    ap.add_argument("--base", default="http://127.0.0.1:8000")
    ap.add_argument("--model", default=None,
                    help="served model name, sent in the request body when set")
    ap.add_argument("--checkpoint", default=None)
    ap.add_argument("--dtype", default="bfloat16",
                    choices=["float32", "float16", "bfloat16"])
    ap.add_argument("--device", default="cuda")
    ap.add_argument("--audio-capable", action="store_true",
                    help="the checkpoint takes a fourth audio argument")
    ap.add_argument("--compile", action="store_true",
                    help="torch.compile(mode='reduce-overhead') -- CUDA graphs")
    ap.add_argument("--cases", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--arm", required=True)
    ap.add_argument("--model-label", default=None)
    ap.add_argument("--no-warmup", action="store_true")
    ap.add_argument("--only", default=None,
                    help="comma-separated case ids to run (substring match ok)")
    args = ap.parse_args()

    cases, batches = load_cases(Path(args.cases))
    if args.only:
        wanted = {s.strip() for s in args.only.split(",")}
        cases = [c for c in cases if c.get("id") in wanted]
        batches = [b for b in batches if b.get("id") in wanted
                   or any(m in wanted for m in b.get("members", []))]

    if args.backend == "http":
        backend = HttpBackend(args.base, model=args.model)
        backend_name, model_label = "http", args.model_label or args.model or "served"
        dtype = "n/a"
    else:
        if not args.checkpoint:
            ap.error("--checkpoint is required for the inproc backend")
        backend = InProcBackend(args.checkpoint, dtype=args.dtype, device=args.device,
                                audio_capable=args.audio_capable, compile_model=args.compile)
        backend_name, model_label = "inproc", args.model_label or Path(args.checkpoint).name
        dtype = args.dtype

    if args.backend == "inproc":
        cfg = Path(args.checkpoint) / "config.json"
        try:
            conf = json.loads(cfg.read_text(encoding="utf-8"))
            print(f"[{args.arm}] checkpoint {args.checkpoint}\n"
                  f"         model_type={conf.get('model_type')} "
                  f"architectures={conf.get('architectures')} "
                  f"dtype={conf.get('dtype') or conf.get('torch_dtype')} "
                  f"requested_dtype={args.dtype}", flush=True)
        except (OSError, json.JSONDecodeError) as exc:
            print(f"[{args.arm}] WARNING: cannot read {cfg}: {exc}", flush=True)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if not args.no_warmup:
        w = warmup(backend)
        print(f"[warmup] ok={w['ok']} {w.get('latency_ms', 0):.1f}ms "
              f"{w.get('error') or ''}", flush=True)

    by_id = {c.get("id"): c for c in cases}
    t_start = time.perf_counter()
    n = 0
    with out_path.open("w", encoding="utf-8") as fh:
        for case in cases:
            repeats = int(case.get("repeat", 1))
            for i in range(repeats):
                result = backend.decide(case_state(case), case.get("questions", {}))
                rec = record(args.arm, backend_name, model_label, dtype, case, result, i)
                fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
                n += 1
                status = "ok" if rec["ok"] else f"ERR {rec['error']}"
                print(f"[{args.arm}] {rec['case_id']}#{i} {rec['latency_ms']:.1f}ms {status}",
                      flush=True)

        # Batches: the same cases decided together instead of one by one. The
        # d1-3B runner warns that "in bf16 the kernels differ by batch shape",
        # so the focused member's probabilities are recorded for comparison
        # against its single-call record.
        for batch in batches:
            members = [by_id[m] for m in batch.get("members", []) if m in by_id]
            focus = by_id.get(batch.get("focus"))
            if not members or focus is None:
                continue
            payload = [(case_state(m), m.get("questions", {}), None) for m in members]
            try:
                bres = backend.decide_batch(payload)
            except NotImplementedError:
                print(f"[{args.arm}] {batch['id']} SKIPPED (backend has no batch route)",
                      flush=True)
                continue
            if not bres.get("ok"):
                print(f"[{args.arm}] {batch['id']} batch error: {bres.get('error')}",
                      flush=True)
                continue
            idx = members.index(focus)
            case = dict(focus)
            case["id"] = batch["id"]
            rec = record(args.arm, backend_name, model_label, dtype, case,
                         {"ok": True, "answers": bres["answers"][idx],
                          "usage": (bres["usage"][idx] if isinstance(bres.get("usage"), list)
                                    else bres.get("usage", {})),
                          "error": None,
                          "latency_ms": bres["latency_ms"] / max(1, len(members))},
                         0)
            rec["batch_size"] = len(members)
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
            n += 1
            print(f"[{args.arm}] {batch['id']} batch of {len(members)} "
                  f"{rec['latency_ms']:.1f}ms/case", flush=True)

    elapsed = time.perf_counter() - t_start
    print(f"[{args.arm}] wrote {n} records to {out_path} in {elapsed:.1f}s "
          f"({backend.calls} model calls)", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
