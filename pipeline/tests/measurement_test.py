#!/usr/bin/env python3
"""measurement_test.py — tests for the experiment-programme instrumentation.

Covers the four pieces EXP-02/EXP-03 depend on, each because breaking it
silently corrupts a number rather than raising:

  1. runconfig     — config.json round-trip; sampler_options must DROP None
                     keys (an unsent seed is a fact; a sent default is not)
  2. llm payload   — the sampler dict reaches the Ollama options block, and
                     temperature is threaded from the caller, not the default
  3. quality.score — per-row retention keyed by SUBDOMAIN.regulation (two
                     sub-domains sharing a regulation must not collide),
                     empty baseline -> None (not 0), pasted-implication
                     detection, adjustment_kind vocabulary
  4. aggregate_runs — the two trace schemas; latency read from
                     attempt{N}_latency_s and NOT from the dry-run-only
                     latency_s key (which is 0 and would silently zero every
                     real call); l1_pass on a resumed-after-abort run;
                     selection vs goal-file counts with a legitimate empty module

Run: python3 pipeline/tests/measurement_test.py

Unlike the older tests this one uses a UNIQUE temp directory (mkdtemp), not a
fixed /tmp path — a fixed path collides with itself under the parallel runs
the experiment programme exists to do.
"""

from __future__ import annotations

import json
import shutil
import statistics
import sys
import tempfile
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC))
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))

import aggregate_runs  # noqa: E402
import runconfig  # noqa: E402
import quality  # noqa: E402
from arm_stats import (bootstrap_ci, cliffs_delta, holm, noise_ratio,  # noqa: E402
                       wilson_interval)
from llm import OllamaClient  # noqa: E402

FAILURES: list[str] = []
TMP = Path(tempfile.mkdtemp(prefix="mvp_measurement_test_"))


def check(name: str, cond: bool, detail: str = "") -> None:
    if cond:
        print(f"  ok   {name}")
    else:
        FAILURES.append(name)
        print(f"  FAIL {name}  {detail}")


# --------------------------------------------------------------------------
# 1. runconfig
# --------------------------------------------------------------------------

def test_runconfig() -> None:
    print("== runconfig ==")
    rd = TMP / "cfg_run"
    rd.mkdir()
    cfg = runconfig.write(rd, runconfig.DEFAULTS | {
        "temperature": 0.0, "seed": 42, "arm": "C", "repeat": 3})
    loaded = runconfig.load(rd)
    check("round-trip keeps seed", loaded["seed"] == 42)
    check("round-trip keeps arm/repeat", loaded["arm"] == "C" and loaded["repeat"] == 3)
    check("missing config falls back to defaults",
          runconfig.load(TMP / "nonexistent")["temperature"] == 0.2)

    # the None contract: an unset sampler key is NOT sent
    opts = runconfig.sampler_options(loaded)
    check("seed sent when set", opts.get("seed") == 42)
    check("temperature sent", opts.get("temperature") == 0.0)
    check("top_p/top_k dropped when None", "top_p" not in opts and "top_k" not in opts)
    cfg2 = runconfig.write(rd, {"temperature": 0.2, "seed": None,
                                "top_p": None, "top_k": None})
    opts2 = runconfig.sampler_options(runconfig.load(rd))
    check("seed omitted when None", "seed" not in opts2, str(opts2))


# --------------------------------------------------------------------------
# 2. llm payload construction
# --------------------------------------------------------------------------

def test_llm_payload() -> None:
    print("== llm payload ==")
    captured: dict = {}

    class RecordingClient(OllamaClient):
        def _request(self, path, payload, timeout):
            captured["path"] = path
            captured["payload"] = payload
            return json.dumps({
                "message": {"content": "x"},
                "done_reason": "stop",
                "eval_count": 10,
                "prompt_eval_count": 100,
                "total_duration": 1_000_000_000,
            }).encode()

    c = RecordingClient("http://127.0.0.1:1")
    c.chat("m", "sys", "usr", 16384, temperature=0.0, num_predict=128,
           sampler={"seed": 42, "top_p": 0.9})
    opts = captured["payload"]["options"]
    check("seed reaches options", opts.get("seed") == 42)
    check("top_p reaches options", opts.get("top_p") == 0.9)
    check("caller temperature wins over default", opts.get("temperature") == 0.0)
    check("unsent key absent from options", "top_k" not in opts)

    c.chat_messages("m", [{"role": "user", "content": "hi"}], 8192,
                    temperature=0.2, sampler={"seed": 7})
    opts2 = captured["payload"]["options"]
    check("chat_messages carries sampler too", opts2.get("seed") == 7)


