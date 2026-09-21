# D-04.1 — Pair analysis: GDPR ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ CRA

**GDPR article (verbatim):**
> Art. 32(1)(b) requires the ability to ensure ongoing confidentiality, integrity, availability and resilience of processing systems and services. Art. 4(12) defines a personal data breach. Art. 33(1) anchors the 72-hour clock to the moment of becoming aware.

**CRA article (verbatim):**
> Annex I Part I (2)(l) requires products with digital elements to provide security-related information by recording and monitoring relevant internal activity — including the access to or modification of data, services, or functions — with an opt-out mechanism for the user.

**Scope comparison:**
- GDPR scope: controller detection of personal-data breaches.
- CRA scope: product-internal activity recording and monitoring.
- Scope overlap: Conditional where a CRA product processes personal data.

**Trigger comparison:**
- GDPR trigger: awareness of a personal-data breach.
- CRA trigger: continuous product monitoring and corruption reporting.
- Trigger alignment: DIFFERENT.

**Threshold/timeline comparison:**
- GDPR: 72-hour clock.
- CRA: continuous product monitoring.
- Tension: NONE.

**Recipient comparison:**
- GDPR: supervisory authority.
- CRA: manufacturer, product users and market surveillance.

**Content template comparison:**
- GDPR: breach notification content per Art. 33(3).
- CRA: corruption and unauthorised-modification reporting.

**Classified relationship (from CRDA):** DIFFERENT-PERSPECTIVE

**Verified relationship (after OJ-text analysis):** SAME — DIFFERENT-PERSPECTIVE

**Reasoning (1-2 paragraphs):** The OJ text supports the CRDA classification. GDPR detection operates at the data-flow boundary; CRA detection operates inside the product. They are layered, not overlapping: a CRA product deployed in a GDPR controller's environment contributes its product-internal detection to the entity-level GDPR detection, but neither replaces the other.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect**; it should be "scope-disjoint" in baseline. This pair was not classified contradictory.

**Downstream implication (1-2 sentences):** Doc 07 should treat CRA product monitoring as one detection source feeding the GDPR detection pipeline, not as a substitute for entity-level detection.


## Summary (Domain Analysis)

| GDPR ↔ CRA | **different-perspective** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-014, Art. 33(1)) | Continuous breach detection enabling the 72-hour clock |  |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-014 |
| **CRA** (SR-CRA-027 + SR-CRA-100, Annex I Part I (2)(l)) | On-device activity monitoring with user opt-out — product-internal visibility only |  |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-027, SR-CRA-100 |

**Why different-perspective**: GDPR detection operates at the controller/processor entity boundary (data flows in/out); CRA detection operates inside the product (intra-product state changes). They are layered, not overlapping: a CRA product deployed in a GDPR controller's environment contributes its product-internal detection to the entity-level GDPR detection, but neither replaces the other.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_

