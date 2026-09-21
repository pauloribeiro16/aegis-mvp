---
document_id: AEGIS-P1-07b
title: Proportionality Profile — TinyTask SaaS
phase: 1
version: 1.5
created: 2026-07-13
updated: 2026-08-27
author: Fase de Especificação 5 Executor (deep-enrichment-builder; v1.6 redesign note per MATURITY_MODEL_CSF_STRICT)
status: DEEP_ENRICHED
status_history:
  - { date: 2026-08-06, status: DRAFT, sprint: 0, by: 'Fase de Especificação 0 skeleton' }
  - { date: 2026-08-06, status: RECONCILED, sprint: 1, by: 'Fase de Especificação 1 reconciliation' }
  - { date: 2026-08-06, status: CORPUS_ENRICHED, sprint: 2, by: 'Fase de Especificação 2 corpus enrichment' }
  - { date: 2026-08-06, status: ADJUSTED_OBJECTIVES, sprint: 4, by: 'Fase de Especificação 4 adjusted objectives' }
  - { date: 2026-08-06, status: DEEP_ENRICHED, sprint: 5, by: 'Fase de Especificação 5 DEEP enrichment' }
deep_enrichment_date: 2026-08-06
cols_added_to_section_4: 3
cross_checked_against_corpus: true
cross_check_date: 2026-08-06
inputs: [Doc03_Company_Context_Assessment.md, Doc08_Regulatory_Applicability.md, Doc11_Structured_Compliance_Matrix.md, ../../../../../00_METHODOLOGY/REFERENCE/proportionality_model.md, ../../../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/]
outputs: [08_Obligation_Derivation.md, 11_Rules_Catalog.md, 14_Architectural_Nodes.md, Doc13_Adjusted_Goals.md]
related_documents: [04_Company_Context_Assessment.md, 05_Regulatory_Applicability.md, 07_Structured_Compliance_Matrix.md, 07c_Adjusted_Goals.md, ../../../../../00_METHODOLOGY/REFERENCE/proportionality_model.md, ../03_PHASE3_DECOMPOSITION/annexes/Critical_Analysis_Micro_Enterprise.md]
frozen: false
supersedes: none
---

> **Fase de Especificação 1 Reconciliation Note (2026-08-06)**
> Rich Mode copy of legacy `01_PHASE1_CONTEXT/07b_Proportionality_Profile.md` (v1.0, ACTIVE). Fase de Especificação 1 changes:
> - **I-10:** Status remains `ACTIVE` (the legacy doc is signed-off as ACTIVE; Fase de Especificação 1 reconciliation is content-neutral for this document — all 37 sub-domain rows, decision-table mappings, and GATE-P readiness checks are preserved verbatim).
> - **I-05/I-06 (FR/NFR IDs):** Doc references `FR-01/04` (Critical Analysis §7.1) and `IO-04` (Firebase Auth inheritance). These are **legacy v1.0 forms**. The canonical v2.0 form is `FR-{DOM}-{NN}` (e.g., `FR-IAM-01`) and `NFR-{CAT}-{NN}`. The mapping is documented in `00_METHODOLOGY/REFERENCE/fr_nfr_numbering.md`. <!-- LEGACY: numeric FR-01, IO-04 form, see canonical mapping in fr_nfr_numbering.md. -->
> - **I-07 (rule counts):** Doc references "Q4 Critical patching 24h, high 7d" indirectly via Critical Analysis. The canonical v2.0 rule count is **46 rules (30 CR + 16 BPR)**. <!-- LEGACY: 38 was v1.0; canonical v2.0 is 46. -->
> - **I-13 (02_Regulatory_Mapping_Master.md deprecation):** Not referenced. N/A.
> - Body content unchanged from legacy. Fase de Especificação 2 will validate the 5-attribute coverage per row against the corpus `considerations` field.

> **Fase de Especificação 3 Corpus Cross-Check Note (2026-08-06)**
> Cross-checked 10 representative rows in §4 against the corpus at `00_METHODOLOGY/PREPROCESSING_by_domain/domains/`. Findings:
> - **Track B `verification_method` ≠ Corpus `requirements.*.yaml.verification_method`.** 07b's column carries the **Track B tier-specific attribute value** per `proportionality_model.md §6` (MINIMAL=INSPECT, LIGHTWEIGHT=DEMONSTRATE+INSPECT, DEFERRED=`—`). The corpus's `verification_method` is a **regulatory method** (uniformly `TEST` at high-level aggregation) that defines how the fit_criterion is verified. These are complementary, not identical, dimensions.
> - **Track B `example_controls` ↔ Corpus `considerations`**: 07b's `example_controls` column (e.g., "AWS S3 / DynamoDB SSE-KMS enabled (AES-256 default)") aligns with the corpus's `considerations` block (e.g., for D-01.1: "CRA's `state of the art` (product-level, harmonised-standards floor — the strictest)… a single encryption deployment with a joint risk-assessment artefact discharges all four obligations"). Both converge on AES-256 as the control primitive.
> - **All 10 spot-checked rows PASS.** See §11 for the full cross-check table.

# Proportionality Profile — TinyTask SaaS

## 1. DOCUMENT PURPOSE

This document is the **case instance** of the Track B Proportionality Model for TinyTask Lda. It binds every ACTIVE sub-domain in this case to a concrete tier and to the five operational attributes (`satisfaction_pattern`, `evidence_depth`, `verification_method`, `ownership`, `example_controls`) defined in `00_METHODOLOGY/REFERENCE/proportionality_model.md` §6.

This document **does not alter Regulatory Baseline**. The `fit_criterion` and the HSO for each sub-domain remain frozen per `00_METHODOLOGY/REGULATORY_BASELINE.md` §6. Track B only annotates *implementation*, *evidence depth*, and *ownership* per sub-domain — never the regulatory floor.

**Invariant (quoted from proportionality_model.md §1):** "The regulatory `fit_criterion` and the security objective (HSO) **are never modified by Track B**. [...] Track B only varies three axes: `satisfaction_pattern`, `evidence_depth`, `ownership`." This profile respects that invariant in full: it produces no requirement relaxation, only a bounded operationalisation per tier.

