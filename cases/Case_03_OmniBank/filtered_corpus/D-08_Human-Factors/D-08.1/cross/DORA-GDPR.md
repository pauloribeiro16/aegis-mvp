# D-08.1 — Pair analysis: GDPR ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ DORA

**GDPR article (verbatim, Art. 39(1)(a)+(b)):**
> [as quoted above]

**DORA article (verbatim, Art. 13(6)):**
> "Financial entities shall develop ICT security awareness programmes and digital operational resilience training as compulsory modules in their staff training schemes, with a level of complexity commensurate to the remit of their functions." — Art. 13(6) DORA (per SR-DORA-025)

**Scope comparison:**
- GDPR scope: DPO-driven staff awareness.
- DORA scope: compulsory ICT security awareness + digital operational resilience training modules.
- Scope overlap: **Y (when a DORA financial entity is a controller processing personal data over its own staff).**

**Trigger comparison:**
- GDPR trigger: DPO-catalysed awareness activity.
- DORA trigger: compulsory-modules-in-training-schemes requirement.
- Trigger alignment: **PARTIAL** (both staff-targeted but different governance hooks).

**Threshold/timeline comparison:**
- GDPR: no quantitative cadence.
- DORA: `compulsory` (completion-mandatory) per SR-DORA-025 reading; cadence entity-discretionary.
- Tension: **NONE**.

**Recipient comparison:**
- GDPR: data subject, DPA.
- DORA: management body, NCA.

**Content template comparison:**
- GDPR: DPO-discretionary curriculum.
- DORA: `commensurate to the remit of their functions` (Art. 13(6) per SR-DORA-025).

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** DORA training is compulsory-modules-led; GDPR awareness is DPO-catalysed. DORA's `commensurate to the remit of their functions` phrasing subsumes GDPR's role-specific dimension; the two regimes stack with the DORA programme as the carrier and GDPR content as a module.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y (when the DORA financial entity is a controller with workforce awareness obligations)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce a DORA-led stack: DORA Art. 13(6) compulsory modules as carrier + GDPR Art. 39(1) data-protection module as sub-component.

---


## Summary (Domain Analysis)

<!-- pair: GDPR,DORA -->
| GDPR ↔ DORA | **complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-042, Art. 39(1)(a)+(b)) | DPO-driven GDPR awareness. | |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-042 |
| **DORA** (SR-DORA-025, Art. 13(6)) | Compulsory ICT security awareness and digital operational resilience training. | |
|   → full rationale: `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-025 |

**Why complementary**: DORA training is compulsory-modules-led; GDPR awareness is DPO-catalysed. DORA's `commensurate to the remit of their functions` phrasing subsumes GDPR's role-specific dimension; the two regimes stack with the DORA programme as the carrier and GDPR content as a module.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
41 lines — see ../../_migration_report.md)_