# D-04.2 — Pair analysis: GDPR ↔ NIS 2

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ NIS2

**GDPR article (verbatim):**
> Art. 33(3)(d) requires the controller's breach notification to the supervisory authority to describe the measures taken or proposed to be taken by the controller to address the personal data breach, including, where appropriate, measures to mitigate its possible adverse effects. Art. 34(3)(a) and (b) provide that subsequent measures rendering the personal data unintelligible or eliminating the high risk are valid exceptions to the data-subject notification under Art. 34(1).

**NIS2 article (verbatim):**
> Article 21(2)(b) of Directive (EU) 2022/2555 requires essential and important entities to take measures regarding incident handling. Article 6(8) defines `incident handling` as all actions and procedures aiming at, where appropriate, preventing, detecting, analysing, containing and responding to and recovering from an incident (OJ L 333, 27.12.2022, p. 113) — a six-action process including `containing` as one of the six actions.

**Scope comparison:**
- GDPR scope: personal-data-breach-specific containment, mitigation and remediation runbooks.
- NIS2 scope: entity-level incident-handling `contain` phase.
- Scope overlap: Conditional where the controller is also a NIS2 entity and the breach affects NIS-scoped systems.

**Trigger comparison:**
- GDPR trigger: personal-data breach occurrence.
- NIS2 trigger: significant incident under Art. 23(3) test A or test B.
- Trigger alignment: DIFFERENT.

**Threshold/timeline comparison:**
- GDPR: where-appropriate measures and unintelligibility carve-out under Art. 34(3)(a)/(b).
- NIS2: lifecycle-phase content; no specific deadline for `contain` step.
- Tension: NONE.

**Recipient comparison:**
- GDPR: data subjects (where Art. 34 applies) and supervisory authority.
- NIS2: CSIRT or competent authority.

**Content template comparison:**
- GDPR: containment and mitigation measures per Art. 33(3)(d).
- NIS2: containment action records in the incident-handling plan.

**Classified relationship (from CRDA):** COMPLEMENTARY

**Verified relationship (after OJ-text analysis):** SAME — COMPLEMENTARY

**Reasoning (1-2 paragraphs):** The OJ text supports complementarity. GDPR containment is breach-specific; NIS2 containment is the entity-wide lifecycle phase. A NIS2-compliant response plan provides the procedural framework that the GDPR Art. 33(3)(d) measures operationalise for the personal-data subset.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect**; it should be "scope-disjoint" in baseline. This pair was not classified contradictory.

**Downstream implication (1-2 sentences):** Doc 07 should use the NIS2 incident-handling plan as the procedural wrapper, with GDPR-specific measures documented inside the plan.


## Summary (Domain Analysis)

<!-- pair: GDPR,NIS2 -->
| GDPR ↔ NIS2 | **complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-015, Art. 33(3)(d) + Art. 34(3)(a)/(b)) | Post-breach containment, mitigation, and remediation runbooks — including cryptographic unintelligibility carve-out |  |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-015 |
| **NIS2** (SR-NIS2-008, Art. 21(2)(b) + Art. 6(8) — `contain`) | Six-action incident-handling lifecycle covers containment as a defined lifecycle phase |  |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-008 |

**Why complementary**: GDPR containment is breach-specific (personal data, render unintelligible); NIS2 containment is the entity-wide lifecycle phase. A NIS2-compliant response plan provides the procedural framework that the GDPR Art. 33(3)(d) measures operationalise for the personal-data subset.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_

