# D-07.1 — Pair analysis: GDPR ↔ AI Act

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ AI_Act

**GDPR article (verbatim, Art. 25(1)):**
> [as quoted above]

**AI_Act article (verbatim, Art. 15(1) + Art. 17(1)(c)):**
> "High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle." — Art. 15(1) AI Act
> "The quality management system shall include at least the following aspects: … (c) the techniques, procedures and systematic actions to be used for the design, design control and design verification of the high-risk AI system." — Art. 17(1)(c) AI Act

**Scope comparison:**
- GDPR scope: controller-side data-protection by-design.
- AI Act scope: high-risk AI system design (accuracy, robustness, cybersecurity) + QMS-level design control.
- Scope overlap: **Y (when a high-risk AI system processes personal data and the provider/deployer is a controller).**

**Trigger comparison:**
- GDPR trigger: controller's means-determination.
- AI Act trigger: design/development of high-risk AI system + QMS design-control subprocess.
- Trigger alignment: **DIFFERENT** (data-protection focus vs. AI-system design focus) but co-applicable.

**Threshold/timeline comparison:**
- GDPR: no quantitative threshold.
- AI Act: no quantitative threshold for accuracy/robustness/cybersecurity (qualitative envelope); lifecycle-consistency clause is qualitative.
- Tension: **NONE**.

**Recipient comparison:**
- GDPR: supervisory authority (DPA).
- AI Act: provider, market surveillance authority, AI Office.

**Content template comparison:**
- GDPR: documented Art. 25(1) assessment.
- AI Act: QMS documented design-control procedures + Annex IV technical documentation.

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** GDPR Art. 25(1) addresses data-protection by-design; AI Act Art. 15(1) + Art. 17(1)(c) addresses high-risk AI system design (accuracy / robustness / cybersecurity) and the QMS design-control sub-process. AI-Act-Recital 78 explicitly preserves the GDPR. The two obligations stack — a high-risk AI system processing personal data discharges both with distinct design outputs (privacy property vs. AI-system property). No overlap in object; full coverage requires both.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y (when the provider-deployer is a controller processing personal data via a high-risk AI system)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce a 2-track by-design matrix: (1) GDPR Art. 25(1) data-protection by-design for personal data; (2) AI Act Art. 15(1) + Art. 17(1)(c) AI-system design with QMS design-control. Recital 78 preservation is the operative OJ cross-link.

---


## Summary (Domain Analysis)

<!-- pair: GDPR,AI_Act -->
| GDPR ↔ AI_Act | **complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-039, Art. 25(1)) | Privacy-by-design integrated at means-determination. | |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-039 |
| **AI_Act** (SR-AIACT-014, Art. 15(1); SR-AIACT-018, Art. 17(1)(c)) | Accuracy/robustness/cybersecurity baseline + design/design control/design verification in QMS. | |
|   → full rationale: `../../../Regulation/AI_Act/02_SecurityRules_NIST.md` SR-AIACT-014 / SR-AIACT-018 |

**Why complementary**: GDPR by-design addresses privacy data flows; AI Act by-design addresses high-risk AI system properties (accuracy, robustness, cybersecurity). AI-Act-Recital-78 explicitly preserves the GDPR, so the two obligations stack — a high-risk AI system processing personal data discharges both simultaneously with distinct design outputs (privacy property vs. AI property).



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_