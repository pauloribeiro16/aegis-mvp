# D-07.1 — Pair analysis: CRA ↔ AI Act

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: CRA ↔ AI_Act

**CRA article (verbatim, Art. 13(1) + Art. 13(4) sentence 2):**
> [as quoted above, plus]
> "The cybersecurity risk assessment referred to in paragraph 2 shall be part of, or combined with, the risk assessment required by other Union legal acts applicable to the product with digital elements." — Art. 13(4) sentence 2 CRA

**AI_Act article (verbatim, Art. 15(1) + Art. 17(1)(c)):**
> [as quoted in GDPR ↔ AI_Act above]

**Scope comparison:**
- CRA scope: manufacturer-side product cybersecurity.
- AI Act scope: high-risk AI system design + QMS design control.
- Scope overlap: **Y (for AI-enabled CRA products, the same product is both CRA-regulated and AI-Act high-risk).**

**Trigger comparison:**
- CRA trigger: manufacturer places product on market.
- AI Act trigger: design/development of high-risk AI system.
- Trigger alignment: **DIFFERENT** but co-applicable.

**Threshold/timeline comparison:**
- CRA: support period ≥ 5 years.
- AI Act: lifecycle-consistency qualitative.
- Tension: **NONE**.

**Recipient comparison:**
- CRA: MSA.
- AI Act: MSA, AI Office.

**Content template comparison:**
- CRA: Annex VII technical documentation.
- AI Act: QMS design control + Annex IV technical documentation.

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** For an AI-enabled product (CRA-regulated product that embeds a high-risk AI system), both regimes apply. CRA Art. 13(4) sentence 2 explicitly permits a "unified risk assessment" under AI Act Art. 9 to substitute for the CRA risk assessment when both apply — see SR-CRA-066 ambiguity_notes. The AI Act QMS and CRA Annex I conformity stack with the explicit cross-regulation consolidation rule for risk assessment.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y (when the same product is both CRA-regulated and AI-Act high-risk)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must operationalise CRA Art. 13(4) sentence 2: a unified risk assessment under AI Act Art. 9 substitutes for CRA risk assessment when both apply. QMS (AI Act) + Annex I conformity (CRA) stack with documented cross-walk.

---


## Summary (Domain Analysis)

<!-- pair: CRA,AI_Act -->
| CRA ↔ AI_Act | **complementary** | Tension/difference |
|---|---|---|
| **CRA** (SR-CRA-064, Art. 13(1); SR-CRA-065, Art. 13(2)) | Product-level design/development/production per Annex I Part I. | |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-064 / SR-CRA-065 |
| **AI_Act** (SR-AIACT-014, Art. 15(1); SR-AIACT-018, Art. 17(1)(c)) | AI-system-specific design + QMS with 13 enumerated aspects. | |
|   → full rationale: `../../../Regulation/AI_Act/02_SecurityRules_NIST.md` SR-AIACT-014 / SR-AIACT-018 |

**Why complementary + partial overlap**: For an AI-enabled product (e.g., a CRA-regulated product that embeds a high-risk AI system), both regimes apply. CRA Annex I (2)(l) (recording and monitoring) and AI Act Art. 12 (logging) operate on different layers (product internal vs. AI system). CRA Art. 13(4) sentence 2 explicitly permits a "unified risk assessment" under AI Act Art. 9 to substitute for the CRA risk assessment when both apply — see SR-CRA-066 ambiguity_notes for the cross-regulation consolidation rule.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_