---
document_id: AEGIS-PREPROC-DORA-ART-30
title: DORA Art. 30 — SecurityObjectives & SecurityRules
regulation: DORA
article: Art. 30
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.1.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.1.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.3.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.3.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.4.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.4.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.3.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.3.md
status: DRAFT
---

# DORA Art. 30

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-DORA-012 | Rights and obligations in ICT third-party contractual arrangements are clearly allocated and set out in writing, including the minimum elements (a)–(i) of Art. 30(2); the financial entity (or an appointed third party) and the competent authority have unrestricted rights of access, inspection and audit, including the right to take copies of relevant documentation on-site if critical to the operations of the ICT third-party service provider, the effective exercise of which is not impeded or limited by other contractual arrangements or implementation policies, with the possibility to agree on alternative assurance levels if other clients' rights are affected. | `DORA-C37` (Art. 30(1)+(2) `clearly allocated` + closed list of 9 minimum elements (a)–(i)); `DORA-C38` (Art. 30(3)(e)(i)+(ii) `unrestricted` universal + `if other clients' rights are affected` qualification + `alternative assurance levels`) | D-06.3, D-06.4 |
| SO-DORA-012 | D-06.3, D-06.4 | Art. 30(1)–(3) | Contracts (minimum elements) + audit rights |

## Security Rules (from 02_SecurityRules_NIST.md)

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
- sr_id: SR-DORA-020
  title: "Information-security standards compliance for ICT third-party contracts"
  source_clauses:
    - { clause_id: DORA-C36, article_ref: "Art. 28(5) — `financial entities may only enter into contractual arrangements with ICT third-party service providers that comply with appropriate information security standards. When those contractual arrangements concern critical or important functions, financial entities shall … take due consideration of the use, by ICT third-party service providers, of the most up-to-date and highest quality information security standards`" }
  linked_objectives: [SO-DORA-011]
  sub_domain: [D-06.3]
  nist_csf_mapping:
    - { id: GV.SC-01, title: "A cybersecurity supply chain risk management program, strategy, objectives, policies, and processes are established and agreed to by organizational stakeholders" }
    - { id: GV.SC-03, title: "Contracts with suppliers and other third parties are used to implement appropriate measures designed to meet the objectives of an organization's cybersecurity program" }
  applies_to_role: [FINANCIAL_ENTITY, ICT_THIRD_PARTY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 28(5) requires financial entities to enter only into contractual
    arrangements with ICT third-party service providers that comply with
    appropriate information security standards; for contractual arrangements
    concerning critical or important functions, the financial entity shall
    take due consideration of the use by providers of the most up-to-date and
    highest quality information security standards. The clause carries the
    central DORA ambiguity flagged in `../Regulation/DORA/Ambiguity/05_DORA.md` §3.5: the OJ text does not
    name a specific standard — ISO/IEC 27001, SOC 2, NIST CSF, CIS Controls,
    and ENISA guidance are all plausible reference points, and EBA Guidelines
    on outsourcing arrangements provide the supervisory-recognised floor for
    critical or important functions outsourcing. The clause co-exists with
    CRA Art. 24 conformity-assessment duties for ICT products supplied under
    contract (Regulation (EU) 2024/2847) and with the GDPR Art. 32 security-
    of-processing baseline. An EBA RTS under Art. 28(9) is expected to refine
    the standards-set for CTPPs but has not closed the open-naming question.
  security_rationale: |
    The Art. 28(5) standards-compliance duty is operationalised in NIST CSF
    2.0 through **GV.SC-01 (A cybersecurity supply chain risk management
    program, strategy, objectives, policies, and processes are established
    and agreed to by organizational stakeholders)** and **GV.SC-03 (Contracts
    with suppliers and other third parties are used to implement appropriate
    measures designed to meet the objectives of an organization's cybersecurity
    program)**. GV.SC-01 establishes the entity-wide supply-chain cybersecurity
    governance that articulates which information-security standards the entity
    treats as acceptable baselines — the very `appropriate information security
    standards` that the OJ text leaves POLY — and the criteria for distinguishing
    between routine and critical-or-important-function contracts. GV.SC-03
    converts that governance into enforceable contract terms, ensuring that
    the `most up-to-date and highest quality` anchor for critical-or-important
    functions is reflected in measurable contract clauses (certification
    evidence, audit-rights linkage to Art. 30(3)(e), sub-outsourcing
    transparency). Together these two subcategories close the gap between an
    entity's stated standards-set and the contractual surface with third-party
    providers, allowing ex-post demonstration under Art. 28(5) that every
    ICT-service contract was anchored in a documented program-level standards
    framework and tied back through enforceable contract terms — satisfying
    both the general `appropriate` floor and the critical-or-important
    `most up-to-date AND highest quality` escalator.
  ambiguity_notes: |
    S3 POLY on `information security standards` — the central DORA ambiguity
    per `../Regulation/DORA/Ambiguity/05_DORA.md` §3.5: the clause names no specific standard. The chosen
    reading is entity-selected standards with supervisory-recognised standards
    (ISO/IEC 27001, SOC 2 Type 2, NIST CSF, ENISA guidance, EBA Guidelines)
    as the EU-acceptable floor. S3 POLY on `most up-to-date` is read against
    alternatives of current published version, state-of-the-art, or frontier
    practice. S3 VAG on `highest quality` is read at the literal most-
    rigorous, comprehensive, industry-leading end of the spectrum. S3 COORD
    on `most up-to-date AND highest quality` — both anchors required
    cumulatively. S2 POLY on `critical or important functions` — the
    undefined distinction propagates from `../Regulation/DORA/Ambiguity/05_DORA.md` §3.4. Compliance-
    framework note: ISO 27001, NIST 800-53, and EBA Guidelines function as
    reference frameworks rather than technology selections and are not part
    of the tech-stack exemption. Remain open: identification of the binding
    standards-set for CTPP designation remains subject to EBA RTS under
    Art. 28(9) and to the Joint Committee oversight of CTPPs at Ch. V Sec. 2.
```

