---
document_id: AEGIS-PREPROC-DORA-ART-21
title: DORA Art. 21 — SecurityObjectives & SecurityRules
regulation: DORA
article: Art. 21
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-01_Data-Protection/D-01.1.md
  - ../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.1.md
  - ../../CrossRegulation/DomainAnalysis/D-01_Data-Protection/D-01.2.md
  - ../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.2.md
  - ../../CrossRegulation/DomainAnalysis/D-01_Data-Protection/D-01.3.md
  - ../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.3.md
  - ../../CrossRegulation/DomainAnalysis/D-01_Data-Protection/D-01.4.md
  - ../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.4.md
  - ../../CrossRegulation/DomainAnalysis/D-02_Vulnerability-Management/D-02.1.md
  - ../../CrossRegulation/DeepAnalysis/D-02_Vulnerability-Management/D-02.1.md
  - ../../CrossRegulation/DomainAnalysis/D-02_Vulnerability-Management/D-02.2.md
  - ../../CrossRegulation/DeepAnalysis/D-02_Vulnerability-Management/D-02.2.md
  - ../../CrossRegulation/DomainAnalysis/D-02_Vulnerability-Management/D-02.4.md
  - ../../CrossRegulation/DeepAnalysis/D-02_Vulnerability-Management/D-02.4.md
  - ../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.3.md
  - ../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.3.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.1.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.1.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.2.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.2.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.4.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.4.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.1.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.1.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.3.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.3.md
  - ../../CrossRegulation/DomainAnalysis/D-07_Secure-Development/D-07.1.md
  - ../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.1.md
  - ../../CrossRegulation/DomainAnalysis/D-07_Secure-Development/D-07.4.md
  - ../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.4.md
  - ../../CrossRegulation/DomainAnalysis/D-08_Human-Factors/D-08.1.md
  - ../../CrossRegulation/DeepAnalysis/D-08_Human-Factors/D-08.1.md
  - ../../CrossRegulation/DomainAnalysis/D-08_Human-Factors/D-08.2.md
  - ../../CrossRegulation/DeepAnalysis/D-08_Human-Factors/D-08.2.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.2.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.2.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.3.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.3.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.1.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.1.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.2.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.2.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.3.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.3.md
status: DRAFT
---

# DORA Art. 21

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

_No standalone SO row cites this article directly (covered via the rules below)._

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-DORA-001 (CIA + A maintained across data states)

```yaml
- sr_id: SR-DORA-001
  title: "Cross-state CIA+A protection matrix with risk-tiered controls"
  source_clauses:
    - { clause_id: DORA-C09, article_ref: "Art. 9(2) — CIA+A 4-way AND + at-rest/in-use/in-transit 3-way OR" }
    - { clause_id: DORA-C10, article_ref: "Art. 9(2) — in-transit dimension (same locus, explicit in OJ)" }
    - { clause_id: DORA-C11, article_ref: "Art. 9(2) — integrity dimension (same locus, explicit in OJ)" }
  linked_objectives: [SO-DORA-001]
  sub_domain: [D-01.1, D-01.2, D-01.4]
  nist_csf_mapping:
    - { id: PR.DS-01, title: "Data-at-rest protected" }
    - { id: PR.DS-02, title: "Data-in-transit protected" }
    - { id: PR.DS-10, title: "Data-in-use protected" }
    - { id: PR.DS-12, title: "Data managed consistent with the organization's risk strategy" }
  applies_to_role: [FINANCIAL_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 9(2) requires financial entities to design, procure and implement
    ICT security policies, procedures, protocols and tools that aim to
    ensure the resilience, continuity and availability of ICT systems and
    to maintain high standards of availability, authenticity, integrity
    and confidentiality of data, whether at rest, in use or in transit.
    This provision sits at the core of Chapter II Section II's operational
    resilience architecture and supplies the substantive content to the
    chapeau obligation in Art. 6(8) that the ICT risk-management
    framework must address data security across the full ICT lifecycle
    (EBA Guidelines on ICT and security risk management §123). The four
    security objectives (availability, authenticity, integrity and
    confidentiality) are coordinated by `and` and the three data states
    by `or`, yielding a 4×3 protection matrix whose combination rule is
    the principal subject of Art. 9(2) itself. Recital 49 makes clear
    that the financial-sector objective is continuity of service under
    both normal and adverse conditions, so availability across states
    carries operational weight comparable to confidentiality (NIS 2
    Art. 21(2)(a) supplies a parallel cross-state formulation to which
    DORA-fall-back NSIEs are subject, reinforcing the vocabulary).
  security_rationale: |
    The obligation in Art. 9(2) for cross-state CIA+A protection of
    financial-entity data is operationalised in NIST CSF 2.0 through
    **PR.DS-01 (Data-at-rest protected)**, **PR.DS-02 (Data-in-transit
    protected)**, **PR.DS-10 (Data-in-use protected)**, and **PR.DS-12
    (Data managed consistent with the organization's risk strategy)**.
    PR.DS-01 and PR.DS-02 anchor confidentiality and integrity through
    encryption-at-rest (validated cryptographic modules, AES-class symmetric
    primitives for bulk data) and authenticated-transport encryption for transit, with authenticated-encryption
    modes preventing the classical confidentiality-without-integrity gap.
    PR.DS-10 closes the in-use dimension that financial entities have
    historically under-protected through confidential-computing enclaves
    and memory-encryption primitives, preventing the cross-state gap that
    turns a protected data store into an unprotected memory dump.
    PR.DS-12 supplies the risk-strategy calibration: data-handling
    rules are tiered against impact assessment (RTO/RPO alignment with
    business-criticality), ensuring the 4×3 matrix reflects the entity's
    own criticality taxonomy rather than a uniform posture. The
    accountability link under Art. 5(2): these four PR.DS subcategories
    jointly produce the documented evidence trail — classification
    inventory, cipher-algorithm register, key-custody records, in-use
    enclave attestations — that the management body can present to
    competent authorities to demonstrate that the CIA+A and cross-state
    obligations are continuously maintained, risk-calibrated, and
    inspectable.
  ambiguity_notes: |
    Source clause DORA-C09 carries S3 on `high standards` (VAG — no
    measurement criterion), S3 on the 4-way AND of CIA+A (COORD —
    partial-compliance undefined; reading chosen: R1 all four required,
    any absence is non-compliance), and S3 on the 3-way OR of data
    states (COORD — reading chosen: R1 all three required for the
    protection to be effective across the data lifecycle). `at rest`,
    `in use`, `in transit` are explicit in the OJ text — unlike GDPR's
    T1-imposed split or NIS 2's T3-imposed split. `high standards` (R1
    best practice / R2 published standards / R3 frontier research) —
    reading chosen: R1 best practice with R2 published standards as
    the dominant EU supervisory reading (cf. EBA Guidelines on ICT and
    security risk management). As a structural alternative to that
    dominant reading the OJ text could be argued to require an
    open-ended pursuit of `high standards` calibrated against frontier
    research literature, raising the bar substantially but removing
    any comfortable reference set. A third constructed reading would
    treat `high standards` as a composite trigger encompassing all
    three reference frameworks simultaneously. Reading chosen: the
    dominant R1-with-R2 framing because supervisory convergence on
    published ISO/IEC and NIST standards is the only source of
    measurability. The data-state 3-way OR reads as a *coordination*
    of three states rather than an alternative: a control that protects
    data at rest but not in transit fails to deliver the
    `high standards` of confidentiality OJ-implied because movement
    is the dominant flow in financial-entity ICT. The Art. 15 RTS
    mandate to the ESAs remains pending for elements of Art. 9(2),
    which may eventually harden the measurability of `high standards`
    via technical standards adopted under Art. 15(2)–(3). Remain open: (a)
    whether the ESAs Joint Committee RTS under Art. 15 will introduce a
    measurable threshold that closes the `high standards` VAG regress;
    (b) whether supervisory convergence will hold across the three ESAs
    given divergent sectoral risk perceptions (banking, insurance,
    securities) and the EBA's prior preference for ISO/IEC alignment.
```

