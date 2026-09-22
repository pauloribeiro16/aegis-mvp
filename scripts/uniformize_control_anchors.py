#!/usr/bin/env python3
"""
uniformize_control_anchors.py
=============================
Makes the aegis-mvp baseline control anchors correspond EXACTLY to the
per-regulation dashboard mappings extracted into
`baseline/MAPPINGS/sr_control_mappings/<REG>.json` (see
scripts/extract_dashboard_mappings.py), and adds the NIST PF 1.1 / AI RMF
axes where the dashboards publish them (GDPR -> PF, AI_Act -> AI RMF;
dashboard coverage only — no overlay supplementation).

Policy (user-confirmed):
  - The dashboards are the reference. For the same sr_id / clause, the
    dashboard control set wins. Line replacements are recorded in
    `baseline/MAPPINGS/_uniformization_changes.json` so that
    scripts/verify_no_loss.py can treat them as documented transformations.
  - Ids that do not resolve against baseline/CONTROLS referentials are never
    propagated (the extractor already excluded them).
  - Baseline-only SRs (no dashboard record) are left untouched and reported.
  - Anchors list lines carrying prose annotations (e.g. "(+ PR.DS-02 for the
    second limb)") are kept verbatim and flagged — never rewritten
    mechanically.

Surfaces updated (baseline only):
  1. D-*/D-XX.Y/regs/<REG>.md        Sub-SO "CSF anchors" blocks (CSF set
                                     uniformized; PF 1.1 / AI RMF anchor blocks
                                     added on their dashboard axes) + requirement
                                     YAML (`nist_csf` corrected; `nist_pf:` /
                                     `nist_airmf:` added).
  2. D-*/D-XX.Y/regs/<REG>.ambiguity.md
                                     one generated `**Control anchors:**` line
                                     per clause card (clause_id -> consuming SRs).
  3. baseline/registry.csv + baseline/01_Ambiguity_Registry.md
                                     `nist_csf,nist_pf,nist_airmf` columns / card
                                     anchor bullets (clause_id + regulation join).
  4. D-*/D-*.manifest.json           anchor indexes recomputed to stay coherent
                                     (+ `nist_pf` / `nist_airmf` / applicable
                                     PF/AI RMF keys where non-empty).

Usage:
  python scripts/uniformize_control_anchors.py            # check (dry run)
  python scripts/uniformize_control_anchors.py --apply    # write everything
"""

import argparse
import csv
import json
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DOMAINS = REPO / "baseline" / "domains"
XWALK_DIR = REPO / "baseline" / "MAPPINGS" / "sr_control_mappings"
CHANGES_JSON = REPO / "baseline" / "MAPPINGS" / "_uniformization_changes.json"
LEDGER = REPO / "baseline" / "MAPPINGS" / "_control_uniformization.md"
REGS = ["GDPR", "CRA", "NIS2", "DORA", "AI_Act"]
DASH_REL = {r: f"00_VISUALISATIONS/{r}/{r}_Dashboard.html" for r in REGS}
AXES_BY_REG = {"GDPR": [("nist_pf", "PF 1.1")], "AI_Act": [("nist_airmf", "AI RMF")]}
REG_ALIASES = {"NIS 2": "NIS2", "NIS_2": "NIS2", "AI Act": "AI_Act", "AI_ACT": "AI_Act"}

RE_SR_TOKEN = re.compile(r"SR-[A-Z0-9_]+-\d+")
RE_HDR = re.compile(r"^\*\*CSF anchors \(from (?P<from>[^*]*?)\):\*\*(?P<inline>.*)$")
RE_CSF_ANN = re.compile(r"\b(?:GV|ID|PR|DE|RS|RC)\.[A-Z]{2}-\d{2}(?: \(primary\))?")
_TOK = r"(?:GV|ID|PR|DE|RS|RC)\.[A-Z]{2}-\d{2}(?: \(primary\))?"
RE_STRICT_LIST = re.compile(rf"^{_TOK}(?:,\s*{_TOK})*\.?\s*$")
RE_YAML_FENCE = re.compile(r"^```")
RE_NIST_LINE = re.compile(r"^(\s*)nist_csf:\s*\[([^\]]*)\]\s*$")
RE_SR_FIELD = re.compile(r"source_SR?:\s*(SR-[A-Z0-9_]+-\d+)")
RE_CLAUSE = re.compile(r"^\*\*Clause: ([A-Za-z0-9_\-]+)\*\*")
RE_CA_LINE = re.compile(r"^(?:- )?\*\*Control anchors:\*\*")
RE_YAML_FENCE_INDENTED = re.compile(r"^\s*```")
RE_AXIS_HDR = re.compile(r"^\*\*(?:PF 1\.1|AI RMF) anchors \(from")


