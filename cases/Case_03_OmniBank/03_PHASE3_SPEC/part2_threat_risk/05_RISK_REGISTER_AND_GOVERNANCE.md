# AEGIS Phase 3 — Part 2: Step 5 — Consolidated Risk Register & Exit Gate Certification (OmniBank Financial Systems)

> **Case Study:** Case 03 — OmniBank Financial Systems S.A. (Consumer Banking with In-House High-Risk Credit-Scoring AI)  
> **Lifecycle Phase:** AEGIS Phase 3 — Specification, **Part 2 of 2 (Threat & Risk Analysis)**  
> **Step Deliverable:** Step 5 of 5 (`05_RISK_REGISTER_AND_GOVERNANCE.md`)  
> **Upstream Inputs:** Step 1 ([`01_SYSTEM_MODEL_ASSETS_AND_BOUNDARIES.md`](01_SYSTEM_MODEL_ASSETS_AND_BOUNDARIES.md)), Step 2 ([`02_TECHNICAL_THREATS_STRIDE.md`](02_TECHNICAL_THREATS_STRIDE.md)), Step 3 ([`03_PRIVACY_THREATS_LINDDUN.md`](03_PRIVACY_THREATS_LINDDUN.md)), Step 4 ([`04_ATTACK_VECTORS_AND_DEFENSE_TREES.md`](04_ATTACK_VECTORS_AND_DEFENSE_TREES.md))  
> **Methodological Standard:** [`../../../templates/phase3_threat_risk_guidelines.md`](../../../templates/phase3_threat_risk_guidelines.md) §6.5 & [`00_METHODOLOGY_AND_EXECUTION_GUIDE.md`](00_METHODOLOGY_AND_EXECUTION_GUIDE.md) §6.5  

---

## 1. Executive Summary & Cockpit Dashboard

This document provides the **authoritative risk governance ledger, executive visualization cockpit, and Exit Gate certification** consolidating 100% of the technical, AI, and privacy threats elicited across OmniBank Financial Systems under Phase 3 Part 2.

### 1.1 Executive KPI Cockpit (30-Second Overview)

| Metric | Inherent Value (Unconstrained) | Residual Value (Post-Mitigation) | Operational Delta ($\Delta$) | Governance Status |
|---|---|---|---|---|
| **Total Threats Elicited** | 36 consolidated threats (26 STRIDE + 10 LINDDUN, 0 cross-lens merges) | 36 register rows cataloged | 100% coverage | **COMPLETE** |
| **Critical Risk Threats (🔴)** | **18 threats (50.0%)** | **0 threats (0.0%)** | **-18 (-100.0%)** | 🟢 **ZERO-CRITICAL RULE MET** |
| **High Risk Threats (🟠)** | **15 threats (41.7%)** | **3 threats (8.3%)** | **-12 (-80.0%)** | 🟢 **FORMALLY MITIGATED & JUSTIFIED** |
| **Medium Risk Threats (🟡)** | **3 threats (8.3%)** | **10 threats (27.8%)** | **+7 (+233.3%)** | 🟢 **OPERATIONAL CONTROLS ACTIVE** |
| **Low Risk Threats (🟢)** | **0 threats (0.0%)** | **23 threats (63.9%)** | **+23 (+100.0%)** | 🟢 **BROADLY ACCEPTABLE POSTURE** |
| **Aggregate Risk Score Sum** | **123 points** (Avg 3.42 / threat) | **52 points** (Avg 1.44 / threat) | **-71 points (-57.7%)** | 🟢 **57.7% RISK REDUCTION QUOTIENT** |
| **Part 2 Exit Gate (G7–G12)** | Pending verification | **All 6 Gates GREEN** | Passed without exception | 🟢 **CLEARED FOR HANDOFF TO PHASE 4** |

---

### 1.2 Visual Risk Heatmap (Inherent vs. Residual Migration)

$$\text{Qualitative Risk Level} = \text{Likelihood (1: Low, 2: Med, 3: High)} \times \text{Impact (1: Low, 2: Med, 3: High, 4: Critical)}$$
$$\text{Color Scale: } \color{green}\blacksquare\text{ Baixo (1–2)} \quad \color{gold}\blacksquare\text{ Médio (3–4)} \quad \color{orange}\blacksquare\text{ Alto (6)} \quad \color{red}\blacksquare\text{ Crítico (8–12)}$$

#### A. Inherent Risk Matrix ($R_{\text{inh}}$ — Functional Surface Unconstrained)

