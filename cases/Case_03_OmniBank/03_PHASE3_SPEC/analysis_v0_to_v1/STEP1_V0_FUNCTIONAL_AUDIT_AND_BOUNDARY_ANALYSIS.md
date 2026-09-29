# Step 1 — V0 Functional Audit & Boundary Analysis (OmniBank Financial Systems)

> **Case:** Case 03 — OmniBank Financial Systems S.A. (Consumer Banking with In-House High-Risk Credit-Scoring AI)
> **Input:** `../v0_functional_baseline/Doc01`/`Doc02` (LOCKED, 1.0.0) — 11 functional areas, 43 requirement cards, 43 PUCs, 43 Level-1 use cases, 10 quality attributes (`RN1`–`RN10`).

## 1. Functional Areas, Assets, and Trust Boundaries

| Area | Requirement cards | Core assets handled | Trust boundaries crossed |
|---|---|---|---|
| R1 Banking Services & Credit Decisions | `R1.1`–`R1.4` | Customer accounts and transactions; credit applications; **OmniScore model versions**; decision records | Customer↔mobile/web channel; channel↔core banking; decision↔authority/registry; model registry↔serving estate |
| R2 Cryptographic Protection | `R2.1`–`R2.3` | Stored personal/financial/AI data; cryptographic key material | Operator↔custody service; estate↔custody (separated) |
| R3 Vulnerabilities & Patches | `R3.1`–`R3.4` | Vulnerability register; update packages; disclosure records; test evidence | Advisory feeds↔register; release pipeline↔fleet |
| R4 Identities & Access | `R4.1`–`R4.4` | Operator identities, credentials, entitlements; configuration baselines | Workforce↔identity store; AI platform roles↔model artefacts |
| R5 Incidents | `R5.1`–`R5.4` | Security events; incident records; continuity state; AI anomaly records | Estates↔SOC; SOC↔supervisory/registry channels |
| R6 Data Lifecycle & Rights | `R6.1`–`R6.5` | Collection points; retention schedules; rights cases; **AI training datasets** | Data subject↔back-office; datasets↔training pipeline |
| R7 Vendors & Supply Chain | `R7.1`–`R7.4` | **Register of ICT third-party providers**; SBOMs; contracts; exit plans | Entity↔suppliers/processors; procurement↔register |
| R8 Secure Development & Release | `R8.1`–`R8.4` | Review records; release gates; change approvals; model artefacts | Development↔pipeline↔serving estate |
| R9 Training & Competence | `R9.1`–`R9.3` | Training completions; role competence; board training | Entity↔workforce↔management body |
| R10 Security & AI Governance | `R10.1`–`R10.4` | ISMS documents; **unified five-regime assessments**; asset/AI documentation; reporting dossiers | Entity↔supervisors↔registries |
| R11 Testing & Assurance | `R11.1`–`R11.4` | Detection alerts; **tamper-evident event store**; findings; adversarial results | Detection↔SOC; test environments↔production models |

## 2. Actor & External-System Inventory

- **Customer / Applicant** (banking channel; credit applicant; data subject), **Credit Decision Overseer** (AI Act Art. 14 empowered reviewer), **Bank Operators** (SOC analysts, security engineers, cryptographic officers, release engineers, ML/AI data engineers, AI operations, DPO team, compliance officers, vendor risk managers, identity administrators, internal audit, penetration testers, training officers), **Management Body**.
- **External systems:** supervisory authorities / CSIRT / financial authorities / market-surveillance authorities, AI registry (notification and registry channels).

## 3. Ingress Points and Exposure Surface

1. **Customer channels** (mobile application, web platform) — retail PII, transactions, card data.
2. **Credit-origination path** — applicant data, financial data, and the **OmniScore high-risk AI surface** (training data, model artefacts, serving decisions).
3. **Authority and registry channels** — incident notifications, conformity and registration submissions (five regimes).
4. **Release and model-update channel** — signed software and model updates to a multi-site estate.
5. **Back-office operator interfaces** — oversight, identity, incident, governance functions.

## 4. V0 Characteristics Relevant to Synthesis

- The V0 was elicited for a **LARGE, ECB-supervised critical-sector entity** whose functional repertoire already spans the operating functions the five regimes demand of the *product and its operation* (SOC monitoring, vulnerability management, resilience testing, vendor register, AI governance, training) — this forecasts high functional coverage in the exhaustive mapping.
- UCs are in the light identification format; the **fully-dressed Cockburn anatomy** is elaborated in the V1 synthesis, weaving in the accepted security preconditions/extensions.
- Quality attributes `RN1`–`RN10` are standalone and company-given (performance, availability, scalability, recoverability, privacy responsiveness, auditability, AI quality, AI fairness, interoperability, architectural integrity) — the synthesis adds the regulatory constraint set as `RN11`–`RN26` plus chain rows.
- Tensions T-001 (five notification regimes), T-002 (erasure vs financial-record/AI-log retention), T-003 (assessment trigger mismatch), T-004 (vendor-management scope incl. the DORA register), T-005 (provider/deployer duty stacking) are pre-harmonized upstream and bind specific objective sets (see STEP2).
