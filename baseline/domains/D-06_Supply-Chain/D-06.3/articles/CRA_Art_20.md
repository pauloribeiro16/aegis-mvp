---
document_id: AEGIS-PREPROC-CRA-ART-20
title: CRA Art. 20 — SecurityObjectives & SecurityRules
regulation: CRA
article: Art. 20
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.2.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.2.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.3.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.3.md
status: DRAFT
---

# CRA Art. 20

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-CRA-040 | A distributor acts with due care in relation to the requirements of this Regulation when making a product with digital elements available on the market, and — before making the product available — verifies the CE marking and that the manufacturer / importer have complied with their respective obligations; the distributor takes corrective measures on non-conformity and informs the manufacturer and the market surveillance authority where the product presents a significant risk or vulnerability. | `CRA-CL92` (Art. 20(1) — distributor due care); `CRA-CL93` (Art. 20(2) — distributor pre-market checks); `CRA-CL94` (Art. 20(3) — distributor non-conformity); `CRA-CL95` (Art. 20(4) — distributor corrective measures) | D-06.3, D-09.4 |
| SO-CRA-040 | D-06.3, D-09.4 | Art. 20(1)/(2)/(3)/(4) | Distributor due care, pre-market checks, non-conformity, corrective measures |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-057
  title: "Distributor due-care and pre-market verification"
  source_clauses:
    - { clause_id: CRA-CL92, article_ref: "Art. 20(1) — distributor due care" }
    - { clause_id: CRA-CL93, article_ref: "Art. 20(2) — distributor pre-market checks" }
  linked_objectives: [SO-CRA-040]
  sub_domain: [D-06.3]
  nist_csf_mapping:
    - { id: GV.SC-04, title: "Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations" }
  applies_to_role: [DISTRIBUTOR]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 20(1) requires distributors to act with due care in relation to the requirements of this Regulation when making a product with digital elements available on the market. Article 20(2) requires distributors — before making the product available — to verify that the CE marking has been affixed, that the product is accompanied by the required documentation and instructions (Annex II), and that the manufacturer and importer have complied with their respective obligations. The two paragraphs operate at a documentary level — the distributor does not re-verify the product's technical conformity, but only the evidence chain.
  security_rationale: |
    The Article 20(1)/(2) distributor due-care duty is operationalised in NIST CSF 2.0 through **GV.SC-04 (suppliers and other third parties routinely assessed against contractual obligations)**. GV.SC-04 is the operative Subcategory here: the distributor's three Article 20(2) checks (CE marking affixed, Annex II documentation present, manufacturer + importer compliance posture verified) are contractual-obligation confirmation points, with the due-care backstop of Article 20(1) supplying the procedural frame. The distributor's verification is procedurally lighter than the importer's — the technical-documentation copy is not required to be held; only the upstream evidence chain is verified. The duty to act with due care (Article 20(1)) is the procedural backbone; Article 20(2)'s verification list is the operational expression. GV.SC-04 enables the distributor to demonstrate ex post, through documented per-check confirmation records, that the (1)/(2) due-care duty has been discharged and that the marketplace-end verification gate has been applied consistent with the proportionality principle.
  ambiguity_notes: |
    `Due care` is VAG+POLY-S3 — case-law-laden; cf. CRA-C24 in v0.1 §3.2 and SR-CRA-050 due diligence. Reading chosen: R3 (procedural + substantive). The Berry-VAG signature of `due care` parallels `due diligence` (SR-CRA-050) but with a proportionality knob: distributor due care is procedurally lighter than Article 13(5) due diligence. The substantive content is supplied by Annex VII §2 and the Annex II information that the distributor verifies under Article 20(2). Remain open: (a) the operational threshold between distributor `due care` and distributor `non-conformity duty` under Article 20(3) — i.e. whether the verification under Article 20(2) is sufficient or whether the distributor must independently investigate suspicious indicators before Article 20(3) fires; (b) the demarcation between distributor and online marketplace provider under the CRA's liability framework — pending implementing-acts guidance on e-commerce platform obligations.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-058
  title: "Distributor non-conformity and corrective-measures escalation"
  source_clauses:
    - { clause_id: CRA-CL94, article_ref: "Art. 20(3) — distributor non-conformity" }
    - { clause_id: CRA-CL95, article_ref: "Art. 20(4) — distributor corrective measures + inform manufacturer" }
  linked_objectives: [SO-CRA-040]
  sub_domain: [D-06.3, D-04.2]
  nist_csf_mapping:
    - { id: RS.MI-01, title: "Incidents are contained" }
    - { id: RS.CO-04, title: "Coordination with stakeholders occurs consistent with applicable rules and regulations" }
  applies_to_role: [DISTRIBUTOR]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 20(3) requires the distributor — where they have reason to believe that a product is not in conformity — not to make the product available until conformity is restored, and to inform the manufacturer and the market surveillance authority of the significant risk. Article 20(4) requires the distributor — if a vulnerability is identified in a product they have made available — to inform the manufacturer and to take immediate corrective measures. The two paragraphs are the distributor-side analogue of the importer's Article 19(3)/(5); see SR-CRA-055 for the upstream-importer analysis. The corrective-measure set is the same as the manufacturer's Article 13(21): fix, withdraw, or recall — applied at the distributor boundary within the distributor's power.
  security_rationale: |
    The Article 20(3)/(4) distributor escalation duty is operationalised in NIST CSF 2.0 through **RS.MI-01 (incidents contained)** and **RS.CO-04 (coordination with stakeholders consistent with applicable rules and regulations)**. RS.MI-01 captures the marketplace-end containment dimension: where the distributor has reason to believe a product is non-conforming, the product is held back from the market (or withdrawn if already made available) until conformity is restored — the corrective-measure set mirrors the manufacturer's Article 13(21), applied at the distributor boundary. RS.CO-04 anchors the manufacturer-MSA coordination function: the distributor informs the manufacturer and the MSA of the significant risk, with the Article 20(4) duty explicitly preserving the manufacturer's upstream awareness and discharging the parallel duty to take corrective measures. Together RS.MI-01 and RS.CO-04 enable the distributor to demonstrate ex post, through documented hold-and-withdraw records and notification logs, that the (3)/(4) escalation duty has been discharged and that the manufacturer's parallel Article 14 reporting (SR-CRA-029 to SR-CRA-038) fires as appropriate.
  ambiguity_notes: |
    `Significant risk` (Article 20(3)) is VAG-S3 — same reading as the importer's under SR-CRA-055: R2 (qualitative judgment by the distributor's competent personnel). `Corrective measures` (Article 20(4)) is POLY-S2 — R1 (literal OR of fix / withdraw / recall, applied to the distributor's circle of control). The relationship to Article 21 (manufacturer-equivalent trigger, SR-CRA-061) is significant: a distributor who substantially modifies a product ceases to be a distributor and becomes a manufacturer. Remain open: (a) the operational interface with online marketplace providers that operate as quasi-distributors under the CRA's e-commerce platform framework — whether the distributor duty under Article 20 extends to platforms that do not take legal title; (b) whether distributor corrective measures must be coordinated with the manufacturer's parallel corrective measures (e.g. recall) or whether independent actions are permissible.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

