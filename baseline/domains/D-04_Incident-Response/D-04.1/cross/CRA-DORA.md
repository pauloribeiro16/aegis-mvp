# D-04.1 — Pair analysis: CRA ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: CRA ↔ DORA

**CRA article (verbatim):**
> Annex I Part I (2)(l) requires products with digital elements to provide security-related information by recording and monitoring relevant internal activity — including the access to or modification of data, services, or functions — with an opt-out mechanism for the user.

**DORA article (verbatim):**
> Art. 10(1) requires financial entities to have in place mechanisms to promptly detect anomalous activities, in accordance with Art. 17, including ICT network performance issues and ICT-related incidents, and to identify potential material single points of failure.

**Scope comparison:**
- CRA scope: product-internal activity recording and monitoring.
- DORA scope: financial-entity ICT-detection of anomalous activities, performance issues, SPOFs.
- Scope overlap: Conditional where a DORA financial entity deploys CRA products.

**Trigger comparison:**
- CRA trigger: continuous product-internal activity monitoring.
- DORA trigger: detection of anomalous ICT activities meeting DORA thresholds.
- Trigger alignment: DIFFERENT.

**Threshold/timeline comparison:**
- CRA: continuous product monitoring.
- DORA: without undue delay, with classification thresholds.
- Tension: NONE.

**Recipient comparison:**
- CRA: manufacturer, product users and market surveillance.
- DORA: financial-entity governance and competent authority.

**Content template comparison:**
- CRA: product-internal event records and corruption reporting.
- DORA: classification-driven notification content.

**Classified relationship (from CRDA):** DIFFERENT-PERSPECTIVE

**Verified relationship (after OJ-text analysis):** SAME — DIFFERENT-PERSPECTIVE

**Reasoning (1-2 paragraphs):** The OJ text supports the CRDA classification. CRA detection is inside the product; DORA detection is at the entity infrastructure level. Both are needed; CRA does not substitute for DORA SPOF identification, and DORA does not substitute for CRA product-internal state-change visibility.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect**; it should be "scope-disjoint" in baseline. This pair was not classified contradictory.

**Downstream implication (1-2 sentences):** Doc 07 should treat CRA product monitoring and DORA entity detection as two layers of the same detection posture, not as alternatives.


## Summary (Domain Analysis)

| CRA ↔ DORA | **different-perspective** | Tension/difference |
|---|---|---|
| **CRA** (SR-CRA-027, Annex I Part I (2)(l)) | On-device activity monitoring with user opt-out |  |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-027 |
| **DORA** (SR-DORA-011 + SR-DORA-012, Art. 10(1)–(2)) | Multi-class anomalous-activity detection at entity level |  |
|   → full rationale: `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-011, SR-DORA-012 |

**Why different-perspective**: CRA detection is inside the product boundary (the financial entity consumes detection signals as a deployer); DORA detection is at the financial-entity infrastructure level. Both are needed; CRA does not substitute for DORA's SPOF identification, and DORA does not substitute for CRA's product-internal state-change visibility.



## Deep analysis — Part 3 rendering (differs from Part 1 §1)

##### Pair: CRA ↔ DORA

**CRA article (verbatim):**
> Annex I Part I (2)(l) requires products with digital elements to provide security-related information by recording and monitoring relevant internal activity — including the access to or modification of data, services, or functions — with an opt-out mechanism for the user.

**DORA article (verbatim):**
> Art. 10(1) requires financial entities to have in place mechanisms to promptly detect anomalous activities, in accordance with Art. 17, including ICT network performance issues and ICT-related incidents, and to identify potential material single points of failure.

**Scope comparison:**
- CRA scope: product-internal activity recording and monitoring.
- DORA scope: financial-entity ICT-detection of anomalous activities, performance issues, SPOFs.
- Scope overlap: Conditional where a DORA financial entity deploys CRA products.

**Trigger comparison:**
- CRA trigger: continuous product-internal activity monitoring.
- DORA trigger: detection of anomalous ICT activities meeting DORA thresholds.
- Trigger alignment: DIFFERENT.

**Threshold/timeline comparison:**
- CRA: continuous product monitoring.
- DORA: without undue delay, with classification thresholds.
- Tension: NONE.

**Recipient comparison:**
- CRA: manufacturer, product users and market surveillance.
- DORA: financial-entity governance and competent authority.

**Content template comparison:**
- CRA: product-internal event records and corruption reporting.
- DORA: classification-driven notification content.

**Classified relationship (from CRDA):** DIFFERENT-PERSPECTIVE

**Verified relationship (after OJ-text analysis):** SAME — DIFFERENT-PERSPECTIVE

**Reasoning (1-2 paragraphs):** The OJ text supports the CRDA classification. CRA detection is inside the product; DORA detection is at the entity infrastructure level. Both are needed; CRA does not substitute for DORA SPOF identification, and DORA does not substitute for CRA product-internal state-change visibility.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect**; it should be "scope-disjoint" in baseline. This pair was not classified contradictory.

**Downstream implication (1-2 sentences):** Doc 07 should treat CRA product monitoring and DORA entity detection as two layers of the same detection posture, not as alternatives.


---


