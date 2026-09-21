---
document_id: AEGIS-PREPROC-AI_Act-ART-9
title: AI_Act Art. 9 — SecurityObjectives & SecurityRules
regulation: AI_Act
article: Art. 9
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-01_Data-Protection/D-01.4.md
  - ../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.4.md
  - ../../CrossRegulation/DomainAnalysis/D-02_Vulnerability-Management/D-02.1.md
  - ../../CrossRegulation/DeepAnalysis/D-02_Vulnerability-Management/D-02.1.md
  - ../../CrossRegulation/DomainAnalysis/D-02_Vulnerability-Management/D-02.4.md
  - ../../CrossRegulation/DeepAnalysis/D-02_Vulnerability-Management/D-02.4.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DomainAnalysis/D-07_Secure-Development/D-07.1.md
  - ../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.1.md
  - ../../CrossRegulation/DomainAnalysis/D-07_Secure-Development/D-07.2.md
  - ../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.2.md
  - ../../CrossRegulation/DomainAnalysis/D-07_Secure-Development/D-07.3.md
  - ../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.3.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.2.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.2.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.1.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.1.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.3.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.3.md
status: DRAFT
---

# AI_Act Art. 9

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-AIACT-004 | Where strictly necessary for the purpose of ensuring bias detection and correction in high-risk AI systems, providers may exceptionally process special categories of personal data subject to appropriate safeguards and six cumulative conditions, including state-of-the-art security and privacy-preserving measures. | `AIA-C08` (Art. 10(5) — exception to GDPR Art. 9 prohibition; 6 cumulative conditions (a)–(f) all required; cross-regulation borrow from GDPR) | D-05.1 |
| SO-AIACT-010 | A quality management system is implemented to ensure compliance with the AI Act, documented in a systematic and orderly manner in the form of written policies, procedures and instructions, and covering at least 13 enumerated aspects including techniques, procedures and systematic actions for the design, design control and design verification of the high-risk AI system. | `AIA-C20` (Art. 17(1) — `systematic and orderly manner` + `quality management system` POLY (ISO 9001 / ISO/IEC 23053 / internal bespoke) + 13-element closed list (a)–(m)); `AIA-C21` (Art. 17(1)(c) — `design, design control and design verification` 3-way AND of near-synonyms); `AIA-C22` (Art. 17(1)(g) — risk-management-system documentation cross-reference to Art. 9) | D-09.1 (primary), D-07.1 (cross) |
| SO-AIACT-001 | A risk management system is established, implemented, documented and maintained for high-risk AI systems throughout their lifecycle, comprising a continuous, iterative process of (a) identification and analysis of known and reasonably foreseeable risks, (b) estimation and evaluation of risks emerging from use under conditions of reasonably foreseeable misuse, (c) evaluation of other risks arising from analysis of post-market monitoring data, and (d) adoption of appropriate and targeted risk management measures. | `AIA-C01` (Art. 9(1) — `established, implemented, documented and maintained` 4-way verb coordination; **`risk management system` POLY central ambiguity**); `AIA-C02` (Art. 9(2) — 4-step list (a)–(d); `reasonably foreseeable` recurs 4× across Art. 9; `known and reasonably foreseeable risks` SCOPE-Q + `reasonably foreseeable misuse` POLY) | D-09.2 (primary), D-02.1 (cross) |
| SO-AIACT-001 | D-09.2, D-02.1 | Art. 9(1)+(2) | Risk management system with foreseeable-risk identification |
| SO-AIACT-002 | D-02.1, D-10.3, D-02.4 | Art. 9(6)+(7) | Testing for risk management including real-world conditions |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-AIACT-001 (AI risk management lifecycle)

```yaml
- sr_id: SR-AIACT-001
  title: "Continuous risk-management governance for high-risk AI lifecycle"
  source_clauses:
    - { clause_id: AIA-C01, article_ref: "Art. 9(1) — `A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems`" }
  linked_objectives: [SO-AIACT-001]
  sub_domain: [D-09.2]
  nist_csf_mapping:
    - { id: GV.RM-01, title: "Risk management objectives are established and agreed to by organizational stakeholders" }
    - { id: GV.RM-06, title: "A standardized method for calculating, documenting, categorizing, and prioritizing cybersecurity risks is established and communicated" }
  applies_to_role: [PROVIDER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 9(1) of Regulation (EU) 2024/1689 (the AI Act) imposes an
    institutional duty on providers of high-risk AI systems to
    establish, implement, document and maintain a risk management
    system across the full lifecycle of those systems. The four
    coordinated verbs frame this as a continuous obligation rather
    than a one-off design exercise, and the clause operates as the
    umbrella provision for the more substantive risk-management
    requirements set out in paragraphs (2) to (10), which impose
    concrete identification, evaluation and treatment steps. By
    binding providers to the lifecycle scope — covering design,
    development, deployment, operation and post-market evolution —
    Article 9(1) anchors the entire high-risk-AI risk-management
    apparatus under a single governance substrate. Cross-regulation,
    the clause mirrors the continuous risk-treatment duty in GDPR
    Article 32 and the risk-management expectations under DORA
    Article 6, and it sits upstream of the CRA cybersecurity-risk
    assessment in CRA Annex I §1.
  security_rationale: |
    The obligation in Art. 9(1) is operationalised in NIST CSF 2.0
    through **GV.RM-01 (Risk management objectives are established
    and agreed to by organizational stakeholders)** and **GV.RM-06
    (A standardized method for calculating, documenting,
    categorizing, and prioritizing cybersecurity risks is established
    and communicated)**. GV.RM-01 anchors the stakeholder-agreement
    substrate that the four coordinated verbs — establish, implement,
    document and maintain — require: without a documented set of
    objectives agreed by the organisation, the lifecycle duty
    fragments into disconnected activities. GV.RM-06 supplies the
    standardised calculation, documentation, categorisation and
    prioritisation method that prevents the umbrella Art. 9(1)
    provision from operating as a vacuous frame, ensuring that the
    more substantive obligations in paragraphs (2) to (10) plug
    into a shared risk vocabulary. Together, the two GV.RM
    sub-categories supply the governance vocabulary (GV.RM-01) and
    the methodological discipline (GV.RM-06) on which the
    lifecycle-wide risk-management apparatus depends. A provider
    evidencing GV.RM-01 stakeholder-agreed objectives and a
    documented GV.RM-06 risk-calculation method demonstrates ex
    post that the Art. 9(1) institutional substrate is in place,
    satisfying the AI Act accountability envelope through
    auditable evidence of organisational alignment and
    methodological rigour.
  ambiguity_notes: |
    The clause carries medium severity on the risk management system
    reference because the AI Act does not specify which framework
    providers must adopt, leaving a poly-semous reading where the
    risk-management system could be aligned with ISO 31000:2018 (the
    canonical international risk-management standard), the NIST AI
    RMF 1.0 (the US-equivalent AI-specific frame) or an internal
    bespoke system. The chosen reading is that the clause is
    framework-agnostic and permits ISO 31000-style or NIST AI RMF
    based practice, while preserving an entity-internal bespoke
    reading as the literal OJ. The four-way verb coordination
    `established, implemented, documented AND maintained` raises a
    parallelism question whether each verb is a distinct activity or
    a facet of a composite duty, and the literal reading treats them
    as cumulative activities each of which must be performed. As an
    alternative, providers could read the verbs as facets of one
    composite duty, simplifying documentation. The implicit VAG
    burden propagates from the substantive paragraphs (2) to (10),
    where `reasonably foreseeable` and `appropriate and targeted`
    sit. Remain open: whether the framework-agnosticism survives
    when the AI Office issues its first code of practice on
    risk-management systems under Article 56.
```

### SO-AIACT-001 (AI risk management lifecycle)

