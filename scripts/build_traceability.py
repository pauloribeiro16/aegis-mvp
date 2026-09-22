#!/usr/bin/env python3
"""
build_traceability.py
=====================
Builds the complete baseline traceability chain for every regulation published
in the per-regulation dashboards (GDPR, CRA, NIS2, DORA, AI_Act):

    regulation -> article(s) -> ambiguity clause(s) -> baseline goal (SO-D-XX.Y.HL; legacy HSO)
    -> SO-<REG>-NNN -> Sub-SO (SO-D-XX.Y.<REG>) -> requirement (req_id + SR)
    -> NIST CSF 2.0 | NIST PF 1.1 | NIST AI RMF

Sources (all read from the aegis-mvp baseline, already uniformized with the
dashboards by scripts/uniformize_control_anchors.py):
  - D-*/D-XX.Y/objective.md              baseline goal id (SO-D-XX.Y.HL; legacy HSO)
  - D-*/D-XX.Y/regs/<REG>.md             Sub-SO YAML (id, inherits_from, source_SR)
                                         + requirement YAML (req_id, title,
                                         source_sr, nist_csf / nist_pf / nist_airmf)
                                         + participant table (SO-<REG> summary)
  - D-*/D-XX.Y/_index.md                 canonical sub-domain name
  - baseline/MAPPINGS/sr_control_mappings/<REG>.json
                                         SR records: source_clauses (clause_id +
                                         article_ref), linked_objectives, controls

Outputs:
  - baseline/MAPPINGS/traceability/<REG>.md   readable chain, grouped by sub-domain
  - baseline/MAPPINGS/traceability/traceability.csv   one row per
    (sub-domain, regulation, requirement) with semicolon-joined articles/clauses
  - baseline/MAPPINGS/traceability/index.md   how-to-read + coverage counts

Baseline-only by design: per-company adjusted goals (AG-D-XX.Y-NNN) are
recorded in each Phase 1 run (templates/phase1_output.md §4.1), never here.

Usage:
  python scripts/build_traceability.py
"""

import csv
import json
import re
import sys
from collections import OrderedDict
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DOMAINS = REPO / "baseline" / "domains"
XWALK = REPO / "baseline" / "MAPPINGS" / "sr_control_mappings"
OUT = REPO / "baseline" / "MAPPINGS" / "traceability"
REGS = ["GDPR", "CRA", "NIS2", "DORA", "AI_Act"]

RE_FENCE = re.compile(r"^```")
RE_REQ = re.compile(r"^- req_id:\s*([0-9.]+)")
RE_KV = re.compile(r"^\s*-?\s*([A-Za-z_]+):\s*(.*)$")
RE_LIST = re.compile(r"^\s*([A-Za-z_]+):\s*\[([^\]]*)\]\s*$")
RE_SRTOK = re.compile(r"SR-[A-Z0-9_]+-\d+")
RE_SUBSO = re.compile(r"^id:\s*(SO-D-\d+\.\d+\.[A-Za-z_0-9]+)")
RE_INHERIT = re.compile(r"^inherits_from:\s*(SO-[A-Za-z_0-9.-]+)")
RE_SRC_SR = re.compile(r"source_[sS][rR]:\s*(SR-[A-Z0-9_]+-\d+)")
RE_HSO = re.compile(r"^id:\s*(SO-D-\d+\.\d+\.HL)")
RE_TITLE = re.compile(r'^\s*title:\s*"(.*)"\s*$')
RE_PART_ROW = re.compile(r"^\|\s*" + r"(GDPR|CRA|NIS2|DORA|AI_Act)" +
                         r"\s*\|\s*(SO-[A-Za-z_0-9.-]+)\s*\|\s*(.*?)\s*\|")
RE_INDEX_NAME = re.compile(r"^# (D-\d+\.\d+) — (.+)$")


