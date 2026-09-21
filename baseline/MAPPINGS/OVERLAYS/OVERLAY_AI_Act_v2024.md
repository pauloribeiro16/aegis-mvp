# OVERLAY_AI_Act_v2024.md

> **Camada 2 — Regulations Overlay (legal, obrigatório)**
> AI Act — Regulation (EU) 2024/1689
> Source-of-truth: `02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/05_Regulatory_Applicability.md` §8.5-D + `02_PHASE2_RULES_RICH/08_Obligation_Derivation.md` §11.4
> AEGIS 10×38 (D-XX.Y) ← AI Act Articles — only the obligations that apply to SecureBorder Solutions B.V. (high-risk biometric + border control, Anexo III §1 + §7)

## 1. Scope & Application

**SecureBorder's AI system classification (per AI Act Anexo III):**
- §1 (Biometric identification & categorization of natural persons)
- §7 (AI systems for border control management)

→ High-risk AI system → conformity assessment + ongoing obligations per Art. 43 + 47.

**Applicability flags (per `05_Regulatory_Applicability.md`):**
- AIGIS sub-domains with AI Act coverage: **D-01.4, D-04.3, D-05.1, D-05.2, D-07.1, D-07.2, D-08.2, D-09.1, D-09.2, D-09.4, D-10.1, D-10.2, D-10.3**
- 29 articles mapped, 14 obligations derived (`08_Obligation_Derivation.md` §11.4)

## 2. AI Act → AEGIS Sub-domain Mapping (29 articles)

| AI Act Article | Topic | AEGIS D-XX.Y | Obligated Party | Risk if not met | Source |
|---|---|---|---|---|---|
| Art. 4 (C01) | AI literacy | D-08.2 | PROVIDER | MEDIUM | §8.5-D C01 |
| Art. 5 (C02) | Prohibited practices (negative analysis) | — | PROVIDER | LOW | §8.5-D C02 |
| Art. 9 (C03) | Risk management system | D-09.1, D-09.2, D-07.1 | PROVIDER | HIGH | §8.5-D C03 |
| Art. 10 (C04) | Data governance | D-05.1, D-01.4 | PROVIDER | HIGH | §8.5-D C04 |
| Art. 11 (C05) | Technical documentation (Annex IV) | D-09.4 | PROVIDER | HIGH | §8.5-D C05 |
| Art. 12 (C06) | Logging capability | D-09.4, D-10.2 | PROVIDER | HIGH | §8.5-D C06 |
| Art. 13 (C07) | Transparency to deployers | D-09.1 | PROVIDER | MEDIUM | §8.5-D C07 |
| Art. 14 (C08) | Human oversight | D-08.2, D-09.1 | PROVIDER | HIGH | §8.5-D C08 |
| Art. 15 (C09) | Accuracy + robustness + cybersecurity | D-01.4, D-07.2 | PROVIDER | HIGH | §8.5-D C09 |
| Art. 19(1) (C10) | Automatic logging retention (≥6 months) | D-05.2, D-10.2 | PROVIDER | HIGH | §8.5-D C10 |
| Art. 25 (C11) | Downstream provider | D-09.1 | PROVIDER | MEDIUM | §8.5-D C11 |
| Art. 27 (C12) | FRIA — fundamental rights impact assessment | D-09.2 | PROVIDER | HIGH | §8.5-D C12 |
| Art. 43 (C13) | Conformity assessment | D-10.3 | PROVIDER | **CRITICAL** (market access blocked) | §8.5-D C13 |
| Art. 49 (C14) | Registration (EU database) | D-09.4 | PROVIDER | MEDIUM | §8.5-D C14 |
| Art. 72 (C15) | Post-market monitoring | D-10.1 | PROVIDER | HIGH | §8.5-D C15 |
| Art. 73(1) (C16) | Serious incident reporting — general | D-04.3 | PROVIDER | **CRITICAL** | §8.5-D C16 |
| Art. 73(2) (C17) | Serious incident — default 15d | D-04.3 | PROVIDER | HIGH | §8.5-D C17 |
| Art. 73(3) (C18) | Widespread infringement — 2d | D-04.3 | PROVIDER | **CRITICAL** | §8.5-D C18 |
| Art. 73(4) (C19) | Death of person — 10d | D-04.3 | PROVIDER | HIGH | §8.5-D C19 |
| Art. 75 (C20) | Reporting to market surveillance authorities | D-04.3 | PROVIDER | HIGH | §8.5-D C20 |
| Art. 76 (C21) | Investigation of AI systems | D-09.1 | PROVIDER | MEDIUM | §8.5-D C21 |
| Art. 79 (C22) | Classification rules for high-risk AI systems | D-09.1 | PROVIDER | HIGH | §8.5-D C22 |
| Art. 80 (C23) | Annex III amendments | D-09.1 | PROVIDER | LOW | §8.5-D C23 |
| Art. 84 (C24) | Market surveillance | D-09.1 | PROVIDER | MEDIUM | §8.5-D C24 |
| Art. 85 (C25) | Confidentiality | D-09.1 | PROVIDER | LOW | §8.5-D C25 |
| Art. 86 (C26) | Information to data subjects | D-09.1 | PROVIDER | MEDIUM | §8.5-D C26 |
| Art. 87 (C27) | Complaints handling | D-09.1 | PROVIDER | MEDIUM | §8.5-D C27 |
| Art. 99 (C28) | Penalties (up to €15M / 3% turnover) | D-09.1 | MEMBER STATE | **CRITICAL** | §8.5-D C28 |
| Anexo III (C29) | High-risk AI system categories | D-09.1 | PROVIDER | HIGH | §8.5-D C29 |

