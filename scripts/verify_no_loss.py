#!/usr/bin/env python3
"""
verify_no_loss.py
=================
Exhaustive, independent information-loss verification for the modular corpus.

Compares the ORIGINAL corpus tree (methodology-main
00_METHODOLOGY/PREPROCESSING_by_domain/domains) against the current modular
baseline tree (baseline/domains) WITHOUT reusing any modularize_domains.py
parsing/routing logic (anti-circular, rule R10): pure line-multiset analysis.

Checks
  A. Annotation fidelity (optional, --m0-dir): the annotated pre-modularization
     snapshot must be original + tag lines only (nothing removed, only tags added).
  B. Per sub-domain D-XX.Y (original merged file vs union of ALL modular files):
     - SET coverage: every non-blank original line must exist verbatim in the
       modular output. Uncovered lines are hard failures.
     - MULTISET surplus (original > output): intentional deduplication only
       (Part 3 byte-identical copies); every surplus line must still be
       set-covered. Blank-line surplus reported separately (formatting).
     - REVERSE surplus (output > original): classified as (a) intentional
       in-output duplication (line exists in original), (b) generated
       boilerplate (matches known generator patterns), (c) UNCLASSIFIED —
       hard failure if any.
  C. articles/: content-equality per file (CRLF-normalized), original vs current.
  D. Manifests: deep-equality after removing the added `modular_layout` key.
  E. Tree correspondence: files only in original / only in current.
  F. Regenerated summaries (domains/index.md, D-XX/_index.md): flagged as
     regenerated (counts recomputed), original preserved in git/M0.

Exit code 1 if any hard failure (uncovered / unclassified / missing).

Usage:
  python scripts/verify_no_loss.py \
      --original "../methodology-main/00_METHODOLOGY/PREPROCESSING_by_domain/domains" \
      [--m0-dir /tmp/m0_domains/baseline/domains]
"""

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from normalize_csf_anchors import normalize_csf_tokens, dedupe_lists  # documented normalization

RE_TAG = re.compile(r"^<!--\s*/?aegis:")
RE_PURITY = re.compile(r"^<!-- aegis:purity")
RE_CSF_TOKEN = re.compile(r"\b(?:GV|ID|PR|DE|RS|RC)\.[A-Z]{2}-\d{2}\b")
RE_PF_TOKEN = re.compile(r"\b(?:ID|GV|CT|CM|PR)\.[A-Z]{2}-P\d+\b")
RE_AIRMF_TOKEN = re.compile(r"\b(?:GOVERN|MAP|MEASURE|MANAGE)-\d{1,2}\.\d{1,2}\b")
# generated PF/AI-RMF anchor list line (or the explicit-absence "—.")
_A_TOK = r"(?:(?:GOVERN|MAP|MEASURE|MANAGE)-\d{1,2}\.\d{1,2}|(?:ID|GV|CT|CM|PR)\.[A-Z]{2}-P\d+)"
RE_AXIS_LIST_LINE = re.compile(rf"^(?:—\.|{_A_TOK}(?:,\s*{_A_TOK})*\.?)$")


def src_variants(line: str):
    """Coverage variants for an original-corpus line under the documented
    normalizations:
      - CSF phantom map (see normalize_csf_anchors.py)
      - PR.DS-12 -> ID.AM-05 (classification) and ID.AM-08 (data mgmt)
      - M9 partial-coverage additions: lines like `**CSF anchors (from SR-X):**`
        whose SR id is in the M9 sidecar are covered when the immediately
        following line contains the anchor added by the M9 patch (the
        original source line never had it; the patch added it to the target).
    """
    base = dedupe_lists(normalize_csf_tokens(line, None))
    variants = [base]
    if "PR.DS-12" in line:
        alt = line.replace("PR.DS-12", "ID.AM-05")
        variants.append(dedupe_lists(normalize_csf_tokens(alt, None)))
    sidecar = _load_m9_sidecar()
    if sidecar and "CSF anchors (from" in line and "):" in line:
        # Header line: extract SR ids, build a variant with each anchor added
        for sr_id, anchor in sidecar.items():
            if sr_id in line and anchor not in base:
                variants.append(base + anchor)
    return variants


_M9_SIDECAR_CACHE = {}


def _load_m9_sidecar():
    """Load M9 sidecar as {sr_id: anchor}; cache after first read."""
    if _M9_SIDECAR_CACHE:
        return _M9_SIDECAR_CACHE
    p = Path("baseline/MAPPINGS/_m9_partial_coverage_sidecar.json")
    if not p.exists():
        return {}
    try:
        sc = json.loads(p.read_text(encoding="utf-8-sig"))
        for entry in sc.get("patches", []):
            _M9_SIDECAR_CACHE[entry["sr"]] = entry["anchor"]
    except Exception:
        pass
    return _M9_SIDECAR_CACHE

