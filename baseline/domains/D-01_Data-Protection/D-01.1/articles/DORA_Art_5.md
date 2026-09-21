---
document_id: AEGIS-PREPROC-DORA-ART-5
title: DORA Art. 5 — SecurityObjectives & SecurityRules
regulation: DORA
article: Art. 5
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
  - ../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.1.md
  - ../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.1.md
  - ../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.2.md
  - ../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.2.md
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
  - ../../CrossRegulation/DomainAnalysis/D-07_Secure-Development/D-07.1.md
  - ../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.1.md
  - ../../CrossRegulation/DomainAnalysis/D-08_Human-Factors/D-08.1.md
  - ../../CrossRegulation/DeepAnalysis/D-08_Human-Factors/D-08.1.md
  - ../../CrossRegulation/DomainAnalysis/D-08_Human-Factors/D-08.2.md
  - ../../CrossRegulation/DeepAnalysis/D-08_Human-Factors/D-08.2.md
  - ../../CrossRegulation/DomainAnalysis/D-08_Human-Factors/D-08.3.md
  - ../../CrossRegulation/DeepAnalysis/D-08_Human-Factors/D-08.3.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.2.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.2.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.1.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.1.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.2.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.2.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.3.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.3.md
status: DRAFT
---

# DORA Art. 5

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-DORA-014 | Members of the management body actively keep up to date with sufficient knowledge and skills, including by following specific training on a regular basis, commensurate to the ICT risk being managed. | `DORA-C02` (Art. 5(4) `sufficient knowledge and skills` + `regular basis` + `commensurate to the ICT risk`) | D-08.3 |
| SO-DORA-014 | D-08.3 | Art. 5(4) | Management body training and knowledge |
| SO-DORA-016 | The management body defines, approves, oversees and is responsible for the implementation of all arrangements related to the ICT risk management framework, supported by a sound, comprehensive and well-documented framework that enables the entity to address ICT risk quickly, efficiently and comprehensively. | `DORA-C01` (Art. 5(2) four-verb coordination: define/approve/oversee/be responsible + `all arrangements`); `DORA-C03` (Art. 6(1) `sound, comprehensive and well-documented` + `quickly, efficiently and comprehensively`) | D-09.1, D-09.3 |
| SO-DORA-016 | D-09.1, D-09.3 | Art. 5(2) + Art. 6(1) | Management body responsibility + ICT risk management framework |

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
- sr_id: SR-DORA-009
  title: "Threat-led penetration testing on triennial supervisory cycle"
  source_clauses:
    - { clause_id: DORA-C34, article_ref: "Art. 26(1) — `shall carry out at least every 3 years advanced testing by means of TLPT`" }
  linked_objectives: [SO-DORA-005]
  sub_domain: [D-02.4]
  nist_csf_mapping:
    - { id: ID.RA-01, title: "Vulnerabilities in assets are identified, validated, and recorded" }
    - { id: ID.RA-04, title: "Potential impacts and likelihoods of threats exploiting vulnerabilities are identified, recorded, and prioritized" }
  applies_to_role: [FINANCIAL_ENTITY]
  obligation_type: [PERIODIC]
  regulatory_rationale: |
    Art. 26(1) requires financial entities to carry out at least every
    3 years advanced testing by means of TLPT. The competent authority
    may, where necessary, request a reduction or increase in this
    frequency based on the entity's risk profile and operational
    circumstances. The provision sits inside Chapter IV with scope
    limitations dependent on entity significance (Art. 26(8)–(11)):
    the TLPT obligation applies to entities identified as significant
    under Art. 26(8) on the basis of size, interconnectedness,
    complexity, and risk profile. Art. 26(11) defines TLPT by
    reference to the TIBER-EU framework or equivalent, which
    incorporates ISO/IEC 33069 and threat-intelligence-led
    methodology (cf. ESAs Joint Committee TIBER-EU Knowledge Hub).
    Recital 65 sets the policy rationale: TLPT bridges the gap
    between compliance-driven testing and real-world adversarial
    capability.
  security_rationale: |
    The obligation in Art. 26(1) for threat-led penetration testing
    on a triennial cycle is operationalised in NIST CSF 2.0 through
    **ID.RA-01 (Vulnerabilities in assets are identified, validated,
    and recorded)** and **ID.RA-04 (Potential impacts and likelihoods
    of threats exploiting vulnerabilities are identified, recorded,
    and prioritized)**. ID.RA-01 supplies the validated-vulnerability
    substrate that TLPT exercises: identified vulnerabilities are re-
    tested under adversarial conditions to verify remediation efficacy
    and detect regression. ID.RA-04 supplies the threat-likelihood-
    impact framing that TLPT's threat-intelligence-led methodology
    depends on — TIBER-EU scenarios are constructed from current
    campaigns whose impact-likelihood must be quantified to scope
    the test realistically and prioritised so test-team effort
    targets the most consequential threat paths. The OJ `at least
    every 3 years` hard anchor maps to a supervisory-cycle rather
    than operational-cadence frame, ensuring TLPT findings are
    reviewed in light of contemporary threat-actor capability at a
    frequency aligned to strategic-risk reassessment. The
    accountability link under Art. 5(2): the TLPT charter, threat-
    scenario justifications, test-execution records, and remediation-
    traceability documentation produce the documented evidence trail
    the management body can present to competent authorities
    demonstrating that adversarial-defence verification is performed
    at supervisory-relevant cadence with documented findings-to-
    remediation closure.
  ambiguity_notes: |
    Source clause DORA-C34 carries S2 on `risk profile` (POLY —
    entity-internal vs. sectoral; R1 entity-internal literal), S2 on
    `operational circumstances` (VAG — entity-context dependent),
    and S2 on `where necessary` (VAG — CA judgment). The hard
    numeric anchor (3 years) closes the temporal ambiguity. `TLPT`
    (POLY S2) — defined by reference to the TIBER-EU framework
    (Art. 26(11) — non-binding ESA guidance); R1 TIBER-EU, R2
    equivalent framework accepted; R1 dominant. `reduce or
    increase` (COORD S2) — R1 either direction authorised; R1
    literal. The dominant TIBER-EU reading is anchored in the
    ESAs Joint Committee TIBER-EU Knowledge Hub, which converges
    on the ECB-led methodology; equivalent framework acceptance
    is contingent on competent-authority recognition (an
    AOFIRST-only entity operating in France would still satisfy
    TLPT under national recognition even without TIBER-EU
    certification). An open question remains the scope of
    `significant` under Art. 26(8): the OJ text references
    Art. 26(8) criteria but defers the operational scope
    determination to the supervisory authority.
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
- sr_id: SR-DORA-011
  title: "Multi-class anomalous activity detection with SPOF identification"
  source_clauses:
    - { clause_id: DORA-C20, article_ref: "Art. 10(1) — `mechanisms to promptly detect anomalous activities … including ICT network performance issues and ICT-related incidents, and to identify potential material single points of failure`" }
  linked_objectives: [SO-DORA-007]
  sub_domain: [D-04.1, D-10.1]
  nist_csf_mapping:
    - { id: DE.CM-01, title: "Networks and network services are monitored to find potentially adverse events" }
    - { id: DE.CM-09, title: "Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events" }
    - { id: DE.AE-02, title: "Detected events are analyzed to understand attack targets and methods" }
  applies_to_role: [FINANCIAL_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 10(1) requires financial entities to deploy mechanisms to
    promptly detect anomalous activities, in accordance with Art. 17,
    including ICT network performance issues and ICT-related incidents,
    and to identify potential material single points of failure.
    Article 10 Chapter II Section II establishes the detection
    substrate that Chapter III operationalises into the incident-
    management process. The cross-reference `in accordance with Art.
    17` ties detection to incident-management process (NIS 2 Art.
    21(2)(b) on incident-handling imposes a parallel baseline on
    NSIEs that DORA NSIEs also satisfy). Recital 54 highlights
    the dual objective: cyber-threat detection and operational-
    performance anomaly detection (the latter catching availability-
    oriented incidents that the cyber-threat lens alone would miss).
    [OJ-corrective note (v0.2 audit, cosmetic): Art. 10(1) — "deploy" vs "have in place". OJ Art. 10(1) reads: `Financial entities shall have in place mechanisms to promptly detect anomalous activities` — the operative verb is `have in place`, not `deploy`. Operatively equivalent; no operational change required.]
  security_rationale: |
    The obligation in Art. 10(1) for prompt detection of anomalous
    activities and SPOF identification is operationalised in NIST CSF
    2.0 through **DE.CM-01 (Networks and network services are monitored
    to find potentially adverse events)**, **DE.CM-09 (Computing
    hardware and software, runtime environments, and their data are
    monitored to find potentially adverse events)**, and **DE.AE-02
    (Detected events are analyzed to understand attack targets and
    methods)**. DE.CM-01 covers the network-layer detection surface —
    flow telemetry, IDS/IPS signatures, east-west traffic baselining,
    DNS-monitoring, and CTPP-traffic anomaly detection. DE.CM-09
    extends coverage to the compute-layer surface — endpoint
    detection and response, file-integrity monitoring, runtime-
    anomaly detection on transaction-processing hosts, and
    authentication-system anomaly detection. DE.AE-02 supplies the
    analysis layer that converts raw detections into understood
    attack patterns and supports SPOF identification through
    performance-anomaly correlation (latency drift, error-rate
    spikes, capacity-saturation). The OJ three-class coverage
    (network, compute, performance) maps directly onto these three
    DE subcategories, ensuring no detection blind spot. The
    accountability link under Art. 5(2): the detection-coverage
    matrix, SPOF register, and analysis-output records produce the
    documented evidence trail the management body can present to
    competent authorities demonstrating that detection is genuinely
    multi-class and SPOF-aware rather than cyber-flavour-only.
  ambiguity_notes: |
    Source clause DORA-C20 carries S2 on `promptly` (VAG — no
    specified time-to-detect; reading chosen: R3 risk-based, per
    entity risk profile), S2 on `potential material` (VAG — VAG +
    POLY combined; reading chosen: R1 reasonable-judgment-of-
    materiality), and S2 on `anomalous activities` (POLY — R1
    security anomaly / R2 performance anomaly / R3 behavioural
    anomaly; reading chosen: R3 cumulative, all three classes per
    the `including ICT network performance issues AND ICT-related
    incidents` opening). A contrasting reading of `promptly` would
    treat the term as a supervisor-imposed deterministic window
    (e.g. 24 hours), but no OJ-text support exists for a
    deterministic interpretation. An alternative reading would limit
    `anomalous activities` to cyber-security flavour only, ignoring
    the OJ qualifier `including ICT network performance issues` —
    this reading is rejected because the qualifier is in OJ text.
```

### SO-DORA-001 (CIA + A maintained across data states)

```yaml
- sr_id: SR-DORA-012
  title: "Multi-layer detection with threshold-driven response triggering"
  source_clauses:
    - { clause_id: DORA-C21, article_ref: "Art. 10(2) — `detection mechanisms … shall enable multiple layers of control, define alert thresholds and criteria to trigger and initiate ICT-related incident response processes, including automatic alert mechanisms for relevant staff in charge of ICT-related incident response`" }
  linked_objectives: [SO-DORA-007]
  sub_domain: [D-04.1, D-10.1]
  nist_csf_mapping:
    - { id: DE.CM-01, title: "Networks and network services are monitored to find potentially adverse events" }
    - { id: RS.MA-01, title: "The incident management plan is executed in coordination with relevant third parties once an incident is declared" }
  applies_to_role: [FINANCIAL_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 10(2) requires financial entities to ensure that detection
    mechanisms enable multiple layers of control, define alert
    thresholds and criteria to trigger and initiate ICT-related
    incident response processes, including automatic alert mechanisms
    for relevant staff in charge of ICT-related incident response.
    This sub-paragraph specifies the operational shape of the
    detection apparatus of Art. 10(1) — the four coordinated
    requirements (multiple layers, thresholds, trigger, automatic
    alerts) build the detection-to-response bridge (NIS 2 Art.
    21(2)(b) parallels this with NSIE-side handling, with CRA Art.
    13(6) on handled vulnerabilities as upstream fact-flow into the
    detection layer). Recital 54 frames `multiple layers` in
    defence-in-depth terms, and EBA Guidelines on ICT and security
    risk management §194 specify the supervisory expectation that
    layers include at least network-layer, compute-layer and
    application-layer detection.
  security_rationale: |
    The obligation in Art. 10(2) for multi-layer detection with
    alert thresholds and automatic response-triggering is
    operationalised in NIST CSF 2.0 through **DE.CM-01 (Networks
    and network services are monitored to find potentially adverse
    events)** and **RS.MA-01 (The incident management plan is
    executed in coordination with relevant third parties once an
    incident is declared)**. DE.CM-01 establishes the network-layer
    detection substrate whose outputs are channelled into
    threshold-driven alerting, with the OJ `multiple layers`
    requirement operationalised through complementary coverage at
    network, compute, and application layers (per EBA Guidelines
    §194 supervisory expectation). RS.MA-01 bridges detection to
    response: alert thresholds and trigger criteria operationalise
    the transition from detection to declared-incident, ensuring
    the response process initiates automatically without operator
    delay once crossing triggers fire. The four-verb OJ coordination
    `enable, define, trigger, initiate` maps cleanly onto DE.CM-01
    (enable monitoring, define thresholds) and RS.MA-01 (trigger
    declaration, initiate response execution with relevant third
    parties including CTPPs and competent authorities). The
    accountability link under Art. 5(2): the layer-coverage
    documentation, threshold-tuning records, and response-trigger
    audit logs produce the documented evidence trail the management
    body can present to competent authorities demonstrating that
    detection-to-response is mechanised, threshold-driven, and
    auditably fast rather than operator-judgement-dependent.
  ambiguity_notes: |
    Source clause DORA-C21 carries S2 on `multiple` (VAG — R1 ≥2
    layers / R2 ≥3 layers; R1 literal minimum), S2 on `relevant
    staff` (VAG — R1 incident-response team / R2 security
    operations / R3 management; R3 literal OJ), and S2 on
    `thresholds and criteria` (POLY — R1 quantitative thresholds
    / R2 qualitative criteria / R3 both; R3 literal AND). The
    four-verb coordination `enable, define, trigger, initiate`
    (S2) — reading chosen: R1 cumulative, the four verbs together
    describe the complete mechanism lifecycle. A contrasting reading
    of `multiple` would impose three or more layers (R2), aligned
    with EBA Guidelines supervisory expectation of at least three
    (network, compute, application), but the OJ literal `multiple`
    permits as few as two. An open question is whether supervisory
    guidance has the operational force to displace the OJ literal
    minimum.
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
- sr_id: SR-DORA-024
  title: "Management-body ICT-risk literacy maintained through regular training"
  source_clauses:
    - { clause_id: DORA-C02, article_ref: "Art. 5(4) — `Members of the management body … shall actively keep up to date with sufficient knowledge and skills … including by following specific training on a regular basis, commensurate to the ICT risk being managed`" }
  linked_objectives: [SO-DORA-014]
  sub_domain: [D-08.3]
  nist_csf_mapping:
    - { id: PR.AT-03, title: "All senior executives understand their roles and responsibilities in achieving the organization's cybersecurity objectives" }
    - { id: GV.RR-01, title: "Organizational leadership is responsible and accountable for cybersecurity risk and promotes a risk-aware ethical culture" }
  applies_to_role: [FINANCIAL_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 5(4) requires members of the management body of the financial entity
    to actively keep up to date with sufficient knowledge and skills to enable
    them to understand and assess ICT risk and its impact on the operations of
    the financial entity, including by following specific training on a
    regular basis, commensurate to the ICT risk being managed. The clause is
    the literacy underpinning of Art. 5(2) management-body responsibility and
    defines the personal-capacity threshold for Art. 5(2) to operate
    meaningfully. The clause co-exists with EBA Guidelines on Internal
    Governance and with the fit-and-proper frameworks (CRD Art. 91, MiFID II
    Art. 4(1)(36)/(37) cross-reference); for smaller entities under Art. 4
    proportionality, training evidence can be proportionate to risk exposure.
  security_rationale: |
    The Art. 5(4) management-body literacy duty is operationalised in NIST
    CSF 2.0 through **PR.AT-03 (All senior executives understand their roles
    and responsibilities in achieving the organization's cybersecurity
    objectives)** and **GV.RR-01 (Organizational leadership is responsible
    and accountable for cybersecurity risk and promotes a risk-aware ethical
    culture)**. PR.AT-03 anchors the training-and-knowledge component — the
    `sufficient knowledge and skills` OJ phrase operationalised as documented
    role-and-responsibility literacy, evidence of `actively keep up to date`,
    and training records calibrated to the ICT risk being managed. GV.RR-01
    layers the accountability-and-culture dimension, ensuring that the
    management body's literacy is not decorative but tied to the personal-
    capacity prerequisite for the Art. 5(2) oversight-and-liability regime
    and to the broader fit-and-proper expectations under EBA Guidelines on
    Internal Governance, CRD Art. 91, and MiFID II Art. 4(1)(36)/(37). Together
    these two subcategories close the gap between training-attendance
    evidence and demonstrable governance competence, and an entity
    evidencing PR.AT-03 senior-executive literacy plus GV.RR-01 leadership
    accountability can demonstrate ex-post to supervisory review that the
    Art. 5(4) `sufficient knowledge and skills` obligation was met at
    personal-capacity level and that the management body was structurally
    positioned to discharge Art. 5(2) oversight responsibilities with
    informed judgement rather than ceremonial sign-off.
  ambiguity_notes: |
    S2 VAG on `sufficient` is read at the role-relevant-competency end of the
    spectrum per the `commensurate to the ICT risk` qualifier. S2 VAG on
    `regular basis` is read as risk-driven cadence per the literal
    `actively keep up to date` formulation (alternatives include scheduled or
    ongoing). S2 VAG on `commensurate to the ICT risk` — the chosen reading
    is risk-proportional rather than risk-quantified. S2 POLY on `actively
    keep up to date` — alternatives include self-study, formal training, or
    both; the chosen reading is the literal AND. Remain open: evidence
    forms for `actively keep up to date` (training-attendance logs,
    assessment scores, peer-benchmark exercises) remain for entity policy.
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

