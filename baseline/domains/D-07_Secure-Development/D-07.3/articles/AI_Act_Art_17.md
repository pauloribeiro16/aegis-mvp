---
document_id: AEGIS-PREPROC-AI_Act-ART-17
title: AI_Act Art. 17 — SecurityObjectives & SecurityRules
regulation: AI_Act
article: Art. 17
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
  - ../../CrossRegulation/DomainAnalysis/D-07_Secure-Development/D-07.1.md
  - ../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.1.md
  - ../../CrossRegulation/DomainAnalysis/D-07_Secure-Development/D-07.3.md
  - ../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.3.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
status: DRAFT
---

# AI_Act Art. 17

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-AIACT-010 | A quality management system is implemented to ensure compliance with the AI Act, documented in a systematic and orderly manner in the form of written policies, procedures and instructions, and covering at least 13 enumerated aspects including techniques, procedures and systematic actions for the design, design control and design verification of the high-risk AI system. | `AIA-C20` (Art. 17(1) — `systematic and orderly manner` + `quality management system` POLY (ISO 9001 / ISO/IEC 23053 / internal bespoke) + 13-element closed list (a)–(m)); `AIA-C21` (Art. 17(1)(c) — `design, design control and design verification` 3-way AND of near-synonyms); `AIA-C22` (Art. 17(1)(g) — risk-management-system documentation cross-reference to Art. 9) | D-09.1 (primary), D-07.1 (cross) |
| SO-AIACT-010 | D-09.1, D-07.1 | Art. 17(1)+(1)(c)+(1)(g) | QMS with 13 enumerated aspects + design/design control/verification |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-AIACT-001 (AI risk management lifecycle)

```yaml
- sr_id: SR-AIACT-017
  title: "Documented quality management system governing AI compliance"
  source_clauses:
    - { clause_id: AIA-C20, article_ref: "Art. 17(1) — `Providers of high-risk AI systems shall put a quality management system in place that ensures compliance with this Regulation. That system shall be documented in a systematic and orderly manner in the form of written policies, procedures and instructions, and shall include at least the following aspects: (a) … (m)`" }
    - { clause_id: AIA-C22, article_ref: "Art. 17(1)(g) — `the risk management system referred to in Article 9`" }
  linked_objectives: [SO-AIACT-010]
  sub_domain: [D-09.1]
  nist_csf_mapping:
    - { id: GV.PO-01, title: "Organizational cybersecurity policy is established, communicated, and enforced" }
    - { id: GV.RM-01, title: "Risk management objectives are established and agreed to by organizational stakeholders" }
    - { id: GV.RM-04, title: "Strategic direction on identifying and responding to risks established and communicated" }
  applies_to_role: [PROVIDER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 17(1) of Regulation (EU) 2024/1689 requires providers of
    high-risk AI systems to put in place a quality management
    system (QMS) that ensures compliance with the AI Act. The QMS
    must be documented in a systematic and orderly manner as
    written policies, procedures, and instructions, and must
    cover at least the 13 enumerated aspects (a)–(m) of the
    paragraph. Sub-point (g) cross-refers to Art. 9 (the risk
    management system), so the QMS is the governance substrate
    for the substantive Title III obligations. Recital 67
    characterises the QMS as inspired by established quality
    standards (ISO 9001 family) but does not mandate a specific
    standard, leaving the provider to choose. A compliance officer
    should treat the QMS as the umbrella obligation that the
    conformity assessment will examine first.
  security_rationale: |
    The Art. 17(1) QMS duty is operationalised in NIST CSF 2.0
    through **GV.PO-01 (Organisational cybersecurity policy
    established, communicated, enforced)**, **GV.RM-01 (Risk
    management objectives established and agreed)**, and
    **GV.RM-04 (Strategic direction on identifying and
    responding to risks)**, with supplementary alignment to
    **GV.PO-02 (Cybersecurity processes and procedures
    established, communicated, enforced)** and **GV.OC-03
    (Legal, regulatory, contractual requirements understood
    and managed)**. GV.PO-01 is the policy arm of the QMS —
    the top-level written cybersecurity policy that
    operationalises the 13-element list (a)–(m), including the
    policies, procedures, and instructions anchor in Art. 17(1).
    GV.RM-01 binds the QMS to risk-management objectives that
    have been agreed by organisational stakeholders, satisfying
    sub-point (g)'s cross-reference to Art. 9. GV.RM-04 supplies
    the strategic-direction layer (risk appetite, response
    posture, escalation criteria) that connects policy
    formulation (GV.PO-01) and risk-objective setting
    (GV.RM-01) to operational risk-treatment decisions.
    Supplementary GV.PO-02 ensures that the policies are
    accompanied by processes and procedures that are also
    documented, communicated, and enforced — the systematic
    and orderly requirement of Art. 17(1). GV.OC-03 closes the
    loop by ensuring the QMS understands and manages the full
    set of legal, regulatory, and contractual obligations that
    the AI Act adds on top of CRA, NIS 2, GDPR, and DORA. The
    combined control set yields a documented policy stack,
    agreed risk-management objectives, a strategic-direction
    document, process and procedure manuals, and a legal/
    regulatory obligations register — the evidentiary
    substrate for the conformity-assessment body to examine
    the QMS as the umbrella obligation under the Art. 17
    QMS + Art. 9 risk-management + Art. 43/47 conformity-
    assessment accountability chain.
  ambiguity_notes: |
    Source clause AIA-C20 carries **S2** features (per
    `../Regulation/AI_Act/Ambiguity/06_AI_Act.md` §2.20). `systematic and orderly manner` is
    VAG-2 (Berry §5.1 — the OJ does not anchor the sense).
    `quality management system` is POLY-2 with R1 ISO 9001
    / R2 ISO/IEC 23053 (AI risk management framework
    standard) / R3 internal bespoke; the OJ does not name
    any specific standard (reading chosen: R3 literal). The
    3-way AND of `written policies, procedures AND instructions`
    and the 13-element closed list (a)–(m) are both COORD-2.
    AIA-C22 inherits POLY-2 from AIA-C01 (`risk management
    system` — the central AI Act ambiguity per `../Regulation/AI_Act/Ambiguity/06_AI_Act.md`
    §3.5). Remain open: (a) whether conformity-assessment
    bodies will accept an ISO 9001 certificate as a proxy
    for the QMS or require a stand-alone AI-QMS file; (b)
    whether the 13 elements must be discrete QMS chapters or
    can be embedded into a single integrated management
    system.
```

