#!/usr/bin/env python3
"""
build_audit_input.py
=====================
Read-only packer: emits an NDJSON file (`_audit_input.jsonl`) with one line
per objective in the modular corpus. Each record carries everything an
auditor needs to judge the adequacy of the CSF 2.0 anchors without reading
the full corpus file by file.

Targets (post-M6 normalized corpus):
  baseline/domains/D-XX_Name/D-XX.Y/regs/*.md        (excl *.ambiguity.md)
Output:
  baseline/domains/_audit_input.jsonl                 (NOT committed)

For each Sub-SO card and each Volere requirement card:
  - YAML fields (id, applies_to, inherits_from, source_SR, etc.)
  - Objective prose (verbatim)
  - CSF anchors listed + their official CSF 2.0 text
  - Candidate regulatory articles: articles/<REG>_Art_<N>.md whose nist_csf_mapping
    references the same source_SR (or, fallback, whose article number appears
    in the Objective prose).
"""

import json
import re
from pathlib import Path

ROOT = Path("baseline/domains")
ART = ROOT.parent / "domains"  # articles/ live at the same D-XX.Y/ level (sibling of regs/)
OUT = ROOT / "_audit_input.jsonl"

# --- CSF 2.0 referential (title text per ID) -------------------------------
csf_text = {}
for p in (ROOT.parent / "CONTROLS" / "NIST_CSF_2.0").rglob("*.json"):
    if p.name.startswith("_") or p.name == "CSF_2.0.json":
        continue
    d = json.loads(p.read_text(encoding="utf-8-sig"))
    csf_text[d["subcategory_id"]] = d["subcategory_text"]


def norm_reg(reg):
    """Module filename stem -> canonical reg token used by Source SR."""
    return {"GDPR": "GDPR", "CRA": "CRA", "NIS2": "NIS2", "DORA": "DORA",
            "AI_Act": "AI_Act"}.get(reg, reg)


def article_candidates(reg: str, src_sr: str, objective_text: str) -> list:
    """Articles in articles/ that cite the SR (or whose Art. number appears
    in the Objective prose)."""
    art_dir = ART / "D-01_Data-Protection" / "D-01.1" / "articles"  # path doesn't matter
    # find articles/ for the same sub-domain — caller's parent has the dir
    # The real location will be resolved by the caller (we receive sub_dir).
    raise NotImplementedError  # set later per caller


def extract_csf_titles(ids):
    return [{"id": i, "title": csf_text.get(i, "(unknown)")} for i in ids]


def extract_yaml(lines, start):
    """Parse a fenced ```yaml block starting at line index `start` (the fence
    opener). Returns (inner_lines, fence_closer_index)."""
    j = start + 1
    inner = []
    while j < len(lines):
        if lines[j].strip().startswith("```"):
            return inner, j
        inner.append(lines[j])
        j += 1
    return inner, j


# --- per-module walk --------------------------------------------------------

records = []
sub_to_articles = {}  # sub_id -> articles/ dir (for resolution by caller later)

