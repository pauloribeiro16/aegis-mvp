#!/usr/bin/env python3
"""quality.py — content-quality gates for the Phase 1 P4 output.

The L0 shape contract (column count, enums, IDs) and validate.py's doc<->JSON
diff are integrity checks: they prove the render is faithful, not that the
content is any good. These gates target the defect classes a red-team injected
that passed every automated check:

  * meta-goal / obligation deletion — the adjusted goal must RETAIN the Sub-SO's
    obligation content (not drop a leg like the Art. 32(1)(b) CIA-resilience
    clause) yet must NOT be a near-verbatim copy (no adaptation);
  * ungrounded company facts — company-specific tokens in the goal/implication
    must trace to the fact sheet, framing, or the Sub-SO itself (R6);
  * technology leakage (R5) — L4 vocabulary;
  * generic Company implication — must be distinct from every other row's
    (a globally pasted sentence is the cheapest way to satisfy the instruction
    and is invisible to shape checks);
  * silent Sub-SO drop / duplicate — every (sub-domain, confirmed reg) Sub-SO
    card must be covered exactly once;
  * Adjustment outside the closed vocabulary; rows for non-confirmed regs (R8).

Each function returns human-readable findings (empty list == clean). Stdlib
only, so it runs on compute nodes.
"""

from __future__ import annotations

import re
from difflib import SequenceMatcher

# R5 technology neutrality: L4 vocabulary banned from Phase 1 artifacts.
L4_TERMS = re.compile(
    r"\b(aws|azure|gcp|google cloud|s3|ec2|lambda|kubernetes|docker|istio|"
    r"postgres|postgresql|mysql|sqlite|mongodb|oracle|sql server|"
    r"hashicorp|terraform|ansible|openssl|vault|keycloak|okta|auth0|"
    r"react|angular|vue|spring boot|django|rails|dotnet|node\.?js|"
    r"tls|ssl|mtls|oauth|saml|oidc|jwt|kerberos|"
    r"websocket|graphql|grpc|"
    r"iso ?27001|socia? ?2|socia?2|pci ?dss|fedramp|"
    r"microsoft|amazon|google cloud|alibaba|huawei)\b", re.I)

# Short function words carry no obligation content.
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
    return set(re.findall(r"art(?:icle)?\.?\s*(\d+(?:\([a-z0-9]+\))*)",
                          (text or "").lower()))


def check_obligation_retention(goal: str, baseline: str) -> list[str]:
    """The adjusted goal must KEEP the baseline's obligation content and ADD
    company calibration. Both directions are failures: dropping a leg loses an
    obligation; a near-copy is no adaptation at all. The golden case sits in
    the middle (Sub-SO wording + company specificity), so both bounds are
    calibrated around that band, not around word counts."""
    if not (baseline or "").strip():
        return []  # no Sub-SO objective in this module: nothing to retain
    g, b = set(tokens(goal)), set(tokens(baseline))
    if not g:
        return ["adjusted goal carries no substantive content"]
    retention = len(g & b) / max(len(b), 1)
    if retention < 0.30:
        # An ABSOLUTE count, not a percentage: mid-size models are measurably
        # worse at aggregate ratios than at "keep these words" checklists, and
        # the two instructions ("restate in your own words" + "cover N terms")
        # are one instruction to them — the concision half wins. Say how many
        # terms the duty has, how many the row kept, and list them.
        need = max(1, round(len(b) * 0.30))
        missing = sorted(b - g)
        return [f"adjusted goal keeps {len(g & b)} of the Sub-SO's {len(b)} obligation "
                f"terms; at least {need} are required ({retention:.0%}). "
                f"Keep the Sub-SO's own obligation vocabulary — change the sentence "
                f"structure and add the company calibration, do NOT substitute synonyms "
                f"or drop clauses. Terms still missing: {', '.join(missing)}. "
                f"The Sub-SO objective you must restate (verbatim, do not omit any leg): "
                f"\n\n{baseline.strip()}\n"]
    # the article citation lives in the Articles column, not in the goal prose:
    # requiring it inside the goal would force redundant citation. What must
    # not happen is the row carrying NO legal basis at all — that is enforced
    # against the resolved source at L1 (resolve_reg_source), not here.
    # REFORMULATION, not embedding: the goal may quote long stretches of the
    # baseline as long as it also carries company calibration, but a goal that
    # IS the baseline (a verbatim or near-verbatim copy) is not an adaptation
    sim = SequenceMatcher(None, norm(goal), norm(baseline)).ratio()
    gb, bb = norm(goal), norm(baseline)
    if bb and bb in gb and len(gb) < len(bb) * 2.2:
        return ["adjusted goal embeds the Sub-SO objective verbatim instead of "
                "restating it — a restatement reformulates the duty in the company's "
                "terms, it does not paste the baseline"]
    if sim > 0.88:
        return [f"adjusted goal is a near-verbatim copy of the Sub-SO objective "
                f"({sim:.0%} similar) — it restates nothing about this company; "
                "calibrate it against the §2 framing"]
    return []


