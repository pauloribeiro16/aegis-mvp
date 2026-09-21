---
document_id: AEGIS-PREPROC-DORA-ART-6
title: DORA Art. 6 — SecurityObjectives & SecurityRules
regulation: DORA
article: Art. 6
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
  - ../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.1.md
  - ../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.1.md
  - ../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.2.md
  - ../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.2.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.2.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.2.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.1.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.1.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.2.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.2.md
status: DRAFT
---

# DORA Art. 6

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-DORA-016 | The management body defines, approves, oversees and is responsible for the implementation of all arrangements related to the ICT risk management framework, supported by a sound, comprehensive and well-documented framework that enables the entity to address ICT risk quickly, efficiently and comprehensively. | `DORA-C01` (Art. 5(2) four-verb coordination: define/approve/oversee/be responsible + `all arrangements`); `DORA-C03` (Art. 6(1) `sound, comprehensive and well-documented` + `quickly, efficiently and comprehensively`) | D-09.1, D-09.3 |
| SO-DORA-016 | D-09.1, D-09.3 | Art. 5(2) + Art. 6(1) | Management body responsibility + ICT risk management framework |
| SO-DORA-017 | Responsibility for managing and overseeing ICT risk is assigned to a control function with an appropriate level of independence according to the three lines of defence model (or an internal risk management and control model); ICT supported business functions, roles and responsibilities, the information assets and ICT assets supporting those functions, and their roles and dependencies in relation to ICT risk are identified, classified and adequately documented. | `DORA-C04` (Art. 6(4) `appropriate level of independence` + `three lines of defence model`); `DORA-C05` (Art. 7(1) `identify, classify and adequately document` 3-verb + long AND chain of asset classes) | D-09.1, D-09.2, D-09.3 |
| SO-DORA-017 | D-09.1, D-09.2, D-09.3 | Art. 6(4) + Art. 7(1) | Three lines of defence + asset identification/classification |

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
- sr_id: SR-DORA-002
  title: "Strong authentication and cryptographic-key protection baseline"
  source_clauses:
    - { clause_id: DORA-C15, article_ref: "Art. 9(4)(d) — strong authentication mechanisms based on relevant standards and dedicated control systems" }
    - { clause_id: DORA-C16, article_ref: "Art. 9(4)(d) same locus — T4 reads `Multi-Factor Authentication`; OJ says `strong authentication mechanisms`" }
    - { clause_id: DORA-C17, article_ref: "Art. 9(4)(d) same locus — `protection measures of cryptographic keys`" }
  linked_objectives: [SO-DORA-002]
  sub_domain: [D-01.3, D-03.1, D-03.2]
  nist_csf_mapping:
    - { id: PR.AA-03, title: "Users, services, and hardware are authenticated" }
    - { id: PR.AA-04, title: "Identity assertions are managed, protected, and conveyed in a manner that verifies authenticity" }
  applies_to_role: [FINANCIAL_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 9(4)(d) requires financial entities to implement policies and
    protocols for strong authentication mechanisms, based on relevant
    standards and dedicated control systems, and protection measures of
    cryptographic keys whereby data is encrypted based on results of
    approved data classification and ICT risk assessment processes.
    This sub-paragraph forms part of the eight-item control list in
    Art. 9(4) (a)–(h), each item self-implementing under the Art. 6(8)
    chapeau framework, with the Art. 15 ESAs RTS mandate expected to
    specify further the `relevant standards` against which the OJ text
    remains directionless (Recital 53 frames authentication strength
    in terms of contemporary best practice and recognised standards).
    The two cited phrases sit in coordinated conjunction with the
    preceding encryption obligation: `protection measures of
    cryptographic keys whereby data is encrypted` makes the
    protection-measure layer substantively dependent on a data
    classification and ICT risk assessment result. The EBA Guidelines
    on ICT and security risk management §145–§148 specify the
    supervisory expectation that financial entities operate
    authentication mechanisms aligned with NIST SP 800-63 or
    equivalent, and that cryptographic keys be managed under ISO/IEC
    27001 Annex A.10 or successor.
  security_rationale: |
    The obligation in Art. 9(4)(d) for strong authentication and
    cryptographic-key protection is operationalised in NIST CSF 2.0
    through **PR.AA-03 (Users, services, and hardware are
    authenticated)** and **PR.AA-04 (Identity assertions are managed,
    protected, and conveyed in a manner that verifies authenticity)**.
    PR.AA-03 covers human and machine identities through NIST SP 800-63B
    AAL2/AAL3-aligned authenticators — FIDO2/WebAuthn for phishing-
    resistance, smartcard and PKI for privileged users, certificate-
    based authentication in service-to-service flows — with strength
    calibrated to risk-tier under Art. 4 proportionality. PR.AA-04
    enforces the integrity of identity-assertion conveyance via signed
    federated-identity tokens, mutual transport authentication, and PKI chain-of-trust, preventing
    assertion tampering, replay, and cross-context token reuse that
    dominate modern federation attacks. The two subcategories jointly
    close the credential-compromise attack surface that dominates
    financial-entity breach statistics. The accountability link under
    Art. 5(2): PR.AA-03 and PR.AA-04 outputs — authenticator-inventory
    registers, AAL-mapping documentation, PKI chain-of-trust audit
    logs, and identity-provider assurance records — produce the
    documented evidence trail that the management body can present to
    competent authorities to demonstrate that strong-authentication and
    key-protection obligations are continuously enforced across human,
    service-to-service, and machine identities.
  ambiguity_notes: |
    Source clause DORA-C15 carries S3 on `strong authentication` (VAG
    — no defined strength benchmark; reading chosen: R4 mechanism-
    agnostic, the OJ does not specify), S3 on `relevant standards`
    (VAG — POLY with `information security standards` of C36; no
    specific standard is named), and S3 on the three-control AND
    (COORD — `strong auth` AND `key protection` AND `encryption`;
    reading chosen: R1 all three required). **T4-vs-text gap:** T4
    maps DORA-C16 to `Multi-Factor Authentication` but the OJ
    Art. 9(4)(d) text contains only `strong authentication
    mechanisms`. The dominant EBA Guidelines reading is MFA;
    alternative readings include hardware-token-only or other
    `strong` mechanisms (e.g. certificate-based authentication in
    service-to-service contexts). Reading chosen: R5 mechanism-
    agnostic with R3 MFA as the dominant EU supervisory reading. The
    mechanism-agnostic fallback reading treats `strong authentication`
    as a category that admits hardware-tokens, certificate-based
    authentication in machine-to-machine flows, FIDO2/WebAuthn-based
    phishing-resistant authentication, and other contemporary
    authentication primitives whose `strength` claim can be
    substantiated. The MFA-as-default reading is the supervisory
    minimum that meets the EBA Guidelines' expectation but is
    vulnerable to under-specification for service-to-service flows
    where MFA in the human sense is structurally inapplicable. A
    third constructed reading would impose MFA uniformly across all
    authentication events including service-to-service, which the OJ
    text does not require and which is operationally unrealistic. The
    `relevant standards` term inherits the broader POLY with C36
    `information security standards`, and the Art. 15 ESAs RTS is
    expected to give content to that POLY through concrete standards
    references. Remain open: (a) whether the ESAs Joint Committee RTS
    under Art. 15(2) will name specific authentication-strength
    standards (e.g. ENISA-baseline, NIST SP 800-63B) and close the
    S3 VAG on `strong`; (b) whether service-account authentication in
    M2M flows will require comparable treatment to user authentication
    or be carved out as a separate sub-regime.
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

