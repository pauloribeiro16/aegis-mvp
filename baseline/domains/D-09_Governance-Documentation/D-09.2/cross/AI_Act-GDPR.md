# D-09.2 — Pair analysis: GDPR ↔ AI Act

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ AI_Act

**GDPR article (verbatim, Art. 35(1) + Art. 35(7)):**
> [as quoted above]

**AI_Act article (verbatim, Art. 9(1) + Art. 9(2)):**
> "A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems." — Art. 9(1) AI Act (per SR-AIACT-001)
> "The risk management system shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks to health, safety and fundamental rights; (b) the estimation and evaluation of the risks emerging from use under conditions of reasonably foreseeable misuse; (c) the evaluation of other risks arising from analysis of post-market monitoring data; (d) the adoption of appropriate and targeted risk management measures …" — Art. 9(2)(a)–(d) AI Act (per SR-AIACT-002)

**Scope comparison:**
- GDPR scope: pre-launch DPIA for high-risk personal-data processing.
- AI Act scope: continuous, iterative risk-management system across AI lifecycle with 4-step process.
- Scope overlap: **Y (when a high-risk AI system processes personal data).**

**Trigger comparison:**
- GDPR trigger: high-risk processing event.
- AI Act trigger: high-risk AI system lifecycle (continuous + iterative).
- Trigger alignment: **PARTIAL** (different cadences — pre-launch DPIA vs. continuous).

**Threshold/timeline comparison:**
- GDPR: DPIA before processing + review on change of risk.
- AI Act: continuous + iterative across lifecycle.
- Tension: **NONE**.

**Recipient comparison:**
- GDPR: DPA.
- AI Act: provider, MSA.

**Content template comparison:**
- GDPR: 4-item Art. 35(7) content.
- AI Act: 4-step closed list (a)–(d) + Art. 27 FRIA for certain Annex III categories.

**Classified relationship (from CRDA):** DIFFERENT-PERSPECTIVE
**Verified relationship (after OJ-text analysis):** **SAME — DIFFERENT-PERSPECTIVE**
**Reasoning:** GDPR DPIA is pre-launch for high-risk processing; AI Act Art. 9 risk management is continuous across the AI lifecycle. The two assessments overlap in scope for AI systems processing personal data but the triggers differ (high-risk-processing trigger vs. high-risk-AI trigger). AI Act Recital 78 preserves GDPR; the two stack without substitution.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y (when a high-risk AI system processes personal data — Art. 27 FRIA may be required for certain Annex III categories)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce two separate artefacts: GDPR Art. 35 DPIA + AI Act Art. 9 risk-management system + Art. 27 FRIA where applicable. AI Act Recital 78 preservation is the operative OJ cross-link.

---


## Summary (Domain Analysis)

| GDPR ↔ AI_Act | **different-perspective** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-045, Art. 35(1)-(4)) | DPIA pre-launch. | |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-045 |
| **AI_Act** (SR-AIACT-001, Art. 9(1)+(2); SR-AIACT-002, Art. 9(2) 4-step list) | Continuous, iterative risk management system across AI lifecycle with 4-step process. | |
|   → full rationale: `../../../Regulation/AI_Act/02_SecurityRules_NIST.md` SR-AIACT-001 / SR-AIACT-002 |

**Why different-perspective**: GDPR DPIA is pre-launch for high-risk processing; AI Act Art. 9 risk management is continuous across the AI lifecycle. The two assessments overlap in scope for AI systems processing personal data but the triggers differ (high-risk-processing trigger vs. high-risk-AI trigger). AI Act Recital 78 preserves GDPR; the two stack without substitution.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_

