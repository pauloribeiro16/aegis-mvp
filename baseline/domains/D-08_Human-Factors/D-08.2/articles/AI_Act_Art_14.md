---
document_id: AEGIS-PREPROC-AI_Act-ART-14
title: AI_Act Art. 14 — SecurityObjectives & SecurityRules
regulation: AI_Act
article: Art. 14
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DomainAnalysis/D-07_Secure-Development/D-07.1.md
  - ../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.1.md
  - ../../CrossRegulation/DomainAnalysis/D-08_Human-Factors/D-08.2.md
  - ../../CrossRegulation/DeepAnalysis/D-08_Human-Factors/D-08.2.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
status: DRAFT
---

# AI_Act Art. 14

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-AIACT-008 | High-risk AI systems are designed and developed to be effectively overseen by natural persons during the period in which they are in use, including with appropriate human-machine interface tools; the natural persons assigned to human oversight have the necessary competence, training and authority, as well as the necessary support, to (a) properly understand, (b) remain aware of automation bias, (c) correctly interpret, (d) decide, and (e) intervene on the AI system's operation. | `AIA-C14` (Art. 14(1) — `effectively overseen` POLY + `appropriate human-machine interface tools`); `AIA-C15` (Art. 14(4) — `as appropriate and proportionate` + 5-element closed list (a)–(e) of oversight abilities + `automation bias` POLY) | D-08.2 (primary), D-07.1 (cross) |
| SO-AIACT-008 | D-08.2, D-07.1 | Art. 14(1)+(4) | Human oversight design + 5-element oversight capability list |

## Security Rules (from 02_SecurityRules_NIST.md)

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

### SO-AIACT-001 (AI risk management lifecycle)

```yaml
- sr_id: SR-AIACT-013
  title: "Five cumulative human-oversight abilities enabled as appropriate"
  source_clauses:
    - { clause_id: AIA-C15, article_ref: "Art. 14(4) — `natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate: (a) to properly understand … (b) to remain aware … (c) to correctly interpret … (d) to decide … (e) to intervene …`" }
  linked_objectives: [SO-AIACT-008]
  sub_domain: [D-08.2]
  nist_csf_mapping:
    - { id: PR.AT-02, title: "All members of the organization's workforce understand their roles and responsibilities in achieving the organization's cybersecurity objectives" }
    - { id: PR.AT-01, title: "All users are informed and trained on cybersecurity topics (e.g., recognition of phishing, social engineering, and other relevant risks)" }
    - { id: GV.RR-02, title: "Roles, responsibilities, authorities, and accountabilities related to cybersecurity risk management are established, communicated, understood, and enforced" }
  applies_to_role: [PROVIDER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 14(4) of the AI Act requires that natural persons to
    whom human oversight is assigned are enabled, as appropriate
    and proportionate, to discharge five cumulative oversight
    abilities: (a) to properly understand the relevant capacities
    and limitations of the high-risk AI system and foreseeable
    misuse scenarios; (b) to remain aware of automation bias; (c)
    to correctly interpret the output; (d) to decide not to use
    the high-risk AI system or to disregard, override or reverse
    its output; and (e) to intervene on the operation or
    interrupt the system through a stop button or similar
    procedure. The five-element list operationalises the umbrella
    human-oversight duty in Article 14(1) and is reinforced by
    Article 14(5) on deployer-oversight enablement.
  security_rationale: |
    The obligation in Art. 14(4) is operationalised in NIST CSF
    2.0 through **PR.AT-02 (All members of the organization's
    workforce understand their roles and responsibilities in
    achieving the organization's cybersecurity objectives)**,
    **PR.AT-01 (All users are informed and trained on
    cybersecurity topics (e.g., recognition of phishing, social
    engineering, and other relevant risks))**, and **GV.RR-02
    (Roles, responsibilities, authorities, and accountabilities
    related to cybersecurity risk management are established,
    communicated, understood, and enforced)**. PR.AT-02 covers
    the role-understanding dimension that sub-points (a) `properly
    understand` and (c) `correctly interpret` require. PR.AT-01
    anchors the awareness-and-training substrate that sub-point
    (b) `remain aware of automation bias` and sub-points (d)
    `decide` and (e) `intervene` require, ensuring overseers
    detect and respond to AI-specific failure modes including the
    cognitive-bias correction that `automation bias` operationalises.
    GV.RR-02 supplies the RACI substrate that sub-points (d) and
    (e) require — overseers must hold formal authority to override
    and interrupt the system. A provider evidencing PR.AT-02 role
    understanding, PR.AT-01 awareness training and GV.RR-02 RACI
    definition demonstrates ex post that the five-element Art.
    14(4) oversight-abilities list — cumulative AND of all five
    abilities plus the last-resort sub-point (e) intervention
    safety net — is operationalised in the provider's training
    and tooling programme.
  ambiguity_notes: |
    The clause carries medium severity on the soft-hedge opening
    `as appropriate and proportionate`, which modifies the entire
    five-element list and which itself is a Berry-classic soft
    hedge. The phrase `automation bias` is poly-semous and
    imported from human-factors research without definition in
    the OJ; the chosen reading is that the technical term carries
    its established human-factors meaning, which encompasses both
    the cognitive tendency to defer to automated outputs and the
    related tendency to under-detect automation errors. The
    five-element list is AND-coordinated, so all five abilities
    must be enabled cumulatively. As an alternative reading,
    providers could collapse the five abilities into a single
    integrated training-and-tooling programme that addresses each
    ability without treating them as separate documentation
    deliverables. Remain open: whether the `as appropriate and
    proportionate` hedge permits omission of certain abilities for
    low-risk categories of high-risk systems, such as Annex III
    category 1 biometric systems where some abilities are
    operationally infeasible or where sub-point (e) intervention
    is impossible at biometric-decision latency.
```

