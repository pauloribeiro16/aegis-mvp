# D-03.2 — Pair analysis: NIS 2 ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: NIS2 ↔ CRA

**NIS2 article (verbatim):**
> Article 21(2)(j) of Directive (EU) 2022/2555, in its first clause, requires essential and important entities to use multi-factor authentication or continuous authentication solutions, where appropriate.

**CRA article (verbatim):**
> Annex I Part I (2)(d) requires protection from unauthorised access by appropriate control mechanisms, including but not limited to authentication, identity, or access-management systems; the "including but not limited to" clause keeps the floor open to other technical means while naming the three substantive control families.

**Scope comparison:**
- NIS2 scope: entity-level MFA or continuous authentication.
- CRA scope: product-level appropriate access controls that may include authentication.
- Scope overlap: Conditional where a NIS2 entity deploys or manufactures CRA products.

**Trigger comparison:**
- NIS2 trigger: continuous entity authentication obligation where appropriate.
- CRA trigger: continuous product access-control obligation.
- Trigger alignment: PARTIAL.

**Threshold/timeline comparison:**
- NIS2: MFA or continuous authentication where appropriate.
- CRA: appropriate controls, not explicit MFA.
- Tension: NONE.

**Recipient comparison:**
- NIS2: entity governance and competent-authority evidence.
- CRA: manufacturer documentation and user-facing controls.

**Content template comparison:**
- NIS2: authentication policy, factor/continuous-authentication rationale.
- CRA: product control-mechanism design and risk assessment.

**Classified relationship (from CRDA):** COMPLEMENTARY

**Verified relationship (after OJ-text analysis):** SAME — COMPLEMENTARY

**Reasoning (1-2 paragraphs):** NIS2 is the explicit MFA/continuous-authentication source. CRA is broader and permissive, naming authentication as one possible control family. Therefore, a product can support the entity's NIS2 authentication duties, but the CRA clause alone does not impose the same MFA threshold.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect**; it should be "scope-disjoint" in baseline. This pair was not classified contradictory.

**Downstream implication (1-2 sentences):** Doc 07 should place the explicit MFA requirement under NIS2, with CRA as product-control support.


## Summary (Domain Analysis)

| NIS2 ↔ CRA | **Complementary** | Tension/difference |
|---|---|---|
| **NIS2** (SR-NIS2-006, Art. 21(2)(j) first clause) | MFA or continuous authentication "where appropriate" | Entity-level; OR of MFA and continuous; PR.AA-03 + PR.AA-05 |
| **CRA** (SR-CRA-016, Annex I Part I (2)(d) — partial) | "Appropriate control mechanisms, may include authentication, identity, or access-management" | Product-level; "may include" + 3-way OR; PR.AA-05 + PR.AA-06 + DE.CM-09 |

**Why Complementary**: NIS 2 has an explicit MFA mandate ("where appropriate"); CRA has only "appropriate control mechanisms, may include authentication". The CRA T2-vs-text gap (T3 imposed MFA + continuous authentication not in OJ) is acknowledged in `99_CRA_Synthesis.md` §4. A NIS 2 essential entity using CRA-regulated products is bound by the NIS 2 MFA/continuous-authentication obligation (entity-side) + the CRA "appropriate control mechanisms" obligation (product-side). The two are compatible: NIS 2's MFA/continuous authentication is the authentication paradigm; CRA's "appropriate control mechanisms" is the broader framing that admits MFA as one of several choices. → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-006; `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-016



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_

