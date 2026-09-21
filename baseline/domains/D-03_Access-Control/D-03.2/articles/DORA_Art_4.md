---
document_id: AEGIS-PREPROC-DORA-ART-4
title: DORA Art. 4 — SecurityObjectives & SecurityRules
regulation: DORA
article: Art. 4
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-01_Data-Protection/D-01.3.md
  - ../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.3.md
  - ../../CrossRegulation/DomainAnalysis/D-02_Vulnerability-Management/D-02.1.md
  - ../../CrossRegulation/DeepAnalysis/D-02_Vulnerability-Management/D-02.1.md
  - ../../CrossRegulation/DomainAnalysis/D-02_Vulnerability-Management/D-02.2.md
  - ../../CrossRegulation/DeepAnalysis/D-02_Vulnerability-Management/D-02.2.md
  - ../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.1.md
  - ../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.1.md
  - ../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.2.md
  - ../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.2.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.1.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.1.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.3.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.3.md
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
status: DRAFT
---

# DORA Art. 4

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

_No standalone SO row cites this article directly (covered via the rules below)._

## Security Rules (from 02_SecurityRules_NIST.md)

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

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

