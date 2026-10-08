#!/usr/bin/env python3
"""exp_m11_implication.py — the preregistered M11 metrics.

Same construct as M10 Leg C, computed on the M11 cells: for each arm, how far
apart are two companies' `Company implication` for the same duty, against a
placebo of a genuinely different duty under the same company.

    python3 scripts/exp_m11_implication.py \
        run_m11_c2_ctrl run_m11_c3_ctrl run_m11_c2_concrete run_m11_c3_concrete

Predictions (PREREG_M11 §5):
  Q1  implication cross-company - placebo  >= +0.10 on >= 1 case
  Q2  modal-string share of the Adjustment column < 0.80 on >= 1 case
  Q3  concrete carries >= ctrl sub-domains on both cases
  Q4  concrete produces <= ctrl check_grounded fabrications on both cases
"""
from __future__ import annotations

import itertools
import json
import statistics
import sys
from collections import Counter, defaultdict
from difflib import SequenceMatcher
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "pipeline" / "src"))
from quality import norm  # noqa: E402

RUNS = Path.home() / "Work" / "aegis-runs"
Q1_TARGET, Q2_TARGET, Q3_Q4 = +0.10, 0.80, True


def sim(a: str, b: str) -> float:
    return SequenceMatcher(None, norm(a), norm(b)).ratio() if a and b else 0.0


def load(run_id: str):
    d = RUNS / run_id
    rows = []
    for f in sorted((d / "steps" / "goals").glob("*.json")):
        sd = f.name[:-5].replace("_", ".")
        for row in json.loads(f.read_text(encoding="utf-8")).get("goals", []):
            rows.append({"sd": sd, "regulation": row.get("regulation"),
                         "goal": row.get("goal", ""),
                         "implication": row.get("implication", ""),
                         "adjustment": row.get("adjustment", "")})
    ov = {}
    cfg = d / "config.json"
    if cfg.exists():
        ov = json.loads(cfg.read_text(encoding="utf-8")).get("ficha_overrides") or {}
    return rows, ov


def divergence(rows: list[dict], field: str) -> tuple:
    """Cross-company for the same (sd, regulation), minus the different-duty placebo."""
    cell: dict = defaultdict(list)
    placebo: dict = defaultdict(list)
    for r in rows:
        cell[(r["sd"], r["regulation"])].append(r[field])
        placebo["all"].append((r["sd"], r["regulation"], r[field]))
    cross = [sim(a, b) for items in cell.values()
             for a, b in itertools.combinations(items, 2)]
    plc = [sim(a[2], b[2]) for a, b in itertools.combinations(placebo["all"], 2)]
    if not cross or not plc:
        return None, None, len(cross), len(plc)
    return statistics.median(cross), statistics.median(plc), len(cross), len(plc)


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    runs = {r: load(r) for r in sys.argv[1:]}
    arms = defaultdict(dict)
    for name, (rows, ov) in runs.items():
        case = "c2" if "_c2_" in name else "c3"
        arm = ov.get("p4_implication") or "ctrl"
        arms[arm][case] = rows

    print("=" * 84)
    print("M11 — Company implication intervention (PREREG_M11, frozen 2026-10-08)")
    print("=" * 84)

    for arm, by_case in arms.items():
        if len(by_case) < 2:
            print(f"\narm {arm}: needs both cases, has {sorted(by_case)}")
            continue
        a_rows = by_case.get("c2", [])
        b_rows = by_case.get("c3", [])
        print(f"\n--- arm {arm}  (C2 {len(a_rows)} rows · C3 {len(b_rows)} rows) ---")
        for field, label in (("implication", "Company implication"),
                             ("goal", "Adjusted goal")):
            combined = a_rows + b_rows
            cross, plc, nc, npc = divergence(combined, field)
            if cross is None:
                print(f"  {label:<22} not computable")
                continue
            print(f"  {label:<22} cross={cross:.3f} (n={nc})  placebo={plc:.3f} "
                  f"(n={npc})  difference={cross - plc:+.3f}")
        strings = [r["adjustment"] for r in a_rows + b_rows]
        modal, n = Counter(strings).most_common(1)[0]
        print(f"  {'Adjustment modal share':<22} {n / len(strings):.0%} "
              f"({len(set(strings))} distinct)  {modal[:44]!r}")

    # delivery and fabrication counts, per run
    print()
    print(f"  {'run':<34}{'carried':>9}{'rows':>7}{'modal%':>8}{'fabrications':>14}")
    for name, (rows, _) in sorted(runs.items()):
        strings = [r["adjustment"] for r in rows]
        modal, n = Counter(strings).most_common(1)[0] if strings else ("", 0)
        fabs = 0
        trace = RUNS / name / "trace.jsonl"
        if trace.exists():
            for line in trace.read_text(encoding="utf-8").splitlines():
                if not line.strip():
                    continue
                rec = json.loads(line)
                err = str(rec.get("l0_first_error", ""))
                fabs += err.count("company quantity not traceable")
        print(f"  {name:<34}{len({r['sd'] for r in rows}):>9}{len(rows):>7}"
              f"{(n / len(strings) if strings else 0):>7.0%}{fabs:>14}")

    # verdicts
    print()
    print("=" * 84)
    print("VERDICTS (PREREG_M11 §5)")
    print("=" * 84)
    def div(arm, field="implication"):
        rows = arms[arm].get("c2", []) + arms[arm].get("c3", [])
        c, p, _, _ = divergence(rows, field)
        return None if c is None else c - p

    q1 = {a: div(a) for a in arms}
    print(f"  Q1 implication divergence: " +
          ", ".join(f"{a}={v:+.3f}" if v is not None else f"{a}=n/a"
                    for a, v in q1.items()))
    fire1 = any(v is not None and v >= Q1_TARGET for v in q1.values())
    print(f"     (target >= {Q1_TARGET:+.2f} on >= 1 case)  -> {'FIRED' if fire1 else 'NOT FIRED'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())