# D-09.2 — Pair analysis: NIS 2 ↔ AI Act

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: NIS2 ↔ AI_Act

**NIS2 article (verbatim, Art. 21(2)(a)):**
> [as quoted above]

**AI_Act article (verbatim, Art. 9(1) + Art. 9(2)):**
> [as quoted above]

**Scope comparison:**
- NIS 2 scope: entity-level operational risk-analysis policy.
- AI Act scope: AI-system continuous, iterative risk-management system with 4-step process.
- Scope overlap: **Y (when an NSIE deploys high-risk AI).**

**Trigger comparison:**
- NIS 2 trigger: continuous operational analysis.
- AI Act trigger: high-risk AI system lifecycle (continuous + iterative).
- Trigger alignment: **SAME** (both continuous).

**Threshold/timeline comparison:**
- NIS 2: continuous.
- AI Act: continuous + iterative across lifecycle.
- Tension: **NONE**.

**Recipient comparison:**
- NIS 2: management body, competent authority.
- AI Act: provider, MSA.

**Content template comparison:**
- NIS 2: not codified for content.
- AI Act: 4-step closed list (a)–(d).

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** NIS 2 risk analysis is entity-level operational; AI Act risk management is AI-system-level continuous. For NSIEs deploying high-risk AI, both apply — the AI Act layer adds the AI-specific 4-step process to the NIS 2 risk-analysis policy.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y (when the NSIE deploys high-risk AI)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce a layered stack: NIS 2 Art. 21(2)(a) entity-level risk-analysis policy + AI Act Art. 9 AI-system risk-management system as sub-component.

---


## Summary (Domain Analysis)

| NIS2 ↔ AI_Act | **complementary** | Tension/difference |
|---|---|---|
| **NIS2** (SR-NIS2-035, Art. 21(2)(a)) | Risk-analysis policy. | |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-035 |
| **AI_Act** (SR-AIACT-001, Art. 9(1); SR-AIACT-002, Art. 9(2)) | Continuous iterative risk management system with 4-step process. | |
|   → full rationale: `../../../Regulation/AI_Act/02_SecurityRules_NIST.md` SR-AIACT-001 / SR-AIACT-002 |

**Why complementary**: NIS 2 risk analysis is entity-level operational; AI Act risk management is AI-system-level continuous. For NSIEs deploying high-risk AI, both apply — the AI Act layer adds the AI-specific 4-step process to the NIS 2 risk-analysis policy.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
41 lines — see ../../_migration_report.md)_

