---
document_id: AEGIS-PREPROC-DORA-ART-17
title: DORA Art. 17 — SecurityObjectives & SecurityRules
regulation: DORA
article: Art. 17
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.1.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.1.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.4.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.4.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.3.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.3.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.1.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.1.md
status: DRAFT
---

# DORA Art. 17

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-DORA-008 | An ICT-related incident management process is defined, established and implemented to detect, manage and notify ICT-related incidents; major ICT-related incidents are reported to the relevant competent authority, and clients are informed about the major ICT-related incident without undue delay as soon as the financial entity becomes aware of it. | `DORA-C30` (Art. 17(1) incident management process — twin 3-way verb coordination: define/establish/implement + detect/manage/notify); `DORA-C31` (Art. 19(1)+(3) major incident reporting to CA + client notification — twin temporal trigger `without undue delay AS SOON AS they become aware`) | D-04.1, D-04.3 |
| SO-DORA-008 | D-04.1, D-04.3 | Art. 17(1) + Art. 19(1)+(3) | Incident management process + major incident reporting |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-DORA-001 (CIA + A maintained across data states)

```yaml
- sr_id: SR-DORA-011
  title: "Multi-class anomalous activity detection with SPOF identification"
  source_clauses:
    - { clause_id: DORA-C20, article_ref: "Art. 10(1) — `mechanisms to promptly detect anomalous activities … including ICT network performance issues and ICT-related incidents, and to identify potential material single points of failure`" }
  linked_objectives: [SO-DORA-007]
  sub_domain: [D-04.1, D-10.1]
  nist_csf_mapping:
    - { id: DE.CM-01, title: "Networks and network services are monitored to find potentially adverse events" }
    - { id: DE.CM-09, title: "Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events" }
    - { id: DE.AE-02, title: "Detected events are analyzed to understand attack targets and methods" }
  applies_to_role: [FINANCIAL_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 10(1) requires financial entities to deploy mechanisms to
    promptly detect anomalous activities, in accordance with Art. 17,
    including ICT network performance issues and ICT-related incidents,
    and to identify potential material single points of failure.
    Article 10 Chapter II Section II establishes the detection
    substrate that Chapter III operationalises into the incident-
    management process. The cross-reference `in accordance with Art.
    17` ties detection to incident-management process (NIS 2 Art.
    21(2)(b) on incident-handling imposes a parallel baseline on
    NSIEs that DORA NSIEs also satisfy). Recital 54 highlights
    the dual objective: cyber-threat detection and operational-
    performance anomaly detection (the latter catching availability-
    oriented incidents that the cyber-threat lens alone would miss).
    [OJ-corrective note (v0.2 audit, cosmetic): Art. 10(1) — "deploy" vs "have in place". OJ Art. 10(1) reads: `Financial entities shall have in place mechanisms to promptly detect anomalous activities` — the operative verb is `have in place`, not `deploy`. Operatively equivalent; no operational change required.]
  security_rationale: |
    The obligation in Art. 10(1) for prompt detection of anomalous
    activities and SPOF identification is operationalised in NIST CSF
    2.0 through **DE.CM-01 (Networks and network services are monitored
    to find potentially adverse events)**, **DE.CM-09 (Computing
    hardware and software, runtime environments, and their data are
    monitored to find potentially adverse events)**, and **DE.AE-02
    (Detected events are analyzed to understand attack targets and
    methods)**. DE.CM-01 covers the network-layer detection surface —
    flow telemetry, IDS/IPS signatures, east-west traffic baselining,
    DNS-monitoring, and CTPP-traffic anomaly detection. DE.CM-09
    extends coverage to the compute-layer surface — endpoint
    detection and response, file-integrity monitoring, runtime-
    anomaly detection on transaction-processing hosts, and
    authentication-system anomaly detection. DE.AE-02 supplies the
    analysis layer that converts raw detections into understood
    attack patterns and supports SPOF identification through
    performance-anomaly correlation (latency drift, error-rate
    spikes, capacity-saturation). The OJ three-class coverage
    (network, compute, performance) maps directly onto these three
    DE subcategories, ensuring no detection blind spot. The
    accountability link under Art. 5(2): the detection-coverage
    matrix, SPOF register, and analysis-output records produce the
    documented evidence trail the management body can present to
    competent authorities demonstrating that detection is genuinely
    multi-class and SPOF-aware rather than cyber-flavour-only.
  ambiguity_notes: |
    Source clause DORA-C20 carries S2 on `promptly` (VAG — no
    specified time-to-detect; reading chosen: R3 risk-based, per
    entity risk profile), S2 on `potential material` (VAG — VAG +
    POLY combined; reading chosen: R1 reasonable-judgment-of-
    materiality), and S2 on `anomalous activities` (POLY — R1
    security anomaly / R2 performance anomaly / R3 behavioural
    anomaly; reading chosen: R3 cumulative, all three classes per
    the `including ICT network performance issues AND ICT-related
    incidents` opening). A contrasting reading of `promptly` would
    treat the term as a supervisor-imposed deterministic window
    (e.g. 24 hours), but no OJ-text support exists for a
    deterministic interpretation. An alternative reading would limit
    `anomalous activities` to cyber-security flavour only, ignoring
    the OJ qualifier `including ICT network performance issues` —
    this reading is rejected because the qualifier is in OJ text.
```