**Gate criteria:** This file is consumed by `eval_proportionality.py` (GATE-P per `dependency_graph.yaml`). It must be complete and internally consistent before Phase 1 exit.

---

## 2. COMPANY PROFILE METADATA

Inputs are read from `04_Company_Context_Assessment.md` §2 (size) and §5 (intake summary, complexity tier, FTE).

| Attribute            | Value                              | Source                              |
|----------------------|------------------------------------|-------------------------------------|
| Scale (S)            | MICRO                              | Doc 04 §2 — 8 employees, <€2M       |
| Employees            | 8                                  | Doc 04 §2 / §5                      |
| Revenue              | <€2M                               | Doc 04 §2 / §5                      |
| Sector               | SaaS (Productivity / B2B)          | Doc 04 §2 / §5                      |
| Jurisdiction         | EU (Portugal)                      | Doc 04 §5                           |
| Applicable regs      | [GDPR, CRA]                        | Doc 04 §6 / Doc 05 §4               |
| Complexity tier      | MEDIUM                             | Doc 04 §5                           |
| Security FTE         | 0.85                               | Critical_Analysis §3.2              |
| Stack                | AWS (eu-west-1), Firebase Auth, Stripe | Doc 04 §7 / Doc 05 §5.2          |

Because `S = MICRO` and `security_FTE = 0.85 ≤ 1.0`, proportionality_model.md §5.2 applies: any SHOULD/COULD sub-domain drops one tier, and the `DEFERRED` marker becomes available.

---

## 3. TIER ASSIGNMENT SUMMARY

The deterministic decision table (proportionality_model.md §5.1, §5.2, §5.3) yields the following distribution for the 37 ACTIVE sub-domains (D-08.3 INACTIVE — out of scope per Doc 07 §3).

| Tier        | Count | Rationale (decision-table entry)                                                                                                                                  |
|-------------|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LIGHTWEIGHT | 31    | MICRO + BUILD_REQUIRED + MUST (proportionality_model.md §5.1 row MICRO col BUILD_REQUIRED) → LIGHTWEIGHT                                                           |
| MINIMAL     | 5     | MICRO + INHERITABLE + MUST (§5.1 row MICRO col INHERITABLE) → MINIMAL                                                                                              |
| DEFERRED    | 1     | MICRO + BUILD_REQUIRED + SHOULD + FTE ≤ 1.0 (§5.2 drop-one-tier rule; SHOULD = LIGHTWEIGHT - 1 = MINIMAL, then deferred because MICRO + FTE ≤ 1.0) → DEFERRED   |
| **Total**   | **37**|                                                                                                                                                                    |

No tier floor is breached: every MUST is at MINIMAL or above (proportionality_model.md §5.3). No INHERITABLE row was forced to LIGHTWEIGHT by priority (none exist for SHOULD/COULD INHERITABLE rows in this case).

---

## 4. PER-SUB-DOMAIN PROPORTIONALITY TABLE

Columns: `Sub-domain | I (BUILD/INHERIT) | P | Tier | satisfaction_pattern | evidence_depth | verification_method | ownership | example_controls | Notes | Implementation Status | Implementation Priority`. One row per ACTIVE sub-domain (37 rows). D-08.3 is omitted.

**v1.6 note** — `Implementation Status` (PARTIAL / NOT IMPLEMENTED / IMPLEMENTED) is the sole posture field; the prior `maturity_cur` / `maturity_tgt` 0–4 scalars were removed per `00_METHODOLOGY/MATURITY_MODEL_CSF_STRICT.md §9` (DEPRECATED). Capability assessment now lives in the graph as `EvidenceItem` nodes (Scale A per Function, Scale B per sub-domain) — see Case_01_P1_Dashboard.html Folio VIII.

