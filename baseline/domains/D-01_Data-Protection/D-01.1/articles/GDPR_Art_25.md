---
document_id: AEGIS-PREPROC-GDPR-ART-25
title: GDPR Art. 25 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 25
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
  - ../../CrossRegulation/DomainAnalysis/D-01_Data-Protection/D-01.3.md
  - ../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.3.md
  - ../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.4.md
  - ../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.4.md
  - ../../CrossRegulation/DomainAnalysis/D-05_Data-Lifecycle/D-05.1.md
  - ../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.1.md
  - ../../CrossRegulation/DomainAnalysis/D-07_Secure-Development/D-07.1.md
  - ../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.1.md
status: DRAFT
---

# GDPR Art. 25

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-GDPR-007 | Personal-data processing systems implement appropriate technical and organisational measures ensuring that, by default, only personal data which are necessary for each specific purpose are processed — across amount of data collected, extent of processing, period of storage, and accessibility. | `GDPR-CP03` (Art. 25(2)) | D-03.4 |
| SO-GDPR-007 | D-03.4 | Art. 25(2) | Default-necessary processing across amount/extent/period/access |
| SO-GDPR-024 | Personal-data processing implements data-protection principles (such as data minimisation) in an effective manner at the time of means-determination and at the time of processing itself, integrating necessary safeguards (including pseudonymisation, encryption, by-default limits) at state-of-the-art level. | `GDPR-CP02` (Art. 25(1)); `GDPR-CP03` (Art. 25(2)); `GDPR-CL06` (Art. 5(1)(f)) | D-07.1, D-05.1, D-01.1 |
| SO-GDPR-024 | D-07.1, D-05.1, D-01.1 | Art. 25(1), Art. 25(2), Art. 5(1)(f) | Data protection by design and by default |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-013
  title: "Privacy-by-default across collection, retention, and exposure"
  source_clauses:
    - { clause_id: GDPR-CP03, article_ref: "Art. 25(2) — privacy by default" }
    - { clause_id: GDPR-CP02, article_ref: "Art. 25(1) — privacy by design (cross)" }
    - { clause_id: GDPR-CL03, article_ref: "Art. 5(1)(c) — data minimisation (cross)" }
  linked_objectives: [SO-GDPR-007, SO-GDPR-024]
  sub_domain: [D-03.4, D-05.1]
  nist_csf_mapping:
    - { id: PR.PS-01, title: "Configuration management practices established and applied" }
    - { id: PR.DS-12, title: "Data managed consistent with risk strategy" }
  applies_to_role: [CONTROLLER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 25(2) obliges the controller to implement appropriate technical and organisational measures for ensuring that, by default, only personal data which are necessary for each specific purpose of the processing are processed. That obligation applies to the amount of personal data collected, the extent of their processing, the period of their storage and their accessibility. In particular, such measures shall ensure that by default personal data are not made accessible without the individual's intervention to an indefinite number of natural persons. Art. 25(1) supplies the design-time counterpart (privacy by design) and Art. 5(1)(c) data minimisation supplies the underlying principle. Read together, the provisions establish that the default configuration of any processing system must minimise on four dimensions simultaneously: amount (collect only what is needed), extent (process only the operations needed), period (retain only as long as needed), accessibility (do not expose beyond the intended recipients).
  security_rationale: |
    The obligation in Art. 25(2), read with Art. 25(1) and Art. 5(1)(c), to configure processing systems so that by default only necessary personal data is processed is operationalised in NIST CSF 2.0 through **PR.PS-01 (Configuration management practices established and applied)** and **PR.DS-12 (Data managed consistent with risk strategy)**.
    PR.PS-01 anchors the configuration-management baseline that sets the four default dimensions — amount collected, extent processed, retention period and accessibility — to their minimum-necessary values, satisfying the Art. 25(2) AND-coordinated default and ensuring the minimum is enforced as a system property rather than left to operator judgement.
    PR.DS-12 captures the policy-level data-management strategy that the defaults express: a documented risk-strategy positioning opt-in collection, opt-out for out-of-purpose operations, minimum-necessary retention and no public access unless explicitly granted.
    The two subcategories together operationalise the privacy-by-default pattern across all four Art. 25(2) dimensions simultaneously, so that relaxation requires affirmative data-subject intervention.
    A controller documenting PR.PS-01 default configurations, PR.DS-12 data-strategy and the per-system minimisation evidence can demonstrate ex post, under Art. 5(2), that the default state of every processing system was the minimum-necessary setting required by Art. 25(2).
  ambiguity_notes: |
    GDPR-CP03 (Art. 25(2)) carries VAG+COORD-S3 on `necessary for each specific purpose` and the four-element AND. Reading chosen: all four dimensions must individually be minimised and AND-coordinated. An alternative reading allowing some dimensions to be relaxed if others are tightened would weaken the default and is rejected. The AND reading is anchored to EDPB Guidelines 04/2019 on Article 25, which treat the four dimensions as independent minima. On "without the individual's intervention", the chosen reading treats the intervention requirement as the opt-in gate: the controller must not bypass the data subject's affirmative action to expose data. Remain open: (a) whether privacy-by-default applies to AI model defaults (e.g. opt-in vs opt-out for training-data inclusion), pending EDPB AI Act interaction guidance; and (b) whether the four-dimensional test applies per data subject or per processing activity, pending alignment with Art. 35 DPIA granularity.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-039
  title: "Privacy by design integrated at means-and-processing determination"
  source_clauses:
    - { clause_id: GDPR-CP02, article_ref: "Art. 25(1) — privacy by design" }
    - { clause_id: GDPR-CP03, article_ref: "Art. 25(2) — privacy by default (cross)" }
    - { clause_id: GDPR-CL06, article_ref: "Art. 5(1)(f) — integrity & confidentiality (cross)" }
    - { clause_id: GDPR-CP15, article_ref: "Art. 32(1) — security measures (cross)" }
  linked_objectives: [SO-GDPR-024]
  sub_domain: [D-07.1, D-01.1, D-05.1]
  nist_csf_mapping:
    - { id: PR.PS-06, title: "Secure software development practices integrated, and their performance is monitored throughout the SDLC" }
    - { id: PR.DS-12, title: "Data managed consistent with risk strategy" }
  applies_to_role: [CONTROLLER]
  obligation_type: [CONTINUOUS, ONE_TIME]
  regulatory_rationale: |
    Art. 25(1) requires the controller, both at the time of
    determination of the means for processing and at the time of the
    processing itself, taking into account the state of the art, the
    cost of implementation and the nature, scope, context and purposes
    of processing as well as the risks of varying likelihood and
    severity for the rights and freedoms of natural persons, to
    implement appropriate technical and organisational measures, such
    as pseudonymisation, which are designed to implement data-
    protection principles, such as data minimisation, in an effective
    manner and to integrate the necessary safeguards into the
    processing in order to meet the requirements of this Regulation and
    protect the rights of data subjects. Art. 25(2) is the privacy-by-
    default mandate. Art. 5(1)(f) integrity and confidentiality and Art.
    32(1) security measures provide the cross-clause anchor.
  security_rationale: |
    The obligation in Art. 25(1), read with Art. 25(2), Art. 5(1)(f) and Art. 32(1), to implement appropriate technical and organisational measures (such as pseudonymisation and minimisation) both at the time of determination of the means for processing and at the time of the processing itself is operationalised in NIST CSF 2.0 through **PR.PS-06 (Secure software development practices are integrated, and their performance is monitored throughout the SDLC)** and **PR.DS-12 (Data is managed consistent with the organization's risk strategy to protect the confidentiality, integrity, and availability of data)**.
    PR.PS-06 captures the lifecycle-spanning SDLC discipline: the obligation fires both at means-determination and during ongoing processing, which is structurally the same as the secure-development lifecycle expectation that controls be designed in at architecture and requirements time and continuously validated through later stages.
    PR.DS-12 captures the data-management discipline that turns design-time choices into continuous posture: pseudonymisation, minimisation, integrity and confidentiality safeguards are not one-off architectural decisions but live properties of the data set, maintained against the risk strategy and refreshed as purpose or context evolves.
    A controller that documents PR.PS-06 SDLC integration of by-design measures and PR.DS-12 risk-strategy data-handling discipline can demonstrate ex post, against the Art. 5(2) accountability duty, that the state-of-the-art, cost, nature, scope, context, purposes and risks factors in the Art. 25(1) preamble were actually weight-balanced on the day of any processing operation.
  ambiguity_notes: |
    `state of the art` (Art. 25(1)) carries Berry-flagged VAG-S3 — the
    canonical time-dependent, jurisdiction-dependent, sector-dependent
    vague phrase (cf. Art. 32(1) `state of the art`). The reading
    adopted for this SR is the industry-framework reading: ISO 27001
    and 27002, NIST SP 800-53, and sector-specific certifications
    (PCI-DSS, ISO 27701) constitute the `state of the art` reference
    set at design time. Two alternative readings remain. First, the
    strict reading that anchors `state of the art` to ENISA or
    EDPB-published state-of-the-art guidance would freeze the
    reference to a slowly-updating body of soft law. Second, the loose
    reading that accepts any reasonable technical measure documented
    at design time would weaken the design-time bar and let cost of
    implementation dominate. The industry-framework reading balances
    the two by anchoring on recognised frameworks while allowing
    context-appropriate selection. Remain open: (a) whether `state of
    the art` for AI and ML processing in 2026 should be anchored on the
    EU AI Act risk-management requirements or on the NIST AI RMF; (b)
    whether the by-design obligation requires documented threat
    modelling or accepts generic data-protection-by-design checklists.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-040
  title: "Pseudonymisation-by-design with separation of identifying information"
  source_clauses:
    - { clause_id: GDPR-CP02, article_ref: "Art. 25(1) — pseudonymisation reference" }
    - { clause_id: GDPR-CP15, article_ref: "Art. 32(1)(a) — pseudonymisation/encryption (cross)" }
    - { clause_id: GDPR-CP20, article_ref: "Art. 34(3)(a) — encryption exception (cross)" }
  linked_objectives: [SO-GDPR-024, SO-GDPR-002]
  sub_domain: [D-07.1, D-01.3]
  nist_csf_mapping:
    - { id: PR.PS-06, title: "Secure software development practices integrated, and their performance is monitored throughout the SDLC" }
    - { id: PR.DS-01, title: "Data-at-rest protected" }
  applies_to_role: [CONTROLLER]
  obligation_type: [CONTINUOUS, ONE_TIME]
  regulatory_rationale: |
    Art. 25(1) cites pseudonymisation as the canonical by-design
    technique. Art. 4(5) defines pseudonymisation as the processing of
    personal data in such a manner that the personal data can no longer
    be attributed to a specific data subject without the use of
    additional information, provided that such additional information is
    kept separately and is subject to technical and organisational
    measures. Art. 32(1)(a) anchors the operational security measure.
    Art. 34(3)(a) recognises the by-design benefit by exempting the
    controller from breach communication when the data was rendered
    unintelligible to unauthorised persons through such means.
  security_rationale: |
    The obligation in Art. 25(1), Art. 32(1)(a) and Art. 4(5) to integrate pseudonymisation into the processing by design — together with the Art. 34(3)(a) recognition that unintelligibility removes the breach-communication trigger — is operationalised in NIST CSF 2.0 through **PR.PS-06 (Secure software development practices are integrated, and their performance is monitored throughout the SDLC)** and **PR.DS-01 (The confidentiality, integrity, and availability of data-at-rest are protected)**.
    PR.PS-06 captures the design-time discipline: pseudonymisation is a design choice, not a runtime patch, so the obligation only fires when it is embedded at means-determination through the SDLC rather than retrofitted after deployment — exactly the lifecycle PR.PS-06 disciplines.
    PR.DS-01 captures the storage-layer protection that pseudonymisation delivers once applied: the underlying data-at-rest benefits from the confidentiality property of the de-attributed form, and the additional-information-equivalent (the mapping table or key) is held under separate technical and organisational control consistent with the Art. 4(5) de-attribution requirement, which preserves the Art. 34(3)(a) unintelligibility carve-out.
    A controller that documents PR.PS-06 SDLC-level pseudonymisation integration and PR.DS-01 separation-of-identifying-information discipline can demonstrate ex post, against the Art. 5(2) accountability duty, that by-design pseudonymisation was genuine on the day of any personal-data breach and that the Art. 34(3)(a) exception conditions were actually met.
  ambiguity_notes: |
    No new ambiguity. The rule preserves the cryptographic and
    irreversible-pseudonymisation reading chain from SR-GDPR-003.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-041
  title: "Privacy by default across four coordinated minimisation dimensions"
  source_clauses:
    - { clause_id: GDPR-CP03, article_ref: "Art. 25(2) — by-default limits" }
    - { clause_id: GDPR-CP02, article_ref: "Art. 25(1) — by-design (cross)" }
  linked_objectives: [SO-GDPR-024, SO-GDPR-007]
  sub_domain: [D-07.1, D-03.4]
  nist_csf_mapping:
    - { id: PR.PS-01, title: "Configuration management practices are established, documented, and applied to assets" }
    - { id: PR.PS-06, title: "Secure software development practices integrated, and their performance is monitored throughout the SDLC" }
  applies_to_role: [CONTROLLER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 25(2) is the privacy-by-default mandate: only personal data
    which are necessary for each specific purpose of the processing are
    processed, with no indefinite accessibility absent data-subject
    intervention. That obligation applies to four coordinated
    dimensions: the amount of personal data collected, the extent of
    their processing, the period of their storage, and their
    accessibility. In particular, the measures shall ensure that by
    default personal data are not made accessible without the
    individual's intervention to an indefinite number of natural
    persons. Art. 25(1) by-design is the upstream obligation; Art.
    25(2) by-default is its operational manifestation at configuration
    time.
  security_rationale: |
    The obligation in Art. 25(2), read with Art. 25(1), to bind each personal-data collection to what is necessary for each specific purpose and to ensure that, by default, personal data are not made accessible without the data subject's intervention to an indefinite number of natural persons — across the four coordinated dimensions of amount, extent, period and accessibility — is operationalised in NIST CSF 2.0 through **PR.PS-01 (Configuration management practices are established, documented, and applied to assets)** and **PR.PS-06 (Secure software development practices are integrated, and their performance is monitored throughout the SDLC)**.
    PR.PS-01 captures the by-default configuration discipline: every default setting that affects personal-data exposure — collection scope, processing extent, retention horizon, accessibility — must be set to the least-intrusive option, with configuration changes rather than per-transaction decisions altering the posture.
    PR.PS-06 captures the upstream design-time anchor: the four coordinated dimensions are not all reachable by configuration alone, because the design of the data flow itself constrains what the configuration can do. Art. 25(1) by-design must therefore establish the architecture in which PR.PS-01 by-default configurations can operate.
    A controller that documents PR.PS-01 default-closed configuration per dimension and PR.PS-06 design-time alignment of those defaults to the four coordinated dimensions can demonstrate ex post, against the Art. 5(2) accountability duty, that on the day of any processing operation the by-default posture was actually the least-intrusive posture the specific purpose permitted.
  ambiguity_notes: |
    GDPR-CP03 (Art. 25(2)) carries Berry-flagged S3 VAG+COORD on
    `necessary for each specific purpose` combined with four coordinated
    dimensions (amount, extent, period, accessibility). The reading
    adopted for this SR is the all-four-dimensions-individually-
    minimised reading (per EDPB Guidelines 04/2019): each dimension is
    independently bounded to what is necessary for the specific purpose,
    and the four constraints are AND-coordinated minima. Two
    alternative readings remain. First, a trade-off reading under which
    some dimensions can be relaxed if others are tightened would
    conflict with the OJ text, which lists the dimensions as
    AND-coordinated minima. Second, a single-purpose reading that
    treats the four dimensions as a single obligation would lose the
    granular controls each dimension provides. Remain open: (a) whether
    `accessibility` requires default-deny-on-API or accepts default-
    allow-with-policy; (b) how `extent of processing` is operationalised
    for AI-training pipelines where the necessary extent cannot be
    specified in advance.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