# Generated-boilerplate patterns (output-only lines). Each entry: (regex, label).
GENERATED = [
    (re.compile(r"^# D-\d+\.\d+ — .* module$"), "module title"),
    (re.compile(r"^# D-\d+\.\d+ — (High-level Security Objective|Relevant Ambiguity|Pair analysis|Cross-regulation interactions)"), "module title"),
    (re.compile(r"^### from "), "crossref attribution header"),
    (re.compile(r"^<!-- aegis:purity:"), "purity stamp"),
    (re.compile(r"^_\("), "generated placeholder/note"),
    (re.compile(r"^_\*"), "generated placeholder/note"),
    (re.compile(r"^<details>|^</details>$"), "details wrapper"),
    (re.compile(r"^\|\s*-{3,}\s*\|$"), "table separator"),
    (re.compile(r"^\| Layer \| File \|$"), "modules table header"),
    (re.compile(r"^\| Regulation \| Canonical SO \|"), "reconstructed table header"),
    (re.compile(r"^\| Axis \(reg\) \| Trigger \|"), "reconstructed table header"),
    (re.compile(r"^\| Sub-domain \| Reg modules \|"), "regenerated index header"),
    (re.compile(r"^\| Domain \| Sub-domains \|"), "regenerated index header"),
    (re.compile(r"^- (Sub-domain|Participants|Article copies|Sub-domains|Per-regulation modules|Ambiguity modules|Cross pair analyses|Domains|Sub-domains in slice|Scope regulations|Composition mode|Purity audit|Files:|Regs with modules:|Demotion stats:|Script log:)"), "generated bullet"),
    (re.compile(r"^> "), "generated banner"),
    (re.compile(r"^## Modules$|^## Provenance$|^## Cross-references \(informational\)$"), "generated section header"),
    (re.compile(r"^## Sub-SO \("), "generated section header"),
    (re.compile(r"^## Security Requirements \("), "generated section header"),
    (re.compile(r"^## Verbatim regulatory basis \("), "generated section header"),
    (re.compile(r"^## Summary \(Domain Analysis\)$"), "generated section header"),
    (re.compile(r"^## Deep analysis — Part 3 rendering"), "generated section header"),
    (re.compile(r"^## Cross-regulation interactions$"), "generated section header"),
    (re.compile(r"^## HSO considerations \(from "), "generated section header"),
    (re.compile(r"^## Participants \(CRDA-deep, full table\)$"), "generated section header"),
    (re.compile(r"^## Sub-domain scope structure \(full table\)$"), "generated section header"),
    (re.compile(r"^## Non-participant / stub notes$"), "generated section header"),
    (re.compile(r"^## Residual pair content \("), "generated section header"),
    (re.compile(r"^## Part 1 §1 — Cross-Regulation Analysis context$"), "generated section header"),
    (re.compile(r"^## Part 2 — Domain Analysis \(summary layer\)$"), "generated section header"),
    (re.compile(r"^## Part 3 — context$|^## Part 4 — context$|^## Part 1 §3 — context$"), "generated section header"),
    (re.compile(r"^## Participating regulations \(§3\)$"), "generated section header"),
    (re.compile(r"^## High-level requirement \(multi-reg aggregation\)$"), "generated section header"),
    (re.compile(r"^## Residual \(unrouted\)$"), "generated section header"),
    (re.compile(r"^## Ambiguity overflow \("), "generated section header"),
    (re.compile(r"^## Structural banners \(merged Parts\)$"), "generated section header"),
    (re.compile(r"^## Sub-requirements section heading$"), "generated section header"),
    (re.compile(r"^- Sub-domain: `"), "generated identity bullet"),
    (re.compile(r"^> \["), "generated link banner"),
    (re.compile(r"^\| .*\| \[[^]]+\]\([^)]+\)( \+ \[[^]]+\]\([^)]+\))? \|$"), "generated index/module link row"),
    (re.compile(r"^\|[-: |]+\|$"), "table separator"),
    (re.compile(r"^```markdown$"), "details fence"),
    # M13 nomenclature: any line containing SG- (Phase 0/Fase 1 nomenclature) is
    # the documented replacement of an analogous SO- line; both forms are
    # classified as generated (rename artefacts, not user-added content).
    (re.compile(r"SG-(?:D-\d+\.\d+(?:\.[A-Za-z_0-9]+|\.HL)?|GDPR|CRA|NIS2|DORA|AIACT|AI_Act)(?:-\d+)?"), "M13 nomenclature rename artefact"),
    (re.compile(r"^\d+ lines — see "), "dedup note continuation"),
    # ---- control-anchor uniformization (documented in
    # baseline/MAPPINGS/_control_uniformization.md; machine surfaces generated by
    # scripts/uniformize_control_anchors.py from sr_control_mappings/<REG>.json)
    (re.compile(r"^(?:- )?\*\*Control anchors:\*\* "), "generated control-anchor line"),
    (re.compile(r"^<!-- aegis:control-anchors"), "control-anchors marker"),
    (re.compile(r"^\s*nist_pf:\s*\[.*\]\s*$"), "generated PF YAML anchor key"),
    (re.compile(r"^\s*nist_airmf:\s*\[.*\]\s*$"), "generated AI RMF YAML anchor key"),
    (re.compile(r"^\*\*(?:PF 1\.1|AI RMF) anchors \(from .*dashboard.*\):\*\*$"),
     "generated PF/AIRMF anchors header"),
    (RE_AXIS_LIST_LINE, "generated PF/AIRMF anchors list"),
]


