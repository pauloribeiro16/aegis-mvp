---
document_id: AEGIS-METH-AMBIG-REG-INDEX
title: "Ambiguity Registry — Index by Regulation"
phase: 0 (methodology baseline)
version: 1.0
created: 2026-09-14
status: ACTIVE
counts:
  total_clauses: 49
  by_regulation:
    GDPR: 17
    NIS_2: 6
    CRA: 9
    DORA: 4
    AI_Act: 3
  by_card_variant:
    GDPR-light: 11
    NIS_2-light: 6
    CRA-light: 9
    DORA-grade: 4
    AI-Act-light: 3
    source-locus: 16  # all DORA + AI Act + NIS 2 CVD
supersedes: nothing
---

# Ambiguity Registry — Index by Regulation

**Sources (consolidated from):**
- Case_01 [Doc09_Ambiguity_Register.md](../../../02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/Doc09_Ambiguity_Register.md) — top-20 of 417 cards (GDPR + CRA, 9 cards cited here)
- Case_02 [Doc09_Ambiguity_Register.md](../../../02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/Doc09_Ambiguity_Register.md) — top-20 of 1292 cards (GDPR + CRA + NIS 2, 20 cards cited here)
- Case_03 [Doc09_Ambiguity_Register.md](../../../02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/Doc09_Ambiguity_Register.md) — top-20 of 846 cards (GDPR + CRA + NIS 2 + DORA + AI Act, 20 cards cited here)

Each entry is the **canonical methodology reading**. Where cases diverged, both readings are recorded and the divergence is flagged.

---

## GDPR (17 cards)

### GDPR-CL23 — Art. 9(2)(g) — Substantial public interest

- **Berry flag:** VAG (S3)
- **Verbatim phrase:** `substantial public interest`
- **Sub-domain touchpoints:** D-01.1
- **Card variant:** GDPR-light
- **Control anchors:** CSF: — · PF 1.1: — · AI RMF: — (no consuming SR in dashboard mappings)

**Instances across cases:** C01 card #4 (case impact: biometric data optional); C02 card 3.01 (case impact: government-contracted border control).

**Variants:**
- **R1 (loose):** `substantial` = materially more weighty than legitimate interests.
- **R2 (strict):** `substantial` = government-contracted public interest qualifies per Charter Art. 52(1) `essence of the right` test.

**Recommended Variant:** **R2** (strict — EDPB Charter-aligned). Both cases adopt R2; cases diverge only in the operational mitigation documented in Phase 2 (DPO sign-off per processing scope).

**Source authority:** EDPB Guidelines on legitimate interests; Charter Art. 52(1).

