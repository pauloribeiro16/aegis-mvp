# D-03.4 — Relevant Ambiguity (CRA)

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
#### 3.2 CRA-CL02 — Art. 6(a) proviso — Installation/use conditions
**Source locus:**
> …provided that they are **properly installed, maintained, used for their intended purpose or under conditions which can reasonably be foreseen, and, where applicable, the necessary security updates have been installed**;
**Instance 1 — VAG — S3 — `properly installed, maintained`**
`properly` — what constitutes proper?
- **R1:** Per manufacturer instructions (Annex II §8).
- **R2:** Per industry standards.
- **R3:** Per a reasonable user's understanding.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Per instructions | In-Directive: Annex II §8 `necessary measures during initial commissioning` |
| R2 | Per industry | None in OJ |
| R3 | Per reasonable user | None in OJ |
R1 is the literal reading. R2/R3 admit materially different compliance populations. S3.
*Berry anchor:* §5.1 (`properly`).
**Instance 2 — VAG — S3 — `intended purpose or under conditions which can reasonably be foreseen`**
`intended purpose` (Art. 3(23)) OR `reasonably foreseeable` (Art. 3(24)) — alternative conditions.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Intended purpose OR foreseeable | In-Directive: literal `or` |
| R2 | Intended purpose ONLY | None in OJ |
| R3 | Foreseeable ONLY | None in OJ |
R1 is the literal reading. S3.
*Berry anchor:* §5.1 (`intended purpose`); §5.4.7 (OR).
**Instance 3 — VAG — S2 — `where applicable, the necessary security updates have been installed`**
`necessary security updates` — which updates are necessary?
- **R1:** Critical security updates only.
- **R2:** All security updates.
- **R3:** Updates required by Annex I Part II §3 (effective and regular tests).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Critical | None in OJ |
| R2 | All | In-Directive: Annex I Part II §3 |
| R3 | Per Annex I | In-Directive: Annex I Part II §3 |
R2 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`necessary security updates`).
**Instance 4 — POLY — S2 — `installed`**
`installed` — software-only? Hardware? Firmware?
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Software | None in OJ |
| R2 | Hardware | None in OJ |
| R3 | Any | In-Directive: literal `installed` |
R3 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`installed`).
---
## CRA v0.2 — Annex I Essential Cybersecurity Requirements
> **Source.** OJ L, 20.11.2024, p. 68–69. `03_REFERENCE_MATERIAL/Regulatory_References/CRA.txt`, lines ~4153–4234.
>
> **Pattern.** Each Part quoted verbatim with highlighting, then per-clause analysis. Universal `[recital NN]` convention.
>
> **Annex I is the binding normative core of CRA.** Part I defines security properties for products; Part II defines vulnerability-handling obligations for manufacturers. These are referenced by Art. 6, 7, 8, 13, 27, 28, 32, and are the ultimate compliance target. 21 of the 26 T2 clauses lived in Annex I.
---
### 1. Annex I — full text
#### 3.2 CRA-CL131 — Part I (2)(b) — Secure by default
**Source locus:**
> be made available on the market with a **secure by default configuration**, unless otherwise agreed between manufacturer and business user in relation to a tailor-made product with digital elements, including the possibility to **reset the product to its original state**;
**Instance 1 — VAG — S3 — `secure by default configuration`**
`secure by default` — undefined. Three materially distinct readings:
- **R1:** Minimal-privilege default (lock down first, open on user choice).
- **R2:** Configuration with security features enabled by default.
- **R3:** The product works securely without user configuration (no setup required).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Minimal-privilege | None in OJ |
| R2 | Features enabled | None in OJ |
| R3 | Zero-config security | None in OJ |
S3 because R1/R2/R3 produce materially different compliance obligations.
*Berry anchor:* §5.1 (`secure by default configuration`).
**Instance 2 — SCOPE-Q — S2 — `unless otherwise agreed between manufacturer and business user in relation to a tailor-made product with digital elements`**
Exception clause — tailor-made products.
- **R1:** Business users only (consumer products cannot opt out).
- **R2:** All users (tailor-made = any customised product).
- **R3:** Only formal contractual agreements (not unilateral changes).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Business users only | In-Directive: literal `business user` |
| R2 | All users | None in OJ |
| R3 | Formal contracts | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`business user`).
**Instance 3 — VAG — S2 — `reset the product to its original state`**
`original state` — factory-reset state? Initial-configuration state?
- **R1:** Factory-reset state (no user data).
- **R2:** Initial-configuration state (preserves user data).
- **R3:** Either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Factory reset | In-Directive: literal `original state` |
| R2 | Initial config | None in OJ |
| R3 | Either | None in OJ |
S2.
*Berry anchor:* §3.3.1 (`original state`).
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

<!-- aegis:purity: own_reg=CRA; demoted=0; core_cross_mentions=0 -->

