#!/usr/bin/env python3
"""watch_p302.py — follow the Onda C calibration arms and extract the metrics.

TOKEN DISCIPLINE (the operator's constraint): everything is aggregated
SERVER-SIDE and the only thing that crosses ssh is one JSON dict per arm —
the counts the prereg judges (H1 L0 first-attempt rate, H2 the 25-60%
routing band, M-26 the 65% collapse alert, the round's standing). No pack,
verdict row or document is ever fetched whole: the artifacts stay on the
cluster, the numbers come here.

Usage: python3 scripts/watch_p302.py [--once]
"""
from __future__ import annotations

import json
import subprocess
import sys

HOST = "paulinho@login.deucalion.macc.fccn.pt"
RUNS = "/projects/F202512235CPCAA1/mvp-pipeline/aegis-runs"
ARMS = [
    ("run_p302_qwen38_c1", "qwen3.8:27b", "Case_01"),
    ("run_p302_qwen38_c3", "qwen3.8:27b", "Case_03"),
    ("run_p302_qwen38_c2", "qwen3.8:27b", "Case_02"),
    ("run_p302_muse_c1", "muse-glimmer:30b", "Case_01"),
    ("run_p302_muse_c3", "muse-glimmer:30b", "Case_03"),
    ("run_p302_gemma4_c1", "gemma4:31b", "Case_01"),
]


def ssh(cmd: str) -> str:
    proc = subprocess.run(
        ["ssh", "-o", "LogLevel=ERROR", "-o", "ConnectTimeout=20", HOST, cmd],
        capture_output=True, text=True, timeout=120,
    )
    return proc.stdout or ""


def arm_metrics(run_id: str) -> dict:
    """The metrics the prereg judges, read from the run's own store."""
    script = f"""
import json, glob, os, re
from collections import Counter
run = "{RUNS}/{run_id}"
out = {{"run": "{run_id}", "exists": os.path.isdir(run)}}
rows = []
acts = Counter(); verdicts = Counter()
for f in glob.glob(run + "/steps/phase3/verdicts_*.json"):
    try:
        rs = json.load(open(f)); rows.extend(rs)
        for row in rs:
            acts[str(row.get("action", "")).strip()[:40]] += 1
            verdicts[str(row.get("verdict", "")).strip()[:50]] += 1
    except Exception as e:
        out["err"] = str(e)
out["n_rows"] = len(rows)
out["actions"] = acts.most_common(6)
out["verdicts"] = verdicts.most_common(5)
total = sum(acts.values()) or 1
out["global_org_share"] = round(acts.get("ROUTE_ORG", 0) / total, 3)
m26 = [r for r in rows if re.match(r"^(?:PO|SO)-(?:D-0[2-7])\\.", r.get("id", ""))]
m26_share = round(sum(1 for r in m26 if r.get("action") == "ROUTE_ORG") / len(m26), 3) \\
    if len(m26) >= 5 else None
out["m26"] = {{"n": len(m26), "org_share": m26_share}}
ok = retried = 0
trace = run + "/trace.jsonl"
CUTOFF = "2026-10-28T20:05"  # the 1st submission aborted; only count records after the clean
if os.path.isfile(trace):
    for line in open(trace, encoding="utf-8"):
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        if str(rec.get("ts_start", "")) < CUTOFF:
            continue
        if str(rec.get("step", "")).startswith("p3a") and rec.get("status") == "ok":
            ok += 1
            retried += bool(rec.get("l0_retried"))
l0_first = round((ok - retried) / ok, 3) if ok else None
out["l0"] = {{"ok_calls": ok, "retried": retried, "first_attempt": l0_first}}
proposals = []
for f in glob.glob(run + "/steps/phase3/proposals_*.json"):
    try:
        proposals.extend(json.load(open(f)).get("proposals", []))
    except Exception:
        pass
out["n_proposals"] = len(proposals)
out["n_prin_proposals"] = sum(len(json.load(open(f)).get("proposals", []))
    for f in glob.glob(run + "/steps/phase3/proposals_prin_*.json"))
for n in (1, 2):
    p = run + "/steps/phase3/round" + str(n) + "_state.json"
    if os.path.isfile(p):
        try:
            s = json.load(open(p))
            out["round" + str(n)] = {{k: (len(v) if isinstance(v, list) else v)
                              for k, v in s.items() if k in
                              ("accepted", "rejected", "adjusted", "pending_adjustment",
                               "open", "converged")}}
        except Exception as e:
            out["round" + str(n) + "_err"] = str(e)
stages = []
for f in sorted(glob.glob(run + "/steps/stage_result*.json")) + \\
        sorted(glob.glob(run + "/steps/*/stage_result*.json")):
    try:
        d = json.load(open(f))
        stages.append({{"stage": d.get("stage"), "status": d.get("status"),
                       "carried": d.get("carried"), "selected": d.get("selected"),
                       "failed": d.get("failed"), "summary": str(d.get("summary"))[:110]}})
    except Exception:
        pass
out["stages"] = stages
print(json.dumps(out))
"""
    raw = ssh(f"python3 - <<'PYEOF'\n{script}\nPYEOF")
    for line in raw.splitlines():
        line = line.strip()
        if line.startswith("{"):
            try:
                return json.loads(line)
            except json.JSONDecodeError:
                continue
    return {"run": run_id, "error": raw[-300:] or "no output"}


def main() -> int:
    once = "--once" in sys.argv
    # optional positional run ids: `watch_p302.py --once run_p304_qwen38_c1`
    # reports ONLY those arms (the Onda C-2 re-calibration reuses the same
    # aggregation instead of a second watcher script)
    arms = ARMS if len(sys.argv) <= 1 + once else [
        (rid, "?", "?") for rid in sys.argv[1 + once:]]
    queue = ssh("squeue -u $USER -h -o '%i %T %M %j' 2>/dev/null")
    print(f"=== queue ===\n{queue or '(empty)'}")
    verdict = []
    for run_id, model, case in arms:
        m = arm_metrics(run_id)
        if not m.get("exists"):
            print(f"\n--- {run_id} ({model}, {case}): NO RUN DIR")
            continue
        acts = dict(m.get("actions", []))
        total = m.get("n_rows") or sum(acts.values()) or 1
        g = m.get("global_org_share")
        m26 = m.get("m26") or {}
        l0 = m.get("l0") or {}
        print(f"\n--- {run_id} ({model}, {case})  rows={m.get('n_rows')}")
        if g is not None:
            print(f"    H2 global ROUTE_ORG: {g:.0%} (band 25-60%)")
        if m26.get("org_share") is not None:
            print(f"    M-26 D-02..D-07: {m26['org_share']:.0%} "
                  f"(n={m26.get('n')}, alert >65%)")
        else:
            print(f"    M-26 D-02..D-07: n/a (n={m26.get('n')})")
        if l0.get("first_attempt") is not None:
            print(f"    H1 L0 first-attempt: {l0['first_attempt']:.0%} "
                  f"({l0['ok_calls'] - l0['retried']}/{l0['ok_calls']} calls)")
        print(f"    proposals: {m.get('n_proposals')} (+{m.get('n_prin_proposals')} principle)")
        for key in ("round1", "round2"):
            if key in m:
                print(f"    {key}: {m[key]}")
        for s in m.get("stages", []):
            print(f"      {s['stage']}: {s['status']} carried={s['carried']}/{s['selected']} "
                  f"failed={s['failed']} — {(s.get('summary') or '')[:80]}")
        verdict.append((run_id, g, m26.get("org_share"), l0.get("first_attempt")))
    if once:
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
