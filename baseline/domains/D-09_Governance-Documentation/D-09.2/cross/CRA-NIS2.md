# D-09.2 — Pair analysis: NIS 2 ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: NIS2 ↔ CRA

**NIS2 article (verbatim, Art. 21(2)(a) + Art. 21(3) sentence 2 + Art. 22(1)):**
> "[Member States shall ensure that essential and important entities take appropriate and proportionate technical, operational and organisational measures to … ] (a) policies on risk analysis and information system security …" — Art. 21(2)(a) NIS 2 (per SR-NIS2-035)
> "When considering which of the measures referred to in paragraph 2, point (d), are appropriate, essential and important entities shall also take into account the results of the coordinated security risk assessments of critical supply chains carried out in accordance with Article 22(1) …" — Art. 21(3) sentence 2 NIS 2 (per SR-NIS2-025)
> "The Cooperation Group may carry out coordinated security risk assessments of specific critical ICT services, ICT systems or ICT products supply chains …" — Art. 22(1) NIS 2 (per SR-NIS2-025)

**CRA article (verbatim, Art. 13(2) + Art. 13(3)):**
> [as quoted above]

**Scope comparison:**
- NIS 2 scope: entity-level operational risk analysis + EU-level coordinated assessments (Art. 22).
- CRA scope: product-level pre-market risk assessment.
- Scope overlap: **Y (when the entity procures CRA-conformant products — the CRA risk assessment is an input to the NIS 2 entity's supplier-risk register).**

**Trigger comparison:**
- NIS 2 trigger: continuous operational analysis + EU-level coordinated assessments.
- CRA trigger: product placement on market + support-period maintenance.
- Trigger alignment: **DIFFERENT**.

**Threshold/timeline comparison:**
- NIS 2: continuous + yearly review.
- CRA: documented + updated during support period.
- Tension: **NONE**.

**Recipient comparison:**
- NIS 2: management body, competent authority, Cooperation Group.
- CRA: MSA.

**Content template comparison:**
- NIS 2: not codified for content (entity-discretionary under Recital 56).
- CRA: Annex VII §3 risk-assessment record.

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** NIS 2 risk analysis is entity-level operational; CRA risk assessment is product-level pre-market. The two regimes meet at the supplier-customer interface — a CRA-conformant product's risk assessment is an input to the NIS 2 entity's supplier-risk register.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y (when the entity procures CRA-conformant products)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce two separate artefacts: NIS 2 Art. 21(2)(a) risk-analysis policy + CRA Art. 13(3) product-level risk assessment as upstream input.

---


## Summary (Domain Analysis)

| NIS2 ↔ CRA | **complementary** | Tension/difference |
|---|---|---|
| **NIS2** (SR-NIS2-035, Art. 21(2)(a); SR-NIS2-025, Art. 21(3) sentence 2 take into account Art. 22 results) | Risk-analysis policy + take-into-account Art. 22 coordinated supply-chain assessments. | |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-035 / SR-NIS2-025 |
| **CRA** (SR-CRA-064, Art. 13(2); SR-CRA-066, Art. 13(3)) | Cybersecurity risk assessment documented + updated during support period. | |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-064 / SR-CRA-066 |

**Why complementary**: NIS 2 risk analysis is entity-level operational; CRA risk assessment is product-level pre-market. The two regimes meet at the supplier-customer interface — a CRA-conformant product's risk assessment is an input to the NIS 2 entity's supplier-risk register.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
43 lines — see ../../_migration_report.md)_