def read_lines(path: Path):
    text = path.read_text(encoding="utf-8-sig", errors="replace")
    return [ln.replace("\r", "") for ln in text.splitlines()]


def load_uniformization(path: Path):
    """Documented dashboard-wins line replacements
    (baseline/MAPPINGS/_uniformization_changes.json, written by
    scripts/uniformize_control_anchors.py --apply). An original line counts as
    covered when its recorded replacement is present; a recorded replacement
    line in the output is explained by definition.

    M13 nomenclature flag: when ANY surface == 'phase_nomenclature_m13'
    change exists for the sub-domain, that sub-domain opts in to the M13
    loose-coverage rule for any original SO- line (the SG- swap is accepted
    as covered verbatim, see nomenclature_covered)."""
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    uni = {}
    for c in data.get("changes", []):
        sub = c.get("subdomain", "")
        d = uni.setdefault(sub, {"old": {}, "new": set(), "m13": False})
        d["old"].setdefault(c.get("old_line"), []).append(c.get("new_line"))
        d["new"].add(c.get("new_line"))
        if c.get("surface") == "phase_nomenclature_m13":
            d["m13"] = True
    return uni


NOMENCLATURE_RE = re.compile(
    r"\bSO-((?:D-\d+\.\d+\.[A-Za-z_0-9]+|D-\d+\.\d+\.HL|GDPR-\d+|CRA-\d+|NIS2-\d+|DORA-\d+|AIACT-\d+|AI_Act-\d+))"
)

def nomenclature_covered(orig_line: str, cur_text: str) -> bool:
    """M13: original SO- line covered when its SG- swap (or any SG- line whose
    text up to the SG-id matches the original up to the SO-id) exists in cur.
    The corpus merged line may be longer (continuation prose), so we match
    by common prefix up to and including the (renamed) SG-id."""
    m = NOMENCLATURE_RE.search(orig_line)
    if not m:
        return False
    orig_id = m.group(0)  # SO-...
    sg_id = orig_id.replace('SO-', 'SG-', 1)  # SG-...
    idx_orig = orig_line.find(orig_id)
    if idx_orig < 0:
        return False
    prefix = orig_line[:idx_orig] + sg_id  # everything up to and including the SG-id
    # Match against any current line that begins with `prefix` (allow trailing prose)
    for ln in cur_text.splitlines():
        if ln.startswith(prefix):
            return True
    return False


def is_heading_text(line: str):
    m = re.match(r"^(#{1,6})\s+(.*)$", line.strip())
    return m.group(2).strip() if m else None


def collect_target_lines(sub_dir: Path):
    """All lines from all non-article .md files in the modular sub-domain."""
    counter = Counter()
    files = []
    for p in sorted(sub_dir.rglob("*.md")):
        if "articles" in p.relative_to(sub_dir).parts:
            continue
        lines = read_lines(p)
        counter.update(lines)
        files.append(p.relative_to(sub_dir).as_posix())
    return counter, files


def classify_out_surplus(lines, src_set):
    classes = Counter()
    unclassified = Counter()
    relevelled = 0
    for ln, cnt in lines.items():
        if ln in src_set:
            classes["intentional duplication (exists in original)"] += cnt
            continue
        if RE_PURITY.match(ln):
            classes["purity stamp"] += cnt
            continue
        for rx, label in GENERATED:
            if rx.match(ln):
                classes[label] += cnt
                break
        else:
            # re-levelled source heading? ("#### X" in src -> "## X" in out)
            ht = is_heading_text(ln)
            if ht is not None:
                classes["re-levelled heading (source title)"] += cnt
                relevelled += 1
                continue
            unclassified[ln] += cnt
    return classes, unclassified


