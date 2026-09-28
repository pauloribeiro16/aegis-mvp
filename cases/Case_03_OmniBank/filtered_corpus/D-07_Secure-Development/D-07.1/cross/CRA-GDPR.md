# D-07.1 — Pair analysis: GDPR ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ CRA

**GDPR article (verbatim, Art. 25(1)):**
> [as quoted in GDPR ↔ NIS2 above]

**CRA article (verbatim, Art. 13(1) + Art. 13(2)):**
> "When placing a product with digital elements on the market, manufacturers shall ensure that it has been designed, developed and produced in accordance with the essential cybersecurity requirements set out in Part I of Annex I." — Art. 13(1) CRA
> "The manufacturer shall undertake an assessment of the cybersecurity risks associated with a product with digital elements … and take the outcome of that assessment into account during the planning, design, development, production, delivery and maintenance phases of the product with digital elements …" — Art. 13(2) CRA

**Scope comparison:**
- GDPR scope: controller-side processing of personal data; data-protection properties by design.
- CRA scope: manufacturer-side product design, development, production across 6 lifecycle phases (planning, design, development, production, delivery, maintenance).
- Scope overlap: **Y (when the controller deploys a CRA-regulated product that processes personal data, OR when the manufacturer is also a controller for its own product telemetry).**

**Trigger comparison:**
- GDPR trigger: controller's means-determination.
- CRA trigger: manufacturer places product with digital elements on market (pre-market).
- Trigger alignment: **DIFFERENT** (controller-side vs. manufacturer-side) but co-applicable.

**Threshold/timeline comparison:**
- GDPR: no quantitative threshold.
- CRA: support period ≥ 5 years (Art. 13(8)) + 10-year Annex II information accessibility (Art. 13(18)).
- Tension: **NONE** (different actors / different lifecycles).

**Recipient comparison:**
- GDPR: supervisory authority (DPA).
- CRA: market surveillance authority (MSA), users.

**Content template comparison:**
- GDPR: documented necessity assessment.
- CRA: Annex VII §3 risk-assessment record + Annex I Part I (2) sub-point evidence.

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** GDPR Art. 25(1) addresses *what* data-protection properties must be designed in; CRA Art. 13(1) addresses *that* the design discipline applies to product-with-digital-elements across three coordinated verbs (designed, developed, produced). For a CRA-regulated product that processes personal data, both regimes apply: the manufacturer's CRA design discipline discharges the engineering substrate, and the controller's GDPR Art. 25(1) discharges the personal-data overlay. The two converge on "design as a regulatory event" but address different design-output objects (data-protection properties vs. product cybersecurity).

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y (when the controller deploys a CRA-regulated product processing personal data)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce a 2-track by-design matrix: (1) GDPR Art. 25(1) controller-side personal-data by-design; (2) CRA Art. 13(1)/(2) manufacturer-side product by-design with Annex VII §3 risk-assessment record.

---


## Summary (Domain Analysis)

<!-- pair: GDPR,CRA -->
| GDPR ↔ CRA | **complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-039, Art. 25(1)) | Privacy-by-design at controller means-determination. | |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-039 |
| **CRA** (SR-CRA-064, Art. 13(1); SR-CRA-065, Art. 13(2)) | Three-phase design/development/production per Annex I Part I with risk assessment across 6 lifecycle phases. | |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-064 / SR-CRA-065 |

**Why complementary**: GDPR addresses what must be designed in (privacy properties); CRA addresses the design discipline itself (processes, risk-assessment propagation, lifecycle propagation). The two converge on the "design as a regulatory event" concept but do not overlap in substance — a product controller simultaneously discharging GDPR Art. 25(1) and CRA Art. 13(1)/(2) discharges two distinct by-design obligations with distinct evidence trails.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_