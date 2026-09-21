---
document_id: AEGIS-P1-06
title: Clause Mapping Matrix
phase: 1
version: 1.1
created: 2026-04-01
updated: 2026-08-06
author: Compliance Lead (Fase de Especificação 1 reconciliation)
status: RECONCILED
inputs: [Doc03_Company_Context_Assessment.md, Doc08_Regulatory_Applicability.md]
outputs: [Doc11_Structured_Compliance_Matrix.md]
traceability: AEGIS Class Model → RegulatoryClause, DomainCoverageEntry classes
related_documents: 00_Taxonomy_Reference.md
---

> **Fase de Especificação 1 Reconciliation Note (2026-08-06)**
> Rich Mode copy of legacy `01_PHASE1_CONTEXT/06_Clause_Mapping_Matrix.md` (v1.0). Fase de Especificação 1 changes:
> - **I-01 (Clause ID shim):** Added the **Cross-Reference: Case Clause IDs ↔ Corpus Clause IDs** section below. The case form (`GDPR-C{NN}` / `CRA-C{NN}`) is preserved for Phase 2/3 backward compat. The corpus form (`GDPR-CL/CP/RT{xx}` / `CRA-CL{xx}`) is added as a parallel reference. The 28 GDPR + 26 CRA rows are mapped per the AEGIS Rich Mode corpus (`00_METHODOLOGY/PREPROCESSING_by_domain/domains/`).
> - **GDPR-C08 conflict resolution:** Per `phase1_ontology.yaml` (Rich copy v1.1, header note), `GDPR-C08 = Art. 9 → D-05.3` is the **canonical case-form** mapping. The legacy scripts that map `GDPR-C08 = Art. 24(1) → D-09.1` are now deprecated; the `06_Clause_Mapping_Matrix.xlsx` sheet `GDPR_MAPPING` and all downstream documents (Doc 07, Doc 07b) use the ontology-canonical mapping. The shim table below documents the chosen canonical.
> - **I-10 (status DRAFT → RECONCILED):** Fase de Especificação 1 milestone.
> - **I-13 (02_Regulatory_Mapping_Master.md deprecation):** Banner not added in this doc (no reference).

# Clause Mapping Matrix

## 1. DOCUMENT PURPOSE

This document specifies the Excel-based Clause Mapping Matrix (Step B2), mapping regulatory clauses to the 10×38 taxonomy with Normative Intensity and gap analysis.

**Note:** The actual matrix is maintained in Excel format (`06_Clause_Mapping_Matrix.xlsx`). This document provides the specification and summary.

**Phase 1 Step:** B (Clause Mapping)

---

## 2. EXCEL STRUCTURE (7 Sheets)

### Sheet 1: COVER
| Field | Value |
|-------|-------|
| Document ID | AEGIS-P1-06 |
| Title | Clause Mapping Matrix - TinyTask SaaS |
| Version | 1.0 |
| Created | 2026-04-01 |
| Author | Compliance Lead |
| Applicable Regulations | GDPR, CRA |

### Sheet 2: GDPR_MAPPING (T1)
**Columns:** Clause ID | Article | Sub-Domain ID | Sub-Domain Name | Description | obligatedParty | obligationType | Normative Weight | Justification | TinyTask Relevance

**Summary for TinyTask:**

| Metric | Value |
|--------|-------|
| Total GDPR Clauses | 28 |
| Applicable to TinyTask | 28 |
| Weight 3 (Mandatory) | 20 (71.4%) |
| Weight 2 (Recommended) | 8 (28.6%) |
| Mean NI | 2.714 |

### Sheet 3: CRA_MAPPING (T2)
**Columns:** Clause ID | Article/Annex | Sub-Domain ID | Sub-Domain Name | Description | obligatedParty | obligationType | Normative Weight | Justification | TinyTask Relevance

**Summary for TinyTask:**

| Metric | Value |
|--------|-------|
| Total CRA Clauses | 26 |
| Applicable to TinyTask | 26 |
| Weight 3 (Mandatory) | 24 (92.3%) |
| Weight 2 (Recommended) | 2 (7.7%) |
| Mean NI | 2.923 |

