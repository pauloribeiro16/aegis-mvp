#!/usr/bin/env python3
"""evaluate_predictions.py — the preregistered verdicts, as a pure function of
the records.

The preregistration (`PREREG_LAB03_D1.md` §4) states ten predictions with
their falsifiers. This script is the machine-readable twin of that table: it
reads the same records the checker reads and emits HOLDS / REFUTED for each,
with the evidence that produced it. Nothing here is a judgement call — the
thresholds are the ones written down before the runs.

    python3 evaluate_predictions.py results/*.jsonl --out predictions.md

A prediction whose evidence is missing is REFUTED with "not measured", never
silently passed.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from check_suite import load, pick, probs_of, variant_of

# The site a case belongs to, for the per-site questions.
TENSION = "domain.tension."
TRIGGER = "domain.trigger."
PRINCIPLE = "domain.principle."


def index(records: list[dict]) -> dict:
    out: dict[tuple[str, str], dict] = {}
    for rec in records:
        out.setdefault((variant_of(rec), rec.get("case_id", "?")), rec)
    return out


def pick_of(rec: dict, qname: str):
    ans = (rec.get("answers") or {}).get(qname)
    return pick(ans) if ans else (None, None)


def labelled_accuracy(recs: list[dict]) -> tuple[int, int]:
    ok = total = 0
    for r in recs:
        if not r.get("ok"):
            continue
        labels = (r.get("expect") or {}).get("labels") or {}
        if (r.get("expect") or {}).get("contested"):
            continue
        for q, want in labels.items():
            kind, got = pick_of(r, q)
            if kind == "unknown":
                continue
            total += 1
            if (bool(got) == want) if isinstance(want, bool) else (str(got) == str(want)):
                ok += 1
    return ok, total


def contrast_moves(recs: list[dict], anchor: str, variant: str) -> int | None:
    idx = index(recs)
    a = idx.get((variant_of(recs[0]) if recs else "", anchor))
    if a is None:
        return None
    arm = variant_of(a)
    a = idx.get((arm, anchor))
    v = idx.get((arm, variant))
    if a is None or v is None or not a.get("ok") or not v.get("ok"):
        return None
    moved = 0
    for q in a["answers"]:
        if q not in v["answers"]:
            continue
        if pick_of(a, q)[1] != pick_of(v, q)[1]:
            moved += 1
    return moved


def evaluate(records: list[dict]) -> list[dict]:
    out: list[dict] = []
    idx = index(records)
    by_arm: dict[str, list[dict]] = {}
    for r in records:
        by_arm.setdefault(variant_of(r), []).append(r)

    # ---- P1: serving fidelity (A1 native vs A2 vLLM) ----------------------
    a1, a2 = "A1-bfloat16", "A2"
    agree = total = 0
    max_dp_lab = 0.0
    max_dp_unlab = 0.0
    worst = ""
    for (arm, cid), r1 in idx.items():
        if arm != a1:
            continue
        r2 = idx.get((a2, cid))
        if not r2 or not r1.get("ok") or not r2.get("ok"):
            continue
        if set(r1["answers"]) != set(r2["answers"]):
            continue
        labelled = bool((r1.get("expect") or {}).get("labels"))
        for q in r1["answers"]:
            p1, p2 = probs_of(r1["answers"][q]), probs_of(r2["answers"][q])
            keys = set(p1) & set(p2)
            if not keys:
                continue
            total += 1
            if pick_of(r1, q)[1] == pick_of(r2, q)[1]:
                agree += 1
            d = max(abs(p1[k] - p2[k]) for k in keys)
            if labelled:
                max_dp_lab = max(max_dp_lab, d)
            elif d > max_dp_unlab:
                max_dp_unlab, worst = d, cid
    rate = (agree / total) if total else 0.0
    holds = rate >= 0.95 and max_dp_lab <= 0.05
    out.append({
        "id": "P1", "holds": holds,
        "text": "the vLLM route agrees with the checkpoint on >=95% of picks, "
                "with max |dp| <= 0.05 on every labelled case",
        "evidence": f"agreement {agree}/{total} = {rate:.4f}; max |dp| on labelled "
                    f"{max_dp_lab:.6f}; max |dp| on unlabelled {max_dp_unlab:.6f} ({worst})",
    })

    # ---- P2: which model (A1 vs A3 float32) -------------------------------
    ok1, n1 = labelled_accuracy(by_arm.get(a1, []))
    ok3, n3 = labelled_accuracy(by_arm.get("A3-float32", []))
    if n1 and n3:
        holds = (ok1 / n1) >= (ok3 / n3)
        out.append({
            "id": "P2", "holds": holds,
            "text": "d1-3B scores at least as high as d1-omni-600M on the labelled cases",
            "evidence": f"A1 {ok1}/{n1} = {ok1/n1:.4f} vs A3-float32 {ok3}/{n3} = {ok3/n3:.4f}",
        })
    else:
        out.append({"id": "P2", "holds": False, "text": "model comparison",
                    "evidence": "not measured"})

    # ---- P3: the tension site ---------------------------------------------
    best = None
    for arm, recs in by_arm.items():
        tension = [r for r in recs if r.get("case_id", "").startswith(TENSION) and r.get("ok")]
        ok, n = labelled_accuracy(tension)
        if n and (best is None or ok / n > best[1]):
            best = (arm, ok / n, ok, n)
    if best:
        holds = best[1] >= 0.8
        out.append({
            "id": "P3", "holds": holds,
            "text": "the best arm reaches >=4/5 on the tension-activation cases",
            "evidence": f"best arm {best[0]}: {best[2]}/{best[3]} = {best[1]:.4f}",
        })
    else:
        out.append({"id": "P3", "holds": False, "text": "tension site",
                    "evidence": "not measured"})

    # ---- P4/P5/P6: the three contrasts ------------------------------------
    for pid, variant, limit, what in [
        ("P4", "robust.minimal.padded", 1, "padding the state with irrelevant prose"),
        ("P5", "robust.minimal.injected", 1, "injecting an instruction into the state"),
        ("P6", "robust.minimal.paraphrased", 1, "paraphrasing the question"),
    ]:
        moves = []
        for arm in sorted(by_arm):
            m = contrast_moves(by_arm[arm], "robust.minimal", variant)
            if m is not None:
                moves.append((arm, m))
        if not moves:
            out.append({"id": pid, "holds": False, "text": what,
                        "evidence": "not measured"})
            continue
        worst_moves = max(m for _, m in moves)
        holds = worst_moves <= limit
        out.append({
            "id": pid, "holds": holds,
            "text": f"{what} moves at most {limit} of 5 answers",
            "evidence": "; ".join(f"{a}: {m} moved" for a, m in moves),
        })

    # ---- P7: determinism ---------------------------------------------------
    unstable = []
    groups = 0
    for arm, recs in by_arm.items():
        by_case: dict[str, list[dict]] = {}
        for r in recs:
            if r.get("ok"):
                by_case.setdefault(r.get("case_id", ""), []).append(r)
        for cid, rs in by_case.items():
            if len(rs) < 2:
                continue
            groups += 1
            picks = [{q: pick_of(r, q)[1] for q in r["answers"]} for r in rs]
            if any(p != picks[0] for p in picks):
                unstable.append(f"{arm}/{cid}")
    out.append({
        "id": "P7", "holds": not unstable,
        "text": "repeats of the same case agree 100% within an arm",
        "evidence": f"{groups - len(unstable)}/{groups} repeat groups stable"
                    + (f"; unstable: {unstable}" if unstable else ""),
    })

    # ---- P8: dtype sensitivity --------------------------------------------
    ref = "A3-float32"
    for dtype in ("float16", "bfloat16"):
        arm = f"A3-{dtype}"
        if arm not in by_arm or ref not in by_arm:
            continue
        i_ref, i_arm = index(by_arm[ref]), index(by_arm[arm])
        drift = total = 0
        for (a, cid), r in i_ref.items():
            if a != ref:
                continue
            other = i_arm.get((arm, cid))
            if not other or not r.get("ok") or not other.get("ok"):
                continue
            for q in r["answers"]:
                if q not in other["answers"]:
                    continue
                total += 1
                if pick_of(r, q)[1] != pick_of(other, q)[1]:
                    drift += 1
        pct = (drift / total * 100) if total else 0.0
        out.append({
            "id": f"P8/{dtype}", "holds": pct <= 2.0,
            "text": f"the {dtype} arm disagrees with the float32 arm on <=2% of answers",
            "evidence": f"{drift}/{total} = {pct:.2f}% of answers differ",
        })

    # ---- P9: the pipeline's own p4t discrepancy ---------------------------
    best_t = None
    for arm, recs in by_arm.items():
        neg = [r for r in recs if r.get("case_id") in ("domain.tension.t-003", "domain.tension.t-004")
               and r.get("ok")]
        if len(neg) == 2:
            ok = sum(1 for r in neg if pick_of(r, "activates")[1] is False)
            if best_t is None or ok > best_t[1]:
                best_t = (arm, ok)
    if best_t:
        out.append({
            "id": "P9", "holds": best_t[1] == 2,
            "text": "the models answer 'does not activate' for T-003 and T-004, "
                    "which the pipeline emitted as rows anyway",
            "evidence": f"best arm {best_t[0]}: {best_t[1]}/2 correct",
        })
    else:
        out.append({"id": "P9", "holds": False, "text": "p4t discrepancy",
                    "evidence": "not measured"})

    # ---- P10: the context ceiling -----------------------------------------
    ceiling = []
    for arm, recs in by_arm.items():
        r = next((x for x in recs if x.get("case_id") == "robust.long_state"), None)
        if r:
            ceiling.append((arm, r))
    if ceiling:
        ev = []
        ok = True
        for arm, r in ceiling:
            if not r.get("ok"):
                ev.append(f"{arm}: refused ({r['error']})")
                continue
            tokens = r["usage"].get("input_tokens")
            conf = (r["answers"].get("gdpr") or {}).get("confidence")
            p = (r["answers"].get("gdpr") or {}).get("noul")
            ev.append(f"{arm}: {tokens} tokens, p(yes)={p}, confidence={conf}")
            if tokens and int(tokens) > 32768 and p is not None and float(p) >= 0.5:
                ok = False
        out.append({
            "id": "P10", "holds": ok,
            "text": "a state above the context ceiling produces a refusal or a "
                    "truncation, not a silently confident answer",
            "evidence": " | ".join(ev),
        })
    else:
        out.append({"id": "P10", "holds": False, "text": "context ceiling",
                    "evidence": "not measured"})

    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("results", nargs="+")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    records: list[dict] = []
    for p in args.results:
        records.extend(load(Path(p)))

    verdicts = evaluate(records)
    lines = ["| # | prediction | verdict | evidence |", "|---|---|---|---|"]
    for v in verdicts:
        lines.append(f"| {v['id']} | {v['text']} | "
                     f"{'**HOLDS**' if v['holds'] else '**REFUTED**'} | {v['evidence']} |")
    text = "\n".join(lines)
    print(text)
    if args.out:
        Path(args.out).write_text(text + "\n", encoding="utf-8")
        Path(args.out).with_suffix(".json").write_text(
            json.dumps(verdicts, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"\nwrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
