# D-04.2 — Pair analysis: CRA ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: CRA ↔ DORA

**CRA article (verbatim):**
> Annex I Part I (2)(h) requires products to protect the availability of essential and basic functions — also after an incident — including through resilience and mitigation measures against denial-of-service attacks. Annex I Part I (2)(i) requires products to minimise the negative impact by the products themselves or connected devices on the availability of services provided by other devices or networks. Annex I Part I (2)(k) requires reducing the impact of an incident using appropriate exploitation-mitigation mechanisms and techniques.

**DORA article (verbatim):**
> Art. 11(1) requires financial entities to put in place a comprehensive ICT business continuity policy. Art. 11(2) requires financial entities to implement the ICT business continuity policy through dedicated, appropriate and documented arrangements, plans, procedures and mechanisms aiming to (a)–(e).

**Scope comparison:**
- CRA scope: product-level post-incident availability and cross-product impact limitation.
- DORA scope: financial-entity BC arrangements and BC policy including containment plans.
- Scope overlap: Conditional where a DORA financial entity deploys CRA products.

**Trigger comparison:**
- CRA trigger: continuous product design and post-incident availability preservation.
- DORA trigger: ICT-related incident under Art. 17(1).
- Trigger alignment: DIFFERENT.

**Threshold/timeline comparison:**
- CRA: post-incident availability and exploitation mitigation.
- DORA: dedicated plans activated without delay per Art. 11(2)(c).
- Tension: NONE.

**Recipient comparison:**
- CRA: manufacturer documentation, product users and market surveillance.
- DORA: competent authority and clients.

**Content template comparison:**
- CRA: product resilience and exploitation-mitigation architecture.
- DORA: dedicated plans, procedures, mechanisms per Art. 11(2) chapeau + (a)–(e).

**Classified relationship (from CRDA):** COMPLEMENTARY

**Verified relationship (after OJ-text analysis):** SAME — COMPLEMENTARY

**Reasoning (1-2 paragraphs):** The OJ text supports complementarity. CRA product contains the incident inside its boundary; DORA entity contains the incident across its ICT estate. Both layers are required and complementary.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect**; it should be "scope-disjoint" in baseline. This pair was not classified contradictory.

**Downstream implication (1-2 sentences):** Doc 07 should record CRA product resilience evidence as one input feeding the DORA entity BC arrangements, with the entity plan remaining the binding artefact.


## Summary (Domain Analysis)

<!-- pair: CRA,DORA -->
| CRA ↔ DORA | **complementary** | Tension/difference |
|---|---|---|
| **CRA** (SR-CRA-043 + SR-CRA-044, Annex I Part I (2)(h)/(i)) | Product-level post-incident availability + cross-product impact containment |  |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-043, SR-CRA-044 |
| **DORA** (SR-DORA-013 + SR-DORA-014, Art. 11(1)–(3)) | Entity-level BC framework + response/recovery plans |  |
|   → full rationale: `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-013, SR-DORA-014 |

**Why complementary**: CRA product contains the incident inside its boundary; DORA entity contains the incident across its ICT estate (including the CRA product's deployer-side integration). Both layers are required and complementary.



## Deep analysis — Part 3 rendering (differs from Part 1 §1)

##### Pair: CRA ↔ DORA

**CRA article (verbatim):**
> Annex I Part I (2)(h) requires products to protect the availability of essential and basic functions — also after an incident — including through resilience and mitigation measures against denial-of-service attacks. Annex I Part I (2)(i) requires products to minimise the negative impact by the products themselves or connected devices on the availability of services provided by other devices or networks. Annex I Part I (2)(k) requires reducing the impact of an incident using appropriate exploitation-mitigation mechanisms and techniques.

**DORA article (verbatim):**
> Art. 11(1) requires financial entities to put in place a comprehensive ICT business continuity policy. Art. 11(2) requires financial entities to implement the ICT business continuity policy through dedicated, appropriate and documented arrangements, plans, procedures and mechanisms aiming to (a)–(e).

**Scope comparison:**
- CRA scope: product-level post-incident availability and cross-product impact limitation.
- DORA scope: financial-entity BC arrangements and BC policy including containment plans.
- Scope overlap: Conditional where a DORA financial entity deploys CRA products.

**Trigger comparison:**
- CRA trigger: continuous product design and post-incident availability preservation.
- DORA trigger: ICT-related incident under Art. 17(1).
- Trigger alignment: DIFFERENT.

**Threshold/timeline comparison:**
- CRA: post-incident availability and exploitation mitigation.
- DORA: dedicated plans activated without delay per Art. 11(2)(c).
- Tension: NONE.

**Recipient comparison:**
- CRA: manufacturer documentation, product users and market surveillance.
- DORA: competent authority and clients.

**Content template comparison:**
- CRA: product resilience and exploitation-mitigation architecture.
- DORA: dedicated plans, procedures, mechanisms per Art. 11(2) chapeau + (a)–(e).

**Classified relationship (from CRDA):** COMPLEMENTARY

**Verified relationship (after OJ-text analysis):** SAME — COMPLEMENTARY

**Reasoning (1-2 paragraphs):** The OJ text supports complementarity. CRA product contains the incident inside its boundary; DORA entity contains the incident across its ICT estate. Both layers are required and complementary.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect**; it should be "scope-disjoint" in baseline. This pair was not classified contradictory.

**Downstream implication (1-2 sentences):** Doc 07 should record CRA product resilience evidence as one input feeding the DORA entity BC arrangements, with the entity plan remaining the binding artefact.


---


