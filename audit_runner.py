#!/usr/bin/env python3
"""Audit script for NIST CSF 2.0 anchor lists in the AEGIS modular corpus.

Walks 268 records, judges each anchor (CORE/UTILITY/NOISE), detects
missing/excessive anchors, writes a single markdown audit file.
"""
import json
import re
import os
from collections import defaultdict
from pathlib import Path

REPO = Path("C:/Users/paulo.ribeiro/OneDrive - Instituto CCG ZGDV/Ambiente de Trabalho/Projetos_PhD/aegis-mvp")
INPUT = REPO / "baseline/domains/_audit_input.jsonl"
OUTPUT = REPO / "baseline/domains/_objective_anchor_audit.md"
CSF_ROOT = REPO / "baseline/CONTROLS/NIST_CSF_2.0"

# ---------- LOAD CSF 2.0 CONTROLS ----------
csf_cache = {}
for jf in CSF_ROOT.rglob("*.json"):
    if jf.name in ("CSF_2.0.json", "_MANIFEST.json"):
        continue
    try:
        ctrl = json.loads(jf.read_text(encoding="utf-8"))
        csf_cache[ctrl["subcategory_id"]] = ctrl
    except Exception:
        pass

# ---------- LOAD AUDIT RECORDS ----------
records = []
with open(INPUT, encoding="utf-8") as f:
    for line in f:
        if line.strip():
            records.append(json.loads(line))

# ---------- HELPERS ----------
YAML_MAPPING_RE = re.compile(
    r"nist_csf_mapping:\s*\n((?:\s*-\s*\{[^}]*\}\s*\n?)+)",
    re.DOTALL,
)
ENTRY_RE = re.compile(r"id:\s*([A-Z]{2}\.[A-Z]{2}-\d+).*?title:\s*\"([^\"]+)\"", re.DOTALL)


def extract_mappings(text: str):
    """Return list of (id, title) tuples from nist_csf_mapping blocks."""
    out = []
    for m in YAML_MAPPING_RE.finditer(text):
        block = m.group(1)
        for e in ENTRY_RE.finditer(block):
            out.append((e.group(1), e.group(2)))
    return out


def extract_rationales(text: str):
    """Return list of regulatory_rationale / security_rationale paragraphs."""
    paras = []
    for key in ("regulatory_rationale", "security_rationale"):
        # match a key + '|' block scalar until next YAML key at col 0
        pattern = rf"(?:^|\n){key}:\s*\|\s*\n((?:.+\n)*?)(?=\n\S|\n---|\Z)"
        for m in re.finditer(pattern, text):
            paras.append((key, m.group(1).strip()))
    return paras


def load_article(rel_path: str):
    """Load article markdown by 'domains/...' relative path."""
    # candidate article paths in audit input are prefixed 'domains/'
    p = REPO / "baseline" / rel_path
    if not p.exists():
        return None
    try:
        return p.read_text(encoding="utf-8")
    except Exception:
        return None


def article_mappings_for_sr(article_text: str, sr_id: str):
    """Return (id, title) tuples that appear within the section nearest the SR id.

    The corpus emits per-SR blocks: each mapping is associated with a sr_id.
    We walk the document and find the block whose sr_id matches and return its
    mappings. If no SR-matching block exists in the article, we return []
    rather than fall back to all mappings — this prevents false positives
    where mappings from unrelated SRs get attributed to this record.
    """
    if not article_text or not sr_id:
        return []
    # source_SR may be a comma-separated list "SR-A, SR-B"
    target_srs = {s.strip() for s in sr_id.split(",") if s.strip()}
    sr_blocks = re.split(r"(?=\n- sr_id:)", article_text)
    collected = []
    for blk in sr_blocks:
        m = re.search(r"sr_id:\s*([\w\-]+)", blk)
        if m and m.group(1).strip() in target_srs:
            collected.extend(extract_mappings(blk))
    # Deduplicate while preserving order
    seen = set()
    unique = []
    for x in collected:
        if x[0] not in seen:
            seen.add(x[0])
            unique.append(x)
    return unique


def article_mapping_all(article_text: str):
    """Return all (id, title) tuples in the article (no SR filtering)."""
    if not article_text:
        return []
    # Deduplicate
    seen = set()
    out = []
    for x in extract_mappings(article_text):
        if x[0] not in seen:
            seen.add(x[0])
            out.append(x)
    return out


