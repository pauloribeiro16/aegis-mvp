---
document_id: AEGIS-PREPROC-NIS2-ART-24
title: NIS2 Art. 24 — SecurityObjectives & SecurityRules
regulation: NIS2
article: Art. 24
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
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.4.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.4.md
status: DRAFT
---

# NIS2 Art. 24

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-NIS2-024 | Where required by a Member State in accordance with Art. 24(1), or by a Commission delegated act under Art. 24(2), essential and important entities use particular ICT products, ICT services, and ICT processes that are certified under European cybersecurity certification schemes adopted pursuant to Art. 49 of Regulation (EU) 2019/881 (Cybersecurity Act). | `NIS2-CL48` (Art. 24(1) sentence 1 — Member States `may require` certified ICT products/services/processes); `NIS2-CL49` (Art. 24(1) sentence 2 — qualified trust services encouragement); `NIS2-CL50` (Art. 24(2) — Commission delegated acts specifying categories of entities that must use certified products); `NIS2-CL51` (Art. 24(3) — ENISA candidate scheme request) | D-09.4, D-06.3 |
| SO-NIS2-024 | D-09.4, D-06.3 | Art. 24(1)/(2)/(3) | Use of certified ICT products/services/processes where required by MS or delegated act |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-043
  title: "European cybersecurity certification aligned with Article 21 requirements"
  source_clauses:
    - { clause_id: NIS2-CL48, article_ref: "Art. 24(1) sentence 1 — Member States `may require` certified ICT products/services/processes" }
    - { clause_id: NIS2-CL50, article_ref: "Art. 24(2) — Commission delegated acts (cross)" }
    - { clause_id: NIS2-CL49, article_ref: "Art. 24(1) sentence 2 — qualified trust services encouragement (cross)" }
  linked_objectives: [SO-NIS2-024]
  sub_domain: [D-09.4, D-06.3]
  nist_csf_mapping:
    - { id: GV.SC-04, title: "Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation" }
    - { id: GV.OC-03, title: "Legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [CONTINUOUS, PER-MS-REQUIREMENT]
  regulatory_rationale: |
    Article 24(1) sentence 1 of Directive (EU) 2022/2555 permits Member States to require essential and important entities to use particular ICT products, ICT services and ICT processes that are certified under European cybersecurity certification schemes adopted pursuant to Article 49 of Regulation (EU) 2019/881 (Cybersecurity Act), in order to demonstrate compliance with particular requirements of Article 21. Article 24(1) sentence 2 encourages the use of qualified trust services. Article 24(2) empowers the Commission to adopt delegated acts specifying which categories of entities are required to use certified products, services or processes, and on which European cybersecurity certification schemes those entities may rely, in particular where a Member State so requests. The SR is REFERENTIAL: the entity-side obligation is conditional on either Member-State exercise of the Article 24(1) permission or Commission adoption of Article 24(2) delegated acts. Until either trigger occurs, the SR is conditional; downstream Phase-1 filtering must apply the per-MS check.
  security_rationale: |
    The obligation in Art. 24(1) sentence 1 that Member States may require essential and important entities to use particular ICT products, ICT services and ICT processes that are certified under European cybersecurity certification schemes adopted pursuant to Article 49 of Regulation (EU) 2019/881 is operationalised in NIST CSF 2.0 through **GV.OC-03 (Legal, regulatory, and contractual requirements regarding cybersecurity are understood and managed)** and, by extension, **GV.SC-04 (Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation)** as the supplier-side attestation substrate. GV.OC-03 anchors the per-MS conditional register: the entity maintains a current register of the European cybersecurity certification schemes that the Member State has mandated for its sector, sub-sector, and entity category, and the particular Article 21 requirements that each scheme addresses. The register is conditional on either the Member-State exercise of the Article 24(1) permission or the Commission adoption of an Article 24(2) delegated act specifying the categories of entities that must use certified artefacts. The control set enables ex-post demonstration that the entity identified and met the certification requirements applicable to its sector under the OJ and the relevant Member State transposition, with the certification status reflected in the supplier register.
  ambiguity_notes: |
    Article 24 is REFERENTIAL: the entity-side obligation is conditional on Member-State exercise of the Article 24(1) permission or Commission adoption of Article 24(2) delegated acts. The verb `may require` carries an S3 VAG ambiguity on the conditionality locus: a pure-discretion reading (Member State may require without further condition), a compliance-conditioned reading (Member State may require only where the Member State identifies compliance gaps), or a Commission-conditioned reading (Member State may require only after a Commission delegated act specifies the categories), with the chosen reading being the pure-discretion reading because Article 24(1) sentence 1 is structurally permissive and the Commission-conditioned reading would be imposed only via Article 24(2). The compound `particular requirements of Article 21` admits an any-sub-point reading, a certification-relevant-sub-point reading, or a delegated-act-named-sub-point reading, with the chosen reading being the literal any-sub-point reading. The compound `ICT products, ICT services and ICT processes` admits three-distinct-objects, composite-object, or all-objects readings, with the three-distinct reading being literal. The qualifier `developed by the essential or important entity or procured from third parties` admits an entity-choice reading, a procured-only reading, or a both-equal reading, with the entity-choice reading being literal. The Article 24(2) trigger `insufficient levels of cybersecurity` admits an ENISA-measured reading, a national-CSA-measured reading, or an incident-statistics reading, with the ENISA-measured reading being literal. The compound `categories of essential and important entities` in Article 24(2) admits a sector-anchor reading (Annex I/II), a size-anchor reading, or a risk-anchor reading, with the sector-anchor reading being dominant because Annex I and Annex II of the Directive define the sectors and sub-sectors. Member State transposition divergence may apply: national transposition laws may operationalise Article 24(1) earlier than EU-level delegated acts, creating a heterogeneous landscape where an entity in Member State X must use certified artefacts while an entity in Member State Y does not. The Executor's SR maps to GV.SC-04 + GV.OC-03; until a Member State exercises the permission or the Commission adopts a delegated act, the SR is conditional. Remain open: (a) whether the Commission will adopt delegated acts under Article 24(2) by the 17 October 2024 deadline (which has slipped to mid-2025 without publication as of the current reference date), and on which European cybersecurity certification schemes they will rely; (b) whether the Article 24(1) Member-State discretion is constrained by the CRA (Regulation (EU) 2024/2847) horizontal cybersecurity baseline, since CRA-class products may attract mandatory certification that would convert the permissive Article 24(1) into a mandatory overlap.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