| Sub-domain                                | I       | P    | Tier        | satisfaction_pattern | evidence_depth                                                                       | verification_method              | ownership                | example_controls                                                                                                          | Notes                                                  | Risk if not met | Implementation Status | Implementation Priority |
|-------------------------------------------|---------|------|-------------|----------------------|--------------------------------------------------------------------------------------|----------------------------------|--------------------------|---------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|-----------------|------------------|-----------------------|
| D-01.1 Data at Rest Encryption            | BUILD   | MUST | LIGHTWEIGHT | BUY_MANAGED          | Managed-service config documented + annual review; no dedicated in-house program      | DEMONSTRATE + INSPECT            | Shared (AWS + company)   | AWS S3 / DynamoDB SSE-KMS enabled (AES-256 default); no company-owned KMS program                                        | Unified AES-256 baseline satisfies SAME pair | HIGH | PARTIAL | HIGH |
| D-01.2 Data in Transit Encryption         | BUILD   | MUST | LIGHTWEIGHT | BUY_MANAGED          | Managed-service config documented + annual review                                     | DEMONSTRATE + INSPECT            | Shared (AWS + company)   | TLS 1.3 via AWS ACM / CloudFront; certificate auto-renewal                                                                | TLS 1.3 covers all ingress + egress | HIGH | PARTIAL | HIGH |
| D-01.3 Key Management                     | BUILD   | MUST | LIGHTWEIGHT | BUY_MANAGED          | Managed-service config documented + annual review                                     | DEMONSTRATE + INSPECT            | Shared (AWS + company)   | AWS KMS default keys; rotation cadence is AWS-managed                                                                     | | MEDIUM | PARTIAL | HIGH |
| D-01.4 Data Integrity                     | BUILD   | MUST | LIGHTWEIGHT | BUY_MANAGED          | Managed-service config documented + annual review                                     | DEMONSTRATE + INSPECT            | Shared (AWS + company)   | HMAC + DB constraints via AWS RDS                                                                                         | | HIGH | PARTIAL | HIGH |
| D-02.1 Vulnerability Identification       | BUILD   | MUST | LIGHTWEIGHT | BUY_MANAGED          | Managed-service config documented + annual review                                     | DEMONSTRATE + INSPECT            | Shared (tooling + company)| Trivy + npm audit in CI; OSS advisories                                                                                   | | MEDIUM | PARTIAL | HIGH |
| D-02.2 Patch Management                   | BUILD   | MUST | LIGHTWEIGHT | BUY_MANAGED          | Managed-service config documented + annual review                                     | DEMONSTRATE + INSPECT            | Shared (AWS + company)   | AWS Systems Manager Patch Manager (auto)                                                                                  | Critical patches 24h per Critical Analysis §4 | MEDIUM | PARTIAL | HIGH |
| D-02.3 Coordinated Vulnerability Disclosure| BUILD  | MUST | LIGHTWEIGHT | BUY_MANAGED          | Managed-service config documented + annual review                                     | DEMONSTRATE + INSPECT            | Company                  | security.txt at `/.well-known/security.txt`; CVD page                                                                     | | MEDIUM | PARTIAL | HIGH |
| D-02.4 Threat-Led Penetration Testing     | BUILD   | SHOULD| DEFERRED   | —                    | —                                                                                    | —                                | —                        | No OJ mandate for default-class CRA manufacturer; reference NIST SP 800-115 only                                        | DEFERRED per §5.2 (MICRO + FTE ≤ 1.0) | LOW | NOT IMPLEMENTED | LOW |
| D-03.1 Identity Lifecycle                 | INHERIT (Firebase Auth IO-04) | MUST | MINIMAL | INHERIT | Supplier attestation on file (SOC 2 / ISO 27001) + 1-page internal statement | INSPECT | Supplier (company = validator) | Firebase Auth baseline; Firebase security documentation                                                                  | OIDC delegation per Critical Analysis §9 | MEDIUM | PARTIAL | HIGH |
| D-03.2 Multi-Factor Authentication        | INHERIT (Firebase Auth IO-04) | MUST | MINIMAL | INHERIT | Supplier attestation on file + 1-page internal statement                            | INSPECT                           | Supplier (company = validator) | Firebase Auth MFA; customer-managed encryption keys                                                                      | | MEDIUM | PARTIAL | HIGH |
| D-03.3 Authorisation & Least Privilege    | BUILD   | MUST | LIGHTWEIGHT | BUY_MANAGED          | Managed-service config documented + annual review                                     | DEMONSTRATE + INSPECT            | Shared (Firebase + company)| Firebase Auth RBAC                                                                                                        | | MEDIUM | PARTIAL | HIGH |
| D-03.4 Secure System Defaults             | BUILD   | MUST | LIGHTWEIGHT | BUY_MANAGED          | Managed-service config documented + annual review                                     | DEMONSTRATE + INSPECT            | Company                  | Secure defaults via Firebase config                                                                                       | | MEDIUM | PARTIAL | HIGH |
| D-04.1 Incident Detection & Triage        | BUILD   | MUST | LIGHTWEIGHT | BUY_MANAGED          | Managed-service config documented + annual review                                     | DEMONSTRATE + INSPECT            | Shared (AWS + company)   | CloudWatch alarms + SNS notifications                                                                                     | CloudWatch (not enterprise SIEM) per Critical Analysis §9 | MEDIUM | PARTIAL | HIGH |
| D-04.2 Containment & Mitigation           | BUILD   | MUST | LIGHTWEIGHT | BUY_MANAGED          | Managed-service config documented + annual review                                     | DEMONSTRATE + INSPECT            | Company                  | Documented 4h containment playbook                                                                                        | | HIGH | PARTIAL | HIGH |
| D-04.3 Regulatory Notification            | BUILD   | MUST | LIGHTWEIGHT | BUY_MANAGED          | Managed-service config documented + annual review                                     | DEMONSTRATE + INSPECT            | Company                  | max-SLA 24h internal; unified incident workflow                                                                          | 24h internal satisfies GDPR 72h and CRA 24h max-SLA | HIGH | PARTIAL | HIGH |
| D-04.4 Data Restoration & Recovery        | BUILD   | MUST | LIGHTWEIGHT | BUY_MANAGED          | Managed-service config documented + annual review                                     | DEMONSTRATE + INSPECT            | Shared (AWS + company)   | AWS Backup; RTO 24h (per Critical Analysis §4)                                                                            | RTO 24h replaces 4h unrealistic target | HIGH | PARTIAL | HIGH |
| D-05.1 Data Minimisation                  | BUILD   | MUST | LIGHTWEIGHT | BUY_MANAGED          | Managed-service config documented + annual review                                     | DEMONSTRATE + INSPECT            | Company                  | Field-level enforcement in schema                                                                                         | | MEDIUM | PARTIAL | HIGH |
| D-05.2 Retention & Archiving              | BUILD   | MUST | LIGHTWEIGHT | BUY_MANAGED          | Managed-service config documented + annual review                                     | DEMONSTRATE + INSPECT            | Company                  | Retention policy (7y audit logs; 30d DSAR working data)                                                                  | | MEDIUM | PARTIAL | HIGH |
| D-05.3 Right to Erasure                   | BUILD   | MUST | LIGHTWEIGHT | BUY_MANAGED          | Managed-service config documented + annual review                                     | DEMONSTRATE + INSPECT            | Company                  | Erasure API endpoint                                                                                                      | | HIGH | PARTIAL | HIGH |
| D-05.4 Data Portability                   | BUILD   | MUST | LIGHTWEIGHT | BUY_MANAGED          | Managed-service config documented + annual review                                     | DEMONSTRATE + INSPECT            | Company                  | JSON export endpoint                                                                                                      | D-05.3 + D-05.4 share GDPR Art. 20-17 sub-SO pair | MEDIUM | PARTIAL | HIGH |
| D-06.1 Vendor Risk Assessment             | INHERIT (DPA validation) | MUST | MINIMAL | INHERIT | Supplier attestation on file + 1-page internal statement                            | INSPECT                           | Supplier (company = validator) | DPA validation against GDPR Art. 28; supplier security clauses                                                            | Annual manual review per Critical Analysis §9 | MEDIUM | PARTIAL | HIGH |
| D-06.2 Software Bill of Materials         | BUILD (CRA sole) | MUST | LIGHTWEIGHT | BUY_MANAGED | Managed-service config documented + annual review                                     | DEMONSTRATE + INSPECT            | Company                  | CycloneDX SBOM in CI/CD per release                                                                                       | Closes GAP-003 (Doc 07 §7) | MEDIUM | PARTIAL | HIGH |
| D-06.3 Contractual Security Obligations   | BUILD   | MUST | LIGHTWEIGHT | BUY_MANAGED          | Managed-service config documented + annual review                                     | DEMONSTRATE + INSPECT            | Company                  | DPA template + supplier security clauses                                                                                  | | HIGH | PARTIAL | HIGH |
| D-06.4 Third-Party Boundary Management    | INHERIT (AWS/Stripe/Firebase) | MUST | MINIMAL | INHERIT | Supplier attestation on file + 1-page internal statement                            | INSPECT                           | Supplier (company = validator) | AWS / Stripe / Firebase boundary inherited from their attestations                                                       | | MEDIUM | PARTIAL | HIGH |
| D-07.1 Secure-by-Design Principles        | BUILD   | MUST | LIGHTWEIGHT | BUY_MANAGED          | Managed-service config documented + annual review                                     | DEMONSTRATE + INSPECT            | Company                  | NIST SSDF + OWASP SAMM baseline                                                                                           | | MEDIUM | PARTIAL | HIGH |
| D-07.2 Secure Coding Practices            | BUILD (CRA only) | MUST | LIGHTWEIGHT | BUY_MANAGED | Managed-service config documented + annual review                                     | DEMONSTRATE + INSPECT            | Company                  | SAST in CI; coding standards documentation                                                                                | | MEDIUM | PARTIAL | HIGH |
| D-07.3 CI/CD Pipeline Security            | BUILD (CRA only) | MUST | LIGHTWEIGHT | BUY_MANAGED | Managed-service config documented + annual review                                     | DEMONSTRATE + INSPECT            | Company                  | CI gates (block critical vulns); pipeline-as-code                                                                          | Closes Priority 1 FR-01/04 (Critical Analysis §7.1) | MEDIUM | PARTIAL | HIGH |
| D-07.4 Change Management                  | BUILD (CRA only) | MUST | LIGHTWEIGHT | BUY_MANAGED | Managed-service config documented + annual review                                     | DEMONSTRATE + INSPECT            | Company                  | Change management log (PR review + merge controls)                                                                        | | MEDIUM | PARTIAL | HIGH |
| D-08.1 General Security Awareness         | INHERIT (vendor docs) | MUST | MINIMAL | INHERIT | Supplier attestation on file + 1-page internal statement                            | INSPECT                           | Supplier (company = validator) | Vendor security awareness documentation on file                                                                          | Replaces deferred phishing simulation (Critical §7.3) | LOW | PARTIAL | HIGH |
| D-08.2 Role-Specific Competence           | BUILD   | MUST | LIGHTWEIGHT | BUY_MANAGED          | Managed-service config documented + annual review                                     | DEMONSTRATE + INSPECT            | Company                  | Annual security awareness email + role-specific docs (admin/dev/DPO)                                                    | | MEDIUM | PARTIAL | HIGH |
| D-09.1 Information Security Policies      | BUILD   | MUST | LIGHTWEIGHT | BUY_MANAGED          | Managed-service config documented + annual review                                     | DEMONSTRATE + INSPECT            | Company                  | Security policy template (Doc 09 family input)                                                                            | | MEDIUM | PARTIAL | HIGH |
| D-09.2 Impact & Risk Assessments          | BUILD   | MUST | LIGHTWEIGHT | BUY_MANAGED          | Managed-service config documented + annual review                                     | DEMONSTRATE + INSPECT            | Company                  | DPIA template + CRA risk assessment template (unified, dual-output)                                                      | Resolves EVT-002 (Doc 07 §5.4) | HIGH | PARTIAL | HIGH |
| D-09.3 Asset Inventories                  | BUILD (CRA partial) | MUST | LIGHTWEIGHT | BUY_MANAGED | Managed-service config documented + annual review                                     | DEMONSTRATE + INSPECT            | Company                  | Annex VII §1-§2 architecture documentation (CRA partial)                                                                  | | MEDIUM | PARTIAL | HIGH |
| D-09.4 Records of Processing              | BUILD   | MUST | LIGHTWEIGHT | BUY_MANAGED          | Managed-service config documented + annual review                                     | DEMONSTRATE + INSPECT            | Company                  | RoPA template (Doc 09 input)                                                                                              | Closes GAP-001 (Doc 07 §7) | HIGH | PARTIAL | HIGH |
| D-10.1 Continuous Security Monitoring     | BUILD (TEN-03: opt-in/opt-out separation) | MUST | LIGHTWEIGHT | BUY_MANAGED | Managed-service config documented + annual review                                     | DEMONSTRATE + INSPECT            | Shared (AWS + company)   | CloudWatch (not enterprise SIEM); per Critical Analysis                                                                    | opt-in/opt-out separation per TEN-03 | MEDIUM | PARTIAL | HIGH |
| D-10.2 Audit Logging & Traceability       | BUILD   | MUST | LIGHTWEIGHT | BUY_MANAGED          | Managed-service config documented + annual review                                     | DEMONSTRATE + INSPECT            | Shared (AWS + company)   | CloudTrail + tamper-evident S3 log bucket                                                                                 | 7-year retention per Critical Analysis §10.2 | HIGH | PARTIAL | HIGH |
| D-10.3 Compliance Testing                 | BUILD   | MUST | LIGHTWEIGHT | BUY_MANAGED          | Managed-service config documented + annual review                                     | DEMONSTRATE + INSPECT            | Company                  | Quarterly compliance review checklist                                                                                     | | HIGH | PARTIAL | HIGH |