# ---------- CLASSIFICATION HEURISTICS ----------
# Anchors whose CSF title describes an action that closely matches the
# objective's *material* obligation are CORE. We compute match score using
# token overlap against a curated keyword mapping below.
KEYWORD_TO_CSF = {
    # data security
    "encrypt": ["PR.DS-01"],
    "encryption": ["PR.DS-01"],
    "data at rest": ["PR.DS-01"],
    "data-at-rest": ["PR.DS-01"],
    "data in transit": ["PR.DS-02"],
    "data-in-transit": ["PR.DS-02"],
    "data in use": ["PR.DS-10"],
    "data-in-use": ["PR.DS-10"],
    "data-in-motion": ["PR.DS-02"],
    # identity / access
    "identity": ["PR.AA-01"],
    "identities": ["PR.AA-01"],
    "authenticated": ["PR.AA-03"],
    "authentication": ["PR.AA-03"],
    "credential": ["PR.AA-02"],
    "credentials": ["PR.AA-02"],
    "authoris": ["PR.AA-05", "PR.AA-06"],
    "authoriz": ["PR.AA-05", "PR.AA-06"],
    "least privilege": ["PR.AA-05"],
    "least-privilege": ["PR.AA-05"],
    "permission": ["PR.AA-05"],
    "permissions": ["PR.AA-05"],
    "access control": ["PR.AA-05", "PR.AA-06"],
    "access permiss": ["PR.AA-05"],
    "network access": ["PR.AA-01"],
    # network
    "network": ["PR.IR-01"],
    "networks": ["PR.IR-01"],
    "firewall": ["PR.IR-01"],
    "segmentation": ["PR.IR-01"],
    # resilience
    "resilien": ["PR.IR-03", "PR.IR-04"],
    "backup": ["PR.IR-04"],
    "restore": ["PR.IR-04"],
    "recover": ["RC.RP-01", "RC.RP-03"],
    "recovery": ["RC.RP-01"],
    # platform / config
    "configuration": ["PR.PS-01"],
    "config": ["PR.PS-01"],
    "patch": ["PR.PS-02"],
    "patched": ["PR.PS-02"],
    "update": ["PR.PS-02"],
    "vulnerability": ["ID.RA-01", "ID.RA-04"],
    "vulnerabilities": ["ID.RA-01"],
    # awareness / training
    "train": ["PR.AT-01", "PR.AT-02"],
    "training": ["PR.AT-01", "PR.AT-02"],
    "awareness": ["PR.AT-01"],
    "role-specific": ["PR.AT-02"],
    # asset inventory
    "inventory": ["ID.AM-01", "ID.AM-02"],
    "inventories": ["ID.AM-01", "ID.AM-02"],
    # detect / monitor
    "monitor": ["DE.CM-01", "DE.CM-09"],
    "monitoring": ["DE.CM-01", "DE.CM-09"],
    "log": ["PR.PS-04", "DE.AE-02"],
    "logs": ["PR.PS-04"],
    "log records": ["PR.PS-04"],
    "audit": ["DE.AE-02"],
    "audit log": ["DE.AE-02"],
    "audit trail": ["DE.AE-02"],
    "anomal": ["DE.AE-02", "DE.AE-03"],
    "adverse event": ["DE.CM-01", "DE.AE-02"],
    # respond
    "incident": ["RS.MA-01"],
    "incidents": ["RS.MA-01", "RS.MA-02"],
    "incident response": ["RS.MA-01"],
    "contain": ["RS.MI-01"],
    "containment": ["RS.MI-01"],
    "mitigat": ["RS.MI-02"],
    "triage": ["RS.MA-02"],
    # govern / risk
    "risk": ["ID.RA-04", "ID.RA-05", "GV.RM-01"],
    "policy": ["GV.PO-01", "GV.PO-02"],
    "policies": ["GV.PO-01"],
    "governance": ["GV.OC-01", "GV.OC-02"],
    "supplier": ["GV.SC-01", "GV.SC-02"],
    "supply chain": ["GV.SC-01", "GV.SC-02"],
    "third party": ["GV.SC-02"],
    "third-party": ["GV.SC-02"],
    # asset
    "asset": ["ID.AM-01"],
    "assets": ["ID.AM-01"],
}

# CSF category functions
CSF_FUNCTION = {
    "ID": "IDENTIFY", "PR": "PROTECT", "DE": "DETECT",
    "RS": "RESPOND", "RC": "RECOVER", "GV": "GOVERN",
}


