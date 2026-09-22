#!/usr/bin/env python3
"""
extract_dashboard_mappings.py
=============================
Extracts the security-requirement <-> NIST control mappings embedded in the
per-regulation dashboards of the frozen methodology corpus and materializes
them as modular, machine-readable JSON + a human-readable index INSIDE the
aegis-mvp baseline. The dashboards themselves are READ-ONLY (SPEC §10:
Methodology_compact is provenance, never written to).

Source (read-only):
  <corpus>/00_METHODOLOGY/00_VISUALISATIONS/{GDPR,CRA,NIS2,DORA,AI_Act}/
      *_Dashboard.html   — each embeds `<script id="<id>-data"
      type="application/json">` whose `srs[]` records carry:
      sr_id, source_clauses[{clause_id, article_ref}], nist_csf_mapping,
      nist_pf_mapping (GDPR only), nist_airmf_mapping (AI_Act only).

  Deliberately IGNORED (user instruction): Case_*/ , data/ , UNIFIED/ , tests/
  subfolders and the QNRCS dashboard (outside the 5-regulation MVP scope).

Outputs (written here, into aegis-mvp):
  baseline/MAPPINGS/sr_control_mappings/<REG>.json
      Per regulation: meta (provenance, normalization accounting) + srs[] with
      normalized anchor sets (nist_csf / nist_pf / nist_airmf) AND the full
      verbatim source record (`source_record`) so no dashboard information is
      lost or summarized.
  baseline/MAPPINGS/sr_control_mappings/index.md
      Readable complete mapping: SR -> articles -> clauses -> CSF | PF | AI RMF.

ID normalization (documented, mirrors scripts/normalize_csf_anchors.py):
  - CSF 1.1-style single-digit suffixes are padded to the CSF 2.0 two-digit
    form (PR.DS-1 -> PR.DS-01).
  - The documented phantom map is applied (PR.IP-07 -> ID.IM-03, ... and the
    internal 4x3-matrix cell PR.DS-12 -> ID.AM-08); every replacement is
    recorded per SR (`replaced_tokens`).
  - AI RMF ids are canonicalized to the referential filename form
    (GOVERN-1.1, MAP-5.1 — hyphenated, no zero padding); PF ids already match
    (PR.DS-P1).
  - Every normalized id is validated against baseline/CONTROLS referentials.
    Ids that still do not resolve are NEVER propagated: they are excluded from
    the anchor sets and reported per SR under `unresolved`.

Usage:
  python scripts/extract_dashboard_mappings.py [--dashboards-root <path>] [--out <path>]
"""

import argparse
import json
import re
import sys
from collections import OrderedDict
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from normalize_csf_anchors import PHANTOM_MAP, RE_PRDS12, prds12_replacement

REPO = Path(__file__).resolve().parent.parent
DEFAULT_DASHBOARDS = (REPO.parent / "methodology_compact" / "00_METHODOLOGY"
                      / "00_VISUALISATIONS")
DEFAULT_OUT = REPO / "baseline" / "MAPPINGS" / "sr_control_mappings"

DASHBOARDS = OrderedDict([
    ("GDPR",   ("gdpr",  "GDPR/GDPR_Dashboard.html")),
    ("CRA",    ("cra",   "CRA/CRA_Dashboard.html")),
    ("NIS2",   ("nis2",  "NIS2/NIS2_Dashboard.html")),
    ("DORA",   ("dora",  "DORA/DORA_Dashboard.html")),
    ("AI_Act", ("aiact", "AI_Act/AI_Act_Dashboard.html")),
])

RE_EMBEDDED_JSON = re.compile(
    r'<script id="{sid}-data" type="application/json">(.*?)</script>'.format(sid=r"([a-z0-9-]+)"),
    re.S)

RE_CSF_TOKEN = re.compile(r"^(GV|ID|PR|DE|RS|RC)\.([A-Z]{2})-(\d{1,2})$")
RE_AIRMF_TOKEN = re.compile(r"^(GOVERN|MAP|MEASURE|MANAGE)[- ](\d{1,2})\.(\d{1,2})$")
RE_PF_TOKEN = re.compile(r"^(ID|GV|CT|CM|PR)\.([A-Z]{2})-P(\d+)$")


