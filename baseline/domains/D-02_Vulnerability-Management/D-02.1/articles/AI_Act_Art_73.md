---
document_id: AEGIS-PREPROC-AI_Act-ART-73
title: AI_Act Art. 73 — SecurityObjectives & SecurityRules
regulation: AI_Act
article: Art. 73
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-02_Vulnerability-Management/D-02.1.md
  - ../../CrossRegulation/DeepAnalysis/D-02_Vulnerability-Management/D-02.1.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DomainAnalysis/D-07_Secure-Development/D-07.2.md
  - ../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.2.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.1.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.1.md
status: DRAFT
---

# AI_Act Art. 73

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-AIACT-013 | Providers and deployers of high-risk AI systems report any serious incident to the market surveillance authorities of the Member States where the incident occurred, in accordance with the differentiated timelines and triggers (awareness / causal link / death / widespread infringement) of Art. 73(1)–(4). | `AIA-C26` (Art. 73(1)–(4) — 4 differentiated timelines × 4 distinct triggers; `serious incident` defined in Art. 3(49) via three sub-categories (a)/(b)/(c); 28 instances of S3 ambiguity across VAG+SCOPE-Q+POLY+COORD) | D-04.3 |
| SO-AIACT-013 | D-04.3 | Art. 73(1)–(4) | Serious incident reporting with 4 differentiated timelines × 4 triggers |
| SO-AIACT-014 | Providers of general-purpose AI models with systemic risk keep track of, document and report relevant information about serious incidents and possible corrective measures to the AI Office and, as appropriate, to national competent authorities, without undue delay. | `AIA-C28` (Art. 55(1)(a) — `standardised protocols` + `state of the art` + `systemic risks` POLY triple; adversarial testing mandate); `AIA-C29` (Art. 55(1)(c) — `serious incidents` POLY distinct from Art. 73 serious incidents; `without undue delay` VAG; cross-article boundary undefined) | D-04.3 |

## Security Rules (from 02_SecurityRules_NIST.md)

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

