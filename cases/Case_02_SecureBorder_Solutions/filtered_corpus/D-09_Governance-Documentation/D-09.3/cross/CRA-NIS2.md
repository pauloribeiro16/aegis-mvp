# D-09.3 — Pair analysis: NIS 2 ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: NIS2 ↔ CRA

**NIS2 article (verbatim, Art. 21(2)(i)):**
> "[Member States shall ensure that essential and important entities take appropriate and proportionate technical, operational and organisational measures to … ] (i) human resources security, access control policies and asset management." — Art. 21(2)(i) NIS 2 (per SR-NIS2-005)

**CRA article (verbatim, Annex VII §1-§2):**
> "The technical documentation shall contain: (1) a general description of the product with digital elements … (2) a description of the design, development, production and vulnerability-handling processes of the product with digital elements …" — CRA Annex VII §1-§2 (per SR-CRA-087)

**Scope comparison:**
- NIS 2 scope: asset management as one of three coordinated sub-domains of access control (Art. 21(2)(i) — partial coverage).
- CRA scope: general description + architecture documentation (Annex VII §1-§2 — documentation-centric, not a formal asset register).
- Scope overlap: **N (typically)** — different objects (entity asset register vs. product architecture documentation).

**Trigger comparison:**
- NIS 2 trigger: entity asset management.
- CRA trigger: manufacturer technical-documentation obligation.
- Trigger alignment: **DIFFERENT**.

**Threshold/timeline comparison:**
- NIS 2: no quantitative cadence.
- CRA: support period + 10-year accessibility.
- Tension: **NONE**.

**Recipient comparison:**
- NIS 2: management body, competent authority.
- CRA: MSA.

**Content template comparison:**
- NIS 2: not codified for granularity.
- CRA: general description + architecture.

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** NIS 2 covers entity-level asset management; CRA covers product-level architecture documentation. The two regimes meet at the supplier-customer interface — CRA Annex VII §1-§2 architecture documentation feeds the NIS 2 entity's asset register.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **N (typically)** — different objects (entity asset register vs. product architecture documentation). Substantively scope-disjoint; CRDA "complementary" is a taxonomy artifact.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce two parallel artefacts: NIS 2 Art. 21(2)(i) asset-management sub-domain + CRA Annex VII §1-§2 architecture documentation as upstream input.

---


## Summary (Domain Analysis)

<!-- pair: NIS2,CRA -->
| NIS2 ↔ CRA | **complementary** | Tension/difference |
|---|---|---|
| **NIS2** (SR-NIS2-005, Art. 21(2)(i) — partial via access-control coordination) | Asset management as one of three coordinated sub-domains of access control. | |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-005 |
| **CRA** (SR-CRA-087, Annex VII §1-§2 — partial coverage) | General description including SW versions + system-architecture description. | |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-087 |

**Why complementary**: NIS 2 covers entity-level asset management; CRA covers product-level architecture documentation. The two regimes meet at the supplier-customer interface — CRA Annex VII §1-§2 architecture documentation feeds the NIS 2 entity's asset register.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
41 lines — see ../../_migration_report.md)_