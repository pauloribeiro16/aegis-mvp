# Phase 2 — Operationalization & Secure Design Rules (Case 01 — TinyTask SaaS)

> **Phase Mission:** Bridge Phase 1 contextual intent into testable, assignable **Operational Objectives** and **Technology-Class Secure Design Rules**, maintaining technology neutrality until architecture and use cases are specified in Phase 3.

---

## 1. Phase Context & Pipeline Contract

Under **ADR-004 (Pipeline I/O Contract)** and **ADR-002 (TECHNOLOGY-only MVP Scope)**:
- **Input:** Phase 1 Adjusted Goals (`cases/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT/Doc02_Adjusted_Goals.md`), establishing regulatory obligations (GDPR + CRA) tailored to TinyTask's scale (MICRO tier, 8 employees, B2B cloud SaaS).
- **Exchange Unit:** Phase 2 produces:
  1. **Operational Objectives** (`Doc01_Operational_Objectives.md`): Privacy and Security Operational Objectives (`PO-` and `SO-D-XX.Y-NNN`), formulated under ISO/IEC 27001:2022 clause 6.2 discipline (measurable criteria, assignable owners, evaluation methods).
  2. **Secure Design & Systems Engineering Principles** (`Doc02_Secure_Design_Principles.md`): Transversal, technology-agnostic engineering principles (Shostack, Saltzer & Schroeder, ISO 29148, Cavoukian) governing architectural diagramming, trust boundaries, requirements engineering, and privacy by design.
- **Handoff to Phase 3:** These operational objectives and transversal principles establish the verifiable boundary constraints and modeling grammar for the system. When engineering defines the software architecture, tech stack (e.g. database model, API protocols), and use cases (`UC-*`), Phase 3 maps them to granular implementation controls and specialized agentic skills.

---

## 2. Directory Layout

```text
cases/Case_01_TinyTask_SaaS/02_PHASE2_RULES/
├── README.md                          # Phase overview and pipeline contract
├── Doc01_Operational_Objectives.md     # The Regulatory Spine (35 sub-domains, PO/SO objectives & tensions)
└── Doc02_Secure_Design_Principles.md   # The Engineering Spine (7 transversal principles across 4 categories)
```

---

## 3. Key Design Choices & Integrity Rules

1. **Technology Neutrality (Rule R5):** Objectives and rules specify *what* verifiable security property must hold across the system boundary, without prematurely assuming concrete software stacks (e.g. SQL vs NoSQL, REST vs gRPC, specific HTTP header names).
2. **Proportionality (Rule R3):** TinyTask leverages managed cloud services for underlying infrastructure (managed cryptographic custody, managed patching, automated backups) rather than operating custom PKI or dedicated security operations centers.
3. **Harmonized Strategic Tensions:** Where GDPR and CRA impose divergent operational tempos (e.g. incident reporting timelines: 24h CRA vs 72h GDPR), Phase 2 harmonizes the response around a unified incident triage mechanism routing to the most restrictive deadline.
