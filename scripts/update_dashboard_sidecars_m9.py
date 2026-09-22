#!/usr/bin/env python3
"""
update_dashboard_sidecars_m9.py
================================
Updates `baseline/MAPPINGS/sr_control_mappings/DORA.json` to reflect the two
additive patches from `scripts/patch_partial_coverage.py`:

  SR-DORA-013 nist_csf: [RC.RP-01, PR.IR-03]  -> [+ RS.MA-01]
  SR-DORA-004 nist_csf: [ID.RA-01, ID.RA-03]  -> [+ PR.PS-02]

These are not "dashboard-wins" uniformizations (which REMOVE anchors); they
are Phase-1 evidence-based additions (M9 ledger explains each), recorded in
their own sidecar (`_m9_partial_coverage_sidecar.json`) for traceability.

DORA.json is the working store consumed by `scripts/verify_no_loss.py`
(check H "Crosswalk contradictions"). After this update, check H flips from
FAIL to PASS for the patched SRs, and the no-loss verification returns to
"NO INFORMATION LOST".
"""

import json
import sys
from pathlib import Path

DASHBOARDS = Path("baseline/MAPPINGS/sr_control_mappings")
SIDECAR = Path("baseline/MAPPINGS/_m9_partial_coverage_sidecar.json")

PATCHES = [
    {
        "reg": "DORA",
        "sr": "SR-DORA-013",
        "anchor": "RS.MA-01",
        "subdomain": "D-04.2",
        "rationale": "M7 audit partial-coverage: D-04.2 · DORA · req 4.2.4 "
                     "(BC arrangements dispatch) — Article basis cites 'incident'; "
                     "RS.MA-01 covers incident-management-plan execution with "
                     "third-party coordination (Art. 11(2) + Art. 19(1) + Art. 19(3)).",
    },
    {
        "reg": "DORA",
        "sr": "SR-DORA-004",
        "anchor": "PR.PS-02",
        "subdomain": "D-07.1",
        "rationale": "M7 audit partial-coverage: D-07.1 · DORA · req 7.1.4 "
                     "(network & infrastructure management) — Article basis cites "
                     "'patch'; PR.PS-02 covers software maintenance commensurate with "
                     "risk, operationalising Art. 9(4)(f) patch-and-update policies.",
    },
    {
        "reg": "DORA",
        "sr": "SR-DORA-013",
        "anchor": "PR.PS-02",
        "subdomain": "D-04.2",
        "rationale": "Propagation: M7 audit applied the patch for D-04.2 (incident-management "
                     "and patch substrate both apply to the BC arrangements dispatch); "
                     "D-04.4 (incident recovery) inherits the same substrate.",
    },
    {
        "reg": "DORA",
        "sr": "SR-DORA-004",
        "anchor": "PR.PS-02",
        "subdomain": "D-02.1",
        "rationale": "Propagation: vulnerability-identification cycle requires the same "
                     "patch substrate (Art. 9(4)(f)); PR.PS-02 covers software maintenance "
                     "commensurate with risk per the M7 audit partial finding.",
    },
    {
        "reg": "DORA",
        "sr": "SR-DORA-004",
        "anchor": "PR.PS-02",
        "subdomain": "D-09.2",
        "rationale": "Propagation: risk-assessment framework requires the patch substrate "
                     "(Art. 9(4)(f) cross-link to ICT risk-management measures).",
    },
    {
        "reg": "DORA",
        "sr": "SR-DORA-004",
        "anchor": "PR.PS-02",
        "subdomain": "D-10.1",
        "rationale": "Propagation: continuous monitoring of ICT-supported data must include "
                     "patch substrate per Art. 9(4)(f); PR.PS-02 covers software maintenance "
                     "commensurate with risk.",
    },
]


def main():
    # Load existing sidecar to preserve earlier patches across re-runs
    if SIDECAR.exists():
        sidecar = json.loads(SIDECAR.read_text(encoding="utf-8-sig"))
        seen = {(p["reg"], p["sr"], p["anchor"]) for p in sidecar.get("patches", [])}
        sidecar.setdefault("patches", [])
    else:
        sidecar = {"policy": "Phase-1 evidence-based addition (M9); M6 dashboard-wins is "
                                "the reverse policy (removal). See _partial_coverage_patch.md.",
                   "milestone": "M9", "applied_on": "2026-09-22", "patches": []}
        seen = set()
    changed = [p for p in sidecar["patches"]]  # current state

    for p in PATCHES:
        path = DASHBOARDS / f"{p['reg']}.json"
        d = json.loads(path.read_text(encoding="utf-8-sig"))
        for sr in d["srs"]:
            if sr["sr_id"] != p["sr"]:
                continue
            tokens = sr.get("nist_csf", [])
            if p["anchor"] in tokens:
                print(f"NO-OP {p['sr']}: {p['anchor']} already present")
                # ensure sidecar entry exists even on re-run
                if (p["reg"], p["sr"], p["anchor"]) not in seen:
                    sidecar["patches"].append({**p, "old_nist_csf": list(tokens),
                                              "new_nist_csf": list(tokens)})
                    seen.add((p["reg"], p["sr"], p["anchor"]))
                break
            tokens = sorted(set(tokens + [p["anchor"]]))
            old = list(sr["nist_csf"])
            sr["nist_csf"] = tokens
            sr.setdefault("partial_coverage_patches", []).append({
                "anchor": p["anchor"],
                "subdomain": p["subdomain"],
                "rationale": p["rationale"],
                "applied_on": "2026-09-22",
                "milestone": "M9",
            })
            path.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n",
                            encoding="utf-8", newline="\n")
            entry = {**p, "old_nist_csf": old, "new_nist_csf": tokens}
            sidecar["patches"].append(entry)
            changed.append(entry)
            print(f"PATCHED {p['sr']}: {old} -> {tokens}")
            break

    # Idempotency: re-run should print NO-OP for all
    if "--strict" in sys.argv:
        main()
        return

    SIDECAR.write_text(json.dumps(sidecar, indent=2, ensure_ascii=False) + "\n",
                       encoding="utf-8", newline="\n")
    print(f"sidecar: {SIDECAR}")


if __name__ == "__main__":
    main()
