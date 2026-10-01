# AEGIS Phase 3 — Part 2: Step 5 — Consolidated Risk Register & Exit Gate Certification (TinyTask SaaS)

> **Case Study:** Case 01 — TinyTask SaaS (B2B Task Management Multi-Tenant Platform)  
> **Lifecycle Phase:** AEGIS Phase 3 — Specification, **Part 2 of 2 (Threat & Risk Analysis)**  
> **Step Deliverable:** Step 5 of 5 (`05_RISK_REGISTER_AND_GOVERNANCE.md`)  
> **Upstream Inputs:** Step 1 ([`01_SYSTEM_MODEL_ASSETS_AND_BOUNDARIES.md`](01_SYSTEM_MODEL_ASSETS_AND_BOUNDARIES.md)), Step 2 ([`02_TECHNICAL_THREATS_STRIDE.md`](02_TECHNICAL_THREATS_STRIDE.md)), Step 3 ([`03_PRIVACY_THREATS_LINDDUN.md`](03_PRIVACY_THREATS_LINDDUN.md)), Step 4 ([`04_ATTACK_VECTORS_AND_DEFENSE_TREES.md`](04_ATTACK_VECTORS_AND_DEFENSE_TREES.md))  
> **Methodological Standard:** [`../../../templates/phase3_threat_risk_guidelines.md`](../../../templates/phase3_threat_risk_guidelines.md) §6.5 & [`00_METHODOLOGY_AND_EXECUTION_GUIDE.md`](00_METHODOLOGY_AND_EXECUTION_GUIDE.md) §6.5  

---

## 1. Executive Summary & Cockpit Dashboard

This document provides the **authoritative risk governance ledger, executive visualization cockpit, and Exit Gate certification** consolidating 100% of the technical and privacy threats elicited across TinyTask SaaS under Phase 3 Part 2.

### 1.1 Executive KPI Cockpit (30-Second Overview)

| Metric | Inherent Value (Unconstrained) | Residual Value (Post-Mitigation) | Operational Delta ($\Delta$) | Governance Status |
|---|---|---|---|---|
| **Total Threats Elicited** | 28 consolidated threats (21 STRIDE + 8 LINDDUN, less 1 declared cross-lens merge) | 28 register rows cataloged | 100% coverage | **COMPLETE** |
| **Critical Risk Threats (🔴)** | **15 threats (53.6%)** | **0 threats (0.0%)** | **-15 (-100.0%)** | 🟢 **ZERO-CRITICAL RULE MET** |
| **High Risk Threats (🟠)** | **9 threats (32.1%)** | **7 threats (25.0%)** | **-2 (-22.2%)** | 🟢 **FORMALLY MITIGATED & JUSTIFIED** |
| **Medium Risk Threats (🟡)** | **4 threats (14.3%)** | **1 threats (3.6%)** | **-3 (-75.0%)** | 🟢 **OPERATIONAL CONTROLS ACTIVE** |
| **Low Risk Threats (🟢)** | **0 threats (0.0%)** | **20 threats (71.4%)** | **+20 (+100.0%)** | 🟢 **BROADLY ACCEPTABLE POSTURE** |
| **Aggregate Risk Score Sum** | **95 points** (Avg 3.39 / threat) | **43 points** (Avg 1.54 / threat) | **-52 points (-54.7%)** | 🟢 **54.7% RISK REDUCTION QUOTIENT** |
| **Part 2 Exit Gate (G7–G12)** | Pending verification | **All 6 Gates GREEN** | Passed without exception | 🟢 **CLEARED FOR HANDOFF TO PHASE 4** |

---

### 1.2 Visual Risk Heatmap (Inherent vs. Residual Migration)

$$\text{Qualitative Risk Level} = \text{Likelihood (1: Low, 2: Med, 3: High)} \times \text{Impact (1: Low, 2: Med, 3: High, 4: Critical)}$$
$$\text{Color Scale: } \color{green}\blacksquare\text{ Baixo (1–2)} \quad \color{gold}\blacksquare\text{ Médio (3–4)} \quad \color{orange}\blacksquare\text{ Alto (6)} \quad \color{red}\blacksquare\text{ Crítico (8–12)}$$

#### A. Inherent Risk Matrix ($R_{\text{inh}}$ — Functional Surface Unconstrained)
*Demonstrates the baseline exposure of TinyTask SaaS before the enforcement of AEGIS Part 1 constraints:*

