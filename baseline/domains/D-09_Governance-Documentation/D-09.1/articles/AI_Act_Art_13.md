---
document_id: AEGIS-PREPROC-AI_Act-ART-13
title: AI_Act Art. 13 — SecurityObjectives & SecurityRules
regulation: AI_Act
article: Art. 13
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-07_Secure-Development/D-07.1.md
  - ../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.1.md
  - ../../CrossRegulation/DomainAnalysis/D-08_Human-Factors/D-08.2.md
  - ../../CrossRegulation/DeepAnalysis/D-08_Human-Factors/D-08.2.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
status: DRAFT
---

# AI_Act Art. 13

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-AIACT-007 | High-risk AI systems are designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system's output and use it appropriately, accompanied by concise, complete, correct and clear instructions for use that include relevant, accessible and comprehensible information about the characteristics, capabilities and limitations of performance. | `AIA-C12` (Art. 13(1) — `sufficiently transparent` + `appropriate type and degree of transparency` POLY triple); `AIA-C13` (Art. 13(3) — `concise, complete, correct and clear` 4-way AND + `relevant, accessible and comprehensible` 3-way AND + `characteristics, capabilities and limitations of performance` POLY triple) | D-09.1 |
| SO-AIACT-007 | D-09.1 | Art. 13(1)+(3) | Transparency to deployers + instructions for use |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-AIACT-001 (AI risk management lifecycle)

```yaml
- sr_id: SR-AIACT-010
  title: "Deployer-interpretable transparency enabling appropriate system use"
  source_clauses:
    - { clause_id: AIA-C12, article_ref: "Art. 13(1) — `High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system's output and use it appropriately. An appropriate type and degree of transparency shall be ensured`" }
  linked_objectives: [SO-AIACT-007]
  sub_domain: [D-09.1]
  nist_csf_mapping:
    - { id: GV.PO-01, title: "Organizational cybersecurity policy is established, communicated, and enforced" }
    - { id: GV.OC-03, title: "Legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed" }
    - { id: GV.OC-04, title: "Critical objectives, capabilities, and services that stakeholders depend on or expect from the organization are understood and communicated" }
  applies_to_role: [PROVIDER]
  obligation_type: [CONTINUOUS, ONE_TIME]
  regulatory_rationale: |
    Article 13(1) of the AI Act requires that high-risk AI systems
    be designed and developed in such a way as to ensure that their
    operation is sufficiently transparent to enable deployers to
    interpret a system's output and use it appropriately. A second
    sentence requires that an appropriate type and degree of
    transparency shall be ensured. The clause sits at the
    intersection of the design-and-development obligations in
    Chapter III, Section 2 and the broader transparency obligations
    in Chapter V (Articles 50 to 52) that apply to all AI systems
    interacting with natural persons. Article 13(1) is the
    principal high-risk-specific transparency duty, distinct from
    the Article 50 user-facing transparency duty and the Article 70
    deployer-information duty, and is also the principal locus
    where AI-explainability expectations are operationalised as a
    regulatory requirement.
    the Article 50 user-facing transparency duty for AI systems
    interacting with natural persons and from the Article 70
    deployer-information duty. The clause is also the principal
    locus where AI-explainability expectations are operationalised
    as a regulatory requirement, with downstream effects on
    technical-architecture choices for high-risk providers.
  security_rationale: |
    The obligation in Art. 13(1) is operationalised in NIST CSF
    2.0 through **GV.PO-01 (Organizational cybersecurity policy
    is established, communicated, and enforced)**, **GV.OC-03
    (Legal, regulatory, and contractual requirements regarding
    cybersecurity — including privacy and civil liberties
    obligations — are understood and managed)**, and **GV.OC-04
    (Critical objectives, capabilities, and services that
    stakeholders depend on or expect from the organization are
    understood and communicated)**. GV.PO-01 anchors the
    cybersecurity-policy substrate that the dual-anchor
    `sufficiently transparent` plus `appropriate type and degree`
    qualifier requires — transparency must be policy-bound and
    enforced to be supervisory-auditable. GV.OC-03 supplies the
    legal-and-regulatory understanding substrate that
    distinguishes the high-risk-specific Art. 13(1) transparency
    duty from the Article 50 user-facing and Article 70
    deployer-information duties, ensuring the cumulative AND of
    explainability, disclosure and interpretability senses is
    operationalised against an understood regulatory baseline.
    GV.OC-04 anchors the stakeholder-communication dimension —
    deployers are the principal stakeholders for AI-system
    transparency — operationalising the `interpret a system's
    output AND use it appropriately` opening through understood
    capabilities and limitations. A provider documenting GV.PO-01
    transparency policy, GV.OC-03 regulatory distinction and
    GV.OC-04 deployer-stakeholder communication demonstrates ex
    post that the Art. 13(1) high-risk-specific transparency duty
    is operationalised with policy enforcement, regulatory clarity
    and stakeholder usability.
  ambiguity_notes: |
    The clause carries the central S3 ambiguity on `sufficiently
    transparent` and on `appropriate type and degree of
    transparency` — two vague anchors in one sentence, both
    modifying the same concept. The phrase `transparent` is
    poly-semous and admits three distinct AI-governance senses:
    explainability (the deployer can understand why the system
    produced this output), disclosure (the deployer is told what
    the system does in general) and interpretability (the deployer
    can map inputs to outputs). The three senses imply different
    technical implementations — explainable-AI tooling,
    system documentation and model-architecture disclosure
    respectively. The chosen reading is cumulative, covering all
    three senses, because the `interpret a system's output AND
    use it appropriately` opening implicates each. As an
    alternative, providers could focus on disclosure only, which
    is the cheapest to operationalise but the weakest against the
    explanatory demands of automation-bias mitigation. As a second
    alternative, providers could focus on explainability only,
    which requires the most sophisticated technical tooling such
    as SHAP or LIME post-hoc explanation. The scope-determiner
    `intended purpose` remains undefined in Article 3 and recurs
    across eleven of the twenty-nine mapped clauses, with its
    scope ambiguity propagating into Article 13(1). Remain open:
    (a) whether `appropriate type and degree of transparency`
    introduces a tiered obligation calibrated to the risk class of
    the high-risk system per Annex III categories, or a uniform
    obligation across all high-risk systems; (b) whether the
    explainability sense requires post-hoc explanation tooling
    such as LIME or SHAP, or whether architectural transparency
    in the form of model-card disclosure suffices.