| Likelihood \ Impact | Low Impact (1) | Medium Impact (2) | High Impact (3) | Critical Impact (4) |
|---|---|---|---|---|
| **High Likelihood (3)** | 🟢 0 Ameaças | 🟢 0 Ameaças | 🟢 0 Ameaças | 🔴 **2 Ameaças** (`#27`, `#35`) |
| **Med Likelihood (2)** | 🟢 0 Ameaças | 🟡 3 Ameaças (`#29`, `#30`, `#31`) | 🟠 15 Ameaças (`#1`, `#7`, `#9`, `#10`, `#13`, `#14`, `#16`, `#17`, `#19`, `#21`, `#26`, `#28`, `#32`, `#33`, `#34`) | 🔴 **16 Ameaças** (`#2`, `#3`, `#4`, `#5`, `#6`, `#8`, `#11`, `#12`, `#15`, `#18`, `#20`, `#22`, `#23`, `#24`, `#25`, `#36`) |
| **Low Likelihood (1)** | 🟢 0 Ameaças | 🟢 0 Ameaças | 🟢 0 Ameaças | 🔴 0 Ameaças |

> **Inherent Quadrant Verdict:** **18 Críticos (🔴)**, **15 Altos (🟠)**, **3 Médios (🟡)**, **0 Baixos (🟢)**.  
> *50% das ameaças residem no quadrante inaceitável de risco crítico — reflexo de cinco regimes regulamentares sobre um sistema financeiro crítico com IA de alto risco.*

---

#### B. Residual Risk Matrix ($R_{\text{res}}$ — Post-Mitigation via EARS Constraints `RN1`–`RN26`)

| Likelihood \ Impact | Low Impact (1) | Medium Impact (2) | High Impact (3) | Critical Impact (4) |
|---|---|---|---|---|
| **High Likelihood (3)** | 🟢 0 Ameaças | 🟡 0 Ameaças | 🟠 0 Ameaças | 🔴 **0 Ameaças** |
| **Med Likelihood (2)** | 🟢 0 Ameaças | 🟡 0 Ameaças | 🟠 0 Ameaças | 🔴 **0 Ameaças** |
| **Low Likelihood (1)** | 🟢 **3 Ameaças** (`#28`, `#29`, `#30`) | 🟢 **20 Ameaças** (`#1`, `#2`, `#7`, `#9`, `#10`, `#13`, `#14`, `#16`, `#17`, `#19`, `#20`, `#21`, `#26`, `#27`, `#31`, `#32`, `#33`, `#34`, `#35`, `#36`) | 🟡 **10 Ameaças** (`#3`, `#4`, `#8`, `#11`, `#12`, `#15`, `#18`, `#22`, `#24`, `#25`) | 🟠 **3 Ameaças** (`#5`, `#6`, `#23`) |

> **Residual Quadrant Verdict:** **0 Críticos (🔴 — 100% esvaziado)**, **3 Altos (🟠 — custo criptográfico latente sob custódia separada)**, **10 Médios (🟡)**, **23 Baixos (🟢)**.  
> *A massa crítica de risco foi deslocada 100% para os quadrantes de aceitabilidade operacional.*

---

### 1.3 Postura de Risco por Componente e Subsistema Arquitetural

