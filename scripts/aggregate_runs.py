#!/usr/bin/env python3
"""Aggregate metrics across many pipeline runs (read-only, report-only).

The starting point for EXP-02 (noise floor) and EXP-03 (orchestration). One
run is an anecdote; a distribution over runs is evidence.

This exists because nothing in the repo could compare more than two runs, and
because the two arms do not share a trace schema. Getting that wrong does not
crash — it silently reports the wrong number, which is the failure mode that
matters:

  * the pipeline arm writes ``est_prompt_tokens``; the agent arm writes
    ``history_est_tokens``. A reader that looks for only one of them sees zero
    for the other arm and reports it as "cheaper".
  * ``latency_s`` exists ONLY on dry-run records, where it is 0. Successful
    calls carry ``attempt1_latency_s`` / ``attempt2_latency_s``. A reader that
    does ``record.get("latency_s")`` reads None on every real call and reports
    zero latency without failing.

Both are handled explicitly below and both are covered by the test suite.

Usage::

    python3 scripts/aggregate_runs.py ~/Work/aegis-runs/run_*
    python3 scripts/aggregate_runs.py --json out.json ~/Work/aegis-runs
    python3 scripts/aggregate_runs.py --arm-summary ~/Work/aegis-runs

Stdlib only. The compute nodes have no pip egress, and the workstation has no
numpy either, so every statistic is computed here in plain Python.
"""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "pipeline" / "src"))

from compose import sub_so_objective  # noqa: E402
import quality  # noqa: E402
import runconfig  # noqa: E402


# --------------------------------------------------------------------------
# trace readers — the two schemas, handled explicitly
# --------------------------------------------------------------------------

def read_trace(run_dir: Path) -> list[dict]:
    trace = run_dir / "trace.jsonl"
    if not trace.is_file():
        return []
    out = []
    for line in trace.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError:
            # a half-written final line is what a killed job leaves behind;
            # dropping it is right, and it is not the same as an empty trace
            continue
    return out


def prompt_tokens(rec: dict) -> int:
    """Prompt tokens for either arm.

    Pipeline: a per-call prompt (``est_prompt_tokens``, and now the real
    ``attemptN_prompt_tokens``). Agent: the whole accumulated history re-sent
    each turn (``history_est_tokens``) — a different quantity, so the caller is
    told which it got.
    """
    for key in ("attempt1_prompt_tokens", "est_prompt_tokens"):
        v = rec.get(key)
        if isinstance(v, (int, float)):
            return int(v)
    v = rec.get("history_est_tokens")
    return int(v) if isinstance(v, (int, float)) else 0


def latency_seconds(rec: dict) -> float:
    """Seconds for one recorded call.

    ``latency_s`` is dry-run-only and is 0 there, so it is deliberately NOT
    consulted for real records. The repair retry's time is included when it
    happened, because it was spent producing this run.
    """
    total = 0.0
    for attempt in (1, 2):
        v = rec.get(f"attempt{attempt}_latency_s")
        if isinstance(v, (int, float)):
            total += float(v)
    return round(total, 1)


def eval_tokens(rec: dict) -> int:
    v = rec.get("attempt1_eval_tokens")
    if isinstance(v, (int, float)):
        return int(v)
    v = rec.get("est_output_tokens")
    return int(v) if isinstance(v, (int, float)) else 0


# --------------------------------------------------------------------------
# per-run metrics
# --------------------------------------------------------------------------

