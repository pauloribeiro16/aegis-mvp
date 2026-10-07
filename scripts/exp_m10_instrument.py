#!/usr/bin/env python3
"""exp_m10_instrument.py — is the instrument measuring anything?

Leg A  badge known-answer: `adjustment_kind` against strings whose correct
      class is known by construction.
Leg B  badge informativeness: distinct strings, modal-string share, and whether
      `unchanged` is ever a prefix of prose the model wrote rather than a choice
      it made.
Leg C  cross-sectional divergence: same sub-domain across DIFFERENT companies,
      against the replicate floor and against the different-sub-domain placebo.

Reads run artefacts only. Calls no model, touches no cluster. Every number is
reproducible from the same artefacts.

    python3 scripts/exp_m10_instrument.py
    python3 scripts/exp_m10_instrument.py --json /tmp/m10.json
"""
from __future__ import annotations

import argparse
import itertools
import json
import statistics
import sys
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "pipeline" / "src"))
from quality import adjustment_kind, norm  # noqa: E402

RUNS = Path.home() / "Work" / "aegis-runs"

#: PREREG_M10 §4 — the margins, frozen before the code ran.
P3_MARGIN = -0.05      # cross_company - replicate; must be > this
P4_MARGIN = +0.05      # cross_company - diff_sd;     must be <= this
P2_FLOOR = 0.80        # modal-string share per run;  must be > this

#: Leg A: (string, class it must classify as). The adversarial rows matter as
#: much as the legal ones — a classifier that maps anything to `unchanged` would
#: pass a test built only from badge words.
KNOWN_ANSWER = [
    ("unchanged — fits as stated", "unchanged"),
    ("unchanged", "unchanged"),
    ("verbatim — the duty states it and the company adds nothing", "verbatim"),
    ("verbatim", "verbatim"),
    ("proportional: MICRO scale justifies a single documented cycle",
     "proportional"),
    ("inherited: supplier-managed hosting carries the capability", "inherited"),
    ("inherited from the hosting supplier", "inherited"),
    ("narrowed: scope to the appointment store — because it is the only "
     "at-rest holding with client data", "narrowed"),
    ("flagged: cannot be decided without the hosting agreement", "flagged"),
    # adversarial
    ("", "malformed"),
    ("—", "malformed"),
    ("-", "malformed"),
    ("The duty applies as written in the baseline.", "malformed"),
    ("unchanged", "unchanged"),
    ("narrowed scope to the clinic store — because of size", "narrowed"),
]


