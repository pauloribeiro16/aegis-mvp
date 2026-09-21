# D-04.4 — Pair analysis: GDPR ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ CRA

**GDPR article (verbatim):**
> Art. 32(1)(c) requires, among the security measures the controller and processor must implement, the ability to restore the availability and access to personal data in a timely manner in the event of a physical or technical incident.

**CRA article (verbatim):**
> Annex I Part I (2)(h) requires products to protect the availability of essential and basic functions — also after an incident — including through resilience and mitigation measures against denial-of-service attacks.

**Scope comparison:**
- GDPR scope: restoration of personal-data availability and access by controller/processor.
- CRA scope: product-level availability of essential and basic functions after an incident.
- Scope overlap: Conditional when a CRA product processes or stores personal data for the controller.

**Trigger comparison:**
- GDPR trigger: physical or technical incident affecting personal data.
- CRA trigger: continuous product design duty to preserve availability after incident.
- Trigger alignment: DIFFERENT.

**Threshold/timeline comparison:**
- GDPR: timely restoration.
- CRA: post-incident availability and resilience/mitigation measures.
- Tension: NONE.

**Recipient comparison:**
- GDPR: supervisory accountability and data-subject service impact.
- CRA: product users and market-surveillance evidence.

**Content template comparison:**
- GDPR: restore capability, tested backups and recovery records.
- CRA: resilience architecture and availability-preservation evidence.

**Classified relationship (from CRDA):** DIFFERENT-PERSPECTIVE

**Verified relationship (after OJ-text analysis):** SAME — DIFFERENT-PERSPECTIVE

**Reasoning (1-2 paragraphs):** GDPR is post-event and data-centric; CRA is design-time and product-centric. A CRA product can help satisfy the controller's GDPR restoration outcome, but CRA does not replace the controller's duty to restore access to personal data.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: any contradiction claim would be scope-incorrect; CRDA did not classify this pair as contradictory.

**Downstream implication (1-2 sentences):** Doc 07 should treat CRA product resilience as a control input to the GDPR recovery plan, not as the GDPR recovery plan itself.


## Summary (Domain Analysis)

<!-- pair: GDPR,CRA -->
| GDPR ↔ CRA | **different-perspective** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-024, Art. 32(1)(c)) | Timely availability restoration |  |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-024 |
| **CRA** (SR-CRA-043, Annex I Part I (2)(h)) | Product availability preserved post-incident via resilience + DoS-resistance |  |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-043 |

**Why different-perspective**: GDPR restoration is post-event (controller restores availability); CRA availability is pre-event design (product is built to maintain essential functions during/after attack). CRA's resilience design reduces the probability that GDPR's restoration trigger fires.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_

