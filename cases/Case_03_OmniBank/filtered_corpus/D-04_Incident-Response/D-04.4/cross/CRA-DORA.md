# D-04.4 — Pair analysis: CRA ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: CRA ↔ DORA

**CRA article (verbatim):**
> Annex I Part I (2)(h) requires products to protect the availability of essential and basic functions — also after an incident — including through resilience and mitigation measures against denial-of-service attacks.

**DORA article (verbatim):**
> Art. 12(1)(a) requires financial entities to develop and document backup policies and procedures specifying the scope of the data subject to backup and the minimum frequency of backup, based on the criticality of information or the confidentiality level of the data. Art. 12(1)(b) requires restoration and recovery procedures and methods.

**Scope comparison:**
- CRA scope: product-level resilience and availability after incident.
- DORA scope: financial-entity backup and restoration/recovery procedures.
- Scope overlap: Conditional when a financial entity deploys CRA products as part of its ICT estate.

**Trigger comparison:**
- CRA trigger: continuous product design duty and incident-resilience expectation.
- DORA trigger: continuous BC/backup duty and restoration activation after ICT incident.
- Trigger alignment: PARTIAL.

**Threshold/timeline comparison:**
- CRA: availability of essential and basic functions also after incident.
- DORA: backup scope/frequency and restoration methods calibrated by criticality or confidentiality.
- Tension: NONE.

**Recipient comparison:**
- CRA: product users and market surveillance.
- DORA: financial competent authority evidence path.

**Content template comparison:**
- CRA: resilience and product-availability evidence.
- DORA: backup, restoration, recovery and continuity evidence.

**Classified relationship (from CRDA):** COMPLEMENTARY

**Verified relationship (after OJ-text analysis):** SAME — COMPLEMENTARY

**Reasoning (1-2 paragraphs):** CRA and DORA regulate different layers. CRA supports continued product functionality; DORA requires the financial entity to restore services and data through documented backup and recovery procedures. Neither substitutes for the other.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: any contradiction claim would be scope-incorrect; CRDA classified this pair as complementary.

**Downstream implication (1-2 sentences):** Doc 07 should treat CRA product resilience as input evidence inside the DORA recovery architecture, not as replacement for DORA backup and restoration procedures.


## Summary (Domain Analysis)

<!-- pair: CRA,DORA -->
| CRA ↔ DORA | **complementary** | Tension/difference |
|---|---|---|
| **CRA** (SR-CRA-043, Annex I Part I (2)(h)) | Product-level resilience + DoS-resistance |  |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-043 |
| **DORA** (SR-DORA-013 + SR-DORA-015, Art. 11(1) + Art. 12(1)) | Entity-level BC framework + backup policies |  |
|   → full rationale: `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-013, SR-DORA-015 |

**Why complementary**: CRA product resilience + DORA entity BC framework are the two layers of recovery: product continues to operate, entity restores if product fails. Both required, neither substitutes.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_