### Sheets 4-6: NIS2, DORA, AIACT
**Status:** Not applicable for TinyTask (see 05_Regulatory_Applicability.md)

### Sheet 7: CONSOLIDATED_VIEW (T6 + T9)
**Pivot Table:** Sub-Domain coverage across applicable regulations

---

## 3. CLAUSE-TO-SUB-DOMAIN MAPPING SUMMARY

### GDPR Mapping (28 clauses → 10×38 taxonomy)

| Sub-Domain | Clause Count | Clauses |
|------------|--------------|---------|
| D-01 (Encryption) | 3 | GDPR-C04, C05, C14 |
| D-03 (Access Control) | 2 | GDPR-C10, C17 |
| D-04 (Incident Response) | 3 | GDPR-C18, C21, C23 |
| D-05 (Data Lifecycle) | 4 | GDPR-C01, C02, C03, C06, C07 |
| D-09 (Governance) | 4 | GDPR-C08, C13, C20, C22 |
| D-10 (Monitoring) | 3 | GDPR-C19, C25, C26 |
| ... | ... | ... |

### CRA Mapping (26 clauses → 10×38 taxonomy)

| Sub-Domain | Clause Count | Clauses |
|------------|--------------|---------|
| D-01 (Encryption) | 2 | CRA-C07, C08 |
| D-02 (Vuln Management) | 4 | CRA-C01, C04, C17, C19, C21, C26 |
| D-03 (Access Control) | 2 | CRA-C03, C05, C06 |
| D-06 (Supply Chain) | 2 | CRA-C18, C22 |
| D-07 (Secure Development) | 3 | CRA-C02, C09, C10 |
| ... | ... | ... |

---

## 4. GAP ANALYSIS SUMMARY

| Gap ID | Sub-Domain | Regulation | Clause | Gap Description | Risk Level |
|--------|------------|------------|--------|-----------------|------------|
| GAP-001 | D-09.4 | GDPR | Art.30 | No records of processing | HIGH |
| GAP-002 | D-01 | GDPR | Art.32 | No formal security policy | MEDIUM |
| GAP-003 | D-06.2 | CRA | Art.18 | No SBOM process | HIGH |
| GAP-004 | D-02.3 | CRA | Art.21 | No vuln disclosure process | MEDIUM |

---

## 5. NORMATIVE INTENSITY SUMMARY (T9)

| Regulation | Mean NI | Weight 3 % | Weight 2 % | Weight 1 % |
|------------|---------|------------|------------|------------|
| GDPR | 2.714 | 71.4% | 28.6% | 0.0% |
| CRA | 2.923 | 92.3% | 7.7% | 0.0% |
| **COMBINED (TinyTask)** | **2.819** | **81.9%** | **18.1%** | **0.0%** |

---

## 6. VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-01 | Compliance Lead | Initial release - TinyTask SaaS case |

---

## 7. DOCUMENT APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Document Author | Compliance Lead | | 2026-04-01 |
| Technical Review | | | |
| AEGIS Methodology Review | | | |

---

## 8. CROSS-REFERENCE: CASE CLAUSE IDS ↔ CORPUS CLAUSE IDS

> **Fase de Especificação 1 reconciliation (I-01).** Mapping between case-form (`GDPR-C{NN}` / `CRA-C{NN}`) and corpus-form (`GDPR-CL/CP/RT{xx}` / `CRA-CL{xx}`).
> **Canonical: case-form preserved for Phase 2/3 backward compat.** Corpus-form added as a parallel reference. The corpus form uses semantic prefixes: `GDPR-CL{xx}` = Clause, `GDPR-CP{xx}` = Privacy-by-design obligation, `GDPR-RT{xx}` = data-subject RighT, `CRA-CL{xx}` = Clause. There is **no 1:1 numerical correspondence** between case-form and corpus-form (e.g., case `GDPR-C01` ≠ corpus `GDPR-CL01`); the mapping is **semantic**.
> **Source:** case's `06_Clause_Mapping_Matrix.xlsx → GDPR_MAPPING` (28 rows) and `CRA_MAPPING` (26 rows) cross-referenced with corpus `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-XX.Y/D-XX.Y.md` Part 4 `**Clause: ...**` metadata lines and the AEGIS Fase de Especificação 0 `corpus_field_map.md §4.1`.

