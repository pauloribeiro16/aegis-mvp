---
document_id: AEGIS-PREPROC-AI_Act-ART-55
title: AI_Act Art. 55 — SecurityObjectives & SecurityRules
regulation: AI_Act
article: Art. 55
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
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DomainAnalysis/D-07_Secure-Development/D-07.3.md
  - ../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.3.md
status: DRAFT
---

# AI_Act Art. 55

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-AIACT-014 | Providers of general-purpose AI models with systemic risk keep track of, document and report relevant information about serious incidents and possible corrective measures to the AI Office and, as appropriate, to national competent authorities, without undue delay. | `AIA-C28` (Art. 55(1)(a) — `standardised protocols` + `state of the art` + `systemic risks` POLY triple; adversarial testing mandate); `AIA-C29` (Art. 55(1)(c) — `serious incidents` POLY distinct from Art. 73 serious incidents; `without undue delay` VAG; cross-article boundary undefined) | D-04.3 |
| SO-AIACT-014 | D-04.3 | Art. 55(1)(a)+(c) | GPAI model evaluation + serious incident reporting |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-AIACT-001 (AI risk management lifecycle)

```yaml
- sr_id: SR-AIACT-022
  title: "Tiered serious incident reporting with differentiated timelines"
  source_clauses:
    - { clause_id: AIA-C26, article_ref: "Art. 73(1)–(4) — `report any serious incident`; `not later than 15 days after … becomes aware`; `not later than two days` (widespread infringement); `not later than 10 days` (death)" }
  linked_objectives: [SO-AIACT-013]
  sub_domain: [D-04.3]
  nist_csf_mapping:
    - { id: RS.CO-02, title: "Incidents are reported internally to the appropriate stakeholders, including executive leadership and legal counsel" }
    - { id: RS.CO-04, title: "Coordination with stakeholders occurs consistent with applicable rules and regulations" }
    - { id: RS.MA-03, title: "Incidents are categorized, prioritized, and scoped" }
    - { id: RS.MA-01, title: "The incident management plan is executed in coordination with relevant third parties once an incident is declared" }
  applies_to_role: [PROVIDER, DEPLOYER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 73(1)–(4) of Regulation (EU) 2024/1689 requires
    providers of high-risk AI systems, and deployers where
    applicable, to report any serious incident to the market
    surveillance authorities of the Member States where the
    incident occurred. The reporting timeline depends on the
    severity: 15 days after the provider becomes aware
    (default), 10 days if the incident results in death,
    2 days for widespread infringement. Art. 73(2)
    alternatively starts the 15-day clock on a reasonable
    likelihood to consider that a serious incident has
    occurred (whichever is later with the awareness trigger);
    the same 15-day window governs both attribution thresholds.
    Art. 3(49) defines `serious incident` via three
    sub-categories (a)/(b)/(c). Recital 92 sets the penalty
    envelope (Art. 99). The Art. 73 obligation is the most
    temporally complex notification clause in the AEGIS
    corpus — three numerical timelines (15 / 2 / 10 days) ×
    two attribution thresholds (awareness OR reasonable
    likelihood, whichever is later). A compliance officer
    should treat the Art. 73 timeline matrix as a mandatory
    operational reference, with pre-computed clock-start
    events and per-trigger escalation paths.
  security_rationale: |
    The Art. 73(1)–(4) serious-incident reporting duty is
    operationalised in NIST CSF 2.0 through **RS.CO-02
    (Incidents reported internally to executive leadership
    and legal counsel)**, **RS.CO-04 (Coordination with
    stakeholders consistent with applicable rules and
    regulations)**, **RS.MA-03 (Incidents categorised,
    prioritised, scoped)**, and **RS.MA-01 (Incident
    management plan executed in coordination with relevant
    third parties)**, with supplementary alignment to
    **RS.AN-03 (Root-cause analysis)**, **GV.OC-03 (Legal,
    regulatory, contractual requirements understood and
    managed)**, and **GV.PO-02 (Cybersecurity processes and
    procedures established, communicated, enforced)**.
    RS.CO-02 is the internal-reporting arm: the provider
    must route incident awareness to leadership and legal
    counsel so the market-surveillance report can be
    reviewed before transmission. RS.CO-04 is the
    external-reporting arm — coordination with the market
    surveillance authorities of the Member State(s) where
    the incident occurred, consistent with the Art. 73
    differentiated timelines. RS.MA-03 binds the reporting
    chain to a categorised scope so the correct timeline
    (15 / 10 / 2 days) is selected based on the incident
    class. RS.MA-01 ensures the provider's incident
    management plan is executed in coordination with
    deployers and other third parties, closing the
    provider-deployer handoff for joint incidents.
    Supplementary RS.AN-03 (root-cause analysis) supplies
    the substantiation the report must carry; GV.OC-03
    ensures the provider understands the cross-regulation
    (NIS 2 C30, DORA Art. 19) reporting obligations; and
    GV.PO-02 anchors the reporting workflow in documented
    processes. The combined control set yields an incident
    categorisation matrix, a timeline decision tree,
    internal-reporting records, external-reporting
    transmissions, a third-party coordination procedure,
    and a cross-regulation obligations register — the
    evidentiary substrate for ex post demonstration of
    compliance with the Art. 73 timeline matrix and the
    4-timeline × 4-trigger cross-product under the
    Art. 9 risk-management + Art. 72 PMM + Art. 73 incident
    reporting + Art. 99 penalty-envelope accountability
    chain.
  ambiguity_notes: |
    Source clause AIA-C26 carries **S3** features on three
    axes (per `../Regulation/AI_Act/Ambiguity/06_AI_Act.md` §2.26). `serious incident` is
    VAG-3 (defined in Art. 3(49) via three sub-categories
    (a)/(b)/(c) with distinct severity thresholds and
    undefined interaction; reading chosen: R3 literal —
    the three sub-categories apply independently and an
    incident can satisfy one or more). `becomes aware of
    the serious incident` is **SCOPE-Q-3** (Berry §5.7 —
    same awareness-trigger ambiguity as GDPR Art. 33
    `becomes aware`, CRA Art. 14, NIS 2 C30, DORA Art. 19;
    POLY+SCOPE-Q — R1 actual knowledge / R2 constructive
    knowledge / R3 either; R2 dominant CJEU reading
    applies). `reasonable likelihood of a causal link` is
    POLY-2 (distinct from `established causal link`; the
    two thresholds trigger the same 15-day clock).
    The 4-timeline × 4-trigger cross-product is **COORD-3**
    (Berry §5.7) — ≥16 distinct reporting-obligation
    shapes per `../Regulation/AI_Act/Ambiguity/06_AI_Act.md` §2.26. **Cross-article
    POLY:** the `serious incidents` of Art. 73 (high-risk)
    and Art. 55 (GPAI — SR-AIACT-024) may overlap; the
    boundary (when does a GPAI incident trigger Art. 73
    reporting vs. Art. 55 reporting vs. both?) is
    undefined. Remain open: (a) whether the 2-day
    widespread-infringement clock is calendar or business
    days; (b) whether the `immediate` reporting duty
    imposes a numeric clock (e.g. 24 hours) or is unbounded;
    (c) whether the Art. 73 vs. Art. 55 boundary is
    resolved by the AI Office or by the provider's own
    classification.
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

### SO-AIACT-001 (AI risk management lifecycle)

```yaml
- sr_id: SR-AIACT-024
  title: "GPAI serious incident reporting to the AI Office"
  source_clauses:
    - { clause_id: AIA-C29, article_ref: "Art. 55(1)(c) — `keep track of, document, and report, without undue delay, to the AI Office and, as appropriate, to national competent authorities, relevant information about serious incidents and possible corrective measures to address them`" }
  linked_objectives: [SO-AIACT-014]
  sub_domain: [D-04.3]
  nist_csf_mapping:
    - { id: RS.CO-02, title: "Incidents are reported internally to the appropriate stakeholders, including executive leadership and legal counsel" }
    - { id: RS.MA-03, title: "Incidents are categorized, prioritized, and scoped" }
    - { id: RS.AN-03, title: "Analysis is performed to determine what has occurred during an event and the root cause of the event" }
  applies_to_role: [PROVIDER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 55(1)(c) of Regulation (EU) 2024/1689 requires
    providers of general-purpose AI models with systemic
    risk to keep track of, document, and report, without
    undue delay, to the AI Office and, as appropriate, to
    national competent authorities, relevant information
    about serious incidents and possible corrective
    measures to address them. The recipient differs from
    the high-risk AI obligation of Art. 73 — the GPAI
    report goes to the AI Office (an EU-level body
    established by Art. 64), not the market surveillance
    authorities of the Member States. Recital 110
    clarifies the GPAI-specific nature of the obligation
    and the upstream nature of the reporting (foundation
    model vs. downstream application). A compliance officer
    at a GPAI provider should treat Art. 55(1)(c) as the
    upstream companion to the high-risk Art. 73 obligation,
    with a separate recipient and a separate (open-text)
    timeline.
  security_rationale: |
    The Art. 55(1)(c) GPAI serious-incident reporting duty
    is operationalised in NIST CSF 2.0 through **RS.CO-02
    (Incidents reported internally to executive leadership
    and legal counsel)**, **RS.MA-03 (Incidents
    categorised, prioritised, scoped)**, and **RS.AN-03
    (Root-cause analysis)**, with supplementary alignment
    to **GV.OC-03 (Legal, regulatory, contractual
    requirements understood and managed)**, **GV.PO-01
    (Organisational cybersecurity policy established,
    communicated, enforced)**, and **RS.CO-04
    (Coordination with stakeholders consistent with
    applicable rules and regulations)**. RS.CO-02 is the
    internal-reporting arm: the GPAI provider must route
    incident awareness to leadership and legal counsel so
    the AI Office report can be reviewed and the
    `without undue delay` clock is controlled. RS.MA-03
    binds the reporting to a categorised scope so the
    `serious incidents AND possible corrective measures`
    elements are both addressed. RS.AN-03 enforces the
    root-cause analysis that the report must carry to
    satisfy the `relevant information` element of
    Art. 55(1)(c). Supplementary GV.OC-03 ensures the
    GPAI provider understands the cross-regulation
    reporting regime (Art. 55 GPAI + Art. 73 high-risk
    + NIS 2 C30 + DORA Art. 19, with the Art. 55 vs.
    Art. 73 boundary per the SR-AIACT-022 ambiguity
    note). GV.PO-01 anchors the reporting workflow in
    a top-level policy; and RS.CO-04 ensures
    coordination with the AI Office and national
    competent authorities is consistent with applicable
    rules. The combined control set yields a categorised
    incident register, a root-cause analysis pipeline,
    internal-reporting records, AI Office transmissions,
    a top-level policy, a cross-regulation obligations
    register, and a coordination procedure — the
    evidentiary substrate for ex post demonstration of
    compliance with the Art. 55(1)(c) reporting duty
    under the Art. 9 risk-management + Art. 55(1)(a)
    model-evaluation + Art. 55(1)(c) GPAI incident
    reporting + Art. 72 PMM accountability chain.
  ambiguity_notes: |
    Source clause AIA-C29 carries three **S3** features
    (per `../Regulation/AI_Act/Ambiguity/06_AI_Act.md` §2.29). `without undue delay`
    is VAG-3 (Berry classic; cf. NIS 2 C30 on `without
    undue delay`). `relevant information` is VAG-3
    (the OJ does not enumerate what is `relevant`).
    `as appropriate` is POLY-3 (R1 mandatory / R2
    optional / R3 case-by-case). The `serious incidents`
    term is **POLY-3** for GPAI models — distinct from
    `serious incidents` for high-risk AI systems (Art. 73)
    but the cross-reference is implicit; the boundary
    (when does a GPAI incident trigger Art. 55 reporting
    vs. Art. 73 reporting vs. both?) is undefined
    (Berry §3.3.1 cross-article polysemy). The 3-way
    verb AND `keep track of, document, AND report` and
    the AND `serious incidents AND possible corrective
    measures` are COORD-2. Remain open: (a) whether
    `without undue delay` imposes a numeric clock (and
    if so, what number — 72h? 7d?) or is unbounded;
    (b) whether the `as appropriate` axis is mandatory
    when the national competent authority requests
    the report; (c) whether the AI Office will issue
    a unified incident-reporting template that
    resolves the Art. 55 vs. Art. 73 boundary.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