def trace_metrics(run_dir: Path) -> dict:
    recs = read_trace(run_dir)
    ok = [r for r in recs if r.get("status") == "ok"]
    failed = [r for r in recs if r.get("status") == "failed"]
    agentic = bool(recs) and recs[0].get("mode") == "agentic"

    return {
        "n_calls": len(recs),
        "n_ok": len(ok),
        "n_failed": len(failed),
        "mode": "agentic" if agentic else "pipeline",
        "prompt_tokens_total": sum(prompt_tokens(r) for r in recs),
        "output_tokens_total": sum(eval_tokens(r) for r in recs),
        "llm_seconds": round(sum(latency_seconds(r) for r in recs), 1),
        "warmup_seconds": round(
            sum(float(r.get("warmup_s", 0) or 0) for r in recs), 1),
        "n_l0_retries": sum(1 for r in recs if r.get("l0_retried")),
        "n_truncated": sum(1 for r in recs
                           for k in r if str(k).endswith("_truncated_chars")),
        "n_escalated_ctx": sum(
            1 for r in recs
            if isinstance(r.get("num_ctx"), (int, float)) and r["num_ctx"] > 32768),
        "steps": sorted({str(r.get("step", "?")) for r in recs}),
    }


def selection_ids(run_dir: Path) -> list[str]:
    """The selected sub-domain set, from selection.json (the authoritative
    artefact — goal FILES can be empty for legitimate reasons)."""
    f = run_dir / "steps" / "selection.json"
    if not f.is_file():
        return []
    try:
        sel = json.loads(f.read_text(encoding="utf-8")).get("selected", [])
    except json.JSONDecodeError:
        return []
    ids = []
    for e in sel:
        ids.append(e if isinstance(e, str) else (e.get("id") or ""))
    return [i for i in ids if i]


def goal_modules(run_dir: Path) -> tuple[list[dict], int]:
    """(rows, n_modules) across steps/goals/*.json.

    A module with an empty goals list is counted as a module: it is usually
    legitimate (the module carries no Sub-SO card for the confirmed
    regulations — 11 of the 38 corpus modules — and the assembler renders it
    with an explicit "None" line, as D-08.3 does in run_agent03_1971145), so
    dropping it would undercount the selection and misread an empty module as
    a missing one. Whether an empty module is legitimate is what L1 checks;
    here it is only counted.
    """
    rows: list[dict] = []
    n_modules = 0
    goals_dir = run_dir / "steps" / "goals"
    if not goals_dir.is_dir():
        return rows, 0
    for f in sorted(goals_dir.glob("*.json")):
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        n_modules += 1
        for g in data.get("goals", []):
            g.setdefault("subdomain", data.get("subdomain", ""))
            rows.append(g)
    return rows, n_modules


def artefact_metrics(run_dir: Path) -> dict:
    """Everything measurable from the assembled deliverable, no model needed.

    Scoped to the sections the model actually writes (§2 framing, §3 goals,
    §4 tensions). §0/§1/§5/§6 are code-derived, so including them would dilute
    every quality metric with content that cannot vary with the model.
    """
    out: dict = {"has_deliverable": False}
    doc = run_dir / "doc02_adjusted_goals.md"
    if not doc.is_file():
        return out
    out["has_deliverable"] = True
    out["deliverable_chars"] = len(doc.read_text(encoding="utf-8"))

    out["n_selected"] = len(selection_ids(run_dir))
    rows, n_modules = goal_modules(run_dir)
    out["n_modules"] = n_modules
    out["n_subdomains_with_rows"] = len({r.get("subdomain") for r in rows
                                         if r.get("subdomain")})
    out["n_empty_modules"] = n_modules - out["n_subdomains_with_rows"]
    if not rows:
        return out

    # Baselines and source texts, resolved with the SAME canonical extractors
    # the p4 content gate uses (compose.sub_so_objective), so the number the
    # aggregator reports is the number the gate measured rather than a
    # parallel implementation that could drift from it.
    baselines, sources = _run_corpus_context(run_dir, rows)
    score = quality.score_run(rows, baselines, sources)
    score.pop("rows", None)  # per-row detail stays available via --per-row
    out["quality"] = score
    out["n_goal_rows"] = len(rows)

    tensions = run_dir / "steps" / "tensions.json"
    if tensions.is_file():
        try:
            t = json.loads(tensions.read_text(encoding="utf-8"))
            out["n_tensions"] = len(t.get("tensions", []) or [])
        except json.JSONDecodeError:
            pass
    return out


