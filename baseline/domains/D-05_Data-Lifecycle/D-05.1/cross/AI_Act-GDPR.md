# D-05.1 — Pair analysis: GDPR ↔ AI Act

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ AI_Act

**GDPR article (verbatim, Art. 5(1)(c) + Art. 9(1)):**
> "Personal data shall be adequate, relevant and limited to what is necessary in relation to the purposes for which they are processed ('data minimisation')." — Art. 5(1)(c) GDPR
>
> "Processing of personal data revealing racial or ethnic origin, political opinions, religious or philosophical beliefs, or trade union membership, and the processing of genetic data, biometric data for the purpose of uniquely identifying a natural person, data concerning health or data concerning a natural person's sex life or sexual orientation shall be prohibited." — Art. 9(1) GDPR

**AI_Act article (verbatim, Art. 10(2)(f)/(g) + Art. 10(5)):**
> "Training, validation and testing data sets shall be relevant, representative and, to the best extent possible, free of errors and complete. They shall have the appropriate statistical properties, including where applicable, as regards the persons or groups of persons on which the high-risk AI system is intended to be used. These properties of the data sets can be met at the level of individual data sets or a combination thereof … The data sets shall take into account, to the extent required by their intended purpose, the characteristics or elements that are particular to the specific geographical, behavioural or functional setting within which the high-risk AI system is intended to be used." — AI Act Art. 10(3)
>
> "Where it is not possible to fully comply with paragraph 4 in order to detect and prevent biases in relation to the training, validation and testing datasets of high-risk AI systems referred to in points (a) and (b) of Article 6(2), the providers of such systems may exceptionally process special categories of personal data referred to in Article 9(1) of Regulation (EU) 2016/679 … insofar as the following conditions are fulfilled: (a) the bias detection and correction cannot be effectively achieved by processing other data; (b) the special categories of personal data are processed strictly necessary and limited to the bias detection and correction; (c) the providers have put in place effective technical and organisational safeguards to protect the data; (d) the datasets used for bias detection and correction are subject to enhanced data governance; (e) the safeguards are documented; (f) the special-category data are deleted after the bias detection and correction." — AI Act Art. 10(5)

**Scope comparison:**
- GDPR scope: any processing of special-category personal data is prohibited unless an Art. 9(2) basis applies.
- AI Act scope: training / validation / testing datasets of high-risk AI systems; processing of special-category data for bias detection / correction is *exceptionally* permitted when 6 conditions (a)–(f) are met.
- Scope overlap: **Y when training a high-risk AI system with bias-detection needs that cannot be met by other data.**

**Trigger comparison:**
- GDPR trigger: any processing of special-category personal data.
- AI Act trigger: bias detection and correction in training / validation / testing datasets of high-risk AI systems.
- Trigger alignment: **PARTIAL** — AI Act trigger is a *subset* of possible processing events (bias correction only); GDPR trigger is universal.

**Threshold/timeline comparison:**
- GDPR: no quantitative threshold; prohibition unless Art. 9(2) applies.
- AI Act: 6 cumulative conditions (a)–(f) must all be satisfied.
- Tension: **GENUINE but regulated by Art. 10(5)** — the AI Act creates a carve-out into GDPR's prohibition. The carve-out does not contradict the principle of minimisation but creates a specific, narrowly-conditioned permission to process special-category data for bias detection.

**Recipient comparison:**
- GDPR: data subject + supervisory authority (DPA).
- AI Act: provider + market surveillance authority (MSA) + national competent authorities for fundamental rights.

**Content template comparison:**
- GDPR: no codified template; controller documents Art. 9(2) basis and Art. 5(2) accountability.
- AI Act: providers must document the safeguards (condition (e)) and the bias-detection / correction process; data is deleted after the process (condition (f)).

**Classified relationship (from CRDA):** CONTRADICTORY (special-category scope)
**Verified relationship (after OJ-text analysis):** **CORRECTED — SCOPE-DISJOINT** (with regulatory carve-out)
**Reasoning:** The CRDA reasoning itself acknowledges: "This is a regulatory carve-out *into* the data minimisation architecture, not a contradiction of minimisation as a principle, but it expands the set of permissible processing." That admission is dispositive. The AI Act Art. 10(5) provision is a *permission* that GDPR does not provide, conditioned on 6 safeguards. It is not a contradiction of GDPR Art. 5(1)(c) — it is an exception that allows *one specific additional purpose* (bias correction) for *one specific data class* (high-risk AI training data) when *one specific technical condition* (no alternative data) is met. The CRDA label "contradictory" is scope-incorrect; the correct label is "scope-disjoint" with explicit recognition of the Art. 10(5) carve-out. Two regulators cannot impose mutually exclusive obligations on the same event when one creates a conditional exception to the other — that is the textbook exception-permission pattern, not the prohibition-vs-prohibition pattern that "contradictory" connotes.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y only for the narrow Art. 10(5) carve-out scenario: a high-risk AI provider training a system with bias-detection needs that cannot be met by non-special-category data.** Outside that narrow window, the AI Act does not trigger special-category processing, so the pair does not overlap. The pair is therefore scope-disjoint in baseline, with the carve-out as the single overlap point.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must codify AI Act Art. 10(5) as a **gateway clause** that *expands* the set of permissible special-category processing under GDPR Art. 9(1) when all 6 conditions are satisfied. The CRDA "contradictory" label should be corrected to "scope-disjoint" with carve-out annotation. Phase 3 case generation must surface the 6-condition matrix explicitly when the case company is a high-risk AI provider processing special-category data for bias correction.

---


## Summary (Domain Analysis)

<!-- pair: GDPR,AI_Act -->
| GDPR ↔ AI_Act | **contradictory** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-025, Art. 5(1)(c) + Art. 6(4)) | Purpose-bound data minimisation + Art. 6(4) compatibility |  |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-025 |
| **AI_Act** (SR-AIACT-004 + SR-AIACT-005 + SR-AIACT-006, Art. 10(1)–(5)) | Dataset quality criteria + 8-element data governance practice + exceptional special-category processing for bias correction |  |
|   → full rationale: `../../../Regulation/AI_Act/02_SecurityRules_NIST.md` SR-AIACT-004, SR-AIACT-005, SR-AIACT-006 |

**Why contradictory (special-category scope)**: GDPR Art. 9(1) prohibits special-category personal data processing absent one of Art. 9(2) bases; AI Act Art. 10(5) creates an *exception* to GDPR Art. 9(1) — providers of high-risk AI may exceptionally process special-category data for bias detection/correction, subject to 6 cumulative conditions. This is a regulatory carve-out *into* the data minimisation architecture, not a contradiction of minimisation as a principle, but it expands the set of permissible processing. Phase 2 must surface this exception explicitly and codify that the AI Act exception applies only when all 6 conditions (a)–(f) are simultaneously satisfied.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
45 lines — see ../../_migration_report.md)_