| Subsistema / Componente | Papel Funcional no OmniBank | Ameaças Mapeadas | Risco Inerente Máximo | Risco Residual Máximo | Princípios de Segurança Ativos (Fase 2) | Requisitos Mitigadores (Fase 3 Part 1) |
|---|---|---|---|---|---|---|
| **P1: Banking Services & Credit Decisions** | Canais, OmniScore, revisão humana, versões | `#1`, `#2`, `#3`, `#4`, `#15`, `#22`, `#23`, `#25`, `#26`, `#27`, `#28`, `#29`, `#31`, `#33` | 🔴 **Crítico** (12) | 🟠 **Alto** (4, Mitigado) | `PRIN-ENG-01` (Least Privilege)<br>`PRIN-ENG-03` (Complete Mediation) | `RN6`, `RN11`, `RN12`, `RN13`, `RN19`, `RN22`, `RN23` |
| **P2: Cryptographic Protection** | Encriptação at-rest, trânsito, custódia de chaves | `#5`, `#6` | 🔴 **Crítico** (8) | 🟠 **Alto** (4, Mitigado) | `PRIN-ENG-01` (Least Privilege)<br>`PRIN-ENG-05` (Separation of Duties) | `RN13`, `RN14`, `RN15`, `RN17`, `RN19` |
| **P3: Vulnerabilities & Patches** | Avaliação, remediação, CVD, testing | `#7` | 🟠 **Alto** (6) | 🟢 **Baixo** (2) | `PRIN-ENG-04` (Fail-Safe Defaults) | `RN6`, `RN18` |
| **P4: Identities & Access** | Ciclo de vida, MFA privilegiada, reconciliação | `#8`, `#9`, `#10`, `#30` | 🔴 **Crítico** (8) | 🟡 **Médio** (3, Mitigado) | `PRIN-ENG-01` (Least Privilege)<br>`PRIN-ENG-04` (Fail-Safe Defaults) | `RN19`, `RN20`, `RN21` |
| **P5: Detect & Respond** | Monitorização, notificação multi-regime, DR, recuperação AI | `#11`, `#12`, `#13`, `#14`, `#32` | 🔴 **Crítico** (8) | 🟡 **Médio** (3, Mitigado) | `PRIN-ENG-07` (Accountability)<br>`PRIN-ENG-04` (Fail-Safe Defaults) | `RN4`, `RN6`, `RN11`, `RN13`, `RN18`, `RN19`, `RN21`, `RN24` |
| **P6: Data Lifecycle & Rights** | Retenção, pedidos de titulares, training-data | `#16`, `#27`, `#34`, `#35`, `#36` | 🔴 **Crítico** (12) | 🟢 **Baixo** (2) | `PRIN-ENG-07` (Storage Limitation)<br>`PRIN-ENG-06` (Data Minimization) | `RN12`, `RN15`, `RN16`, `RN17`, `RN21`, `RN24` |
| **P7: Vendors & Supply Chain** | Registo ICT, SBOM, contratos, exit | `#17` | 🟠 **Alto** (6) | 🟢 **Baixo** (2) | `PRIN-ENG-02` (Defense in Depth) | `RN19`, `RN26` |
| **P8: Develop & Release Securely** | Pipelines, mudanças de produção, pipeline AI | `#18`, `#24` | 🔴 **Crítico** (8) | 🟡 **Médio** (3, Mitigado) | `PRIN-ENG-04` (Fail-Safe Defaults)<br>`PRIN-ENG-02` (Defense in Depth) | `RN11`, `RN12`, `RN20`, `RN21`, `RN24` |
| **P10: Govern Security & AI Compliance** | Sistema unificado, relatórios regulatórios | `#19` | 🟠 **Alto** (6) | 🟢 **Baixo** (2) | `PRIN-ENG-07` (Accountability) | `RN6`, `RN13` |
| **P11: Test & Assure Continuously** | Audit logging imutável, robustez adversarial | `#20`, `#21` | 🔴 **Crítico** (8) | 🟢 **Baixo** (2) | `PRIN-ENG-07` (Accountability)<br>`PRIN-ENG-04` (Fail-Safe Defaults) | `RN6`, `RN17`, `RN22`, `RN23`, `RN24`, `RN25` |

---

## 2. Master Consolidated Risk Register (18-Column Enriched Ledger)

### 2.1 Cross-Lens Merge Record

The STRIDE and LINDDUN lenses share the canonical `TM-D-XX.Y-NNN` namespace. For Case 03, **no cross-lens merges were required**: every STRIDE card and LINDDUN card names a distinct real-world threat (verified pairwise during Step 3 — e.g., model *inversion* [STRIDE serving reconstruction] vs. applicant *re-identification from tokens* [LINDDUN record correlation] are distinct threats with distinct mitigations). The ledger reconciles as 26 + 10 − 0 = **36 rows**.

### 2.2 Master Ledger

The central register links every threat to its architectural design weakness (**CWE**), attack mechanism (**CAPEC**), operational adversary tactic (**MITRE ATT&CK** / **ATLAS**), defensive countermeasure (**MITRE D3FEND**), the **NIST CSF 2.0 anchors** published by its mitigating constraints in the accepted Part 1 baseline (`—` where the cited constraints are Table 7 quality rows without published anchors), the governing **Secure Design Principle (PRIN-ENG)**, and testable Part 1 EARS requirement (**RNxx**):

