#!/usr/bin/env python3
"""Re-anchor Phase 3 chain citations onto the case's compact Phase 2 numbering.

Root cause (Case_03_OmniBank, 2026-09-29): the Phase 3 chains were authored
against a fixed five-slot convention (001=GDPR, 002=CRA, 003=NIS2, 004=DORA,
005=AI_Act) while Phase 2 numbers *compactly* — regulations in the canonical
order GDPR→CRA→NIS2→DORA→AI_Act, numbered 001..n over those actually present in
that sub-domain.  Where a sub-domain lacks an earlier regulation, every later
suffix shifts down, so 28 of 134 objectives carry a suffix the chains never
anticipated.  The result: 23 objective IDs cited in the delivered Doc01 that
resolve to nothing, and 25 law→driver pairings citing a driver of the wrong
regulation.

The mapping is deterministic and verifiable: for a cited ``(sub-domain,
regulation)`` the correct suffix is simply the regulation's rank among those
present.  ``--apply`` rewrites the active deliverable in place; the default is a
dry run.  Version folders (``v1_``/``v2_``) are never touched — they are
historical snapshots.

Usage::

    python scripts/reanchor_chains.py --case Case_03_OmniBank
    python scripts/reanchor_chains.py --case Case_03_OmniBank --apply
"""

from __future__ import annotations

import argparse
import io
import re
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

REG_ORDER = ["GDPR", "CRA", "NIS2", "DORA", "AI_Act"]
LAW_ALT = "GDPR|CRA|NIS\\s*2|AI[\\s_]?Act|DORA"
CANON = {
    "GDPR": "GDPR", "CRA": "CRA", "NIS 2": "NIS2", "NIS2": "NIS2",
    "AI Act": "AI_Act", "AI_Act": "AI_Act", "DORA": "DORA",
}

RE_ID = re.compile(r"\b((?:PO|SO)-D-(\d\d\.\d)-(\d{3}))\b")
RE_CELL_ROW = re.compile(r"^\|\s*`((?:PO|SO)-D-\d\d\.\d-\d{3})`\s*\|")
RE_REG_CELL = re.compile(r"\*\*(GDPR|CRA|NIS\s*2|AI\s*Act|AI_Act|DORA)\*\*")
# One chain segment: a run of law tokens, an arrow, one backticked driver set.
RE_SEGMENT = re.compile(
    r"(?P<laws>(?:GDPR|CRA|NIS\s*2|AI[\s_]?Act|DORA)[^|·<]{0,70}?)+"
    r"(?:[→>]{1,2}|-->)"
    r"\s*`(?P<objs>[^`]+)`"
)
RE_LAW_IN_RUN = re.compile(LAW_ALT)


def canon(tok: str) -> str:
    return CANON[re.sub(r"\s+", " ", tok)]


def build_truth(p2: Path) -> tuple[dict[str, dict[str, str]], dict[str, str]]:
    """sub-domain -> regulation -> suffix, and id -> regulation."""
    by_sub: dict[str, dict[str, str]] = defaultdict(dict)
    by_id: dict[str, str] = {}
    text = io.open(p2, encoding="utf-8", errors="replace").read()
    for line in text.splitlines():
        m = RE_CELL_ROW.match(line)
        if not m:
            continue
        reg = RE_REG_CELL.search(line)
        if not reg:
            continue
        oid = m.group(1)
        sd, suffix = oid.split("-D-")[1].rsplit("-", 1)
        r = canon(reg.group(1))
        by_sub[sd][r] = suffix
        by_id[oid] = r
    return dict(by_sub), by_id


