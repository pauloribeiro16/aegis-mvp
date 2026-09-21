# D-07.1 — Pair analysis: NIS 2 ↔ AI Act

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: NIS2 ↔ AI_Act

**NIS2 article (verbatim, Art. 21(2)(e)):**
> [as quoted above]

**AI_Act article (verbatim, Art. 15(1) + Art. 17(1)(c)):**
> [as quoted in GDPR ↔ AI_Act above]

**Scope comparison:**
- NIS 2 scope: entity-level security of NIS across acquisition, development, maintenance.
- AI Act scope: high-risk AI system design + QMS design-control.
- Scope overlap: **Y (when NIS embeds a high-risk AI system).**

**Trigger comparison:**
- NIS 2 trigger: NIS lifecycle activity.
- AI Act trigger: high-risk AI system design/development.
- Trigger alignment: **DIFFERENT** but co-applicable on NIS that embed AI.

**Threshold/timeline comparison:**
- NIS 2: no quantitative threshold.
- AI Act: no quantitative threshold.
- Tension: **NONE**.

**Recipient comparison:**
- NIS 2: management body, competent authority.
- AI Act: provider, market surveillance authority.

**Content template comparison:**
- NIS 2: not codified for content.
- AI Act: QMS design-control + Annex IV.

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** NIS 2 Art. 21(2)(e) development-time obligations apply to NIS that embed AI; AI Act Art. 15(1) + Art. 17(1)(c) design obligations apply to high-risk AI systems regardless of NIS status. The regimes stack — NIS 2 procurement gate (SR-NIS2-026) and AI Act QMS (SR-AIACT-017) both apply to the same entity, with the AI Act design verification record supplementing the NIS 2 supplier-assessment evidence.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y (when NIS embeds high-risk AI)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce a layered AI-NIS stack: NIS 2 Art. 21(2)(e) lifecycle evidence + AI Act QMS design verification as separate artefacts.

---


## Summary (Domain Analysis)

| NIS2 ↔ AI_Act | **complementary** | Tension/difference |
|---|---|---|
| **NIS2** (SR-NIS2-027, Art. 21(2)(e) development) | Security in NIS development (OJ literal — T3-vs-text gap per synthesis §8). | |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-027 |
| **AI_Act** (SR-AIACT-014, Art. 15(1); SR-AIACT-018, Art. 17(1)(c)) | AI-system design with accuracy/robustness/cybersecurity baseline + QMS design controls. | |
|   → full rationale: `../../../Regulation/AI_Act/02_SecurityRules_NIST.md` SR-AIACT-014 / SR-AIACT-018 |

**Why complementary**: NIS 2 development-time obligations apply to NIS that embed AI; AI Act design obligations apply to high-risk AI systems regardless of NIS status. The regimes stack — NIS 2 procurement gate (SR-NIS2-026) and AI Act QMS (SR-AIACT-017) both apply to the same entity, with the AI-Act design verification record supplementing the NIS 2 supplier-assessment evidence.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
41 lines — see ../../_migration_report.md)_