# ---------------------------------------------------------------- crosswalk
def load_crosswalk():
    by_sr, clause_index = {}, defaultdict(list)
    for reg in REGS:
        doc = json.loads((XWALK_DIR / f"{reg}.json").read_text(encoding="utf-8-sig"))
        for s in doc["srs"]:
            by_sr[s["sr_id"]] = s
            for c in s.get("source_clauses", []):
                cid = c.get("clause_id")
                if cid:
                    clause_index[(reg, cid)].append(s["sr_id"])
    for k in clause_index:
        clause_index[k] = sorted(set(clause_index[k]))
    return by_sr, clause_index


BY_SR = {}


def union_axis(sr_ids, axis):
    out = []
    for sr in sr_ids:
        for tok in BY_SR.get(sr, {}).get(axis, []):
            if tok not in out:
                out.append(tok)
    return out


def split_ann(tokens_with_ann):
    ids, ann = [], {}
    for t in tokens_with_ann:
        base = re.sub(r"\s*\(primary\)$", "", t)
        ids.append(base)
        if "(primary)" in t:
            ann[base] = True
    return ids, ann


def fmt_anchors(ids, ann=None):
    ann = ann or {}
    return ", ".join(i + (" (primary)" if ann.get(i) else "") for i in ids) + "."


def fmt_yaml(indent, key, ids):
    return f"{indent}{key}: [{', '.join(ids)}]"


def sr_ref_short(sr_ids):
    shown = [f"`{s}`" for s in sr_ids[:3]]
    if len(sr_ids) > 3:
        shown.append(f"+{len(sr_ids) - 3} more")
    return ", ".join(shown)


# ------------------------------------------------------------ file editing
class FileDoc:
    def __init__(self, path):
        self.path = path
        self.lines = path.read_text(encoding="utf-8-sig").splitlines()
        self.ops = []  # (line_no_1based, kind, payload); kind: replace|insert_after

    def replace(self, line_no, text):
        self.ops.append((line_no, "replace", text))

    def insert_after(self, line_no, text):
        self.ops.append((line_no, "insert_after", text))

    def insert_block_after(self, line_no, texts):
        """Atomic multi-line insertion (order-independent w.r.t. other ops)."""
        self.ops.append((line_no, "insert_block", list(texts)))

    def run(self):
        if not self.ops:
            return False
        for n, kind, payload in sorted(self.ops, key=lambda t: -t[0]):
            if kind == "replace":
                self.lines[n - 1] = payload
            elif kind == "insert_block":
                self.lines[n:n] = payload
            else:
                self.lines.insert(n, payload)
        self.path.write_text("\n".join(self.lines) + "\n", encoding="utf-8", newline="\n")
        return True

    def preview(self):
        """Lines with ops applied, without writing (for post-state computation)."""
        lines = list(self.lines)
        for n, kind, payload in sorted(self.ops, key=lambda t: -t[0]):
            if kind == "replace":
                lines[n - 1] = payload
            elif kind == "insert_block":
                lines[n:n] = payload
            else:
                lines.insert(n, payload)
        return lines


def parse_yaml_anchors(lines):
    """Every fenced-yaml `nist_csf:` line with nearest preceding source_SR."""
    out, in_fence, block_sr = [], False, None
    for i, ln in enumerate(lines):
        if RE_YAML_FENCE.match(ln.strip()):
            in_fence = not in_fence
            block_sr = None
            continue
        if not in_fence:
            continue
        m = RE_SR_FIELD.search(ln)
        if m:
            block_sr = m.group(1)
        m = RE_NIST_LINE.match(ln)
        if m and block_sr:
            out.append({"line_no": i + 1, "indent": m.group(1),
                        "items": [t.strip() for t in m.group(2).split(",") if t.strip()],
                        "sr": block_sr})
    return out


