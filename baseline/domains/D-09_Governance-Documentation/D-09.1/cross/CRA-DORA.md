# D-09.1 — Pair analysis: CRA ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: CRA ↔ DORA

**CRA article (verbatim, Art. 27(1)/(2)/(5)):**
> [as quoted above]

**DORA article (verbatim, Art. 6(1)):**
> "Financial entities shall have a sound, comprehensive and well-documented ICT risk management framework … which enables them to address ICT risk quickly, efficiently and comprehensively." — Art. 6(1) DORA (per SR-DORA-027)

**Scope comparison:**
- CRA scope: manufacturer-side presumption-of-conformity machinery.
- DORA scope: financial-entity ICT risk-management framework.
- Scope overlap: **N (typically)** — different actors (manufacturer vs. financial entity).

**Trigger comparison:**
- CRA trigger: manufacturer conformity-assessment procedure.
- DORA trigger: financial-entity framework adoption.
- Trigger alignment: **DIFFERENT**.

**Threshold/timeline comparison:**
- CRA: support period + 10-year accessibility.
- DORA: no quantitative cadence.
- Tension: **NONE**.

**Recipient comparison:**
- CRA: MSA.
- DORA: NCA.

**Content template comparison:**
- CRA: presumption-of-conformity machinery.
- DORA: 5-artefact list (Art. 6(2)).

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** CRA's presumption of conformity via harmonised standards allows DORA entities to rely on CRA-conformant products as inputs to their ICT risk-management framework. The two policies operate on different layers (product vs. entity).

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Conditional (Y when the DORA entity procures CRA-conformant products; N otherwise)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce a DORA-led stack: DORA Art. 6(1) ICT risk-management framework + CRA Art. 27 presumption-of-conformity as upstream gate for DORA-entity procurements.

---


## Summary (Domain Analysis)

<!-- pair: CRA,DORA -->
| CRA ↔ DORA | **complementary** | Tension/difference |
|---|---|---|
| **CRA** (SR-CRA-077, Art. 27(1)/(2)/(5)) | Presumption of conformity via harmonised standards / common specs. | |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-077 |
| **DORA** (SR-DORA-027, Art. 6(1)) | Sound/comprehensive/well-documented ICT risk management framework. | |
|   → full rationale: `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-027 |

**Why complementary**: CRA's presumption of conformity via harmonised standards allows DORA entities to rely on CRA-conformant products as inputs to their ICT risk management framework. The two policies operate on different layers (product vs. entity).



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
41 lines — see ../../_migration_report.md)_