| Likelihood \ Impact | Low Impact (1) | Medium Impact (2) | High Impact (3) | Critical Impact (4) |
|---|---|---|---|---|
| **High Likelihood (3)** | 🟢 0 Ameaças | 🟠 1 Ameaça (`#23`) | 🔴 **6 Ameaças** (`#1`, `#7`, `#14`, `#15`, `#19`, `#24`) | 🔴 **8 Ameaças** (`#2`, `#4`, `#5`, `#9`, `#12`, `#13`, `#21`, `#28`) |
| **Med Likelihood (2)** | 🟢 0 Ameaças | 🟡 4 Ameaças (`#8`, `#16`, `#26`, `#27`) | 🟠 8 Ameaças (`#3`, `#6`, `#10`, `#11`, `#17`, `#18`, `#20`, `#25`) | 🔴 **1 Ameaça** (`#22`) |
| **Low Likelihood (1)** | 🟢 0 Ameaças | 🟢 0 Ameaças | 🟢 0 Ameaças | 🔴 0 Ameaças |

> **Inherent Quadrant Verdict:** **15 Críticos (🔴)**, **9 Altos (🟠)**, **4 Médios (🟡)**, **0 Baixos (🟢)**.  
> *54% das interações residem no quadrante inaceitável de risco crítico.*

---

#### B. Residual Risk Matrix ($R_{\text{res}}$ — Post-Mitigation via EARS Constraints `RN1`–`RN30`)
*Demonstrates the post-mitigation state following architectural enforcement, rate limiting, RBAC mediation, and cryptographic isolation:*

| Likelihood \ Impact | Low Impact (1) | Medium Impact (2) | High Impact (3) | Critical Impact (4) |
|---|---|---|---|---|
| **High Likelihood (3)** | 🟢 0 Ameaças | 🟡 0 Ameaças | 🟠 0 Ameaças | 🔴 **0 Ameaças** |
| **Med Likelihood (2)** | 🟢 0 Ameaças | 🟡 0 Ameaças | 🟠 0 Ameaças | 🔴 **0 Ameaças** |
| **Low Likelihood (1)** | 🟢 **15 Ameaças** (`#6`, `#7`, `#8`, `#11`, `#14`, `#15`, `#16`, `#18`, `#19`, `#20`, `#23`, `#24`, `#25`, `#26`, `#27`) | 🟢 **5 Ameaças** (`#3`, `#10`, `#12`, `#17`, `#28`) | 🟡 **1 Ameaça** (`#1`) | 🟠 **7 Ameaças** (`#2`, `#4`, `#5`, `#9`, `#13`, `#21`, `#22`) |

> **Residual Quadrant Verdict:** **0 Críticos (🔴 — 100% esvaziado)**, **7 Altos (🟠 — impacto latente mitigado por criptografia/tenancy com probabilidade mínima)**, **1 Médio (🟡)**, **20 Baixos (🟢)**.  
> *A massa crítica de risco foi deslocada 100% para os quadrantes de aceitabilidade operacional.*

---

### 1.3 Postura de Risco por Componente e Subsistema Arquitetural

Esta tabela consolida a exposição de risco e a eficácia das defesas por subsistema funcional (`P1` a `P8`), identificando o papel de cada componente na arquitetura:

| Subsistema / Componente | Papel Funcional no TinyTask | Ameaças Mapeadas | Risco Inerente Máximo | Risco Residual Máximo | Princípios de Segurança Ativos (Fase 2) | Requisitos Mitigadores (Fase 3 Part 1) |
|---|---|---|---|---|---|---|
| **P1: Identity & Authentication** | Registo, autenticação, perfil, recuperação de conta | `#1`, `#2`, `#3`, `#4` | 🔴 **Crítico** (12) | 🟠 **Alto** (4, Mitigado) | `PRIN-ENG-01` (Least Privilege)<br>`PRIN-ENG-04` (Fail-Safe Defaults) | `RN10` (Credential Confidentiality), `RN11` (Session Invalidation), `RN18` (Audit), `RN24` (Transport Crypto), `RN26` (Privacy Audit) |
| **P2: Workspace Governance** | Workspaces, membros, papéis, métricas | `#5`, `#6`, `#7`, `#8` | 🔴 **Crítico** (12) | 🟠 **Alto** (4, Mitigado) | `PRIN-ENG-05` (Separation of Duties)<br>`PRIN-ENG-03` (Complete Mediation) | `RN9` (Tenancy Isolation), `RN12` (RBAC), `RN22` (Anti-Profiling), `RN28` (Safe Defaults) |
| **P3: Project Management** | Projetos, configuração, isolamento | `#9`, `#10` | 🔴 **Crítico** (12) | 🟠 **Alto** (4, Mitigado) | `PRIN-ENG-06` (Least Common Mechanism)<br>`PRIN-ENG-03` (Complete Mediation) | `RN9` (Isolation Filter), `RN12` (RBAC), `RN18` (Security Logging) |
| **P4: Task Engine & Automation** | Tarefas, estados, recorrência | `#11` | 🟠 **Alto** (6) | 🟢 **Baixo** (1) | `PRIN-ENG-04` (Fail-Safe Defaults) | `RN9` (Isolated Daemon), `RN17` (Throttling), `RN18` (Audit) |
| **P5: Attachments & Collaboration** | Anexos binários, comentários | `#12`, `#13`, `#14`, `#15`, `#16` | 🔴 **Crítico** (12) | 🟠 **Alto** (4, Mitigado) | `PRIN-ENG-02` (Defense in Depth)<br>`PRIN-ENG-03` (Complete Mediation) | `RN13` (Upload Validation & Content Isolation), `RN14` (Content Neutralization), `RN25` (Orphan Cleanup) |
| **P6: Audit History & Notifications** | Histórico de auditoria, alertas, digests | `#17`, `#18` | 🟠 **Alto** (6) | 🟢 **Baixo** (2) | `PRIN-ENG-07` (Data Minimization)<br>`PRIN-ENG-02` (Defense in Depth) | `RN9` (Read Permissions), `RN17` (Throttling), `RN18` (Read-Only Records), `RN24` (Transport Crypto) |
| **P7: Billing & Quota Engine** | Subscrições, checkout, webhooks, grace period | `#19`, `#20` | 🔴 **Crítico** (9) | 🟢 **Baixo** (1) | `PRIN-ENG-02` (Third-Party Isolation)<br>`PRIN-ENG-05` (Separation of Duties) | `RN7` (Gateway Channels), `RN12` (Owner Auth), `RN15` (Billing Invariant), `RN16` (Webhook Verification), `RN18` (Audit) |
| **P8: Subject Rights & Erasure** | GDPR Arts. 15–22, exportação, purge | `#21`, `#22`, `#23`, `#24`, `#25`, `#26`, `#27`, `#28` | 🔴 **Crítico** (12) | 🟠 **Alto** (4, Mitigado) | `PRIN-ENG-01` (Least Privilege)<br>`PRIN-ENG-04` (Cryptographic Erasure) | `RN20` (Portability Export), `RN21` (Erasure & Pseudonymization), `RN26` (Privacy Audit), `RN27` (Requester Verification), `RN30` (Permanent Removal) |