def check_grounded(text: str, sources: list[str], label: str) -> list[str]:
    """Fabricated company QUANTITIES (R6): a headcount / clinic-count / volume
    claim absent from the fact sheet, framing, or Sub-SO is a fabrication.
    Scoped to quantities deliberately — a general proper-noun detector is too
    noisy (it fires on legal vocabulary, canonical ids, and possessives) and
    would reject valid rows. The technology/vendor class is handled by
    check_no_technology; named-entity fabrication is a G-P1-D human-gate call."""
    src = " ".join(sources or "")
    src_digits = re.sub(r"[^\d]", "", src)
    # strip canonical ids and article refs so D-01.1 / Art. 32(1)(b) are not read
    # as company quantities ("01.1" collapses to "011")
    text = re.sub(r"(?<![\w-])D-\d{2}\.\d(?:\.[A-Za-z_]+)*(?![\w-])", " ", text or "")
    text = re.sub(r"(?<![\w-])(?:SG|AG|SO|SR)-[\w.]+(?![\w-])", " ", text)
    text = re.sub(r"(?<![\w-])[A-Z]{2,}-[A-Z0-9.]+(?![\w-])", " ", text)
    text = re.sub(r"\b(?:Art|Article|Clause|Annex|Chapter|Section|Part)\.?\s*[\d(][\d()a-z.]*",
                  " ", text)
    invented = []
    for qty in set(re.findall(r"\b\d[\d.,]{2,}\s*(?:employees|staff|people|clinics|"
                              r"users|customers|offices|locations)?", text or "", re.I)):
        digits = re.sub(r"[^\d]", "", qty)
        if digits and digits not in src_digits:
            invented.append(qty.strip())
    if invented:
        return [f"{label}: company quantity not traceable to the intake or corpus "
                f"(R6): {', '.join(sorted(set(invented))[:6])}"]
    return []


def check_no_technology(*texts: str) -> list[str]:
    hits = []
    for t in texts:
        m = L4_TERMS.search(t or "")
        if m:
            hits.append(f"technology leakage (R5) — technology-neutral wording "
                        f"required, found {m.group(0)!r}")
    return hits


def check_adjustment_vocab(adjustment: str) -> list[str]:
    a = norm(adjustment)
    if not a:
        return ["empty adjustment record (R3)"]
    if not a.startswith(ADJ_PREFIXES):
        return [f"adjustment outside the closed vocabulary (R3): {adjustment[:70]!r} — "
                "use 'unchanged — fits as stated', 'narrowed: <what> — because "
                "<company fact>' or 'flagged: <open question>'"]
    return []


def check_implication_specific(implication: str, other_implications: list[str]) -> list[str]:
    """The Company implication must be specific to this duty and this company.
    A sentence pasted identically across every row satisfies the instruction on
    paper while saying nothing — reject duplicates and near-duplicates.
    `other_implications` are the implications of every OTHER row (by id/index,
    never by value): an identical string here IS the pasted-sentence defect."""
    imp = norm(implication)
    if len(imp.split()) < 5:
        return ["company implication is too short to be specific to this duty"]
    # No identity skip: Python constant-folds identical literals into one
    # object, so an identity test silently treats a pasted duplicate as "self"
    # and never fires (probe-caught 2026-10-03). Value-equality through
    # cached_ratio is the check.
    for other in other_implications:
        if cached_ratio(imp, norm(other)) > 0.95:
            return ["company implication is a near-duplicate of another row's — it must "
                    "be specific to this duty"]
    return []


def check_subso_coverage(rows: list[dict], expected_regs: list[str]) -> list[str]:
    """Every Sub-SO the module carries for a confirmed regulation must be
    restated exactly once (no silent drop, no duplicate) and no row may cite a
    regulation that is not confirmed (R8)."""
    got = [r.get("regulation", "") for r in rows]
    findings = []
    for reg in expected_regs:
        n = got.count(reg)
        if n == 0:
            findings.append(f"Sub-SO {reg} is not restated at all (silent drop) — "
                            "the module carries it and the regulation is confirmed")
        elif n > 1:
            findings.append(f"Sub-SO {reg} is restated {n} times (expected 1)")
    for reg in got:
        if reg not in expected_regs:
            findings.append(f"row cites {reg}, which has no Sub-SO in this module for a "
                            "confirmed regulation (R8)")
    return findings


