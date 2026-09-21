# D-04.2 — Pair analysis: GDPR ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ CRA

**GDPR article (verbatim):**
> Art. 33(3)(d) requires the controller's breach notification to the supervisory authority to describe the measures taken or proposed to be taken by the controller to address the personal data breach, including, where appropriate, measures to mitigate its possible adverse effects.

**CRA article (verbatim):**
> Annex I Part I (2)(h) requires products to protect the availability of essential and basic functions — also after an incident — including through resilience and mitigation measures against denial-of-service attacks. Annex I Part I (2)(i) requires products to minimise the negative impact by the products themselves or connected devices on the availability of services provided by other devices or networks. Annex I Part I (2)(k) requires reducing the impact of an incident using appropriate exploitation-mitigation mechanisms and techniques.

**Scope comparison:**
- GDPR scope: post-breach containment and mitigation by the controller.
- CRA scope: pre-event design resilience and post-incident availability preservation.
- Scope overlap: Conditional when a CRA product is the source of, or subject to, a personal-data breach.

**Trigger comparison:**
- GDPR trigger: personal-data breach occurrence.
- CRA trigger: continuous product design and post-incident impact limitation.
- Trigger alignment: DIFFERENT.

**Threshold/timeline comparison:**
- GDPR: where-appropriate mitigation measures.
- CRA: post-incident availability and cross-product impact limitation.
- Tension: NONE.

**Recipient comparison:**
- GDPR: supervisory authority.
- CRA: manufacturer documentation, product users and market surveillance.

**Content template comparison:**
- GDPR: containment and mitigation measures per Art. 33(3)(d).
- CRA: resilience and exploitation-mitigation architecture.

**Classified relationship (from CRDA):** DIFFERENT-PERSPECTIVE

**Verified relationship (after OJ-text analysis):** SAME — DIFFERENT-PERSPECTIVE

**Reasoning (1-2 paragraphs):** The OJ text supports the CRDA classification. GDPR containment is a post-event reaction; CRA availability architecture is pre-event design. The CRA product is designed to contain an incident internally and minimise cascading impact, reducing the probability that a GDPR-relevant breach occurs; if one does, the GDPR Art. 33(3)(d) runbook takes over.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect**; it should be "scope-disjoint" in baseline. This pair was not classified contradictory.

**Downstream implication (1-2 sentences):** Doc 07 should keep CRA resilience design and GDPR post-breach runbook as two separate artefacts, with the GDPR runbook identifying CRA control inputs.


## Summary (Domain Analysis)

<!-- pair: GDPR,CRA -->
| GDPR ↔ CRA | **different-perspective** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-015, Art. 33(3)(d)) | Post-breach containment via TOMs rendering data unintelligible |  |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-015 |
| **CRA** (SR-CRA-043 + SR-CRA-044, Annex I Part I (2)(h)/(i)/(k)) | Post-incident availability architecture + cross-product impact containment + exploitation mitigation |  |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-043, SR-CRA-044 |

**Why different-perspective**: GDPR containment is a post-event reaction (response phase); CRA availability architecture is pre-event design (prevention + resilience). The CRA product is designed to contain an incident internally and minimise cascading impact, reducing the probability that a GDPR-relevant breach occurs; if one does, the GDPR Art. 33(3)(d) runbook takes over.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_