---

## 2. Master Consolidated Risk Register (18-Column Enriched Ledger)

### 2.1 Cross-Lens Merge Record

The STRIDE and LINDDUN lenses share the canonical `TM-D-XX.Y-NNN` namespace. Where both lenses carry the **same real-world threat**, the register consolidates them into one row under this declared record — no threat is silently dropped, and the ledger arithmetic (21 STRIDE + 8 LINDDUN − 1 declared merge = **28 rows**) is auditable:

| Merged ID | STRIDE Lens Card (`02_TECHNICAL_THREATS_STRIDE.md`) | LINDDUN Lens Card (`03_PRIVACY_THREATS_LINDDUN.md`) | Merge Justification | Canonical Register Scores |
|---|---|---|---|---|
| `TM-D-05.1-001` | Telemetry Leakage & Worker Profiling via Operational Metrics — Information Disclosure (I) | Worker Telemetry Linkability & Productivity Profiling via Activity Timestamps — Linkability (L) / Identifiability (I) | One real-world threat (worker productivity profiling from operational telemetry on `R2.3` / `{U.C. 2.3}`, mitigated by `RN22`): the STRIDE lens scores it High (L2 × I3), the LINDDUN lens scores it Critical (L3 × I3); the register adopts the conservative maximum of the two lens scores. | Inherent L3 × I3 🔴 Crit (9) → Residual L1 × I1 🟢 Baixo (1) — Mitigado |

---

### 2.2 Master Ledger

The central register links every threat to its architectural design weakness (**CWE**), attack mechanism (**CAPEC**), operational adversary tactic (**MITRE ATT&CK**), defensive countermeasure (**MITRE D3FEND**), the **NIST CSF 2.0 anchors** published by its mitigating constraints in the accepted Part 1 baseline, the governing **Secure Design Principle (PRIN-ENG)**, and testable Part 1 EARS requirement (**RNxx**):

