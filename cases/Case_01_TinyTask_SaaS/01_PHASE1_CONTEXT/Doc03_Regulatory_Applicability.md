---
document_id: AEGIS-P1-05
title: Regulatory Applicability Assessment
phase: 1
version: 2.1
created: 2026-04-01
updated: 2026-08-10
author: Fase de Especificação 5 Executor (deep-enrichment-builder)
status: DEEP_ENRICHED
deep_enrichment_date: 2026-08-06
ao_id_cross_ref_note_date: 2026-08-10
per_article_rows: 54
fields_excluded: [Effort Estimate, Cost Estimate, Target Timeline]
inputs: [Doc03_Company_Context_Assessment.md]
outputs: [Doc10_Clause_Mapping_Matrix.md]
traceability: AEGIS Class Model → ComplianceContext, RegulatoryClause classes
related_documents: 00_Taxonomy_Reference.md, 04_Company_Context_Assessment.md
ao_id_migration_note: Each row's `Operational check per Doc 07c Appendix A §A.1.1/D-XX.X` references the sub-domain (not a specific PG/SG ID). The 74 detail cards in Doc 07c Appendix A retain their legacy PG/SG headings for Phase 2 traceability; see `07c_Adjusted_Goals.md` Appendix A §A.0 alias table for the corr-008 AO ID equivalents.
---

<!-- Note: 02_Regulatory_Mapping_Master.md is DEPRECATED as of Phase 1 v1.2 (2026-07-13). Use 00_METHODOLOGY/PREPROCESSING_by_domain/domains/ corpus or 00_Taxonomy_Reference.md instead. -->

> **Fase de Especificação 1 Reconciliation Note (2026-08-06)**
> Rich Mode copy of legacy `01_PHASE1_CONTEXT/05_Regulatory_Applicability.md` (v1.2, the "v1.1" + Art. 32/33(2)/CRA Art. 13 updates from April). Fase de Especificação 1 changes:
> - **I-10 (status DRAFT → RECONCILED):** Fase de Especificação 1 milestone.
> - **I-13 (02_Regulatory_Mapping_Master.md deprecation):** Banner added. The legacy `02_Regulatory_Mapping_Master.md` (00_COMMON) is deprecated as a master mapping source; the Rich equivalent is the corpus + `00_Taxonomy_Reference.md`.
> - Body content unchanged from legacy. Fase de Especificação 2 will add L1 participant lists per sub-domain.

> **Mapping to Phase 1 Strategy:** This document is the artifact of
> **Filter 1 (Regulation Applicability — binary predicates)** in
> [`00_METHODOLOGY/PHASE1_STRATEGY.md`](../../../00_METHODOLOGY/PHASE1_STRATEGY.md) §5.
> Updates to the underlying filter logic should be reflected here.

# Regulatory Applicability Assessment

## 1. DOCUMENT PURPOSE

This document consolidates the regulatory applicability assessment (Step B1+B3), determining which regulations apply to the company context and establishing the Native vs. Inherited compliance boundaries.

**Alignment with Class Model:**
- `ComplianceContext` - Applicable regulations and applicability scores
- `RegulatoryClause` - Filtered clauses based on applicability
- `DomainCoverageEntry` - Initial domain coverage assessment

**Phase 1 Step:** B (Regulatory Applicability)

**Gate Criteria:** Clear applicability determination for all 5 regulations with documented rationale

---

## 2. APPLICABILITY ASSESSMENT METADATA

| Attribute | Value |
|-----------|-------|
| complianceContextId | COMPLIANCE-TINYTASK-2026-001 |
| assessmentDate | 2026-04-01 |
| basedOnCompanyContext | CC-TINYTASK-2026-001 |
| assessedBy | Compliance Lead |
| reviewedBy | Legal Counsel (pending) |

---

## 3. REGULATION-BY-REGULATION APPLICABILITY ANALYSIS

### 3.1 GDPR (General Data Protection Regulation)