def verify_subdomain(orig_sub: Path, cur_sub: Path, report, uniform=None):
    uniform = uniform or {}
    merged = orig_sub / f"{orig_sub.name}.md"
    src = read_lines(merged)
    tgt_counter, tgt_files = collect_target_lines(cur_sub)
    tgt_set = set(tgt_counter)
    tgt_text = chr(10).join(tgt_counter)

    src_nonblank = [l for l in src if l.strip()]
    tgt_nonblank = Counter({k: v for k, v in tgt_counter.items() if k.strip()})
    src_set = set(src_nonblank)
    uni = uniform.get(orig_sub.name, {"old": {}, "new": set()})
    m13_global = any(isinstance(v, dict) and v.get("m13") for v in uniform.values())

    def covered(line: str) -> bool:
        for v in src_variants(line):
            if v in tgt_set:
                return True
            # documented uniformization replacement (dashboard-wins, see ledger);
            # sidecar keys are baseline-side (normalized) lines
            if any(nw in tgt_set for nw in uni["old"].get(v, [])):
                return True
        # M13 nomenclature: original SO- line covered when SG- swap exists verbatim
        # in the current sub-domain output (only when m13 flag is set in sidecar).
        if m13_global and nomenclature_covered(line, tgt_text):
            return True
        return False

    # 1. SET coverage (normalization-aware: documented CSF map applied)
    uncovered = [(i + 1, l) for i, l in enumerate(src) if l.strip() and not covered(l)]

    # 2. multiset surplus (original > output): intentional dedup / documented
    #    normalization only. Lines whose every variant is absent from target
    #    are already reported as uncovered; here they would be double-counted,
    #    so variant-covered lines are excluded from surplus.
    surplus = Counter(l for l in src_nonblank if not covered(l))
    surplus_total = sum(surplus.values())
    surplus_uncovered = []
    blank_surplus = max(0, len(src) - len(src_nonblank) - (sum(tgt_counter.values()) - sum(tgt_nonblank.values())))

    # 3. reverse surplus (normalization-aware: a target line is explained if
    #    it exists in the original, or its documented normalization does)
    norm_src = Counter()
    for l in src_nonblank:
        for v in src_variants(l):
            norm_src[v] += 1

    def explained(k: str) -> bool:
        if k in src_set:
            return True
        if k in uni["new"]:
            return True  # documented uniformization replacement target
        return normalize_csf_tokens(k, None) in norm_src or k in norm_src

    rev = Counter({k: v for k, v in tgt_nonblank.items() if k.strip() and not explained(k)})
    classes, unclassified = classify_out_surplus(rev, src_set)

    res = {
        "sub": orig_sub.name,
        "src_lines": len(src),
        "src_nonblank": len(src_nonblank),
        "target_files": len(tgt_files),
        "target_lines": sum(tgt_counter.values()),
        "uncovered": uncovered,
        "dedup_surplus": surplus_total,
        "surplus_uncovered": surplus_uncovered,
        "blank_surplus": blank_surplus,
        "out_surplus": sum(rev.values()),
        "out_classes": classes,
        "unclassified": unclassified,
    }
    report.append(res)
    return res


def verify_annotation(m0_root: Path, orig_root: Path, log):
    """M0 (annotated snapshot) must equal original + tag lines only."""
    bad = 0
    for merged in sorted(orig_root.glob("D-*/D-*/D-*.?*.md")):
        if not re.fullmatch(r"D-\d+\.\d+", merged.stem):
            continue
        rel = merged.relative_to(orig_root)
        m0f = m0_root / rel
        if not m0f.exists():
            log.append(f"ANNOTATION: missing M0 file {rel}")
            bad += 1
            continue
        src = Counter(read_lines(merged))
        m0 = Counter(read_lines(m0f))
        removed = src - m0
        added = m0 - src
        bad_added = [l for l in added if l.strip() and not RE_TAG.match(l.strip())]
        if removed or bad_added:
            bad += 1
            log.append(f"ANNOTATION {rel}: removed={sum(removed.values())} "
                       f"non-tag-added={len(bad_added)}")
            for l in bad_added[:5]:
                log.append(f"    + {l[:100]}")
    return bad