```

### SO-AIACT-001 (AI risk management lifecycle)

```yaml
- sr_id: SR-AIACT-011
  title: "Concise complete and clear deployer instructions for use"
  source_clauses:
    - { clause_id: AIA-C13, article_ref: "Art. 13(3) — `instructions for use in an appropriate digital format or otherwise that include concise, complete, correct and clear information that is relevant, accessible and comprehensible to deployers`" }
  linked_objectives: [SO-AIACT-007]
  sub_domain: [D-09.1]
  nist_csf_mapping:
    - { id: GV.PO-01, title: "Organizational cybersecurity policy is established, communicated, and enforced" }
    - { id: GV.OC-04, title: "Critical objectives, capabilities, and services that stakeholders depend on or expect from the organization are understood and communicated" }
  applies_to_role: [PROVIDER]
  obligation_type: [ONE_TIME]
  regulatory_rationale: |
    Article 13(3) of the AI Act requires high-risk AI systems to be
    accompanied by instructions for use, in an appropriate digital
    format or otherwise, that include concise, complete, correct
    and clear information that is relevant, accessible and
    comprehensible to deployers. The instructions-for-use duty
    operationalises the upstream transparency duty in Article
    13(1) by translating the abstract transparency requirement
    into a concrete documentation deliverable that accompanies the
    high-risk AI system at placement on the market or putting into
    service. The eight quality adjectives — concise, complete,
    correct, clear, relevant, accessible, comprehensible, plus
    `appropriate digital format` — set a substantive quality
    threshold that providers must evidence in their documentation.
    Article 13(3) is also a locus where the AI Act intersects with
    CRA Article 7(4) instructions-for-use obligations for products
    with digital elements and with CRA Annex I documentation
    requirements.
  security_rationale: |
    The obligation in Art. 13(3) is operationalised in NIST CSF
    2.0 through **GV.PO-01 (Organizational cybersecurity policy is
    established, communicated, and enforced)** and **GV.OC-04
    (Critical objectives, capabilities, and services that
    stakeholders depend on or expect from the organization are
    understood and communicated)**. GV.PO-01 anchors the
    policy-and-enforcement substrate that the eight quality
    adjectives (concise, complete, correct, clear, relevant,
    accessible, comprehensible, plus `appropriate digital format`)
    require — instructions for use must be policy-bound and
    enforced to ensure documentation discipline, with the twin
    4-way AND (`concise, complete, correct AND clear`) plus
    3-way AND (`relevant, accessible AND comprehensible`) both
    evidenced as compliance artefacts. GV.OC-04 supplies the
    stakeholder-communication substrate that the
    deployer-facing documentation requires, ensuring that the
    eight quality adjectives are operationalised as communication
    outputs rather than as engineering artefacts, and that the
    characteristics, capabilities and limitations of performance
    are conveyed in a manner the deployer can actually use.
    Together, the two GV sub-categories cover policy enforcement
    (GV.PO-01) and stakeholder-usable communication (GV.OC-04)
    that Art. 13(3) operationalises. A provider evidencing
    GV.PO-01 documentation policy and GV.OC-04
    deployer-stakeholder communication demonstrates ex post that
    the Art. 13(3) instructions-for-use duty is discharged as an
    operationally usable deliverable accompanying the high-risk
    AI system at placement on the market or putting into service.
  ambiguity_notes: |
    The clause carries medium severity on eight vague adjectives
    in one sentence: `appropriate`, `concise`, `complete`,
    `correct`, `clear`, `relevant`, `accessible`,
    `comprehensible`. The phrase `characteristics, capabilities
    and limitations of performance` is poly-semous, with three
    near-synonyms for system properties; the chosen reading is
    that the three near-synonyms are intentionally cumulative and
    each must be addressed in the instructions. The twin
    AND-chains — `concise, complete, correct AND clear` (4-way)
    plus `relevant, accessible AND comprehensible` (3-way) —
    form a compounded coordination that is hard to satisfy with
    single-modality documentation. As an alternative reading,
    providers could collapse the twin chains into a single
    integrated documentation requirement. Remain open: whether
    `appropriate digital format` accepts machine-readable PDF/A-3
    plus human-readable HTML, or whether it requires a
    structured-machine-readable format such as JSON-LD or XBRL
    that supports automated supervisory ingestion under Article
    21 conformity-assessment documentation expectations.