| Criterion | Company Context Value | Threshold | Met? |
|-----------|----------------------|-----------|------|
| processes_personal_data | TRUE (emails, names, passwords) | ANY | YES |
| EU data subjects | TRUE (EU customers) | ANY | YES |
| Special category data | FALSE | ANY | N/A |

**Applicability Result:** ✅ APPLICABLE

**Rationale:** TinyTask processes personal data (emails, names, passwords) of EU residents. As a data controller for account data and processor for B2B client content, GDPR applies fully.

**Obligated Party:** CONTROLLER (for account data, user management) + PROCESSOR (for B2B client content stored on behalf of customers).

**Multi-Actor Note:** GDPR Art. 32 (security of processing) applies **directly to both controllers AND processors** ("the controller and the processor shall implement..."). For clauses under Art. 32, TinyTask as processor has **NativeCompliance** obligations — not merely InheritedCompliance via DPA. Other GDPR clauses (e.g., Art. 5, 6, 7) apply only in the controller capacity.

**Key Clauses in Scope:** GDPR-C01 through GDPR-C28 (all applicable clauses)

**Nuance:** Where TinyTask acts solely as processor (hosting client content), Art. 28(3)(f) requires it to implement Art. 32 measures directly. This means encryption, access control, and breach notification obligations are not inherited via contract — they are direct statutory duties under the GDPR.

**Nuance — Processor Breach Notification (Art. 33(2)):** Art. 33(2) requires processors to notify controllers "without undue delay" after becoming aware of a personal data breach. This is **not** the same as the 72h controller→SA deadline in Art. 33(1). As a processor, TinyTask must notify its B2B clients (who are controllers) "without undue delay" — an unquantified timeframe that should be defined internally (e.g., within 4-8 hours). The 72h clock applies to the controller's notification to the supervisory authority, not to TinyTask's notification to its clients.

---

### 3.2 CRA (Cyber Resilience Act)

| Criterion | Company Context Value | Threshold | Met? |
|-----------|----------------------|-----------|------|
| places_digital_products_eu | TRUE (SaaS in EU market) | TRUE | YES |
| Digital element | TRUE (Web App + Mobile App) | YES/NO | YES |
| Manufacturer status | TRUE (TinyTask develops and operates) | YES/NO | YES |

**Applicability Result:** ✅ APPLICABLE

**Rationale:** TinyTask Team Organizer is a digital product (SaaS) placed on the EU market. TinyTask Lda. qualifies as the manufacturer under CRA definitions.

**Key Clauses in Scope:** CRA-C01 through CRA-C26 (all applicable clauses)

**Quantitative Thresholds:**
- **Support Period (Art. 13(8)):** Minimum **5 years** from product placement (or expected use time if less than 5 years). For TinyTask's SaaS, each release has its own 5-year support clock.
- **Security Update Retention (Art. 13(9)):** Security updates must remain available for a minimum of **10 years** or the support period, whichever is longer. This means old versions' patches must be archived for at least a decade.
- **Technical Documentation Retention (Art. 13(13)):** Technical documentation must be kept for **10 years** after the product has been placed on the market.

---

### 3.3 NIS 2 (Network and Information Systems Directive)

| Criterion | Company Context Value | Threshold | Met? |
|-----------|----------------------|-----------|------|
| nis2_sector | Technology | Essential/Important | NO |
| size (employees) | 8 | ≥50 (medium) / ≥250 (large) | NO |
| size (revenue) | <€2M | ≥€10M / ≥€50M | NO |
| Critical entity status | FALSE | YES/NO | NO |

**Applicability Result:** ❌ NOT APPLICABLE

**Rationale:** TinyTask is below all NIS 2 thresholds: 8 employees (< 50), <€2M revenue (< €10M), and operates in non-critical sector (productivity software, not essential service).

**Key Clauses in Scope:** N/A

---

### 3.4 DORA (Digital Operational Resilience Act)

| Criterion | Company Context Value | Threshold | Met? |
|-----------|----------------------|-----------|------|
| dora_financial_entity | FALSE | TRUE | NO |
| Financial sector classification | N/A | Credit institution, Investment firm, etc. | NO |
| ICT third-party provider | FALSE | YES/NO | NO |

