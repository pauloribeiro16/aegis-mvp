# Phase 2 — Operationalization & Secure Design Rules (Case 02 — SecureBorder Solutions)

> **Phase Mission:** Bridge Phase 1 contextual intent into testable, assignable **Operational Objectives** and **Technology-Class Secure Design Rules**, maintaining technology neutrality until architecture and use cases are specified in Phase 3.

---

## 1. Phase Context & Pipeline Contract

Under **ADR-004 (Pipeline I/O Contract)** and **ADR-002 (TECHNOLOGY-only MVP Scope)**:
- **Input:** Phase 1 Adjusted Goals (`cases/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT/Doc02_Adjusted_Goals.md`), establishing regulatory obligations (GDPR + CRA + NIS 2 + AI Act) tailored to SecureBorder's scale (MEDIUM tier, 450 employees, critical-infrastructure supplier of AI-enabled border-control gates).
- **Exchange Unit:** Phase 2 produces:
  1. **Operational Objectives** (`Doc01_Operational_Objectives.md`): Privacy and Security Operational Objectives (`PO-` and `SO-D-XX.Y-NNN`), formulated under ISO/IEC 27001:2022 clause 6.2 discipline (measurable criteria, assignable owners, evaluation methods), across 100 objectives separating the four regulatory ambits.
  2. **Secure Design & Systems Engineering Principles** (`Doc02_Secure_Design_Principles.md`): Transversal, technology-agnostic engineering principles (Shostack, Saltzer & Schroeder, ISO 29148, Cavoukian) governing architectural diagramming, trust boundaries, requirements engineering, and privacy by design.
- **Handoff to Phase 3:** These operational objectives and transversal principles establish the verifiable boundary constraints and modeling grammar for the system. When engineering defines the software architecture, technology classes, and use cases (`UC-*`), Phase 3 maps them to granular implementation controls and specialized agentic skills.

---

## 2. Directory Layout

```text
cases/Case_02_SecureBorder_Solutions/02_PHASE2_RULES/
├── README.md                          # Phase overview and pipeline contract
├── Doc01_Operational_Objectives.md     # The Regulatory Spine (35 sub-domains, PO/SO objectives & tensions)
└── Doc02_Secure_Design_Principles.md   # The Engineering Spine (7 transversal principles across 4 categories)
```

---

## 3. Key Design Choices & Integrity Rules

1. **Technology Neutrality (Rule R5):** Objectives and rules specify *what* verifiable security property must hold across the system boundary, without prematurely assuming concrete software stacks or product names.
2. **Proportionality (Rule R3):** SecureBorder operates a certified management system, a 24/7 in-house security operations centre, hardware-backed key custody, and a signed-release pipeline — the objectives leverage these in-house capabilities rather than assuming managed third-party primitives.
3. **Four-Regulation Ambit Separation:** GDPR (personal data), CRA (product security), NIS 2 (network and information systems of the essential entity), and AI Act (high-risk AI lifecycle) bind distinct operational ambits per sub-domain; no objective conflates two ambits.
4. **Harmonized Strategic Tensions:** Where regulations impose divergent operational tempos (T-001 notification timing: 24h CRA/NIS 2 vs 72h GDPR vs 15-day AI Act; T-002 erasure vs AI log retention; T-003 unified DPIA/FRIA/risk assessment; T-004 three-regime vendor scope), Phase 2 harmonizes the response around unified mechanisms bound in the objective tables.