### SO-AIACT-001 (AI risk management lifecycle)

```yaml
- sr_id: SR-AIACT-018
  title: "Secure design control and verification integrated into SDLC"
  source_clauses:
    - { clause_id: AIA-C21, article_ref: "Art. 17(1)(c) — `techniques, procedures and systematic actions to be used for the design, design control and design verification of the high-risk AI system`" }
  linked_objectives: [SO-AIACT-010]
  sub_domain: [D-07.1]
  nist_csf_mapping:
    - { id: PR.PS-06, title: "Secure software development practices are integrated, and their performance is monitored throughout the SDLC" }
    - { id: PR.PS-01, title: "Configuration management practices are established, documented, and applied to assets" }
  applies_to_role: [PROVIDER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 17(1)(c) of Regulation (EU) 2024/1689 requires the QMS
    to include the techniques, procedures, and systematic actions
    used for the design, design control, and design verification
    of the high-risk AI system. This is the secure-development-
    lifecycle anchor of the QMS and is the operational bridge
    between Art. 17(1) (QMS) and Art. 9 (risk management) on
    one side, and Art. 15 (accuracy / robustness / cybersecurity)
    on the other. A compliance officer should treat Art. 17(1)(c)
    as the SDLC sub-process specification that the conformity
    assessment will examine alongside the technical documentation
    (Annex IV).
  security_rationale: |
    The Art. 17(1)(c) SDLC duty is operationalised in NIST CSF
    2.0 through **PR.PS-06 (Secure software development
    practices integrated across the SDLC)** and **PR.PS-01
    (Configuration management practices established,
    documented, applied)**, with supplementary alignment to
    **PR.PS-02 (Software maintenance commensurate with risk)**,
    **ID.RA-01 (Vulnerability identification, validation,
    recording)**, and **GV.PO-02 (Cybersecurity processes and
    procedures established, communicated, enforced)**. PR.PS-06
    is the principal anchor: it directly maps to the
    `techniques, procedures and systematic actions` for
    `design, design control and design verification` of the
    high-risk AI system, covering threat modelling (design),
    code review and change control (design control), and
    testing and review (design verification). PR.PS-01 enforces
    the design-control axis — configuration baselines,
    integrity of design artefacts, controlled changes — so
    that the design can be traced to its source and
    reconstructed. Supplementary PR.PS-02 binds software
    maintenance to the risk picture (patching, replacement,
    removal), closing the post-market SDLC loop. ID.RA-01
    ensures that vulnerabilities identified during design
    verification are recorded, validated, and feed back into
    the risk-management file under Art. 9. GV.PO-02 enforces
    that the SDLC is anchored in documented, communicated, and
    enforced processes. The combined control set yields
    documented design specifications, configuration baselines,
    change-control records, verification reports (test
    results, code-review records), vulnerability register
    entries, and process manuals — the evidentiary substrate
    for ex post demonstration of compliance under the Art. 17
    QMS + Art. 9 risk-management + Art. 15 accuracy-
    robustness-cybersecurity + Art. 43/47 conformity-
    assessment accountability chain.
  ambiguity_notes: |
    Source clause AIA-C21 carries **S2** POLY-2 on
    `design` vs. `design control` vs. `design verification`
    — three engineering terms with overlapping but distinct
    industry meanings (Berry §3.3.1; cf. ISO 9001 §8.3, IEC
    62304, NIST SP 800-218 SSDF PW.4/PW.5/PW.7). The 3-way
    AND of `design, design control AND design verification`
    + 3-way AND of `techniques, procedures AND systematic
    actions` is a twin 3-way AND that compounds the
    cumulative obligation (Berry §5.5). Remain open: (a)
    whether `design verification` requires independent
    verification (i.e. a separate team) or self-verification
    by the design team is acceptable; (b) whether the
    `systematic actions` axis covers post-deployment
    verification or only pre-market verification.
```