| # | Threat ID | Threat Title | Cards / UCs | Class. | MITRE CWE | MITRE CAPEC | MITRE ATT&CK | MITRE D3FEND | NIST CSF Anchors | Secure Design Principle (`PRIN-ENG`) | Inh. L | Inh. I | Inh. Risk | Mitigating Constraints | Res. L | Res. I | Res. Risk & Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `TM-D-01.2-001` | Customer Channel Interception | `R1.1` / `{U.C. 1.1}` | I, T | `CWE-319` | `CAPEC-94` | `T1557` | `D3-EAC` | PR.DS-02, PR.IR-01 | `PRIN-ENG-02: Defense in Depth` | 2 | 3 | 🟠 **Alto** (6) | `RN13` | 1 | 2 | 🟢 **Baixo** (2) — Mitigado |
| 2 | `TM-D-01.4-001` | Transaction & Decision Record Tampering | `R1.1`, `R1.2` / `{U.C. 1.1}`, `{U.C. 1.2}` | T, R | `CWE-354` | `CAPEC-180` | `T1565.001` | `D3-IV` | PR.DS-02, PR.IR-01 | `PRIN-ENG-07: Accountability` | 2 | 4 | 🔴 **Crit** (8) | `RN13`, `RN6` | 1 | 2 | 🟢 **Baixo** (2) — Mitigado |
| 3 | `TM-D-03.1-001` | OmniScore Decision Forgery at Serving | `R1.2` / `{U.C. 1.2}` | S, T | `CWE-345` | `CAPEC-148` | `T1565.001` | `D3-IV` | PR.DS-01, PR.DS-10, DE.AE-03, DE.CM-09, PR.PS-04 | `PRIN-ENG-03: Complete Mediation` | 2 | 4 | 🔴 **Crit** (8) | `RN11`, `RN23` | 1 | 3 | 🟡 **Médio** (3) — Mitigado |
| 4 | `TM-D-03.3-001` | Human Review Bypass & Explanation Falsification | `R1.3` / `{U.C. 1.3}` | E, T | `CWE-862` | `CAPEC-233` | `T1078.004` | `D3-AZ` | GV.RR-02, PR.AT-01, PR.AT-02, PR.AA-03, PR.AA-05, PR.AA-06, DE.AE-03, DE.CM-09, PR.PS-04 | `PRIN-ENG-05: Separation of Duties` | 2 | 4 | 🔴 **Crit** (8) | `RN22`, `RN19`, `RN23` | 1 | 3 | 🟡 **Médio** (3) — Mitigado |
| 5 | `TM-D-01.1-001` | Data-at-Rest Decryption via Key Compromise | `R2.1` / `{U.C. 2.1}` | I | `CWE-321` | `CAPEC-475` | `T1552.004` | `D3-DE` | PR.DS-01, PR.DS-10, PR.AA-05, PR.AA-03, PR.AA-06 | `PRIN-ENG-01: Least Privilege` | 2 | 4 | 🔴 **Crit** (8) | `RN14`, `RN15`, `RN19` | 1 | 4 | 🟠 **Alto** (4) — Mitigado |
| 6 | `TM-D-01.2-002` | Key Custody Violation & Lifecycle Evidence Falsification | `R2.3` / `{U.C. 2.3}` | I, T | `CWE-320` | `CAPEC-475` | `T1552.004` | `D3-AL` | PR.AA-05, PR.DS-01, ID.AM-08, PR.DS-10, PR.AA-03, PR.AA-06 | `PRIN-ENG-05: Separation of Duties` | 2 | 4 | 🔴 **Crit** (8) | `RN15`, `RN17`, `RN19` | 1 | 4 | 🟠 **Alto** (4) — Mitigado |
| 7 | `TM-D-02.1-001` | Vulnerability Remediation Circumvention | `R3.1`, `R3.2` / `{U.C. 3.1}`, `{U.C. 3.2}` | T, D | `CWE-778` | `CAPEC-180` | `T1562.001` | `D3-AL` | RS.CO-02, RS.MA-02, RS.MA-04 | `PRIN-ENG-04: Fail-Safe Defaults` | 2 | 3 | 🟠 **Alto** (6) | `RN18`, `RN6` | 1 | 2 | 🟢 **Baixo** (2) — Mitigado |
| 8 | `TM-D-03.1-002` | Privileged Access MFA Bypass | `R4.2` / `{U.C. 4.2}` | S | `CWE-308` | `CAPEC-115` | `T1110` | `D3-IRA` | PR.AA-03, PR.AA-05, PR.AA-06 | `PRIN-ENG-03: Complete Mediation` | 2 | 4 | 🔴 **Crit** (8) | `RN19` | 1 | 3 | 🟡 **Médio** (3) — Mitigado |
| 9 | `TM-D-03.3-002` | Entitlement Drift & Unreviewed Access | `R4.1`, `R4.3` / `{U.C. 4.1}`, `{U.C. 4.3}` | E | `CWE-269` | `CAPEC-233` | `T1098` | `D3-AZ` | PR.AA-03, PR.AA-05, PR.AA-06 | `PRIN-ENG-01: Least Privilege` | 2 | 3 | 🟠 **Alto** (6) | `RN19`, `RN21` | 1 | 2 | 🟢 **Baixo** (2) — Mitigado |
| 10 | `TM-D-03.4-002` | Configuration Hardening Bypass | `R4.4` / `{U.C. 4.4}` | E, T | `CWE-1188` | `CAPEC-180` | `T1562.001` | `D3-SC` | PR.AA-03, PR.AA-05, PR.AA-06, PR.PS-01 | `PRIN-ENG-04: Fail-Safe Defaults` | 2 | 3 | 🟠 **Alto** (6) | `RN19`, `RN20` | 1 | 2 | 🟢 **Baixo** (2) — Mitigado |
| 11 | `TM-D-10.1-001` | Security Event Suppression | `R5.1` / `{U.C. 5.1}` | T, R | `CWE-778` | `CAPEC-180` | `T1562.002` | `D3-AL` | PR.DS-02, PR.IR-01 | `PRIN-ENG-07: Accountability` | 2 | 4 | 🔴 **Crit** (8) | `RN13`, `RN6` | 1 | 3 | 🟡 **Médio** (3) — Mitigado |
| 12 | `TM-D-04.1-001` | Notification Clock Circumvention | `R5.2` / `{U.C. 5.2}` | T, D | `CWE-400` | `CAPEC-130` | `T1499` | `D3-MAM` | RS.CO-02, RS.MA-02, RS.MA-04, PR.DS-02, PR.IR-01, PR.AA-03, PR.AA-05, PR.AA-06 | `PRIN-ENG-07: Accountability` | 2 | 4 | 🔴 **Crit** (8) | `RN18`, `RN13`, `RN19` | 1 | 3 | 🟡 **Médio** (3) — Mitigado |
| 13 | `TM-D-04.4-001` | Backup & Disaster Recovery Sabotage | `R5.3` / `{U.C. 5.3}` | D, T | `CWE-400` | `CAPEC-130` | `T1490` | `D3-BR` | — | `PRIN-ENG-04: Fail-Safe Defaults` | 2 | 3 | 🟠 **Alto** (6) | `RN4` | 1 | 2 | 🟢 **Baixo** (2) — Mitigado |
| 14 | `TM-D-04.1-002` | AI Failure Investigation Evidence Tampering | `R5.4` / `{U.C. 5.4}` | T, R | `CWE-778` | `CAPEC-180` | `T1070` | `D3-AL` | PR.DS-01, PR.DS-10, PR.AA-05, DE.CM-09 | `PRIN-ENG-07: Accountability` | 2 | 3 | 🟠 **Alto** (6) | `RN11`, `RN21`, `RN24` | 1 | 2 | 🟢 **Baixo** (2) — Mitigado |
| 15 | `TM-D-03.2-001` | Cross-Estate Data Flow Breach | `R1.1`, `R5.1` / `{U.C. 1.1}`, `{U.C. 5.1}` | I | `CWE-639` | `CAPEC-122` | `T1567` | `D3-UAI` | PR.DS-02, PR.IR-01 | `PRIN-ENG-06: Least Common Mechanism` | 2 | 4 | 🔴 **Crit** (8) | `RN10`, `RN13` | 1 | 3 | 🟡 **Médio** (3) — Mitigado |
| 16 | `TM-D-01.4-002` | Retention Execution Tampering | `R6.2` / `{U.C. 6.2}` | T | `CWE-459` | `CAPEC-180` | `T1565.001` | `D3-FDS` | ID.AM-08, PR.DS-10 | `PRIN-ENG-07: Storage Limitation` | 2 | 3 | 🟠 **Alto** (6) | `RN17` | 1 | 1 | 🟢 **Baixo** (1) — Mitigado |
| 17 | `TM-D-06.1-001` | ICT Register & SBOM Falsification | `R7.1`, `R7.2` / `{U.C. 7.1}`, `{U.C. 7.2}` | T | `CWE-345` | `CAPEC-438` | `T1195.001` | `D3-SC` | PR.AA-03, PR.AA-05, PR.AA-06, GV.SC-02, GV.SC-03 | `PRIN-ENG-02: Defense in Depth` | 2 | 3 | 🟠 **Alto** (6) | `RN19`, `RN26` | 1 | 2 | 🟢 **Baixo** (2) — Mitigado |
| 18 | `TM-D-07.2-001` | Release Pipeline Security Bypass | `R8.2`, `R8.3` / `{U.C. 8.2}`, `{U.C. 8.3}` | E, T | `CWE-279` | `CAPEC-180` | `T1562.001` | `D3-SC` | PR.PS-01 | `PRIN-ENG-04: Fail-Safe Defaults` | 2 | 4 | 🔴 **Crit** (8) | `RN20` | 1 | 3 | 🟡 **Médio** (3) — Mitigado |
| 19 | `TM-D-09.3-001` | Regulatory Report Falsification | `R10.4` / `{U.C. 10.4}` | T, R | `CWE-345` | `CAPEC-148` | `T1565.001` | `D3-IV` | PR.DS-02, PR.IR-01 | `PRIN-ENG-07: Accountability` | 2 | 3 | 🟠 **Alto** (6) | `RN6`, `RN13` | 1 | 2 | 🟢 **Baixo** (2) — Mitigado |
| 20 | `TM-D-10.2-001` | Immutable Audit Trail Tampering | `R11.2` / `{U.C. 11.2}` | T, R | `CWE-778` | `CAPEC-180` | `T1070` | `D3-IV` | ID.AM-08, PR.DS-10, DE.AE-03, DE.CM-09, PR.PS-04 | `PRIN-ENG-07: Accountability` | 2 | 4 | 🔴 **Crit** (8) | `RN17`, `RN23`, `RN6` | 1 | 2 | 🟢 **Baixo** (2) — Mitigado |
| 21 | `TM-D-02.2-001` | AI Adversarial Robustness Assurance Bypass | `R11.4` / `{U.C. 11.4}` | T, R | `CWE-778` | `CAPEC-180` | `T1562.001` | `D3-AL` | GV.RR-02, PR.AT-01, PR.AT-02, DE.CM-09, ID.RA-04, PR.PS-06, RS.MI-01 | `PRIN-ENG-04: Fail-Safe Defaults` | 2 | 3 | 🟠 **Alto** (6) | `RN22`, `RN24`, `RN25` | 1 | 2 | 🟢 **Baixo** (2) — Mitigado |
| 22 | `TM-D-03.1-003` | AI Model Evasion at Serving | `R1.2` / `{U.C. 1.2}` | S (ATLAS) | `CWE-290` | `CAPEC-148` | `AML.T0044` | `D3-RQL` | PR.DS-01, PR.DS-10, DE.AE-03, DE.CM-09, PR.PS-04 | `PRIN-ENG-04: Fail-Safe Defaults` | 2 | 4 | 🔴 **Crit** (8) | `RN11`, `RN23` | 1 | 3 | 🟡 **Médio** (3) — Mitigado |
| 23 | `TM-D-01.1-002` | Model Inversion & Applicant Feature Reconstruction | `R1.2` / `{U.C. 1.2}` | I (ATLAS) | `CWE-200` | `CAPEC-116` | `AML.T0043` | `D3-RQL` | PR.DS-01, PR.DS-10, DE.AE-03, DE.CM-09, PR.PS-04, ID.AM-08 | `PRIN-ENG-01: Least Privilege` | 2 | 4 | 🔴 **Crit** (8) | `RN11`, `RN23`, `RN12` | 1 | 4 | 🟠 **Alto** (4) — Mitigado |
| 24 | `TM-D-06.2-002` | Training Data Poisoning | `R6.5`, `R8.4` / `{U.C. 6.5}`, `{U.C. 8.4}` | T (ATLAS) | `CWE-345` | `CAPEC-438` | `AML.T0024` | `D3-IV` | ID.AM-08, PR.AA-05, DE.CM-09, PR.DS-01, PR.DS-10 | `PRIN-ENG-02: Defense in Depth` | 2 | 4 | 🔴 **Crit** (8) | `RN12`, `RN21`, `RN24`, `RN11` | 1 | 3 | 🟡 **Médio** (3) — Mitigado |
| 25 | `TM-D-06.2-003` | AI Model Version Registry Tampering | `R1.4` / `{U.C. 1.4}` | T | `CWE-345` | `CAPEC-180` | `T1565.001` | `D3-IV` | PR.DS-01, PR.DS-10, PR.AA-05 | `PRIN-ENG-03: Complete Mediation` | 2 | 4 | 🔴 **Crit** (8) | `RN11`, `RN21` | 1 | 3 | 🟡 **Médio** (3) — Mitigado |
| 26 | `TM-D-01.2-003` | AI Model Artifact Exfiltration | `R1.4` / `{U.C. 1.4}` | I | `CWE-200` | `CAPEC-122` | `T1567` | `D3-AL` | PR.DS-01, PR.DS-10, PR.AA-05 | `PRIN-ENG-01: Least Privilege` | 2 | 3 | 🟠 **Alto** (6) | `RN11`, `RN21` | 1 | 2 | 🟢 **Baixo** (2) — Mitigado |
| 27 | `TM-D-05.1-001` | Applicant Profiling & Secondary Use of Scoring Data | `R1.2` / `{U.C. 1.2}` | L | `CWE-200` | `CAPEC-116` | `T1005` | `D3-PSN` | ID.AM-08 | `PRIN-ENG-07: Purpose Limitation` | 3 | 4 | 🔴 **Crit** (12) | `RN12`, `RN6` | 1 | 2 | 🟢 **Baixo** (2) — Mitigado |
| 28 | `TM-D-05.1-002` | Applicant Re-Identification from Token Records | `R1.2` / `{U.C. 1.2}` | I | `CWE-200` | `CAPEC-116` | `T1005` | `D3-PSN` | ID.AM-08 | `PRIN-ENG-06: Data Minimization` | 2 | 3 | 🟠 **Alto** (6) | `RN12`, `RN6` | 1 | 1 | 🟢 **Baixo** (1) — Mitigado |
| 29 | `TM-D-05.2-001` | Excessive Permanent Attribution in Human Review Records | `R1.3` / `{U.C. 1.3}` | N | `CWE-200` | `CAPEC-116` | `T1005` | `D3-PSN` | GV.RR-02, PR.AT-01, PR.AT-02, DE.AE-03, DE.CM-09, PR.PS-04 | `PRIN-ENG-07: Purpose Limitation` | 2 | 2 | 🟡 **Méd** (4) | `RN22`, `RN23` | 1 | 1 | 🟢 **Baixo** (1) — Mitigado |
| 30 | `TM-D-05.2-002` | Employee Monitoring via Access Reconciliation | `R4.1`, `R4.3` / `{U.C. 4.1}`, `{U.C. 4.3}` | N | `CWE-200` | `CAPEC-116` | `T1005` | `D3-MAM` | PR.AA-03, PR.AA-05, PR.AA-06 | `PRIN-ENG-07: Purpose Limitation` | 2 | 2 | 🟡 **Méd** (4) | `RN19`, `RN21` | 1 | 1 | 🟢 **Baixo** (1) — Mitigado |
| 31 | `TM-D-05.2-003` | Application Detectability via Decision-Endpoint Probing | `R1.2` / `{U.C. 1.2}` | D | `CWE-200` | `CAPEC-116` | `T1589` | `D3-RO` | ID.AM-08 | `PRIN-ENG-07: Data Minimization` | 2 | 2 | 🟡 **Méd** (4) | `RN12`, `RN6` | 1 | 1 | 🟢 **Baixo** (1) — Mitigado |
| 32 | `TM-D-07.1-001` | PII Over-Disclosure in Authority & Supervisory Submissions | `R5.2`, `R10.4` / `{U.C. 5.2}`, `{U.C. 10.4}` | D | `CWE-200` | `CAPEC-158` | `T1040` | `D3-OM` | RS.CO-02, RS.MA-02, RS.MA-04, PR.AA-03, PR.AA-05, PR.AA-06, PR.DS-02, PR.IR-01 | `PRIN-ENG-07: Data Minimization` | 2 | 3 | 🟠 **Alto** (6) | `RN18`, `RN19`, `RN13` | 1 | 2 | 🟢 **Baixo** (2) — Mitigado |
| 33 | `TM-D-05.2-004` | Unawareness of OmniScore Logic & Contested Decisions | `R1.2`, `R1.3` / `{U.C. 1.2}`, `{U.C. 1.3}` | U | `CWE-200` | `CAPEC-116` | `T1589` | `D3-AL` | GV.RR-02, PR.AT-01, PR.AT-02, DE.AE-03, DE.CM-09, PR.PS-04 | `PRIN-ENG-07: Transparency` | 2 | 3 | 🟠 **Alto** (6) | `RN22`, `RN23` | 1 | 2 | 🟢 **Baixo** (2) — Mitigado |
| 34 | `TM-D-09.4-002` | Obstruction of Erasure & Portability Against Statutory Floors | `R6.3`, `R6.4` / `{U.C. 6.3}`, `{U.C. 6.4}` | U | `CWE-285` | `CAPEC-115` | `T1499` | `D3-FDS` | PR.AA-02, PR.AA-03, PR.AA-05, PR.DS-01, ID.AM-08, PR.DS-10 | `PRIN-ENG-07: Transparency` | 2 | 3 | 🟠 **Alto** (6) | `RN16`, `RN15`, `RN17` | 1 | 1 | 🟢 **Baixo** (1) — Mitigado |
| 35 | `TM-D-05.3-001` | Retention Beyond Statutory Floors & Erasure Windows | `R6.2` / `{U.C. 6.2}` | N | `CWE-459` | `CAPEC-180` | `T1070` | `D3-FDS` | ID.AM-08, PR.DS-10 | `PRIN-ENG-07: Storage Limitation` | 3 | 4 | 🔴 **Crit** (12) | `RN17` | 1 | 1 | 🟢 **Baixo** (1) — Mitigado |
| 36 | `TM-D-05.3-002` | Training Data Residue & Purpose Drift | `R6.5` / `{U.C. 6.5}` | N | `CWE-345` | `CAPEC-438` | `T1195.001` | `D3-PSN` | ID.AM-08, PR.AA-05, DE.CM-09 | `PRIN-ENG-07: Purpose Limitation` | 2 | 4 | 🔴 **Crit** (8) | `RN12`, `RN21`, `RN24` | 1 | 2 | 🟢 **Baixo** (2) — Mitigado |

