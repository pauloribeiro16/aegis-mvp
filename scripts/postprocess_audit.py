#!/usr/bin/env python3
"""
postprocess_audit.py
====================
Prepends an executive summary block to the auditor's report
(`baseline/domains/_objective_anchor_audit.md`) based on its existing structure.
Reads the report, parses verdict + confidence + excessive + missing counts per
entry and aggregates them into a top-of-file Executive Summary that an
operator can scan in seconds.

Idempotent: skips if the report already has the marker block.
"""

import re
from pathlib import Path
from collections import Counter, defaultdict

REPORT = Path("baseline/domains/_objective_anchor_audit.md")
MARKER = "<!-- executive-summary-v1 -->\n"

VERDICT_RE = re.compile(r"\*\*Coverage verdict\*\*:\s*([^*]+)")
CONFIDENCE_RE = re.compile(r"\*\*Confidence\*\*:\s*([^*]+)")
SUB_RE = re.compile(r"^### (D-\d+\.\d+) ·")
ANCHORS_RE = re.compile(r"\*\*Anchors listed\*\*:\s*\n((?:  - [^\n]*\n)*)")
SECTION_HEAD_RE = re.compile(r"^## (D-\d+\.\d+) ")


def parse_report():
    verdicts = Counter()
    confidences = Counter()
    by_sub = defaultdict(lambda: Counter())  # sub -> verdict->count
    objectives_by_sub = Counter()
    excessive = Counter()
    partial_records = []
    if not REPORT.exists():
        return None
    cur_sub = None
    cur_title = None
    in_per_sub_table = False
    for line in REPORT.read_text(encoding="utf-8-sig").splitlines():
        if SECTION_HEAD_RE.match(line):
            in_per_sub_table = False
        if line.startswith("## Per-subdomain summary"):
            in_per_sub_table = True
            continue
        if in_per_sub_table:
            continue
        m_sub = SUB_RE.match(line)
        if m_sub:
            cur_sub = m_sub.group(1)
            cur_title = line.lstrip("# ").strip()
            continue
        if not cur_sub:
            continue
        # within a record
        m_v = VERDICT_RE.search(line)
        m_c = CONFIDENCE_RE.search(line)
        if m_v:
            v = m_v.group(1).strip().split(" ")[0]
            verdicts[v] += 1
            by_sub[cur_sub][v] += 1
            objectives_by_sub[cur_sub] += 1
            if v == "partial":
                partial_records.append((cur_sub, cur_title))
        if m_c:
            c = m_c.group(1).strip().split(" ")[0]
            confidences[c] += 1
        m_a = ANCHORS_RE.match(line + "\n" + "")
        # not used here
    return {
        "verdicts": verdicts,
        "confidences": confidences,
        "by_sub": by_sub,
        "objectives_by_sub": objectives_by_sub,
        "partial_records": partial_records,
    }


def render_summary(stats):
    lines = [MARKER]
    lines.append("# Executive summary — objective-anchor audit\n")
    lines.append(f"- Total objectives audited: **{sum(stats['objectives_by_sub'].values())}**")
    lines.append(f"- Sub-domains covered: **{len(stats['objectives_by_sub'])}**")
    v = stats["verdicts"]
    lines.append(f"- Verdicts: sufficient={v.get('sufficient', 0)}, "
                 f"partial={v.get('partial', 0)}, excessive={v.get('excessive', 0)}")
    c = stats["confidences"]
    lines.append(f"- Confidence: high={c.get('high', 0)}, medium={c.get('medium', 0)}, "
                 f"low={c.get('low', 0)}")
    if stats["partial_records"]:
        lines.append("")
        lines.append("## Partial-coverage findings (requires review)")
        lines.append("")
        lines.append("| Sub-domain | Entry |")
        lines.append("|---|---|")
        for sub, title in stats["partial_records"]:
            lines.append(f"| {sub} | {title} |")
        lines.append("")
        lines.append("These objectives have a missing CSF 2.0 anchor relative to the "
                     "regulatory obligation in their article basis. The agent judges "
                     "them as worth human review.")
    # sub-domains with partial verdict
    partial_subs = sorted(s for s, v in stats["by_sub"].items() if v.get("partial", 0) > 0)
    if partial_subs:
        lines.append("")
        lines.append("## Sub-domains containing partial-coverage entries")
        lines.append("")
        lines.append(", ".join(partial_subs))
    lines.append("")
    lines.append("## How to read this report")
    lines.append("")
    lines.append("- Each `### D-XX.Y · REG · subso SO-...` and `### D-XX.Y · REG · req N.N.N` entry follows the 7-field template.")
    lines.append("- Anchors classified CORE / UTILITY / NOISE based on objective + fit_criterion keywords vs. CSF 2.0 official title.")
    lines.append("- `excessive` verdicts flag literal duplicate IDs in the same objective's `anchors_listed` (mechanical duplication, safe to deduplicate).")
    lines.append("- `partial` verdicts flag an objective whose regulatory article cites a CSF control not in the listed anchors.")
    lines.append("- `low` confidence: the article block for the source_SR does not list a per-SR nist_csf_mapping; CORE/UTILITY judgments use only the official CSF title and the objective prose. Verify by opening the article.")
    lines.append("")
    return "\n".join(lines) + "\n\n---\n\n"


def main():
    text = REPORT.read_text(encoding="utf-8-sig")
    if text.startswith(MARKER):
        print("summary already prepended; skipping")
        return
    stats = parse_report()
    if not stats:
        print("report not found")
        return
    summary = render_summary(stats)
    REPORT.write_text(summary + text, encoding="utf-8", newline="\n")
    print(f"prepended executive summary; {sum(stats['objectives_by_sub'].values())} "
          f"objectives audited, {stats['verdicts'].get('partial', 0)} partial, "
          f"{stats['verdicts'].get('excessive', 0)} excessive, "
          f"{stats['confidences'].get('low', 0)} low-confidence")


if __name__ == "__main__":
    main()
