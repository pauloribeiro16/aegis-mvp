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
# A chain segment is a *run* of law tokens terminated by one arrow and one
# driver set.  The run must be captured whole: because '·' separates laws, a
# pattern that anchors on a single law would only ever see the last law of the
# run and pair it with the first driver — which is how a correct multi-law chain
# gets "corrected" into a wrong one.  A run whose length differs from its driver
# set is not positionally resolvable and is left alone for a human.
RE_SEGMENT = re.compile(
    r"(?P<laws>(?:GDPR|CRA|NIS\s*2|AI[\s_]?Act|DORA)[^|·<]{0,70}?)+"
    r"(?:[→>]{1,2}|-->)"
    r"\s*(?P<objs>(?:`(?:PO|SO)-D-\d\d\.\d-\d{3}`[\s,/]*)+)"
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
        # Store the FULL id: the PO-/SO- prefix is not a function of the
        # regulation (Case_01 writes GDPR rows under both), so it must be read
        # from the row itself rather than inferred.
        by_sub[sd][r] = oid
        by_id[oid] = r
    return dict(by_sub), by_id


def is_versioned(p: Path) -> bool:
    return any(part.startswith(("v0_", "v1_", "v2_", "v3_")) for part in p.parts)


# One chain segment inside a single constraint: everything before the first
# arrow is the law run, everything after it (within the same backtick group) is
# the driver set.  Both are read from the piece, not from a token pattern, so a
# '·'-separated run of several laws is captured whole.
RE_ARROW = re.compile(r"(?:[→>]{1,2}|-->)")
RE_OBJ_SPAN = re.compile(r"(?:`(?:PO|SO)-D-\d\d\.\d-\d{3}`[\s,/]*)+")


def reanchor_piece(piece: str, rank: dict, filename: str) -> tuple[str, int]:
    """Re-anchor one constraint's chain. Returns the (possibly) rewritten piece.

    Conservative by construction: it acts only when the law run and the driver set
    are the same length *and* the same sub-domain, i.e. when the pairing is
    unambiguous. Anything else is reported and left untouched.
    """
    m = RE_ARROW.search(piece)
    if not m:
        return piece, 0
    laws = list(RE_LAW_IN_RUN.finditer(piece[: m.start()]))
    tail = piece[m.end():]
    span = RE_OBJ_SPAN.match(tail.lstrip())
    if not laws or not span:
        return piece, 0
    objs_text = span.group(0)
    pairs = list(RE_ID.finditer(objs_text))
    if not pairs:
        return piece, 0
    subs = [d for d in re.findall(r"-D-(\d\d\.\d)-", objs_text)]
    single_sub = len(set(subs)) == 1
    if len(laws) != len(pairs) or not single_sub:
        print(
            f"  ! {filename}: {len(laws)} law(s) vs {len(pairs)} driver(s)"
            f"{'' if single_sub else ' across sub-domains'} — manual decision"
        )
        return piece, 0
    # Rebuild positionally.  A global str.replace would also rewrite every other
    # position holding the same id — which silently drops a driver when the same
    # objective appears twice in one set.
    n = 0
    out, cursor = [], 0
    for law_m, pair in zip(laws, pairs):
        oid = pair.group(1)
        sd = oid.split("-D-")[1].rsplit("-", 1)[0]
        law = canon(law_m.group(0))
        want = rank.get((sd, law))
        out.append(objs_text[cursor:pair.start()])
        cursor = pair.end()
        if want is None:
            print(f"  ! {filename}: no {law} objective in D-{sd} (cited {oid}) — manual decision")
            out.append(pair.group(0))
            continue
        if want == oid:
            out.append(pair.group(0))
            continue
        n += 1
        print(f"  {filename}: {oid} ({law} in D-{sd}) → {want}")
        out.append(pair.group(0).replace(oid, want))
    out.append(objs_text[cursor:])
    new_text = "".join(out)
    return (piece.replace(objs_text, new_text) if new_text != objs_text else piece), n


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
    for sd, regs in by_sub.items():
        for r in regs:
            rank[(sd, r)] = regs[r]

    targets = [
        p for p in sorted(p3dir.rglob("Doc0*.md"))
        if not is_versioned(p) and "filtered_corpus" not in p.as_posix()
    ]
    print(f"case: {args.case}")
    print(f"ground truth: {len(by_sub)} sub-domains, {len(by_id)} objectives")
    print(f"targets (active only): {[p.name for p in targets]}\n")

    total_fix = 0
    for path in targets:
        lines = io.open(path, encoding="utf-8", newline="").read().splitlines()
        changed = 0
        out: list[str] = []
        for line in lines:
            # A table cell packs several constraints separated by <br>.  Parse each
            # constraint on its own: a segment's laws and drivers belong together,
            # and a cross-constraint match would pair a law from one chain with a
            # driver from the next.
            pieces = line.split("<br>")
            first, n0 = reanchor_piece(pieces[0], rank, path.name)
            rebuilt = [first]
            changed += n0
            for piece in pieces[1:]:
                new_piece, n1 = reanchor_piece(piece, rank, path.name)
                rebuilt.append(new_piece)
                changed += n1
            out.append("<br>".join(rebuilt))
        if changed:
            total_fix += changed
            if args.apply:
                io.open(path, "w", encoding="utf-8", newline="").write("\n".join(out) + "\n")
        print(f"  {path.name}: {changed} citation(s) {'rewritten' if args.apply else 'to rewrite'}")

    print(f"\n{total_fix} citation(s) {'rewritten' if args.apply else 'would be rewritten'}")
    if not args.apply:
        print("dry run — pass --apply to write")
    return 0


if __name__ == "__main__":
    sys.exit(main())
