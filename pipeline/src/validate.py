#!/usr/bin/env python3
"""validate.py — local L1 validator for a completed Phase 1 run folder.

Covers SPEC §8 items that are mechanically checkable (2–6, 9), the
deterministic-assembly guarantee for the Doc02 deliverable
(doc02_adjusted_goals.md: every §2–§6 table is diffed against the artifact or
the code derivation that produced it), a pipeline-layer hygiene check
equivalent to doc_lint R12 for the run folder (doc_lint itself scopes cases/,
example/, output/, templates/), and a trace-consistency report (inputs/ and
outputs/ file counts vs trace.jsonl lines vs manifest call count).

Run this locally after sync_down, where baseline/ exists:
  python3 pipeline/src/validate.py --run-dir pipeline/runs/<RUN_ID> [--repo <aegis-mvp>]
Exit 0 iff every check passes.
"""

from __future__ import annotations

import argparse
import json
import re
import threading
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from compose import (REGULATIONS, SD_RE, confirmed_regulations, domain_dir,
                     load_case, objective_paragraph, parse_simple_yaml,
                     sub_so_objective)  # noqa: E402
from controls import goal_anchors, parse_overrides, sd_control_sections, track_b_rows  # noqa: E402

REPO_DEFAULT = Path(__file__).resolve().parents[2]

# Per-thread findings. A module-level list is shared mutable state: a
# concurrent caller (the inspector validated several runs at once) had one
# run's findings leak into another's verdict — a run that passes was reported
# FAIL. thread-local fixes it for every caller.
_TLS = threading.local()


def _findings() -> list[str]:
    f = getattr(_TLS, "findings", None)
    if f is None:
        f = _TLS.findings = []
    return f

PROPERTY_LONG = {"c": "Confidentiality", "i": "Integrity", "a": "Availability",
                 "privacy-right": "Privacy Right", "accountability": "Accountability"}


def check(name: str, ok: bool, detail: str = "") -> bool:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        _findings().append(f"{name}: {detail}")
    return ok


def warn(name: str, detail: str = "") -> None:
    print(f"  [WARN] {name}" + (f" — {detail}" if detail else ""))



def resolve_control_anchor(repo: Path, anchor: str) -> bool:
    """Anchor id resolves to a control JSON under CONTROLS/ (R2b), any of the
    enforced referentials (NIST CSF 2.0 / NIST PF 1.1 / NIST AI RMF)."""
    a = anchor.strip().strip("`").replace("*", "")
    if not re.fullmatch(r"[A-Z]{2,7}(\.[A-Z0-9]+)?-[A-Z0-9.]+(-P\d+)?", a):
        return False
    hits = list((repo / "baseline" / "CONTROLS").rglob(f"{a}.json"))
    return bool(hits)


def resolve_reg_source(repo: Path, sd_id: str, source: str) -> tuple[bool, str]:
    """Regulatory source resolves to articles/ copy or verbatim text in regs/<REG>.md (R2a)."""
    sd_dir = domain_dir(repo, sd_id)
    for reg, num in re.findall(r"\b(GDPR|CRA|NIS2?|DORA|AI_Act)\s+Art(?:icle)?\.?\s*([0-9]+)", source):
        art_files = list((sd_dir / "articles").glob(f"{reg}*Art*{num}*")) if (sd_dir / "articles").exists() else []
        if art_files:
            continue
        regf = sd_dir / "regs" / f"{reg}.md"
        if regf.exists() and re.search(rf"Art(?:icle)?\.?\s*{num}\b", regf.read_text(encoding="utf-8")):
            continue
        return False, f"{sd_id}: {reg} Art. {num} neither in articles/ nor quotable from regs/{reg}.md"
    return True, ""


def doc_sections(doc: str) -> dict[str, str]:
    """Split the assembled deliverable into its `## §N` sections (H2 only —
    the H3 `### D-XX.Y` and `### §6.N` blocks stay inside their sections)."""
    out: dict[str, str] = {}
    for part in re.split(r"(?m)^(?=## §)", doc):
        m = re.match(r"## (§\d)", part)
        if m:
            out[m.group(1)] = part.strip()
    return out


