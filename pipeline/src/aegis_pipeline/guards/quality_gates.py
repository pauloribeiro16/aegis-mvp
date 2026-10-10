#!/usr/bin/env python3
"""aegis_pipeline.guards.quality_gates — content-quality gates for Phase 1 output.

Covers:
  * Obligation retention & anti-verbatim bounds
  * R6 factual grounding (no invented company quantities)
  * R5 technology neutrality (L4 vocabulary prohibition)
  * Unique and specific Company implications
  * Sub-SO coverage checks without silent drops or duplicates
  * Continuous metrics measurement layer (score_run, retention_ratio)

Stdlib only, runnable on compute nodes.
"""

from __future__ import annotations

import re
from difflib import SequenceMatcher

L4_TERMS = re.compile(
    r"\b(aws|azure|gcp|google cloud|s3|ec2|lambda|kubernetes|docker|istio|"
    r"postgres|postgresql|mysql|sqlite|mongodb|oracle|sql server|"
    r"hashicorp|terraform|ansible|openssl|vault|keycloak|okta|auth0|"
    r"react|angular|vue|spring boot|django|rails|dotnet|node\.?js|"
    r"tls|ssl|mtls|oauth|saml|oidc|jwt|kerberos|"
    r"websocket|graphql|grpc|"
    r"iso ?27001|socia? ?2|socia?2|pci ?dss|fedramp|"
    r"microsoft|amazon|google cloud|alibaba|huawei)\b",
    re.I,
)

STOP = {
    "the", "and", "or", "of", "to", "in", "is", "are", "was", "were", "that",
    "with", "for", "on", "by", "as", "at", "an", "be", "it", "its", "this",
    "these", "those", "which", "from", "any", "all", "such", "not", "but",
    "where", "when", "their", "there", "into", "than", "then", "they", "them",
    "also", "may", "must", "can", "each", "other", "own", "same", "more",
    "most", "if", "no", "nor", "do", "does", "did", "has", "have", "had",
    "been", "being", "will", "would", "should", "could", "per", "via", "one",
    "two", "both", "under", "over", "between", "within", "without", "upon",
    "who", "whom", "whose", "what", "how", "why", "when", "where", "only",
}

ADJ_PREFIXES = ("unchanged", "verbatim", "narrowed", "proportional", "inherited", "flagged")


def tokens(text: str) -> list[str]:
    """Lowercase word tokens >= 3 chars, function words removed."""
    return [w for w in re.findall(r"[a-z][a-z0-9\-']*", (text or "").lower())
            if len(w) >= 3 and w not in STOP]


def norm(text: str) -> str:
    return " ".join((text or "").lower().split())


def _articles(text: str) -> set[str]:
    """Art. N / Art. N(a)(b) references — obligation anchors that must survive."""
    return set(re.findall(r"art(?:icle)?\.?\s*(\d+(?:\([a-z0-9]+\))*)", (text or "").lower()))


def check_obligation_retention(goal: str, baseline: str) -> list[str]:
    """The adjusted goal must KEEP the baseline's obligation content and ADD
    company calibration. Both dropping a leg and near-verbatim copying fail."""
    if not (baseline or "").strip():
        return []
    g, b = set(tokens(goal)), set(tokens(baseline))
    if not g:
        return ["adjusted goal carries no substantive content"]
    retention = len(g & b) / max(len(b), 1)
    if retention < 0.30:
        need = max(1, round(len(b) * 0.30))
        missing = sorted(b - g)
        return [
            f"adjusted goal keeps {len(g & b)} of the Sub-SO's {len(b)} obligation "
            f"terms; at least {need} are required ({retention:.0%}). "
            f"Keep the Sub-SO's own obligation vocabulary — change the sentence "
            f"structure and add the company calibration, do NOT substitute synonyms "
            f"or drop clauses. Terms still missing: {', '.join(missing)}. "
            f"Aim for roughly half the Sub-SO's vocabulary expressed in the "
            f"company's own sentence structure. Reproducing the baseline text "
            f"below scores ZERO regardless of how many terms it keeps — a copy "
            f"is not a restatement. "
            f"The Sub-SO objective you must restate (verbatim, do not omit any leg): "
            f"\n\n{baseline.strip()}\n"
        ]
    sim = SequenceMatcher(None, norm(goal), norm(baseline)).ratio()
    gb, bb = norm(goal), norm(baseline)
    if bb and bb in gb and len(gb) < len(bb) * 2.2:
        return [
            f"adjusted goal embeds the Sub-SO objective verbatim instead of "
            f"restating it ({retention:.0%} of its terms kept) — a restatement "
            f"reformulates the duty in the company's terms, it does not paste the "
            f"baseline. Keep the OBLIGATION, drop the baseline's sentence shape: "
            f"aim for roughly half the Sub-SO's vocabulary, rebuilt around this "
            f"company's own actors, systems and scope. Keeping fewer terms is "
            f"correct here; keeping all of them by copying is not."
        ]
    if sim > 0.88:
        return [
            f"adjusted goal is a near-verbatim copy of the Sub-SO objective "
            f"({sim:.0%} similar) — it restates nothing about this company; "
            f"calibrate it against the §2 framing. Keep the obligation's terms "
            f"but rebuild the sentence around this company's own actors and "
            f"scope; roughly half the vocabulary is the target, not all of it."
        ]
    return []


