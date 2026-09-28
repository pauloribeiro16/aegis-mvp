# D-09.3 — Pair analysis: CRA ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: CRA ↔ DORA

**CRA article (verbatim, Annex VII §1-§2):**
> [as quoted above]

**DORA article (verbatim, Art. 7(1) per SR-DORA-029; OJ-literal locus Art. 8(1) per the v0.2 audit):**
> [as quoted above]

**Scope comparison:**
- CRA scope: general description + architecture documentation (Annex VII §1-§2 — documentation-centric, not a formal asset register).
- DORA scope: financial-entity identify, classify, document mandate.
- Scope overlap: **Conditional (Y when the DORA entity procures CRA-conformant products)**.

**Trigger comparison:**
- CRA trigger: manufacturer technical-documentation obligation.
- DORA trigger: financial-entity ICT risk identification.
- Trigger alignment: **DIFFERENT**.

**Threshold/timeline comparison:**
- CRA: support period + 10-year accessibility.
- DORA: no quantitative cadence.
- Tension: **NONE**.

**Recipient comparison:**
- CRA: MSA.
- DORA: NCA.

**Content template comparison:**
- CRA: general description + architecture.
- DORA: 3-way AND inventory.

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** CRA architecture documentation feeds the DORA entity's asset register. DORA's ICT asset inventory is the entity-level master record; CRA Annex VII §1-§2 is the product-level sub-register.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Conditional (Y when the DORA entity procures CRA-conformant products; N otherwise)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce a DORA-led stack: DORA Art. 7(1) master record + CRA Annex VII §1-§2 product-level sub-register.

---


## Summary (Domain Analysis)

<!-- pair: CRA,DORA -->
| CRA ↔ DORA | **complementary** | Tension/difference |
|---|---|---|
| **CRA** (SR-CRA-087, Annex VII §1-§2 — partial coverage) | General description + architecture documentation. | |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-087 |
| **DORA** (SR-DORA-029, Art. 7(1) — sole authority) | Identify, classify, document ICT supported business functions + assets + dependencies. | |
|   → full rationale: `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-029 |

**Why complementary**: CRA architecture documentation feeds the DORA entity's asset register. DORA's ICT asset inventory is the entity-level master record; CRA Annex VII §1-§2 is the product-level sub-register.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
41 lines — see ../../_migration_report.md)_