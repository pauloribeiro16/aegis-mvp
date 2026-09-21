---
document_id: AEGIS-PREPROC-GDPR-ART-36
title: GDPR Art. 36 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 36
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
  - ../../CrossRegulation/DomainAnalysis/D-08_Human-Factors/D-08.1.md
  - ../../CrossRegulation/DeepAnalysis/D-08_Human-Factors/D-08.1.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.2.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.2.md
status: DRAFT
---

# GDPR Art. 36

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-GDPR-013 | Where a data-protection impact assessment indicates that the intended processing would result in a high risk in the absence of mitigation measures, the controller consults the supervisory authority prior to processing. | `GDPR-CP23` (Art. 36(1)); `GDPR-CP24` (Art. 36(2)) | D-04.3, D-09.2 |
| SO-GDPR-013 | D-04.3, D-09.2 | Art. 36(1)/(2) | Prior consultation with supervisory authority |
| SO-GDPR-028 | Prior to processing that is likely to result in a high risk to the rights and freedoms of natural persons, the controller carries out a data-protection impact assessment covering the four Art. 35(7) content items (systematic description, necessity & proportionality, risks, mitigation measures); the assessment is reviewed on change of risk. | `GDPR-CP21` (Art. 35(1)–(4)); `GDPR-CP22` (Art. 35(7)/(11)); `GDPR-C23` (Art. 9(2)(g)); `GDPR-CP23` (Art. 36(1)) | D-09.2 |
| SO-GDPR-028 | D-09.2 | Art. 35(1)–(4)/(7), Art. 9(2)(g), Art. 36(1) | Pre-launch DPIA for high-risk processing |

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
- sr_id: SR-GDPR-045
  title: "Pre-launch DPIA with risk treatment and prior-consultation trigger"
  source_clauses:
    - { clause_id: GDPR-CP21, article_ref: "Art. 35(1) — DPIA trigger" }
    - { clause_id: GDPR-CP22, article_ref: "Art. 35(7) — DPIA content" }
    - { clause_id: GDPR-CP23, article_ref: "Art. 36(1) — prior consultation (cross)" }
    - { clause_id: GDPR-C01, article_ref: "Art. 4(1) — personal data" }
  linked_objectives: [SO-GDPR-028]
  sub_domain: [D-09.2]
  nist_csf_mapping:
    - { id: ID.RA-01, title: "Vulnerabilities in assets are identified, validated, and recorded" }
    - { id: ID.RA-05, title: "Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response decisions" }
    - { id: ID.RA-06, title: "Risk responses are chosen, prioritized, planned, tracked, and communicated" }
  applies_to_role: [CONTROLLER]
  obligation_type: [TRIGGERED, PERIODIC]
  regulatory_rationale: |
    Art. 35(1) requires the controller to carry out an assessment of
    the impact of the envisaged processing operations on the protection
    of personal data, prior to processing, where the processing is
    likely to result in a high risk to the rights and freedoms of
    natural persons, in particular using new technologies. Art. 35(7)
    specifies the four content items: a systematic description of the
    processing and purposes; an assessment of necessity and
    proportionality; an assessment of the risks to data-subject
    rights; and the measures envisaged to address the risks. Art. 36(1)
    requires prior consultation with the supervisory authority where
    the DPIA indicates that processing would result in a high risk in
    the absence of mitigation measures. Art. 4(1) supplies the personal-
    data definition on which the DPIA scope rests.
  security_rationale: |
    The obligation in Art. 35(1), Art. 35(7) and Art. 36(1) to carry out a pre-launch data-protection impact assessment for processing likely to result in a high risk, covering the four Art. 35(7) content items, and to consult the supervisory authority where the residual risk remains high, is operationalised in NIST CSF 2.0 through **ID.RA-01 (Vulnerabilities in assets are identified, validated, and recorded)**, **ID.RA-05 (Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response decisions)** and **ID.RA-06 (Risk responses are chosen, prioritized, planned, tracked, and communicated)**.
    ID.RA-01 captures the asset-level vulnerability-recording discipline: the DPIA's systematic-description requirement (Art. 35(7)(a)) is operationally the same as the vulnerability-recording posture that the controller maintains for the data, processing and supporting assets under assessment.
    ID.RA-05 captures the inherent-risk understanding requirement in Art. 35(7)(c): threats (including new-technology exposures), vulnerabilities, likelihoods and impacts must be brought together to understand the inherent risk envelope of the processing, before any risk-response measure is layered on top.
    ID.RA-06 captures the risk-response layer in Art. 35(7)(d) and Art. 36(1): the controller must choose, prioritise, plan and track the measures that address the identified risks, and where residual risk stays high the prior-consultation obligation under Art. 36(1) is triggered, with the supervisory authority becoming the next-step risk-response stakeholder.
    A controller that documents ID.RA-01 vulnerability coverage, ID.RA-05 inherent-risk assessment and ID.RA-06 risk-response selection plus Art. 36(1) consultation trigger can demonstrate ex post, against the Art. 5(2) accountability duty, that on the day of any high-risk processing the controller had performed and refreshed the four-part DPIA and consulted the supervisory authority where the threshold was met.
  ambiguity_notes: |
    Source clause GDPR-CP21 carries Berry-flagged S3 POLY+VAG on `new
    technologies` and `high risk` (Berry §5.1, §3.3.1). `New
    technologies` is the recurring time-dependent phrase — was cloud
    `new` in 2018, is generative AI `new` in 2026. The reading adopted
    for this SR is that `new technologies` means technologies not
    widely deployed in the industry at the time of assessment (EDPB
    Guidelines 4/2019). `High risk` inherits the Art. 35(1) threshold,
    with the EDPB Guidelines 4/2019 nine-criteria list as the
    operational anchor (evaluation and scoring, automated decision-
    making with legal effect, systematic monitoring, sensitive data or
    data of a vulnerable nature, data processed on a large scale,
    combination of data, data concerning vulnerable data subjects,
    innovative use or applying new technological or organisational
    solutions, and processing that prevents data subjects from
    exercising a right or using a service). Two alternative readings
    remain. First, a strict supervisory-list reading would limit DPIA
    triggers to those listed by the national supervisory authority
    under Art. 35(4); this conflicts with Art. 35(1), which is open-
    textured. Second, a controller-discretion reading that treats the
    EDPB criteria as illustrative would weaken the high-risk threshold.
    Remain open: (a) whether generative-AI model training falls inside
    or outside `new technologies` in 2026; (b) whether a single DPIA
    may legitimately cover a set of similar processing operations per
    Art. 35(1) when the operations span multiple controllers in a
    joint-controllership arrangement.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-064
  title: "Advisory, monitoring and assurance delivered by DPO function"
  source_clauses:
    - { clause_id: GDPR-CP28, article_ref: "Art. 39(1)(a)–(e) — DPO tasks" }
    - { clause_id: GDPR-CP28, article_ref: "Art. 39(2) — risk-associated processing" }
  linked_objectives: [SO-GDPR-037, SO-GDPR-025]
  sub_domain: [D-09.1, D-09.2, D-08.1]
  nist_csf_mapping:
    - { id: GV.OV-03, title: "Organizational cybersecurity performance evaluated and reviewed" }
    - { id: PR.AT-02, title: "All workforce understand their role-specific security responsibilities" }
    - { id: ID.IM-02, title: "Improvement processes implemented across organizational tiers" }
  applies_to_role: [DPO]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 39(1) requires the DPO to have at least the following tasks: (a) inform and advise the controller, the processor and employees on their GDPR obligations; (b) monitor compliance, including assignment of responsibilities, awareness-raising and training, and related audits; (c) provide advice where requested on data protection impact assessments and monitor their performance pursuant to Art. 35; (d) cooperate with the supervisory authority; (e) act as the contact point for the supervisory authority on processing issues, including Art. 36 consultation. Art. 39(2) requires that the DPO have due regard to the risk associated with processing operations, taking into account the nature, scope, context and purposes of processing.
    [OJ-corrective note (v0.2 audit): the OJ text reads verbatim — to provide advice where requested as regards the data protection impact assessment and monitor its performance pursuant to Article 35]
  security_rationale: |
    The obligation in Art. 39(1)(a)–(e) and Art. 39(2) is operationalised in NIST
    CSF 2.0 through **GV.OV-03 (Organizational cybersecurity performance evaluated
    and reviewed for needed adjustments)**, **PR.AT-02 (All members of the
    organization's workforce understand their roles and responsibilities in
    achieving the organization's cybersecurity objectives)** and **ID.IM-02
    (Improvement processes for cybersecurity risk management implemented across
    organizational tiers)**.

    GV.OV-03 controls the monitoring and audit dimension of the DPO role under
    Art. 39(1)(b): the DPO evaluates organisational compliance with the GDPR,
    assigns responsibilities, and runs the related audits, with the performance
    review feeding back into management. PR.AT-02 controls the awareness-raising
    and training dimension under Art. 39(1)(b): the workforce must understand its
    role-specific responsibilities, with the DPO orchestrating the curricula.
    ID.IM-02 controls the continuous-improvement dimension under Art. 39(1)(c):
    DPIA advice and monitoring drive improvement processes across organisational
    tiers, scaled to the risk associated with processing operations under Art.
    39(2).

    Together the three subcategories embed the DPO as the privacy-and-security
    assurance function across evaluation (GV.OV-03), awareness (PR.AT-02) and
    improvement (ID.IM-02), enabling ex-post demonstration through an annual
    report to the highest management level that the advisory, monitoring and
    assurance tasks were performed and that the resulting improvements were
    adopted.
  ambiguity_notes: |
    The five-element AND-list under Art. 39(1)(a)–(e) is COORD-S2: all five tasks are mandatory and the DPO must be in a position to perform each of them. The where-requested qualifier on Art. 39(1)(c) is a request-trigger qualifier on the advisory task, while monitor its performance is a continuous obligation; the two are separate and not interchangeable. Due regard to the risk in Art. 39(2) is VAG-S2; both readings converge on a risk-proportionate DPO-task practice in which the DPO prioritises and scales effort according to the assessed risk of the processing operations at issue. Remain open: (a) whether the where-requested qualifier on Art. 39(1)(c) advisory applies per DPIA or per controller; (b) whether awareness-raising under Art. 39(1)(b) must include role-specific curricula per processing role, or whether generic privacy-awareness content satisfies the obligation.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