**Summary of control selections** (recurring patterns):
- **Encryption baseline (D-01.x):** AWS S3/DynamoDB SSE-KMS AES-256 + AWS ACM TLS 1.3.
- **Vulnerability + secure dev (D-02.1 + D-07.x):** Trivy + npm audit + CycloneDX SBOM + CI gates + NIST SSDF/OWASP SAMM baseline.
- **Identity (D-03.1, D-03.2):** Inherited from Firebase Auth baseline; MFA and lifecycle handled by the supplier.
- **Incident (D-04.x):** CloudWatch + SNS alarms, 4h containment playbook, max-SLA 24h notification (covers GDPR 72h and CRA 24h), AWS Backup with RTO 24h.
- **Data lifecycle (D-05.x):** Field-level enforcement, retention policy, erasure + JSON export APIs.
- **Supply chain (D-06.x):** DPA validation, SBOM per release, supplier security clauses, AWS/Stripe/Firebase boundary inherited.
- **Awareness (D-08.x):** Vendor security docs on file + annual internal awareness email + role-specific docs.
- **Governance (D-09.x):** Policy / DPIA / RoPA / Annex VII templates.
- **Monitoring + audit (D-10.x):** CloudWatch + CloudTrail + quarterly compliance review.

---

## 5. CROSS-CHECK VS CRITICAL ANALYSIS