def parse_module_module(path, reg):
    """(subso, [reqs]) parsed from one regs/<REG>.md."""
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    subso, reqs = {}, []
    in_fence, cur_req, so_summary = False, None, ""
    for ln in lines:
        if RE_FENCE.match(ln.strip()):
            in_fence = not in_fence
            if not in_fence:
                cur_req = None
            continue
        m = RE_PART_ROW.match(ln)
        if m and m.group(1) == reg:
            so_summary = m.group(3).strip()
        if in_fence:
            m = RE_SUBSO.match(ln)
            if m and not reqs:
                subso["id"] = m.group(1)
            m = RE_INHERIT.match(ln)
            if m:
                subso["inherits_from"] = m.group(1)
            m = RE_SRC_SR.search(ln)
            if m and not cur_req:
                subso["source_sr"] = m.group(1)
            m = RE_REQ.match(ln)
            if m:
                cur_req = {"req_id": m.group(1), "sr": None, "title": "",
                           "nist_csf": [], "nist_pf": [], "nist_airmf": []}
                reqs.append(cur_req)
                continue
            if cur_req is not None:
                m = RE_TITLE.match(ln)
                if m:
                    cur_req["title"] = m.group(1).strip()
                m = RE_SRC_SR.search(ln)
                if m:
                    cur_req["sr"] = m.group(1)
                m = RE_LIST.match(ln)
                if m and m.group(1) in ("nist_csf", "nist_pf", "nist_airmf"):
                    cur_req[m.group(1)] = [t.strip() for t in m.group(2).split(",") if t.strip()]
    return subso, reqs, so_summary


def parse_hso(obj_path):
    m = re.search(r"^id:\s*(SO-D-\d+\.\d+\.HL)", obj_path.read_text(encoding="utf-8-sig"), re.M)
    return m.group(1) if m else None


def subdomain_name(idx_path):
    m = RE_INDEX_NAME.match(idx_path.read_text(encoding="utf-8-sig").splitlines()[0])
    return m.group(2) if m else ""