**Applicability Result:** ❌ NOT APPLICABLE

**Rationale:** TinyTask is not a financial entity. Payment processing is fully delegated to Stripe (licensed payment processor).

**Key Clauses in Scope:** N/A

---

### 3.5 AI Act (Artificial Intelligence Regulation)

| Criterion | Company Context Value | Threshold | Met? |
|-----------|----------------------|-----------|------|
| aiact_high_risk_system | FALSE | TRUE | NO |
| AI system provider | FALSE | YES/NO | NO |
| AI system deployer | FALSE | YES/NO | NO |
| High-risk use case | FALSE (deterministic logic only) | Annex III listing | NO |

**Applicability Result:** ❌ NOT APPLICABLE

**Rationale:** TinyTask uses standard application logic with no AI/ML components. All decisions are made by users; the system only stores and displays data.

**Key Clauses in Scope:** N/A

---

## 4. APPLICABILITY MATRIX SUMMARY

| Regulation | Applicable? | Confidence | Key Driver | Exclusion Reason (if applicable) |
|------------|-------------|------------|------------|----------------------------------|
| GDPR | YES | HIGH | Processes EU personal data | — |
| CRA | YES | HIGH | SaaS product in EU market | — |
| NIS 2 | NO | HIGH | Below employee/revenue threshold | 8 employees (< 50), <€2M revenue |
| DORA | NO | HIGH | Not a financial entity | Payments via Stripe |
| AI Act | NO | HIGH | No AI/ML systems | Deterministic logic only |

---

## 5. NATIVE VS. INHERITED COMPLIANCE

### 5.1 Native Compliance Requirements

Compliance obligations that TinyTask must implement directly:

| Regulation | Domain | Obligation | Actor Capacity | Implementation Responsibility |
|------------|--------|------------|----------------|-------------------------------|
| GDPR | D-05, D-09, D-10 | Data protection, Records, Security | Controller | Internal (CTO + Lead Dev) |
| GDPR (Art. 32) | D-01 | Security of processing (encryption, access control, breach notification) | **Processor** (NativeCompliance, not via DPA) | Internal (CTO + Lead Dev) |
| CRA | D-02, D-06, D-07 | Vuln management, SBOM, Secure dev | Manufacturer | Internal (Lead Dev) |

### 5.2 Inherited Compliance Requirements

Compliance obligations inherited from suppliers/partners:

| Regulation | Domain | Obligation | Source (Supplier/Partner) | Evidence Required |
|------------|--------|------------|---------------------------|-------------------|
| GDPR | D-01 | Infrastructure security | AWS (eu-west-1) | SOC 2 Type II report |
| GDPR | D-01 | Payment security | Stripe | PCI-DSS certification |
| CRA | D-01 | Cloud security | AWS/Firebase | Security documentation |

### 5.3 Compliance Boundary Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    TINYTASK BOUNDARY                         │
│                                                              │
│   ┌─────────────────┐         ┌─────────────────┐           │
│   │  NATIVE         │         │  INHERITED      │           │
│   │  Compliance     │         │  Compliance     │           │
│   │  (Direct)       │         │  (Via contracts)│           │
│   │                 │         │                 │           │
│   │ • App security  │         │ • AWS: Physical │           │
│   │ • Access control│         │ • Stripe: PCI   │           │
│   │ • SBOM          │         │ • Firebase: Infra│          │
│   │ • Vuln mgmt     │         │                 │           │
│   └─────────────────┘         └─────────────────┘           │
│                                                              │
└─────────────────────────────────────────────────────────────┘
         ▲                               ▲
         │                               │
    Direct implementation          Supplier/Partner
    within TinyTask                compliance evidence
