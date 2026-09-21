---
document_id: AEGIS-PREPROC-AI_Act-ART-83
title: AI_Act Art. 83 — SecurityObjectives & SecurityRules
regulation: AI_Act
article: Art. 83
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.1.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.1.md
status: DRAFT
---

# AI_Act Art. 83

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-AIACT-012 | A post-market monitoring system is established and documented in a manner that is proportionate to the nature of the AI technologies and the risks of the high-risk AI system, actively and systematically collecting, documenting and analysing relevant data to evaluate the AI system's continued compliance; market-surveillance cooperation under Regulation (EU) 2019/1020 applies to AI systems covered by the AI Act. | `AIA-C25` (Art. 72(1)–(2) — `proportionate to the nature` + `actively and systematically collect, document and analyse` 3-way verb AND + `post-market monitoring system` POLY borrows from MDR Art. 83); `AIA-C27` (Art. 74(1) — borrows the entire Regulation (EU) 2019/1020 market-surveillance framework; POLY cross-regulation borrow) | D-10.1 |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-AIACT-001 (AI risk management lifecycle)

```yaml
- sr_id: SR-AIACT-021
  title: "Post-market monitoring feedback loop with documented analysis"
  source_clauses:
    - { clause_id: AIA-C25, article_ref: "Art. 72(1)–(2) — `Providers shall establish and document a post-market monitoring system in a manner that is proportionate to the nature of the AI technologies and the risks of the high-risk AI system. The post-market monitoring system shall actively and systematically collect, document and analyse relevant data`" }
    - { clause_id: AIA-C27, article_ref: "Art. 74(1) — `Regulation (EU) 2019/1020 shall apply to AI systems covered by this Regulation`" }
  linked_objectives: [SO-AIACT-012]
  sub_domain: [D-10.1]
  nist_csf_mapping:
    - { id: DE.CM-09, title: "Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events" }
    - { id: ID.IM-04, title: "Cybersecurity risk management improvements are informed by awareness of related developments and context (e.g., threat intelligence, incidents, technology evolution)" }
    - { id: GV.OV-03, title: "Organizational cybersecurity performance is evaluated and reviewed for needed adjustments" }
  applies_to_role: [PROVIDER, DEPLOYER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 72(1)–(2) of Regulation (EU) 2024/1689 requires high-
    risk AI providers to establish and document a post-market
    monitoring (PMM) system proportionate to the AI technology
    and the risks of the system, actively and systematically
    collecting, documenting, and analysing relevant data. The
    PMM system feeds the lifecycle consistency duty of
    Art. 15(1) and the serious incident reporting duty of
    Art. 73. Art. 74(1) extends Regulation (EU) 2019/1020
    (the EU market-surveillance framework) to AI systems,
    imposing market-surveillance cooperation obligations on
    providers and deployers. Recital 80 frames the PMM
    obligation as parallel to — but distinct from — the
    medical-device PMM obligation under MDR Art. 83; the
    borrow is implicit (the OJ does not name the MDR).
    A compliance officer should treat the PMM system as the
    ex-post assurance loop that complements the ex-ante
    conformity assessment.
  security_rationale: |
    The Art. 72(1)–(2) post-market monitoring duty is
    operationalised in NIST CSF 2.0 through **DE.CM-09
    (Computing hardware, software, runtime environments and
    data monitored for adverse events)**, **ID.IM-04
    (Improvements informed by threat intelligence,
    incidents, technology evolution)**, and **GV.OV-03
    (Organisational cybersecurity performance evaluated and
    reviewed for needed adjustments)**, with supplementary
    alignment to **DE.AE-03 (Event data collected and
    correlated from multiple sources)**, **GV.PO-02
    (Cybersecurity processes and procedures established,
    communicated, enforced)**, and **GV.OC-03 (Legal,
    regulatory, contractual requirements understood and
    managed)**. DE.CM-09 is the principal anchor: it binds
    the PMM system to the runtime monitoring of the AI
    substrate (inference logs, telemetry, drift indicators)
    so that adverse events are detected in the operational
    environment, not just asserted at conformity-assessment
    time. ID.IM-04 closes the feedback loop by requiring the
    PMM data to inform risk-management improvements
    (Art. 9 + Art. 15(1) lifecycle consistency), with
    explicit reference to threat intelligence, incidents,
    and technology evolution. GV.OV-03 enforces the
    organisational performance-evaluation cadence — the
    PMM data must be reviewed and trigger adjustments, not
    merely archived. Supplementary DE.AE-03 ensures
    cross-source event correlation; GV.PO-02 anchors the
    PMM system in documented, communicated, and enforced
    processes; and GV.OC-03 ensures the PMM system
    understands and manages the Regulation (EU) 2019/1020
    market-surveillance framework extended by Art. 74(1).
    The combined control set yields a documented PMM plan,
    runtime telemetry, an event-correlation pipeline, a
    review cadence with minutes, an improvement register,
    and a market-surveillance cooperation procedure — the
    evidentiary substrate for ex post demonstration of
    compliance under the Art. 9 risk-management + Art. 15
    lifecycle consistency + Art. 72 PMM + Art. 73 incident
    reporting + Art. 74(1) market-surveillance
    accountability chain.
  ambiguity_notes: |
    Source clause AIA-C25 carries **S2** features (per
    `06_AI_Art.md` §2.25). `proportionate to the nature` and
    `relevant data` are VAG-2. `post-market monitoring system`
    is POLY-2 — borrows from medical-device regulation (MDR
    Art. 83) but applied to AI; the borrow is implicit and
    practitioners must be familiar with both regimes. The
    adverbial AND `actively AND systematically` and the
    3-way verb AND `collect, document AND analyse` are
    COORD-2. AIA-C27 (`market surveillance`) is POLY-2 and
    borrows the entire Regulation (EU) 2019/1020 framework
    — operators unfamiliar with 2019/1020 cannot read this
    clause self-contained (Berry §3.3.1 cross-regulation
    borrow). Remain open: (a) whether the PMM plan must
    be submitted to the market-surveillance authority or
    is held internally; (b) whether deployer-side PMM
    contributions are mandatory or optional.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

