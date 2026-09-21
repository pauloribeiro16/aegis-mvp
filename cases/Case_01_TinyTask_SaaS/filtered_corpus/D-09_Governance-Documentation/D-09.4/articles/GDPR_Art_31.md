---
document_id: AEGIS-PREPROC-GDPR-ART-31
title: GDPR Art. 31 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 31
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.4.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.4.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.2.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.2.md
status: DRAFT
---

# GDPR Art. 31

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-GDPR-031 | Compliance records (records of processing, consent records, processor contract records, breach notification records, DPIA records) are maintained in writing or in electronic form with integrity and traceability sufficient to demonstrate compliance and to support supervisory-authority inspections. | `GDPR-CP12` (Art. 30(3)); `GDPR-CL07` (Art. 5(2) — accountability / demonstrability); `GDPR-CP14` (Art. 31 — SA cooperation) | D-10.2, D-09.4 |
| SO-GDPR-031 | D-10.2, D-09.4 | Art. 30(3), Art. 5(2), Art. 31 | Audit-grade records integrity and traceability |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-050
  title: "Integrity-preserved RoPA records available to supervisory authority"
  source_clauses:
    - { clause_id: GDPR-CP12, article_ref: "Art. 30(3) — in writing/electronic form" }
    - { clause_id: GDPR-CL07, article_ref: "Art. 5(2) — accountability (cross)" }
    - { clause_id: GDPR-CP14, article_ref: "Art. 31 — supervisory authority cooperation" }
  linked_objectives: [SO-GDPR-031]
  sub_domain: [D-10.2, D-09.4]
  nist_csf_mapping:
    - { id: PR.PS-04, title: "Log records are generated and made available for continuous monitoring and analysis" }
    - { id: DE.AE-03, title: "Event data are collected and correlated from multiple sources and sensors" }
    - { id: RS.AN-07, title: "Incident data and metadata are collected, and their integrity and provenance are preserved" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 30(3) requires the records referred to in paragraphs 1 and 2
    to be in writing, including in electronic form. Art. 5(2)
    accountability requires the controller to demonstrate compliance;
    the records are the primary evidence. Art. 31 requires cooperation
    with the supervisory authority, on request, in the performance of
    its tasks, including on inspection. The three provisions together
    set the integrity and availability baseline for the RoPA itself.
  security_rationale: |
    The obligation in Art. 30(3), Art. 5(2) and Art. 31 to keep the records of processing in writing (including in electronic form), to treat them as the primary evidence supporting the Art. 5(2) accountability duty, and to make them available to the supervisory authority on request under the Art. 31 cooperation duty, is operationalised in NIST CSF 2.0 through **PR.PS-04 (Log records are generated and made available for continuous monitoring and analysis)**, **DE.AE-03 (Event data are collected and correlated from multiple sources and sensors)** and **RS.AN-07 (Incident data and metadata are collected, and their integrity and provenance are preserved)**.
    PR.PS-04 captures the record-generation discipline: each RoPA entry must be generated and made available as log-grade record material, with continuous monitoring and analysis over it, rather than as a static document that ages between inspections.
    DE.AE-03 captures the multi-source correlation discipline: where the RoPA is maintained across multiple systems, the records must be collectable and correlatable into a single supervisory-authority-presentable view, so that Art. 31 cooperation does not stall on data-source fragmentation.
    RS.AN-07 captures the integrity-and-provenance discipline: records that the supervisory authority relies on must be tamper-evident and provenance-preserving, so that any update between inspections leaves a chain that supports the Art. 5(2) demonstrability requirement rather than weakens it.
    A controller or processor that documents PR.PS-04 log-grade RoPA generation, DE.AE-03 cross-source correlation and RS.AN-07 integrity-preservation discipline can demonstrate ex post, against the Art. 5(2) accountability duty, that on the day of any supervisory inspection the records were complete, current and integrity-preserved, satisfying the Art. 31 cooperation duty without reconstruction effort.
  ambiguity_notes: |
    `in writing, including in electronic form` is unambiguous; no S3
    ambiguity registered.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