def load_referentials():
    """Build the three id universes from the CONTROLS referentials (R2)."""
    csf_ref = json.loads((REPO / "baseline/CONTROLS/NIST_CSF_2.0/CSF_2.0.json")
                         .read_text(encoding="utf-8-sig"))
    csf_ids = set()
    for sub in csf_ref["subcategories"]:
        csf_ids.add(sub if isinstance(sub, str) else sub.get("id"))
    airmf_ids, pf_ids = set(), set()
    ctrl = REPO / "baseline" / "CONTROLS"
    for p in (ctrl / "NIST_AI_RMF").rglob("*.json"):
        airmf_ids.add(p.stem)
    for p in (ctrl / "NIST_PF").rglob("*.json"):
        pf_ids.add(p.stem)
    return csf_ids, airmf_ids, pf_ids


def norm_csf(raw):
    """CSF token -> canonical 2.0 form (+ replacement note) or None."""
    tok = raw.strip().rstrip(".,")
    m = RE_CSF_TOKEN.match(tok)
    if not m:
        return None, f"not a CSF token: {raw!r}"
    fam, cat, num = m.group(1), m.group(2), f"{int(m.group(3)):02d}"
    canon = f"{fam}.{cat}-{num}"
    note = None
    if canon in PHANTOM_MAP:
        new, why = PHANTOM_MAP[canon]
        note = f"{canon} -> {new} ({why})"
        canon = new
    elif RE_PRDS12.match(canon):
        new = prds12_replacement(Path("regs/DORA.md"))  # default policy: ID.AM-08
        note = f"{canon} -> {new} (internal 4x3 matrix cell; data-management policy)"
        canon = new
    return canon, note


def norm_airmf(raw):
    tok = raw.strip().rstrip(".,")
    m = RE_AIRMF_TOKEN.match(tok)
    if not m:
        return None, f"not an AI RMF token: {raw!r}"
    return f"{m.group(1)}-{int(m.group(2))}.{int(m.group(3))}", None


def norm_pf(raw):
    tok = raw.strip().rstrip(".,")
    m = RE_PF_TOKEN.match(tok)
    if not m:
        return None, f"not a PF token: {raw!r}"
    return f"{m.group(1)}.{m.group(2)}-P{int(m.group(3))}", None


def normalize_mapping(entries, normalizer, universe):
    """[(id, title)] -> (ordered canonical ids, replacements, unresolved)."""
    out, repl, unres, seen = [], {}, [], set()
    for e in entries or []:
        canon, note = normalizer(e.get("id", ""))
        if canon is None:
            unres.append({"raw": e.get("id"), "reason": note})
            continue
        if canon not in universe:
            unres.append({"raw": e.get("id"), "reason": f"not in referential (canon {canon})"})
            continue
        if note:
            repl[e.get("id")] = note
        if canon not in seen:
            seen.add(canon)
            out.append(canon)
    return out, repl, unres


def split_markers(entries):
    """Dashboard 'UNMAPPED_X' placeholder entries are deliberate 'no mapping,
    justified' records — captured as markers, never treated as control ids."""
    markers, rest = [], []
    for e in entries or []:
        if str(e.get("id", "")).startswith("UNMAPPED"):
            markers.append({"id": e.get("id"), "title": e.get("title", ""),
                            "justification": e.get("unmapped_pf_justification",
                                                   e.get("unmapped_csf_justification",
                                                         e.get("unmapped_airmf_justification", "")))})
        else:
            rest.append(e)
    return markers, rest


