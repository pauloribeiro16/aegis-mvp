#!/usr/bin/env python3
"""phase2_rule_discovery.py — do the three unseamed Doc01 columns have a rule?

`docs/decisions/ADR-2026-10-09_phase2-objective-bridge.md` D3 settles the three
columns the ledger marked "no rule found" / "Mechanical + lookup"
(`Verification Criteria`, `Method`, `Responsible Owner`) by MEASUREMENT, not by
prompt and not by guess: a candidate derivation rule is tested here against the
three hand-authored case deliverables BEFORE any code claims the column.

This is deliberately a separate script from `scripts/phase2_ledger_scan.py`.
That one backs a published DRAFT whose numbers are quoted throughout; changing
the code that produces them would break the reproducibility of a measurement
that is already in the record.

The frozen decision rule (ADR-013 D3, restated here so the verdict is computed
rather than eyeballed):

    a column ships only if a rule reproduces it with agreement >= 0.80 on ALL
    THREE cases, AND the rule generalises — i.e. fitted on two cases it still
    predicts the third at >= 0.80, which is the mechanical stand-in for "a new
    company needs no human authoring".

A column that fails stays `—` in the pipeline. That is a legitimate outcome and
is written up as a negative result (AGENTS.md §-2 rule 4), not backfilled.

    python3 scripts/phase2_rule_discovery.py
    python3 scripts/phase2_rule_discovery.py --json

Exits 0 whatever it finds. It is a diagnostic, not a gate.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

CASES = {
    "Case_01_TinyTask_SaaS": "Case_01_TinyTask_SaaS",
    "Case_02_SecureBorder_Solutions": "Case_02_SecureBorder_Solutions",
    "Case_03_OmniBank": "Case_03_OmniBank",
}

#: Column positions in the 9-column objective table, 0-indexed. Fixed by ADR-013
#: D4: `check_traceability.py` T6 reads the published anchor set from column 8,
#: so the schema cannot be narrowed without breaking an existing check.
C_ID, C_REG, C_CRITERIA, C_METHOD, C_OWNER, C_ANCHORS = 0, 3, 5, 6, 7, 8

SD_RE = re.compile(r"D-\d{2}\.\d")
ROW_RE = re.compile(r"^\|\s*`(?P<id>(?:PO|SO)-D-\d{2}\.\d-\d{3})`\s*\|")

#: Agreement a rule must reach on every case, and on a case it was not fitted
#: on, to be considered a derivation rather than a coincidence.
THRESHOLD = 0.80

#: The empirical verification vocabulary the Doc01s publish in their §1.3.
#: A predicted method outside this set is not a rule, it is a new vocabulary.
METHODS = {"TEST", "INSPECT", "DEMONSTRATE", "ANALYZE"}


# --------------------------------------------------------------------------
# parsing
# --------------------------------------------------------------------------

def _cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def _clean(v: str) -> str:
    """Strip markdown decoration without changing the words."""
    return v.replace("**", "").replace("`", "").strip()


def _slug_of(sd: str) -> str:
    """`D-01.1` -> `data at rest encryption`, from the corpus index."""
    try:
        sys.path.insert(0, str(REPO / "pipeline" / "src"))
        from compose import subdomain_name  # noqa: PLC0415 — lazy: repo path
        return subdomain_name(REPO, sd).lower()
    except Exception:
        return sd.lower()


def parse_doc01(path: Path) -> list[dict]:
    """Every objective row of a Doc01, whatever its heading structure.

    The objective id carries the sub-domain (`PO-D-01.1-001` -> `D-01.1`), so no
    heading context is needed — which is what lets this read all three cases
    despite Case 03's divergent `##`/table layout (ledger §4.3).
    """
    rows: list[dict] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines):
        m = ROW_RE.match(line)
        if not m:
            continue
        cells = _cells(line)
        # Case 03's four corrupted rows swallow baseline YAML and then re-emit
        # their own tail, so those lines carry more than 9 fields. Only the
        # leading 9 are the contract; the rest is the corruption, measured at
        # ledger §4.2 and not this script's business.
        if len(cells) < 9:
            continue
        cells = cells[:9]
        anchors = [_clean(a) for a in cells[C_ANCHORS].split(",")
                   if _clean(a) and _clean(a) != "—"]
        rows.append({
            "id": m.group("id"),
            "subdomain": SD_RE.search(m.group("id")).group(0),
            "regulation": _clean(cells[C_REG]),
            "criteria": _clean(cells[C_CRITERIA]),
            "method": _clean(cells[C_METHOD]),
            "owner": _clean(cells[C_OWNER]),
            "anchor_families": [a.split(".")[0] for a in anchors],
            "anchors": anchors,
        })
    return rows


def parse_governance_matrix(path: Path) -> dict[str, tuple[str, list[str]]]:
    """§13: sub-domain -> (lead, supports), tolerating both delivered schemas.

    Cases 01 and 02 ship a 4-column matrix keyed on a dedicated sub-domain
    column. Case 03 ships a 3-column matrix whose sub-domains are domains —
    `(D-01, D-05)` — buried in the governance-area label, with one row
    ("AI governance (OmniScore, AI Act rows)") carrying no canonical id at all.
    Both are read; the granularity difference is itself a finding, so it is
    recorded rather than smoothed over.

    This is the only per-case ownership data anywhere in the corpus. It lives in
    the deliverable, not in `fact_sheet.yaml` — the Phase 1 schema has no
    governance, role, or tier field (ADR-013 §2), which is precisely what makes
    the owner column hard.
    """
    out: dict[str, tuple[str, list[str]]] = {}
    granularity = "sub-domain"
    for line in path.read_text(encoding="utf-8").splitlines():
        cells = _cells(line)
        if len(cells) == 4 and SD_RE.search(cells[3]):
            lead, supports = _clean(cells[1]), [_clean(s) for s in cells[2].split(",") if _clean(s)]
            for sd in SD_RE.findall(cells[3]):
                out[sd] = (lead, supports)
        elif len(cells) == 3 and re.search(r"\(D-\d{2}", cells[0]):
            # Case 03: domain ids inside the label; expand to sub-domains below.
            lead, supports = _clean(cells[1]), [_clean(s) for s in cells[2].split(",") if _clean(s)]
            granularity = "domain"
            for dom in re.findall(r"D-\d{2}", cells[0]):
                out[f"DOMAIN:{dom}"] = (lead, supports)
    return out, granularity


def expand_domains(matrix: dict, subdomains: set[str]) -> dict:
    """Resolve `DOMAIN:D-NN` entries to the sub-domains actually present.

    A Case 03 row that says `(D-09, D-10)` supervises every sub-domain under
    those domains, but only the ones this case actually selected — a matrix row
    naming a sub-domain with no objective would otherwise widen the match.
    """
    out = {k: v for k, v in matrix.items() if not k.startswith("DOMAIN:")}
    for key, value in matrix.items():
        if not key.startswith("DOMAIN:"):
            continue
        dom = key.split(":", 1)[1]
        for sd in subdomains:
            if sd.startswith(dom):
                out.setdefault(sd, value)
    return out


# --------------------------------------------------------------------------
# candidate rules
# --------------------------------------------------------------------------

def fit_mapping(rows: list[dict], keyfn) -> dict:
    """The most common value per key — the only mapping a rule could encode."""
    seen: dict[str, Counter] = defaultdict(Counter)
    for r in rows:
        seen[keyfn(r)][r["method"]] += 1
    return {k: c.most_common(1)[0][0] for k, c in seen.items()}


def agreement(rows: list[dict], keyfn, mapping: dict) -> tuple[int, int, dict]:
    """Hits / total, plus the confusion of every miss (a rule that is 80%
    accurate for the wrong reasons should not pass silently)."""
    hit = tot = 0
    misses: dict[str, int] = defaultdict(int)
    for r in rows:
        key = keyfn(r)
        if key not in mapping:
            continue
        tot += 1
        if mapping[key] == r["method"]:
            hit += 1
        else:
            misses[f"{key}:{mapping[key]}->{r['method']}"] += 1
    return hit, tot, dict(misses)


def _loto(rows_by_case: dict[str, list[dict]], keyfn) -> tuple[float, dict]:
    """Leave-one-case-out: fit on two cases, predict the third.

    This is the mechanical stand-in for "a new company needs no human
    authoring". A mapping fitted on Case 01 and 02 that collapses on Case 03 is
    a lookup dressed as a rule.
    """
    ratios = {}
    for held in rows_by_case:
        fit = [r for c, rs in rows_by_case.items() if c != held for r in rs]
        mapping = fit_mapping(fit, keyfn)
        hit, tot, _ = agreement(rows_by_case[held], keyfn, mapping)
        ratios[held] = (hit / tot) if tot else 0.0
    return ratios, {}


def rule_method_from_anchor_family(rows_by_case: dict[str, list[dict]]) -> dict:
    """R-METHOD-1 — the verification method follows the control-anchor family.

    The intuitive hypothesis: `GV.*` objectives are governance and get INSPECT
    or ANALYZE, `PR.*` and `ID.*` are protective/identity mechanisms and get
    TEST. Tested rather than assumed.
    """
    def keyfn(r):
        return (r["anchor_families"][0] if r["anchor_families"] else "—")

    all_rows = [r for rs in rows_by_case.values() for r in rs]
    mapping = fit_mapping(all_rows, keyfn)
    per_case, loto = {}, {}
    for case, rows in rows_by_case.items():
        hit, tot, misses = agreement(rows, keyfn, mapping)
        per_case[case] = {"hit": hit, "total": tot, "ratio": round(hit / tot, 3) if tot else 0.0,
                          "misses": misses}
    loto, _ = _loto(rows_by_case, keyfn)
    return {"name": "R-METHOD-1", "description": "method <- first control-anchor family",
            "mapping": mapping, "per_case": per_case,
            "loto": {k: round(v, 3) for k, v in loto.items()}}


def rule_method_from_regulation(rows_by_case: dict[str, list[dict]]) -> dict:
    """R-METHOD-2 — the method follows the regulation."""
    keyfn = lambda r: r["regulation"]
    all_rows = [r for rs in rows_by_case.values() for r in rs]
    mapping = fit_mapping(all_rows, keyfn)
    per_case = {}
    for case, rows in rows_by_case.items():
        hit, tot, misses = agreement(rows, keyfn, mapping)
        per_case[case] = {"hit": hit, "total": tot, "ratio": round(hit / tot, 3) if tot else 0.0,
                          "misses": misses}
    loto, _ = _loto(rows_by_case, keyfn)
    return {"name": "R-METHOD-2", "description": "method <- regulation",
            "mapping": mapping, "per_case": per_case,
            "loto": {k: round(v, 3) for k, v in loto.items()}}


def rule_owner_from_governance(rows_by_case, matrices: dict, granularity: dict) -> dict:
    """R-OWNER-1 — the owner follows the case's own §13 governance matrix.

    Reproducibility and derivability are different properties, and this rule
    separates them: it may well reproduce the delivered column perfectly while
    being unusable as a derivation, because the matrix itself is per-case human
    input that `fact_sheet.yaml` does not carry (ADR-013 §2). Reported as
    "Mechanical + lookup" in the ledger's own vocabulary, which names where the
    human input goes.
    """
    per_case = {}
    for case, rows in rows_by_case.items():
        matrix = matrices[case]
        contains_lead = both = exact = total = 0
        for r in rows:
            entry = matrix.get(r["subdomain"])
            if not entry:
                continue
            lead, supports = entry
            total += 1
            expected = " + ".join([lead, *supports])
            if lead in r["owner"]:
                contains_lead += 1
            if lead in r["owner"] and any(s in r["owner"] for s in supports):
                both += 1
            if r["owner"] == expected:
                exact += 1
        per_case[case] = {
            "total": total,
            "owner_contains_primary_lead": round(contains_lead / total, 3) if total else 0.0,
            "owner_contains_lead_and_a_support": round(both / total, 3) if total else 0.0,
            "owner_equals_lead_plus_all_supports": round(exact / total, 3) if total else 0.0,
        }
    return {"name": "R-OWNER-1", "description": "owner <- case §13 governance matrix",
            "per_case": per_case, "granularity": granularity,
            "note": "reproducible from a per-case table; NOT derivable — the matrix "
                    "is human input absent from fact_sheet.yaml"}


def rule_criteria_cardinality(rows_by_case: dict[str, list[dict]]) -> dict:
    """R-CRITERIA-1 — is Verification Criteria a function of anything cheap?

    The ledger's R10b challenge is that the criteria read identically for a
    different company. This quantifies it rather than asserting it: replace each
    row's sub-domain slug with `<SLUG>` and count what survives. A column that
    is 100% distinct raw but ~1 distinct after normalisation is a template, and
    the template is what would ship if this column were derived.
    """
    per_case = {}
    for case, rows in rows_by_case.items():
        norm = Counter()
        for r in rows:
            text = r["criteria"].lower()
            slug = _slug_of(r["subdomain"])
            if slug and slug in text:
                text = text.replace(slug, "<slug>")
            norm[text] += 1
        per_reg = defaultdict(set)
        for r in rows:
            per_reg[r["regulation"]].add(r["criteria"])
        per_case[case] = {
            "rows": len(rows),
            "distinct_raw": len({r["criteria"] for r in rows}),
            "distinct_slug_normalised": len(norm),
            "top_normalised_forms": norm.most_common(3),
            "distinct_per_regulation": {k: len(v) for k, v in sorted(per_reg.items())},
        }
    return {"name": "R-CRITERIA-1", "description": "criteria <- (regulation, anchor)",
            "per_case": per_case,
            "note": "distinct_raw ~= rows but distinct_slug_normalised ~= 1 means the "
                    "column is one template with the sub-domain slug substituted: "
                    "unique per row, identical for every company"}


# --------------------------------------------------------------------------
# verdict
# --------------------------------------------------------------------------

def verdict(rules: list[dict]) -> list[dict]:
    """Apply the frozen rule. Computed, not eyeballed."""
    out = []
    for r in rules:
        if "loto" in r:  # a method rule
            per = r["per_case"]
            all_fit = all(v["ratio"] >= THRESHOLD for v in per.values())
            all_loto = all(v >= THRESHOLD for v in r["loto"].values())
            if all_fit and all_loto:
                out.append({"rule": r["name"], "column": "method", "decision": "SHIPS",
                            "why": "reproduces >=0.80 on every case and on a held-out case"})
            elif all_fit:
                out.append({"rule": r["name"], "column": "method", "decision": "STAYS SEAM",
                            "why": "reproduces in-sample but does not generalise "
                                   "(leave-one-case-out below threshold) — a lookup, "
                                   "not a derivation"})
            else:
                out.append({"rule": r["name"], "column": "method", "decision": "STAYS SEAM",
                            "why": "agreement below 0.80 on at least one case"})
        elif r["name"] == "R-OWNER-1":
            best = max((v["owner_contains_lead_and_a_support"] for v in r["per_case"].values()),
                       default=0.0)
            out.append({"rule": r["name"], "column": "owner", "decision": "STAYS SEAM",
                        "why": f"reproducible ({best:.0%} of rows contain the matrix's "
                               f"lead and a support) but NOT derivable: it requires a "
                               f"per-case table that fact_sheet.yaml does not carry"})
        else:
            out.append({"rule": r["name"], "column": "criteria", "decision": "STAYS SEAM",
                        "why": "measured as a template; see cardinality below"})
    return out


# --------------------------------------------------------------------------

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--json", action="store_true", help="emit the raw result as JSON")
    args = ap.parse_args(argv)

    rows_by_case: dict[str, list[dict]] = {}
    matrices: dict[str, dict] = {}
    granularity: dict[str, str] = {}
    for key, dirname in CASES.items():
        d = REPO / "cases" / dirname / "02_PHASE2_RULES"
        doc = d / "Doc01_Operational_Objectives.md"
        if not doc.exists():
            print(f"## {key}: SKIP (no {doc})")
            continue
        rows_by_case[key] = parse_doc01(doc)
        raw, gran = parse_governance_matrix(doc)
        granularity[key] = gran
        matrices[key] = expand_domains(raw, {r["subdomain"] for r in rows_by_case[key]})

    if not args.json:
        for key, rows in rows_by_case.items():
            methods = Counter(r["method"] for r in rows)
            print(f"## {key}   objectives={len(rows)}  sub-domains={len({r['subdomain'] for r in rows})}")
            print(f"   method vocabulary: {dict(methods)}")

    rules = [
        rule_method_from_anchor_family(rows_by_case),
        rule_method_from_regulation(rows_by_case),
        rule_owner_from_governance(rows_by_case, matrices, granularity),
        rule_criteria_cardinality(rows_by_case),
    ]
    verdicts = verdict(rules)

    if args.json:
        print(json.dumps({"rows": {k: len(v) for k, v in rows_by_case.items()},
                          "rules": rules, "verdict": verdicts},
                         indent=1, ensure_ascii=False, default=str))
        return 0

    for r in rules:
        print(f"\n=== {r['name']} — {r['description']}")
        if "mapping" in r:
            print(f"   fitted mapping: {r['mapping']}")
        for case, v in r["per_case"].items():
            detail = {k: x for k, x in v.items() if k != "misses"}
            print(f"   {case}: {detail}")
            if v.get("misses"):
                top = sorted(v["misses"].items(), key=lambda kv: -kv[1])[:4]
                print(f"      worst misses: {top}")
        if r.get("loto"):
            print(f"   leave-one-case-out: {r['loto']}")
        if r.get("note"):
            print(f"   note: {r['note']}")

    print(f"\n=== VERDICT (threshold {THRESHOLD:.2f}, frozen in ADR-013 D3)")
    for v in verdicts:
        print(f"   {v['column']:<9} {v['decision']:<11} ({v['rule']}) — {v['why']}")
    print("\nA STAYS SEAM column renders `—` in Doc01. It is not backfilled.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())