#!/usr/bin/env python3
"""preflight.py — exercise the whole lane with no model and no GPU.

A stub implements the decision endpoint's contract exactly as the server does
(it is the same code path the vLLM route takes), so this exercises:
  run_suite.py -> the HTTP client -> the JSONL record shape
  check_suite.py -> the contract invariants and the accuracy scoring
  report.py -> the pairwise and contrast comparisons

and then asserts on the result. It also feeds check_suite a deliberately
malformed record, because a checker that only ever sees well-formed input
is not a checker.

    python3 preflight.py        # exits 0 iff every guarantee holds

This is the Stage 0 gate: it runs on the workstation, before any cluster
time is spent.
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from check_suite import check_contract, load, pick, summarise  # noqa: E402

# The stub's answers, keyed by a phrase in the instructions.
def answer_for(qtype: str, instructions: str) -> dict:
    low = instructions.lower()
    if qtype == "noul":
        yes = 0.9 if "gdpr" in low else 0.1
        return {"type": "noul", "noul": yes}
    if qtype == "choice":
        # First criterion wins, except where the label demands otherwise.
        return {"type": "choice", "choice": "PENDING"}
    return {"type": "score", "score": 2.0, "confidence": 0.6,
            "probabilities": {"0": 0.1, "1": 0.3, "2": 0.6},
            "legend": {"0": "low", "1": "mid", "2": "high"}}


class StubHandler(BaseHTTPRequestHandler):
    def log_message(self, *a):  # noqa: D102 - silence the default stderr spam
        pass

    def do_POST(self):  # noqa: N802
        if not self.path.endswith("/v1/systemone"):
            self.send_error(404)
            return
        body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        answers = {}
        for name, q in (body.get("questions") or {}).items():
            qtype = q.get("type", "choice")
            instr = q.get("instructions", "")
            ans = answer_for(qtype, instr)
            if qtype == "choice":
                crit = q.get("criteria") or {}
                keys = list(crit)
                want = "billing"
                if "coverage verdict" in instr.lower():
                    want = keys[0]
                ans["choice"] = want if want in keys else keys[0]
                ans["confidence"] = 0.9
                ans["probabilities"] = {k: (0.9 if k == ans["choice"] else 0.1 / max(1, len(keys) - 1))
                                        for k in keys}
            answers[name] = ans
        payload = json.dumps({"answers": answers,
                              # The vLLM route counts one output token per
                              # question -- the label token it read. The
                              # checkpoint's own API reports 0.
                              "usage": {"input_tokens": 42,
                                        "output_tokens": len(answers)}}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)


def main() -> int:
    fails: list[str] = []

    server = HTTPServer(("127.0.0.1", 0), StubHandler)
    port = server.server_address[1]
    threading.Thread(target=server.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{port}"
    print(f"[preflight] stub decision endpoint on {base}")

    with tempfile.TemporaryDirectory() as tmp:
        tmpd = Path(tmp)
        out = tmpd / "results.jsonl"

        # --- run_suite.py against the stub ---------------------------------
        rc = subprocess.run(
            [sys.executable, str(HERE / "run_suite.py"),
             "--backend", "http", "--base", base,
             "--cases", str(HERE / "cases_smoke.json"),
             "--out", str(out), "--arm", "STUB", "--no-warmup"],
            capture_output=True, text=True)
        if rc.returncode != 0:
            fails.append(f"run_suite.py exited {rc.returncode}: {rc.stderr[-800:]}")
        else:
            print("[preflight] run_suite.py OK")

            recs = load(out)
            if len(recs) != 4:
                fails.append(f"expected 4 records, got {len(recs)}")
            if not all(r["ok"] for r in recs):
                fails.append("some records came back as errors")
            for r in recs:
                want = len(r.get("answers") or {})
                if r["usage"].get("output_tokens") != want:
                    fails.append(f"{r['case_id']}: output_tokens "
                                 f"{r['usage'].get('output_tokens')} != {want}")
                    break
            if any(r["state_chars"] == 0 for r in recs):
                fails.append("a record lost the state")

            summary = summarise(recs)
            arm = summary["arms"][0]
            if not arm["contract_ok"]:
                fails.append(f"contract violations on well-formed input: {arm['failures']}")
            if arm["accuracy"] != 1.0:
                fails.append(f"accuracy on the labelled smoke case was {arm['accuracy']}, expected 1.0")
            if arm["labelled"] != 2:
                fails.append(f"labelled count {arm['labelled']}, expected 2")
            print(f"[preflight] check_suite.py OK "
                  f"(accuracy {arm['accuracy']}, contract {arm['contract_ok']})")

            # --- a malformed record MUST be flagged ------------------------
            # The two routes own different shapes, so each malformation is
            # checked against the route it belongs to.
            bad = dict(recs[0])
            bad["backend"] = "inproc"
            bad["answers"] = {"refund": {"type": "noul", "noul": 0.9,
                                         "confidence": 0.9, "probabilities": {"yes": 1.0}}}
            bad["expect"] = {"answer_type": "noul"}
            violations = check_contract(bad)
            if not violations:
                fails.append("an inproc noul carrying confidence+probabilities was NOT flagged")
            else:
                print(f"[preflight] inproc noul with confidence flagged: {violations[0]}")

            rich = dict(recs[0])
            rich["backend"] = "http"
            rich["answers"] = {"refund": {"type": "noul", "noul": 0.9,
                                          "confidence": 0.9, "probabilities": {"yes": 1.0}}}
            rich["expect"] = {"answer_type": "noul"}
            if check_contract(rich):
                fails.append("an http noul carrying confidence+probabilities was flagged, "
                             "but the vLLM route legitimately returns them")
            else:
                print("[preflight] http noul with confidence accepted (route contract)")

            bad2 = dict(recs[0])
            bad2["answers"] = {"refund": {"type": "choice", "choice": "x", "confidence": 0.5,
                                          "probabilities": {"a": 0.5, "b": 0.4},
                                          "legend": {"0": "x"}}}
            if not check_contract(bad2):
                fails.append("a choice carrying a legend was NOT flagged")
            else:
                print("[preflight] choice-with-legend flagged")

            bad3 = dict(recs[0])
            bad3["answers"] = {"refund": {"type": "noul", "noul": 1.4}}
            if not check_contract(bad3):
                fails.append("a noul outside [0,1] was NOT flagged")
            else:
                print("[preflight] out-of-range noul flagged")

            bad4 = dict(recs[0])
            bad4["answers"] = {"refund": {"type": "noul", "noul": 0.9}}
            bad4["usage"] = {"input_tokens": 5, "output_tokens": 0}
            if not check_contract(bad4):
                fails.append("an http record with output_tokens=0 was NOT flagged")
            else:
                print("[preflight] http output_tokens mismatch flagged")

        # --- report.py over the stub records ------------------------------
        if out.exists():
            rep = tmpd / "report.md"
            rc = subprocess.run(
                [sys.executable, str(HERE / "report.py"),
                 "--results", str(out), "--cases", str(HERE / "cases_smoke.json"),
                 "--out", str(rep)],
                capture_output=True, text=True)
            if rc.returncode != 0:
                fails.append(f"report.py exited {rc.returncode}: {rc.stderr[-800:]}")
            elif not rep.exists() or "Per-arm summary" not in rep.read_text():
                fails.append("report.py produced no usable markdown")
            else:
                print("[preflight] report.py OK")

    server.shutdown()

    # --- the pick() semantics the accuracy scoring depends on -------------
    if pick({"type": "noul", "noul": 0.49})[1] is not False:
        fails.append("pick() on noul=0.49 should be False")
    if pick({"type": "noul", "noul": 0.5})[1] is not True:
        fails.append("pick() on noul=0.5 should be True")
    if pick({"type": "score", "probabilities": {"0": 0.1, "1": 0.7, "2": 0.2}})[1] != 1:
        fails.append("pick() on a score should be the argmax level")

    if fails:
        print("\nPREFLIGHT FAILED")
        for f in fails:
            print(f"  - {f}")
        return 1
    print("\nPREFLIGHT OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
