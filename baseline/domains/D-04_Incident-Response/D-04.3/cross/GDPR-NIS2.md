# D-04.3 — Pair analysis: GDPR ↔ NIS 2

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ NIS2

**GDPR article (verbatim):**
> Art. 33(1) requires the controller, in the case of a personal data breach, to notify the personal data breach to the supervisory authority competent in accordance with Art. 55 without undue delay and, where feasible, not later than 72 hours after having become aware of it, unless the personal data breach is unlikely to result in a risk to the rights and freedoms of natural persons.

**NIS2 article (verbatim):**
> Article 23(4)(a) of Directive (EU) 2022/2555 requires the entity, upon becoming aware of a significant incident, to submit to the CSIRT or, where applicable, the competent authority, without undue delay and in any event within 24 hours of becoming aware of the significant incident, an early warning which, where applicable, shall indicate whether the significant incident is suspected of being caused by unlawful or malicious acts or could have a cross-border impact (OJ L 333, 27.12.2022, p. 129).

**Scope comparison:**
- GDPR scope: personal-data breaches by controllers.
- NIS2 scope: significant incidents affecting essential or important entities.
- Scope overlap: Conditional, when the same controller is also a NIS2 entity and the same incident is both a personal-data breach and a significant incident.

**Trigger comparison:**
- GDPR trigger: controller awareness of a personal-data breach, unless unlikely to result in risk.
- NIS2 trigger: entity awareness of a significant incident under Art. 23(3).
- Trigger alignment: PARTIAL.

**Threshold/timeline comparison:**
- GDPR: without undue delay and, where feasible, not later than 72 hours.
- NIS2: without undue delay and in any event within 24 hours for early warning, then 72 hours for incident notification.
- Tension: GENUINE if the same event triggers both; NONE if the events or actors are disjoint.

**Recipient comparison:**
- GDPR: competent supervisory authority.
- NIS2: CSIRT or competent authority.

**Content template comparison:**
- GDPR: nature of breach, contact point, likely consequences, measures taken or proposed.
- NIS2: suspected unlawful or malicious acts, cross-border impact, severity, impact and indicators of compromise at the 72-hour tier.

**Classified relationship (from CRDA):** CONTRADICTORY

**Verified relationship (after OJ-text analysis):** CORRECTED — SCOPE-DISJOINT baseline / CONTRADICTORY on confirmed same-party overlap

**Reasoning (1-2 paragraphs):** The OJ-derived text supports a genuine timeline tension only in the overlap case. GDPR and NIS2 do not regulate the same event by default: GDPR follows the personal-data-breach trigger, while NIS2 follows the significant-incident trigger. A personal-data breach at a non-NIS2 controller does not trigger NIS2, and a significant incident without personal data does not trigger GDPR.

When the same entity is both controller and NIS2 entity, and one incident satisfies both trigger tests, the NIS2 24-hour early warning creates an earlier regulatory clock than GDPR's 72-hour supervisory-authority clock. That is an operational conflict/tension, not an inherent contradiction in all cases. The unconditional CRDA X overstates baseline overlap.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect** as a baseline; it should be scope-disjoint unless the overlap facts are established.

**Downstream implication (1-2 sentences):** Phase 1C Doc 07 should add a trigger gate: classify the event first as personal-data breach, significant incident, or both; only the "both" branch should activate the 24h/72h dual-routing playbook.


## Summary (Domain Analysis)

<!-- pair: GDPR,NIS2 -->
| GDPR ↔ NIS2 | **contradictory** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-016, Art. 33(1)) | 72-hour breach notification to the supervisory authority — `where feasible` qualifier |  |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-016 |
| **NIS2** (SR-NIS2-010 + SR-NIS2-011, Art. 23(4)(a)/(b)) | 24h early warning + 72h incident notification — no `where feasible` qualifier |  |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-010, SR-NIS2-011 |

**Why contradictory (mild)**: The 72h SA notification under GDPR has the `where feasible` softening (Art. 33(1) `where feasible, no later than 72 hours`), which is absent from NIS2's 72h tier (Art. 23(4)(b) `in any event within 72 hours`). When the same event triggers both, the controller must satisfy the stricter NIS2 anchor (no `where feasible` escape) for the notification core. The downstream Phase 2 derivation must flag that NIS2's 72h is the operative binding deadline.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
44 lines — see ../../_migration_report.md)_

