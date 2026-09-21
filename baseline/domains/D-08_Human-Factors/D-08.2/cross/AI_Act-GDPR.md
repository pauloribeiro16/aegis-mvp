# D-08.2 — Pair analysis: GDPR ↔ AI Act

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ AI_Act

**GDPR article (verbatim, Art. 39(1)(b)):**
> [as quoted above]

**AI_Act article (verbatim, Art. 14(4)(a)–(e) + Art. 26(2)):**
> "Natural persons to whom human oversight is assigned shall be enabled, as appropriate and proportionate, to: (a) properly understand the relevant capacities and limitations of the high-risk AI system and foreseeable misuse; (b) remain aware of automation bias; (c) correctly interpret the output; (d) decide not to use the high-risk AI system or to disregard, override or reverse its output; (e) intervene on the operation or interrupt the system through a stop button or similar procedure." — Art. 14(4)(a)–(e) AI Act (per SR-AIACT-013)
> "Deployers shall assign human oversight to natural persons who have the necessary competence, training and authority, as well as the necessary support." — Art. 26(2) AI Act (per SR-AIACT-020)

**Scope comparison:**
- GDPR scope: DPO-driven role-specific training for staff involved in processing.
- AI Act scope: human overseer assignment with competence + training + authority + support (provider-side Art. 14(4), deployer-side Art. 26(2)).
- Scope overlap: **Y (when the deployer-controller assigns human oversight for high-risk AI processing personal data).**

**Trigger comparison:**
- GDPR trigger: DPO-catalysed role-specific training.
- AI Act trigger: provider design (Art. 14) + deployer assignment (Art. 26).
- Trigger alignment: **DIFFERENT** (DPO-driven data-protection vs. AI-overseer competence).

**Threshold/timeline comparison:**
- GDPR: no quantitative cadence.
- AI Act: `as appropriate and proportionate` (qualitative) — 5 cumulative abilities must be enabled (Art. 14(4)).
- Tension: **NONE**.

**Recipient comparison:**
- GDPR: data subject, DPA.
- AI Act: deployer, provider, MSA.

**Content template comparison:**
- GDPR: DPO-discretionary curriculum.
- AI Act: 5-element cumulative abilities + `competence, training, authority, support` (Art. 26(2)).

**Classified relationship (from CRDA):** DIFFERENT-PERSPECTIVE
**Verified relationship (after OJ-text analysis):** **SAME — DIFFERENT-PERSPECTIVE**
**Reasoning:** GDPR role-specific targets processing staff with data-subject-facing responsibilities; AI Act targets human overseers of high-risk AI systems with the 5-element competence set. Different role, different content. The two can co-exist for a deployer that processes personal data via high-risk AI.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Conditional (Y when the same natural person is both a data-processing staff member and an AI human overseer)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce a layered stack: GDPR Art. 39(1)(b) processing-staff role-specific + AI Act Art. 14(4) + Art. 26(2) human-overseer competence. Where the same person holds both roles, the AI Act layer is the additional competence dimension.

---


## Summary (Domain Analysis)

| GDPR ↔ AI_Act | **different-perspective** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-042, Art. 39(1)(b)) | DPO-driven role-specific training for processing staff. | |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-042 |
| **AI_Act** (SR-AIACT-013, Art. 14(4) 5-element oversight abilities; SR-AIACT-020, Art. 26(2) deployer assignment) | Human overseers must have competence, training, authority, support to (a) understand, (b) remain aware of automation bias, (c) interpret, (d) decide, (e) intervene. | |
|   → full rationale: `../../../Regulation/AI_Act/02_SecurityRules_NIST.md` SR-AIACT-013 / SR-AIACT-020 |

**Why different-perspective**: GDPR role-specific targets processing staff with data-subject-facing responsibilities; AI Act targets human overseers of high-risk AI systems with the 5-element competence set. Different role, different content. The two can co-exist for a deployer that processes personal data via high-risk AI.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_