### SO-DORA-001 (CIA + A maintained across data states)

```yaml
- sr_id: SR-DORA-003
  title: "Classification-driven cryptographic-key protection with policy linkage"
  source_clauses:
    - { clause_id: DORA-C15, article_ref: "Art. 9(4)(d) — `protection measures of cryptographic keys whereby data is encrypted based on results of approved data classification and ICT risk assessment processes`" }
    - { clause_id: DORA-C17, article_ref: "Art. 9(4)(d) same locus — key-management sub-phrase" }
  linked_objectives: [SO-DORA-002]
  sub_domain: [D-01.3]
  nist_csf_mapping:
    - { id: PR.DS-01, title: "Data-at-rest protected" }
    - { id: GV.RM-04, title: "Strategic direction on identifying and responding to risks established and communicated" }
  applies_to_role: [FINANCIAL_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 9(4)(d) `protection measures of cryptographic keys whereby
    data is encrypted based on results of approved data classification
    and ICT risk assessment processes`. The clause ties encryption to
    approved data classification and ICT risk assessment — the
    classification and assessment drive the encryption level. The
    `approved` qualifier is binding: data-classification processes must
    be approved by the financial entity's governance layer (Art. 5(2)
    management body oversight), and ICT risk assessment processes must
    satisfy Art. 6 chapeau's requirement to maintain a sound and
    comprehensive risk-management framework (NIS 2 Art. 21(2)(d) on
    cryptography supplies a parallel regime for non-financial NSIEs
    that DORA financial entities retain as joint obligation where they
    also operate as NIS 2 entities). Recital 53 grounds the
    data-classification link in the precautionary principle applied
    to sensitive financial data, which EBA Guidelines on ICT and
    security risk management §149 interpret as requiring tiered
    classification reflected in tiered cryptographic strength.
  security_rationale: |
    The obligation in Art. 9(4)(d) for classification-driven
    cryptographic-key protection is operationalised in NIST CSF 2.0
    through **PR.DS-01 (Data-at-rest protected)** and **GV.RM-04
    (Strategic direction on identifying and responding to risks
    established and communicated)**. PR.DS-01 anchors encryption-at-
    rest with HSM-anchored key custodianship, split-knowledge
    ceremonies, documented rotation cadences scaled to data
    criticality, and quorum-based key-recovery procedures — the
    operational substrate that makes the Art. 9(4)(d) classification-
    driven proportionality tractable in practice. GV.RM-04 elevates
    the strategic posture by requiring documented board-level direction
    on risk response (including cryptographic-key policy as a strategic
    risk-management artefact), aligned to the entity's risk appetite
    and reviewed under the broader framework-review cadence. The two
    subcategories together bridge the technical layer (PR.DS-01) and
    the governance layer (GV.RM-04) that the OJ text couples through
    `approved data classification and ICT risk assessment processes`.
    The accountability link under Art. 5(2): PR.DS-01's key-inventory
    and rotation logs combined with GV.RM-04's strategic-policy records
    produce the documented evidence trail the management body can
    present to competent authorities demonstrating that encryption is
    genuinely classification-driven, governance-approved, and risk-
    tiered rather than uniformly applied.
  ambiguity_notes: |
    `approved data classification` (POLY S2) — R1 entity-internal
    classification / R2 supervisory-recognised classification scheme
    / R3 either; reading chosen: R1 entity-internal with R2 as the
    supervisory expectation. `ICT risk assessment processes` (POLY
    S2) — R1 entity-internal / R2 sectoral / R3 EU-level; R1 literal.
    `protection measures` (POLY S2) — R1 key-management policy / R2
    key-management operational capability / R3 both; R3 literal.
    The reading chosen on `approved data classification` harmonises
    with the management-body approval pattern of Art. 5(2), under
    which data classification is governance-approved. An alternative
    reading would interpret `approved` as supervisory-approved, in
    line with sectoral schemes such as EBA's payment-data taxonomy,
    but that reading is unsupported by the OJ text because DORA does
    not designate a single supervisory-recognised classification
    scheme for all financial entities.     The risk-assessment-processes
    variant reading is straightforward: DORA imposes the obligation on
    the entity, not on a sectoral authority. A supervisory-recognised
    classification reading is otherwise unexplored in OJ text and so
    was discarded. Remain open: (a) the operational threshold for `approved` governance approval — whether a documented policy suffices or a board-level resolution is required — pending EBA Guidelines clarification; (b) the relationship between the Art. 9(4)(d) classification scheme and any sectoral scheme the entity already operates, pending Art. 15 RTS.
```

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
- sr_id: SR-DORA-006
  title: "Network and infrastructure management with automated blast-radius isolation"
  source_clauses:
    - { clause_id: DORA-C13, article_ref: "Art. 9(4)(b) — `sound network and infrastructure management structure using appropriate techniques, methods and protocols that may include implementing automated mechanisms to isolate affected information assets in the event of cyber-attacks`" }
  linked_objectives: [SO-DORA-004]
  sub_domain: [D-02.2, D-07.1]
  nist_csf_mapping:
    - { id: PR.PS-01, title: "Configuration management practices are established, documented, and applied to assets" }
    - { id: PR.IR-01, title: "Networks and environments are protected from unauthorized logical access and usage" }
    - { id: PR.IR-03, title: "Mechanisms are put in place to achieve resilience requirements in normal and adverse situations" }
  applies_to_role: [FINANCIAL_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 9(4)(b) requires financial entities to establish a sound
    network and infrastructure management structure using appropriate
    techniques, methods and protocols that may include implementing
    automated mechanisms to isolate affected information assets in
    the event of cyber-attacks. This is one of eight mandatory control
    domains in Art. 9(4) chapeau, anchoring the structural dimension
    of ICT security controls (NIS 2 Art. 21(2)(b)–(c) on
    incident-handling and business-continuity supply a parallel
    operational dimension). Recital 53 highlights network-segmentation
    practice as a primary defence against lateral movement. The `may
    include` construction explicitly makes automated isolation
    capability one of several possible control techniques within a
    broader required structure of techniques, methods and protocols,
    not a stand-alone obligation (cf. EBA Guidelines on ICT and
    security risk management §172).
  security_rationale: |
    The obligation in Art. 9(4)(b) for sound network and infrastructure
    management structure is operationalised in NIST CSF 2.0 through
    **PR.PS-01 (Configuration management practices are established,
    documented, and applied to assets)**, **PR.IR-01 (Networks and
    environments are protected from unauthorized logical access and
    usage)**, and **PR.IR-03 (Mechanisms are put in place to achieve
    resilience requirements in normal and adverse situations)**.
    PR.PS-01 establishes the configuration baseline — golden images,
    drift detection, configuration-as-code — that makes subsequent
    segmentation and isolation enforceable rather than aspirational.
    PR.IR-01 enforces the logical-access layer (zero-trust east-west
    traffic controls, network segmentation, micro-segmentation around
    payment-processing and settlement-infrastructure zones) that limits
    lateral movement once a perimeter is breached. PR.IR-03 supplies
    the resilience layer (redundant paths, failover, automated
    isolation mechanisms triggered on detected compromise) that the
    OJ `may include` clause operationalises through segmented
    blast-radius containment. The three PR subcategories together
    transform the OJ `sound network and infrastructure management
    structure` from a procedural requirement into a measured
    architectural capability. The accountability link under Art. 5(2):
    configuration-management records, segmentation-policy
    documentation, and isolation-test outcomes produce the documented
    evidence trail the management body can present to competent
    authorities demonstrating that network and infrastructure
    management is structurally protective rather than nominal.
  ambiguity_notes: |
    Source clause DORA-C13 carries S2 on `sound` and `appropriate`
    (VAG), S2 on `network and infrastructure` (POLY — distinct or
    composite), and S2 on `techniques, methods and protocols` (COORD
    3-way AND of near-synonyms; reading chosen: R1 cumulative, the
    three together cover the structural, procedural, and protocol-
    level dimensions of network and infrastructure management).
    **`may include` (POLY S2)** — R1 optional illustrative / R2
    expected minimum; R1 literal OJ (the `may` softens the
    `include`). **T4-vs-text gap:** T4 maps DORA-C13 to `D-02.2
    Patch Management & Updates` but the OJ Art. 9(4)(b) text is
    about network and infrastructure management structure, not
    patching. The Executor preserves OJ-literal locus at network
    management. A contrasting reading would treat the segmentation
    mechanism as the dominant expected control and read `may
    include` as a quasi-mandatory listing (R2), but the literal OJ
    construction makes the listing illustrative. An open question is
    whether the EBA Guidelines + ESAs Joint Committee output under
    Art. 15(2) will harden `may include` into a measurable
    segmentation expectation, de facto converting it from R1 to R2.
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
- sr_id: SR-DORA-008
  title: "Multi-modality resilience testing programme as framework component"
  source_clauses:
    - { clause_id: DORA-C32, article_ref: "Art. 24(1) — `establish, maintain and review a sound and comprehensive digital operational resilience testing programme as an integral part of the ICT risk-management framework`" }
    - { clause_id: DORA-C33, article_ref: "Art. 25(1) — testing modalities portfolio (12-way open list)" }
  linked_objectives: [SO-DORA-005]
  sub_domain: [D-10.3, D-02.4]
  nist_csf_mapping:
    - { id: GV.OV-02, title: "The organizational cybersecurity risk management strategy is reviewed and adjusted to address changes in the organization's risk landscape" }
    - { id: ID.RA-01, title: "Vulnerabilities in assets are identified, validated, and recorded" }
    - { id: PR.PS-06, title: "Secure software development practices are integrated, and their performance is monitored throughout the SDLC" }
  applies_to_role: [FINANCIAL_ENTITY]
  obligation_type: [CONTINUOUS, PERIODIC]
  regulatory_rationale: |
    Art. 24(1) requires financial entities to establish, maintain and
    review a sound and comprehensive digital operational resilience
    testing programme as an integral part of the ICT risk-management
    framework. Art. 25(1) operationalises this through a portfolio of
    testing modalities — vulnerability assessments, scans, open source
    analyses, network security assessments, gap analyses, physical
    security reviews, questionnaires, source code reviews where
    feasible, scenario-based tests, compatibility testing, performance
    testing, end-to-end testing and penetration testing. Chapter IV
    is dedicated to the testing programme, with Art. 26 (TLPT) and
    Art. 27 (advanced testing for significant entities) imposing
    higher-tier obligations alongside Art. 24–25 baseline (NIS 2
    Art. 21(2)(f) on basic cyber-hygiene and policy review imposes
    a parallel periodic-test expectation on NSIEs that DORA NSIEs
    retain as joint obligation). The Art. 24(7) RTS mandate is the
    principal pending source of measurability for the `sound and
    comprehensive` qualifier.
    [OJ-corrective note (v0.2 audit, material): Art. 25(1) — 12 OJ items miscounted (split + omission). OJ Art. 25(1) lists 12 comma-separated testing modalities: (1) vulnerability assessments and scans, (2) open source analyses, (3) network security assessments, (4) gap analyses, (5) physical security reviews, (6) questionnaires and scanning software solutions, (7) source code reviews where feasible, (8) scenario-based tests, (9) compatibility testing, (10) performance testing, (11) end-to-end testing, (12) penetration testing. The SR splits chunk #1 into 2 items and omits `scanning software solutions` from chunk #6.]
  security_rationale: |
    The obligation in Art. 24(1)/Art. 25(1) for a sound and
    comprehensive digital operational resilience testing programme is
    operationalised in NIST CSF 2.0 through **GV.OV-02 (The
    organizational cybersecurity risk management strategy is reviewed
    and adjusted to address changes in the organization's risk
    landscape)**, **ID.RA-01 (Vulnerabilities in assets are
    identified, validated, and recorded)**, and **PR.PS-06 (Secure
    software development practices are integrated, and their
    performance is monitored throughout the SDLC)**. GV.OV-02 anchors
    the testing programme as a strategic-review instrument whose
    findings must feed strategy adjustment, ensuring the programme
    is integral to the framework rather than parallel. ID.RA-01
    supplies the validated vulnerability substrate that the twelve-
    modality portfolio in Art. 25(1) — vulnerability assessments,
    scans, source-code reviews, scenario tests, penetration testing —
    operationalises into concrete testing outputs traceable to known
    vulnerabilities. PR.PS-06 closes the SDLC dimension by ensuring
    secure-development controls are themselves tested rather than
    assumed, completing the modality coverage on the
    application-layer side. The OJ `sound and comprehensive`
    qualifier is delivered by the multi-modality coverage plus
    strategic-feedback loop. The accountability link under Art. 5(2):
    the testing-programme charter, modality-coverage matrix,
    test-execution records, and findings-to-strategy-adjustment logs
    produce the documented evidence trail the management body can
    present to competent authorities demonstrating that resilience
    testing is structurally embedded and strategy-influencing rather
    than incident-driven.
  ambiguity_notes: |
    Source clause DORA-C32 carries S2 on `sound` and `comprehensive`
    (VAG), S2 on `testing programme` (POLY — single programme vs.
    portfolio of tests), and S2 on `establish, maintain AND review`
    (COORD 3-way verb coordination; reading chosen: R1 all three
    activities required). DORA-C33 carries S3 on the 12-way open
    list (`such as` pattern, COORD S3 — the `such as` softens the
    list to illustrative; reading chosen: R2 illustrative-with-
    floor — the entity selects from the list appropriate to its
    risk profile, with the modalities collectively covering the
    ICT-system attack surface). `where feasible` (VAG S2) — R1
    technically achievable / R2 cost-effective / R3 either; R3
    literal. The dominance of `R2 illustrative-with-floor` over
    pure-illustrative reflects the supervisory expectation that an
    entity running none of the twelve modalities would fail to
    establish a `sound and comprehensive` testing programme. A
    contrasting reading treats the `such as` clause as strictly
    illustrative with no floor, leaving the entity entirely free
    to select any testing modalities; this reading is consistent
    with the OJ literal text but inconsistent with the supervisory
    expectation in EBA Guidelines on ICT and security risk
    management §208–§212. A third constructed reading would impose
    all twelve modalities as an enumerated floor — supported by
    the structural formality of the twelve-item list in OJ but
    unsupported by the `such as` pattern's softening language. The
    Art. 24(7) RTS mandate is pending and may close the modality-
    selection question. Remain open: (a) whether the ESAs Joint
    Committee RTS under Art. 24(7) will impose a quantified
    baseline-modality floor for specific entity classes; (b) whether
    `where feasible` will be interpreted by supervisory practice as
    R1 (technically achievable) or R2 (cost-effective), with the
    distinction materially affecting the supervisory treatment of
    closed-source third-party components.
```

### SO-DORA-001 (CIA + A maintained across data states)

```yaml
- sr_id: SR-DORA-010
  title: "Least-privilege physical and logical access governance"
  source_clauses:
    - { clause_id: DORA-C14, article_ref: "Art. 9(4)(c) — `implement policies that limit the physical or logical access to information assets and ICT assets to what is required for legitimate and approved functions and activities only`" }
  linked_objectives: [SO-DORA-006]
  sub_domain: [D-03.3]
  nist_csf_mapping:
    - { id: PR.AA-05, title: "Access permissions, entitlements, and authorizations are defined and managed in accordance with the principle of least privilege" }
    - { id: PR.AA-06, title: "Access to physical and logical assets is limited to authorized users, services, and hardware" }
  applies_to_role: [FINANCIAL_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 9(4)(c) requires financial entities to implement policies that
    limit physical or logical access to information assets and ICT
    assets to what is required for legitimate and approved functions
    and activities only. This sits within Art. 9(4) chapeau and is
    one of eight mandatory control categories (NIS 2 Art. 21(2)(d)
    on cryptography and (e) on access control impose parallel
    obligations on NSIEs outside DORA). The OJ text is markedly
    careful: the limiting phrase `what is required for legitimate
    and approved functions and activities only` carries the entire
    substantive burden of the rule, with `only` properly placed
    before the limiting phrase to avoid ambiguity (Berry §5.3.1
    faithfully reproduces this placement). Recital 53 supplies
    the principle-aligned framing without introducing normative
    additionality.
  security_rationale: |
    The obligation in Art. 9(4)(c) for least-privilege physical and
    logical access is operationalised in NIST CSF 2.0 through
    **PR.AA-05 (Access permissions, entitlements, and authorizations
    are defined and managed in accordance with the principle of
    least privilege)** and **PR.AA-06 (Access to physical and
    logical assets is limited to authorized users, services, and
    hardware)**. PR.AA-05 establishes the permission-tier discipline:
    function-aligned entitlements, role-based and attribute-based
    access control, just-in-time elevation with documented business
    justification, separation-of-duties enforcement on payment-
    authorisation workflows, and privileged-access management with
    session recording. PR.AA-06 enforces the physical-and-logical
    twin layer — badge access, mantrap entry, secure-room zoning,
    and CCTV coverage complementing logical controls — preventing
    physical-bypass of logical controls that an attacker can otherwise
    use to circumvent authentication entirely. The OJ `legitimate
    AND approved` two-axis gating (function-aligned AND governance-
    approved) is operationalised through PR.AA-05's documented
    entitlement rationales and PR.AA-06's access-request approval
    workflows with multi-party authorisation for privileged grants.
    The accountability link under Art. 5(2): the entitlement
    inventory, access-review records, separation-of-duties
    attestation logs, and physical-access audit trails produce the
    documented evidence trail the management body can present to
    competent authorities demonstrating that access governance is
    dual-axis-gated and continuously enforced across both access
    modalities.
  ambiguity_notes: |
    Source clause DORA-C14 carries S2 on `physical or logical` (POLY
    — distinct access modes coordinated by OR; reading chosen: R1
    both required, distinct instruments for physical and logical
    access), S2 on `legitimate AND approved` (COORD — both qualifiers
    required; R1 literal), and S2 on the `only` qualifier (Berry §5.3.1
    — correctly placed before the limiting phrase). **T4-vs-text
    gap:** T4 unpacks DORA-C14 as `need-to-know and least privilege`.
    **The OJ text contains neither `need-to-know` nor `least
    privilege`** — these are imported from ISO 27001 interpretation.
    The Executor preserves OJ-literal language (`what is required for
    legitimate and approved functions and activities only`) and maps
    to PR.AA-05 (least privilege) by meaning-alignment without
    importing non-OJ vocabulary. A contrasting reading would treat
    `physical or logical` as an alternative (either suffices), but
    the structural-protective objective of the provision requires
    both layers to be governed because physical-access bypasses of
    logical controls are an established threat vector. An open
    question is whether supervisory expectations will progressively
    harden `legitimate and approved` into formal need-to-know
    registries.
```

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
- sr_id: SR-DORA-019
  title: "ICT third-party risk managed under four-factor proportionality"
  source_clauses:
    - { clause_id: DORA-C35, article_ref: "Art. 28(1) — `manage ICT third-party risk … taking into account: (i) the nature, scale, complexity and importance of ICT-related dependencies; (ii) the risks arising from contractual arrangements on the use of ICT services … taking into account the criticality or importance of the respective service, process or function`" }
  linked_objectives: [SO-DORA-011]
  sub_domain: [D-06.1, D-06.3]
  nist_csf_mapping:
    - { id: GV.SC-02, title: "Suppliers and other third parties are known, prioritized, and assessed using a cybersecurity supply chain risk management process" }
    - { id: ID.AM-04, title: "Inventories of suppliers and other third parties (e.g., vendors, partners, service providers) are maintained" }
  applies_to_role: [FINANCIAL_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 28(1) requires financial entities to manage ICT third-party risk while
    taking into account (i) the nature, scale, complexity and importance of
    ICT-related dependencies and (ii) the risks arising from contractual
    arrangements on the use of ICT services, including the criticality or
    importance of the respective service, process or function. The clause is
    the foundational third-party risk-governance rule, with the contractual
    minimum elements at Art. 30(1)–(2) and audit rights at Art. 30(3)(e)
    operationalising it. The regime parallels — but does not replace — GDPR
    Art. 28 processor controls and NIS 2 Art. 21 supply-chain security duties
    (Directive (EU) 2022/2555). The EBA Guidelines on outsourcing arrangements
    provide the dominant EU supervisory baseline where the underlying service is
    outsourcing, including proportionality assessment under Art. 4.
  security_rationale: |
    The Art. 28(1) ICT third-party risk-management duty is operationalised in
    NIST CSF 2.0 through **GV.SC-02 (Suppliers and other third parties are
    known, prioritized, and assessed using a cybersecurity supply chain risk
    management process)** and **ID.AM-04 (Inventories of suppliers and other
    third parties (e.g., vendors, partners, service providers) are maintained)**.
    GV.SC-02 supplies the prioritisation and assessment engine that the
    four-factor proportionality clause demands: suppliers are not treated
    uniformly but stratified by nature, scale, complexity, and importance of
    their ICT-supported dependency, and assessed using a documented supply-
    chain risk-management process that aligns with EBA Guidelines on
    outsourcing arrangements. ID.AM-04 anchors the upstream inventory that
    GV.SC-02 cannot operate without — the proportionality judgement under
    Art. 28(1)(i)+(ii) is only as defensible as the inventory on which it is
    computed. Together these two subcategories ensure that the financial
    entity maintains an evidence-backed picture of every third-party
    dependency and applies a documented prioritisation framework, allowing
    ex-post demonstration to the competent authority that the Art. 28(1)
    four-factor proportionality assessment was grounded in an actual
    supplier inventory rather than ad-hoc case-by-case reasoning.
  ambiguity_notes: |
    S2 COORD on `nature, scale, complexity AND importance` — read as cumulative,
    all four factors inform the risk assessment. S2 COORD on
    `service, process OR function` — read as cumulative, all three artefacts in
    scope. S2 POLY on `critical or important functions` — the undefined
    distinction propagates to 18 of 38 DORA clauses per `../Regulation/DORA/Ambiguity/05_DORA.md` §3.4;
    the chosen reading is that both categories are in scope and that distinct
    obligations may attach to each (DORA RTS may eventually fix the distinction
    but as of the OJ text it is open). Remain open: how to operationalise the
    OR-coordination between `critical` and `important` remains a documented
    entity-policy matter awaiting EBA RTS clarity.
```

### SO-DORA-001 (CIA + A maintained across data states)

```yaml
- sr_id: SR-DORA-023
  title: "ICT change management under six-step risk-based process"
  source_clauses:
    - { clause_id: DORA-C18, article_ref: "Art. 9(4)(e) — `implement documented policies, procedures and controls for ICT change management, including changes to software, hardware, firmware components, systems or security parameters … that are based on a risk assessment approach … in order to ensure that all changes to ICT systems are recorded, tested, assessed, approved, implemented and verified in a controlled manner`" }
  linked_objectives: [SO-DORA-013]
  sub_domain: [D-07.4]
  nist_csf_mapping:
    - { id: PR.PS-01, title: "Configuration management practices are established, documented, and applied to assets" }
    - { id: PR.PS-02, title: "Software is maintained, replaced, and removed commensurate with risk" }
    - { id: PR.PS-06, title: "Secure software development practices are integrated, and their performance is monitored throughout the SDLC" }
  applies_to_role: [FINANCIAL_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 9(4)(e) requires financial entities to implement documented policies,
    procedures, and controls for ICT change management, including changes to
    software, hardware, firmware components, systems, or security parameters,
    based on a risk-assessment approach, so that all changes to ICT systems are
    recorded, tested, assessed, approved, implemented, and verified in a
    controlled manner. The clause sits in the ICT-risk-management-framework
    core of Chapter II Section 2 (per `02b_DORA_Ch2Sec2_Framework.md`) and is
    the operational hinge of the protection-prevention architecture. It runs
    alongside CRA Art. 13 conformity-assessment obligations for ICT products
    (Regulation (EU) 2024/2847) where the changed component is a digital
    product, and alongside NIS 2 Art. 21(2)(e) basic security vulnerability-
    handling duties (Directive (EU) 2022/2555). EBA Guidelines on ICT and
    security risk management provide the supervisory baseline for the
    risk-assessment approach.
  security_rationale: |
    The Art. 9(4)(e) change-management duty is operationalised in NIST CSF
    2.0 through **PR.PS-01 (Configuration management practices are
    established, documented, and applied to assets)**, **PR.PS-02 (Software
    is maintained, replaced, and removed commensurate with risk)**, and
    **PR.PS-06 (Secure software development practices are integrated, and
    their performance is monitored throughout the SDLC)**. PR.PS-01 anchors
    the documented-policy substrate — golden baselines, drift detection,
    configuration-as-code — that operationalises the `controlled manner`
    qualifier across the five change-target categories (software, hardware,
    firmware, systems, security parameters). PR.PS-02 supplies the
    commensurate-with-risk axis that the OJ `risk assessment approach`
    demands, ensuring that change decisions are weighted by impact and
    likelihood rather than treated uniformly. PR.PS-06 closes the SDLC
    integration loop, ensuring that the `tested, assessed, approved`
    stages of the six-step process tie back to secure-development practices
    upstream and to verified-deployment evidence downstream. Together
    these three subcategories convert a paper change-approval workflow into
    an evidence-backed governance discipline covering the full change-
    target surface, and an entity documenting PR.PS-01 + PR.PS-02 +
    PR.PS-06 coverage can demonstrate ex-post to supervisory review
    that the Art. 9(4)(e) six-step process — recorded, tested, assessed,
    approved, implemented, verified — was anchored in platform-security
    configuration practice and proportionate to risk across the SDLC.
  ambiguity_notes: |
    S3 COORD on the five-way OR of change-targets (`software, hardware,
    firmware components, systems OR security parameters`) is read as all five
    categories in scope. S3 COORD on the six-way AND of change-management steps
    (`recorded, tested, assessed, approved, implemented AND verified`) is read
    as cumulative — all six steps required; partial-process compliance is
    non-compliance. S2 VAG on `controlled manner` is read as the combination
    of documented procedure and segregated approval at the literal end of the
    spectrum. S2 POLY on `change management` — distinct from release
    management and configuration management in industry usage; the chosen
    reading keeps the OJ-literal locus at change management proper. Open
    question: how to evidence `tested` in the context of emergency changes
    remains a documented-entity-policy matter awaiting accumulated supervisory
    practice.
```

### SO-DORA-001 (CIA + A maintained across data states)

```yaml
- sr_id: SR-DORA-025
  title: "Compulsory ICT security awareness and resilience training for staff"
  source_clauses:
    - { clause_id: DORA-C27, article_ref: "Art. 13(6) — `ICT security awareness programmes and digital operational resilience training as compulsory modules in their staff training schemes`" }
    - { clause_id: DORA-C28, article_ref: "Art. 13(6) same locus — `level of complexity commensurate to the remit of their functions`" }
    - { clause_id: DORA-C26, article_ref: "Art. 13(6) same locus — T4 mapping mismatch per `../Regulation/DORA/Ambiguity/05_DORA.md` §2.26" }
  linked_objectives: [SO-DORA-015]
  sub_domain: [D-08.1, D-08.2]
  nist_csf_mapping:
    - { id: PR.AT-01, title: "All users are informed and trained on cybersecurity topics (e.g., recognition of phishing, social engineering, and other relevant risks)" }
    - { id: PR.AT-02, title: "All members of the organization's workforce understand their roles and responsibilities in achieving the organization's cybersecurity objectives" }
  applies_to_role: [FINANCIAL_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 13(6) requires financial entities to develop ICT security awareness
    programmes and digital operational resilience training as compulsory
    modules in their staff training schemes, with a level of complexity
    commensurate to the remit of staff functions. The clause is the workforce-
    scale counterpart to Art. 5(4) management-body training (governance track)
    and to the digital operational resilience testing duty at Chapter IV. The
    clause co-exists with GDPR Art. 39 staff-awareness duties for personal-
    data processing (Regulation (EU) 2016/679) and with NIS 2 Art. 21(2)(g)
    basic security training baselines (Directive (EU) 2022/2555). EBA
    Guidelines on ICT and security risk management set out the supervisory
    expectation on calibration, and AI Act Art. 4(2) provider-deployer
    literacy duties (Regulation (EU) 2024/1689) intersect where AI systems
    are in scope of the same staff training schemes.
  security_rationale: |
    The Art. 13(6) workforce training duty is operationalised in NIST CSF
    2.0 through **PR.AT-01 (All users are informed and trained on cybersecurity
    topics (e.g., recognition of phishing, social engineering, and other
    relevant risks))** and **PR.AT-02 (All members of the organization's
    workforce understand their roles and responsibilities in achieving the
    organization's cybersecurity objectives)**. PR.AT-01 anchors the baseline
    awareness layer that closes the human-factor gap — phishing recognition,
    social-engineering resistance, password hygiene, incident-reporting
    reflexes — and converts the OJ `ICT security awareness programmes` from
    an opt-in continuing-professional-development activity into a compulsory
    training-module floor across the workforce. PR.AT-02 layers the role-
    specific depth dimension that the OJ `commensurate to the remit of
    their functions` qualifier demands, ensuring that staff in
    security-critical roles (incident response, ICT operations, fraud
    investigation, third-party governance) receive calibrated depth rather
    than a uniform baseline. Together these two subcategories operationalise
    both the `compulsory` and the `commensurate` axes of Art. 13(6), and
    an entity evidencing PR.AT-01 coverage plus PR.AT-02 role-calibrated
    depth can demonstrate ex-post to supervisory review that the Art. 13(6)
    workforce-training obligation was met at both the universal-awareness
    floor and the role-specific depth required by the staff function
    taxonomy, and that completion thresholds were documented as a
    condition of employment rather than as optional professional
    development.
  ambiguity_notes: |
    S2 VAG on `compulsory` is read as completion-mandatory (not mere
    attendance). S2 COORD on `programmes, training, modules` is read
    cumulatively as three artefact types used interchangeably. S2 VAG on
    `level of complexity commensurate to the remit of their functions` is
    read as function-specific calibration per the OJ literal formulation.
    T4-vs-text gap (per `../Regulation/DORA/Ambiguity/05_DORA.md` §2.26): T4 maps DORA-C26 to D-02.2
    `Patch Management & Updates` with description `Learning and evolving:
    post-incident reviews; incorporate findings into patching and update
    processes`, while the OJ Art. 13(6) text is about training programmes
    only — post-incident reviews live in Art. 13(2) and patching lives in
    Art. 9(4)(f). The Executor keeps the OJ-literal locus at D-08.1/D-08.2.
    T4-vs-text gap on DORA-C28: T4 reads `role-specific training` while the
    OJ Art. 13(6) uses only `commensurate to the remit of their functions`.
    Remain open: demonstration thresholds (completion percentages,
    assessment-pass thresholds) for `compulsory` are an entity-policy
    matter awaiting industry convergence.
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

### SO-DORA-001 (CIA + A maintained across data states)

```yaml
- sr_id: SR-DORA-031
  title: "Information security policy covering CIA+A across data and ICT assets"
  source_clauses:
    - { clause_id: DORA-C12, article_ref: "Art. 9(4)(a) — `develop and document an information security policy defining rules to protect the availability, authenticity, integrity and confidentiality of data, information assets and ICT assets, including those of their customers, where applicable`" }
  linked_objectives: [SO-DORA-018]
  sub_domain: [D-10.2]
  nist_csf_mapping:
    - { id: GV.PO-01, title: "Organizational cybersecurity policy is established, communicated, and enforced" }
    - { id: PR.DS-12, title: "Data is managed consistent with the organization's risk strategy to protect the confidentiality, integrity, and availability of data" }
    - { id: GV.OC-03, title: "Legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed" }
  applies_to_role: [FINANCIAL_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 9(4)(a) requires financial entities to develop and document an
    information security policy defining rules to protect the availability,
    authenticity, integrity, and confidentiality of data, information assets,
    and ICT assets, including those of their customers, where applicable. The
    clause is the top-level policy instrument complementing the framework at
    Art. 6(1) and the operational polices at Art. 9(4)(b)–(j). The clause
    co-exists with GDPR Art. 5 principles relating to processing of personal
    data (Regulation (EU) 2016/679), with NIS 2 Art. 21(2)(d) baseline-
    cryptography-policy duty (Directive (EU) 2022/2555), and with CRA
    conformity-of-products duties (Regulation (EU) 2024/2847) where the
    policy covers protection of digital products. EBA Guidelines on ICT and
    security risk management set the supervisory expectations on policy
    documentation and review cadence.
  security_rationale: |
    The Art. 9(4)(a) information-security-policy duty is operationalised in
    NIST CSF 2.0 through **GV.PO-01 (Organizational cybersecurity policy is
    established, communicated, and enforced)**, **PR.DS-12 (Data is managed
    consistent with the organization's risk strategy to protect the
    confidentiality, integrity, and availability of data)**, and **GV.OC-03
    (Legal, regulatory, and contractual requirements regarding cybersecurity
    — including privacy and civil liberties obligations — are understood
    and managed)**. GV.PO-01 anchors the policy-substrate dimension — the
    OJ `develop and document an information security policy` requirement is
    operationalised as an established, communicated, and enforced policy
    rather than as an aspirational artefact. PR.DS-12 layers the data-
    management axis, ensuring that the OJ `availability, authenticity,
    integrity and confidentiality` four-way protection objective is
    translated into a risk-strategy-aligned data-governance regime
    covering data, information assets, and ICT assets (including
    customer-owned assets where applicable). GV.OC-03 closes the
    legal-regulatory-contractual alignment loop, ensuring that the
    policy accounts for parallel GDPR, NIS 2, CRA, and contractual
    obligations rather than operating as an isolated DORA artefact.
    Together these three subcategories convert the top-level policy
    requirement into an enforceable, risk-strategy-aligned, and
    multi-regulation-aware instrument, and an entity evidencing
    GV.PO-01 + PR.DS-12 + GV.OC-03 coverage can demonstrate ex-post
    to supervisory review that the Art. 9(4)(a) `develop and document`
    obligation was met through established-policy discipline, risk-
    strategy alignment, and legal-regulatory mapping — closing the
    common gap where information-security policies exist as
    documents but not as enforceable instruments.
  ambiguity_notes: |
    S2 COORD on the nested AND (CIA+A four-way of data/information assets/
    ICT assets three-way = twelve pairings) is read as all twelve pairings in
    scope. S2 VAG on `where applicable` is read at the risk-based end of the
    spectrum per recital context; alternatives include entity-judgment or
    contractually-determined scoping. S2 POLY on `information security policy`
    is read as a policy framework rather than a single document given the
    rule-definition scope. Remain open: `where applicable` evidence
    standard (when applicable applies and when it does not) is an entity-
    policy matter.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

