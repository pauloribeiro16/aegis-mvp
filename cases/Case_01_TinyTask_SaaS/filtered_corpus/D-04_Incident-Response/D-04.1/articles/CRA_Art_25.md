---
document_id: AEGIS-PREPROC-CRA-ART-25
title: CRA Art. 25 — SecurityObjectives & SecurityRules
regulation: CRA
article: Art. 25
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

# CRA Art. 25

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

_No standalone SO row cites this article directly (covered via the rules below)._

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-027
  title: "Product internal-activity recording with user opt-out"
  source_clauses:
    - { clause_id: CRA-CL141, article_ref: "Annex I Part I (2)(l) — recording + monitoring + user opt-out" }
    - { clause_id: CRA-CL158, article_ref: "Annex II §8 — detailed instructions" }
  linked_objectives: [SO-CRA-020, SO-CRA-068]
  sub_domain: [D-10.1, D-04.1]
  nist_csf_mapping:
    - { id: PR.PS-04, title: "Log records are generated and made available for continuous monitoring and analysis" }
    - { id: DE.AE-08, title: "Incidents are declared when adverse events meet the defined incident criteria" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Annex I Part I (2)(l) requires products with digital elements to provide security-related information by recording and monitoring relevant internal activity — including the access to or modification of data, services, or functions — with an opt-out mechanism for the user. The clause is the product-side mirror of the manufacturer-side access reporting under Annex I (2)(d) (SR-CRA-024) and is supported by Annex II §8, which requires the manufacturer to provide the user with detailed instructions on how the product records and monitors activity and how the opt-out can be exercised. For a compliance officer the operational reading is: log generation on by default, opt-out discoverable, instructions published under Annex II §8, and the security-event lifecycle properly interfaced with downstream incident-management obligations under Art. 14.
  security_rationale: |
    The Annex I Part I (2)(l) + Annex II section 8 internal-activity recording obligation is operationalised in NIST CSF 2.0 through **PR.PS-04 (log records generated and made available for continuous monitoring and analysis)** and **DE.AE-08 (incidents declared when adverse events meet the defined incident criteria)**. PR.PS-04 anchors the log-generation leg: the manufacturer instruments the product to generate log records covering the relevant-internal-activity data class identified by the Art. 13(2) risk assessment, with logs made available for the continuous-monitoring pipeline that consumes them. DE.AE-08 captures the incident-declaration dimension: the recorded events feed into the incident-criteria-evaluation pipeline so that events meeting the criteria are declared as incidents and routed into the Art. 14 reporting architecture (SR-CRA-028 / SR-CRA-031), closing the loop from local product-side recording to upstream regulatory notification. Together PR.PS-04 and DE.AE-08 enable the manufacturer to demonstrate ex post, through documented log-retention evidence, monitoring-pipeline records, and incident-declaration timestamps, that the (2)(l) recording duty has been exercised across the support period and that the upstream declaration pathway is operable when the recorded events meet the criteria.
  ambiguity_notes: |
    The phrase "opt-out mechanism for the user" in Annex I Part I (2)(l) is VAG-S2 because "opt-out" admits at least three materially distinct operational readings. Reading chosen: R1 (the user can disable logging entirely), preserving the literal OJ text. The opt-out creates a privacy-by-design tension: GDPR Art. 25 emphasises by-default-on privacy controls under certain readings, but the OJ CRA text on this clause is opt-out; rule preserves the OJ-literal opt-out interpretation rather than importing non-CRA framings. No S3 instance is introduced on this rule.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

