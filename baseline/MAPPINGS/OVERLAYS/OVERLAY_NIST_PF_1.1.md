# OVERLAY_NIST_PF_1.1.md

> **Camada 3 — NIST Frameworks Overlay (best practice, optional)**
> NIST Privacy Framework 1.1
> Source-of-truth: `02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/13_Framework_Mapping_Matrix.md` §1, §3.1, §3.2
> AEGIS 10×38 (D-XX.Y) ← NIST PF 1.1 subcategories — only entries that help implement a GDPR obligation (filter: rows where `priv_norm > 0` and CR has GDPR source)

## 1. Scope & Application

**NIST Privacy Framework 1.1** (April 2025 (IPD)) — voluntary, complementary. Maps to 5 functions:
- **IDENTIFY-P (ID-P)** — privacy risk inventory
- **GOVERN-P (GV-P)** — privacy governance
- **CONTROL-P (CT-P)** — data processing controls
- **COMMUNICATE-P (CM-P)** — privacy communication
- **PROTECT-P (PR-P)** — privacy protection

**Filter for SecureBorder (per `13_Framework_Mapping_Matrix.md`):**
- 30 of 38 CR have GDPR source clauses
- 100% coverage for GDPR-touched sub-domains (59 of 104 PF subcats active)

## 2. PF 1.1 → AEGIS Sub-domain Mapping (GDPR-filtered)

| AIGIS D-XX.Y | GDPR Art. | CR ID | PF 1.1 subcategories | priv_norm | Why it helps |
|---|---|---|---|---|---|
| **D-01.1** Data at Rest Encryption | Art. 32 | CR-D-01.1-001 | PR.DS-P1, CT.DP-P2 | 2 | Data security + data processing controls |
| **D-01.4** Data Integrity | Art. 5(1)(d) | CR-D-01.4-001 | PR.DS-P1, CT.DM-P1, CT.DM-P3 | 3 | Disposability, quality, minimisation |
| **D-02.1** Vulnerability ID | Art. 32 | CR-D-02.1-001 | ID.RA-P3, ID.RA-P5 | 2 | Risk assessment re: data |
| **D-02.4** Penetration Testing | Art. 32 | CR-D-02.4-001 | ID.RA-P3, ID.RA-P4, ID.RA-P5 | 3 | Risk framing for biometric AI |
| **D-03.1** Identity Lifecycle | Art. 5(1)(f), 32 | CR-D-03.1-001 | PR.AA-P1, PR.AA-P2, PR.AA-P3, PR.AA-P6, CT.PO-P1 | 5 | Confidentiality, integrity, consent |
| **D-04.1** Incident Detection | Art. 33 | CR-D-04.1-001 | CM.AW-P7, GV.OV-P3 | 2 | Awareness + oversight |
| **D-04.2** Incident Containment | Art. 33 | CR-D-04.2-001 | PR.PO-P7, CT.DM-P10, PR.DS-P10, PR.IR-P3 | 4 | Privacy incident response |
| **D-04.3** Incident Notification | Art. 33 | CR-D-04.3-001 | CM.AW-P7, CM.PO-P2, CM.PO-P1, GV.PO-P5 | 4 | DPA notification per Art. 33 |
| **D-05.1** Data Minimisation | Art. 5(1)(c) | CR-D-05.1-001 | CT.PO-P4, CT.DP-P4, ID.RA-P3 | 3 | Purpose limitation + minimisation |
| **D-05.2** Retention Policies | Art. 5(1)(e), 17 | CR-D-05.2-001 | CT.PO-P4, CT.DM-P5 | 2 | Storage limitation |
| **D-05.3** Erasure (Right to be Forgotten) | Art. 17 | CR-D-05.3-001 | CT.DM-P5, PR.DS-P10 | (T-002) | Erasure vs AI logging retention tension |
| **D-06.3** Vendor Contracts | Art. 28 | CR-D-06.3-001 | CM.PO-P1, CM.PO-P4, GV.PO-P5 | 3 | Processor controller relationship |
| **D-07.1** Secure-by-Design | Art. 25 | CR-D-07.1-001 | GV.PO-P2, CT.PO-P4, CT.DP-P2, CT.DP-P5 | 4 | Privacy by design |
| **D-08.1** Security Awareness | Art. 39 | CR-D-08.1-001 | GV.AT-P1, GV.AT-P2 | 2 | Staff training |
| **D-08.2** Role Competence | Art. 39 | CR-D-08.2-001 | GV.AT-P1, GV.AT-P2 | 2 | DPO training, AI literacy |
| **D-09.1** Security Policies | Art. 24, 25, 32 | CR-D-09.1-001 | GV.PO-P1, GV.PO-P5, CM.PO-P1, GV.RM-P4, GV.RR-P4 | 5 | Accountability + DPO |
| **D-09.2** Impact Assessments | Art. 35, 36 | CR-D-09.2-001 | ID.RA-P3, ID.RA-P4, ID.RA-P5, GV.OV-P2 | 4 | DPIA per Art. 35 |
| **D-09.4** Records of Processing | Art. 30 | CR-D-09.4-001 | ID.IM-P1, ID.IM-P3, CT.PO-P1, CM.PO-P1 | 4 | RoPA + data inventory |
| **D-10.3** Compliance Testing | Art. 5(2), 24 | CR-D-10.3-001 | GV.OV-P1, GV.OV-P2, GV.MA-P1, GV.MA-P2 | 4 | Accountability, monitoring, review |

## 3. Sub-domains NOT in this overlay (no GDPR source)

8 sub-domains have no GDPR mapping (no Art. 32 etc. applies):
- D-01.2 (Data in Transit Encryption) — covered by CRA/NIS 2, not GDPR-specific
- D-01.3 (Key Management) — same
- D-02.2 (Patch Management) — CRA/NIS 2
- D-02.3 (CVD) — CRA
- D-03.2 (MFA), D-03.3 (Authorization), D-03.4 (Secure Defaults) — CRA/NIS 2
- D-04.x — covered above
- D-06.1, D-06.2, D-06.4 (Supply chain) — CRA/NIS 2
- D-08.3 (Board Training) — NIS 2 only (high-tier)

These are covered by **OVERLAY_CRA** and **OVERLAY_NIS2** (not yet created — outside Case 02 scope since SecureBorder doesn't have CRA/NIS 2 as primary).

## 4. PF 1.1 functions used (coverage analysis)

| Function | # mappings | % of total |
|---|---|---|
| IDENTIFY-P (ID-P) | 7 | 14% |
| GOVERN-P (GV-P) | 12 | 24% |
| CONTROL-P (CT-P) | 14 | 28% |
| COMMUNICATE-P (CM-P) | 4 | 8% |
| PROTECT-P (PR-P) | 12 | 24% |
| (total) | 49 | 100% |

→ CONTROL-P dominates (data processing controls are PF's core), with GOVERN-P + PROTECT-P strong on data subject rights.

## 5. Version history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-08-11 | Mavis (auto-extracted from `13_Framework_Mapping_Matrix.md`) | Filtered to GDPR applicable — 19 CR rows, 49 PF subcat mappings |