### SO-DORA-001 (CIA + A maintained across data states)

```yaml
- sr_id: SR-DORA-021
  title: "Minimum contractual elements for ICT third-party arrangements"
  source_clauses:
    - { clause_id: DORA-C37, article_ref: "Art. 30(1)+(2) — `rights and obligations … shall be clearly allocated and set out in writing … shall include at least the following elements (a)–(i)`" }
  linked_objectives: [SO-DORA-012]
  sub_domain: [D-06.3]
  nist_csf_mapping:
    - { id: GV.SC-03, title: "Contracts with suppliers and other third parties are used to implement appropriate measures designed to meet the objectives of an organization's cybersecurity program" }
    - { id: GV.SC-04, title: "Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations" }
  applies_to_role: [FINANCIAL_ENTITY, ICT_THIRD_PARTY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 30(1) requires that the rights and obligations of the financial entity
    and the ICT third-party service provider be clearly allocated and set out
    in writing; Art. 30(2) requires that the contractual arrangements include
    at least the minimum elements (a)–(i), covering description of functions,
    locations, data, access and audit rights, SLAs, termination, and exit
    strategies. The clause sits in the contractual core of the DORA third-party
    regime alongside Art. 28(5) (standards compliance) and Art. 30(3)(e)
    (audit rights), with EBA Guidelines on outsourcing arrangements providing
    the supervisory baseline and with the open question of harmonised template
    elements pending EBA technical standards under Art. 30(7). The clause
    parallels — without replacing — GDPR Art. 28 controller-processor contract
    requirements for personal-data processing.
    [OJ-corrective note (v0.2 audit, material): Art. 30(2) — audit rights and exit strategies misattributed. OJ Art. 30(2) lists minimum contractual elements (a)–(i) for ICT-service contracts; `audit rights` are in Art. 30(3)(e)(i) (CIF-only) and `exit strategies` are in Art. 30(3)(f) (CIF-only). The SR's 7-item gloss misattributes both to Art. 30(2), leading a compliance officer to require these for all ICT-service contracts when OJ only requires them for CIF-supporting contracts (with microenterprise carve-outs in Art. 30(3)).]
  security_rationale: |
    The Art. 30(1)+(2) minimum contractual-elements duty is operationalised in
    NIST CSF 2.0 through **GV.SC-03 (Contracts with suppliers and other third
    parties are used to implement appropriate measures designed to meet the
    objectives of an organization's cybersecurity program)** and **GV.SC-04
    (Suppliers and other third parties are routinely assessed using audits,
    test results, or other forms of evaluation to confirm they are meeting
    their contractual obligations)**. GV.SC-03 anchors the contractual
    surface as the execution instrument of supply-chain cybersecurity —
    the nine-element minimum list in Art. 30(2) (functions, locations,
    data, access, audit rights linkage, SLAs, termination, exit strategies,
    and the sub-outsourcing transparency expectation) maps directly onto
    GV.SC-03's `appropriate measures` contract design, ensuring that the
    `clearly allocated and set out in writing` Art. 30(1) requirement is
    operationalised through enforceable clauses. GV.SC-04 closes the
    downstream verification loop: the contractual allocation is only as
    reliable as the routine assessment that confirms delivery against it,
    which feeds the audit-rights Art. 30(3)(e)(i) (CIF-only) and exit-
    strategy Art. 30(3)(f) (CIF-only) obligations separately mapped at
    SR-DORA-022. Together these two subcategories convert a written
    contract into an enforceable supply-chain control, and an entity
    evidencing GV.SC-03 contract design plus GV.SC-04 routine assessment
    can demonstrate ex-post to the competent authority that the Art. 30
    minimum-elements obligation was met and that contract-level controls
    were routinely verified — closing both the formal-allocation axis
    and the operational-performance axis of the third-party regime.
  ambiguity_notes: |
    S2 VAG on `clearly allocated` is read in the operational sense of being
    unambiguous on rights and obligations under contractual-construction
    conventions. S2 COORD on the closed list of nine minimum elements is read
    as all nine required (closed-list reduction of ambiguity). S2 VAG on
    `at least` is read as a minimum floor; additional elements are permitted.
    Remain open: harmonised contract templates from EBA under Art. 30(7) are
    pending and may crystallise supervisory expectations on `clearly
    allocated` (especially exit-strategy granularity and sub-outsourcing
    transparency).
```

