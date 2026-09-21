---
document_id: AEGIS-PREPROC-DORA-ART-15
title: DORA Art. 15 — SecurityObjectives & SecurityRules
regulation: DORA
article: Art. 15
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
  - ../../CrossRegulation/DomainAnalysis/D-02_Vulnerability-Management/D-02.2.md
  - ../../CrossRegulation/DeepAnalysis/D-02_Vulnerability-Management/D-02.2.md
  - ../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.1.md
  - ../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.1.md
  - ../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.2.md
  - ../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.2.md
  - ../../CrossRegulation/DomainAnalysis/D-07_Secure-Development/D-07.1.md
  - ../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.1.md
status: DRAFT
---

# DORA Art. 15

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

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

