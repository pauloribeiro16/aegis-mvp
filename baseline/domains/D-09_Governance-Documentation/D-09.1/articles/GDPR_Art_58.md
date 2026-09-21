---
document_id: AEGIS-PREPROC-GDPR-ART-58
title: GDPR Art. 58 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 58
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.2.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.2.md
status: DRAFT
---

# GDPR Art. 58

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

_No standalone SO row cites this article directly (covered via the rules below)._

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-044
  title: "Continuous evidence-of-compliance with performance review"
  source_clauses:
    - { clause_id: GDPR-CL07, article_ref: "Art. 5(2) — accountability" }
    - { clause_id: GDPR-CP01, article_ref: "Art. 24(1) — demonstrate compliance (cross)" }
    - { clause_id: GDPR-CP12, article_ref: "Art. 30(1) — records of processing (cross)" }
  linked_objectives: [SO-GDPR-027]
  sub_domain: [D-09.1, D-10.2]
  nist_csf_mapping:
    - { id: GV.PO-02, title: "Cybersecurity processes and procedures for implementing the cybersecurity policy are established, communicated, and enforced" }
    - { id: GV.OV-03, title: "Organizational cybersecurity performance is evaluated and reviewed for needed adjustments" }
  applies_to_role: [CONTROLLER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 5(2) requires the controller to be responsible for, and able to
    demonstrate, compliance with the Art. 5(1) principles (lawfulness,
    fairness and transparency; purpose limitation; data minimisation;
    accuracy; storage limitation; integrity and confidentiality; and
    accountability). Art. 24(1) extends the demonstrability requirement
    to all GDPR compliance, not just Art. 5(1). Art. 30(1) supplies the
    supporting evidence instrument in the form of the records of
    processing. The three provisions together create the accountability-
    and-evidence chain that grounds the entire supervisory-authority
    enforcement regime (Art. 58 powers of investigation; Art. 83
    administrative fines).
  security_rationale: |
    The obligation in Art. 5(2), Art. 24(1) and Art. 30(1) to be able to demonstrate, on a continuous basis, that the controller is complying with the Art. 5(1) principles and with the rest of GDPR, and to maintain the records of processing as the supporting evidence instrument, is operationalised in NIST CSF 2.0 through **GV.PO-02 (Cybersecurity processes and procedures for implementing the cybersecurity policy are established, communicated, and enforced)** and **GV.OV-03 (Organizational cybersecurity performance is evaluated and reviewed for needed adjustments)**.
    GV.PO-02 captures the procedural-evidence backbone: the controller must maintain evidence-generating processes — RoPA entries, DPIA artefacts, audit logs, training records, breach-response records — on a continuous basis, because the demonstrability threshold set by Art. 5(2) and Art. 24(1) is not a point-in-time promise but a standing capability.
    GV.OV-03 captures the evaluated-and-reviewed-correction dimension that converts raw evidence into accountability: the controller's performance against the cybersecurity and data-protection objectives must be measured and adjusted, with the adjustments materialising as refreshed policies, processes and procedures rather than as isolated interventions.
    A controller that documents GV.PO-02 continuous-evidence processes and GV.OV-03 performance-evaluation-and-correction cadence can demonstrate ex post, against the Art. 5(2) accountability duty, that on the day of any supervisory inspection the controller could produce evidence of compliance across the entire Art. 5(1) principles chain and the broader GDPR surface that Art. 24(1) reaches.
  ambiguity_notes: |
    `able to demonstrate` carries Berry-flagged VAG-S3 (Berry §5.1) on
    the threshold of evidence sufficient. The reading adopted for this
    SR is the continuous-evidentiary-trail reading: logs, audit reports,
    certifications, DPIA artefacts, RoPA entries, training records and
    breach-response records, all preserved on a continuous basis per
    EDPB Guidelines on accountability 07/2019. Two alternative readings
    remain. First, a point-in-time reading that treats `able to
    demonstrate` as satisfied by the existence of policies without
    evidence of operation would lose the substantive protection the
    accountability principle is meant to provide. Second, an annual-
    evidence reading that aggregates evidence only at supervisory-
    authority-request time would conflict with the continuous-monitoring
    expectations of EDPB Guidelines 07/2019. Remain open: (a) whether
    internal audit reports fall under legal-professional privilege for
    accountability purposes or must be disclosed to supervisory
    authorities on request; (b) whether the demonstrability threshold
    differs between Art. 5(2) (principles compliance) and Art. 24(1)
    (full GDPR compliance).
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