def _run_corpus_context(run_dir: Path, rows: list[dict]) -> tuple[dict, list[str]]:
    """Baseline Sub-SO objectives and grounding sources for a run's goal rows.

    Keyed by "<subdomain>.<regulation>", NOT by regulation alone: two
    sub-domains can each carry a GDPR Sub-SO, and comparing a row against the
    wrong one yields a plausible but meaningless retention number.

    `sources` mirrors check_p4_quality exactly — the Sub-SO objectives plus the
    fact sheet and the §2 framing, because those are the texts a fabricated
    quantity would have to be absent from.
    """
    baselines: dict[str, str] = {}
    sources: list[str] = []
    for r in rows:
        sd = r.get("subdomain", "")
        reg = r.get("regulation") or r.get("baseline_source", "").rsplit(".", 1)[-1]
        if not sd or not reg:
            continue
        key = f"{sd}.{reg}"
        if key in baselines:
            continue
        try:
            text = sub_so_objective(REPO, sd, reg)
        except (OSError, ValueError):
            # no Sub-SO card for this pair: the row's retention is undefined,
            # which score_run reports as None rather than as a zero drop
            continue
        baselines[key] = text
        sources.append(text)

    steps_dir = run_dir / "steps"
    for name in ("fact_sheet.yaml", "framing.md"):
        f = steps_dir / name
        if f.is_file():
            sources.append(f.read_text(encoding="utf-8"))
    return baselines, sources


def run_metrics(run_dir: Path) -> dict:
    """All metrics for one run directory."""
    run_dir = Path(run_dir)
    manifest_path = run_dir / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8")) \
        if manifest_path.is_file() else {}
    cfg = runconfig.load(run_dir)

    history = manifest.get("stage_history", [])
    aborted = [h for h in history if h.get("status") == "aborted"]
    has_deliverable = (run_dir / "doc02_adjusted_goals.md").is_file()
    # A run that aborted mid-way and was then resumed and completed is L1
    # valid: run_agent03_1971145 aborted at the 80-turn budget, was resumed
    # twice, and produced an L1 PASS deliverable. What invalidates a run is an
    # abort as the LAST thing that happened, or no deliverable at all.
    last_status = history[-1].get("status") if history else None
    l1_pass = has_deliverable and (last_status != "aborted")

    return {
        "run_id": run_dir.name,
        "case_id": manifest.get("case_id"),
        "model": manifest.get("model"),
        "git_rev": manifest.get("aegis_git_rev") or None,
        "has_config": runconfig.config_path(run_dir).is_file(),
        "arm": cfg.get("arm"),
        "repeat": cfg.get("repeat"),
        "temperature": cfg.get("temperature"),
        "seed": cfg.get("seed"),
        "top_p": cfg.get("top_p"),
        "top_k": cfg.get("top_k"),
        "preapprove_gates": bool(cfg.get("preapprove_gates")),
        "stages": [h.get("stage") for h in history],
        "n_stages": len(history),
        "n_aborted": len(aborted),
        "l1_pass": l1_pass,
        # the selected set travels with the record so cross-run selection
        # divergence is computable without re-reading the directories
        "selection": selection_ids(run_dir),
        "trace": trace_metrics(run_dir),
        "artefact": artefact_metrics(run_dir),
    }


def discover(roots: list[str]) -> list[Path]:
    out: list[Path] = []
    for r in roots:
        p = Path(r)
        if (p / "manifest.json").is_file():
            out.append(p)
        elif p.is_dir():
            for child in sorted(p.iterdir()):
                if (child / "manifest.json").is_file():
                    out.append(child)
    # de-duplicate while preserving order
    seen, uniq = set(), []
    for p in out:
        rp = p.resolve()
        if rp not in seen:
            seen.add(rp)
            uniq.append(p)
    return uniq


# --------------------------------------------------------------------------
# reporting
# --------------------------------------------------------------------------

def _fmt(v, nd=3) -> str:
    if v is None:
        return "—"
    if isinstance(v, float):
        return f"{v:.{nd}f}"
    return str(v)


