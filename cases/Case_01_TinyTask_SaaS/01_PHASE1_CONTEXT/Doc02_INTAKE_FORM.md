---
document_id: AEGIS-COMMON-01
title: AEGIS Intake Form — Company Context
version: 2.1
created: 2026-04-01
updated: 2026-08-06
author: Compliance Lead (Fase de Especificação 1 reconciliation)
status: RECONCILED
inputs: [Doc01_Taxonomy_Reference.md]
outputs: [Doc03_Company_Context_Assessment.md]
<!-- Note: 02_Regulatory_Mapping_Master.md is DEPRECATED as of Phase 1 v1.2 (2026-07-13). Use 00_METHODOLOGY/PREPROCESSING_by_domain/domains/ corpus or 00_Taxonomy_Reference.md instead. -->
traceability: AEGIS Class Model → CompanyContext class
related_documents: [00_Taxonomy_Reference.md]
---

> **Fase de Especificação 1 Reconciliation Note (2026-08-06)**
> Rich Mode copy of legacy `02_CASES/Case_01_TinyTask_SaaS/00_COMMON/01_Company_Context.md` (v2.0). File renamed from `01_Company_Context.md` → `01_INTAKE_FORM.md` per Rich Mode naming convention (this doc is the case's Intake Form, not a generic company context doc). Fase de Especificação 1 changes:
> - **I-10 (status DRAFT → RECONCILED):** Fase de Especificação 1 milestone.
> - **I-13 (02_Regulatory_Mapping_Master.md deprecation):** Banner added in frontmatter. `02_Regulatory_Mapping_Master.md` was previously cited as a downstream output; it is deprecated and superseded by `00_Taxonomy_Reference.md` + corpus.
> - Body content unchanged from legacy. Fase de Especificação 2 will add L2 manifest cross-references per answered question.

# AEGIS Intake Form — Company Context Assessment

## CHANGELOG

| Version | Date | Changes |
|---------|------|---------|
| 2.0 | 2026-04-23 | Converted to layered intake format — Layer 0 (Company Profile), Layer 1 (Decision Tree), Layer 2 (Conditional Blocks) |
| 1.0 | 2026-04-01 | Initial release - TinyTask SaaS case (legacy format) |

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
| Company Legal Name | TinyTask Lda. | |
| Registration Country | Portugal (EU) | |
| HQ Location | Lisbon, Portugal | |
| Legal Structure | Private Limited Company (Lda.) | Portuguese sociedade por quotas |
| Website / Contact | info@tinytask.eu | B2B SaaS productivity tools |

### 2.2 Size Classification

| Field | Value | Threshold Check |
|-------|-------|----------------|
| Number of Employees | 8 | >250 = Large, >50 = Medium, ≤50 = Small |
| Annual Revenue (EUR) | <€2M | >€50M = Large, >€10M = Medium, ≤€10M = Small |
| EU Size Classification | Micro-enterprise | Per EU recommendation 2003/361 |

### 2.3 Business Sector

| Field | Value | Regulatory Relevance |
|-------|-------|---------------------|
| Primary Industry Sector | Technology / Software | NIS 2 Annex I/II — NOT CLASSIFIED (not essential/important sector) |
| Secondary Sectors (if any) | None | |
| Service Criticality | Non-Critical | Not essential service; downtime inconvenient but not catastrophic |

---

## 3. LAYER 1 — REGULATORY DECISION TREE

**Purpose:** Determine which regulations apply through branching logic.

### 3.1 GDPR Applicability

```
START: Does the company process personal data of EU residents?
├── YES ──────────────────┐
│                        │
│  Is the processing      │
│  purely local/household│
│  activity?             │
│  ├── YES → GDPR: NOT  │
│  │     APPLICABLE     │
│  └── NO ──────────────→ GDPR: APPLICABLE
│                        │
└── NO → GDPR: NOT APPLICABLE
```

| Decision Point | Answer | GDPR Applicable? |
|----------------|--------|-----------------|
| Processes EU resident personal data? | YES | Data types: Emails, Names, Passwords, Task Content |
| Any exemption (household/individual)? | NO | Commercial B2B SaaS operations |

**GDPR Roles (circle applicable):**
- **CONTROLLER** (decides purposes/means) — for account data, user content
- **PROCESSOR** (processes on behalf of controller) — for B2B client content
- BOTH (mixed controller/processor) — applies to TinyTask

### 3.2 CRA Applicability

```
START: Does the company place products on the EU market?
├── YES ──────────────────┐
│                        │
│  Does the product      │
│  have digital         │
│  elements?            │
│  ├── NO → CRA: NOT   │
│  │     APPLICABLE    │
│  └── YES ───────────→ CRA: APPLICABLE
│                        │
│  Product Class?        │
│  ├── Default          │ ← SELECTED
│  ├── Important Class I│
│  ├── Important Class II│
│  └── Critical         │
│
└── NO → CRA: NOT APPLICABLE
```

| Decision Point | Answer | CRA Applicable? |
|----------------|--------|-----------------|
| Places products on EU market? | YES | SaaS delivered to EU customers |
| Product has digital elements? | YES | Web App + Mobile App |
| Product Class | Default | No critical functionality per CRA Art. 7 |

**CRA Roles:**
- MANUFACTURER (develops and places on EU market)

### 3.3 NIS 2 Applicability

```
START: Is the company in a NIS 2 sector?
├── YES ──────────────────┐
│  Technology sector      │
│  (not in Annex I/II)   │
│                        │
│  Annex II?             │
│  (cloud, DC, CDN, MSP, │
│   marketplace, search,  │
│   social)               │
│  ├── NO → NIS 2:      │
│  │    NOT APPLICABLE   │
│  └── YES → Check size │
│                        │
│  SIZE THRESHOLDS:      │
│  ├── ≥50 employees OR │
│  ├── ≥€10M revenue    │
│  └── ANY → NIS 2:    │
│       APPLICABLE      │
│
│  8 employees, <€10M   │
│  → BELOW THRESHOLD    │
│
└── NO → NIS 2: NOT APPLICABLE
```

| Decision Point | Answer | NIS 2 Applicable? |
|----------------|--------|-------------------|
| NIS 2 Sector (Annex I or II)? | NO | Technology/Software — not in NIS 2 sectors |
| Employees ≥50? | NO | 8 employees |
| Revenue ≥€10M? | NO | <€2M |
| Entity Type | Not classified | Below all thresholds |

**Result: NIS 2 — NOT APPLICABLE**

### 3.4 DORA Applicability

```
START: Is the company a financial entity?
├── YES ──────────────────┐
│                        │
│  Art. 2(1) entity?     │
│  (bank, investment,     │
│   insurance, payment,   │
│   crypto, UCITS, AIFM) │
│  ├── YES → DORA:     │
│  │    APPLICABLE      │
│  └── NO → ICT third   │
│       party to finance?│
│       ├── YES → DORA: │
│       │    APPLICABLE │
│       └── NO → DORA:  │
│            NOT APPLIC. │
│
└── NO → DORA: NOT APPLICABLE
```

| Decision Point | Answer | DORA Applicable? |
|----------------|--------|-----------------|
| Financial entity per Art. 2? | NO | B2B SaaS productivity tool; Stripe handles payments |
| ICT provider to financial entities? | NO | Not providing ICT services to financial entities |

**Result: DORA — NOT APPLICABLE**

### 3.5 AI Act Applicability

```
START: Does the company develop/deploy/use AI systems?
├── YES ──────────────────┐
│  Rule-based task         │
│  management; no AI/ML   │
│                        │
│  Annex II product?     │
│  (AI-enabled products) │
│  ├── YES → High-risk  │
│  │    PROVIDER        │
│  └── NO → Annex III  │
│       use case?        │
│       (biometric, ... ) │
│       ├── YES → High  │
│       │    -risk      │
│       │    DEPLOYER   │
│       └── NO → Check  │
│            prohibited? │
│            (Art. 5)   │
│            ├── YES →  │
│            │    PROHIB-│
│            │    ITED  │
│            └── NO →   │
│                 Limited│
│                 /Min-  │
│                 imal   │
│                 risk   │
│
└── NO → AI Act: NOT APPLICABLE
```

| Decision Point | Answer | AI Act Applicable? |
|----------------|--------|---------------------|
| AI system present? | NO | Rule-based task management; no machine learning |
| Annex II product? | NO | Standard SaaS product |
| Annex III use case? | NO | No AI-enabled decision-making |

**Result: AI Act — NOT APPLICABLE**

### 3.6 APPLICABILITY SUMMARY

| Regulation | Applicable | Confidence | Role(s) | Notes |
|------------|------------|------------|---------|-------|
| GDPR | **YES** | HIGH | CONTROLLER / PROCESSOR / BOTH | Processes personal data of EU residents |
| CRA | **YES** | HIGH | MANUFACTURER | Places digital products on EU market; Default class |
| NIS 2 | **NO** | HIGH | — | Below all thresholds (8 employees, <€2M) |
| DORA | **NO** | HIGH | — | Not a financial entity |
| AI Act | **NO** | HIGH | — | No AI/ML systems deployed |

**Complexity Tier:** MEDIUM (2 regulations applicable)

---

## 4. LAYER 2 — CONDITIONAL QUESTIONS

**Purpose:** Capture additional context based on applicable regulations.

### 4.1 Block Activation Matrix

| Block ID | Trigger Condition | Status | Questions |
|----------|------------------|--------|-----------|
| B1: AI Governance | AI Act applicable | NOT APPLICABLE | Q39-Q46 |
| B2: NIS 2 / SOC | NIS 2 applicable | NOT APPLICABLE | Q47-Q52 |
| B3: DORA Financial | DORA applicable | NOT APPLICABLE | Q53-Q56 |
| B4: Security Org | size ≥50 OR posture ≥Managed | NOT APPLICABLE | Q57-Q61 |
| B5: Special Category Data | GDPR + special category data | NOT APPLICABLE | Q62-Q65 |
| **B6: Supply Chain** | supplyChainVisibility = Low | **ACTIVATED** | Q66-Q68 |
| **B7: CRA Classification** | CRA applicable | **ACTIVATED** | Q69-Q72 |
| **B8: Multi-Actor Roles** | 2+ regulations OR mixed roles | **ACTIVATED** | Q73-Q75 |

**Block Activation Statement:**
> Block B1: NOT APPLICABLE — AI Act not applicable
> Block B2: NOT APPLICABLE — NIS 2 not applicable
> Block B3: NOT APPLICABLE — DORA not applicable
> Block B4: NOT APPLICABLE — 8 employees, securityPosture = None
> Block B5: NOT APPLICABLE — No special category data
> Block B6: **ACTIVATED** — supplyChainVisibility = Low (open source not tracked)
> Block B7: **ACTIVATED** — CRA applicable (Default class)
> Block B8: **ACTIVATED** — GDPR (controller/processor) + CRA (manufacturer)

---

#### BLOCK B6: Supply Chain Extension
**Trigger:** supplyChainVisibility = Low
**Activated:** YES

| Question | Response | Notes |
|----------|----------|-------|
| Q66: SBOM Practices | Not started | No formal SBOM; npm/pip dependencies not tracked |
| Q67: Supplier Security Assessment | None | No formal supplier evaluation process |
| Q68: Component Vulnerability Management | Manual review (occasional) | Dependencies checked ad-hoc when issues arise |

---

#### BLOCK B7: CRA Classification Extension
**Trigger:** CRA applicable
**Activated:** YES

| Question | Response | Notes |
|----------|----------|-------|
| Q69: CRA Product Class | Default | SaaS product; no critical functionality per CRA Art. 7 |
| Q70: Conformity Assessment Regime | Self-assessment | Standard digital product; self-assessment applicable |
| Q71: Art. 24 Exclusion Check | Confirmed not excluded | SaaS product with connectivity; not in CRA Art. 24 exclusions |
| Q72: EU Certification Scheme Availability | No scheme available | No EU cybersecurity certification scheme for SaaS category |

---

#### BLOCK B8: Multi-Actor Role Resolution Extension
**Trigger:** 2+ regulations applicable AND dataRole = Mixed
**Activated:** YES

| Question | Response | Notes |
|----------|----------|-------|
| Q73: Per-Data-Element Role Assignment | Controller for account data; Processor for client content | Email/Name/Password = Controller; Task Content = Processor |
| Q74: Cross-Regulation Role Implications | CRA = manufacturer; GDPR = controller/processor | Multiple roles across applicable regulations |
| Q75: Processor Native Compliance | No — inherited obligations only | No direct Art. 32-type obligations as processor |

---

## 5. LAYER 3 — REGULATORY INTERACTION SCANS

**Purpose:** Identify conflicts and tensions when 2+ regulations apply.
**Required when:** 2+ regulations applicable — **ACTIVE (GDPR + CRA)**

### 5.1 Scan 1: Temporal Conflict Scan

| Conflict ID | Regulation A | Deadline A | Regulation B | Deadline B | Conflict Type | Resolution Principle |
|-------------|-------------|------------|-------------|------------|---------------|---------------------|
| TC-001 | CRA Art. 14 | 24h (vulnerability) | GDPR Art. 33 | 72h (breach) | Same event, different deadlines | Max-SLA: use 24h workflow |

### 5.2 Scan 2: Requirement Conflict Scan

No requirement conflicts identified for TinyTask profile.

### 5.3 Scan 3: Trigger Mismatch Scan

No trigger mismatches identified at current applicability profile.

### 5.4 Scan 4: Negative Analysis Checklist

| Item | Regulation | Provision | Non-Applicability Confirmed? | Rationale |
|------|-----------|-----------|------------------------------|-----------|
| NA-001 | AI Act | Art. 5 (Prohibited practices) | YES | No AI/ML systems deployed |
| NA-002 | CRA | Art. 24 (Exclusions) | YES | SaaS product with connectivity; not in exclusions |
| NA-003 | AI Act | Art. 25 (Downstream provider) | YES | Customers unlikely to substantially modify web app |
| NA-004 | GDPR | Art. 37 (DPO mandatory) | YES | Below Art. 30 threshold (small-scale processing) |
| NA-005 | NIS 2 | Art. 3 (Entity classification) | YES | 8 employees; below 50 threshold |

### 5.5 Interaction Summary

| Metric | Value |
|--------|-------|
| Applicable Regulations | 2/5 (GDPR, CRA) |
| Active Conditional Blocks | B6, B7, B8 |
| Temporal Conflicts Identified | 1 |
| Requirement Conflicts Identified | 0 |
| Trigger Mismatches Identified | 0 |
| Negative Analyses Completed | 5/5 |
| **Complexity Tier (Final)** | MEDIUM |

---

## 6. IMPLEMENTATION READINESS PREVIEW

### 6.1 Client Declaration vs System Verification

| Regulation | Client Declaration | System Check | Final Applicable | Confidence |
|------------|-------------------|--------------|------------------|------------|
| GDPR | YES | processes_personal_data = TRUE | YES | HIGH |
| CRA | YES | Digital product + EU market = TRUE | YES | HIGH |
| NIS 2 | NO | Below all thresholds | NO | HIGH |
| DORA | NO | Not financial entity | NO | HIGH |
| AI Act | NO | No AI systems present | NO | HIGH |

### 6.2 Implementation Readiness Areas

| Area | Question | Response | Evidence / Notes |
|------|----------|----------|------------------|
| IR-01: Governance | Named security responsible? | NO | No CISO; all 8 employees are developers |
| IR-02: DPO | DPO appointed/required? | NOT REQUIRED | Below Art. 30 threshold |
| IR-03: Incident Response | Incident response capability? | PARTIAL | Basic procedures; no formal IR team |
| IR-04: Business Continuity | BCP documented? | PARTIAL | Ad-hoc backup procedures; no formal BCP |
| IR-05: Data Processing Register | Art. 30 register? | NO | Not started |
| IR-06: Supplier Register | Critical suppliers tracked? | NO | No formal register |
| IR-07: Security Policies | Documented security policies? | PARTIAL | Basic password policy only |
| IR-08: Training | Security training program? | NO | No formal training |
| IR-09: Access Control | Formal access control policy? | PARTIAL | Basic RBAC; no MFA implemented |
| IR-10: Data Classification | Data classification scheme? | NO | Not defined |
| IR-11: Asset Inventory | IT asset inventory? | PARTIAL | Basic list; no CMDB |
| IR-12: Risk Management | Risk management process? | NO | Not formalized |

### 6.3 Implementation Readiness Summary

| Metric | Count |
|--------|-------|
| Total Areas Assessed | 12 |
| Fully Implemented (YES) | 0 |
| Partially Implemented | 5 |
| Not Implemented (NO) | 7 |
| **Readiness Score** | 5/12 — LOW |

### 6.4 Existing Implementation Posture (observed)

> **Added 2026-09-14** (F1-pilot C1 fold). Aligns each Implementation Readiness area from §6.2 with the Implementation Posture Model — see [`00_METHODOLOGY/IMPLEMENTATION_POSTURE_MODEL_CSF_STRICT.md`](../../../../00_METHODOLOGY/IMPLEMENTATION_POSTURE_MODEL_CSF_STRICT.md) v2.0. **Three states only** — IMPLEMENTED / PARTIAL / NOT IMPLEMENTED. No numerical scores, no Tiers (T1-T4 prohibited per the CSF-strict canon). Used as qualitative input by Phase 2 `Doc19_Framework_Mapping_Matrix.md` §5.1.

| Area | Readiness (from §6.2) | Posture State | Rationale |
|------|------------------------|---------------|-----------|
| IR-01: Governance | NO | NOT IMPLEMENTED | No CISO; 8 dev-only employees |
| IR-02: DPO | NOT REQUIRED | NOT IMPLEMENTED | Below Art. 30 threshold; voluntary DPO hat on CEO |
| IR-03: Incident Response | PARTIAL | PARTIAL | Basic procedures; no formal IR team |
| IR-04: Business Continuity | PARTIAL | PARTIAL | Ad-hoc backup; no formal BCP, no restore tests |
| IR-05: Data Processing Register | NO | NOT IMPLEMENTED | Art. 30 register not started |
| IR-06: Supplier Register | NO | NOT IMPLEMENTED | No formal register (Doc06 inventory exists but not RoPA-grade) |
| IR-07: Security Policies | PARTIAL | PARTIAL | Basic password policy only |
| IR-08: Training | NO | NOT IMPLEMENTED | No formal training programme |
| IR-09: Access Control | PARTIAL | PARTIAL | Basic RBAC; no MFA for customers |
| IR-10: Data Classification | NO | NOT IMPLEMENTED | Scheme not defined |
| IR-11: Asset Inventory | PARTIAL | PARTIAL | Basic list; no CMDB |
| IR-12: Risk Management | NO | NOT IMPLEMENTED | Not formalized |

**Detailed qualitative evidence per control area** lives in [`Doc05_Security_Posture.md §2`](Doc05_Security_Posture.md) (historical instance — `DEPRECATED_FOR_MATURITY` since 2026-08-27; ownership of the formal posture scale at Phase 2 `Doc19_Framework_Mapping_Matrix.md §5.1`). The compact form above is the only Phase 1 deliverable for posture.

**Posture ownership declaration (per AEGIS P5):** any change to the column values here must be reflected in `Doc19 §5.1` rationale column and announced via `CHANGE_LOG_CENTRAL.md`. No Phase 1 doc owns the posture *scale*; Phase 1 owns the *observed state*.

---

## 7. STAKEHOLDERS × SUB-DOMAIN OWNERSHIP

> **Renamed 2026-09-14** (was `ROLE MATRIX`). Satisfies handoff artefact #8 (Role Matrix). The detailed per-activity RACI previously in `Doc07_Org_Roles_RACI.md` is folded into the compact form below; the historical instance remains in Doc07 for audit and parser liveness.

### 7.1 Role Matrix (regulation-centric)

| Regulation | Role(s) | Native Obligations | Inherited Obligations | Notes |
|------------|---------|-------------------|----------------------|-------|
| GDPR | CONTROLLER + PROCESSOR | Art. 32 security, Art. 33 breach notification | Via DPA from processors | Mixed role per data element |
| CRA | MANUFACTURER | Annex I essential requirements, Art. 13-14 reporting | Via contracts from suppliers | Default class; self-assessment |
| NIS 2 | — | — | — | NOT APPLICABLE |
| DORA | — | — | — | NOT APPLICABLE |
| AI Act | — | — | — | NOT APPLICABLE |

### 7.2 Sub-Domain × Accountable (compact ownership)

> Compiled from `Doc07_Org_Roles_RACI.md §4` (Fase de Especificação 2 enrichment) and the §10 Stakeholder roster. A = single sign-off; R = does the work. Dev = Lead Developer + developer team (5 staff, on-call rotation).

| Sub-domain | Accountable (A) | Responsible (R) | Notes |
|------------|-----------------|-----------------|-------|
| D-01 Data Protection | CTO/CISO | Lead Dev | DPO=R for D-05.3 erasure (Art. 17) |
| D-02 Vulnerability Mgmt | CTO/CISO | Lead Dev | Dev rota on-call for D-04.1 |
| D-03 Access Control | CTO/CISO | Lead Dev | Quarterly review not yet documented |
| D-04 Incident Response | CTO/CISO | Lead Dev | DPO=R for regulatory notification |
| D-05 Data Lifecycle | DPO (CEO) | Lead Dev | DPO owns erasure, retention; CTO owns encryption keys |
| D-06 Supply Chain | CTO/CISO | Lead Dev | DPO=R for DPA contracts |
| D-07 Secure Development | CTO/CISO | Lead Dev | Dev=R/A for code review self-check |
| D-08 Human Factors | DPO (CEO) for DPO competence; CTO/CISO for technical roles | CEO (HR coord) for awareness | D-08.3 INACTIVE — record explicitly |
| D-09 Governance | Board (policy approval); CTO/CISO (operations) | Lead Dev | Board=A on approvals |
| D-10 Monitoring & Audit | CTO/CISO | Lead Dev | — |

**Open Governance Gaps (handed to Phase 2 as input):**

| Gap ID | Description | Severity |
|--------|-------------|----------|
| GAP-GOV-01 | No formal security-awareness programme (IR-08 in §6.2 = NO) | MEDIUM |
| GAP-GOV-02 | No formal secure-coding curriculum for developers | MEDIUM |
| GAP-GOV-03 | DPO refresher not cadence-locked (last done 2025-Q4 informally) | LOW |
| GAP-GOV-04 | Single CISO-individual concentration risk (CTO wears CISO hat) | LOW |
| GAP-GOV-05 | D-08.3 board training absent — deliberately not in scope; recorded here as non-derivation per Doc05 §6.3 | LOW (informational) |

> The full per-activity RACI (41 activities × 7 columns) remains in [`Doc07_Org_Roles_RACI.md`](Doc07_Org_Roles_RACI.md) as a historical instance — folded 2026-09-14, body preserved for graph/parser liveness and audit traceability.

---

## 8. COMPLEXITY TIER DERIVATION

| Criterion | Threshold | Result |
|-----------|-----------|--------|
| Number of applicable regulations | ≥4 | — |
| | 2-3 | MEDIUM (2 regulations: GDPR, CRA) |
| Active conditional blocks | ≥4 | — |
| | 2-3 | MEDIUM (3 blocks: B6, B7, B8) |
| Regulatory interactions | ≥3 | — |
| | 1-2 | MEDIUM (1 temporal conflict) |

**Final Complexity Tier:** MEDIUM

---

## 9. GATE CRITERIA

### MEDIUM Complexity Tier
- [x] Layer 0 complete
- [x] At least 2 regulations applicable
- [x] Section 6.1: Client declaration vs system check
- [x] Section 6.2: Implementation Readiness (5/12 areas responded)
- [x] Layer 1 decision tree completed
- [x] Layer 2: 3 conditional blocks activated
- [x] Layer 3: Temporal Conflict Scan + Negative Analysis required
- [x] Role Matrix completed

---

## 10. STAKEHOLDERS

Stakeholders relevant to the regulatory compliance programme. Internal
parties drive strategy and implementation; external parties are either
data controllers (B2B customers) or sub-processors / suppliers (Stripe,
AWS).

| ID | Name | Role | Organisation | Contact | Responsibilities |
|----|------|------|--------------|---------|-----------------|
| SH-01 | CEO | Executive | TinyTask Lda. | ceo@tinytask.pt | Strategic direction, regulatory oversight, business accountability |
| SH-02 | CTO | Technical | TinyTask Lda. | cto@tinytask.pt | Engineering, security architecture, infrastructure decisions |
| SH-03 | DPO | Compliance | TinyTask Lda. (external advisor) | dpo@tinytask.pt | GDPR compliance, RoPA maintenance, breach response coordination |
| SH-04 | Dev Team | Technical | TinyTask Lda. | dev@tinytask.pt | Implementation, secure development, vulnerability remediation |
| SH-05 | B2B Customers | External | Various enterprises | (via portal) | Data controllers for project content uploaded by end users |
| SH-06 | Stripe | Supplier | Stripe Inc. | (via API) | Payment processing (sub-processor; PCI-DSS scope) |
| SH-07 | AWS | Supplier | Amazon Web Services (EU region) | (via console) | Cloud infrastructure (sub-processor; inherited controls) |

**ID Pattern:** `SH-{NN}` where `{NN}` is a 2-digit sequential number.

### 10.1 Stakeholder Influence Matrix

| Stakeholder ID | Influence Level | Interest Level | Engagement Strategy |
|----------------|----------------|----------------|---------------------|
| SH-01 | HIGH | HIGH | Weekly briefings; direct involvement in compliance decisions |
| SH-02 | HIGH | HIGH | Technical reviews; architecture decisions |
| SH-03 | MEDIUM | HIGH | Quarterly reviews; incident coordination |
| SH-04 | MEDIUM | MEDIUM | Sprint reviews; implementation feedback |
| SH-05 | LOW | HIGH | Annual review; contract updates; breach notifications |
| SH-06 | LOW | LOW | Ad-hoc coordination; compliance documentation review |
| SH-07 | LOW | LOW | Ad-hoc coordination; annual security review |

### 10.5 Interpretation Doubts Raised by this Organisation

> **Added 2026-09-14** (F1-pilot C1 fold). Generic regulatory interpretation lives in the methodology baseline [`00_METHODOLOGY/AMBIGUITY_REGISTRY/`](../../../../00_METHODOLOGY/AMBIGUITY_REGISTRY/README.md) (49 clauses dedup, 5 regulations). This section captures only interpretation doubts that **this organisation** raised while filling the intake — doubts whose resolution depends on the company's posture or operational scope, not on regulatory text alone. If no doubts were raised, write "None" and skip.

| ID | Doubt | Article / Source | Variant this organisation defends | Source of variant | Downstream Impact |
|----|-------|------------------|----------------------------------|-------------------|-------------------|
| ORG-INT-01 | For TinyTask's Stripe integration, is Stripe a sub-processor under Art. 28, given that card PAN is tokenised and never reaches TinyTask servers? | GDPR Art. 28(4) | **Yes** — Stripe is a sub-processor for payment data only; TinyTask stores only billing metadata + Stripe customer IDs. | EDPB Guidelines 07/2020 §3.1.3 (sub-processor definition applies regardless of PAN scope) | D-06.3 subprocessor obligations; DPA template update required |
| ORG-INT-02 | CRA Annex I Part I (2)(f) requires "secure update mechanism" — does Snyk's weekly dependency review + GitHub PR-only workflow satisfy this, or is an automatic OTA mechanism required? | CRA Annex I Part I (2)(f) | **Manual PR workflow satisfies** for a B2B SaaS without consumer-side auto-update; the proportionality principle per Track B applies (8 FTE, no OTA infrastructure). | ENISA state-of-the-art guidance for class-I SaaS proportionality | D-02.2 Patch Management; if D-02.2 §4 target ever moves to MUST+MEDIUM, OTA becomes relevant |
| ORG-INT-03 | The voluntary DPO hat on the CEO (0.2 FTE) — does the EDPB Guidelines 3/2019 §4.1 conflict-of-interest criterion apply, given that the CEO is also the data controller's legal representative? | GDPR Art. 37-39; EDPB Guidelines 3/2019 | **No conflict** at MICRO scale: DPO advises; CEO + Board approve and remain accountable under Art. 5(2). Conflict-of-interest criterion is invoked only for organisations with dedicated DPO and CISO functions. | EDPB Guidelines 3/2019 §4.1 (criteria for conflict); CNIL 2018 guidance on MICRO DPO dual-hat | D-09.1 Information Security Policies; governance posture |
| ORG-INT-04 | The 72-hour breach notification clock — does it start at CEO/DPO awareness (informal intake) or at formal incident classification (IR-03 trigger)? | GDPR Art. 33(1); NIS 2 Art. 23(4) | **Awareness at internal documentation** (i.e., the first written record in the incident ticket) — not informal CEO/DPO chat. Aligns with EDPB Guidelines 9/2022 §3.1. | EDPB Guidelines 9/2022 §3.1 | D-04.3 Regulatory Notification; affects `BPR-D-04.3-002` (max-SLA routing pipeline in Doc19) |
| ORG-INT-05 | For CRA Art. 13 vulnerability handling — does the marketing copy "Built for teams" on the public website constitute a "placement on the EU market" that activates Art. 13 obligations, or only the SaaS subscription flow? | CRA Art. 13(1); Recital 11 | **Subscription flow** is the placement on the market; the marketing copy is pre-contractual information and does not by itself activate Art. 13(1). | CRA Recital 11 (definition of "making available on the market") | D-06.3 Contractual Security Obligations; CRA Annex VII technical documentation scope |

**Total: 5 cards.** (Cap at 10 per AEGIS P2 proportionality for MICRO. Larger organisations may exceed.)

---

## 11. BUSINESS GOALS

Strategic objectives that the regulatory compliance programme must
support. Each goal is traceable to at least one applicable regulation
and has a measurable success criterion.

| ID | Description | Priority | Related Regulations | Success Metric |
|----|-------------|----------|---------------------|----------------|
| BG-01 | Maintain EU regulatory compliance | HIGH | GDPR, CRA | Zero high-severity audit findings |
| BG-02 | Achieve CRA conformity assessment readiness | HIGH | CRA | Completed technical documentation (Annex I) |
| BG-03 | Grow EU B2B customer base by 25% YoY | MEDIUM | GDPR (B2B data) | New B2B contracts signed |
| BG-04 | Reduce mean-time-to-detect for incidents | MEDIUM | GDPR (breach), CRA (vulns) | MTTD < 24h |
| BG-05 | Establish formal security policies | LOW | All applicable | Documented policies in place |

**ID Pattern:** `BG-{NN}` where `{NN}` is a 2-digit sequential number.

---

## N. COMPANY CONTEXT CLASS INSTANTIATION

```
CompanyContext {
    companyContextId: "CC-TINYTASK-2026-001"
    assessmentDate: "2026-04-01"
    version: "2.0"

    sector: "Technology/Software"
    size: "Micro (8 employees, <€2M revenue)"
    processes_personal_data: TRUE
    places_digital_products_eu: TRUE
    dora_financial_entity: FALSE
    nis2_sector: "Technology (not classified)"
    aiact_high_risk_system: FALSE
    technologicalControlPlane: "Cloud (AWS/Firebase)"

    complexityTier: "MEDIUM"
    activeExtensions: ["B6", "B7", "B8"]

    // Block B6 attributes (supplyChainVisibility = Low)
    sbomPractices: "Not started"
    supplierSecurityAssessment: "None"
    componentVulnManagement: "Manual review"

    // Block B7 attributes (CRA applicable)
    craProductClass: "Default"
    craConformityRegime: "Self-assessment"
    craExclusionCheck: "Confirmed not excluded"
    craCertificationScheme: "No scheme available"

    // Block B8 attributes (dataRole = Mixed)
    dataElementRoles: "Controller (account data) / Processor (client content)"
    crossRegulationRoles: "CRA=manufacturer; GDPR=controller/processor"
    processorNativeCompliance: FALSE

    // Implementation readiness
    readinessScore: "5/12 — LOW"
}
```

---

## N+1. VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 2.1 | 2026-07-14 | Compliance Lead | Added §10 Stakeholders register + §11 Business Goals catalog (Sprint D-final) |
| 2.0 | 2026-04-23 | Compliance Lead | Converted to layered intake format |
| 1.0 | 2026-04-01 | Compliance Lead | Initial release - TinyTask SaaS case |

---

## N+2. DOCUMENT APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Document Author | Compliance Lead | | 2026-04-01 |
| Technical Review (CTO) | | | |
| Business Review (CEO) | | | |
| AEGIS Methodology Review | | | |

---

**Next Document:** 04_Company_Context_Assessment.md
**Dependency:** None (foundational input for Phase 1)

## N. ARCHITECTURE INVENTORY

### N.1 Systems

| ID | Name | Type | Tech Stack | Owner | Criticality | Hosts Personal Data |
|----|------|------|-----------|-------|-------------|---------------------|
| SYS-01 | Main SaaS Application | Cloud SaaS application | Node.js API, React web client, PostgreSQL driver | CTO and development team | Important | Y |
| SYS-02 | Auth Service | Managed identity service | Auth0 using OAuth 2.0 and OIDC | CTO | Important | Y |
| SYS-03 | Customer Data Store | Managed relational database | PostgreSQL on EU cloud region | CTO and lead developer | Critical | Y |
| SYS-04 | Cloud KMS | Managed key management | Cloud KMS with provider-managed key storage | CTO | Supporting | N |
| SYS-05 | Backup Store | Managed object storage | S3-compatible encrypted bucket | CTO | Important | Y |

### N.2 Cloud Services

| Provider | Service | Data Stored | Region | DPA in Place |
|----------|---------|-------------|--------|--------------|
| AWS or equivalent EU cloud provider | PostgreSQL managed database | Customer accounts, project metadata, B2B project content | eu-west-1 or equivalent EU region | Y |
| AWS or equivalent EU cloud provider | S3-compatible object storage | Encrypted database backups | eu-west-1 or equivalent EU region | Y |
| AWS or equivalent EU cloud provider | Cloud KMS | Encryption keys and key metadata | EU region | Y |
| Auth0 | Authentication and identity | Email identifiers, authentication metadata, session metadata | EU tenant where available | Y |
| Stripe | Payment processing | Card/payment data, billing contact metadata | Stripe controlled processing locations | Y |
| Datadog or equivalent | Logs and analytics | Pseudonymised event logs and operational metrics | EU site where available | Y |

### N.3 Authentication & Identity Systems

| System | Purpose | MFA | SSO | Password Policy |
|--------|---------|-----|-----|-----------------|
| SYS-02 Auth0 | Customer and administrator authentication | Admins only; optional for customers | OIDC for SYS-01 | Auth0 default password policy with minimum length and breached-password checks |
| Cloud provider IAM | Infrastructure administration | Y for CTO and developers | No enterprise SSO | Individual accounts with least-privilege roles; quarterly review not yet formalised |
| GitHub organisation | Source-code repository and pull requests | Y for developers | No enterprise SSO | GitHub enforced 2FA; branch protection limited to main branch |

### N.4 Data Stores

| ID | Type | Location | System | Encryption at Rest | Owner | Retention Period | Backup |
|----|------|----------|--------|-------------------|-------|------------------|--------|
| STORE-01 | PostgreSQL database | EU cloud region | SYS-03 | Y, AES-256 provider-managed encryption using SYS-04 keys | CTO and lead developer | Active account lifetime plus 30 days after deletion request where legally permissible | Y |
| STORE-02 | Object storage backups | EU cloud region | SYS-05 | Y, SSE-KMS/AES-256 using SYS-04 keys | CTO | Daily backups for 30 days; monthly backups for 12 months | Y |
| STORE-03 | Logs and analytics | EU monitoring region where available | SYS-01 and monitoring provider | Y, provider-managed encryption; no raw task content intentionally logged | CTO | 30 days | N |

### N.5 Data Flows

| ID | Source | Destination | Data Type | Volume | Encryption in Transit | Protocol | Subprocessor |
|----|--------|-------------|-----------|---------|----------------------|----------|--------------|
| FLOW-01 | Web client | SYS-01 Main SaaS Application | Account data and project data | Low to medium | Y, TLS 1.3 | HTTPS REST | N |
| FLOW-02 | SYS-01 Main SaaS Application | STORE-01 Main PostgreSQL | Customer accounts, project data, audit metadata | Low to medium | Y, encrypted internal database transport | PostgreSQL TLS | N |
| FLOW-03 | SYS-01 Main SaaS Application | STORE-03 Logs and analytics | Pseudonymised events, request metadata, error traces | Low | Y, TLS 1.2 or higher | HTTPS agent/API | Y, Datadog or equivalent |
| FLOW-04 | Web client | SYS-02 Auth Service | Authentication credentials, email identifier, OIDC tokens | Low | Y, TLS 1.3 | OAuth 2.0/OIDC over HTTPS | Y, Auth0 |
| FLOW-05 | SYS-01 Main SaaS Application | Stripe | Billing metadata and hosted-checkout redirect; no card PAN stored by TinyTask | Low | Y, TLS 1.2 or higher | HTTPS API | Y, Stripe |

### N.6 Data Subject Categories

| Subject Type | Data Categories | Access Mechanism | Erasure Mechanism |
|--------------|-----------------|-------------------|-------------------|
| EU customers (B2B and B2C) | Email, name, account metadata, project data, billing metadata | In-app account view and support request | Manual support workflow; active records deleted and backup expiry relied on for residual copies |
| Free-tier users | Email, name where provided, project data, usage events | In-app account view and support request | Manual support workflow; inactive accounts reviewed ad hoc |
| Enterprise customer end users | Email, name, project data controlled by enterprise customer | Enterprise administrator export and support-assisted DSAR | Processor-assisted deletion on controller instruction under DPA |
