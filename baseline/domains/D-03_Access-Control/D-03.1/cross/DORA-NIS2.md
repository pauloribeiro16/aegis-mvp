# D-03.1 — Pair analysis: NIS 2 ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: NIS2 ↔ DORA

**NIS2 article (verbatim):**
> Article 21(2)(i) of Directive (EU) 2022/2555 requires essential and important entities to take measures regarding human resources security, access control policies and asset management, coordinated by the conjunction AND.

**DORA article (verbatim):**
> Art. 9(4)(d) requires financial entities to implement policies and protocols for strong authentication mechanisms, based on relevant standards and dedicated control systems, and protection measures of cryptographic keys whereby data is encrypted based on results of approved data classification and ICT risk assessment processes.

**Scope comparison:**
- NIS2 scope: essential/important entity access-control and HR-security measures.
- DORA scope: financial-entity strong-authentication and cryptographic-key controls.
- Scope overlap: Conditional for financial entities also treated as NIS2 entities or where NIS2 obligations are retained alongside DORA.

**Trigger comparison:**
- NIS2 trigger: continuous entity cyber-risk-management duty.
- DORA trigger: continuous financial-sector ICT-risk-management duty.
- Trigger alignment: PARTIAL.

**Threshold/timeline comparison:**
- NIS2: appropriate and proportionate controls.
- DORA: strong authentication and dedicated control systems.
- Tension: NONE.

**Recipient comparison:**
- NIS2: NIS competent authority / CSIRT evidence path.
- DORA: financial-sector competent-authority evidence path.

**Content template comparison:**
- NIS2: identity lifecycle, access-control and HR-security records.
- DORA: authentication-strength, standards and key-protection policy records.

**Classified relationship (from CRDA):** COMPLEMENTARY

**Verified relationship (after OJ-text analysis):** SAME — COMPLEMENTARY

**Reasoning (1-2 paragraphs):** The OJ text supports complementarity. NIS2 gives the broad entity-level access-control foundation; DORA adds financial-sector authentication depth. There is no incompatibility. In an overlap case, DORA is the more specific operational floor for strong authentication, while NIS2 supplies broader HR and access-policy governance.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect**; it should be "scope-disjoint" in baseline. This pair was not classified contradictory.

**Downstream implication (1-2 sentences):** Doc 07 should use DORA as the financial-sector authentication depth layer and NIS2 as the broader access-governance layer.


## Summary (Domain Analysis)

| NIS2 ↔ DORA | **Complementary** | Tension/difference |
|---|---|---|
| **NIS2** (SR-NIS2-003, Art. 21(2)(i) — access-control + HR-security dimension) | Workforce identity lifecycle + access-control policies | Entity-level; PR.AA-01 + PR.AA-05 + PR.AT-02 |
| **DORA** (SR-DORA-002, Art. 9(4)(d)) | Strong authentication + key protection; identity is one dimension of the 3-control AND | Financial entity; strong-authentication; PR.AA-03 + PR.AA-04 |

**Why Complementary**: NIS 2's Art. 21(2)(i) access-control + HR-security dimension is the broader entity-side architecture; DORA's strong-authentication is the financial-sector-specific anchor with a 3-control AND (strong auth + key protection + encryption). A DORA financial entity that is a NIS 2 essential entity is jointly bound: the NIS 2 access-control policy + HR lifecycle + the DORA strong-authentication dimension. The two converge on PR.AA-01 (identities managed) + PR.AA-05 (least privilege) as shared anchors; DORA adds PR.AA-03 + PR.AA-04 (the strong-authentication specific layer). → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-003; `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-002



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_