def md_table_rows(section: str) -> list[list[str]]:
    """Markdown table rows of a section as cell lists (separator rows dropped)."""
    rows: list[list[str]] = []
    for line in section.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
            continue
        rows.append(cells)
    return rows


def md_table_defects(text: str) -> list[str]:
    """Tables whose rendered structure is broken.

    A markdown table only renders when the header, the separator row and every
    body row carry the SAME number of cells. `md_table_rows` drops separator
    rows and never counts them, so a header/separator mismatch is invisible to
    every content check — the table silently renders as literal pipe text.
    That is exactly how the §3 goal tables shipped with a 10-cell header over a
    9-cell separator while L1 still reported PASS.
    """
    defects: list[str] = []
    rows: list[tuple[int, str]] = []

    def close() -> None:
        if not rows:
            return
        start, header = rows[0]
        ncol = len(_split_row(header))
        if len(rows) < 2 or not _is_separator(rows[1][1]):
            defects.append(f"line {start}: no valid separator row under a {ncol}-column header")
            return
        nsep = len(_split_row(rows[1][1]))
        if nsep != ncol:
            defects.append(f"line {start}: header has {ncol} cells, separator has {nsep} "
                           f"(table will not render)")
        for lineno, row in rows[2:]:
            n = len(_split_row(row))
            if n != ncol:
                defects.append(f"line {lineno}: body row has {n} cells, header has {ncol}")

    for lineno, line in enumerate(text.splitlines(), 1):
        if line.strip().startswith("|"):
            rows.append((lineno, line))
        else:
            close()
            rows = []
    close()
    return defects


def _split_row(line: str) -> list[str]:
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return s.split("|")


def _is_separator(line: str) -> bool:
    s = line.strip()
    return bool(s.startswith("|")) and bool(re.fullmatch(r"\|[\s:|-]+\|", s))


