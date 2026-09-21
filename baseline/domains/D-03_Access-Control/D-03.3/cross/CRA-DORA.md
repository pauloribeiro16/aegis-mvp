# D-03.3 — Pair analysis: CRA ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: CRA ↔ DORA

**CRA article (verbatim):**
> Annex I Part I (2)(d) requires protection from unauthorised access through appropriate control mechanisms. Annex I Part I (2)(j) limits attack surfaces, including external interfaces.

**DORA article (verbatim):**
> Art. 9(4)(c) requires financial entities to implement policies that limit physical or logical access to information assets and ICT assets to what is required for legitimate and approved functions and activities only.

**Scope comparison:**
- CRA scope: product-level access control and attack-surface limitation.
- DORA scope: financial-entity physical/logical access to information assets and ICT assets.
- Scope overlap: Conditional where a DORA financial entity deploys or manufactures a CRA product.

**Trigger comparison:**
- CRA trigger: continuous product access-control duty.
- DORA trigger: continuous financial-entity ICT-access-policy duty.
- Trigger alignment: PARTIAL.

**Threshold/timeline comparison:**
- CRA: limited to authenticated and authorised users, services and hardware.
- DORA: access limited to legitimate and approved functions and activities only.
- Tension: NONE.

**Recipient comparison:**
- CRA: manufacturer documentation, product users and market surveillance.
- DORA: financial-entity governance and competent authority.

**Content template comparison:**
- CRA: product access-control records and attack-surface-limitation evidence.
- DORA: legitimate-and-approved function register and `only` qualifier evidence.

**Classified relationship (from CRDA):** COMPLEMENTARY

**Verified relationship (after OJ-text analysis):** SAME — COMPLEMENTARY

**Reasoning (1-2 paragraphs):** The OJ text supports complementarity. CRA's product boundary is one layer; DORA's entity boundary is the next. The DORA `only` qualifier is more demanding than CRA's `limited to authenticated and authorised users, services, and hardware` and is the binding floor where they overlap.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect**; it should be "scope-disjoint" in baseline. This pair was not classified contradictory.

**Downstream implication (1-2 sentences):** Doc 07 should keep the CRA product primitive and the DORA entity register linked, with DORA as the binding floor.


## Summary (Domain Analysis)

<!-- pair: CRA,DORA -->
| CRA ↔ DORA | **Complementary** | Tension/difference |
|---|---|---|
| **CRA** (SR-CRA-017 + SR-CRA-024, Annex I Part I (2)(d) + (2)(j)) | Access limited to authenticated + authorised users/services/hardware; attack-surface limitation | Product-level; PR.AA-05 + PR.AA-06 + DE.CM-09 |
| **DORA** (SR-DORA-006, Art. 9(4)(c)) | Access limited to "legitimate and approved functions and activities only" | Financial entity; "legitimate and approved" + "only" qualifier; PR.AA-05 |

**Why Complementary**: CRA's product-level access control + attack-surface limitation is the product-side invariant; DORA's Art. 9(4)(c) is the financial-entity-side access control. A DORA financial entity using CRA-regulated products is jointly bound: the product-side access control (CRA) + the entity-side access control (DORA). The two are complementary, with the boundary at product users (CRA) vs staff/services (DORA), and converge on PR.AA-05 (least privilege) as the shared anchor. The DORA "only" qualifier is operationally more demanding than CRA's `limited to authenticated and authorised` framing. → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-017 + SR-CRA-024; `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-006



## Deep analysis — Part 3 rendering (differs from Part 1 §1)

##### Pair: CRA ↔ DORA

**CRA article (verbatim):**
> Annex I Part I (2)(d) requires protection from unauthorised access through appropriate control mechanisms. Annex I Part I (2)(j) limits attack surfaces, including external interfaces.

**DORA article (verbatim):**
> Art. 9(4)(c) requires financial entities to implement policies that limit physical or logical access to information assets and ICT assets to what is required for legitimate and approved functions and activities only.

**Scope comparison:**
- CRA scope: product-level access control and attack-surface limitation.
- DORA scope: financial-entity physical/logical access to information assets and ICT assets.
- Scope overlap: Conditional where a DORA financial entity deploys or manufactures a CRA product.

**Trigger comparison:**
- CRA trigger: continuous product access-control duty.
- DORA trigger: continuous financial-entity ICT-access-policy duty.
- Trigger alignment: PARTIAL.

**Threshold/timeline comparison:**
- CRA: limited to authenticated and authorised users, services and hardware.
- DORA: access limited to legitimate and approved functions and activities only.
- Tension: NONE.

**Recipient comparison:**
- CRA: manufacturer documentation, product users and market surveillance.
- DORA: financial-entity governance and competent authority.

**Content template comparison:**
- CRA: product access-control records and attack-surface-limitation evidence.
- DORA: legitimate-and-approved function register and `only` qualifier evidence.

**Classified relationship (from CRDA):** COMPLEMENTARY

**Verified relationship (after OJ-text analysis):** SAME — COMPLEMENTARY

**Reasoning (1-2 paragraphs):** The OJ text supports complementarity. CRA's product boundary is one layer; DORA's entity boundary is the next. The DORA `only` qualifier is more demanding than CRA's `limited to authenticated and authorised users, services, and hardware` and is the binding floor where they overlap.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect**; it should be "scope-disjoint" in baseline. This pair was not classified contradictory.

**Downstream implication (1-2 sentences):** Doc 07 should keep the CRA product primitive and the DORA entity register linked, with DORA as the binding floor.


---


