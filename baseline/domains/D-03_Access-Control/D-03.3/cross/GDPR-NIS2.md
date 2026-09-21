# D-03.3 — Pair analysis: GDPR ↔ NIS 2

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ NIS2

**GDPR article (verbatim):**
> Art. 29 requires the processor and any person acting under the authority of the controller or of the processor, who has access to personal data, not to process those data except on instructions from the controller, unless required to do so by Union or Member State law. Art. 32(4) reinforces this for natural persons acting under controller or processor authority by requiring the controller and processor to take steps to ensure that any such natural person does not process the data except on instructions.

**NIS2 article (verbatim):**
> Article 21(2)(i) of Directive (EU) 2022/2555 requires essential and important entities to take measures regarding human resources security, access control policies and asset management, coordinated by the conjunction AND.

**Scope comparison:**
- GDPR scope: chain of authority controller → processor → authorised persons for personal-data processing.
- NIS2 scope: entity-level access-control and HR-security measures.
- Scope overlap: Conditional when a controller is also a NIS2 entity.

**Trigger comparison:**
- GDPR trigger: any personal-data processing by authorised persons.
- NIS2 trigger: continuous entity access-control duty.
- Trigger alignment: PARTIAL.

**Threshold/timeline comparison:**
- GDPR: documented instructions and confidentiality.
- NIS2: appropriate and proportionate access-control policies.
- Tension: NONE.

**Recipient comparison:**
- GDPR: data subjects and supervisory authority if audited.
- NIS2: NIS competent authority and CSIRT.

**Content template comparison:**
- GDPR: chain-of-authority evidence and confidentiality undertakings.
- NIS2: access-control policy, role definitions, HR lifecycle.

**Classified relationship (from CRDA):** COMPLEMENTARY

**Verified relationship (after OJ-text analysis):** SAME — COMPLEMENTARY

**Reasoning (1-2 paragraphs):** The OJ text supports complementarity. GDPR anchors authorisation to instruction-bound processing; NIS2 anchors it to entity-wide access-control policies. The two obligations are compatible: a NIS2 access-control policy can document the GDPR instructions as the basis for the policy.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect**; it should be "scope-disjoint" in baseline. This pair was not classified contradictory.

**Downstream implication (1-2 sentences):** Doc 07 should map GDPR instruction sets into NIS2 access-control policies without forcing two separate artefacts.


## Summary (Domain Analysis)

| GDPR ↔ NIS2 | **Complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-011, Art. 29 + Art. 32(4) + Art. 28(3)(a)/(b)) | Instruction-bound processing under least-privilege authorisation; chain of authority controller → processor → authorised persons | Controller/processor; personal-data scope; PR.AA-05 + PR.AA-06 |
| **NIS2** (SR-NIS2-003, Art. 21(2)(i) — access-control + HR-security dimension) | Access control policies + HR security; model-agnostic; RBAC/ABAC/MAC/DAC all admissible | Entity-level; PR.AA-01 + PR.AA-05 |

**Why Complementary**: GDPR's Art. 29 + Art. 32(4) chain-of-authority pattern (controller → processor → authorised persons) is the personal-data-scope authorisation obligation; NIS 2's Art. 21(2)(i) access-control + HR-security is the entity-side architecture. A controller that is a NIS 2 essential entity is jointly bound: the personal-data-scope chain of authority (GDPR) + the entity-side access-control policy (NIS 2). The two converge on PR.AA-05 (least privilege) as the shared anchor. → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-011; `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-003



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_

