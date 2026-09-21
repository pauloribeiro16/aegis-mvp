# D-04.1 — Pair analysis: NIS 2 ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: NIS2 ↔ CRA

**NIS2 article (verbatim):**
> Article 21(2)(b) of Directive (EU) 2022/2555 requires essential and important entities to take measures regarding incident handling. Article 6(8) defines `incident handling` as all actions and procedures aiming at, where appropriate, preventing, detecting, analysing, containing and responding to and recovering from an incident.

**CRA article (verbatim):**
> Annex I Part I (2)(l) requires products with digital elements to provide security-related information by recording and monitoring relevant internal activity — including the access to or modification of data, services, or functions — with an opt-out mechanism for the user.

**Scope comparison:**
- NIS2 scope: entity-level all-hazards incident-handling detection.
- CRA scope: product-internal activity recording and monitoring.
- Scope overlap: Conditional where a NIS2 entity deploys or manufactures CRA products.

**Trigger comparison:**
- NIS2 trigger: detection of an adverse event affecting service continuity.
- CRA trigger: continuous product-internal activity monitoring.
- Trigger alignment: PARTIAL.

**Threshold/timeline comparison:**
- NIS2: 24h/72h/1m tiered reporting clocks.
- CRA: continuous product monitoring.
- Tension: NONE.

**Recipient comparison:**
- NIS2: CSIRT or competent authority.
- CRA: manufacturer, product users and market surveillance.

**Content template comparison:**
- NIS2: severity, impact, IoCs, cross-border, suspected unlawful or malicious acts.
- CRA: product-internal event records and corruption reporting.

**Classified relationship (from CRDA):** COMPLEMENTARY

**Verified relationship (after OJ-text analysis):** SAME — COMPLEMENTARY

**Reasoning (1-2 paragraphs):** The OJ text supports complementarity. NIS2 detection is at the entity boundary; CRA detection is inside the product. A CRA product feeds detection signals into the NIS2 entity-level pipeline via Annex I (2)(l); NIS2 requires the deployer to act on those signals under Art. 21(2)(b).

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect**; it should be "scope-disjoint" in baseline. This pair was not classified contradictory.

**Downstream implication (1-2 sentences):** Doc 07 should treat CRA product monitoring as a detection source feeding the NIS2 entity-level detection architecture.


## Summary (Domain Analysis)

<!-- pair: NIS2,CRA -->
| NIS2 ↔ CRA | **complementary** | Tension/difference |
|---|---|---|
| **NIS2** (SR-NIS2-008 + SR-NIS2-009, Art. 21(2)(b)) | Entity-wide incident-handling + all-hazards monitoring |  |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-008, SR-NIS2-009 |
| **CRA** (SR-CRA-027, Annex I Part I (2)(l)) | Product-internal activity recording with user opt-out |  |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-027 |

**Why complementary**: NIS2 detection covers the entity level (the deployer's ICT environment); CRA detection covers the product level (the manufacturer's deployed product). A CRA-compliant product feeds detection signals into the NIS2 entity-level pipeline via its Annex I (2)(l) recording obligation; NIS2 in turn requires the deployer to act on those signals under Art. 21(2)(b).



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_

