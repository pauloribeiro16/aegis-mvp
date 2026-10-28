#!/usr/bin/env python3
"""watch_p302.py — follow the Onda C calibration arms and extract the metrics.

Reads each arm's run directory on the cluster (via ssh) and reports, per arm:
the L0 first-attempt pass rate, the routing balance (ROUTE_ORG vs
PROPOSE_PRODUCT) and the round's standing. The numbers the PREREG_P3_02
falsifiers judge.

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
        capture_output=True, text=True, timeout=90,
    )
    return proc.stdout or ""


def arm_metrics(run_id: str) -> dict:
    """The metrics the prereg judges, read from the run's own store."""
    script = f"""
import json, glob, os
from collections import Counter
run = "{RUNS}/{run_id}"
out = {{"run": "{run_id}", "exists": os.path.isdir(run)}}
# 1. routing balance from the verdict store
acts = Counter(); verdicts = Counter()
for f in glob.glob(run + "/steps/phase3/verdicts_*.json"):
    try:
        for row in json.load(open(f)):
            acts[str(row.get("action", "")).strip()[:40]] += 1
            verdicts[str(row.get("verdict", "")).strip()[:50]] += 1
    except Exception as e:
        out["err"] = str(e)
out["actions"] = acts.most_common(8)
out["verdicts"] = verdicts.most_common(6)
# 2. L0 first-attempt: the stores vs the failures recorded in the log
proposals = []
for f in glob.glob(run + "/steps/phase3/proposals_*.json"):
    try:
        proposals.extend(json.load(open(f)).get("proposals", []))
    except Exception:
        pass
out["n_proposals"] = len(proposals)
out["n_prin_proposals"] = sum(len(json.load(open(f)).get("proposals", []))
    for f in glob.glob(run + "/steps/phase3/proposals_prin_*.json"))
# 3. the round's standing
for n in (1, 2):
    p = run + f"/steps/phase3/round{{n}}_state.json"
    if os.path.isfile(p):
        try:
            s = json.load(open(p))
            out[f"round{{n}}"] = {{k: (len(v) if isinstance(v, list) else v)
                              for k, v in s.items() if k in
                              ("accepted", "rejected", "adjusted", "pending_adjustment",
                               "open", "converged")}}
        except Exception as e:
            out[f"round{{n}}_err"] = str(e)
# 4. stage results (status + summary) — the first-attempt signal lives here
stages = []
for f in sorted(glob.glob(run + "/steps/stage_result*.json")) + sorted(glob.glob(run + "/steps/*/stage_result*.json")):
    try:
        d = json.load(open(f))
        stages.append({{"stage": d.get("stage"), "status": d.get("status"),
                       "carried": d.get("carried"), "selected": d.get("selected"),
                       "failed": d.get("failed"), "summary": str(d.get("summary"))[:120]}})
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
    queue = ssh("squeue -u $USER -h -o '%i %T %M %j' 2>/dev/null")
    print(f"=== queue ===\n{queue or '(empty)'}")
    for run_id, model, case in ARMS:
        m = arm_metrics(run_id)
        if not m.get("exists"):
            print(f"\n--- {run_id} ({model}, {case}): NO RUN DIR")
            continue
        acts = dict(m.get("actions", []))
        total = sum(acts.values()) or 1
        org = acts.get("ROUTE_ORG", 0)
        prod = acts.get("PROPOSE_PRODUCT", 0)
        print(f"\n--- {run_id} ({model}, {case})")
        print(f"    routing: ROUTE_ORG {org}/{total} ({org/total:.0%}) · "
              f"PROPOSE_PRODUCT {prod}/{total} ({prod/total:.0%})")
        print(f"    verdicts: {m.get('verdicts')}")
        print(f"    proposals: {m.get('n_proposals')} (+{m.get('n_prin_proposals')} principle)")
        for key in ("round1", "round2"):
            if key in m:
                print(f"    {key}: {m[key]}")
        for s in m.get("stages", []):
            print(f"      {s['stage']}: {s['status']} carried={s['carried']} "
                  f"selected={s['selected']} failed={s['failed']} — {s['summary'][:90]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
