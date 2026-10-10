#!/usr/bin/env python3
"""aegis_pipeline.phases.phase2.principles — 7 architectural secure-design principles."""

from __future__ import annotations

import json
import re
from pathlib import Path

UNSET = "—"

PREFIX_BY_REG = {"GDPR": "PO"}
SCOPE_BY_REG = {
    "GDPR": "Personal Data Scope",
    "CRA": "Product & Software Security Scope",
    "NIS2": "Network & Information Systems Scope",
    "DORA": "ICT Risk Scope",
    "AI_Act": "High-Risk AI System Scope",
}

REG_ORDER = ["GDPR", "CRA", "NIS2", "DORA", "AI_Act"]

CATEGORIES = [
    {
        "n": 1,
        "title": "Architectural & Data Flow Modeling",
        "sec": "§2",
        "def_col": "Architectural Definition",
        "con_col": "Diagrammatic & Modeling Constraint",
        "domain": "System Architecture, Data Flow Diagrams (DFD), Component Topology, and Network Boundaries.",
        "lit": "Adam Shostack (2014, *Threat Modeling: Designing for Security*); Jerome Saltzer & Michael Schroeder (1975).",
    },
    {
        "n": 2,
        "title": "Core Systems & Access Security",
        "sec": "§3",
        "def_col": "Security Definition",
        "con_col": "Architectural & Operational Constraint",
        "domain": "System-wide access control, failure state handling, and resource isolation.",
        "lit": "Jerome Saltzer & Michael Schroeder (1975, *The Protection of Information in Computer Systems*); OWASP.",
    },
    {
        "n": 3,
        "title": "Requirements Engineering & Verifiability",
        "sec": "§4",
        "def_col": "Requirements Engineering Definition",
        "con_col": "Specification Constraint",
        "domain": "Specification of system behaviors, verification criteria, and lifecycle traceability.",
        "lit": "ISO/IEC/IEEE 29148:2018; INCOSE Guide to Writing Requirements; EARS (Mavin et al., 2009).",
    },
    {
        "n": 4,
        "title": "Privacy by Design & Data Lifecycle",
        "sec": "§5",
        "def_col": "Privacy Engineering Definition",
        "con_col": "Operational & Diagrammatic Constraint",
        "domain": "Personal data lifecycle, data-subject sovereignty, and purpose-bound processing.",
        "lit": "Ann Cavoukian (2009, *Privacy by Design: 7 Foundational Principles*); GDPR Art. 5, 17, 25; ISO/IEC 27701:2019.",
    },
]

PRINCIPLES = [
    {
        "id": "PRIN-ENG-01",
        "category": 1,
        "skill": "trust-boundary-analysis",
        "name": "Explicit Trust Boundaries & Complete Mediation",
        "source": "Shostack (2014) / Saltzer & Schroeder (1975)",
        "definition": "Every interface separating zones of differing privilege must be visually demarcated, and every crossing flow must be authenticated and validated with zero unmediated bypasses.",
    },
    {
        "id": "PRIN-ENG-02",
        "category": 1,
        "skill": "attack-surface-analysis",
        "name": "Attack Surface Minimization & Peripheral Resilience",
        "source": "Howard & LeBlanc (2003) / Schneier (2000)",
        "definition": "Accessible entry points, communication channels, and active interfaces must be reduced to the minimum necessary, and auxiliary ingress hooks must match core security intensity.",
    },
    {
        "id": "PRIN-ENG-03",
        "category": 2,
        "skill": "least-privilege-analysis",
        "name": "Least Privilege & Mechanism Isolation",
        "source": "Saltzer & Schroeder (1975)",
        "definition": "Every principal (user, service, background worker) must operate with the minimum privileges necessary, and distinct tenants or sensitivity levels must not share unisolated execution mechanisms.",
    },
    {
        "id": "PRIN-ENG-04",
        "category": 2,
        "skill": "fail-safe-defaults-analysis",
        "name": "Fail-Safe Defaults & Closed Failure States",
        "source": "Saltzer & Schroeder (1975) / OWASP",
        "definition": "Access decisions and state transitions must default to refusal, and unexpected failures or exceptions must terminate in a secure closed state without state corruption or data leakage.",
    },
    {
        "id": "PRIN-ENG-05",
        "category": 3,
        "skill": "verifiability-analysis",
        "name": "Requirement Verifiability & Atomicity",
        "source": "ISO/IEC/IEEE 29148:2018 / EARS (2009)",
        "definition": "Every security and privacy requirement must be atomic (one single condition and response) and possess a deterministic, automated pass/fail verification method.",
    },
    {
        "id": "PRIN-ENG-06",
        "category": 4,
        "skill": "data-minimization-analysis",
        "name": "Proactive Data Minimization & Scoped Projection",
        "source": "Cavoukian (2009) / GDPR Art. 5(1)(c)",
        "definition": "Only data strictly indispensable for fulfilling the declared service purpose may be collected, transmitted, or retained, and egress models must project strictly scoped data views.",
    },
    {
        "id": "PRIN-ENG-07",
        "category": 4,
        "skill": "lifecycle-erasure-analysis",
        "name": "End-to-End Lifecycle Security & Irreversible Erasure",
        "source": "Cavoukian (2009) / GDPR Art. 17",
        "definition": "Protection covers the entire data lifecycle; data subject to erasure must be permanently destroyed across edge caches, primary stores, archives, and disaster-recovery copies.",
    },
]

PRINCIPLE_IDS = [p["id"] for p in PRINCIPLES]

STOPWORDS = {
    "the", "and", "for", "with", "that", "this", "from", "every",
    "must", "may", "its", "any", "all", "not", "are", "their",
    "each", "which", "when", "where", "only", "into", "than", "then",
}


def principles_for(run_dir: Path) -> list[dict]:
    """Return the 7 principles with per-case generative cells merged in."""
    merged = [dict(p) for p in PRINCIPLES]
    synth_path = run_dir / "steps" / "principles.json"
    if not synth_path.exists():
        for p in merged:
            p["constraint"] = UNSET
            p["method_lead"] = UNSET
            p["eval_scope"] = UNSET
        return merged
    synth = {r["id"]: r for r in json.loads(synth_path.read_text(encoding="utf-8")).get("principles", [])}
    for p in merged:
        row = synth.get(p["id"], {})
        p["constraint"] = row.get("constraint") or UNSET
        p["method_lead"] = row.get("method_lead") or UNSET
        p["eval_scope"] = row.get("eval_scope") or UNSET
    return merged


def grounding_ratio(principles: list[dict], fact_sheet: str) -> float:
    """Fraction of substantive tokens in the constraints that trace to fact sheet."""
    def_tokens = {
        w
        for p in PRINCIPLES
        for w in re.findall(r"[a-z]{3,}", p["definition"].lower())
        if w not in STOPWORDS
    }
    fact_tokens = {
        w
        for w in re.findall(r"[a-z]{3,}", (fact_sheet or "").lower())
        if w not in STOPWORDS and w not in def_tokens
    }
    con_tokens = [
        w
        for p in principles
        for w in re.findall(r"[a-z]{3,}", (p.get("constraint") or "").lower())
        if w not in STOPWORDS and w not in def_tokens and w != UNSET
    ]
    if not con_tokens or not fact_tokens:
        return 0.0
    grounded = sum(1 for w in con_tokens if w in fact_tokens)
    return round(grounded / len(con_tokens), 3)
