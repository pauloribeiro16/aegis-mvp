# D-04.3 — Pair analysis: GDPR ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ CRA

**GDPR article (verbatim):**
> Art. 33(1) requires the controller, in the case of a personal data breach, to notify the personal data breach to the supervisory authority competent in accordance with Art. 55 without undue delay and, where feasible, not later than 72 hours after having become aware of it, unless the personal data breach is unlikely to result in a risk to the rights and freedoms of natural persons.

**CRA article (verbatim):**
> Art. 14(2)(a) requires the manufacturer to submit an early warning notification of an actively exploited vulnerability, without undue delay and in any event within 24 hours of the manufacturer becoming aware of it, indicating — where applicable — the Member States on the territory of which the manufacturer is aware that the product has been made available.

**Scope comparison:**
- GDPR scope: controller-side personal-data-breach reporting.
- CRA scope: manufacturer-side reporting for actively exploited vulnerabilities or severe incidents in products with digital elements.
- Scope overlap: Conditional, when the manufacturer is also the controller or the same product event creates a controller-side personal-data breach.

**Trigger comparison:**
- GDPR trigger: awareness of a personal-data breach.
- CRA trigger: manufacturer awareness of an actively exploited vulnerability or severe incident.
- Trigger alignment: PARTIAL.

**Threshold/timeline comparison:**
- GDPR: 72-hour supervisory-authority notification, with the where-feasible qualifier.
- CRA: 24-hour early warning, 72-hour notification, and 14-day AEV final report or 1-month severe-incident final report.
- Tension: NONE in the common actor-split case; GENUINE only if the same party owns both controller and manufacturer duties.

**Recipient comparison:**
- GDPR: supervisory authority.
- CRA: CSIRT designated as coordinator and ENISA through the single reporting platform.

**Content template comparison:**
- GDPR: breach nature, contact, consequences and measures.
- CRA: product, exploit/vulnerability or severe-incident facts, territorial scope, corrective or mitigating measures and user actions.

**Classified relationship (from CRDA):** COMPLEMENTARY

**Verified relationship (after OJ-text analysis):** SAME — COMPLEMENTARY, with explicit scope-disjoint baseline note

**Reasoning (1-2 paragraphs):** The CRDA complementarity is defensible. GDPR and CRA have different actors, recipients and event objects. GDPR is controller/data-subject-facing; CRA is manufacturer/product-facing. The OJ text does not create a prohibition conflict.

The P0 concern is still relevant: many GDPR-CRA cases are actor-disjoint. A service controller using a CRA-regulated product is not automatically the CRA manufacturer. In that baseline, both obligations may relate to one incident chain but do not land on the same party.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: any contradictory reading would be scope-incorrect; CRDA did not classify this pair as contradictory.

**Downstream implication (1-2 sentences):** Doc 07 should keep GDPR and CRA as parallel routes with a hand-off field identifying whether the same legal entity is both controller and manufacturer.


## Summary (Domain Analysis)

<!-- pair: GDPR,CRA -->
| GDPR ↔ CRA | **complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-016, Art. 33(1)) | 72h SA notification |  |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-016 |
| **CRA** (SR-CRA-029 + SR-CRA-030, Art. 14(2)(a)/(b)/(c)) | AEV: 24h early warning + 72h vulnerability notification + 14d final report |  |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-029, SR-CRA-030 |

**Why complementary (with timeline overlap)**: CRA's 72h AEV notification maps cleanly onto the NIS2 72h tier (both anchored at 72h). The GDPR 72h SA notification has the same 72h anchor but different recipient (DPA vs CSIRT) and different scope (personal-data breach vs AEV). When the same event is both an AEV and a personal-data breach, the manufacturer must notify both CSIRT+ENISA (CRA) and the DPA (GDPR) in parallel.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
44 lines — see ../../_migration_report.md)_

