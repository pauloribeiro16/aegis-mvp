# D-08.1 — Pair analysis: GDPR ↔ NIS 2

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ NIS2

**GDPR article (verbatim, Art. 39(1)(a)+(b)):**
> "The data protection officer shall … (a) inform and advise the controller or the processor and the employees who carry out processing of their obligations pursuant to this Regulation and to other Union or Member State data protection provisions; (b) monitor compliance with this Regulation, including the assignment of responsibilities, awareness-raising and training of staff involved in processing operations …" — Art. 39(1)(a)+(b) GDPR

**NIS2 article (verbatim, Art. 21(2)(g) first clause):**
> "[Member States shall ensure that essential and important entities take appropriate and proportionate technical, operational and organisational measures to … ] (g) basic cyber hygiene practices and cybersecurity training." — Art. 21(2)(g) first clause NIS 2 (per SR-NIS2-029)

**Scope comparison:**
- GDPR scope: DPO-driven awareness and training of staff involved in processing operations.
- NIS 2 scope: entity-wide basic cyber hygiene baseline (workforce-and-systems substrate).
- Scope overlap: **Y (when the controller-NSIE's workforce needs both data-protection awareness and cyber-hygiene training).**

**Trigger comparison:**
- GDPR trigger: DPO-catalysed awareness/training activity.
- NIS 2 trigger: cyber-hygiene baseline training.
- Trigger alignment: **DIFFERENT** (DPO-driven data-protection focus vs. hygiene focus).

**Threshold/timeline comparison:**
- GDPR: no quantitative cadence (DPO-discretionary under Recital 56).
- NIS 2: no quantitative cadence (entity-discretionary under Recital 56).
- Tension: **NONE**.

**Recipient comparison:**
- GDPR: data subject, DPA.
- NIS 2: management body, competent authority.

**Content template comparison:**
- GDPR: not codified for content (DPO-discretionary).
- NIS 2: not codified for content (entity-discretionary under Recital 56).

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** GDPR awareness is DPO-driven and data-protection-focused; NIS 2 awareness is hygiene-focused (phishing, password discipline, removable-media). The two training programmes can be combined into a single curriculum where the data-protection module feeds the GDPR obligation and the hygiene module feeds the NIS 2 obligation.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y (when the controller-NSIE operates a single training programme covering both DPO-catalysed data-protection and hygiene modules)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce a unified training curriculum: GDPR module (data-protection awareness, DPO-catalysed) + NIS 2 module (cyber-hygiene baseline, entity-discretionary).

---


## Summary (Domain Analysis)

<!-- pair: GDPR,NIS2 -->
| GDPR ↔ NIS2 | **complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-042, Art. 39(1)(a)+(b)) | DPO drives awareness and training of staff involved in processing operations. | |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-042 |
| **NIS2** (SR-NIS2-029, Art. 21(2)(g)) | Basic cyber-hygiene practices baseline across workforce and systems. | |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-029 |

**Why complementary**: GDPR awareness is DPO-driven and data-protection-focused; NIS 2 awareness is hygiene-focused (phishing, password discipline, removable-media). The two training programmes can be combined into a single curriculum where the data-protection module feeds the GDPR obligation and the hygiene module feeds the NIS 2 obligation.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
41 lines — see ../../_migration_report.md)_