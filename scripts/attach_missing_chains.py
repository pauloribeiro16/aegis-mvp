#!/usr/bin/env python3
"""Attach missing chain citations to the carrier the coverage matrix declares.

T5 of ``check_traceability.py`` reports drivers the matrix binds to a card whose
``Security & Privacy Constraints`` row does not cite them.  These arise when a
round asserts a chain in bulk and records it in the matrix without writing it
into the card, so the derivation was real but not written down.

This script makes it written down: for each such driver it resolves the
regulation and the governing article from the case's Phase 2 spine and appends a
chain segment to the declared carrier — a requirement card
(``Security & Privacy Constraints:`` cell) or a quality-attributes NFR row
(``| **RN<n>** |``).  Nothing is invented: the law comes from the objective's
own Regulation column and the article from its Operational Statement.

A card citation makes the derivation *auditable*; it does not assert that the
card's fit criteria discharge the objective.  That remains the ADR-007 D2
coverage-granularity debt, recorded in each matrix.

Usage::

    python scripts/attach_missing_chains.py --case Case_03_OmniBank
    python scripts/attach_missing_chains.py --case Case_03_OmniBank --apply
"""

from __future__ import annotations

import argparse
import io
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_traceability as ct  # noqa: E402

REPO = ct.REPO

LAW_TOKEN = {
    "GDPR": "GDPR", "CRA": "CRA", "NIS2": "NIS 2", "DORA": "DORA", "AI_Act": "AI Act",
}
# Article as written in the Phase 2 statement, e.g. "Art. 33(1))" -> "Art. 33(1)".
RE_ARTICLE = re.compile(r"Art\.\s*\d+[A-Za-z0-9()\-–]*(?:\s*\([^)]{0,12}\))*")
RE_CARD_HDR = re.compile(r"^\|\s*\*\*ID:\*\*\s*R(\d{1,2})\.(\d{1,2})\b")
RE_RN_ROW = re.compile(r"^\|\s*\*\*(RN\d{1,3})\*\*\s*\|")
RE_MATRIX_CARD = re.compile(r"R(\d{1,2})\.(\d{1,2})")
RE_MATRIX_RN = re.compile(r"RN(\d{1,3})")


def clean_article(text: str) -> str:
    a = RE_ARTICLE.search(text)
    if not a:
        return ""
    art = a.group(0).strip()
    art = re.sub(r"\s+", " ", art)
    # Trim a trailing ")" that belongs to an enclosing clause, keeping "(1)" style.
    while art.endswith("))") and art.count("(") < art.count(")"):
        art = art[:-1]
    return art.rstrip(" .")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--case", required=True)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    case = [c for c in ct.discover_cases(None) if args.case in c.name]
    if not case:
        print(f"case not found: {args.case}")
        return 2
    case = case[0]

    # Phase 2 spine: id -> (regulation, statement)
    spine: dict[str, tuple[str, str]] = {}
    for line in ct.read(case.p2):
        m = ct.RE_MATRIX_ROW.match(line)
        if not m:
            continue
        f = [c.strip() for c in line.split("|")[1:-1]]
        if len(f) >= 4:
            spine[m.group(1)] = (f[3].strip("*").strip(), f[1])

    delivered = set(ct.RE_OBJECTIVE.findall(case.active_text))
    targets: list[tuple[str, str, str]] = []  # (objective, carrier-token, law+article)
    for line in ct.read(case.mapping):
        m = ct.RE_MATRIX_ROW.match(line)
        if not m:
            continue
        oid = m.group(1)
        cells = [c.strip() for c in line.split("|")[1:-1]]
        state = " ".join(cells[1:]).lower()
        non_cover = any(k in state for k in ("**n/a**", "no functional carrier", "design guidance"))
        transversal = "transversal" in cells[2].lower() if len(cells) > 2 else False
        if non_cover or transversal or oid in delivered:
            continue
        if not ct.CARRIER_TOKENS.search(state):
            continue
        reg, stmt = spine.get(oid, ("", ""))
        law = LAW_TOKEN.get(reg, reg)
        art = clean_article(stmt)
        basis = f"{law} {art}".strip()
        for card in RE_MATRIX_CARD.findall(cells[2]):
            targets.append((oid, f"R{card[0]}.{card[1]}", basis))
        for rn in RE_MATRIX_RN.findall(cells[2]):
            targets.append((oid, f"RN{rn}", basis))

    if not targets:
        print("nothing to attach")
        return 0

    # Locate each carrier in the active Doc01.  An RN may sit in the
    # quality-attributes table (`| **RN5** |`) or be absorbed into a card
    # (`**NFR-RN14**` inside its constraints cell); both resolve to a line.
    doc = case.p3
    lines = ct.read(doc)
    card_line: dict[str, int] = {}
    rn_line: dict[str, int] = {}
    for i, l in enumerate(lines):
        h = RE_CARD_HDR.match(l)
        if h:
            card_line[f"R{h.group(1)}.{h.group(2)}"] = i
        r = RE_RN_ROW.match(l)
        if r:
            rn_line[r.group(1)[2:]] = i  # keys are bare numbers, like `absorbed`
    # Absorbed constraints: the first card line mentioning NFR-RN<n>.
    absorbed: dict[str, int] = {}
    for i, l in enumerate(lines):
        for rn in re.findall(r"NFR-RN(\d{1,3})", l):
            absorbed.setdefault(rn, i)

    # Accumulate per target line: (objective -> segment text).
    per_line: dict[int, list[str]] = {}
    skipped: list[tuple[str, str]] = []
    for oid, carrier, basis in targets:
        if carrier.startswith("RN"):  # must precede the R<n>.<m> test — "RN14" starts with "R"
            rn = carrier[2:]
            idx = rn_line.get(rn, absorbed.get(rn))
        else:
            idx = card_line.get(carrier)
        if idx is None:
            skipped.append((oid, carrier))
            continue
        if oid in lines[idx]:
            continue
        seg = f"{basis} → `{oid}`" if basis else f"`{oid}`"
        per_line.setdefault(idx, []).append(seg)
        print(f"  {carrier:7s} += {seg}")

    if not per_line:
        print("\nnothing to attach")
        if skipped:
            print(f"skipped (carrier not located): {skipped}")
        return 0

    n_att = sum(len(v) for v in per_line.values())
    for idx, segs in sorted(per_line.items()):
        line = lines[idx]
        if "Security & Privacy Constraints:" in line:
            new = line.replace("| **Priority:**", f"<br>**Chain** {' · '.join(segs)} | **Priority:**", 1)
            if new == line:
                new = line.rstrip()[:-1].rstrip() + f"<br>**Chain** {' · '.join(segs)} |"
        elif line.rstrip().endswith("|"):
            new = line.rstrip()[:-1].rstrip() + f" · {' · '.join(segs)} |"
        else:
            skipped.append((f"line {idx+1}", "no constraint cell"))
            continue
        lines[idx] = new

    print(f"\n{n_att} attachment(s) on {len(per_line)} line(s)")
    if skipped:
        print(f"skipped: {skipped}")
    if args.apply:
        io.open(doc, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
        print("written")
    else:
        print("dry run — pass --apply to write")
    return 0


if __name__ == "__main__":
    sys.exit(main())