def is_versioned(p: Path) -> bool:
    return any(part.startswith(("v0_", "v1_", "v2_", "v3_")) for part in p.parts)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--case", required=True, help="case directory name, e.g. Case_03_OmniBank")
    ap.add_argument("--apply", action="store_true", help="write changes (default: dry run)")
    args = ap.parse_args()

    root = REPO / "cases" / args.case
    p2 = root / "02_PHASE2_RULES" / "Doc01_Operational_Objectives.md"
    p3dir = root / "03_PHASE3_SPEC"
    if not p2.is_file() or not p3dir.is_dir():
        print(f"case not found or missing Phase 2/3: {args.case}")
        return 2

    by_sub, by_id = build_truth(p2)
    # rank of each regulation within its sub-domain, per the canonical order
    rank: dict[tuple[str, str], str] = {}
    for sd, regs in by_sub.items():
        present = [r for r in REG_ORDER if r in regs]
        for i, r in enumerate(present, 1):
            rank[(sd, r)] = f"{i:03d}"
    # PO- objectives are GDPR-only; SO- carry CRA/NIS2/DORA/AI_Act.  A citation
    # must therefore be resolved to the *whole* id, prefix included, or a DORA
    # citation re-pointed at a GDPR row keeps a PO- prefix that does not exist.
    prefix_of: dict[str, str] = {}
    for oid, reg in by_id.items():
        prefix_of.setdefault(reg, oid.split("-")[0])
    for sd, regs in by_sub.items():
        for r in regs:
            rank[(sd, r)] = f"{prefix_of[r]}-D-{sd}-{rank[(sd, r)]}"

    targets = [
        p for p in sorted(p3dir.rglob("Doc0*.md"))
        if not is_versioned(p) and "filtered_corpus" not in p.as_posix()
    ]
    print(f"case: {args.case}")
    print(f"ground truth: {len(by_sub)} sub-domains, {len(by_id)} objectives")
    print(f"targets (active only): {[p.name for p in targets]}\n")

    total_fix = 0
    for path in targets:
        lines = io.open(path, encoding="utf-8", errors="replace").read().splitlines()
        changed = 0
        out: list[str] = []
        for line in lines:
            def repl(seg: re.Match) -> str:
                nonlocal changed
                law_tokens = [canon(m.group(0)) for m in RE_LAW_IN_RUN.finditer(seg.group("laws"))]
                # Collapse a combined "DORA/NIS 2" token into its two laws.
                laws: list[str] = []
                for tok in law_tokens:
                    laws.append(tok)
                spans = [(m.start(), m.end(), m.group(0)) for m in RE_LAW_IN_RUN.finditer(seg.group("laws"))]
                pairs = [m for m in RE_ID.finditer(seg.group("objs"))]
                if not pairs:
                    return seg.group(0)
                # Positional: law i drives the i-th objective in the set.  When
                # the counts differ the set cannot be trusted positionally —
                # report and leave it for a human.
                if len(spans) == len(pairs):
                    objs_text = seg.group("objs")
                    out_text = objs_text
                    for (s0, s1, raw), pair in zip(spans, pairs):
                        law = canon(raw)
                        oid = pair.group(1)
                        sd = oid.split("-D-")[1].rsplit("-", 1)[0]
                        want = rank.get((sd, law))
                        if want is None:
                            print(f"  ! {path.name}: no {law} objective in D-{sd} (cited {oid}) — manual decision")
                            continue
                        if want == oid:
                            continue
                        changed += 1
                        print(f"  {path.name}: {oid} ({law} in D-{sd}) → {want}")
                        out_text = out_text.replace(oid, want)
                    if out_text == objs_text:
                        return seg.group(0)
                    return seg.group(0).replace(objs_text, out_text)
                # Single law, possibly several ids (a law carrying a set).
                if len(spans) == 1:
                    law = canon(spans[0][2])
                    objs_text = seg.group("objs")
                    out_text = objs_text
                    for pair in pairs:
                        oid = pair.group(1)
                        sd = oid.split("-D-")[1].rsplit("-", 1)[0]
                        want = rank.get((sd, law))
                        if want is None:
                            print(f"  ! {path.name}: no {law} objective in D-{sd} (cited {oid}) — manual decision")
                            continue
                        if want == oid:
                            continue
                        changed += 1
                        print(f"  {path.name}: {oid} ({law} in D-{sd}) → {want}")
                        out_text = out_text.replace(oid, want)
                    if out_text == objs_text:
                        return seg.group(0)
                    return seg.group(0).replace(objs_text, out_text)
                print(f"  ! {path.name}: {len(spans)} laws vs {len(pairs)} drivers — manual decision needed")
                return seg.group(0)

            out.append(RE_SEGMENT.sub(repl, line))
        if changed:
            total_fix += changed
            if args.apply:
                io.open(path, "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
        print(f"  {path.name}: {changed} citation(s) {'rewritten' if args.apply else 'to rewrite'}")

    print(f"\n{total_fix} citation(s) {'rewritten' if args.apply else 'would be rewritten'}")
    if not args.apply:
        print("dry run — pass --apply to write")
    return 0


if __name__ == "__main__":
    sys.exit(main())
