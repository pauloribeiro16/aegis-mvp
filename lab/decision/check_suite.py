#!/usr/bin/env python3
"""check_suite.py — score the records a suite run produced.

    python3 check_suite.py results/*.jsonl --out results/summary.json

Two kinds of check, kept apart on purpose:

  CONTRACT   -- the answer shape the Decision Index defines. A noul carries no
                confidence and no probabilities; a choice carries no legend; a
                score carries both and is zero-based and continuous; every
                probability distribution sums to 1; output_tokens is 0.

  ACCURACY   -- the pick against a label. A case with no label is UNLABELLED,
                which is NOT a failure and NOT a pass. Conflating the two is
                how a suite reports a number it never measured.

Also reports, separately and never merged into accuracy:
  determinism -- do repeats of the same case agree?
  latency     -- median / p95 per arm, reported as a secondary metric.
"""
from __future__ import annotations

import argparse
import json
import statistics
import sys
from pathlib import Path

ANSWER_TYPES = ("noul", "choice", "score")
PROB_SUM_TOL = 1e-3

# The two routes do NOT return the same shape, and that is a finding, not a
# bug to hide behind a laxer check:
#
#   inproc  the checkpoint's own answer(): a noul is {type, noul} and nothing
#           else, and usage.output_tokens is 0 (nothing is generated).
#   http    vLLM's decision route returns the FULL typed answer for a noul
#           (with probabilities and confidence) and counts output_tokens as
#           the label tokens it read -- one per question.
#
# Both are recorded. The per-question-type invariants below are checked
# against the route that owns them.
BACKEND_CONTRACT = {
    "inproc": {"noul_bare": True, "output_tokens": "zero"},
    "http": {"noul_bare": False, "output_tokens": "per_question"},
}


def pick(answer: dict) -> tuple[str, object]:
    """The categorical answer a decision model commits to."""
    t = answer.get("type")
    if t == "noul":
        return "noul", bool(float(answer.get("noul", 0.0)) >= 0.5)
    if t == "choice":
        return "choice", answer.get("choice")
    if t == "score":
        probs = answer.get("probabilities", {}) or {}
        if not probs:
            return "score", None
        best = max(probs.items(), key=lambda kv: float(kv[1]))
        return "score", int(best[0])
    return "unknown", None


def probs_of(answer: dict) -> dict:
    """The answer's distribution over its options, keyed by option name."""
    t = answer.get("type")
    if t == "noul":
        p = float(answer.get("noul", 0.0))
        return {"yes": p, "no": 1.0 - p}
    if t in ("choice", "score"):
        return {k: float(v) for k, v in (answer.get("probabilities", {}) or {}).items()}
    return {}