def main():
    xw = {}
    for reg in REGS:
        doc = json.loads((XWALK / f"{reg}.json").read_text(encoding="utf-8-sig"))
        for s in doc["srs"]:
            xw[s["sr_id"]] = s
    OUT.mkdir(parents=True, exist_ok=True)

    csv_rows = []
    index_lines = ["# Traceability index — regulation -> article -> objective -> "
                   "requirement -> control", ""]
    index_lines.append(f"- Generated: {date.today().isoformat()} by "
                       "`scripts/build_traceability.py` (re-run after any "
                       "`uniformize_control_anchors.py --apply`).")
    index_lines.append("- Chain per row: regulation -> article(s) -> ambiguity clause(s) -> "
                       "Baseline goals (HSO `SO-D-XX.Y.HL` -> `SO-<REG>-NNN` -> Sub-SO `SO-D-XX.Y.<REG>`, legacy) -> "
                       "requirement (`req_id` + `SR`) -> CSF 2.0 | PF 1.1 | AI RMF.")
    index_lines.append("- Baseline-only: per-company adjusted goals (`AG-D-XX.Y-NNN`) are "
                       "recorded in each Phase 1 output (`templates/phase1_output.md` §4.1).")
    index_lines.append("- Control values are the module YAML sets, guaranteed equal to the "
                       "dashboard crosswalk (check H of `scripts/verify_no_loss.py`).")
    index_lines.append("")
    index_lines.append("| Regulation | Sub-domains | Requirements | Articles | Clauses | "
                       "Reqs with PF 1.1 | Reqs with AI RMF |")
    index_lines.append("|---|---|---|---|---|---|---|")

    for reg in REGS:
        md = [f"# Traceability — {reg}", ""]
        md.append("> Chain: regulation -> article(s) -> ambiguity clause(s) -> baseline goal -> "
                  f"SO-{reg} -> Sub-SO -> requirement -> controls. Generated from the "
                  "modular corpus + `sr_control_mappings` (dashboard-uniformized).")
        md.append("")
        n_req = n_pf = n_ai = n_art_set = n_cls_set = 0
        subs = 0
        for obj_path in sorted(DOMAINS.glob(f"D-*/*/objective.md")):
            sub_dir = obj_path.parent
            sub = sub_dir.name
            reg_path = sub_dir / "regs" / f"{reg}.md"
            if not reg_path.exists():
                continue
            subs += 1
            hso = parse_hso(obj_path)
            subso, reqs, so_summary = parse_module_module(reg_path, reg)
            name = subdomain_name(sub_dir / "_index.md")
            md.append(f"## {sub} — {name}")
            md.append("")
            md.append("| Requisito | SR | Artigos | Cláusulas | "
                      "Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |")
            md.append("|---|---|---|---|---|---|---|---|")

            def req_key(r):
                return [int(p) for p in r["req_id"].split(".")]

            for r in sorted(reqs, key=req_key):
                rec = xw.get(r["sr"]) or {}
                arts, cls = [], []
                for c in rec.get("source_clauses", []):
                    ref, cid = c.get("article_ref", ""), c.get("clause_id", "")
                    if ref and ref not in arts:
                        arts.append(ref)
                    if cid and cid not in cls:
                        cls.append(cid)
                so_reg = subso.get("inherits_from") or ", ".join(rec.get("linked_objectives", []))
                obj_cell = " -> ".join(x for x in (hso, so_reg, subso.get("id")) if x)
                title = r["title"] or rec.get("title", "")
                md.append("| {rq} | `{sr}` | {a} | {c} | {o} | {csf} | {pf} | {ai} |".format(
                    rq=f"{r['req_id']} — {title}" if title else r["req_id"],
                    sr=r["sr"] or "—",
                    a="; ".join(arts) or "—",
                    c=", ".join(cls) or "—",
                    o=obj_cell or "—",
                    csf=", ".join(r["nist_csf"]) or "—",
                    pf=", ".join(r["nist_pf"]) or "—",
                    ai=", ".join(r["nist_airmf"]) or "—"))
                n_req += 1
                n_pf += 1 if r["nist_pf"] else 0
                n_ai += 1 if r["nist_airmf"] else 0
                if arts:
                    n_art_set += 1
                if cls:
                    n_cls_set += 1
                csv_rows.append(OrderedDict([
                    ("regulation", reg),
                    ("sub_domain", sub),
                    ("sub_domain_name", name),
                    ("hso_id", hso or ""),
                    ("so_reg_id", so_reg or ""),
                    ("so_reg_summary", so_summary),
                    ("subso_id", subso.get("id", "")),
                    ("req_id", r["req_id"]),
                    ("req_title", title),
                    ("sr_id", r["sr"] or ""),
                    ("sr_title", rec.get("title", "")),
                    ("articles", "; ".join(arts)),
                    ("ambiguity_clauses", ", ".join(cls)),
                    ("nist_csf", ", ".join(r["nist_csf"])),
                    ("nist_pf", ", ".join(r["nist_pf"])),
                    ("nist_airmf", ", ".join(r["nist_airmf"])),
                ]))
            md.append("")
        (OUT / f"{reg}.md").write_text("\n".join(md) + "\n", encoding="utf-8", newline="\n")
        index_lines.append(f"| {reg} | {subs} | {n_req} | {n_art_set} | {n_cls_set} "
                           f"| {n_pf} | {n_ai} |")
        print(f"{reg}: {subs} sub-domains, {n_req} requirements "
              f"(PF {n_pf}, AI RMF {n_ai}) -> {OUT / (reg + '.md')}")

    with (OUT / "traceability.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(csv_rows[0].keys()))
        w.writeheader()
        w.writerows(csv_rows)
    (OUT / "index.md").write_text("\n".join(index_lines) + "\n",
                                  encoding="utf-8", newline="\n")
    print(f"csv: {OUT / 'traceability.csv'} ({len(csv_rows)} rows)")
    print(f"index: {OUT / 'index.md'}")

    # consistency: every req SR must exist in the crosswalk
    missing = [r["sr_id"] for r in csv_rows if not r["sr_id"]
               or r["sr_id"] not in xw]
    if missing:
        print(f"WARNING: {len(missing)} requirement SR ids not in crosswalk: {missing[:5]}")
        sys.exit(1)
    print("consistency: all requirement SR ids resolve in the crosswalk (100%)")


if __name__ == "__main__":
    main()