| # | Threat ID | Threat Title | Cards / UCs | Class. | MITRE CWE | MITRE CAPEC | MITRE ATT&CK | MITRE D3FEND | NIST CSF Anchors | Secure Design Principle (`PRIN-ENG`) | Inh. L | Inh. I | Inh. Risk | Mitigating Constraints | Res. L | Res. I | Res. Risk & Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `TM-D-03.1-001` | Credential Brute Force & Stuffing | `R1.1` / `{U.C. 1.1}` | S | `CWE-307` | `CAPEC-115` | `T1110.003` | `D3-IRA`, `D3-URR` | PR.DS-01, PR.AA-01, PR.AA-05, PR.AA-06, DE.CM-01, DE.CM-09 | `PRIN-ENG-04: Fail-Safe Defaults` | 3 | 3 | 🔴 **Crit** (9) | `RN10`, `RN11`, `RN18` | 1 | 3 | 🟡 **Médio** (3) — Mitigado |
| 2 | `TM-D-07.1-001` | Cleartext Network Interception | `R1.1` / `{U.C. 1.1}` | I, T | `CWE-319` | `CAPEC-158` | `T1040` | `D3-EAC` | PR.DS-02, PR.IR-01 | `PRIN-ENG-02: Defense in Depth` | 3 | 4 | 🔴 **Crit** (12) | `RN24` | 1 | 4 | 🟠 **Alto** (4) — Mitigado |
| 3 | `TM-D-06.1-001` | Repudiation of Profile Alteration | `R1.2` / `{U.C. 1.2}` | R | `CWE-778` | `CAPEC-81` | `T1070` | `D3-AL` | DE.CM-01, DE.CM-09, ID.AM-08, PR.DS-10 | `PRIN-ENG-07: Accountability` | 2 | 3 | 🟠 **Alto** (6) | `RN18`, `RN26` | 1 | 2 | 🟢 **Baixo** (2) — Mitigado |
| 4 | `TM-D-03.1-003` | Recovery Flow Abuse & Account Takeover | `R1.3` / `{U.C. 1.3}` | S, I | `CWE-640` | `CAPEC-50` | `T1110.003` | `D3-RO`, `D3-IRA` | PR.DS-01, PR.AA-01, PR.AA-05, PR.AA-06, DE.CM-01, DE.CM-09 | `PRIN-ENG-04: Fail-Safe Defaults` | 3 | 4 | 🔴 **Crit** (12) | `RN10`, `RN11`, `RN18` | 1 | 4 | 🟠 **Alto** (4) — Mitigado |
| 5 | `TM-D-03.3-001` | Unauthorized Member Privilege Escalation | `R2.2` / `{U.C. 2.2}` | E, T | `CWE-862` | `CAPEC-233` | `T1078.004` | `D3-AZ` | PR.AA-05, PR.AA-06 | `PRIN-ENG-01: Least Privilege` | 3 | 4 | 🔴 **Crit** (12) | `RN12` | 1 | 4 | 🟠 **Alto** (4) — Mitigado |
| 6 | `TM-D-03.4-001` | Insecure Default Configuration | `R2.1` / `{U.C. 2.1}` | E, I | `CWE-1188` | `CAPEC-203` | `T1565` | `D3-SPM` | PR.PS-01, PR.AA-05, PR.AA-06 | `PRIN-ENG-04: Fail-Safe Defaults` | 2 | 3 | 🟠 **Alto** (6) | `RN28`, `RN9` | 1 | 1 | 🟢 **Baixo** (1) — Mitigado |
| 7 | `TM-D-05.1-001` | Worker Telemetry Productivity Profiling (merged cross-lens) | `R2.3` / `{U.C. 2.3}` | L, I | `CWE-200` | `CAPEC-116` | `T1005` | `D3-DA` | GV.OC-03, PR.DS-10 | `PRIN-ENG-07: Purpose Limitation` | 3 | 3 | 🔴 **Crit** (9) | `RN22` | 1 | 1 | 🟢 **Baixo** (1) — Mitigado |
| 8 | `TM-D-05.1-002` | Audit Log Re-Identification | `R2.3`, `R6.1` / `{U.C. 2.3}`, `{U.C. 6.1}` | I | `CWE-200` | `CAPEC-116` | `T1005` | `D3-PSN` | DE.CM-01, DE.CM-09, GV.OC-03, PR.DS-10 | `PRIN-ENG-07: Data Minimization` | 2 | 2 | 🟡 **Méd** (4) | `RN18`, `RN22` | 1 | 1 | 🟢 **Baixo** (1) — Mitigado |
| 9 | `TM-D-03.2-001` | Cross-Tenant Project & Task Access (IDOR) | `R3.1`, `R4.1`, `R4.2` / `{U.C. 3.1}`, `{U.C. 4.1}`, `{U.C. 4.2}` | I | `CWE-639` | `CAPEC-122` | `T1567` | `D3-UAI`, `D3-MAM` | PR.AA-05, PR.AA-06 | `PRIN-ENG-06: Least Common Mechanism` | 3 | 4 | 🔴 **Crit** (12) | `RN9` | 1 | 4 | 🟠 **Alto** (4) — Mitigado |
| 10 | `TM-D-03.3-002` | Restricted Project Assignment Manipulation | `R3.1` / `{U.C. 3.1}` | E, T | `CWE-862` | `CAPEC-180` | `T1078` | `D3-AZ` | PR.AA-05, PR.AA-06, DE.CM-01, DE.CM-09 | `PRIN-ENG-03: Complete Mediation` | 2 | 3 | 🟠 **Alto** (6) | `RN12`, `RN18` | 1 | 2 | 🟢 **Baixo** (2) — Mitigado |
| 11 | `TM-D-03.4-003` | Recurrence Automation Abuse & Scheduler Exhaustion | `R4.3` / `{U.C. 4.3}` | D, T | `CWE-770` | `CAPEC-130` | `T1499` | `D3-RQL` | PR.AA-05, PR.AA-06, PR.PS-02, PR.PS-06, DE.CM-01, DE.CM-09 | `PRIN-ENG-04: Fail-Safe Defaults` | 2 | 3 | 🟠 **Alto** (6) | `RN9`, `RN17`, `RN18` | 1 | 1 | 🟢 **Baixo** (1) — Mitigado |
| 12 | `TM-D-01.4-001` | Malicious File Attachment Injection | `R5.1` / `{U.C. 5.1}` | T, E | `CWE-434` | `CAPEC-63` | `T1204.002` | `D3-FA` | PR.PS-06, PR.DS-10, ID.AM-03 | `PRIN-ENG-02: Defense in Depth` | 3 | 4 | 🔴 **Crit** (12) | `RN13`, `RN25` | 1 | 2 | 🟢 **Baixo** (2) — Mitigado |
| 13 | `TM-D-03.2-002` | Direct Object Storage Retrieval | `R5.1` / `{U.C. 5.1}` | I | `CWE-639` | `CAPEC-180` | `T1567` | `D3-EAA` | PR.PS-06 | `PRIN-ENG-03: Complete Mediation` | 3 | 4 | 🔴 **Crit** (12) | `RN13` | 1 | 4 | 🟠 **Alto** (4) — Mitigado |
| 14 | `TM-D-03.4-002` | Storage Exhaustion Denial of Service | `R5.1` / `{U.C. 5.1}` | D | `CWE-400` | `CAPEC-130` | `T1499` | `D3-RQL` | PR.PS-06, PR.DS-10, ID.AM-03 | `PRIN-ENG-04: Fail-Safe Defaults` | 3 | 3 | 🔴 **Crit** (9) | `RN13`, `RN25` | 1 | 1 | 🟢 **Baixo** (1) — Mitigado |
| 15 | `TM-D-01.4-002` | Stored XSS in Task Comments | `R5.2` / `{U.C. 5.2}` | T, I | `CWE-79` | `CAPEC-63` | `T1189` | `D3-OEN`, `D3-CSP` | PR.PS-06 | `PRIN-ENG-02: Defense in Depth` | 3 | 3 | 🔴 **Crit** (9) | `RN14` | 1 | 1 | 🟢 **Baixo** (1) — Mitigado |
| 16 | `TM-D-03.3-003` | Collaboration Record Tampering | `R5.2` / `{U.C. 5.2}` | T, R | `CWE-285` | `CAPEC-180` | `T1565.001` | `D3-MAM` | PR.PS-06, DE.CM-01, DE.CM-09 | `PRIN-ENG-01: Least Privilege` | 2 | 2 | 🟡 **Méd** (4) | `RN14`, `RN18` | 1 | 1 | 🟢 **Baixo** (1) — Mitigado |
| 17 | `TM-D-03.2-003` | Cross-Task Audit History Probing | `R6.1` / `{U.C. 6.1}` | I | `CWE-639` | `CAPEC-122` | `T1005` | `D3-UAI` | PR.AA-05, PR.AA-06, PR.PS-02, PR.PS-06, DE.CM-01, DE.CM-09 | `PRIN-ENG-03: Complete Mediation` | 2 | 3 | 🟠 **Alto** (6) | `RN9`, `RN17`, `RN18` | 1 | 2 | 🟢 **Baixo** (2) — Mitigado |
| 18 | `TM-D-07.1-002` | Cleartext Email Notification Leakage | `R6.2` / `{U.C. 6.2}` | I | `CWE-319` | `CAPEC-158` | `T1040` | `D3-EAC` | PR.DS-02, PR.IR-01 | `PRIN-ENG-02: Defense in Depth` | 2 | 3 | 🟠 **Alto** (6) | `RN24` | 1 | 1 | 🟢 **Baixo** (1) — Mitigado |
| 19 | `TM-D-01.4-003` | Payment Webhook Signature Forgery | `R7.1`, `R7.2` / `{U.C. 7.1}`, `{U.C. 7.2}` | S, T | `CWE-345` | `CAPEC-148` | `T1565.002` | `D3-MAM` | PR.DS-01, PR.DS-10, DE.CM-01, DE.CM-09 | `PRIN-ENG-02: Third-Party Isolation` | 3 | 3 | 🔴 **Crit** (9) | `RN16`, `RN15`, `RN18` | 1 | 1 | 🟢 **Baixo** (1) — Mitigado |
| 20 | `TM-D-03.3-004` | Malicious Subscription Manipulation | `R7.1` / `{U.C. 7.1}` | D, T | `CWE-862` | `CAPEC-180` | `T1078` | `D3-AZ`, `D3-AL` | PR.AA-05, PR.AA-06, DE.CM-01, DE.CM-09 | `PRIN-ENG-05: Separation of Duties` | 2 | 3 | 🟠 **Alto** (6) | `RN12`, `RN18` | 1 | 1 | 🟢 **Baixo** (1) — Mitigado |
| 21 | `TM-D-09.4-001` | Spoofed Subject Rights Data Export | `R8.1` / `{U.C. 8.1}` | S, I | `CWE-287` | `CAPEC-115` | `T1567` | `D3-IRA` | PR.AA-03, PR.AA-02, PR.DS-10, DE.CM-01, DE.CM-09 | `PRIN-ENG-03: Complete Mediation` | 3 | 4 | 🔴 **Crit** (12) | `RN27`, `RN20`, `RN18` | 1 | 4 | 🟠 **Alto** (4) — Mitigado |
| 22 | `TM-D-03.3-005` | Unauthorized Workspace Erasure | `R8.3` / `{U.C. 8.3}` | D, T | `CWE-285` | `CAPEC-180` | `T1485` | `D3-AZ`, `D3-FDS` | PR.AA-05, PR.AA-06, PR.AA-03, PR.AA-02, PR.DS-10, PR.DS-02 | `PRIN-ENG-01: Least Privilege` | 2 | 4 | 🔴 **Crit** (8) | `RN12`, `RN27`, `RN30` | 1 | 4 | 🟠 **Alto** (4) — Mitigado |
| 23 | `TM-D-03.1-002` | User Identity Enumeration | `R1.1`, `R1.3`, `R2.2` / `{U.C. 1.1}`, `{U.C. 1.3}`, `{U.C. 2.2}` | D | `CWE-200` | `CAPEC-115` | `T1589` | `D3-IRA` | PR.DS-01, PR.AA-01, PR.AA-05, DE.CM-01, DE.CM-09 | `PRIN-ENG-07: Data Minimization` | 3 | 2 | 🟠 **Alto** (6) | `RN10`, `RN18` | 1 | 1 | 🟢 **Baixo** (1) — Mitigado |
| 24 | `TM-D-07.1-003` | PII Exposure in Cleartext Email Alerts | `R6.2` / `{U.C. 6.2}` | D | `CWE-319` | `CAPEC-158` | `T1040` | `D3-OM`, `D3-EAC` | PR.DS-02, PR.IR-01 | `PRIN-ENG-07: Data Minimization` | 3 | 3 | 🔴 **Crit** (9) | `RN24` | 1 | 1 | 🟢 **Baixo** (1) — Mitigado |
| 25 | `TM-D-09.4-002` | Obstruction of Portability Rights | `R8.1` / `{U.C. 8.1}` | U | `CWE-285` | `CAPEC-115` | `T1499` | `D3-SPM` | PR.DS-10, PR.AA-03, PR.AA-02 | `PRIN-ENG-07: Transparency` | 2 | 3 | 🟠 **Alto** (6) | `RN20`, `RN27` | 1 | 1 | 🟢 **Baixo** (1) — Mitigado |
| 26 | `TM-D-05.2-002` | Sub-Processor Transparency Deficit | `R2.2`, `R7.1` / `{U.C. 2.2}`, `{U.C. 7.1}` | U, N | `CWE-1188` | `CAPEC-203` | `T1584` | `D3-OM` | PR.AT-01 | `PRIN-ENG-07: Transparency` | 2 | 2 | 🟡 **Méd** (4) | `RN29`, `RN7` | 1 | 1 | 🟢 **Baixo** (1) — Mitigado |
| 27 | `TM-D-05.2-001` | Excessive Comment Attribution | `R5.2`, `R8.2` / `{U.C. 5.2}`, `{U.C. 8.2}` | N | `CWE-200` | `CAPEC-116` | `T1005` | `D3-DA` | PR.DS-10, PR.PS-06 | `PRIN-ENG-07: Data Minimization` | 2 | 2 | 🟡 **Méd** (4) | `RN14`, `RN21` | 1 | 1 | 🟢 **Baixo** (1) — Mitigado |
| 28 | `TM-D-05.3-001` | Incomplete Lifecycle Erasure | `R8.2`, `R8.3` / `{U.C. 8.2}`, `{U.C. 8.3}` | N | `CWE-459` | `CAPEC-180` | `T1070` | `D3-FDS` | PR.DS-10, PR.AA-03, PR.AA-02, PR.DS-02 | `PRIN-ENG-04: Cryptographic Erasure` | 3 | 4 | 🔴 **Crit** (12) | `RN21`, `RN27`, `RN30` | 1 | 2 | 🟢 **Baixo** (2) — Mitigado |

