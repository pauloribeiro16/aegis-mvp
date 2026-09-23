---
document_id: AEGIS-P2-RICH-01-INTAKE
title: AEGIS Intake Form — Company Context (SecureBorder Solutions)
version: 1.0
created: 2026-09-23
updated: 2026-09-23
author: Compliance Lead
status: RECONCILED
case: Case_02_SecureBorder_Solutions
applicable_regs: [GDPR, CRA, NIS2, AI_Act]
active_subdomains: 35
not_addressed: [D-07.4, D-08.3, D-09.3]
inputs: [baseline/00_Taxonomy_Reference.md]
outputs: [Doc02_Adjusted_Goals.md]
traceability: AEGIS Class Model → CompanyContext class
related_documents: [baseline/00_Taxonomy_Reference.md]
---

# AEGIS Intake Form — Company Context Assessment (SecureBorder Solutions)

## CHANGELOG

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-09-23 | Initial Case_02 release — streamlined layered intake (Layer 0 profile, Layer 1 decision tree, Layer 2 conditional context, Layer 3 regulatory interactions). |

---

## 1. PURPOSE

This document is the **structured intake form** for AEGIS Phase 1. It captures company facts through a layered approach: Layer 0 (static profile), Layer 1 (regulatory decision tree), Layer 2 (conditional questions based on applicability).

**Gate Criteria:**
- [x] Layer 0 (Company Profile) complete
- [x] Layer 1 (Regulatory Decision Tree) completed for all 5 regulations
- [x] Layer 2: Conditional blocks answered based on trigger conditions
- [x] Layer 3 (Regulatory Interaction Scans) completed
- [x] complexityTier derived and recorded
- [x] No "TBD" or "TODO" responses remain
- [x] Regulatory applicability flags confirmed

---

## 2. LAYER 0 — COMPANY PROFILE

**Purpose:** Capture foundational company facts that determine regulatory applicability.

### 2.1 Basic Information

| Field | Value | Notes |
|-------|-------|-------|
| Company Legal Name | SecureBorder Solutions B.V. | |
| Registration Country | Netherlands (EU) | |
| HQ Location | Amsterdam, Netherlands | |
| Legal Structure | Private Limited Company (B.V.) | Dutch besloten vennootschap |
| Website / Contact | info@secureborder.eu | Automated border-control gates and identity management |

### 2.2 Size Classification

| Field | Value | Threshold Check |
|-------|-------|----------------|
| Number of Employees | 450 | >250 = Large, >50 = Medium, ≤50 = Small |
| Annual Revenue (EUR) | ~€120M | >€50M = Large, >€10M = Medium, ≤€10M = Small |
| EU Size Classification | Medium-Large (MEDIUM scale band for proportionality) | Per EU recommendation 2003/361 |

### 2.3 Business Sector

| Field | Value | Regulatory Relevance |
|-------|-------|---------------------|
| Primary Industry Sector | Defense, Security & Critical Infrastructure | NIS 2 Annex I — Essential sector (border control) |
| Secondary Sectors (if any) | None | |
| Service Criticality | **Essential/Critical** | Critical component for airport and border operations across multiple Member States |

---

## 3. LAYER 1 — REGULATORY DECISION TREE

**Purpose:** Determine which regulations apply through branching logic.

### 3.1 Applicability Assessment Table

| Regulation | Decision Points & Triggers | Result | Role(s) | Summary Rationale |
|------------|----------------------------|--------|---------|-------------------|
| **GDPR** | Processes EU personal data on a continuous, large-scale basis — traveller biometric templates (Art. 9 special category), passport data, watchlist-derived decisions, employee data | **APPLICABLE** | CONTROLLER + PROCESSOR | Processor for traveller data (government authorities are controllers); Controller for employee data and audit logs |
| **CRA** | Manufactures and places products with digital elements on the EU market (eGate kiosks: hardware + on-board AI software) | **APPLICABLE** | MANUFACTURER | **Critical Class** product (border-control security function); notified-body conformity assessment |
| **NIS 2** | Security sector (border control, Annex I); 450 employees; supplier of services to essential entities | **APPLICABLE** | ESSENTIAL ENTITY SUPPLIER | Essential-entity supplier scope; Art. 21 risk-management measures and Art. 23 incident notification bind directly |
| **DORA** | Not a financial entity; provides no ICT services to financial entities | **NOT APPLICABLE** | — | Fails both Art. 2 limbs (financial entity; ICT third-party provider to financial entities) |
| **AI Act** | Develops and operates an AI system for border control — Annex III high-risk use case (migration, asylum and border control management) | **APPLICABLE** | PROVIDER + DEPLOYER | Provider of the on-board verification AI; deployer-side obligations flow through airport/government customers; notified-body conformity assessment |

