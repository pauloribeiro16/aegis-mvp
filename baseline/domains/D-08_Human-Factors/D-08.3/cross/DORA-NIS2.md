# D-08.3 — Pair analysis: NIS 2 ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: NIS2 ↔ DORA

**NIS2 article (verbatim, Art. 20(2) sentence 1):**
> "Member States shall ensure that members of the management bodies of essential and important entities are required to follow training, in order that they gain sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices and their impact on the services provided by the entity." — Art. 20(2) sentence 1 NIS 2 (per SR-NIS2-031)

**DORA article (verbatim, Art. 5(4)):**
> "Members of the management body shall actively keep up to date with sufficient knowledge and skills to enable them to understand and assess ICT risk and its impact on the operations of the financial entity, including by following specific training on a regular basis, commensurate to the ICT risk being managed." — Art. 5(4) DORA (per SR-DORA-024)

**Scope comparison:**
- NIS 2 scope: Member-State-imposed management-body training (the binding force is on the MS).
- DORA scope: direct entity-side management-body training obligation.
- Scope overlap: **Y (when the DORA financial entity is also an NSIE).**

**Trigger comparison:**
- NIS 2 trigger: Member-State obligation.
- DORA trigger: entity-side direct obligation.
- Trigger alignment: **PARTIAL** (both management-body training but different binding-force locus).

**Threshold/timeline comparison:**
- NIS 2: training mandatory under Art. 20(2) sentence 1 (Member-State-imposed); entity-side SR applies only where the MS has transposed.
- DORA: `actively keep up to date` + `regular basis` + `commensurate to the ICT risk`.
- Tension: **NONE** (both require sufficient knowledge and skills, but DORA is direct and ICT-risk-commensurate; NIS 2 is MS-imposed and literacy-prerequisite).

**Recipient comparison:**
- NIS 2: management body, competent authority.
- DORA: management body, NCA.

**Content template comparison:**
- NIS 2: not codified for content (entity-internal programme per SR-NIS2-031).
- DORA: not codified for content (entity-internal programme per SR-DORA-024).

**Classified relationship (from CRDA):** EQUAL
**Verified relationship (after OJ-text analysis):** **SAME — EQUAL**
**Reasoning:** Both regulations impose management-body training. DORA's OJ-literal anchor is direct (Art. 5(4) is the entity-side obligation); NIS 2's anchor is indirect (Art. 20(2) sentence 1 is the Member-State obligation, with the entity-side SR applying only where the Member State has transposed). For DORA financial entities, the DORA Art. 5(4) obligation is the dominant authority.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y (when the DORA financial entity is also an NSIE applying management-body training)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce a DORA-dominant stack: DORA Art. 5(4) `actively keep up to date` + `commensurate to the ICT risk` discharges both DORA's dedicated management-body obligation and NIS 2's Member-State-imposed Art. 20(2) sentence 1 literacy prerequisite for DORA financial entities.

---


## Summary (Domain Analysis)

<!-- pair: NIS2,DORA -->
| NIS2 ↔ DORA | **equal** | Tension/difference |
|---|---|---|
| **NIS2** (SR-NIS2-031, Art. 20(2) sentence 1) | Management body follows cybersecurity training (Member-State-imposed; literacy prerequisite for approve/oversee/liable under Art. 20(1)). | |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-031 |
| **DORA** (SR-DORA-024, Art. 5(4)) | Management body keeps up to date with sufficient knowledge and skills via regular training, commensurate to the ICT risk. | |
|   → full rationale: `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-024 |

**Why equal**: Both regulations impose management-body training. DORA's OJ-literal anchor is direct (Art. 5(4) is the entity-side obligation); NIS 2's anchor is indirect (Art. 20(2) sentence 1 is the Member-State obligation, with the entity-side SR applying only where the Member State has transposed). For DORA financial entities, the DORA Art. 5(4) obligation is the dominant authority.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
41 lines — see ../../_migration_report.md)_