```

### SO-AIACT-001 (AI risk management lifecycle)

```yaml
- sr_id: SR-AIACT-012
  title: "Built-in effective human-oversight capability by design"
  source_clauses:
    - { clause_id: AIA-C14, article_ref: "Art. 14(1) — `High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use`" }
  linked_objectives: [SO-AIACT-008]
  sub_domain: [D-08.2, D-07.1]
  nist_csf_mapping:
    - { id: PR.AT-02, title: "All members of the organization's workforce understand their roles and responsibilities in achieving the organization's cybersecurity objectives" }
    - { id: GV.RR-02, title: "Roles, responsibilities, authorities, and accountabilities related to cybersecurity risk management are established, communicated, understood, and enforced" }
    - { id: GV.RR-04, title: "Cybersecurity is included in human resources practices (e.g., people screening, onboarding, training, awareness, offboarding)" }
  applies_to_role: [PROVIDER]
  obligation_type: [CONTINUOUS, ONE_TIME]
  regulatory_rationale: |
    Article 14(1) of the AI Act requires that high-risk AI systems
    be designed and developed in such a way, including with
    appropriate human-machine interface tools, that they can be
    effectively overseen by natural persons during the period in
    which they are in use. The clause is the umbrella provision
    for the human-oversight duty in Article 14, with the more
    substantive content of the duty operationalised in Article
    14(2) to (5). The clause allocates responsibility for
    oversight design to the provider, and it ensures that human
    oversight is a built-in architectural feature of the high-risk
    AI system rather than an externally imposed deployment-time
    add-on. Article 14(1) is the principal locus where the AI Act
    bridges from technical-design obligations to human-factors
    obligations, and it is reinforced by Article 14(2) on
    deployer-implemented oversight measures and Article 14(3) on
    proportionality of oversight to the risks and intended purpose.
  security_rationale: |
    The obligation in Art. 14(1) is operationalised in NIST CSF
    2.0 through **PR.AT-02 (All members of the organization's
    workforce understand their roles and responsibilities in
    achieving the organization's cybersecurity objectives)**,
    **GV.RR-02 (Roles, responsibilities, authorities, and
    accountabilities related to cybersecurity risk management are
    established, communicated, understood, and enforced)**, and
    **GV.RR-04 (Cybersecurity is included in human resources
    practices (e.g., people screening, onboarding, training,
    awareness, offboarding))**. PR.AT-02 anchors the
    workforce-role-understanding substrate that the `appropriate
    human-machine interface tools` qualifier requires — providers
    must design oversight interfaces the deploying workforce can
    actually use to discharge the five abilities of Art. 14(4).
    GV.RR-02 supplies the RACI substrate that the `effectively
    overseen` duty requires, ensuring human oversight is a
    built-in architectural feature with formal authority to
    intervene, not a deployment-time add-on. GV.RR-04 covers the
    HR-practices dimension — onboarding, training, awareness —
    that the upstream Art. 13(3) instructions for use and the
    downstream Art. 14(2) deployer-implemented measures jointly
    require for oversight sustainability. A provider documenting
    PR.AT-02 workforce role understanding, GV.RR-02 RACI
    definition and GV.RR-04 HR-practice integration demonstrates
    ex post that the Art. 14(1) oversight-design substrate is
    operationalised as a built-in architectural feature,
    satisfying the cumulative supervisor-can-intervene,
    supervisor-does-intervene and supervisor-understands senses.
  ambiguity_notes: |
    The clause carries medium severity on the vague adjectives
    `appropriate` (modifying human-machine interface tools) and
    `effectively overseen`. The phrase `effectively overseen` is
    poly-semous and admits three readings: supervisor-can-intervene,
    supervisor-does-intervene, and supervisor-understands. The
    three senses drive different design choices — stop-button,
    dashboard and explanation-panel respectively. The chosen
    reading is cumulative, covering all three senses, because the
    `during the period in which they are in use` opening implicates
    each. As an alternative reading, providers could focus on
    supervisor-can-intervene only, which is the cheapest to
    operationalise but the weakest against the
    supervisor-does-intervene and supervisor-understands senses
    that Article 14(4) separately addresses. Remain open: whether
    `appropriate human-machine interface tools` requires the
    provider to supply proprietary oversight tooling, or whether
    deployer-supplied oversight tooling suffices where the
    provider documents the oversight-design interface and the
    minimum-tooling expectations in the instructions for use under
    Article 13(3).
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