### 8.1 GDPR Cross-Reference (28 clauses)

| Case ID | Article | Sub-Domain | Case NW | Corpus Clause ID | obligatedParty (corpus) | Notes |
|---------|---------|-----------|---:|---|---|---|
| GDPR-C01 | Art. 1 | D-05.1 | 3 | `GDPR-CL01` or `GDPR-CL02` (TBD verify) | CONTROLLER | Subject-matter / scope clause; D-05.1 corpus heuristic match |
| GDPR-C02 | Art. 2 | D-05.1 | 3 | `GDPR-CL02` (verify) | CONTROLLER | Material scope |
| GDPR-C03 | Art. 3 | D-05.1 | 3 | `GDPR-CL03` (verify) | CONTROLLER | Territorial scope |
| GDPR-C04 | Art. 5(1)(c) | D-01.1 | 3 | `GDPR-CL06` | CONTROLLER | Data minimisation principle (D-01.1 corpus: `**Clause: GDPR-CL06 \| type: principle \| obligatedParty: CONTROLLER \| obligationType: CONTINUOUS**`) |
| GDPR-C05 | Art. 5(1)(b) | D-05.1 | 3 | `GDPR-CL02` | CONTROLLER | Purpose limitation principle |
| GDPR-C06 | Art. 5(1)(e) | D-05.2 | 3 | `GDPR-CL05` | CONTROLLER | Storage limitation principle (retention-linked) |
| GDPR-C07 | Art. 5(1)(f) | D-01.1 | 2 | `GDPR-CL06` | CONTROLLER | Integrity & confidentiality principle |
| **GDPR-C08** | **Art. 9** | **D-05.3** | **3** | **`GDPR-CL09` (verify)** | **CONTROLLER + PROCESSOR** | **Processing of special categories. CANONICAL: Art. 9 → D-05.3 per `phase1_ontology.yaml` v1.1. The legacy script mapping `GDPR-C08 = Art. 24(1) → D-09.1` is DEPRECATED. Fase de Especificação 2 must verify the corpus `D-05.3.md` Part 4 carries a `**Clause: GDPR-CL09 \| obligatedParty: CONTROLLER + PROCESSOR**` line; if not, the corpus clause ID is TBD and Fase de Especificação 2 must assign one.** |
| GDPR-C09 | Art. 17 | D-05.3 | 3 | `GDPR-RT03` or `GDPR-RT06` (verify) | CONTROLLER | Right to erasure (data subject right family) |
| GDPR-C10 | Art. 20 | D-05.4 | 3 | `GDPR-RT09` | CONTROLLER | Right to data portability (D-05.4 corpus carries `**Clause: GDPR-RT09 \| type: data subject right**`) |
| GDPR-C11 | Art. 24(1) | D-09.1 | 2 | `GDPR-CL24` (verify) | CONTROLLER + PROCESSOR | Responsibility of the controller — case-form preserved as `GDPR-C11` (NOT `GDPR-C08`); mapping per ontology. Fase de Especificação 2 verify corpus. |
| GDPR-C12 | Art. 25(1) | D-07.1 | 2 | `GDPR-CP02` (verify) | CONTROLLER | Data protection by design |
| GDPR-C13 | Art. 25(2) | D-03.3 | 3 | `GDPR-CP03` (verify) | CONTROLLER | Data protection by default |
| GDPR-C14 | Art. 28(1) | D-06.1 | 3 | `GDPR-CP07` (verify) | CONTROLLER | Processor obligations (selection) |
| GDPR-C15 | Art. 28(3) | D-06.3 | 3 | `GDPR-CP09` or `GDPR-CP11` (verify) | PROCESSOR | Processor obligations (contract execution) |
| GDPR-C16 | Art. 30 | D-09.4 | 3 | `GDPR-CL26` (verify) | CONTROLLER + PROCESSOR | Records of processing (D-09.4 EMPTY in corpus) |
| GDPR-C17 | Art. 32(1)(a) | D-01.1 | 2 | `GDPR-CL06` | CONTROLLER + PROCESSOR | Pseudonymisation & encryption (Art. 32) |
| GDPR-C18 | Art. 32(1)(a) | D-01.2 | 2 | `GDPR-CL06` | CONTROLLER + PROCESSOR | Pseudonymisation & encryption (in transit) |
| GDPR-C19 | Art. 32(1)(b) | D-03.3 | 3 | `GDPR-CL06` | CONTROLLER + PROCESSOR | Confidentiality (access control) |
| GDPR-C20 | Art. 32(1)(c) | D-04.2 | 2 | `GDPR-CL06` | CONTROLLER + PROCESSOR | Integrity / restoration capability |
| GDPR-C21 | Art. 32(1)(c) | D-04.4 | 2 | `GDPR-CL06` | CONTROLLER + PROCESSOR | Availability (D-04.4) |
| GDPR-C22 | Art. 32(1)(c) | D-04.3 | 2 | `GDPR-CL06` | CONTROLLER + PROCESSOR | Recovery / business continuity |
| GDPR-C23 | Art. 32(1)(d) | D-10.3 | 3 | `GDPR-CP15` or `GDPR-CP03` (verify) | CONTROLLER + PROCESSOR | Regular testing of security (D-10.3 corpus EMPTY) |
| GDPR-C24 | Art. 32(2) | D-09.2 | 2 | `GDPR-CP16` (verify) | CONTROLLER + PROCESSOR | Risk assessment of processing operations |
| GDPR-C25 | Art. 33(1) | D-04.3 | 3 | `GDPR-CP17` | CONTROLLER | Breach notification (controller → SA within 72h) |
| GDPR-C26 | Art. 33(3) | D-09.4 | 3 | `GDPR-CP18` | CONTROLLER | Breach notification (documentation in RoPA) |
| GDPR-C27 | Art. 34(1) | D-04.3 | 3 | `GDPR-CP19` | CONTROLLER | Breach communication to data subject |
| GDPR-C28 | Art. 35(1) | D-09.2 | 3 | `GDPR-CP21` (verify) | CONTROLLER | Data protection impact assessment (DPIA) |

