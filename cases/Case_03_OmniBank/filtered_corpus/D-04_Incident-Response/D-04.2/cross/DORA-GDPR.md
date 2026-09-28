# D-04.2 — Pair analysis: GDPR ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ DORA

**GDPR article (verbatim):**
> Art. 33(3)(d) requires the controller's breach notification to the supervisory authority to describe the measures taken or proposed to be taken by the controller to address the personal data breach, including, where appropriate, measures to mitigate its possible adverse effects.

**DORA article (verbatim):**
> Art. 11(1) requires financial entities to put in place a comprehensive ICT business continuity policy, which may be adopted as a dedicated specific policy forming an integral part of the overall business continuity policy of the financial entity. Art. 11(2) requires financial entities to implement the ICT business continuity policy through dedicated, appropriate and documented arrangements, plans, procedures and mechanisms aiming to (a) ensure the continuity of the financial entity's critical or important functions; (b) quickly, appropriately and effectively respond to, and resolve, all ICT-related incidents; (c) activate, without delay, dedicated plans that enable containment measures, processes and technologies suited to each type of ICT-related incident; (d) estimate preliminary impacts, damages and losses; (e) set out communication and crisis management actions that ensure that updated information is transmitted to all relevant internal staff and external stakeholders in accordance with Article 14, and report to the competent authorities in accordance with Article 19.

**Scope comparison:**
- GDPR scope: post-breach containment, mitigation and remediation by the controller.
- DORA scope: BC arrangements covering critical functions, response plans, containment plans, impact estimation, crisis communication.
- Scope overlap: Conditional where a DORA financial entity also processes personal data.

**Trigger comparison:**
- GDPR trigger: personal-data breach.
- DORA trigger: ICT-related incident under Art. 17(1).
- Trigger alignment: DIFFERENT.

**Threshold/timeline comparison:**
- GDPR: where-appropriate mitigation measures.
- DORA: dedicated plans activated without delay under Art. 11(2)(c).
- Tension: NONE.

**Recipient comparison:**
- GDPR: supervisory authority.
- DORA: competent authority and clients per Art. 19.

**Content template comparison:**
- GDPR: Art. 33(3)(d) measures.
- DORA: BC arrangements, plans, procedures and mechanisms per Art. 11(2) chapeau + (a)–(e).

**Classified relationship (from CRDA):** COMPLEMENTARY

**Verified relationship (after OJ-text analysis):** SAME — COMPLEMENTARY

**Reasoning (1-2 paragraphs):** The OJ text supports complementarity. DORA mandates the response/recovery-plan architecture; GDPR mandates the breach-specific content. DORA provides the planning infrastructure, GDPR provides the personal-data-specific content that the plans must operationalise.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect**; it should be "scope-disjoint" in baseline. This pair was not classified contradictory.

**Downstream implication (1-2 sentences):** Doc 07 should record GDPR personal-data-specific containment content as a section within the DORA BC arrangements, rather than as a separate plan.


## Summary (Domain Analysis)

<!-- pair: GDPR,DORA -->
| GDPR ↔ DORA | **complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-015, Art. 33(3)(d)) | Post-breach containment via TOMs |  |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-015 |
| **DORA** (SR-DORA-013 + SR-DORA-014 + SR-DORA-016, Art. 11(1)–(3) + Art. 17(1)) | BC policy + dedicated arrangements (response/recovery plans subject to independent internal audit for non-microenterprises) |  |
|   → full rationale: `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-013, SR-DORA-014, SR-DORA-016 |

**Why complementary**: DORA mandates the response/recovery-plan architecture (BC framework, arrangements, independent audit); GDPR mandates the breach-specific content (render data unintelligible). DORA provides the planning infrastructure, GDPR provides the personal-data-specific content that the plans must operationalise.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_