---

## 3. Quantitative Risk Reduction Analysis

### 3.1 Aggregate Risk Reduction Quotient ($\Delta R$)
- Total Inherent Risk Score: $15 \times 4 (\text{Crit}) + 9 \times 3 (\text{High}) + 4 \times 2 (\text{Med}) = 60 + 27 + 8 = \mathbf{95 \text{ points}}$
- Total Residual Risk Score: $0 \times 4 (\text{Crit}) + 7 \times 3 (\text{High}) + 1 \times 2 (\text{Med}) + 20 \times 1 (\text{Low}) = 0 + 21 + 2 + 20 = \mathbf{43 \text{ points}}$
- **Empirical Risk Reduction Quotient:**
  $$\Delta R = 95 - 43 = \mathbf{52 \text{ points}} \quad (\mathbf{54.7\% \text{ absolute risk reduction at specification level}})$$

### 3.2 Impact Scoring Basis (Four-Dimension Max-Rule Audit)
Per template §4.3, each threat's Impact is the worst-case maximum across the four objective dimensions (Technical CIA-A, GDPR Statutory, CRA/Regulatory, Business). The audit over all 28 register rows confirms the **governing (maximum) dimension for every threat is recorded in its card's Impact justification**; in no row does a non-technical dimension exceed the scored maximum:
- GDPR-statutory dimension governs the privacy rows (`#7`, `#24`, `#25`, `#26`, `#27`, `#28`) and is co-governing with Technical on `#3` and `#21` (Art. 33 reportable-breach exposure).
- CRA/Regulatory dimension is co-governing on `#1`–`#4` and `#12` (Annex I secure-by-default and secure-processing obligations).
- Business/Financial dimension is co-governing on `#19` and `#20` (subscription fraud, churn).
- All remaining rows are governed by the Technical (CIA-A) dimension.
No score changes result from the audit; the maximum rule is satisfied as scored.