def parse_anchors_block(lines, hdr_idx):
    """(sr_ids, [strict list line indexes], tokens_with_ann, [(idx, text) gloss/odd lines],
    primary_is_odd, axis_seen)
    Gloss lines are italic prose annotations AFTER a strict list line (contextual,
    often referencing other SRs). A non-strict list line DIRECTLY after the header
    (no strict line first) is the primary anchor list itself -> primary_is_odd.
    Generated `**PF 1.1 / AI RMF anchors (from ...**` blocks are transparent to the
    consumption loop (recorded in axis_seen: label -> header line index) so parsing
    is stable between the first apply and subsequent idempotency checks."""
    header = lines[hdr_idx]
    inline = header.split("):**", 1)[1].strip() if "):**" in header else ""
    sr_ids = RE_SR_TOKEN.findall(header.split("):**")[0])
    list_idx, tokens, odd, axis_seen = [], [], [], {}
    if inline:
        tokens += RE_CSF_ANN.findall(inline)
    j = hdr_idx + 1
    while j < len(lines) and lines[j].strip():
        s = lines[j].strip()
        if RE_AXIS_HDR.match(s):
            axis_seen["PF 1.1" if "PF 1.1" in s else "AI RMF"] = j
            j += 2  # header + its list line
            continue
        if RE_STRICT_LIST.match(s):
            list_idx.append(j)
            tokens += RE_CSF_ANN.findall(s)
            j += 1
            continue
        if RE_CSF_ANN.search(s) and not s.startswith(("#", "|", ">", "-", "```")):
            odd.append((j, s))
            j += 1
            continue
        break
    primary_is_odd = bool(odd) and not list_idx and not inline
    return sr_ids, list_idx, tokens, odd, primary_is_odd, axis_seen


def req_id_for(lines_0based, line_no_1based):
    """req_id of the item containing the given 1-based line (scan upwards)."""
    for k in range(line_no_1based - 1, max(-1, line_no_1based - 90), -1):
        m = re.match(r"^\s*-?\s*req_id:\s*([0-9.]+)", lines_0based[k])
        if m:
            return m.group(1)
    return None


# --------------------------------------------------------------- reporting
class Report:
    def __init__(self):
        self.rows = []

    def add(self, kind, reg, where, detail):
        self.rows.append({"kind": kind, "reg": reg, "where": where, "detail": detail})

    def count(self, kind):
        return sum(1 for r in self.rows if r["kind"] == kind)


