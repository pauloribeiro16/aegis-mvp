---
document_id: AEGIS-PREPROC-AI_Act-ART-15
title: AI_Act Art. 15 — SecurityObjectives & SecurityRules
regulation: AI_Act
article: Art. 15
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
  - ../../CrossRegulation/DomainAnalysis/D-07_Secure-Development/D-07.1.md
  - ../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.1.md
  - ../../CrossRegulation/DomainAnalysis/D-07_Secure-Development/D-07.2.md
  - ../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.2.md
  - ../../CrossRegulation/DomainAnalysis/D-07_Secure-Development/D-07.3.md
  - ../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.3.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.1.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.1.md
status: DRAFT
---

# AI_Act Art. 15

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-AIACT-009 | D-07.1, D-02.1, D-01.4 | Art. 15(1)+(3)+(4)–(5) | Accuracy, robustness, cybersecurity + resilience + AI-attack defence |

## Security Rules (from 02_SecurityRules_NIST.md)

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

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