def summarise(records: list[dict]) -> list[str]:
    lines: list[str] = []
    hdr = (f"{'run_id':<28} {'arm':<5} {'rep':<4} {'seed':<6} {'temp':<5} "
           f"{'L1':<4} {'calls':<6} {'llm_s':<8} {'ret_mean':<9} {'ret_min':<8} "
           f"{'rows':<5} {'sd':<4} {'narrow':<7} {'tens':<5}")
    lines.append(hdr)
    lines.append("-" * len(hdr))
    for r in records:
        t = r["trace"]
        q = r["artefact"].get("quality", {})
        ret = q.get("retention", {})
        mix = q.get("adjustment_mix", {})
        lines.append(
            f"{r['run_id']:<28} {_fmt(r['arm'] or '—'):<5} "
            f"{_fmt(r['repeat'] if r['repeat'] is not None else '—'):<4} "
            f"{_fmt(r['seed'] if r['seed'] is not None else 'none'):<6} "
            f"{_fmt(r['temperature']):<5} "
            f"{('PASS' if r['l1_pass'] else 'fail'):<4} "
            f"{t['n_calls']:<6} {_fmt(t['llm_seconds'], 1):<8} "
            f"{_fmt(ret.get('mean')):<9} {_fmt(ret.get('min')):<8} "
            f"{_fmt(r['artefact'].get('n_goal_rows')):<5} "
            f"{_fmt(q.get('n_subdomains')):<4} "
            f"{_fmt(mix.get('narrowed', 0)):<7} "
            f"{_fmt(r['artefact'].get('n_tensions')):<5}")
    return lines


def arm_summary(records: list[dict]) -> list[str]:
    """Per-arm distribution — the table EXP-02 is actually read from."""
    arms: dict[str, list[dict]] = {}
    for r in records:
        arms.setdefault(str(r["arm"]), []).append(r)

    lines: list[str] = []
    lines.append(f"{'arm':<6} {'n':<4} {'L1 pass':<9} {'ret mean±sd':<18} "
                 f"{'ret min':<9} {'calls':<7} {'llm_s':<9} {'rows':<6} {'sd':<4}")
    lines.append("-" * 72)
    for arm in sorted(arms):
        rs = arms[arm]
        rets = [r["artefact"]["quality"]["retention"]["mean"]
                for r in rs
                if r["artefact"].get("quality", {}).get("retention", {}).get("mean")
                is not None]
        sd = statistics.stdev(rets) if len(rets) > 1 else None
        passes = sum(1 for r in rs if r["l1_pass"])
        calls = [r["trace"]["n_calls"] for r in rs]
        secs = [r["trace"]["llm_seconds"] for r in rs]
        rows_ = [r["artefact"].get("n_goal_rows") for r in rs
                 if r["artefact"].get("n_goal_rows")]
        sds = [r["artefact"]["quality"].get("n_subdomains") for r in rs
               if r["artefact"].get("quality", {}).get("n_subdomains")]
        lines.append(
            f"{arm:<6} {len(rs):<4} {f'{passes}/{len(rs)}':<9} "
            f"{_fmt(statistics.mean(rets) if rets else None) + '±' + _fmt(sd):<18} "
            f"{_fmt(min(rets) if rets else None):<9} "
            f"{_fmt(statistics.mean(calls) if calls else None):<7} "
            f"{_fmt(statistics.mean(secs) if secs else None, 1):<9} "
            f"{_fmt(statistics.mean(rows_) if rows_ else None):<6} "
            f"{_fmt(statistics.mean(sds) if sds else None):<4}")
    return lines


