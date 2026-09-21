# OVERLAY_NIST_AI_RMF_1.0.md

> **Camada 3 — NIST Frameworks Overlay (best practice, optional)**
> NIST AI Risk Management Framework 1.0
> Source-of-truth: `02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/13_Framework_Mapping_Matrix.md` §1, §3.1, §3.2
> AEGIS 10×38 (D-XX.Y) ← NIST AI RMF 1.0 subcategories — only entries that help implement an AI Act obligation (filter: rows where `airmf_norm > 0` and CR has AI_Act source)

## 1. Scope & Application

**NIST AI RMF 1.0** (January 2023) — voluntary, complementary. Maps to 4 functions:
- **GOVERN** — culture, policies, roles
- **MAP** — context, risk framing
- **MEASURE** — analysis, assessment, monitoring
- **MANAGE** — risk treatment, response

**Filter for SecureBorder (per `13_Framework_Mapping_Matrix.md`):**
- 24 of 38 CR have AI Act source clauses (AI-C*)
- Of these, 14 CR have at least one AI RMF subcategory mapped (airmf_norm > 0)
- 7 CR have `UNMAPPED_AIRMF` (justified — out of AI RMF scope)

## 2. AI RMF 1.0 → AEGIS Sub-domain Mapping (SecureBorder-filtered)

| AIGIS D-XX.Y | AI Act Art. | CR ID | AI RMF subcategories | airmf_norm | Why it helps |
|---|---|---|---|---|---|
| **D-01.1** Data at Rest Encryption | Art. 10, 15 | CR-D-01.1-001 | GOVERN-1.6, MEASURE-2.7, MEASURE-2.5 | 3 | Data quality controls include cryptographic protection of training/inference data |
| **D-01.3** Key Management | Art. 15 | CR-D-01.3-001 | MEASURE-2.7, GOVERN-1.6 | 2 | Key rotation/escrow validated via MEASURE |
| **D-01.4** Data Integrity | Art. 10, 15 | CR-D-01.4-001 | MEASURE-2.6, MEASURE-2.7, MANAGE-2.3 | 3 | Data integrity for AI training data + inference outputs |
| **D-02.1** Vulnerability Identification | Art. 9, 15 | CR-D-02.1-001 | MEASURE-1.1, MEASURE-2.1, MEASURE-2.3, MAP-3.3, MEASURE-2.7, MANAGE-1.3, MAP-3.2 | 7 | AI-specific adversarial testing; model inversion, prompt injection |
| **D-02.4** Penetration Testing | Art. 9, 15 | CR-D-02.4-001 | MEASURE-2.7, MEASURE-2.11 | 2 | Adversarial robustness for high-risk AI |
| **D-03.1** Identity Lifecycle | Art. 9, 14 | CR-D-03.1-001 | MAP-3.5, GOVERN-2.1, GOVERN-3.1 | 3 | AI literacy role mapping; multi-party AI ops |
| **D-04.1** Incident Detection | Art. 9, 72, 73 | CR-D-04.1-001 | MEASURE-2.4, MEASURE-3.1, MANAGE-2.3, MANAGE-4.1 | 4 | AI-specific incident detection (model drift, bias) |
| **D-04.3** Incident Notification | Art. 73(1-4), 75 | CR-D-04.3-001 | MANAGE-2.3, MANAGE-4.3, GOVERN-1.1 | 3 | Reporting workflow per AI Act 3-tier (24h/2d/10d) |
| **D-05.1** Data Minimisation | Art. 10 | CR-D-05.1-001 | GOVERN-1.4, MAP-2.1, MEASURE-2.11, MAP-2.2 | 4 | Data inventory + AI-specific data minimisation |
| **D-05.2** Retention Policies | Art. 11, 19(1) | CR-D-05.2-001 | MEASURE-2.4, MEASURE-4.2, GOVERN-1.4 | 3 | 6-month AI log retention (T-002 with GDPR erasure) |
| **D-08.2** Role Competence | Art. 4, 14 | CR-D-08.2-001 | MAP-3.5, GOVERN-2.1, GOVERN-2.2, GOVERN-3.1 | 4 | AI literacy (Art. 4) + human oversight role clarity (Art. 14) |
| **D-09.1** Security Policies | Art. 9, 13, 14, 25, 43, 49, 79, 80, 84, 85, 86, 87, 99, Anexo III | CR-D-09.1-001 | GOVERN-1.1, GOVERN-1.3, GOVERN-1.4, GOVERN-1.6, MAP-1.1, MEASURE-2.8, MEASURE-2.9, MAP-3.4 | 8 | Central AI governance hub — 14+ articles map here |
| **D-09.2** Impact Assessments | Art. 9, 27 | CR-D-09.2-001 | GOVERN-1.1, GOVERN-1.3, GOVERN-1.5, MAP-5.1, MAP-3.1, MAP-3.2, MANAGE-1.2 | 7 | FRIA (Art. 27) — fundamental rights impact assessment |

## 3. Subcategories intentionally NOT mapped (out of scope)

7 CRs have `UNMAPPED_AIRMF` per the matrix:
- CR-D-04.2-001 (Incident Containment) — `UNMAPPED_AIRMF` justified: AI RMF doesn't define containment procedures; uses MANAGE-2 which is mapped via D-04.1
- CR-D-07.1-001 (Secure-by-Design) — `UNMAPPED_AIRMF` justified: AI RMF GOVERNS risk management at system level, not engineering practices
- CR-D-04.3 et al — partial mapping; MANAGE-2.3 (verified per incident)
- Others — see `13_Framework_Mapping_Matrix.md` §3.1 for per-CR justification

## 4. AI RMF 1.0 functions used (coverage analysis)

| Function | # mappings | % of total |
|---|---|---|
| GOVERN | 13 | 28% |
| MAP | 9 | 20% |
| MEASURE | 17 | 37% |
| MANAGE | 7 | 15% |
| (total) | 46 | 100% |

→ MEASURE dominates (model evaluation, testing, bias detection) — consistent with high-risk AI requiring formal validation.

## 5. Version history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-08-11 | Mavis (auto-extracted from `13_Framework_Mapping_Matrix.md`) | Filtered to AI Act applicable — 14 CR rows, 46 AI RMF subcat mappings |