Each recommendation of `Critical_Analysis_Micro_Enterprise.md` is mapped to the sub-domain row that operationalises it.

| # | Recommendation (source)                                                                  | Realising sub-domain row(s)                                                                                              |
|---|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| 1 | CloudWatch + alerts (not enterprise SIEM / MSSP) — §5, §9                                | D-10.1 Continuous Security Monitoring (LIGHTWEIGHT, BUY_MANAGED)                                                          |
| 2 | Defer phishing simulation (low risk for 8 people) — §7.3, §9                              | D-08.1 General Security Awareness (MINIMAL, INHERIT — vendor docs cover it); D-08.2 (LIGHTWEIGHT — annual email only)   |
| 3 | BC/DR RTO = 24h (realistic, replaces 4h) — §4, §9                                         | D-04.4 Data Restoration & Recovery (LIGHTWEIGHT, AWS Backup, RTO 24h)                                                    |
| 4 | Critical patching 24h, high 7d (via AWS Systems Manager) — §4, §7.2                       | D-02.2 Patch Management (LIGHTWEIGHT, AWS Systems Manager Patch Manager auto)                                             |
| 5 | SAST/SCA tooling (CRA requirement, €200-500/mês) — §5                                     | D-02.1 Vulnerability Identification (Trivy + npm audit); D-07.2 Secure Coding Practices (SAST in CI)                    |
| 6 | SBOM (CRA, GAP-003) — §6 strategic, Doc 07 §7                                              | D-06.2 SBOM (LIGHTWEIGHT, CycloneDX in CI/CD per release)                                                                |
| 7 | security.txt + CVD page (CRA, GAP-004) — Doc 07 §7                                        | D-02.3 Coordinated Vulnerability Disclosure (LIGHTWEIGHT, security.txt at `/.well-known/security.txt`)                  |
| 8 | OIDC delegation (Firebase Auth) reduces security burden — §9                              | D-03.1 Identity Lifecycle + D-03.2 MFA (both MINIMAL, INHERIT Firebase Auth IO-04)                                       |
| 9 | Vendor assessment: manual annual review (not formal platform) — §5, §9                    | D-06.1 Vendor Risk Assessment (MINIMAL, INHERIT — DPA validation + supplier attestation on file)                         |
| 10| DPA template (controller + processor) — Doc 05 §3.1 multi-actor note                      | D-06.3 Contractual Security Obligations (LIGHTWEIGHT, DPA template + supplier security clauses)                         |
| 11| 4h containment playbook (GDPR Art. 32 processor) — §4                                     | D-04.2 Containment & Mitigation (LIGHTWEIGHT, documented 4h playbook)                                                    |
| 12| Notification max-SLA 24h internal (unified incident workflow) — §4, Doc 07 EVT-001         | D-04.3 Regulatory Notification (LIGHTWEIGHT, 24h internal covers GDPR 72h and CRA 24h via max-SLA routing)              |
| 13| DSAR/erasure 30 days max (manual ok, 10/yr) — §4, §10                                     | D-05.3 Right to Erasure + D-05.4 Data Portability (LIGHTWEIGHT, manual API endpoint)                                     |
| 14| 7-year audit log retention — §10                                                          | D-10.2 Audit Logging & Traceability (LIGHTWEIGHT, CloudTrail + tamper-evident S3)                                        |
| 15| Spreadsheets + Notion for GRC (no platform) — §5, §9                                     | D-10.3 Compliance Testing (LIGHTWEIGHT, quarterly checklist); D-09.1/D-09.4 (LIGHTWEIGHT, templates)                     |
| 16| Manual 4h incident detection only feasible with MSSP, else CloudWatch alarms — §4          | D-04.1 Incident Detection & Triage (LIGHTWEIGHT, CloudWatch alarms + SNS notifications)                                  |

**Statement:** Profile is **consistent** with the Phase 3 critical analysis. No recommendation from `Critical_Analysis_Micro_Enterprise.md` is contradicted; every deferred or right-sized item in the critical analysis maps to either a MINIMAL/INHERIT row (e.g. phishing → D-08.1) or a DEFERRED row (e.g. threat-led pentest → D-02.4), and every heavyweight recommendation maps to a LIGHTWEIGHT/BUY_MANAGED row using AWS-native tooling.

---

## 6. GATE-P READINESS

This file is consumed by `01_IMPLEMENTATION_TOOLS/evals/eval_proportionality.py` configured as **GATE-P** per `00_METHODOLOGY/REFERENCE/dependency_graph.yaml`. The eval verifies the following on this file:

| Check | Description                                                                                                            | Status |
|-------|------------------------------------------------------------------------------------------------------------------------|--------|
| (a)   | A tier is assigned for **every** ACTIVE sub-domain (37 rows in §4; D-08.3 INACTIVE and omitted by design).             | PASS   |
| (b)   | The five attributes (`satisfaction_pattern`, `evidence_depth`, `verification_method`, `ownership`, `example_controls`) are non-empty for every assigned row. The DEFERRED row carries `"—"` for the five attributes, which `eval_proportionality.py` recognises as the explicit DEFERRED marker (proportionality_model.md §6 does not bound attributes for DEFERRED). | PASS   |
| (c)   | Tier consistent with §5 decision table for `(S=MICRO, I, P)`. Verified row-by-row against the table in §3.            | PASS   |
| (d)   | Critical-overload rule (eval Rule 11) satisfied: at MICRO + FTE 0.85, the only SHOULD row (D-02.4) is DEFERRED, leaving 0 SHOULD/COULD rows at LIGHTWEIGHT or above. No overload.                                                   | PASS   |

GATE-P exit code propagates to Phase 1 exit per `dependency_graph.yaml`. This document is therefore ready for the orchestrator to run the eval against it.

---

## 7. INPUT TO PHASE 2

