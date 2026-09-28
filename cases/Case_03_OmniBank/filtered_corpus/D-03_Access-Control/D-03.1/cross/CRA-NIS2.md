# D-03.1 — Pair analysis: NIS 2 ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: NIS2 ↔ CRA

**NIS2 article (verbatim):**
> Article 21(2)(i) of Directive (EU) 2022/2555 requires essential and important entities to take measures regarding human resources security, access control policies and asset management, coordinated by the conjunction AND.

**CRA article (verbatim):**
> Annex I Part I (2)(d) requires protection from unauthorised access by appropriate control mechanisms, including but not limited to authentication, identity, or access-management systems; the "including but not limited to" clause keeps the floor open to other technical means while naming the three substantive control families.

**Scope comparison:**
- NIS2 scope: entity-level HR security, access-control and asset-management measures.
- CRA scope: product-level authentication, identity and access-management mechanisms.
- Scope overlap: Conditional when a NIS2 entity deploys or manufactures a CRA product.

**Trigger comparison:**
- NIS2 trigger: continuous entity risk-management obligation.
- CRA trigger: continuous product security-design obligation.
- Trigger alignment: PARTIAL.

**Threshold/timeline comparison:**
- NIS2: appropriate and proportionate entity controls.
- CRA: appropriate product control mechanisms.
- Tension: NONE.

**Recipient comparison:**
- NIS2: entity governance and competent-authority evidence.
- CRA: manufacturer documentation, users and market surveillance.

**Content template comparison:**
- NIS2: workforce lifecycle, access policy and asset register.
- CRA: product identities, access-management systems and product identification.

**Classified relationship (from CRDA):** COMPLEMENTARY

**Verified relationship (after OJ-text analysis):** SAME — COMPLEMENTARY

**Reasoning (1-2 paragraphs):** NIS2 and CRA operate at different layers. NIS2 governs the entity operating network and information systems; CRA governs the product with digital elements. The same organisation may need to show both, but the evidence is not interchangeable. Product identity controls can feed the entity access-control framework, but do not replace it.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect**; it should be "scope-disjoint" in baseline. This pair was not classified contradictory.

**Downstream implication (1-2 sentences):** Doc 07 should express this as product-to-entity layering, not as a single merged identity-lifecycle obligation.


## Summary (Domain Analysis)

<!-- pair: NIS2,CRA -->
| NIS2 ↔ CRA | **Complementary** | Tension/difference |
|---|---|---|
| **NIS2** (SR-NIS2-003 + SR-NIS2-004, Art. 21(2)(i) — HR-security + access-control dimensions) | Workforce identity lifecycle + access-control policies (3-domain AND) | Entity-level; workforce + access-control; PR.AT-02 + PR.AA-01 + PR.AA-05 |
| **CRA** (SR-CRA-023, Annex I Part I (2)(d) + Art. 13(15)) | Authentication identity + unique product identification | Product-level; user/service/component identities; PR.AA-01 + ID.AM-01 |

**Why Complementary**: NIS 2's workforce identity lifecycle + access-control policies are the entity-side architecture; CRA's product-level identity management (users, services, integrated components) is the product-side invariant. A NIS 2 entity using CRA-regulated products is jointly bound: the entity-side workforce lifecycle (NIS 2) + the product-side user/service/component identity management (CRA). The two are complementary, with the boundary at workforce (NIS 2) vs product users (CRA). → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-003 + SR-NIS2-004; `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-023



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_