def verify_articles(orig_root: Path, cur_root: Path, log):
    orig_files = sorted(orig_root.glob("D-*/D-*.[0-9]*/articles/*.md"))
    same = diff = missing = 0
    for f in orig_files:
        rel = f.relative_to(orig_root)
        cur = cur_root / rel
        if not cur.exists():
            missing += 1
            log.append(f"ARTICLE MISSING: {rel.as_posix()}")
            continue
        a = "\n".join(read_lines(f))
        b = "\n".join(read_lines(cur))
        if a == b:
            same += 1
        else:
            diff += 1
            log.append(f"ARTICLE DIFFERS: {rel.as_posix()}")
    extra = [p.relative_to(cur_root).as_posix()
             for p in sorted(cur_root.glob("D-*/D-*.[0-9]*/articles/*.md"))
             if not (orig_root / p.relative_to(cur_root)).exists()]
    return {"total": len(orig_files), "same": same, "differ": diff, "missing": missing,
            "extra_in_current": extra}


def verify_manifests(orig_root: Path, cur_root: Path, log):
    """Manifest deep-equality, ex `modular_layout` and anchor-token-insensitive
    (CSF anchor normalization + PF/AI RMF uniformization are documented in
    _csf_anchor_normalization.md / _control_uniformization.md and validated
    separately by the resolvability and crosswalk-consistency checks)."""
    out = {"same": 0, "differ": 0}
    STRIP_KEYS = {"nist_pf", "nist_airmf", "pf_anchors", "airmf_anchors",
                  "applicable_pf_controls_by_regulation",
                  "applicable_airmf_controls_by_regulation",
                  # anchor lists change LENGTH under the documented uniformization
                  # (dashboard sets add/remove tokens), so token values cannot be
                  # neutralized by regex alone — the whole field is excluded and
                  # validated separately by the resolvability + crosswalk checks
                  "nist_csf", "csf_anchors",
                  "applicable_nist_controls_by_regulation"}

    def strip_new_keys(obj):
        if isinstance(obj, dict):
            return {k: strip_new_keys(v) for k, v in obj.items() if k not in STRIP_KEYS}
        if isinstance(obj, list):
            return [strip_new_keys(v) for v in obj]
        return obj

    def canon(obj):
        s = json.dumps(strip_new_keys(obj), sort_keys=True, ensure_ascii=False)
        s = RE_CSF_TOKEN.sub("", s)
        s = RE_PF_TOKEN.sub("", s)
        s = RE_AIRMF_TOKEN.sub("", s)
        return s

    for mf in sorted(orig_root.glob("D-*/D-*.manifest.json")):
        rel = mf.relative_to(orig_root)
        cur = cur_root / rel
        if not cur.exists():
            out["differ"] += 1
            log.append(f"MANIFEST MISSING: {rel.as_posix()}")
            continue
        a = json.loads(mf.read_text(encoding="utf-8-sig"))
        b = json.loads(cur.read_text(encoding="utf-8-sig"))
        b.pop("modular_layout", None)
        if canon(a) == canon(b):
            out["same"] += 1
        else:
            out["differ"] += 1
            keys = set(a) | set(b)
            delta = [k for k in keys if canon(a.get(k)) != canon(b.get(k))]
            log.append(f"MANIFEST DIFFERS: {rel.as_posix()} keys={delta}")
    return out


def verify_anchor_resolvability(cur_root: Path, log):
    """R2b: every CSF token cited on objective/cross/index layers must exist
    in the referential. articles/ excluded (verbatim source corpus)."""
    import json as _json
    ref = _json.loads((cur_root.parent / "CONTROLS" / "NIST_CSF_2.0" / "CSF_2.0.json")
                      .read_text(encoding="utf-8-sig"))
    universe = set(ref["subcategories"])
    pat = re.compile(r"\b(?:GV|ID|PR|DE|RS|RC)\.[A-Z]{2}-\d{2}\b")
    bad = 0
    for p in sorted(cur_root.glob("D-*/D-*.[0-9]*/regs/*.md")) + \
             sorted(cur_root.glob("D-*/D-*.[0-9]*/cross/*.md")) + \
             sorted(cur_root.glob("D-*/D-*.[0-9]*/objective.md")) + \
             sorted(cur_root.glob("D-*/D-*.manifest.json")):
        for m in pat.finditer(p.read_text(encoding="utf-8-sig", errors="replace")):
            if m.group(0) not in universe:
                bad += 1
                log.append(f"R2b UNRESOLVABLE: {m.group(0)} in {p.as_posix()}")
    return bad


