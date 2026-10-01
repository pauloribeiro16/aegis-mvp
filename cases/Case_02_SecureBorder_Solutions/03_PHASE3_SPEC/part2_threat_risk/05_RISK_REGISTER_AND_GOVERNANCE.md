# AEGIS Phase 3 — Part 2: Step 5 — Consolidated Risk Register & Exit Gate Certification (SecureBorder eGate)

> **Case Study:** Case 02 — SecureBorder Solutions B.V. (Automated Border-Control Gates with On-Board Biometric Verification AI)  
> **Lifecycle Phase:** AEGIS Phase 3 — Specification, **Part 2 of 2 (Threat & Risk Analysis)**  
> **Step Deliverable:** Step 5 of 5 (`05_RISK_REGISTER_AND_GOVERNANCE.md`)  
> **Upstream Inputs:** Step 1 ([`01_SYSTEM_MODEL_ASSETS_AND_BOUNDARIES.md`](01_SYSTEM_MODEL_ASSETS_AND_BOUNDARIES.md)), Step 2 ([`02_TECHNICAL_THREATS_STRIDE.md`](02_TECHNICAL_THREATS_STRIDE.md)), Step 3 ([`03_PRIVACY_THREATS_LINDDUN.md`](03_PRIVACY_THREATS_LINDDUN.md)), Step 4 ([`04_ATTACK_VECTORS_AND_DEFENSE_TREES.md`](04_ATTACK_VECTORS_AND_DEFENSE_TREES.md))  
> **Methodological Standard:** [`../../../templates/phase3_threat_risk_guidelines.md`](../../../templates/phase3_threat_risk_guidelines.md) §6.5 & [`00_METHODOLOGY_AND_EXECUTION_GUIDE.md`](00_METHODOLOGY_AND_EXECUTION_GUIDE.md) §6.5  

---

## 1. Executive Summary & Cockpit Dashboard

This document provides the **authoritative risk governance ledger, executive visualization cockpit, and Exit Gate certification** consolidating 100% of the technical, AI, hardware, and privacy threats elicited across SecureBorder eGate under Phase 3 Part 2.

### 1.1 Executive KPI Cockpit (30-Second Overview)

| Metric | Inherent Value (Unconstrained) | Residual Value (Post-Mitigation) | Operational Delta ($\Delta$) | Governance Status |
|---|---|---|---|---|
| **Total Threats Elicited** | 33 consolidated threats (23 STRIDE + 10 LINDDUN, 0 cross-lens merges) | 33 register rows cataloged | 100% coverage | **COMPLETE** |
| **Critical Risk Threats (🔴)** | **23 threats (69.7%)** | **0 threats (0.0%)** | **-23 (-100.0%)** | 🟢 **ZERO-CRITICAL RULE MET** |
| **High Risk Threats (🟠)** | **7 threats (21.2%)** | **7 threats (21.2%)** | **0 (0.0%)** | 🟢 **FORMALLY MITIGATED & JUSTIFIED** |
| **Medium Risk Threats (🟡)** | **3 threats (9.1%)** | **12 threats (36.4%)** | **+9 (+300.0%)** | 🟢 **OPERATIONAL CONTROLS ACTIVE** |
| **Low Risk Threats (🟢)** | **0 threats (0.0%)** | **14 threats (42.4%)** | **+14 (+100.0%)** | 🟢 **BROADLY ACCEPTABLE POSTURE** |
| **Aggregate Risk Score Sum** | **119 points** (Avg 3.61 / threat) | **59 points** (Avg 1.79 / threat) | **-60 points (-50.4%)** | 🟢 **50.4% RISK REDUCTION QUOTIENT** |
| **Part 2 Exit Gate (G7–G12)** | Pending verification | **All 6 Gates GREEN** | Passed without exception | 🟢 **CLEARED FOR HANDOFF TO PHASE 4** |

---

### 1.2 Visual Risk Heatmap (Inherent vs. Residual Migration)

$$\text{Qualitative Risk Level} = \text{Likelihood (1: Low, 2: Med, 3: High)} \times \text{Impact (1: Low, 2: Med, 3: High, 4: Critical)}$$
$$\text{Color Scale: } \color{green}\blacksquare\text{ Baixo (1–2)} \quad \color{gold}\blacksquare\text{ Médio (3–4)} \quad \color{orange}\blacksquare\text{ Alto (6)} \quad \color{red}\blacksquare\text{ Crítico (8–12)}$$

#### A. Inherent Risk Matrix ($R_{\text{inh}}$ — Functional Surface Unconstrained)

| Likelihood \ Impact | Low Impact (1) | Medium Impact (2) | High Impact (3) | Critical Impact (4) |
|---|---|---|---|---|
| **High Likelihood (3)** | 🟢 0 Ameaças | 🟢 0 Ameaças | 🟢 0 Ameaças | 🔴 **6 Ameaças** (`#1`, `#7`, `#10`, `#24`, `#25`, `#31`) |
| **Med Likelihood (2)** | 🟢 0 Ameaças | 🟡 3 Ameaças (`#26`, `#27`, `#33`) | 🟠 7 Ameaças (`#13`, `#14`, `#17`, `#21`, `#28`, `#29`, `#30`) | 🔴 **17 Ameaças** (`#2`, `#3`, `#4`, `#5`, `#6`, `#8`, `#9`, `#11`, `#12`, `#15`, `#16`, `#18`, `#19`, `#20`, `#22`, `#23`, `#32`) |
| **Low Likelihood (1)** | 🟢 0 Ameaças | 🟢 0 Ameaças | 🟢 0 Ameaças | 🔴 0 Ameaças |

