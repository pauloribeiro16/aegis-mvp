# D-01.1 — Pair analysis: CRA ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: CRA ↔ DORA

**CRA article (verbatim — SR-CRA-001 + SR-CRA-002, Annex I Part I (1) + (2)(e)):**
> Annex I Part I (2)(e) the confidentiality of stored, transmitted or otherwise processed data — personal or other — by encrypting relevant data at rest or in transit using state-of-the-art mechanisms.

**DORA article (verbatim — SR-DORA-001, Art. 9(2)):**
> Art. 9(2) … high standards of availability, authenticity, integrity and confidentiality of data, whether at rest, in use or in transit.

**Scope comparison:**
- CRA scope: product with digital elements (manufacturer is the obligor; data is the object).
- DORA scope: financial entity's ICT (financial entity is the obligor; ICT-supported data is the object).
- Scope overlap: Y (conditional) when the DORA financial entity uses a CRA-regulated product.

**Trigger comparison:**
- CRA: continuous + support-period bound.
- DORA: continuous.
- Trigger alignment: SAME.

**Threshold/timeline comparison:**
- CRA: "state-of-the-art mechanisms" (bench-anchored to support-period commencement + harmonised-standards floor).
- DORA: "high standards" (R1 best practice + R2 published standards).
- Tension: NONE — both target the same state-of-the-art floor in operational practice; CRA is the more precise term because it is anchored to the support-period commencement date.

**Recipient comparison:**
- CRA: MSA + ENISA.
- DORA: national CA + ESAs.

**Classified relationship (from CRDA):** COMPLEMENTARY.

**Verified relationship (after OJ-text analysis):** SAME (CORRECTED — wording only).

**Reasoning:** CRA is the product-side state-of-the-art baseline; DORA is the entity-side "high standards" + classification-driven key-management overlay. They share the at-rest cell, but DORA adds the in-use dimension (which CRA does not treat as a standalone obligation — see SR-DORA-001 ambiguity_notes on the OJ-explicit 3-state). A DORA financial entity using a CRA-regulated product has a stack-merge where the CRA product is the floor and DORA is the overlay (in-use + classification-driven cipher strength).

**Scope-disjoint test:** Y when the DORA financial entity deploys a CRA product; disjoint in baseline (CRA manufacturer ≠ DORA financial entity).

**Downstream implication:** Stack-merge. The CRA product supplies the at-rest floor (Annex I (2)(e)); DORA financial entity adds in-use (PR.DS-10) + classification-driven cipher strength (SR-DORA-003, GV.RM-04) + key custody.

---


## Summary (Domain Analysis)

<!-- pair: CRA,DORA -->
| CRA ↔ DORA | **Complementary** | Tension/difference |
|---|---|---|
| **CRA** (SR-CRA-001 + SR-CRA-002, Annex I Part I (1)+(2)(e)) | State-of-the-art encryption of stored data; "personal or other" | Product-level; state-of-the-art baseline; harmonised-standards anchor |
| **DORA** (SR-DORA-001, Art. 9(2)) | CIA+A 4×3 matrix maintained at "high standards" | Financial entity; ICT-system scope; CIA+A dimensions enumerated |

**Why Complementary**: CRA is product-level (the manufacturer ensures the product protects stored data via state-of-the-art encryption); DORA is entity-level (the financial entity deploys products whose at-rest encryption is operationally maintained). A DORA financial entity deploying CRA-regulated products inherits the product-side baseline but remains responsible for the in-use dimension (which CRA does not cover as a standalone obligation) and for entity-level classification-driven cipher strength (DORA Art. 9(4)(d) layer). The two are complementary, not redundant. → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-001; `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-001



## Deep analysis — Part 3 rendering (differs from Part 1 §1)

##### Pair: CRA ↔ DORA

**CRA article (verbatim — SR-CRA-001 + SR-CRA-002, Annex I Part I (1) + (2)(e)):**
> Annex I Part I (2)(e) the confidentiality of stored, transmitted or otherwise processed data — personal or other — by encrypting relevant data at rest or in transit using state-of-the-art mechanisms.

**DORA article (verbatim — SR-DORA-001, Art. 9(2)):**
> Art. 9(2) … high standards of availability, authenticity, integrity and confidentiality of data, whether at rest, in use or in transit.

**Scope comparison:**
- CRA scope: product with digital elements (manufacturer is the obligor; data is the object).
- DORA scope: financial entity's ICT (financial entity is the obligor; ICT-supported data is the object).
- Scope overlap: Y (conditional) when the DORA financial entity uses a CRA-regulated product.

**Trigger comparison:**
- CRA: continuous + support-period bound.
- DORA: continuous.
- Trigger alignment: SAME.

**Threshold/timeline comparison:**
- CRA: "state-of-the-art mechanisms" (bench-anchored to support-period commencement + harmonised-standards floor).
- DORA: "high standards" (R1 best practice + R2 published standards).
- Tension: NONE — both target the same state-of-the-art floor in operational practice; CRA is the more precise term because it is anchored to the support-period commencement date.

**Recipient comparison:**
- CRA: MSA + ENISA.
- DORA: national CA + ESAs.

**Classified relationship (from CRDA):** COMPLEMENTARY.

**Verified relationship (after OJ-text analysis):** SAME (CORRECTED — wording only).

**Reasoning:** CRA is the product-side state-of-the-art baseline; DORA is the entity-side "high standards" + classification-driven key-management overlay. They share the at-rest cell, but DORA adds the in-use dimension (which CRA does not treat as a standalone obligation — see SR-DORA-001 ambiguity_notes on the OJ-explicit 3-state). A DORA financial entity using a CRA-regulated product has a stack-merge where the CRA product is the floor and DORA is the overlay (in-use + classification-driven cipher strength).

**Scope-disjoint test:** Y when the DORA financial entity deploys a CRA product; disjoint in baseline (CRA manufacturer ≠ DORA financial entity).

**Downstream implication:** Stack-merge. The CRA product supplies the at-rest floor (Annex I (2)(e)); DORA financial entity adds in-use (PR.DS-10) + classification-driven cipher strength (SR-DORA-003, GV.RM-04) + key custody.

---


---


