#!/usr/bin/env python3
"""build_scoring_pack.py — the blind scoring pack for EXP-03 (L2_RUBRIC.md).

Takes the 15 pipeline documents and the 15 agent documents, strips every trace
of which arm produced which, samples 8 goal rows per document (stratified, with
the registered seed), and emits:

  scoring/pack/          the anonymised documents + the sample manifest
  scoring/L2_SCORES.csv  the file the researcher fills in
  scoring/_key.json      the un-blinding map — DO NOT OPEN before scoring

Blinding is enforced mechanically, not by convention: the pack carries no run
id, no arm, no model, and the presentation order is a seeded shuffle. The key is
written last and is the only file that names the arms.

Usage:
    python3 scripts/build_scoring_pack.py
    python3 scripts/build_scoring_pack.py --open   # reveal the key (after scoring)

Stdlib only. Reads $AEGIS_RUNS_DIR (default ~/Work/aegis-runs).
"""

from __future__ import annotations

import argparse
import csv
import json
import random
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RUNS = Path.home() / "Work" / "aegis-runs"
OUT = REPO / "scoring"

# Registered seeds (L2_RUBRIC.md §5)
SEED_ROWS = 20261003      # which goal rows get sampled
SEED_ORDER = 20261004     # presentation order of the documents
N_ROWS = 8                # sampled goal rows per document
DOC_IDS = [f"doc{i:02d}" for i in range(1, 8)]  # §4 D1..D7

ARMS = {
    "pipeline": "run_exp02_b_",   # 15 runs, seeded (EXP-02 arm B)
    "agent": "run_exp03_ag_",     # 15 runs, seeded (EXP-03 agent arm)
}


def find_runs(prefix: str) -> list[Path]:
    return sorted(p for p in RUNS.glob(prefix + "*") if (p / "doc02_adjusted_goals.md").is_file())


def goal_rows(doc: str) -> list[dict]:
    """Rows of the §3 goal table, as {id, goal, implication, pattern, property, adjustment}."""
    rows, in3 = [], False
    for line in doc.splitlines():
        if line.startswith("## §3"):
            in3 = True
        elif line.startswith("## §") and not line.startswith("## §3"):
            if in3:
                break
        if in3 and line.strip().startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 10 or not re.match(r"`?AG-", cells[0]):
                continue
            rows.append({
                "id": cells[0].strip("` "),
                "goal": cells[1],
                "implication": cells[2],
                "pattern": cells[3],
                "property": cells[4],
                "adjustment": cells[9] if len(cells) > 9 else "",
            })
    return rows


def sample_rows(rows: list[dict], seed: int) -> list[dict]:
    """8 rows, stratified across sub-domain blocks by row index (L2_RUBRIC §2a)."""
    if len(rows) <= N_ROWS:
        return rows
    rng = random.Random(seed)
    step = len(rows) / N_ROWS
    return [rows[int(i * step)] for i in range(N_ROWS)]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--open", action="store_true",
                    help="reveal the key file (only after scoring)")
    args = ap.parse_args()

    key_path = OUT / "_key.json"
    if args.open:
        if not key_path.is_file():
            print("no key file — run without --open first", file=sys.stderr)
            return 2
        print(json.dumps(json.loads(key_path.read_text()), indent=1))
        return 0

    runs = {arm: find_runs(p) for arm, p in ARMS.items()}
    for arm, rs in runs.items():
        if len(rs) < 10:
            print(f"only {len(rs)} {arm} runs with a deliverable — need >=10", file=sys.stderr)
            return 2

    # one document per run, but only runs whose goal table parses
    docs = []
    for arm, rs in runs.items():
        for r in rs:
            rows = goal_rows((r / "doc02_adjusted_goals.md").read_text(encoding="utf-8"))
            if len(rows) >= N_ROWS:
                docs.append({"arm": arm, "run": r.name, "rows": rows})

    rng = random.Random(SEED_ORDER)
    order = list(range(len(docs)))
    rng.shuffle(order)

    pack_dir = OUT / "pack"
    pack_dir.mkdir(parents=True, exist_ok=True)
    manifest = []
    for new_i, old_i in enumerate(order, start=1):
        d = docs[old_i]
        doc_id = f"doc{new_i:02d}"
        sampled = sample_rows(d["rows"], SEED_ROWS + new_i)
        (pack_dir / f"{doc_id}.md").write_text(render(doc_id, sampled), encoding="utf-8")
        manifest.append({
            "doc_id": doc_id,
            "rows": [r["id"] for r in sampled],
            "n_rows_available": len(d["rows"]),
        })

    (OUT / "_manifest.json").write_text(json.dumps(manifest, indent=1), encoding="utf-8")

    with (OUT / "L2_SCORES.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["doc_id", "unit", "item", "score_1_5", "notes"])
        for m in manifest:
            for i, rid in enumerate(m["rows"], start=1):
                w.writerow([m["doc_id"], f"row{i}:{rid}", "holistic", "", ""])
            for d in DOC_IDS:
                w.writerow([m["doc_id"], "document", d, "", ""])

    # the key last, and it is the only file that names arms
    key_path.write_text(json.dumps(
        [{"doc_id": m["doc_id"], "arm": docs[order[i]]["arm"],
          "run": docs[order[i]]["run"]} for i, m in enumerate(manifest)], indent=1),
        encoding="utf-8")

    print(f"pack built: {len(manifest)} documents, {N_ROWS} sampled rows each")
    print(f"  {OUT / 'pack'}/          anonymised documents")
    print(f"  {OUT / 'L2_SCORES.csv'}  fill this in (score_1_5 per row)")
    print(f"  {key_path}  DO NOT OPEN until the CSV is filled")
    return 0


def render(doc_id: str, rows: list[dict]) -> str:
    """An anonymised sheet: only the sampled goals, no ids that leak provenance."""
    out = [f"# {doc_id}", "",
           "Score each goal row 1-5 against the anchors in L2_RUBRIC.md §2a:",
           "5 = keeps the regulatory duty AND is calibrated to this company; "
           "3 = the duty survives but the calibration is thin; "
           "1 = wrong, fabricated, or a near-copy of the baseline.", ""]
    for i, r in enumerate(rows, start=1):
        out += [f"## Goal {i}", "",
                f"**Adjusted goal:** {r['goal']}", "",
                f"**Company implication:** {r['implication']}", "",
                f"**Pattern / property:** {r['pattern']} / {r['property']}", "",
                f"**Adjustment:** {r['adjustment']}", "",
                f"Holistic score (1-5): ______", "", "---", ""]
    return "\n".join(out)


if __name__ == "__main__":
    sys.exit(main())