> **Inherent Quadrant Verdict:** **23 Críticos (🔴)**, **7 Altos (🟠)**, **3 Médios (🟡)**, **0 Baixos (🟢)**.  
> *70% das ameaças residem no quadrante inaceitável de risco crítico — reflexo da classe de produto (fronteira crítica + IA de alto risco + hardware CRA).*

---

#### B. Residual Risk Matrix ($R_{\text{res}}$ — Post-Mitigation via EARS Constraints `RN1`–`RN30`)

| Likelihood \ Impact | Low Impact (1) | Medium Impact (2) | High Impact (3) | Critical Impact (4) |
|---|---|---|---|---|
| **High Likelihood (3)** | 🟢 0 Ameaças | 🟡 0 Ameaças | 🟠 0 Ameaças | 🔴 **0 Ameaças** |
| **Med Likelihood (2)** | 🟢 0 Ameaças | 🟡 0 Ameaças | 🟠 0 Ameaças | 🔴 **0 Ameaças** |
| **Low Likelihood (1)** | 🟢 **6 Ameaças** (`#26`, `#27`, `#29`, `#30`, `#31`, `#33`) | 🟢 **8 Ameaças** (`#3`, `#13`, `#14`, `#17`, `#21`, `#24`, `#28`, `#32`) | 🟡 **12 Ameaças** (`#4`, `#6`, `#7`, `#8`, `#11`, `#12`, `#16`, `#18`, `#19`, `#22`, `#23`, `#25`) | 🟠 **7 Ameaças** (`#1`, `#2`, `#5`, `#9`, `#10`, `#15`, `#20`) |

> **Residual Quadrant Verdict:** **0 Críticos (🔴 — 100% esvaziado)**, **7 Altos (🟠 — impacto latente sob limites verificados)**, **12 Médios (🟡)**, **14 Baixos (🟢)**.  
> *A massa crítica de risco foi deslocada 100% para os quadrantes de aceitabilidade operacional.*

---

### 1.3 Postura de Risco por Componente e Subsistema Arquitetural

| Subsistema / Componente | Papel Funcional no SecureBorder | Ameaças Mapeadas | Risco Inerente Máximo | Risco Residual Máximo | Princípios de Segurança Ativos (Fase 2) | Requisitos Mitigadores (Fase 3 Part 1) |
|---|---|---|---|---|---|---|
| **P1: Biometric Verification & Gate** | Captação, decisão de passagem, consultas | `#1`, `#2`, `#3`, `#4`, `#5`, `#20`, `#21`, `#23`, `#24`, `#25`, `#27`, `#31` | 🔴 **Crítico** (12) | 🟠 **Alto** (4, Mitigado) | `PRIN-ENG-01` (Least Privilege)<br>`PRIN-ENG-04` (Fail-Safe Defaults) | `RN5`, `RN6`, `RN10`, `RN11`, `RN12`, `RN13`, `RN14`, `RN15`, `RN20`, `RN22`, `RN24` |
| **P2: Human Oversight & Gate Control** | Revisão, override, referral manual | `#6`, `#7`, `#26` | 🔴 **Crítico** (12) | 🟡 **Médio** (3, Mitigado) | `PRIN-ENG-01` (Least Privilege)<br>`PRIN-ENG-03` (Complete Mediation) | `RN18`, `RN19`, `RN29` |
| **P3: Operator Identity & Access** | Ciclo de vida, MFA, papéis | `#8`, `#9`, `#33` | 🔴 **Crítico** (8) | 🟠 **Alto** (4, Mitigado) | `PRIN-ENG-01` (Least Privilege)<br>`PRIN-ENG-03` (Complete Mediation) | `RN10`, `RN17`, `RN18`, `RN19` |
| **P4: Traveller Data Rights** | Pedidos de titulares, RoPA | `#10`, `#29`, `#30`, `#32` | 🔴 **Crítico** (12) | 🟠 **Alto** (4, Mitigado) | `PRIN-ENG-03` (Complete Mediation)<br>`PRIN-ENG-07` (Transparency) | `RN10`, `RN16`, `RN28` |
| **P5: Security Monitoring & Incidents** | Eventos de frota, triagem, continuidade | `#11`, `#12`, `#13` | 🔴 **Crítico** (8) | 🟡 **Médio** (3, Mitigado) | `PRIN-ENG-07` (Accountability)<br>`PRIN-ENG-04` (Fail-Safe Defaults) | `RN4`, `RN14`, `RN21`, `RN22`, `RN23`, `RN25`, `RN26` |
| **P6: Regulatory Notifications** | Notificação unificada multi-regime | `#12`, `#14`, `#28` | 🔴 **Crítico** (8) | 🟢 **Baixo** (2) | `PRIN-ENG-02` (Third-Party Isolation)<br>`PRIN-ENG-07` (Data Minimization) | `RN9`, `RN14`, `RN21`, `RN26` |
| **P7/P8: Updates, Releases & Supply Chain** | Canal de atualização, gates, SBOM, registry | `#15`, `#16`, `#17`, `#18`, `#19` | 🔴 **Crítico** (8) | 🟡 **Médio** (3, Mitigado) | `PRIN-ENG-02` (Defense in Depth)<br>`PRIN-ENG-04` (Fail-Safe Defaults) | `RN9`, `RN10`, `RN12`, `RN15`, `RN20`, `RN24`, `RN25`, `RN27` |
| **P9: AI Quality & Conformity (ATLAS Lane)** | Precisão, drift, adversarial, explicabilidade | `#19`, `#20`, `#22`, `#23` | 🔴 **Crítico** (8) | 🟠 **Alto** (4, Mitigado) | `PRIN-ENG-01` (Least Privilege)<br>`PRIN-ENG-02` (Defense in Depth) | `RN7`, `RN11`, `RN15`, `RN20`, `RN24`, `RN25` |

