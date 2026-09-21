---
document_id: AEGIS-PREPROC-CRA-ART-12
title: CRA Art. 12 — SecurityObjectives & SecurityRules
regulation: CRA
article: Art. 12
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
status: DRAFT
---

# CRA Art. 12

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-CRA-073 | ENISA establishes and maintains the single reporting platform via which the notifications of Arts. 14 and 15 are submitted, and takes appropriate and proportionate measures to secure the platform; the platform supports electronic notification end-points of CSIRTs designated as coordinators and ENISA, and is accessible simultaneously to ENISA when notification is submitted via a CSIRT end-point. | `CRA-CL74` (Art. 16(1) — ENISA single reporting platform); `CRA-CL77` (Art. 16(4) — platform security); `CRA-CL82` (Art. 17(5) — EU vulnerability database integration with NIS 2 Art. 12(2)); `CRA-CL78` (Art. 17(1) — EU-CyCLONe submission); `CRA-CL80` (Art. 17(3) — ENISA biennial report on cybersecurity risks) | D-09.4 |
| SO-CRA-074 | ENISA prepares a biennial report on cybersecurity risks in products with digital elements and maintains the EU vulnerability database (Art. 12(2) NIS 2); CSIRTs designated as coordinators provide helpdesk support to manufacturers on the reporting obligations. | `CRA-CL80` (Art. 17(3) — ENISA biennial report); `CRA-CL82` (Art. 17(5) — EU vulnerability database — writes back to NIS 2 Art. 12(2)); `CRA-CL83` (Art. 17(6) — CSIRT helpdesk for manufacturers) | D-09.4 |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-114
  title: "ENISA biennial report, EU vulnerability database, CSIRT helpdesk"
  source_clauses:
    - { clause_id: CRA-CL76, article_ref: "Art. 16(3) — CSIRT provides notification info to market-surveillance authorities" }
    - { clause_id: CRA-CL80, article_ref: "Art. 17(3) — ENISA biennial report on cybersecurity risks in products" }
    - { clause_id: CRA-CL82, article_ref: "Art. 17(5) — EU vulnerability database (writes back to NIS 2 Art. 12(2))" }
    - { clause_id: CRA-CL83, article_ref: "Art. 17(6) — CSIRT helpdesk for manufacturers on reporting obligations" }
  linked_objectives: [SO-CRA-073, SO-CRA-074]
  sub_domain: [D-09.4]
  nist_csf_mapping:
    - { id: RS.CO-04, title: "Coordination with stakeholders occurs consistent with applicable rules and regulations" }
    - { id: ID.IM-04, title: "Cybersecurity risk management improvements are informed by awareness of related developments and context (e.g., threat intelligence, incidents, technology evolution)" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 16(3) provides that CSIRTs designated as coordinators shall
    provide notification information to the relevant market-surveillance
    authorities. Article 17(3) requires ENISA to prepare a biennial
    report on cybersecurity risks in products with digital elements.
    Article 17(5) requires ENISA to add publicly known vulnerabilities
    to the EU vulnerability database established under NIS 2 Article
    12(2). Article 17(6) requires CSIRTs designated as coordinators to
    provide helpdesk support to manufacturers on the reporting
    obligations under Articles 14 and 15 [Recital 38, Recital 39].
  security_rationale: |
    The Art. 16(3)/17(3)/(5)/(6) ENISA-CSIRT coordination cluster is
    operationalised in NIST CSF 2.0 through RS.CO-04 and ID.IM-04.
    RS.CO-04 (Coordination with stakeholders occurs consistent with
    applicable rules and regulations) anchors the multi-institutional
    coordination posture — CSIRTs pass notification information to
    MSAs (Art. 16(3)) and ENISA populates the EU vulnerability database
    (Art. 17(5)). ID.IM-04 (Cybersecurity risk management improvements
    are informed by awareness of related developments and context)
    anchors the improvement-loop input that the biennial report
    (Art. 17(3)) and the vulnerability database provide — the
    manufacturer's risk-assessment refresh can cite ENISA's outputs
    as evidence of current threat context. Together, RS.CO-04 and
    ID.IM-04 give the cluster a coordination-and-improvement control
    set that lets the manufacturer consume ENISA outputs in its own
    Art. 13(2) risk picture and demonstrate ex post that those outputs
    were considered.
  ambiguity_notes: |
    "Biennial" reads literally as every two years. "Publicly known
    vulnerabilities" reads as already publicly disclosed vulnerabilities
    — the database is curation rather than original publication; the
    threshold is ENISA's curated-vs-undisclosed judgement. The
    helpdesk support is a guidance channel rather than a binding
    interpretation service: written ENISA guidance and the formal
    Regulation text remain the controlling sources.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

