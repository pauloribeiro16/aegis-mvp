#!/usr/bin/env python3
"""derive_qnrcs_anchors.py — the objective → QNRCS measure linkage, derived.

The QNRCS is the national maturity reference (Reg. n.º 756/2026) and, with
NIST CSF 2.0, NIST PF and NIST AI RMF, the active control referential of the
pipeline (ADR-015 §5). It was, until this script, a tree of 108 measures that
nothing could reach: the resolver knew three families, the mapping store
carried three axes, and `phase3/maturity.py` — which computes the maturity
level a run attains — had no importer at all.

The linkage is not authored. Every QNRCS measure already carries
`mapped_nist_csf`: the CSF ids it implements. The mapping store already
carries, per SR, the CSF ids that SR maps to. So:

    objective → SR → CSF id → QNRCS measure whose mapped_nist_csf contains it

is a set intersection over data that is already in the repository, and it is
reproducible by this script. What it produces is a *proposal*: the judgement
that a QNRCS measure implementing CSF id X is the right anchor for an
objective whose SR maps to X is normative, and is the researcher's
(ADR-015 §5).

Usage:
    python3 scripts/derive_qnrcs_anchors.py            # write the mapping
    python3 scripts/derive_qnrcs_anchors.py --report   # print the coverage
    python3 scripts/derive_qnrcs_anchors.py --check    # verify it is current

Stdlib only.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
MAPPINGS = REPO / "baseline" / "MAPPINGS"
STORE_DIR = MAPPINGS / "sr_control_mappings"
OUT = MAPPINGS / "advisory_anchor_mappings" / "QNRCS.json"
QNRCS_ROOT = REPO / "baseline" / "CONTROLS" / "QNRCS"


def load_stores() -> list[dict]:
    stores = []
    for path in sorted(STORE_DIR.glob("*.json")):
        stores.append(json.loads(path.read_text(encoding="utf-8")))
    return stores


def load_qnrcs_measures() -> dict[str, set[str]]:
    """{control_id: CSF ids the measure implements}."""
    out: dict[str, set[str]] = {}
    for path in sorted(QNRCS_ROOT.rglob("*.json")):
        if path.name.startswith("_"):
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        cid = data.get("control_id") or path.stem
        out[cid] = set(data.get("mapped_nist_csf") or [])
    return out


def derive() -> dict:
    measures = load_qnrcs_measures()
    by_csf: dict[str, list[str]] = {}
    for cid, csfs in measures.items():
        for csf in csfs:
            by_csf.setdefault(csf, []).append(cid)

    srs: list[dict] = []
    for store in load_stores():
        reg = store.get("meta", {}).get("regulation", "?")
        for sr in store.get("srs", []):
            csfs = set(sr.get("nist_csf") or [])
            if not csfs:
                continue
            hits = sorted({cid for csf in csfs for cid in by_csf.get(csf, [])})
            if not hits:
                continue
            srs.append({
                "sr_id": sr.get("sr_id"),
                "regulation": reg,
                "sub_domain": sr.get("sub_domain"),
                "linked_objectives": sr.get("linked_objectives"),
                "nist_csf": sorted(csfs),
                "qnrcs": hits,
            })
    srs.sort(key=lambda s: (str(s["regulation"]), str(s["sr_id"])))
    return {
        "meta": {
            "framework": "QNRCS",
            "title": "Regulamento n.º 756/2026",
            "advisory": False,
            "derived_by": "scripts/derive_qnrcs_anchors.py",
            "derivation": "objective → SR → NIST CSF 2.0 id → QNRCS measure whose "
                          "mapped_nist_csf contains it",
            "normative_status": "PROPOSED — the linkage is machine-derived; the "
                                 "researcher's approval of each anchor is recorded in "
                                 "ADR-015 §5",
        },
        "srs": srs,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--report", action="store_true", help="print the coverage and exit")
    ap.add_argument("--check", action="store_true", help="verify the stored mapping is current")
    args = ap.parse_args()

    derived = derive()
    srs = derived["srs"]
    measures = load_qnrcs_measures()
    covered = {cid for s in srs for cid in s["qnrcs"]}
    objectives = {o for s in srs for o in (s.get("linked_objectives") or [])}

    if args.report:
        print(f"SRs with at least one QNRCS anchor : {len(srs)}")
        print(f"objectives reachable via those SRs  : {len(objectives)}")
        print(f"QNRCS measures reached              : {len(covered)} of {len(measures)}")
        by_reg: dict[str, int] = {}
        for s in srs:
            by_reg[s["regulation"]] = by_reg.get(s["regulation"], 0) + 1
        print("by regulation:", ", ".join(f"{k}={v}" for k, v in sorted(by_reg.items())))
        print(f"measures NOT reached: {len(measures) - len(covered)}")
        return 0

    if args.check:
        if not OUT.is_file():
            print(f"missing: {OUT}")
            return 2
        stored = json.loads(OUT.read_text(encoding="utf-8"))
        if stored.get("srs") != derived["srs"]:
            print(f"STALE: {OUT} does not match what the derivation produces now")
            return 1
        print(f"current: {OUT}")
        return 0

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(derived, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"written: {OUT}")
    print(f"  {len(srs)} SR(s), {len({c for s in srs for c in s['qnrcs']})} QNRCS measure(s) reached")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
