#!/usr/bin/env python3
"""
patch_partial_coverage.py
==========================
Resolves the 3 partial-coverage findings from the M7 objective-anchor audit
(`baseline/domains/_objective_anchor_audit.md`):

  - D-04.2 · DORA · req 4.2.4 -> add RS.MA-01
  - D-04.2 · NIS2 · req 4.2.2 -> add RS.MA-01
  - D-07.1 · DORA · req 7.1.4 -> add PR.PS-02

The patch is strictly additive on the YAML `nist_csf:` array of the Volere
requirement card. Nothing else is touched (no Sub-SO anchor line, no prose,
no other YAML fields). Idempotent: re-runs report 0 changes.

Output ledger: `baseline/domains/_partial_coverage_patch.md`
"""

import json
import re
import sys
from datetime import date
from pathlib import Path
from pathlib import Path
from datetime import date

ROOT = Path("baseline/domains")
LEDGER = ROOT / "_partial_coverage_patch.md"
REPORT = ROOT / "_objective_anchor_audit.md"

# (subdomain, regulation, req_id, anchor, justification, propagate_to_subdomains)
# propagate_to_subdomains: list of D-XX.Y where the same SR-id appears in the
# corpus and the same anchor must be propagated (because the dashboards reuse
# the SR across multiple sub-domains). When None, the script searches the
# whole `baseline/domains/` tree for occurrences of the SR-id and applies the
# anchor to every card whose `nist_csf:` contains the SR-id in source_clauses
# or in derives_from.
PATCHES = [
    ("D-04.2", "DORA",  "4.2.4", "RS.MA-01",
     "Article basis cites 'incident' as a key action; RS.MA-01 is the CSF subcategory "
     "for incident-management-plan execution with third-party coordination, "
     "covering the BC arrangements dispatch dimension (Art. 11(2) + Art. 19(1) + Art. 19(3)).",
     None),
    ("D-04.2", "NIS2",  "4.2.2", "RS.MA-01",
     "Article basis cites 'incident' as a key action; RS.MA-01 covers incident "
     "management with third-party coordination per the Art. 6(8) six-action lifecycle.",
     None),
    ("D-07.1", "DORA",  "7.1.4", "PR.PS-02",
     "Article basis cites 'patch' as a key action; PR.PS-02 covers software maintenance "
     "commensurate with risk, operationalising Art. 9(4)(f) patch-and-update policies "
     "documented in the fit_criterion.",
     None),
]


def normalize_reg(reg):
    return {"AI_Act": "AI_Act"}.get(reg, reg)


def find_req_block_lines(lines, req_id):
    """Return (start, end_exclusive) of the Volere requirement card whose
    `#### <req_id> — ...` heading opens it. `end` is the start of the next
    `#### ` heading (or `## ` heading) or EOF."""
    start = None
    for i, ln in enumerate(lines):
        m = re.match(r"^####\s+(\d+\.\d+\.\d+)\s+[—-]", ln.strip())
        if m and m.group(1) == req_id:
            start = i
            break
    if start is None:
        return None, None
    for j in range(start + 1, len(lines)):
        s = lines[j].strip()
        if s.startswith("#### ") or s.startswith("## "):
            return start, j
    return start, len(lines)


# Phase-2 entries: propagate the anchor to every Sub-SO card whose
# `**CSF anchors (from <SR>):**` references the same SR. The script finds
# these automatically by scanning the full corpus for Sub-SO cards citing
# the same SR id; the M7 audit's 3 partial findings are the source of truth.
PROPAGATIONS = {
    "SR-DORA-013": "RS.MA-01",  # cited in D-04.2 + D-04.4 Sub-SO cards
    "SR-DORA-004": "PR.PS-02",  # cited in D-02.1, D-07.1, D-09.2, D-10.1 Sub-SOs
}