### SO-AIACT-001 (AI risk management lifecycle)

```yaml
- sr_id: SR-AIACT-019
  title: "Deployer measures aligned with provider instructions for use"
  source_clauses:
    - { clause_id: AIA-C23, article_ref: "Art. 26(1) — `Deployers of high-risk AI systems shall take appropriate technical and organisational measures to ensure they use such systems in accordance with the instructions for use`" }
  linked_objectives: [SO-AIACT-011]
  sub_domain: [D-09.1]
  nist_csf_mapping:
    - { id: GV.PO-01, title: "Organizational cybersecurity policy is established, communicated, and enforced" }
    - { id: GV.OC-03, title: "Legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed" }
    - { id: PR.AT-01, title: "All users are informed and trained on cybersecurity topics (e.g., recognition of phishing, social engineering, and other relevant risks)" }
  applies_to_role: [DEPLOYER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 26(1) of Regulation (EU) 2024/1689 requires deployers
    of high-risk AI systems to take appropriate technical and
    organisational measures to ensure they use the system in
    accordance with the provider's instructions for use. This
    is the deployer-side mirror of the provider's QMS
    obligation under Art. 17: the deployer cannot rely on the
    provider's design-time safeguards to discharge its own
    duty. The phrase `technical and organisational measures`
    uses the same AND/OR pattern as GDPR Art. 5(1)(f) (security
    of processing, `C04`) and as NIS 2 Art. 21(1) (C18), so
    the provider-deployer interface inherits the consolidated
    cross-regulation reading. A compliance officer at the
    deployer should treat the instructions for use as the
    binding use-case specification.
  security_rationale: |
    The Art. 26(1) deployer duty is operationalised in NIST CSF
    2.0 through **GV.PO-01 (Organisational cybersecurity policy
    established, communicated, enforced)**, **GV.OC-03 (Legal,
    regulatory, contractual requirements understood and
    managed)**, and **PR.AT-01 (User awareness and training)**,
    with supplementary alignment to **GV.RR-01 (Leadership
    accountability for cybersecurity risk)**, **GV.RR-02 (Roles,
    responsibilities, authorities, accountabilities established
    and communicated)**, and **PR.AT-03 (Senior executive
    understanding of cybersecurity roles)**. GV.PO-01 anchors
    the deployer's own organisational policy — the deployer
    cannot satisfy Art. 26(1) by merely adopting the
    provider's policy unchanged; it must have a deployer-side
    policy that maps to the provider's instructions for use.
    GV.OC-03 ensures the deployer understands and manages the
    full set of legal (Art. 26 + Art. 27), regulatory (NIS 2 +
    DORA + CRA), and contractual (Art. 26 provider-deployer
    agreement) obligations layered on top of the AI Act.
    PR.AT-01 binds the technical-and-organisational measures
    to user awareness and training, so that deployer staff
    recognise AI-specific risks (data poisoning, model
    evasion, automation bias). Supplementary GV.RR-01 and
    GV.RR-02 reinforce accountability by requiring leadership
    ownership and explicit RACI for the AI system, and
    PR.AT-03 ensures the deployer's executives understand
    their role. The combined control set yields a documented
    deployer cybersecurity policy, an obligations register,
    a training programme, an executive accountability
    statement, and a RACI matrix — the evidentiary substrate
    for the deployer to demonstrate ex post that its use of
    the high-risk AI system complied with the provider's
    instructions and with Art. 26 (deployer obligations)
    under the Art. 17 QMS + Art. 26 deployer + Art. 27
    fundamental-rights impact assessment + GDPR Art. 5(1)(f)
    + NIS 2 Art. 21 accountability chain.
  ambiguity_notes: |
    Source clause AIA-C23 carries **S2** features (per
    `../Regulation/AI_Act/Ambiguity/06_AI_Act.md` §2.23). `appropriate` is VAG-2 (Berry
    §5.1 — the legal-hedge vs. technical-recommendation
    distinction is material; reading chosen: R3 cumulative —
    `appropriate` is read as `proportionate to the risk`,
    not as a soft floor). The AND of `technical AND
    organisational` is COORD-2 (Berry §5.4.7 — same pattern
    as GDPR C04 and NIS 2 C18; reading chosen: R1 inclusive
    — both dimensions required, exclusive readings not
    accommodated by the OJ). Remain open: (a) whether a
    deployer can satisfy `appropriate` by adopting the
    provider's TOMs unchanged, or must adapt them to the
    deployer's own risk profile; (b) whether the deployer's
    `appropriate` threshold is a separate assessment or
    inherits the provider's `appropriate` ceiling.
```