### SO-DORA-001 (CIA + A maintained across data states)

```yaml
- sr_id: SR-DORA-022
  title: "Unrestricted audit rights over critical ICT third-party providers"
  source_clauses:
    - { clause_id: DORA-C38, article_ref: "Art. 30(3)(e)(i)+(ii) — `unrestricted rights of access, inspection and audit by the financial entity, or an appointed third party, and by the competent authority … the right to take copies of relevant documentation on-site … the right to agree on alternative assurance levels if other clients' rights are affected`" }
  linked_objectives: [SO-DORA-012]
  sub_domain: [D-06.4]
  nist_csf_mapping:
    - { id: GV.SC-03, title: "Contracts with suppliers and other third parties are used to implement appropriate measures" }
    - { id: DE.CM-06, title: "External service provider activities and services are monitored to find potentially adverse events" }
  applies_to_role: [FINANCIAL_ENTITY, ICT_THIRD_PARTY]
  obligation_type: [CONTINUOUS, TRIGGERED]
  regulatory_rationale: |
    Art. 30(3)(e)(i) requires contractual arrangements to include unrestricted
    rights of access, inspection and audit by the financial entity (or an
    appointed third party) and by the competent authority, including the right
    to take copies of relevant documentation on-site, the effective exercise of
    which is not impeded or limited by other contractual arrangements or
    implementation policies. Art. 30(3)(e)(ii) permits the right to agree on
    alternative assurance levels where other clients' rights are affected. The
    clause operationalises the financial-entity verification axis of Art. 28
    and runs in parallel with — and does not substitute for — the supervisory
    audit powers under EBA Guidelines on outsourcing arrangements and with the
    CTPP Joint Committee oversight under Ch. V Sec. 2. EBA technical
    standards are expected to refine the form of alternative-assurance levels
    under Art. 30(7).
  security_rationale: |
    The Art. 30(3)(e)(i)+(ii) audit-rights duty is operationalised in NIST
    CSF 2.0 through **GV.SC-03 (Contracts with suppliers and other third
    parties are used to implement appropriate measures designed to meet the
    objectives of an organization's cybersecurity program)** and **DE.CM-06
    (External service provider activities and services are monitored to find
    potentially adverse events)**. GV.SC-03 anchors the contractual surface:
    the unrestricted-rights clause — access, inspection, audit, on-site copy
    taking — must be expressed in enforceable contract terms that pre-empt
    supplier-side carve-outs, sub-outsourcing dilution, or competing-client
    confidentiality claims, with the alternative-assurance-level exception
    of Art. 30(3)(e)(ii) narrowly bounded. DE.CM-06 layers the operational
    monitoring dimension, ensuring that the contract-level right translates
    into continuous surveillance of external service-provider activities so
    that adverse events at the supplier are detected and routed into the
    entity's incident-response process under Art. 17 before they cascade.
    Together these two subcategories convert a paper audit-right into a
    live detection-and-verification capability, and an entity evidencing
    GV.SC-03 contract design plus DE.CM-06 ongoing monitoring can
    demonstrate ex-post to the competent authority that the Art. 30(3)(e)
    unrestricted-rights obligation was both contractually anchored and
    operationally exercised — closing the gap between formal right and
    effective use that has historically caused post-incident forensics
    to stall at the supplier boundary.
  ambiguity_notes: |
    S3 SCOPE-Q (Berry §5.2.1) on `unrestricted` — the universal quantifier
    is qualified immediately by `if other clients' rights are affected`;
    the chosen reading is that `unrestricted` is the default rule with the
    `other clients' rights` exception permitting alternative-assurance levels
    on a case-by-case basis. S3 VAG on `relevant documentation` is read at
    the directly-material-evidence end of the spectrum, with the alternative
    of any plausible link reserved for residual cases. S3 VAG on `critical to
    the operations` is read at the literal entity-judgement default. S2 POLY
    on `access, inspection AND audit` — three distinct activities, the
    chosen reading is the literal AND. Remain open: the operational
    thresholds for `other clients' rights are affected` remain to be refined
    through EBA technical standards and through case-by-case bilateral
    negotiations until a market convention crystallises.
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