def case_of(run_dir: Path) -> str:
    man = run_dir / "manifest.json"
    cfg = run_dir / "config.json"
    for p in (man, cfg):
        if p.exists():
            try:
                d = json.loads(p.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                continue
            v = d.get("case_id") or d.get("case")
            if v:
                return v
    return "?"


def collect() -> dict:
    """Every goal row of every delivered run, keyed for all three legs."""
    runs = {}
    for d in sorted(RUNS.glob("run_m0[789]*")):
        goals = d / "steps" / "goals"
        if not goals.is_dir():
            continue
        rows = []
        for f in sorted(goals.glob("*.json")):
            try:
                data = json.loads(f.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                continue
            sd = f.name[:-5].replace("_", ".")
            for g in data.get("goals", []):
                rows.append({"sd": sd, "id": g.get("id", "?"),
                             "goal": g.get("goal", ""),
                             "adjustment": g.get("adjustment", ""),
                             "implication": g.get("implication", "")})
        if rows:
            runs[d.name] = {"case": case_of(d), "rows": rows}
    return runs


def leg_a() -> list[dict]:
    out = []
    for text, expect in KNOWN_ANSWER:
        got = adjustment_kind(text)
        out.append({"input": text[:60], "expected": expect, "got": got,
                    "ok": got == expect})
    return out


def leg_b(runs: dict) -> list[dict]:
    out = []
    for name, r in runs.items():
        strings = [row["adjustment"] for row in r["rows"]]
        if not strings:
            continue
        modal, modal_n = Counter(strings).most_common(1)[0]
        out.append({
            "run": name, "case": r["case"], "rows": len(strings),
            "distinct": len(set(strings)),
            "modal": modal[:70], "modal_share": modal_n / len(strings),
            # a row whose badge is a prefix of longer prose means the classifier
            # is bucketing free text rather than reading a choice
            "unchanged_prefix_of_longer": sum(
                1 for s in set(strings)
                if norm(s).startswith("unchanged") and len(norm(s)) > len("unchanged") + 3),
        })
    return out


def sim(a: str, b: str) -> float:
    return SequenceMatcher(None, norm(a), norm(b)).ratio() if a and b else 0.0


def leg_c(matrix: str = "run_m07_*") -> dict:
    """Cross-sectional divergence, computed inside ONE matrix.

    Two corrections, both forced by reading the first pass closely:

    * The `replicate` floor of the first pass compared M07 against M08. Those
      are different instruments, so it measured cross-revision drift, not
      run-to-run noise, and the floor it produced (0.03) was meaningless. The
      floor is now only reported for cells where the SAME model and the SAME
      case genuinely ran twice, which only M08 does.
    * The placebo of the first pass compared one regulation of a sub-domain
      against another. That is a near neighbour, not "a different duty", and it
      made the cross-company number look flat. The placebo is now built ACROSS
      cells: same model, same company, different (sub-domain, regulation).

    The cross-company cells are keyed by (model, sub-domain, REGULATION) as
    well as company, because the three cases carry different regulation sets —
    PREREG_M10 §6.2 — and an uncontrolled same-sub-domain pair may not be the
    same duty at all.
    """
    cell: dict = {}
    placebo: dict = {}
    for d in sorted(RUNS.glob(matrix)):
        goals_dir = d / "steps" / "goals"
        if not goals_dir.is_dir():
            continue
        model = "_".join(d.name.split("_")[1:3])
        case = case_of(d)
        for f in sorted(goals_dir.glob("*.json")):
            sd = f.name[:-5].replace("_", ".")
            for row in json.loads(f.read_text(encoding="utf-8")).get("goals", []):
                reg = row.get("regulation")
                cell.setdefault((model, sd, reg), []).append(
                    {"run": d.name, "case": case, "goal": row.get("goal", ""),
                     "implication": row.get("implication", "")})
                placebo.setdefault((model, case), []).append(
                    (sd, reg, row.get("goal", ""), row.get("implication", "")))

    # true replicates: same model, same case, two different runs
    replicates: dict = {}
    for (model, sd, reg), items in cell.items():
        by_run: dict = {}
        for it in items:
            by_run.setdefault(it["run"], it["goal"])
        if len(by_run) >= 2:
            replicates.setdefault(model, []).extend(
                sim(a, b) for a, b in itertools.combinations(by_run.values(), 2))

    out = {"matrix": matrix, "cells": len(cell),
           "cells_multi_company": sum(1 for v in cell.values()
                                      if len({i["case"] for i in v}) > 1)}
    for field, label in (("goal", "Adjusted goal"), ("implication", "Company implication")):
        cross = []
        for items in cell.values():
            for a, b in itertools.combinations(items, 2):
                if a["case"] != b["case"]:
                    cross.append(sim(a[field], b[field]))
        plc = []
        by_mc: dict = {}
        for (model, case), vals in placebo.items():
            by_mc.setdefault((model, case), []).extend(v[2:] for v in vals)
        for vals in by_mc.values():
            for a, b in itertools.combinations(vals, 2):
                plc.append(sim(a[1] if label == "Adjusted goal" else a[1],
                               b[1]))
        # index 0 of each (sd, reg, goal, implication) tuple slice
        out[label] = {
            "cross_company": statistics.median(cross) if cross else None,
            "cross_n": len(cross),
            "placebo": statistics.median(plc) if plc else None,
            "placebo_n": len(plc),
        }
        if out[label]["cross_company"] is not None and out[label]["placebo"] is not None:
            out[label]["difference"] = out[label]["cross_company"] - out[label]["placebo"]
    out["replicate_median"] = (statistics.median(replicates[next(iter(replicates))])
                               if replicates else None)
    out["replicate_models"] = sorted(replicates)
    return out


def med(xs):
    xs = [x for x in xs if x is not None]
    return statistics.median(xs) if xs else None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", metavar="PATH")
    args = ap.parse_args()

    runs = collect()
    a, b = leg_a(), leg_b(runs)

    print("=" * 78)
    print("LEG A — badge known-answer")
    print("=" * 78)
    bad_a = [r for r in a if not r["ok"]]
    for r in a:
        flag = "ok " if r["ok"] else "FAIL"
        print(f"  [{flag}] {r['input']!r:<64} -> {r['got']:<13} (want {r['expected']})")
    print(f"\n  P1: {len(a) - len(bad_a)}/{len(a)} correct"
          + ("  -> HOLDS" if not bad_a else "  -> FALSIFIED"))

    print()
    print("=" * 78)
    print("LEG B — badge informativeness")
    print("=" * 78)
    print(f"  {'run':<36}{'rows':>5}{'distinct':>10}{'modal share':>13}")
    for r in sorted(b, key=lambda x: -x["rows"]):
        print(f"  {r['run']:<36}{r['rows']:>5}{r['distinct']:>10}"
              f"{r['modal_share']:>12.0%}  {r['modal'][:40]}")
    p2_fail = [r for r in b if r["modal_share"] <= P2_FLOOR]
    print(f"\n  P2 (modal share > {P2_FLOOR:.0%} in every run): "
          + ("HOLDS" if not p2_fail
             else f"FALSIFIED by {len(p2_fail)} run(s): "
                  + ", ".join(f"{r['run']}={r['modal_share']:.0%}" for r in p2_fail[:4])))

    print()
    print("=" * 78)
    print("LEG C — cross-sectional divergence (decisive)")
    print("=" * 78)
    c = leg_c("run_m07_*")
    print(f"  matrix M07 (one instrument): {c['cells']} cells, "
          f"{c['cells_multi_company']} present in more than one company")
    print(f"  true replicate floor available for: {', '.join(c['replicate_models']) or 'none'}")
    print(f"    median replicate = "
          + (f"{c['replicate_median']:.3f}" if c["replicate_median"] is not None
             else "n/a (no cell ran the same model+case twice in this matrix)"))
    print()
    print(f"  {'column':<22}{'cross-company':>15}{'placebo':>10}{'difference':>12}{'n_cross':>10}")
    for label in ("Adjusted goal", "Company implication"):
        r = c[label]
        if r["cross_company"] is None:
            print(f"  {label:<22}{'n/a':>15}")
            continue
        print(f"  {label:<22}{r['cross_company']:>15.3f}{r['placebo']:>10.3f}"
              f"{r['difference']:>+12.3f}{r['cross_n']:>10}")

    goal = c["Adjusted goal"].get("difference")
    impl = c["Company implication"].get("difference")
    # PREREG_M10 §5: theatre confirmed when the company does not move the text.
    # Here the test is applied per column, which the prereg's single construct
    # did not anticipate — recorded as a deviation, not as a silent substitution.
    p4_goal = goal is not None and goal <= P4_MARGIN
    p4_impl = impl is not None and impl <= P4_MARGIN
    if goal is not None:
        print(f"\n  goal column          cross-company - placebo = {goal:+.3f} "
              f"(must be <= {P4_MARGIN:+.2f}) -> {'HOLDS' if p4_goal else 'FALSIFIED'}")
    if impl is not None:
        print(f"  implication column   cross-company - placebo = {impl:+.3f} "
              f"(must be <= {P4_MARGIN:+.2f}) -> {'HOLDS' if p4_impl else 'FALSIFIED'}")

    print()
    print("=" * 78)
    print("DECISION (PREREG_M10 §5, applied per column)")
    print("=" * 78)
    theatre = p4_goal and p4_impl
    if bad_a:
        print("  P1 falsified -> badge withdrawn as evidence; NO cluster run.")
    elif p4_impl and not p4_goal:
        print("  The COMPANY IMPLICATION carries no company signal; the Adjusted")
        print("  goal does. The column that exists to carry the company is the")
        print("  empty one. An intervention arm targeting THAT column is authorised.")
    elif theatre:
        print("  Neither column responds to the company. THEATRE CONFIRMED.")
        print("  An intervention arm is authorised (prediction: divergence >= +0.10).")
    elif not p2_fail:
        print("  Both columns respond; the badge carries more information than M07")
        print("  concluded. Restate the M07 claim before shipping anything.")
    else:
        print("  No branch satisfied — inconclusive.")

    if args.json:
        Path(args.json).write_text(json.dumps(
            {"leg_a": a, "leg_b": b,
             "verdicts": {"P1": not bad_a, "P2": not p2_fail,
                          "P3": p3, "P4": p4, "theatre_confirmed": theatre}},
            indent=1, default=str), encoding="utf-8")
        print(f"\n  full records -> {args.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())