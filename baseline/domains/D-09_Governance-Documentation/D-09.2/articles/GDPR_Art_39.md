---
document_id: AEGIS-PREPROC-GDPR-ART-39
title: GDPR Art. 39 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 39
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-08_Human-Factors/D-08.1.md
  - ../../CrossRegulation/DeepAnalysis/D-08_Human-Factors/D-08.1.md
  - ../../CrossRegulation/DomainAnalysis/D-08_Human-Factors/D-08.2.md
  - ../../CrossRegulation/DeepAnalysis/D-08_Human-Factors/D-08.2.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.2.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.2.md
status: DRAFT
---

# GDPR Art. 39

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-GDPR-025 | Personnel authorised to process personal data are informed and trained on GDPR obligations and on the controller's or processor's data-protection policies applicable to their role. | `GDPR-CP28` (Art. 39(1)(b) — DPO tasks on awareness/training); `GDPR-CP28` (Art. 39(1)(a)); `GDPR-CP12` (Art. 30 — awareness of staff); `GDPR-TR06` (Art. 47(2)(n) — BCR training) | D-08.1, D-08.2 |
| SO-GDPR-025 (cross-ref) | The data-protection officer monitors the assignment of responsibilities, awareness-raising and training of staff involved in processing operations. | `GDPR-CP28` (Art. 39(1)(b)) | D-08.2 |
| SO-GDPR-025 | D-08.1, D-08.2 | Art. 39(1)(a)/(b), Art. 30(4), Art. 47(2)(n) | Staff informed and trained on data-protection obligations |
| SO-GDPR-037 | A data protection officer is designated where any of the three Art. 37(1) triggers apply (public authority; core activities of regular/systematic monitoring on large scale; core activities of large-scale special-category or criminal-conviction processing); the DPO performs the Art. 39(1) tasks with adequate independence, resources, and expert knowledge. | `GDPR-CP25` (Art. 37(1)(a)/(b)/(c)); `GDPR-CP26` (Art. 38); `GDPR-CP28` (Art. 39); `GDPR-CP27` (Art. 38(6) — conflict of interests) | D-09.1, D-09.2 |
| SO-GDPR-037 | D-09.1, D-09.2 | Art. 37, Art. 38, Art. 39 | DPO designation and tasks |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-042
  title: "DPO-driven GDPR awareness and role-specific training"
  source_clauses:
    - { clause_id: GDPR-CP28, article_ref: "Art. 39(1)(b) — awareness and training" }
    - { clause_id: GDPR-CP28, article_ref: "Art. 39(1)(a) — inform and advise" }
  linked_objectives: [SO-GDPR-025]
  sub_domain: [D-08.1, D-08.2]
  nist_csf_mapping:
    - { id: PR.AT-01, title: "All users are informed and trained on cybersecurity topics" }
    - { id: PR.AT-02, title: "All members of the organization's workforce understand their roles and responsibilities in achieving the organization's cybersecurity objectives" }
  applies_to_role: [DPO, CONTROLLER, PROCESSOR]
  obligation_type: [CONTINUOUS, PERIODIC]
  regulatory_rationale: |
    Art. 39(1)(b) requires the DPO to monitor compliance with GDPR,
    including the assignment of responsibilities, awareness-raising, and
    training of staff involved in processing operations. Art. 39(1)(a)
    requires the DPO to inform and advise the controller or processor
    and the employees who carry out processing of their obligations
    pursuant to GDPR and to other Union or Member State data protection
    provisions. The two sub-paragraphs together establish the DPO's
    role as the internal awareness and training catalyst, distinct
    from the controller's substantive training obligation.
  security_rationale: |
    The obligation in Art. 39(1)(a) and Art. 39(1)(b), on the DPO acting as the internal advisor and awareness-and-training catalyst for staff involved in processing, is operationalised in NIST CSF 2.0 through **PR.AT-01 (All users are informed and trained on cybersecurity topics, e.g. recognition of phishing, social engineering, and other relevant risks)** and **PR.AT-02 (All members of the organization's workforce understand their roles and responsibilities in achieving the organization's cybersecurity objectives)**.
    PR.AT-01 captures the broad-coverage discipline: the DPO's awareness-raising obligation is structurally a general-population training duty covering all personnel involved in processing, on a recurring cadence and with content that updates to reflect emerging threats and the changing data flows of the organisation.
    PR.AT-02 captures the role-specific layer that PR.AT-01 cannot cover: personnel with data-subject-facing, access-management, breach-response or DPO-deputy responsibilities need role-specific reinforcement of their GDPR and cybersecurity obligations, distinct from the general awareness programme.
    A controller or processor that documents PR.AT-01 general-population awareness cadence and PR.AT-02 role-specific training records can demonstrate ex post, against the Art. 5(2) accountability duty read with the Art. 39(1) DPO mandate, that the DPO's awareness-and-training function was operationally exercised and recorded on the day of any supervisory inspection.
  ambiguity_notes: |
    `awareness-raising` and `training` carry Berry-flagged POLY+VAG-S2
    (Berry §5.1): both terms have a recurrent GDPR polysemy. The
    reading adopted for this SR splits the obligation into two: (1)
    general awareness training on GDPR for all personnel involved in
    processing, on an annual basis; and (2) role-specific training for
    personnel with data-subject-facing or access-management
    responsibilities, on a quarterly or event-triggered basis. An
    alternative reading under which one-off induction training
    suffices would conflict with the `awareness-raising` qualifier,
    which implies ongoing reinforcement. Remain open: whether `staff
    involved in processing` includes board members and senior
    management in the awareness scope, or only operational personnel.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-063
  title: "Independent and adequately resourced data protection officer"
  source_clauses:
    - { clause_id: GDPR-CP26, article_ref: "Art. 38 — DPO position" }
    - { clause_id: GDPR-CP27, article_ref: "Art. 38(6) — conflict of interests" }
  linked_objectives: [SO-GDPR-037]
  sub_domain: [D-09.1]
  nist_csf_mapping:
    - { id: GV.RR-01, title: "Organizational leadership responsible and accountable for cybersecurity risk" }
    - { id: GV.RR-03, title: "Adequate resources allocated commensurate with risk strategy" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 38 requires the controller and the processor to ensure that the data protection officer is involved properly and in a timely manner in all issues which relate to the protection of personal data (Art. 38(1)), is supported in performing the tasks referred to in Art. 39 by providing the resources necessary to carry out those tasks as well as access to personal data and processing operations and to maintain the DPO's expert knowledge (Art. 38(2)), receives no instructions regarding the exercise of those tasks and reports directly to the highest management level (Art. 38(3)), and is not dismissed or penalised by the controller or processor for performing the tasks (Art. 38(4)). Art. 38(6) provides that the DPO may fulfil other tasks and duties, but the controller or processor shall ensure that any such tasks and duties do not result in a conflict of interests.
  security_rationale: |
    The obligation in Art. 38(1)–(6) is operationalised in NIST CSF 2.0 through
    **GV.RR-01 (Organizational leadership responsible and accountable for
    cybersecurity risk and promoting a risk-aware ethical culture)** and
    **GV.RR-03 (Adequate resources allocated commensurate with the cybersecurity
    risk strategy, roles, responsibilities, authorities, and accountabilities)**.

    GV.RR-01 controls the leadership accountability and direct-reporting line
    that Art. 38(3) requires: the DPO must receive no instructions regarding the
    exercise of Art. 39 tasks and must report directly to the highest management
    level, so that leadership remains accountable for the assurance function. The
    same subcategory captures the protection against dismissal or penalty under
    Art. 38(4) and the conflict-of-interests prohibition under Art. 38(6), both
    of which are leadership-culture obligations. GV.RR-03 controls the resourcing
    that Art. 38(2) requires: the controller must provide the DPO with the
    resources, access to personal data and processing operations, and expert-
    knowledge maintenance necessary to carry out the Art. 39 tasks.

    Together the two subcategories embed DPO independence and resourcing in
    leadership accountability (GV.RR-01) backed by adequate resource allocation
    (GV.RR-03), enabling ex-post demonstration to the supervisory authority —
    through the documented budget, training plan and reporting line — that the
    DPO could perform the Art. 39 tasks without operational-management
    interference.
  ambiguity_notes: |
    Properly and in a timely manner, resources necessary, and conflict of interests carry VAG-S2. Reading chosen: EDPB Guidelines 3/2018 §6, under which the DPO cannot also hold roles with direct data-processing decision authority (such as head of marketing, head of IT operations, or chief information security officer where that role includes decisions about processing purposes or means), because such roles produce a conflict of interests incompatible with Art. 38(6). An alternative reading treats conflict of interests as confined to personal financial conflicts, excluding organisational conflicts; this reading is rejected by EDPB §6 and is not consistent with the supervisory practice. Remain open: whether a DPO may simultaneously serve as the data-protection officer for multiple affiliated legal entities within a group, on the condition that all entities are bound by group-level policies and the DPO's operational reporting line is unambiguous.
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