### SO-DORA-001 (CIA + A maintained across data states)

```yaml
- sr_id: SR-DORA-016
  title: "End-to-end ICT-related incident management process with root-cause analysis"
  source_clauses:
    - { clause_id: DORA-C30, article_ref: "Art. 17(1) — `define, establish and implement an ICT-related incident management process to detect, manage and notify ICT-related incidents`" }
  linked_objectives: [SO-DORA-008]
  sub_domain: [D-04.1, D-04.3]
  nist_csf_mapping:
    - { id: RS.MA-01, title: "The incident management plan is executed in coordination with relevant third parties once an incident is declared" }
    - { id: RS.AN-03, title: "Analysis is performed to determine what has occurred during an event and the root cause of the event" }
  applies_to_role: [FINANCIAL_ENTITY]
  obligation_type: [CONTINUOUS, TRIGGERED]
  regulatory_rationale: |
    Art. 17(1) requires financial entities to define, establish and
    implement an ICT-related incident management process to detect,
    manage and notify ICT-related incidents. Article 17 Chapter III
    chapeau establishes the process obligation that Art. 18
    classification and Art. 19 reporting operationalise (NIS 2
    Art. 21(2)(b) on incident-handling and Art. 23 on incident-
    notification impose parallel obligations on NSIEs outside
    DORA, with the cross-notification interface between DORA
    Art. 19 and GDPR Art. 33 on personal-data breach creating
    composite supervisory exposure). The three-verb coordination
    `define, establish and implement` is process-setup; the
    three-verb coordination `detect, manage and notify` is
    process-operation. Both coordinations are read cumulatively
    per the OJ coordination grammar.
  security_rationale: |
    The obligation in Art. 17(1) for an end-to-end ICT-related
    incident management process is operationalised in NIST CSF 2.0
    through **RS.MA-01 (The incident management plan is executed
    in coordination with relevant third parties once an incident
    is declared)** and **RS.AN-03 (Analysis is performed to
    determine what has occurred during an event and the root cause
    of the event)**. RS.MA-01 establishes the process-execution
    layer: the two OJ three-verb coordinations — `define, establish
    and implement` (process setup) and `detect, manage and notify`
    (process operation) — map onto pre-incident planning and post-
    declaration execution dimensions respectively, with third-
    party-coordination covering CTPPs, competent authorities, and
    client-communication channels under Art. 19 and Art. 14. RS.AN-03
    supplies the root-cause-analysis substrate that converts
    incident response into organisational learning, ensuring the
    process is genuinely end-to-end rather than terminating at
    containment. The OJ Chapter III framing (Art. 17 chapeau, Art. 18
    classification, Art. 19 reporting) is operationalised through
    RS.MA-01's third-party-coordination dimension, with RS.AN-03
    findings feeding back into SR-DORA-005's annual scenario-register
    refresh and SR-DORA-007's patch-priority ordering. The
    accountability link under Art. 5(2): the process-charter
    documentation, incident-timeline records, root-cause-analysis
    findings, and notification-completion logs produce the
    documented evidence trail the management body can present to
    competent authorities demonstrating that incident management
    is process-driven, auditably end-to-end, and learning-feeding
    rather than containment-terminating.
  ambiguity_notes: |
    Source clause DORA-C30 carries S2 on the twin 3-way verb
    coordinations: `define, establish AND implement` (process setup
    verbs) and `detect, manage AND notify` (process operation
    verbs). Reading chosen: R1 cumulative — all three setup
    activities required, all three operation activities required.
    `ICT-related incident` (POLY S2) — distinct from `cyber
    incident` (narrower) and `business continuity event` (broader);
    R1 OJ-literal locus at ICT-related. A contrasting reading of
    `ICT-related incident` would import a GDPR-style `personal
    data breach` framing, but the OJ definition in Art. 3(8) is
    broader and includes any ICT-related availability, integrity,
    confidentiality or authenticity incident (CRA Art. 3(40)
    defines `actively exploited vulnerability` which can trigger
    ICT-related incidents under Art. 3(8) when exploited in
    financial entities' ICT systems). An open question is whether
    a major ICT-related incident under Art. 18 always triggers
    parallel reporting under GDPR Art. 33 or only when the
    incident involves personal data (the cross-regulation trigger
    characterisation remains unsettled in OJ text).
```