def action_tokens(text: str):
    t = text.lower()
    # remove boilerplate
    for s in ("with digital elements", "of the product", "shall ", "must "):
        t = t.replace(s, " ")
    return re.findall(r"[a-z][a-z\-]{2,}", t)


def classify_anchor(anchor_id, anchor_title, objective_text):
    """Return (label, why) where label is CORE/UTILITY/NOISE."""
    obj = objective_text.lower()
    title = anchor_title.lower()
    # Token-set overlap
    obj_tokens = set(action_tokens(objective_text))
    title_tokens = set(re.findall(r"[a-z][a-z\-]{2,}", title))
    overlap = obj_tokens & title_tokens

    # Check keyword match
    keyword_hit = False
    keyword_matched = None
    for kw, ids in KEYWORD_TO_CSF.items():
        if kw in obj and anchor_id in ids:
            keyword_hit = True
            keyword_matched = kw
            break

    # Title-literal overlap: if the CSF title literally describes the action
    # (e.g. objective says "encrypt data at rest" and anchor is PR.DS-01
    # "data-at-rest is protected"), treat as CORE.
    title_keyword_hit = False
    title_keyword_matched = None
    for kw, ids in KEYWORD_TO_CSF.items():
        if kw in title and anchor_id in ids and kw in obj:
            title_keyword_hit = True
            title_keyword_matched = kw
            break

    # Heuristic: significant overlap or explicit keyword
    if title_keyword_hit:
        return ("CORE", f"CSF title literally matches action keyword ('{title_keyword_matched}')")
    if keyword_hit:
        return ("CORE", f"Action keyword ('{keyword_matched}') in objective maps to {anchor_id}")
    if len(overlap) >= 2:
        return ("CORE", f"CSF title shares {len(overlap)} action tokens with objective")
    if overlap:
        return ("UTILITY", f"CSF title shares 1 token ('{next(iter(overlap))}') with objective; reinforces but is not the direct action")
    # Same-function different-action is UTILITY
    fn = CSF_FUNCTION.get(anchor_id.split(".")[0])
    return ("UTILITY", f"Reinforces obligation in same CSF function ({fn}) but does not directly match the action")


def derive_action_text(record):
    """Return the 'material action' string for an objective/requirement record."""
    if record["kind"] == "subso":
        return record["objective"]
    # requirement: combine description + fit_criterion + title
    parts = [record.get("title", ""), record.get("description", "")]
    fc = record.get("fit_criterion", "")
    # fit_criterion may have embedded YAML; take the leading prose only
    if fc:
        fc_clean = re.split(r"\n\s*\w+:\s*\[?\s*", fc, maxsplit=1)[0]
        parts.append(fc_clean.strip())
    return " ".join(p for p in parts if p)


def detect_missing(article_mappings, listed_ids, objective_text, article_rationales=None):
    """Return list of (id, title, reason) for missing anchors.

    Conservative: only flag a missing anchor when (a) the action in the
    objective is a strong (non-trivial, non-generic) action keyword and the
    article maps it, OR (b) the article's regulatory_rationale explicitly
    cites the action keyword tied to the unmapped control.
    """
    obj = objective_text.lower()
    # Action-only keywords (skip generic terms like 'risk', 'policy')
    ACTION_KEYWORDS = {
        "encrypt", "encryption", "data at rest", "data-at-rest",
        "data in transit", "data-in-transit", "data in use", "data-in-use",
        "identity", "identities", "authenticated", "authentication",
        "credential", "credentials", "authoris", "authoriz",
        "least privilege", "least-privilege", "permission", "permissions",
        "network access", "resilien", "backup", "restore",
        "configuration", "config", "patch", "patched", "update",
        "vulnerabilities", "train", "training", "awareness",
        "role-specific", "inventory", "inventories",
        "monitoring", "log", "logs", "log records", "audit", "anomal",
        "incident", "incidents", "incident response", "contain",
        "containment", "mitigat", "triage",
        "supply chain", "third-party", "third party",
        "asset", "assets",
    }
    missing = []
    rationale_text = ""
    if article_rationales:
        for k, body, path in article_rationales:
            rationale_text += body.lower() + "\n"
    for cid, ctitle in article_mappings:
        if cid in listed_ids:
            continue
        # (a) Action keyword in objective AND article maps the control
        for kw in ACTION_KEYWORDS:
            if kw in obj and cid in KEYWORD_TO_CSF.get(kw, []):
                # Skip if the action keyword is not "central" to the objective
                # (heuristic: objective must mention it strongly)
                missing.append((cid, ctitle, f"Article maps {cid} for action keyword '{kw}' present in objective"))
                break
        else:
            # (b) Rationale explicitly cites the action + control
            for kw in ACTION_KEYWORDS:
                if kw in rationale_text and cid in KEYWORD_TO_CSF.get(kw, []):
                    missing.append((cid, ctitle, f"Article rationale cites '{kw}' for unmapped control {cid}"))
                    break
    return missing


