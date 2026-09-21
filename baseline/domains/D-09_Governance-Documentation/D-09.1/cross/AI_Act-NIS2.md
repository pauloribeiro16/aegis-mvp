# D-09.1 — Pair analysis: NIS 2 ↔ AI Act

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: NIS2 ↔ AI_Act

**NIS2 article (verbatim, Art. 20(1) + Art. 21(2)(a)):**
> [as quoted above]

**AI_Act article (verbatim, Art. 17(1)):**
> "Providers of high-risk AI systems shall put a quality management system in place that ensures compliance with this Regulation. That system shall be documented in a systematic and orderly manner in the form of written policies, procedures and instructions, and shall include at least the following aspects: (a) … (m)" — Art. 17(1) AI Act (per SR-AIACT-017)

**Scope comparison:**
- NIS 2 scope: entity-level risk-analysis policy + IS-security policy + management-body approval.
- AI Act scope: provider-side QMS with 13 enumerated aspects.
- Scope overlap: **Y (when an NSIE deploys high-risk AI and the AI Act QMS becomes a sub-policy).**

**Trigger comparison:**
- NIS 2 trigger: entity adoption of policies.
- AI Act trigger: provider QMS establishment.
- Trigger alignment: **PARTIAL** (both policy-driven).

**Threshold/timeline comparison:**
- NIS 2: no quantitative cadence.
- AI Act: no quantitative cadence.
- Tension: **NONE**.

**Recipient comparison:**
- NIS 2: management body, competent authority.
- AI Act: provider, MSA, AI Office.

**Content template comparison:**
- NIS 2: Art. 21(2)(a)+(f) policy artefacts.
- AI Act: 13-element closed list (a)–(m).

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** NIS 2 governance applies at the entity level; AI Act QMS applies at the AI-system level. For NSIEs deploying high-risk AI, the QMS becomes a sub-policy of the entity-level NIS 2 governance framework.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y (when the NSIE deploys high-risk AI and integrates QMS into the entity-level framework)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce a layered stack: NIS 2 Art. 21(2)(a)+(f) entity-level policies + AI Act Art. 17(1) QMS as sub-policy.

---


## Summary (Domain Analysis)

| NIS2 ↔ AI_Act | **complementary** | Tension/difference |
|---|---|---|
| **NIS2** (SR-NIS2-032, Art. 20(1); SR-NIS2-035, Art. 21(2)(a)) | Management body approval + risk-analysis policy. | |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-032 / SR-NIS2-035 |
| **AI_Act** (SR-AIACT-017, Art. 17(1) QMS) | QMS with 13 enumerated aspects as the AI-system policy carrier. | |
|   → full rationale: `../../../Regulation/AI_Act/02_SecurityRules_NIST.md` SR-AIACT-017 |

**Why complementary**: NIS 2 governance applies at the entity level; AI Act QMS applies at the AI-system level. For NSIEs deploying high-risk AI, the QMS becomes a sub-policy of the entity-level NIS 2 governance framework.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
41 lines — see ../../_migration_report.md)_