---

## 2. Master Consolidated Risk Register (18-Column Enriched Ledger)

### 2.1 Cross-Lens Merge Record

The STRIDE and LINDDUN lenses share the canonical `TM-D-XX.Y-NNN` namespace. For Case 02, **no cross-lens merges were required**: every STRIDE card and LINDDUN card names a distinct real-world threat (verified pairwise during Step 3 — e.g., template *theft* [STRIDE exfiltration] vs. biometric *re-identification* [LINDDUN correlation] are distinct threats with distinct mitigations). The ledger reconciles as 23 + 10 − 0 = **33 rows**.

### 2.2 Master Ledger

The central register links every threat to its architectural design weakness (**CWE**), attack mechanism (**CAPEC**), operational adversary tactic (**MITRE ATT&CK** / **ATLAS**), defensive countermeasure (**MITRE D3FEND**), the **NIST CSF 2.0 anchors** published by its mitigating constraints in the accepted Part 1 baseline (`—` where the cited constraints are Table 7 quality rows without published anchors), the governing **Secure Design Principle (PRIN-ENG)**, and testable Part 1 EARS requirement (**RNxx**):

| # | Threat ID | Threat Title | Cards / UCs | Class. | MITRE CWE | MITRE CAPEC | MITRE ATT&CK | MITRE D3FEND | NIST CSF Anchors | Secure Design Principle (`PRIN-ENG`) | Inh. L | Inh. I | Inh. Risk | Mitigating Constraints | Res. L | Res. I | Res. Risk & Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `TM-D-03.1-001` | Traveller Identity Spoofing via Presentation Attacks & AI Evasion | `R1.2` / `{U.C. 1.2}` | S (ATLAS) | `CWE-290` | `CAPEC-115` | `T1036` / `AML.T0044` | `D3-IRA` | PR.DS-11, PR.IR-03, PR.IR-04, DE.CM-01, DE.CM-09, PR.PS-04 | `PRIN-ENG-04: Fail-Safe Defaults` | 3 | 4 | 🔴 **Crit** (12) | `RN15`, `RN22`, `RN24` | 1 | 4 | 🟠 **Alto** (4) — Mitigado |
| 2 | `TM-D-01.1-001` | Biometric Template Theft at Rest | `R1.1` / `{U.C. 1.1}` | I | `CWE-312` | `CAPEC-122` | `T1005` | `D3-DE` | PR.DS-01, PR.DS-10, PR.AA-05 | `PRIN-ENG-01: Least Privilege` | 2 | 4 | 🔴 **Crit** (8) | `RN11`, `RN12`, `RN10` | 1 | 4 | 🟠 **Alto** (4) — Mitigado |
| 3 | `TM-D-01.4-001` | Decision Record & RoPA Tampering | `R1.3`, `R4.2` / `{U.C. 1.3}`, `{U.C. 4.2}` | T, R | `CWE-354` | `CAPEC-180` | `T1565.001` | `D3-IV` | PR.DS-01, PR.DS-10, PR.PS-04 | `PRIN-ENG-07: Accountability` | 2 | 4 | 🔴 **Crit** (8) | `RN14`, `RN6` | 1 | 2 | 🟢 **Baixo** (2) — Mitigado |
| 4 | `TM-D-01.2-001` | Gate–Back-Office Channel Interception | `R1.2` / `{U.C. 1.2}` | I, T | `CWE-319` | `CAPEC-94` | `T1557` | `D3-EAC` | PR.DS-02, PR.IR-01 | `PRIN-ENG-02: Defense in Depth` | 2 | 4 | 🔴 **Crit** (8) | `RN13` | 1 | 3 | 🟡 **Médio** (3) — Mitigado |
| 5 | `TM-D-03.2-001` | Cross-Country Decision Record Access (IDOR) | `R1.3` / `{U.C. 1.3}` | I | `CWE-639` | `CAPEC-122` | `T1530` | `D3-UAI` | PR.DS-01, PR.DS-10, PR.PS-04 | `PRIN-ENG-06: Least Common Mechanism` | 2 | 4 | 🔴 **Crit** (8) | `RN10`, `RN14`, `RN11` | 1 | 4 | 🟠 **Alto** (4) — Mitigado |
| 6 | `TM-D-03.3-001` | Human Oversight Override Bypass | `R2.1` / `{U.C. 2.1}` | E, T | `CWE-862` | `CAPEC-233` | `T1078.004` | `D3-AZ` | PR.AA-05, PR.AA-06, GV.RR-02, PR.AT-01, PR.AT-02 | `PRIN-ENG-01: Least Privilege` | 2 | 4 | 🔴 **Crit** (8) | `RN19`, `RN29` | 1 | 3 | 🟡 **Médio** (3) — Mitigado |
| 7 | `TM-D-03.1-002` | Manual-Lane Impersonation & Collusion | `R2.2` / `{U.C. 2.2}` | S | `CWE-288` | `CAPEC-115` | `T1036` | `D3-IRA` | PR.AA-03, PR.AA-05, PR.AA-06 | `PRIN-ENG-04: Fail-Safe Defaults` | 3 | 4 | 🔴 **Crit** (12) | `RN18` | 1 | 3 | 🟡 **Médio** (3) — Mitigado |
| 8 | `TM-D-03.1-003` | Operator Credential Compromise & MFA Bypass | `R3.2` / `{U.C. 3.2}` | S | `CWE-308` | `CAPEC-115` | `T1110` | `D3-IRA` | PR.AA-03, PR.AA-05, PR.AA-06 | `PRIN-ENG-03: Complete Mediation` | 2 | 4 | 🔴 **Crit** (8) | `RN18` | 1 | 3 | 🟡 **Médio** (3) — Mitigado |
| 9 | `TM-D-03.3-002` | Operator Role Escalation & Cross-Country Reach | `R3.3` / `{U.C. 3.3}` | E, I | `CWE-269` | `CAPEC-233` | `T1098` | `D3-AZ` | PR.AA-01, PR.AA-05, PR.AA-06 | `PRIN-ENG-01: Least Privilege` | 2 | 4 | 🔴 **Crit** (8) | `RN17`, `RN19`, `RN10` | 1 | 4 | 🟠 **Alto** (4) — Mitigado |
| 10 | `TM-D-09.4-001` | Spoofed Traveller Rights Request | `R4.1` / `{U.C. 4.1}` | S, I | `CWE-287` | `CAPEC-115` | `T1567` | `D3-IRA` | PR.AA-02, PR.AA-03, ID.AM-08, PR.DS-10 | `PRIN-ENG-03: Complete Mediation` | 3 | 4 | 🔴 **Crit** (12) | `RN16`, `RN28` | 1 | 4 | 🟠 **Alto** (4) — Mitigado |
| 11 | `TM-D-10.1-001` | Fleet Security Event Suppression & Tampering | `R5.1` / `{U.C. 5.1}` | T, R | `CWE-778` | `CAPEC-180` | `T1562.002` | `D3-AL` | DE.CM-01, DE.CM-09, ID.IM-04 | `PRIN-ENG-07: Accountability` | 2 | 4 | 🔴 **Crit** (8) | `RN22`, `RN25` | 1 | 3 | 🟡 **Médio** (3) — Mitigado |
| 12 | `TM-D-04.1-001` | Incident Containment & Notification Clock Circumvention | `R5.2`, `R6.1` / `{U.C. 5.2}`, `{U.C. 6.1}` | T, D | `CWE-446` | `CAPEC-180` | `T1562.001` | `D3-MAM` | RS.AN-03, RS.MA-01, DE.CM-01, RS.MA-02, RS.MI-01, RS.CO-02, RS.MA-04, PR.DS-01, PR.DS-10, PR.PS-04 | `PRIN-ENG-07: Accountability` | 2 | 4 | 🔴 **Crit** (8) | `RN23`, `RN26`, `RN21`, `RN14` | 1 | 3 | 🟡 **Médio** (3) — Mitigado |
| 13 | `TM-D-04.4-001` | Backup & Recovery Sabotage | `R5.3` / `{U.C. 5.3}` | D, T | `CWE-400` | `CAPEC-130` | `T1490` | `D3-BR` | RS.AN-03, RS.MA-01 | `PRIN-ENG-04: Fail-Safe Defaults` | 2 | 3 | 🟠 **Alto** (6) | `RN23`, `RN4` | 1 | 2 | 🟢 **Baixo** (2) — Mitigado |
| 14 | `TM-D-01.4-002` | Forged Regulatory Notification Injection | `R6.1` / `{U.C. 6.1}` | S, T | `CWE-345` | `CAPEC-148` | `T1565.001` | `D3-IRA` | PR.DS-01, PR.DS-10, PR.PS-04, RS.CO-02, RS.MA-02, RS.MA-04 | `PRIN-ENG-02: Third-Party Isolation` | 2 | 3 | 🟠 **Alto** (6) | `RN14`, `RN9`, `RN21` | 1 | 2 | 🟢 **Baixo** (2) — Mitigado |
| 15 | `TM-D-06.1-001` | Malicious Update Injection into the Gate Fleet | `R7.2` / `{U.C. 7.2}` | T, E | `CWE-494` | `CAPEC-184` | `T1195.002` | `D3-SI` | GV.SC-03, ID.AM-02 | `PRIN-ENG-02: Defense in Depth` | 2 | 4 | 🔴 **Crit** (8) | `RN27`, `RN9`, `RN10` | 1 | 4 | 🟠 **Alto** (4) — Mitigado |
| 16 | `TM-D-07.2-001` | Release Pipeline Security Gate Bypass | `R8.1` / `{U.C. 8.1}` | E, T | `CWE-279` | `CAPEC-180` | `T1562.001` | `D3-SC` | PR.PS-01 | `PRIN-ENG-04: Fail-Safe Defaults` | 2 | 4 | 🔴 **Crit** (8) | `RN20` | 1 | 3 | 🟡 **Médio** (3) — Mitigado |
| 17 | `TM-D-06.2-001` | SBOM & Component Provenance Falsification | `R8.1`, `R8.2`, `R10.2` / `{U.C. 8.1}`, `{U.C. 8.2}`, `{U.C. 10.2}` | T | `CWE-1357` | `CAPEC-438` | `T1195.001` | `D3-SC` | PR.PS-01 | `PRIN-ENG-02: Defense in Depth` | 2 | 3 | 🟠 **Alto** (6) | `RN20` | 1 | 2 | 🟢 **Baixo** (2) — Mitigado |
| 18 | `TM-D-06.2-002` | AI Model Registry & Rollback Tampering | `R8.3` / `{U.C. 8.3}` | T | `CWE-345` | `CAPEC-180` | `T1565.001` | `D3-IV` | PR.DS-11, PR.IR-03, PR.IR-04 | `PRIN-ENG-03: Complete Mediation` | 2 | 4 | 🔴 **Crit** (8) | `RN15`, `RN10` | 1 | 3 | 🟡 **Médio** (3) — Mitigado |
| 19 | `TM-D-06.2-003` | Training Data Poisoning of the Verification Model | `R8.3`, `R9.2` / `{U.C. 8.3}`, `{U.C. 9.2}` | T (ATLAS) | `CWE-345` | `CAPEC-438` | `T1195.001` / `AML.T0024` | `D3-IV` | PR.DS-11, PR.IR-03, PR.IR-04, DE.AE-03, DE.CM-09, PR.PS-04, ID.IM-04 | `PRIN-ENG-02: Defense in Depth` | 2 | 4 | 🔴 **Crit** (8) | `RN15`, `RN24`, `RN25` | 1 | 3 | 🟡 **Médio** (3) — Mitigado |
| 20 | `TM-D-01.1-002` | Model Inversion & Biometric Reconstruction | `R1.2`, `R1.3` / `{U.C. 1.2}`, `{U.C. 1.3}` | I (ATLAS) | `CWE-200` | `CAPEC-116` | `T1005` / `AML.T0043` | `D3-RQL` | PR.DS-11, PR.IR-03, PR.IR-04, DE.AE-03, DE.CM-09, PR.PS-04, PR.DS-01, PR.DS-10 | `PRIN-ENG-01: Least Privilege` | 2 | 4 | 🔴 **Crit** (8) | `RN15`, `RN24`, `RN11` | 1 | 4 | 🟠 **Alto** (4) — Mitigado |
| 21 | `TM-D-01.2-002` | AI Model Artifact Exfiltration | `R1.2` / `{U.C. 1.2}` | I | `CWE-200` | `CAPEC-122` | `T1567` | `D3-EAC` | PR.DS-02, PR.IR-01, DE.AE-03, DE.CM-09, PR.PS-04 | `PRIN-ENG-01: Least Privilege` | 2 | 3 | 🟠 **Alto** (6) | `RN13`, `RN24` | 1 | 2 | 🟢 **Baixo** (2) — Mitigado |
| 22 | `TM-D-10.1-002` | AI Monitoring & Accuracy Concealment | `R9.2` / `{U.C. 9.2}` | T, R | `CWE-778` | `CAPEC-180` | `T1562.002` | `D3-AL` | DE.AE-03, DE.CM-09, PR.PS-04, ID.IM-04 | `PRIN-ENG-07: Accountability` | 2 | 4 | 🔴 **Crit** (8) | `RN7`, `RN24`, `RN25` | 1 | 3 | 🟡 **Médio** (3) — Mitigado |
| 23 | `TM-D-03.4-002` | AI Fail-Safe Bypass to Fail-Open | `R1.2` / `{U.C. 1.2}` | E, T | `CWE-1188` | `CAPEC-180` | `T1565.001` | `D3-SC` | PR.DS-11, PR.IR-03, PR.IR-04, PR.PS-01 | `PRIN-ENG-04: Fail-Safe Defaults` | 2 | 4 | 🔴 **Crit** (8) | `RN15`, `RN20` | 1 | 3 | 🟡 **Médio** (3) — Mitigado |
| 24 | `TM-D-05.1-001` | Traveller Movement Linkability via Passage Records | `R1.2`, `R1.3` / `{U.C. 1.2}`, `{U.C. 1.3}` | L | `CWE-200` | `CAPEC-116` | `T1005` | `D3-PSN` | — | `PRIN-ENG-07: Purpose Limitation` | 3 | 4 | 🔴 **Crit** (12) | `RN6`, `RN10` | 1 | 2 | 🟢 **Baixo** (2) — Mitigado |
| 25 | `TM-D-05.1-002` | Biometric Re-Identification from Pseudonymized Stores | `R1.1`, `R1.2` / `{U.C. 1.1}`, `{U.C. 1.2}` | I | `CWE-200` | `CAPEC-116` | `T1005` | `D3-DE` | PR.DS-01, PR.DS-10, PR.AA-05 | `PRIN-ENG-06: Data Minimization` | 3 | 4 | 🔴 **Crit** (12) | `RN11`, `RN12`, `RN5` | 1 | 3 | 🟡 **Médio** (3) — Mitigado |
| 26 | `TM-D-05.2-001` | Excessive Permanent Attribution of Oversight Actions | `R2.1`, `R2.2` / `{U.C. 2.1}`, `{U.C. 2.2}` | N | `CWE-200` | `CAPEC-116` | `T1005` | `D3-PSN` | GV.RR-02, PR.AT-01, PR.AT-02, PR.AA-05, PR.AA-06 | `PRIN-ENG-07: Purpose Limitation` | 2 | 2 | 🟡 **Méd** (4) | `RN29`, `RN19` | 1 | 1 | 🟢 **Baixo** (1) — Mitigado |
| 27 | `TM-D-05.2-002` | Traveller Presence Detection via Response Discrepancies | `R1.3` / `{U.C. 1.3}` | D | `CWE-200` | `CAPEC-116` | `T1589` | `D3-RO` | PR.DS-01, PR.DS-10, PR.PS-04 | `PRIN-ENG-07: Data Minimization` | 2 | 2 | 🟡 **Méd** (4) | `RN14`, `RN6` | 1 | 1 | 🟢 **Baixo** (1) — Mitigado |
| 28 | `TM-D-07.1-001` | PII Over-Disclosure in Authority Dispatch | `R6.1` / `{U.C. 6.1}` | D | `CWE-200` | `CAPEC-158` | `T1040` | `D3-OM` | PR.DS-01, PR.DS-10, PR.PS-04, RS.CO-02, RS.MA-02, RS.MA-04, DE.CM-01, RS.MI-01 | `PRIN-ENG-07: Data Minimization` | 2 | 3 | 🟠 **Alto** (6) | `RN14`, `RN21`, `RN26` | 1 | 2 | 🟢 **Baixo** (2) — Mitigado |
| 29 | `TM-D-05.2-003` | Lack of Traveller Transparency Regarding Authority Processing | `R4.1`, `R6.1` / `{U.C. 4.1}`, `{U.C. 6.1}` | U, N | `CWE-200` | `CAPEC-116` | `T1589` | `D3-IRA` | ID.AM-08, PR.DS-10, PR.AA-02, PR.AA-03 | `PRIN-ENG-07: Transparency` | 2 | 3 | 🟠 **Alto** (6) | `RN28`, `RN16` | 1 | 1 | 🟢 **Baixo** (1) — Mitigado |
| 30 | `TM-D-09.4-002` | Obstruction of Traveller Erasure & Portability | `R4.1` / `{U.C. 4.1}` | U | `CWE-285` | `CAPEC-115` | `T1499` | `D3-FDS` | ID.AM-08, PR.DS-10, PR.AA-02, PR.AA-03 | `PRIN-ENG-07: Transparency` | 2 | 3 | 🟠 **Alto** (6) | `RN28`, `RN16` | 1 | 1 | 🟢 **Baixo** (1) — Mitigado |
| 31 | `TM-D-05.3-001` | Raw Biometric Capture Retention Beyond the 5-Second Envelope | `R1.1` / `{U.C. 1.1}` | N | `CWE-459` | `CAPEC-180` | `T1070` | `D3-FDS` | PR.DS-01, PR.DS-10 | `PRIN-ENG-07: Storage Limitation` | 3 | 4 | 🔴 **Crit** (12) | `RN5`, `RN11` | 1 | 1 | 🟢 **Baixo** (1) — Mitigado |
| 32 | `TM-D-05.3-002` | Cross-Country Erasure Gap (Zombie Records in Sibling Deployments) | `R4.1` / `{U.C. 4.1}` | N | `CWE-459` | `CAPEC-180` | `T1070` | `D3-FDS` | ID.AM-08, PR.DS-10, PR.AA-02, PR.AA-03 | `PRIN-ENG-04: Cryptographic Erasure` | 2 | 4 | 🔴 **Crit** (8) | `RN28`, `RN16`, `RN10` | 1 | 2 | 🟢 **Baixo** (2) — Mitigado |
| 33 | `TM-D-05.3-003` | Operator Identity Residue After Departure | `R3.1` / `{U.C. 3.1}` | N | `CWE-200` | `CAPEC-116` | `T1005` | `D3-PSN` | PR.AA-01, PR.AA-05 | `PRIN-ENG-07: Storage Limitation` | 2 | 2 | 🟡 **Méd** (4) | `RN17` | 1 | 1 | 🟢 **Baixo** (1) — Mitigado |

