---
document_id: AEGIS-PREPROC-GDPR-ART-37
title: GDPR Art. 37 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 37
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
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.2.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.2.md
status: DRAFT
---

# GDPR Art. 37

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-GDPR-037 | A data protection officer is designated where any of the three Art. 37(1) triggers apply (public authority; core activities of regular/systematic monitoring on large scale; core activities of large-scale special-category or criminal-conviction processing); the DPO performs the Art. 39(1) tasks with adequate independence, resources, and expert knowledge. | `GDPR-CP25` (Art. 37(1)(a)/(b)/(c)); `GDPR-CP26` (Art. 38); `GDPR-CP28` (Art. 39); `GDPR-CP27` (Art. 38(6) — conflict of interests) | D-09.1, D-09.2 |
| SO-GDPR-037 | D-09.1, D-09.2 | Art. 37, Art. 38, Art. 39 | DPO designation and tasks |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-062
  title: "DPO designation triggered by processing profile"
  source_clauses:
    - { clause_id: GDPR-CP25, article_ref: "Art. 37(1)(a)/(b)/(c) — DPO designation triggers" }
  linked_objectives: [SO-GDPR-037]
  sub_domain: [D-09.1, D-09.2]
  nist_csf_mapping:
    - { id: GV.RR-02, title: "Roles/responsibilities/accountabilities established and communicated" }
    - { id: GV.SC-02, title: "Suppliers prioritized and assessed using SCRM processes" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 37(1) requires the controller and the processor to designate a data protection officer in any case where: (a) the processing is carried out by a public authority or body, regardless of the nature of the processing carried out; (b) the core activities of the controller or the processor consist of processing operations which, by virtue of their nature, their scope and/or their purposes, require regular and systematic monitoring of data subjects on a large scale; or (c) the core activities of the controller or the processor consist of processing on a large scale of special categories of data pursuant to Art. 9 or of personal data relating to criminal convictions and offences. The designation is mandatory where any of the three triggers applies; voluntary designation is permitted under Art. 37(4) and is treated equivalently under the WP29 and EDPB Guidelines 3/2018, with the designation made public under Art. 37(7).
  security_rationale: |
    The obligation in Art. 37(1)(a)–(c) is operationalised in NIST CSF 2.0
    through **GV.RR-02 (Roles, responsibilities, authorities, and accountabilities
    related to cybersecurity risk management established, communicated,
    understood, and enforced)** and **GV.SC-02 (Suppliers and other third parties
    known, prioritized, and assessed using a cybersecurity supply chain risk
    management process)**.

    GV.RR-02 controls the designation of the data protection officer as an
    established organisational role with defined responsibilities, reporting line
    and accountability: Art. 37(1) makes designation mandatory where any of the
    three triggers applies — public-authority processing, core-activity regular
    and systematic monitoring of data subjects on a large scale, or core-activity
    large-scale processing of special-category data under Art. 9 or criminal-
    conviction data under Art. 10. GV.SC-02 is applied by analogy to capture the
    controller's self-assessment of whether its processing profile crosses the
    Art. 37(1) thresholds, treated as a risk-based prioritisation of the
    controller's own data-protection exposure.

    Together the two subcategories embed the DPO role in an established
    accountability structure (GV.RR-02) backed by a documented trigger assessment
    (GV.SC-02 analogously), enabling ex-post demonstration to the supervisory
    authority that the designation decision is traceable to the controller's
    processing profile and is updated whenever that profile materially changes.
  ambiguity_notes: |
    Core activities carries VAG-S3; regular and systematic and large scale carry VAG-S3 and POLY-S3; nature, scope and/or purposes contains the Berry §5.1 explicitly-flagged and/or operator. Reading chosen: EDPB Guidelines 3/2018 §3.1, under which core activities are the primary, revenue-driving business activities of the controller and exclude supporting or ancillary functions (HR, IT helpdesk); the and/or in nature, scope and/or purposes is interpreted as inclusive-OR, so that any one of the three dimensions triggering regular and systematic monitoring on a large scale suffices for Art. 37(1)(b). An alternative reading confines core activities to the central business purpose, excluding processing closely related to but not constitutive of that purpose; this reading is narrower than EDPB §3.1 and creates a category of borderline processing that supervisors have generally resolved against the controller. A second alternative reading treats large scale as a hard numeric threshold (for example, the EDPB Guidelines 3/2018 §3.1 reference points of 1000 data subjects for special-category processing); this reading is operationally attractive but the EDPB has declined to fix a universal threshold and treats the assessment as fact-intensive. Remain open: (a) whether a single integrated service that performs both core and ancillary functions can split its processing profile for Art. 37(1)(b) purposes, or whether the controller's overall profile determines designation; (b) whether special-category processing at sub-large-scale on a recurring basis cumulatively reaches the large-scale threshold for Art. 37(1)(c).
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

