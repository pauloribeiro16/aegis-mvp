---
document_id: AEGIS-PREPROC-DORA-ART-8
title: DORA Art. 8 — SecurityObjectives & SecurityRules
regulation: DORA
article: Art. 8
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
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.2.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.2.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.3.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.3.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.1.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.1.md
status: DRAFT
---

# DORA Art. 8

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-DORA-003 | Sources of ICT risk — including cyber threats and ICT vulnerabilities relevant to ICT supported business functions, information assets and ICT assets — are identified on a continuous basis; risk scenarios impacting the entity are reviewed on a regular basis, at least yearly. | `DORA-C06` (Art. 7(2) continuous basis + regular basis + yearly review); `DORA-C08` (Art. 8(2) `all sources of ICT risk` + risk exposure to/from other financial entities) | D-02.1, D-10.1 |
| SO-DORA-003 | D-02.1, D-10.1 | Art. 7(2) + Art. 8(2) | Continuous ICT risk identification + yearly review of risk scenarios |
| SO-DORA-018 | ICT systems and tools are continuously monitored and controlled for security and functioning, and the impact of ICT risk is minimised through the deployment of appropriate ICT security tools, policies and procedures; an information security policy defines rules to protect the availability, authenticity, integrity and confidentiality of data, information assets and ICT assets, including those of customers where applicable. | `DORA-C07` (Art. 8(1) `continuously monitor and control` + `security and functioning` AND + `tools, policies and procedures` 3-way AND); `DORA-C12` (Art. 9(4)(a) information security policy + nested AND of CIA+A 4-way of data/information assets/ICT assets 3-way) | D-10.1, D-10.2 |
| SO-DORA-018 | D-10.1, D-10.2 | Art. 8(1) + Art. 9(4)(a) | Continuous monitoring + information security policy |

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

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

