# D-03.2 — Pair analysis: CRA ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: CRA ↔ DORA

**CRA article (verbatim):**
> Annex I Part I (2)(d) requires protection from unauthorised access by appropriate control mechanisms, including but not limited to authentication, identity, or access-management systems; the "including but not limited to" clause keeps the floor open to other technical means while naming the three substantive control families.

**DORA article (verbatim):**
> Art. 9(4)(d) requires financial entities to implement policies and protocols for strong authentication mechanisms, based on relevant standards and dedicated control systems, and protection measures of cryptographic keys whereby data is encrypted based on results of approved data classification and ICT risk assessment processes.

**Scope comparison:**
- CRA scope: product-level appropriate control mechanisms.
- DORA scope: financial-entity strong authentication and key protection.
- Scope overlap: Conditional where a DORA financial entity deploys or manufactures a CRA product.

**Trigger comparison:**
- CRA trigger: continuous product security-design obligation.
- DORA trigger: continuous financial-entity ICT-control obligation.
- Trigger alignment: PARTIAL.

**Threshold/timeline comparison:**
- CRA: appropriate controls; authentication is one of several admitted mechanisms.
- DORA: strong authentication based on standards and dedicated controls.
- Tension: NONE.

**Recipient comparison:**
- CRA: manufacturer documentation and product users.
- DORA: financial-entity governance and competent authority.

**Content template comparison:**
- CRA: product control-mechanism records and risk assessment.
- DORA: strong-authentication standard, control-system and key-protection evidence.

**Classified relationship (from CRDA):** COMPLEMENTARY

**Verified relationship (after OJ-text analysis):** SAME — COMPLEMENTARY

**Reasoning (1-2 paragraphs):** CRA's product-side controls and DORA's financial-entity-side controls are layered. The DORA OJ text does not say "multi-factor" but does say "strong authentication"; CRA's Annex I (2)(d) does not require authentication specifically. A common implementation satisfies both, with DORA requiring governance depth that CRA's product-side text does not reach.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect**; it should be "scope-disjoint" in baseline. This pair was not classified contradictory.

**Downstream implication (1-2 sentences):** Doc 07 should treat CRA as the product baseline and DORA as the financial-sector deployer depth layer.


## Summary (Domain Analysis)

<!-- pair: CRA,DORA -->
| CRA ↔ DORA | **Complementary** | Tension/difference |
|---|---|---|
| **CRA** (SR-CRA-016, Annex I Part I (2)(d) — partial) | "Appropriate control mechanisms, may include authentication" | Product-level; "may include" + 3-way OR; PR.AA-05 + PR.AA-06 + DE.CM-09 |
| **DORA** (SR-DORA-002, Art. 9(4)(d)) | Strong authentication mechanisms (dominant EBA reading: MFA) | Financial entity; strong-authentication; PR.AA-03 + PR.AA-04 |

**Why Complementary**: CRA's "may include" framing admits MFA as one of several choices; DORA's "strong authentication" is the financial-sector anchor. A DORA financial entity using CRA-regulated products is jointly bound: CRA's product-level "appropriate control mechanisms" + DORA's entity-level strong-authentication. The two converge on PR.AA-03 (users/services/hardware authenticated) as the shared anchor (CRA via the 3-way OR + DORA's explicit strong-authentication). **Caveat:** CRA's "may include" creates a partial-coverage flag in `01_SecurityObjectives.md` §D-03.2; the AEGIS taxonomy notes CRA as the sole authority for explicit MFA mandates but the CRA OJ text is not as explicit as NIS 2 or DORA. → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-016; `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-002



## Deep analysis — Part 3 rendering (differs from Part 1 §1)

##### Pair: CRA ↔ DORA

**CRA article (verbatim):**
> Annex I Part I (2)(d) requires protection from unauthorised access by appropriate control mechanisms, including but not limited to authentication, identity, or access-management systems; the "including but not limited to" clause keeps the floor open to other technical means while naming the three substantive control families.

**DORA article (verbatim):**
> Art. 9(4)(d) requires financial entities to implement policies and protocols for strong authentication mechanisms, based on relevant standards and dedicated control systems, and protection measures of cryptographic keys whereby data is encrypted based on results of approved data classification and ICT risk assessment processes.

**Scope comparison:**
- CRA scope: product-level appropriate control mechanisms.
- DORA scope: financial-entity strong authentication and key protection.
- Scope overlap: Conditional where a DORA financial entity deploys or manufactures a CRA product.

**Trigger comparison:**
- CRA trigger: continuous product security-design obligation.
- DORA trigger: continuous financial-entity ICT-control obligation.
- Trigger alignment: PARTIAL.

**Threshold/timeline comparison:**
- CRA: appropriate controls; authentication is one of several admitted mechanisms.
- DORA: strong authentication based on standards and dedicated controls.
- Tension: NONE.

**Recipient comparison:**
- CRA: manufacturer documentation and product users.
- DORA: financial-entity governance and competent authority.

**Content template comparison:**
- CRA: product control-mechanism records and risk assessment.
- DORA: strong-authentication standard, control-system and key-protection evidence.

**Classified relationship (from CRDA):** COMPLEMENTARY

**Verified relationship (after OJ-text analysis):** SAME — COMPLEMENTARY

**Reasoning (1-2 paragraphs):** CRA's product-side controls and DORA's financial-entity-side controls are layered. The DORA OJ text does not say "multi-factor" but does say "strong authentication"; CRA's Annex I (2)(d) does not require authentication specifically. A common implementation satisfies both, with DORA requiring governance depth that CRA's product-side text does not reach.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect**; it should be "scope-disjoint" in baseline. This pair was not classified contradictory.

**Downstream implication (1-2 sentences):** Doc 07 should treat CRA as the product baseline and DORA as the financial-sector deployer depth layer.


---
