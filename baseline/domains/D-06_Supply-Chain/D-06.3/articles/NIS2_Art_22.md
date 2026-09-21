---
document_id: AEGIS-PREPROC-NIS2-ART-22
title: NIS2 Art. 22 — SecurityObjectives & SecurityRules
regulation: NIS2
article: Art. 22
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.3.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.3.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.2.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.2.md
status: DRAFT
---

# NIS2 Art. 22

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-NIS2-016 | The results of EU-level coordinated security risk assessments of critical supply chains (Cooperation Group + Commission + ENISA under Art. 22(1)) are taken into account in supplier-risk decisions. | `NIS2-CL21` (Art. 21(3) sentence 2 — entity `take into account` Art. 22 results); `NIS2-CL23` (Art. 22(1) — Cooperation Group coordinated assessments); `NIS2-CL24` (Art. 22(1) — technical and, where relevant, non-technical risk factors); `NIS2-CL25` (Art. 22(2) — Commission selection) | D-06.3, D-09.2 |
| SO-NIS2-016 | D-06.3, D-09.2 | Art. 21(3) sentence 2 + Art. 22(1) | Take into account EU-level coordinated supply-chain risk assessments |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-025
  title: "Coordinated supply-chain risk assessments integrated into supplier decisions"
  source_clauses:
    - { clause_id: NIS2-CL21, article_ref: "Art. 21(3) sentence 2 — entity `take into account` Art. 22 results" }
    - { clause_id: NIS2-CL23, article_ref: "Art. 22(1) — Cooperation Group coordinated assessments" }
    - { clause_id: NIS2-CL24, article_ref: "Art. 22(1) — technical and, where relevant, non-technical risk factors" }
  linked_objectives: [SO-NIS2-016]
  sub_domain: [D-06.3, D-09.2]
  nist_csf_mapping:
    - { id: ID.RA-02, title: "Threat and vulnerability information received from internal and external sources is collected and used to support risk identification" }
    - { id: GV.SC-02, title: "Suppliers and other third parties are known, prioritized, and assessed using a cybersecurity supply chain risk management process" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [PER-ASSESSMENT]
  regulatory_rationale: |
    Article 21(3) sentence 2 of Directive (EU) 2022/2555 requires essential and important entities, when considering which of the Article 21(2)(d) measures are appropriate, to take into account the results of the coordinated security risk assessments of critical supply chains carried out in accordance with Article 22(1). Article 22(1) enables the Cooperation Group, in cooperation with the Commission and ENISA, to carry out coordinated assessments of specific critical ICT services, ICT systems or ICT products supply chains, taking into account technical and, where relevant, non-technical risk factors. The chain is therefore Article 22(1) institutional → Article 21(3) sentence 2 entity-implementable; the SR captures the entity-side propagation hook.
  security_rationale: |
    The obligation in Art. 21(3) sentence 2 to take into account the results of Article 22(1) coordinated supply-chain risk assessments is operationalised in NIST CSF 2.0 through **ID.RA-02 (Threat and vulnerability information received from internal and external sources is collected and used to support risk identification)** and **GV.SC-02 (Suppliers known, prioritised, and assessed using a C-SCRM process)**. ID.RA-02 anchors the ingestion of Article 22 institutional outputs into the entity's threat-and-vulnerability register: the Cooperation Group's coordinated assessments, in cooperation with the Commission and ENISA, are treated as authoritative external threat intelligence that no individual entity could replicate from internal sources alone. GV.SC-02 then requires that this intelligence propagate into the supplier-risk decisions, so that Article 22 outputs alter the prioritisation, contractual escalation or substitution decisions on assessed suppliers. Together, ID.RA-02 and GV.SC-02 convert a fragmented national view into a harmonised European baseline for supplier remediation. The control set enables ex-post demonstration that the entity's supplier-risk register reflects the latest Union-scale supply-chain threat picture with documented propagation from external intelligence to internal decision.
  ambiguity_notes: |
    The verb `take into account` admits two operative readings: a passive-consideration reading (the entity reviews the assessment and files it) or an active-integration reading (the entity updates its supplier-risk register to reflect the assessment), with the chosen reading being the literal passive-consideration reading since Article 21(3) sentence 2 does not prescribe a specific decision mechanism. The Article 22(1) chapeau `may carry out` carries the same hybrid discretion/conditional pattern, so that the entity's obligation is triggered only when an Article 22(1) assessment actually exists for a relevant supply chain. Member State transposition divergence may apply on the documentation expected to evidence `taken into account`. Remain open: whether the Commission will publish a standardised mechanism under Article 22(2) (NIS2-CL25) for flagging specific critical ICT subject to assessment in a way that makes the entity-side `take into account` check trivially operational, or whether each entity must monitor the Cooperation Group outputs independently.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

