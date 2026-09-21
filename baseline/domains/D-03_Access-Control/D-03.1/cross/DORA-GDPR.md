# D-03.1 — Pair analysis: GDPR ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ DORA

**GDPR article (verbatim):**
> Art. 12(6) permits the controller, where the controller has reasonable doubts concerning the identity of the natural person making a request under Art. 15–22, to request the additional information necessary to confirm the identity of the data subject.

**DORA article (verbatim):**
> Art. 9(4)(d) requires financial entities to implement policies and protocols for strong authentication mechanisms, based on relevant standards and dedicated control systems, and protection measures of cryptographic keys whereby data is encrypted based on results of approved data classification and ICT risk assessment processes.

**Scope comparison:**
- GDPR scope: rights-request identity verification for data subjects.
- DORA scope: financial-entity authentication and key-protection policies.
- Scope overlap: Conditional when the financial entity is also a controller; otherwise the identity object differs.

**Trigger comparison:**
- GDPR trigger: reasonable doubt about a data-subject requester.
- DORA trigger: continuous ICT security-policy duty.
- Trigger alignment: DIFFERENT.

**Threshold/timeline comparison:**
- GDPR: necessary additional information.
- DORA: strong authentication based on relevant standards and dedicated control systems.
- Tension: NONE.

**Recipient comparison:**
- GDPR: data subject and controller.
- DORA: financial-entity governance and competent-authority evidence.

**Content template comparison:**
- GDPR: proofing criteria and data-minimisation record.
- DORA: authentication policy, standard selection and control-system evidence.

**Classified relationship (from CRDA):** COMPLEMENTARY

**Verified relationship (after OJ-text analysis):** SAME — COMPLEMENTARY

**Reasoning (1-2 paragraphs):** The OJ text supports complementarity. DORA supplies a stronger internal authentication baseline for financial entities, while GDPR supplies the data-subject rights verification rule. The shared implementation can be one identity stack, but the obligations remain layered: DORA governs financial-entity ICT access, and GDPR governs personal-data-rights verification.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect**; it should be "scope-disjoint" in baseline. This pair was not classified contradictory.

**Downstream implication (1-2 sentences):** Doc 07 should allow one authentication system to satisfy both, but should document distinct GDPR requester-verification and DORA staff/service-authentication rules.


## Summary (Domain Analysis)

| GDPR ↔ DORA | **Complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-009 + SR-GDPR-010, Art. 12(6) + Art. 11(2)) | Proportionate identity verification for data subjects | Data-subject-side; PR.AA-03 + PR.AA-02 + PR.DS-12 |
| **DORA** (SR-DORA-002, Art. 9(4)(d)) | Strong authentication + key protection (3-control AND); identity-lifecycle is one dimension | Financial entity; strong-authentication; PR.AA-03 + PR.AA-04 |

**Why Complementary**: DORA's strong-authentication obligation is the principal identity-lifecycle anchor for DORA financial entities; GDPR's data-subject identity verification is the rights-exercise anchor. A DORA financial entity processing personal data is jointly bound: DORA strong-authentication for staff/services (PR.AA-03 + PR.AA-04) + GDPR data-subject verification (PR.AA-03 + PR.AA-02). The two converge on PR.AA-03 as the shared anchor. → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-009; `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-002



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_