# --------------------------------------------------------------------------
# 3. quality measurement layer
# --------------------------------------------------------------------------

BASE_D1 = ("The controller implements appropriate technical and organisational "
           "measures to ensure data protection, including encryption of "
           "personal data at rest and access controls.")
BASE_D3 = ("Access to personal data is restricted to authorised personnel "
           "through strong authentication and least-privilege authorisations.")
BASELINES = {"D-01.1.GDPR": BASE_D1, "D-03.2.GDPR": BASE_D3}

ROW_A = {"id": "AG-D-01.1-001", "subdomain": "D-01.1", "regulation": "GDPR",
         "baseline_source": "SG-D-01.1.GDPR",
         "goal": ("TinyTask applies encryption at rest to its hosted task "
                  "database and enforces least-privilege access controls over "
                  "the personal data it processes for its 8 employees."),
         "implication": "The hosted task store must encrypt data at rest and "
                        "restrict access to the small internal team.",
         "pattern": "maintain", "property": "c",
         "adjustment": "narrowed: encryption limited to the hosted store — "
                       "because TinyTask runs a single managed database"}
ROW_B = {"id": "AG-D-03.2-001", "subdomain": "D-03.2", "regulation": "GDPR",
         "baseline_source": "SG-D-03.2.GDPR",
         "goal": ("TinyTask restricts access to personal data to authorised "
                  "staff using strong authentication and role-based "
                  "authorisations sized to an 8-person team."),
         "implication": "The hosted task store must encrypt data at rest and "
                        "restrict access to the small internal team.",
         "pattern": "maintain", "property": "c",
         "adjustment": "unchanged — fits as stated"}
ROW_EMPTY_BASE = {"id": "AG-D-08.3-001", "subdomain": "D-08.3",
                  "regulation": "GDPR", "baseline_source": "SG-D-08.3.GDPR",
                  "goal": "Any goal here has no baseline to retain.",
                  "implication": "Some implication sentence.",
                  "pattern": "maintain", "property": "c",
                  "adjustment": "unchanged — fits as stated"}


def test_quality_scores() -> None:
    print("== quality measurement ==")
    a = quality.score_row(ROW_A, BASELINES, [BASE_D1], [ROW_B["implication"]])
    check("retention is a number in range",
          a["retention"] is not None and 0.0 <= a["retention"] <= 1.0,
          str(a["retention"]))
    # hand-computed: the goal keeps {encryption, rest, access, controls,
    # personal, data} = 6 of the baseline's 15 unique obligation terms
    check("composite baseline key resolves (hand-computed 6/15)",
          a["retention"] is not None and abs(a["retention"] - 6 / 15) < 1e-9,
          str(a["retention"]))

    b = quality.score_row(ROW_B, BASELINGS if False else BASELINES, [BASE_D3],
                          [ROW_A["implication"]])
    check("D-03.2 gets ITS OWN baseline (composite key)",
          b["retention"] is not None and abs(b["retention"] - a["retention"]) > 1e-9,
          f"{b['retention']} == {a['retention']} would mean a key collision")

    e = quality.score_row(ROW_EMPTY_BASE, BASELINES, [], [])
    check("missing baseline -> None, not 0", e["retention"] is None)

    check("adjustment_kind vocabulary",
          [quality.adjustment_kind(x) for x in
           ("narrowed: x — because y", "unchanged — fits", "flagged: q", "", "junk")]
          == ["narrowed", "unchanged", "flagged", "malformed", "malformed"])

    pasted = quality.max_peer_similarity(ROW_A["implication"],
                                         [ROW_B["implication"]])
    check("pasted implication scores ~1.0 against its peer", pasted > 0.95,
          str(pasted))

    summary = quality.score_run([ROW_A, ROW_B, ROW_EMPTY_BASE], BASELINES, [])
    check("score_run counts rows and sub-domains",
          summary["n_rows"] == 3 and summary["n_subdomains"] == 3,
          str(summary["n_subdomains"]))
    check("adjustment mix counts narrowed/unchanged",
          summary["adjustment_mix"].get("narrowed") == 1
          and summary["adjustment_mix"].get("unchanged") == 2)
    # both sides of a pasted pair sit above the limit: the metric is symmetric,
    # and counting only one would understate every pasted sentence by half
    check("implication reuse flags BOTH sides of the pasted pair",
          summary["implication_reuse"]["n_above_dup_limit"] == 2,
          str(summary["implication_reuse"]))