```yaml
- sr_id: SR-AIACT-002
  title: "Four-step AI risk-identification and treatment cycle"
  source_clauses:
    - { clause_id: AIA-C02, article_ref: "Art. 9(2)(a)–(d) — 4-step list: (a) identification and analysis of the known and the reasonably foreseeable risks; (b) estimation and evaluation of the risks … under conditions of reasonably foreseeable misuse; (c) evaluation of other risks arising from analysis of post-market monitoring data; (d) adoption of appropriate and targeted risk management measures" }
  linked_objectives: [SO-AIACT-001]
  sub_domain: [D-09.2, D-02.1]
  nist_csf_mapping:
    - { id: ID.RA-03, title: "Threats, both internal and external, are identified, recorded, and prioritized" }
    - { id: ID.RA-04, title: "Potential impacts and likelihoods of threats exploiting vulnerabilities are identified, recorded, and prioritized" }
    - { id: ID.RA-06, title: "Risk responses are chosen, prioritized, planned, tracked, and communicated" }
  applies_to_role: [PROVIDER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 9(2) of the AI Act operationalises the institutional duty
    in Article 9(1) by prescribing a four-step closed list that the
    risk-management system must comprise on a continuous and
    iterative basis. Sub-point (a) requires identification and
    analysis of the known and the reasonably foreseeable risks to
    health, safety and fundamental rights; sub-point (b) requires
    estimation and evaluation of the risks emerging from use under
    conditions of reasonably foreseeable misuse; sub-point (c)
    requires evaluation of other risks arising from analysis of
    post-market monitoring data collected under Article 72; and
    sub-point (d) requires the adoption of appropriate and targeted
    risk-management measures to address the identified risks. The
    framework language `It shall comprise the following steps`
    together with the `at least` qualifier preceding the list
    signals that the four sub-points are a closed cumulative set
    rather than an exemplary list. By extending the threat picture
    from intended-purpose use to reasonably foreseeable misuse, the
    clause displaces the older product-safety baseline and aligns AI
    risk-management with forward-looking foreseeability reasoning
    already familiar in product-liability and GDPR
    data-protection-by-design practice, with parallel effects in
    NIS 2 Article 21 risk-analysis and CRA Annex I §1 risk
    assessment.
  security_rationale: |
    The obligation in Art. 9(2)(a)–(d) is operationalised in NIST
    CSF 2.0 through **ID.RA-03 (Threats, both internal and
    external, are identified, recorded, and prioritized)**,
    **ID.RA-04 (Potential impacts and likelihoods of threats
    exploiting vulnerabilities are identified, recorded, and
    prioritized)**, and **ID.RA-06 (Risk responses are chosen,
    prioritized, planned, tracked, and communicated)**. ID.RA-03
    covers the identification-and-analysis half of sub-points (a)
    and (b) — known threats together with the foresight extension
    to reasonably foreseeable misuse scenarios that AI-specific
    failure modes (data poisoning, model evasion, confidentiality
    attacks) require. ID.RA-04 supplies the impact-and-likelihood
    estimation that sub-point (b) operationalises, capturing both
    probability and the harm envelope of each identified risk in a
    prioritised record. ID.RA-06 implements the sub-point (c)–(d)
    response-selection and treatment-tracking pipeline, including
    the feedback loop from post-market monitoring data into the
    treatment cycle. Together, the three ID.RA sub-categories
    operationalise the four-step identify–estimate–evaluate–treat
    cycle that Art. 9(2) prescribes as a closed cumulative set. A
    provider evidencing ID.RA-03 threat records, ID.RA-04
    impact-and-likelihood scores, and ID.RA-06 response-tracking
    trails demonstrates ex post that the Art. 9(2) closed-list
    duty — including the foreseeable-misuse extension and the
    post-market data feedback — is discharged, with documented
    traceability from identified risk to selected treatment.
  ambiguity_notes: |
    The clause carries the central AI Act ambiguity on the phrase
    `reasonably foreseeable`, which recurs four times across Article
    9(2)(a) and 9(2)(b) and has no anchor in the OJ. The chosen
    reading is that the foresight standard is objective, anchored to
    industry consensus and supervisory practice, with the hybrid
    court-determined reading available as a fallback. As an
    alternative, providers could read it as a subjective
    provider-expectation standard calibrated to what a particular
    provider should reasonably have foreseen. As a second
    alternative, a strict hybrid reading could defer the
    determination to court adjudication on a case-by-case basis,
    deferring operational risk-allocation to litigation outcomes.
    The phrase `known and the reasonably foreseeable risks` further
    raises a scope question about where the boundary between
    `known` and `reasonably foreseeable` sits. The phrase
    `reasonably foreseeable misuse` raises a poly-semous demarcation
    issue because the boundary between `use` and `misuse` is itself
    undefined in the Act. The four-step coordination by `It shall
    comprise the following steps:` with `at least` is a closed
    AND-list, so providers must implement all four steps
    cumulatively; partial compliance of three of four does not
    satisfy the clause. The verb phrase `appropriate and targeted`
    on the risk-management measures is itself vague and undefined.
    Remain open: (a) whether `reasonably foreseeable misuse` extends
    to dual-use scenarios where the provider cannot realistically
    foresee the downstream application chain; (b) whether the
    boundary between `known` and `reasonably foreseeable` will be
    settled by AI Office guidance under Article 56 or by
    case-by-case supervisory practice under Article 70.
```

### SO-AIACT-001 (AI risk management lifecycle)

```yaml
- sr_id: SR-AIACT-003
  title: "Risk-measure validation through targeted testing"
  source_clauses:
    - { clause_id: AIA-C03, article_ref: "Art. 9(6) — `High-risk AI systems shall be tested for the purpose of identifying the most appropriate and targeted risk management measures. Testing shall ensure that high-risk AI systems perform consistently for their intended purpose`" }
    - { clause_id: AIA-C04, article_ref: "Art. 9(7) — `Testing procedures may include testing in real-world conditions in accordance with Article 60`" }
  linked_objectives: [SO-AIACT-002]
  sub_domain: [D-02.1, D-10.3, D-02.4]
  nist_csf_mapping:
    - { id: ID.RA-01, title: "Vulnerabilities in assets are identified, validated, and recorded" }
    - { id: ID.RA-04, title: "Potential impacts and likelihoods of threats exploiting vulnerabilities are identified, recorded, and prioritized" }
    - { id: PR.PS-06, title: "Secure software development practices are integrated, and their performance is monitored throughout the SDLC" }
    - { id: GV.SC-04, title: "Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations" }
  applies_to_role: [PROVIDER]
  obligation_type: [CONTINUOUS, TRIGGERED]
  regulatory_rationale: |
    Article 9(6) of the AI Act requires that high-risk AI systems be
    tested in order to identify the most appropriate and targeted
    risk-management measures, and that testing ensure that the
    systems perform consistently for their intended purpose. Article
    9(7) permits the testing procedures to include testing in
    real-world conditions in accordance with the detailed rules set
    out in Article 60, which governs real-world testing plans,
    informed-consent regimes for natural persons, and the obligation
    to suspend or terminate a test where serious risks materialise.
    Together the two paragraphs form the verification layer of the
    AI-Act risk-management apparatus, ensuring that the measures
    adopted under Article 9(2)(d) are validated against actual
    AI-system behaviour rather than asserted on the basis of
    design-time analysis alone. Cross-regulation, the real-world
    testing cross-reference interacts with CRA Article 24
    vulnerability-handling testing expectations and with NIS 2
    Article 21 cybersecurity risk-management measures where
    real-world testing uncovers incident-grade vulnerabilities.
  security_rationale: |
    The obligation in Art. 9(6)–(7) is operationalised in NIST CSF
    2.0 through **ID.RA-01 (Vulnerabilities in assets are
    identified, validated, and recorded)**, **ID.RA-04 (Potential
    impacts and likelihoods of threats exploiting vulnerabilities
    are identified, recorded, and prioritized)**, **PR.PS-06
    (Secure software development practices are integrated, and their
    performance is monitored throughout the SDLC)**, and **GV.SC-04
    (Suppliers and other third parties are routinely assessed using
    audits, test results, or other forms of evaluation to confirm
    they are meeting their contractual obligations)**. ID.RA-01
    anchors the test-for-most-appropriate-measures duty:
    vulnerabilities must be discovered, validated and recorded
    before any targeted measure can be selected. ID.RA-04 connects
    testing output to impact-and-likelihood prioritisation, so
    test results feed upstream risk-treatment selection. PR.PS-06
    integrates secure development practices throughout the SDLC,
    making testing a continuous practice that satisfies the
    `test-for-consistency` qualifier of Art. 9(6). GV.SC-04 covers
    supplier assessment where testing relies on third-party
    evaluation infrastructure, including Article 60 real-world-
    testing plans. A provider documenting ID.RA-01 records,
    ID.RA-04 impact scores, PR.PS-06 SDLC integration and GV.SC-04
    third-party assessments demonstrates ex post that the Art.
    9(6)–(7) verification layer — including test-for-consistency
    continuity and the Article 60 cross-reference — is operational.
  ambiguity_notes: |
    The clause carries medium severity on the phrase `most
    appropriate AND targeted`, which is vague on both modifiers and
    on the AND-coordination. The verb `testing` is poly-semous and
    could be read as unit, integration, system, acceptance or
    red-team testing; the chosen reading is cumulative, with
    multiple test levels required to satisfy the open-ended
    verification standard. Real-world testing under Article 9(7) is
    itself poly-semous between pilot deployment, A/B testing and
    live inference monitoring, and the substantive boundary is
    delegated to Article 60 detailed rules. The chosen reading is
    literal: the substantive rules are in Article 60. As an
    alternative, providers could limit themselves to lab/sandbox
    testing only, treating Article 9(7) as permissive rather than
    enabling. Remain open: whether testing-in-real-world-conditions
    under Article 9(7) covers inference-time stress testing on
    production traffic, or only pre-market sandboxed pilots
    governed by Article 60 informed-consent regimes.
```

