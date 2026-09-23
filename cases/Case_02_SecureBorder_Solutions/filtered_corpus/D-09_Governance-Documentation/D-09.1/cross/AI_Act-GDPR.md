# D-09.1 — Pair analysis: GDPR ↔ AI Act

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ AI_Act

**GDPR article (verbatim, Art. 24(1) + Art. 5(2)):**
> [as quoted above]

**AI_Act article (verbatim, Art. 13(1) + Art. 17(1) + Art. 26(1)):**
> "The quality management system shall be documented in a systematic and orderly manner in the form of written policies, procedures and instructions, and shall include at least the following aspects: (a) … (m)" — Art. 17(1) AI Act (per SR-AIACT-017)
> "Deployers of high-risk AI systems shall take appropriate technical and organisational measures to ensure they use such systems in accordance with the instructions for use accompanying the systems." — Art. 26(1) AI Act (per SR-AIACT-019)

**Scope comparison:**
- GDPR scope: controller-side data-protection policies.
- AI Act scope: provider-side QMS (Art. 17(1)) + deployer-side measures aligned with provider instructions (Art. 26(1)).
- Scope overlap: **Y (when the provider/deployer is a controller).**

**Trigger comparison:**
- GDPR trigger: controller's adoption of data-protection policies.
- AI Act trigger: provider QMS establishment + deployer measures aligned with provider instructions.
- Trigger alignment: **PARTIAL** (both policy-driven but different governance hooks).

**Threshold/timeline comparison:**
- GDPR: no quantitative cadence.
- AI Act: no quantitative cadence.
- Tension: **NONE**.

**Recipient comparison:**
- GDPR: data subject, DPA.
- AI Act: provider, deployer, MSA, AI Office.

**Content template comparison:**
- GDPR: not codified for content.
- AI Act: 13-element closed list (a)–(m) in Art. 17(1).

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** GDPR data-protection policies stack with AI Act QMS policies; AI Act does not displace GDPR. AI Act Recital 78 explicitly preserves GDPR.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y (when the provider/deployer is a controller processing personal data via high-risk AI)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce a layered stack: GDPR Art. 24 data-protection policies + AI Act Art. 17(1) QMS + AI Act Art. 26(1) deployer measures.

---


## Summary (Domain Analysis)

<!-- pair: GDPR,AI_Act -->
| GDPR ↔ AI_Act | **complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-043, Art. 24(1)+(2)) | Appropriate data-protection policies. | |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-043 |
| **AI_Act** (SR-AIACT-010, Art. 13(1)+(3); SR-AIACT-011, Art. 17(1); SR-AIACT-017, Art. 17(1) QMS; SR-AIACT-019, Art. 26(1) deployer measures aligned with instructions) | Transparency to deployers + instructions for use; QMS with 13 enumerated aspects; deployer-side measures. | |
|   → full rationale: `../../../Regulation/AI_Act/02_SecurityRules_NIST.md` SR-AIACT-010 / SR-AIACT-011 / SR-AIACT-017 / SR-AIACT-019 |

**Why complementary**: GDPR data-protection policies stack with AI Act QMS policies; AI Act does not displace GDPR for personal-data processing. AI Act Recital 78 explicitly preserves GDPR.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_