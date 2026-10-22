#!/usr/bin/env python3
"""report.py — compare the arms of the d1 decision-model suite.

    python3 report.py --results results/*.jsonl --out RESULTS_LAB03_D1.md

Two comparisons, kept apart because they answer different questions:

  A1 vs A2   SERVING FIDELITY. Same checkpoint (d1-3B), two routes. vLLM's
             LiquidStrategy rebuilds the checkpoint's prompt and reads
             next-token logprobs; the in-process arm runs the checkpoint's own
             tree-batched forward pass. If they disagree, the SERVER is the
             thing that changed the answer, not the model.

  A1 vs A3   MODEL COMPARISON. Both in-process, so the serving layer is held
             constant and the difference is d1-3B against d1-omni-600M.

  A3 dtype   DTYPE SENSITIVITY. d1-omni was trained in float32; its card warns
             that bfloat16 changes the top answer on ~0.8% of text rows. We
             measure that on our own cases instead of citing it.
"""
from __future__ import annotations

import argparse
import json
import statistics
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from check_suite import load, pick, probs_of, summarise, variant_of  # noqa: E402

ARM_NAMES = {
    "A1": "d1-3B · in-process (transformers)",
    "A2": "d1-3B · vLLM 0.32.0 /v1/systemone",
    "A3": "d1-omni-600M · in-process",
    "A1-bfloat16": "d1-3B · in-process (bfloat16)",
    "A3-float32": "d1-omni-600M · in-process (float32)",
    "A3-float16": "d1-omni-600M · in-process (float16)",
    "A3-bfloat16": "d1-omni-600M · in-process (bfloat16)",
}


def index(records: list[dict]) -> dict:
    """(variant, case_id) -> record, keeping the first repeat of each."""
    out: dict[tuple[str, str], dict] = {}
    for rec in records:
        key = (variant_of(rec), rec.get("case_id", "?"))
        out.setdefault(key, rec)
    return out


def compare(rec_a: dict, rec_b: dict) -> dict:
    """Agreement and probability drift between two arms on the same case."""
    res = {"comparable": False, "agreement": None, "max_abs_dp": None,
           "per_question": [], "notes": []}
    if not rec_a.get("ok") or not rec_b.get("ok"):
        res["notes"].append(
            f"not comparable: a={_short(rec_a)} b={_short(rec_b)}")
        return res
    ans_a = rec_a.get("answers") or {}
    ans_b = rec_b.get("answers") or {}
    if set(ans_a) != set(ans_b):
        res["notes"].append(f"different answer keys: {sorted(ans_a)} vs {sorted(ans_b)}")
        return res

    res["comparable"] = True
    agree = True
    drifts = []
    for qname in sorted(ans_a):
        ka, va = pick(ans_a[qname])
        kb, vb = pick(ans_b[qname])
        same = (ka == kb) and (va == vb)
        agree = agree and same
        pa, pb = probs_of(ans_a[qname]), probs_of(ans_b[qname])
        keys = sorted(set(pa) & set(pb))
        dp = max((abs(pa[k] - pb[k]) for k in keys), default=0.0)
        drifts.append(dp)
        res["per_question"].append({
            "question": qname, "type": ka, "a": va, "b": vb,
            "same_pick": same, "max_abs_dp": round(dp, 6),
            "a_probs": pa, "b_probs": pb,
        })
    res["agreement"] = agree
    res["max_abs_dp"] = round(max(drifts), 6) if drifts else None
    res["mean_abs_dp"] = round(statistics.fmean(drifts), 6) if drifts else None
    return res


def _short(rec: dict) -> str:
    if rec.get("ok"):
        return "answered"
    err = rec.get("error") or {}
    return f"error({err.get('type') or err.get('kind')})"


def pairwise(records: list[dict], pairs: list[tuple[str, str]]) -> dict:
    idx = index(records)
    out = {}
    for a, b in pairs:
        case_ids = sorted({c for (arm, c) in idx if arm == a} & {c for (arm, c) in idx if arm == b})
        rows = []
        for cid in case_ids:
            rows.append({"case_id": cid, **compare(idx[(a, cid)], idx[(b, cid)])})
        comparable = [r for r in rows if r["comparable"]]
        agree = [r for r in comparable if r["agreement"]]
        dps = [r["max_abs_dp"] for r in comparable if r["max_abs_dp"] is not None]
        out[f"{a}_vs_{b}"] = {
            "a": a, "b": b, "cases": len(rows), "comparable": len(comparable),
            "agreement_rate": round(len(agree) / len(comparable), 4) if comparable else None,
            "max_abs_dp": round(max(dps), 6) if dps else None,
            "mean_abs_dp": round(statistics.fmean(dps), 6) if dps else None,
            "rows": rows,
        }
    return out


