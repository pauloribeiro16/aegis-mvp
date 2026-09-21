# D-03.3 — Pair analysis: GDPR ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ DORA

**GDPR article (verbatim):**
> Art. 29 requires the processor and any person acting under the authority of the controller or of the processor, who has access to personal data, not to process those data except on instructions from the controller, unless required to do so by Union or Member State law. Art. 32(4) reinforces this for natural persons acting under controller or processor authority.

**DORA article (verbatim):**
> Art. 9(4)(c) requires financial entities to implement policies that limit physical or logical access to information assets and ICT assets to what is required for legitimate and approved functions and activities only.

**Scope comparison:**
- GDPR scope: personal-data-processing chain of authority.
- DORA scope: financial-entity access to information assets and ICT assets.
- Scope overlap: Conditional where a financial entity processes personal data.

**Trigger comparison:**
- GDPR trigger: personal-data processing by authorised persons.
- DORA trigger: continuous financial-entity ICT access-policy duty.
- Trigger alignment: PARTIAL.

**Threshold/timeline comparison:**
- GDPR: instruction-bound processing, confidentiality.
- DORA: access limited to "legitimate and approved functions and activities only" with the OJ `only` qualifier.
- Tension: NONE.

**Recipient comparison:**
- GDPR: data subjects and supervisory authority.
- DORA: financial-entity governance and competent authority.

**Content template comparison:**
- GDPR: instruction records, confidentiality undertakings.
- DORA: legitimate-and-approved function mapping per access grant.

**Classified relationship (from CRDA):** COMPLEMENTARY

**Verified relationship (after OJ-text analysis):** SAME — COMPLEMENTARY

**Reasoning (1-2 paragraphs):** The OJ text supports complementarity. DORA adds the `legitimate and approved` + `only` qualifiers on the financial-entity side; GDPR adds the chain-of-authority and confidentiality obligations on the personal-data side. A DORA financial entity also acting as a controller can map GDPR instructions into the DORA legitimate-and-approved function register.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect**; it should be "scope-disjoint" in baseline. This pair was not classified contradictory.

**Downstream implication (1-2 sentences):** Doc 07 should require one legitimate-and-approved function register to satisfy both, with the DORA `only` qualifier documented in the same artefact.


## Summary (Domain Analysis)

<!-- pair: GDPR,DORA -->
| GDPR ↔ DORA | **Complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-011, Art. 29 + Art. 32(4)) | Instruction-bound processing under least-privilege authorisation | Controller/processor; personal-data scope; PR.AA-05 + PR.AA-06 |
| **DORA** (SR-DORA-006, Art. 9(4)(c)) | Access limited to "legitimate and approved functions and activities only" | Financial entity; ICT-system scope; T4-vs-text gap (T4 reads RBAC + need-to-know + least privilege; OJ literal preserves "legitimate and approved") |

**Why Complementary**: GDPR's instruction-bound processing is the personal-data-scope chain of authority; DORA's Art. 9(4)(c) is the financial-entity-side access-control obligation with the "legitimate and approved" AND + "only" qualifier. A DORA financial entity processing personal data is jointly bound: the personal-data-scope chain of authority (GDPR) + the ICT-system access control (DORA). The two converge on PR.AA-05 (least privilege) as the shared anchor. **Caveat:** the T4-vs-text gap on DORA-C14 (Art. 9(4)(c)) — T4 unpacks as `need-to-know and least privilege` but OJ text contains neither phrase; the literal `legitimate and approved functions and activities only` is preserved in SR-DORA-006. → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-011; `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-006



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_

