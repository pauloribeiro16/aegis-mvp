# D-09.2 — Pair analysis: GDPR ↔ NIS 2

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ NIS2

**GDPR article (verbatim, Art. 35(1) + Art. 35(7)):**
> "Where a type of processing is likely to result in a high risk to the rights and freedoms of natural persons, the controller shall, prior to processing, carry out an assessment of the impact of the envisaged processing operations on the protection of personal data …" — Art. 35(1) GDPR
> "The assessment shall contain at least: (a) a systematic description of the envisaged processing operations and the purposes of the processing, including, where applicable, the legitimate interest pursued by the controller; (b) an assessment of the necessity and proportionality of the processing operations in relation to the purposes; (c) an assessment of the risks to the rights and freedoms of data subjects; (d) the measures envisaged to address the risks …" — Art. 35(7) GDPR

**NIS2 article (verbatim, Art. 21(2)(a) + Art. 21(1) + Art. 22(1)):**
> "[Member States shall ensure that essential and important entities take appropriate and proportionate technical, operational and organisational measures to … ] (a) policies on risk analysis and information system security …" — Art. 21(2)(a) NIS 2 (per SR-NIS2-035)
> "[Member States shall ensure that essential and important entities take appropriate and proportionate … measures to … ] taking into account the degree of exposure of the entity to risks … the likelihood of incidents … their severity …" — Art. 21(1) NIS 2 (per SR-NIS2-039)

**Scope comparison:**
- GDPR scope: pre-launch DPIA for high-risk personal-data processing, with 4 Art. 35(7) content items.
- NIS 2 scope: operational (continuous) risk-analysis policy + methodology, not pre-launch.
- Scope overlap: **N (typically)** — different triggers (pre-launch DPIA vs. continuous operational analysis).

**Trigger comparison:**
- GDPR trigger: high-risk processing event.
- NIS 2 trigger: ongoing NIS operations + risk-analysis policy.
- Trigger alignment: **DIFFERENT**.

**Threshold/timeline comparison:**
- GDPR: DPIA before processing + review on change of risk (Art. 35(11)).
- NIS 2: continuous methodology.
- Tension: **NONE**.

**Recipient comparison:**
- GDPR: supervisory authority (DPA), data subjects.
- NIS 2: management body, competent authority.

**Content template comparison:**
- GDPR: 4-item Art. 35(7) content.
- NIS 2: not codified for content (entity-discretionary under Recital 56).

**Classified relationship (from CRDA):** DIFFERENT-PERSPECTIVE
**Verified relationship (after OJ-text analysis):** **SAME — DIFFERENT-PERSPECTIVE**
**Reasoning:** GDPR DPIA is pre-launch for high-risk processing; NIS 2 risk analysis is operational (continuous, not pre-launch). The two regimes do not substitute — a controller-NSIE must operate both. Different triggers and review cadences; no OJ-level consolidation rule.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Conditional (Y when the DPIA is conducted for an NSIE's processing; N otherwise)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce two separate artefacts: GDPR Art. 35 DPIA (pre-launch) + NIS 2 Art. 21(2)(a) continuous risk-analysis policy.

---


## Summary (Domain Analysis)

<!-- pair: GDPR,NIS2 -->
| GDPR ↔ NIS2 | **different-perspective** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-045, Art. 35(1)-(4); SR-GDPR-046, Art. 35(7); SR-GDPR-047, Art. 35(11)) | DPIA with four Art. 35(7) content items; reviewed on change of risk. | |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-045 / SR-GDPR-046 / SR-GDPR-047 |
| **NIS2** (SR-NIS2-035, Art. 21(2)(a); SR-NIS2-039, Art. 21(1) appropriate-and-proportionate measures; SR-NIS2-040, all-hazards methodology) | Documented risk-analysis methodology with proportional scope; no DPIA-like pre-launch obligation. | |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-035 / SR-NIS2-039 / SR-NIS2-040 |

**Why different-perspective**: GDPR DPIA is pre-launch for high-risk processing; NIS 2 risk analysis is operational (continuous, not pre-launch). The two regimes do not substitute — a controller-NSIE must operate both.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
43 lines — see ../../_migration_report.md)_