**Complexity Tier:** HIGH (4 regulations applicable, 7 conditional blocks activated, 5 regulatory interactions)

---

## 4. LAYER 2 — CONDITIONAL CONTEXT

**Purpose:** Capture specific operational parameters triggered by applicable regulations.

### 4.1 AI Governance Parameters (AI Act)
- **AI System Classification:** Annex III use case (border control management); biometric verification is 1:1 (verification, not identification).
- **Conformity Assessment:** Notified body required for the high-risk AI system.
- **Human Oversight:** Human-in-the-loop for all decisions; border control officers can review and override AI decisions in real time.
- **Post-Market Monitoring:** Defined; continuous monitoring of accuracy, drift and demographic disparities through the security operations centre.
- **Prohibited Practices (Art. 5):** Confirmed not applicable (no subliminal manipulation, no biometric categorisation).
- **Risk Management System:** Defined; extends the certified risk-management process to the AI lifecycle.

### 4.2 NIS 2 / Security Operations Parameters
- **Entity Classification:** Essential-entity supplier (services to essential entities under NIS 2 Art. 3).
- **Incident Response Capability:** Dedicated team; 24/7 in-house security operations centre.
- **Business Continuity:** Documented and tested annually; covers all per-airport deployments.
- **Supply Chain Security:** Formal programme; hardware suppliers audited, component records required from all vendors.
- **Crisis Communication:** Defined procedures for regulatory and public notification.

### 4.3 Security Organisation Maturity Parameters
- **CISO Appointment:** Appointed; dedicated security organisation (>25 staff).
- **DPO Appointment:** Mandatory — large-scale processing of special-category biometric data.
- **Management System Certification:** Certified information-security and privacy management system (ISMS), annually audited.
- **Security Training:** Formal programme; annual awareness plus role-specific curricula.
- **Internal Audit:** Dedicated internal audit function for compliance verification.

### 4.4 Special Category Data Parameters (GDPR)
- **Art. 9(2) Legal Basis:** Art. 9(2)(g) — substantial public interest (government contracts for border control).
- **DPIA Requirement:** Mandatory by statute (large-scale biometric processing).
- **Consent Feasibility:** Not applicable — legal-obligation basis; consent not viable.
- **Protection Measures:** Encryption, access control, audit trails, retention limits — beyond standard Art. 32 measures; raw biometric captures discarded immediately after template extraction.

### 4.5 Supply Chain Parameters (CRA / NIS 2)
- **Component Tracking:** Software bills of materials generated and maintained per release (Critical Class requirement).
- **Supplier Evaluation:** Formal process; hardware suppliers audited; security documentation required contractually.
- **Component Vulnerability Management:** Continuous monitoring across hardware and software components.

### 4.6 CRA Classification Parameters
- **Product Class:** **Critical** (border-control security function, hardware + software eGate).
- **Conformity Assessment:** Notified body (third-party assessment).
- **Exclusion Check:** Confirmed in scope (connected product not falling under Art. 24 exclusions).
- **EU Cybersecurity Scheme:** None published for this product category; self-declaration not permitted for Critical Class.

### 4.7 Multi-Actor Roles
- **Per-Data-Element Assignment:** Processor for traveller data; Controller for employee data and audit logs.
- **Cross-Regulation Roles:** CRA = manufacturer; GDPR = processor (traveller data) / controller (employee data); AI Act = provider + deployer; NIS 2 = essential-entity supplier.
- **Processor Native Compliance:** Yes — direct Art. 32 obligations apply to the processing role.

---

## 5. LAYER 3 — REGULATORY INTERACTIONS

**Purpose:** Identify timing, procedural, and negative constraints arising from simultaneous applicability.

### 5.1 Temporal Conflict Scan

| Conflict ID | Regulation A | Deadline A | Regulation B | Deadline B | Resolution Principle |
|-------------|-------------|------------|-------------|------------|---------------------|
| TC-001 | CRA Art. 14 | 24h (actively exploited vulnerability early warning) | GDPR Art. 33 | 72h (breach notification) | Max-SLA: single workflow on the 24h clock |
| TC-002 | NIS 2 Art. 23 | 24h (early warning) | GDPR Art. 33 | 72h (breach notification) | Max-SLA: single workflow on the 24h clock |
| TC-003 | AI Act Art. 73 | 15 days default / 10 / 2 days (serious incidents) | NIS 2 Art. 23 | 24h (incident early warning) | Separate workflows, one incident record |

### 5.2 Requirement Conflict Scan

