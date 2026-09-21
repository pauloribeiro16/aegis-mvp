---
document_id: AEGIS-PREPROC-DORA-ART-11
title: DORA Art. 11 — SecurityObjectives & SecurityRules
regulation: DORA
article: Art. 11
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.2.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.2.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.4.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.4.md
status: DRAFT
---

# DORA Art. 11

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-DORA-010 | A comprehensive ICT business continuity policy is operationalised through dedicated, appropriate and documented arrangements, plans, procedures and mechanisms, including ICT response and recovery plans (subject to independent internal audit for non-microenterprises), backup policies and procedures (specifying scope of data subject to backup and minimum frequency of backup, based on criticality or confidentiality), and restoration and recovery procedures and methods. | `DORA-C22` (Art. 11(1) BC policy + integral part of overall BC policy); `DORA-C23` (Art. 11(2) `dedicated, appropriate and documented` + 4-way AND of artefacts); `DORA-C24` (Art. 11(3) response + recovery plans AND + independent internal audit for non-microenterprises); `DORA-C25` (Art. 12(1) backup policies + restoration/recovery procedures + criticality OR confidentiality basis) | D-04.2, D-04.4, D-09.4 |
| SO-DORA-010 | D-04.2, D-04.4, D-09.4 | Art. 11(1)–(3) + Art. 12(1) | BC policy + response/recovery plans + backup + restoration |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-DORA-001 (CIA + A maintained across data states)

```yaml
- sr_id: SR-DORA-013
  title: "Integrated ICT business continuity policy framework"
  source_clauses:
    - { clause_id: DORA-C22, article_ref: "Art. 11(1) — `comprehensive ICT business continuity policy, which may be adopted as a dedicated specific policy, forming an integral part of the overall business continuity policy of the financial entity`" }
  linked_objectives: [SO-DORA-010]
  sub_domain: [D-04.2, D-04.4]
  nist_csf_mapping:
    - { id: RC.RP-01, title: "The recovery portion of the incident response plan is executed once the incident response plan has been performed to acceptable criteria" }
    - { id: PR.IR-03, title: "Mechanisms are put in place to achieve resilience requirements in normal and adverse situations" }
  applies_to_role: [FINANCIAL_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 11(1) requires financial entities to put in place a
    comprehensive ICT business continuity policy, which may be
    adopted as a dedicated specific policy forming an integral part
    of the overall business continuity policy of the financial
    entity. The provision sits in Chapter II Section II alongside
    Art. 12 backup and recovery obligations (NIS 2 Art. 21(2)(c)
    on business-continuity imposes a parallel obligation on NSIEs
    outside DORA, with CRA Art. 13(8) on secure-by-default and
    secure-update flows feeding the upstream incident-prevention
    side). The OJ `may be adopted as a dedicated specific policy`
    qualifier explicitly recognises either form-factor (standalone
    document or embedded within overall BC policy).
  security_rationale: |
    The obligation in Art. 11(1) for a comprehensive ICT business
    continuity policy is operationalised in NIST CSF 2.0 through
    **RC.RP-01 (The recovery portion of the incident response plan
    is executed once the incident response plan has been performed
    to acceptable criteria)** and **PR.IR-03 (Mechanisms are put in
    place to achieve resilience requirements in normal and adverse
    situations)**. RC.RP-01 anchors the recovery-execution dimension:
    the BC policy must specify the criteria under which recovery
    transitions from incident-response to recovery-mode, ensuring
    continuity of critical functions with documented decision
    points and recovery-time-objectives. PR.IR-03 supplies the
    broader resilience-mechanism substrate that the BC policy
    operationalises — redundant systems, geographic dispersion,
    failover orchestration, alternative-site arrangements, and
    crisis-mode operations. The OJ `integral part` qualifier (BC
    policy embedded within overall BC) is delivered through
    PR.IR-03's cross-policy consistency requirements and RC.RP-01's
    coordination-with-overall-BC framing, preventing trigger-
    divergence between ICT-BC and overall-BC activation. The
    accountability link under Art. 5(2): the BC policy document,
    recovery-execution criteria, and resilience-mechanism inventory
    produce the documented evidence trail the management body can
    present to competent authorities demonstrating that ICT
    continuity is structurally embedded in the entity's overall
    business-continuity framework rather than a free-standing
    document with unaligned triggers.
  ambiguity_notes: |
    `comprehensive` (VAG S2) — R1 broad scope / R2 detailed
    coverage / R3 both; R3 literal. `may be adopted as a dedicated
    specific policy` (POLY S2) — R1 standalone document / R2
    embedded within overall BC policy / R3 either; R3 literal
    (the OJ explicitly permits either form). `integral part`
    (VAG S2) — R1 structurally embedded / R2 logically linked; R1
    literal. A contrasting reading of `integral part` would allow
    logical linking without structural embedding, but the
    supervisory expectation (EBA Guidelines on ICT and security
    risk management §210) requires structural integration to
    ensure trigger-coordination. The literal OJ construction
    makes `integral part` structurally protective. An open
    question is whether Art. 11(1) `integral part` extends to the
    third-party risk dimension under Art. 28–30 (i.e. whether
    the BC policy must cover CTPP-failure scenarios) or is
    restricted to in-entity ICT.
```

