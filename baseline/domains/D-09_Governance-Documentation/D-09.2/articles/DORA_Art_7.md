---
document_id: AEGIS-PREPROC-DORA-ART-7
title: DORA Art. 7 — SecurityObjectives & SecurityRules
regulation: DORA
article: Art. 7
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
  - ../../CrossRegulation/DomainAnalysis/D-02_Vulnerability-Management/D-02.2.md
  - ../../CrossRegulation/DeepAnalysis/D-02_Vulnerability-Management/D-02.2.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.2.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.2.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.3.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.3.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.1.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.1.md
status: DRAFT
---

# DORA Art. 7

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-DORA-003 | Sources of ICT risk — including cyber threats and ICT vulnerabilities relevant to ICT supported business functions, information assets and ICT assets — are identified on a continuous basis; risk scenarios impacting the entity are reviewed on a regular basis, at least yearly. | `DORA-C06` (Art. 7(2) continuous basis + regular basis + yearly review); `DORA-C08` (Art. 8(2) `all sources of ICT risk` + risk exposure to/from other financial entities) | D-02.1, D-10.1 |
| SO-DORA-003 | D-02.1, D-10.1 | Art. 7(2) + Art. 8(2) | Continuous ICT risk identification + yearly review of risk scenarios |
| SO-DORA-017 | Responsibility for managing and overseeing ICT risk is assigned to a control function with an appropriate level of independence according to the three lines of defence model (or an internal risk management and control model); ICT supported business functions, roles and responsibilities, the information assets and ICT assets supporting those functions, and their roles and dependencies in relation to ICT risk are identified, classified and adequately documented. | `DORA-C04` (Art. 6(4) `appropriate level of independence` + `three lines of defence model`); `DORA-C05` (Art. 7(1) `identify, classify and adequately document` 3-verb + long AND chain of asset classes) | D-09.1, D-09.2, D-09.3 |
| SO-DORA-017 | D-09.1, D-09.2, D-09.3 | Art. 6(4) + Art. 7(1) | Three lines of defence + asset identification/classification |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-DORA-001 (CIA + A maintained across data states)