### 3.3 Formal Justification for the 7 High-Residual Risks
The seven threats remaining at **High residual risk** are:
1. `TM-D-07.1-001` (Cleartext Network Interception): Mitigated by mandatory transport cryptographic protection (`RN24`). Impact of a hypothetical cipher break remains Critical (4), but Likelihood is reduced to Low (1).
2. `TM-D-03.1-003` (Recovery Flow Abuse): Mitigated by neutral recovery responses, unguessable single-use tokens, and session invalidation (`RN10`, `RN11`). The residual channel is a compromised third-party mailbox; Likelihood is reduced to Low (1), Impact of a completed takeover remains Critical (4).
3. `TM-D-03.3-001` (Unauthorized Privilege Escalation): Mitigated by non-delegable Owner check (`RN12`). Impact of a hypothetical account takeover remains Critical (4), but Likelihood is reduced to Low (1).
4. `TM-D-03.2-001` (Cross-Tenant Project & Task Access): Mitigated by mandatory relational workspace predicate injection (`RN9`). Theoretical impact remains Critical (4), but Likelihood is reduced to Low (1).
5. `TM-D-03.2-002` (Direct Object Storage Retrieval): Mitigated by storage content isolation and application-mediated downloads (`RN13`). Theoretical impact remains Critical (4), but Likelihood is reduced to Low (1).
6. `TM-D-09.4-001` (Spoofed Subject Rights Export): Mitigated by requester identity re-verification (`RN27`). Potential PII exposure remains Critical (4), but Likelihood is reduced to Low (1).
7. `TM-D-03.3-005` (Unauthorized Workspace Erasure): Mitigated by Owner-only authorization, identity re-verification, and pending-erasure semantics (`RN12`, `RN27`, `RN30`). Impact of data erasure remains Critical (4), but Likelihood is reduced to Low (1).

