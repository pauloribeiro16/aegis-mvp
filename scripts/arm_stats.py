#!/usr/bin/env python3
"""Statistics for the AEGIS experiment programme (stdlib only).

There is no numpy or scipy on the compute nodes (no pip egress) or on the
workstation, so every estimator here is plain Python. That is a constraint, but
it is also a virtue: the statistics used to interpret the runs are short enough
to read and audit, which is the same reason the repo's own linters are
hand-written.

What this provides, and why each one:

  * ``bootstrap_ci``       — the default interval. The metrics are bounded
                             (retention in [0,1]), near-integer (row counts) and
                             skewed, so a t-interval on them would be an
                             assumption rather than a fact.
  * ``cliffs_delta``       — a non-parametric effect size that stays meaningful
                             at n=15 per arm, where a standardised mean
                             difference is dominated by sampling noise in the
                             SD estimate.
  * ``welch_t``            — included for reference, and reported alongside the
                             bootstrap so the two can disagree visibly.
  * ``wilson_interval``    — for proportions such as the L1 PASS rate, where the
                             normal approximation breaks down near 0 and 1
                             (which is where a passing pipeline sits).
  * ``holm``               — multiplicity. A programme with three experiments and
                             a dozen secondary metrics makes ~30 comparisons;
                             uncorrected, one of them is expected to look
                             significant by chance alone.

The central use is not "is A better than B" but "is the A-B difference larger
than the within-arm noise", which is ``noise_ratio`` below.

Usage::

    python3 scripts/arm_stats.py --demo
    python3 scripts/arm_stats.py --json arm_a.json --json arm_b.json
    python3 scripts/arm_stats.py --compare retention a.json b.json
"""

from __future__ import annotations

import argparse
import json
import math
import random
import statistics
import sys
from pathlib import Path
from typing import Callable, Sequence

BOOTSTRAP_RESAMPLES = 10_000
BOOTSTRAP_SEED = 20261003  # fixed: a CI that moves between runs is not a CI


# --------------------------------------------------------------------------
# interval estimation
# --------------------------------------------------------------------------

def bootstrap_ci(values: Sequence[float], statistic: Callable[[list[float]], float]
                 = statistics.mean, alpha: float = 0.05,
                 resamples: int = BOOTSTRAP_RESAMPLES,
                 seed: int = BOOTSTRAP_SEED) -> tuple[float, float]:
    """Percentile bootstrap CI for any statistic.

    Seeded, so the interval is reproducible: an interval that differs between
    two invocations on the same data is a nuisance that erodes trust in every
    other number in the report.
    """
    data = [v for v in values if v is not None]
    if len(data) < 2:
        return (float("nan"), float("nan"))
    rng = random.Random(seed)
    n = len(data)
    stats = []
    for _ in range(resamples):
        sample = [data[rng.randrange(n)] for _ in range(n)]
        try:
            stats.append(statistic(sample))
        except statistics.StatisticsError:
            continue
    if not stats:
        return (float("nan"), float("nan"))
    stats.sort()
    lo = stats[int((alpha / 2) * len(stats))]
    hi = stats[min(len(stats) - 1, int((1 - alpha / 2) * len(stats)))]
    return (lo, hi)


def welch_t(a: Sequence[float], b: Sequence[float]) -> tuple[float, float]:
    """Welch's t and its two-sided p, via the normal approximation to the t
    distribution. Adequate at n>=15 per arm; at smaller n the bootstrap is the
    answer and this is only reported so the two can be compared."""
    a = [v for v in a if v is not None]
    b = [v for v in b if v is not None]
    if len(a) < 2 or len(b) < 2:
        return (float("nan"), float("nan"))
    va, vb = statistics.variance(a), statistics.variance(b)
    se = math.sqrt(va / len(a) + vb / len(b))
    if se == 0:
        return (float("inf") if statistics.mean(a) != statistics.mean(b) else 0.0, 0.0)
    t = (statistics.mean(a) - statistics.mean(b)) / se
    # two-sided normal tail; with Welch df this is approximate and labelled so
    p = math.erfc(abs(t) / math.sqrt(2))
    return (t, p)


def cliffs_delta(a: Sequence[float], b: Sequence[float]) -> float:
    """P(a > b) - P(a < b). Bounded [-1, 1]; 0 means the distributions overlap.

    Chosen over Cohen's d because d divides by a pooled SD estimated from ~30
    observations, and the resulting number moves more with n than with the
    effect. delta does not.
    """
    a = [v for v in a if v is not None]
    b = [v for v in b if v is not None]
    if not a or not b:
        return float("nan")
    gt = lt = 0
    for x in a:
        for y in b:
            if x > y:
                gt += 1
            elif x < y:
                lt += 1
    return (gt - lt) / (len(a) * len(b))