```yaml
- sr_id: SR-DORA-004
  title: "Continuous ICT risk-source identification with inter-entity awareness"
  source_clauses:
    - { clause_id: DORA-C06, article_ref: "Art. 7(2) — `on a continuous basis, identify all sources of ICT risk`" }
    - { clause_id: DORA-C08, article_ref: "Art. 8(2) — `identify all sources of ICT risk … and assess cyber threats and ICT vulnerabilities relevant to their ICT supported business functions`" }
  linked_objectives: [SO-DORA-003]
  sub_domain: [D-02.1, D-10.1]
  nist_csf_mapping:
    - { id: ID.RA-01, title: "Vulnerabilities in assets are identified, validated, and recorded" }
    - { id: ID.RA-03, title: "Threats, both internal and external, are identified, recorded, and prioritized" }
  applies_to_role: [FINANCIAL_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 7(2) sentence 1 requires financial entities, on a continuous
    basis, to identify all sources of ICT risk, in particular the risk
    exposure to and from other financial entities, and to assess cyber
    threats and ICT vulnerabilities relevant to their ICT supported
    business functions, information assets and ICT assets. Art. 8(2)
    reinforces the requirement to identify all sources of ICT risk.
    These two articles form the temporal and methodological chassis of
    the ICT risk-management framework mandated by Art. 6(8)(a):
    identification is continuous rather than periodic, and the
    inter-entity risk-exposure qualifier (cf. Recital 55 on
    interconnectedness) propagates the obligation across the financial
    sector's value chain (NIS 2 Art. 21(2)(c) imposes a parallel
    baseline-risk identification regime on NSIEs outside DORA, and
    CRA Art. 13(5) on vulnerability handling supplies a downstream
    fact-feeding layer for product vendors feeding DORA entities).
    [OJ-corrective note (v0.2 audit, material): Art. 7(2) → Art. 8(2) misattribution (P0 disagreement cross-cutting). Art. 8(2) sentence 1 (Identification function): financial entities shall, on a regular basis, identify all ICT-supported business functions and the ICT assets that support those functions, including those of third-party providers, and identify the dependencies between those ICT assets. The audit notes that the source article_ref points to Art. 7(2) but the OJ text is in Art. 8(2).]
  security_rationale: |
    The obligation in Art. 7(2)/Art. 8(2) for continuous identification
    of ICT risk sources is operationalised in NIST CSF 2.0 through
    **ID.RA-01 (Vulnerabilities in assets are identified, validated,
    and recorded)** and **ID.RA-03 (Threats, both internal and
    external, are identified, recorded, and prioritized)**. ID.RA-01
    supplies the asset-vulnerability layer — continuous vulnerability
    scanning, CVE-feed ingestion, authenticated vulnerability
    validation, and validated vulnerability records tied to the
    entity's asset inventory, ensuring risk identification is
    evidence-based rather than self-declared. ID.RA-03 supplies the
    threat-intelligence layer — internal-source threat catalogues
    (privileged-activity anomalies, insider-risk indicators) and
    external-source feeds (ISAC partnerships, ENISA threat landscape,
    sectoral TI providers) — with priority scoring aligned to entity
    risk appetite. The OJ qualifier `in particular the risk exposure
    to and from other financial entities` requires the ID.RA-03
    threat-prioritisation model to weight interconnectedness, shared
    CTPP exposure, and shared settlement-infrastructure dependency
    explicitly, not as an after-thought. The accountability link
    under Art. 5(2): the ID.RA-01 vulnerability register and ID.RA-03
    threat catalogue, with documented update cadence, validation
    evidence, and inter-entity-exposure annotations, constitute the
    documented evidence trail the management body can present to
    competent authorities demonstrating that ICT risk identification
    is genuinely continuous and inter-entity-aware rather than
    perimeter-confined.
  ambiguity_notes: |
    Source clause DORA-C06 carries S2 on `continuous basis` vs.
    `regular basis` (POLY — the two terms coexist in the same article
    without differentiation; reading chosen: `continuous` = always-on
    monitoring, `regular` = scheduled review cadence), and S2 on
    `cyber threats AND ICT vulnerabilities` (POLY — distinct concepts;
    reading chosen: R1 cumulative, both assessed). `all sources of
    ICT risk` (SCOPE-Q S2) — R1 all known / R2 all discoverable / R3
    universal quantifier; R3 literal OJ reading (per Berry §5.2.1).
    `relevant to` (VAG S2) — R1 directly impacting / R2 any plausible
    link; R1 dominant. A contrasting reading of `relevant to` could
    take a wider scope (any plausible link) given the OJ qualifier
    `information assets and ICT assets` is broad, but supervisory
    practice in EBA Guidelines on ICT and security risk management
    §92 treats `relevant to` as delimiting to assets whose compromise
    would materially affect ICT-supported business functions. An
    open question remains how to operationalise inter-entity
    risk-identification in practice: bilateral information-sharing
    arrangements under Art. 45 ESAs cooperation framework are one
    recognised mechanism but do not yet have OJ-delegated form.
```

### SO-DORA-001 (CIA + A maintained across data states)