def check_contract(rec: dict) -> list[str]:
    """Contract violations of one record. Empty list == the shape is right."""
    fails: list[str] = []
    if not rec.get("ok"):
        return fails  # the error path is checked separately

    answers = rec.get("answers") or {}
    usage = rec.get("usage") or {}
    expect = rec.get("expect") or {}
    questions = rec.get("questions") or {}
    contract = BACKEND_CONTRACT.get(rec.get("backend", "inproc"), BACKEND_CONTRACT["inproc"])
    n_questions = len(questions) or 1

    for name, ans in answers.items():
        t = ans.get("type")
        if t not in ANSWER_TYPES:
            fails.append(f"{name}: unknown answer type {t!r}")
            continue
        # `answer_type` is either one type for every answer, or a map per question.
        want_type = expect.get("answer_type")
        if isinstance(want_type, dict):
            want_type = want_type.get(name)
        if want_type and t != want_type:
            fails.append(f"{name}: answer type {t!r} != expected {want_type!r}")

        if t == "noul":
            # The checkpoint's answer() returns a bare noul; the vLLM route
            # returns the full typed answer. A legend is wrong on both.
            if contract["noul_bare"]:
                if "confidence" in ans:
                    fails.append(f"{name}: noul must not carry a confidence")
                if "probabilities" in ans:
                    fails.append(f"{name}: noul must not carry probabilities")
            if "legend" in ans:
                fails.append(f"{name}: noul must not carry a legend")
            p = ans.get("noul")
            if not isinstance(p, (int, float)) or not (0.0 <= float(p) <= 1.0):
                fails.append(f"{name}: noul value {p!r} outside [0,1]")

        elif t == "choice":
            if "legend" in ans:
                fails.append(f"{name}: choice must not carry a legend")
            if "confidence" not in ans:
                fails.append(f"{name}: choice without confidence")
            probs = ans.get("probabilities")
            if not isinstance(probs, dict) or not probs:
                fails.append(f"{name}: choice without probabilities")
            else:
                total = sum(float(v) for v in probs.values())
                if abs(total - 1.0) > PROB_SUM_TOL:
                    fails.append(f"{name}: probabilities sum to {total:.6f}, not 1")
                crit = (questions.get(name, {}) or {}).get("criteria") or {}
                if crit and set(probs) != set(crit):
                    fails.append(f"{name}: probability keys {sorted(probs)} != criteria "
                                 f"{sorted(crit)}")
                if ans.get("choice") is not None and crit and ans["choice"] not in crit:
                    fails.append(f"{name}: choice {ans['choice']!r} is not one of the criteria")

        elif t == "score":
            if "confidence" not in ans:
                fails.append(f"{name}: score without confidence")
            probs = ans.get("probabilities")
            legend = ans.get("legend")
            if not isinstance(probs, dict) or not probs:
                fails.append(f"{name}: score without probabilities")
            else:
                total = sum(float(v) for v in probs.values())
                if abs(total - 1.0) > PROB_SUM_TOL:
                    fails.append(f"{name}: probabilities sum to {total:.6f}, not 1")
                crit = (questions.get(name, {}) or {}).get("criteria") or []
                want = {str(i) for i in range(len(crit))} if crit else set(probs)
                if set(probs) != want:
                    fails.append(f"{name}: score probability keys {sorted(probs)} != {sorted(want)}")
                if not isinstance(legend, dict) or set(legend) != set(probs):
                    fails.append(f"{name}: score legend keys do not match the probabilities")
            s = ans.get("score")
            crit = (questions.get(name, {}) or {}).get("criteria") or []
            if crit and isinstance(s, (int, float)):
                if not (0.0 <= float(s) <= len(crit) - 1):
                    fails.append(f"{name}: score {s} outside [0, {len(crit) - 1}]")

    out_tokens = usage.get("output_tokens")
    if out_tokens is None:
        fails.append("usage without output_tokens")
    elif contract["output_tokens"] == "zero" and int(out_tokens) != 0:
        fails.append(f"usage.output_tokens = {out_tokens}, expected 0")
    elif contract["output_tokens"] == "per_question" and int(out_tokens) != n_questions:
        fails.append(f"usage.output_tokens = {out_tokens}, expected {n_questions} "
                     f"(one label token per question)")
    in_tokens = usage.get("input_tokens")
    if in_tokens is None:
        fails.append("usage without input_tokens")
    elif int(in_tokens) <= 0:
        fails.append(f"usage.input_tokens = {in_tokens}, expected > 0")

    return fails


def model_key(rec: dict) -> str:
    """A route-independent key for the model a record came from.

    "LiquidAI/d1-3B" (the server label) and "LiquidAI_d1-3B" (the checkpoint
    directory name) are the same model and must resolve to the same key.
    """
    return (rec.get("model") or "").strip().lower().replace("/", "_").replace("-", "_")


def route_key(rec: dict) -> str:
    """Backend AND model: the checkpoint and the server are the same model
    with different contracts, so the key has to name both."""
    return f"{rec.get('backend', '?')}:{model_key(rec)}"


def expected_error(rec: dict) -> bool | None:
    """What this route was expected to do with the case.

    True/False asserts for every route; a map asserts per model, and a model
    the map does not mention carries no assertion.
    """
    spec = rec.get("expect_error")
    if spec is None:
        return None
    if isinstance(spec, bool):
        return spec
    if isinstance(spec, dict):
        return spec.get(route_key(rec))
    return None