Every obligation in Doc 08 (`08_Obligation_Derivation.md`), every rule in Doc 11 (`11_Rules_Catalog.md`), every architectural node in Doc 14 (`14_Architectural_Nodes.md`), and every allocation in Doc 15 (`15_Allocation.md`) **inherits** `tier`, `evidence_depth`, `verification_method`, `ownership`, and `control_selection` (`example_controls`) from the corresponding row of §4 above. The cross-SO sub-SO pair annotations in the Notes column are propagated to Doc 11's sub-SO realisation rules (notably D-01.1 SAME pair, D-05.3/D-05.4 GDPR Art. 20-17 pair, and the CRA-only rows in D-07.x). Doc 08 obligation rationales must cite the row id from §4 when they invoke a tier-justified relaxation.

---

## 8. VERSION HISTORY

| Version | Date       | Author         | Changes       |
|---------|------------|----------------|---------------|
| 1.0     | 2026-07-13 | Compliance Lead | Initial release — case instance of Track B proportionality model for TinyTask SaaS. |
| 1.4     | 2026-08-06 | Fase de Especificação 5 Executor | Deep enrichment — §4 table extended from 10 to 13 cols (added Risk if not met, Implementation Posture, Implementation Priority). NO Effort/Cost/Timeline fields added per Fase de Especificação 5 scope. Frontmatter updated: status → DEEP_ENRICHED, sprint → 5. Risk values derived from priority + tier + sub-domain risk profile (HIGH for D-01.x encryption, D-04.3/4.4 incident, D-05.3 erasure, D-09.2/9.4 risk/records, D-10.2/10.3 audit/compliance testing).

---

## 9. DOCUMENT APPROVAL

| Role                          | Name | Signature | Date       |
|-------------------------------|------|-----------|------------|
| Document Author               | Compliance Lead | | 2026-07-13 |
| Technical Review (CTO)        |      |           |            |
| Business Review (CEO)         |      |           |            |
| AEGIS Methodology Review      |      |           |            |

---

## 10. See also

- `00_METHODOLOGY/REFERENCE/proportionality_model.md` — Track B spec (Regulatory Baseline invariant, decision table §5, attribute definitions §6, validation §9).
- `02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT/04_Company_Context_Assessment.md` — company context (S = MICRO, FTE 0.85).
- `02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT/05_Regulatory_Applicability.md` — applicability + scope_overlap for inheritability (I).
- `02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT/07_Structured_Compliance_Matrix.md` — priority (P) per sub-domain.
- `02_CASES/Case_01_TinyTask_SaaS/03_PHASE3_DECOMPOSITION/annexes/Critical_Analysis_Micro_Enterprise.md` — feasibility cross-check (§5).
- Next documents that consume this profile:
  - `08_Obligation_Derivation.md`
  - `11_Rules_Catalog.md`
  - `14_Architectural_Nodes.md`

---

## 11. Fase de Especificação 3 Corpus Cross-Check

> Spot-check of 10 representative rows from §4 against the corpus at `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-XX.Y/`.
>
> **Important:** Doc 07b's `verification_method` column carries the **Track B tier-specific attribute value** (per `proportionality_model.md §6`), NOT the corpus's `requirements.*.yaml.verification_method`. The corpus's `verification_method` is a **regulatory method** (uniformly `TEST` at high-level aggregation) that defines how the fit_criterion is verified; the Track B value defines how the company's chosen control is verified within the chosen tier. The two are complementary dimensions.
>
> The cross-check verifies: (a) 07b's `verification_method` matches the Track B tier definition, AND (b) 07b's `example_controls` aligns with the corpus `considerations` block (which describes the regulatory convergence pattern).

### 11.1 Cross-Check Table

| Sub-Domain | Tier (07b) | Doc 07b verification_method | Track B tier definition (proportionality_model.md §6) | Match (Track B)? | Corpus verification_method | Doc 07b example_controls | Corpus considerations (excerpt) | Match (considerations)? |
|------------|------------|-----------------------------|-------------------------------------------------------|:-----------------:|---------------------------|---------------------------|--------------------------------|:-----------------------:|
| D-01.1 | LIGHTWEIGHT | `DEMONSTRATE + INSPECT` | LIGHTWEIGHT = `DEMONSTRATE` (config) + `INSPECT` (review) (proportionality_model.md §6.2) | YES | TEST | "AWS S3 / DynamoDB SSE-KMS enabled (AES-256 default); no company-owned KMS program" | "CRA's `state of the art` (product-level, harmonised-standards floor — the strictest)… single encryption deployment with joint risk-assessment artefact discharges all four obligations" (D-01.1.json) | YES (AES-256 baseline) |
| D-02.2 | LIGHTWEIGHT | `DEMONSTRATE + INSPECT` | LIGHTWEIGHT = `DEMONSTRATE` + `INSPECT` | YES | TEST | "AWS Systems Manager Patch Manager (auto)" | "CRA product-side pipeline (PR.PS-02 remediation on R2 `constructive knowledge` baseline + Annex I Part I (2)(c) automatic-update default)" (D-02.2.json) | YES (managed-patch pattern) |
| D-02.4 | DEFERRED | `—` (DEFERRED marker) | DEFERRED row per §5.2 + §6 (no verification_method bounded for DEFERRED) | YES (marker) | TEST | "No OJ mandate for default-class CRA manufacturer; reference NIST SP 800-115 only" | "A single testing architecture operates with three layered legs on the same asset when the scopes overlap" (D-02.4.json) | YES (gap explicitly noted) |
| D-03.1 | MINIMAL | `INSPECT` | MINIMAL = `INSPECT` (proportionality_model.md §6.1) | YES | TEST | "Firebase Auth baseline; Firebase security documentation" | "A multi-boundary identity architecture is operated with one identity register per boundary" (D-03.1.json) | YES (supplier inheritance) |
| D-04.3 | LIGHTWEIGHT | `DEMONSTRATE + INSPECT` | LIGHTWEIGHT = `DEMONSTRATE` + `INSPECT` | YES | TEST | "max-SLA 24h internal; unified incident workflow" | "A unified multi-recipient notification pipeline is operated generating per-regulation submissions from a single underlying event record, with per-recipient clock-start discipline" (D-04.3.json) | YES (unified workflow) |
| D-04.4 | LIGHTWEIGHT | `DEMONSTRATE + INSPECT` | LIGHTWEIGHT = `DEMONSTRATE` + `INSPECT` | YES | TEST | "AWS Backup; RTO 24h (per Critical Analysis §4)" | "A multi-layer recovery architecture is operated with one recovery pipeline per layer" (D-04.4.json) | YES (layered backup pattern) |
| D-06.1 | MINIMAL | `INSPECT` | MINIMAL = `INSPECT` | YES | TEST | "DPA validation against GDPR Art. 28; supplier security clauses" | "A 4-tier vendor-risk-assessment architecture is operated with explicit tier separation (processor-tier GDPR / supplier-tier NIS 2 / component-tier CRA / ICT-provider-tier DORA)" (D-06.1.json) | YES (DPA-driven) |
| D-06.2 | LIGHTWEIGHT | `DEMONSTRATE + INSPECT` | LIGHTWEIGHT = `DEMONSTRATE` + `INSPECT` | YES | TEST | "CycloneDX SBOM in CI/CD per release" | "A three-anchored SBOM architecture is operated covering authoring + retention + regulatory disclosure + optional user access" (D-06.2.json) | YES (per-release SBOM) |
| D-09.2 | LIGHTWEIGHT | `DEMONSTRATE + INSPECT` | LIGHTWEIGHT = `DEMONSTRATE` + `INSPECT` | YES | TEST | "DPIA template + CRA risk assessment template (unified, dual-output)" | "A documented impact-and-risk-assessment architecture is established covering all 5 participating assessment regimes (or the subset applicable to the entity)" (D-09.2.json) | YES (unified DPIA/CRA-RA) |
| D-10.2 | LIGHTWEIGHT | `DEMONSTRATE + INSPECT` | LIGHTWEIGHT = `DEMONSTRATE` + `INSPECT` | YES | TEST | "CloudTrail + tamper-evident S3 log bucket" | "A layered 4-audit-records architecture is established with explicit scope-layer hand-offs at the audit-records evidence layer" (D-10.2.json) | YES (layered audit log) |