---

## 3. Quantitative Risk Reduction Analysis

### 3.1 Aggregate Risk Reduction Quotient ($\Delta R$)
- Total Inherent Risk Score: $23 \times 4 (\text{Crit}) + 7 \times 3 (\text{High}) + 3 \times 2 (\text{Med}) = 92 + 21 + 6 = \mathbf{119 \text{ points}}$
- Total Residual Risk Score: $0 \times 4 (\text{Crit}) + 7 \times 3 (\text{High}) + 12 \times 2 (\text{Med}) + 14 \times 1 (\text{Low}) = 0 + 21 + 24 + 14 = \mathbf{59 \text{ points}}$
- **Empirical Risk Reduction Quotient:**
  $$\Delta R = 119 - 59 = \mathbf{60 \text{ points}} \quad (\mathbf{50.4\% \text{ absolute risk reduction at specification level}})$$

### 3.2 Impact Scoring Basis (Four-Dimension Max-Rule Audit)
Per template §4.3, each threat's Impact is the worst-case maximum across Technical (CIA-A), GDPR Statutory, CRA/NIS 2/AI Act Regulatory, and Business dimensions. The audit over all 33 rows confirms the governing dimension is recorded in each card's Impact justification; the **regulatory dimension governs or co-governs 30 of 33 rows** (border-control criticality under NIS 2 Annex I, CRA Critical Class duties, AI Act Annex III obligations, GDPR Art. 9 processing), which is the defining feature of this case's risk ceiling relative to Case 01. No score changes result from the audit; the maximum rule is satisfied as scored.

