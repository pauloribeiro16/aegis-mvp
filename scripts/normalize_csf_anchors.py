#!/usr/bin/env python3
"""
normalize_csf_anchors.py
========================
Repairs R2b violations found by the anchor audit: 8 control IDs cited on
objective anchors that do NOT exist in the NIST CSF 2.0 referential
(`baseline/CONTROLS/NIST_CSF_2.0/`).

Provenance of the mapping (documented, not invented):
  - 7 IDs are CSF v1.1-era leftovers. The official v1.1 -> v2.0 lineage is
    taken from the referential itself: each CSF_2.0 control JSON carries its
    `informative_references` entry "CSF v1.1: <id>", giving the authoritative
    predecessor mapping:
      RS.CO-04 -> RS.MA-04   (official targets {RS.MA-01, RS.MA-04}; the
                              corpus contexts are notification escalation /
                              routing -> escalation)
      PR.IP-07 -> ID.IM-03   (official)
      PR.AT-03 -> PR.AT-02   (official targets {PR.AT-01, PR.AT-02}; contexts
                              are specialized-role/board training)
      PR.AT-04 -> PR.AT-02   (official)
      ID.SC-04 -> GV.SC-07   (official targets {GV.SC-07, ID.RA-10}; supplier
                              risk contexts; ID.RA-10 is a draft-2.0
                              numbering artifact and is deliberately avoided)
      PR.IP-06 -> ID.AM-08   (official)
      PR.PT-01 -> PR.PS-04   (official)
  - PR.DS-12 is not a CSF ID at all: it is the corpus's internal 4x3 matrix
    cell ("data managed consistent with risk strategy" / DORA
    classification-driven overlay). Policy, per the corpus's own glosses:
      PR.DS-12 -> ID.AM-05  (classification-driven overlay gloss)
                  inside D-01_*/regs/DORA.md
      PR.DS-12 -> ID.AM-08  (data-management / lifecycle / records gloss)
                  everywhere else

Scope: objective-bearing and cross layers of the modular corpus
  - D-*/D-XX.Y/regs/*.md          (Sub-SO anchor lines + requirement nist_csf)
  - D-*/D-XX.Y/cross/_interactions.md (SR cross-validation narratives)
  - D-*/D-XX.manifest.json        (nist control lists)
NOT normalized (intentional): articles/*.md — verbatim inherited regulatory
basis corpus; anchor mentions there are superseded source material, never the
objective anchor surface (SPEC §5 P4 reads anchors from regs/).

Every change is recorded in baseline/domains/_csf_anchor_normalization.md.
scripts/verify_no_loss.py applies the same token map to the original corpus
before comparison, so the no-loss guarantee remains verifiable after this
documented correction.
"""

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

# phantom -> (replacement, rationale tag)
PHANTOM_MAP = {
    "RS.CO-04": ("RS.MA-04", "official 1.1->2.0 crosswalk (escalation context)"),
    "PR.IP-07": ("ID.IM-03", "official 1.1->2.0 crosswalk"),
    "PR.AT-03": ("PR.AT-02", "official 1.1->2.0 crosswalk (specialized roles)"),
    "PR.AT-04": ("PR.AT-02", "official 1.1->2.0 crosswalk"),
    "ID.SC-04": ("GV.SC-07", "official 1.1->2.0 crosswalk (supplier risk)"),
    "PR.IP-06": ("ID.AM-08", "official 1.1->2.0 crosswalk"),
    "PR.PT-01": ("PR.PS-04", "official 1.1->2.0 crosswalk"),
}
PHANTOM_TOKENS = sorted(PHANTOM_MAP, key=len, reverse=True)
RE_PHANTOM = re.compile(r"\b(" + "|".join(p.replace(".", r"\.") for p in PHANTOM_TOKENS) + r")\b")
RE_PRDS12 = re.compile(r"\bPR\.DS-12\b")
RE_CSF_ANY = re.compile(r"\b(?:GV|ID|PR|DE|RS|RC)\.[A-Z]{2}-\d{2}\b")
RE_CSF_LIST = re.compile(r"(nist_csf:\s*\[)([^\]]*)(\])")
RE_ANCHOR_LIST_LINE = re.compile(r"^((?:[A-Z]{2}\.[A-Z]{2}-\d{2})(?:,\s*[A-Z]{2}\.[A-Z]{2}-\d{2})*\.?)\s*$")


