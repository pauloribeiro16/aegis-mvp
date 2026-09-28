# D-10.3 — Pair analysis: GDPR ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ DORA

**GDPR article (verbatim, Art. 32(1)(d)):**
> [as quoted above]

**DORA article (verbatim, Art. 24 + Art. 25 + Art. 26):**
> "Financial entities shall, in accordance with Chapter II, establish, maintain and review a sound and comprehensive digital operational resilience testing programme as an integral part of the ICT risk-management framework." — Art. 24(1) DORA (per SR-DORA-008)
> "The testing programme shall provide for the use of appropriate testing methodologies, including vulnerability assessments and scans, open source analyses, network security assessments, gap analyses, physical security reviews, questionnaires and scanning software solutions, source code reviews where feasible, scenario-based tests, compatibility testing, performance testing, end-to-end testing and penetration testing." — Art. 25(1) DORA (per SR-DORA-008)
> "Significant financial entities shall, on a regular basis, carry out advanced testing of their ICT systems using threat-led penetration testing." — Art. 26(1) DORA (TLPT)

**Scope comparison:**
- GDPR scope: regular testing of security-measure effectiveness.
- DORA scope: testing programme with 12-way testing modalities portfolio + TLPT for significant entities.
- Scope overlap: **Conditional (Y when the DORA financial entity is a controller processing personal data)**.

**Trigger comparison:**
- GDPR trigger: effectiveness-evaluation.
- DORA trigger: testing programme + TLPT.
- Trigger alignment: **PARTIAL** (different scopes — security measures vs. ICT operational resilience).

**Threshold/timeline comparison:**
- GDPR: `regularly testing`.
- DORA: `on a regular basis` for TLPT.
- Tension: **NONE**.

**Recipient comparison:**
- GDPR: data subject, DPA.
- DORA: NCA.

**Content template comparison:**
- GDPR: not codified for content.
- DORA: 12-way testing modalities (Art. 25(1)) + TLPT (Art. 26(1)).

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** DORA's testing programme is the dominant authority for financial entities with explicit TLPT obligation. GDPR regular testing is a sub-component.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Conditional (Y when the DORA financial entity is a controller adopting testing programmes)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce a DORA-led stack: DORA Art. 24 testing programme + Art. 25 modalities + Art. 26 TLPT (for significant entities) + GDPR Art. 32(1)(d) effectiveness-evaluation as sub-component.

---