---

## 3. Quantitative Risk Reduction Analysis

### 3.1 Aggregate Risk Reduction Quotient ($\Delta R$)
- Total Inherent Risk Score: $18 \times 4 (\text{Crit}) + 15 \times 3 (\text{High}) + 3 \times 2 (\text{Med}) = 72 + 45 + 6 = \mathbf{123 \text{ points}}$
- Total Residual Risk Score: $0 \times 4 (\text{Crit}) + 3 \times 3 (\text{High}) + 10 \times 2 (\text{Med}) + 23 \times 1 (\text{Low}) = 0 + 9 + 20 + 23 = \mathbf{52 \text{ points}}$
- **Empirical Risk Reduction Quotient:**
  $$\Delta R = 123 - 52 = \mathbf{71 \text{ points}} \quad (\mathbf{57.7\% \text{ absolute risk reduction at specification level}})$$

### 3.2 Impact Scoring Basis (Four-Dimension Max-Rule Audit)
Per template §4.3, each threat's Impact is the worst-case maximum across Technical (CIA-A), GDPR Statutory, CRA/NIS 2/DORA/AI Act Regulatory, and Business dimensions. The audit over all 36 rows confirms the governing dimension is recorded in each card's Impact justification; the **regulatory dimension governs or co-governs 30 of 36 rows** — the highest regulatory dominance of the three cases, driven by DORA's critical-function classification, the AI Act Annex III duties, and GDPR Art. 22 automated-decision conditions. No score changes result from the audit; the maximum rule is satisfied as scored.