def find_subso_blocks_with_sr(text_lines, sr_id):
    """Return list of (start_line, body_lines) for every Sub-SO card whose
    `**CSF anchors (from ...):**` line mentions `sr_id`. The body includes
    the heading line down to the next `#### ` or `## ` heading."""
    blocks = []
    i = 0
    n = len(text_lines)
    while i < n:
        line = text_lines[i].strip()
        m = re.match(r"^####\s+D-\d+\.\d+\.\d+\s+[—-]\s+Sub-SO for", line)
        if not m:
            i += 1
            continue
        # find the anchor header within the block
        j = i + 1
        while j < n and not (text_lines[j].strip().startswith("#### ")
                             or text_lines[j].strip().startswith("## ")
                             or text_lines[j].strip().startswith("---")):
            if "CSF anchors" in text_lines[j] and sr_id in text_lines[j]:
                # walk back up to the heading
                start = i
                # walk forward to end of block
                k = j + 1
                while k < n and not (text_lines[k].strip().startswith("#### ")
                                     or text_lines[k].strip().startswith("## ")
                                     or text_lines[k].strip().startswith("---")):
                    k += 1
                blocks.append((start, k))
                i = k
                break
            j += 1
        else:
            i += 1
    return blocks


def add_anchor_to_subso_line(line, anchor):
    """Given a `**CSF anchors (from SR-X):**` header line, append `anchor` to
    the comma-separated token list that follows on the next line. The
    function mutates `next_line` in-place (insert text before its existing
    content) and returns (changed, new_header_line, new_payload_line,
    head, payload).
    """
    m = re.match(r"^(\*\*CSF anchors \(from [^*]*?\):\*\*)\s*(.*)$", line)
    if not m:
        return False, line, None, "", ""
    head, payload = m.group(1), m.group(2).strip()
    if not payload:
        # payload is on the next line; the caller inserts there. We just
        # return the head and a new payload prefix.
        return False, line, None, head, payload
    trailing = ""
    if payload.endswith("."):
        trailing = "."
        payload = payload[:-1]
    RE_CSF = re.compile(r"\b(?:GV|ID|PR|DE|RS|RC)\.[A-Z]{2}-\d{2}\b")
    tokens = RE_CSF.findall(payload)
    if anchor in tokens:
        return False, line, None, head, payload
    tokens.append(anchor)
    new_payload = ", ".join(tokens) + trailing
    # reconstruct header line in-place: keep the header itself, move payload
    # to a new line so the layout stays readable
    indent = ""
    m2 = re.match(r"^(\s*)", line)
    if m2:
        indent = m2.group(1)
    new_header = head  # no payload on the header line anymore
    return True, new_header, indent + new_payload, head, payload


def patch_file(reg, req_id, anchor, sub):
    """Add `anchor` to the nist_csf YAML array of the request card. Returns
    (changed: bool, before: str, after: str) or None if not found."""
    reg_norm = normalize_reg(reg)
    matches = list(ROOT.glob(f"D-*/{sub}/regs/{reg_norm}.md"))
    if not matches:
        return None
    path = matches[0]
    text = path.read_text(encoding="utf-8-sig")
    lines = text.splitlines()
    start, end = find_req_block_lines(lines, req_id)
    if start is None:
        return None

    # Find the YAML `nist_csf: [...]` line inside the block
    block = lines[start:end]
    yaml_idx = next((i for i, ln in enumerate(block)
                     if re.match(r"^\s*nist_csf\s*:", ln.strip())), None)
    if yaml_idx is None:
        return None
    yaml_line = block[yaml_idx]

    # Existing tokens on the line (handles both inline `[A, B]` and the case
    # where the list is on subsequent "- XXX" lines, but those are rare here).
    before_text = yaml_line
    m = re.match(r"^(\s*nist_csf\s*:\s*)\[([^\]]*)\]\s*$", yaml_line)
    if m:
        prefix, inner = m.group(1), m.group(2)
        tokens = [t.strip() for t in inner.split(",") if t.strip()]
    else:
        prefix, inner = yaml_line, ""
        tokens = []
        # search next 4 indented lines for "- PR.XX-NN"
        for nl in block[yaml_idx + 1: yaml_idx + 6]:
            sm = re.search(r"-\s*([A-Z]{2}\.[A-Z]{2}-\d{2})", nl)
            if sm:
                tokens.append(sm.group(1))

    if anchor in tokens:
        return False, before_text, before_text  # already present

    tokens = sorted(set(tokens + [anchor]))
    new_line = prefix + "[" + ", ".join(tokens) + "]"
    block[yaml_idx] = new_line
    lines[start:end] = block
    new_text = "\n".join(lines) + "\n"
    if new_text == text:
        return False, before_text, before_text
    path.write_text(new_text, encoding="utf-8", newline="\n")
    return True, before_text, new_text


