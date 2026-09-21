# D-03.3 — Pair analysis: NIS 2 ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: NIS2 ↔ DORA

**NIS2 article (verbatim):**
> Article 21(2)(i) of Directive (EU) 2022/2555 requires essential and important entities to take measures regarding human resources security, access control policies and asset management, coordinated by the conjunction AND.

**DORA article (verbatim):**
> Art. 9(4)(c) requires financial entities to implement policies that limit physical or logical access to information assets and ICT assets to what is required for legitimate and approved functions and activities only.

**Scope comparison:**
- NIS2 scope: essential/important entity access-control and HR-security measures.
- DORA scope: financial-entity physical/logical access to information assets and ICT assets.
- Scope overlap: Conditional for financial entities also within retained NIS2 scope.

**Trigger comparison:**
- NIS2 trigger: continuous entity cyber-risk-management duty.
- DORA trigger: continuous financial-entity ICT-risk-management duty.
- Trigger alignment: PARTIAL.

**Threshold/timeline comparison:**
- NIS2: appropriate and proportionate controls.
- DORA: access limited to "legitimate and approved functions and activities only".
- Tension: NONE.

**Recipient comparison:**
- NIS2: NIS competent authority and CSIRT.
- DORA: financial-entity governance and competent authority.

**Content template comparison:**
- NIS2: access-control policy and HR-lifecycle records.
- DORA: legitimate-and-approved function register and `only` qualifier evidence.

**Classified relationship (from CRDA):** EQUAL

**Verified relationship (after OJ-text analysis):** CORRECTED — COMPLEMENTARY

**Reasoning (1-2 paragraphs):** Both regulations impose an entity-level access-control obligation, but the OJ anchors differ: NIS2's Art. 21(2)(i) is model-agnostic (`access control policies`), while DORA's Art. 9(4)(c) explicitly carries the `legitimate and approved functions and activities only` qualifier. The two are not the same obligation because DORA's `only` qualifier is operationally more demanding. The CRDA EQUAL classification is over-tight; COMPLEMENTARY is the verified classification.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect**; it should be "scope-disjoint" in baseline. This pair was not classified contradictory.

**Downstream implication (1-2 sentences):** Doc 07 should keep the two access-control policies linked, with DORA's `only` qualifier recorded as the floor for the financial-sector.


## Summary (Domain Analysis)

| NIS2 ↔ DORA | **Equal** | Tension/difference |
|---|---|---|
| **NIS2** (SR-NIS2-003, Art. 21(2)(i) — access-control dimension) | Access control policies + HR security + asset management; model-agnostic | Entity-level; PR.AA-01 + PR.AA-05 |
| **DORA** (SR-DORA-006, Art. 9(4)(c)) | Access limited to "legitimate and approved functions and activities only" | Financial entity; "legitimate and approved" + "only" qualifier; T4-vs-text gap on `need-to-know` / `least privilege` |

**Why Equal (with textual anchor difference)**: Both regulations impose an access-control obligation at the entity level; the principal difference is the textual anchor (NIS 2 "access control policies" model-agnostic; DORA "legitimate and approved functions and activities only" with the literal "only" qualifier). A DORA financial entity that is a NIS 2 essential entity is jointly bound: the NIS 2 access-control policy + the DORA "legitimate and approved" anchor. The DORA "only" qualifier is operationally more demanding (it closes off any access that is not strictly tied to a legitimate and approved function), while NIS 2's model-agnostic framing leaves the access-control model to entity discretion. The two converge on PR.AA-05 (least privilege) as the shared anchor. → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-003; `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-006



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_

