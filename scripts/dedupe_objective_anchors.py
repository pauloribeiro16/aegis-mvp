#!/usr/bin/env python3
"""
dedupe_objective_anchors.py
============================
Removes literal duplicate CSF 2.0 IDs from objective anchor lists in
`baseline/domains/D-XX/D-XX.Y/regs/*.md` (Sub-SO **CSF anchors** line + Volere
requirement `nist_csf:` YAML field). Preserves first-occurrence order.

Audit M7 found 78 objectives with this defect (the same anchor id listed more
than once within the same objective's `anchors_listed`). Most occurrences are
in Sub-SO **CSF anchors** lines that look like:

    PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-01.

(CSF anchors are stored as a comma-separated string in `regs/`; the duplication
is mechanical, not semantic, and the trailing period + new line may be
separated by italic `*(*..*` rationale notes.)

Idempotent: re-runs report 0 changes.

Output ledger:
  baseline/domains/_objective_anchor_dedup.md
"""

import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path("baseline/domains")
RE_CSF = re.compile(r"\b(?:GV|ID|PR|DE|RS|RC)\.[A-Z]{2}-\d{2}\b")


def dedupe_tokens(tokens):
    """Remove consecutive duplicates (a, a, b, c, c) keeping first
    occurrences. The corpus's duplication pattern is 'PR.DS-01, PR.DS-02,
    PR.DS-10, PR.DS-01.' — note the period after the last token — so
    trailing punctuation is preserved on the final element."""
    seen, out = set(), []
    for t in tokens:
        if t not in seen:
            seen.add(t)
            out.append(t)
    return out


def dedupe_subso_anchors_line(text: str):
    """Replace the **CSF anchors (...)** block body with the deduped list."""
    pat = re.compile(
        r"(^\*\*CSF anchors\b[^\n]*\*\*:\s*)([^\n]*)",
        re.M,
    )

    def sub(m):
        head, payload = m.group(1), m.group(2)
        # Strip optional trailing period; tokens are comma- and whitespace-
        # separated; the line may be followed on the next line by an italic
        # rationale (`*(...*)`).
        trailing = ""
        if payload.endswith("."):
            trailing = "."
            payload = payload[:-1]
        tokens = RE_CSF.findall(payload)
        # remove consecutive duplicates only (the corpus pattern is exactly
        # this; semantic-equality deduplication would need the official
        # crosswalk).
        deduped = dedupe_tokens(tokens)
        return head + ", ".join(deduped) + trailing

    return pat.sub(sub, text)


def dedupe_nist_csf_yaml(text: str):
    """Rewrite every `nist_csf: [PR.DS-01, PR.DS-02, PR.DS-01]` (or
    multi-line list) to deduped tokens."""
    # Inline: nist_csf: [A, B, A]
    pat_inline = re.compile(
        r"(nist_csf:\s*)\[([^\]]*)\]",
    )

    def sub_inline(m):
        head, payload = m.group(1), m.group(2)
        tokens = RE_CSF.findall(payload)
        deduped = dedupe_tokens(tokens)
        return head + "[" + ", ".join(deduped) + "]"

    text = pat_inline.sub(sub_inline, text)
    return text


def process():
    changes = []  # (rel, line, old, new)
    n_files = 0
    for regf in sorted(ROOT.glob("D-*/D-*.[0-9]*/regs/*.md")):
        if ".ambiguity" in regf.name:
            continue
        text = regf.read_text(encoding="utf-8-sig")
        old_text = text
        text = dedupe_subso_anchors_line(text)
        text = dedupe_nist_csf_yaml(text)
        if text == old_text:
            continue
        n_files += 1
        # build change log
        old_lines = old_text.splitlines()
        new_lines = text.splitlines()
        for i, (a, b) in enumerate(zip(old_lines, new_lines), 1):
            if a != b:
                # only log lines containing CSF tokens
                if RE_CSF.search(a) or RE_CSF.search(b):
                    changes.append((regf.as_posix(), i, a.strip(), b.strip()))
        regf.write_text(text, encoding="utf-8", newline="\n")

    # Ledger
    out = ROOT / "_objective_anchor_dedup.md"
    lines = ["# CSF anchor list deduplication ledger (literal duplicates)", ""]
    lines.append(f"- Date: 2026-09-22")
    lines.append(f"- Scope: `baseline/domains/D-*/D-*.[0-9]*/regs/*.md` "
                 f"(Sub-SO **CSF anchors** lines + Volere `nist_csf:` YAML).")
    lines.append(f"- Algorithm: dedupe adjacent identical CSF IDs in the same "
                 f"objective's anchor list, preserving first-occurrence order. "
                 f"Non-adjacent semantic-equivalence dedup is NOT performed (would "
                 f"require the official CSF crosswalk).")
    lines.append(f"- Idempotent.")
    lines.append("")
    lines.append(f"- Files touched: **{n_files}**")
    lines.append(f"- Lines changed: **{len(changes)}**")
    lines.append("")
    lines.append("## Per-change log")
    lines.append("")
    lines.append("| File | Line | Before | After |")
    lines.append("|---|---|---|---|")
    for rel, ln, before, after in changes:
        lines.append(f"| {rel} | {ln} | `{before[:100]}` | `{after[:100]}` |")
    lines.append("")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")

    print(f"deduplicated {len(changes)} lines in {n_files} files")
    print(f"ledger: {out}")
    return len(changes)


if __name__ == "__main__":
    n = process()
    if "--strict" in sys.argv:
        # re-run; should be 0
        n2 = process()
        if n2:
            print(f"WARN: idempotency violated, {n2} remaining changes", file=sys.stderr)
            sys.exit(1)