### SO-AIACT-001 (AI risk management lifecycle)

```yaml
- sr_id: SR-AIACT-014
  title: "Accuracy robustness and cybersecurity baseline across AI lifecycle"
  source_clauses:
    - { clause_id: AIA-C16, article_ref: "Art. 15(1) — `High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle`" }
  linked_objectives: [SO-AIACT-009]
  sub_domain: [D-07.1, D-02.1]
  nist_csf_mapping:
    - { id: PR.PS-06, title: "Secure software development practices are integrated, and their performance is monitored throughout the SDLC" }
    - { id: PR.IR-03, title: "Mechanisms are put in place to achieve resilience requirements in normal and adverse situations" }
    - { id: ID.RA-04, title: "Potential impacts and likelihoods of threats exploiting vulnerabilities are identified, recorded, and prioritized" }
  applies_to_role: [PROVIDER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 15(1) of Regulation (EU) 2024/1689 is the single provision
    that fuses three AI-technical properties — accuracy, robustness,
    and cybersecurity — into one continuous, lifecycle-wide duty of
    the high-risk AI provider. The provision applies from design
    through decommissioning and is read together with Recital 66,
    which clarifies that the three properties are to be interpreted
    in light of the system's intended purpose and the state of the
    art. The duty is articulated in 3-way AND form (the OJ does not
    contemplate partial compliance with two of the three properties),
    and is anchored in Title III Chapter 2 (Section 2 — Requirements
    for High-Risk AI Systems), placing it on the same legal plane as
    the data-governance, documentation, transparency, human-oversight
    and risk-management obligations of Arts. 10–14. The combined
    reading with the cross-cutting post-market monitoring obligation
    of Art. 72(1) means the provider must demonstrate — ex-ante
    (conformity assessment) and ex-post (post-market surveillance)
    — that the three properties are not merely aspirational at
    design time but are maintained throughout the AI system's
    lifecycle. A compliance officer should treat Art. 15(1) as the
    corner-stone substantive duty of the high-risk AI title, on par
    with Art. 9 (risk management) and Art. 10 (data governance).
  security_rationale: |
    The Art. 15(1) three-property duty is operationalised in NIST
    CSF 2.0 through **PR.PS-06 (Secure software development
    practices integrated across the SDLC)**, **PR.IR-03
    (Resilience mechanisms in normal and adverse situations)**,
    and **ID.RA-04 (Threat-impact prioritisation)**, with
    supplementary alignment to **GV.OV-02 (Strategy review
    against changing risk landscape)**, **PR.DS-02
    (Data-in-transit confidentiality, integrity, availability)**,
    and **ID.RA-01 (Vulnerability identification, validation,
    recording)**. PR.PS-06 anchors the SDLC substrate — secure
    coding, threat modelling, verification, change control — on
    which the three properties rest: an accuracy, robustness, or
    cybersecurity defect is most often a defect of process rigour.
    PR.IR-03 enforces the resilience dimension of robustness:
    failure-mode envelopes, graceful degradation, fail-safe
    patterns. ID.RA-04 supplies the risk-prioritisation
    discipline that converts the abstract duty into a ranked
    treatment set. GV.OV-02 closes the loop by requiring the
    provider to revisit the strategy when the threat landscape,
    the regulatory baseline, or the technology stack shifts,
    satisfying the lifecycle-consistency clause. PR.DS-02
    reinforces the cybersecurity property by binding data-in-
    transit CIA to the substrate, and ID.RA-01 records each
    identified vulnerability as evidence. Together these
    subcategories produce auditable artefacts — SDLC records,
    resilience test reports, risk register, strategy-review
    minutes — that enable the provider to demonstrate ex post
    to the conformity-assessment body and the market-
    surveillance authority that the three properties were
    maintained throughout the system lifecycle (Art. 9 + Art. 15
    + Art. 72 accountability chain).
  ambiguity_notes: |
    Source clause AIA-C16 carries three **S3** features (per
    `../Regulation/AI_Act/Ambiguity/06_AI_Act.md` §2.16). First, `appropriate level of accuracy,
    robustness, and cybersecurity` is VAG-3 — the three properties
    are each inquiry-resistant (Berry §5.1): `accuracy` has no OJ
    anchor for metric, threshold, or confidence level; `robustness`
    has no OJ anchor for the perturbation class; `cybersecurity`
    inherits the EU-level definitional gap that CRA C07
    (`cybersecurity` POLY) and NIS 2 C01 (`cybersecurity` POLY)
    also fail to close. Second, **POLY-S3** decomposes `accuracy`
    into R1 precision / R2 recall / R3 F1 / R4 calibration, and
    `robustness` into R1 distributional shift / R2 adversarial /
    R3 operational — the OJ does not pick. Third, **COORD-S2** on
    `accuracy, robustness AND cybersecurity` admits no partial
    compliance (2 of 3) reading, so the provider must address all
    three in parallel. The lifecycle-consistency clause
    (`perform consistently in those respects throughout their
    lifecycle`) is itself VAG+POLY: `consistently` is POLY between
    R1 same-as-design-time / R2 monotonic improvement / R3 no-
    degradation, and the OJ does not say which sense binds.
    Practical reading chosen (Berry §3.3.1): the three properties
    form an integrated engineering envelope, with the metric-set
    and the threshold-set disclosed in the technical documentation
    (Annex IV §2) and justified in the risk-management file
    (Art. 9). Remain open: (a) whether the supervisory authorities
    will accept any one of the four accuracy metrics in lieu of a
    metric-set, or require the full vector; (b) whether the
    `perform consistently` sense binds at design-time parity or at
    a no-degradation floor; (c) whether partial compliance (2 of 3
    properties) is ever tolerated in conformity-assessment practice.
```

### SO-AIACT-001 (AI risk management lifecycle)