### SO-AIACT-001 (AI risk management lifecycle)

```yaml
- sr_id: SR-AIACT-020
  title: "Competent human overseers assigned with training and authority"
  source_clauses:
    - { clause_id: AIA-C24, article_ref: "Art. 26(2) — `Deployers shall assign human oversight to natural persons who have the necessary competence, training and authority, as well as the necessary support`" }
  linked_objectives: [SO-AIACT-011]
  sub_domain: [D-08.2, D-09.1]
  nist_csf_mapping:
    - { id: PR.AT-02, title: "All members of the organization's workforce understand their roles and responsibilities in achieving the organization's cybersecurity objectives" }
    - { id: GV.RR-02, title: "Roles, responsibilities, authorities, and accountabilities related to cybersecurity risk management are established, communicated, understood, and enforced" }
    - { id: GV.RR-04, title: "Cybersecurity is included in human resources practices (e.g., people screening, onboarding, training, awareness, offboarding)" }
  applies_to_role: [DEPLOYER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 26(2) of Regulation (EU) 2024/1689 requires deployers
    to assign human oversight to natural persons who have the
    necessary competence, training, and authority, and the
    necessary support. This is the deployer-side mirror of
    Art. 14(1) (provider design of oversight) and Art. 14(2)
    (provider enablement of oversight by deployers): the
    deployer must identify, qualify, authorise, and resource
    the natural persons who will exercise the oversight
    function. A compliance officer at the deployer should
    treat this provision as the personnel-qualification anchor
    of the deployer's AI-governance framework.
  security_rationale: |
    The Art. 26(2) deployer-oversight duty is operationalised
    in NIST CSF 2.0 through **PR.AT-02 (Workforce understanding
    of roles and responsibilities)**, **GV.RR-02 (Roles,
    responsibilities, authorities, accountabilities
    established, communicated, understood, enforced)**, and
    **GV.RR-04 (Cybersecurity in HR practices)**, with
    supplementary alignment to **PR.AT-01 (User awareness and
    training)**, **PR.AT-03 (Senior executive understanding
    of roles)**, and **GV.RR-01 (Leadership accountability
    for cybersecurity risk)**. PR.AT-02 is the principal
    anchor: it requires the deployer to ensure the assigned
    human overseers understand their role (Art. 14(4)(a) —
    properly understand the system's capacities, limitations
    and foreseeable misuse) and their responsibilities
    (Art. 14(4)(b)–(e) — awareness of automation bias,
    interpretation, decision, intervention). GV.RR-02
    enforces the formal `competence, training AND authority`
    structure by requiring roles, responsibilities,
    authorities, and accountabilities to be established,
    communicated, understood, and enforced — the four-way
    AND that the deployer must evidence for each overseer.
    GV.RR-04 binds the overseer assignment to the deployer's
    HR practices (screening, onboarding, training, awareness,
    offboarding) so the `necessary support` element of
    Art. 26(2) is operationalised across the employment
    lifecycle. Supplementary PR.AT-01 covers the
    `awareness` training dimension, PR.AT-03 ensures the
    deployer's executives understand the role, and GV.RR-01
    anchors leadership accountability. The combined control
    set yields personnel files per overseer documenting the
    four elements (competence, training, authority,
    support), a RACI matrix, a training programme, HR
    onboarding/offboarding records, and an executive
    accountability statement — the evidentiary substrate
    for the deployer to demonstrate ex post that each
    overseer met the Art. 26(2) qualification standard
    under the Art. 14(1)+(2)+(4) provider-side design +
    Art. 26(2) deployer-side assignment + Art. 27
    fundamental-rights impact assessment accountability
    chain.
  ambiguity_notes: |
    Source clause AIA-C24 carries **S2** features (per
    `../Regulation/AI_Act/Ambiguity/06_AI_Act.md` §2.24). `necessary` is VAG-2 (Berry §5.1).
    `competence, training, authority` is POLY-2 (three near-
    synonyms for personnel qualifications; reading chosen:
    R3 literal AND — the three terms collectively cover the
    cognitive, capability, and authority dimensions). The
    3-way AND `competence, training AND authority` + the
    4th element `necessary support` is COORD-2. The deployer
    must therefore maintain a personnel file per oversight
    person, documenting each of the four elements. Remain
    open: (a) whether `necessary support` is limited to
    technical support (access, tooling) or extends to
    organisational support (escalation paths, indemnity);
    (b) whether the same natural person can hold oversight
    for multiple high-risk AI systems or whether one-person-
    per-system is required.
```

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

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