# ---------------------------------------------------------- regs/<REG>.md
def process_regs_module(doc, sub, reg, rep, changes):
    lines = doc.lines
    # ---- requirement YAML
    for req in parse_yaml_anchors(lines):
        rec = BY_SR.get(req["sr"])
        if not rec:
            rep.add("baseline_sr_no_dashboard", reg, f"{sub}/regs/{reg}.md", req["sr"])
            continue
        cur = []
        for t in req["items"]:
            cur += RE_CSF_ANN.findall(t)
        cur_ids, _ = split_ann(cur)
        tgt = rec["nist_csf"]
        if sorted(cur_ids) != sorted(tgt):
            new = fmt_yaml(req["indent"], "nist_csf", tgt)
            doc.replace(req["line_no"], new)
            changes.append({"file": str(doc.path.relative_to(REPO)).replace("\\", "/"),
                            "subdomain": sub, "old_line": lines[req["line_no"] - 1],
                            "new_line": new, "sr": req["sr"], "surface": "req_yaml_nist_csf"})
            rep.add("csf_replaced", reg, f"{sub}/regs/{reg}.md req@L{req['line_no']}",
                    f"{req['sr']}: {cur_ids} -> {tgt}")
        # PF / AI RMF YAML keys (only axes the dashboard publishes for this reg)
        for axis, _label in AXES_BY_REG.get(reg, []):
            vals = rec.get(axis, [])
            if not vals:
                continue
            new = fmt_yaml(req["indent"], axis, vals)
            existing = None
            for k in range(req["line_no"], min(req["line_no"] + 30, len(lines))):
                s = lines[k]
                if RE_YAML_FENCE_INDENTED.match(s):
                    break
                m2 = re.match(rf"^{re.escape(req['indent'])}{axis}:\s*\[([^\]]*)\]", s)
                if m2:
                    existing = (k + 1, [t.strip() for t in m2.group(1).split(",") if t.strip()])
                    break
                if re.match(rf"^{re.escape(req['indent'])}[A-Za-z_]+:", s):
                    break  # next key at same indent -> not present
            if existing:
                if existing[1] != vals:
                    doc.replace(existing[0], new)
                    rep.add("axis_yaml_updated", reg, f"{sub}/regs/{reg}.md",
                            f"{axis} @L{existing[0]} ({req['sr']})")
            else:
                doc.insert_after(req["line_no"], new)
                rep.add("axis_yaml_added", reg, f"{sub}/regs/{reg}.md",
                        f"{axis} after L{req['line_no']} ({req['sr']}: {', '.join(vals)})")
    # ---- Sub-SO anchors blocks
    for i, ln in enumerate(lines):
        if not RE_HDR.match(ln):
            continue
        sr_ids, list_idx, tokens, odd, primary_odd, axis_seen = parse_anchors_block(lines, i)
        joinable = [s for s in sr_ids if s in BY_SR]
        if sr_ids and not joinable:
            rep.add("baseline_sr_no_dashboard", reg, f"{sub}/regs/{reg}.md", ", ".join(sr_ids))
        cur_ids, cur_ann = split_ann(tokens)
        tgt = union_axis(joinable, "nist_csf") if joinable else []
        last_consumed = i
        if list_idx:
            last_consumed = list_idx[-1]
        elif odd:
            last_consumed = odd[-1][0]
        if joinable and primary_odd:
            # non-strict primary list: leave verbatim ONLY if its token set already
            # matches the dashboard; otherwise replace it (documented) — a stale
            # prose-annotated set is precisely a contradiction.
            if sorted(cur_ids) == sorted(tgt):
                rep.add("primary_list_verbatim_ok", reg, f"{sub}/regs/{reg}.md @L{odd[0][0] + 1}",
                        f"non-strict format, set matches dashboard ({len(cur_ids)} tokens)")
            else:
                new = fmt_anchors(tgt, cur_ann)
                doc.replace(odd[0][0] + 1, new)
                changes.append({"file": str(doc.path.relative_to(REPO)).replace("\\", "/"),
                                "subdomain": sub, "old_line": lines[odd[0][0]],
                                "new_line": new, "sr": "+".join(joinable),
                                "surface": "subso_anchors_nonstrict"})
                rep.add("csf_replaced", reg, f"{sub}/regs/{reg}.md subso@L{odd[0][0] + 1}",
                        f"{'+'.join(joinable)} (non-strict list): {cur_ids} -> {tgt}")
        elif joinable and list_idx and sorted(cur_ids) != sorted(tgt):
            new = fmt_anchors(tgt, cur_ann)
            doc.replace(list_idx[0] + 1, new)
            changes.append({"file": str(doc.path.relative_to(REPO)).replace("\\", "/"),
                            "subdomain": sub, "old_line": lines[list_idx[0]],
                            "new_line": new, "sr": "+".join(joinable), "surface": "subso_anchors"})
            rep.add("csf_replaced", reg, f"{sub}/regs/{reg}.md subso@L{list_idx[0] + 1}",
                    f"{'+'.join(joinable)}: {cur_ids} -> {tgt}")
        elif joinable and not list_idx and not odd and sorted(cur_ids) != sorted(tgt):
            rep.add("primary_list_kept_verbatim", reg, f"{sub}/regs/{reg}.md @L{i + 1}",
                    f"inline anchor list not mechanically editable: {ln.strip()[:80]}")
        # glosses are contextual prose (kept verbatim); independently of the list
        # branch, note gloss tokens that fall outside the uniformized set
        if joinable and odd and list_idx:
            gloss_tokens = []
            for _j, s in odd:
                gloss_tokens += [t for t in (a.rstrip() for a in RE_CSF_ANN.findall(s))]
            gloss_base = sorted({re.sub(r"\s*\(primary\)$", "", t) for t in gloss_tokens})
            stray = [t for t in gloss_base if t not in tgt]
            if stray:
                rep.add("gloss_stray_tokens", reg, f"{sub}/regs/{reg}.md @L{odd[0][0] + 1}",
                        f"gloss mentions outside uniformized set: {stray}")
        # PF 1.1 / AI RMF anchor blocks (dashboard axes only)
        for axis, label in AXES_BY_REG.get(reg, []):
            if not joinable:
                continue
            vals = union_axis(joinable, axis)
            vals_line = fmt_anchors(vals) if vals else "—."
            exists_at = axis_seen.get(label)
            if exists_at is not None:
                doc.replace(exists_at + 2, vals_line)
            else:
                first_after = list_idx[0] if list_idx else (odd[0][0] if odd else i)
                hdr = (f"**{label} anchors (from {sr_ref_short(joinable)} — dashboard "
                       f"`{DASH_REL[reg]}`, mechanical uniformization):**")
                doc.insert_block_after(first_after + 1, [hdr, vals_line])
                rep.add("axis_block_added", reg, f"{sub}/regs/{reg}.md",
                        f"{label} after L{first_after + 1}: {vals_line}")


