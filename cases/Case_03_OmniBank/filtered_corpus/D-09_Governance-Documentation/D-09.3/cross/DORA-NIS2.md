# D-09.3 — Pair analysis: NIS 2 ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: NIS2 ↔ DORA

**NIS2 article (verbatim, Art. 21(2)(i)):**
> [as quoted above]

**DORA article (verbatim, Art. 7(1) per SR-DORA-029; OJ-literal locus Art. 8(1) per the v0.2 audit):**
> "Financial entities shall identify, classify and adequately document all ICT supported business functions, the roles and responsibilities supporting those functions, the information assets and ICT assets supporting those functions, and their roles and dependencies in relation to ICT risk." — DORA Art. 7(1) per SR-DORA-029

**Scope comparison:**
- NIS 2 scope: asset management as one of three coordinated sub-domains of access control (Art. 21(2)(i) — partial coverage).
- DORA scope: financial-entity identify, classify, document mandate on ICT supported business functions + information assets + ICT assets + roles + dependencies (the dedicated authority per AEGIS taxonomy §4.1).
- Scope overlap: **Y (when a DORA financial entity is also an NSIE).**

**Trigger comparison:**
- NIS 2 trigger: entity asset management.
- DORA trigger: financial-entity ICT risk identification (Art. 7(1)).
- Trigger alignment: **SAME** (both entity-level asset inventory).

**Threshold/timeline comparison:**
- NIS 2: no quantitative cadence.
- DORA: no quantitative cadence.
- Tension: **NONE**.

**Recipient comparison:**
- NIS 2: management body, competent authority.
- DORA: NCA.

**Content template comparison:**
- NIS 2: not codified for granularity.
- DORA: 3-way AND of ICT supported business functions + information assets + ICT assets + roles + dependencies.

**Classified relationship (from CRDA):** EQUAL
**Verified relationship (after OJ-text analysis):** **SAME — EQUAL**
**Reasoning:** Both regulations impose asset-inventory obligations. DORA Art. 7(1) is the dominant authority with explicit OJ-literal anchor. NIS 2 Art. 21(2)(i) is partial via access-control coordination.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y (when the DORA financial entity is also an NSIE applying asset inventory)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce a DORA-dominant stack: DORA Art. 7(1) explicit `identify, classify, adequately document` mandate discharges both DORA's dedicated inventory obligation and NIS 2's Art. 21(2)(i) partial-coverage asset-management sub-domain for DORA financial entities.

---


## Summary (Domain Analysis)

<!-- pair: NIS2,DORA -->
| NIS2 ↔ DORA | **equal** | Tension/difference |
|---|---|---|
| **NIS2** (SR-NIS2-005, Art. 21(2)(i) — partial) | Asset management coordinated with access control. | |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-005 |
| **DORA** (SR-DORA-029, Art. 7(1) — sole authority) | Identify, classify, and adequately document ICT supported business functions + information assets + ICT assets + dependencies. | |
|   → full rationale: `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-029 |

**Why equal for financial entities**: Both regulations impose asset-inventory obligations. DORA Art. 7(1) is the dominant authority with explicit OJ-literal anchor. NIS 2 Art. 21(2)(i) is partial via access-control coordination.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
41 lines — see ../../_migration_report.md)_