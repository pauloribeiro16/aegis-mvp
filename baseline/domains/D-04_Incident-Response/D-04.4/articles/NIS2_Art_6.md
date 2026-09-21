---
document_id: AEGIS-PREPROC-NIS2-ART-6
title: NIS2 Art. 6 — SecurityObjectives & SecurityRules
regulation: NIS2
article: Art. 6
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-01_Data-Protection/D-01.1.md
  - ../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.1.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.1.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.1.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.2.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.2.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.4.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.4.md
status: DRAFT
---

# NIS2 Art. 6

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

_No standalone SO row cites this article directly (covered via the rules below)._

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-001
  title: "Documented cryptography and encryption governance baseline"
  source_clauses:
    - { clause_id: NIS2-CL17, article_ref: "Art. 21(2)(h) — cryptography and, where appropriate, encryption" }
    - { clause_id: NIS2-CL07, article_ref: "Art. 21(1) — appropriate and proportionate (propagates)" }
    - { clause_id: NIS2-CL08, article_ref: "Art. 21(1) sentence 2 — state-of-the-art + standards + cost" }
    - { clause_id: NIS2-D01, article_ref: "Art. 6(1) — network and information system (cross)" }
    - { clause_id: NIS2-D02, article_ref: "Art. 6(2) — security of network and information systems" }
  linked_objectives: [SO-NIS2-001]
  sub_domain: [D-01.1]
  nist_csf_mapping:
    - { id: PR.DS-01, title: "Data-at-rest protected" }
    - { id: PR.DS-02, title: "Data-in-transit protected" }
    - { id: GV.RM-04, title: "Strategic direction on identifying and responding to risks established and communicated" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 21(2)(h) of Directive (EU) 2022/2555 (NIS2) requires essential and important entities to establish policies and procedures regarding the use of cryptography and, where appropriate, encryption. The opening qualifier of Article 21(1) — that the technical, operational and organisational measures taken must be appropriate and proportionate to the risks posed — propagates to this sub-point, and Article 21(1) sentence 2 anchors the baseline against the state of the art, relevant European and international standards, and the cost of implementation (OJ L 333, 27.12.2022, p. 127). The four CIA-A dimensions of Article 6(2) — availability, authenticity, integrity and confidentiality of stored, transmitted or processed data — define what cryptography is to protect. Article 6(1) provides the operational scope by defining network and information systems through three coordinated sub-clauses (electronic communications networks; interconnected devices; digital data stored, processed, retrieved or transmitted). The Directive deliberately fuses cryptography as a discipline (algorithm selection, key management, protocol design) with encryption as a sub-technique applied where the risk assessment demands it, and leaves the application thresholds to the entity under the appropriate-and-proportionate qualifier (Recital 56). For the software-compliance track this means a documented cryptography policy that maps algorithms to data classifications and references the European standards landscape (ETSI TS 103 744 series on quantum-safe migration, ISO/IEC 27001:2022 Annex A.10 Cryptographic controls).
  security_rationale: |
    The obligation in Article 21(2)(h) of Directive (EU) 2022/2555 to establish policies and procedures regarding the use of cryptography and, where appropriate, encryption is operationalised in NIST CSF 2.0 through **PR.DS-01 (Data-at-rest protected)**, **PR.DS-02 (Data-in-transit protected)** and **GV.RM-04 (Strategic direction on identifying and responding to risks established and communicated)**. PR.DS-01 anchors the cryptographic protection of stored data — algorithm selection, key-management lifecycle (generation, distribution, storage, rotation, revocation, destruction), and decommissioning of deprecated primitives on a known schedule. PR.DS-02 extends the same discipline to data in motion, translating cryptographic policy into mutually-authenticated transport between services, between entity and recipient, and between the entity and the supervisory authority during incident reporting. GV.RM-04 supplies the governance superstructure that converts ad-hoc algorithm choice into a position the entity can defend at audit. Together the three subcategories generate the policy artefacts, key-management records and review-cadence evidence that the Article 21(1) risk-management framework requires an entity to assemble to demonstrate, ex post, that its cryptographic posture is appropriate, proportionate and state-of-the-art.
  ambiguity_notes: |
    Article 21(2)(h) carries two compounding S3 ambiguities that drive materially different compliance obligations. First, the `cryptography and, where appropriate, encryption` conjunction is a hierarchical AND-with-hedge: cryptography is always required (a policy must address cryptographic mechanisms as a discipline) but encryption is additionally required only where the entity's risk assessment indicates it; the alternative reading that cryptography and encryption are synonyms is rejected by the literal text and by the CRA parallel (CRA Art. 13(2) on default passwords, Art. 14(2) on vulnerability remediation, treat cryptography and encryption as distinct concepts). Second, `state of the art` in Article 21(1) sentence 2 admits three readings — current best practice (qualitative), published standards (e.g. ISO/IEC 27001:2022, NIST CSF 2.0), or cutting-edge frontier research — of which the third is rejected by Recital 56 (cost of implementation implies off-the-shelf); the chosen reading accepts both R1 best practice and R2 published standards as operative, with ENISA's 2022 baseline guidance as the practical floor. Member State transposition divergence may apply on `state of the art`: the German BSI standardises the term through BSI TR-02102; French ANSSI requires an independent assessment by a qualified body; Italian ACN publishes annual guidance. The substantive software-compliance consequence is that a 5-FTE SaaS entity and a 500-FTE operator may both satisfy Article 21(2)(h) with materially different documentation depth, provided each documents the proportionality decision. Remain open: (a) whether the European Commission implementing acts under Article 21(5) will specify a baseline cryptography standard or only methodological requirements (the 17 October 2024 deadline has slipped to mid-2025 without publication as of the current reference date); (b) whether Member State national transposition will impose sector-specific cryptography mandates beyond the Directive... (line truncated to 2000 chars)
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-008
  title: "Incident handling as a six-action lifecycle"
  source_clauses:
    - { clause_id: NIS2-CL11, article_ref: "Art. 21(2)(b) — incident handling" }
    - { clause_id: NIS2-D06, article_ref: "Art. 6(8) — incident handling definition (6-action list: prevent, detect, analyse, contain, respond, recover)" }
    - { clause_id: NIS2-CL07, article_ref: "Art. 21(1) — appropriate and proportionate (propagates)" }
  linked_objectives: [SO-NIS2-005, SO-NIS2-013]
  sub_domain: [D-04.1, D-04.2, D-04.4]
  nist_csf_mapping:
    - { id: RS.MA-01, title: "Incident management plan executed in coordination with relevant third parties once an incident is declared" }
    - { id: RS.AN-03, title: "Analysis performed to determine what has occurred during an event and the root cause of the event" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [CONTINUOUS, TRIGGERED]
  regulatory_rationale: |
    Article 21(2)(b) of Directive (EU) 2022/2555 requires essential and important entities to take measures regarding incident handling. Article 6(8) defines `incident handling` as all actions and procedures aiming at, where appropriate, preventing, detecting, analysing, containing and responding to and recovering from an incident (OJ L 333, 27.12.2022, p. 113) — a six-action process anchored in the Article 21(2) all-hazards approach (Article 21(2) chapeau) and the Article 6(2) CIA-A security-of-NIS definition. The Article 21(1) appropriate-and-proportionate qualifier propagates. The incident-handling capability is the operational substrate of the Article 23 reporting flow (SR-NIS2-010 to SR-NIS2-018) and the Article 21(2)(c) business-continuity hook (SR-NIS2-019). The 24-hour early-warning clock of Article 23(4)(a) starts upon the entity becoming aware of the significant incident; the entity's incident-handling capability is the apparatus that produces the awareness event in a defensible manner.
    [OJ-corrective note (v0.2 audit): the OJ text reads verbatim — Art. 6(8) defines `incident handling` as all actions and procedures aiming at, where appropriate, preventing, detecting, analysing, containing and responding to and recovering from an incident; the six actions are listed as gerunds conjunctively coordinated, not as four verbs + OR.]
  security_rationale: |
    The Article 21(2)(b) incident-handling obligation, anchored by the Article 6(8) six-action definition (prevent, detect, analyse, contain, respond, recover), is operationalised in NIST CSF 2.0 through **RS.MA-01 (The incident management plan is executed in coordination with relevant third parties once an incident is declared)** and **RS.AN-03 (Analysis is performed to determine what has occurred during an event and the root cause of the event)**. RS.MA-01 operationalises the coordination dimension — the entity's plan must specify, for each phase of the lifecycle, who executes, who is informed, and how the entity coordinates with the CSIRT, competent authority, single point of contact and any sectoral peers, preventing the plan from collapsing into a unilateral internal exercise. RS.AN-03 operationalises the analysis dimension: root-cause work, scope assessment and indicator-of-compromise extraction produce the evidence base on which both technical containment and the subsequent 24h/72h/1m regulatory reporting flows (SR-NIS2-010, SR-NIS2-011, SR-NIS2-012) depend. Together the two subcategories cover the two distinct cognitive demands of incident handling — coordination under uncertainty and analysis under time pressure — and generate the incident records, triage decisions and post-incident artefacts that constitute the Article 21(1) accountability evidence.
  ambiguity_notes: |
    `Incident handling` admits process/team/capability/programme readings; the chosen reading is process (R1) per the Article 6(8) `actions and procedures` anchor. The `aiming at, where appropriate` qualifier is read as illustrative (the six actions form a floor; the entity may add more — e.g. eradication, post-incident activity) rather than exhaustive. T3-vs-text gap awareness: T3 imports NIST SP 800-61 vocabulary not in the OJ text; the SR preserves the OJ six-action language. The handling capability is operationally triggered (process executed on incident declaration) and continuous (the capability is maintained). Member State transposition divergence may apply on incident-handling scope (whether the capability must operate 24/7; whether it must be staffed by named CSIRT-equivalent personnel or by a function that may include outsourced MSSPs); the Article 21(1) appropriate-and-proportionate qualifier is the basis for national variation. Remain open: whether the Commission's Article 21(5) implementing acts will specify a minimum 24/7 availability requirement for the incident-handling capability of essential entities in critical sectors (energy, transport, health, finance) — the Directive is silent on staffing continuity.
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-014
  title: "24-hour derogation notification for trust service providers"
  source_clauses:
    - { clause_id: NIS2-CL40, article_ref: "Art. 23(4) ¶2 — TSP 24h derogation" }
    - { clause_id: NIS2-D02, article_ref: "Art. 6(24) — trust service (eIDAS cross-reference)" }
  linked_objectives: [SO-NIS2-009]
  sub_domain: [D-04.3]
  nist_csf_mapping:
    - { id: RS.CO-04, title: "Coordination with stakeholders occurs consistent with applicable rules and regulations" }
    - { id: RS.MA-03, title: "Incidents are categorized, prioritized, and scoped" }
  applies_to_role: [ESSENTIAL_ENTITY]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 23(4) paragraph 2 of Directive (EU) 2022/2555 derogates from the Article 23(4)(b) 72-hour notification tier: a trust service provider shall, with regard to significant incidents that have an impact on the provision of its trust services, notify the CSIRT or, where applicable, the competent authority, without undue delay and in any event within 24 hours of becoming aware of the significant incident (OJ L 333, 27.12.2022, p. 129). The Article 6(24) definition of `trust service` references Regulation (EU) No 910/2014 (eIDAS), so the derogation applies to eIDAS-defined trust service providers and qualified trust service providers. Annex I of NIS 2 includes eIDAS qualified trust service providers as essential entities; Annex II includes digital providers as important entities, but the substantive eIDAS obligations attach to the QTSP designation regardless of the Annex II classification. The `applies_to_role: ESSENTIAL_ENTITY` reflects the Annex I/QTSP designation. The twin-trigger pattern (`without undue delay and in any event within 24 hours`) is identical to SR-NIS2-010 (same reading structure).
  security_rationale: |
    The Article 23(4) paragraph 2 derogation requiring trust service providers (per Article 6(24) and the eIDAS cross-reference) to submit a 24-hour notification for significant incidents affecting the provision of their trust services, derogating from the Article 23(4)(b) 72-hour tier, is operationalised in NIST CSF 2.0 through **RS.CO-04 (Coordination with stakeholders occurs consistent with applicable rules and regulations)** and **RS.MA-03 (Incidents are categorized, prioritized, and scoped)**. RS.CO-04 anchors the regulatory-clock discipline: the 24-hour tier is shorter than the 72-hour tier it derogates from, and the entity's procedure must ensure the trust-service-provision scope is correctly identified and the notification channel is the one designated for the TSP's national supervisory body and CSIRT. RS.MA-03 supplies the categorisation discipline on which the substantive content depends: the entity must distinguish trust-service-affecting incidents from non-trust-service incidents, and apply the more stringent tier only to the former, so that the derogation is targeted rather than generalised. The two subcategories together address the regulatory-clock dimension and the scope-discipline dimension of the TSP derogation. The resulting notification records and categorisation outputs supply the supervisory feed on which the cross-border eIDAS coordination depends and the accountability evidence under Article 21(1).
  ambiguity_notes: |
    The TSP derogation applies only to trust service providers as defined in Article 6(24) (the eIDAS cross-reference). The chosen reading is that the derogation applies to QTSPs (qualified trust service providers per Annex I) and to TSPs in scope of Article 6(24) more broadly (non-qualified trust service providers may be subject to the derogation if they meet the eIDAS trust-service definition). Member State transposition divergence may apply; national supervisory authorities may publish sector-specific guidance. Remain open: whether non-qualified TSPs in Annex II (important entity classification) can opt into the 24-hour derogation by agreement with the national CSIRT, or whether the derogation is reserved to Annex I QTSPs.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