def check_grounded(text: str, sources: list[str], label: str) -> list[str]:
    """Fabricated company QUANTITIES (R6): a headcount / clinic-count / volume
    claim absent from the fact sheet, framing, or Sub-SO is a fabrication."""
    src = " ".join(sources or "")
    src_digits = re.sub(r"[^\d]", "", src)
    text = re.sub(r"(?<![\w-])D-\d{2}\.\d(?:\.[A-Za-z_]+)*(?![\w-])", " ", text or "")
    text = re.sub(r"(?<![\w-])(?:SG|AG|SO|SR)-[\w.]+(?![\w-])", " ", text)
    text = re.sub(r"(?<![\w-])[A-Z]{2,}-[A-Z0-9.]+(?![\w-])", " ", text)
    text = re.sub(
        r"\b(?:Art|Article|Clause|Annex|Chapter|Section|Part|Recital|Guidelines?|Standard|Law|Decree)\.?\s*[\d(][\d()a-z./-]*",
        " ", text, flags=re.I,
    )
    text = re.sub(r"\b(?:ISO(?:/IEC)?|NIST(?:\s*SP)?|ENISA|RFC|BSI|CIS|OWASP)\s*[\dA-Z.-]+", " ", text, flags=re.I)
    text = re.sub(r"\b\d{4}/\d{1,6}\b", " ", text)
    text = re.sub(r"\b(?:19|20)\d{2}\b", " ", text)
    invented = []
    for qty in set(re.findall(
        r"\b\d[\d.,]{2,}\s*(?:employees|staff|people|clinics|users|customers|offices|locations)?",
        text or "", re.I,
    )):
        digits = re.sub(r"[^\d]", "", qty)
        if digits and digits not in src_digits:
            invented.append(qty.strip())
    if invented:
        return [
            f"{label}: company quantity not traceable to the intake or corpus "
            f"(R6): {', '.join(sorted(set(invented))[:6])}"
        ]
    return []


def check_no_technology(*texts: str) -> list[str]:
    hits = []
    for t in texts:
        m = L4_TERMS.search(t or "")
        if m:
            hits.append(f"technology leakage (R5) — technology-neutral wording required, found {m.group(0)!r}")
    return hits


def check_adjustment_vocab(adjustment: str) -> list[str]:
    a = norm(adjustment)
    if not a:
        return ["empty adjustment record (R3)"]
    if a in ("—", "-", "--"):
        return []
    if a.startswith(ADJ_PREFIXES) or len(a.split()) >= 3:
        return []
    return [
        f"adjustment record too brief or invalid (R3): {adjustment[:70]!r} — "
        "provide a substantive proportionality rationale, badge, or '—'"
    ]


def check_implication_specific(implication: str, other_implications: list[str]) -> list[str]:
    imp = norm(implication)
    if len(imp.split()) < 5:
        return ["company implication is too short to be specific to this duty"]
    for other in other_implications:
        if cached_ratio(imp, norm(other)) > 0.95:
            return ["company implication is a near-duplicate of another row's — it must be specific to this duty"]
    return []


