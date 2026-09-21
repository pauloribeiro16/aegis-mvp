# D-03.3 — Pair analysis: GDPR ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ CRA

**GDPR article (verbatim):**
> Art. 29 requires the processor and any person acting under the authority of the controller or of the processor, who has access to personal data, not to process those data except on instructions from the controller, unless required to do so by Union or Member State law. Art. 32(4) reinforces this for natural persons acting under controller or processor authority.

**CRA article (verbatim):**
> Annex I Part I (2)(d) requires protection from unauthorised access through appropriate control mechanisms — and the clause's broader scope in the OJ covers both the control itself and the visibility into access events, supporting the manufacturer-side reporting on possible unauthorised access. Annex I Part I (2)(j) limits attack surfaces, including external interfaces, in support of this access-control posture by reducing the number of contact points an adversary could probe.

**Scope comparison:**
- GDPR scope: chain of authority for personal-data processing.
- CRA scope: product-level access control to authenticated and authorised users, services and hardware.
- Scope overlap: Conditional when a CRA product processes personal data.

**Trigger comparison:**
- GDPR trigger: personal-data processing.
- CRA trigger: continuous product access-control duty.
- Trigger alignment: PARTIAL.

**Threshold/timeline comparison:**
- GDPR: documented instructions, confidentiality.
- CRA: limited to authenticated and authorised users, services and hardware, with possible unauthorised access reported.
- Tension: NONE.

**Recipient comparison:**
- GDPR: data subjects and supervisory authority.
- CRA: manufacturer documentation, product users and market surveillance.

**Content template comparison:**
- GDPR: instruction records and confidentiality undertakings.
- CRA: product access-control records and unauthorised-access reporting.

**Classified relationship (from CRDA):** COMPLEMENTARY

**Verified relationship (after OJ-text analysis):** SAME — COMPLEMENTARY

**Reasoning (1-2 paragraphs):** GDPR governs the chain of authority over data subjects' personal data; CRA governs the product's access boundary. The two are complementary, with the GDPR instruction typically being the source of CRA access-control decisions when the product is used by a controller.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect**; it should be "scope-disjoint" in baseline. This pair was not classified contradictory.

**Downstream implication (1-2 sentences):** Doc 07 should require deployer-side GDPR instruction records to flow into the CRA product's access-control policy and reporting.


## Summary (Domain Analysis)

<!-- pair: GDPR,CRA -->
| GDPR ↔ CRA | **Complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-011, Art. 29 + Art. 32(4) + Art. 28(3)(a)/(b)) | Instruction-bound processing under least-privilege authorisation; chain of authority | Controller/processor; personal-data scope; PR.AA-05 + PR.AA-06 |
| **CRA** (SR-CRA-017 + SR-CRA-024, Annex I Part I (2)(d) + (2)(j)) | Access limited to authenticated + authorised users/services/hardware; attack-surface limitation | Manufacturer; product-level; PR.AA-05 + PR.AA-06 + DE.CM-09 |

**Why Complementary**: GDPR's chain-of-authority is the personal-data-scope authorisation; CRA's Annex I Part I (2)(d) + (2)(j) is the product-side authorisation + attack-surface-limitation obligation. A controller using a CRA-regulated product is jointly bound: the personal-data-scope chain of authority (GDPR) + the product-side access control (CRA). The two converge on PR.AA-05 + PR.AA-06 as the shared anchors. → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-011; `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-017 + SR-CRA-024



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_

