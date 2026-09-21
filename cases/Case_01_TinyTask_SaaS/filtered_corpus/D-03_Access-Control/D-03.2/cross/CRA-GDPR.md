# D-03.2 — Pair analysis: GDPR ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ CRA

**GDPR article (verbatim):**
> Art. 28(3)(b) requires the processor contract to ensure that persons authorised to process personal data have committed themselves to confidentiality or are under an appropriate statutory obligation of confidentiality.

**CRA article (verbatim):**
> Annex I Part I (2)(d) requires protection from unauthorised access by appropriate control mechanisms, including but not limited to authentication, identity, or access-management systems; the "including but not limited to" clause keeps the floor open to other technical means while naming the three substantive control families.

**Scope comparison:**
- GDPR scope: controller/processor staff-side confidentiality and instructions.
- CRA scope: product-level unauthorised-access controls that may include authentication.
- Scope overlap: Conditional when a CRA product processes personal data or supports staff access.

**Trigger comparison:**
- GDPR trigger: personal-data processing by authorised persons.
- CRA trigger: continuous product security design.
- Trigger alignment: DIFFERENT.

**Threshold/timeline comparison:**
- GDPR: no explicit MFA requirement.
- CRA: appropriate controls; authentication is optional within an open control family.
- Tension: NONE.

**Recipient comparison:**
- GDPR: controller/processor accountability.
- CRA: manufacturer documentation and user-facing controls.

**Content template comparison:**
- GDPR: instruction and confidentiality evidence.
- CRA: product authentication/identity/access-management evidence.

**Classified relationship (from CRDA):** COMPLEMENTARY

**Verified relationship (after OJ-text analysis):** SAME — COMPLEMENTARY

**Reasoning (1-2 paragraphs):** The OJ-derived CRA text says authentication is included but not limited; it does not impose MFA expressly. GDPR likewise does not mandate MFA. The pair is compatible but weak as an MFA source. It should not be used to derive a hard MFA requirement without NIS2 or DORA.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect**; it should be "scope-disjoint" in baseline. This pair was not classified contradictory.

**Downstream implication (1-2 sentences):** Doc 07 should mark this pair as permissive authentication support, not an explicit MFA mandate.


## Summary (Domain Analysis)

| GDPR ↔ CRA | **Complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-011 + SR-GDPR-012, Art. 28(3)(b) + Art. 29) | No explicit MFA; staff instructions + confidentiality | Controller/processor; staff-side; PR.AA-05 + PR.AA-06 + PR.AT-02 |
| **CRA** (SR-CRA-016, Annex I Part I (2)(d) — partial) | Protection from unauthorised access via "appropriate control mechanisms, which may include authentication, identity, or access-management systems" | Manufacturer; product-level; "including but not limited to" + 3-way OR; PR.AA-05 + PR.AA-06 + DE.CM-09 |

**Why Complementary**: Neither GDPR nor CRA has an explicit MFA mandate in the OJ text (the "may include" in CRA + the "appropriate control mechanisms" + 3-way OR in CRA are the textual evidence). Both rely on the broader "appropriate control mechanisms" framing. A controller using a CRA-regulated product is jointly bound by the staff-side instructions (GDPR) and the product-side "appropriate control mechanisms" (CRA). Where MFA is selected as the appropriate control mechanism for the product (CRA) and for staff (GDPR via controller discretion), the two are compatible. → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-011; `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-016



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_

