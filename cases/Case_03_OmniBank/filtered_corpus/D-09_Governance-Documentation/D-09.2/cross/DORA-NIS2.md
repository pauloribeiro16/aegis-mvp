# D-09.2 — Pair analysis: NIS 2 ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: NIS2 ↔ DORA

**NIS2 article (verbatim, Art. 21(2)(a)):**
> [as quoted above]

**DORA article (verbatim, Art. 6(4) + Art. 7(2)):**
> [as quoted above]

**Scope comparison:**
- NIS 2 scope: entity-level operational risk-analysis policy.
- DORA scope: financial-entity three-lines-of-defence + ICT risk identification + yearly risk-scenario review.
- Scope overlap: **Y (when the DORA financial entity is also an NSIE).**

**Trigger comparison:**
- NIS 2 trigger: continuous operational analysis.
- DORA trigger: continuous ICT risk identification + yearly review.
- Trigger alignment: **SAME** (both operational continuous).

**Threshold/timeline comparison:**
- NIS 2: continuous.
- DORA: continuous + at-least-yearly.
- Tension: **NONE**.

**Recipient comparison:**
- NIS 2: management body, competent authority.
- DORA: NCA.

**Content template comparison:**
- NIS 2: not codified for content.
- DORA: risk identification register + risk-scenario register.

**Classified relationship (from CRDA):** EQUAL
**Verified relationship (after OJ-text analysis):** **SAME — EQUAL**
**Reasoning:** Both regulations impose risk-analysis obligations. DORA's three-lines-of-defence is the dominant authority for financial entities under DORA's direct scope. NIS 2 applies to the financial entity only insofar as it is an NSIE outside DORA.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y (when the DORA financial entity is also an NSIE applying risk-analysis)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce a DORA-dominant stack: DORA Art. 7(2) continuous identification + Art. 7(2) sentence 2 yearly review discharges both DORA's dedicated risk-analysis obligations and NIS 2's Art. 21(2)(a) policy artefacts for DORA financial entities.

---


## Summary (Domain Analysis)

<!-- pair: NIS2,DORA -->
| NIS2 ↔ DORA | **equal** | Tension/difference |
|---|---|---|
| **NIS2** (SR-NIS2-035, Art. 21(2)(a)) | Risk-analysis policy. | |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-035 |
| **DORA** (SR-DORA-028, Art. 6(4) three-lines-of-defence) | Three-lines-of-defence + asset identification. | |
|   → full rationale: `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-028 |

**Why equal for financial entities**: Both regulations impose risk-analysis obligations. DORA's three-lines-of-defence is the dominant authority for financial entities under DORA's direct scope. NIS 2 applies to the financial entity only insofar as it is an NSIE outside DORA.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
41 lines — see ../../_migration_report.md)_