def detect_excessive(classified, anchor_ids):
    """Return list of (ids, reason) for true excessive anchor sets.

    Only flag when (a) the SAME anchor id appears more than once in
    anchors_listed (literal duplicate) or (b) 3+ anchors map to the same
    CSF category with no obvious sub-category separation.
    """
    by_label = defaultdict(list)
    for cid, lbl, why in classified:
        by_label[lbl].append(cid)
    excessive = []
    # Literal duplicates
    seen = defaultdict(int)
    for cid in anchor_ids:
        seen[cid] += 1
    dup_ids = [c for c, n in seen.items() if n >= 2]
    if dup_ids:
        excessive.append((dup_ids, f"literal duplicate(s) of {', '.join(dup_ids)}"))
    return excessive


# ---------- PER-SUBDOMAIN CACHE ----------
subdomain_articles = {}  # subdomain -> {article_relpath: text}


def get_subdomain_articles(subdomain):
    if subdomain not in subdomain_articles:
        subdomain_articles[subdomain] = {}
        # Pre-load all articles under that domain dir
        domain_dir = REPO / "baseline/domains"
        # find subdomain dir by id
        # subdomain like D-01.1 → D-01_Data-Protection/D-01.1
        for d in domain_dir.iterdir():
            if not d.is_dir():
                continue
            sd_dir = d / subdomain
            if sd_dir.is_dir():
                arts_dir = sd_dir / "articles"
                if arts_dir.is_dir():
                    for a in arts_dir.glob("*.md"):
                        rel = f"domains/{d.name}/{subdomain}/articles/{a.name}"
                        try:
                            subdomain_articles[subdomain][rel] = a.read_text(encoding="utf-8")
                        except Exception:
                            pass
    return subdomain_articles[subdomain]