**Cases citing this card:** C01 (Doc09 card #4), C02 (Doc09 §3.01).

---

### GDPR-CP02 — Art. 25(1) — Privacy by design

- **Berry flag:** VAG (S3) + POLY (S2) — `state of the art`, `effective manner`
- **Sub-domain touchpoints:** D-01.1, D-01.3
- **Card variant:** GDPR-light
- **Control anchors:** CSF: PR.PS-01, ID.AM-08, PR.PS-06, PR.DS-01 · PF 1.1: CT.DP-P4, CT.PO-P4, GV.PO-P2, CT.DP-P2 · AI RMF: — · from `SR-GDPR-013`, `SR-GDPR-039`, `SR-GDPR-040`, +1 more (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)

**Instances across cases:** C01 card #2; C02 card 3.02; C03 card 3.

**Variants:**
- **R1 (industry):** `State of the art` = ISO 27001 + sector-specific best practices at design time.
- **R2 (strict):** `State of the art` = ENISA / EDPB-published state-of-the-art guidance.
- **R3 (loose):** `State of the art` = any reasonable technical measure documented at design time.

**Recommended Variant:** **R2** — ENISA / EDPB-published state-of-the-art guidance as the strictest ceiling; ISO 27001 + sector best practices as a minimum. All three cases adopt R2.

**Source authority:** EDPB Guidelines 4/2019 on Article 25; ENISA state-of-the-art reports.

**Cases citing this card:** C01 (Doc09 card #2), C02 (Doc09 §3.02), C03 (Doc09 card 3).

---

### GDPR-CP15 — Art. 32(1) — Security measures (open list)

- **Berry flag:** VAG (S3) + COORD (S3) + POLY (S2)
- **Sub-domain touchpoints:** D-01.1, D-01.2, D-04.3, D-06.3, D-09.2
- **Card variant:** GDPR-light
- **Control anchors:** CSF: PR.DS-01, PR.DS-10, PR.DS-02, PR.IR-01, PR.IR-03, ID.RA-01, PR.PS-02, ID.RA-05, ID.IM-02, PR.AA-05, PR.AA-06, PR.AT-02, DE.CM-01, DE.CM-09, RS.MA-02, RS.MI-01, RS.MI-02, PR.IR-04, PR.DS-11, RC.RP-04, GV.SC-03, GV.SC-04, DE.CM-06, PR.PS-06, ID.AM-08 · PF 1.1: PR.DS-P1, PR.PO-P3, PR.DS-P2, PR.AC-P5, CT.DP-P2, GV.MT-P3, CT.DM-P10, ID.RA-P3, ID.RA-P5, PR.AC-P1, PR.AC-P2, CT.PO-P1, GV.AT-P2, GV.MT-P5, CM.AW-P7, PR.PO-P7, ID.DE-P5, CT.DM-P9, GV.PO-P2, CT.PO-P4 · AI RMF: — · from `SR-GDPR-001`, `SR-GDPR-002`, `SR-GDPR-003`, +11 more (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)

**Verbatim phrases:** `state of the art`, `(a) AND (b) AND (c) AND (d)`, `in a timely manner`

**Variants on `state of the art`:** same as GDPR-CP02 above (R1 / R2 / R3).

**Variants on `(a) AND (b) AND (c) AND (d)`:** 4-element list is closed (all required).

**Variants on `in a timely manner`:**
- **R1:** `Timely` = RTO defined per processing activity (objective measure). Source: ISO 27001 BCP/DRP best practice.
- **R2:** `Timely` = as-soon-as-practicable for the specific incident. Source: EDPB Guidelines 7/2019.

**Recommended Variants:**
- `state of the art` → **R2** (strict; matches GDPR-CP02).
- 4-element list → **all 4 required** (closed list).
- `timely` → **C01 / C03 adopt R2** (EDPB Guidelines 7/2019); **C02 adopts R1** (RTO defined per activity, ISO 27001 BCP/DRP best practice).

**Divergence flagged:** C01/C03 choose EDPB-aligned `timely`; C02 chooses ISO 27001 objective RTO. Both are defensible. Methodology position: **R2** as the **default** (EDPB Guidelines are authoritative for GDPR); R1 admissible when the controller documents a per-processing RTO that meets or exceeds `as-soon-as-practicable`.

**Source authority:** EDPB Guidelines 7/2019 (Sections 4-5 on appropriate measures); ISO 27001 A.17 BCP.

**Cases citing this card:** C01 (Doc09 card #3, #7, #10, #15), C02 (Doc09 §3.03), C03 (Doc09 card 2, plus 4 MEDIUM-priority cross-cutting per Doc09 §4).

---

### GDPR-CP19 — Art. 34(1) — High-risk threshold

- **Berry flag:** POLY+VAG (S3)
- **Verbatim phrase:** `likely to result in a high risk`
- **Sub-domain touchpoints:** D-01.3, D-04.3
- **Card variant:** GDPR-light
- **Control anchors:** CSF: RS.CO-03, RS.MA-04, PR.DS-01, PR.IR-03 · PF 1.1: CM.AW-P7, CM.AW-P8, PR.DS-P1, CT.DP-P2, CM.PO-P1 · AI RMF: — · from `SR-GDPR-019`, `SR-GDPR-020`, `SR-GDPR-021` (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)

**Variants:**
- **R1 (EDPB 9/2022):** `High risk` = objectively elevated above ordinary processing risk.
- **R2 (CNIL):** `High risk` = severe impact on data subject's rights.

**Recommended Variant:** **R1** — EDPB Guidelines 9/2022. Communication to data subject within Art. 12(3) one-month clock; high-risk + Art. 9 fingerprint triggers immediate communication.

**Source authority:** EDPB Guidelines 9/2022 on personal data breach notification.

**Cases citing this card:** C01 (Doc09 card #11), C02 (Doc09 §3.05).

---

### GDPR-CP20 — Art. 34(3) — Exceptions to data-subject communication

- **Berry flag:** VAG (S3) × 2
- **Verbatim phrases:** `render the personal data unintelligible`, `disproportionate effort`
- **Sub-domain touchpoints:** D-01.3, D-04.3
- **Card variant:** GDPR-light
- **Control anchors:** CSF: PR.DS-01, PR.IR-03, RS.MI-01, RS.MI-02, RS.CO-03, PR.PS-06 · PF 1.1: PR.DS-P1, CT.DP-P2, PR.PO-P7, CT.DM-P10, CM.AW-P7, CM.PO-P1 · AI RMF: — · from `SR-GDPR-004`, `SR-GDPR-015`, `SR-GDPR-020`, +2 more (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)

**Variants:**
- **R1 (strict):** Art. 34(3) exceptions interpreted strictly; biometric Art. 9 data fails the encryption carve-out only if AES-256 + HSM-backed key + cryptographic sharding + AI Act log re-identification prevented.
- **R2 (loose):** Encrypted data always qualifies for the carve-out.

**Recommended Variant:** **R1** (strict). All cited cases adopt R1.

**Source authority:** EDPB Guidelines 9/2022 §3.4 (encryption exception).

**Cases citing this card:** C01 (Doc09 card #12), C02 (Doc09 §3.06).

---

### GDPR-CP01 — General controller responsibility

- **Berry flag:** VAG (S2)
- **Sub-domain touchpoints:** D-09.1
- **Card variant:** GDPR-light
- **Control anchors:** CSF: GV.PO-01, GV.PO-02, GV.RM-04, GV.OV-03 · PF 1.1: GV.PO-P1, GV.PO-P6, GV.MT-P3, GV.PO-P5 · AI RMF: — · from `SR-GDPR-043`, `SR-GDPR-044` (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)

**Variants:** Single Recommended Variant per C03: scope of `responsibility` includes downstream processors (controller cannot delegate accountability). Cites Art. 5(2) accountability principle.

**Cases citing this card:** C03 (Doc09 card 4).

---

### GDPR-CP04 — Art. 26(1) — Joint controllers

- **Berry flag:** VAG (S3)
- **Sub-domain touchpoints:** D-09.1
- **Card variant:** GDPR-light
- **Control anchors:** CSF: GV.RR-02, GV.SC-03, GV.PO-01, GV.OV-03 · PF 1.1: GV.PO-P3, ID.DE-P3, CM.PO-P1, GV.MT-P3 · AI RMF: — · from `SR-GDPR-060`, `SR-GDPR-061` (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)

**Variants:** R1 (transparent allocation in JCA document), R2 (controller-only by default). C02 §3.10 adopted R1.

**Cases citing this card:** C02 (Doc09 §3.10).

---

### GDPR-CP17 — 72-hour notification

- **Berry flag:** VAG (S2)
- **Sub-domain touchpoints:** D-04.3, D-06.3 (cross-cut)
- **Card variant:** GDPR-light
- **Control anchors:** CSF: DE.CM-01, DE.CM-09, RS.MA-02, RS.CO-02, RS.MA-04, RS.MA-03, RS.AN-03, RS.AN-07, DE.CM-03, DE.AE-02 · PF 1.1: GV.MT-P5, GV.MT-P3, CM.AW-P7, CM.PO-P2, ID.DE-P3, CM.PO-P1, ID.RA-P3 · AI RMF: — · from `SR-GDPR-014`, `SR-GDPR-016`, `SR-GDPR-017`, +2 more (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)

**Variants:** R1 (notification starts at controller awareness, not incident detection); R2 (notification starts at incident detection by controller or processor under contract).

**Recommended Variant:** **R1** — aligns with DORA RTS 4h universal SLA (per C03 cross-cutting §4).

**Cases citing this card:** C03 (Doc09 card 5, plus cross-cutting §4).

---

### GDPR-CL25 — Art. 33 — Personal data breach notification

- **Berry flag:** VAG (S2)
- **Sub-domain touchpoints:** D-04.3
- **Card variant:** GDPR-light
- **Control anchors:** CSF: — · PF 1.1: — · AI RMF: — (no consuming SR in dashboard mappings)

**Variants:** R1 (notification within 72h of awareness, not of detection); R2 (72h clock starts at first detection by any internal party).

**Recommended Variant:** **R1** — C03 adopts R1.

**Cases citing this card:** C03 (Doc09 card 1).

---

### GDPR-RT08 — Art. 14(5)(b) — Disproportionate effort exception

- **Berry flag:** VAG (S3)
- **Verbatim phrase:** `proves impossible or would involve a disproportionate effort`
- **Sub-domain touchpoints:** D-04.3
- **Card variant:** GDPR-light
- **Control anchors:** CSF: — · PF 1.1: — · AI RMF: — (no consuming SR in dashboard mappings)

**Variants:**
- **R1 (Recital 62):** Exception applies narrowly to research/archiving; controllers must demonstrate efforts.
- **R2 (industry):** Exception applies broadly; controllers judge what is disproportionate.

**Recommended Variant:** **R1** — Art. 14(5)(b) disclosure limited to extent strictly necessary.

**Source authority:** Recital 62 GDPR (non-binding, but the only available anchor); EDPB Guidelines 8/2022 on direct/indirect disclosure.

**Cases citing this card:** C02 (Doc09 §3.07).

---

### GDPR-RT11 — Art. 15(4) — Third-party rights

- **Berry flag:** VAG (S3)
- **Verbatim phrase:** `shall not adversely affect the rights and freedoms of others`
- **Sub-domain touchpoints:** D-04.3
- **Card variant:** GDPR-light
- **Control anchors:** CSF: RS.CO-02, ID.AM-08 · PF 1.1: CM.AW-P5, CT.DM-P3 · AI RMF: — · from `SR-GDPR-022` (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)

**Variants:**
- **R1 (EDPB):** Redact only data identifying other natural persons.

**Recommended Variant:** **R1** (only EDPB reading available).

**Cases citing this card:** C02 (Doc09 §3.08).

---

### GDPR-RT12 — Art. 16 — Rectification right

- **Berry flag:** VAG (S2)
- **Sub-domain touchpoints:** D-01.4
- **Card variant:** GDPR-light
- **Control anchors:** CSF: PR.DS-10, ID.AM-08, RS.CO-02 · PF 1.1: CT.DM-P3, CM.AW-P5 · AI RMF: — · from `SR-GDPR-006`, `SR-GDPR-022` (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)

**Cases citing this card:** C01 (Doc09 card #14).

---

### GDPR-RT16 — Art. 21(1) — Objection grounds and overriding

- **Berry flag:** VAG (S3)
- **Verbatim phrase:** `compelling legitimate grounds`
- **Sub-domain touchpoints:** D-01.1
- **Card variant:** GDPR-light
- **Control anchors:** CSF: — · PF 1.1: — · AI RMF: — (no consuming SR in dashboard mappings)

**Variants:**
- **R1 (EDPB):** `Compelling` = strictly necessary (lex specialis to legitimate interests).
- **R2 (loose):** `Compelling` = materially more weighty than legitimate interests.

**Recommended Variant:**
- **C01 adopts R2** (loose reading aligned with EDPB Guidelines on legitimate interests).
- **C02 adopts R1** (strict — documented per-objection risk assessment with DPO sign-off).

**Divergence flagged:** Both are EDPB-aligned; the difference is operational granularity. Methodology position: **R1** for cases where the company operates at scale (each objection warrants documented assessment); **R2** admissible for MICRO cases where the volume does not justify per-objection documentation.

**Source authority:** EDPB Guidelines on legitimate interests under GDPR.

**Cases citing this card:** C01 (Doc09 card #1), C02 (Doc09 §3.04).

---

### GDPR-RT20 — Art. 23(1) — Restrictions on data subject rights

- **Berry flag:** VAG (S3)
- **Sub-domain touchpoints:** D-09.1
- **Card variant:** GDPR-light
- **Control anchors:** CSF: — · PF 1.1: — · AI RMF: — (no consuming SR in dashboard mappings)

**Cases citing this card:** C02 (Doc09 §3.09).

---

### GDPR — Art. 35 — Data protection impact assessment (DPIA)

- **Berry flag:** POLY+VAG (S3)
- **Sub-domain touchpoints:** D-09.2
- **Card variant:** GDPR-light
- **Control anchors:** CSF: — · PF 1.1: — · AI RMF: — (no consuming SR in dashboard mappings)

**Instance:** Both C01 and C02 reproduce the full Art. 35 verbatim (10 paragraphs). The ambiguity is whether a single DPIA can address a set of similar processing operations (Art. 35(1)) vs requiring one DPIA per processing operation.

**Recommended Variant:** **Single DPIA per set of similar operations is permitted** (Art. 35(1) sentence 2).

**Cases citing this card:** C01 (Doc09 §3 verbatim block), C02 (Doc09 §3 verbatim block before §3.10).

---

### GDPR — 5-reg max-SLA routing pipeline (D-04.3 cross-cut)

- **Berry flag:** COORD (S3)
- **Sub-domain touchpoints:** D-04.3
- **Card variant:** GDPR-light (cross-regulation)
- **Control anchors:** CSF: — · PF 1.1: — · AI RMF: — (no consuming SR in dashboard mappings)

**Verbatim resolution (C03 §4 cross-cutting):** DORA 4h + RTS Art. 6 + NIS 2 24h + CRA 24h + GDPR 72h + AI Act 15d/2d/10d — single SOC pipeline with per-regulation output stream.

**Cases citing this card:** C03 (Doc09 §4 cross-cutting).

---

## NIS 2 (6 cards)

### NIS2-CL07 — Art. 21(1) sentence 1 — Risk-management core obligation

- **Berry flag:** VAG (S3)
- **Sub-domain touchpoints:** D-06.1, D-09.3
- **Card variant:** source-locus / NIS 2-light
- **Control anchors:** CSF: PR.DS-01, PR.DS-02, GV.RM-04, ID.RA-01, GV.SC-04, PR.AA-01, PR.AA-05, PR.AT-02, ID.AM-01, ID.AM-02, PR.AA-03, PR.IR-03, RS.MA-01, RS.AN-03, DE.CM-01, DE.CM-09, RC.RP-04, PR.DS-11, GV.SC-02, GV.SC-03, PR.PS-06, PR.PS-02, PR.AT-01, PR.PS-01, ID.RA-05, GV.PO-01, ID.IM-01, GV.OV-03, GV.RM-06, ID.RA-06, PR.IR-01, RS.MI-02 · PF 1.1: — · AI RMF: — · from `SR-NIS2-001`, `SR-NIS2-002`, `SR-NIS2-003`, +19 more (00_VISUALISATIONS/NIS2/NIS2_Dashboard.html)

**Recommended Variant (C02 + C03):** Art. 21(2)(a)–(j) closed-AND-list reading; CRO + CISO owns.

**Cases citing this card:** C02 (Doc09 §3.11), C03 (Doc09 card 10).

---

### NIS2-CL08 — Art. 21(1) sentence 2 — Risk-management proportionality

- **Berry flag:** VAG (S3)
- **Sub-domain touchpoints:** D-09.1
- **Card variant:** source-locus
- **Control anchors:** CSF: PR.DS-01, PR.DS-02, GV.RM-04, GV.SC-02, GV.SC-03, GV.PO-01, ID.IM-01, GV.OV-03, GV.PO-02, GV.RM-06, ID.RA-06 · PF 1.1: — · AI RMF: — · from `SR-NIS2-001`, `SR-NIS2-020`, `SR-NIS2-037`, +2 more (00_VISUALISATIONS/NIS2/NIS2_Dashboard.html)

**Cases citing this card:** C02 (Doc09 §3.12).

---

### NIS2-CL17 — Art. 21(2)(h) — Supply chain security

- **Berry flag:** VAG (S2)
- **Sub-domain touchpoints:** D-06.1
- **Card variant:** source-locus
- **Control anchors:** CSF: PR.DS-01, PR.DS-02, GV.RM-04 · PF 1.1: — · AI RMF: — · from `SR-NIS2-001` (00_VISUALISATIONS/NIS2/NIS2_Dashboard.html)

**Cases citing this card:** C02 (Doc09 §3.13).

---

### NIS2-CL26 — Art. 23(1) ¶1 — Incident notification initial

- **Berry flag:** VAG (S3)
- **Sub-domain touchpoints:** D-04.3
- **Card variant:** source-locus
- **Control anchors:** CSF: RS.MA-04, RS.MA-02, RS.MA-03, RS.CO-03, GV.OC-03 · PF 1.1: — · AI RMF: — · from `SR-NIS2-010`, `SR-NIS2-011`, `SR-NIS2-016`, +1 more (00_VISUALISATIONS/NIS2/NIS2_Dashboard.html)

**Cases citing this card:** C02 (Doc09 §3.14).

---

### NIS2-CL33 — Art. 23(3)(a) — Incident notification final

- **Berry flag:** VAG (S3)
- **Sub-domain touchpoints:** D-04.3
- **Card variant:** source-locus
- **Control anchors:** CSF: RS.MA-04, RS.MA-02, RS.MA-03 · PF 1.1: — · AI RMF: — · from `SR-NIS2-010`, `SR-NIS2-011` (00_VISUALISATIONS/NIS2/NIS2_Dashboard.html)

**Cases citing this card:** C02 (Doc09 §3.15).

---

### NIS2-CL22 — Art. 23(4) — Incident notification (variant framing)

- **Berry flag:** VAG (S3)
- **Sub-domain touchpoints:** D-04.3
- **Card variant:** source-locus
- **Control anchors:** CSF: ID.IM-01, GV.OV-03, RS.MI-02 · PF 1.1: — · AI RMF: — · from `SR-NIS2-042` (00_VISUALISATIONS/NIS2/NIS2_Dashboard.html)

**Cases citing this card:** C03 (Doc09 card 11).

---

### NIS2-CL20 — Art. 20 — Management body liability

- **Berry flag:** VAG (S3)
- **Sub-domain touchpoints:** D-08.3
- **Card variant:** source-locus
- **Control anchors:** CSF: ID.AM-04, ID.RA-01, ID.RA-02, GV.SC-02, GV.SC-04, PR.PS-06 · PF 1.1: — · AI RMF: — · from `SR-NIS2-022`, `SR-NIS2-023`, `SR-NIS2-024` (00_VISUALISATIONS/NIS2/NIS2_Dashboard.html)

**Cases citing this card:** C03 (Doc09 card 12).

---

### NIS2-CL12 — Coordinated vulnerability disclosure ecosystem (Art. 12)

- **Berry flag:** VAG (S2)
- **Sub-domain touchpoints:** D-02.3
- **Card variant:** source-locus
- **Control anchors:** CSF: RC.RP-04, PR.DS-11 · PF 1.1: — · AI RMF: — · from `SR-NIS2-019` (00_VISUALISATIONS/NIS2/NIS2_Dashboard.html)

**Variants:**
- **R1:** security.txt + email + CVD page only.
- **R2:** + bug bounty + CSIRT integration.

**Recommended Variant:** **R1** — security.txt + dedicated intake mailbox + CVD page + ISO 29147 process. Bug bounty deferred.

**Cases citing this card:** C03 (Doc09 card 13).

---

## CRA (9 cards)

### CRA-CL02 — Art. 6(a) proviso — Installation/use conditions

- **Berry flag:** VAG (S3)
- **Sub-domain touchpoints:** D-01.1, D-01.2
- **Card variant:** CRA-light / source-locus
- **Control anchors:** CSF: — · PF 1.1: — · AI RMF: — (no consuming SR in dashboard mappings)

**Cases citing this card:** C01 (Doc09 card #5, #13, #25+); C02 (Doc09 §3.16).

---

### CRA-CL04 — Important-products classification gate

- **Berry flag:** VAG (S3)
- **Sub-domain touchpoints:** D-09.3
- **Card variant:** CRA-light
- **Control anchors:** CSF: — · PF 1.1: — · AI RMF: — (no consuming SR in dashboard mappings)

**Cases citing this card:** C03 (Doc09 card 8).

---

### CRA-CL06 — Art. 7(2)(a) — Classification criterion A

- **Berry flag:** VAG (S2)
- **Sub-domain touchpoints:** D-09.3
- **Card variant:** CRA-light
- **Control anchors:** CSF: — · PF 1.1: — · AI RMF: — (no consuming SR in dashboard mappings)

**Cases citing this card:** C01 (Doc09).

---

### CRA-CL15 — Cybersecurity risk-assessment core duty

- **Berry flag:** VAG (S3)
- **Sub-domain touchpoints:** D-09.2
- **Card variant:** CRA-light
- **Control anchors:** CSF: ID.RA-05, PR.PS-06 · PF 1.1: — · AI RMF: — · from `SR-CRA-065` (00_VISUALISATIONS/CRA/CRA_Dashboard.html)

**Cases citing this card:** C03 (Doc09 card 7).

---

### CRA-CL23a — Supply-chain due diligence (Q6=b split)

- **Berry flag:** VAG (S3)
- **Sub-domain touchpoints:** D-06.1
- **Card variant:** CRA-light
- **Control anchors:** CSF: GV.SC-01, GV.SC-02, ID.RA-02 · PF 1.1: — · AI RMF: — · from `SR-CRA-050` (00_VISUALISATIONS/CRA/CRA_Dashboard.html)

**Recommended Variant (C03 cross-cutting):** Annex I Part I (2)(h) closed-list reading; CRO + Procurement owns.

**Cases citing this card:** C03 (Doc09 card 6).

---

### CRA-CL30 — Contractual arrangements (DORA-style)

- **Berry flag:** VAG (S3)
- **Sub-domain touchpoints:** D-06.3
- **Card variant:** CRA-light
- **Control anchors:** CSF: PR.PS-02, GV.SC-04, RS.MI-01, RS.MI-02, GV.OV-02, GV.SC-02 · PF 1.1: — · AI RMF: — · from `SR-CRA-015`, `SR-CRA-045`, `SR-CRA-061`, +1 more (00_VISUALISATIONS/CRA/CRA_Dashboard.html)

**Cases citing this card:** C03 (Doc09 card 9).

---

### CRA-CL51 — Art. 14(1) sentence 1 — Vulnerability handling

- **Berry flag:** VAG (S3)
- **Sub-domain touchpoints:** D-02.3, D-04.1
- **Card variant:** source-locus
- **Control anchors:** CSF: RS.MA-01, RS.MA-04, RS.MA-02, RS.CO-02 · PF 1.1: — · AI RMF: — · from `SR-CRA-028`, `SR-CRA-029` (00_VISUALISATIONS/CRA/CRA_Dashboard.html)

**Cases citing this card:** C02 (Doc09 §3.17).

---

### CRA-CL56 — Art. 14(3) sentence 1 — Coordinated disclosure

- **Berry flag:** VAG (S3)
- **Sub-domain touchpoints:** D-02.3
- **Card variant:** source-locus
- **Control anchors:** CSF: RS.MA-01, RS.AN-03 · PF 1.1: — · AI RMF: — · from `SR-CRA-031` (00_VISUALISATIONS/CRA/CRA_Dashboard.html)

**Cases citing this card:** C02 (Doc09 §3.18).

---

### CRA-CL61 — Art. 14(5)(a) — Notification to authorities

- **Berry flag:** VAG (S3)
- **Sub-domain touchpoints:** D-04.3
- **Card variant:** source-locus
- **Control anchors:** CSF: RS.MA-01, RS.AN-03, ID.RA-04, RS.MA-03, GV.OC-04, GV.PO-01 · PF 1.1: — · AI RMF: — · from `SR-CRA-031`, `SR-CRA-034`, `SR-CRA-090` (00_VISUALISATIONS/CRA/CRA_Dashboard.html)

**Cases citing this card:** C02 (Doc09 §3.19).

---

### CRA-CL62 — Art. 14(5)(b) — Notification to users

- **Berry flag:** VAG (S3)
- **Sub-domain touchpoints:** D-04.3
- **Card variant:** source-locus
- **Control anchors:** CSF: RS.MA-01, RS.AN-03, RS.MA-03 · PF 1.1: — · AI RMF: — · from `SR-CRA-031`, `SR-CRA-035` (00_VISUALISATIONS/CRA/CRA_Dashboard.html)

**Cases citing this card:** C02 (Doc09 §3.20).

---

## DORA (4 cards)

### DORA Art. 5(2) — ICT risk management framework

- **Berry flag:** VAG (S3) — 4-verb coordination
- **Verbatim phrase:** `shall define, approve, oversee and be responsible for the implementation`
- **Sub-domain touchpoints:** D-09.1
- **Card variant:** DORA-grade

**Variants:**
- **R1 (literal):** 4 verbs are 4 separate duties.
- **R2 (loose):** 4 verbs describe one composite duty.

**Recommended Variant:** **R1** — 4 separate duties. Board briefing programme + 5-policy architecture + ISMS surveillance audit + DORA Art. 5 framework documented.

**Cases citing this card:** C03 (Doc09 card 16).

---

### DORA Art. 17(1) — ICT-related incident management process

- **Berry flag:** VAG (S3) — twin 3-way verb coordinations
- **Verbatim phrase:** `define, establish and implement an ICT-related incident management process`
- **Sub-domain touchpoints:** D-04.1
- **Card variant:** DORA-grade

**Variants:**
- **R1:** 3 separate duties.
- **R2:** 3 verbs describe one composite process.

**Recommended Variant:** **R1** — 3 separate duties. 24/7 SOC + SIEM + SOAR + EDR + NDR + UEBA + 5-reg max-SLA routing pipeline.

**Cases citing this card:** C03 (Doc09 card 17).

---

### DORA Art. 26(1) — Threat-Led Penetration Testing (TLPT)

- **Berry flag:** VAG (S3) — frequency
- **Verbatim phrase:** `at least every 3 years`
- **Sub-domain touchpoints:** D-02.4
- **Card variant:** DORA-grade

**Variants:**
- **R1:** 3y baseline + ECB frequency adjustment.
- **R2:** 3y baseline only.

**Recommended Variant:** **R1** — 3y baseline + ECB frequency adjustment. T-005 RESOLVED with parallel cycles + unified scope + findings tracking.

**Cases citing this card:** C03 (Doc09 card 14).

---

### DORA Art. 30(2)+(3)(e)+(f) — Critical ICT third-party contracts (CTPP)

- **Berry flag:** VAG (S3) — sub-clause location
- **Verbatim phrase:** `minimum 9-element list`
- **Sub-domain touchpoints:** D-06.3
- **Card variant:** DORA-grade

**Variants:**
- **R1 (OJ-literal):** Art. 30(2) 9 elements; audit rights + exit strategies 30(3)(e)/(f) CIF-only.
- **R2 (corpus misattribution):** All 9 elements (including audit/exit) per corpus.

**Recommended Variant:** **R1** — OJ-literal. 100% critical vendor contracts with CTPP clauses + audit rights + exit strategies for CIF.

**Cases citing this card:** C03 (Doc09 card 15).

---

## AI Act (3 cards)

### AI-Act Art. 9(1) — Risk management system

- **Berry flag:** VAG (S3)
- **Verbatim phrase:** `appropriate and effective measures`
- **Sub-domain touchpoints:** D-09.1
- **Card variant:** AI-Act-light

**Variants:**
- **R1 (literal):** Lifecycle (5-step cycle per Art. 9(2)).
- **R2 (industry):** Pre-deployment only.

**Recommended Variant:** **R1** — Continuous lifecycle. IPSARA Unified Assessment Framework (T-003 RESOLVED) integrates AI Act Art. 9 + DORA Art. 5 + GDPR DPIA + CRA + NIS 2.

**Cases citing this card:** C03 (Doc09 card 18).

---

### AI-Act Art. 27 — Fundamental Rights Impact Assessment (FRIA)

- **Berry flag:** VAG (S3)
- **Sub-domain touchpoints:** D-09.2
- **Card variant:** AI-Act-light

**Variants:**
- **R1 (industry):** Separate FRIA + DPIA.
- **R2 (C03 T-003 RESOLVED):** Unified IPSARA assessment generates FRIA + DPIA outputs.

**Recommended Variant:** **R2** — IPSARA Unified Assessment Framework. Single underlying assessment, per-regulation output stream.

**Cases citing this card:** C03 (Doc09 card 19).

---

### AI-Act Art. 72 — Post-market monitoring

- **Berry flag:** VAG (S3)
- **Verbatim phrase:** `throughout the lifecycle`
- **Sub-domain touchpoints:** D-10.1
- **Card variant:** AI-Act-light

**Variants:**
- **R1 (industry):** Passive (incident reports only).
- **R2 (literal + AI Office):** Active (continuous model monitoring + drift detection).

**Recommended Variant:** **R2** — Active continuous monitoring. 24/7 SOC + SIEM + AI model monitoring integrated with security monitoring.

**Cases citing this card:** C03 (Doc09 card 20).

---

## Provenance summary

| Case | Cards contributed | Top-20 vs deep-20 |
|------|-------------------:|-------------------|
| Case_01 (GDPR + CRA, MICRO) | 9 (top-20) | Top-20 cards only (severity-sorted) |
| Case_02 (GDPR + CRA + NIS 2, MEDIUM) | 20 (top-20) | Top-20 cards only |
| Case_03 (GDPR + CRA + NIS 2 + DORA + AI Act, MAX) | 20 (top-20) | Top-20 cards only (post-V-04 FIXED) |

The remaining 417 / 1292 / 846 cards in each case's Doc09 (per `ambiguity_cards_total` field in frontmatter) are duplicate or sub-priority instances of the same clauses — kept in the per-case Doc09 for traceability, not consolidated here.

**Cross-cutting themes consolidated at methodology level (per C03 §4):**
- DORA 4h + RTS Art. 6 + NIS 2 24h + CRA 24h + GDPR 72h + AI Act 15d/2d/10d — single SOC pipeline with per-regulation output stream.
- DORA Art. 5-16 ICT risk framework: CRO-owned register aligned with ISO 27005 + NIST CSF 2.0 GV.RM.
- GDPR-CP15 `appropriate technical and organisational measures`: adopt NIST CSF 2.0 mapping as the structured reading.
- GDPR-CP02 `privacy by design` (D-01.1, D-01.3): adopt Art. 25(1) by-design necessity assessment; 4-factor proportionality.

---

## Divergence log

When cases adopted divergent recommended variants for the same clause:

| Clause | Cases diverging | C01 reading | C02 reading | C03 reading | Methodology position |
|--------|----------------|-------------|-------------|-------------|----------------------|
| GDPR-CP15 `timely manner` | C01 vs C02 | R2 (EDPB 7/2019) | R1 (RTO per activity) | R2 (EDPB 7/2019) | R2 default; R1 admissible with per-activity RTO |
| GDPR-RT16 `compelling legitimate grounds` | C01 vs C02 | R2 (loose) | R1 (strict, per-objection) | (not cited) | R1 for MEDIUM+/scale; R2 for MICRO |