### 3.3 Formal Justification for the 7 High-Residual Risks
The seven threats remaining at **High residual risk** are:
1. `TM-D-03.1-001` (Presentation Attack & AI Evasion): Mitigated by liveness-controlled fail-safe reversion and tamper-evident recording (`RN15`, `RN22`, `RN24`). Impact of a successful passage remains Critical (4); Likelihood is reduced to Low (1).
2. `TM-D-01.1-001` (Template Theft): Mitigated by protected-form templates under separated key custody (`RN11`, `RN12`, `RN10`). Impact of Art. 9 data compromise remains Critical (4); Likelihood is reduced to Low (1).
3. `TM-D-03.2-001` (Cross-Country IDOR): Mitigated by structural per-country isolation and integrity-mediated queries (`RN10`, `RN14`, `RN11`). Impact of theoretical commingling remains Critical (4); Likelihood is reduced to Low (1).
4. `TM-D-03.3-002` (Role Escalation & Cross-Country Reach): Mitigated by lifecycle-managed, mediated role assignment (`RN17`, `RN19`, `RN10`). Impact remains Critical (4); Likelihood is reduced to Low (1).
5. `TM-D-09.4-001` (Spoofed Rights Request): Mitigated by requester identity verification and bounded delivery (`RN16`, `RN28`). Impact remains Critical (4); Likelihood is reduced to Low (1).
6. `TM-D-06.1-001` (Malicious Update Injection): Mitigated by signed update distribution and key custody separation (`RN27`, `RN9`, `RN10`, bounded by `RN12`). The residual channel is signing-custody compromise itself; Likelihood is reduced to Low (1), Impact remains Critical (4).
7. `TM-D-01.1-002` (Model Inversion): Mitigated by serving-side resilience, lifetime AI event logging, and protected-form templates (`RN15`, `RN24`, `RN11`). Impact of Art. 9 reconstruction remains Critical (4); Likelihood is reduced to Low (1).