### SO-AIACT-001 (AI risk management lifecycle)

```yaml
- sr_id: SR-AIACT-023
  title: "Adversarial evaluation of GPAI models for systemic risk mitigation"
  source_clauses:
    - { clause_id: AIA-C28, article_ref: "Art. 55(1)(a) — `perform model evaluation in accordance with standardised protocols and tools reflecting the state of the art, including conducting and documenting adversarial testing of the model with a view to identifying and mitigating systemic risks`" }
  linked_objectives: [SO-AIACT-014]
  sub_domain: [D-07.3, D-02.1]
  nist_csf_mapping:
    - { id: GV.RM-06, title: "A standardized method for calculating, documenting, categorizing, and prioritizing cybersecurity risks is established and communicated" }
    - { id: ID.RA-04, title: "Potential impacts and likelihoods of threats exploiting vulnerabilities are identified, recorded, and prioritized" }
    - { id: PR.PS-06, title: "Secure software development practices are integrated, and their performance is monitored throughout the SDLC" }
  applies_to_role: [PROVIDER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 55(1)(a) of Regulation (EU) 2024/1689 requires
    providers of general-purpose AI (GPAI) models with
    systemic risk to perform model evaluation in
    accordance with standardised protocols and tools
    reflecting the state of the art, including conducting
    and documenting adversarial testing of the model with
    a view to identifying and mitigating systemic risks.
    Art. 55 sits in Title IV (General-Purpose AI Models),
    Chapter V (Obligations of Providers of GPAI Models
    with Systemic Risk), and is parallel to — but
    distinct from — the Title III high-risk AI obligations
    of Arts. 9–15. Recital 110 frames the model-evaluation
    obligation as the upstream assurance for foundation
    models that can serve many downstream AI applications.
    A compliance officer at a GPAI provider should treat
    Art. 55(1)(a) as the technical-assurance anchor of
    the systemic-risk regime, on par with the QMS
    obligation of Art. 17(1) for high-risk providers.
  security_rationale: |
    The Art. 55(1)(a) GPAI model-evaluation duty is
    operationalised in NIST CSF 2.0 through **GV.RM-06
    (Standardised method for calculating, documenting,
    categorising, prioritising cybersecurity risks)**,
    **ID.RA-04 (Threat-impact prioritisation)**, and
    **PR.PS-06 (Secure SDLC practices integrated,
    performance monitored)**, with supplementary alignment
    to **GV.OC-03 (Legal, regulatory, contractual
    requirements understood and managed)**, **GV.PO-01
    (Organisational cybersecurity policy established,
    communicated, enforced)**, and **GV.OV-02 (Strategy
    reviewed against changing risk landscape)**. GV.RM-06
    is the principal anchor: it operationalises the
    `standardised protocols` element of Art. 55(1)(a) by
    requiring the GPAI provider to establish and
    communicate a standardised risk-calculation method,
    so that the model-evaluation is reproducible and
    defensible rather than ad hoc. ID.RA-04 enforces the
    `identifying systemic risks` element: threats,
    vulnerabilities, likelihoods, and impacts are
    recorded and prioritised, providing the structured
    input to the `mitigating systemic risks` follow-up.
    PR.PS-06 binds the `conducting and documenting`
    element to the SDLC substrate — secure development
    practices, threat modelling, and verification
    artefacts, so that the adversarial testing produces
    auditable records. Supplementary GV.OC-03 ensures
    the GPAI provider understands the layered regulatory
    regime (AI Act + CRA + NIS 2 + DORA for financial-
    sector GPAI), GV.PO-01 anchors the model-evaluation
    programme in a top-level policy, and GV.OV-02
    enforces the strategy-review cadence required by
    the `state of the art` element. The combined
    control set yields a standardised evaluation
    methodology, prioritised systemic-risk register,
    adversarial-testing reports, SDLC artefacts, a
    top-level policy, a cross-regulation obligations
    register, and strategy-review minutes — the
    evidentiary substrate for ex post demonstration of
    compliance with the Art. 55(1)(a) model-evaluation
    + Art. 9 risk-management + Art. 15(4)–(5) AI-
    specific attack + Art. 72 PMM accountability chain.
  ambiguity_notes: |
    Source clause AIA-C28 carries three **S3** features
    (per `../Regulation/AI_Act/Ambiguity/06_AI_Act.md` §2.28 — the second-most-
    consequential AI Act ambiguity after `risk management
    system`). `standardised protocols` is VAG-3 (R1 ISO/IEC
    standards / R2 NIST standards / R3 MLCommons benchmarks;
    reading chosen: R3 literal — the clause does not anchor
    the sense, so the OJ defers to whichever standard the
    provider can defend as `state of the art`). `state of
    the art` is VAG-3 (Berry classic; cf. GDPR C09, CRA C07;
    time-dependent, jurisdiction-dependent). `systemic risks`
    is VAG-3 (undefined at Union level for AI; the term is
    borrowed from financial-services regulation where it
    has a specific meaning; the AI-Act use is broader —
    the borrow is implicit and operators unfamiliar with
    DORA Art. 4(50) cannot read this clause self-contained).
    `adversarial testing` is POLY-2 (distinct from
    red-teaming, fuzzing, robustness testing). The
    `conducting AND documenting` + `identifying AND
    mitigating` pairs are COORD-2. The triple
    `standardised protocols + state of the art + systemic
    risks` is **the second-most-consequential AI Act
    ambiguity** per `../Regulation/AI_Act/Ambiguity/06_AI_Act.md` §3.5. Remain open:
    (a) whether the AI Office will issue a list of
    recognised `standardised protocols` or leave the
    determination to the provider; (b) whether
    `systemic risks` includes downstream-application-
    level risks or only foundation-model-level risks;
    (c) whether `adversarial testing` requires a public
    report (as some red-team frameworks recommend) or
    a confidential internal report.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

