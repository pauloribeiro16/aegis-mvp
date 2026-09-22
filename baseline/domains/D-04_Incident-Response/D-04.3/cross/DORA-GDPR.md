# D-04.3 — Pair analysis: GDPR ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ DORA

**GDPR article (verbatim):**
> Art. 33(1) requires the controller, in the case of a personal data breach, to notify the personal data breach to the supervisory authority competent in accordance with Art. 55 without undue delay and, where feasible, not later than 72 hours after having become aware of it, unless the personal data breach is unlikely to result in a risk to the rights and freedoms of natural persons.

**DORA article (verbatim):**
> Art. 19(1) imposes on financial entities a hard duty to notify the relevant competent authority of any major ICT-related incident, operating in parallel with — and not substituting for — the GDPR Art. 72-hour personal data breach notification under Regulation (EU) 2016/679 Art. 33 and the NIS 2 incident-notification workflow under Directive (EU) 2022/2555 Art. 23, both of which must be triggered under their own criteria where applicable.
> [OJ-corrective note (v0.2 audit, material): Art. 19(3) — trigger condition dropped. OJ Art. 19(3) conditions client notification: `Where a major ICT-related incident occurs AND HAS AN IMPACT ON THE FINANCIAL INTERESTS OF CLIENTS, financial entities shall, without undue delay as soon as they become aware of it, inform their clients about the major ICT-related incident and about the measures that have been taken to mitigate the adverse effects of such incident.` The SR drops the trigger condition `and has an impact on the financial interests of clients` — converting a conditional obligation into an unconditional one. Every major incident would trigger client notification under the SR; OJ scopes to those with client-financial-impact.]

**Scope comparison:**
- GDPR scope: personal-data breach at a controller.
- DORA scope: major ICT-related incident at a financial entity, with client notification only where financial interests of clients are affected.
- Scope overlap: Conditional, when the financial entity is also the controller and the same incident is both a personal-data breach and a major ICT-related incident.

**Trigger comparison:**
- GDPR trigger: becoming aware of a personal-data breach.
- DORA trigger: classification as major ICT-related incident; client communication adds client-financial-interest impact.
- Trigger alignment: PARTIAL.

**Threshold/timeline comparison:**
- GDPR: 72 hours, where feasible, from awareness.
- DORA: without undue delay for major ICT-related incident reporting and client communication where the client-financial-impact condition is met.
- Tension: GENUINE if one incident triggers both; NONE if no financial-entity/personal-data overlap exists.

**Recipient comparison:**
- GDPR: supervisory authority.
- DORA: relevant competent authority; clients when Art. 19(3) conditions are met.

**Content template comparison:**
- GDPR: Art. 33(3) four-element breach content.
- DORA: major-incident reporting template and client mitigation information.

**Classified relationship (from CRDA):** CONTRADICTORY

**Verified relationship (after OJ-text analysis):** CORRECTED — CONDITIONAL-CONTRADICTORY, not unconditional contradiction

**Reasoning (1-2 paragraphs):** The OJ text supports genuine tension only in a financial-entity personal-data-breach scenario. GDPR and DORA recipients, scopes and trigger tests differ. DORA also contains a corrective caveat in the source file: client notification is conditional on impact on clients' financial interests, so treating all major incidents as client-notifiable would overstate DORA scope.

Where one event is both a personal-data breach and a major ICT-related incident at a financial entity, the entity must route to both authorities. The tension is not that one law forbids the other; it is that the timing and content templates diverge. The CRDA X is therefore too broad unless made conditional on same-party overlap.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect** as a baseline; it should be conditional.

**Downstream implication (1-2 sentences):** Doc 07 should include a financial-entity branch that treats GDPR 72h and DORA without-undue-delay as parallel recipient-specific clocks, with the DORA client-notification condition preserved.


## Summary (Domain Analysis)

<!-- pair: GDPR,DORA -->
| GDPR ↔ DORA | **contradictory** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-016, Art. 33(1)) | 72h SA notification |  |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-016 |
| **DORA** (SR-DORA-017, Art. 19(1) + Art. 19(3)) | `without undue delay` supervisor notification + `without undue delay as soon as aware` client notification |  |
|   → full rationale: `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-017 |

**Why contradictory (temporal)**: GDPR specifies a hard 72h anchor for SA notification; DORA specifies only `without undue delay as soon as the financial entity becomes aware`. When a personal-data breach within a financial entity triggers both, the GDPR 72h is binding, and DORA's `without undue delay` must be operationalised to satisfy the GDPR deadline. Phase 2 must set the DORA anchor at the stricter GDPR 72h via the binding-procedure principle.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
45 lines — see ../../_migration_report.md)_