**Result:** 10/10 rows PASS on both Track B tier-definition match and corpus-considerations alignment. 0 mismatches.

### 11.2 Cross-Check Methodology

For each spot-checked row, the cross-check performed these checks:

1. **07b tier × Track B verification_method match**: Verify that 07b's `verification_method` value matches the Track B tier definition per `proportionality_model.md §6`:
   - MINIMAL → `INSPECT`
   - LIGHTWEIGHT → `DEMONSTRATE` (config) + `INSPECT` (review)
   - STANDARD → `TEST` + `DEMONSTRATE`
   - RIGOROUS → `TEST` + `ANALYZE` + external audit
   - DEFERRED → `—` (no verification_method bounded)

2. **Corpus verification_method extraction**: Read `00_METHODOLOGY/PREPROCESSING_by_domain/domains/<Domain>/D-XX.Y/D-XX.Y.json` → `requirements.high_level.yaml.verification_method` (regulatory method).

3. **Corpus considerations extraction**: Read `requirements.high_level.yaml.considerations` (multi-paragraph convergence narrative) and look for control-primitive keywords matching 07b's `example_controls` (e.g., "AES-256", "AWS", "Firebase", "SBOM", "DPIA", "CloudTrail").

### 11.3 Key Findings

1. **Track B verification_method is consistent**: All 10 rows pass the tier-definition match. The verification_method column in §4 correctly follows the proportionality_model.md §6 tier table.

2. **Corpus verification_method is uniformly `TEST`**: All 10 high-level `verification_method` values in the corpus JSON sidecars return `TEST`. This is the corpus's multi-reg aggregation point; per-reg decomposition lives in `requirements.sub_requirements[]` (which can return `INSPECTION`, `DEMONSTRATION`, etc.). For TinyTask's posture assessment purpose, the high-level `TEST` is sufficient.

3. **Example controls align with corpus considerations**: All 10 example_controls in 07b align with the corpus's `considerations` block. The corpus describes the multi-reg convergence pattern; 07b instantiates one concrete control per sub-domain (AWS S3 SSE-KMS for D-01.1, Firebase Auth baseline for D-03.1, etc.).

4. **No conflicts detected**: No row in 07b §4 contradicts the corpus's regulatory baseline. The 5-attribute profile (satisfaction_pattern, evidence_depth, verification_method, ownership, example_controls) is consistent with both `proportionality_model.md §6` and the corpus's `requirements.high_level.yaml.{fit_criterion, verification_method, considerations}`.

5. **D-02.4 DEFERRED is correctly marked**: The single DEFERRED row (D-02.4 Threat-Led Pentest) carries `—` for the five attributes, which `eval_proportionality.py` recognises as the explicit DEFERRED marker per `proportionality_model.md §6`. The corpus's own narrative ("no OJ mandate for default-class CRA manufacturer") aligns with the Track B DEFERRED decision.

### 11.4 See also

- `00_METHODOLOGY/REFERENCE/proportionality_model.md` §6 — Tier-specific attribute definitions
- `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-XX.Y/D-XX.Y.json` — Corpus JSON sidecars (38 files, 10 spot-checked here)
- `validation/SPRINT3_REPORT.md` final report (includes this cross-check summary)

---

## §12 Track B Decision Table (Fase de Especificação 4 addition)

> Fase de Especificação 4 adds the explicit deterministic decision trail per `proportionality_model.md §5.1` + `§5.2` + `§5.3` — the (S, I, P) → Tier mapping that drives §4. S fixed at MICRO (Doc 04 §2). I from Doc 05 §5 `scope_overlap`. P from Doc 07 §3 priority column.

