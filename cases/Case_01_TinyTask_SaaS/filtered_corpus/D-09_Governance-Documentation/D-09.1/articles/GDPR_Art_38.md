---
document_id: AEGIS-PREPROC-GDPR-ART-38
title: GDPR Art. 38 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 38
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
status: DRAFT
---

# GDPR Art. 38

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-GDPR-037 | A data protection officer is designated where any of the three Art. 37(1) triggers apply (public authority; core activities of regular/systematic monitoring on large scale; core activities of large-scale special-category or criminal-conviction processing); the DPO performs the Art. 39(1) tasks with adequate independence, resources, and expert knowledge. | `GDPR-CP25` (Art. 37(1)(a)/(b)/(c)); `GDPR-CP26` (Art. 38); `GDPR-CP28` (Art. 39); `GDPR-CP27` (Art. 38(6) — conflict of interests) | D-09.1, D-09.2 |
| SO-GDPR-037 | D-09.1, D-09.2 | Art. 37, Art. 38, Art. 39 | DPO designation and tasks |

## Security Rules (from 02_SecurityRules_NIST.md)

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

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

