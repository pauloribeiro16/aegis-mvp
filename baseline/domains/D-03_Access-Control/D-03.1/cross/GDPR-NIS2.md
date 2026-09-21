# D-03.1 — Pair analysis: GDPR ↔ NIS 2

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ NIS2

**GDPR article (verbatim):**
> Art. 12(6) permits the controller, where the controller has reasonable doubts concerning the identity of the natural person making a request under Art. 15–22, to request the additional information necessary to confirm the identity of the data subject. Art. 11(2) preserves data-subject rights where the data subject provides additional information enabling identification, anchoring the reciprocal obligation: the data subject must supply enough information to be identified if they wish to exercise the rights.

**NIS2 article (verbatim):**
> Article 21(2)(i) of Directive (EU) 2022/2555 requires essential and important entities to take measures regarding human resources security, access control policies and asset management, coordinated by the conjunction AND.

**Scope comparison:**
- GDPR scope: data-subject identity verification at rights-exercise endpoints.
- NIS2 scope: workforce, access-control and asset-management identity foundations at essential/important entities.
- Scope overlap: N typically; Conditional only when a controller is also a NIS2 entity, but the identity objects remain different.

**Trigger comparison:**
- GDPR trigger: reasonable doubts concerning the identity of a rights requester.
- NIS2 trigger: continuous obligation to maintain HR security / access-control measures.
- Trigger alignment: DIFFERENT.

**Threshold/timeline comparison:**
- GDPR: proportionate additional information when reasonable doubts exist.
- NIS2: appropriate-and-proportionate continuous measures.
- Tension: NONE.

**Recipient comparison:**
- GDPR: controller-facing rights requester.
- NIS2: internal entity governance and competent-authority evidence if audited.

**Content template comparison:**
- GDPR: identity-proofing decision and minimised additional information.
- NIS2: HR-lifecycle, access-control-policy and asset-management evidence.

**Classified relationship (from CRDA):** DIFFERENT-PERSPECTIVE

**Verified relationship (after OJ-text analysis):** SAME — DIFFERENT-PERSPECTIVE

**Reasoning (1-2 paragraphs):** The OJ-derived text supports the CRDA distinction. GDPR is external and data-subject-facing; NIS2 is internal and workforce/entity-facing. Both are identity-management concerns, but they are not the same control object. The pair is not contradictory because no clause requires one party to do what the other forbids. A single organisation may need both workflows, but the identity subjects, triggers and evidentiary artefacts differ.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? N
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect**; it should be "scope-disjoint" in baseline. This pair was not classified contradictory.

**Downstream implication (1-2 sentences):** Phase 1C Doc 07 should keep data-subject verification and workforce identity lifecycle as separate control rows, even when implemented through a shared identity platform.


## Summary (Domain Analysis)

| GDPR ↔ NIS2 | **Different perspective** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-009 + SR-GDPR-010, Art. 12(6) + Art. 11(2) + Art. 5(1)(c)) | Proportionate identity verification for rights requests; minimised collection of identity verification data | Controller; data-subject-side; PR.AA-03 + PR.AA-02 + PR.DS-12 |
| **NIS2** (SR-NIS2-003 + SR-NIS2-004, Art. 21(2)(i) HR-security dimension) | Workforce identity lifecycle (joiner-mover-leaver) as HR-security substrate | Entity-level; workforce-side; PR.AT-02 + PR.AA-01 |

**Why Different perspective**: GDPR's identity verification is for data subjects exercising rights (external/rights-exercise context); NIS 2's identity lifecycle is for workforce (joiner-mover-leaver internal context). A controller that is a NIS 2 essential entity is jointly bound: data-subject-side verification (GDPR) + workforce-side lifecycle (NIS 2). The two are different perspectives on identity management at different boundaries (external vs internal). → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-009; `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-003 + SR-NIS2-004



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_