```yaml
- sr_id: SR-AIACT-015
  title: "Resilience against errors faults and environmental drift"
  source_clauses:
    - { clause_id: AIA-C17, article_ref: "Art. 15(3) — `High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment … The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans`" }
  linked_objectives: [SO-AIACT-009]
  sub_domain: [D-01.4, D-02.1]
  nist_csf_mapping:
    - { id: PR.IR-03, title: "Mechanisms are put in place to achieve resilience requirements in normal and adverse situations" }
    - { id: PR.IR-04, title: "Adequate resource capacity to ensure availability is maintained" }
    - { id: PR.DS-11, title: "Backups of data are created, protected, maintained, and tested" }
  applies_to_role: [PROVIDER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 15(3) of Regulation (EU) 2024/1689 requires high-risk AI
    providers to make the system `as resilient as possible`
    regarding errors, faults, and inconsistencies arising in the
    system or its operating environment, and lists technical
    redundancy (including backup and fail-safe plans) as one
    permissible means. Recital 66 confirms that resilience
    measures are to be proportionate to the intended purpose and
    the state of the art. The 3-way OR of `errors, faults or
    inconsistencies` is broad — it covers both AI-technical
    failures (e.g. inference-stage numerical instability) and
    environmental failures (e.g. sensor degradation) — and the
    2-way OR for the means (`backup OR fail-safe plans`) signals
    that the OJ does not mandate a specific engineering pattern.
    A compliance officer should treat this provision as the
    resilience backstop to Art. 15(1): where Art. 15(1) sets the
    continuous property baseline, Art. 15(3) sets the failure-
    mode envelope.
  security_rationale: |
    The Art. 15(3) resilience duty is operationalised in NIST
    CSF 2.0 through **PR.IR-03 (Resilience mechanisms in normal
    and adverse situations)**, **PR.IR-04 (Adequate resource
    capacity for availability)**, and **PR.DS-11 (Backups
    created, protected, maintained, tested)**, with
    supplementary alignment to **PR.PS-02 (Software maintenance
    commensurate with risk)** and **ID.RA-04 (Threat-impact
    prioritisation)**. PR.IR-03 is the principal anchor: it
    requires the provider to design, document, and verify
    resilience mechanisms — failover, redundant inference paths,
    graceful degradation — that match the enumerated failure
    modes (`errors, faults, inconsistencies`). PR.IR-04 binds
    the capacity dimension: the resource budget (compute,
    storage, network) must be sized for the resilience target,
    not just the steady-state workload, so that backup and
    fail-safe modes have the substrate they need. PR.DS-11
    operationalises the explicit `backup` means: backups must
    not only be created and protected but also tested, which
    closes the gap between a documented backup and a usable
    backup. PR.PS-02 reinforces the resilience chain by binding
    software maintenance (patching, replacement) to risk, and
    ID.RA-04 ensures the failure modes are prioritised in the
    risk register rather than enumerated exhaustively. The
    combined control set yields documented resilience
    architectures, backup-restore test reports, capacity-planning
    records, and risk-prioritisation minutes — the evidentiary
    substrate that supports ex post demonstration of compliance
    to the conformity-assessment body and the market-
    surveillance authority (Art. 9 + Art. 15(3) + Art. 72
    accountability chain).
  ambiguity_notes: |
    Source clause AIA-C17 carries **S2** features (per
    `../Regulation/AI_Act/Ambiguity/06_AI_Act.md` §2.17). `as resilient as possible` is VAG-2
    (Berry §5.1 soft hedge; R1 best-effort maximum / R2
    reasonable best effort / R3 state-of-the-art — R3 dominant as
    the literal OJ sense; cf. CRA C07 `state of the art` POLY
    on the parallel product-cybersecurity axis). `errors, faults
    or inconsistencies` is POLY-2 (three near-synonyms for
    system deviations; reading chosen: R3 cumulative OR per the
    3-way OR). The 2-way OR of `backup OR fail-safe plans` is
    COORD-2 — the OJ does not require both, only that
    technical redundancy be present in some recognised form.
    Remain open: (a) whether `as resilient as possible` collapses
    to `state of the art` or imposes a stricter best-effort
    ceiling; (b) whether `fail-safe` requires a documented safe-
    state behaviour or merely a documented fallback plan.
```

### SO-AIACT-001 (AI risk management lifecycle)

```yaml
- sr_id: SR-AIACT-016
  title: "AI-specific attack vector mitigation across training and inference"
  source_clauses:
    - { clause_id: AIA-C18, article_ref: "Art. 15(4)–(5) — `measures to prevent, detect, respond to, resolve and control for attacks trying to manipulate the training data set (data poisoning), or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws`" }
  linked_objectives: [SO-AIACT-009]
  sub_domain: [D-02.1, D-07.2]
  nist_csf_mapping:
    - { id: ID.RA-04, title: "Potential impacts and likelihoods of threats exploiting vulnerabilities are identified, recorded, and prioritized" }
    - { id: PR.PS-06, title: "Secure software development practices are integrated, and their performance is monitored throughout the SDLC" }
    - { id: RS.MI-01, title: "Incidents are contained" }
    - { id: RS.MA-03, title: "Incidents are categorized, prioritized, and scoped" }
  applies_to_role: [PROVIDER]
  obligation_type: [CONTINUOUS, TRIGGERED]
  regulatory_rationale: |
    Art. 15(4) of Regulation (EU) 2024/1689 requires high-risk AI
    providers to put in place appropriate technical and
    organisational measures against AI-specific attack categories —
    data poisoning, model poisoning, adversarial examples / model
    evasion, confidentiality attacks, and model flaws. Art. 15(5)
    elaborates the technical-and-organisational-measure framework,
    placing the obligation on a CONTINUOUS+TRIGGERED axis (the
    continuous baseline; the triggered escalation when an attack
    is detected or suspected). Recital 66 frames the obligation as
    parallel to — not duplicative of — the CRA product-cybersecurity
    baseline (CRA Annex I §(1)(b)–(c) for confidentiality,
    integrity, availability of the AI substrate). The combined
    reading with Art. 73 (serious incident reporting) and Art. 72
    (post-market monitoring) means an attack on the AI substrate
    can trigger a chain: detection → incident categorisation →
    market-surveillance reporting within the Art. 73 differentiated
    timelines. A compliance officer should treat Art. 15(4)–(5) as
    the AI-specific complement to the conventional cybersecurity
    controls inherited from CRA and NIS 2.
  security_rationale: |
    The Art. 15(4)–(5) AI-specific attack duty is operationalised
    in NIST CSF 2.0 through **ID.RA-04 (Threat-impact
    prioritisation)**, **PR.PS-06 (Secure SDLC)**, **RS.MI-01
    (Incident containment)**, and **RS.MA-03 (Incident
    categorisation, prioritisation, scoping)**, with
    supplementary alignment to **RS.AN-03 (Root-cause
    analysis)**, **DE.AE-02 (Event analysis)**, and **DE.CM-09
    (Runtime monitoring)**. ID.RA-04 forces the provider to
    rank the six attack categories — data poisoning, model
    poisoning, adversarial examples, confidentiality attacks,
    model flaws — by impact and likelihood rather than
    enumerate them, so that controls are sized to the
    prioritised threat picture. PR.PS-06 anchors the SDLC
    substrate (threat modelling, secure coding, code review,
    verification) where AI-specific attacks are most cheaply
    prevented by design. RS.MI-01 supplies the triggered
    containment arm — when an attack is detected, the
    provider must contain it (model rollback, input filtering,
    inference quarantining) without waiting for full
    attribution. RS.MA-03 binds the response to a categorised
    scope so the Art. 73 reporting chain (SR-AIACT-022) can
    fire with the correct timeline (15 / 10 / 2 days).
    Supplementary RS.AN-03 (root cause), DE.AE-02 (event
    analysis) and DE.CM-09 (runtime monitoring) close the
    loop on detection, attribution, and continuous
    observability. The combined control set produces a
    threat-prioritised control matrix, SDLC artefacts
    (threat models, code-review records, test reports),
    incident-response runbooks with categorised playbooks per
    attack class, and a continuous monitoring telemetry
    stream — the evidentiary substrate for ex post compliance
    demonstration under the Art. 9 risk-management + Art. 15
    cybersecurity + Art. 73 incident-reporting + Art. 72
    post-market-monitoring accountability chain.
  ambiguity_notes: |
    Source clause AIA-C18 carries **S2** on `where appropriate`
    (VAG soft hedge) and on the six named attack categories
    (POLY-2 — each is a research-term-of-art with multiple
    operational definitions: `data poisoning` alone covers label-
    flipping, backdoor injection, and feature-collision). The
    5-way AND of incident-response phases (`prevent, detect,
    respond to, resolve AND control`) + 6-way OR of attack
    types is **S3** on the COORD axis (Berry §5.4.7 — twin
    multi-element coordination); the cross-product admits ≥30
    distinct obligation shapes per `../Regulation/AI_Act/Ambiguity/06_AI_Act.md` §2.18.
    Practical reading chosen: R1 cumulative AND for the 5 phases
    (all five must be present in the provider's IR process) and
    R1 cumulative OR for the 6 attack types (any of the six
    attack categories must be reachable by the 5-phase process).
    Remain open: (a) whether the supervisory authorities will
    require one mitigation per attack category, or accept a
    cross-cutting mitigation that subsumes several; (b) whether
    `confidentiality attacks` includes model inversion and
    membership inference or only the narrower exfiltration
    sense used in some CRA readings.
```

