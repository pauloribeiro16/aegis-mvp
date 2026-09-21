# D-09.4 — Pair analysis: NIS 2 ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: NIS2 ↔ CRA

**NIS2 article (verbatim, Art. 24(1)/(2)/(3)):**
> [as quoted above]

**CRA article (verbatim, Art. 27(8)/(9)):**
> "A product with digital elements and the processes put in place by the manufacturer for which the manufacturer has obtained an EU statement of conformity or an EU certificate under a European cybersecurity certification scheme adopted pursuant to Regulation (EU) 2019/881, at assurance level at least 'substantial', shall be presumed to be in conformity with the essential cybersecurity requirements …" — Art. 27(8) CRA (per SR-CRA-078)

**Scope comparison:**
- NIS 2 scope: certification-driven recordkeeping (Art. 24).
- CRA scope: CSA-certification presumption-of-conformity machinery.
- Scope overlap: **N (typically)** — different certification frameworks.

**Trigger comparison:**
- NIS 2 trigger: certification requirement.
- CRA trigger: manufacturer CSA certification.
- Trigger alignment: **DIFFERENT**.

**Threshold/timeline comparison:**
- NIS 2: per Member State.
- CRA: support period + 10-year accessibility.
- Tension: **NONE**.

**Recipient comparison:**
- NIS 2: management body, competent authority.
- CRA: MSA.

**Content template comparison:**
- NIS 2: not codified.
- CRA: Annex VII 8-item content list + EU statement of conformity / EU certificate.

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** NIS 2 Art. 24 requires use of certified products; CRA Art. 27(8)/(9) provides the CSA-certification presumption-of-conformity machinery. The two regimes link at the certification boundary.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Conditional (Y when the NSIE procures CSA-certified CRA products; N otherwise)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce a NIS 2 Art. 24 certification-driven record + CRA Art. 27 CSA-certification presumption-of-conformity as upstream gate for NSIE procurements.

---


## Summary (Domain Analysis)

| NIS2 ↔ CRA | **complementary** | Tension/difference |
|---|---|---|
| **NIS2** (SR-NIS2-043, Art. 24(1)/(2)/(3) — partial) | Use of certified ICT products/services/processes. | |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-043 |
| **CRA** (SR-CRA-078, Art. 27(8)/(9) CSA-certification presumption) | Presumption of conformity via CSA certification. | |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-078 |

**Why complementary**: NIS 2 Art. 24 requires use of certified products; CRA Art. 27(8)/(9) provides the CSA-certification presumption-of-conformity machinery. The two regimes link at the certification boundary.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
41 lines — see ../../_migration_report.md)_

