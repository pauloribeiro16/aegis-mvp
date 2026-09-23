# D-04.1 — Pair analysis: GDPR ↔ NIS 2

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ NIS2

**GDPR article (verbatim):**
> Art. 32(1)(b) requires the ability to ensure ongoing confidentiality, integrity, availability and resilience of processing systems and services. Art. 33(1) creates the 72-hour clock from the moment of becoming aware; awareness requires detection capability. Art. 4(12) defines a personal data breach as a breach of security leading to the accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to personal data transmitted, stored or otherwise processed.

**NIS2 article (verbatim):**
> Article 21(2)(b) of Directive (EU) 2022/2555 requires essential and important entities to take measures regarding incident handling. Article 6(8) defines `incident handling` as all actions and procedures aiming at, where appropriate, preventing, detecting, analysing, containing and responding to and recovering from an incident (OJ L 333, 27.12.2022, p. 113) — a six-action process anchored in the Article 21(2) all-hazards approach.

**Scope comparison:**
- GDPR scope: detection of personal-data breaches enabling the 72-hour clock.
- NIS2 scope: entity-level all-hazards incident-handling detection.
- Scope overlap: Conditional where the controller is also a NIS2 entity and the breach affects NIS-scoped systems.

**Trigger comparison:**
- GDPR trigger: awareness of a personal-data breach.
- NIS2 trigger: awareness of a significant incident under Art. 23(3) test A or test B.
- Trigger alignment: DIFFERENT.

**Threshold/timeline comparison:**
- GDPR: 72-hour clock to the supervisory authority.
- NIS2: 24-hour early warning + 72-hour incident notification + 1-month final report.
- Tension: NONE.

**Recipient comparison:**
- GDPR: supervisory authority.
- NIS2: CSIRT or competent authority.

**Content template comparison:**
- GDPR: nature, contact, consequences, measures per Art. 33(3).
- NIS2: severity, impact, indicators of compromise, cross-border, suspected unlawful or malicious acts.

**Classified relationship (from CRDA):** COMPLEMENTARY

**Verified relationship (after OJ-text analysis):** SAME — COMPLEMENTARY

**Reasoning (1-2 paragraphs):** The OJ text supports complementarity. GDPR is breach-detection-anchored to the 72-hour clock; NIS2 is incident-handling-anchored to the six-action lifecycle. The same detection event can feed both pipelines, but the downstream notifications go to different recipients under different templates.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect**; it should be "scope-disjoint" in baseline. This pair was not classified contradictory.

**Downstream implication (1-2 sentences):** Doc 07 should design the detection pipeline to publish awareness events to both a GDPR-aware channel and a NIS-aware channel, with the supervisory and CSIRT routes in parallel.


## Summary (Domain Analysis)

<!-- pair: GDPR,NIS2 -->
| GDPR ↔ NIS2 | **complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-014, Art. 33(1) — `becoming aware`) | Continuous breach detection enabling the 72-hour clock |  |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-014 |
| **NIS2** (SR-NIS2-008 + SR-NIS2-009, Art. 21(2)(b) + Art. 21(2) chapeau) | Six-action incident-handling lifecycle + all-hazards monitoring to surface adverse events |  |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-008, SR-NIS2-009 |

**Why complementary**: GDPR anchors the "becoming aware" anchor for a specific subset of events (personal-data breach), while NIS2 provides the entity-wide detection architecture that produces the awareness signal. Without NIS2 detection, GDPR has nothing to anchor; without GDPR, NIS2 detection has no personal-data-specific temporal escalation rule.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_