def module_post_state(preview_lines, sub, reg):
    """Anchor state AFTER planned edits, for manifest recomputation."""
    lines = preview_lines
    so = {"csf": [], "pf": [], "airmf": []}
    for i, ln in enumerate(lines):
        if not RE_HDR.match(ln):
            continue
        srs, _li, _t, _o, _p, _ax = parse_anchors_block(lines, i)
        joinable = [s for s in srs if s in BY_SR]
        if joinable:
            so = {"csf": union_axis(joinable, "nist_csf"),
                  "pf": union_axis(joinable, "nist_pf"),
                  "airmf": union_axis(joinable, "nist_airmf")}
    reqs = {}
    for rq in parse_yaml_anchors(lines):
        rec = BY_SR.get(rq["sr"])
        rid = req_id_for(lines, rq["line_no"])
        if rec and rid:
            reqs[rid] = {"csf": rec["nist_csf"], "pf": rec.get("nist_pf", []),
                         "airmf": rec.get("nist_airmf", [])}
    return so, reqs


# ---------------------------------------------------------- ambiguity cards
def control_anchors_line(reg, sr_ids, prefix=""):
    if not sr_ids:
        return f"{prefix}**Control anchors:** CSF: — · PF 1.1: — · AI RMF: — " \
               f"(no consuming SR in dashboard mappings)"
    csf = union_axis(sr_ids, "nist_csf")
    pf = union_axis(sr_ids, "nist_pf")
    airmf = union_axis(sr_ids, "nist_airmf")
    return (f"{prefix}**Control anchors:** CSF: {', '.join(csf) or '—'} · "
            f"PF 1.1: {', '.join(pf) or '—'} · AI RMF: {', '.join(airmf) or '—'} · "
            f"from {sr_ref_short(sr_ids)} ({DASH_REL[reg]})")


def process_ambiguity(doc, sub, reg, clause_index, rep):
    lines = doc.lines
    touched = 0
    for i, ln in enumerate(lines):
        m = RE_CLAUSE.match(ln)
        if not m:
            continue
        sr_ids = clause_index.get((reg, m.group(1)), [])
        new = control_anchors_line(reg, sr_ids)
        if i + 1 < len(lines) and RE_CA_LINE.match(lines[i + 1]):
            if lines[i + 1] == new:
                continue
            doc.replace(i + 2, new)
        else:
            doc.insert_after(i + 1, new)
        touched += 1
        rep.add("ambiguity_anchors", reg, f"{sub}/regs/{reg}.ambiguity.md",
                f"{m.group(1)}: {len(sr_ids)} SR(s)")
    if touched and not any("aegis:control-anchors" in l for l in lines):
        marker = ("<!-- aegis:control-anchors: generated by scripts/uniformize_control_anchors.py "
                  "from baseline/MAPPINGS/sr_control_mappings; not part of the verbatim Part 4 body -->")
        for i in range(len(lines) - 1, -1, -1):
            if lines[i].startswith("<!-- aegis:purity"):
                doc.insert_after(i + 1, marker)
                break
        else:
            doc.insert_after(len(lines) - 1, marker)
    return touched