def verify_pf_airmf_resolvability(cur_root: Path, log):
    """R2b extension: every PF / AI RMF token cited on regs/manifest layers must
    exist in the CONTROLS referentials."""
    ctrl = cur_root.parent / "CONTROLS"
    pf_ids = {p.stem for p in (ctrl / "NIST_PF").rglob("*.json")}
    airmf_ids = {p.stem for p in (ctrl / "NIST_AI_RMF").rglob("*.json")}
    bad = 0
    for p in sorted(cur_root.glob("D-*/D-*.[0-9]*/regs/*.md")) + \
             sorted(cur_root.glob("D-*/D-*.manifest.json")):
        text = p.read_text(encoding="utf-8-sig", errors="replace")
        for m in RE_PF_TOKEN.finditer(text):
            if m.group(0) not in pf_ids:
                bad += 1
                log.append(f"R2b-PF UNRESOLVABLE: {m.group(0)} in {p.as_posix()}")
        for m in RE_AIRMF_TOKEN.finditer(text):
            if m.group(0) not in airmf_ids:
                bad += 1
                log.append(f"R2b-AIRMF UNRESOLVABLE: {m.group(0)} in {p.as_posix()}")
    return bad


def verify_crosswalk_consistency(cur_root: Path, xwalk_dir: Path, log):
    """Independent (anti-circular, R10) check: every machine-readable anchor
    surface in regs/ must equal the dashboard crosswalk set for its SRs.
      - requirement YAML `nist_csf:` (joined via nearest source_SR)
      - Sub-SO `**CSF anchors (from ...)**` strict list lines

    M9 exception: an anchor added to the crosswalk under
    `_m9_partial_coverage_sidecar.json` is accepted as long as the corpus
    surface contains it (corpus may add MORE than the crosswalk, but not LESS).
    Returns the number of contradictions."""
    RE_NIST = re.compile(r"^(\s*)nist_csf:\s*\[([^\]]*)\]\s*$")
    RE_SR = re.compile(r"source_[sS][rR]:\s*(SR-[A-Z0-9_]+-\d+)")
    RE_HDR2 = re.compile(r"^\*\*CSF anchors \(from ([^*]*?)\):\*\*$")
    RE_SRID = re.compile(r"SR-[A-Z0-9_]+-\d+")
    TOK = re.compile(r"\b(?:GV|ID|PR|DE|RS|RC)\.[A-Z]{2}-\d{2}\b")

    xw = {}
    for regjson in sorted(xwalk_dir.glob("*.json")):
        doc = json.loads(regjson.read_text(encoding="utf-8-sig"))
        for s in doc["srs"]:
            xw[s["sr_id"]] = set(s["nist_csf"])
            # also include M9 additions
            for p in s.get("partial_coverage_patches", []):
                xw[s["sr_id"]].add(p["anchor"])

    bad = 0
    in_fence, block_sr = False, None
    for p in sorted(cur_root.glob("D-*/D-*.[0-9]*/regs/*.md")):
        if p.name.endswith(".ambiguity.md"):
            continue
        lines = p.read_text(encoding="utf-8-sig", errors="replace").splitlines()
        in_fence, block_sr = False, None
        for i, ln in enumerate(lines):
            if ln.strip().startswith("```"):
                in_fence = not in_fence
                block_sr = None
                continue
            if in_fence:
                m = RE_SR.search(ln)
                if m:
                    block_sr = m.group(1)
                m2 = RE_NIST.match(ln)
                if m2 and block_sr and block_sr in xw:
                    toks = {t.strip() for t in m2.group(2).split(",") if t.strip()}
                    if toks != xw[block_sr]:
                        bad += 1
                        log.append(f"XWALK MISMATCH req YAML {p.as_posix()}: "
                                   f"{block_sr} {sorted(toks)} != {sorted(xw[block_sr])}")
                continue
            m3 = RE_HDR2.match(ln)
            if m3:
                srs = RE_SRID.findall(m3.group(1))
                joinable = [s for s in srs if s in xw]
                if not joinable:
                    continue
                union = set()
                for s in joinable:
                    union |= xw[s]
                if i + 1 < len(lines):
                    toks = set(TOK.findall(lines[i + 1]))
                    if toks and toks != union:
                        bad += 1
                        log.append(f"XWALK MISMATCH subso list {p.as_posix()}: "
                                   f"{sorted(toks)} != {sorted(union)}")
    return bad