### SO-AIACT-001 (AI risk management lifecycle)

```yaml
- sr_id: SR-AIACT-017
  title: "Documented quality management system governing AI compliance"
  source_clauses:
    - { clause_id: AIA-C20, article_ref: "Art. 17(1) — `Providers of high-risk AI systems shall put a quality management system in place that ensures compliance with this Regulation. That system shall be documented in a systematic and orderly manner in the form of written policies, procedures and instructions, and shall include at least the following aspects: (a) … (m)`" }
    - { clause_id: AIA-C22, article_ref: "Art. 17(1)(g) — `the risk management system referred to in Article 9`" }
  linked_objectives: [SO-AIACT-010]
  sub_domain: [D-09.1]
  nist_csf_mapping:
    - { id: GV.PO-01, title: "Organizational cybersecurity policy is established, communicated, and enforced" }
    - { id: GV.RM-01, title: "Risk management objectives are established and agreed to by organizational stakeholders" }
    - { id: GV.RM-04, title: "Strategic direction on identifying and responding to risks established and communicated" }
  applies_to_role: [PROVIDER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 17(1) of Regulation (EU) 2024/1689 requires providers of
    high-risk AI systems to put in place a quality management
    system (QMS) that ensures compliance with the AI Act. The QMS
    must be documented in a systematic and orderly manner as
    written policies, procedures, and instructions, and must
    cover at least the 13 enumerated aspects (a)–(m) of the
    paragraph. Sub-point (g) cross-refers to Art. 9 (the risk
    management system), so the QMS is the governance substrate
    for the substantive Title III obligations. Recital 67
    characterises the QMS as inspired by established quality
    standards (ISO 9001 family) but does not mandate a specific
    standard, leaving the provider to choose. A compliance officer
    should treat the QMS as the umbrella obligation that the
    conformity assessment will examine first.
  security_rationale: |
    The Art. 17(1) QMS duty is operationalised in NIST CSF 2.0
    through **GV.PO-01 (Organisational cybersecurity policy
    established, communicated, enforced)**, **GV.RM-01 (Risk
    management objectives established and agreed)**, and
    **GV.RM-04 (Strategic direction on identifying and
    responding to risks)**, with supplementary alignment to
    **GV.PO-02 (Cybersecurity processes and procedures
    established, communicated, enforced)** and **GV.OC-03
    (Legal, regulatory, contractual requirements understood
    and managed)**. GV.PO-01 is the policy arm of the QMS —
    the top-level written cybersecurity policy that
    operationalises the 13-element list (a)–(m), including the
    policies, procedures, and instructions anchor in Art. 17(1).
    GV.RM-01 binds the QMS to risk-management objectives that
    have been agreed by organisational stakeholders, satisfying
    sub-point (g)'s cross-reference to Art. 9. GV.RM-04 supplies
    the strategic-direction layer (risk appetite, response
    posture, escalation criteria) that connects policy
    formulation (GV.PO-01) and risk-objective setting
    (GV.RM-01) to operational risk-treatment decisions.
    Supplementary GV.PO-02 ensures that the policies are
    accompanied by processes and procedures that are also
    documented, communicated, and enforced — the systematic
    and orderly requirement of Art. 17(1). GV.OC-03 closes the
    loop by ensuring the QMS understands and manages the full
    set of legal, regulatory, and contractual obligations that
    the AI Act adds on top of CRA, NIS 2, GDPR, and DORA. The
    combined control set yields a documented policy stack,
    agreed risk-management objectives, a strategic-direction
    document, process and procedure manuals, and a legal/
    regulatory obligations register — the evidentiary
    substrate for the conformity-assessment body to examine
    the QMS as the umbrella obligation under the Art. 17
    QMS + Art. 9 risk-management + Art. 43/47 conformity-
    assessment accountability chain.
  ambiguity_notes: |
    Source clause AIA-C20 carries **S2** features (per
    `../Regulation/AI_Act/Ambiguity/06_AI_Act.md` §2.20). `systematic and orderly manner` is
    VAG-2 (Berry §5.1 — the OJ does not anchor the sense).
    `quality management system` is POLY-2 with R1 ISO 9001
    / R2 ISO/IEC 23053 (AI risk management framework
    standard) / R3 internal bespoke; the OJ does not name
    any specific standard (reading chosen: R3 literal). The
    3-way AND of `written policies, procedures AND instructions`
    and the 13-element closed list (a)–(m) are both COORD-2.
    AIA-C22 inherits POLY-2 from AIA-C01 (`risk management
    system` — the central AI Act ambiguity per `../Regulation/AI_Act/Ambiguity/06_AI_Act.md`
    §3.5). Remain open: (a) whether conformity-assessment
    bodies will accept an ISO 9001 certificate as a proxy
    for the QMS or require a stand-alone AI-QMS file; (b)
    whether the 13 elements must be discrete QMS chapters or
    can be embedded into a single integrated management
    system.
```

### SO-AIACT-001 (AI risk management lifecycle)

```yaml
- sr_id: SR-AIACT-018
  title: "Secure design control and verification integrated into SDLC"
  source_clauses:
    - { clause_id: AIA-C21, article_ref: "Art. 17(1)(c) — `techniques, procedures and systematic actions to be used for the design, design control and design verification of the high-risk AI system`" }
  linked_objectives: [SO-AIACT-010]
  sub_domain: [D-07.1]
  nist_csf_mapping:
    - { id: PR.PS-06, title: "Secure software development practices are integrated, and their performance is monitored throughout the SDLC" }
    - { id: PR.PS-01, title: "Configuration management practices are established, documented, and applied to assets" }
  applies_to_role: [PROVIDER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 17(1)(c) of Regulation (EU) 2024/1689 requires the QMS
    to include the techniques, procedures, and systematic actions
    used for the design, design control, and design verification
    of the high-risk AI system. This is the secure-development-
    lifecycle anchor of the QMS and is the operational bridge
    between Art. 17(1) (QMS) and Art. 9 (risk management) on
    one side, and Art. 15 (accuracy / robustness / cybersecurity)
    on the other. A compliance officer should treat Art. 17(1)(c)
    as the SDLC sub-process specification that the conformity
    assessment will examine alongside the technical documentation
    (Annex IV).
  security_rationale: |
    The Art. 17(1)(c) SDLC duty is operationalised in NIST CSF
    2.0 through **PR.PS-06 (Secure software development
    practices integrated across the SDLC)** and **PR.PS-01
    (Configuration management practices established,
    documented, applied)**, with supplementary alignment to
    **PR.PS-02 (Software maintenance commensurate with risk)**,
    **ID.RA-01 (Vulnerability identification, validation,
    recording)**, and **GV.PO-02 (Cybersecurity processes and
    procedures established, communicated, enforced)**. PR.PS-06
    is the principal anchor: it directly maps to the
    `techniques, procedures and systematic actions` for
    `design, design control and design verification` of the
    high-risk AI system, covering threat modelling (design),
    code review and change control (design control), and
    testing and review (design verification). PR.PS-01 enforces
    the design-control axis — configuration baselines,
    integrity of design artefacts, controlled changes — so
    that the design can be traced to its source and
    reconstructed. Supplementary PR.PS-02 binds software
    maintenance to the risk picture (patching, replacement,
    removal), closing the post-market SDLC loop. ID.RA-01
    ensures that vulnerabilities identified during design
    verification are recorded, validated, and feed back into
    the risk-management file under Art. 9. GV.PO-02 enforces
    that the SDLC is anchored in documented, communicated, and
    enforced processes. The combined control set yields
    documented design specifications, configuration baselines,
    change-control records, verification reports (test
    results, code-review records), vulnerability register
    entries, and process manuals — the evidentiary substrate
    for ex post demonstration of compliance under the Art. 17
    QMS + Art. 9 risk-management + Art. 15 accuracy-
    robustness-cybersecurity + Art. 43/47 conformity-
    assessment accountability chain.
  ambiguity_notes: |
    Source clause AIA-C21 carries **S2** POLY-2 on
    `design` vs. `design control` vs. `design verification`
    — three engineering terms with overlapping but distinct
    industry meanings (Berry §3.3.1; cf. ISO 9001 §8.3, IEC
    62304, NIST SP 800-218 SSDF PW.4/PW.5/PW.7). The 3-way
    AND of `design, design control AND design verification`
    + 3-way AND of `techniques, procedures AND systematic
    actions` is a twin 3-way AND that compounds the
    cumulative obligation (Berry §5.5). Remain open: (a)
    whether `design verification` requires independent
    verification (i.e. a separate team) or self-verification
    by the design team is acceptable; (b) whether the
    `systematic actions` axis covers post-deployment
    verification or only pre-market verification.
```

