# D-01.4 — Pair analysis: CRA ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: CRA ↔ DORA

**CRA article (verbatim — SR-CRA-005, Annex I Part I (2)(f) + (l)):**
> Annex I Part I (2)(f) protect the integrity of stored, transmitted or otherwise processed data — personal or other — as well as the integrity of commands, programs and configuration against any manipulation or modification not authorised by the user.

**DORA article (verbatim — SR-DORA-001, Art. 9(2)):**
> Art. 9(2) … high standards of availability, authenticity, integrity and confidentiality of data, whether at rest, in use or in transit.

**Scope comparison:**
- CRA: data + commands + programs + configuration integrity (product-level).
- DORA: integrity cell of 4×3 matrix (entity-level).
- Scope overlap: Y on the same asset when DORA financial entity uses CRA product.

**Trigger comparison:**
- CRA: continuous + corruption-event reporting.
- DORA: continuous + annual scenario review.
- Trigger alignment: SAME on continuous; PARTIAL on event-triggered (CRA-only).

**Threshold/timeline comparison:**
- CRA: "any manipulation" (universal quantifier).
- DORA: "high standards".
- Tension: NONE.

**Recipient comparison:**
- CRA: user / administering party (corruption report).
- DORA: CA (entity-level).

**Classified relationship (from CRDA):** EQUAL.

**Verified relationship (after OJ-text analysis):** SAME (CORRECTED — no change).

**Reasoning:** Both impose an integrity obligation with the same PR.DS-01 + PR.DS-10 anchors. The layer is product-level (CRA) vs entity-level ICT-system (DORA); the property is the same. CRA's "report corruptions" + Annex I (2)(l) logging overlay adds the corruption-detection reporting loop that DORA does not separately require (DORA's reporting is the entity-level major ICT-related incident reporting under Art. 19, which is event-triggered and threshold-driven). On a single event (corruption on a CRA product used by a DORA financial entity), the CRA reporting loop fires; the DORA Art. 19 reporting loop fires only if the corruption escalates to a major ICT-related incident — which is a substantive threshold difference, but not a contradiction.

**Scope-disjoint test:** Y for the DORA financial entity using a CRA product.

**Downstream implication:** Stack-merge with conditional reporting cascades. The CRA product-side PR.DS-01 + PR.DS-10 + PR.PS-04 stack satisfies the integrity + monitoring layer; DORA adds the entity-level classification and Art. 19 incident-classification cascade.

---


## Summary (Domain Analysis)

<!-- pair: CRA,DORA -->
| CRA ↔ DORA | **Equal** | Tension/difference |
|---|---|---|
| **CRA** (SR-CRA-005, Annex I Part I (2)(f)+(l)) | Integrity of data + commands + programs + configuration; corruption reported | Product-level; PR.DS-01 + PR.DS-10 + PR.PS-04 |
| **DORA** (SR-DORA-001, Art. 9(2)) | Integrity is one of the 4×3 CIA+A cells | Financial entity; ICT-system scope; PR.DS-01 + PR.DS-10 + PR.DS-12 |

**Why Equal**: Both regulations impose an integrity obligation with the same CSF anchors (PR.DS-01 + PR.DS-10); the principal difference is the layer (CRA product vs DORA ICT system) and the supplementary CSF (CRA PR.PS-04 logging; DORA PR.DS-12 risk-strategy). A DORA financial entity using CRA-regulated products meets both when the integrity stack is documented as product + deployment. → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-005; `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-001



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
39 lines — see ../../_migration_report.md)_

