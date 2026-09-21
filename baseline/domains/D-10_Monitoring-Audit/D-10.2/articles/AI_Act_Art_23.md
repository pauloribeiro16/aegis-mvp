---
document_id: AEGIS-PREPROC-AI_Act-ART-23
title: AI_Act Art. 23 — SecurityObjectives & SecurityRules
regulation: AI_Act
article: Art. 23
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.2.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.2.md
status: DRAFT
---

# AI_Act Art. 23

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

_No standalone SO row cites this article directly (covered via the rules below)._

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-AIACT-001 (AI risk management lifecycle)

```yaml
- sr_id: SR-AIACT-007
  title: "Lifetime automatic logging of high-risk AI system events"
  source_clauses:
    - { clause_id: AIA-C09, article_ref: "Art. 12(1) — `High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system`" }
    - { clause_id: AIA-C10, article_ref: "Art. 12(2) — `In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) … (b) … (c) …`" }
  linked_objectives: [SO-AIACT-005]
  sub_domain: [D-10.2]
  nist_csf_mapping:
    - { id: PR.PS-04, title: "Log records are generated and made available for continuous monitoring and analysis" }
    - { id: DE.CM-09, title: "Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events" }
    - { id: DE.AE-03, title: "Event data are collected and correlated from multiple sources and sensors" }
  applies_to_role: [PROVIDER]
  obligation_type: [CONTINUOUS, ONE_TIME]
  regulatory_rationale: |
    Article 12(1) of the AI Act requires that high-risk AI systems
    technically allow for the automatic recording of events (logs)
    over the lifetime of the system. Article 12(2) operationalises
    this requirement by mandating that logging capabilities ensure a
    level of traceability of the functioning of the high-risk AI
    system that is appropriate to the intended purpose of the
    system, by enabling the recording of events relevant for
    ensuring traceability of the functioning of the system,
    monitoring its operation, and facilitating post-market
    monitoring under Article 72. Together the two paragraphs form
    the log-generation and log-capability substrate for the AI-Act
    post-market-monitoring apparatus. The lifetime-scope qualifier
    ties logging into the broader lifecycle obligations under
    Articles 9 and 17 and mirrors the log-retention duty that DORA
    Article 12 places on financial entities and that NIS 2 Article
    21 places on essential and important entities.
  security_rationale: |
    The obligation in Art. 12(1)–(2) is operationalised in NIST
    CSF 2.0 through **PR.PS-04 (Log records are generated and
    made available for continuous monitoring and analysis)**,
    **DE.CM-09 (Computing hardware and software, runtime
    environments, and their data are monitored to find potentially
    adverse events)**, and **DE.AE-03 (Event data are collected
    and correlated from multiple sources and sensors)**. PR.PS-04
    anchors the lifetime automatic-event-recording substrate — the
    provider must technically enable log generation across the full
    AI-system lifecycle, including AI-specific events (inference
    decisions, model decisions, override events) implied by the
    `functioning of a high-risk AI system` opening of Art. 12(2)
    beyond conventional security logs. DE.CM-09 covers the
    runtime-monitoring dimension of the three-element purpose list
    (traceability, monitoring, post-market monitoring), supporting
    live operational monitoring alongside post-incident
    reconstruction. DE.AE-03 supplies the cross-source event
    correlation that converts the raw log stream into an
    audit-grade narrative, including cross-regulation flows under
    NIS 2 Art. 23 and DORA Art. 19. A provider documenting
    PR.PS-04 log generation, DE.CM-09 continuous-monitoring
    coverage and DE.AE-03 multi-source correlation demonstrates
    ex post that the Art. 12(1)–(2) lifetime logging duty —
    including AI-specific events beyond conventional security logs
    — is reconstructable for supervisory review.
  ambiguity_notes: |
    The phrase `over the lifetime` is vague and undefined in the
    AI Act; the chosen reading aligns lifetime with the
    product-lifecycle definition in Article 3(1)(c), by analogy
    with the CRA support-period concept in CRA Article 13(8). The
    phrase `events (logs)` is poly-semous, since AI-specific events
    such as inference events, model-decision events and override
    events are not enumerated in the Act; the chosen reading is
    broad, covering AI-specific events per the `functioning of a
    high-risk AI system` opening of Article 12(2). As an
    alternative, providers could read `events` as security-event
    logs familiar from DORA and NIS 2, which is narrower and
    excludes AI-specific inference-decision events. The phrase
    `appropriate to the intended purpose` in Article 12(2) is
    vague, and the term `traceability` is poly-semous between
    ML-ops training-run reproducibility, runtime decision
    audit-trail traceability and data-lineage traceability; the
    chosen reading is cumulative, covering all three senses. The
    three-element list in Article 12(2) (a)–(c) is AND-coordinated.
    Remain open: whether `over the lifetime` aligns lifetime
    duration with the deployer's deployment window or with the
    manufacturer's broader product-lifecycle window extending into
    post-decommissioning support obligations.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