def extract_one(reg, sid, rel_html, dash_root, universes):
    html_path = dash_root / rel_html
    html = html_path.read_text(encoding="utf-8-sig")
    m = RE_EMBEDDED_JSON.search(html)
    if not m or m.group(1) != sid:
        raise SystemExit(f"{reg}: embedded JSON script '{sid}-data' not found in {html_path}")
    data = json.loads(m.group(2))
    csf_uni, airmf_uni, pf_uni = universes

    srs_out, totals = [], {"replaced": 0, "unresolved": 0}
    for rec in data.get("srs", []):
        mk_csf, csf_e = split_markers(rec.get("nist_csf_mapping"))
        mk_pf, pf_e = split_markers(rec.get("nist_pf_mapping"))
        mk_airmf, airmf_e = split_markers(rec.get("nist_airmf_mapping"))
        csf, r1, u1 = normalize_mapping(csf_e, norm_csf, csf_uni)
        pf, r2, u2 = normalize_mapping(pf_e, norm_pf, pf_uni)
        airmf, r3, u3 = normalize_mapping(airmf_e, norm_airmf, airmf_uni)
        replaced, unresolved = {}, []
        for d in (r1, r2, r3):
            replaced.update(d)
        for u in (u1, u2, u3):
            unresolved.extend(u)
        markers = mk_csf + mk_pf + mk_airmf
        totals["replaced"] += len(replaced)
        totals["unresolved"] += len(unresolved)
        srs_out.append(OrderedDict([
            ("sr_id", rec.get("sr_id")),
            ("title", rec.get("title")),
            ("sub_domain", rec.get("sub_domain", [])),
            ("linked_objectives", rec.get("linked_objectives", [])),
            ("source_clauses", rec.get("source_clauses", [])),
            ("nist_csf", csf),
            ("nist_pf", pf),
            ("nist_airmf", airmf),
            ("unmapped_markers", markers),
            ("replaced_tokens", replaced),
            ("unresolved", unresolved),
            ("source_record", rec),  # verbatim dashboard record (no loss)
        ]))
    srs_out.sort(key=lambda s: s["sr_id"])

    doc = OrderedDict([
        ("meta", OrderedDict([
            ("regulation", reg),
            ("source_dashboard", f"methodology_compact/00_METHODOLOGY/00_VISUALISATIONS/{rel_html}"),
            ("extracted_by", "scripts/extract_dashboard_mappings.py"),
            ("extracted_on", date.today().isoformat()),
            ("sr_count", len(srs_out)),
            ("axes", {"nist_csf": True,
                      "nist_pf": reg == "GDPR",
                      "nist_airmf": reg == "AI_Act"}),
            ("id_normalization", {"replaced_tokens": totals["replaced"],
                                  "unresolved_excluded": totals["unresolved"],
                                  "policy": "scripts/normalize_csf_anchors.py phantom map + "
                                            "CSF 1.1->2.0 suffix padding; unresolved ids are "
                                            "excluded from anchor sets and reported per SR"}),
            ("ignored_source_folders",
             ["Case_01", "Case_02", "Case_03", "data", "UNIFIED", "tests", "QNRCS"]),
        ])),
        ("srs", srs_out),
    ])
    return doc


def write_index(docs, out_dir):
    lines = [
        "# SR control mappings — complete index (from per-regulation dashboards)",
        "",
        "> Complete, verbatim-provenance mapping of every dashboard security requirement",
        "> to NIST CSF 2.0 / NIST PF 1.1 / NIST AI RMF controls. Machine-readable store:",
        "> `sr_control_mappings/<REG>.json` (each SR keeps its full `source_record`).",
        "> Dashboards are read-only provenance (SPEC §10); PF axis exists only for GDPR,",
        "> AI RMF axis only for AI_Act (dashboard coverage, per uniformization decision).",
        "",
    ]
    for reg, doc in docs.items():
        lines.append(f"## {reg} — {doc['meta']['sr_count']} SRs")
        lines.append("")
        lines.append("| SR | Sub-domains | Articles / clauses | CSF 2.0 | PF 1.1 | AI RMF |")
        lines.append("|---|---|---|---|---|---|")
        for s in doc["srs"]:
            arts, cls = [], []
            for c in s["source_clauses"]:
                ref = c.get("article_ref", "")
                if ref and ref not in arts:
                    arts.append(ref)
                cid = c.get("clause_id", "")
                if cid and cid not in cls:
                    cls.append(cid)
            cell = ("; ".join(arts) if arts else "—") + " <br> " + \
                   (", ".join(cls) if cls else "—")
            lines.append("| `{sr}` | {sd} | {a} | {c} | {p} | {m} |".format(
                sr=s["sr_id"],
                sd=", ".join(s["sub_domain"]) or "—",
                a=cell.replace("|", "\\|"),
                c=", ".join(s["nist_csf"]) or "—",
                p=", ".join(s["nist_pf"]) or "—",
                m=", ".join(s["nist_airmf"]) or "—"))
        lines.append("")
    (out_dir / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dashboards-root", default=str(DEFAULT_DASHBOARDS))
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    args = ap.parse_args()
    dash_root, out_dir = Path(args.dashboards_root), Path(args.out)

    universes = load_referentials()
    out_dir.mkdir(parents=True, exist_ok=True)
    docs = OrderedDict()
    for reg, (sid, rel) in DASHBOARDS.items():
        doc = extract_one(reg, sid, rel, dash_root, universes)
        (out_dir / f"{reg}.json").write_text(
            json.dumps(doc, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8", newline="\n")
        docs[reg] = doc
        m = doc["meta"]
        print(f"{reg}: {m['sr_count']} SRs -> {out_dir / (reg + '.json')} "
              f"(replaced {m['id_normalization']['replaced_tokens']}, "
              f"unresolved {m['id_normalization']['unresolved_excluded']})")
    write_index(docs, out_dir)
    print(f"index: {out_dir / 'index.md'}")


if __name__ == "__main__":
    main()