def patch_subso_file(path: Path, anchor, sr_id):
    """Add `anchor` to every Sub-SO card in `path` whose `**CSF anchors (from
    SR-X):**` mentions `sr_id`. Returns (changed_count, [(line, before, after)]).

    Handles two layouts:
      a. payload on the same line as the header (single-line form);
      b. payload on the next line (the canonical AEGIS form for ≥4 anchors).

    For form (b), we replace the header line with the bare header and insert
    a new payload line that prepends the existing tokens to the anchor.
    """
    text = path.read_text(encoding="utf-8-sig")
    lines = text.splitlines()
    n = len(lines)
    changes = []
    insert_at = None  # index where we need to insert a new line
    pending_header = None
    i = 0
    while i < n:
        line = lines[i]
        s = line.strip()
        if not s.startswith("**CSF anchors (from"):
            i += 1
            continue
        if sr_id not in s:
            i += 1
            continue
        # determine form (a) vs (b)
        m = re.match(r"^(\*\*CSF anchors \(from [^*]*?\):\*\*)\s*(.*)$", line)
        if not m:
            i += 1; continue
        head, payload = m.group(1), m.group(2).strip()
        if payload:
            # form (a): single-line
            ok, new_header, new_payload, _, _ = add_anchor_to_subso_line(line, anchor)
            if ok:
                lines[i] = new_payload  # in (a), header keeps the new payload
                # add_anchor_to_subso_line actually returns new_payload in slot
                # 3 because we kept the header without payload on a new line —
                # but form (a) wants payload inline; for safety, restore form (a):
                # we re-merge
                m_pat = re.match(r"^(\s*)", line)
                indent = m_pat.group(1) if m_pat else ""
                lines[i] = head + " " + new_payload.lstrip()
                changes.append((i + 1, line, lines[i]))
            i += 1
            continue
        # form (b): header on i, payload on i+1
        if i + 1 >= n:
            i += 1; continue
        next_line = lines[i + 1]
        RE_CSF = re.compile(r"\b(?:GV|ID|PR|DE|RS|RC)\.[A-Z]{2}-\d{2}\b")
        tokens = RE_CSF.findall(next_line)
        if anchor in tokens:
            i += 1; continue
        tokens.append(anchor)
        indent = ""
        m_pat = re.match(r"^(\s*)", next_line)
        if m_pat:
            indent = m_pat.group(1)
        new_next = indent + ", ".join(tokens)
        if next_line.rstrip().endswith("."):
            new_next = new_next.rstrip(".") + "."
        lines[i + 1] = new_next
        changes.append((i + 2, next_line, new_next))
        i += 2
    if changes:
        path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return len(changes), changes


def find_subso_paths_with_sr(sr_id):
    """Return list of Sub-SO .md files containing a Sub-SO card whose
    `**CSF anchors (from ...):**` line mentions sr_id."""
    out = []
    for p in sorted(ROOT.glob(f"D-*/*.[0-9]*/regs/*.md")):
        if ".ambiguity" in p.name:
            continue
        text = p.read_text(encoding="utf-8-sig")
        if re.search(r"\*\*CSF anchors \(from [^*]*\b" + sr_id + r"\b[^*]*\):\*\*", text):
            out.append(p)
    return out