for sub_dir in sorted(ROOT.glob("D-*/D-*.[0-9]*")):
    if not re.fullmatch(r"D-\d+\.\d+", sub_dir.name):
        continue
    sub_id = sub_dir.name
    sub_name = ""
    idx = sub_dir / "_index.md"
    if idx.exists():
        m = re.search(r"^# D-[\d.]+ — (.+)$", idx.read_text(encoding="utf-8-sig"), re.M)
        if m:
            sub_name = m.group(1).strip()

    art_dir = sub_dir / "articles"
    art_files = sorted(art_dir.glob("*.md")) if art_dir.exists() else []

    for regf in sorted((sub_dir / "regs").glob("*.md")):
        if ".ambiguity" in regf.name:
            continue
        reg = regf.stem  # GDPR, CRA, NIS2, DORA, AI_Act
        text = regf.read_text(encoding="utf-8-sig")
        lines = text.splitlines()

        # --- Sub-SO cards ---
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            m = re.match(r"^####\s+D-\d+\.\d+\.\d+\s+[—-]\s+Sub-SO for\s+(\S+.*)$", line)
            if not m:
                i += 1
                continue
            # parse this Sub-SO block (from line i until next heading)
            j = i + 1
            while j < len(lines) and not (lines[j].strip().startswith("####")
                                          or lines[j].strip().startswith("## ")
                                          or lines[j].strip() == "---"):
                j += 1
            block = lines[i:j]
            yaml_idx = next((k for k, ln in enumerate(block)
                             if ln.strip().startswith("```yaml")), None)
            yaml = {}
            if yaml_idx is not None:
                ylines, _ = extract_yaml(block, yaml_idx)
                for yln in ylines:
                    ym = re.match(r"^\s*([A-Za-z0-9_]+):\s*(.*?)\s*$", yln)
                    if ym:
                        yaml[ym.group(1)] = ym.group(2)
            # Objective prose: lines from "**Objective.**" up to next blank
            # line or another bold label (`**CSF anchors**`, `**Considerations.**`).
            obj_lines = []
            in_obj = False
            for ln in block:
                s = ln.strip()
                if s.startswith("**Objective.**"):
                    in_obj = True
                    obj_lines.append(re.sub(r"^\*\*Objective\.\*\*\s*", "", s))
                    continue
                if in_obj:
                    if not s or s.startswith("**") or s.startswith("#"):
                        break
                    obj_lines.append(s)
            obj_text = " ".join(obj_lines).strip()
            csf_anchors = []
            in_csf = False
            for ln in block:
                s = ln.strip()
                m2 = re.match(r"^\*\*CSF anchors\b.*?\*\*:?\s*(.*)$", s)
                if m2:
                    head_payload = m2.group(1)
                    for tok in re.findall(r"\b(?:GV|ID|PR|DE|RS|RC)\.[A-Z]{2}-\d{2}\b", head_payload):
                        csf_anchors.append(tok)
                    in_csf = True
                    continue
                if in_csf:
                    for tok in re.findall(r"\b(?:GV|ID|PR|DE|RS|RC)\.[A-Z]{2}-\d{2}\b", s):
                        csf_anchors.append(tok)
                    # close on blank line or new heading
                    if not s or s.startswith("#"):
                        in_csf = False
            # Find candidate articles by SR or Art. number in prose
            src = yaml.get("source_SR", "").strip()
            article_paths = []
            art_nums = set(re.findall(r"Art(?:\.|icle)\s*(\d+(?:\([^)]*\))?)", obj_text))
            for a in art_files:
                a_text = a.read_text(encoding="utf-8-sig")
                if src and (src in a_text or
                            re.search(rf"\b{re.escape(src)}\b", a_text)):
                    article_paths.append(a.relative_to(ROOT.parent).as_posix())
            if not article_paths and art_nums:
                for a in art_files:
                    if any(f"Art. {n}" in a.read_text(encoding="utf-8-sig") for n in art_nums):
                        article_paths.append(a.relative_to(ROOT.parent).as_posix())
            records.append({
                "kind": "subso",
                "subdomain": sub_id,
                "subdomain_name": sub_name,
                "regulation": reg,
                "id": yaml.get("id", ""),
                "applies_to": yaml.get("applies_to", ""),
                "inherits_from": yaml.get("inherits_from", ""),
                "source_SR": src,
                "objective": obj_text.strip(),
                "anchors_listed": extract_csf_titles(csf_anchors),
                "candidate_articles": sorted(set(article_paths))[:6],
            })
            i = j

        # --- Requirement cards (split by `#### N.N.N — title`) ---
        in_req_section = False
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if line.startswith("## Security Requirements"):
                in_req_section = True
                i += 1
                continue
            if line.startswith("## ") and in_req_section and not line.startswith("## Security Requirements"):
                in_req_section = False
                i += 1
                continue
            if not in_req_section or not line.startswith("#### "):
                i += 1
                continue
            # req block: from here to next heading of equal/higher level.
            # `---` is a section separator (not a heading) and must be
            # contained in the block.
            j = i + 1
            while j < len(lines) and not lines[j].strip().startswith("####") \
                    and not lines[j].strip().startswith("## "):
                j += 1
            block = lines[i:j]
            # find ```yaml fence
            yaml_idx = next((k for k, ln in enumerate(block)
                             if ln.strip().startswith("```yaml")), None)
            if yaml_idx is None:
                i = j
                continue
            ylines, _ = extract_yaml(block, yaml_idx)
            # Minimal YAML list-aware parser. Top-level of these cards is a
            # single list item starting with "- key: value". Child fields are
            # indented lines; under nist_csf, the actual items are "- PR.XX-NN".
            items = []  # (key, value, kind) where kind in {list, kv, nist_item}
            current_list_value_key = None  # e.g. "nist_csf" collecting items

            def strip_list_prefix(ln: str):
                # "- " (possibly with leading spaces) at the start of an item
                m = re.match(r"^(\s*)-\s+(.*)$", ln)
                if not m:
                    return None
                return m.group(1), m.group(2)

            for yln in ylines:
                # New list item: "- key: value" or "- token" under a parent key
                if re.match(r"^\s*-\s+", yln):
                    indent, rest = strip_list_prefix(yln)
                    m = re.match(r"^([A-Za-z0-9_]+):\s*(.*?)\s*$", rest)
                    if m:
                        k, v = m.group(1), m.group(2)
                        items.append((k, v, "list"))
                        current_list_value_key = k
                    else:
                        # "- PR.DS-01" inside nist_csf / derives_from list
                        tok = rest.strip().strip('"').strip("'")
                        items.append((current_list_value_key or "__list_item__", tok, "list_item"))
                    continue
                # Plain "  key: value" line (with optional leading whitespace)
                m = re.match(r"^\s*([A-Za-z0-9_]+):\s*(.*?)\s*$", yln)
                if m:
                    items.append((m.group(1), m.group(2), "kv"))
                    # When value is a block scalar marker `|`, keep the key
                    # as the current list-value key so the following indented
                    # continuation lines (kind='cont') are attributed to it.
                    current_list_value_key = (
                        m.group(1) if m.group(2).startswith("|") else None
                    )
                    continue
                # Continuation of a list of scalars (rare)
                items.append((current_list_value_key or "__cont__", yln, "cont"))

            yaml = {}
            list_values = {}
            i_list = None
            src_sr = ""
            title = ""
            req_id = ""
            for k, v, kind in items:
                if kind == "kv":
                    yaml[k] = v
                    if k == "source_sr":
                        src_sr = v
                    elif k == "req_id":
                        req_id = v
                    elif k == "title":
                        title = v
                    elif k == "nist_csf":
                        # possible inline value
                        if v:
                            list_values.setdefault(k, []).append(v)
                if kind == "list":
                    # list opener: "- key: value" — record scalar fields
                    yaml[k] = v
                    if k == "source_sr":
                        src_sr = v
                    elif k == "req_id":
                        req_id = v
                    elif k == "title":
                        title = v
                    if k in ("nist_csf",) and v and not v.startswith("-"):
                        list_values.setdefault(k, []).append(v)
                    # list openers close any open block scalar
                    in_block = k if v.startswith("|") else None
                elif kind == "list_item":
                    if re.match(r"^[A-Z]{2}\.[A-Z]{2}-\d{2}$", v):
                        list_values.setdefault("nist_csf", []).append(v)
            csf_tokens = []
            for ln in list_values.get("nist_csf", []):
                csf_tokens += re.findall(r"[A-Z]{2}\.[A-Z]{2}-\d{2}", ln)
            i_list = sorted(set(csf_tokens))
            # Collect description / fit_criterion block scalars (`key: |`).
            # Re-walk ylines because the block scalar body is NOT broken by
            # item boundaries (which were rebuilt with stripped keys).
            desc_parts = []
            fit_parts = []
            in_block = None
            for idx, ln in enumerate(ylines):
                s = ln.strip()
                if s.startswith("description:") or s.startswith("fit_criterion:"):
                    key = "description" if s.startswith("description:") else "fit_criterion"
                    cont = s.split(":", 1)[1].lstrip()
                    in_block = key if cont.startswith("|") else None
                    continue
                if in_block:
                    # body of the block scalar (any indent level)
                    if s.startswith("#") or (s.startswith("- ") and idx > 0 and ylines[idx - 1].strip() == ""):
                        # new key or comment — close block
                        in_block = None
                        continue
                    if in_block == "description":
                        desc_parts.append(ln.rstrip())
                    else:
                        fit_parts.append(ln.rstrip())
            desc = "\n".join(desc_parts).strip()
            fit = "\n".join(fit_parts).strip()
            article_paths = []
            if src_sr:
                for a in art_files:
                    a_text = a.read_text(encoding="utf-8-sig")
                    if src_sr in a_text or re.search(rf"\b{re.escape(src_sr)}\b", a_text):
                        article_paths.append(a.relative_to(ROOT.parent).as_posix())
            if not article_paths:
                # fallback: any article cited in description/fit
                for n in re.findall(r"Art(?:\.|icle)\s*(\d+(?:\([^)]*\))?)", desc + " " + fit):
                    for a in art_files:
                        if f"Art. {n}" in a.read_text(encoding="utf-8-sig"):
                            article_paths.append(a.relative_to(ROOT.parent).as_posix())
            records.append({
                "kind": "requirement",
                "subdomain": sub_id,
                "subdomain_name": sub_name,
                "regulation": reg,
                "req_id": req_id,
                "title": title,
                "source_sr": src_sr,
                "description": desc.strip(),
                "fit_criterion": fit.strip(),
                "anchors_listed": extract_csf_titles(i_list or []),
                "candidate_articles": sorted(set(article_paths))[:6],
            })
            i = j

OUT.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in records) + "\n",
                encoding="utf-8", newline="\n")
print(f"records: {len(records)} ({sum(1 for r in records if r['kind']=='subso')} Sub-SO, "
      f"{sum(1 for r in records if r['kind']=='requirement')} requirement)")
print(f"sub-domains covered: {len(set(r['subdomain'] for r in records))}")
print(f"regulations covered: {sorted(set(r['regulation'] for r in records))}")
print(f"output: {OUT}")
