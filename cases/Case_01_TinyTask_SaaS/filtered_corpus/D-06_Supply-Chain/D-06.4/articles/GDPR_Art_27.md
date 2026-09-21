---
document_id: AEGIS-PREPROC-GDPR-ART-27
title: GDPR Art. 27 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 27
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.4.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.4.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.2.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.2.md
status: DRAFT
---

# GDPR Art. 27

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-GDPR-023 | Non-EU controllers and processors falling under Art. 3(2) designate a representative in writing in the Union, with limited exceptions for occasional, low-risk, small-scale processing and for public authorities. | `GDPR-CP06` (Art. 27(1)/(2)) | D-06.4, D-09.1 |
| SO-GDPR-023 | D-06.4, D-09.1 | Art. 27(1)/(2) | Union representative for non-EU controllers/processors |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-023
  title: "Pre-launch supervisory consultation on residual high risk"
  source_clauses:
    - { clause_id: GDPR-CP23, article_ref: "Art. 36(1) — prior consultation" }
    - { clause_id: GDPR-CP21, article_ref: "Art. 35(1) — high-risk DPIA" }
    - { clause_id: GDPR-CP22, article_ref: "Art. 35(7) — DPIA content" }
  linked_objectives: [SO-GDPR-013, SO-GDPR-028]
  sub_domain: [D-04.3, D-09.2]
  nist_csf_mapping:
    - { id: GV.OC-03, title: "Legal/regulatory/contractual requirements understood and managed" }
    - { id: ID.RA-06, title: "Risk responses chosen, prioritized, planned, tracked, communicated" }
  applies_to_role: [CONTROLLER, SUPERVISORY_AUTHORITY]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 36(1) requires the controller to consult the supervisory authority prior to processing where a data protection impact assessment under Art. 35 indicates that the processing would result in a high risk in the absence of measures taken by the controller to mitigate the risk. Art. 35(1) supplies the DPIA trigger (high-risk processing), and Art. 35(7) supplies the DPIA content requirement (systematic description, necessity and proportionality assessment, risk assessment, mitigation measures). Art. 36(2) defines the supervisory authority's 8-week response obligation. Read together, the provisions establish a pre-launch gate: where DPIA identifies residual high risk after mitigation, the controller must consult the supervisory authority before launching the processing.
  security_rationale: |
    The obligation in Art. 36(1), read with Art. 35(1) and Art. 35(7), to consult the supervisory authority before launching processing that retains residual high risk after DPIA mitigation is operationalised in NIST CSF 2.0 through **GV.OC-03 (Legal, regulatory, and contractual requirements understood and managed)** and **ID.RA-06 (Risk responses chosen, prioritized, planned, tracked, and communicated)**.
    GV.OC-03 anchors the governance layer that recognises the prior-consultation duty as a legal-regulatory requirement to be managed, satisfying the Art. 36(1) pre-launch-gate status and ensuring the consultation is scheduled into the launch timeline rather than treated as optional, with the Art. 36(2) eight-week supervisory window accommodated.
    ID.RA-06 captures the risk-response leg: the residual risk that survives the Art. 35(7) DPIA mitigation assessment is explicitly chosen, prioritised, planned, tracked and communicated to the authority, with the DPIA content (systematic description, necessity and proportionality, risk assessment, mitigation measures) supplying the evidence base.
    The two subcategories together operationalise the structured risk-response communication that the prior-consultation gate represents, distinguishing it from post-launch incident reporting.
    A controller documenting GV.OC-03 consultation records and ID.RA-06 residual-risk decisions can demonstrate ex post, under Art. 5(2), that the pre-launch engagement occurred before processing began and that the residual-risk justification was transparent.
  ambiguity_notes: |
    `high risk in the absence of measures` is the same `high risk` POLY family as Arts. 34 and 35. Readings converge via the Art. 35(1) threshold inheritance. The `prior to processing` wording is read strictly: the controller must consult before launching, not after, and the supervisory authority's 8-week window under Art. 36(2) must be accommodated in the launch timeline. EDPB Guidelines 4/2019 on DPIA provide factors for high-risk classification but do not bind the controller. Remain open: (a) whether iterative processing activities (e.g. machine-learning model updates) trigger fresh Art. 36(1) consultations on each iteration or whether a single consultation covers the iterative cycle, pending EDPB AI Act interaction guidance; and (b) how the consultation interacts with the Art. 27 representative designation for non-EU controllers, pending alignment with international supervisory cooperation.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-038
  title: "Written EU representative for non-EU controllers and processors"
  source_clauses:
    - { clause_id: GDPR-CP06, article_ref: "Art. 27(1) — designate in writing" }
    - { clause_id: GDPR-CP06, article_ref: "Art. 27(2)(a) — occasional exception" }
  linked_objectives: [SO-GDPR-023]
  sub_domain: [D-06.4, D-09.1]
  nist_csf_mapping:
    - { id: GV.OC-02, title: "Internal and external stakeholders are understood, and their needs and expectations regarding cybersecurity risks are understood and considered" }
    - { id: GV.RR-02, title: "Roles, responsibilities, authorities, and accountabilities related to cybersecurity risk management are established, communicated, understood, and enforced" }
  applies_to_role: [NON_EU_CONTROLLER, NON_EU_PROCESSOR]
  obligation_type: [CONTINUOUS, PER-PROCESSING-ACTIVITY]
  regulatory_rationale: |
    Art. 27(1) requires, where Art. 3(2) applies (offering goods or
    services to EU data subjects, or monitoring their behaviour,
    regardless of whether the processing takes place in the Union), the
    controller or processor to designate in writing a representative in
    the Union. Art. 27(2)(a) provides the exception for processing which
    is occasional, does not include, on a large scale, processing of
    special categories of data as referred to in Art. 9(1) or processing
    of personal data relating to criminal convictions and offences
    referred to in Art. 10, and is unlikely to result in a risk to the
    rights and freedoms of natural persons, taking into account the
    nature, context, scope and purposes of the processing. Art. 27(2)(b)
    carves out public authorities or bodies.
    [OJ-corrective note (v0.2 audit): the OJ text reads verbatim — processing which is occasional, does not include, on a large scale, processing of special categories of data as referred to in Article 9(1) or processing of personal data relating to criminal convictions and offences referred to in Article 10, and is unlikely to result in a risk to the rights and freedoms of natural persons]
  security_rationale: |
    The obligation in Art. 27(1) and Art. 27(2)(a) for any non-EU controller or processor covered by Art. 3(2) to designate in writing a Union-based representative, unless the conjunctive occasional, small-scale, low-risk exception is satisfied, is operationalised in NIST CSF 2.0 through **GV.OC-02 (Internal and external stakeholders are understood, and their needs and expectations regarding cybersecurity risks are understood and considered)** and **GV.RR-02 (Roles, responsibilities, authorities, and accountabilities related to cybersecurity risk management are established, communicated, understood, and enforced)**.
    GV.OC-02 captures the stakeholder-recognition discipline: the non-EU controller treats EU data subjects, supervisory authorities and the designated representative as standing stakeholders whose needs (point of contact, address for enforcement, language of communication) must be understood and documented before processing begins, so that the representative function is operationally real rather than a paper address.
    GV.RR-02 captures the role-accountability discipline: the representative role carries authorities and responsibilities for handling supervisory-authority correspondence, data-subject requests and incident notifications, with the mandate of Art. 27(1) made enforceable through documented communication channels and refusal-to-act safeguards.
    A non-EU controller that documents GV.OC-02 stakeholder identification and GV.RR-02 representative-mandate clarity can demonstrate ex post, against the Art. 5(2) accountability duty read with the Art. 3(2) jurisdictional anchor, that on the day of any supervisory action the designated representative was operationally present and properly authorised.
  ambiguity_notes: |
    `occasional`, `large scale` and `unlikely to result in a risk` (Art.
    27(2)(a)) carry VAG+SCOPE-Q S3 (Berry §5.1): three inquiry-resistant
    qualifiers combined with AND. The exception requires all three to be
    in the controller's favour for the exception to apply — i.e.,
    occasional AND small-scale AND low-risk — and the OJ additionally
    ties `large scale` to the special-category and criminal-conviction
    carve-outs. The reading adopted for this SR is the conjunctive
    reading: each qualifier must hold individually; `occasional` is read
    as not regular or periodic (EDPB Guidelines 3/2018); `large scale`
    follows the EDPB Guidelines 9/2022 factors (number of data subjects,
    volume of data, geographic range, duration); and `unlikely` is read
    as non-negligible risk absent. Two alternative readings remain.
    First, a disjunctive reading under which any one of the three would
    suffice to trigger the exception would conflict with the OJ text,
    which is conjunctive (the negative construction `shall not apply`
    applies only when all three conditions hold). Second, a literal-
    procedural reading that treats `unlikely` as `more probable than
    not` would expand the exception inappropriately. Remain open: (a)
    whether a SaaS offering with a freemium tier counts as `occasional`
    when only a small fraction of EU users sign up; (b) whether
    behavioural monitoring of EU employees of a non-EU employer triggers
    Art. 27 irrespective of the exception's `risk` prong.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

