---
document_id: AEGIS-PREPROC-AI_Act-ART-33
title: AI_Act Art. 33 — SecurityObjectives & SecurityRules
regulation: AI_Act
article: Art. 33
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
status: DRAFT
---

# AI_Act Art. 33

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

_No standalone SO row cites this article directly (covered via the rules below)._

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

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

