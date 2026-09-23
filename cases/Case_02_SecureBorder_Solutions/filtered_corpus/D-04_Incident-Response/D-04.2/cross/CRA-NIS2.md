# D-04.2 — Pair analysis: NIS 2 ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: NIS2 ↔ CRA

**NIS2 article (verbatim):**
> Article 21(2)(b) of Directive (EU) 2022/2555 requires essential and important entities to take measures regarding incident handling. Article 6(8) defines `incident handling` as all actions and procedures aiming at, where appropriate, preventing, detecting, analysing, containing and responding to and recovering from an incident (OJ L 333, 27.12.2022, p. 113) — a six-action process including `containing` as one of the six actions.

**CRA article (verbatim):**
> Annex I Part I (2)(h) requires products to protect the availability of essential and basic functions — also after an incident — including through resilience and mitigation measures against denial-of-service attacks. Annex I Part I (2)(i) requires products to minimise the negative impact by the products themselves or connected devices on the availability of services provided by other devices or networks. Annex I Part I (2)(k) requires reducing the impact of an incident using appropriate exploitation-mitigation mechanisms and techniques.

**Scope comparison:**
- NIS2 scope: entity-level incident-handling `contain` phase.
- CRA scope: product-level post-incident availability preservation and cross-product impact limitation.
- Scope overlap: Conditional where a NIS2 entity deploys or manufactures CRA products.

**Trigger comparison:**
- NIS2 trigger: significant incident under Art. 23(3).
- CRA trigger: continuous product design for availability preservation.
- Trigger alignment: DIFFERENT.

**Threshold/timeline comparison:**
- NIS2: lifecycle-phase content.
- CRA: post-incident availability and cross-product impact limitation.
- Tension: NONE.

**Recipient comparison:**
- NIS2: CSIRT or competent authority.
- CRA: manufacturer documentation, product users and market surveillance.

**Content template comparison:**
- NIS2: containment action records.
- CRA: product resilience and exploitation-mitigation architecture.

**Classified relationship (from CRDA):** COMPLEMENTARY

**Verified relationship (after OJ-text analysis):** SAME — COMPLEMENTARY

**Reasoning (1-2 paragraphs):** The OJ text supports complementarity. NIS2 contains at the entity boundary; CRA contains at the product boundary. The two are layered, not overlapping — a CRA-compliant product supports entity-level NIS2 containment by reducing blast radius.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect**; it should be "scope-disjoint" in baseline. This pair was not classified contradictory.

**Downstream implication (1-2 sentences):** Doc 07 should keep NIS2 entity-level containment plan and CRA product-level resilience evidence linked but not duplicated.


## Summary (Domain Analysis)

<!-- pair: NIS2,CRA -->
| NIS2 ↔ CRA | **complementary** | Tension/difference |
|---|---|---|
| **NIS2** (SR-NIS2-008, Art. 21(2)(b) + Art. 6(8)) | Entity-wide `contain` as lifecycle phase |  |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-008 |
| **CRA** (SR-CRA-043 + SR-CRA-044, Annex I Part I (2)(h)/(i)) | Product-level post-incident availability + cross-product impact containment |  |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-043, SR-CRA-044 |

**Why complementary**: NIS2 contains at the entity boundary (isolate affected systems); CRA contains at the product boundary (limit cascading impact to other devices/networks). The two are layered and complementary, not overlapping — a CRA-compliant product supports the entity-level NIS2 containment by reducing blast radius.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_