**Verdict:** All seven High residuals are **formally accepted as fully mitigated** under mandatory, testable EARS constraints. None represents an unaddressed architectural vulnerability.

### 3.4 Part 2 to Part 1 Feedback Reconciliation Matrix (ADR-005 / ADR-009 D2)

In accordance with ADR-005 and ADR-009, threat modeling in Part 2 is not a terminal artifact but an active validation engine. The following matrix documents the closed-loop bidirectional traceability between identified threats, their inherent risk, the derived Part 1 mitigating specification elements (EARS constraints, derived functional cards, and Level-2 subfunction use cases), and the resulting verified residual risk:

| Threat ID | Threat Name | Inherent Risk | ADR-005 / ADR-009 Feedback Action | Part 1 Carrier (Req / UC Level 2) | Governing NFR / EARS | Residual Risk |
|---|---|---|---|---|---|---|
| `TM-D-03.1-001` | Credential Brute Force & Stuffing | 🔴 **Crit** (9) | Level-2 subfunction decomposition with progressive timing delay and lockout state machine | `{U.C. 1.1.1}` under `{U.C. 1.1}` | `RN10`, `RN11` | 🟡 **Médio** (3) — Mitigado |
| `TM-D-03.1-003` | Recovery Flow Abuse & Account Takeover | 🔴 **Crit** (12) | Derived functional requirement (D1) for locked account self-service recovery | `R1.3`, `{U.C. 1.3}` | `RN10`, `RN11`, `RN18` | 🟠 **Alto** (4) — Mitigado |
| `TM-D-01.4-001` | Malicious File Attachment Injection | 🔴 **Crit** (12) | Level-2 subfunction for magic-bytes verification, macro sanitization, and execution stripping | `{U.C. 5.1.1}` under `{U.C. 5.1}` | `RN13`, `RN25` | 🟢 **Baixo** (2) — Mitigado |
| `TM-D-03.2-002` | Direct Object Storage Retrieval | 🔴 **Crit** (12) | Enforce application-mediated storage tokenization and zero direct public URL generation | `R5.1`, `{U.C. 5.1.1}` | `RN13` | 🟠 **Alto** (4) — Mitigado |
| `TM-D-01.4-003` | Payment Webhook Signature Forgery | 🔴 **Crit** (9) | Level-2 subfunction for constant-time HMAC verification and replay window enforcement | `{U.C. 7.2.1}` under `{U.C. 7.2}` | `RN15`, `RN16` | 🟢 **Baixo** (1) — Mitigado |
| `TM-D-03.3-005` | Unauthorized Workspace Erasure | 🔴 **Crit** (8) | Level-2 subfunction for multi-tenant cryptographic key shredding and cascading disposal | `{U.C. 8.3.1}` under `{U.C. 8.3}` | `RN27`, `RN30` | 🟠 **Alto** (4) — Mitigado |
| `TM-D-05.3-001` | Incomplete Lifecycle Erasure | 🔴 **Crit** (12) | Derived requirement (D1) for permanent workspace deletion and signed disposal receipt | `R8.3`, `{U.C. 8.3.1}` | `RN21`, `RN30` | 🟢 **Baixo** (2) — Mitigado |

