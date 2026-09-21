# D-07.4 — Pair analysis: CRA ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: CRA ↔ DORA

**CRA article (verbatim, Art. 13(14) + Art. 21-22):**
> "Manufacturers of products with digital elements that are part of a series of production shall ensure that … such products remain in conformity with this Regulation. The manufacturer shall also ensure that procedures are in place for series of production to remain in conformity, including, where applicable, procedures for …" — Art. 13(14) CRA (per SR-CRA-069 reading; SR-CRA-070 covers substantial-modification)

**DORA article (verbatim, Art. 9(4)(e)):**
> [as quoted above]

**Scope comparison:**
- CRA scope: product-level change management across series production (Art. 13(14)) + substantial-modification triggers (Art. 21-22).
- DORA scope: entity-level change management — explicit OJ-mandate six-step process.
- Scope overlap: **Y (when a DORA financial entity customises a CRA-conformant product, triggering Art. 22 third-party substantial modification = manufacturer).**

**Trigger comparison:**
- CRA trigger: series-production conformity review (continuous) + substantial modification event (triggered).
- DORA trigger: ICT change event (continuous).
- Trigger alignment: **PARTIAL** (substantial-modification trigger overlaps with DORA change event).

**Threshold/timeline comparison:**
- CRA: no quantitative threshold for change cadence; substantial-modification threshold qualitative.
- DORA: no quantitative cadence; six-step mandatory.
- Tension: **NONE**.

**Recipient comparison:**
- CRA: MSA.
- DORA: NCA, management body.

**Content template comparison:**
- CRA: Annex VII §2 design/development documentation.
- DORA: documented change-management policy.

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** CRA covers product-level changes (substantial modification = manufacturer; series-production conformity); DORA covers entity-level changes (every software/hardware/firmware change goes through six-step process). The two regimes meet at the manufacturer-customer boundary — a CRA-conformant product that a DORA entity customises may trigger DORA Art. 22 third-party substantial-modification = manufacturer, layering DORA's six-step on top of CRA's substantial-modification trigger.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y (when the DORA entity customises a CRA-conformant product — Art. 22 third-party substantial modification)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 1 entities must implement both regimes' change-management obligations: CRA's substantial-modification assessment for product changes; DORA's six-step process for entity-side changes. The DORA six-step documentation can serve as the evidence trail for CRA Art. 13(14) series-production conformity.

---


## Summary (Domain Analysis)

| CRA ↔ DORA | **complementary** | Tension/difference |
|---|---|---|
| **CRA** (SR-CRA-069, Art. 13(14) series-production; SR-CRA-070, Art. 21-22 substantial modification) | Series-production conformity + substantial-modification = manufacturer trigger; third-party substantial mod = manufacturer (Art. 22). | |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-069 / SR-CRA-070 |
| **DORA** (SR-DORA-023, Art. 9(4)(e) six-step process) | Six-step change management: recorded, tested, assessed, approved, implemented, verified under risk-based approach. | |
|   → full rationale: `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-023 |

**Why complementary**: CRA covers product-level changes (substantial modification = manufacturer; series-production conformity); DORA covers entity-level changes (every software/hardware/firmware change goes through six-step process). The two regimes meet at the manufacturer-customer boundary — a CRA-conformant product that a DORA entity customises may trigger DORA Art. 22 third-party substantial-modification = manufacturer, layering DORA's six-step on top of CRA's substantial-modification trigger.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
41 lines — see ../../_migration_report.md)_