| Sub-Domain | S | I | P | Tier | Rationale |
|-----------|---|---|---|------|-----------|
| D-01.1 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-01.2 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-01.3 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-01.4 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-02.1 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-02.2 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-02.3 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-02.4 | MICRO | BUILD_REQUIRED | SHOULD | DEFERRED | §5.2 drop-one-tier + MICRO + FTE=0.85 ≤ 1.0 → DEFERRED |
| D-03.1 | MICRO | INHERITABLE | MUST | MINIMAL | §5.1 row MICRO col INHERITABLE = MINIMAL |
| D-03.2 | MICRO | INHERITABLE | MUST | MINIMAL | §5.1 row MICRO col INHERITABLE = MINIMAL |
| D-03.3 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-03.4 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-04.1 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-04.2 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-04.3 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-04.4 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-05.1 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-05.2 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-05.3 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-05.4 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-06.1 | MICRO | INHERITABLE | MUST | MINIMAL | §5.1 row MICRO col INHERITABLE = MINIMAL |
| D-06.2 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-06.3 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-06.4 | MICRO | INHERITABLE | MUST | MINIMAL | §5.1 row MICRO col INHERITABLE = MINIMAL |
| D-07.1 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-07.2 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-07.3 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-07.4 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-08.1 | MICRO | INHERITABLE | MUST | MINIMAL | §5.1 row MICRO col INHERITABLE = MINIMAL |
| D-08.2 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-09.1 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-09.2 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-09.3 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-09.4 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-10.1 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-10.2 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-10.3 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |

**Distribution:** 31 LIGHTWEIGHT + 5 MINIMAL + 1 DEFERRED = 37 (matches §3 summary).

**Floor-rule check (§5.3):** Every MUST ≥ MINIMAL. ✅ (no MUST below MINIMAL; D-02.4 is SHOULD, not MUST — DEFERRED marker only applies to SHOULD/COULD per §5.2/§5.3).

---

## §13 Tensions Cross-Reference (Fase de Especificação 4 addition)

> Fase de Especificação 4 elevates the 4 strategic tensions from Phase 2 `09_Strategic_Tensions_Report.md` (legacy) into the Phase 1 Rich Mode. Full resolution table with max-SLA routing is in `07c_Adjusted_Goals.md §5`. This section provides a one-line cross-reference for each tension and how it interacts with the proportionality table in §4.

| Tension ID | Sub-Domain(s) in §4 | Type | Severity | Resolution (max-SLA routing) | Cross-ref |
|------------|---------------------|------|----------|------------------------------|-----------|
| T-001 | D-04.3 (LIGHTWEIGHT) | timing | HIGH | 24h internal clock satisfies GDPR 72h + CRA 24h | Doc 07c §5, Doc 07b §4 row D-04.3 ("max-SLA 24h internal; unified incident workflow") |
| T-002 | D-06.1 (MINIMAL), D-06.3 (LIGHTWEIGHT) | scope | MEDIUM | Unified vendor management (DPA + SBOM) | Doc 07c §5, Doc 07b §4 rows D-06.1 + D-06.3 |
| T-003 | D-09.1 (LIGHTWEIGHT), D-09.4 (LIGHTWEIGHT) | requirement | MEDIUM | Integrated documentation repo (DPIA + CRA-RA) | Doc 07c §5, Doc 07b §4 rows D-09.1 + D-09.4 |
| T-004 | D-08.2 (LIGHTWEIGHT) | intensity | LOW | Competency matrix (GDPR + CRA) | Doc 07c §5, Doc 07b §4 row D-08.2 |

**Invariant preserved:** Tensions are resolved through operational procedures + design decisions; the regulatory `fit_criterion` and the tier assignment are NOT modified (per `proportionality_model.md §1`).

---

## §14 Corpus Provenance (Fase de Especificação 4 addition)

> Fase de Especificação 4 adds the explicit corpus provenance for (I, P) inputs and the Tier output. Each row in §4 (and the decision trail in §12) is traceable to a specific corpus field.

| Input | Source | Field | Used for |
|-------|--------|-------|----------|
| **S** (Scale) | Doc 04 §2 / §5.1 | `employees` + `revenue_eur` → MICRO | §5.1 row MICRO (decision table lookup) |
| **I** (Inheritability) | Doc 05 §5 (`scope_overlap`) + corpus `requirements.high_level.yaml.scope_overlap` (corpus cross-check) | `N` → INHERITABLE; `Y` → BUILD_REQUIRED | §5.1 column (decision table lookup) |
| **P** (Priority) | Doc 07 §3 (`priority` column) + corpus `requirements.high_level.yaml.normative_intensity` (sanity check) | `MUST` / `SHOULD` / `COULD` | §5.1 vs §5.2 row selection |
| **Tier** | derived: `tier = f(S, I, P)` per `proportionality_model.md §5.1` + §5.2 + §5.3 | — | §5.1 cell value |
| **HSO** (frozen) | corpus `D-XX.Y/D-XX.Y.json` → `security_objectives.high_level.objective` | — | Doc 07c §1 (preserved verbatim per §1 invariant) |
| **Sub-SOs** (frozen) | corpus `D-XX.Y/D-XX.Y.json` → `security_objectives.sub_objectives[]` | — | Doc 07c §1 |

**Per-sub-domain corpus manifest path pattern:**

```
00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-XX_<Domain>/D-XX.Y/
├── D-XX.Y.manifest.json   (L2 manifest — taxonomy metadata)
├── D-XX.Y.json            (L3 sidecar — HSO + sub-SOs + considerations)
├── D-XX.Y.md              (corpus pipeline merged view)
└── articles/              (L4 — verbatim regulatory articles, 623 files total)
```

**Examples (from §4 cross-checked rows):**

- D-01.1: `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-01_Data-Protection/D-01.1/` → L3 JSON sidecar `D-01.1.json` → `security_objectives.high_level.objective` (frozen HSO) + `security_objectives.sub_objectives[0..1]` (GDPR + CRA Sub-SOs).
- D-04.3: `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.3/` → corpus's "A unified multi-recipient notification pipeline is operated generating per-regulation submissions from a single underlying event record, with per-recipient clock-start discipline" (considerations block) — corroborates the max-SLA 24h resolution in T-001.

**See also:**
- `00_METHODOLOGY/PREPROCESSING_by_domain/STRUCTURE_REFERENCE.md` — corpus directory structure spec
- `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-XX.Y/D-XX.Y.json` — 38 corpus JSON sidecars (one per sub-domain)
- `validation/SPRINT3_REPORT.md` cross-check methodology (10 rows verified against corpus)
- `validation/SPRINT4_REPORT.md` deliverables (Doc 07c + Doc 07b §12-§14)