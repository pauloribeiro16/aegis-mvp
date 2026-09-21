---
document_id: AEGIS-PREPROC-DORA-ART-3
title: DORA Art. 3 — SecurityObjectives & SecurityRules
regulation: DORA
article: Art. 3
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
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
status: DRAFT
---

# DORA Art. 3

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
- sr_id: SR-DORA-026
  title: "Management body owns full lifecycle of ICT risk management framework"
  source_clauses:
    - { clause_id: DORA-C01, article_ref: "Art. 5(2) — `the management body of the financial entity shall define, approve, oversee and be responsible for the implementation of all arrangements related to the ICT risk management framework`" }
  linked_objectives: [SO-DORA-016]
  sub_domain: [D-09.1]
  nist_csf_mapping:
    - { id: GV.RR-01, title: "Organizational leadership is responsible and accountable for cybersecurity risk and promotes a risk-aware ethical culture" }
    - { id: GV.RR-02, title: "Roles, responsibilities, authorities, and accountabilities related to cybersecurity risk management are established, communicated, understood, and enforced" }
  applies_to_role: [FINANCIAL_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 5(2) requires the management body of the financial entity to define,
    approve, oversee, and be responsible for the implementation of all
    arrangements related to the ICT risk management framework. The clause is
    the top-of-the-pyramid governance rule of DORA and establishes personal
    liability for the management body, which co-exists with the EBA Guidelines
    on Internal Governance fit-and-proper expectations and with the cross-
    reference to MiFID II Art. 4(1)(36), CRD Art. 3(1)(7), UCITS, CSDR, and
    BMR `management body` definitions (per `02a_DORA_Ch2Sec1_Governance.md`
    §6.x). For smaller entities under Art. 4 proportionality, the management-
    body definition follows national corporate-law default.
  security_rationale: |
    The Art. 5(2) management-body ownership duty is operationalised in NIST
    CSF 2.0 through **GV.RR-01 (Organizational leadership is responsible and
    accountable for cybersecurity risk and promotes a risk-aware ethical
    culture)** and **GV.RR-02 (Roles, responsibilities, authorities, and
    accountabilities related to cybersecurity risk management are established,
    communicated, understood, and enforced)**. GV.RR-01 anchors the
    accountability substrate — the four-verb OJ coordination `define, approve,
    oversee, be responsible` is operationalised as a personal-liability
    threshold at the management-body level, complementing the EBA Guidelines
    on Internal Governance fit-and-proper regime. GV.RR-02 layers the
    role-allocation engine that translates the top-level ownership into
    delegated authority and operational accountability, ensuring that the
    `all arrangements related to the ICT risk management framework` OJ
    qualifier is distributed across the entity's three-lines-of-defence
    structure (or alternative model) without diluting the top-of-pyramid
    ownership. Together these two subcategories close the gap between
    board-level sign-off and operational accountability, and an entity
    evidencing GV.RR-01 leadership accountability plus GV.RR-02 role-
    allocation discipline can demonstrate ex-post to supervisory review
    that the Art. 5(2) four-verb obligation was discharged through both
    personal liability and documented delegation, rather than collapsing
    into ceremonial approval without follow-through.
  ambiguity_notes: |
    S2 SCOPE-Q on `all arrangements` is read at the literal in-scope end of
    the spectrum — all arrangements within the framework. S2 POLY on
    `management body` is read at the board-of-directors end of the spectrum
    per EU corporate-law default. S2 COORD on the four-verb coordination
    `define, approve, oversee AND be responsible` (Berry §5.5) — the chosen
    reading is that each of the four activities is distinct and must be
    performed. Remain open: how `all arrangements` interacts with new-
    arrangement onboarding remains an entity-policy matter.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