def run_row(row: dict, baselines: dict[str, str], sources: list[str],
            peer_implications: list[str]) -> list[str]:
    """Every content gate for a single goal row. `peer_implications` are the
    implications of all OTHER rows (this run's earlier sub-domains plus this
    sub-domain's sibling rows) — never the row's own text."""
    reg = row.get("baseline_source", "").rsplit(".", 1)[-1]
    findings = list(check_obligation_retention(row.get("goal", ""),
                                               baselines.get(reg, "")))
    findings += check_grounded(row.get("goal", ""), sources, "adjusted goal")
    findings += check_grounded(row.get("implication", ""), sources,
                               "company implication")
    findings += check_no_technology(row.get("goal", ""), row.get("implication", ""),
                                    row.get("adjustment", ""))
    findings += check_adjustment_vocab(row.get("adjustment", ""))
    findings += check_implication_specific(row.get("implication", ""),
                                           peer_implications)
    return findings


def run_all(*, goals: list[dict], baselines: dict[str, str], expected_regs: list[str],
            sources: list[str], all_implications: list[str]) -> list[str]:
    """All content gates over one sub-domain's goal rows (used by validate.py
    for the assembled document; each row is compared against its peers)."""
    findings: list[str] = []
    for r in goals:
        peers = [i for i in all_implications if i != r.get("implication")]
        findings += [f"{r.get('id', '?')}: {m}" for m in
                     run_row(r, baselines, sources, peers)]
    findings += check_subso_coverage(goals, expected_regs)
    return findings


# --------------------------------------------------------------------------
# Measurement layer (EXP-02 / EXP-03)
# --------------------------------------------------------------------------
#
# Everything above answers a yes/no question and is used that way. This section
# returns the NUMBER those checks compute and throw away, so the same pass that
# decides accept/reject also produces a continuous, model-free outcome
# variable for every run — past and future.
#
# It is purely additive: score_rows() never changes a gate verdict. The
# acceptance thresholds stay where they are, because a measurement instrument
# that also decides what counts as good is not a measurement.
#
# The primary metric of EXP-02 is `retention`: the fraction of the Sub-SO's
# obligation vocabulary that survives into the adjusted goal. It is the closest
# available proxy to the methodology's central claim — that an adjusted goal
# restates the regulatory duty while calibrating it to the company — and it
# needs no model and no human to compute.

RETENTION_FLOOR = 0.30
NEAR_VERBATIM_LIMIT = 0.88
IMPLICATION_DUP_LIMIT = 0.95


def retention_ratio(goal: str, baseline: str) -> float | None:
    """Fraction of the baseline's obligation terms kept by the goal.

    None when there is no baseline to retain (a module with no Sub-SO for a
    confirmed regulation) — distinct from 0.0, which is a genuine total drop.
    """
    if not (baseline or "").strip():
        return None
    g, b = set(tokens(goal)), set(tokens(baseline))
    if not b:
        return None
    return len(g & b) / len(b)


def near_verbatim_similarity(goal: str, baseline: str) -> float | None:
    """Lexical similarity to the Sub-SO objective.

    This is the quantity behind the 0.88 gate whose firing rate had never been
    measured (EXP-01 recorded a max of 0.79 across 65 rows by hand). Reported
    per row so the distribution is a measurement rather than an anecdote.
    """
    if not (baseline or "").strip():
        return None
    return SequenceMatcher(None, norm(goal), norm(baseline)).ratio()


def _ratio_ceiling(a: str, b: str) -> float:
    """The maximum SequenceMatcher ratio two strings can possibly have:
    2·min(len)/ (len_a + len_b). Comparisons whose ceiling sits below the
    caller's threshold cannot fire and can be skipped without changing any
    verdict — difflib is pure Python, and the O(n²) peer loop over 65 rows is
    minutes without this filter and seconds with it (measured: 29 s -> 2 s)."""
    la, lb = len(a), len(b)
    if la == 0 or lb == 0:
        return 0.0
    return 2 * min(la, lb) / (la + lb)


