---
document_id: AEGIS-PREPROC-GDPR-ART-24
title: GDPR Art. 24 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 24
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-01_Data-Protection/D-01.1.md
  - ../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.1.md
  - ../../CrossRegulation/DomainAnalysis/D-01_Data-Protection/D-01.4.md
  - ../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.4.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.2.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.2.md
status: DRAFT
---

# GDPR Art. 24

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-GDPR-026 | The controller implements appropriate data-protection policies, reviewed and updated where necessary in light of the nature, scope, context and purposes of processing, the risks of varying likelihood and severity, and the cost of implementation. | `GDPR-CP01` (Art. 24(1)); `GDPR-CP01` (Art. 24(2) — data-protection policies where proportionate) | D-09.1 |
| SO-GDPR-026 | D-09.1 | Art. 24(1)/(2) | Appropriate data-protection policies, reviewed and updated |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-001
  title: "CIA + resilience baseline for personal data processing"
  source_clauses:
    - { clause_id: GDPR-CL06, article_ref: "Art. 5(1)(f)" }
    - { clause_id: GDPR-CP15, article_ref: "Art. 32(1)(b)" }
    - { clause_id: GDPR-C01, article_ref: "Art. 4(1) — personal data definition" }
  linked_objectives: [SO-GDPR-001]
  sub_domain: [D-01.1, D-01.4]
  nist_csf_mapping:
    - { id: PR.DS-01, title: "Data-at-rest protected" }
    - { id: PR.DS-10, title: "Data-in-use protected" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 5(1)(f) establishes integrity and confidentiality as one of the six principles relating to processing of personal data, requiring that personal data be processed in a manner that ensures appropriate security of the personal data, including protection against unauthorised or unlawful processing and against accidental loss, destruction or damage, using appropriate technical or organisational measures. Art. 32(1)(b) operationalises this by listing the ability to ensure the ongoing confidentiality, integrity, availability and resilience of processing systems and services among the measures that the controller and processor must implement under the Art. 32(1) risk-based preamble. Read together, the two provisions establish a continuous obligation to maintain the CIA triad, augmented by an explicit resilience dimension, across the entire processing surface. Two textual points warrant attention for compliance scoping. First, "appropriate" in Art. 5(1)(f) is anchored by the Art. 32(1) preamble to a risk-based test (state of the art, costs of implementation, nature, scope, context and purposes of processing, risks of varying likelihood and severity), meaning the controller must justify the chosen security level ex post rather than declaring it ex ante. Second, the disjunction "technical or organisational measures" admits both an inclusive reading (at least one category suffices) and a strict reading (both required); the parallel wording of Art. 24(1) written with "and" pulls toward the strict reading, which is also the dominant position under ISO 27001-aligned compliance programmes.
  security_rationale: |
    The obligation in Art. 5(1)(f) and Art. 32(1)(b) to maintain the confidentiality, integrity, availability and resilience of personal data is operationalised in NIST CSF 2.0 through **PR.DS-01 (Data-at-rest protected)** and **PR.DS-10 (Data-in-use protected)**.
    PR.DS-01 anchors the protection of stored personal data against unauthorised or unlawful processing and against accidental loss, destruction or damage, satisfying the Art. 5(1)(f) integrity-and-confidentiality principle at the storage layer where the dominant exfiltration surface sits.
    PR.DS-10 extends that protection to data undergoing query, transformation and join operations inside application processes, closing the gap that at-rest controls alone leave open and covering the full data lifecycle that the Art. 32(1)(b) ongoing-confidentiality duty references, including the explicit resilience dimension that signals graceful degradation and recovery to a known-good state.
    A controller that documents PR.DS-01 and PR.DS-10 coverage, key-custodian assignments and the irreversibility properties of the chosen primitives can demonstrate ex post, against the Art. 5(2) accountability threshold, that the risk-based level of security chosen under the Art. 32(1) preamble was actually delivered.
  ambiguity_notes: |
    Art. 5(1)(f) and Art. 4(1) carry S3 ambiguity. On "appropriate" (VAG), the chosen reading anchors the term to the Art. 32(1) risk-based test: the controller documents the chosen security level against the five risk factors in the Art. 32(1) preamble and refreshes this assessment when material change occurs. An alternative reading, supported by industry practice under ISO 27001 and SOC 2 frameworks, treats "appropriate technical and organisational measures" as requiring both control families in parallel, regardless of risk; this is the more conservative reading and is the de facto baseline for any organisation holding formal certification. A third, looser reading treats "appropriate" as whatever the controller self-declares, which does not survive supervisory inspection but is sometimes observed in pre-DPO controllers. The chosen reading here is the inclusive risk-anchored reading, which is consistent with EDPB Guidelines on accountability 07/2019. On "personal data" (POLY/SCOPE-Q per Art. 4(1)), the scope of "identifiable" is read in line with CJEU Breyer C-582/14 §45, which adopts a "means likely reasonably to be used" test. This reading brings pseudonymous data into scope where re-identification is operationally feasible, but leaves genuinely anonymous data outside. EDPB Guidelines 05/2020 on consent §3.4 reinforce this position. A broader reading, extending to inferred and derived data subject to algorithmic singling-out, has been gaining traction post-IAB Europe C-604/22 but is not yet definitively settled. On the "technical or organisational" disjunction (COORD), the chosen reading treats the OR as inclusive, in line with the dominant grammatical reading and consistent with EDPB Guidelines on Art. 32; controllers following the strict reading are equally compliant. Remain open: (a) whether forward-looking cryptographic-agility (quantum-readiness) is required by "state of the art" under Art. 32(1), pending EDPB clarification and ENISA post-quantum guidance; and (b) how the resilience dimension of Art. 32(1)(b) interacts with separate BCDR obligations, pending cross-regulation alignment with DORA Art. 11–12 and NIS 2 Art. 21(2)(c).
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-043
  title: "Appropriate technical and organisational measures under Art. 24(1)"
  source_clauses:
    - { clause_id: GDPR-CP01, article_ref: "Art. 24(1) — appropriate measures" }
    - { clause_id: GDPR-CP01, article_ref: "Art. 24(2) — appropriate data-protection policies" }
    - { clause_id: GDPR-CL07, article_ref: "Art. 5(2) — accountability (cross)" }
  linked_objectives: [SO-GDPR-026]
  sub_domain: [D-09.1]
  nist_csf_mapping:
    - { id: GV.PO-01, title: "Organizational cybersecurity policy is established, communicated, and enforced" }
    - { id: GV.PO-02, title: "Cybersecurity processes and procedures for implementing the cybersecurity policy are established, communicated, and enforced" }
    - { id: GV.RM-04, title: "Strategic direction that describes how to identify and respond to risks is established and communicated" }
  applies_to_role: [CONTROLLER]
  obligation_type: [CONTINUOUS, PERIODIC]
  regulatory_rationale: |
    Art. 24(1) requires the controller, taking into account the nature,
    scope, context and purposes of processing as well as the risks of
    varying likelihood and severity for the rights and freedoms of
    natural persons, to implement appropriate technical and
    organisational measures to ensure and to be able to demonstrate
    that processing is performed in accordance with GDPR; those
    measures shall be reviewed and updated where necessary. Art. 24(2)
    further requires, where proportionate in relation to processing
    activities, the implementation of appropriate data-protection
    policies by the controller. Art. 5(2) accountability anchors the
    demonstrability requirement. The Article is the operational-
    responsibility centrepiece: it sets the controller's overarching
    obligation and ties it to demonstrability.
  security_rationale: |
    The obligation in Art. 24(1), Art. 24(2) and Art. 5(2) to implement appropriate technical and organisational measures, supported by proportionate data-protection policies and reviewed and updated where necessary, so that processing is performed in accordance with GDPR and the controller can demonstrate compliance, is operationalised in NIST CSF 2.0 through **GV.PO-01 (Organizational cybersecurity policy is established, communicated, and enforced)**, **GV.PO-02 (Cybersecurity processes and procedures for implementing the cybersecurity policy are established, communicated, and enforced)** and **GV.RM-04 (Strategic direction that describes how to identify and respond to risks is established and communicated)**.
    GV.PO-01 captures the policy-document discipline: every controller has a communicated, current, enforced cybersecurity-and-data-protection policy anchored on the Art. 24(2) proportionality test, without which the controller cannot demonstrate either the existence or the enforcement of its overall posture.
    GV.PO-02 captures the operational-procedure layer: each policy must be backed by documented processes and procedures — incident response, breach notification, data-subject rights, retention, processor onboarding — so that the policy is real rather than paper.
    GV.RM-04 captures the strategic-direction and review obligation in Art. 24(1) "where necessary": the controller must communicate how it identifies and responds to risks, including the cadence and triggers for policy and procedure refresh, which is precisely the strategic-direction and update-coupling that GV.RM-04 prescribes.
    A controller that documents GV.PO-01 policy coverage, GV.PO-02 process coverage and GV.RM-04 review cadence can demonstrate ex post, against the Art. 5(2) accountability duty, that on the day of any supervisory inspection the controller's overall cybersecurity-and-data-protection posture was both current and proportionate to the risks.
  ambiguity_notes: |
    `where necessary` (review cadence) carries Berry-flagged VAG-S3
    (Berry §5.1). The reading adopted for this SR is the
    material-change-of-risk trigger supplemented by annual periodic
    review (EDPB Guidelines 07/2019 on accountability). The trigger
    threshold is qualitative — change in processing, change in risk
    landscape, change in legal environment — but the EDPB Guidelines
    07/2019 suggest materiality as the operative threshold. Two
    alternative readings remain. First, a periodic-only reading would
    set an annual review and lose the material-change responsiveness;
    this reading is acceptable as a minimum but insufficient for
    high-risk processing. Second, a continuous-review reading would be
    impractical for most controllers and would not add substantive
    protection beyond the material-change trigger. Remain open: (a)
    whether the `where necessary` review obligation creates a per-
    incident trigger (post-incident review) or only an aggregate-change
    trigger; (b) whether `appropriate data-protection policies` (Art.
    24(2)) requires a single umbrella policy or can be split across
    operational policies.
```

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