def check_subso_coverage(rows: list[dict], expected_regs: list[str]) -> list[str]:
    got = [r.get("regulation", "") for r in rows]
    findings = []
    for reg in expected_regs:
        n = got.count(reg)
        if n == 0:
            findings.append(
                f"Sub-SO {reg} is not restated at all (silent drop) — "
                "the module carries it and the regulation is confirmed"
            )
        elif n > 1:
            findings.append(f"Sub-SO {reg} is restated {n} times (expected 1)")
    for reg in got:
        if reg not in expected_regs:
            findings.append(
                f"row cites {reg}, which has no Sub-SO in this module for a confirmed regulation (R8)"
            )
    return findings


def run_row(
    row: dict,
    baselines: dict[str, str],
    sources: list[str],
    peer_implications: list[str],
) -> list[str]:
    reg = row.get("baseline_source", "").rsplit(".", 1)[-1]
    findings = list(check_obligation_retention(row.get("goal", ""), baselines.get(reg, "")))
    findings += check_grounded(row.get("goal", ""), sources, "adjusted goal")
    findings += check_grounded(row.get("implication", ""), sources, "company implication")
    findings += check_no_technology(
        row.get("goal", ""), row.get("implication", ""), row.get("adjustment", "")
    )
    findings += check_adjustment_vocab(row.get("adjustment", ""))
    findings += check_implication_specific(row.get("implication", ""), peer_implications)
    return findings


def run_all(
    *,
    goals: list[dict],
    baselines: dict[str, str],
    expected_regs: list[str],
    sources: list[str],
    all_implications: list[str],
) -> list[str]:
    findings: list[str] = []
    for r in goals:
        peers = [i for i in all_implications if i != r.get("implication")]
        findings += [f"{r.get('id', '?')}: {m}" for m in run_row(r, baselines, sources, peers)]
    findings += check_subso_coverage(goals, expected_regs)
    return findings


# --------------------------------------------------------------------------
# Measurement layer (EXP-02 / EXP-03)
# --------------------------------------------------------------------------

RETENTION_FLOOR = 0.30
NEAR_VERBATIM_LIMIT = 0.88
IMPLICATION_DUP_LIMIT = 0.95


def retention_ratio(goal: str, baseline: str) -> float | None:
    if not (baseline or "").strip():
        return None
    g, b = set(tokens(goal)), set(tokens(baseline))
    if not b:
        return None
    return len(g & b) / len(b)


def near_verbatim_similarity(goal: str, baseline: str) -> float | None:
    if not (baseline or "").strip():
        return None
    return SequenceMatcher(None, norm(goal), norm(baseline)).ratio()


def _ratio_ceiling(a: str, b: str) -> float:
    la, lb = len(a), len(b)
    if la == 0 or lb == 0:
        return 0.0
    return 2 * min(la, lb) / (la + lb)


_SIM_CACHE: dict[tuple[str, str], float] = {}
_SIM_CACHE_MAX = 50_000


def cached_ratio(a: str, b: str) -> float:
    if a == b:
        return 1.0
    key = (a, b) if a <= b else (b, a)
    hit = _SIM_CACHE.get(key)
    if hit is not None:
        return hit
    if _ratio_ceiling(a, b) <= IMPLICATION_DUP_LIMIT:
        ratio = 0.0
    else:
        ratio = SequenceMatcher(None, a, b).ratio()
    if len(_SIM_CACHE) < _SIM_CACHE_MAX:
        _SIM_CACHE[key] = ratio
    return ratio


def max_peer_similarity(implication: str, peers: list[str]) -> float:
    imp = norm(implication)
    if not imp:
        return 0.0
    best = 0.0
    for o in peers:
        best = max(best, cached_ratio(imp, norm(o)))
    return best


def _baseline_for(baselines: dict[str, str], subdomain: str, reg: str) -> str:
    if subdomain:
        hit = baselines.get(f"{subdomain}.{reg}")
        if hit:
            return hit
    return baselines.get(reg, "")


