# OVERLAY_NIST_CSF_2.0.md

> **Camada 3 — NIST Frameworks Overlay (best practice, optional)**
> NIST Cybersecurity Framework 2.0
> Source-of-truth: `02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/13_Framework_Mapping_Matrix.md` §1, §3.1, §3.2
> AEGIS 10×38 (D-XX.Y) ← NIST CSF 2.0 subcategories — relevant entries that help implement any of the 4 applicable regulations (GDPR + CRA + NIS 2 + AI_Act)

## 1. Scope & Application

**NIST CSF 2.0** (February 2024) — voluntary, complementary. Maps to 6 functions:
- **GOVERN (GV)** — new in 2.0; risk strategy, roles, policies
- **IDENTIFY (ID)** — asset & risk inventory
- **PROTECT (PR)** — controls implementation
- **DETECT (DE)** — anomaly & event detection
- **RESPOND (RS)** — incident response
- **RECOVER (RC)** — restoration & improvement

**Filter for SecureBorder:** all 38 CR have at least one CSF subcat mapped (csf_norm > 0). This is the most-used overlay.

## 2. CSF 2.0 → AEGIS Sub-domain Mapping (consolidated)

| AIGIS D-XX.Y | CR ID | CSF 2.0 subcategories | csf_norm | Why it helps |
|---|---|---|---|---|
| **D-01.1** Data at Rest Encryption | CR-D-01.1-001 | PR.DS-01 | 1 | Data security baseline |
| **D-01.4** Data Integrity | CR-D-01.4-001 | PR.DS-01, PR.DS-02 | 2 | Integrity + confidentiality |
| **D-02.1** Vulnerability Identification | CR-D-02.1-001 | ID.RA-01, UNMAPPED_CSF | 2 | Vulnerability = risk, partial scope |
| **D-02.4** Penetration Testing | CR-D-02.4-001 | ID.IM-02, ID.RA-03 | 2 | Inventory + risk assessment |
| **D-03.1** Identity Lifecycle | CR-D-03.1-001 | PR.AA-01, PR.AA-03, PR.AA-05 | 3 | Identity, auth, access control |
| **D-04.1** Incident Detection | CR-D-04.1-001 | DE.AE-02, DE.CM-01, DE.CM-09 | 3 | Anomaly + monitoring |
| **D-04.2** Incident Containment | CR-D-04.2-001 | RS.MI-01, RS.MI-02 | 2 | Mitigation |
| **D-04.3** Incident Notification | CR-D-04.3-001 | RS.CO-02, RS.CO-03 | 2 | Communication |
| **D-05.1** Data Minimisation | CR-D-05.1-001 | PR.DS-10, ID.AM-03 | 2 | Data-use + asset inventory |
| **D-05.2** Retention Policies | CR-D-05.2-001 | PR.DS-11, PR.PS-06 | 2 | Backup integrity + secure config |
| **D-07.1** Secure-by-Design | CR-D-07.1-001 | PR.PS-06, ID.RA-01 | 2 | Secure config + risk-based design |
| **D-08.2** Role Competence | CR-D-08.2-001 | PR.AT-02 | 1 | Awareness training |
| **D-09.1** Security Policies | CR-D-09.1-001 | GV.PO-01, GV.PO-02 | 2 | Governance baseline |
| **D-09.2** Impact Assessments | CR-D-09.2-001 | ID.RA-04, ID.RA-05, GV.RM-06 | 3 | Risk assessment + management |
| **D-09.4** Records of Processing | CR-D-09.4-001 | GV.OC-04, ID.AM-08, GV.OC-05 | 3 | Roles + records + OS hardening |
| **D-10.1** Continuous Monitoring | CR-D-10.1-001 | GV.OC-03, DE.CM-01, ID.RA-04 | 3 | Oversight + monitoring + risk |
| **D-10.2** Audit Logging | CR-D-10.2-001 | PR.PS-04, ID.AM-03, PR.AA-01 | 3 | Logging + audit |
| **D-10.3** Compliance Testing | CR-D-10.3-001 | GV.OC-03, GV.OV-03, GV.OC-04 | 3 | Oversight + management review |

## 3. CSF 2.0 functions used (coverage analysis)

| Function | # mappings | % of total |
|---|---|---|
| GOVERN (GV) | 8 | 16% |
| IDENTIFY (ID) | 7 | 14% |
| PROTECT (PR) | 18 | 37% |
| DETECT (DE) | 4 | 8% |
| RESPOND (RS) | 4 | 8% |
| RECOVER (RC) | 0 | 0% |
| (total) | 41 | 100% |

→ PROTECT dominates (CSF's traditional focus). GOVERN rises in 2.0. RECOVER is absent — AEGIS doesn't yet have a D-XX.Y for recovery (gap; consider adding D-11 in future taxonomy revisions).

## 4. Where CSF is "alone" (not covered by PF/AI RMF)

CSF-specific subcategories not in PF/AI RMF (added by CSF 2.0 expansion):
- **PR.PS-04** (Software platform security) — covered in D-10.2
- **PR.PS-06** (Secure software development) — covered in D-05.2, D-07.1
- **GV.OC-04** (Critical infrastructure risk) — covered in D-09.4, D-10.3
- **DE.CM-09** (Hardware monitoring) — covered in D-04.1

→ CSF 2.0 adds **new** subcats not present in 1.1 — important for AEGIS to track (e.g., GV.OC-04 introduced only in 2.0).

## 5. Version history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-08-11 | Mavis (auto-extracted from `13_Framework_Mapping_Matrix.md`) | All 38 CR rows, 41 CSF subcat mappings |