```yaml
- sr_id: SR-DORA-005
  title: "Annual risk-scenario register refresh with strategic recalibration"
  source_clauses:
    - { clause_id: DORA-C06, article_ref: "Art. 7(2) sentence 2 — `Financial entities shall review on a regular basis, and at least yearly, the risk scenarios impacting them`" }
  linked_objectives: [SO-DORA-003]
  sub_domain: [D-02.1, D-09.2]
  nist_csf_mapping:
    - { id: ID.RA-05, title: "Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response decisions" }
    - { id: ID.IM-04, title: "Cybersecurity risk management improvements are informed by awareness of related developments and context" }
    - { id: GV.OV-02, title: "The organizational cybersecurity risk management strategy is reviewed and adjusted to address changes in the organization's risk landscape" }
  applies_to_role: [FINANCIAL_ENTITY]
  obligation_type: [PERIODIC]
  regulatory_rationale: |
    Art. 7(2) sentence 2 requires financial entities to review on a
    regular basis, and at least yearly, the risk scenarios impacting
    them. The hard numeric anchor (`at least yearly`) closes the
    temporal ambiguity of `regular basis`. Recital 56 supports this
    cadence by treating the risk-scenario inventory as a living
    artefact subject to evolving threat-actor capability, and EBA
    Guidelines on ICT and security risk management §100 expressly
    require the inventory to be refreshable at least annually with
    documented evidence of updates. The `at-least-yearly` floor is
    binding even where the entity-internal `regular basis` cadence is
    set tighter (Art. 4 proportionality principle permits upward
    calibration but not downward deviation). The provision sits within
    Art. 7 identification, and the broader Art. 6 chapeau obliges the
    management body to review the framework periodically (NIS 2
    Art. 21(2)(f) on policy review contains a parallel cadence-floor
    obligation).
    [OJ-corrective note (v0.2 audit, material): Art. 7(2) → Art. 8(2) misattribution (P0 disagreement cross-cutting). Art. 8(2) sentence 2 (Identification function): on the basis of an assessment of the criticality of each ICT-supported business function, financial entities shall identify all ICT assets that support those functions, including those of third-party providers, and document the configuration of those ICT assets. The audit notes that the source article_ref points to Art. 7(2) but the OJ text is in Art. 8(2).]
  security_rationale: |
    The obligation in Art. 7(2) sentence 2 for annual risk-scenario
    review is operationalised in NIST CSF 2.0 through **ID.RA-05
    (Threats, vulnerabilities, likelihoods, and impacts are used to
    understand inherent risk and inform risk response decisions)**,
    **ID.IM-04 (Cybersecurity risk management improvements are
    informed by awareness of related developments and context)**, and
    **GV.OV-02 (The organizational cybersecurity risk management
    strategy is reviewed and adjusted to address changes in the
    organization's risk landscape)**. ID.RA-05 forces each scenario
    into a structured likelihood-by-impact matrix, converting
    narrative scenario description into quantified risk inputs that
    can be aggregated across the register. ID.IM-04 closes the
    external-context feedback loop — supervisory guidance, ENISA
    threat-landscape reports, sectoral near-miss incident learnings,
    and CTPP-concentration shifts feed scenario recalibration between
    annual cycles. GV.OV-02 anchors the strategic layer by requiring
    strategy adjustment when scenario-review findings diverge from
    the entity's risk-appetite statement, ensuring the review produces
    governance change rather than documentation churn. The hard
    numeric anchor `at least yearly` aligns naturally with GV.OV-02's
    strategic-review cadence. The accountability link under Art. 5(2):
    the documented scenario-register revisions, likelihood-by-impact
    score evolution, and management-body approval records produce the
    documented evidence trail the management body can present to
    competent authorities demonstrating that annual risk-scenario
    refreshment is operationally substantive and strategy-influencing
    rather than a paperwork ritual.
  ambiguity_notes: |
    `regular basis, and at least yearly` (COORD S2) — R1 the two
    anchors harmonise (regular = at-least-yearly); R2 `regular` may
    impose a tighter cadence than yearly; reading chosen: R1 the
    `and at least yearly` anchors the floor. `risk scenarios`
    (POLY S2) — R1 entity-specific scenarios / R2 sectoral scenarios /
    R3 both; R3 literal. The reading chosen on the cadence-framing is
    explicit that the `and at least yearly` clause is a hard floor
    rather than a softer default: a financial entity whose `regular
    basis` cadence was set at three-yearly would still fail Art. 7(2)
    sentence 2. An alternative reading of `risk scenarios` limited to
    entity-specific scenarios would exclude sector-wide scenarios
    (e.g. CTPP concentration risk arising under Art. 28(4)) and would
    under-deliver on the OJ qualifier `relevant to their ICT supported
    business functions`, which implies external-scenario sensitivity.
    An open question remains whether the EBA's planned supervisory
    review templates under Art. 6(5) will impose a uniform scenario
    taxonomy across the three ESAs.
```