# ----------------------------------------------------------------- registry
def process_registry_csv(clause_index, rep):
    path = REPO / "baseline" / "registry.csv"
    raw = path.read_text(encoding="utf-8-sig").splitlines()
    header = next(csv.reader([raw[0]]))
    cols = ["nist_csf", "nist_pf", "nist_airmf"]
    i_reg = header.index("regulation")
    i_cid = header.index("clause_id")
    existing = [c for c in cols if c in header]
    out = [raw[0] + ("" if existing else "," + ",".join(cols))]
    n = 0
    for line in raw[1:]:
        if not line.strip():
            out.append(line)
            continue
        fields = next(csv.reader([line]))
        reg = REG_ALIASES.get(fields[i_reg], fields[i_reg])
        sr_ids = clause_index.get((reg, fields[i_cid]), [])
        vals = [", ".join(union_axis(sr_ids, a)) or "—"
                for a in ("nist_csf", "nist_pf", "nist_airmf")]
        if existing:  # idempotent update: strip our previously appended suffix
            old_suffix = "," + ",".join(_q(v) for v in fields[len(header) - 3:])
            base = line[: -len(old_suffix)] if line.endswith(old_suffix) else \
                ",".join(_q(v) for v in fields[: len(header) - 3])
        else:
            base = line
        out.append(base + "," + ",".join(_q(v) for v in vals))
        n += 1
    path.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
    rep.add("registry_csv", "ALL", "baseline/registry.csv", f"{n} data rows")
    return n


def _q(v):
    v = str(v)
    return f'"{v}"' if ("," in v or '"' in v) else v


def process_registry_md(clause_index, rep):
    path = REPO / "baseline" / "01_Ambiguity_Registry.md"
    doc = FileDoc(path)
    lines = doc.lines
    reg = None
    for i, ln in enumerate(lines):
        mh = re.match(r"^## (.+?) \(\d+ cards?\)", ln)
        if mh:
            reg = REG_ALIASES.get(mh.group(1).strip(), mh.group(1).strip())
            continue
        mc = re.match(r"^### ([A-Za-z0-9_\-]+) — ", ln)
        if not mc or reg not in REGS:
            continue
        sr_ids = clause_index.get((reg, mc.group(1)), [])
        new = control_anchors_line(reg, sr_ids, prefix="- ")
        # card block ends at the next --- / ###
        end = i + 1
        while end < len(lines) and not (lines[end].startswith("---") or lines[end].startswith("### ")):
            end += 1
        anchor_at = variant_at = None
        for j in range(i + 1, end):
            if lines[j].startswith("- **Card variant:**"):
                variant_at = j
            if RE_CA_LINE.match(lines[j]):
                anchor_at = j
                break
        if anchor_at:
            if lines[anchor_at] != new:
                doc.replace(anchor_at + 1, new)
                rep.add("registry_md", reg, mc.group(1), "updated")
        elif variant_at is not None:
            doc.insert_after(variant_at + 1, new)
            rep.add("registry_md", reg, mc.group(1), "added")
    doc.run()
    return rep.count("registry_md")


# ---------------------------------------------------------------- manifests
def subdomain_from_req_id(rid):
    parts = str(rid).split(".")
    if len(parts) >= 3:
        return f"D-{int(parts[0]):02d}.{parts[1]}"
    return None


