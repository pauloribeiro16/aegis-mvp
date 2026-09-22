# D-09.4 — Pair analysis: GDPR ↔ AI Act

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ AI_Act

**GDPR article (verbatim, Art. 30(1)–(4)):**
> [as quoted above]

**AI_Act article (verbatim, Art. 11 + Art. 12 + Art. 17(1)):**
> "Providers of high-risk AI systems shall keep the logs referred to in Article 12(1) … to the extent that such logs are under their control." — Art. 19(1) AI Act (per SR-AIACT-008/009)
> "The quality management system shall be documented in a systematic and orderly manner in the form of written policies, procedures and instructions …" — Art. 17(1) AI Act (per SR-AIACT-017)

**Scope comparison:**
- GDPR scope: controller/processor RoPA.
- AI Act scope: technical documentation (Annex IV via Art. 11/12) + QMS documentation of 13 enumerated aspects.
- Scope overlap: **Conditional (Y when the provider is a controller processing personal data)**.

**Trigger comparison:**
- GDPR trigger: processing of personal data.
- AI Act trigger: high-risk AI system design + QMS.
- Trigger alignment: **DIFFERENT**.

**Threshold/timeline comparison:**
- GDPR: 250-employee carve-out.
- AI Act: no quantitative retention for documentation (Art. 11/12 + Art. 17(1)).
- Tension: **NONE**.

**Recipient comparison:**
- GDPR: data subject, DPA.
- AI Act: provider, MSA.

**Content template comparison:**
- GDPR: Art. 30(1)/(2) content items.
- AI Act: Annex IV technical documentation + 13-element QMS list.

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** GDPR RoPA + AI Act Annex IV technical documentation + AI Act Art. 17 QMS documentation stack. AI Act does not displace GDPR.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Conditional (Y when the provider is a controller)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce a layered stack: GDPR Art. 30 RoPA + AI Act Annex IV + AI Act Art. 17 QMS.

---


## Summary (Domain Analysis)

<!-- pair: GDPR,AI_Act -->
| GDPR ↔ AI_Act | **complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-048, Art. 30(1)-(4)) | RoPA mandate. | |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-048 |
| **AI_Act** (SR-AIACT-009, Art. 15(1) accuracy/robustness/cybersecurity baseline; SR-AIACT-010, Art. 13(1)+(3); SR-AIACT-017, Art. 17(1) QMS) | Technical documentation (Annex IV) + QMS documentation. | |
|   → full rationale: `../../../Regulation/AI_Act/02_SecurityRules_NIST.md` SR-AIACT-009 / SR-AIACT-010 / SR-AIACT-017 |

**Why complementary**: GDPR RoPA + AI Act Annex IV technical documentation + AI Act Art. 17 QMS documentation stack. AI Act does not displace GDPR.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_