### SO-DORA-001 (CIA + A maintained across data states)

```yaml
- sr_id: SR-DORA-017
  title: "Major-ICT-incident notification to supervisor and affected clients"
  source_clauses:
    - { clause_id: DORA-C31, article_ref: "Art. 19(1) — `Financial entities shall report major ICT-related incidents to the relevant competent authority`" }
    - { clause_id: DORA-C31, article_ref: "Art. 19(3) — `financial entities shall, without undue delay as soon as they become aware of it, inform their clients about the major ICT-related incident`" }
  linked_objectives: [SO-DORA-008]
  sub_domain: [D-04.3]
  nist_csf_mapping:
    - { id: RS.CO-02, title: "Incidents are reported internally to the appropriate stakeholders, including executive leadership and legal counsel" }
    - { id: RS.CO-04, title: "Coordination with stakeholders occurs consistent with applicable rules and regulations" }
  applies_to_role: [FINANCIAL_ENTITY]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 19(1) imposes on financial entities a hard duty to notify the relevant
    competent authority of any major ICT-related incident, operating in parallel
    with — and not substituting for — the GDPR Art. 72-hour personal data breach
    notification under Regulation (EU) 2016/679 Art. 33 and the NIS 2 incident-
    notification workflow under Directive (EU) 2022/2555 Art. 23, both of which
    must be triggered under their own criteria where applicable. The OJ Art. 19(1)
    trigger is the moment of classification as `major`, not the moment of awareness,
    while Art. 19(3) operates on a separate clock — `without undue delay as soon as
    they become aware` — which is direct client-facing disclosure. The threshold
    classification itself (Art. 18) delegates the criteria combination and
    materiality thresholds to an EBA/ESMA/EIOPA RTS under Art. 18(3), with
    Implementing Regulation (EU) 2024/2956 partially addressing reporting templates
    in Annex I to IV. The recital frame (recital 56) confirms the sector-differentiated
    hour-anchors and the recital frame on all-hazards coverage supports the
    classification-as-trigger reading.
    [OJ-corrective note (v0.2 audit, material): Art. 19(3) — trigger condition dropped. OJ Art. 19(3) conditions client notification: `Where a major ICT-related incident occurs AND HAS AN IMPACT ON THE FINANCIAL INTERESTS OF CLIENTS, financial entities shall, without undue delay as soon as they become aware of it, inform their clients about the major ICT-related incident and about the measures that have been taken to mitigate the adverse effects of such incident.` The SR drops the trigger condition `and has an impact on the financial interests of clients` — converting a conditional obligation into an unconditional one. Every major incident would trigger client notification under the SR; OJ scopes to those with client-financial-impact.]
  security_rationale: |
    The Art. 19 major-incident notification duty is operationalised in NIST CSF
    2.0 through **RS.CO-02 (Incidents are reported internally to the appropriate
    stakeholders, including executive leadership and legal counsel)** and
    **RS.CO-04 (Coordination with stakeholders occurs consistent with applicable
    rules and regulations)**. RS.CO-02 anchors the internal escalation path
    that must execute before any external notification — the supervisor-bound
    Art. 19(1) report is only as trustworthy as the internal chain that
    validated classification as `major`, escalated to executive leadership,
    and engaged legal counsel for regulatory-construction review. RS.CO-04
    governs the external notification layer itself, including the pre-approved
    supervisor contact route, the evidence-trail format aligned with the EBA/
    ESMA/EIOPA RTS templates (Implementing Regulation (EU) 2024/2956 Annex
    I–IV), and the parallel client-disclosure leg under Art. 19(3). Together
    these two subcategories convert reactive disclosure into a rehearsed
    communication run-book, and a documented RS.CO-02 + RS.CO-04 control set
    lets the entity demonstrate ex-post to competent authority review that
    the Art. 19(1)+(3) clocks were respected and the Art. 17 incident-
    management process fed the supervisory and client disclosure channels
    in the required sequence.
  ambiguity_notes: |
    S3 (Berry §5.7) on `major ICT-related incident` — the Art. 18(1) criteria are
    multiplicative and residually vague; the chosen reading is that any one criterion
    surpassing its materiality threshold (RTS-defined) triggers classification, with
    the supervisor adjudicating borderline cases. S3 POLY+COORD on the twin temporal
    trigger `without undue delay AS SOON AS they become aware` — the chosen reading
    is that `as soon as they become aware` is the moment the clock starts and
    `without undue delay` anchors the supervisory-side tempo. S3 POLY+SCOPE-Q on
    `becoming aware` — alternatives include actual knowledge, constructive knowledge,
    or either, with the dominant CJEU reading favouring constructive knowledge. S3
    on the Art. 18 implementing acts dependency, which remain pending and may close
    the threshold regress; the SR preserves the OJ-literal `major ICT-related
    incident` wording pending implementing acts. Remain open: pending EBA/ESMA/
    EIOPA technical standards under Art. 18(3), entities should adopt a written
    interpretive position on borderline cases and document it for supervisory
    review. Remain open: (a) whether `without undue delay AS SOON AS they become
    aware` admits an early-warning mini-notification (analogous to NIS 2 Art. 23(4)
    24-hour early warning) before the full Art. 19(4) intermediate report at 72 hours,
    pending EBA/ESMA/EIOPA technical-standards clarification; (b) the carve-out, if
    any, for payment-related incidents under Art. 23 (operational or security
    payment-related incidents) vis-à-vis the Art. 19(3) client-notification trigger,
    pending EBA Guidelines on operational or security payment-related incidents.
```

