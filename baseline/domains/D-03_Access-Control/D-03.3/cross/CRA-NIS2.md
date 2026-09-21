# D-03.3 — Pair analysis: NIS 2 ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: NIS2 ↔ CRA

**NIS2 article (verbatim):**
> Article 21(2)(i) of Directive (EU) 2022/2555 requires essential and important entities to take measures regarding human resources security, access control policies and asset management, coordinated by the conjunction AND.

**CRA article (verbatim):**
> Annex I Part I (2)(d) requires protection from unauthorised access through appropriate control mechanisms. Annex I Part I (2)(j) limits attack surfaces, including external interfaces.

**Scope comparison:**
- NIS2 scope: entity-level access-control and HR-security measures.
- CRA scope: product-level access control and attack-surface limitation.
- Scope overlap: Conditional when a NIS2 entity deploys or manufactures a CRA product.

**Trigger comparison:**
- NIS2 trigger: continuous entity access-control duty.
- CRA trigger: continuous product access-control duty.
- Trigger alignment: PARTIAL.

**Threshold/timeline comparison:**
- NIS2: appropriate and proportionate entity controls.
- CRA: limited to authenticated and authorised users, services and hardware.
- Tension: NONE.

**Recipient comparison:**
- NIS2: entity governance and competent authority.
- CRA: manufacturer documentation, product users and market surveillance.

**Content template comparison:**
- NIS2: access-control policy and HR-lifecycle records.
- CRA: product access-control records and attack-surface-limitation evidence.

**Classified relationship (from CRDA):** COMPLEMENTARY

**Verified relationship (after OJ-text analysis):** SAME — COMPLEMENTARY

**Reasoning (1-2 paragraphs):** The OJ text supports complementarity. NIS2 is the entity-level access-control framework; CRA is the product-level boundary. Both obligations can be met through a single access-control architecture, with CRA supplying the product primitive and NIS2 supplying the entity governance.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect**; it should be "scope-disjoint" in baseline. This pair was not classified contradictory.

**Downstream implication (1-2 sentences):** Doc 07 should map CRA product access-control evidence into the NIS2 entity-level access-control policy as inputs, not duplicates.


## Summary (Domain Analysis)

<!-- pair: NIS2,CRA -->
| NIS2 ↔ CRA | **Complementary** | Tension/difference |
|---|---|---|
| **NIS2** (SR-NIS2-003, Art. 21(2)(i) — access-control dimension) | Access control policies + HR security + asset management; model-agnostic | Entity-level; PR.AA-01 + PR.AA-05 |
| **CRA** (SR-CRA-017 + SR-CRA-024, Annex I Part I (2)(d) + (2)(j)) | Access limited to authenticated + authorised users/services/hardware; attack-surface limitation | Product-level; PR.AA-05 + PR.AA-06 + DE.CM-09 |

**Why Complementary**: NIS 2's access-control policies are the entity-side architecture; CRA's product-side access control + attack-surface-limitation is the product-side invariant. A NIS 2 essential entity using CRA-regulated products is jointly bound: the entity-side access-control policy (NIS 2) + the product-side access control (CRA). The two converge on PR.AA-05 (least privilege) + PR.AA-06 (access limited to authorised users) as shared anchors. → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-003; `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-017 + SR-CRA-024



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_