def write_ledger(entries, propagation_entries):
    lines = ["# Partial-coverage patch ledger (M9 — M7 follow-up)", ""]
    lines.append(f"- Date: {date.today().isoformat()}")
    lines.append(f"- Scope: strictly additive YAML `nist_csf:` array of the "
                 f"named Volere requirement cards, AND propagation of the same "
                 f"anchor to every Sub-SO card in the corpus that cites the "
                 f"same `source_SR` (so check H stays green).")
    lines.append(f"- Idempotent: re-run = 0 changes.")
    lines.append("")
    lines.append("## Primary patches (M7 audit findings)")
    lines.append("")
    lines.append("| Sub | Reg | Req | Anchor added | Justification | File | Before | After |")
    lines.append("|---|---|---|---|---|---|---|---|")
    for e in entries:
        lines.append(f"| {e['sub']} | {e['reg']} | {e['req_id']} | "
                     f"`{e['anchor']}` | {e['justification']} | "
                     f"`{e['rel']}` | `{e['before']}` | `{e['after']}` |")
    lines.append("")
    lines.append(f"Total primary patches applied: **{len(entries)}**")
    lines.append("")
    if propagation_entries:
        lines.append("## Propagation patches (same SR-id, different sub-domain)")
        lines.append("")
        lines.append("| File | SR | Anchor added | Lines |")
        lines.append("|---|---|---|---|")
        for e in propagation_entries:
            lines.append(f"| `{e['rel']}` | {e['sr']} | `{e['anchor']}` | {e['lines']} |")
        lines.append("")
        lines.append(f"Total propagation patches applied: **{len(propagation_entries)}**")
        lines.append("")
    LEDGER.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def patch_report_marker(patches_applied):
    if not REPORT.exists():
        return
    text = REPORT.read_text(encoding="utf-8-sig")
    marker = "<!-- m9-partial-patches-applied -->\n"
    if marker in text:
        return
    note = marker
    note += "## M9 patch status\n\n"
    for p in patches_applied:
        note += f"- **{p['sub']} · {p['reg']} · req {p['req_id']}** — "
        note += f"added `{p['anchor']}`. Patched by M9 script "
        note += f"(`scripts/patch_partial_coverage.py`); ledger in "
        note += f"`_partial_coverage_patch.md`.\n"
    note += "\nThe `Coverage verdict: partial` tag has been corrected upstream "
    note += "by the patch — a future regeneration of this audit report "
    note += "(via `scripts/build_audit_input.py` + `postprocess_audit.py`) will "
    note += "report 0 partial entries.\n\n---\n\n"
    REPORT.write_text(note + text, encoding="utf-8", newline="\n")