**Verdict:** All seven High residuals are **formally accepted as fully mitigated** under mandatory, testable EARS constraints. None represents an unaddressed architectural vulnerability; each residual is the latent impact of a hypothetical constraint-defeating event, structurally bounded by the cited constraints.

### 3.4 Part 2 to Part 1 Feedback Reconciliation Matrix (ADR-005 / ADR-009 D2)

In accordance with ADR-005 and ADR-009, threat modeling in Part 2 is not a terminal artifact but an active validation engine. The following matrix documents the closed-loop bidirectional traceability between identified threats, their inherent risk, the derived Part 1 mitigating specification elements (EARS constraints, derived functional cards, and Level-2 subfunction use cases), and the resulting verified residual risk:

| Threat ID | Threat Name | Inherent Risk | ADR-005 / ADR-009 Feedback Action | Part 1 Carrier (Req / UC Level 2) | Governing NFR / EARS | Residual Risk |
|---|---|---|---|---|---|---|
| `TM-D-03.1-001` | Traveller Identity Spoofing via Presentation Attacks & AI Evasion | 🔴 **Crit** (12) | Level-2 subfunction for depth/spectral liveness verification and enclave fail-closed matching | `{U.C. 1.2.1}` under `{U.C. 1.2}` | `RN11`, `RN14`, `RN15`, `RN20` | 🟠 **Alto** (4) — Mitigado |
| `TM-D-01.1-001` | Biometric Template Theft at Rest | 🔴 **Crit** (8) | Enforce memory-isolated enclave matching and ephemeral vector zeroization within 5 seconds | `R1.1`, `R1.2`, `{U.C. 1.2.1}` | `RN11`, `RN12`, `RN13` | 🟠 **Alto** (4) — Mitigado |
| `TM-D-03.1-003` | Operator Credential Compromise & MFA Bypass | 🔴 **Crit** (8) | Level-2 subfunction for hardware cryptographic nonce challenge, presence verification, and terminal binding | `{U.C. 3.2.1}` under `{U.C. 3.2}` | `RN17`, `RN18` | 🟡 **Médio** (3) — Mitigado |
| `TM-D-05.3-002` | Cross-Country Erasure Gap (Zombie Records in Sibling Deployments) | 🔴 **Crit** (8) | Level-2 subfunction for distributed key shredding, storage block sanitization, and cryptographic purge receipt | `{U.C. 4.1.1}` under `{U.C. 4.1}` | `RN10`, `RN16`, `RN28` | 🟢 **Baixo** (2) — Mitigado |
| `TM-D-09.4-001` | Spoofed Traveller Rights Request | 🔴 **Crit** (12) | Strict requester identity verification, escrow isolation, and non-repudiable audit recording | `R4.1`, `{U.C. 4.1.1}` | `RN16`, `RN28` | 🟠 **Alto** (4) — Mitigado |
| `TM-D-06.1-001` | Malicious Update Injection into the Gate Fleet | 🔴 **Crit** (8) | Level-2 subfunction for dual digital signature verification, hardware anti-rollback check, and provenance validation | `{U.C. 7.2.1}` under `{U.C. 7.2}` | `RN9`, `RN10`, `RN27` | 🟠 **Alto** (4) — Mitigado |
| `TM-D-03.4-002` | AI Fail-Safe Bypass to Fail-Open | 🔴 **Crit** (8) | Hardware-enforced fail-safe default ensuring physical barriers remain safely closed upon sensor or model fault | `R1.2`, `{U.C. 1.2.1}` | `RN15`, `RN20` | 🟡 **Médio** (3) — Mitigado |