> **Case-form enumeration notice:** Case uses sequential numbering 01–28. The mapping above follows `phase1_ontology.yaml` v1.1 (Rich copy, Fase de Especificação 1). The legacy numbering 01–28 is preserved verbatim — only the article/sub-domain mapping for `GDPR-C08` was previously inconsistent (script vs ontology) and is now resolved canonically to the ontology's `Art. 9 → D-05.3`.

### 8.2 CRA Cross-Reference (26 clauses)

| Case ID | Article | Sub-Domain | Case NW | Corpus Clause ID | obligatedParty (corpus) | Notes |
|---------|---------|-----------|---:|---|---|---|
| CRA-C01 | Art. 1 | D-07.1 | 3 | `CRA-CL01` (verify) | MANUFACTURER | Subject matter & scope |
| CRA-C02 | Art. 2 | D-07.1 | 3 | `CRA-CL02` (verify) | MANUFACTURER | Definitions |
| CRA-C03 | Art. 3 | D-03.4 | 3 | `CRA-CL03` (verify) | MANUFACTURER | Security requirements (sole authority: CRA) |
| CRA-C04 | Art. 4 | D-02.2 | 3 | `CRA-CL04` (verify) | MANUFACTURER | Vulnerability handling |
| CRA-C05 | Art. 5 | D-02.1 | 3 | `CRA-CL05` (verify) | MANUFACTURER | Security updates |
| CRA-C06 | Art. 6 | D-04.1 | 2 | `CRA-CL06` (verify) | MANUFACTURER | Incident reporting |
| CRA-C07 | Art. 7 | D-06.2 | 3 | `CRA-CL07` (verify) | MANUFACTURER | Supply chain security (sole authority: CRA) |
| CRA-C08 | Art. 8 | D-03.4 | 3 | `CRA-CL08` (verify) | MANUFACTURER | Secure defaults |
| CRA-C09 | Art. 9 | D-03.2 | 3 | `CRA-CL09` (verify) | MANUFACTURER | Password security |
| CRA-C10 | Art. 10 | D-03.1 | 3 | `CRA-CL10` (verify) | MANUFACTURER | Identity authentication |
| CRA-C11 | Art. 11 | D-05.3 | 3 | `CRA-CL11` (verify) | MANUFACTURER | Data erasure (shared with GDPR-C09) |
| CRA-C12 | Art. 12 | D-10.1 | 3 | `CRA-CL12` (verify) | MANUFACTURER | Availability at end of support |
| CRA-C13 | Art. 13 | D-09.1 | 3 | `CRA-CL13` (verify) | MANUFACTURER | Technical documentation |
| CRA-C14 | Art. 14 | D-10.3 | 3 | `CRA-CL14` (verify) | MANUFACTURER | Conformity assessment |
| CRA-C15 | Art. 15 | D-01.3 | 3 | `CRA-CL15` (verify) | MANUFACTURER | CE marking |
| CRA-C16 | Art. 16 | D-06.3 | 3 | `CRA-CL16` (verify) | MANUFACTURER | Market surveillance |
| CRA-C17 | Art. 17 | D-02.1 | 3 | `CRA-CL17` (verify) | MANUFACTURER | Essential requirements (ICT products) |
| CRA-C18 | Art. 18 | D-07.1 | 3 | `CRA-CL18` (verify) | MANUFACTURER | Security by design |
| CRA-C19 | Art. 19 | D-02.3 | 3 | `CRA-CL19` (verify) | MANUFACTURER | Vulnerability handling & disclosure (sole authority: CRA) |
| CRA-C20 | Art. 20 | D-04.3 | 3 | `CRA-CL20` (verify) | MANUFACTURER | Reporting incidents |
| CRA-C21 | Art. 21 | D-10.3 | 3 | `CRA-CL21` (verify) | MANUFACTURER | EU declarative conformity |
| CRA-C22 | Art. 22 | D-10.2 | 3 | `CRA-CL22` (verify) | MANUFACTURER | Traceability |
| CRA-C23 | Art. 23 | D-07.1 | 3 | `CRA-CL23` (verify) | MANUFACTURER | Software security |
| CRA-C24 | Art. 24 | D-01.1 | 3 | `CRA-CL24` (verify) | MANUFACTURER | Encrypted data storage |
| CRA-C25 | Art. 25 | D-01.2 | 3 | `CRA-CL25` (verify) | MANUFACTURER | Unauthorised access prevention |
| CRA-C26 | Art. 26 | D-04.4 | 3 | `CRA-CL26` (verify) | MANUFACTURER | Resilience to outages |