### SO-AIACT-001 (AI risk management lifecycle)

```yaml
- sr_id: SR-AIACT-021
  title: "Post-market monitoring feedback loop with documented analysis"
  source_clauses:
    - { clause_id: AIA-C25, article_ref: "Art. 72(1)–(2) — `Providers shall establish and document a post-market monitoring system in a manner that is proportionate to the nature of the AI technologies and the risks of the high-risk AI system. The post-market monitoring system shall actively and systematically collect, document and analyse relevant data`" }
    - { clause_id: AIA-C27, article_ref: "Art. 74(1) — `Regulation (EU) 2019/1020 shall apply to AI systems covered by this Regulation`" }
  linked_objectives: [SO-AIACT-012]
  sub_domain: [D-10.1]
  nist_csf_mapping:
    - { id: DE.CM-09, title: "Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events" }
    - { id: ID.IM-04, title: "Cybersecurity risk management improvements are informed by awareness of related developments and context (e.g., threat intelligence, incidents, technology evolution)" }
    - { id: GV.OV-03, title: "Organizational cybersecurity performance is evaluated and reviewed for needed adjustments" }
  applies_to_role: [PROVIDER, DEPLOYER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 72(1)–(2) of Regulation (EU) 2024/1689 requires high-
    risk AI providers to establish and document a post-market
    monitoring (PMM) system proportionate to the AI technology
    and the risks of the system, actively and systematically
    collecting, documenting, and analysing relevant data. The
    PMM system feeds the lifecycle consistency duty of
    Art. 15(1) and the serious incident reporting duty of
    Art. 73. Art. 74(1) extends Regulation (EU) 2019/1020
    (the EU market-surveillance framework) to AI systems,
    imposing market-surveillance cooperation obligations on
    providers and deployers. Recital 80 frames the PMM
    obligation as parallel to — but distinct from — the
    medical-device PMM obligation under MDR Art. 83; the
    borrow is implicit (the OJ does not name the MDR).
    A compliance officer should treat the PMM system as the
    ex-post assurance loop that complements the ex-ante
    conformity assessment.
  security_rationale: |
    The Art. 72(1)–(2) post-market monitoring duty is
    operationalised in NIST CSF 2.0 through **DE.CM-09
    (Computing hardware, software, runtime environments and
    data monitored for adverse events)**, **ID.IM-04
    (Improvements informed by threat intelligence,
    incidents, technology evolution)**, and **GV.OV-03
    (Organisational cybersecurity performance evaluated and
    reviewed for needed adjustments)**, with supplementary
    alignment to **DE.AE-03 (Event data collected and
    correlated from multiple sources)**, **GV.PO-02
    (Cybersecurity processes and procedures established,
    communicated, enforced)**, and **GV.OC-03 (Legal,
    regulatory, contractual requirements understood and
    managed)**. DE.CM-09 is the principal anchor: it binds
    the PMM system to the runtime monitoring of the AI
    substrate (inference logs, telemetry, drift indicators)
    so that adverse events are detected in the operational
    environment, not just asserted at conformity-assessment
    time. ID.IM-04 closes the feedback loop by requiring the
    PMM data to inform risk-management improvements
    (Art. 9 + Art. 15(1) lifecycle consistency), with
    explicit reference to threat intelligence, incidents,
    and technology evolution. GV.OV-03 enforces the
    organisational performance-evaluation cadence — the
    PMM data must be reviewed and trigger adjustments, not
    merely archived. Supplementary DE.AE-03 ensures
    cross-source event correlation; GV.PO-02 anchors the
    PMM system in documented, communicated, and enforced
    processes; and GV.OC-03 ensures the PMM system
    understands and manages the Regulation (EU) 2019/1020
    market-surveillance framework extended by Art. 74(1).
    The combined control set yields a documented PMM plan,
    runtime telemetry, an event-correlation pipeline, a
    review cadence with minutes, an improvement register,
    and a market-surveillance cooperation procedure — the
    evidentiary substrate for ex post demonstration of
    compliance under the Art. 9 risk-management + Art. 15
    lifecycle consistency + Art. 72 PMM + Art. 73 incident
    reporting + Art. 74(1) market-surveillance
    accountability chain.
  ambiguity_notes: |
    Source clause AIA-C25 carries **S2** features (per
    `06_AI_Art.md` §2.25). `proportionate to the nature` and
    `relevant data` are VAG-2. `post-market monitoring system`
    is POLY-2 — borrows from medical-device regulation (MDR
    Art. 83) but applied to AI; the borrow is implicit and
    practitioners must be familiar with both regimes. The
    adverbial AND `actively AND systematically` and the
    3-way verb AND `collect, document AND analyse` are
    COORD-2. AIA-C27 (`market surveillance`) is POLY-2 and
    borrows the entire Regulation (EU) 2019/1020 framework
    — operators unfamiliar with 2019/1020 cannot read this
    clause self-contained (Berry §3.3.1 cross-regulation
    borrow). Remain open: (a) whether the PMM plan must
    be submitted to the market-surveillance authority or
    is held internally; (b) whether deployer-side PMM
    contributions are mandatory or optional.
```

### SO-AIACT-001 (AI risk management lifecycle)