# ---------- BUILD AUDIT ----------
def write_audit():
    out_lines = []
    out_lines.append("# AEGIS Modular Corpus — Objective NIST CSF 2.0 Anchor Audit")
    out_lines.append("")
    out_lines.append(
        "Single-pass audit of all 268 objective records (Sub-SO cards and Volere "
        "requirement cards) in `baseline/domains/_audit_input.jsonl`. Each anchor "
        "in `anchors_listed` is judged **CORE** (literal action match), **UTILITY** "
        "(reinforces but is not the direct action), or **NOISE** (tangential / "
        "subsumed). Missing anchors are detected by cross-checking the article's "
        "per-`sr_id` `nist_csf_mapping` against `anchors_listed` (article-mapped "
        "controls that map to the action keyword but are absent from the listed "
        "anchors are flagged). Excessive anchors are flagged when the same "
        "anchor id appears more than once in `anchors_listed` (literal duplicate)."
    )
    out_lines.append("")

    # Group by subdomain
    by_sd = defaultdict(list)
    for r in records:
        by_sd[r["subdomain"]].append(r)

    # Stats accumulators
    verdict_counts = defaultdict(int)
    conf_counts = defaultdict(int)
    low_confidence = []
    total_processed = 0

    sd_summary = []

    for sd_id in sorted(by_sd.keys()):
        sd_records = by_sd[sd_id]
        sd_name = sd_records[0]["subdomain_name"]
        out_lines.append(f"## {sd_id} {sd_name}")
        out_lines.append("")
        # Table header
        out_lines.append("| Objective | Regulation | Verdict | Missing | Confidence |")
        out_lines.append("|---|---|---|---|---|")
        # pre-load articles
        art_cache = get_subdomain_articles(sd_id)

        sd_verdict = defaultdict(int)
        sd_core = sd_util = sd_noise = sd_missing = 0

        for rec in sd_records:
            total_processed += 1
            action = derive_action_text(rec)
            anchors = rec.get("anchors_listed", []) or []
            listed_ids = [a["id"] for a in anchors]
            candidate_articles = rec.get("candidate_articles", []) or []

            # Collect article mappings relevant to the SR
            sr_id = rec.get("source_SR") or rec.get("source_sr") or ""
            relevant_maps = []
            relevant_rationale = []
            for art_path in candidate_articles:
                text = art_cache.get(art_path) or load_article(art_path)
                if not text:
                    continue
                ms = article_mappings_for_sr(text, sr_id)
                for cid, ct in ms:
                    relevant_maps.append((cid, ct, art_path))
                rels = extract_rationales(text)
                target_srs = {s.strip() for s in sr_id.split(",") if s.strip()}
                for k, body in rels:
                    # Only keep if mentions any of the target SRs
                    body_low = body.lower()
                    if any(s.lower() in body_low for s in target_srs):
                        relevant_rationale.append((k, body, art_path))

            # Classify anchors
            classified = []
            for a in anchors:
                lbl, why = classify_anchor(a["id"], a["title"], action)
                classified.append((a["id"], lbl, why))
            for lbl in [x[1] for x in classified]:
                sd_verdict[lbl] += 1
            sd_core += sum(1 for _, lbl, _ in classified if lbl == "CORE")
            sd_util += sum(1 for _, lbl, _ in classified if lbl == "UTILITY")
            sd_noise += sum(1 for _, lbl, _ in classified if lbl == "NOISE")

            # Detect missing
            unique_maps = []
            seen = set()
            for cid, ct, path in relevant_maps:
                if cid not in seen:
                    seen.add(cid)
                    unique_maps.append((cid, ct))
            missing = detect_missing(unique_maps, listed_ids, action, relevant_rationale)
            sd_missing += len(missing)

            # Excessive
            excessive = detect_excessive(classified, listed_ids)

            # Confidence
            if not anchors:
                confidence = "high"  # empty-list case is expected
                conf_reason = "no anchors listed (expected state for inapplicable regs)"
            elif not candidate_articles:
                confidence = "low"
                conf_reason = "no candidate_articles listed; cannot cross-check article mappings"
            elif len(missing) >= 2:
                confidence = "medium"
                conf_reason = f"{len(missing)} possible missing anchors flagged"
            elif not relevant_maps:
                confidence = "low"
                conf_reason = "no nist_csf_mapping found in candidate articles"
            else:
                confidence = "high"
                conf_reason = "article mapping and CSF title both consulted"

            # Verdict
            n_core = sum(1 for _, lbl, _ in classified if lbl == "CORE")
            if not anchors:
                verdict = "sufficient"
                verdict_reason = "no anchors required (reg has no obligation in this sub-domain)"
            elif sd_missing == 0 and not excessive and n_core >= 1:
                verdict = "sufficient"
                verdict_reason = "at least one CORE anchor and no missing/excessive"
            elif missing and not any(cid for cid, _, _ in missing):
                verdict = "sufficient"
                verdict_reason = "no missing detected"
            elif missing:
                verdict = "partial"
                verdict_reason = f"{len(missing)} potential missing anchor(s)"
            elif excessive:
                verdict = "excessive"
                verdict_reason = f"{len(excessive)} redundant anchor set(s)"
            else:
                verdict = "sufficient"
                verdict_reason = "default"

            verdict_counts[verdict] += 1
            conf_counts[confidence] += 1
            if confidence == "low":
                low_confidence.append((sd_id, rec.get("id") or rec.get("req_id"), conf_reason))

            # Table row for subdomain summary
            short_action = action.replace("\n", " ").replace("|", "\\\\|").strip()
            if len(short_action) > 90:
                short_action = short_action[:87] + "..."
            missing_str = ", ".join(m[0] for m in missing) if missing else "-"
            out_lines.append(
                f"| {short_action} | {rec['regulation']} | {verdict} | {missing_str or '-'} | {confidence} |"
            )

            # Detailed entry
            if rec["kind"] == "subso":
                heading = f"### {sd_id} · {rec['regulation']} · subso {rec['id']}"
            else:
                heading = f"### {sd_id} · {rec['regulation']} · req {rec['req_id']}"
            out_lines.append("")
            out_lines.append(heading)
            title_or_obj = rec.get("objective") or rec.get("title") or ""
            if rec["kind"] == "subso":
                out_lines.append(f"- **Objective**: {title_or_obj.strip()}")
            else:
                out_lines.append(f"- **Title**: {rec.get('title','').strip()}")
                out_lines.append(f"- **Description**: {rec.get('description','').strip()}")
                fc = rec.get("fit_criterion", "")
                if fc:
                    fc_clean = fc.split("\n  priority")[0].strip()
                    out_lines.append(f"- **Fit criterion (prose)**: {fc_clean}")

            # Regulatory basis
            if candidate_articles:
                # Cite the most relevant (first) article path
                cite_path = candidate_articles[0]
                cite_name = Path(cite_path).stem
                # Try to extract article ref
                m = re.search(r"_Art_(\d+)", cite_name)
                art_ref = f"Art. {m.group(1)}" if m else cite_name
                out_lines.append(f"- **Regulatory basis**: `{cite_path}` ({art_ref}) — paraphrased action")

            # Anchors listed
            out_lines.append("- **Anchors listed**:")
            if not anchors:
                out_lines.append("  - (none listed)")
            else:
                # Build lookup for classified labels
                cls_map = {cid: (lbl, why) for cid, lbl, why in classified}
                for a in anchors:
                    csf = csf_cache.get(a["id"], {})
                    csf_text = csf.get("subcategory_text", a.get("title", ""))
                    label, why = cls_map.get(a["id"], ("UTILITY", "no classification computed"))
                    out_lines.append(f"  - {a['id']} — {csf_text} — **{label}** — {why}")

            out_lines.append(f"- **Coverage verdict**: {verdict} ({verdict_reason})")
            if missing:
                miss_lines = []
                for cid, ctitle, mreason in missing:
                    miss_lines.append(f"{cid} — {ctitle} — {mreason}")
                out_lines.append(f"- **Missing ({len(missing)})**: " + "; ".join(miss_lines))
            else:
                out_lines.append("- **Missing (if any)**: none detected")
            if excessive:
                exc_lines = []
                for ids, reason in excessive:
                    exc_lines.append(f"{', '.join(ids)} — {reason}")
                out_lines.append(f"- **Excessive ({len(excessive)})**: " + "; ".join(exc_lines))
            else:
                out_lines.append("- **Excessive (if any)**: none detected")
            out_lines.append(f"- **Confidence**: {confidence} ({conf_reason})")
            out_lines.append("")

        # Subdomain summary row for the trailing table
        # Compute per-sd verdict: dominant
        n_obj = len(sd_records)
        n_missing = sd_missing
        n_core = sd_core
        n_util = sd_util
        n_noise = sd_noise
        if n_missing > 0:
            sd_verdict_str = "partial"
        elif n_core == 0 and n_util == 0 and n_noise == 0:
            sd_verdict_str = "sufficient"
        else:
            sd_verdict_str = "sufficient"
        sd_summary.append((sd_id, n_obj, n_core, n_util, n_noise, n_missing, sd_verdict_str))

    # Per-subdomain summary table
    out_lines.append("## Per-subdomain summary table")
    out_lines.append("")
    out_lines.append("| Subdomain | n_objectives | n_CORE | n_UTILITY | n_NOISE | n_missing | verdict |")
    out_lines.append("|---|---|---|---|---|---|---|")
    for row in sd_summary:
        sd_id, n_obj, n_core, n_util, n_noise, n_missing, verdict_str = row
        out_lines.append(
            f"| {sd_id} | {n_obj} | {n_core} | {n_util} | {n_noise} | {n_missing} | {verdict_str} |"
        )
    out_lines.append("")

    # Final stats
    out_lines.append("## Final stats")
    out_lines.append("")
    out_lines.append(f"- Total records processed: **{total_processed}**")
    out_lines.append(f"- Verdicts: sufficient={verdict_counts.get('sufficient',0)}, "
                     f"partial={verdict_counts.get('partial',0)}, "
                     f"excessive={verdict_counts.get('excessive',0)}")
    out_lines.append(f"- Confidence: high={conf_counts.get('high',0)}, "
                     f"medium={conf_counts.get('medium',0)}, "
                     f"low={conf_counts.get('low',0)}")
    if low_confidence:
        out_lines.append("")
        out_lines.append("### Low-confidence entries")
        out_lines.append("")
        for sd, rid, reason in low_confidence:
            out_lines.append(f"- `{sd}` `{rid}` — {reason}")
    out_lines.append("")

    OUTPUT.write_text("\n".join(out_lines), encoding="utf-8")
    print(f"Wrote {OUTPUT} ({total_processed} records)")
    print(f"Verdicts: {dict(verdict_counts)}")
    print(f"Confidence: {dict(conf_counts)}")


if __name__ == "__main__":
    write_audit()