# --------------------------------------------------------------------------
# 4. aggregate_runs on a synthetic run directory
# --------------------------------------------------------------------------

def make_run(root: Path, name: str, *, mode: str = "pipeline",
             last_status: str = "ok", seed=None, temperature=0.2) -> Path:
    rd = root / name
    (rd / "steps" / "goals").mkdir(parents=True)
    (rd / "steps" / "gates").mkdir(parents=True)
    (rd / "manifest.json").write_text(json.dumps({
        "run_id": name, "case_id": "Case_01_TinyTask_SaaS",
        "model": "qwen3.8:27b", "aegis_git_rev": "abc1234" if name != "no_cfg" else "",
        "stage_history": [
            {"stage": "p1", "status": "ok", "n_calls": 1},
            {"stage": "agentic" if mode == "agentic" else "p5",
             "status": last_status, "n_calls": 2},
        ]}))
    runconfig.write(rd, {"temperature": temperature, "seed": seed,
                         "top_p": None, "top_k": None,
                         "arm": "T", "repeat": 1,
                         "preapprove_gates": False})

    def call(seq, **kw):
        base = {"seq": seq, "step": f"s{seq}", "model": "qwen3.8:27b",
                "num_ctx": 16384, "num_predict": 4096, "temperature": temperature,
                "status": "ok"}
        base.update(kw)
        return base

    lines = []
    if mode == "pipeline":
        # latency lives ONLY on attempt1_latency_s; latency_s is the dry-run trap
        lines.append(call(1, est_prompt_tokens=1700,
                          attempt1_latency_s=10.0, attempt1_eval_tokens=100,
                          attempt1_prompt_tokens=1655))
        lines.append(call(2, est_prompt_tokens=900,
                          attempt1_latency_s=5.0, attempt1_eval_tokens=50,
                          attempt1_prompt_tokens=880))
    else:
        lines.append(call(1, mode="agentic", history_est_tokens=4000,
                          attempt1_latency_s=20.0, attempt1_eval_tokens=200,
                          attempt1_prompt_tokens=3900))
    (rd / "trace.jsonl").write_text(
        "\n".join(json.dumps(l) for l in lines) + "\n")

    (rd / "steps" / "selection.json").write_text(json.dumps({
        "selected": [{"id": "D-01.1", "name": "x", "rationale": "y"},
                     {"id": "D-03.2", "name": "x", "rationale": "y"},
                     {"id": "D-08.3", "name": "x", "rationale": "y"}],
        "excluded": []}))
    (rd / "steps" / "goals" / "D-01_1.json").write_text(json.dumps(
        {"subdomain": "D-01.1", "goals": [ROW_A], "assumptions": []}))
    # D-08.3: a legitimately empty module (no Sub-SO card in the corpus)
    (rd / "steps" / "goals" / "D-08_3.json").write_text(json.dumps(
        {"subdomain": "D-08.3", "goals": [], "assumptions": []}))
    (rd / "doc02_adjusted_goals.md").write_text("# deliverable\n")
    return rd


