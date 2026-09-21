# D-04.1 — Relevant Ambiguity (CRA)

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
## CRA v0.2 — Annex I Essential Cybersecurity Requirements
> **Source.** OJ L, 20.11.2024, p. 68–69. `03_REFERENCE_MATERIAL/Regulatory_References/CRA.txt`, lines ~4153–4234.
>
> **Pattern.** Each Part quoted verbatim with highlighting, then per-clause analysis. Universal `[recital NN]` convention.
>
> **Annex I is the binding normative core of CRA.** Part I defines security properties for products; Part II defines vulnerability-handling obligations for manufacturers. These are referenced by Art. 6, 7, 8, 13, 27, 28, 32, and are the ultimate compliance target. 21 of the 26 T2 clauses lived in Annex I.
---
### 1. Annex I — full text
#### 3.5 CRA-CL141 — Part I (2)(l) — Logging and monitoring
**Source locus:**
> provide security related information by **recording and monitoring relevant internal activity**, including the access to or modification of data, services or functions, **with an opt-out mechanism for the user**;
**Instance 1 — VAG — S2 — `relevant internal activity`**
`relevant` — to what?
- **R1:** Security-relevant only.
- **R2:** All activity (audit log).
- **R3:** Risk-based.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Security-relevant | In-Directive: literal `security related` |
| R2 | All | None in OJ |
| R3 | Risk-based | In-Directive: Art. 13(2) risk assessment |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`relevant`).
**Instance 2 — VAG — S2 — `opt-out mechanism for the user`**
User can opt out of logging? The reading:
- **R1:** User can disable logging entirely.
- **R2:** User can limit logging scope.
- **R3:** Both.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Disable entirely | In-Directive: literal `opt-out` |
| R2 | Limit scope | None in OJ |
| R3 | Both | None in OJ |
---
#### 3.3 CRA-CL158 — Ann. II §8 — Instructions
**Source locus:**
> detailed instructions or an internet address referring to such detailed instructions and information on: (a) … (f) …
**Instance 1 — VAG — S2 — `detailed instructions`**
`detailed` — how detailed?
- **R1:** Complete security guide.
- **R2:** Summary of key points.
- **R3:** Context-dependent (based on product complexity).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Complete guide | In-Directive: literal `detailed` |
| R2 | Summary | None in OJ |
| R3 | Context-dependent | In-Directive: Art. 13(8) support period context |
R1 is the literal reading. S2.
*Berry anchor:* §5.1 (`detailed`).
**Instance 2 — SCOPE-Q — S2 — `or an internet address referring to such detailed instructions`**
Alternative: physical document or URL.
- **R1:** Physical document sufficient.
- **R2:** URL sufficient.
- **R3:** Either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Physical | In-Directive: literal `or` |
| R2 | URL | In-Directive: literal `internet address` |
| R3 | Either | In-Directive: literal `or` |
R3 is the literal reading. S2.
*Berry anchor:* §5.4.7 (OR).
---
**End of Annex II file. Next: `11_CRA_AnnexVII_TechDocumentation.md`.**

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/CRA.ambiguity.md

R1 is the literal reading. S2. **Cross-reference to Art. 21(2)(j) NIS 2** where the opt-out is also present.

<!-- aegis:purity: own_reg=CRA; demoted=1; core_cross_mentions=0 -->

