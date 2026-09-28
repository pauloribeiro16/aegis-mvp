# D-09.1 — Pair analysis: NIS 2 ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: NIS2 ↔ DORA

**NIS2 article (verbatim, Art. 20(1) + Art. 21(2)(a) + Art. 21(2)(f)):**
> [as quoted above]

**DORA article (verbatim, Art. 5(2) + Art. 6(1) + Art. 6(4)):**
> [as quoted above]

**Scope comparison:**
- NIS 2 scope: management-body approve/oversee/liable + risk-analysis + IS-security + effectiveness-assessment policies.
- DORA scope: management-body define/approve/oversee/implement + ICT risk-management framework + three-lines-of-defence.
- Scope overlap: **Y (when the DORA financial entity is also an NSIE).**

**Trigger comparison:**
- NIS 2 trigger: management-body approval of risk-management measures.
- DORA trigger: management-body define/approve/oversee/implement of ICT risk-management framework.
- Trigger alignment: **SAME** (both management-body governance of risk-management framework).

**Threshold/timeline comparison:**
- NIS 2: no quantitative cadence.
- DORA: no quantitative cadence.
- Tension: **NONE**.

**Recipient comparison:**
- NIS 2: management body, competent authority.
- DORA: management body, NCA.

**Content template comparison:**
- NIS 2: Art. 21(2)(a)+(f) policy artefacts.
- DORA: Art. 6(2) 5-artefact list.

**Classified relationship (from CRDA):** EQUAL
**Verified relationship (after OJ-text analysis):** **SAME — EQUAL**
**Reasoning:** Both regulations impose policy + governance architecture. DORA's ICT risk-management framework is the dominant authority for financial entities under DORA's direct scope. NIS 2 applies to the financial entity only insofar as it is an NSIE outside DORA.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y (when the DORA financial entity is also an NSIE adopting risk-management policies subject to management-body approval)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce a DORA-dominant stack: DORA Art. 6(1) ICT risk-management framework discharges both DORA's dedicated framework obligation and NIS 2's Art. 21(2)(a)+(f) policy artefacts for DORA financial entities.

---


## Summary (Domain Analysis)

<!-- pair: NIS2,DORA -->
| NIS2 ↔ DORA | **equal** | Tension/difference |
|---|---|---|
| **NIS2** (SR-NIS2-032, Art. 20(1); SR-NIS2-035, Art. 21(2)(a); SR-NIS2-037, Art. 21(2)(f)) | Management body approve/oversee/liable; risk-analysis + IS-security + effectiveness-assessment policies. | |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-032 / SR-NIS2-035 / SR-NIS2-037 |
| **DORA** (SR-DORA-026, Art. 5(2); SR-DORA-027, Art. 6(1); SR-DORA-028, Art. 6(4)) | ICT risk management framework with management body ownership and three-lines-of-defence. | |
|   → full rationale: `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-026 / SR-DORA-027 / SR-DORA-028 |

**Why equal for financial entities**: Both regulations impose policy + governance architecture. DORA's ICT risk management framework is the dominant authority for financial entities under DORA's direct scope. NIS 2 applies to the financial entity only insofar as it is an NSIE (essential/important entity) outside DORA.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
41 lines — see ../../_migration_report.md)_