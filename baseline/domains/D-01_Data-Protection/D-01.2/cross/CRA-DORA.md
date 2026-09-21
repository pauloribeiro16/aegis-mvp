# D-01.2 — Pair analysis: CRA ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: CRA ↔ DORA

**CRA article (verbatim — SR-CRA-003, Annex I Part I (2)(e)+(j)):**
> Annex I Part I (2)(e) … encrypting relevant data at rest or in transit using state-of-the-art mechanisms. Annex I Part I (2)(j) limit attack surfaces.

**DORA article (verbatim — SR-DORA-001, Art. 9(2)):**
> Art. 9(2) … high standards of availability, authenticity, integrity and confidentiality of data, whether at rest, in use or in transit.

**Scope comparison:**
- CRA: product with digital elements (product-level).
- DORA: financial entity's ICT (entity-level).
- Scope overlap: Y (conditional) when a DORA financial entity uses a CRA-regulated product that transmits data.

**Trigger comparison:**
- CRA: continuous.
- DORA: continuous.
- Trigger alignment: SAME.

**Threshold/timeline comparison:**
- CRA: state-of-the-art + harm-surf-limit.
- DORA: high standards.
- Tension: NONE.

**Classified relationship (from CRDA):** COMPLEMENTARY.

**Verified relationship (after OJ-text analysis):** SAME (CORRECTED — wording only).

**Reasoning:** CRA product-side state-of-the-art in-transit + attack-surface-limitation is the floor; DORA entity-side adds the entity-level transport-security governance (zone trust, mTLS architecture, peer-peer authentication between internal services). PR.DS-02 + PR.IR-01 are shared anchors.

**Scope-disjoint test:** Y (DORA financial entity using CRA product); disjoint in baseline (manufacturer ≠ financial entity).

**Downstream implication:** Stack-merge — CRA product supplies the in-transit cipher-suite and surface-limitation baseline; DORA entity adds the deployment governance.

---


## Summary (Domain Analysis)

| CRA ↔ DORA | **Complementary** | Tension/difference |
|---|---|---|
| **CRA** (SR-CRA-003, Annex I Part I (2)(e)+(j)) | State-of-the-art in-transit encryption at the product level | Product-level; PR.DS-02 + PR.IR-01 |
| **DORA** (SR-DORA-001, Art. 9(2)) | CIA+A in-transit at the financial-entity ICT system level | Financial entity; in-transit as one cell of the 4×3 matrix |

**Why Complementary**: CRA's product-level in-transit state-of-the-art baseline (Annex I (2)(e)) + attack-surface limitation (Annex I (2)(j)) is the floor for any product used by a DORA financial entity. The DORA financial entity retains responsibility for entity-level transport-security choices (mTLS architecture, network segmentation, zone trust boundaries) above the CRA product baseline. PR.DS-02 + PR.IR-01 are shared; the actor split is product (CRA) vs deployment (DORA). → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-003; `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-001



## Deep analysis — Part 3 rendering (differs from Part 1 §1)

##### Pair: CRA ↔ DORA

**CRA article (verbatim — SR-CRA-003, Annex I Part I (2)(e)+(j)):**
> Annex I Part I (2)(e) … encrypting relevant data at rest or in transit using state-of-the-art mechanisms. Annex I Part I (2)(j) limit attack surfaces.

**DORA article (verbatim — SR-DORA-001, Art. 9(2)):**
> Art. 9(2) … high standards of availability, authenticity, integrity and confidentiality of data, whether at rest, in use or in transit.

**Scope comparison:**
- CRA: product with digital elements (product-level).
- DORA: financial entity's ICT (entity-level).
- Scope overlap: Y (conditional) when a DORA financial entity uses a CRA-regulated product that transmits data.

**Trigger comparison:**
- CRA: continuous.
- DORA: continuous.
- Trigger alignment: SAME.

**Threshold/timeline comparison:**
- CRA: state-of-the-art + harm-surf-limit.
- DORA: high standards.
- Tension: NONE.

**Classified relationship (from CRDA):** COMPLEMENTARY.

**Verified relationship (after OJ-text analysis):** SAME (CORRECTED — wording only).

**Reasoning:** CRA product-side state-of-the-art in-transit + attack-surface-limitation is the floor; DORA entity-side adds the entity-level transport-security governance (zone trust, mTLS architecture, peer-peer authentication between internal services). PR.DS-02 + PR.IR-01 are shared anchors.

**Scope-disjoint test:** Y (DORA financial entity using CRA product); disjoint in baseline (manufacturer ≠ financial entity).

**Downstream implication:** Stack-merge — CRA product supplies the in-transit cipher-suite and surface-limitation baseline; DORA entity adds the deployment governance.

---


---


