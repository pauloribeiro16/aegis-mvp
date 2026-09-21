# D-01.4 — Pair analysis: DORA ↔ AI Act

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: DORA ↔ AI_Act

**DORA article (verbatim — SR-DORA-001, Art. 9(2)):**
> Art. 9(2) … high standards of availability, authenticity, integrity and confidentiality of data, whether at rest, in use or in transit.

**AI Act article (verbatim — SR-AIACT-015, Art. 15(3)):**
> Art. 15(3) … as resilient as possible regarding errors, faults or inconsistencies … technical redundancy solutions, which may include backup or fail-safe plans.

**Scope comparison:**
- DORA: integrity cell of 4×3 matrix.
- AI Act: AI-system resilience.
- Scope overlap: Y when a DORA financial entity deploys high-risk AI (e.g. credit scoring).

**Trigger comparison:**
- DORA: continuous + annual scenario review.
- AI Act: continuous + lifecycle.
- Trigger alignment: SAME on continuous.

**Threshold/timeline comparison:**
- DORA: "high standards".
- AI Act: "as resilient as possible".
- Tension: NONE.

**Recipient comparison:**
- DORA: CA.
- AI Act: conformity-assessment body + MSA + AI Office.

**Classified relationship (from CRDA):** DIFFERENT PERSPECTIVE.

**Verified relationship (after OJ-text analysis):** SAME (CORRECTED — wording only).

**Reasoning:** Different objects (ICT-system integrity cell vs AI-system resilience). DORA's integrity cell applies to the AI substrate (data + transmission); AI Act's Art. 15(3) applies to the AI subsystem above it. A DORA financial entity deploying high-risk AI has both layers stacked.

**Scope-disjoint test:** Y for the DORA financial entity deploying high-risk AI.

**Downstream implication:** Layered stack with DORA Art. 9(2) integrity + AI Act Art. 15(3) resilience + AI Act Art. 15(1) accuracy/robustness/cybersecurity.

---


## Summary (Domain Analysis)

| DORA ↔ AI_Act | **Different perspective** | Tension/difference |
|---|---|---|
| **DORA** (SR-DORA-001, Art. 9(2)) | Integrity is one of the 4×3 CIA+A cells | Financial entity; CIA+A 4×3 matrix |
| **AI_Act** (SR-AIACT-014 + SR-AIACT-015, Art. 15(1)+(3)) | Accuracy + robustness + cybersecurity; resilience | High-risk AI provider; system-resilience framing |

**Why Different perspective**: DORA's integrity cell is one of four CIA+A dimensions; AI Act's resilience is a system-level property bundled with accuracy and robustness. The two converge on the integrity-of-data property at the cell level but diverge on the AI-system resilience scope. A DORA financial entity deploying high-risk AI (e.g. credit scoring) operates both: ICT-system integrity (DORA) + AI-system resilience (AI Act). → full rationale: `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-001; `../../../Regulation/AI_Act/02_SecurityRules_NIST.md` SR-AIACT-014 + SR-AIACT-015



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
39 lines — see ../../_migration_report.md)_