def wilson_interval(successes: int, n: int, z: float = 1.96
                    ) -> tuple[float, float, float]:
    """Wilson score interval for a proportion. Correct where the normal
    approximation degenerates — which is exactly at p≈1, where a pipeline that
    always passes L1 lives."""
    if n == 0:
        return (0.0, float("nan"), float("nan"))
    p = successes / n
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    margin = (z / denom) * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (p, max(0.0, centre - margin), min(1.0, centre + margin))


# --------------------------------------------------------------------------
# the question the programme actually asks
# --------------------------------------------------------------------------

def noise_ratio(a: Sequence[float], b: Sequence[float]) -> dict:
    """Is the A-B difference larger than the run-to-run noise?

    Two different ratios, because they answer two different questions and
    conflating them produces a wrong verdict:

      ``effect_sd``   — the difference in units of the pooled within-arm SD.
                        The classic reading: 1.0 means "the arms differ by one
                        standard rerun deviation". This does NOT depend on n,
                        and on its own it says nothing about detectability.

      ``detectability`` — the difference in units of the standard error of the
                        difference. It DOES depend on n, and it is the one that
                        answers "could this design have seen it". A 1.3-SD
                        difference is undetectable at n=3 per arm and obvious at
                        n=50; reporting only the first number invites calling a
                        real effect "within noise".

    A verdict is reported, but the numbers above it are the answer — a verdict
    that hides its own inputs cannot be checked.
    """
    a = [v for v in a if v is not None]
    b = [v for v in b if v is not None]
    if len(a) < 2 or len(b) < 2:
        return {"effect_sd": float("nan"), "detectability": float("nan"),
                "verdict": "insufficient n"}
    sa, sb = statistics.stdev(a), statistics.stdev(b)
    pooled = math.sqrt((sa * sa + sb * sb) / 2)
    diff = statistics.mean(a) - statistics.mean(b)
    se_diff = pooled * math.sqrt(1 / len(a) + 1 / len(b)) if pooled else 0.0
    _, p = welch_t(a, b)

    effect = diff / pooled if pooled else float("inf")
    detect = abs(diff) / se_diff if se_diff else float("inf")

    if se_diff == 0:
        verdict = "identical" if diff == 0 else "separated with zero variance"
    elif detect >= 1.96:
        verdict = "distinguishable at this n"
    elif detect >= 1.0:
        verdict = "underpowered: suggestive, not established at this n"
    else:
        verdict = "within noise"

    return {
        "n_a": len(a), "n_b": len(b),
        "mean_a": statistics.mean(a), "mean_b": statistics.mean(b),
        "sd_a": sa, "sd_b": sb,
        "diff": diff,
        "pooled_sd": pooled,
        "se_diff": se_diff,
        "effect_sd": effect,
        "detectability": detect,
        "welch_p": p,
        "cliffs_delta": cliffs_delta(a, b),
        "verdict": verdict,
    }


# --------------------------------------------------------------------------
# multiplicity
# --------------------------------------------------------------------------

def holm(pvalues: dict[str, float], alpha: float = 0.05) -> dict[str, dict]:
    """Holm-Bonferroni step-down. Returns per-test adjusted p and verdict.

    With three experiments and a dozen secondary metrics each, uncorrected
    testing produces roughly one spurious "significant" finding per thirty
    comparisons — which is indistinguishable from a real effect at a glance.
    """
    items = sorted(pvalues.items(), key=lambda kv: kv[1])
    m = len(items)
    out: dict[str, dict] = {}
    running_max = 0.0
    for i, (name, p) in enumerate(items):
        adj = min(1.0, (m - i) * p)
        running_max = max(running_max, adj)
        out[name] = {"p": p, "p_holm": running_max,
                     "significant": running_max < alpha}
    return out


# --------------------------------------------------------------------------
# reporting
# --------------------------------------------------------------------------

def _load(path: str) -> list[float]:
    """Accept a JSON file of numbers, a list, or {'<metric>': [...]}' and pull
    the named metric out."""
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if isinstance(data, dict):
        # a full aggregate_runs.py record set: take the first numeric metric
        # found, preferring the pre-registered primary
        for key in ("retention_mean", "retention"):
            if key in data:
                return [float(v) for v in data[key] if v is not None]
        for v in data.values():
            if isinstance(v, list) and v and all(isinstance(x, (int, float))
                                                 for x in v):
                return [float(x) for x in v]
        raise SystemExit(f"{path}: no numeric metric found")
    return [float(v) for v in data if v is not None]