### 3.3 Formal Justification for the 3 High-Residual Risks
The three threats remaining at **High residual risk** are:
1. `TM-D-01.1-001` (Data-at-Rest Decryption): Mitigated by field-level protection and separated key custody (`RN14`, `RN15`, `RN19`). Impact of a hypothetical full custody compromise remains Critical (4), but Likelihood is reduced to Low (1).
2. `TM-D-01.2-002` (Key Custody Violation): Mitigated by custody separation, cryptographic destruction, and tamper-evident lifecycle records (`RN15`, `RN17`, `RN19`). Impact of unaccounted live keys remains Critical (4), but Likelihood is reduced to Low (1).
3. `TM-D-01.1-002` (Model Inversion): Mitigated by serving integrity, lifetime AI event logging, and purpose-bound minimized scoring data (`RN11`, `RN23`, `RN12`). Impact of population-scale feature reconstruction remains Critical (4), but Likelihood is reduced to Low (1).

**Verdict:** All three High residuals are **formally accepted as fully mitigated** under mandatory, testable EARS constraints. None represents an unaddressed architectural vulnerability; each residual is the latent impact of a hypothetical cryptographic or serving-platform compromise whose likelihood the cited constraints reduce to the floor.

---

## 4. Part 2 Exit Gate Formal Certification (Gates G7–G12)