```yaml
- sr_id: SR-AIACT-022
  title: "Tiered serious incident reporting with differentiated timelines"
  source_clauses:
    - { clause_id: AIA-C26, article_ref: "Art. 73(1)–(4) — `report any serious incident`; `not later than 15 days after … becomes aware`; `not later than two days` (widespread infringement); `not later than 10 days` (death)" }
  linked_objectives: [SO-AIACT-013]
  sub_domain: [D-04.3]
  nist_csf_mapping:
    - { id: RS.CO-02, title: "Incidents are reported internally to the appropriate stakeholders, including executive leadership and legal counsel" }
    - { id: RS.CO-04, title: "Coordination with stakeholders occurs consistent with applicable rules and regulations" }
    - { id: RS.MA-03, title: "Incidents are categorized, prioritized, and scoped" }
    - { id: RS.MA-01, title: "The incident management plan is executed in coordination with relevant third parties once an incident is declared" }
  applies_to_role: [PROVIDER, DEPLOYER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 73(1)–(4) of Regulation (EU) 2024/1689 requires
    providers of high-risk AI systems, and deployers where
    applicable, to report any serious incident to the market
    surveillance authorities of the Member States where the
    incident occurred. The reporting timeline depends on the
    severity: 15 days after the provider becomes aware
    (default), 10 days if the incident results in death,
    2 days for widespread infringement. Art. 73(2)
    alternatively starts the 15-day clock on a reasonable
    likelihood to consider that a serious incident has
    occurred (whichever is later with the awareness trigger);
    the same 15-day window governs both attribution thresholds.
    Art. 3(49) defines `serious incident` via three
    sub-categories (a)/(b)/(c). Recital 92 sets the penalty
    envelope (Art. 99). The Art. 73 obligation is the most
    temporally complex notification clause in the AEGIS
    corpus — three numerical timelines (15 / 2 / 10 days) ×
    two attribution thresholds (awareness OR reasonable
    likelihood, whichever is later). A compliance officer
    should treat the Art. 73 timeline matrix as a mandatory
    operational reference, with pre-computed clock-start
    events and per-trigger escalation paths.
  security_rationale: |
    The Art. 73(1)–(4) serious-incident reporting duty is
    operationalised in NIST CSF 2.0 through **RS.CO-02
    (Incidents reported internally to executive leadership
    and legal counsel)**, **RS.CO-04 (Coordination with
    stakeholders consistent with applicable rules and
    regulations)**, **RS.MA-03 (Incidents categorised,
    prioritised, scoped)**, and **RS.MA-01 (Incident
    management plan executed in coordination with relevant
    third parties)**, with supplementary alignment to
    **RS.AN-03 (Root-cause analysis)**, **GV.OC-03 (Legal,
    regulatory, contractual requirements understood and
    managed)**, and **GV.PO-02 (Cybersecurity processes and
    procedures established, communicated, enforced)**.
    RS.CO-02 is the internal-reporting arm: the provider
    must route incident awareness to leadership and legal
    counsel so the market-surveillance report can be
    reviewed before transmission. RS.CO-04 is the
    external-reporting arm — coordination with the market
    surveillance authorities of the Member State(s) where
    the incident occurred, consistent with the Art. 73
    differentiated timelines. RS.MA-03 binds the reporting
    chain to a categorised scope so the correct timeline
    (15 / 10 / 2 days) is selected based on the incident
    class. RS.MA-01 ensures the provider's incident
    management plan is executed in coordination with
    deployers and other third parties, closing the
    provider-deployer handoff for joint incidents.
    Supplementary RS.AN-03 (root-cause analysis) supplies
    the substantiation the report must carry; GV.OC-03
    ensures the provider understands the cross-regulation
    (NIS 2 C30, DORA Art. 19) reporting obligations; and
    GV.PO-02 anchors the reporting workflow in documented
    processes. The combined control set yields an incident
    categorisation matrix, a timeline decision tree,
    internal-reporting records, external-reporting
    transmissions, a third-party coordination procedure,
    and a cross-regulation obligations register — the
    evidentiary substrate for ex post demonstration of
    compliance with the Art. 73 timeline matrix and the
    4-timeline × 4-trigger cross-product under the
    Art. 9 risk-management + Art. 72 PMM + Art. 73 incident
    reporting + Art. 99 penalty-envelope accountability
    chain.
  ambiguity_notes: |
    Source clause AIA-C26 carries **S3** features on three
    axes (per `../Regulation/AI_Act/Ambiguity/06_AI_Act.md` §2.26). `serious incident` is
    VAG-3 (defined in Art. 3(49) via three sub-categories
    (a)/(b)/(c) with distinct severity thresholds and
    undefined interaction; reading chosen: R3 literal —
    the three sub-categories apply independently and an
    incident can satisfy one or more). `becomes aware of
    the serious incident` is **SCOPE-Q-3** (Berry §5.7 —
    same awareness-trigger ambiguity as GDPR Art. 33
    `becomes aware`, CRA Art. 14, NIS 2 C30, DORA Art. 19;
    POLY+SCOPE-Q — R1 actual knowledge / R2 constructive
    knowledge / R3 either; R2 dominant CJEU reading
    applies). `reasonable likelihood of a causal link` is
    POLY-2 (distinct from `established causal link`; the
    two thresholds trigger the same 15-day clock).
    The 4-timeline × 4-trigger cross-product is **COORD-3**
    (Berry §5.7) — ≥16 distinct reporting-obligation
    shapes per `../Regulation/AI_Act/Ambiguity/06_AI_Act.md` §2.26. **Cross-article
    POLY:** the `serious incidents` of Art. 73 (high-risk)
    and Art. 55 (GPAI — SR-AIACT-024) may overlap; the
    boundary (when does a GPAI incident trigger Art. 73
    reporting vs. Art. 55 reporting vs. both?) is
    undefined. Remain open: (a) whether the 2-day
    widespread-infringement clock is calendar or business
    days; (b) whether the `immediate` reporting duty
    imposes a numeric clock (e.g. 24 hours) or is unbounded;
    (c) whether the Art. 73 vs. Art. 55 boundary is
    resolved by the AI Office or by the provider's own
    classification.
```

### SO-AIACT-001 (AI risk management lifecycle)

```yaml
- sr_id: SR-AIACT-023
  title: "Adversarial evaluation of GPAI models for systemic risk mitigation"
  source_clauses:
    - { clause_id: AIA-C28, article_ref: "Art. 55(1)(a) — `perform model evaluation in accordance with standardised protocols and tools reflecting the state of the art, including conducting and documenting adversarial testing of the model with a view to identifying and mitigating systemic risks`" }
  linked_objectives: [SO-AIACT-014]
  sub_domain: [D-07.3, D-02.1]
  nist_csf_mapping:
    - { id: GV.RM-06, title: "A standardized method for calculating, documenting, categorizing, and prioritizing cybersecurity risks is established and communicated" }
    - { id: ID.RA-04, title: "Potential impacts and likelihoods of threats exploiting vulnerabilities are identified, recorded, and prioritized" }
    - { id: PR.PS-06, title: "Secure software development practices are integrated, and their performance is monitored throughout the SDLC" }
  applies_to_role: [PROVIDER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 55(1)(a) of Regulation (EU) 2024/1689 requires
    providers of general-purpose AI (GPAI) models with
    systemic risk to perform model evaluation in
    accordance with standardised protocols and tools
    reflecting the state of the art, including conducting
    and documenting adversarial testing of the model with
    a view to identifying and mitigating systemic risks.
    Art. 55 sits in Title IV (General-Purpose AI Models),
    Chapter V (Obligations of Providers of GPAI Models
    with Systemic Risk), and is parallel to — but
    distinct from — the Title III high-risk AI obligations
    of Arts. 9–15. Recital 110 frames the model-evaluation
    obligation as the upstream assurance for foundation
    models that can serve many downstream AI applications.
    A compliance officer at a GPAI provider should treat
    Art. 55(1)(a) as the technical-assurance anchor of
    the systemic-risk regime, on par with the QMS
    obligation of Art. 17(1) for high-risk providers.
  security_rationale: |
    The Art. 55(1)(a) GPAI model-evaluation duty is
    operationalised in NIST CSF 2.0 through **GV.RM-06
    (Standardised method for calculating, documenting,
    categorising, prioritising cybersecurity risks)**,
    **ID.RA-04 (Threat-impact prioritisation)**, and
    **PR.PS-06 (Secure SDLC practices integrated,
    performance monitored)**, with supplementary alignment
    to **GV.OC-03 (Legal, regulatory, contractual
    requirements understood and managed)**, **GV.PO-01
    (Organisational cybersecurity policy established,
    communicated, enforced)**, and **GV.OV-02 (Strategy
    reviewed against changing risk landscape)**. GV.RM-06
    is the principal anchor: it operationalises the
    `standardised protocols` element of Art. 55(1)(a) by
    requiring the GPAI provider to establish and
    communicate a standardised risk-calculation method,
    so that the model-evaluation is reproducible and
    defensible rather than ad hoc. ID.RA-04 enforces the
    `identifying systemic risks` element: threats,
    vulnerabilities, likelihoods, and impacts are
    recorded and prioritised, providing the structured
    input to the `mitigating systemic risks` follow-up.
    PR.PS-06 binds the `conducting and documenting`
    element to the SDLC substrate — secure development
    practices, threat modelling, and verification
    artefacts, so that the adversarial testing produces
    auditable records. Supplementary GV.OC-03 ensures
    the GPAI provider understands the layered regulatory
    regime (AI Act + CRA + NIS 2 + DORA for financial-
    sector GPAI), GV.PO-01 anchors the model-evaluation
    programme in a top-level policy, and GV.OV-02
    enforces the strategy-review cadence required by
    the `state of the art` element. The combined
    control set yields a standardised evaluation
    methodology, prioritised systemic-risk register,
    adversarial-testing reports, SDLC artefacts, a
    top-level policy, a cross-regulation obligations
    register, and strategy-review minutes — the
    evidentiary substrate for ex post demonstration of
    compliance with the Art. 55(1)(a) model-evaluation
    + Art. 9 risk-management + Art. 15(4)–(5) AI-
    specific attack + Art. 72 PMM accountability chain.
  ambiguity_notes: |
    Source clause AIA-C28 carries three **S3** features
    (per `../Regulation/AI_Act/Ambiguity/06_AI_Act.md` §2.28 — the second-most-
    consequential AI Act ambiguity after `risk management
    system`). `standardised protocols` is VAG-3 (R1 ISO/IEC
    standards / R2 NIST standards / R3 MLCommons benchmarks;
    reading chosen: R3 literal — the clause does not anchor
    the sense, so the OJ defers to whichever standard the
    provider can defend as `state of the art`). `state of
    the art` is VAG-3 (Berry classic; cf. GDPR C09, CRA C07;
    time-dependent, jurisdiction-dependent). `systemic risks`
    is VAG-3 (undefined at Union level for AI; the term is
    borrowed from financial-services regulation where it
    has a specific meaning; the AI-Act use is broader —
    the borrow is implicit and operators unfamiliar with
    DORA Art. 4(50) cannot read this clause self-contained).
    `adversarial testing` is POLY-2 (distinct from
    red-teaming, fuzzing, robustness testing). The
    `conducting AND documenting` + `identifying AND
    mitigating` pairs are COORD-2. The triple
    `standardised protocols + state of the art + systemic
    risks` is **the second-most-consequential AI Act
    ambiguity** per `../Regulation/AI_Act/Ambiguity/06_AI_Act.md` §3.5. Remain open:
    (a) whether the AI Office will issue a list of
    recognised `standardised protocols` or leave the
    determination to the provider; (b) whether
    `systemic risks` includes downstream-application-
    level risks or only foundation-model-level risks;
    (c) whether `adversarial testing` requires a public
    report (as some red-team frameworks recommend) or
    a confidential internal report.
```