def _report(name: str, values: Sequence[float]) -> None:
    lo, hi = bootstrap_ci(values)
    p, wlo, whi = wilson_interval(len(values), len(values)) if values else (0, 0, 0)
    print(f"\n{name}  n={len(values)}")
    if values:
        print(f"  mean {statistics.mean(values):.4f}  sd {statistics.stdev(values):.4f}"
              if len(values) > 1 else f"  value {values[0]:.4f}")
        print(f"  median {statistics.median(values):.4f}  "
              f"min {min(values):.4f}  max {max(values):.4f}")
        print(f"  bootstrap 95% CI  [{lo:.4f}, {hi:.4f}]")


def _demo() -> None:
    """Three synthetic cases with known answers, so the implementation can be
    checked without spending a GPU hour (R10: a test that only confirms the
    assumptions of the code just written proves nothing)."""
    print("=== bootstrap_ci on a constant sample ===")
    lo, hi = bootstrap_ci([5.0] * 12)
    print(f"  constant 5.0 x12  ->  [{lo:.4f}, {hi:.4f}]  (must be exactly 5.0)")

    print("\n=== cliffs_delta on known separations ===")
    print(f"  [1..10] vs [11..20] -> {cliffs_delta(list(range(1,11)), list(range(11,21))):+.3f}  (a<b, must be -1.000)")
    print(f"  [11..20] vs [1..10] -> {cliffs_delta(list(range(11,21)), list(range(1,11))):+.3f}  (a>b, must be +1.000)")
    print(f"  [1..10] vs [1..10]  -> {cliffs_delta(list(range(1,11)), list(range(1,11))):+.3f}  (must be  0.000)")

    print("\n=== wilson_interval near p=1 (where the normal approximation fails) ===")
    for k, n in ((15, 15), (14, 15), (10, 15)):
        p, lo, hi = wilson_interval(k, n)
        print(f"  {k}/{n}  p={p:.3f}  CI [{lo:.3f}, {hi:.3f}]")

    print("\n=== noise_ratio: a real shift, at three sample sizes ===")
    print("  (a real 1.25-SD effect must read as undetectable at n=3 and")
    print("   detectable at n=40 — that is the point of the two ratios)")
    rng = random.Random(7)
    a15 = [rng.gauss(0.73, 0.08) for _ in range(15)]
    a40 = [rng.gauss(0.73, 0.08) for _ in range(40)]
    for n_a, n_b, label in ((3, 3, "n=3/arm"), (15, 15, "n=15/arm"), (40, 40, "n=40/arm")):
        aa = a15[:n_a] if n_a <= 15 else a40[:n_a]
        bb = ([rng.gauss(0.73, 0.08) for _ in range(n_a)],
              [rng.gauss(0.83, 0.08) for _ in range(n_a)])[1]
        r = noise_ratio(aa, bb)
        print(f"  shifted +0.10, {label:<9} effect={r['effect_sd']:+.3f} sd  "
              f"detect={r['detectability']:.2f}  -> {r['verdict']}")

    print("\n=== holm on three p-values, one genuinely small ===")
    res = holm({"real": 0.001, "borderline": 0.02, "null": 0.4})
    for k, v in res.items():
        print(f"  {k:<12} p={v['p']:.3f}  holm={v['p_holm']:.4f}  "
              f"significant={v['significant']}")

    print("\n=== reproducibility: same data, same seed, same CI ===")
    c1 = bootstrap_ci(a15)
    c2 = bootstrap_ci(a15)
    print(f"  {c1} == {c2}  -> {c1 == c2}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("a", nargs="?", help="JSON file of per-run values (arm A)")
    ap.add_argument("b", nargs="?", help="JSON file of per-run values (arm B)")
    ap.add_argument("--demo", action="store_true",
                    help="self-check against cases with known answers")
    args = ap.parse_args()

    if args.demo:
        _demo()
        return 0
    if not args.a:
        ap.print_help()
        return 2

    a = _load(args.a)
    _report(args.a, a)
    if args.b:
        b = _load(args.b)
        _report(args.b, b)
        r = noise_ratio(a, b)
        print("\ncomparison")
        print("-" * 60)
        print(f"  n                    {r['n_a']} vs {r['n_b']}")
        print(f"  mean difference      {r['diff']:+.4f}")
        print(f"  pooled within-arm sd {r['pooled_sd']:.4f}")
        print(f"  se of difference     {r['se_diff']:.4f}")
        print(f"  effect               {r['effect_sd']:+.3f} sd")
        print(f"  detectability        {r['detectability']:.2f}  (>=1.96 to be established)")
        print(f"  Welch p              {r['welch_p']:.4f}")
        print(f"  Cliff's delta        {r['cliffs_delta']:+.3f}")
        print(f"  verdict              {r['verdict']}")
        if r["detectability"] < 1.96:
            print("\n  NOTE: not established at this n. Report the null; do not re-run")
            print("  with more repeats hunting for a difference, which is exactly the")
            print("  multiple-comparisons trap this programme is designed to avoid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
