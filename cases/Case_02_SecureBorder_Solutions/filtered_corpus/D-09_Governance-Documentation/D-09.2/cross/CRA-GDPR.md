# D-09.2 — Pair analysis: GDPR ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ CRA

**GDPR article (verbatim, Art. 35(1) + Art. 35(7)):**
> [as quoted above]

**CRA article (verbatim, Art. 13(2) + Art. 13(3) + Art. 13(4) sentence 2):**
> [as quoted above]
> "The cybersecurity risk assessment referred to in paragraph 2 shall be part of, or combined with, the risk assessment required by other Union legal acts applicable to the product with digital elements." — Art. 13(4) sentence 2 CRA

**Scope comparison:**
- GDPR scope: pre-launch DPIA for high-risk personal-data processing.
- CRA scope: pre-market + support-period cybersecurity risk assessment with 6-phase lifecycle propagation.
- Scope overlap: **Y (when the CRA-regulated product processes personal data).**

**Trigger comparison:**
- GDPR trigger: high-risk processing event.
- CRA trigger: product placement on market + support-period maintenance.
- Trigger alignment: **DIFFERENT** (pre-launch for personal data vs. pre-market for product).

**Threshold/timeline comparison:**
- GDPR: DPIA before processing + review on change of risk.
- CRA: documented + updated during support period.
- Tension: **NONE**.

**Recipient comparison:**
- GDPR: DPA.
- CRA: MSA.

**Content template comparison:**
- GDPR: 4-item Art. 35(7) content.
- CRA: Annex VII §3 risk-assessment record + Annex I Part I (2) applicability mapping.

**Classified relationship (from CRDA):** DIFFERENT-PERSPECTIVE
**Verified relationship (after OJ-text analysis):** **SAME — DIFFERENT-PERSPECTIVE**
**Reasoning:** GDPR DPIA assesses impact on data subjects' rights and freedoms; CRA cybersecurity risk assessment assesses cybersecurity risks to the product and its users. The two risk objects differ (rights-and-freedoms vs. cybersecurity). For a CRA-regulated product that processes personal data, both assessments are required — but the OJ does not require cross-referencing. The CRA Art. 13(4) sentence 2 carve-out for AI Act Art. 9 unified-risk-assessment does not extend to GDPR DPIA.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y (when the CRA-regulated product processes personal data)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce two separate artefacts: GDPR Art. 35 DPIA + CRA Art. 13(3) cybersecurity risk assessment. No OJ-level consolidation rule for the GDPR/CRA pair.

---


## Summary (Domain Analysis)

<!-- pair: GDPR,CRA -->
| GDPR ↔ CRA | **different-perspective** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-045, Art. 35(1)-(4); SR-GDPR-046, Art. 35(7)) | DPIA with four Art. 35(7) content items. | |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-045 / SR-GDPR-046 |
| **CRA** (SR-CRA-064, Art. 13(2); SR-CRA-065, Art. 13(2) risk-assessment propagation across 6 phases; SR-CRA-066, Art. 13(3) documented + updated risk assessment; SR-CRA-079, Art. 13(3) documented/updated; SR-CRA-080, Annex VII §3 risk-assessment record; SR-CRA-081, systematic always-current record) | Cybersecurity risk assessment documented + updated during support period; Annex I Part I (2) applicability mapping. | |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-064 / SR-CRA-065 / SR-CRA-066 / SR-CRA-079 / SR-CRA-080 / SR-CRA-081 |

**Why different-perspective + CRITICAL TENSION**: GDPR DPIA assesses impact on data subjects' rights and freedoms; CRA cybersecurity risk assessment assesses cybersecurity risks to the product and its users. The two risk objects differ (rights-and-freedoms vs. cybersecurity). For a CRA-regulated product that processes personal data, both assessments are required — but the OJ does not require cross-referencing between the two. The CRA Art. 13(4) sentence 2 carve-out for AI Act Art. 9 unified-risk-assessment does not extend to GDPR DPIA.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_