# Phase 2 — Operationalization & Secure Design Rules (Case 03 — OmniBank Financial Systems)

> **Phase Mission:** Bridge Phase 1 contextual intent into testable, assignable **Operational Objectives** and **Technology-Class Secure Design Rules**, maintaining technology neutrality until architecture and use cases are specified in Phase 3.

## 1. Phase Context & Pipeline Contract

Under **ADR-004** and **ADR-002**:
- **Input:** Phase 1 Adjusted Goals (`../01_PHASE1_CONTEXT/Doc02_Adjusted_Goals.md`) — 103 AGs, 38/38 sub-domains, five regulations (GDPR, CRA, NIS 2, DORA, AI Act), LARGE banking entity.
- **Exchange Unit:**
  1. **Operational Objectives** (`Doc01_Operational_Objectives.md`): 103 PO-/SO- rows with verification criteria, methods, owners and published CSF anchor sets; five harmonised tensions.
  2. **Secure Design & Systems Engineering Principles** (`Doc02_Secure_Design_Principles.md`): the 7 transversal principles (`PRIN-ENG-01..07`) with 1:1 skills mapping.
- **Handoff to Phase 3:** objectives + principles are the verifiable boundary constraints and modeling grammar; Phase 3 Part 1 maps them onto the functional model through the exhaustive coverage matrix and the risk-acceptance rounds (ADR-005), then selects controls explicitly (Step 4).

## 2. Directory Layout

```text
cases/Case_03_OmniBank/02_PHASE2_RULES/
├── README.md                          # Phase overview and pipeline contract
├── Doc01_Operational_Objectives.md    # The Regulatory Spine (38 sub-domains, 5 regulations, 5 tensions)
└── Doc02_Secure_Design_Principles.md  # The Engineering Spine (7 transversal principles across 4 categories)
```

## 3. Key Design Choices & Integrity Rules

1. **Technology Neutrality (R5):** objectives state *what* verifiable property must hold, never the stack.
2. **Proportionality (R3):** LARGE-scale banking — in-house key custody, dedicated SOC/CSIRT, DORA resilience-testing program, AI conformity file; no inherited-consumer-tier simplifications.
3. **Harmonised Tensions:** five (notification clocks, erasure vs financial-record/AI-log retention, unified risk assessment, vendor management incl. the DORA register, provider/deployer duty stacking).
