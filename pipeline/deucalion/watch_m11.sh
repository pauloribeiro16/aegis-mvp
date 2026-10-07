#!/usr/bin/env bash
# watch_m11.sh — wait for the four M11 cells, pull them down, and verify from
# the artefacts that each arm actually received the instruction it declares.
#
# Three checks, in increasing order of how much they actually prove:
#
#   1. config.json records the arm          — bookkeeping
#   2. the p4_instruction digest is EQUAL  — both arms ran the same code, so
#      across arms                         the digest must NOT differ. The
#                                           digest hashes the variant TABLE,
#                                           not the selection, so a difference
#                                           here would mean the payload moved
#                                           mid-matrix, not that the arms are
#                                           distinguishable.
#   3. the prompt BYTES differ where the  — the claim itself. Compare one
#      arms claim to differ                   `*_p4_*_user.md` per arm on the
#                                           same case: the head up to
#                                           `P4_STYLE_MARKER` must be
#                                           byte-identical, and the tail must
#                                           carry the shipped clause in
#                                           ctrl and none in meta.
#
# Usage: bash pipeline/deucalion/watch_m11.sh [--once]
set -uo pipefail

HOST="${MVP_HOST:-paulinho@login.deucalion.macc.fccn.pt}"
RUNS="${AEGIS_RUNS_DIR:-$HOME/Work/aegis-runs}"
LOG="$RUNS/m11_submissions.log"
REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
ONCE="${1:-}"
POLL="${MVP_POLL:-120}"

ssh_q() { ssh -n -o BatchMode=yes "$HOST" \
  "squeue -u \$USER -h -o '%i %j %t' | grep mvp_ || true" 2>/dev/null; }

our_jobs() { awk '{for(i=1;i<=NF;i++) if($i ~ /^p1=|^all=/) print $i}' "$LOG" \
             | sed 's/.*=//' | grep -E '^[0-9]+$' | sort -u; }

remaining() {
  local queued now j
  queued=$(ssh_q | awk '{print $1}')
  [ -z "$queued" ] && return 1
  now=$(our_jobs)
  for j in $now; do echo "$queued" | grep -qx "$j" && return 0; done
  return 1
}

echo "M11 watcher — jobs: $(our_jobs | tr '\n' ' ')"
while remaining; do
  [ "$ONCE" = "--once" ] && { echo "still running"; exit 0; }
  printf '%s  %s job(s) queued\n' "$(date -u +%H:%M:%S)" "$(ssh_q | wc -l)"
  sleep "$POLL"
done
echo "$(date -u +%H:%M:%S)  queue drained"

echo
echo "=== pull down ==="
cd "$REPO_ROOT"
# the log line is `tag p1=J all=J run=R case=C arm=A` — six fields, so a
# positional `read` leaves `run` holding the `run=` prefix and every scp targets
# a directory that does not exist. Pull the run id out by key.
while read -r line; do
  tag=$(echo "$line" | awk '{print $1}')
  case "$tag" in m11_*) ;; *) continue ;; esac
  run=$(echo "$line" | awk '{for(i=1;i<=NF;i++) if($i ~ /^run=/){sub(/^run=/,"",$i); print $i; exit}}')
  [ -z "$run" ] && { echo "  $tag: no run id in the log line"; continue; }
  if [ -d "$RUNS/$run" ]; then
    echo "  $run already local"
  else
    bash pipeline/deucalion/sync_down.sh "$run" >/dev/null 2>&1 \
      && echo "  $run pulled" || echo "  $run SYNC FAILED"
  fi
done < "$LOG"

echo
python3 - "$RUNS" <<'PY'
import json, re, sys
from pathlib import Path

MARKER = "Company implication = what this duty concretely means for THIS company"
runs = Path(sys.argv[1])
log = runs / "m11_submissions.log"
bad, digests, prompts = [], {}, {}

for line in log.read_text().splitlines():
    f = dict(kv.split("=", 1) for kv in line.split() if "=" in kv)
    tag = line.split()[0]
    if not tag.startswith("m11_") or "run" not in f:
        continue
    run, arm = runs / f["run"], tag.rsplit("_", 1)[1]
    cfg = run / "config.json"
    if not cfg.exists():
        bad.append(f"{tag}: not pulled")
        continue
    conf = json.loads(cfg.read_text())
    ov = conf.get("ficha_overrides") or {}
    dig = (conf.get("prompt_digests") or {}).get("p4_instruction", "?")
    got = ov.get("p4_implication")
    print(f"{f['run']:<32} arm={arm:<5} ficha_overrides={str(ov):<26} "
          f"seed={conf.get('seed')} T={conf.get('temperature')} digest={dig}")
    if arm == "concrete" and got != "concrete":
        bad.append(f"{tag}: declares concrete but p4_implication={got!r}")
    if arm == "ctrl" and got is not None:
        bad.append(f"{tag}: declares ctrl but p4_implication={got!r}")
    if arm == "ctrl" and got is not None:
        bad.append(f"{tag}: declares ctrl but p4_instruction={got!r}")
    digests.setdefault(dig, []).append(tag)
    # the prompt bytes this run actually sent
    users = sorted((run / "inputs").glob("*_p4_*_user.md")) if (run / "inputs").is_dir() else []
    if users:
        prompts[tag] = users[0].read_text(encoding="utf-8")

if len(digests) != 1:
    bad.append(f"p4_instruction digests differ across arms ({digests}) — the "
               "payload moved mid-matrix; both arms must run the same code")
else:
    (d, tags), = digests.items()
    print(f"\ndigest {d} shared by all {len(tags)} cells — as it must be: the "
          "digest hashes the variant table, not the selection")

# byte-level comparison, per case, ctrl against meta
for case in ("c2", "c3"):
    a, b = prompts.get(f"m11_{case}_ctrl"), prompts.get(f"m11_{case}_concrete")
    if not a or not b:
        print(f"\n{case}: prompt bytes unavailable (inputs/ not pulled)")
        continue
    ha = a.partition(MARKER)[0], a.partition(MARKER)[2]
    hb = b.partition(MARKER)[0], b.partition(MARKER)[2]
    if ha[0] != hb[0]:
        bad.append(f"{case}: the head before the style marker differs between arms")
    # the intervention replaces the whole clause, so the discriminating signal
    # is whether the treatment still carries the SHIPPED clause and the control
    # does — not a count of exemplars.
    shipped = lambda t: MARKER in t
    print(f"\n{case}: head identical={ha[0] == hb[0]}  "
          f"shipped clause in ctrl={shipped(a)} concrete={shipped(b)}  "
          f"clause differs={ha[1] != hb[1]}")
    if not shipped(a):
        bad.append(f"{case}: ctrl does not carry the shipped clause — arm is not what it claims")
    if shipped(b):
        bad.append(f"{case}: concrete arm still carries the shipped clause — override did not land")
    if ha[1] == hb[1]:
        bad.append(f"{case}: the clause did not change between arms")

print()
print("RESULT: FAIL — " + "; ".join(bad) if bad
      else "RESULT: PASS — each arm received the instruction it declares, on the same code")
sys.exit(1 if bad else 0)
PY