def variant_of(rec: dict) -> str:
    """The label of one run.

    The three d1-omni arms share an arm name and differ only by dtype, so
    the dtype is part of the label -- otherwise one run silently overwrites
    another in every summary.
    """
    arm = rec.get("arm", "?")
    dtype = rec.get("dtype") or "n/a"
    if dtype in ("n/a", "none", ""):
        return arm
    return f"{arm}-{dtype}"


def load(path: Path) -> list[dict]:
    recs = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            recs.append(json.loads(line))
    return recs


def summarise(records: list[dict]) -> dict:
    by_arm: dict[str, dict] = {}
    for rec in records:
        arm = variant_of(rec)
        s = by_arm.setdefault(arm, {
            "arm": arm, "variant": arm, "backend": rec.get("backend"),
            "model": rec.get("model"),
            "dtype": rec.get("dtype"), "records": 0, "errors": 0,
            "contract_failures": 0, "contract_failed_records": 0,
            "labelled": 0, "labelled_correct": 0, "unlabelled": 0,
            "contested": 0, "contested_correct": 0,
            "expected_errors": 0, "expected_errors_observed": 0,
            "unexpected_errors": 0, "latencies": [], "failures": [],
        })
        s["records"] += 1
        s["latencies"].append(float(rec.get("latency_ms") or 0.0))

        expect_error = expected_error(rec)
        if not rec.get("ok"):
            s["errors"] += 1
            if expect_error is True:
                s["expected_errors_observed"] += 1
                s["expected_errors"] += 1
            elif expect_error is False:
                s["unexpected_errors"] += 1
                s["failures"].append({
                    "case_id": rec.get("case_id"), "kind": "unexpected_error",
                    "detail": rec.get("error")})
            continue
        if expect_error is True:
            s["unexpected_errors"] += 1
            s["failures"].append({
                "case_id": rec.get("case_id"), "kind": "expected_error_but_answered",
                "detail": rec.get("answers")})
            continue

        fails = check_contract(rec)
        if fails:
            s["contract_failed_records"] += 1
            s["contract_failures"] += len(fails)
            for f in fails:
                s["failures"].append({"case_id": rec.get("case_id"), "kind": "contract", "detail": f})

        labels = (rec.get("expect") or {}).get("labels") or {}
        answers = rec.get("answers") or {}
        if not labels:
            s["unlabelled"] += 1
            continue
        # A contested label is one where two of the project's own artefacts
        # disagree. It is measured and reported, but it is NOT accuracy.
        contested = bool((rec.get("expect") or {}).get("contested"))
        for qname, want in labels.items():
            ans = answers.get(qname)
            if ans is None:
                s["failures"].append({"case_id": rec.get("case_id"), "kind": "missing_answer",
                                       "detail": qname})
                continue
            kind, got = pick(ans)
            if kind == "noul":
                got_cmp, want_cmp = bool(got), bool(want)
            elif kind == "choice":
                got_cmp, want_cmp = str(got), str(want)
            elif kind == "score":
                got_cmp, want_cmp = int(got) if got is not None else None, int(want)
            else:
                got_cmp, want_cmp = None, want
            if contested:
                s["contested"] += 1
                if got_cmp == want_cmp:
                    s["contested_correct"] += 1
                continue
            s["labelled"] += 1
            if got_cmp == want_cmp:
                s["labelled_correct"] += 1
            else:
                s["failures"].append({
                    "case_id": rec.get("case_id"), "kind": "wrong_pick",
                    "detail": f"{qname}: got {got_cmp!r}, expected {want_cmp!r}"})

    out = []
    for s in by_arm.values():
        lat = sorted(s.pop("latencies"))
        s["latency_median_ms"] = round(statistics.median(lat), 2) if lat else None
        s["latency_p95_ms"] = round(lat[int(len(lat) * 0.95) - 1], 2) if lat else None
        s["accuracy"] = (round(s["labelled_correct"] / s["labelled"], 4)
                         if s["labelled"] else None)
        s["contract_ok"] = s["contract_failed_records"] == 0
        s["error_paths_ok"] = s["unexpected_errors"] == 0
        out.append(s)
    return {"arms": sorted(out, key=lambda x: x["arm"])}


