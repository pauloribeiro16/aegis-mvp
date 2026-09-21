---
document_id: AEGIS-PREPROC-DORA-ART-18
title: DORA Art. 18 — SecurityObjectives & SecurityRules
regulation: DORA
article: Art. 18
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
status: DRAFT
---

# DORA Art. 18

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

_No standalone SO row cites this article directly (covered via the rules below)._

## Security Rules (from 02_SecurityRules_NIST.md)

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

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

