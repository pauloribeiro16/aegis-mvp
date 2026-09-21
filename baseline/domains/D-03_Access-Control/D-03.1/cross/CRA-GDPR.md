# D-03.1 — Pair analysis: GDPR ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ CRA

**GDPR article (verbatim):**
> Art. 12(6) permits the controller, where the controller has reasonable doubts concerning the identity of the natural person making a request under Art. 15–22, to request the additional information necessary to confirm the identity of the data subject.

**CRA article (verbatim):**
> Annex I Part I (2)(d) requires protection from unauthorised access by appropriate control mechanisms, including but not limited to authentication, identity, or access-management systems; the "including but not limited to" clause keeps the floor open to other technical means while naming the three substantive control families.

**Scope comparison:**
- GDPR scope: controller-side verification of data subjects.
- CRA scope: product-level identity, authentication and access-management controls.
- Scope overlap: Conditional when a CRA product is used to process data-subject rights requests; otherwise N.

**Trigger comparison:**
- GDPR trigger: reasonable doubts about a data subject's identity.
- CRA trigger: continuous product security-design obligation.
- Trigger alignment: DIFFERENT.

**Threshold/timeline comparison:**
- GDPR: necessary additional information only.
- CRA: appropriate control mechanisms commensurate with cybersecurity risk.
- Tension: NONE.

**Recipient comparison:**
- GDPR: controller and requesting data subject.
- CRA: manufacturer, product users and market-surveillance evidence trail.

**Content template comparison:**
- GDPR: requester identity proofing and minimisation record.
- CRA: product identity/authentication/access-management design records.

**Classified relationship (from CRDA):** DIFFERENT-PERSPECTIVE

**Verified relationship (after OJ-text analysis):** SAME — DIFFERENT-PERSPECTIVE

**Reasoning (1-2 paragraphs):** GDPR and CRA both speak about identity, but the OJ text confirms that they regulate different objects. GDPR regulates whether a controller may request additional information from a natural person; CRA regulates product mechanisms for unauthorised-access protection. The pair is not contradictory and not equal. The same product can support both duties, but the legal duties attach to different roles and evidence sets.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect**; it should be "scope-disjoint" in baseline. This pair was not classified contradictory.

**Downstream implication (1-2 sentences):** Doc 07 should separate controller rights-verification procedures from manufacturer product identity-management requirements, with a hand-off when the product hosts the rights endpoint.


## Summary (Domain Analysis)

| GDPR ↔ CRA | **Different perspective** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-009 + SR-GDPR-010, Art. 12(6) + Art. 11(2)) | Proportionate identity verification for data subjects | Controller; data-subject-side; PR.AA-03 + PR.AA-02 |
| **CRA** (SR-CRA-023, Annex I Part I (2)(d) + Art. 13(15) + Annex II §3) | Authentication identity + unique product identification (type/batch/serial) | Manufacturer; product-level + user/service/integrated-component identities; PR.AA-01 + ID.AM-01 |

**Why Different perspective**: GDPR's identity management is for data subjects (rights-exercise); CRA's is for product users, services, and integrated components. The two operate at different boundaries (data subject vs product identity). A CRA-regulated product with data subjects is jointly bound; the data-subject-side verification (GDPR) and the product-side identity management (CRA) are different perspectives on identity at different layers. → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-009; `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-023



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_