### SO-AIACT-001 (AI risk management lifecycle)

```yaml
- sr_id: SR-AIACT-024
  title: "GPAI serious incident reporting to the AI Office"
  source_clauses:
    - { clause_id: AIA-C29, article_ref: "Art. 55(1)(c) — `keep track of, document, and report, without undue delay, to the AI Office and, as appropriate, to national competent authorities, relevant information about serious incidents and possible corrective measures to address them`" }
  linked_objectives: [SO-AIACT-014]
  sub_domain: [D-04.3]
  nist_csf_mapping:
    - { id: RS.CO-02, title: "Incidents are reported internally to the appropriate stakeholders, including executive leadership and legal counsel" }
    - { id: RS.MA-03, title: "Incidents are categorized, prioritized, and scoped" }
    - { id: RS.AN-03, title: "Analysis is performed to determine what has occurred during an event and the root cause of the event" }
  applies_to_role: [PROVIDER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 55(1)(c) of Regulation (EU) 2024/1689 requires
    providers of general-purpose AI models with systemic
    risk to keep track of, document, and report, without
    undue delay, to the AI Office and, as appropriate, to
    national competent authorities, relevant information
    about serious incidents and possible corrective
    measures to address them. The recipient differs from
    the high-risk AI obligation of Art. 73 — the GPAI
    report goes to the AI Office (an EU-level body
    established by Art. 64), not the market surveillance
    authorities of the Member States. Recital 110
    clarifies the GPAI-specific nature of the obligation
    and the upstream nature of the reporting (foundation
    model vs. downstream application). A compliance officer
    at a GPAI provider should treat Art. 55(1)(c) as the
    upstream companion to the high-risk Art. 73 obligation,
    with a separate recipient and a separate (open-text)
    timeline.
  security_rationale: |
    The Art. 55(1)(c) GPAI serious-incident reporting duty
    is operationalised in NIST CSF 2.0 through **RS.CO-02
    (Incidents reported internally to executive leadership
    and legal counsel)**, **RS.MA-03 (Incidents
    categorised, prioritised, scoped)**, and **RS.AN-03
    (Root-cause analysis)**, with supplementary alignment
    to **GV.OC-03 (Legal, regulatory, contractual
    requirements understood and managed)**, **GV.PO-01
    (Organisational cybersecurity policy established,
    communicated, enforced)**, and **RS.CO-04
    (Coordination with stakeholders consistent with
    applicable rules and regulations)**. RS.CO-02 is the
    internal-reporting arm: the GPAI provider must route
    incident awareness to leadership and legal counsel so
    the AI Office report can be reviewed and the
    `without undue delay` clock is controlled. RS.MA-03
    binds the reporting to a categorised scope so the
    `serious incidents AND possible corrective measures`
    elements are both addressed. RS.AN-03 enforces the
    root-cause analysis that the report must carry to
    satisfy the `relevant information` element of
    Art. 55(1)(c). Supplementary GV.OC-03 ensures the
    GPAI provider understands the cross-regulation
    reporting regime (Art. 55 GPAI + Art. 73 high-risk
    + NIS 2 C30 + DORA Art. 19, with the Art. 55 vs.
    Art. 73 boundary per the SR-AIACT-022 ambiguity
    note). GV.PO-01 anchors the reporting workflow in
    a top-level policy; and RS.CO-04 ensures
    coordination with the AI Office and national
    competent authorities is consistent with applicable
    rules. The combined control set yields a categorised
    incident register, a root-cause analysis pipeline,
    internal-reporting records, AI Office transmissions,
    a top-level policy, a cross-regulation obligations
    register, and a coordination procedure — the
    evidentiary substrate for ex post demonstration of
    compliance with the Art. 55(1)(c) reporting duty
    under the Art. 9 risk-management + Art. 55(1)(a)
    model-evaluation + Art. 55(1)(c) GPAI incident
    reporting + Art. 72 PMM accountability chain.
  ambiguity_notes: |
    Source clause AIA-C29 carries three **S3** features
    (per `../Regulation/AI_Act/Ambiguity/06_AI_Act.md` §2.29). `without undue delay`
    is VAG-3 (Berry classic; cf. NIS 2 C30 on `without
    undue delay`). `relevant information` is VAG-3
    (the OJ does not enumerate what is `relevant`).
    `as appropriate` is POLY-3 (R1 mandatory / R2
    optional / R3 case-by-case). The `serious incidents`
    term is **POLY-3** for GPAI models — distinct from
    `serious incidents` for high-risk AI systems (Art. 73)
    but the cross-reference is implicit; the boundary
    (when does a GPAI incident trigger Art. 55 reporting
    vs. Art. 73 reporting vs. both?) is undefined
    (Berry §3.3.1 cross-article polysemy). The 3-way
    verb AND `keep track of, document, AND report` and
    the AND `serious incidents AND possible corrective
    measures` are COORD-2. Remain open: (a) whether
    `without undue delay` imposes a numeric clock (and
    if so, what number — 72h? 7d?) or is unbounded;
    (b) whether the `as appropriate` axis is mandatory
    when the national competent authority requests
    the report; (c) whether the AI Office will issue
    a unified incident-reporting template that
    resolves the Art. 55 vs. Art. 73 boundary.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