### SO-DORA-001 (CIA + A maintained across data states)

```yaml
- sr_id: SR-DORA-018
  title: "Standing crisis communication plans for major ICT incidents"
  source_clauses:
    - { clause_id: DORA-C29, article_ref: "Art. 14(1) — `crisis communication plans enabling a responsible disclosure of, at least, major ICT-related incidents or vulnerabilities to clients and counterparts as well as to the public, as appropriate`" }
  linked_objectives: [SO-DORA-009]
  sub_domain: [D-04.3]
  nist_csf_mapping:
    - { id: RS.CO-03, title: "Information is shared with designated internal and external stakeholders consistent with the established information-sharing rules" }
    - { id: RS.CO-04, title: "Coordination with stakeholders occurs consistent with applicable rules and regulations" }
  applies_to_role: [FINANCIAL_ENTITY]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 14(1) requires financial entities to maintain crisis communication plans
    enabling responsible disclosure of, at least, major ICT-related incidents or
    vulnerabilities to clients and counterparts and, where appropriate, to the
    public. The clause lives in the Chapter II Section 2 framework (per
    `02b_DORA_Ch2Sec2_Framework.md`) and is the standing-planning counterpart to
    the triggered reporting of Art. 19: Art. 14(1) plans must be in place before
    any incident, whereas Art. 19 reporting is the triggered workflow once
    classification occurs. The clause co-exists with NIS 2 Art. 23 supervisory
    cooperation (Directive (EU) 2022/2555) where the entity is in scope of both
    regimes, and with the CRA Art. 14 vulnerability-handling timeline
    (Regulation (EU) 2024/2847) where the underlying vulnerability originates in
    a digital product. EBA Guidelines on ICT and security risk management frame
    the standing planning requirement as risk-proportional, with recital context
    supporting risk-based `as appropriate` calibration for the public dimension.
  security_rationale: |
    The Art. 14(1) standing crisis-communication duty is operationalised in
    NIST CSF 2.0 through **RS.CO-03 (Information is shared with designated
    internal and external stakeholders consistent with the established
    information-sharing rules)** and **RS.CO-04 (Coordination with stakeholders
    occurs consistent with applicable rules and regulations)**. RS.CO-03
    anchors the pre-agreed stakeholder taxonomy (clients, counterparts, and —
    where appropriate — the public), the templated messaging set calibrated
    per audience, and the information-sharing rules that govern disclosure
    cadence and granularity. RS.CO-04 layers the rules-and-regulations
    consistency check, ensuring that crisis communications stay aligned with
    the supervisor-pre-notification under Art. 19(1), the client-disclosure
    under Art. 19(3), and any parallel obligations under NIS 2 Art. 23
    supervisory cooperation and CRA Art. 14 vulnerability-handling timelines.
    Together the two subcategories convert a reactive disclosure scramble
    into a rehearsed run-book, and an entity exercising these controls
    annually and integrating them with Art. 17 incident-management can
    demonstrate ex-post to supervisory review that the Art. 14(1) standing-
    planning obligation was met before any specific incident trigger fired.
  ambiguity_notes: |
    S3 POLY on `responsible disclosure` — alternatives include entity-judged
    responsibility, supervisory-prescribed disclosure norms, or industry-accepted
    responsible-disclosure practice; the chosen reading is the literal OJ
    formulation that places responsibility with the entity. S3 VAG on `at least`
    is read as a minimum floor that the entity may exceed in coverage. S3 POLY on
    `major` inherits the Art. 18 multiplicative-criteria regress, which remains
    pending the EBA/ESMA/EIOPA RTS under Art. 18(3) and partly addressed in
    Implementing Regulation (EU) 2024/2956. S3 POLY on `as appropriate` is read
    in light of recital-context risk-based judgement. S3 COORD on the cumulative
    recipient set `clients AND counterparts AS WELL AS to the public` — all three
    categories are in scope; `as appropriate` softens only the public disclosure
    dimension. Remain open: how `as appropriate` should be operationalised for
    the public leg, and at what signal threshold, remains for entity-documented
    policy pending implementing-acts clarity.
```

