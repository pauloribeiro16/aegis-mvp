#!/usr/bin/env python3
"""build_scoring_pack.py — the blind scoring pack for L2_RUBRIC.md.

Takes the documents of every run in the batch, strips every trace of which arm
produced which, samples goal rows per document, and emits:

  scoring/pack/          the anonymised scoring sheets
  scoring/_manifest.json which rows each document exposes
  scoring/L2_SCORES.csv  the file the researcher fills in
  scoring/_key.json      the un-blinding map — DO NOT OPEN before scoring

Blinding is enforced mechanically, not by convention: the pack carries no run
id, no arm, no model, and the presentation order is a seeded shuffle. The key is
written last and is the only file that names the arms.

What the sheet carries. The rubric's §2b document items D1-D7 are judgements
about content the model wrote — the §2 framing, the §4 tension resolutions and
the selected sub-domain set. An export that carries only the goal rows leaves
210 of the 450 units asking a question there is no material to answer, so
`sections()` pulls those three surfaces out and `render()` emits them.

Usage:
    python3 scripts/build_scoring_pack.py
    python3 scripts/build_scoring_pack.py --open   # reveal the key (after scoring)
    python3 scripts/build_scoring_pack.py --retest # pick the §6.1 retest subset

Stdlib only. Reads $AEGIS_RUNS_DIR (default ~/Work/aegis-runs).
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import random
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "pipeline" / "src"))

RUNS = Path(os.environ.get("AEGIS_RUNS_DIR") or (Path.home() / "Work" / "aegis-runs"))
OUT = REPO / "scoring"

# Registered seeds (L2_RUBRIC.md §5)
SEED_ROWS = 20261003      # which goal rows get sampled
SEED_ORDER = 20261004     # presentation order of the documents
SEED_RETEST = 20261005    # which documents get re-scored for the §6.1 kappa
N_ROWS = 8                # sampled goal rows per document
DOC_ITEMS = [f"D{i}" for i in range(1, 8)]  # §2b D1..D7
N_RETEST = 2              # documents per arm re-scored for §6.1
# §4 stage 2 — three pass/fail sub-criteria, recorded for rows scored <= 3.
STAGE2_FLAGS = ["legs_retained", "company_proportional", "implication_specific"]
CSV_COLUMNS = ["doc_key", "unit", "item", "score", "notes"] + STAGE2_FLAGS

ARMS = {
    "pipeline": "run_exp02_b_",   # 15 runs, seeded (EXP-02 arm B)
    "agent": "run_exp03_ag_",     # 15 runs, seeded (EXP-03 agent arm)
}

# A delivered document is ~1600 lines and most of it is code-derived (§0, §1,
# §5 Track B, §6 NIST mapping). This is the ceiling the blinding audit applies,
# not a guess: §0 is cut because it carries no model content and §5/§6 would
# re-identify the run by their row counts.
MAX_SECTION_CHARS = 6000


def find_runs(prefix: str) -> list[Path]:
    return sorted(p for p in RUNS.glob(prefix + "*") if (p / "doc02_adjusted_goals.md").is_file())


def _section(doc: str, start: str, stops: tuple[str, ...]) -> str:
    """Body of a `## §n` section, up to the first heading matching `stops`."""
    out, inside = [], False
    for line in doc.splitlines():
        if line.startswith(start):
            inside = True
            continue
        if inside and any(line.startswith(s) for s in stops):
            break
        if inside:
            out.append(line)
    return "\n".join(out).strip()


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
                "regulation": cells[6],
                "adjustment": cells[9] if len(cells) > 9 else "",
            })
    return rows


# ---------------------------------------------------------------------------
# The material the rubric's anchors need and the sheet does not carry.
# ---------------------------------------------------------------------------

RE_OBJECTIVE = re.compile(r"\*\*Objective\.\*\*\s*(.+?)(?=\n\n\*\*|\n\n---|\Z)", re.DOTALL)
RE_ANCHORS = re.compile(r"^\*\*((?:CSF|PF 1\.1|AI RMF)[^*]*anchors[^*]*)\:?\*\*\s*(.+)$",
                         re.MULTILINE | re.IGNORECASE)


def corpus_duty(repo: Path, sd_id: str, reg: str) -> dict:
    """The baseline duty behind one sub-domain/regulation, and its anchors.

    The rubric's §2a anchors — "the duty survives", "an obligation leg is
    dropped or distorted", "near-verbatim baseline copy" — are judgements
    about the baseline the goal had to keep. Without the baseline text in
    front of the scorer, those anchors cannot be applied at all.
    """
    from compose import reg_module_path  # pipeline/src, already on sys.path

    out = {"duty": "", "anchors": ""}
    path = reg_module_path(repo, sd_id, reg)
    if not path.is_file():
        return out
    text = path.read_text(encoding="utf-8")
    if not re.search(rf"id:\s*SG-{re.escape(sd_id)}\.{re.escape(reg)}\b", text):
        return out
    m = RE_OBJECTIVE.search(text)
    if m:
        out["duty"] = " ".join(m.group(1).split())
    anchors = [" ".join(f"{label.strip().rstrip(':')}: {ids.strip()}".split())
               for label, ids in RE_ANCHORS.findall(text)]
    out["anchors"] = " · ".join(anchors)
    return out


def build_reference(repo: Path, duties: dict[str, tuple[str, str]]) -> str:
    """The arm-identical reference the sheets point at.

    Identical for every document in the batch: the case's intake and the
    baseline duties behind the sampled goals. It carries no run id, no arm
    and no model, so the blind is unaffected by it.
    """
    intake_path = repo / "cases" / "Case_01_TinyTask_SaaS" / "01_PHASE1_CONTEXT" / "Doc01_INTAKE_FORM.md"
    out = [
        "# Reference material (arm-identical)",
        "",
        "This file is the same for every document in the batch: the company's "
        "intake and the baseline duties behind the sampled goals. It carries no "
        "run id, no arm and no model, so the blind is unaffected by it.",
        "",
        "The rubric's §2a anchors cannot be applied without it: \"the duty "
        "survives\", \"an obligation leg is dropped or distorted\", \"near-verbatim "
        "baseline copy\" and D1–D4's \"consistent with the intake\" are judgements "
        "about material the scoring sheet does not carry.",
        "",
        "## Company intake",
        "",
    ]
    if intake_path.is_file():
        out.append(intake_path.read_text(encoding="utf-8").strip())
    else:
        out.append(f"_not found: {intake_path}_")
    out += ["", "## Baseline duties behind the sampled goals", ""]
    for ag_id, (sd_id, reg) in sorted(duties.items()):
        d = corpus_duty(repo, sd_id, reg)
        out += [f"### {ag_id} — Sub-SO `SG-{sd_id}.{reg}`", ""]
        out += ["**Objective.** " + (d["duty"] or "_no Sub-SO card in the corpus_"), ""]
        if d["anchors"]:
            out += ["**Published anchors.** " + d["anchors"], ""]
    return "\n".join(out).rstrip() + "\n"


def sample_retest(key: list[dict], seed: int = SEED_RETEST) -> list[str]:
    """The §6.1 test-retest subset: 2 documents per arm, drawn with the seed.

    The rubric registers seed 20261005 for this and nothing implemented it,
    so the instrument could never produce the kappa it is judged by.
    """
    rng = random.Random(seed)
    picked: list[str] = []
    for arm in sorted({k["arm"] for k in key}):
        docs = sorted(k["doc_id"] for k in key if k["arm"] == arm)
        picked += rng.sample(docs, min(N_RETEST, len(docs)))
    return sorted(picked)


def sections(doc: str) -> dict:
    """The model-written surfaces the rubric scores but the goal table omits.

    §2 framing (D1-D4), §4 tension resolutions (D5-D6) and the selected
    sub-domain set (D7). §0, §1, §5 and §6 are code-derived and excluded by
    the rubric's own §1.
    """
    framing = _section(doc, "## §2", ("## §3", "## §4"))
    tensions = _section(doc, "## §4", ("## §5", "## §6"))
    goals = _section(doc, "## §3", ("## §4", "## §5", "## §6"))
    selection = [
        m.group(0).strip()
        for m in re.finditer(r"^###\s+(D-\d{2}\.\d+)\s+—\s*(.+)$", goals, re.MULTILINE)
    ]
    return {
        "framing": framing[:MAX_SECTION_CHARS],
        "tensions": tensions[:MAX_SECTION_CHARS],
        "selection": selection,
    }


def strata(n: int, k: int = N_ROWS) -> list[tuple[int, int]]:
    """k contiguous [lo, hi) strata over n rows (L2_RUBRIC §2a)."""
    step = n / k
    return [(int(i * step), max(int(i * step) + 1, int((i + 1) * step))) for i in range(k)]


def sample_positions(n: int, seed: int = SEED_ROWS) -> list[int]:
    """The within-stratum row index for each stratum, drawn from the seed.

    Drawn ONCE from the registered seed and reused by every document, which is
    what makes the batch PAIRED: the corpus is a single case, so the same duty
    ids exist in each document, and scoring the same duty everywhere makes every
    score difference attributable to the arm rather than to which duty happened
    to be drawn. The seed therefore fixes *which* duties, and pairing decides
    *where* they are read. See L2_RUBRIC.md §2a (v1.1.0) — do not re-seed this
    per document; that converts a paired design into an unpaired one.
    """
    rng = random.Random(seed)
    return [rng.randrange(lo, hi) for lo, hi in strata(n)]


def sample_rows(rows: list[dict], seed: int = SEED_ROWS) -> list[dict]:
    """N_ROWS rows, one per stratum, at the seeded within-stratum position."""
    if len(rows) <= N_ROWS:
        return rows
    positions = sample_positions(len(rows), seed)
    return [rows[min(p, len(rows) - 1)] for p in positions]


def render(doc_id: str, rows: list[dict], sec: dict) -> str:
    """An anonymised sheet: sampled goals plus the surfaces D1-D7 judge."""
    out = [f"# {doc_id}", "",
           "Score each goal row 1-5 against the anchors in L2_RUBRIC.md §2a:",
           "5 = keeps the regulatory duty AND is calibrated to this company; "
           "3 = the duty survives but the calibration is thin; "
           "1 = wrong, fabricated, or a near-copy of the baseline.", "",
           "The company intake and the baseline duty behind each goal are in "
           "`_reference.md` (same file for every document). You cannot judge "
           "\"the duty survives\" or \"near-verbatim baseline copy\" without it.", "",
           "Rows scored 3 or below also need the three stage-2 pass/fail flags "
           "(L2_RUBRIC.md §4).",
           "",
           "Then score D1-D7 at the foot of this sheet against §2b.", ""]

    out += ["## Company framing", "", sec["framing"] or "_none present_", ""]
    out += ["## Selected sub-domains", "",
            ", ".join(sec["selection"]) or "_none present_", ""]
    out += ["## Resolved tensions", "", sec["tensions"] or "_none present_", ""]

    for i, r in enumerate(rows, start=1):
        out += [f"## Goal {i}", "",
                f"**Adjusted goal:** {r['goal']}", "",
                f"**Company implication:** {r['implication']}", "",
                f"**Pattern / property:** {r['pattern']} / {r['property']}", "",
                f"**Adjustment:** {r['adjustment']}", "",
                "Holistic score (1-5): ______", "", "---", ""]

    out += ["## Document items", "",
            "Score 1-5 against L2_RUBRIC.md §2b:", ""]
    out += [f"{d} (1-5): ______" for d in DOC_ITEMS]
    return "\n".join(out) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--open", action="store_true",
                    help="reveal the key file (only after scoring)")
    ap.add_argument("--retest", action="store_true",
                    help="pick the §6.1 test-retest subset (2 documents per arm) and stop")
    ap.add_argument("--force", action="store_true",
                    help="rebuild even if scores have already been entered (destroys them)")
    args = ap.parse_args()

    key_path = OUT / "_key.json"
    if args.open:
        if not key_path.is_file():
            print("no key file — run without --open first", file=sys.stderr)
            return 2
        print(json.dumps(json.loads(key_path.read_text()), indent=1))
        return 0

    if args.retest:
        if not key_path.is_file():
            print("no key file — run without --open first", file=sys.stderr)
            return 2
        key = json.loads(key_path.read_text())
        picked = sample_retest(key)
        (OUT / "_retest.json").write_text(json.dumps(picked, indent=1), encoding="utf-8")
        print(f"retest subset (seed {SEED_RETEST}): {picked}")
        print("Re-score these four documents at least 7 days after the first pass.")
        return 0

    # The entered scores are the one artefact here that cannot be regenerated.
    # Rebuilding also re-randomises which run each `docNN` names, so scores
    # entered against one key cannot be joined to a rebuilt one (rubric §5.3).
    # Refuse before destroying them.
    scores_path = OUT / "L2_SCORES.csv"
    if scores_path.is_file() and not args.force:
        with scores_path.open(newline="", encoding="utf-8") as fh:
            entered = sum(1 for row in csv.DictReader(fh) if (row.get("score") or "").strip())
        if entered:
            print(f"REFUSING to rebuild: {scores_path} already carries {entered} entered "
                  f"score(s), and rebuilding would destroy them and re-randomise the "
                  f"key. Use --force only if you mean to start the batch over.",
                  file=sys.stderr)
            return 2

    runs = {arm: find_runs(p) for arm, p in ARMS.items()}
    for arm, rs in runs.items():
        if len(rs) < 10:
            print(f"only {len(rs)} {arm} runs with a deliverable — need >=10", file=sys.stderr)
            return 2

    # one document per run, but only runs whose goal table parses
    docs = []
    for arm, rs in runs.items():
        for r in rs:
            text = (r / "doc02_adjusted_goals.md").read_text(encoding="utf-8")
            rows = goal_rows(text)
            if len(rows) >= N_ROWS:
                docs.append({"arm": arm, "run": r.name, "rows": rows, "sec": sections(text)})

    rng = random.Random(SEED_ORDER)
    order = list(range(len(docs)))
    rng.shuffle(order)

    pack_dir = OUT / "pack"
    pack_dir.mkdir(parents=True, exist_ok=True)
    manifest = []
    duties: dict[str, tuple[str, str]] = {}
    for new_i, old_i in enumerate(order, start=1):
        d = docs[old_i]
        doc_id = f"doc{new_i:02d}"
        sampled = sample_rows(d["rows"])
        (pack_dir / f"{doc_id}.md").write_text(render(doc_id, sampled, d["sec"]), encoding="utf-8")
        for r in sampled:
            sd_id = re.match(r"AG-(D-\d{2}\.\d)-", r["id"])
            reg = (r.get("regulation") or "").strip().strip("*` ")
            if sd_id and reg:
                duties[r["id"]] = (sd_id.group(1), reg)
        manifest.append({
            "doc_id": doc_id,
            "rows": [r["id"] for r in sampled],
            "n_rows_available": len(d["rows"]),
            "selection": d["sec"]["selection"],
            "has_framing": bool(d["sec"]["framing"]),
            "has_tensions": bool(d["sec"]["tensions"]),
        })

    (OUT / "_manifest.json").write_text(json.dumps(manifest, indent=1), encoding="utf-8")
    (pack_dir / "_reference.md").write_text(build_reference(REPO, duties), encoding="utf-8")

    with scores_path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(CSV_COLUMNS)  # rubric §5.3 + the three stage-2 flags
        for m in manifest:
            for rid in m["rows"]:
                w.writerow([m["doc_id"], f"row:{rid}", "holistic", "", "", "", "", ""])
            for d in DOC_ITEMS:
                w.writerow([m["doc_id"], f"doc:{d}", "document", "", ""])

    # the key last, and it is the only file that names arms
    key_path.write_text(json.dumps(
        [{"doc_id": m["doc_id"], "arm": docs[order[i]]["arm"],
          "run": docs[order[i]]["run"]} for i, m in enumerate(manifest)], indent=1),
        encoding="utf-8")

    units = len(manifest) * (N_ROWS + len(DOC_ITEMS))
    print(f"pack built: {len(manifest)} documents, {N_ROWS} sampled rows each, {units} units")
    print(f"  {OUT / 'pack'}/          anonymised documents")
    print(f"  {OUT / 'pack/_reference.md'}  the arm-identical material the anchors need")
    print(f"  {OUT / 'L2_SCORES.csv'}  fill this in (score 1-5; the three stage-2 flags "
          f"for rows scored <= 3)")
    print(f"  {key_path}  DO NOT OPEN until the CSV is filled")
    print(f"  {OUT / '_retest.json'}  pick the §6.1 retest subset with --retest")
    return 0


if __name__ == "__main__":
    sys.exit(main())