| Gate | Gate Title | Standard & Verification Evidence | Status |
|---|---|---|---|
| **G7** | **Trust Boundary Coverage** | 100% of interactions crossing $TB_{01}$–$TB_{06}$ across all 43 Cockburn Sea-Level Use Cases (`{U.C. 1.1}`..`{U.C. 11.4}`) are evaluated under STRIDE (including the ATLAS AI lane). Evidence: [`02_TECHNICAL_THREATS_STRIDE.md`](02_TECHNICAL_THREATS_STRIDE.md) §13. | **GREEN** |
| **G8** | **GDPR PII Flow Coverage** | 100% of personal data flows (`DF-P1`–`DF-P8`) are evaluated under all 7 LINDDUN categories. Evidence: [`03_PRIVACY_THREATS_LINDDUN.md`](03_PRIVACY_THREATS_LINDDUN.md) §4. | **GREEN** |
| **G9** | **MITRE Harmonization** | 100% of attack paths carry verified CAPEC, CWE, ATT&CK/ATLAS, and D3FEND cross-references; the formal status of ATLAS (**ACTIVE**), EMB3D (**INACTIVE/N/A** with formal justification), and CAR (**ACTIVE** as audit analytics) is recorded with activation-boundary criteria. Evidence: [`04_ATTACK_VECTORS_AND_DEFENSE_TREES.md`](04_ATTACK_VECTORS_AND_DEFENSE_TREES.md) §7–§8. | **GREEN** |
| **G10** | **Risk Register Completeness** | 36/36 identified threats carry Inherent Risk, Residual Risk, Mitigating Constraints, published NIST CSF anchors (or recorded `—`), and explicit Treatment Verdicts; the ledger reconciles 1:1 with the 36 elicited cards (zero merges). Evidence: Master Ledger Table §2. | **GREEN** |
| **G11** | **Residual Risk Policy Compliance** | **Zero Critical residuals** ($0.0\%$); all 3 High residuals formally justified and mitigated. Zero unrecorded risk acceptances. Evidence: Section §3. | **GREEN** |
| **G12** | **Mechanical & Document Hygiene** | `python scripts/check_traceability.py --case Case_03_OmniBank` returns 0 findings (T1–T7, including Part 2 threat-ledger reconciliation); `python scripts/doc_lint.py --strict` returns 0 findings across all dossiers. | **GREEN** |

---

## 5. Certification Sign-Off

**FINAL PART 2 EXIT GATE VERDICT: GREEN — APPROVED & CONCLUDED.**

Phase 3 Part 2 (Threat & Risk Analysis) for Case 03 (OmniBank Financial Systems) is formally closed. The system specification is certified as:
1. **Regulatorily Traceable & Compliant** (GDPR + CRA + NIS 2 + DORA + AI Act, verified in Part 1).
2. **Adversarially Resilient & Control-Anchored** (STRIDE, LINDDUN, Attack Trees, MITRE D3FEND, ATLAS AI lane, NIST CSF anchors, verified in Part 2).
3. **Cleared for Handoff** to **AEGIS Phase 4 (Software Architecture, Verification & Implementation)**.