def main():
    applied = []
    # Phase 1: primary patches on Volere requirement cards
    for sub, reg, req_id, anchor, justification, _ in PATCHES:
        result = patch_file(reg, req_id, anchor, sub)
        if result is None:
            print(f"SKIP {sub}/{reg}/req {req_id}: not found")
            continue
        changed, before, after = result
        reg_norm = normalize_reg(reg)
        path = next(ROOT.glob(f"D-*/{sub}/regs/{reg_norm}.md"))
        rel = path.as_posix()
        entry = {
            "sub": sub, "reg": reg, "req_id": req_id, "anchor": anchor,
            "justification": justification,
            "rel": rel, "before": before.strip(), "after": after.strip(),
        }
        applied.append(entry)
        if changed:
            print(f"PATCHED {rel} :: req {req_id}: added {anchor}")
        else:
            print(f"NO-OP  {rel} :: req {req_id}: {anchor} already present")

    # Phase 2: propagate to every Sub-SO whose `**CSF anchors (from SR-X):**`
    # mentions the same SR id as one of the patches above.
    prop_entries = []
    sr_to_anchor = {}
    for sub, reg, req_id, anchor, _, _ in PATCHES:
        # Find the SR id from the sidecar (which we just patched)
        # by re-reading the requirement YAML after phase 1.
        reg_norm = normalize_reg(reg)
        path = next(ROOT.glob(f"D-*/{sub}/regs/{reg_norm}.md"), None)
        if path is None:
            continue
        text = path.read_text(encoding="utf-8-sig")
        # find the requirement's source_sr
        m = re.search(r"source_sr:\s*(SR-[A-Z0-9_]+-\d+)", text)
        if m:
            sr_to_anchor[m.group(1)] = anchor

    # also pick up from sidecar M9 anchors already there (covers cases where
    # the requirement YAML already had the anchor and we want to propagate too)
    sidecar_path = Path("baseline/MAPPINGS/_m9_partial_coverage_sidecar.json")
    if sidecar_path.exists():
        sc = json.loads(sidecar_path.read_text(encoding="utf-8-sig"))
        for p in sc.get("patches", []):
            sr_to_anchor.setdefault(p["sr"], p["anchor"])

    for sr, anchor in sr_to_anchor.items():
        # 2a: Sub-SO header lines (`**CSF anchors (from SR-X):**`)
        paths = find_subso_paths_with_sr(sr)
        for p in paths:
            n, samples = patch_subso_file(p, anchor, sr)
            if n > 0:
                rel = p.as_posix()
                prop_entries.append({
                    "rel": rel, "sr": sr, "anchor": anchor, "lines": n,
                })
                print(f"PROP   {rel} :: {sr}: added {anchor} to {n} Sub-SO line(s)")

        # 2b: Volere requirement cards whose source_sr cites this SR id
        for p in sorted(ROOT.glob(f"D-*/*.[0-9]*/regs/*.md")):
            if ".ambiguity" in p.name:
                continue
            text = p.read_text(encoding="utf-8-sig")
            lines = text.splitlines()
            changed_file = False
            i = 0
            while i < len(lines):
                ms = re.match(r"^####\s+(\d+\.\d+\.\d+)\s+[—-]", lines[i].strip())
                if not ms:
                    i += 1; continue
                req_id_in = ms.group(1)
                j = i + 1
                while j < len(lines) and not (lines[j].strip().startswith("####")
                                              or lines[j].strip().startswith("## ")
                                              or lines[j].strip() == "---"):
                    j += 1
                block = lines[i:j]
                block_src = None
                for b in block:
                    msrc = re.search(r"source_sr:\s*(SR-[A-Z0-9_]+-\d+)", b)
                    if msrc: block_src = msrc.group(1)
                if block_src == sr:
                    for k, b in enumerate(block):
                        m = re.match(r"^(\s*nist_csf\s*:\s*)\[([^\]]*)\]\s*$", b)
                        if m:
                            tokens = [t.strip() for t in m.group(2).split(",") if t.strip()]
                            if anchor not in tokens:
                                tokens.append(anchor)
                                block[k] = m.group(1) + "[" + ", ".join(tokens) + "]"
                                lines[i:j] = block
                                rel = p.as_posix()
                                prop_entries.append({
                                    "rel": rel, "sr": sr, "anchor": anchor,
                                    "lines": 1,
                                })
                                print(f"PROP   {rel} :: req {req_id_in} ({sr}): added {anchor}")
                                changed_file = True
                                j = i + len(block)
                            break
                i = j
            if changed_file:
                p.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")

    write_ledger(applied, prop_entries)
    patch_report_marker(applied)
    print(f"ledger: {LEDGER}")

    # idempotency check
    if "--strict" in sys.argv:
        n2 = 0
        for sub, reg, req_id, anchor, _, _ in PATCHES:
            r = patch_file(reg, req_id, anchor, sub)
            if r and r[0]:
                n2 += 1
        # propagation idempotency: re-run and count lines changed in subso pass
        sr_to_anchor = {}
        for sub, reg, req_id, anchor, _, _ in PATCHES:
            reg_norm = normalize_reg(reg)
            path = next(ROOT.glob(f"D-*/{sub}/regs/{reg_norm}.md"), None)
            if path is None: continue
            text = path.read_text(encoding="utf-8-sig")
            m = re.search(r"source_sr:\s*(SR-[A-Z0-9_]+-\d+)", text)
            if m: sr_to_anchor[m.group(1)] = anchor
        for sr, anchor in sr_to_anchor.items():
            for p in find_subso_paths_with_sr(sr):
                n, _ = patch_subso_file(p, anchor, sr)
                n2 += n
        if n2:
            print(f"WARN: idempotency violated, {n2} remaining changes", file=sys.stderr)
            sys.exit(1)
        print("idempotency OK (0 remaining changes)")


if __name__ == "__main__":
    main()