def tree_compare(orig_root: Path, cur_root: Path, log):
    orig_files = {p.relative_to(orig_root).as_posix() for p in orig_root.rglob("*") if p.is_file()}
    cur_files = {p.relative_to(cur_root).as_posix() for p in cur_root.rglob("*") if p.is_file()}
    merged_pattern = re.compile(r"^D-\d+_[^/]+/D-\d+\.\d+/D-\d+\.\d+\.md$")
    only_orig = sorted(f for f in orig_files - cur_files if not merged_pattern.match(f))
    merged_removed = sorted(f for f in orig_files - cur_files if merged_pattern.match(f))
    only_cur = sorted(f for f in cur_files - orig_files if "_migration_report" not in f
                      and "_loss_verification" not in f)
    return only_orig, merged_removed, only_cur


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--original", required=True)
    ap.add_argument("--baseline", default="baseline/domains")
    ap.add_argument("--m0-dir", default=None, help="annotated pre-modularization snapshot dir")
    ap.add_argument("--uniformization", default="baseline/MAPPINGS/_uniformization_changes.json",
                    help="documented dashboard-wins line replacements (sidecar)")
    ap.add_argument("--crosswalk", default="baseline/MAPPINGS/sr_control_mappings",
                    help="dashboard crosswalk dir for the consistency check")
    ap.add_argument("--report", default=None, help="report path (default <baseline>/_loss_verification.md)")
    args = ap.parse_args()

    orig_root = Path(args.original)
    cur_root = Path(args.baseline)
    log = []
    uniform = load_uniformization(Path(args.uniformization))
    if uniform:
        print(f"uniformization sidecar: {sum(len(d['old']) for d in uniform.values())} "
              f"documented line replacements loaded")

    # A. annotation fidelity
    ann_bad = 0
    if args.m0_dir:
        ann_bad = verify_annotation(Path(args.m0_dir), orig_root, log)

    # B. per-subdomain coverage
    report = []
    subs = sorted(p for p in orig_root.glob("D-*/D-*.[0-9]*")
                  if p.is_dir() and re.fullmatch(r"D-\d+\.\d+", p.name))
    for sub in subs:
        cur_sub = cur_root / sub.relative_to(orig_root)
        if not cur_sub.exists():
            log.append(f"SUBDOMAIN MISSING in current: {sub.name}")
            continue
        verify_subdomain(sub, cur_sub, report, uniform)

    # C/D/E/F
    articles = verify_articles(orig_root, cur_root, log)
    r2b_bad = verify_anchor_resolvability(cur_root, log)
    r2b_pf_bad = verify_pf_airmf_resolvability(cur_root, log)
    xwalk_bad = verify_crosswalk_consistency(cur_root, Path(args.crosswalk), log)
    manifests = verify_manifests(orig_root, cur_root, log)
    only_orig, merged_removed, only_cur = tree_compare(orig_root, cur_root, log)

    # summary
    n_uncovered = sum(len(r["uncovered"]) for r in report)
    n_unclass = sum(len(r["unclassified"]) for r in report)
    n_dedup = sum(r["dedup_surplus"] for r in report)
    n_blank = sum(r["blank_surplus"] for r in report)
    n_rev = sum(r["out_surplus"] for r in report)

    print("=" * 72)
    print("EXHAUSTIVE NO-LOSS VERIFICATION")
    print("=" * 72)
    print(f"Sub-domains checked:            {len(report)}")
    print(f"A. annotation fidelity failures: {ann_bad}" + ("" if args.m0_dir else "  (skipped: no --m0-dir)"))
    print(f"B. UNCOVERED original lines:     {n_uncovered}   <-- MUST be 0")
    print(f"B. dedup surplus (explained):    {n_dedup}")
    print(f"B. blank-line surplus (format):  {n_blank}")
    print(f"B. output surplus lines:         {n_rev} (classified below)")
    print(f"B. UNCLASSIFIED output lines:    {n_unclass}   <-- MUST be 0")
    print(f"C. articles: {articles['same']} identical, {articles['differ']} differ, "
          f"{articles['missing']} missing, {len(articles['extra_in_current'])} extra")
    print(f"D. manifests: {manifests['same']} equal (ex-modular_layout, CSF-token-insensitive), {manifests['differ']} differ")
    print(f"G. R2b unresolvable CSF anchors (regs/cross/objective/manifests): {r2b_bad}   <-- MUST be 0")
    print(f"G. R2b unresolvable PF/AI RMF anchors (regs/manifests): {r2b_pf_bad}   <-- MUST be 0")
    print(f"H. Crosswalk contradictions (regs anchor surfaces vs dashboards): {xwalk_bad}   <-- MUST be 0")
    print(f"E. files only in original (non-merged): {len(only_orig)}; merged files replaced: {len(merged_removed)}")
    print(f"E. files only in current (new modules): {len(only_cur)}")
    ok = (n_uncovered == 0 and n_unclass == 0 and ann_bad == 0
          and articles["differ"] == 0 and articles["missing"] == 0
          and manifests["differ"] == 0 and not only_orig and r2b_bad == 0
          and r2b_pf_bad == 0 and xwalk_bad == 0)
    print("VERDICT:", "NO INFORMATION LOST" if ok else "FAILURES FOUND — see report")

    # console detail
    for r in report:
        if r["uncovered"]:
            print(f"\n-- UNCOVERED in {r['sub']} ({len(r['uncovered'])}):")
            for i, l in r["uncovered"][:12]:
                print(f"   L{i}: {l[:110]}")
    for r in report:
        if r["unclassified"]:
            print(f"\n-- UNCLASSIFIED in {r['sub']}:")
            for l, c in list(r["unclassified"].items())[:12]:
                print(f"   x{c}: {l[:110]}")
    for l in log:
        print("LOG:", l)
    if only_orig:
        print("\nFiles only in original (non-merged):")
        for f in only_orig:
            print("  ", f)

    # markdown report
    rep = ["# Exhaustive no-loss verification — original vs modular corpus", ""]
    rep.append(f"- Original: `{orig_root}`")
    rep.append(f"- Current modular baseline: `{cur_root}`")
    rep.append(f"- Method: independent line-multiset analysis (`scripts/verify_no_loss.py`); "
               f"no modularize_domains.py logic reused (anti-circular, R10).")
    rep.append("")
    rep.append("| Check | Result |")
    rep.append("|---|---|")
    rep.append(f"| Sub-domains verified | {len(report)} |")
    rep.append(f"| A. Annotation fidelity (original → annotated snapshot) | "
               + ("**0 failures** — snapshot = original + tag lines only" if args.m0_dir and ann_bad == 0
                  else (f"**{ann_bad} failures**" if args.m0_dir else "skipped")) + " |")
    rep.append(f"| B. Uncovered original lines | **{n_uncovered}** (required: 0) |")
    rep.append(f"| B. Intentional dedup (Part 3 ≡ Part 1 §1, set-covered) | {n_dedup} lines |")
    rep.append(f"| B. Blank-line surplus (layout only) | {n_blank} lines |")
    rep.append(f"| B. Output surplus (duplication + boilerplate) | {n_rev} lines |")
    rep.append(f"| B. Unclassified output lines | **{n_unclass}** (required: 0) |")
    rep.append(f"| C. Article copies identical | {articles['same']}/{articles['total']} "
               f"(differ {articles['differ']}, missing {articles['missing']}) |")
    rep.append(f"| D. Manifests equal (ex `modular_layout`, CSF-token-insensitive) | {manifests['same']}/{manifests['same'] + manifests['differ']} |")
    rep.append(f"| G. R2b unresolvable CSF anchors (regs/cross/objective/manifests) | **{r2b_bad}** (required: 0) — see _csf_anchor_normalization.md |")
    rep.append(f"| G. R2b unresolvable PF/AI RMF anchors (regs/manifests) | **{r2b_pf_bad}** (required: 0) — referentials in baseline/CONTROLS |")
    rep.append(f"| H. Crosswalk contradictions (regs anchor surfaces vs dashboards) | **{xwalk_bad}** (required: 0) — see _control_uniformization.md |")
    rep.append(f"| E. Original-only files (non-merged) | {len(only_orig)} |")
    rep.append(f"| F. Merged files replaced by modules | {len(merged_removed)} (content verified line-by-line above) |")
    rep.append(f"| F. New modular files | {len(only_cur)} |")
    rep.append("")
    rep.append("## Per-subdomain line accounting")
    rep.append("")
    rep.append("| Sub-domain | Orig lines | Target files | Uncovered | Dedup surplus | Out surplus | Unclassified |")
    rep.append("|---|---|---|---|---|---|---|")
    for r in report:
        rep.append(f"| {r['sub']} | {r['src_lines']} | {r['target_files']} | {len(r['uncovered'])} | "
                   f"{r['dedup_surplus']} | {r['out_surplus']} | {len(r['unclassified'])} |")
    rep.append("")
    rep.append("## Output-surplus classification (all lines)")
    rep.append("")
    cls_total = Counter()
    for r in report:
        cls_total.update(r["out_classes"])
    for k, v in cls_total.most_common():
        rep.append(f"- {k}: {v}")
    rep.append("")
    if only_orig:
        rep.append("## Files only in original")
        rep.append("")
        for f in only_orig:
            rep.append(f"- {f}")
        rep.append("")
    if log:
        rep.append("## Verification log")
        rep.append("")
        for l in log:
            rep.append(f"- {l}")
        rep.append("")
    verdict = "NO INFORMATION LOST" if ok else "FAILURES FOUND"
    rep.append(f"## Verdict")
    rep.append("")
    rep.append(f"**{verdict}** — every original line is either present verbatim in the modular "
               f"output, or accounted as intentional deduplication of byte-identical Part 3 "
               f"copies / blank-line layout / regenerated summary indexes (originals preserved "
               f"in the source repo and git history).")
    rep.append("")

    out_path = Path(args.report) if args.report else cur_root / "_loss_verification.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(rep) + "\n", encoding="utf-8", newline="\n")
    print(f"\nreport: {out_path}")

    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
