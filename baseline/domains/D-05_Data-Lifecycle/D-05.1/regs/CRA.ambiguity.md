# D-05.1 — Relevant Ambiguity (CRA)

> Part 4 ambiguity analysis for CRA, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## CRA
#### 3.1 CRA-CL01 — Art. 6 chapeau + (a) — Essential-requirements gate (Part I)
**Source locus:**
> Products with digital elements shall be made available on the market only where:
> **(a)** they meet the **<mark>essential cybersecurity requirements set out in Part I of Annex I</mark>** …;
**Instance 1 — VAG — S2 — `essential cybersecurity requirements`**
Inherits from Annex I Part I (analysed in `09_CRA_AnnexI_EssentialRequirements.md`). The `essential` modifier is itself undefined.
- **R1:** `essential` = mandatory (all Part I requirements must be met).
- **R2:** `essential` = core (some Part I requirements apply, depending on risk assessment).
- **R3:** `essential` = minimum baseline (additional requirements allowed).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | All | In-Directive: Art. 13(3) `shall indicate whether and, if so in what manner, the security requirements set out in Part I, point (2), of Annex I are applicable` |
| R2 | Conditional | In-Directive: Art. 13(3) implies Part I (2) is conditional on risk assessment |
| R3 | Baseline | None in OJ |
R2 is the literal reading (Part I (1) is mandatory; Part I (2) is conditional). S2.
*Berry anchor:* §3.3.1 (`essential`).
**Instance 2 — POLY — S2 — `meet`**
`meet` — what threshold?
- **R1:** Pass conformity assessment (Art. 32).
- **R2:** Self-declare conformity.
- **R3:** Demonstrate by technical documentation.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Third-party verified | None in OJ; Art. 32(1)(a) module A (internal) |
| R2 | Self-declared | In-Directive: Art. 32(1)(a) internal control |
| R3 | Documented | In-Directive: Art. 13(12) technical documentation |
R1/R2/R3 are class-dependent (Art. 32 routes products to modules). S2.
*Berry anchor:* §3.3.1 (`meet`).
**Instance 3 — VAG — S2 — `shall be made available on the market only where`**
The "only where" is a **necessary condition** reading. The reading:
- **R1:** Strict necessary condition (no market access without Annex I conformity).
- **R2:** Necessary condition with carve-outs (e.g. trade fairs per Art. 4(2)).
- **R3:** Necessary condition with delegation to implementing acts.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Strict | In-Directive: literal `only where` |
| R2 | With Art. 4(2) carve-outs | In-Directive: Art. 4(2) trade-fair presentation |
| R3 | With IA carve-outs | None in OJ |
R1 is the literal reading; R2 is the harmonised reading. S2.
*Berry anchor:* §5.1 (`only where`).
---
#### 3.6 CRA-CL19 — Art. 13(3) sentence 2 — Intended purpose + reasonably foreseeable use
**Source locus:**
> That cybersecurity risk assessment shall comprise at least an analysis of cybersecurity risks based on the **intended purpose and reasonably foreseeable use, as well as the conditions of use**, of the product with digital elements, such as the operational environment or the assets to be protected …
**Instance 1 — COORD — S3 — `intended purpose AND reasonably foreseeable use`**
The Art. 3(23)/(24) propagation. AND of the two risk-assessment dimensions.
- **R1:** Both required (cumulative).
- **R2:** Either (entity choice).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Both | In-Directive: literal `and` |
| R2 | Either | None in OJ |
R1 is the literal reading. S3.
*Berry anchor:* §5.4.7 (AND).
**Instance 2 — VAG — S2 — `conditions of use`**
`conditions of use` — operational environment? user behaviour? deployment context?
- **R1:** Operational environment.
- **R2:** User behaviour.
- **R3:** Deployment context.
- **R4:** All three.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Operational env | In-Directive: literal `such as the operational environment` |
| R2 | User behaviour | None in OJ |
| R3 | Deployment context | None in OJ |
| R4 | All | In-Directive: literal |
R4 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`conditions of use`).
**Instance 3 — POLY — S2 — `operational environment or the assets to be protected`**
Two illustrative examples (OR).
- **R1:** Operational env only.
- **R2:** Assets only.
- **R3:** Either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Env | In-Directive: literal |
| R2 | Assets | In-Directive: literal |
| R3 | Either | In-Directive: literal `or` |
R3 is the literal reading. S2.
*Berry anchor:* §5.4.7 (OR).
---
## CRA v0.2 — Annex I Essential Cybersecurity Requirements
> **Source.** OJ L, 20.11.2024, p. 68–69. `03_REFERENCE_MATERIAL/Regulatory_References/CRA.txt`, lines ~4153–4234.
>
> **Pattern.** Each Part quoted verbatim with highlighting, then per-clause analysis. Universal `[recital NN]` convention.
>
> **Annex I is the binding normative core of CRA.** Part I defines security properties for products; Part II defines vulnerability-handling obligations for manufacturers. These are referenced by Art. 6, 7, 8, 13, 27, 28, 32, and are the ultimate compliance target. 21 of the 26 T2 clauses lived in Annex I.
---
### 1. Annex I — full text
#### 3.4 CRA-CL136 — Part I (2)(g) — Data minimisation
**Source locus:**
> process only data, personal or other, that are **adequate, relevant and limited to what is necessary** in relation to the **intended purpose** of the product with digital elements (data minimisation);
**Instance 1 — VAG — S3 — `adequate, relevant and limited to what is necessary`**
*Berry anchor:* §5.1 (`adequate`, `relevant`, `necessary`).
**Instance 2 — POLY — S2 — `intended purpose`**
Inherits Art. 3(23) D23. Same multi-source definition (instructions, promotional, statements, technical documentation).
*Berry anchor:* §3.3.1 (`intended purpose`).
---

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/CRA.ambiguity.md

Same as GDPR Art. 5(1)(c) `adequate, relevant and limited to what is necessary`. Cross-regulation pattern.

<!-- aegis:purity: own_reg=CRA; demoted=1; core_cross_mentions=0 -->