### SO-DORA-001 (CIA + A maintained across data states)

```yaml
- sr_id: SR-DORA-022
  title: "Unrestricted audit rights over critical ICT third-party providers"
  source_clauses:
    - { clause_id: DORA-C38, article_ref: "Art. 30(3)(e)(i)+(ii) — `unrestricted rights of access, inspection and audit by the financial entity, or an appointed third party, and by the competent authority … the right to take copies of relevant documentation on-site … the right to agree on alternative assurance levels if other clients' rights are affected`" }
  linked_objectives: [SO-DORA-012]
  sub_domain: [D-06.4]
  nist_csf_mapping:
    - { id: GV.SC-03, title: "Contracts with suppliers and other third parties are used to implement appropriate measures" }
    - { id: DE.CM-06, title: "External service provider activities and services are monitored to find potentially adverse events" }
  applies_to_role: [FINANCIAL_ENTITY, ICT_THIRD_PARTY]
  obligation_type: [CONTINUOUS, TRIGGERED]
  regulatory_rationale: |
    Art. 30(3)(e)(i) requires contractual arrangements to include unrestricted
    rights of access, inspection and audit by the financial entity (or an
    appointed third party) and by the competent authority, including the right
    to take copies of relevant documentation on-site, the effective exercise of
    which is not impeded or limited by other contractual arrangements or
    implementation policies. Art. 30(3)(e)(ii) permits the right to agree on
    alternative assurance levels where other clients' rights are affected. The
    clause operationalises the financial-entity verification axis of Art. 28
    and runs in parallel with — and does not substitute for — the supervisory
    audit powers under EBA Guidelines on outsourcing arrangements and with the
    CTPP Joint Committee oversight under Ch. V Sec. 2. EBA technical
    standards are expected to refine the form of alternative-assurance levels
    under Art. 30(7).
  security_rationale: |
    The Art. 30(3)(e)(i)+(ii) audit-rights duty is operationalised in NIST
    CSF 2.0 through **GV.SC-03 (Contracts with suppliers and other third
    parties are used to implement appropriate measures designed to meet the
    objectives of an organization's cybersecurity program)** and **DE.CM-06
    (External service provider activities and services are monitored to find
    potentially adverse events)**. GV.SC-03 anchors the contractual surface:
    the unrestricted-rights clause — access, inspection, audit, on-site copy
    taking — must be expressed in enforceable contract terms that pre-empt
    supplier-side carve-outs, sub-outsourcing dilution, or competing-client
    confidentiality claims, with the alternative-assurance-level exception
    of Art. 30(3)(e)(ii) narrowly bounded. DE.CM-06 layers the operational
    monitoring dimension, ensuring that the contract-level right translates
    into continuous surveillance of external service-provider activities so
    that adverse events at the supplier are detected and routed into the
    entity's incident-response process under Art. 17 before they cascade.
    Together these two subcategories convert a paper audit-right into a
    live detection-and-verification capability, and an entity evidencing
    GV.SC-03 contract design plus DE.CM-06 ongoing monitoring can
    demonstrate ex-post to the competent authority that the Art. 30(3)(e)
    unrestricted-rights obligation was both contractually anchored and
    operationally exercised — closing the gap between formal right and
    effective use that has historically caused post-incident forensics
    to stall at the supplier boundary.
  ambiguity_notes: |
    S3 SCOPE-Q (Berry §5.2.1) on `unrestricted` — the universal quantifier
    is qualified immediately by `if other clients' rights are affected`;
    the chosen reading is that `unrestricted` is the default rule with the
    `other clients' rights` exception permitting alternative-assurance levels
    on a case-by-case basis. S3 VAG on `relevant documentation` is read at
    the directly-material-evidence end of the spectrum, with the alternative
    of any plausible link reserved for residual cases. S3 VAG on `critical to
    the operations` is read at the literal entity-judgement default. S2 POLY
    on `access, inspection AND audit` — three distinct activities, the
    chosen reading is the literal AND. Remain open: the operational
    thresholds for `other clients' rights are affected` remain to be refined
    through EBA technical standards and through case-by-case bilateral
    negotiations until a market convention crystallises.
```

### SO-DORA-001 (CIA + A maintained across data states)

```yaml
- sr_id: SR-DORA-027
  title: "Sound and comprehensive ICT risk management framework documented"
  source_clauses:
    - { clause_id: DORA-C03, article_ref: "Art. 6(1) — `Financial entities shall have a sound, comprehensive and well-documented ICT risk management framework … which enables them to address ICT risk quickly, efficiently and comprehensively`" }
  linked_objectives: [SO-DORA-016]
  sub_domain: [D-09.1]
  nist_csf_mapping:
    - { id: GV.PO-01, title: "Organizational cybersecurity policy is established, communicated, and enforced" }
    - { id: GV.OC-01, title: "The organizational mission is understood and informs cybersecurity risk management" }
    - { id: GV.RM-04, title: "Strategic direction on identifying and responding to risks established and communicated" }
  applies_to_role: [FINANCIAL_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 6(1) requires financial entities to have a sound, comprehensive, and
    well-documented ICT risk management framework which enables them to address
    ICT risk quickly, efficiently, and comprehensively. Art. 6(2) further
    specifies that the framework shall include strategies, policies, protocols,
    procedures, and ICT risk tools. The clause sets the top-of-stack
    governance artefact and is operationalised by the strategy policies at Art. 7,
    the protection policies at Art. 9, and the incident-handling policies at
    Chapter III. The clause parallels — without replacing — the NIS 2 Art. 21
    basic cybersecurity governance baseline (Directive (EU) 2022/2555) and the
    AI Act Art. 9 risk-management duty for high-risk AI systems (Regulation
    (EU) 2024/1689) where AI components are in scope. EBA Guidelines on ICT
    and security risk management frame the supervisory expectations on
    framework quality attributes.
    [OJ-corrective note (v0.2 audit, cosmetic): Art. 6(2) — artefact order swap. OJ Art. 6(2) lists: `strategies, policies, procedures, ICT protocols and tools`. The SR swaps `procedures` and `protocols` (OJ puts `procedures` first), drops the `ICT` qualifier from `protocols`, and adds `ICT risk` to `tools`. All five items present; no operational change required.]
  security_rationale: |
    The Art. 6(1)+(2) framework obligation is operationalised in NIST CSF 2.0
    through **GV.PO-01 (Organizational cybersecurity policy is established,
    communicated, and enforced)**, **GV.OC-01 (The organizational mission is
    understood and informs cybersecurity risk management)**, and **GV.RM-04
    (Strategic direction on identifying and responding to risks established
    and communicated)**. GV.PO-01 anchors the policy-substrate dimension of
    the OJ `well-documented ICT risk management framework`, ensuring that
    the framework is enforceable rather than aspirational. GV.OC-01
    supplies the mission-alignment layer — the OJ `quickly, efficiently
    and comprehensively` adverb triplet maps onto mission-driven risk-
    management prioritisation, where cybersecurity investment is
    proportionate to the entity's critical objectives and services.
    GV.RM-04 layers the strategic-direction engine, ensuring that the
    OJ `sound and comprehensive` quality attributes are anchored in a
    documented strategic-direction artefact that links identification
    (Art. 7–8) and response (Art. 17–19) into a coherent risk-handling
    chain. Together these three subcategories convert the top-of-stack
    governance artefact into an enforceable policy with mission alignment
    and strategic direction, and an entity evidencing GV.PO-01 + GV.OC-01
    + GV.RM-04 coverage can demonstrate ex-post to supervisory review
    that the Art. 6(1) `sound, comprehensive and well-documented`
    framework was anchored in enforceable policy rather than documented
    aspiration.
  ambiguity_notes: |
    S2 COORD on the three-way AND of adjectives (`sound, comprehensive AND
    well-documented`) — all three required. S2 COORD on the three-way AND of
    adverbs (`quickly, efficiently AND comprehensively`) — all three required.
    S2 POLY on `framework` is read as composite artefact per the Art. 6(2)
    elaboration; alternatives include treating it as a single document, but
    the Art. 6(2) elaboration settles the composite reading. Remain open:
    documentation-control granularity for `well-documented` (versioning,
    approval-trails, archival) is an entity-policy matter.
```

### SO-DORA-001 (CIA + A maintained across data states)

```yaml
- sr_id: SR-DORA-029
  title: "Inventory and classification of ICT-supported business assets"
  source_clauses:
    - { clause_id: DORA-C05, article_ref: "Art. 7(1) — `identify, classify and adequately document all ICT supported business functions, roles and responsibilities, the information assets and ICT assets supporting those functions, and their roles and dependencies in relation to ICT risk`" }
  linked_objectives: [SO-DORA-017]
  sub_domain: [D-09.3]
  nist_csf_mapping:
    - { id: ID.AM-01, title: "Inventories of hardware managed by the organization are maintained" }
    - { id: ID.AM-02, title: "Inventories of software, services, and systems managed by the organization are maintained" }
    - { id: ID.AM-03, title: "Inventories of data and corresponding metadata for designated data types are maintained" }
    - { id: ID.AM-05, title: "Assets are prioritized based on classification, criticality, resources, and impact on the mission" }
  applies_to_role: [FINANCIAL_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 7(1) requires financial entities to identify, classify, and adequately
    document all ICT-supported business functions, the roles and responsibilities
    supporting those functions, the information assets and ICT assets supporting
    those functions, and their roles and dependencies in relation to ICT risk.
    The clause is the inventory-onboarding substrate for every downstream
    obligation (vulnerability management, access control, incident response,
    third-party risk management). The clause runs in parallel with GDPR Art. 30
    records-of-processing activities (Regulation (EU) 2016/679) — the data-asset
    inventory serves both regimes, and with NIS 2 Art. 21(2)(a) basic cybersecurity
    hygiene inventory duty (Directive (EU) 2022/2555). CRA Art. 13 conformity-
    assessment duties (Regulation (EU) 2024/2847) apply where ICT assets are
    digital products. EBA Guidelines on ICT and security risk management set
    the supervisory baseline for asset-classification granularity.
    [OJ-corrective note (v0.2 audit, material): Art. 7(1) → Art. 8(1) misattribution (P0 disagreement cross-cutting). Art. 8(1) (Identification function): financial entities shall identify all ICT-supported business functions and the ICT assets that support those functions, including those of third-party providers, and document them. The audit notes that the source article_ref points to Art. 7(1) but the OJ text is in Art. 8(1).]
  security_rationale: |
    The Art. 7(1) asset-identification duty is operationalised in NIST CSF
    2.0 through **ID.AM-01 (Inventories of hardware managed by the
    organization are maintained)**, **ID.AM-02 (Inventories of software,
    services, and systems managed by the organization are maintained)**,
    **ID.AM-03 (Inventories of data and corresponding metadata for
    designated data types are maintained)**, and **ID.AM-05 (Assets are
    prioritized based on classification, criticality, resources, and
    impact on the mission)**. The three inventory subcategories
    decompose the OJ `information assets and ICT assets` substrate into
    hardware, software/services/systems, and data layers, each with
    its own lifecycle, change-detection cadence, and ownership chain.
    ID.AM-05 closes the prioritisation loop — the OJ `classify` verb is
    operationalised through classification, criticality, resource
    weight, and mission-impact scoring, ensuring that the inventory
    is not a flat list but a priority-ordered substrate for
    downstream controls. Together these four subcategories convert a
    documentary exercise into the upstream input for vulnerability
    management (Art. 9(4)(f)), access control (Art. 9(4)(c)), incident
    response (Art. 17), and third-party risk management (Art. 28), and
    an entity evidencing ID.AM-01/02/03 coverage plus ID.AM-05
    prioritisation can demonstrate ex-post to supervisory review
    that the Art. 7(1) `identify, classify and adequately document`
    obligation was met at the hardware-software-data substrate level
    and that criticality scoring was anchored in mission-impact
    rather than vendor tier.
  ambiguity_notes: |
    S3 COORD on the long AND chain `ICT supported business functions, roles
    and responsibilities, the information assets and ICT assets supporting
    those functions, AND their roles and dependencies` — the chosen reading
    is that all four asset-classes plus dependencies are in scope per the
    inventory intent. The clause admits multiple parse trees; the
    functional-reading selection treats `roles and dependencies in relation
    to ICT risk` as a connective qualifier rather than a separate asset-class.
    S2 VAG on `adequately document` — alternatives include sufficiently-for-
    audit or sufficiently-for-risk-management; the chosen reading is the
    cumulative. S2 POLY on `ICT supported` — alternatives include fully-
    automated, partially-automated, or any-function-with-ICT-dependency; the
    chosen reading is the literal latter. Remain open: change-detection
    cadence for asset-inventory refresh remains for entity policy, with EBA
    supervisory practice providing convergence signals.
```

### SO-DORA-001 (CIA + A maintained across data states)

```yaml
- sr_id: SR-DORA-030
  title: "Continuous monitoring and control of ICT-system security and functioning"
  source_clauses:
    - { clause_id: DORA-C07, article_ref: "Art. 8(1) — `continuously monitor and control the security and functioning of ICT systems and tools and shall minimise the impact of ICT risk on ICT systems through the deployment of appropriate ICT security tools, policies and procedures`" }
  linked_objectives: [SO-DORA-018]
  sub_domain: [D-10.1]
  nist_csf_mapping:
    - { id: DE.CM-01, title: "Networks and network services are monitored to find potentially adverse events" }
    - { id: DE.CM-09, title: "Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events" }
    - { id: PR.PS-04, title: "Log records are generated and made available for continuous monitoring and analysis" }
  applies_to_role: [FINANCIAL_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 8(1) requires financial entities to continuously monitor and control
    the security and functioning of ICT systems and tools and to minimise the
    impact of ICT risk on ICT systems through the deployment of appropriate ICT
    security tools, policies, and procedures. The clause is the real-time
    security-operations substrate of DORA and pairs with the Art. 17 incident-
    management process (which is triggered downstream of monitoring outputs)
    and with the Chapter IV testing regime (which validates monitoring
    effectiveness). The clause co-exists with NIS 2 Art. 21(2)(b) basic
    cybersecurity monitoring baseline (Directive (EU) 2022/2555) and with AI
    Act Art. 9(2) post-market-monitoring duties for high-risk AI systems
    (Regulation (EU) 2024/1689) where AI components are in scope. EBA Guidelines
    on ICT and security risk management set the supervisory baseline for
    monitoring coverage and cadence.
    [OJ-corrective note (v0.2 audit, material): Art. 8(1) → Art. 9(1) misattribution (P0 disagreement cross-cutting). Art. 9(1) (Protection and prevention): financial entities shall continuously monitor and control the security and functioning of ICT systems. The audit notes that the source article_ref points to Art. 8(1) but the OJ text is in Art. 9(1) — the `monitor` obligation actually lives under Art. 9, not Art. 8 (which is the chapeau for Identification, not monitoring).]
  security_rationale: |
    The Art. 8(1) monitoring-and-control duty is operationalised in NIST CSF
    2.0 through **DE.CM-01 (Networks and network services are monitored to
    find potentially adverse events)**, **DE.CM-09 (Computing hardware and
    software, runtime environments, and their data are monitored to find
    potentially adverse events)**, and **PR.PS-04 (Log records are generated
    and made available for continuous monitoring and analysis)**. DE.CM-01
    anchors the network-layer monitoring — east-west traffic, perimeter
    events, north-south anomalies — that operationalises the OJ
    `continuously monitor` qualifier at the network surface. DE.CM-09
    extends coverage to the compute layer (endpoints, servers, runtime
    environments, file integrity) so that the OJ `security AND functioning`
    AND-coordination is met across both cyber-threat and operational-
    performance dimensions. PR.PS-04 closes the evidentiary loop, ensuring
    that the monitoring output is anchored in log records that are
    available for continuous analysis and incident-response consumption
    under Art. 17. Together these three subcategories operationalise the
    OJ `tools, policies AND procedures` triplet through detection-engine
    coverage plus platform-level logging discipline, and an entity
    evidencing DE.CM-01 + DE.CM-09 + PR.PS-04 coverage can demonstrate
    ex-post to supervisory review that the Art. 8(1) `continuously
    monitor and control` obligation was met at network, compute, and
    log-evidence layers, and that the `minimise the impact of ICT risk`
    objective was anchored in real-time detection rather than periodic
    sampling.
  ambiguity_notes: |
    S2 VAG on `continuously` — the chosen reading is the practical EU-
    supervisory reading of always-on or near-real-time at sufficiently fine
    cadence; alternatives include a more relaxed scheduled cadence. S2 POLY
    on `control` — alternatives include preventive, detective, or corrective;
    the chosen reading is the literal AND across all three. S2 COORD on
    `security AND functioning` — distinct aspects of ICT-system monitoring, the
    chosen reading is the literal AND. S2 COORD on `tools, policies AND
    procedures` — all three artefact types required. Remain open:
    cadence expectations on `continuously` are subject to EBA supervisory
    practice; documented and evidence-backed cadences are recommended.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