### SO-DORA-001 (CIA + A maintained across data states)

```yaml
- sr_id: SR-DORA-014
  title: "BC implementation arrangements with independent audit review"
  source_clauses:
    - { clause_id: DORA-C23, article_ref: "Art. 11(2) — `implement the ICT business continuity policy through dedicated, appropriate and documented arrangements, plans, procedures and mechanisms aiming to (a)–(e)`" }
    - { clause_id: DORA-C24, article_ref: "Art. 11(3) — `associated ICT response and recovery plans … shall be subject to independent internal audit reviews` (non-microenterprises)" }
  linked_objectives: [SO-DORA-010]
  sub_domain: [D-04.2, D-04.4]
  nist_csf_mapping:
    - { id: RC.RP-04, title: "Critical mission functions and services are restored through the implementation of the recovery plan" }
    - { id: PR.IR-04, title: "Adequate resource capacity to ensure availability is maintained" }
  applies_to_role: [FINANCIAL_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 11(2) requires financial entities to implement the ICT
    business continuity policy through dedicated, appropriate and
    documented arrangements, plans, procedures and mechanisms
    aiming to (a) continue critical operations, (b) recover from
    ICT-related incidents, (c) manage crises, (d) protect
    stakeholders, and (e) comply with regulatory obligations. Art.
    11(3) requires ICT response and recovery plans to be subject
    to independent internal audit reviews for non-microenterprises.
    The five-objective list (a)–(e) is functionally distinct from
    the three Cs of generic BC (continuity, recovery, crisis) —
    the addition of stakeholder protection and regulatory
    compliance reflects the cross-stakeholder dimension of
    ICT-related disruption in financial entities (NIS 2 Art.
    21(2)(c) on continuity parallels the first three objectives;
    GDPR Art. 32 security-of-processing converges on stakeholder-
    protection (d) for personal-data cases).
    [OJ-corrective note (v0.2 audit, material): Art. 11(2)(c)/(d)/(e) — BCP objectives mislabelled. OJ Art. 11(2) chapeau + (a)–(e) actually reads: (a) ensure the continuity of the financial entity's critical or important functions; (b) quickly, appropriately and effectively respond to, and resolve, all ICT-related incidents in a way that limits damage and prioritises the resumption of activities and recovery actions; (c) activate, without delay, dedicated plans that enable containment measures, processes and technologies suited to each type of ICT-related incident; (d) estimate preliminary impacts, damages and losses; (e) set out communication and crisis management actions that ensure that updated information is transmitted to all relevant internal staff and external stakeholders in accordance with Article 14, and report to the competent authorities in accordance with Article 19. The SR's labels for (c)/(d)/(e) (manage crises, protect stakeholders, comply with regulatory obligations) do NOT match the OJ items.]
  security_rationale: |
    The obligation in Art. 11(2)+(3) for BC-implementation
    arrangements and independent internal audit review is
    operationalised in NIST CSF 2.0 through **RC.RP-04 (Critical
    mission functions and services are restored through the
    implementation of the recovery plan)** and **PR.IR-04 (Adequate
    resource capacity to ensure availability is maintained)**.
    RC.RP-04 anchors the recovery-execution layer: the documented
    arrangements, plans, procedures, and mechanisms (the four-
    artefact AND) operationalise the five-objective Art. 11(2)(a)–(e)
    list into concrete recovery capability — continuity of critical
    functions, rapid response-and-resolution, plan activation for
    containment, impact-and-loss estimation, and crisis-communication
    plus CA reporting. PR.IR-04 supplies the resource-capacity
    substrate — redundant compute, storage, network, and
    alternative-site capacity — without which recovery plans are
    paper artefacts. The OJ Art. 11(3) audit-review obligation
    (non-microenterprises) maps onto RC.RP-04's recovery-execution
    verification dimension, ensuring the arrangements are subject
    to second-line assurance rather than self-attestation. The
    accountability link under Art. 5(2): the recovery-plan
    inventory, resource-capacity attestation, audit-review records,
    and findings-to-improvement-cycle documentation produce the
    documented evidence trail the management body can present to
    competent authorities demonstrating that BC arrangements are
    operationally substantive, audit-verified, and continuously
    resourced rather than nominal.
  ambiguity_notes: |
    Source clause DORA-C23 carries S2 on the 3-way AND of
    adjectives (`dedicated, appropriate, documented`) and the
    4-way AND of artefact types (`arrangements, plans,
    procedures, mechanisms`); reading chosen: R1 cumulative
    (all four artefacts + all three qualities required). DORA-C24
    `response AND recovery plans` (COORD S2) — R1 distinct plans
    / R2 composite plan; R1 literal (the OJ enjoins two plan
    types). `associated` (VAG S2 — Art. 11(3) refers back to
    Art. 11(1) BC policy). `independent internal audit reviews`
    (POLY S2) — R1 third-line assurance / R2 second-line review
    with independence / R3 any internal audit with independence;
    R3 literal. The microenterprise carve-out is preserved in
    `applies_to_role` per the OJ scope. A contrasting reading of
    `response AND recovery plans` would treat them as a single
    composite plan, but the OJ enumeration with `AND` and the
    operational difference between response (triage, containment)
    and recovery (service restoration) justifies the distinct
    reading. An open question is whether `independent internal
    audit` permits internal-audit-function co-sourcing under
    external-lead assurance terms, or restricts to in-house
    audit function with documented independence.
```

