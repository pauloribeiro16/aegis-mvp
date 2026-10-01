#!/usr/bin/env python3
"""validate.py — local L1 validator for a completed Phase 1 run folder.

Covers SPEC §8 items that are mechanically checkable (2–6, 9), a pipeline-layer
hygiene check equivalent to doc_lint R12 for the run folder (doc_lint itself
scopes cases/, example/, output/, templates/), and a trace-consistency report
(inputs/ and outputs/ file counts vs trace.jsonl lines vs manifest call count).

Run this locally after sync_down, where baseline/ exists:
  python3 pipeline/src/validate.py --run-dir pipeline/runs/<RUN_ID> [--repo <aegis-mvp>]
Exit 0 iff every check passes.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from compose import REGULATIONS, SD_RE, domain_dir  # noqa: E402

REPO_DEFAULT = Path(__file__).resolve().parents[2]

FINDINGS: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        FINDINGS.append(f"{name}: {detail}")
    return ok


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


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--run-dir", type=Path, required=True)
    ap.add_argument("--repo", type=Path, default=REPO_DEFAULT)
    args = ap.parse_args()
    repo = args.repo.resolve()
    run = args.run_dir.resolve()

    print(f"== validating {run.name} against {repo} ==")
    steps = run / "steps"
    fact = (steps / "fact_sheet.yaml").read_text(encoding="utf-8") if (steps / "fact_sheet.yaml").exists() else None
    verdicts = json.loads((steps / "verdicts.json").read_text()) if (steps / "verdicts.json").exists() else None
    selection = json.loads((steps / "selection.json").read_text()) if (steps / "selection.json").exists() else None
    doc_path = run / "phase1_output.md"
    doc = doc_path.read_text(encoding="utf-8") if doc_path.exists() else None

    print("== §8 item 2 — §2 covers every regulation, none silently missing ==")
    if verdicts:
        regs = [v["regulation"] for v in verdicts["verdicts"]]
        check("5 canonical rows present", sorted(regs) == sorted(REGULATIONS), f"{regs}")
    else:
        check("verdicts.json present", False, "stage p2 not run")

    print("== §8 item 3 — sub-domain codes exist in the corpus ==")
    if selection:
        bad = [s["id"] for s in selection["selected"] if not re.match(SD_RE, s["id"])
               or not (repo / "baseline" / "domains").glob(f"D-{s['id'][2:4]}*/{s['id']}")]
        check("all selected IDs canonical + on disk", not bad, f"{bad}")

    print("== §8 item 4 — AG IDs unique, sub-domain part matches §3 ==")
    goal_rows = []
    if (steps / "goals").exists():
        for jf in sorted((steps / "goals").glob("*.json")):
            data = json.loads(jf.read_text())
            goal_rows.extend(data["goals"])
    ids = [g["id"] for g in goal_rows]
    check("AG IDs unique", len(ids) == len(set(ids)), f"{len(set(ids))}/{len(ids)} unique")
    sd_parts = {s["id"] for s in selection["selected"]} if selection else set()
    mism = {g["id"] for g in goal_rows if g["id"][3:].rsplit("-", 1)[0] not in sd_parts}
    check("AG sub-domain part matches §3 rows", not mism, f"{mism}")

    print("== §8 item 5 — regulatory sources resolve (R2a) ==")
    unresolved = []
    if selection and (steps / "goals").exists():
        for jf in sorted((steps / "goals").glob("*.json")):
            data = json.loads(jf.read_text())
            for g in data["goals"]:
                ok, why = resolve_reg_source(repo, data["subdomain"], g["source"])
                if not ok:
                    unresolved.append(f"{g['id']}: {g['source']} — {why}")
    check("every cited article resolves", not unresolved, f"{len(unresolved)} unresolved")

    print("== §8 item 6 — control anchors resolve (R2b) ==")
    bad_anchors = []
    for g in goal_rows:
        a = g.get("anchor", "—")
        if a.strip() in ("—", "-"):
            continue
        for tok in re.split(r"[;,/]\s*", a):
            tok = tok.strip()
            if tok and tok not in ("—", "-") and not resolve_control_anchor(repo, tok):
                bad_anchors.append(f"{g['id']}: {tok}")
    check("every anchor exists in CONTROLS/", not bad_anchors, f"{bad_anchors}")

    print("== §4.1 Source=SR-<REG>-NNN exists in mapping store ==")
    bad_sr = []
    m41 = re.findall(r"\|\s*`?(AG-D-\d{2}\.\d-\d{3})`?\s*\|[^|]*\|[^|]*\|[^|]*\|[^|]*\|\s*`?(SR-[A-Za-z_0-9.]+-NNN|SR-[A-Za-z_0-9.\-]+)`?", doc or "")
    for gid, sr in m41:
        reg = sr.split("-")[1]
        jf = repo / "baseline" / "MAPPINGS" / "sr_control_mappings" / f"{reg}.json"
        if not jf.exists() or sr not in jf.read_text(encoding="utf-8"):
            bad_sr.append(f"{gid}: {sr}")
    check("§4.1 SR ids resolve in mapping store" if doc else "§4.1 skipped (no document yet)",
          (not bad_sr) if doc else True, f"{bad_sr}")

    print("== §8 item 9 — pattern, property, parent, adjustment ==")
    bad9 = []
    for g in goal_rows:
        if g["pattern"] not in {"achieve", "cease", "maintain", "avoid", "optimize"}:
            bad9.append(f"{g['id']} pattern")
        if g["property"] not in {"c", "i", "a", "privacy-right", "accountability"}:
            bad9.append(f"{g['id']} property {g['property']!r}")
        if not re.fullmatch(r"SO-D-\d{2}\.\d\.HL", g["parent"]):
            bad9.append(f"{g['id']} parent {g['parent']!r}")
        if not g.get("adjustment", "").strip():
            bad9.append(f"{g['id']} empty adjustment")
    check("every goal row valid", not bad9, f"{bad9}")

    print("== R12-hygiene over the run folder (placeholders / TODO / control paths) ==")
    hygiene_bad = []
    for f in run.rglob("*.md"):
        t = f.read_text(encoding="utf-8")
        if re.search(r"\|\s*\?\s*\|", t) or re.search(r"/\?\w", t) or re.search(r"\bTODO\b|\bFIXME\b", t):
            hygiene_bad.append(str(f.relative_to(run)))
        for path in re.findall(r"(NIST_CSF|NIST_PF|NIST_AI_RMF)/[\w./-]+\.json", t):
            if not (repo / "baseline" / "CONTROLS" / path.replace("NIST_CSF/", "NIST_CSF_2.0/", 1)
                    .replace("NIST_PF/", "NIST_PF/", 1)).exists():
                # try direct resolution under the enforced aliases
                resolved = (repo / "baseline" / "CONTROLS" / path).exists() or \
                           (repo / "baseline" / "CONTROLS" / "NIST_CSF_2.0" / path.split("/", 1)[1]).exists()
                if not resolved:
                    hygiene_bad.append(f"{f.relative_to(run)}: {path}")
    check("no placeholders / unresolved control paths", not hygiene_bad, f"{hygiene_bad[:8]}")

    print("== trace consistency ==")
    trace_path = run / "trace.jsonl"
    calls = [json.loads(l) for l in trace_path.read_text().splitlines() if l.strip()] if trace_path.exists() else []
    n_inputs = len(list((run / "inputs").glob("*_user.md")))
    n_outputs = len(list((run / "outputs").glob("*_output.md")))
    n_real = sum(1 for c in calls if c.get("status") == "ok")
    check("trace.jsonl lines == inputs == outputs", len(calls) == n_inputs and n_outputs == n_real,
          f"trace={len(calls)} inputs={n_inputs} outputs={n_outputs} (ok calls={n_real})")
    manifest = json.loads((run / "manifest.json").read_text())
    check("manifest n_calls_total matches trace", manifest.get("n_calls_total") == len(calls),
          f"manifest={manifest.get('n_calls_total')} trace={len(calls)}")
    failed = [c["seq"] for c in calls if c.get("status") not in ("ok", "dry-run")]
    check("no failed calls", not failed, f"{failed}")

    print()
    if FINDINGS:
        print(f"RESULT: FAIL — {len(FINDINGS)} finding(s)")
        for f in FINDINGS:
            print(f"  - {f}")
        return 1
    print("RESULT: PASS — all L1 checks green")
    return 0


if __name__ == "__main__":
    sys.exit(main())