def update_manifests(module_state, rep):
    for mf in sorted(DOMAINS.glob("D-*/D-*.manifest.json")):
        data = json.loads(mf.read_text(encoding="utf-8-sig"))
        dirty = False
        for reg in REGS:
            so_list = data.get("sub_objectives_by_regulation", {}).get(reg, [])
            rq_list = data.get("sub_requirements_by_regulation", {}).get(reg, [])
            for so in so_list:
                m = re.match(r"SO-(D-\d+\.\d+)\.", str(so.get("id", "")))
                st = module_state.get((m.group(1), reg)) if m else None
                if not st:
                    continue
                csf, pf, airmf = st["so"]["csf"], st["so"]["pf"], st["so"]["airmf"]
                if csf and sorted(so.get("csf_anchors", [])) != sorted(csf):
                    so["csf_anchors"] = csf
                    dirty = True
                if pf and so.get("pf_anchors") != pf:
                    so["pf_anchors"] = pf
                    dirty = True
                if airmf and so.get("airmf_anchors") != airmf:
                    so["airmf_anchors"] = airmf
                    dirty = True
            for rq in rq_list:
                rid = str(rq.get("req_id", ""))
                sub = subdomain_from_req_id(rid)
                st = module_state.get((sub, reg)) if sub else None
                vals = st["reqs"].get(rid) if st else None
                if not vals:
                    continue
                if sorted(rq.get("nist_csf", [])) != sorted(vals["csf"]):
                    rq["nist_csf"] = vals["csf"]
                    dirty = True
                if vals["pf"] and rq.get("nist_pf") != vals["pf"]:
                    rq["nist_pf"] = vals["pf"]
                    dirty = True
                if vals["airmf"] and rq.get("nist_airmf") != vals["airmf"]:
                    rq["nist_airmf"] = vals["airmf"]
                    dirty = True
            if not dirty:
                continue
            uni, pf_uni, airmf_uni = set(), set(), set()
            for so in so_list:
                uni |= set(so.get("csf_anchors", []))
                pf_uni |= set(so.get("pf_anchors", []))
                airmf_uni |= set(so.get("airmf_anchors", []))
            for rq in rq_list:
                uni |= set(rq.get("nist_csf", []))
                pf_uni |= set(rq.get("nist_pf", []))
                airmf_uni |= set(rq.get("nist_airmf", []))
            data.setdefault("applicable_nist_controls_by_regulation", {})[reg] = sorted(uni)
            if pf_uni:
                data.setdefault("applicable_pf_controls_by_regulation", {})[reg] = sorted(pf_uni)
            if airmf_uni:
                data.setdefault("applicable_airmf_controls_by_regulation", {})[reg] = sorted(airmf_uni)
        if dirty:
            mf.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n",
                          encoding="utf-8", newline="\n")
            rep.add("manifest", "ALL", str(mf.relative_to(REPO)).replace("\\", "/"),
                    "anchor indexes updated")


# -------------------------------------------------------------------- main
def main():
    global BY_SR
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true", help="write changes (default: dry-run check)")
    args = ap.parse_args()
    BY_SR, clause_index = load_crosswalk()
    rep = Report()
    changes = []
    module_state = {}

    for path in sorted(DOMAINS.glob("D-*/*/regs/*.md")):
        if path.name.endswith(".ambiguity.md"):
            continue
        reg = path.stem
        if reg not in REGS:
            continue
        sub = path.parent.parent.name
        doc = FileDoc(path)
        process_regs_module(doc, sub, reg, rep, changes)
        so, reqs = module_post_state(doc.preview(), sub, reg)
        module_state[(sub, reg)] = {"so": so, "reqs": reqs}
        if args.apply:
            doc.run()
        else:
            doc.ops.clear()

    for path in sorted(DOMAINS.glob("D-*/*/regs/*.ambiguity.md")):
        reg = path.stem.replace(".ambiguity", "")
        if reg not in REGS:
            continue
        sub = path.parent.parent.name
        doc = FileDoc(path)
        process_ambiguity(doc, sub, reg, clause_index, rep)
        if args.apply:
            doc.run()
        else:
            doc.ops.clear()

    if args.apply:
        process_registry_csv(clause_index, rep)
        process_registry_md(clause_index, rep)
        update_manifests(module_state, rep)

    summarize(rep, changes, args.apply)