---

## 4. Part 2 Exit Gate Formal Certification (Gates G7–G12)

The Part 2 Exit Gate certifies that the specification has passed all quality, coverage, and adversarial validation criteria:

| Gate | Gate Title | Standard & Verification Evidence | Status |
|---|---|---|---|
| **G7** | **Trust Boundary Coverage** | 100% of interactions crossing $TB_{01}$–$TB_{05}$ across all 20 Cockburn Sea-Level Use Cases (`{U.C. 1.1}`..`{U.C. 8.3}`) are evaluated under STRIDE. Evidence: [`02_TECHNICAL_THREATS_STRIDE.md`](02_TECHNICAL_THREATS_STRIDE.md) §10. | **GREEN** |
| **G8** | **GDPR PII Flow Coverage** | 100% of personal data flows (`DF-COL`, `DF-PROC`, `DF-TRN`, `DF-SRA`, `DF-ERS`) are evaluated under all 7 LINDDUN categories. Evidence: [`03_PRIVACY_THREATS_LINDDUN.md`](03_PRIVACY_THREATS_LINDDUN.md) §4. | **GREEN** |
| **G9** | **MITRE Harmonization** | 100% of attack paths carry verified CAPEC, CWE, ATT&CK, and D3FEND cross-references; formal N/A justifications recorded for ATLAS and EMB3D. Evidence: [`04_ATTACK_VECTORS_AND_DEFENSE_TREES.md`](04_ATTACK_VECTORS_AND_DEFENSE_TREES.md) §5–§6. | **GREEN** |
| **G10** | **Risk Register Completeness** | 28/28 identified threats carry Inherent Risk, Residual Risk, Mitigating Constraints, published NIST CSF anchors, and explicit Treatment Verdicts; the ledger reconciles 1:1 with the 29 elicited cards under the declared cross-lens merge (§2.1). Evidence: Master Ledger Table §2. | **GREEN** |
| **G11** | **Residual Risk Policy Compliance** | **Zero Critical residuals** ($0.0\%$); all 7 High residuals formally justified and mitigated. Zero unrecorded risk acceptances. Evidence: Section §3. | **GREEN** |
| **G12** | **Mechanical & Document Hygiene** | `python scripts/check_traceability.py --case Case_01_TinyTask_SaaS` returns 0 findings (T1–T7, including Part 2 threat-ledger reconciliation); `python scripts/doc_lint.py --strict` returns 0 findings across all dossiers. | **GREEN** |

---

## 5. Certification Sign-Off

**FINAL PART 2 EXIT GATE VERDICT: GREEN — APPROVED & CONCLUDED.**

Phase 3 Part 2 (Threat & Risk Analysis) for Case 01 (TinyTask SaaS) is formally closed. The system specification is certified as:
1. **Regulatorily Traceable & Compliant** (GDPR + CRA, verified in Part 1).
2. **Adversarially Resilient & Control-Anchored** (STRIDE, LINDDUN, Attack Trees, MITRE D3FEND, NIST CSF anchors, verified in Part 2).
3. **Cleared for Handoff** to **AEGIS Phase 4 (Software Architecture, Verification & Implementation)**.