> **Fase de Especificação 2 deliverable:** verify each `(verify)` corpus clause ID by reading the corresponding `D-XX.Y.md` Part 4 `**Clause:**` line. Update the table to replace `(verify)` with confirmed IDs.

### 8.3 Migration Notes

- **28 GDPR + 26 CRA = 54 clauses** total; both totals match the legacy `06_Clause_Mapping_Matrix.xlsx` sheet summaries.
- **28 of 28 GDPR rows and 26 of 26 CRA rows** are mapped case-form ↔ article. Of these, **14 GDPR + 28 CRA rows carry a corpus-form `(verify)` marker** must resolve.
- **8 GDPR rows map to corpus EMPTY sub-domains** (D-05.2, D-08.2, D-09.1, D-09.2, D-09.4, D-10.3, etc., per `corpus_field_map.md §3.4`). These rows have **no `D-XX.Y.md`** to verify against; Fase de Especificação 2 must either generate the missing 8 `.md` files OR mark the corpus-form as "TBD — corpus EMPTY".
- **Case-form IDs are NOT renumbered.** Phase 2/3 docs (`15_Requirements_Allocation.md`, `17_Functional_Tree.md`, etc.) that reference `GDPR-C08` continue to refer to **Art. 9 → D-05.3** per this canonical mapping.

---

**Next Document:** 07_Structured_Compliance_Matrix.md
**Gate Status:** ⏳ PENDING REVIEW
