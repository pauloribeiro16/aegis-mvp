# D-04.3 — Pair analysis: GDPR ↔ AI Act

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ AI_Act

**GDPR article (verbatim):**
> Art. 33(1) requires the controller, in the case of a personal data breach, to notify the personal data breach to the supervisory authority competent in accordance with Art. 55 without undue delay and, where feasible, not later than 72 hours after having become aware of it, unless the personal data breach is unlikely to result in a risk to the rights and freedoms of natural persons.

**AI_Act article (verbatim):**
> Art. 73(1)–(4) of Regulation (EU) 2024/1689 requires providers of high-risk AI systems, and deployers where applicable, to report any serious incident to the market surveillance authorities of the Member States where the incident occurred. The reporting timeline depends on the severity: 15 days after the provider becomes aware (default), 10 days if the incident results in death, 2 days for widespread infringement.

**Scope comparison:**
- GDPR scope: personal-data breach at the controller.
- AI Act scope: serious incident involving a high-risk AI system, plus GPAI serious-incident duties for systemic-risk GPAI providers.
- Scope overlap: Conditional, when the same party is controller/provider/deployer and the AI incident is also a personal-data breach.

**Trigger comparison:**
- GDPR trigger: awareness of a personal-data breach.
- AI Act trigger: serious incident under Art. 73, with severity-dependent timelines.
- Trigger alignment: PARTIAL.

**Threshold/timeline comparison:**
- GDPR: 72 hours, where feasible.
- AI Act: 15 days default, 10 days for death, 2 days for widespread infringement.
- Tension: GENUINE if the same AI incident is also a personal-data breach; NONE if the AI incident has no personal-data breach or the roles are split.

**Recipient comparison:**
- GDPR: supervisory authority.
- AI Act: market surveillance authorities; AI Office for GPAI serious incidents.

**Content template comparison:**
- GDPR: personal-data-breach facts, consequences and measures.
- AI Act: serious-incident facts, severity category, causal/awareness trigger and corrective measures.

**Classified relationship (from CRDA):** CONTRADICTORY

**Verified relationship (after OJ-text analysis):** CORRECTED — SCOPE-DISJOINT baseline / CONTRADICTORY on confirmed same-party overlap

**Reasoning (1-2 paragraphs):** The source text corrects an important AI Act timing issue: Art. 73 has three numerical timelines, not a separate immediate-reporting clock for reasonable-likelihood attribution. Against GDPR, the timeline tension remains real when one high-risk AI serious incident is also a personal-data breach.

But the scopes are not automatically coextensive. A high-risk AI serious incident may not involve personal data; a personal-data breach may not involve high-risk AI. The CRDA X should therefore be treated as conditional, not as a baseline contradiction.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect** as a baseline; it should be conditional.

**Downstream implication (1-2 sentences):** Doc 07 should route high-risk-AI incidents through an AI Act decision tree first, then add the GDPR branch only if personal data and controller awareness are present.


## Summary (Domain Analysis)

<!-- pair: GDPR,AI_Act -->
| GDPR ↔ AI_Act | **contradictory** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-016, Art. 33(1)) | 72h SA notification |  |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-016 |
| **AI_Act** (SR-AIACT-022, Art. 73(1)–(4)) | 15d awareness-driven + 10d death-trigger + 2d widespread-infringement trigger |  |
|   → full rationale: `../../../Regulation/AI_Act/02_SecurityRules_NIST.md` SR-AIACT-022 |

**Why contradictory (timeline)**: GDPR's 72h is the tightest deadline in the matrix; AI Act's 15d default is far longer. When a high-risk AI incident is also a personal-data breach, GDPR's 72h binds. The AI Act's 2d widespread-infringement trigger is tighter than 72h only if the operator cannot assemble the Art. 73(4) notification within 72h — practically, GDPR's 72h is operationally operative.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
44 lines — see ../../_migration_report.md)_

