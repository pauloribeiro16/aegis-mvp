# D-05.1 — Pair analysis: CRA ↔ AI Act

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: CRA ↔ AI_Act

**CRA article (verbatim, Annex I Part I (2)(g)):**
> "On the basis of the cybersecurity risk assessment referred to in Article 13(2) … the product with digital elements shall: … (g) limit its attack surfaces … by means of … the processing of only the data that are adequate, relevant and limited to what is necessary in relation to the intended purpose of the product ('data minimisation')." — CRA Annex I Part I (2)(g)

**AI_Act article (verbatim, Art. 10(1)–(3)):**
> "High-risk AI systems which make use of techniques involving the training of AI models with data shall be developed on the basis of training, validation and testing data sets that meet the quality criteria referred to in paragraphs 2 to 5 whenever such data sets are used." — AI Act Art. 10(1)
>
> "Training, validation and testing data sets shall be relevant, representative and, to the best extent possible, free of errors and complete." — AI Act Art. 10(3)

**Scope comparison:**
- CRA scope: data processed by the product at *runtime* (the product's runtime attack surface).
- AI Act scope: data processed by the *training pipeline* (upstream, lifecycle-stage-specific).
- Scope overlap: **N (typically)** — they operate at different lifecycle stages. The overlap is when AI Act training data flows into a CRA-classified AI-enabled product at runtime, in which case both apply in sequence.

**Trigger comparison:**
- CRA trigger: design / development of a product with digital elements with attack-surface implications.
- AI Act trigger: training / validation / testing of high-risk AI systems.
- Trigger alignment: **DIFFERENT** — upstream (training) vs runtime (execution).

**Threshold/timeline comparison:**
- CRA: no quantitative threshold (qualitative proportionality).
- AI Act: dataset quality criteria "to the best extent possible" — qualitative with explicit statistical dimension.
- Tension: **NONE**.

**Recipient comparison:**
- CRA: market surveillance authority (MSA).
- AI Act: provider + national competent authority + AI Office (post-market phase).

**Content template comparison:**
- CRA: documented in Annex VII §3 risk-assessment record.
- AI Act: dataset quality criteria documented per Art. 10(5) safeguards + Art. 11 technical documentation + Annex IV.

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** CRA minimisation operates at runtime on data the product processes when in use; AI Act Art. 10 quality criteria operate upstream on the training pipeline. They address different data sets at different lifecycle stages. When the same dataset flows through both (training data for a CRA-classified high-risk AI product), the AI Act quality criteria sharpen the CRA runtime minimisation principle. No contradiction; full coverage requires both.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **N (typically)**. They are layered at different lifecycle stages. The only overlap is at the data-flow boundary (training data → runtime data) which is sequential, not concurrent.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce a 3-track minimisation matrix for AI-enabled CRA products (runtime minimisation + personal-data minimisation + training-data quality). Phase 3 case generation must validate that the runtime product does not retain more data than the training-data quality permits to flow into it.

---


## Summary (Domain Analysis)

<!-- pair: CRA,AI_Act -->
| CRA ↔ AI_Act | **complementary** | Tension/difference |
|---|---|---|
| **CRA** (SR-CRA-046, Annex I Part I (2)(g)) | Product-design data minimisation |  |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-046 |
| **AI_Act** (SR-AIACT-004 + SR-AIACT-005, Art. 10(1)–(3)) | Dataset quality criteria + data governance practice |  |
|   → full rationale: `../../../Regulation/AI_Act/02_SecurityRules_NIST.md` SR-AIACT-004, SR-AIACT-005 |

**Why complementary**: CRA minimisation is about data the *product* processes at runtime; AI Act data governance is about data the *training pipeline* uses upstream. They operate at different lifecycle stages: CRA = runtime, AI Act = training. When the same data set flows through both (training data for a CRA-classified high-risk AI product), both minimisations apply in sequence. AI Act's training-data-quality criteria (relevant, representative, free of errors, complete) are a training-stage sharpening of CRA's runtime minimisation principle.



## Deep analysis — Part 3 rendering (differs from Part 1 §1)

##### Pair: CRA ↔ AI_Act

**CRA article (verbatim, Annex I Part I (2)(g)):**
> "On the basis of the cybersecurity risk assessment referred to in Article 13(2) … the product with digital elements shall: … (g) limit its attack surfaces … by means of … the processing of only the data that are adequate, relevant and limited to what is necessary in relation to the intended purpose of the product ('data minimisation')." — CRA Annex I Part I (2)(g)

**AI_Act article (verbatim, Art. 10(1)–(3)):**
> "High-risk AI systems which make use of techniques involving the training of AI models with data shall be developed on the basis of training, validation and testing data sets that meet the quality criteria referred to in paragraphs 2 to 5 whenever such data sets are used." — AI Act Art. 10(1)
>
> "Training, validation and testing data sets shall be relevant, representative and, to the best extent possible, free of errors and complete." — AI Act Art. 10(3)

**Scope comparison:**
- CRA scope: data processed by the product at *runtime* (the product's runtime attack surface).
- AI Act scope: data processed by the *training pipeline* (upstream, lifecycle-stage-specific).
- Scope overlap: **N (typically)** — they operate at different lifecycle stages. The overlap is when AI Act training data flows into a CRA-classified AI-enabled product at runtime, in which case both apply in sequence.

**Trigger comparison:**
- CRA trigger: design / development of a product with digital elements with attack-surface implications.
- AI Act trigger: training / validation / testing of high-risk AI systems.
- Trigger alignment: **DIFFERENT** — upstream (training) vs runtime (execution).

**Threshold/timeline comparison:**
- CRA: no quantitative threshold (qualitative proportionality).
- AI Act: dataset quality criteria "to the best extent possible" — qualitative with explicit statistical dimension.
- Tension: **NONE**.

**Recipient comparison:**
- CRA: market surveillance authority (MSA).
- AI Act: provider + national competent authority + AI Office (post-market phase).

**Content template comparison:**
- CRA: documented in Annex VII §3 risk-assessment record.
- AI Act: dataset quality criteria documented per Art. 10(5) safeguards + Art. 11 technical documentation + Annex IV.

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** CRA minimisation operates at runtime on data the product processes when in use; AI Act Art. 10 quality criteria operate upstream on the training pipeline. They address different data sets at different lifecycle stages. When the same dataset flows through both (training data for a CRA-classified high-risk AI product), the AI Act quality criteria sharpen the CRA runtime minimisation principle. No contradiction; full coverage requires both.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **N (typically)**. They are layered at different lifecycle stages. The only overlap is at the data-flow boundary (training data → runtime data) which is sequential, not concurrent.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce a 3-track minimisation matrix for AI-enabled CRA products (runtime minimisation + personal-data minimisation + training-data quality). Phase 3 case generation must validate that the runtime product does not retain more data than the training-data quality permits to flow into it.

---


---