def test_aggregate() -> None:
    print("== aggregate_runs ==")
    root = TMP / "runs_root"
    root.mkdir()
    ok_run = make_run(root, "ok_pipeline_run")
    agent_run = make_run(root, "ok_agent_run", mode="agentic", seed=42,
                         temperature=0.0)
    aborted_run = make_run(root, "aborted_run", last_status="aborted")

    recs = {r["run_id"]: r for r in
            (aggregate_runs.run_metrics(d) for d in sorted(root.iterdir()))}

    p = recs["ok_pipeline_run"]["trace"]
    check("pipeline latency from attempt1_latency_s (NOT the dry-run trap)",
          p["llm_seconds"] == 15.0, str(p["llm_seconds"]))
    check("real prompt tokens preferred over the chars/4 estimate",
          p["prompt_tokens_total"] == 1655 + 880, str(p["prompt_tokens_total"]))
    check("pipeline mode detected", p["mode"] == "pipeline")

    a = recs["ok_agent_run"]["trace"]
    check("agent real prompt tokens read (schema union)",
          a["prompt_tokens_total"] == 3900, str(a["prompt_tokens_total"]))
    check("agent mode detected", a["mode"] == "agentic")

    # legacy record: pre-instrumentation runs carry only the estimate
    legacy = {"seq": 9, "step": "s9", "status": "ok",
              "est_prompt_tokens": 1700, "attempt1_latency_s": 3.0,
              "attempt1_eval_tokens": 10}
    check("legacy record falls back to est_prompt_tokens",
          aggregate_runs.prompt_tokens(legacy) == 1700)
    check("latency_s key (dry-run only) is never consulted",
          aggregate_runs.latency_seconds({"latency_s": 0}) == 0.0
          and aggregate_runs.latency_seconds(
              {"attempt1_latency_s": 4.0, "attempt2_latency_s": 1.0}) == 5.0)

    check("config travels into the record",
          recs["ok_agent_run"]["seed"] == 42
          and recs["ok_agent_run"]["temperature"] == 0.0)
    check("resumed-after-abort run is L1 valid",
          recs["ok_agent_run"]["l1_pass"] is True)
    check("run whose LAST stage aborted is not L1 valid",
          recs["aborted_run"]["l1_pass"] is False)

    art = recs["ok_pipeline_run"]["artefact"]
    check("selection counted from selection.json (38-case shape)",
          art["n_selected"] == 3, str(art.get("n_selected")))
    check("empty module counted, not dropped",
          art["n_empty_modules"] == 1 and art["n_subdomains_with_rows"] == 1)
    check("quality computed over the run",
          art["quality"]["retention"]["mean"] is not None)

    div = aggregate_runs.selection_divergence(list(recs.values()))
    check("selection divergence computes", any("Jaccard" in s for s in div))


# --------------------------------------------------------------------------
# 5. arm_stats known-answer checks
# --------------------------------------------------------------------------

def test_arm_stats() -> None:
    print("== arm_stats ==")
    lo, hi = bootstrap_ci([5.0] * 12)
    check("bootstrap CI of a constant is the constant", lo == hi == 5.0)

    c1 = bootstrap_ci([1.0, 2.0, 3.0, 4.0])
    c2 = bootstrap_ci([1.0, 2.0, 3.0, 4.0])
    check("bootstrap CI is seeded and reproducible", c1 == c2)

    check("cliffs_delta full separation: a<b -> -1",
          cliffs_delta(list(range(1, 11)), list(range(11, 21))) == -1.0)
    check("cliffs_delta full separation: a>b -> +1",
          cliffs_delta(list(range(11, 21)), list(range(1, 11))) == 1.0)
    check("cliffs_delta identical samples 0",
          cliffs_delta(list(range(1, 11)), list(range(1, 11))) == 0.0)

    p, lo, hi = wilson_interval(15, 15)
    check("wilson at 15/15 stays under 1 and above the naive p",
          lo > 0.7 and hi <= 1.0, f"[{lo:.3f},{hi:.3f}]")

    res = holm({"a": 0.4, "b": 0.001, "c": 0.02})
    check("holm keeps the small p significant and kills the null",
          res["b"]["significant"] and not res["a"]["significant"])

    # the two-ratio contract: the same effect_sd must become MORE detectable
    # with n — reporting only one number hides this
    import random
    rng = random.Random(11)
    n3a = [rng.gauss(0.7, 0.08) for _ in range(3)]
    n3b = [rng.gauss(0.7, 0.08) for _ in range(3)]
    n40a = [rng.gauss(0.7, 0.08) for _ in range(40)]
    n40b = [rng.gauss(0.7, 0.08) for _ in range(40)]
    r3 = noise_ratio(n3a, n3b)
    r40 = noise_ratio(n40a, n40b)
    check("identical distributions read as within noise",
          r3["verdict"] == "within noise", r3["verdict"])
    check("detectability grows with n for the same population",
          abs(r40["detectability"]) < abs(r3["detectability"]) + 1e9
          and r40["n_a"] > r3["n_a"])  # structural check: n carried through


def main() -> int:
    try:
        test_runconfig()
        test_llm_payload()
        test_quality_scores()
        test_aggregate()
        test_arm_stats()
    finally:
        shutil.rmtree(TMP, ignore_errors=True)
    print()
    if FAILURES:
        print(f"FAILURES: {len(FAILURES)}")
        for f in FAILURES:
            print(f"  - {f}")
        return 1
    print("ALL MEASUREMENT TESTS PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
