#!/usr/bin/env bash
# watch_m09.sh — wait for the four M09 cells, pull them down, and verify that
# each arm actually received the instruction it claims.
#
# The verification is the point. A prompt override that silently does not
# apply leaves config.json saying one thing and the run shipping another — the
# m06 failure (`p4_instruction` digests identical, badge rewrite invisible, the
# instrument distinguishable only by reading inputs/ verbatim). So this watcher
# reads config.json back from every pulled run and asserts:
#   ctrl  -> ficha_overrides is empty / has no p4_instruction
#   meta  -> ficha_overrides.p4_instruction == "meta"
# and that the two arms carry DIFFERENT prompt_digests.p4_instruction.
#
# Usage: bash pipeline/deucalion/watch_m09.sh [--once]
#   --once = check the queue once and exit (no long poll)
set -uo pipefail

HOST="${MVP_HOST:-paulinho@login.deucalion.macc.fccn.pt}"
RUNS="${AEGIS_RUNS_DIR:-$HOME/Work/aegis-runs}"
LOG="$RUNS/m09_submissions.log"
REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
ONCE="${1:-}"
POLL="${MVP_POLL:-120}"

ssh_q() { ssh -n -o BatchMode=yes "$HOST" \
  "squeue -u \$USER -h -o '%i %j %t' | grep mvp_ || true" 2>/dev/null; }

# every job id this matrix owns, so "done" means none of them are queued
our_jobs() { awk '{for(i=1;i<=NF;i++) if($i ~ /^p1=|^all=/) print $i}' "$LOG" \
             | sed 's/.*=//' | grep -E '^[0-9]+$' | sort -u; }

remaining() {
  local queued now
  queued=$(ssh_q | awk '{print $1}')
  [ -z "$queued" ] && return 1
  now=$(our_jobs)
  for j in $now; do echo "$queued" | grep -qx "$j" && return 0; done
  return 1
}

echo "M09 watcher — jobs: $(our_jobs | tr '\n' ' ')"
while remaining; do
  [ "$ONCE" = "--once" ] && { echo "still running"; exit 0; }
  printf '%s  %s job(s) queued\n' "$(date -u +%H:%M:%S)" "$(ssh_q | wc -l)"
  sleep "$POLL"
done
echo "$(date -u +%H:%M:%S)  queue drained"

echo
echo "=== pull down + verify each arm ==="
cd "$REPO_ROOT"
while read -r tag p1 all run; do
  case "$tag" in m09_*) ;; *) continue ;; esac
  arm="${tag##*_}"
  if [ -n "$run" ] && [ -d "$RUNS/$run" ]; then
    echo "  $run already local"
  else
    bash pipeline/deucalion/sync_down.sh "$run" >/dev/null 2>&1 \
      && echo "  $run pulled" || echo "  $run SYNC FAILED"
  fi
done < "$LOG"

echo
python3 - "$RUNS" <<'PY'
import json, sys
from pathlib import Path

runs = Path(sys.argv[1])
log = runs / "m09_submissions.log"
bad, seen = [], {}
print(f"{'run':<34} {'arm':<5} {'ficha_overrides':<24} {'p4_instruction digest':<20}")
print("-" * 88)
for line in log.read_text().splitlines():
    f = dict(kv.split("=", 1) for kv in line.split() if "=" in kv)
    tag = line.split()[0]
    if not tag.startswith("m09_") or "run" not in f:
        continue
    run = runs / f["run"]
    cfg, man = run / "config.json", run / "manifest.json"
    if not (cfg.exists() and man.exists()):
        bad.append(f"{f['run']}: not pulled")
        continue
    ov = json.loads(cfg.read_text()).get("ficha_overrides") or {}
    dig = json.loads(man.read_text()).get("prompt_digests", {}).get("p4_instruction", "?")
    arm = tag.rsplit("_", 1)[1]
    print(f"{f['run']:<34} {arm:<5} {str(ov):<24} {dig:<20}")
    got = ov.get("p4_instruction")
    if arm == "meta" and got != "meta":
        bad.append(f"{tag}: arm=meta but p4_instruction={got!r} — OVERRIDE DID NOT LAND")
    if arm == "ctrl" and got is not None:
        bad.append(f"{tag}: arm=ctrl but p4_instruction={got!r} — arms are not what they claim")
    seen.setdefault(dig, []).append(tag)

if len(seen) < 2:
    bad.append("both arms share one p4_instruction digest — the instrument is not distinguishable")
else:
    for dig, tags in seen.items():
        print(f"\ndigest {dig}: {', '.join(tags)}")
print()
print("RESULT: FAIL — " + "; ".join(bad) if bad
      else "RESULT: PASS — each arm received the instruction it declares, and the two are distinguishable")
sys.exit(1 if bad else 0)
PY