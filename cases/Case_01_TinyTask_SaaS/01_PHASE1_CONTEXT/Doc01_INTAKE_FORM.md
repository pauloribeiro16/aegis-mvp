---
document_id: AEGIS-COMMON-01
title: AEGIS Intake Form — Company Context
version: 2.1
created: 2026-04-01
updated: 2026-08-06
author: Compliance Lead
status: RECONCILED
inputs: [baseline/00_Taxonomy_Reference.md]
outputs: [Doc02_Adjusted_Goals.md]
traceability: AEGIS Class Model → CompanyContext class
related_documents: [baseline/00_Taxonomy_Reference.md]
---

# AEGIS Intake Form — Company Context Assessment

## CHANGELOG

| Version | Date | Changes |
|---------|------|---------|
| 3.3 | 2026-09-22 | Streamlining: eliminated redundant ASCII decision trees, Phase 2 maturity previews (Score 5/12), operational RACI, influence matrices, and class code duplication. Document reduced to canonical Phase 1 inputs. |
| 3.2 | 2026-09-22 | Phase 1 boundary enforcement: purged technical architecture inventory (former §N, 68 lines of tech stack/vendor details deferred to Phase 2/3) and neutralized brand names to functional operational roles per AGENTS.md R5. |
| 3.1 | 2026-09-22 | Document hygiene: removed editorial notes/blockquotes in §7 and §10.5 per AGENTS.md R11. |
| 3.0 | 2026-08-06 | Rich Mode reconciliation — file renamed from `01_Company_Context.md`; `02_Regulatory_Mapping_Master.md` citations superseded by `00_Taxonomy_Reference.md` + corpus |
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

### 3.1 Applicability Assessment Table

| Regulation | Decision Points & Triggers | Result | Role(s) | Summary Rationale |
|------------|----------------------------|--------|---------|-------------------|
| **GDPR** | Commercial B2B SaaS processing EU personal data (names, emails, passwords, task notes) | **APPLICABLE** | CONTROLLER + PROCESSOR | Controller for customer accounts; Processor for clinic task data |
| **CRA** | Develops and places digital products on EU market (SaaS + web/mobile interface) | **APPLICABLE** | MANUFACTURER | Default product class; self-assessment regime |
| **NIS 2** | Tech sector, non-critical service; 8 employees (<50) and <€2M (<€10M) | **NOT APPLICABLE** | — | Below size and turnover thresholds; not in Annex I/II essential sectors |
| **DORA** | B2B productivity SaaS; external payment provider handles payments | **NOT APPLICABLE** | — | Not a financial entity (Art. 2) and not an ICT provider to financial entities |
| **AI Act** | Rule-based task management platform | **NOT APPLICABLE** | — | Zero AI/ML systems developed, deployed, or integrated |

---

## 4. LAYER 2 — CONDITIONAL CONTEXT

**Purpose:** Capture specific operational parameters triggered by applicable regulations.

### 4.1 Supply Chain Parameters (CRA / GDPR)
- **Component Tracking:** Third-party software dependencies are not yet tracked in a formal Software Bill of Materials (SBOM).
- **Supplier Evaluation:** Supplier security evaluations are conducted ad-hoc with reliance on standard supplier contracts/DPAs.
- **Vulnerability Remediation:** Manual review triggered during routine updates or security advisories.

### 4.2 CRA Classification Parameters
- **Product Class:** Default (no critical or high-risk functions per CRA Art. 7).
- **Conformity Assessment:** Internal production control (self-assessment).
- **Exclusion Check:** Confirmed in scope (connected software not falling under Art. 24 exclusions).
- **EU Cybersecurity Scheme:** None currently published for this product category.

### 4.3 Multi-Actor Roles (GDPR)
- **Account Metadata:** TinyTask acts as Data Controller (purposes and means defined internally).
- **Customer Project Data:** TinyTask acts as Data Processor on behalf of clinics under standard Data Processing Agreements (DPA).

---

## 5. LAYER 3 — REGULATORY INTERACTIONS

**Purpose:** Identify timing, procedural, and negative constraints arising from simultaneous applicability.

### 5.1 Temporal Conflict Scan (CRA Art. 14 vs GDPR Art. 33)
- **Identified Conflict:** CRA Art. 14 requires early reporting of actively exploited vulnerabilities within 24 hours. GDPR Art. 33 requires breach notification to authorities within 72 hours.
- **Resolution Strategy:** Unified incident response with max-SLA routing (internal clock anchored at 24h to satisfy both frameworks simultaneously).

### 5.2 Negative Scope Confirmation
- **AI Act Art. 5 / 25:** Confirmed non-applicable (no biometric, scoring, or downstream AI components).
- **GDPR Art. 37:** Mandatory DPO appointment not triggered (small-scale processing, core activity does not require regular and systematic large-scale monitoring).
- **NIS 2 Art. 3:** Below size threshold (8 employees).

---

## 6. ORGANISATION INTERPRETATION DOUBTS

Specific operational doubts raised regarding regulatory interpretation at MICRO scale:

| ID | Doubt | Source Provision | Organisation Interpretation | Downstream Impact |
|----|-------|------------------|-----------------------------|-------------------|
| ORG-INT-01 | Payment gateway sub-processor status | GDPR Art. 28(4) | Payment provider is sub-processor for payment metadata only | D-06.3 subprocessor obligations; DPA template alignment |
| ORG-INT-02 | Secure update mechanism requirement | CRA Annex I (2)(f) | Managed pull-request workflow satisfies proportional requirements for B2B SaaS | D-02.2 Patch Management baseline |
| ORG-INT-03 | Dual role for executive advisory | GDPR Art. 37-39 | Proportional dual-hat advisory role accepted at MICRO scale (<10 staff) | D-09.1 Security Governance policies |
| ORG-INT-04 | Incident notification clock start | GDPR Art. 33(1) | Clock starts upon confirmed internal incident documentation/ticket | D-04.3 Regulatory Notification workflows |
| ORG-INT-05 | Market placement scope | CRA Art. 13(1) | Placement on market corresponds to commercial SaaS subscription activation | D-06.3 Contractual documentation scope |

---

## 7. BUSINESS GOALS (Contextual Anchors)

| ID | Description | Priority | Related Regulations | Target Metric |
|----|-------------|----------|---------------------|---------------|
| BG-01 | Maintain EU regulatory compliance | HIGH | GDPR, CRA | Zero major non-conformities |
| BG-02 | Achieve CRA conformity readiness | HIGH | CRA | Technical documentation completed |
| BG-03 | Expand EU customer base | MEDIUM | GDPR | Standard DPA compliance pack |
| BG-04 | Reduce incident detection and response time | MEDIUM | GDPR, CRA | Mean-time-to-detect < 24h |
| BG-05 | Establish formalized security and privacy policies | LOW | GDPR, CRA | Documented policy set in place |

---

## 8. DOCUMENT APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Document Author | Compliance Lead | | 2026-04-01 |
| Technical Review (CTO) | | | |
| Business Review (CEO) | | | |
| AEGIS Methodology Review | | | |