def validate_run(repo: Path, run: Path) -> list[str]:
    """Run every L1 check for one run folder; returns the findings list
    (empty == PASS). Used by steps.py stage_p5 (post-assembly gate) and main()."""
    _findings().clear()
    steps = run / "steps"
    fact = parse_simple_yaml((steps / "fact_sheet.yaml").read_text(encoding="utf-8")) \
        if (steps / "fact_sheet.yaml").exists() else None
    verdicts = json.loads((steps / "verdicts.json").read_text()) if (steps / "verdicts.json").exists() else None
    selection = json.loads((steps / "selection.json").read_text()) if (steps / "selection.json").exists() else None
    doc_path = run / "doc02_adjusted_goals.md"
    doc = doc_path.read_text(encoding="utf-8") if doc_path.exists() else None

    print("== §8 item 2 — confirmed regulation set, none silently missing ==")
    if verdicts:
        regs = [v["regulation"] for v in verdicts["verdicts"]]
        check("5 canonical rows present", sorted(regs) == sorted(REGULATIONS), f"{regs}")
    elif doc is None and not selection:
        print("  [SKIP] stage p2 not reached yet (partial run)")
    else:
        check("verdicts.json present", False, "run progressed past p2 but verdicts.json is missing")

    print("== §8 item 3 — sub-domain codes exist in the corpus ==")
    if selection:
        bad = [s["id"] for s in selection["selected"] if not re.match(SD_RE, s["id"])
               or not (repo / "baseline" / "domains").glob(f"D-{s['id'][2:4]}*/{s['id']}")]
        check("all selected IDs canonical + on disk", not bad, f"{bad}")

    print("== §8 item 4 — AG IDs unique, sub-domain part matches selection ==")
    goals_by_sd: dict[str, list] = {}
    if (steps / "goals").exists():
        for jf in sorted((steps / "goals").glob("*.json")):
            data = json.loads(jf.read_text())
            goals_by_sd[data["subdomain"]] = data["goals"]
    goal_rows = [g for gs in goals_by_sd.values() for g in gs]
    ids = [g["id"] for g in goal_rows]
    check("AG IDs unique", len(ids) == len(set(ids)), f"{len(set(ids))}/{len(ids)} unique")
    sd_parts = {s["id"] for s in selection["selected"]} if selection else set()
    mism = {g["id"] for g in goal_rows if g["id"][3:].rsplit("-", 1)[0] not in sd_parts}
    check("AG sub-domain part matches selection rows", not mism, f"{mism}")

    print("== §8 item 5 — regulatory sources resolve (R2a) ==")
    unresolved = []
    for sd, gs in goals_by_sd.items():
        for g in gs:
            ok, why = resolve_reg_source(repo, sd, g["source"])
            if not ok:
                unresolved.append(f"{g['id']}: {g['source']} — {why}")
    check("every cited article resolves", not unresolved, f"{len(unresolved)} unresolved: {unresolved[:3]}")

    print("== §8 item 6 — derived control anchors resolve (R2b, by construction) ==")
    bad_anchors = []
    for sd, gs in goals_by_sd.items():
        for g in gs:
            for tok in goal_anchors(repo, sd, [g["baseline_source"]]):
                if not resolve_control_anchor(repo, tok):
                    bad_anchors.append(f"{g['id']}: {tok}")
    check("every derived anchor exists in CONTROLS/", not bad_anchors, f"{bad_anchors}")

    print("== §8 item 9 — pattern, property, parent, baseline source, adjustment ==")
    bad9 = []
    for g in goal_rows:
        if g["pattern"] not in {"achieve", "cease", "maintain", "avoid", "optimize"}:
            bad9.append(f"{g['id']} pattern")
        if g["property"] not in {"c", "i", "a", "privacy-right", "accountability"}:
            bad9.append(f"{g['id']} property {g['property']!r}")
        if not re.fullmatch(r"SO-D-\d{2}\.\d\.HL", g["parent"]):
            bad9.append(f"{g['id']} parent {g['parent']!r}")
        if not re.fullmatch(rf"SG-D-\d{{2}}\.\d\.({'|'.join(REGULATIONS)})", g["baseline_source"]):
            bad9.append(f"{g['id']} baseline source {g['baseline_source']!r}")
        if not g.get("adjustment", "").strip():
            bad9.append(f"{g['id']} empty adjustment")
    check("every goal row valid", not bad9, f"{bad9}")

    print("== assembled Doc02 == artifacts + code derivations (deterministic guarantee) ==")
    if doc:
        secs = doc_sections(doc)

        def norm(s: str) -> str:
            return " ".join(s.split())

        confirmed = confirmed_regulations(run) if verdicts else []
        sel_ids = sorted(s["id"] for s in selection["selected"]) if selection else []
        names = {s["id"]: s["name"] for s in selection["selected"]} if selection else {}
        case_id = json.loads((run / "manifest.json").read_text())["case_id"] \
            if (run / "manifest.json").exists() else None
        overrides = parse_overrides(load_case(repo, case_id).get("track_b_overrides")) if case_id else {}

        order = [m.group(1) for m in re.finditer(r"^## (§\d)", doc, re.M)]
        check("§0–§6 present exactly once, in order",
              order == ["§0", "§1", "§2", "§3", "§4", "§5", "§6"], f"{order}")

        # §2 framing table == framing.md (data rows only — headers dropped)
        def data_rows(section: str, header: str, width: int | None = None) -> list[list[str]]:
            out = [[norm(c) for c in row] for row in md_table_rows(section)
                   if norm(row[0]).lower() != header.lower()]
            return [r for r in out if width is None or len(r) == width]

        fr_path = steps / "framing.md"
        if fr_path.exists():
            want2 = data_rows(fr_path.read_text(encoding="utf-8"), "dimension", width=2)
            got2 = data_rows(secs.get("§2", ""), "dimension", width=2)
            check("§2 framing table == framing.md", want2 == got2, f"diff: {want2} != {got2}")
        else:
            check("framing.md present", False, "stage p3f artifact missing")

        # §3: per sub-domain — HL paragraph verbatim, per-regulation baseline
        # paragraphs verbatim, goal rows == JSON + derived anchors
        bad3 = []
        for blk in re.split(r"(?m)^(?=### D-)", secs.get("§3", ""))[1:]:
            sd = blk.split("—")[0].strip().lstrip("#").strip()
            hl_m = re.search(r"\*\*High-Level Security Goal \(SO-D-\d{2}\.\d\.HL\):\*\* (.*)", blk)
            if not hl_m:
                bad3.append(f"{sd}: HL goal paragraph missing")
            elif norm(hl_m.group(1)) != norm(objective_paragraph(domain_dir(repo, sd))):
                bad3.append(f"{sd}: HL paragraph != corpus objective.md")
            gs = goals_by_sd.get(sd, [])
            if not gs:
                if "_None — no Sub-SO for the confirmed regulations in this module._" not in blk:
                    bad3.append(f"{sd}: module carries no Sub-SO for the confirmed "
                                f"regulations but the None note is missing")
                continue
            for reg in sorted({g["regulation"] for g in gs}, key=REGULATIONS.index):
                bm = re.search(rf"\*\*Regulation baseline — `SG-{re.escape(sd)}\.{reg}` \({reg}\):\*\* (.*)", blk)
                if not bm:
                    bad3.append(f"{sd}: regulation baseline paragraph for {reg} missing")
                elif norm(bm.group(1)) != norm(sub_so_objective(repo, sd, reg)):
                    bad3.append(f"{sd}: baseline paragraph for {reg} != corpus Sub-SO objective")
            rows_d = [c for c in md_table_rows(blk) if c and re.match(r"`?AG-", c[0])]
            want = [[f"`{g['id']}`", norm(g["goal"]), norm(g["implication"]), g["pattern"],
                     PROPERTY_LONG[g["property"]], g["parent"], g["regulation"],
                     norm(g["source"]),
                     ", ".join(goal_anchors(repo, sd, [g["baseline_source"]])) or "—",
                     norm(g["adjustment"])] for g in gs]
            got = [[norm(c) for c in row] for row in rows_d]
            if want != got:
                bad3.append(f"{sd}: goal table != JSON + derivation")
            thin = [g["id"] for g in gs if len(g.get("implication", "").split()) < 4
                    or len(g.get("goal", "").split()) < 6]
            if thin:
                bad3.append(f"{sd}: thin Adjusted goal / implication rows: {thin}")
        heads3 = [b.split("—")[0].strip().lstrip("#").strip()
                  for b in re.split(r"(?m)^(?=### D-)", secs.get("§3", ""))[1:]]
        check("§3 blocks == selected sub-domains, HL verbatim, tables == JSON+derivation",
              not bad3 and heads3 == sel_ids, f"{bad3}; heads={heads3}")
        guide = "### §3.0" in secs.get("§3", "")
        check("§3.0 interpretation guide present", guide, "missing §3.0 block")

        # Calibration health check (anti-lazy-defaulting guard)
        all_goals = [g for gs in goals_by_sd.values() for g in gs]
        if all_goals:
            n_tot = len(all_goals)
            n_verb = sum(1 for g in all_goals if norm(g.get("adjustment", "")).startswith(("unchanged", "verbatim")))
            ratio_verb = n_verb / n_tot
            delegation_kw = re.compile(
                r"\b(cloud provider|managed service|third-party|vendor|supplier|"
                r"managed|delegat(ed?|ing)|external host(ing)?|saas provider)\b", re.I)
            contradictions = [
                g.get("id", "?") for g in all_goals
                if norm(g.get("adjustment", "")).startswith(("unchanged", "verbatim"))
                and delegation_kw.search(g.get("implication", ""))
            ]
            calib_msg = f"{n_verb}/{n_tot} ({ratio_verb:.0%}) verbatim"
            if contradictions:
                calib_msg += f"; {len(contradictions)} contradiction(s) (delegation in implication vs verbatim in adjustment): {contradictions[:4]}"
            if ratio_verb > 0.70 or contradictions:
                warn("calibration health (anti-lazy-defaulting guard)", calib_msg)
            else:
                print(f"  [PASS] calibration health — {calib_msg}")

        # §4 == tensions.json (or None)
        tpath = steps / "tensions.json"
        tensions = json.loads(tpath.read_text()).get("tensions", []) if tpath.exists() else None
        if tensions is None:
            check("tensions.json present", False, "stage p4t artifact missing (multi-regulation run)")
        elif tensions:
            got_t = re.findall(r"(?m)^### (T-\d{3})", secs.get("§4", ""))
            want_t = [t["id"] for t in tensions]
            empty_res = [t["id"] for t in tensions
                         if not re.search(rf"### {t['id']}.*?\*\*Resolution:\*\* \S", secs.get("§4", ""), re.S)]
            check("§4 tension blocks == tensions.json with non-empty resolutions",
                  got_t == want_t and not empty_res, f"ids {got_t} vs {want_t}; empty resolutions {empty_res}")
        else:
            check("§4 records the mono/none-tension case",
                  bool(re.search(r"(?m)^None\b", secs.get("§4", ""))), f"got: {secs.get('§4', '')[:120]!r}")

        # §5 == deterministic matrix derivation (data rows only)
        if fact and selection:
            want5 = [[r["subdomain"], r["scale"], r["inheritability"], r["priority"],
                      r["tier"], norm(r["rationale"])]
                     for r in track_b_rows(fact, sel_ids, overrides)]
            got5 = data_rows(secs.get("§5", ""), "sub-domain", width=6)
            check("§5 Track B rows == matrix derivation", want5 == got5,
                  f"diff: {want5} != {got5}")

        # §6 == controls derivation
        if selection and (verdicts or not goal_rows):
            confirmed_eff = confirmed or []
            bad6 = []
            blocks6 = re.split(r"(?m)^(?=### §6\.)", secs.get("§6", ""))[1:]
            got6_sds = [m.group(1) for b in blocks6
                        if (m := re.match(r"### §6\.\d+ (D-\d{2}\.\d)", b))]
            for i, sd in enumerate(sel_ids, 1):
                want_secs = sd_control_sections(repo, sd, confirmed_eff)
                blk = next((b for b in blocks6
                            if re.match(rf"### §6\.{i} {re.escape(sd)}\b", b)), None)
                if blk is None:
                    bad6.append(f"{sd}: §6.{i} block missing")
                    continue
                parts6 = {p.split("\n", 1)[0].strip(): p.split("\n", 1)[1] if "\n" in p else ""
                          for p in re.split(r"(?m)^#### ", blk)[1:]}
                for sec in want_secs:
                    if not sec["rows"]:
                        continue
                    want_rows = [[r["function"], r["id"], norm(r["text"]), r["path"]]
                                 for r in sec["rows"]]
                    sec_tail = parts6.get(sec["title"], "")
                    got_rows = data_rows(sec_tail, "function", width=4)
                    if want_rows != got_rows:
                        bad6.append(f"{sd}/{sec['title']}: table != derivation")
            check("§6 blocks == controls derivation, one per selected sub-domain",
                  not bad6 and got6_sds == sel_ids, f"{bad6}; heads={got6_sds}")
    else:
        print("  [SKIP] no assembled document yet (partial run)")

    print("== R12-hygiene over the run folder (placeholders / TODO / control paths) ==")
    hygiene_bad = []
    for f in run.rglob("*.md"):
        t = f.read_text(encoding="utf-8")
        if re.search(r"\|\s*\?\s*\|", t) or re.search(r"/\?\w", t) or re.search(r"\bTODO\b|\bFIXME\b", t):
            hygiene_bad.append(str(f.relative_to(run)))
        # NB: full-match group — a lone capturing group would make findall
        # return just the referential name without the path
        for path in re.findall(r"((?:NIST_CSF|NIST_PF|NIST_AI_RMF)/[\w./-]+\.json)", t):
            if not (repo / "baseline" / "CONTROLS" / path.replace("NIST_CSF/", "NIST_CSF_2.0/", 1)
                    .replace("NIST_PF/", "NIST_PF/", 1)).exists():
                # try direct resolution under the enforced aliases
                resolved = (repo / "baseline" / "CONTROLS" / path).exists() or \
                           (repo / "baseline" / "CONTROLS" / "NIST_CSF_2.0" / path.split("/", 1)[1]).exists()
                if not resolved:
                    hygiene_bad.append(f"{f.relative_to(run)}: {path}")
    check("no placeholders / unresolved control paths", not hygiene_bad, f"{hygiene_bad[:8]}")

    print("== table structure ==")
    # A table with a header/separator width mismatch does not render, but every
    # content check above compares CELLS after dropping the separator row — so
    # the defect must be checked structurally, on the assembled document itself.
    table_bad = md_table_defects(doc) if doc else []
    check("every assembled table renders (header == separator == body width)",
          not table_bad, f"{len(table_bad)} defect(s): {table_bad[:6]}")

    print("== trace consistency ==")
    trace_path = run / "trace.jsonl"
    calls = [json.loads(l) for l in trace_path.read_text().splitlines() if l.strip()] if trace_path.exists() else []
    manifest = json.loads((run / "manifest.json").read_text())
    is_agent = (manifest.get("mode") == "agentic"
                or any(s.get("stage") == "agentic" for s in manifest.get("stage_history", [])))
    n_ok = sum(1 for c in calls if c.get("status") == "ok")
    if is_agent:
        # agent turns: one trace record per accepted LLM turn — inputs are
        # *_messages.json, outputs are *_turn_output.md; failed attempts leave
        # only a raw response behind and must not break the accepted-turn count
        n_inputs = len(list((run / "inputs").glob("*_messages.json")))
        n_outputs = len(list((run / "outputs").glob("*_turn_output.md")))
        check("accepted turns == turn inputs == turn outputs",
              n_ok == n_inputs == n_outputs,
              f"ok={n_ok} inputs={n_inputs} outputs={n_outputs} (trace lines={len(calls)})")
    else:
        n_inputs = len(list((run / "inputs").glob("*_user.md")))
        n_outputs = len(list((run / "outputs").glob("*_output.md")))
        check("trace.jsonl lines == inputs == outputs", len(calls) == n_inputs == n_outputs,
              f"trace={len(calls)} inputs={n_inputs} outputs={n_outputs} (ok calls={n_ok})")
    check("manifest n_calls_total matches trace", manifest.get("n_calls_total") == len(calls),
          f"manifest={manifest.get('n_calls_total')} trace={len(calls)}")
    # a step is complete iff its LAST call succeeded; earlier failed calls are
    # retained history (retries after mid-stage aborts) — informational only
    last_by_step: dict[str, dict] = {}
    for c in calls:
        last_by_step[c["step"]] = c
    open_failures = [s for s, c in last_by_step.items() if c.get("status") != "ok"]
    check("every step's last call succeeded", not open_failures, f"{open_failures}")
    retries = [f"{c['seq']}({c['step']})" for c in calls if c.get("status") != "ok"]
    if retries:
        print(f"  [INFO] {len(retries)} retained failed call(s) from earlier jobs, "
              f"retried later: {retries}")

    print()
    if _findings():
        print(f"RESULT: FAIL — {len(_findings())} finding(s)")
        for f in _findings():
            print(f"  - {f}")
        return _findings()
    print("RESULT: PASS — all L1 checks green")
    return []


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--run-dir", type=Path, required=True)
    ap.add_argument("--repo", type=Path, default=REPO_DEFAULT)
    args = ap.parse_args()
    return 1 if validate_run(args.repo.resolve(), args.run_dir.resolve()) else 0


if __name__ == "__main__":
    sys.exit(main())