| Conflict ID | Regulation A | Requirement A | Regulation B | Requirement B | Resolution |
|-------------|-------------|--------------|-------------|--------------|------------|
| RC-001 | GDPR Art. 17 | Right to erasure of traveller data | AI Act Art. 12/19 (+ national border-security law) | Event logging with retention floor | Token-based separation: biometric material irreversibly de-linked and purged; token-only decision records retained under the longest applicable floor |

### 5.3 Trigger Mismatch Scan

| Conflict ID | Assessment Type | Trigger A | Trigger B | Resolution |
|-------------|----------------|-----------|-----------|------------|
| TM-001 | DPIA / FRIA / risk assessment | GDPR: large-scale Art. 9 processing (DPIA) | AI Act: high-risk system (risk management + fundamental-rights leg) | Unified assessment pass with dual outputs |

### 5.4 Negative Scope Confirmation

| Item | Regulation | Provision | Non-Applicability Confirmed? | Rationale |
|------|-----------|-----------|------------------------------|-----------|
| NA-001 | AI Act | Art. 5 (Prohibited practices) | YES | Biometrics used for border-control verification, not for prohibited purposes |
| NA-002 | CRA | Art. 24 (Exclusions) | YES | Connected eGate product not in the exclusion list |
| NA-003 | GDPR | Art. 37 (DPO designation) | YES — DPO REQUIRED | Large-scale processing of special-category data triggers mandatory designation |
| NA-004 | NIS 2 | Art. 3 (Entity scope) | YES — IN SCOPE | Essential-entity supplier with ≥50 employees in an Annex I sector |
| NA-005 | DORA | Art. 2 (Material scope) | YES — NOT APPLICABLE | Not a financial entity; no ICT services provided to financial entities |

---

## 6. ORGANISATION INTERPRETATION DOUBTS

Specific operational doubts raised regarding regulatory interpretation at MEDIUM scale:

| ID | Doubt | Source Provision | Organisation Interpretation | Downstream Impact |
|----|-------|------------------|-----------------------------|-------------------|
| ORG-INT-01 | Notified-body timeline for Critical Class conformity | CRA Art. 32 + Annex VI | Assessment planned as gate criterion before market expansion; contract already signed with the assessment body | D-09.4 technical documentation; D-10.3 conformity testing |
| ORG-INT-02 | Biometric template retention versus erasure | GDPR Art. 17 vs AI Act Art. 19 | Token-only decision records retainable; biometric material purged irreversibly on erasure request | D-05.2/D-05.3 retention-erasure boundary (T-002) |
| ORG-INT-03 | Essential-entity supplier classification | NIS 2 Art. 3 | Classified as essential-entity supplier; Art. 21/23 obligations accepted in full (no important-entity downgrade) | D-04.3 notification cadence; D-09.1 management-body liability |
| ORG-INT-04 | Processor-side breach clock | GDPR Art. 33(2) | Processor notification to the government controller runs without undue delay on awareness; internal clock anchored at 24h | D-04.3 unified notification workflow (T-001) |
| ORG-INT-05 | Deployer-role boundaries for high-risk AI | AI Act Art. 26 | Deployer obligations flow through airport/government customers; the company discharges them contractually and via oversight tooling + training | D-08.2 oversight competence; D-10.1 post-market monitoring |

---

## 7. BUSINESS GOALS (Contextual Anchors)

| ID | Description | Priority | Related Regulations | Target Metric |
|----|-------------|----------|---------------------|---------------|
| BG-01 | Maintain EU regulatory compliance across the four applicable regimes | HIGH | GDPR, CRA, NIS 2, AI Act | Zero major non-conformities |
| BG-02 | Achieve Critical Class conformity (notified body) for the eGate product | HIGH | CRA | Conformity assessment completed; technical documentation approved |
| BG-03 | Complete high-risk AI conformity and post-market monitoring readiness | HIGH | AI Act | Conformity file complete; monitoring system operational |
| BG-04 | Expand to 5 additional Schengen countries within 18 months without compliance regressions | MEDIUM | GDPR, CRA, NIS 2, AI Act | Per-country deployment checklist 100% complete |
| BG-05 | Reduce incident detection and notification latency | MEDIUM | GDPR, CRA, NIS 2 | Max-SLA 24h notification discipline maintained |
| BG-06 | Sustain certified management-system coverage across all per-airport deployments | LOW | GDPR, NIS 2 | Annual external audit passed with zero major findings |

---

## 8. DOCUMENT APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Document Author | Compliance Lead | | 2026-09-23 |
| Technical Review (CTO) | | | |
| Business Review (CEO) | | | |
| AEGIS Methodology Review | | | |
