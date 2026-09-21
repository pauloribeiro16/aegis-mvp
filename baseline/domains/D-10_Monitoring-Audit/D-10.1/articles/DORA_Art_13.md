---
document_id: AEGIS-PREPROC-DORA-ART-13
title: DORA Art. 13 — SecurityObjectives & SecurityRules
regulation: DORA
article: Art. 13
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
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.2.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.2.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.4.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.4.md
  - ../../CrossRegulation/DomainAnalysis/D-07_Secure-Development/D-07.4.md
  - ../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.4.md
  - ../../CrossRegulation/DomainAnalysis/D-08_Human-Factors/D-08.1.md
  - ../../CrossRegulation/DeepAnalysis/D-08_Human-Factors/D-08.1.md
  - ../../CrossRegulation/DomainAnalysis/D-08_Human-Factors/D-08.2.md
  - ../../CrossRegulation/DeepAnalysis/D-08_Human-Factors/D-08.2.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.3.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.3.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.1.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.1.md
status: DRAFT
---

# DORA Art. 13

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-DORA-015 | ICT security awareness programmes and digital operational resilience training are developed as compulsory modules in staff training schemes, with a level of complexity commensurate to the remit of staff functions. | `DORA-C27` (Art. 13(6) `compulsory modules` + awareness programmes + digital operational resilience training); `DORA-C28` (Art. 13(6) same locus — `commensurate to the remit` T4 reads as role-specific); `DORA-C26` (Art. 13(6) — T4 mapping mismatch per `../Regulation/DORA/Ambiguity/05_DORA.md` §2.26: T4 maps to `D-02.2 Patch Management & Updates` but OJ Art. 13(6) is about training programmes, not patching. SO preserves OJ-literal locus at D-08.1/D-08.2) | D-08.1, D-08.2 |
| SO-DORA-015 | D-08.1, D-08.2 | Art. 13(6) | ICT security awareness + digital operational resilience training |

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

