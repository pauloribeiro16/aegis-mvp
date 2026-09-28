# D-03.1 — Pair analysis: CRA ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: CRA ↔ DORA

**CRA article (verbatim):**
> Annex I Part I (2)(d) requires protection from unauthorised access by appropriate control mechanisms, including but not limited to authentication, identity, or access-management systems; the "including but not limited to" clause keeps the floor open to other technical means while naming the three substantive control families.

**DORA article (verbatim):**
> Art. 9(4)(d) requires financial entities to implement policies and protocols for strong authentication mechanisms, based on relevant standards and dedicated control systems, and protection measures of cryptographic keys whereby data is encrypted based on results of approved data classification and ICT risk assessment processes.

**Scope comparison:**
- CRA scope: product-level unauthorised-access protection.
- DORA scope: financial-entity authentication and cryptographic-key policy.
- Scope overlap: Conditional when a DORA financial entity deploys or manufactures a CRA product.

**Trigger comparison:**
- CRA trigger: continuous product security obligation.
- DORA trigger: continuous financial-entity ICT policy obligation.
- Trigger alignment: PARTIAL.

**Threshold/timeline comparison:**
- CRA: appropriate control mechanisms.
- DORA: strong authentication based on standards and dedicated controls.
- Tension: NONE.

**Recipient comparison:**
- CRA: product users and market-surveillance evidence.
- DORA: financial supervisor evidence and internal governance.

**Content template comparison:**
- CRA: authentication/identity/IAM product controls.
- DORA: strong-authentication, key-protection and data-classification policies.

**Classified relationship (from CRDA):** COMPLEMENTARY

**Verified relationship (after OJ-text analysis):** SAME — COMPLEMENTARY

**Reasoning (1-2 paragraphs):** CRA is product-facing; DORA is financial-entity-facing. The same authentication primitive may serve both, but CRA does not impose the financial-sector governance depth that DORA requires. The CRDA classification is supported because the obligations stack without contradiction.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect**; it should be "scope-disjoint" in baseline. This pair was not classified contradictory.

**Downstream implication (1-2 sentences):** Doc 07 should require deployer-side DORA authentication governance in addition to CRA product controls.


## Summary (Domain Analysis)

<!-- pair: CRA,DORA -->
| CRA ↔ DORA | **Complementary** | Tension/difference |
|---|---|---|
| **CRA** (SR-CRA-023, Annex I Part I (2)(d) + Art. 13(15)) | Authentication identity + unique product identification | Product-level; PR.AA-01 + ID.AM-01 |
| **DORA** (SR-DORA-002, Art. 9(4)(d)) | Strong authentication + key protection; identity is one dimension | Financial entity; PR.AA-03 + PR.AA-04 |

**Why Complementary**: CRA's product-level identity management (users, services, integrated components) + unique product identification (type/batch/serial) is the product-side invariant; DORA's strong-authentication is the entity-side layer. A DORA financial entity using CRA-regulated products is jointly bound: product-side identity management (CRA) + entity-side strong-authentication (DORA). The two are complementary, with the boundary at product users (CRA) vs staff/services (DORA). → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-023; `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-002



## Deep analysis — Part 3 rendering (differs from Part 1 §1)

##### Pair: CRA ↔ DORA

**CRA article (verbatim):**
> Annex I Part I (2)(d) requires protection from unauthorised access by appropriate control mechanisms, including but not limited to authentication, identity, or access-management systems; the "including but not limited to" clause keeps the floor open to other technical means while naming the three substantive control families.

**DORA article (verbatim):**
> Art. 9(4)(d) requires financial entities to implement policies and protocols for strong authentication mechanisms, based on relevant standards and dedicated control systems, and protection measures of cryptographic keys whereby data is encrypted based on results of approved data classification and ICT risk assessment processes.

**Scope comparison:**
- CRA scope: product-level unauthorised-access protection.
- DORA scope: financial-entity authentication and cryptographic-key policy.
- Scope overlap: Conditional when a DORA financial entity deploys or manufactures a CRA product.

**Trigger comparison:**
- CRA trigger: continuous product security obligation.
- DORA trigger: continuous financial-entity ICT policy obligation.
- Trigger alignment: PARTIAL.

**Threshold/timeline comparison:**
- CRA: appropriate control mechanisms.
- DORA: strong authentication based on standards and dedicated controls.
- Tension: NONE.

**Recipient comparison:**
- CRA: product users and market-surveillance evidence.
- DORA: financial supervisor evidence and internal governance.

**Content template comparison:**
- CRA: authentication/identity/IAM product controls.
- DORA: strong-authentication, key-protection and data-classification policies.

**Classified relationship (from CRDA):** COMPLEMENTARY

**Verified relationship (after OJ-text analysis):** SAME — COMPLEMENTARY

**Reasoning (1-2 paragraphs):** CRA is product-facing; DORA is financial-entity-facing. The same authentication primitive may serve both, but CRA does not impose the financial-sector governance depth that DORA requires. The CRDA classification is supported because the obligations stack without contradiction.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect**; it should be "scope-disjoint" in baseline. This pair was not classified contradictory.

**Downstream implication (1-2 sentences):** Doc 07 should require deployer-side DORA authentication governance in addition to CRA product controls.


---
