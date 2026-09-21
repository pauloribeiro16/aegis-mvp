# D-09.1 — Pair analysis: GDPR ↔ NIS 2

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ NIS2

**GDPR article (verbatim, Art. 24(1) + Art. 5(2) + Art. 37-39):**
> "Taking into account the nature, scope, context and purposes of processing as well as the risks of varying likelihood and severity for the rights and freedoms of natural persons, the controller shall implement appropriate technical and organisational measures, such as … policies … which are designed to implement data-protection principles … in an effective manner." — Art. 24(1) GDPR
> "The controller shall be responsible for, and be able to demonstrate compliance with, paragraph 1 ('accountability')." — Art. 5(2) GDPR

**NIS2 article (verbatim, Art. 20(1) sentence 1 + Art. 21(2)(a) + Art. 21(2)(f)):**
> "Member States shall ensure that the management bodies of essential and important entities approve the cybersecurity risk-management measures taken by those entities in order to comply with Article 21, oversee their implementation and can be held liable for infringements by the entities of that Article." — Art. 20(1) sentence 1 NIS 2 (per SR-NIS2-032/033/034)
> "[Member States shall ensure that essential and important entities take appropriate and proportionate technical, operational and organisational measures to … ] (a) policies on risk analysis and information system security; … (f) policies and procedures to assess the effectiveness of cybersecurity risk-management measures." — Art. 21(2)(a)+(f) NIS 2

**Scope comparison:**
- GDPR scope: controller-side data-protection policies (Art. 24) + DPO designation (Art. 37-39).
- NIS 2 scope: management-body approve/oversee/liable (Art. 20(1)) + policies on risk analysis + IS security + effectiveness-assessment (Art. 21(2)(a)+(f)).
- Scope overlap: **Y (when the entity is both a controller and an NSIE).**

**Trigger comparison:**
- GDPR trigger: controller's adoption of data-protection policies.
- NIS 2 trigger: management-body approve + entity adoption of risk-analysis + IS-security + effectiveness-assessment policies.
- Trigger alignment: **PARTIAL** (both policy-driven but different governance hooks).

**Threshold/timeline comparison:**
- GDPR: no quantitative cadence.
- NIS 2: no quantitative cadence (entity-discretionary under Recital 56).
- Tension: **NONE**.

**Recipient comparison:**
- GDPR: data subject, DPA.
- NIS 2: management body, competent authority.

**Content template comparison:**
- GDPR: not codified for content.
- NIS 2: not codified for content.

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** GDPR mandates the policy artefact (data-protection policies); NIS 2 mandates the governance act (management body approves/oversees/liable) AND the policy artefact. NIS 2's governance architecture (approve/oversee/liable) extends to the GDPR policies for entities that are both controllers and NSIEs.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y (when the controller-NSIE adopts data-protection policies subject to management-body approval)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce a layered stack: GDPR Art. 24 data-protection policies + NIS 2 Art. 20(1) management-body approve/oversee/liable governance + NIS 2 Art. 21(2)(a)+(f) policy artefacts.

---


## Summary (Domain Analysis)

| GDPR ↔ NIS2 | **complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-043, Art. 24(1)+(2); SR-GDPR-044, Art. 5(2); SR-GDPR-062/063/064, Art. 37-39) | Appropriate technical and organisational measures; demonstrable compliance; DPO designation and independence. | |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-043 / SR-GDPR-044 / SR-GDPR-062-064 |
| **NIS2** (SR-NIS2-032, Art. 20(1) approve; SR-NIS2-033, Art. 20(1) oversee; SR-NIS2-034, Art. 20(1) liability; SR-NIS2-035, Art. 21(2)(a) risk-analysis policy; SR-NIS2-036, Art. 21(2)(a) IS-security policy; SR-NIS2-037, Art. 21(2)(f) effectiveness-assessment policy) | Management body approve/oversee/liable; risk-analysis policy + IS-security policy + effectiveness-assessment policy. | |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-032 / SR-NIS2-033 / SR-NIS2-034 / SR-NIS2-035 / SR-NIS2-036 / SR-NIS2-037 |

**Why complementary**: GDPR mandates the policy artefact (data-protection policies); NIS 2 mandates the governance act (management body approves/oversees/liable) AND the policy artefact. NIS 2's governance architecture (approve/oversee/liable) extends to the GDPR policies for entities that are both controllers and NSIEs.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
43 lines — see ../../_migration_report.md)_

