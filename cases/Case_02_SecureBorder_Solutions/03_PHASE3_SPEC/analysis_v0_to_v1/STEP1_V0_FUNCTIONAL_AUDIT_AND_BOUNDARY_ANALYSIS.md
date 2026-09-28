# Step 1 — V0 Functional Audit & Boundary Analysis (SecureBorder eGate)

> **Input:** `../v0_functional_baseline/Doc01`/`Doc02` (LOCKED, 1.0.0) — 11 functional areas, 28 requirement cards, 28 PUCs, 28 Level-1 use cases, 10 quality attributes (`RN1`–`RN10`).

## 1. Functional Areas, Assets, and Trust Boundaries

| Area | Requirement cards | Core assets handled | Trust boundaries crossed |
|---|---|---|---|
| R1 — Traveller Biometric Verification | `R1.1`, `R1.2`, `R1.3` | Raw biometric captures (ephemeral), biometric verification templates, passage decision records | Traveller↔gate sensor; gate↔back-office verification service; back-office↔authority enrolment record |
| R2 — Human Oversight & Gate Control | `R2.1`, `R2.2` | Override decisions, referral tickets | Operator workstation↔verification service |
| R3 — Operator Identity & Access | `R3.1`, `R3.2`, `R3.3` | Operator identities, credentials, entitlements | Operator↔identity service; site↔central identity store |
| R4 — Traveller Data Rights | `R4.1`, `R4.2` | Rights requests, erasure/portability outputs, records of processing | Data subject↔back-office; back-office↔authorities (correction cascades) |
| R5 — Security Monitoring & Incidents | `R5.1`, `R5.2`, `R5.3` | Fleet security events, incident records, continuity state | Gates/SOC↔fleet monitoring; SOC↔site operations |
| R6 — Regulatory Notifications | `R6.1` | Notification dossiers (GDPR/CRA/NIS 2/AI Act) | Back-office↔supervisory authorities, CSIRT, market surveillance |
| R7 — Vulnerabilities & Updates | `R7.1`, `R7.2`, `R7.3` | Vulnerability register, update packages, disclosure records | Update pipeline↔deployed fleet; researchers↔CVD intake |
| R8 — Secure Development & Releases | `R8.1`, `R8.2`, `R8.3` | Pipeline gates, SBOMs, AI model versions | Development↔release pipeline; pipeline↔fleet |
| R9 — AI Quality & Conformity | `R9.1`, `R9.2`, `R9.3` | AI risk-management file, conformity documentation, monitoring metrics, test reports | AI governance↔verification service; provider↔deployer |
| R10 — Governance, Risk & Vendors | `R10.1`, `R10.2`, `R10.3` | Unified assessments, vendor records, provenance, compliance dossiers | Entity↔suppliers/processors; entity↔auditors |
| R11 — Training & Competence | `R11.1`, `R11.2` | Training programs, competence records | Entity↔workforce |

## 2. Actor & External-System Inventory

- **Human actors:** Traveller (gate session), Border Control Officer, SOC Analyst, Security Engineer, Release Engineer, AI Governance Lead, Privacy Officer (DPO), Compliance Analyst, Site Operations Technician, CISO.
- **External systems:** Government Border Authority Integration (enrolment records, decision records), Regulatory Dispatch Service (authority notification transport).

## 3. Ingress Points and Exposure Surface

1. **Gate capture session** — biometric capture at the physical gate (the highest-sensitivity ingress; special-category data).
2. **Authority integration channel** — bidirectional enrolment/decision record exchange.
3. **Regulatory dispatch channel** — statutory notification transport under four notification regimes with distinct clocks.
4. **Update/distribution channel** — signed software and AI-model updates to a geographically distributed fleet.
5. **Back-office operator interfaces** — oversight, identity, incident, governance functions.

## 4. V0 Characteristics Relevant to Synthesis

- The V0 was elicited for a **MEDIUM-scale, RIGOROUS-tier essential entity** whose product *is* a security system: the functional set already includes the operational capabilities (fleet monitoring, incident management, vulnerability management, CVD, SBOM, AI governance, vendor assessment, training) that in lighter products remain organizational — this forecasts a high coverage rate in the exhaustive mapping.
- UCs are in the light format (Primary Actor / Goal / Operational Scope); the **fully-dressed Cockburn anatomy is elaborated in the V1 synthesis** (R13 standard), weaving in the security preconditions and extensions from the accepted constraint set.
- Quality attributes `RN1`–`RN10` are standalone (auditability, AI quality/fairness, deployment isolation already present as measurable targets) — the synthesis adds the regulatory constraint set as `RN11`+.
- Tensions T-001 (notification timing), T-002 (erasure vs AI-log retention), T-003 (assessment trigger mismatch), T-004 (vendor-management scope) are pre-harmonized upstream and bind specific objective sets (see STEP2 §4).