### SO-DORA-001 (CIA + A maintained across data states)

```yaml
- sr_id: SR-DORA-007
  title: "Documented patch and update governance covering full asset estate"
  source_clauses:
    - { clause_id: DORA-C19, article_ref: "Art. 9(4)(f) — `have appropriate and comprehensive documented policies for patches and updates`" }
  linked_objectives: [SO-DORA-004]
  sub_domain: [D-02.2]
  nist_csf_mapping:
    - { id: PR.PS-02, title: "Software is maintained, replaced, and removed commensurate with risk" }
    - { id: ID.RA-01, title: "Vulnerabilities in assets are identified, validated, and recorded" }
  applies_to_role: [FINANCIAL_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 9(4)(f) requires financial entities to have appropriate and
    comprehensive documented policies for patches and updates. This
    sub-paragraph addresses the governance instrument (the *policy*)
    rather than the operational patch-deployment cadence, and operates
    alongside Art. 9(4)(b) network-and-infrastructure controls and
    Art. 7 identification (NIS 2 Art. 21(2)(e) on supply-chain
    security contains a parallel patch-governance requirement with
    CRA Art. 13(11) vulnerability-handling rules feeding the supply
    side). The documented-policy qualifier is binding: an entity
    operating patch deployment ad hoc, even with high operational
    cadence, fails Art. 9(4)(f). EBA Guidelines on ICT and security
    risk management §165–§168 expect policies to specify scope,
    approval authorities, exception handling and rollback procedures.
  security_rationale: |
    The obligation in Art. 9(4)(f) for documented patch and update
    policies is operationalised in NIST CSF 2.0 through **PR.PS-02
    (Software is maintained, replaced, and removed commensurate with
    risk)** and **ID.RA-01 (Vulnerabilities in assets are identified,
    validated, and recorded)**. PR.PS-02 establishes the operational
    patch-management discipline — severity classification taxonomies,
    SLA-bound deployment windows, documented exception-handling for
    compensating controls during deferred-patch windows, rollback
    runbooks for production-impacting patches — anchored to risk-tier
    rather than uniform cadence. ID.RA-01 supplies the upstream
    vulnerability-identification substrate without which PR.PS-02
    cannot prioritise: validated vulnerability records tied to the
    asset inventory (CVE-feed ingestion, authenticated validation,
    risk-scored entries) drive patch-priority ordering. The OJ
    `appropriate and comprehensive` qualifier aligns with PR.PS-02's
    risk-commensurate framing under Art. 4 proportionality and with
    the breadth requirement (full asset estate rather than critical-
    only). The accountability link under Art. 5(2): the patch-
    classification taxonomy, SLA-window records, exception registers,
    and rollback-procedure documentation produce the documented
    evidence trail the management body can present to competent
    authorities demonstrating that patch governance is comprehensive,
    documented, and risk-driven rather than ad-hoc.
  ambiguity_notes: |
    `appropriate and comprehensive` (COORD S2) — R1 both qualities
    required (literal AND); R2 either alone may suffice; R1 literal.
    **T4-vs-text gap:** T4 maps DORA-C19 to `D-07.2 Secure Coding
    Practices` but the OJ Art. 9(4)(f) text is `patches and
    updates`, which is patch-management policy not secure-coding.
    The Executor preserves OJ-literal locus at D-02.2 patch
    management. Per AEGIS taxonomy §4.1, DORA is listed as sole
    authority for D-07.2; this pilot finds no OJ-text support for
    that assignment and recommends Layer 2 review. A contrasting
    reading of `appropriate` could treat the word as a proportionality
    elasticity valve under Art. 4 (entities operating at small scale
    maintain less elaborate policies), but the literal conjunction
    `and comprehensive` requires both to be delivered regardless of
    entity scale. An open question is whether the ESAs Joint
    Committee RTS under Art. 15(2) will provide quantified patch-SLA
    expectations (e.g. severity-to-deployment-window mappings) that
    the OJ text itself does not specify.
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
- sr_id: SR-DORA-028
  title: "Independence of ICT risk oversight via three-lines-of-defence model"
  source_clauses:
    - { clause_id: DORA-C04, article_ref: "Art. 6(4) — `assign the responsibility for managing and overseeing ICT risk to a control function and ensure an appropriate level of independence … according to the three lines of defence model, or an internal risk management and control model`" }
  linked_objectives: [SO-DORA-017]
  sub_domain: [D-09.1, D-09.2]
  nist_csf_mapping:
    - { id: GV.RR-02, title: "Roles, responsibilities, authorities, and accountabilities related to cybersecurity risk management are established, communicated, understood, and enforced" }
    - { id: GV.RM-02, title: "Risk roles, responsibilities, authorities, and accountabilities are established and communicated" }
  applies_to_role: [FINANCIAL_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 6(4) requires financial entities to assign the responsibility for
    managing and overseeing ICT risk to a control function and to ensure an
    appropriate level of independence, in accordance with the three lines of
    defence model or an internal risk management and control model. The
    three-lines-of-defence model is the banking-supervision standard (Basel
    Committee; EBA Guidelines on Internal Governance), but the OR with
    `internal risk management and control model` opens the door to alternative
    models (e.g. COSO, ISO 31000). The clause aligns functionally with the
    NIS 2 Art. 21(1) governance-of-cybersecurity-risk baseline (Directive
    (EU) 2022/2555) and is the structural-setup counterpart to Art. 7 asset
    identification and to Art. 9 protection policies.
  security_rationale: |
    The Art. 6(4) control-function independence duty is operationalised in
    NIST CSF 2.0 through **GV.RR-02 (Roles, responsibilities, authorities,
    and accountabilities related to cybersecurity risk management are
    established, communicated, understood, and enforced)** and **GV.RM-02
    (Risk roles, responsibilities, authorities, and accountabilities are
    established and communicated)**. GV.RR-02 anchors the structural
    separation between operational management (first line), risk-and-
    compliance oversight (second line), and internal audit (third line)
    that the OJ `appropriate level of independence` qualifier operationalises
    in the three-lines-of-defence model — the interlock that prevents
    operational blind spots and compliance failures from going uncorrected.
    GV.RM-02 layers the communication-and-understanding engine, ensuring
    that the role allocation is not merely established on paper but is
    communicated across the entity and understood by all three lines so
    that escalation pathways, reporting lines, and authority thresholds
    are exercisable rather than theoretical. Together these two
    subcategories operationalise the OJ `or an internal risk management
    and control model` alternative, and an entity evidencing GV.RR-02
    structural separation plus GV.RM-02 documented role-allocation
    communication can demonstrate ex-post to supervisory review that
    the Art. 6(4) independence obligation was met through both
    architectural choice (3LoD or equivalent) and operational
    communication discipline, allowing alternative-model entities
    (COSO, ISO 31000) to satisfy the duty on equivalence terms.
  ambiguity_notes: |
    S2 VAG on `appropriate level of independence` — alternatives include
    structural separation, functional separation, or both; the chosen reading
    is the literal AND. S2 POLY on `control function` — alternatives include
    first-line, second-line, or third-line; the chosen reading is third-line
    given the three-lines-of-defence reference. S2 COORD on `ICT risk
    management functions, control functions, AND internal audit functions`
    — all three function types in scope. S2 POLY on `or an internal risk
    management and control model` — alternatives include either, with the
    chosen reading that both are accepted. Remain open: documentation of
    which alternative model is used (where not 3LoD) is an entity-policy
    matter.
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

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

