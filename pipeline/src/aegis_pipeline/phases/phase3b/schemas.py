"""aegis_pipeline.phases.phase3b.schemas — the shapes Phase 3 Part 2 agrees on.

Part 2 judges the system that Part 1 specified: assets, flows, trust
boundaries; STRIDE/LINDDUN threats with the risk arithmetic computed in
PYTHON, never trusted to model prose; ADTree broken-path proofs; and the
human risk round the model can propose but never decide (the golden rule).
"""
from __future__ import annotations

import json
import re
from pathlib import Path

UNSET = "—"

#: The threat id shapes, one per family in `baseline/THREATS/_index.json`.
RE_THREAT_IDS = {
    "CWE": re.compile(r"\bCWE-\d+\b"),
    "CAPEC": re.compile(r"\bCAPEC-\d+\b"),
    "ATTACK": re.compile(r"\bT\d{4}(?:\.\d{3})?\b"),
    "D3FEND": re.compile(r"\bD3-[A-Z]{2,6}\b"),
    "ATLAS": re.compile(r"\bAML\.T\d{4}(?:\.\d{3})?\b"),
    "EMB3D": re.compile(r"\bTID-\d+\b"),
}

#: The STRIDE and LINDDUN categories, as the fichas teach them.
STRIDE = ("Spoofing", "Tampering", "Repudiation", "Information disclosure",
          "Denial of service", "Elevation of privilege")
LINDDUN = ("Linkability", "Identifiability", "Non-repudiation",
           "Detectability", "Information disclosure", "Non-compliance")

#: The mitigation verdicts over Part 1's requirements.
MITIGATION = ("FULL_MITIGATION", "PARTIAL_MITIGATION", "UNMITIGATED_GAP")

#: The five human risk decisions (the plan's Etapa 2.4). The model NEVER
#: writes one of these — `risk_verdicts.json` is human-exclusive.
RISK_DECISIONS = (
    "Accept_Mitigated",
    "Accept_Residual_Risk",
    "Transfer",
    "Avoid",
    "Reject_Risk_Require_Mitigation",
)

#: The decisions a non-mitigated STATUTORY threat may never receive (G9).
STATUTORY_FORBIDDEN = ("Accept_Residual_Risk", "Transfer")


def risk_level(score: int) -> str:
    """The measured bands: Low 1-4, Medium 5-9, High 10-15, Critical 16-25."""
    if score >= 16:
        return "Critical"
    if score >= 10:
        return "High"
    if score >= 5:
        return "Medium"
    return "Low"


def threat_index(run_dir: Path, repo: Path) -> dict:
    """The catalog T8 checks against: the run's copy, else the repo's."""
    for path in (run_dir / "steps" / "phase3b" / "threat_index.json",
                 repo / "baseline" / "THREATS" / "_index.json"):
        if path.is_file():
            return json.loads(path.read_text(encoding="utf-8"))
    return {"entries": {}}


def check_threat_ids(text: str, index: dict) -> list[str]:
    """T8 — every cited threat id must exist in the catalog. Zero invented."""
    entries = index.get("entries", {})
    findings = []
    for family, rx in RE_THREAT_IDS.items():
        for tid in sorted(set(rx.findall(text or ""))):
            if tid not in entries:
                findings.append(f"{family} id {tid} is not in baseline/THREATS (T8)")
    return findings


def residual_from_mitigation(l_inh: int, i_inh: int, assessment: str) -> tuple[int, int]:
    """The deterministic residual. No magic risk reduction.

    FULL_MITIGATION lowers both axes by 2 (bounded at 1); PARTIAL by 1;
    an unmitigated gap lowers NOTHING — a requirement that does not exist
    cannot reduce a risk, which is the measured way a register lies.
    """
    if assessment == "FULL_MITIGATION":
        return max(1, l_inh - 2), max(1, i_inh - 2)
    if assessment == "PARTIAL_MITIGATION":
        return max(1, l_inh - 1), max(1, i_inh - 1)
    return l_inh, i_inh