def contrast_table(records: list[dict], case_files: list[str]) -> dict:
    """Within-arm contrast pairs: does padding the state, injecting into it,
    or paraphrasing the question move the answer?

    A contrast pair is (anchor, variant). The anchor's pick is the baseline;
    the variant is asked the same thing with the state or the wording
    changed. Agreement here is what the System-1 documentation's jaggedness
    claims (irrelevant content, prompt injection, literal reading) predict
    or deny on OUR content."""
    pairs: dict[tuple[str, str], str] = {}
    notes: dict[str, str] = {}
    for path in case_files:
        try:
            data = json.loads(Path(path).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        for case in data.get("cases", []):
            if case.get("contrast"):
                pairs[(case["contrast"], case["id"])] = case["contrast"]
                notes[case["id"]] = case.get("contrast_note", "")

    idx = index(records)
    arms = sorted({a for (a, _) in idx})
    out: dict[str, list] = {}
    for arm in arms:
        rows = []
        for (anchor, variant), _ in pairs.items():
            ra, rv = idx.get((arm, anchor)), idx.get((arm, variant))
            if ra is None or rv is None:
                continue
            if not ra.get("ok") or not rv.get("ok"):
                rows.append({"anchor": anchor, "variant": variant, "comparable": False,
                             "note": notes.get(variant, "")})
                continue
            pa = {q: pick(a) for q, a in (ra.get("answers") or {}).items()}
            pv = {q: pick(a) for q, a in (rv.get("answers") or {}).items()}
            drifted = [q for q in sorted(set(pa) & set(pv)) if pa[q] != pv[q]]
            rows.append({
                "anchor": anchor, "variant": variant, "comparable": True,
                "same": not drifted, "drifted_questions": drifted,
                "anchor_picks": {q: pa[q][1] for q in sorted(pa)},
                "variant_picks": {q: pv[q][1] for q in sorted(pv)},
                "note": notes.get(variant, ""),
            })
        out[arm] = rows
    return out


# Which decision site a case belongs to. The overall accuracy number hides
# what actually happened: a set that is 35 positives and 3 negatives can be
# scored by a model that answers "no" to everything, and the site table is
# what makes that visible.
SITES = [
    ("domain.tension.", "tension activation"),
    ("domain.trigger.", "sub-domain trigger"),
    ("domain.principle.", "principle constraint"),
    ("domain.coverage.", "coverage verdict"),
    ("domain.adjustment.", "adjustment (unlabelled)"),
    ("robust.minimal", "regulation applicability"),
    ("robust.repeat5", "regulation applicability (repeats)"),
]


def site_of(case_id: str) -> str:
    for prefix, name in SITES:
        if case_id.startswith(prefix):
            return name
    return "protocol / other"


def site_table(records: list[dict], arm: str | None = None) -> list[dict]:
    """Per site: accuracy, the label distribution and the pick distribution.

    A model that answers "no" to every boolean scores 50 % on a balanced set
    and 7 % on a 35/3 set. The label and pick distributions say which one
    happened; the accuracy alone does not.
    """
    sites: dict[str, dict] = {}
    for rec in records:
        if not rec.get("ok"):
            continue
        if arm is not None and variant_of(rec) != arm:
            continue
        site = site_of(rec.get("case_id", ""))
        d = sites.setdefault(site, {"site": site, "labelled": 0, "correct": 0,
                                    "contested": 0, "label_T": 0, "label_F": 0,
                                    "pick_T": 0, "pick_F": 0, "nonbool": 0,
                                    "nonbool_correct": 0})
        labels = (rec.get("expect") or {}).get("labels") or {}
        contested = bool((rec.get("expect") or {}).get("contested"))
        answers = rec.get("answers") or {}
        for q, want in labels.items():
            ans = answers.get(q)
            if ans is None:
                continue
            kind, got = pick(ans)
            if contested:
                d["contested"] += 1
                continue
            if kind == "unknown":
                continue
            d["labelled"] += 1
            if isinstance(want, bool):
                d["label_T" if want else "label_F"] += 1
                d["pick_T" if bool(got) else "pick_F"] += 1
                if bool(got) == want:
                    d["correct"] += 1
            else:
                d["nonbool"] += 1
                if str(got) == str(want):
                    d["nonbool_correct"] += 1
                    d["correct"] += 1
    rows = []
    for d in sites.values():
        total = d["label_T"] + d["label_F"]
        d["accuracy"] = round(d["correct"] / d["labelled"], 4) if d["labelled"] else None
        d["label_distribution"] = f"{d['label_T']}T/{d['label_F']}F" if total else "—"
        d["pick_distribution"] = f"{d['pick_T']}T/{d['pick_F']}F" if total else "—"
        if total:
            bias = max(d["pick_T"], d["pick_F"]) / total
            d["one_sided"] = bias >= 0.9
        else:
            d["one_sided"] = False
        rows.append(d)
    return sorted(rows, key=lambda r: r["site"])


def accuracy_table(records: list[dict]) -> list[dict]:
    """Per case: each arm's pick and whether it matched the label."""
    idx = index(records)
    arms = sorted({a for (a, _) in idx})
    cases = sorted({c for (_, c) in idx})
    rows = []
    for cid in cases:
        row = {"case_id": cid, "labels": None, "arms": {}}
        labels = None
        for a in arms:
            rec = idx.get((a, cid))
            if rec is None:
                continue
            exp = rec.get("expect") or {}
            if labels is None and exp.get("labels"):
                labels = exp["labels"]
            row["arms"][a] = {
                "ok": rec.get("ok"),
                "error": rec.get("error"),
                "picks": {q: pick(ans) for q, ans in (rec.get("answers") or {}).items()},
                "probs": {q: probs_of(ans) for q, ans in (rec.get("answers") or {}).items()},
            }
        row["labels"] = labels
        rows.append(row)
    return rows


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", nargs="+", required=True)
    ap.add_argument("--cases", nargs="*", default=[],
                    help="case files, for the contrast pairs")
    ap.add_argument("--expect-from", nargs="*", default=[],
                    help="case files whose expect/expect_error win over the "
                         "records' own")
    ap.add_argument("--out", required=True)
    ap.add_argument("--compare", nargs="*",
                    default=["A1-bfloat16:A2", "A1-bfloat16:A3-float32",
                             "A3-float32:A3-float16", "A3-float32:A3-bfloat16"])
    ap.add_argument("--title", default="LAB03 — d1 decision models on Deucalion")
    args = ap.parse_args()

    records: list[dict] = []
    for p in args.results:
        records.extend(load(Path(p)))

    if args.expect_from:
        by_id: dict = {}
        for path in args.expect_from:
            data = json.loads(Path(path).read_text(encoding="utf-8"))
            for c in data.get("cases", []):
                by_id[c.get("id")] = c
        for rec in records:
            case = by_id.get(rec.get("case_id"))
            if not case:
                continue
            if case.get("expect"):
                rec["expect"] = case["expect"]
            if case.get("expect_error") is not None:
                rec["expect_error"] = case["expect_error"]

    pairs = []
    for spec in args.compare:
        if ":" in spec:
            a, b = spec.split(":", 1)
            pairs.append((a, b))

    summary = summarise(records)
    pw = pairwise(records, pairs)
    acc_rows = accuracy_table(records)
    contrast = contrast_table(records, args.cases)

    lines = []
    w = lines.append
    w(f"# {args.title}")
    w("")
    w(f"Records: {len(records)} · arms: "
      f"{', '.join(sorted({r.get('arm', '?') for r in records}))}")
    w("")
    w("## 1. Per-arm summary")
    w("")
    w("| arm | route | model | dtype | records | contract | error paths | accuracy (labelled) | "
      "unlabelled | median ms | p95 ms |")
    w("|---|---|---|---|---|---|---|---|---|---|---|")
    for arm in summary["arms"]:
        w(f"| {arm['arm']} | {ARM_NAMES.get(arm['arm'], arm['backend'])} | {arm['model']} | "
          f"{arm['dtype']} | {arm['records']} | "
          f"{'ok' if arm['contract_ok'] else f'{arm['contract_failed_records']} bad'} | "
          f"{'ok' if arm['error_paths_ok'] else f'{arm['unexpected_errors']} unexpected'} | "
          f"{arm['accuracy'] if arm['accuracy'] is not None else '—'} "
          f"({arm['labelled_correct']}/{arm['labelled']}) | {arm['unlabelled']} | "
          f"{arm['latency_median_ms']} | {arm['latency_p95_ms']} |")
    w("")

    w("## 1b. Per decision site")
    w("")
    w("The overall accuracy hides the shape of the error. A model that answers")
    w("\"no\" to every boolean scores 50 % on a balanced set and 7 % on a 35/3 set,")
    w("so the label and pick distributions are reported next to the accuracy.")
    w("")
    for arm_name in sorted({variant_of(r) for r in records}):
        rows = site_table(records, arm_name)
        if not rows:
            continue
        w(f"### {arm_name}")
        w("")
        w("| site | labelled | accuracy | labels T/F | picks T/F | one-sided |")
        w("|---|---|---|---|---|---|")
        for r in rows:
            w(f"| {r['site']} | {r['labelled']} | "
              f"{r['accuracy'] if r['accuracy'] is not None else '—'} | "
              f"{r['label_distribution']} | {r['pick_distribution']} | "
              f"{'**yes**' if r['one_sided'] else 'no'} |")
        w("")

    w("## 2. Pairwise comparison")
    w("")
    for key, d in pw.items():
        w(f"### {d['a']} vs {d['b']}")
        w("")
        w(f"- comparable cases: {d['comparable']} of {d['cases']}")
        w(f"- pick agreement: **{d['agreement_rate'] if d['agreement_rate'] is not None else '—'}**")
        w(f"- max |Δp|: **{d['max_abs_dp'] if d['max_abs_dp'] is not None else '—'}** · "
          f"mean |Δp|: {d['mean_abs_dp'] if d['mean_abs_dp'] is not None else '—'}")
        w("")
        drifted = [r for r in d["rows"] if r["comparable"] and not r["agreement"]]
        if drifted:
            w("Disagreeing cases:")
            w("")
            w("| case | question | type | A | B | max |Δp| |")
            w("|---|---|---|---|---|---|")
            for r in drifted[:40]:
                for q in r["per_question"]:
                    if not q["same_pick"]:
                        w(f"| `{r['case_id']}` | {q['question']} | {q['type']} | "
                          f"{q['a']!r} | {q['b']!r} | {q['max_abs_dp']} |")
            w("")
        else:
            w("No case where the two arms disagree on the pick.")
            w("")

    w("## 3. Contrast pairs (within an arm)")
    w("")
    w("Does the answer move when the state is padded with irrelevant text, when an")
    w("instruction is injected into the state, or when the question is paraphrased?")
    w("")
    for arm, rows in contrast.items():
        w(f"### {arm}")
        w("")
        if not rows:
            w("_no contrast pairs resolved for this arm_")
            w("")
            continue
        w("| variant | comparable | same answer | drifted questions |")
        w("|---|---|---|---|")
        for r in rows:
            if not r["comparable"]:
                w(f"| `{r['variant']}` | no | — | _not comparable_ |")
            else:
                w(f"| `{r['variant']}` | yes | {'yes' if r['same'] else '**NO**'} | "
                  f"{', '.join(r['drifted_questions']) or '—'} |")
        w("")

    w("## 4. Per-case answers")
    w("")
    w("| case | label | " + " | ".join(sorted({a for (a, _) in index(records)})) + " |")
    w("|---|---|" + "---|" * len({a for (a, _) in index(records)}))
    for row in acc_rows:
        label = json.dumps(row["labels"], ensure_ascii=False) if row["labels"] else "—"
        cells = []
        for arm in sorted({a for (a, _) in index(records)}):
            info = row["arms"].get(arm)
            if info is None:
                cells.append("—")
            elif not info["ok"]:
                err = info["error"] or {}
                cells.append(f"**error** ({err.get('type') or err.get('kind')})")
            else:
                cells.append("; ".join(f"{q}={v[1]!r}" for q, v in info["picks"].items()))
        w(f"| `{row['case_id']}` | {label} | " + " | ".join(cells) + " |")
    w("")

    Path(args.out).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {args.out} ({len(lines)} lines)")

    payload = {"summary": summary, "pairwise": pw, "per_case": acc_rows,
               "contrast": contrast,
               "sites": {a: site_table(records, a)
                         for a in sorted({variant_of(r) for r in records})}}
    Path(args.out).with_suffix(".json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False, default=str), encoding="utf-8")
    print(f"wrote {Path(args.out).with_suffix('.json')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