def determinism(records: list[dict]) -> dict:
    """Do repeats of the same case agree? Grouped per arm."""
    groups: dict[tuple[str, str], list[dict]] = {}
    for rec in records:
        if not rec.get("ok"):
            continue
        groups.setdefault((rec.get("arm", "?"), rec.get("case_id", "?")), []).append(rec)
    per_arm: dict[str, dict] = {}
    for (arm, _case), recs in groups.items():
        if len(recs) < 2:
            continue
        picks = []
        for r in recs:
            p = {q: pick(a) for q, a in (r.get("answers") or {}).items()}
            picks.append(p)
        agree = all(p == picks[0] for p in picks)
        d = per_arm.setdefault(arm, {"groups": 0, "agreeing": 0, "disagreements": []})
        d["groups"] += 1
        if agree:
            d["agreeing"] += 1
        else:
            d["disagreements"].append(_case)
    for arm, d in per_arm.items():
        d["stable"] = d["agreeing"] == d["groups"]
    return per_arm


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("results", nargs="+")
    ap.add_argument("--out", default=None)
    ap.add_argument("--expect-from", "--labels-from", dest="expect_from",
                    nargs="+", default=None,
                    help="case file whose expect/expect_error win over the "
                         "records' own -- the case file is the single source "
                         "of truth for what was asserted")
    args = ap.parse_args()

    records: list[dict] = []
    for p in args.results:
        records.extend(load(Path(p)))

    if args.expect_from:
        # The expectations live in the case file so the researcher can fill
        # them in without touching the records, and so a corrected contract
        # matrix is a documentation change rather than a re-run. The case
        # file wins.
        by_id: dict = {}
        for path in args.expect_from:
            data = json.loads(Path(path).read_text(encoding="utf-8"))
            for c in data.get("cases", []):
                by_id[c.get("id")] = c
        patched = 0
        for rec in records:
            case = by_id.get(rec.get("case_id"))
            if not case:
                continue
            if case.get("expect"):
                rec["expect"] = case["expect"]
            if case.get("expect_error") is not None:
                rec["expect_error"] = case["expect_error"]
            patched += 1
        print(f"expect-from {', '.join(args.expect_from)}: patched {patched} records")

    summary = summarise(records)
    summary["determinism"] = determinism(records)
    summary["total_records"] = len(records)

    for arm in summary["arms"]:
        print(f"\n=== arm {arm['arm']} ({arm['backend']} / {arm['model']} / {arm['dtype']}) ===")
        print(f"  records              {arm['records']}")
        print(f"  contract ok          {arm['contract_ok']} "
              f"({arm['contract_failed_records']} records with shape violations)")
        print(f"  error paths ok       {arm['error_paths_ok']} "
              f"({arm['unexpected_errors']} unexpected)")
        print(f"  expected errors seen {arm['expected_errors_observed']}")
        acc = arm["accuracy"]
        print(f"  accuracy (labelled)  {acc if acc is not None else 'n/a (no labels)'}"
              f"  [{arm['labelled_correct']}/{arm['labelled']}]")
        print(f"  unlabelled records   {arm['unlabelled']}")
        if arm.get("contested"):
            print(f"  contested labels     {arm['contested_correct']}/{arm['contested']} "
                  f"(reported separately, not in the accuracy)")
        print(f"  latency median/p95   {arm['latency_median_ms']} / {arm['latency_p95_ms']} ms")
        det = summary["determinism"].get(arm["arm"])
        if det:
            print(f"  repeat stability     {det['agreeing']}/{det['groups']} groups agree"
                  + (f"  DISAGREE: {det['disagreements']}" if det["disagreements"] else ""))
        for f in arm["failures"][:12]:
            print(f"    ! {f['kind']}: {f['case_id']} — {f['detail']}")
        if len(arm["failures"]) > 12:
            print(f"    ... {len(arm['failures']) - 12} more")

    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(json.dumps(summary, indent=2, ensure_ascii=False),
                                  encoding="utf-8")
        print(f"\nwrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
