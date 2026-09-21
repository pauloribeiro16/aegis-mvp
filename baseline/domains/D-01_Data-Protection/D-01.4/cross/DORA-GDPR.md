# D-01.4 — Pair analysis: GDPR ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ DORA

**GDPR article (verbatim — SR-GDPR-005, Art. 5(1)(d)):**
> Art. 5(1)(d) personal data must be accurate and, where necessary, kept up to date; every reasonable step must be taken … erased or rectified without delay.

**DORA article (verbatim — SR-DORA-001, Art. 9(2)):**
> Art. 9(2) … high standards of availability, authenticity, integrity and confidentiality of data, whether at rest, in use or in transit.

**Scope comparison:**
- GDPR: personal-data accuracy + integrity.
- DORA: integrity cell of the 4×3 matrix (ICT-system scope).
- Scope overlap: Y (conditional) when DORA financial entity processes personal data.

**Trigger comparison:**
- GDPR: continuous + on Art. 16 request.
- DORA: continuous + annual scenario review (Art. 7(2)).
- Trigger alignment: PARTIAL.

**Threshold/timeline comparison:**
- GDPR: "reasonable step" + "without delay".
- DORA: "high standards".
- Tension: NONE.

**Classified relationship (from CRDA):** COMPLEMENTARY.

**Verified relationship (after OJ-text analysis):** SAME (CORRECTED — wording only).

**Reasoning:** DORA's integrity cell is the ICT-system-level integrity property; GDPR's accuracy/integrity duties are the personal-data-level semantic + storage property. On the same data asset, both apply; the stricter operational surface (typically DORA's system-level requirement) covers the GDPR Art. 5(1)(f) storage-integrity leg, with GDPR adding the semantic accuracy + rectification cascade leg.

**Scope-disjoint test:** Y for the DORA financial entity.

**Downstream implication:** Stack-merge with workflow overlay. DORA covers the storage-integrity leg; GDPR adds the rectification workflow + cascade.

---


## Summary (Domain Analysis)

<!-- pair: GDPR,DORA -->
| GDPR ↔ DORA | **Complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-005 + SR-GDPR-006, Art. 5(1)(d) + Art. 16) | Accuracy of stored personal data; rectification workflow with cascade propagation | Personal-data scope; PR.DS-01 + PR.DS-10 + PR.DS-12 |
| **DORA** (SR-DORA-001, Art. 9(2)) | Integrity is one of the 4×3 CIA+A cells | Financial entity; CIA+A 4×3 matrix; integrity at the ICT-system level |

**Why Complementary**: DORA's integrity cell of the 4×3 matrix is the same property as GDPR's Art. 5(1)(f) integrity leg but at the ICT-system level rather than the personal-data level. A DORA financial entity processing personal data operates both: the personal-data accuracy workflow (GDPR) + the ICT-system integrity control (DORA). → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-005; `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-001



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
35 lines — see ../../_migration_report.md)_