---

## 4. Part 2 Exit Gate Formal Certification (Gates G7–G12)

| Gate | Gate Title | Standard & Verification Evidence | Status |
|---|---|---|---|
| **G7** | **Trust Boundary Coverage** | 100% of interactions crossing $TB_{01}$–$TB_{07}$ across all 28 Cockburn Sea-Level Use Cases (`{U.C. 1.1}`..`{U.C. 11.2}`) are evaluated under STRIDE (including the ATLAS AI lane and the EMB3D hardware lane). Evidence: [`02_TECHNICAL_THREATS_STRIDE.md`](02_TECHNICAL_THREATS_STRIDE.md) §11. | **GREEN** |
| **G8** | **GDPR PII Flow Coverage** | 100% of personal data flows (`DF-P1`–`DF-P8`) are evaluated under all 7 LINDDUN categories. Evidence: [`03_PRIVACY_THREATS_LINDDUN.md`](03_PRIVACY_THREATS_LINDDUN.md) §4. | **GREEN** |
| **G9** | **MITRE Harmonization** | 100% of attack paths carry verified CAPEC, CWE, ATT&CK/ATLAS, and D3FEND cross-references; the formal status of ATLAS (**ACTIVE**), EMB3D (**ACTIVE**), and CAR (**ACTIVE** as audit analytics) is recorded with activation-boundary criteria. Evidence: [`04_ATTACK_VECTORS_AND_DEFENSE_TREES.md`](04_ATTACK_VECTORS_AND_DEFENSE_TREES.md) §7–§8. | **GREEN** |
| **G10** | **Risk Register Completeness** | 33/33 identified threats carry Inherent Risk, Residual Risk, Mitigating Constraints, published NIST CSF anchors (or recorded `—`), and explicit Treatment Verdicts; the ledger reconciles 1:1 with the 33 elicited cards (zero merges). Evidence: Master Ledger Table §2. | **GREEN** |
| **G11** | **Residual Risk Policy Compliance** | **Zero Critical residuals** ($0.0\%$); all 7 High residuals formally justified and mitigated. Zero unrecorded risk acceptances. Evidence: Section §3. | **GREEN** |
| **G12** | **Mechanical & Document Hygiene** | `python scripts/check_traceability.py --case Case_02_SecureBorder_Solutions` returns 0 findings (T1–T7, including Part 2 threat-ledger reconciliation); `python scripts/doc_lint.py --strict` returns 0 findings across all dossiers. | **GREEN** |

---

## 5. Certification Sign-Off

**FINAL PART 2 EXIT GATE VERDICT: GREEN — APPROVED & CONCLUDED.**

Phase 3 Part 2 (Threat & Risk Analysis) for Case 02 (SecureBorder eGate) is formally closed. The system specification is certified as:
1. **Regulatorily Traceable & Compliant** (GDPR + CRA + NIS 2 + AI Act, verified in Part 1).
2. **Adversarially Resilient & Control-Anchored** (STRIDE, LINDDUN, Attack Trees, MITRE D3FEND, ATLAS AI lane, EMB3D hardware lane, NIST CSF anchors, verified in Part 2).
3. **Cleared for Handoff** to **AEGIS Phase 4 (Software Architecture, Verification & Implementation)**.