```

---

## 6. SUB-DOMAIN COVERAGE PRELIMINARY ASSESSMENT

Based on applicable regulations (GDPR + CRA):

| Sub-Domain ID | Sub-Domain Name | GDPR | CRA | Total | Coverage Level |
|---------------|-----------------|------|-----|-------|----------------|
| D-01.1 | Data at Rest Encryption | ✅ | ✅ | 2 | SUBSTANTIVE |
| D-01.2 | Data in Transit Encryption | ✅ | ✅ | 2 | SUBSTANTIVE |
| D-01.3 | Cryptographic Key Management | ✅ | ✅ | 2 | SUBSTANTIVE |
| D-01.4 | Data Integrity Mechanisms | ✅ | ✅ | 2 | SUBSTANTIVE |
| D-02.1 | Vulnerability Identification | — | ✅ | 1 | PARTIAL |
| D-02.2 | Patch Management & Updates | — | ✅ | 1 | PARTIAL |
| D-02.3 | Coordinated Vuln. Disclosure | — | ✅ | 1 | PARTIAL |
| D-02.4 | Threat-Led Penetration Testing | — | — | 0 | NOT_ADDRESSED |
| ... | ... | ... | ... | ... | ... |

**Coverage Summary:**
- Substantive Coverage (≥2 regulations): ~15 sub-domains
- Partial Coverage (1 regulation): ~10 sub-domains
- No Coverage (0 regulations): ~13 sub-domains (NIS 2/DORA/AI Act exclusive)

---

## 7. STRATEGIC IMPLICATIONS

| Implication ID | Source Regulation | Description | Impact on Architecture | Priority |
|----------------|-------------------|-------------|------------------------|----------|
| SI-001 | GDPR, CRA | Dual encryption requirements | Single encryption standard satisfies both | HIGH |
| SI-002 | CRA | SBOM requirement new for TinyTask | Need dependency scanning in CI/CD | HIGH |
| SI-003 | GDPR | Data subject rights (erasure, portability) | Need user-facing data export/delete | MEDIUM |
| SI-004 | CRA | Vulnerability disclosure process | Need security.txt + contact email | MEDIUM |

---

## 8. REGULATORY GAPS IDENTIFIED

| Gap ID | Regulation | Clause | Sub-Domain | Gap Description | Risk Level |
|--------|------------|--------|------------|-----------------|------------|
| GAP-001 | GDPR | Art.30 | D-09.4 | No records of processing activities | HIGH |
| GAP-002 | GDPR | Art.32 | D-01 | No formal security policy | MEDIUM |
| GAP-003 | CRA | Art.18 | D-06.2 | No SBOM (Software Bill of Materials) | HIGH |
| GAP-004 | CRA | Art.21 | D-02.3 | No vulnerability disclosure process | MEDIUM |

---


---

## §9 Per-Article Detailed Breakdown (54 articles)

> Fase de Especificação 5 enrichment — per-article table mapping each clause to its sub-domain, obligated party, verification criteria, evidence type, risk, and implementation posture. Source: `phase1_ontology.yaml:clause_mappings[]` (28 GDPR + 26 CRA = 54 articles). **NO Effort/Cost/Timeline fields added per Fase de Especificação 5 scope.**

| Stat | Value |
|------|-------|
| Total articles | 54 |
| GDPR articles | 28 |
| CRA articles | 26 |
| Sub-domains referenced | 26 |

| Article | Topic | Sub-Domains | Obligated Party | Verification Criteria | Evidence Type | Risk if not met | Implementation Status |
|---------|-------|-------------|-----------------|----------------------|---------------|------------------|---------------------|
| Art. 1 | Subject matter and scope | D-07.1 | manufacturer | Operational check per Doc 07c Appendix A §A.1.1/D-07.1 | DEMONSTRATE + INSPECT (SSDF checklist + SAMM posture) | MEDIUM | PARTIAL |
| Art. 2 | Definitions | D-07.1 | — | Operational check per Doc 07c Appendix A §A.1.1/D-07.1 | DEMONSTRATE + INSPECT (SSDF checklist + SAMM posture) | MEDIUM | PARTIAL |
| Art. 3 | Security requirements | D-03.4 | — | Operational check per Doc 07c Appendix A §A.1.1/D-03.4 | DEMONSTRATE + INSPECT (account-level block + Firebase config) | MEDIUM | PARTIAL |
| Art. 4 | Vulnerability handling | D-02.2 | — | Operational check per Doc 07c Appendix A §A.1.1/D-02.2 | DEMONSTRATE + INSPECT (Patch Manager logs + patch log) | MEDIUM | PARTIAL |
| Art. 5 | Security updates | D-02.1 | — | Operational check per Doc 07c Appendix A §A.1.1/D-02.1 | DEMONSTRATE + INSPECT (CI scan output + advisory feed) | MEDIUM | PARTIAL |
| Art. 6 | Incident reporting | D-04.1 | — | Operational check per Doc 07c Appendix A §A.1.1/D-04.1 | DEMONSTRATE + INSPECT (CloudWatch alarms + GuardDuty) | MEDIUM | PARTIAL |
| Art. 7 | Supply chain security | D-06.2 | — | Operational check per Doc 07c Appendix A §A.1.1/D-06.2 | DEMONSTRATE + INSPECT (SBOM per release) | MEDIUM | PARTIAL |
| Art. 8 | Secure defaults | D-03.4 | — | Operational check per Doc 07c Appendix A §A.1.1/D-03.4 | DEMONSTRATE + INSPECT (account-level block + Firebase config) | MEDIUM | PARTIAL |
| Art. 9 | Password security | D-03.2 | — | Operational check per Doc 07c Appendix A §A.1.1/D-03.2 | INSPECT (Firebase MFA enforcement + reset flow test) | MEDIUM | PARTIAL |
| Art. 10 | Identity authentication | D-03.1 | — | Operational check per Doc 07c Appendix A §A.1.1/D-03.1 | INSPECT (Firebase Auth user list + quarterly orphan scan) | MEDIUM | PARTIAL |
| Art. 11 | Data erasure | D-05.3 | — | Operational check per Doc 07c Appendix A §A.1.1/D-05.3 | DEMONSTRATE + INSPECT (erasure API + backup exclude policy) | HIGH | PARTIAL |
| Art. 12 | Availability at end of support | D-10.1 | — | Operational check per Doc 07c Appendix A §A.1.1/D-10.1 | DEMONSTRATE + INSPECT (CloudWatch + GuardDuty) | MEDIUM | PARTIAL |
| Art. 13 | Technical documentation | D-09.1 | — | Operational check per Doc 07c Appendix A §A.1.1/D-09.1 | DEMONSTRATE + INSPECT (policy template + review cadence) | MEDIUM | PARTIAL |
| Art. 14 | Conformity assessment | D-10.3 | — | Operational check per Doc 07c Appendix A §A.1.1/D-10.3 | DEMONSTRATE + INSPECT (quarterly checklist + annual self-attestation) | HIGH | PARTIAL |
| Art. 15 | CE marking | D-01.3 | — | Operational check per Doc 07c Appendix A §A.1.1/D-01.3 | INSPECT (KMS rotation status + key-custody review) | MEDIUM | PARTIAL |
| Art. 16 | Market surveillance | D-06.3 | — | Operational check per Doc 07c Appendix A §A.1.1/D-06.3 | DEMONSTRATE + INSPECT (DPA template + sub-processor list) | HIGH | PARTIAL |
| Art. 17 | Essential requirements for ICT products | D-02.1 | — | Operational check per Doc 07c Appendix A §A.1.1/D-02.1 | DEMONSTRATE + INSPECT (CI scan output + advisory feed) | MEDIUM | PARTIAL |
| Art. 18 | Security by design | D-07.1 | — | Operational check per Doc 07c Appendix A §A.1.1/D-07.1 | DEMONSTRATE + INSPECT (SSDF checklist + SAMM posture) | MEDIUM | PARTIAL |
| Art. 19 | Vulnerability handling and disclosure | D-02.3 | — | Operational check per Doc 07c Appendix A §A.1.1/D-02.3 | INSPECT (security.txt 200 + CVD page test email) | MEDIUM | PARTIAL |
| Art. 20 | Reporting incidents | D-04.3 | — | Operational check per Doc 07c Appendix A §A.1.1/D-04.3 | DEMONSTRATE + INSPECT (tabletop 24h notification drill) | HIGH | PARTIAL |
| Art. 21 | EU declarative conformity | D-10.3 | — | Operational check per Doc 07c Appendix A §A.1.1/D-10.3 | DEMONSTRATE + INSPECT (quarterly checklist + annual self-attestation) | HIGH | PARTIAL |
| Art. 22 | Traceability | D-10.2 | — | Operational check per Doc 07c Appendix A §A.1.1/D-10.2 | DEMONSTRATE + INSPECT (CloudTrail + Object Lock + 7y) | HIGH | PARTIAL |
| Art. 23 | Software security | D-07.1 | — | Operational check per Doc 07c Appendix A §A.1.1/D-07.1 | DEMONSTRATE + INSPECT (SSDF checklist + SAMM posture) | MEDIUM | PARTIAL |
| Art. 24 | Encrypted data storage | D-01.1 | — | Operational check per Doc 07c Appendix A §A.1.1/D-01.1 | INSPECT (config audit + annual review) | HIGH | PARTIAL |
| Art. 25 | Unauthorised access prevention | D-01.2 | — | Operational check per Doc 07c Appendix A §A.1.1/D-01.2 | INSPECT (config audit + annual cert renewal) | HIGH | PARTIAL |
| Art. 26 | Resilience to outages | D-04.4 | — | Operational check per Doc 07c Appendix A §A.1.1/D-04.4 | DEMONSTRATE + INSPECT (AWS Backup + quarterly DR test) | HIGH | PARTIAL |
| Art. 1 | Lawfulness of processing | D-05.1 | controller | Operational check per Doc 07c Appendix A §A.1.1/D-05.1 | DEMONSTRATE + INSPECT (schema validation + log scrub review) | MEDIUM | PARTIAL |
| Art. 2 | Material scope | D-05.1 | — | Operational check per Doc 07c Appendix A §A.1.1/D-05.1 | DEMONSTRATE + INSPECT (schema validation + log scrub review) | MEDIUM | PARTIAL |
| Art. 3 | Territorial scope | D-09.2 | — | Operational check per Doc 07c Appendix A §A.1.1/D-09.2 | DEMONSTRATE + INSPECT (DPIA + CRA-RA unified template) | HIGH | PARTIAL |
| Art. 5 | Principles relating to processing | D-01.1 | controller + processor | Operational check per Doc 07c Appendix A §A.1.1/D-01.1 | INSPECT (config audit + annual review) | HIGH | PARTIAL |
| Art. 6 | Lawfulness of processing | D-05.1 | — | Operational check per Doc 07c Appendix A §A.1.1/D-05.1 | DEMONSTRATE + INSPECT (schema validation + log scrub review) | MEDIUM | PARTIAL |
| Art. 7 | Conditions for consent | D-05.1 | — | Operational check per Doc 07c Appendix A §A.1.1/D-05.1 | DEMONSTRATE + INSPECT (schema validation + log scrub review) | MEDIUM | PARTIAL |
| Art. 8 | Conditions for child's consent | D-05.1 | — | Operational check per Doc 07c Appendix A §A.1.1/D-05.1 | DEMONSTRATE + INSPECT (schema validation + log scrub review) | MEDIUM | PARTIAL |
| Art. 9 | Processing of special categories | D-05.3 | — | Operational check per Doc 07c Appendix A §A.1.1/D-05.3 | DEMONSTRATE + INSPECT (erasure API + backup exclude policy) | HIGH | PARTIAL |
| Art. 12 | Transparent information and communication | D-09.4 | — | Operational check per Doc 07c Appendix A §A.1.1/D-09.4 | DEMONSTRATE + INSPECT (RoPA + 10y retention check) | HIGH | PARTIAL |
| Art. 13 | Information to be provided | D-09.4 | — | Operational check per Doc 07c Appendix A §A.1.1/D-09.4 | DEMONSTRATE + INSPECT (RoPA + 10y retention check) | HIGH | PARTIAL |
| Art. 14 | Information to be provided to data subject | D-09.4 | — | Operational check per Doc 07c Appendix A §A.1.1/D-09.4 | DEMONSTRATE + INSPECT (RoPA + 10y retention check) | HIGH | PARTIAL |
| Art. 15 | Right of access by data subject | D-05.4 | — | Operational check per Doc 07c Appendix A §A.1.1/D-05.4 | DEMONSTRATE + INSPECT (export endpoint + format check) | MEDIUM | PARTIAL |
| Art. 16 | Right to rectification | D-05.3 | — | Operational check per Doc 07c Appendix A §A.1.1/D-05.3 | DEMONSTRATE + INSPECT (erasure API + backup exclude policy) | HIGH | PARTIAL |
| Art. 17 | Right to erasure | D-05.3 | — | Operational check per Doc 07c Appendix A §A.1.1/D-05.3 | DEMONSTRATE + INSPECT (erasure API + backup exclude policy) | HIGH | PARTIAL |
| Art. 18 | Right to restriction of processing | D-05.3 | — | Operational check per Doc 07c Appendix A §A.1.1/D-05.3 | DEMONSTRATE + INSPECT (erasure API + backup exclude policy) | HIGH | PARTIAL |
| Art. 19 | Notification obligation | D-04.4 | — | Operational check per Doc 07c Appendix A §A.1.1/D-04.4 | DEMONSTRATE + INSPECT (AWS Backup + quarterly DR test) | HIGH | PARTIAL |
| Art. 20 | Right to data portability | D-05.4 | — | Operational check per Doc 07c Appendix A §A.1.1/D-05.4 | DEMONSTRATE + INSPECT (export endpoint + format check) | MEDIUM | PARTIAL |
| Art. 21 | Right to object | D-05.1 | — | Operational check per Doc 07c Appendix A §A.1.1/D-05.1 | DEMONSTRATE + INSPECT (schema validation + log scrub review) | MEDIUM | PARTIAL |
| Art. 22 | Automated decision-making | D-03.3 | — | Operational check per Doc 07c Appendix A §A.1.1/D-03.3 | DEMONSTRATE + INSPECT (IAM policies + RBAC matrix review) | MEDIUM | PARTIAL |
| Art. 25 | Data protection by design | D-07.1 | controller + processor | Operational check per Doc 07c Appendix A §A.1.1/D-07.1 | DEMONSTRATE + INSPECT (SSDF checklist + SAMM posture) | MEDIUM | PARTIAL |
| Art. 28 | Processor clauses (DPA, sub-processor auth, processing on instructions, security | D-06.3 | controller + processor | Operational check per Doc 07c Appendix A §A.1.1/D-06.3 | DEMONSTRATE + INSPECT (DPA template + sub-processor list) | HIGH | PARTIAL |
| Art. 30 | Records of processing activities (Art. 30(1) controller, Art. 30(2) processor's  | D-09.4 | controller + processor | Operational check per Doc 07c Appendix A §A.1.1/D-09.4 | DEMONSTRATE + INSPECT (RoPA + 10y retention check) | HIGH | PARTIAL |
| Art. 31 | Cooperation with supervisory authority | D-04.3 | controller + processor | Operational check per Doc 07c Appendix A §A.1.1/D-04.3 | DEMONSTRATE + INSPECT (tabletop 24h notification drill) | HIGH | PARTIAL |
| Art. 32 | Security of processing (Art. 32(1) controller+processor; Art. 32(2) processor ad | D-01.1 | controller + processor | Operational check per Doc 07c Appendix A §A.1.1/D-01.1 | INSPECT (config audit + annual review) | HIGH | PARTIAL |
| Art. 33 | Breach notification — Art. 33(1) controller to SA within 72h; Art. 33(2) process | D-04.3 | controller + processor | Operational check per Doc 07c Appendix A §A.1.1/D-04.3 | DEMONSTRATE + INSPECT (tabletop 24h notification drill) | HIGH | PARTIAL |
| Art. 34 | Breach notification to data subject | D-04.3 | — | Operational check per Doc 07c Appendix A §A.1.1/D-04.3 | DEMONSTRATE + INSPECT (tabletop 24h notification drill) | HIGH | PARTIAL |
| Art. 35 | Data protection impact assessment | D-09.2 | — | Operational check per Doc 07c Appendix A §A.1.1/D-09.2 | DEMONSTRATE + INSPECT (DPIA + CRA-RA unified template) | HIGH | PARTIAL |
| Art. 37 | Designation of DPO | D-08.2 | controller + processor | Operational check per Doc 07c Appendix A §A.1.1/D-08.2 | INSPECT (annual email + competency matrix review) | MEDIUM | PARTIAL |


**Reading guide:**
- **Article** — Regulation article reference (e.g., "Art. 5", "Art. 32(1)").
- **Topic** — One-line clause description from `phase1_ontology.yaml:clause_mappings[].description`.
- **Sub-Domains** — Sub-domain(s) this clause maps to. Multiple sub-domains = clause spans multiple areas.
- **Obligated Party** — Per `phase1_ontology.yaml:clause_mappings[].obligated_party`. GDPR Art. 32 + Art. 28 + Art. 30 + Art. 33(2) address both controller and processor (per Doc 05 §3.1 multi-actor note).
- **Verification Criteria** — Pointer to the operational check in Doc 07c Appendix A §A.1.1 (PG detail card for the sub-domain).
- **Evidence Type** — `INSPECT` (MINIMAL) or `DEMONSTRATE + INSPECT` (LIGHTWEIGHT) per Track B tier definition.
- **Risk if not met** — Qualitative H/M/L derived from priority + tier + sub-domain risk profile.
- **Implementation Status** — Current 2/4 → Target 3/4 for MUST LIGHTWEIGHT; NOT IMPLEMENTED for DEFERRED (D-02.4).

**Cross-references:**
- Each sub-domain maps to Doc 07c Appendix A §A.1.1 (PG detail card) or §A.2.1 (SG detail card) enrichment.
- Each tier inherits from Doc 07b §4 + §12 Track B Decision Table.
- Each clause ID (`GDPR-C01`..`GDPR-C28`, `CRA-C01`..`CRA-C26`) matches `phase1_ontology.yaml:clause_mappings[].clause_id` for full traceability.

---

## §10 Version History (Fase de Especificação 5 addition)

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-01 | Compliance Lead | Initial release - TinyTask SaaS case |
| 1.1 | 2026-04-11 | Compliance Lead | Added GDPR Art. 32 Processor obligations (NativeCompliance, not via DPA); Multi-Actor note for Controller + Processor roles |
| 1.2 | 2026-04-11 | Compliance Lead | Added GDPR Art. 33(2) "without undue delay" processor→controller distinction; Added CRA Art. 13(8) 5-year minimum support period, Art. 13(9) 10-year security update retention, Art. 13(13) 10-year documentation retention |
| 2.0 | 2026-08-06 | Fase de Especificação 5 Executor | **Deep enrichment — §6 Per-Article Detailed Breakdown** (54 rows: 28 GDPR + 26 CRA) with 8 fields per row: Article, Topic, Sub-Domains, Obligated Party, Verification Criteria, Evidence Type, Risk if not met, Implementation Status. **NO Effort/Cost/Timeline fields added** per Fase de Especificação 5 scope. Frontmatter updated: status → DEEP_ENRICHED, sprint → 5. |

---



## §11 DOCUMENT APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Document Author | Compliance Lead | | 2026-04-01 |
| Legal Counsel Review | | | |
| Technical Review (CTO) | | | |
| AEGIS Methodology Review | | | |

---

**Next Document:** 06_Clause_Mapping_Matrix.xlsx
**Gate Status:** ⏳ PENDING REVIEW