# Pairwise similarity memo for implication comparisons. The same (row_i,
# row_j) pair is computed twice per run — once by the gate (run_row) and once
# by the measurement layer (max_peer_similarity) — and difflib is pure Python,
# so without the memo the whole-run pass is 2x slower than it needs to be.
# Keyed by the normalized strings themselves; cleared by score_run and capped
# so a long-lived process cannot grow it without bound.
_SIM_CACHE: dict[tuple[str, str], float] = {}
_SIM_CACHE_MAX = 50_000


def cached_ratio(a: str, b: str) -> float:
    """SequenceMatcher ratio with a memo and the length-ceiling short-circuit.

    Results are identical to calling the matcher directly: the cache key is
    exact, and the ceiling only skips pairs that mathematically cannot exceed
    NEAR_VERBATIM_LIMIT... they are still real numbers, so this helper returns
    the true ratio for pairs that pass the ceiling and 0.0 for pairs that
    cannot reach IMPLICATION_DUP_LIMIT (callers here only use it against that
    limit).
    """
    if a == b:
        return 1.0
    key = (a, b) if a <= b else (b, a)
    hit = _SIM_CACHE.get(key)
    if hit is not None:
        return hit
    if _ratio_ceiling(a, b) <= IMPLICATION_DUP_LIMIT:
        ratio = 0.0  # cannot reach the dup limit: skip the matcher entirely
    else:
        ratio = SequenceMatcher(None, a, b).ratio()
    if len(_SIM_CACHE) < _SIM_CACHE_MAX:
        _SIM_CACHE[key] = ratio
    return ratio


def max_peer_similarity(implication: str, peers: list[str]) -> float:
    """Highest similarity of this implication to any other row's.

    A "reusable sentence" — one sentence pasted across every row — scores near
    1.0 against its peers. This is the mechanical form of the judgement the L2
    rubric asks a human to make.
    """
    imp = norm(implication)
    if not imp:
        return 0.0
    best = 0.0
    for o in peers:
        best = max(best, cached_ratio(imp, norm(o)))
    return best


def _baseline_for(baselines: dict[str, str], subdomain: str, reg: str) -> str:
    """Resolve a row's Sub-SO objective.

    The gate path (run_row) is called per sub-domain, so its `baselines` dict is
    keyed by regulation alone. The measurement path (score_run) sees the whole
    run at once, where "GDPR" is ambiguous: D-01.1's GDPR Sub-SO and D-03.2's
    are different texts, and silently comparing a row against the wrong one
    would produce a plausible, meaningless retention number. The composite key
    is tried first; the bare regulation is the fallback so both call shapes
    work.
    """
    if subdomain:
        hit = baselines.get(f"{subdomain}.{reg}")
        if hit:
            return hit
    return baselines.get(reg, "")


def score_row(row: dict, baselines: dict[str, str], sources: list[str],
              peer_implications: list[str]) -> dict:
    """Per-row measurement record. Same inputs as run_row, numeric outputs."""
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
        "ungrounded_quantities": _count_ungrounded(
            row.get("goal", ""), row.get("implication", ""), sources),
        "max_peer_similarity": max_peer_similarity(
            row.get("implication", ""), peer_implications),
        "findings": run_row(row, baselines, sources, peer_implications),
    }


def _count_ungrounded(goal: str, implication: str, sources: list[str]) -> int:
    n = 0
    for text in (goal, implication):
        n += len(check_grounded(text, sources, "row"))
    return n


def adjustment_kind(adjustment: str) -> str:
    """'unchanged' | 'verbatim' | 'proportional' | 'inherited' | 'narrowed' | 'flagged' | 'malformed'.

    The mix EXP-01 reported as 17 narrowed vs 1, and which is meaningless
    without a noise floor. 'malformed' is separated from the legal values
    so an out-of-vocabulary row cannot be silently absorbed into a legitimate
    bucket in a distribution.
    """
    a = norm(adjustment)
    if not a:
        return "malformed"
    for kind in ("verbatim", "proportional", "inherited", "narrowed", "flagged", "unchanged"):
        if a.startswith(kind):
            return kind
    return "malformed"


def score_run(goals: list[dict], baselines: dict[str, str], sources: list[str]) -> dict:
    """Measure a whole run's goal rows and summarise.

    `goals` is every row in the run (all sub-domains), each carrying id,
    subdomain, baseline_source, goal, implication, pattern, property, adjustment.
    Peer comparisons span the whole run, because "the same sentence pasted
    everywhere" is only detectable against the full set.
    """
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
        r"managed|delegat(ed?|ing)|external host(ing)?|saas provider)\b", re.I)
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
            "n_below_floor": sum(1 for r in rows
                                 if r["retention"] is not None
                                 and r["retention"] < RETENTION_FLOOR),
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
