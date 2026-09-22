# D-10.3 — Pair analysis: GDPR ↔ AI Act

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ AI_Act

**GDPR article (verbatim, Art. 32(1)(d)):**
> [as quoted above]

**AI_Act article (verbatim, Art. 9(6)+(7) + Art. 15(1)):**
> "High-risk AI systems shall be tested for the purpose of identifying the most appropriate and targeted risk management measures. Testing shall ensure that high-risk AI systems perform consistently for their intended purpose." — Art. 9(6) AI Act (per SR-AIACT-003)
> "Testing procedures may include testing in real-world conditions in accordance with Article 60." — Art. 9(7) AI Act
> "High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle." — Art. 15(1) AI Act (per SR-AIACT-014)

**Scope comparison:**
- GDPR scope: regular testing of security-measure effectiveness.
- AI Act scope: testing for risk management + real-world-conditions testing + accuracy/robustness/cybersecurity baseline testing.
- Scope overlap: **Conditional (Y when the high-risk AI system processes personal data)**.

**Trigger comparison:**
- GDPR trigger: effectiveness-evaluation.
- AI Act trigger: high-risk AI system testing + real-world-conditions testing.
- Trigger alignment: **PARTIAL**.

**Threshold/timeline comparison:**
- GDPR: `regularly testing`.
- AI Act: `tested for the purpose of identifying the most appropriate and targeted risk management measures` + `perform consistently … throughout their lifecycle` (Art. 15(1)).
- Tension: **NONE**.

**Recipient comparison:**
- GDPR: data subject, DPA.
- AI Act: provider, MSA.

**Content template comparison:**
- GDPR: not codified for content.
- AI Act: Art. 9(6) testing + Art. 9(7) real-world-conditions testing + Art. 60 detailed rules.

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** GDPR regular testing + AI Act real-world-conditions testing stack for AI systems processing personal data. The AI Act layer adds real-world-conditions testing as a specific dimension.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Conditional (Y when the high-risk AI system processes personal data)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce a layered stack: GDPR Art. 32(1)(d) effectiveness-evaluation + AI Act Art. 9(6)+(7) + Art. 15(1) AI-system testing.

---