def prds12_replacement(path: Path) -> str:
    if (path.name == "DORA.md" and path.parent.name == "regs"
            and any(part.startswith("D-01_") for part in path.parts)):
        return "ID.AM-05"
    return "ID.AM-08"


def normalize_csf_tokens(text: str, path: Path = None) -> str:
    """Shared token-level normalization (also used by verify_no_loss.py).
    Applies the phantom map plus the context-aware PR.DS-12 policy."""
    text = RE_PHANTOM.sub(lambda m: PHANTOM_MAP[m.group(1)][0], text)
    if path is not None:
        text = RE_PRDS12.sub(prds12_replacement(path), text)
    else:
        text = RE_PRDS12.sub("ID.AM-08", text)  # source-corpus normalization default
    return text


def dedupe_lists(text: str) -> str:
    """Deduplicate CSF tokens inside nist_csf YAML arrays and on pure anchor
    list lines (e.g. 'PR.DS-01, PR.DS-02, PR.DS-10.'), preserving order."""

    def _dedupe_csv(items: str) -> str:
        seen, out = set(), []
        for it in [x.strip() for x in items.split(",")]:
            key = it.rstrip(".")
            if key and key not in seen:
                seen.add(key)
                out.append(it)
        return ", ".join(out)

    def _sub_list(m):
        return m.group(1) + ", ".join(_dedupe_csv(m.group(2)).replace(", ", ", ").split(", ")) + m.group(3)

    def _sub_yaml(m):
        inner = ", ".join(_dedupe_csv(m.group(2)).split(", "))
        return m.group(1) + inner + m.group(3)

    text = RE_CSF_LIST.sub(_sub_yaml, text)
    lines = []
    for ln in text.splitlines():
        m = RE_ANCHOR_LIST_LINE.match(ln.strip())
        if m:
            indent = ln[: len(ln) - len(ln.lstrip())]
            ln = indent + _dedupe_csv(m.group(1))
        lines.append(ln)
    return "\n".join(lines)


def simulate_line_changes(old_line: str, path: Path):
    """Deterministically list the replacements normalize_csf_tokens performs
    on a line (in occurrence order). Mirrors normalize_csf_tokens exactly."""
    out = []
    for m in RE_PHANTOM.finditer(old_line):
        out.append((m.start(), m.group(1), PHANTOM_MAP[m.group(1)][0]))
    for m in RE_PRDS12.finditer(old_line):
        out.append((m.start(), "PR.DS-12", prds12_replacement(path)))
    out.sort(key=lambda t: t[0])
    return [(o, n) for _s, o, n in out]


def build_ledger(changes, file_changes, touched, out: Path):
    ledger = ["# CSF anchor normalization ledger (R2b repair)", ""]
    ledger.append("- Date: 2026-09-22")
    ledger.append("- Scope: `regs/*.md`, `cross/_interactions.md`, `D-*.manifest.json` "
                  "(objective/cross/index layers).")
    ledger.append("- **Not** normalized: `articles/*.md` (verbatim inherited regulatory basis; "
                  "never the objective anchor surface — SPEC §5 P4).")
    ledger.append("- Provenance: official v1.1->2.0 lineage read from the referential's own")
    ledger.append("  `informative_references` (`CSF v1.1:` entries); `PR.DS-12` is the corpus's")
    ledger.append("  internal 4x3-matrix cell, not a CSF ID (policy documented in")
    ledger.append("  `scripts/normalize_csf_anchors.py`).")
    ledger.append("- Verification: `scripts/verify_no_loss.py` applies this same map to the")
    ledger.append("  original corpus before comparison (documented normalization).")
    ledger.append("")
    ledger.append("| Phantom | Replacement | Count | Rationale |")
    ledger.append("|---|---|---|---|")
    for (old, new), n in sorted(changes.items(), key=lambda kv: -kv[1]):
        rat = PHANTOM_MAP.get(old, ("", "internal 4x3 matrix cell "
                                         + ("(classification overlay)" if new == "ID.AM-05"
                                            else "(data management)")))[1]
        ledger.append(f"| {old} | {new} | {n} | {rat} |")
    ledger.append("")
    ledger.append(f"Total occurrences normalized: {sum(changes.values())} "
                  f"in {touched} files.")
    ledger.append("")
    ledger.append("## Per-change log")
    ledger.append("")
    ledger.append("| File | Line | Old | New |")
    ledger.append("|---|---|---|---|")
    for rel, ln, old, new in file_changes:
        ledger.append(f"| {rel} | {ln} | {old} | {new} |")
    ledger.append("")
    out.write_text("\n".join(ledger) + "\n", encoding="utf-8", newline="\n")