def score_row(
    row: dict,
    baselines: dict[str, str],
    sources: list[str],
    peer_implications: list[str],
) -> dict:
    reg = row.get("baseline_source", "").rsplit(".", 1)[-1]
    subdomain = row.get("subdomain", "")
    baseline = _baseline_for(baselines, subdomain, reg)
    ret = retention_ratio(row.get("goal", ""), baseline)
    return {
        "id": row.get("id", ""),
        "subdomain": subdomain,
        "regulation": reg,
        "retention": ret,
        "retention_ok": None if ret is None else ret >= RETENTION_FLOOR,
        "near_verbatim": near_verbatim_similarity(row.get("goal", ""), baseline),
        "implication_words": len(norm(row.get("implication", "")).split()),
        "goal_words": len(norm(row.get("goal", "")).split()),
        "pattern": row.get("pattern", ""),
        "property": row.get("property", ""),
        "adjustment": adjustment_kind(row.get("adjustment", "")),
        "ungrounded_quantities": _count_ungrounded(row.get("goal", ""), row.get("implication", ""), sources),
        "max_peer_similarity": max_peer_similarity(row.get("implication", ""), peer_implications),
        "findings": run_row(row, baselines, sources, peer_implications),
    }


def _count_ungrounded(goal: str, implication: str, sources: list[str]) -> int:
    n = 0
    for text in (goal, implication):
        n += len(check_grounded(text, sources, "row"))
    return n


def adjustment_kind(adjustment: str) -> str:
    a = norm(adjustment)
    if not a:
        return "malformed"
    for kind in ("verbatim", "proportional", "inherited", "narrowed", "flagged", "unchanged"):
        if a.startswith(kind):
            return kind
    return "malformed"


def score_run(goals: list[dict], baselines: dict[str, str], sources: list[str]) -> dict:
    _SIM_CACHE.clear()
    all_implications = [r.get("implication", "") for r in goals]
    rows: list[dict] = []
    for i, r in enumerate(goals):
        peers = [imp for j, imp in enumerate(all_implications) if j != i]
        rows.append(score_row(r, baselines, sources, peers))

    rets = [r["retention"] for r in rows if r["retention"] is not None]
    sims = [r["near_verbatim"] for r in rows if r["near_verbatim"] is not None]
    peers_max = [r["max_peer_similarity"] for r in rows]
    mix: dict[str, int] = {}
    for r in rows:
        mix[r["adjustment"]] = mix.get(r["adjustment"], 0) + 1

    n_verbatim = mix.get("verbatim", 0) + mix.get("unchanged", 0)
    ratio_verbatim = (n_verbatim / len(rows)) if rows else 0.0

    delegation_kw = re.compile(
        r"\b(cloud provider|managed service|third-party|vendor|supplier|"
        r"managed|delegat(ed?|ing)|external host(ing)?|saas provider)\b",
        re.I,
    )
    contradictions = [
        r["id"] for r, row_dict in zip(rows, goals)
        if r["adjustment"] in ("verbatim", "unchanged")
        and delegation_kw.search(row_dict.get("implication", ""))
    ]
    calibration_alert = bool(len(rows) >= 10 and ratio_verbatim > 0.70)

    return {
        "n_rows": len(rows),
        "n_subdomains": len({r["subdomain"] for r in rows if r["subdomain"]}),
        "retention": {
            "mean": sum(rets) / len(rets) if rets else None,
            "min": min(rets) if rets else None,
            "max": max(rets) if rets else None,
            "n_measured": len(rets),
            "n_below_floor": sum(1 for r in rows if r["retention"] is not None and r["retention"] < RETENTION_FLOOR),
        },
        "near_verbatim": {
            "max": max(sims) if sims else None,
            "mean": sum(sims) / len(sims) if sims else None,
            "n_above_limit": sum(1 for s in sims if s > NEAR_VERBATIM_LIMIT),
        },
        "implication_reuse": {
            "max_peer_similarity": max(peers_max) if peers_max else None,
            "n_above_dup_limit": sum(1 for s in peers_max if s > IMPLICATION_DUP_LIMIT),
        },
        "adjustment_mix": mix,
        "calibration": {
            "ratio_verbatim": round(ratio_verbatim, 3),
            "calibration_alert": calibration_alert,
            "n_contradictions": len(contradictions),
            "contradiction_rows": contradictions,
        },
        "n_rows_with_findings": sum(1 for r in rows if r["findings"]),
        "total_findings": sum(len(r["findings"]) for r in rows),
        "rows": rows,
    }