## 3. AIGIS Sub-domain Coverage (consolidado)

| AIGIS D-XX.Y | # AI Act articles | Criticality (max risk) | Notes |
|---|---|---|---|
| **D-01.4** Data Integrity Mechanisms | 2 (C04, C09) | HIGH | Data quality + accuracy baseline |
| **D-04.3** Incident Notification | 5 (C16, C17, C18, C19, C20) | **CRITICAL** | 24h/15d/2d/10d — 3-tier reporting (T-001) |
| **D-05.1** Data Minimisation | 1 (C04) | HIGH | Data governance for training data |
| **D-05.2** Retention Policies | 1 (C10) | HIGH | ≥6 months AI Act floor; T-002 with GDPR |
| **D-07.1** Secure-by-Design | 1 (C03) | HIGH | Risk management lifecycle |
| **D-07.2** Secure Coding | 1 (C09) | HIGH | Cybersecurity baseline |
| **D-08.2** Role Competence | 2 (C01, C08) | MEDIUM | AI literacy + human oversight roles |
| **D-09.1** Security Policies | 9 (C03, C07, C08, C11, C21, C22, C23, C24, C25, C26, C27, C28, C29) | **CRITICAL** | Centralised compliance hub |
| **D-09.2** Impact Assessments | 2 (C03, C12) | HIGH | Risk management + FRIA (T-003) |
| **D-09.4** Records of Processing | 3 (C05, C06, C14) | HIGH | Annex IV docs + logging + EU DB |
| **D-10.1** Continuous Monitoring | 1 (C15) | HIGH | Post-market monitoring |
| **D-10.2** Audit Logging | 2 (C06, C10) | HIGH | Tamper-evident + 10y |
| **D-10.3** Compliance Testing | 1 (C13) | **CRITICAL** | Third-party assessment (Annex III) |

## 4. Cross-references (link, don't duplicate)

- **Source of per-article data:** `05_Regulatory_Applicability.md` §8.5-D
- **Source of obligation cards:** `08_Obligation_Derivation.md` §11.4 (14 obligations derived from 29 articles)
- **Source of tensions:** `09_Strategic_Tensions_Report.md` T-001 (multi-reg incident reporting), T-002 (AI Act 6m retention vs GDPR erasure), T-003 (DPIA + FRIA convergence)
- **Case-specific narrative:** `02_PHASE2_RULES_RICH/13_Framework_Mapping_Matrix.md` (unified NIST view)

## 5. What is intentionally OUT of this overlay

- ❌ **Art. 5 negative analysis (no prohibited practices)** — SecureBorder's AI is high-risk classification (Anexo III), not prohibited. Negative confirmation documented separately in `08_Obligation_Derivation.md` §"Nuance — AI_Act Prohibited Practices (Art. 5)".
- ❌ **Art. 80 (Annex III amendments)** — Tracked by EU Commission, not SecureBorder's responsibility.
- ❌ **Art. 99 (Penalties)** — Member State responsibility, not directly applicable to entity compliance actions. Listed for awareness.

## 6. Version history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-08-11 | Mavis (auto-extracted from `05_Regulatory_Applicability.md` §8.5-D + `08_Obligation_Derivation.md` §11.4) | Initial extraction — 29 articles → 13 AIGIS sub-domains |
