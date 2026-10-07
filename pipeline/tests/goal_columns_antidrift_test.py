#!/usr/bin/env python3
"""goal_columns_antidrift_test.py — the goal table's column contract may not drift.

The p4 pack tells the model what shape to emit three times over: the ficha's
`# Output schema`, template §3 as `templates/doc02_adjusted_goals.md §3 (goal
table contract)`, and the worked example sliced out of
`example/doc02_adjusted_goals.md`. The L0 gate in `parse_p4` accepts only one of
those shapes, and `assemble_doc` writes a third, two code-derived columns wider.

Commit c2745f6 migrated the template and the exemplar to the v7 nine-column
format and left the ficha, the gate and the assembler alone. The prompt was left
showing a worked example whose shape its own gate rejected, on the two columns
where the shapes disagreed most: a model imitating the example died in
`parse_p4` on `cells[3]` with a message about an invalid pattern, which never
mentions columns.

Measured on the committed golden, the same example was worse than mis-shaped —
the D-01.2 block, which is what the D-01.1 call is shown, carried a goal at 0.96
similarity to its own Sub-SO against the 0.88 ceiling of
`check_obligation_retention`. The example demonstrated the restatement style
the gate exists to reject. Hence the last check here.

These assertions read only committed files and need no model: run them after any
prompt, template, exemplar or assembler edit.

Usage: python3 pipeline/tests/goal_columns_antidrift_test.py
Exit 0 iff every surface still agrees.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "pipeline" / "src"))

from quality import check_obligation_retention  # noqa: E402
from steps import GOAL_COLUMNS_DOC, GOAL_COLUMNS_EMIT  # noqa: E402

TEMPLATE = REPO / "templates" / "doc02_adjusted_goals.md"
GOLDEN = REPO / "example" / "doc02_adjusted_goals.md"
FICHA = REPO / "docs" / "pipeline" / "prompts" / "PROM-P1-04_DERIVE_ADJUSTED_GOALS.md"

#: the only exemplar blocks that ever reach a prompt. `compose.build_pack` takes
#: `others[0]` — the first block that is not the one being written — so every p4
#: call is shown one of these two and nothing else.
PROMPT_EXEMPLAR_BLOCKS = ("D-01.1", "D-01.2")

#: the DELIVERED shape is the EMIT shape renamed at four labels, with the
#: regulation token split out of `Baseline source` and the code-derived anchors
#: spliced in ahead of `Adjustment`. Stating the rename is what makes the
#: assertion below check the derivation rather than just the widths.
DOC_RENAME = {"ID": "AG ID", "Adjusted goal": "Adjusted Goal",
              "Parent goal": "Parent Goal", "Regulatory source": "Articles"}

FAILURES: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        FAILURES.append(name)


def header_row(text: str) -> list[str] | None:
    for line in text.splitlines():
        m = re.match(r"^\|\s*AG ID\s*\|(.*)\|\s*$", line)
        if m:
            return [c.strip() for c in m.group(1).split("|")]
    return None


def table_rows(text: str) -> list[list[str]]:
    return [[c.strip() for c in line.strip("|").split("|")]
            for line in text.splitlines()
            if re.match(r"^\|\s*`AG-D-\d\d\.\d-\d{3}`\s*\|", line)]


def section(text: str, start: str, stop: str) -> str:
    return text.split(start, 1)[1].split(stop, 1)[0]


def main() -> int:
    print("-- the two shapes --")
    check("EMIT is 9 columns, with Company implication",
          len(GOAL_COLUMNS_EMIT) == 9 and "Company implication" in GOAL_COLUMNS_EMIT,
          f"{len(GOAL_COLUMNS_EMIT)}: {' | '.join(GOAL_COLUMNS_EMIT)}")
    check("EMIT carries no column the model may not fill",
          not {"Control Anchors", "Regulation"} & set(GOAL_COLUMNS_EMIT))
    # derive DELIVERED from EMIT the way assemble_doc renders it
    derived: list[str] = []
    for col in GOAL_COLUMNS_EMIT:
        if col == "Baseline source":
            derived.append("Regulation")          # derived by code from the Sub-SO id
            continue                               # ...and replaces the column
        if col == "Adjustment":
            derived.append("Control Anchors")      # derived by code from the mapping store
        derived.append(DOC_RENAME.get(col, col))
    check("DELIVERED is EMIT renamed, plus the two code-derived columns",
          derived == list(GOAL_COLUMNS_DOC),
          f"{len(GOAL_COLUMNS_DOC)}: {' | '.join(GOAL_COLUMNS_DOC)}")

    print("-- what the model is shown --")
    tpl = header_row(section(TEMPLATE.read_text(encoding="utf-8"), "## §3", "## §4"))
    check("template §3 skeleton is the EMIT shape",
          [c.lower() for c in tpl or []] == [c.lower() for c in GOAL_COLUMNS_EMIT[1:]],
          " | ".join(["AG ID"] + tpl) if tpl else "no header row")

    schema = section(FICHA.read_text(encoding="utf-8"), "## Output schema", "## Prompt body")
    declared = re.search(r"(?m)^`([^`]+)`\s*$", schema)
    check("ficha Output schema is the EMIT shape",
          bool(declared) and [c.strip() for c in declared.group(1).split("|")]
          == list(GOAL_COLUMNS_EMIT),
          declared.group(1) if declared else "no backticked column list")

    print("-- the worked example every p4 call is shown --")
    body = section(GOLDEN.read_text(encoding="utf-8"), "## §3 Adjusted Goals", "## §4 ")
    blocks = {b.split()[1]: b for b in re.split(r"(?m)^(?=### D-)", body)
              if b.startswith("### D-")}
    for sd in PROMPT_EXEMPLAR_BLOCKS:
        rows = table_rows(blocks.get(sd, ""))
        check(f"{sd} exemplar rows are the EMIT shape",
              bool(rows) and all(len(r) == len(GOAL_COLUMNS_EMIT) for r in rows),
              f"{len(rows)} rows" + ("" if all(len(r) == len(GOAL_COLUMNS_EMIT)
                                              for r in rows)
                                    else f", widths {sorted({len(r) for r in rows})}"))
        check(f"{sd} exemplar parent goals use the SO- form parse_p4 requires",
              all(r[5].strip("`") == f"SO-{sd}.HL" for r in rows))
        baselines = {m.group(2): m.group(3) for m in re.finditer(
            r"`SG-(D-\d\d\.\d)\.(\w+)` \((?:GDPR|CRA|NIS2|DORA|AI_Act)\):\*\* (.*)",
            blocks.get(sd, ""))}
        for r in rows:
            reg = r[6].strip("`").split(".")[-1]
            findings = check_obligation_retention(r[1], baselines.get(reg, ""))
            check(f"{sd} {r[0]} passes its own adaptation gate", not findings,
                  findings[0] if findings else "")

    print("-- the delivered references --")
    for path in sorted(REPO.glob("cases/Case_*/01_PHASE1_CONTEXT/Doc02_Adjusted_Goals.md")):
        text = path.read_text(encoding="utf-8")
        rows = table_rows(text)
        if not rows:
            continue
        widths = sorted({len(r) for r in rows})
        # capitalisation is cosmetic; the claim is the column set and order
        ok = [c.lower() for c in header_row(text) or []] \
            == [c.lower() for c in GOAL_COLUMNS_DOC[1:]] \
            and widths == [len(GOAL_COLUMNS_DOC)]
        check(f"{path.parent.parent.name} reference is the DELIVERED shape", ok,
              f"{len(rows)} rows, widths {widths}")
        # R10 anti-circular physical table rendering check: every table must match header vs separator
        lines = text.splitlines()
        bad_seps = []
        for i, l in enumerate(lines):
            if l.startswith("|") and "---" in l and i > 0 and lines[i-1].startswith("|"):
                hp = len([x for x in lines[i-1].split("|")[1:-1]])
                sp = len([x for x in l.split("|")[1:-1]])
                if hp != sp:
                    bad_seps.append(f"line {i+1}: header {hp} != sep {sp}")
        check(f"{path.parent.parent.name} all tables render (header==separator width)",
              not bad_seps, ", ".join(bad_seps))

    print()
    if FAILURES:
        print(f"RESULT: FAIL — {len(FAILURES)}: {FAILURES}")
        return 1
    print("RESULT: PASS — every surface agrees on the column contract")
    return 0


if __name__ == "__main__":
    sys.exit(main())