### SO-DORA-001 (CIA + A maintained across data states)

```yaml
- sr_id: SR-DORA-015
  title: "Risk-calibrated backup with verified restoration capability"
  source_clauses:
    - { clause_id: DORA-C25, article_ref: "Art. 12(1) — `develop and document: (a) backup policies and procedures specifying the scope of the data that is subject to the backup and the minimum frequency of the backup, based on the criticality of information or the confidentiality level of the data; (b) restoration and recovery procedures and methods`" }
  linked_objectives: [SO-DORA-010]
  sub_domain: [D-04.4]
  nist_csf_mapping:
    - { id: PR.DS-11, title: "Backups of data are created, protected, maintained, and tested" }
    - { id: RC.RP-03, title: "The integrity of backups and other restoration assets is verified before using them for restoration" }
    - { id: RC.RP-04, title: "Critical mission functions and services are restored through the implementation of the recovery plan" }
  applies_to_role: [FINANCIAL_ENTITY]
  obligation_type: [CONTINUOUS, TRIGGERED]
  regulatory_rationale: |
    Art. 12(1)(a) requires financial entities to develop and
    document backup policies and procedures specifying the scope of
    the data subject to backup and the minimum frequency of backup,
    based on the criticality of information or the confidentiality
    level of the data. Art. 12(1)(b) requires restoration and
    recovery procedures and methods. Article 12 Chapter II Section
    II operationalises Art. 11 BC policy with specific backup and
    recovery obligations (NIS 2 Art. 21(2)(c) on continuity and
    Art. 21(2)(d) on cryptography supply parallel and overlapping
    obligations; CRA Art. 13(8) on secure-update is upstream).
    Recital 57 highlights the importance of restore-time
    confidence (testing backups, not merely writing them) which
    EBA Guidelines on ICT and security risk management §215
    operationalise through documented restore-test cadence.
  security_rationale: |
    The obligation in Art. 12(1) for backup policies and
    restoration/recovery procedures is operationalised in NIST CSF
    2.0 through **PR.DS-11 (Backups of data are created, protected,
    maintained, and tested)**, **RC.RP-03 (The integrity of backups
    and other restoration assets is verified before using them for
    restoration)**, and **RC.RP-04 (Critical mission functions and
    services are restored through the implementation of the recovery
    plan)**. PR.DS-11 establishes the backup-creation and protection
    layer — encryption-at-rest of backup media, immutable storage
    for ransomware-resistant retention, offsite replication with
    documented RPO alignment, and retention windows scaled to
    data criticality. RC.RP-03 closes the restore-confidence
    dimension by requiring integrity verification before
    restoration (Recital 57's testing-not-merely-writing principle),
    ensuring backups are operationally usable through documented
    restore-test cadence and cryptographic integrity checks. RC.RP-04
    anchors the service-restoration layer: the recovery plan
    operationalises restored data into running services with
    documented recovery-time-objectives. The OJ `based on
    criticality of information OR confidentiality level` risk-
    based proportionality is operationalised through tiered
    backup cadences — Tier 1 critical trading books synchronously
    replicated, Tier 2 settlement data at high cadence, Tier 3
    reporting data at standard cadence. The accountability link
    under Art. 5(2): the backup-tier classification, restore-test
    records, and recovery-execution documentation produce the
    documented evidence trail the management body can present to
    competent authorities demonstrating that backup-and-recovery
    is risk-calibrated, restore-verified, and service-validated
    rather than write-only.
  ambiguity_notes: |
    `minimum frequency` (VAG S2) — R1 fixed interval / R2 risk-
    based interval / R3 event-driven; R2 dominant per the OJ
    qualifier `based on the criticality of information or the
    confidentiality level`. `criticality of information OR
    confidentiality level of the data` (COORD S2) — R1 either
    dimension suffices / R2 both required; R1 literal OR.
    `restoration AND recovery` (POLY S2) — R1 distinct activities
    (restore-from-backup vs. recover-service) / R2 composite
    (one end-to-end activity); reading chosen: R1 distinct (the
    two activities are coordinated but operationally separate;
    restoration is the technical layer, recovery is the service
    layer). A contrasting reading of `restoration AND recovery`
    treats them as a single end-to-end activity, but the OJ
    enumeration with explicit `and` and the operational
    difference between technical restore (data delivery) and
    service recovery (operational state) justifies the distinct
    reading. An open question is whether the regulatory
    expectation extends to cryptographic-key backup separately,
    given that some recovery scenarios rely on key-material
    redundancy.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