def summarize(rep, changes, applied):
    mode = "APPLIED" if applied else "CHECK (dry run)"
    print("=" * 72)
    print(f"CONTROL ANCHOR UNIFORMIZATION — {mode}")
    print("=" * 72)
    for kind in sorted({r["kind"] for r in rep.rows}):
        print(f"  {kind}: {rep.count(kind)}")
    print(f"\nCSF contradictions resolved (dashboard wins): {rep.count('csf_replaced')}")
    print(f"Baseline-only SRs (left untouched): {rep.count('baseline_sr_no_dashboard')}")
    print(f"Non-strict primary lists matching dashboard (kept verbatim): "
          f"{rep.count('primary_list_verbatim_ok')}")
    print(f"Gloss lines with stray tokens (informational): {rep.count('gloss_stray_tokens')}")
    for r in rep.rows:
        if r["kind"] in ("primary_list_kept_verbatim", "baseline_sr_no_dashboard"):
            print(f"  - [{r['kind']}] {r['where']}: {r['detail'][:130]}")
    if not applied:
        print("\nDry run: nothing written. Re-run with --apply to write changes.")
        return
    CHANGES_JSON.write_text(json.dumps(
        {"policy": "dashboard-wins uniformization; applied by scripts/uniformize_control_anchors.py",
         "applied_on": date.today().isoformat(), "changes": changes},
        ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    write_ledger(rep, changes)
    print(f"\nsidecar: {CHANGES_JSON}")
    print(f"ledger:  {LEDGER}")


def write_ledger(rep, changes):
    L = ["# Control anchor uniformization ledger (dashboard correspondence)", ""]
    L.append(f"- Date: {date.today().isoformat()}")
    L.append("- Reference: `baseline/MAPPINGS/sr_control_mappings/<REG>.json` — extracted from the")
    L.append("  per-regulation dashboards in `methodology_compact/00_METHODOLOGY/00_VISUALISATIONS/`")
    L.append("  (read-only; `Case_*`, `data`, `UNIFIED`, `tests` ignored).")
    L.append("- Policy: for the same sr_id / clause, the dashboard control set wins (user decision).")
    L.append("  Baseline-only SRs are left untouched and listed below. Ids unresolvable against")
    L.append("  `baseline/CONTROLS` are never propagated. Primary anchor lists that are not in")
    L.append("  strict machine-readable format are kept verbatim and flagged below.")
    L.append("  Italic gloss lines after a list are contextual prose (kept verbatim); when a gloss")
    L.append("  names a token outside the uniformized set it is listed as informational.")
    L.append("- Axes: PF 1.1 only where the GDPR dashboard publishes it; AI RMF only where the")
    L.append("  AI_Act dashboard publishes it (no overlay supplementation).")
    L.append("- Machine-readable change list: `_uniformization_changes.json` (consumed by")
    L.append("  `scripts/verify_no_loss.py` as documented transformations).")
    L.append("")
    L.append("| Kind | Count |")
    L.append("|---|---|")
    for kind in sorted({r["kind"] for r in rep.rows}):
        L.append(f"| {kind} | {rep.count(kind)} |")
    L.append("")
    L.append("## CSF set replacements (baseline -> dashboard)")
    L.append("")
    L.append("| File | SR | Old | New |")
    L.append("|---|---|---|---|")
    for c in changes:
        L.append(f"| `{c['file']}` | {c['sr']} | `{c['old_line'].strip()[:90]}` "
                 f"| `{c['new_line'].strip()[:90]}` |")
    L.append("")
    L.append("## Review flags")
    L.append("")
    flagged = [r for r in rep.rows
               if r["kind"] in ("primary_list_kept_verbatim", "baseline_sr_no_dashboard",
                                "primary_list_verbatim_ok")]
    if flagged:
        for r in flagged:
            L.append(f"- **[{r['kind']}]** `{r['where']}` — {r['detail']}")
    else:
        L.append("- none")
    L.append("")
    stray = [r for r in rep.rows if r["kind"] == "gloss_stray_tokens"]
    if stray:
        L.append("## Informational: gloss lines mentioning tokens outside the uniformized set")
        L.append("")
        for r in stray:
            L.append(f"- `{r['where']}` — {r['detail']}")
        L.append("")
    LEDGER.write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