def selection_divergence(records: list[dict]) -> list[str]:
    """Selection-set stability: Jaccard of each run's selection against the
    modal selection set. This is the number that says whether EXP-01's
    headline "37 vs 38" was a signal or one draw from a distribution."""
    sets = [set(r["selection"]) for r in records if r["selection"]]
    if len(sets) < 2:
        return ["selection divergence      : <2 runs with a selection — nothing to compare"]

    def jac(a: set, b: set) -> float:
        return len(a & b) / len(a | b) if (a | b) else 1.0

    # the modal set: the member with the highest mean Jaccard to the others
    modal = max(sets, key=lambda s: sum(jac(s, t) for t in sets) / (len(sets) - 1))
    jaccards = sorted(jac(s, modal) for s in sets)
    identical = sum(1 for j in jaccards if j == 1.0)
    return [
        f"selection modal size       : {len(modal)}",
        f"selection Jaccard vs modal : mean {statistics.mean(jaccards):.3f}  "
        f"min {jaccards[0]:.3f}  ({identical}/{len(sets)} identical to modal)",
    ]


def integrity_checks(records: list[dict]) -> list[str]:
    """The internal controls the pre-registration demands.

    These are the cheapest diagnostics in the programme and the most
    diagnostic: a run whose §5 rows move, or whose git rev is missing, or whose
    trace disagrees with its own artefact, is not a valid experimental unit no
    matter how good its headline number looks.
    """
    out: list[str] = []

    missing_rev = [r["run_id"] for r in records if not r["git_rev"]]
    out.append(f"runs without aegis_git_rev : {len(missing_rev)}"
               + (f"  {missing_rev[:5]}" if missing_rev else ""))

    missing_cfg = [r["run_id"] for r in records if not r["has_config"]]
    out.append(f"runs without config.json   : {len(missing_cfg)}"
               + (f"  {missing_cfg[:5]}" if missing_cfg else ""))

    no_deliv = [r["run_id"] for r in records if not r["artefact"]["has_deliverable"]]
    out.append(f"runs without a deliverable : {len(no_deliv)}"
               + (f"  {no_deliv[:5]}" if no_deliv else ""))

    aborted = [r["run_id"] for r in records if r["n_aborted"]]
    out.append(f"runs with an aborted stage  : {len(aborted)}"
               + (f"  {aborted[:5]}" if aborted else ""))

    # The control that catches a broken isolation: §5 is code-derived, so a
    # run whose Track B row count differs from its peers is not a sampling
    # variation — it is a different pipeline.
    row_counts = {}
    for r in records:
        n = r["artefact"].get("n_goal_rows")
        if n:
            row_counts.setdefault(n, []).append(r["run_id"])
    if row_counts:
        out.append(f"goal-row count modes        : "
                   + ", ".join(f"{n}×{len(v)}" for n, v in
                               sorted(row_counts.items(), key=lambda kv: -len(kv[1]))[:5]))

    escalated = sum(1 for r in records if r["trace"]["n_escalated_ctx"])
    out.append(f"runs with a ctx escalation  : {escalated}")

    retr = sum(1 for r in records if r["trace"]["n_l0_retries"])
    out.append(f"runs with an L0 repair      : {retr}")
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("roots", nargs="+",
                    help="run directories, or a directory containing them")
    ap.add_argument("--json", metavar="PATH", help="write full records as JSON")
    ap.add_argument("--arm-summary", action="store_true",
                    help="per-arm distribution table (the EXP-02 view)")
    ap.add_argument("--checks", action="store_true",
                    help="run the integrity controls and print them")
    args = ap.parse_args()

    dirs = discover(args.roots)
    if not dirs:
        print("no run directories found (looked for manifest.json)", file=sys.stderr)
        return 2

    records = [run_metrics(d) for d in dirs]
    print(f"AEGIS run aggregation — {len(records)} run(s)\n")
    print("\n".join(summarise(records)))
    print()
    print("\n".join(arm_summary(records)))

    if args.checks:
        print("\nintegrity controls")
        print("-" * 72)
        print("\n".join(integrity_checks(records)))
        print("\n".join(selection_divergence(records)))

    if args.json:
        Path(args.json).write_text(json.dumps(records, indent=1, default=str),
                                   encoding="utf-8")
        print(f"\nfull records written to {args.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
