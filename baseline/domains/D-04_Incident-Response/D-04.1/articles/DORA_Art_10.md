---
document_id: AEGIS-PREPROC-DORA-ART-10
title: DORA Art. 10 — SecurityObjectives & SecurityRules
regulation: DORA
article: Art. 10
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.1.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.1.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.1.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.1.md
status: DRAFT
---

# DORA Art. 10

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-DORA-007 | Anomalous activities — including ICT network performance issues and ICT-related incidents — are promptly detected through detection mechanisms that enable multiple layers of control, define alert thresholds and criteria, trigger and initiate ICT-related incident response processes, and identify potential material single points of failure. | `DORA-C20` (Art. 10(1) prompt detection + SPOF identification + `anomalous` POLY); `DORA-C21` (Art. 10(2) multiple layers + alert thresholds + auto-alert to relevant staff) | D-04.1, D-10.1 |
| SO-DORA-007 | D-04.1, D-10.1 | Art. 10(1) + Art. 10(2) | Anomalous activity detection with multi-layered controls |

## Security Rules (from 02_SecurityRules_NIST.md)

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

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

