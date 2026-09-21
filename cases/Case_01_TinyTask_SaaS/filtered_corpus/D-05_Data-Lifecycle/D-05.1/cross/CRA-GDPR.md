# D-05.1 — Pair analysis: GDPR ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ CRA

**GDPR article (verbatim, Art. 5(1)(c) + Art. 6(4)):**
> "Personal data shall be adequate, relevant and limited to what is necessary in relation to the purposes for which they are processed ('data minimisation')." — Art. 5(1)(c) GDPR
>
> "Where the processing for a purpose other than that for which the personal data have been collected is not based on the data subject's consent … the controller shall, in order to ascertain whether processing for another purpose is compatible with the purpose for which the personal data are initially collected, take into account, inter alia: (a) any link between the purposes … (b) the context of collection … (c) the nature of the personal data … (d) the possible consequences … (e) the existence of appropriate safeguards." — Art. 6(4) GDPR

**CRA article (verbatim, Annex I Part I (2)(g) + Art. 13(3) sentence 2):**
> "On the basis of the cybersecurity risk assessment referred to in Article 13(2) … the product with digital elements shall: … (g) limit its attack surfaces, including attack surfaces of third-party components integrated into the product, by means of an internal architecture that minimises the exposure of the product's attack surfaces and the data processed by it, including by means of the processing of only the data that are adequate, relevant and limited to what is necessary in relation to the intended purpose of the product ('data minimisation')." — CRA Annex I Part I (2)(g)
>
> "The risk assessment shall be performed by the manufacturer and shall … take into account … the intended purpose of the product with digital elements, as well as the circumstances of use … including the reasonably foreseeable use thereof." — CRA Art. 13(3) sentence 2

**Scope comparison:**
- GDPR scope: personal data, processed by a controller / processor, calibrated to the controller's specified purposes.
- CRA scope: data processed by a product with digital elements (personal or other — Art. 3(1) product + Annex I (2)(g) generic data), calibrated to the product's intended purpose.
- Scope overlap: **Conditional (Y when the same dataset contains personal data and is processed by a CRA-classified product at runtime)**.

**Trigger comparison:**
- GDPR trigger: collection or further processing of personal data.
- CRA trigger: design / development of a product with digital elements with attack-surface implications.
- Trigger alignment: **DIFFERENT** — GDPR is triggered by data-processing events, CRA by product-design events. They overlap when the product's runtime data is personal data.

**Threshold/timeline comparison:**
- GDPR: no quantitative threshold — proportionality is qualitative ("adequate, relevant, limited").
- CRA: no quantitative threshold — Annex I Part I (2)(g) is qualitative ("adequate, relevant, limited").
- Tension: **NONE (scope-conditional; thresholds align qualitatively)**.

**Recipient comparison:**
- GDPR: supervisory authority (DPA), data subject.
- CRA: market surveillance authority (MSA), conformity-assessment body (notified body or self-assessment).

**Content template comparison:**
- GDPR: not codified — controller demonstrates Art. 5(2) accountability via documented necessity assessment (often via DPIA Art. 35).
- CRA: documented in Annex VII §3 risk-assessment record + Annex I Part I (2)(g) technical file.

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** Both provisions use the identical operative language "adequate, relevant and limited to what is necessary" — verbatim wording overlap (GDPR Art. 5(1)(c); CRA Annex I Part I (2)(g)). CRA Annex I Part I (2)(g) explicitly extends GDPR's "data minimisation" terminology to products, anchored to the manufacturer-defined product purpose (Art. 3(23) `intended purpose`), while GDPR anchors to controller-defined purposes. When a CRA-compliant product processes personal data, both minimisation tests apply and the stricter operational interpretation binds. CRA does not require the Art. 6(4) compatibility test, so the residual GDPR-only requirement is the change-of-purpose assessment.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Conditional (Y when the same personal-data stream flows through a CRA-classified product at runtime)**. The two obligations stack rather than contradict.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce a 2-track minimisation matrix: (1) GDPR Art. 5(1)(c) + Art. 6(4) personal-data minimisation with compatibility assessment; (2) CRA Annex I Part I (2)(g) product-data minimisation. For CRA-regulated products processing personal data, the union applies. The Art. 6(4) compatibility test is GDPR-only and must be retained as a residual obligation.

---


## Summary (Domain Analysis)

<!-- pair: GDPR,CRA -->
| GDPR ↔ CRA | **complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-025, Art. 5(1)(c) + Art. 6(4)) | Purpose-bound data minimisation with Art. 6(4) compatibility assessment |  |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-025 |
| **CRA** (SR-CRA-046, Annex I Part I (2)(g) + Art. 13(3) sentence 2 + Art. 3(23)) | Product-design data minimisation adequate to intended purpose |  |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-046 |

**Why complementary**: GDPR minimisation is purpose-driven (controller defines purpose, then minimises data); CRA minimisation is intended-purpose-driven (manufacturer defines product purpose, then minimises data processed). When the same data is processed by a CRA-compliant product deployed by a GDPR controller, both minimisations apply and the stricter operational interpretation binds. CRA explicitly does not require the Art. 6(4) compatibility test; GDPR's Art. 6(4) compatibility assessment is the residual GDPR-only requirement.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
45 lines — see ../../_migration_report.md)_