def process():
    root = Path("baseline/domains")
    targets = []
    targets += sorted(root.glob("D-*/D-*.[0-9]*/regs/*.md"))
    targets += sorted(root.glob("D-*/D-*.[0-9]*/cross/*.md"))
    targets += sorted(root.glob("D-*/D-*.[0-9]*/objective.md"))
    targets += sorted(root.glob("D-*/D-*.manifest.json"))
    targets = [p for p in targets if p.is_file()]

    changes = defaultdict(int)      # (old, new) -> count
    file_changes = []               # (relpath, line, old, new)
    touched = 0
    for p in targets:
        text = p.read_text(encoding="utf-8-sig")
        new_text = normalize_csf_tokens(text, p)
        new_text = dedupe_lists(new_text)
        if new_text == text:
            continue
        touched += 1
        old_lines = text.splitlines()
        new_lines = new_text.splitlines()
        for i, (a, b) in enumerate(zip(old_lines, new_lines), 1):
            if a == b:
                continue
            for old, new in simulate_line_changes(a, p):
                changes[(old, new)] += 1
                file_changes.append((p.as_posix(), i, old, new))
        p.write_text(new_text, encoding="utf-8", newline="\n")

    build_ledger(changes, file_changes, touched, root / "_csf_anchor_normalization.md")
    print(f"normalized {sum(changes.values())} occurrences in {touched} files")
    for (old, new), n in sorted(changes.items(), key=lambda kv: -kv[1]):
        print(f"  {old} -> {new}: {n}")
    print(f"ledger: {root / '_csf_anchor_normalization.md'}")


def ledger_from_git():
    """Reconstruct the ledger after the fact (files already normalized):
    diffs working tree against HEAD and simulates the deterministic mapping
    on every changed line."""
    import subprocess
    root = Path("baseline/domains")
    targets = []
    targets += sorted(root.glob("D-*/D-*.[0-9]*/regs/*.md"))
    targets += sorted(root.glob("D-*/D-*.[0-9]*/cross/*.md"))
    targets += sorted(root.glob("D-*/D-*.[0-9]*/objective.md"))
    targets += sorted(root.glob("D-*/D-*.manifest.json"))
    targets = [p for p in targets if p.is_file()]

    changes = defaultdict(int)
    file_changes = []
    touched = 0
    for p in targets:
        head = subprocess.run(["git", "show", f"HEAD:{p.as_posix()}"],
                              capture_output=True)
        if head.returncode != 0:
            continue  # file not in HEAD (new file)
        old_text = head.stdout.decode("utf-8-sig")
        new_text = p.read_text(encoding="utf-8-sig")
        if old_text == new_text:
            continue
        touched += 1
        old_lines = old_text.splitlines()
        for i, a in enumerate(old_lines, 1):
            for old, new in simulate_line_changes(a, p):
                changes[(old, new)] += 1
                file_changes.append((p.as_posix(), i, old, new))

    build_ledger(changes, file_changes, touched, root / "_csf_anchor_normalization.md")
    print(f"ledger reconstructed: {sum(changes.values())} occurrences in {touched} files")
    for (old, new), n in sorted(changes.items(), key=lambda kv: -kv[1]):
        print(f"  {old} -> {new}: {n}")


if __name__ == "__main__":
    if "--ledger-only" in sys.argv:
        ledger_from_git()
    else:
        process()
