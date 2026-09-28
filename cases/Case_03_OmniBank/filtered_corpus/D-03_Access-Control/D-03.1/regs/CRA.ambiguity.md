# D-03.1 — Relevant Ambiguity (CRA)

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
#### 3.4 CRA-CL04 — Art. 7(1) sentence 1 — Important-products classification gate
**Source locus:**
> Products with digital elements which have the **core functionality** of a product category set out in Annex III shall be considered to be important products with digital elements …
**Instance 1 — VAG — S3 — `core functionality`**
`core` — essential vs auxiliary.
- **R1:** Essential (product is in the category by virtue of this functionality).
- **R2:** Primary (the main thing the product does).
- **R3:** Substantial (any significant functionality overlap with the category).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Essential | None in OJ |
| R2 | Primary | None in OJ |
| R3 | Substantial | None in OJ |
R3 admits materially different compliance populations (R3: a product with one feature in Annex III may qualify; R1: must be defined primarily as such). S3.
*Berry anchor:* §3.3.1 (`core`).
**Instance 2 — POLY — S2 — `product category set out in Annex III`**
`product category` — category granularity.
- **R1:** Per product type (e.g. "routers").
- **R2:** Per function (e.g. "network management").
- **R3:** Per market segment (e.g. "enterprise security").
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Product type | In-Directive: Annex III Class I item 12 "Routers" |
| R2 | Function | In-Directive: Annex III Class I item 7 "SIEM systems" |
| R3 | Market segment | None in OJ |
R1 and R2 are dominant. S2.
*Berry anchor:* §3.3.1 (`product category`).
**Instance 3 — VAG — S2 — `shall be considered to be important products with digital elements`**
`considered to be` — automatic designation? Discretionary?
- **R1:** Automatic (the category defines the designation).
- **R2:** Discretionary (MS or Commission can exclude).
- **R3:** Conditional (subject to Commission implementing acts per Art. 7(4)).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Automatic | In-Directive: literal `shall be considered` |
| R2 | Discretionary | None in OJ |
| R3 | Subject to IA | In-Directive: Art. 7(4) technical descriptions |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`shall be considered`).
---
#### 3.5 CRA-CL05 — Art. 7(1) sentence 2 — Integration carve-out
**Source locus:**
> The integration of a product with digital elements which has the core functionality of a product category set out in Annex III **shall not in itself** render the product in which it is integrated subject to the conformity assessment procedures referred to in Article 32(2) and (3).
**Instance 1 — VAG — S2 — `shall not in itself`**
`in itself` — does this admit combined-effect reading?
- **R1:** Pure integration is exempt (literal).
- **R2:** Combined with other Annex III integration, exempt (combined-effect).
- **R3:** Conditional on the integrating product not being a critical product.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Pure integration exempt | In-Directive: literal `in itself` |
| R2 | Combined exempt | None in OJ |
| R3 | Conditional on Art. 8 | In-Directive: Art. 8 critical-product rules |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`in itself`).
**Instance 2 — POLY — S2 — `the product in which it is integrated`**
`integrated` — what integration modes are covered?
- **R1:** Hardware integration (component on PCB).
- **R2:** Software integration (library, API).
- **R3:** System integration (subsystem).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Hardware | None in OJ |
| R2 | Software | None in OJ |
| R3 | System | None in OJ |
R3 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`integrated`).
---
#### 3.6 CRA-CL06 — Art. 7(2)(a) — Classification criterion A
**Source locus:**
> **(a)** the product with digital elements **primarily performs functions critical to the cybersecurity of other products, networks or services**, including securing authentication and access, intrusion prevention and detection, end-point security or network protection;
**Instance 1 — VAG — S3 — `primarily performs functions critical to the cybersecurity`**
Three modifiers (primarily + critical + cybersecurity). Three readings:
- **R1:** `primarily` = majority of functions.
- **R2:** `primarily` = main function (single dominant function).
- **R3:** `primarily` = principal (the function for which the product is sold).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Majority | None in OJ |
| R2 | Single dominant | None in OJ |
| R3 | Principal | None in OJ |
S3.
*Berry anchor:* §3.3.1 (`primarily`).
**Instance 2 — POLY — S2 — `critical to the cybersecurity`**
`critical to the cybersecurity` — relative to what?
- **R1:** Critical to the cybersecurity of any product/network/service.
- **R2:** Critical to the cybersecurity of an entire class of products.
- **R3:** Critical to the cybersecurity of the user's operations.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Any product | In-Directive: literal `other products, networks or services` |
| R2 | Class of products | None in OJ |
| R3 | User's operations | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`critical`).
**Instance 3 — POLY — S2 — `securing authentication and access, intrusion prevention and detection, end-point security or network protection`**
Four examples (illustrative list). The reading:
- **R1:** These four are the only critical functions.
- **R2:** These four are illustrative; other functions can qualify.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Closed list | None in OJ |
| R2 | Open list | In-Directive: literal `including` |
R2 is the literal reading. S2.
*Berry anchor:* §5.1 (`including`).
---
#### 3.7 CRA-CL07 — Art. 7(2)(b) — Classification criterion B
**Source locus:**
> **(b)** the product with digital elements performs a function which **carries a significant risk of adverse effects in terms of its intensity and ability to disrupt, control or cause damage to a large number of other products or to the health, security or safety of its users through direct manipulation**, such as a central system function, including network management, configuration control, virtualisation or processing of personal data.
**Instance 1 — VAG — S3 — `significant risk of adverse effects`**
`significant` + `adverse` — both undefined. Three readings:
- **R1:** Quantitative threshold (e.g. >X users affected).
- **R2:** Qualitative judgment.
- **R3:** Sector-specific calibration.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Quantitative | None in OJ |
| R2 | Qualitative | None in OJ |
| R3 | Sector-specific | None in OJ |
S3.
*Berry anchor:* §5.1 (`significant`).
**Instance 2 — VAG — S3 — `disrupt, control or cause damage`**
Three adverse-effect types. The reading:
- **R1:** Disruption only.
- **R2:** Control only.
- **R3:** Damage only.
- **R4:** Any combination.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Disruption | In-Directive: literal |
| R2 | Control | In-Directive: literal |
| R3 | Damage | In-Directive: literal |
| R4 | Any | In-Directive: literal `or` |
R4 is the literal reading. S3.
*Berry anchor:* §5.4.7 (OR).
**Instance 3 — VAG — S2 — `intensity and ability`**
Two dimensions (intensity AND ability). The reading:
- **R1:** Both must be present.
- **R2:** Either suffices.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Both | In-Directive: literal `and` |
| R2 | Either | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §5.4.7 (AND).
**Instance 4 — VAG — S2 — `large number of other products`**
`large number` — quantified how?
- **R1:** Per Annex III category baseline.
- **R2:** Per Commission implementing acts.
- **R3:** Per market context.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Annex III | None in OJ |
| R2 | Commission IA | In-Directive: Art. 7(4) |
| R3 | Market context | None in OJ |
R2 is the dominant reading. S2.
*Berry anchor:* §5.1 (`large`).
---
#### 3.8 CRA-CL08–CL09 — Art. 7(3)–(4) — Commission delegated and implementing acts
(Summarised — full articles to be analysed in dedicated file; brief Layer 1 notes here for Art. 6–8 cohesion.)
**Instance 1 — VAG — S2 — `shall take into account the cybersecurity-related functionalities` (Art. 7(3))**
The Commission considers `cybersecurity-related functionalities or the function and the level of cybersecurity risk`. The reading:
- **R1:** Functional assessment.
- **R2:** Risk-based assessment.
- **R3:** Both.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Functional | In-Directive: literal |
| R2 | Risk-based | In-Directive: literal |
| R3 | Both | In-Directive: literal `and` |
R3 is the literal reading. S2.
**Instance 2 — VAG — S2 — `a minimum transitional period of 12 months`**
12-month minimum. Could be longer.
- **R1:** Exactly 12 months.
- **R2:** 12+ months.
- **R3:** Discretionary.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Exactly 12 | None in OJ |
| R2 | 12+ | In-Directive: literal `minimum … 12 months` |
| R3 | Discretionary | None in OJ |
R2 is the literal reading. S2.
**Instance 3 — VAG — S2 — `shall specify the technical description of the categories` (Art. 7(4))**
The Commission's implementing act specifies `technical description` — what level of detail?
- **R1:** Functional description.
- **R2:** Performance description.
- **R3:** Compliance description.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Functional | In-Directive: literal |
| R2 | Performance | None in OJ |
| R3 | Compliance | None in OJ |
R1 is the literal reading. S2.
---
#### 3.10 CRA-CL11 — Art. 8(2)(a)–(b) — Critical-product criteria
**Source locus:**
> **(a)** there is a **critical dependency of essential entities** as referred to in Article 3 of Directive (EU) 2022/2555 on the category of products with digital elements;
> **(b)** **incidents and exploited vulnerabilities** concerning the category of products with digital elements could lead to **serious disruptions of critical supply chains** across the internal market.
**Instance 1 — VAG — S3 — `critical dependency of essential entities`**
`critical` + `dependency` — both undefined in this context.
- **R1:** Operational dependency (the essential entity cannot operate without the product).
- **R2:** Functional dependency (the essential entity uses the product but has alternatives).
- **R3:** Sectoral dependency (the sector as a whole depends on the product).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Operational | In-Directive: literal `critical` |
| R2 | Functional | None in OJ |
| R3 | Sectoral | None in OJ |
R1 vs R2/R3 admit materially different compliance populations. S3.
*Berry anchor:* §3.3.1 (`critical dependency`).
**Instance 2 — VAG — S3 — `serious disruptions of critical supply chains`**
`serious` + `critical supply chains` — undefined.
- **R1:** Sector-wide disruption.
- **R2:** Multi-MS disruption.
- **R3:** Internal-market-wide disruption.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Sector | None in OJ |
| R2 | Multi-MS | None in OJ |
| R3 | Internal-market | In-Directive: literal `internal market` |
R3 is the literal reading. S3.
*Berry anchor:* §3.3.1 (`serious`, `critical supply chains`).
**Instance 3 — POLY — S2 — `incidents and exploited vulnerabilities`**
Two trigger categories (AND). The reading:
- **R1:** Both (incidents AND vulnerabilities).
- **R2:** Either (incidents OR vulnerabilities).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Both | In-Directive: literal `and` |
| R2 | Either | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §5.4.7 (AND).
---
#### 3.11 CRA-CL12 — Art. 8(1) sentence 3 (fallback) — Conformity-assessment fallback
**Source locus:**
> Where no delegated acts as referred to in the first subparagraph of this paragraph have been adopted, products with digital elements which have the core functionality of a product category as set out in Annex IV shall be subject to the conformity assessment procedures referred to in Article 32(3).
**Instance 1 — VAG — S2 — `Where no delegated acts … have been adopted`**
The fallback is conditional on absence of delegated acts. The reading:
- **R1:** Until any delegated act exists (regardless of content).
- **R2:** Only when no delegated act is applicable to the specific category.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Until any IA | In-Directive: literal `Where no delegated acts … have been adopted` |
| R2 | Only when not applicable | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §5.1 (`Where no`).
---
#### 3.12 CRA-CL13 — Art. 8(2) — Annex IV amendment
(Analysed in the synthesis as a delegation pattern.)
---
### 4. Cross-clause structural observations (Art. 6–8)
2. **Art. 7's two criteria (CL06, CL07) define important products.** The criteria are disjunctive (criterion A OR B). Three materially distinct readings admit materially different compliance populations. The Commission's 11 December 2025 implementing acts (CL09) will refine the criteria.
3. **Art. 8's certification requirement (CL10) is the most consequential single clause in this article.** Critical products require European cybersecurity certification at assurance level "substantial." As of mid-2025, **no European cybersecurity certification scheme has been adopted under the CSA that covers critical-product categories.** The fallback (CL12) routes products to Art. 32(3) conformity assessment (modules B+C or H).
   - Default (Art. 6): all products meet Annex I (essential requirements) — Annex I compliance route.
   - Important (Art. 7): Class I or Class II per Annex III — Art. 32(2)/(3) conformity assessment.
   - Critical (Art. 8): Annex IV — European cybersecurity certification at substantial level (or Art. 32(3) fallback).
   Each tier imposes progressively stricter conformity-assessment obligations.
5. **`core functionality` (CL04) is the single most consequential classification term.** The reading determines which products fall into Class I/II vs default. R1–R3 admit materially different compliance populations.
6. **Annex III/IV are flagged for Layer 2.** Their ambiguity is definitional regress ("core functionality of a product category") rather than Berry linguistic in the strict sense.
---
### 5. T2-to-v0.2 mapping
T2 had no clauses for Art. 6–8 — these articles were outside the T2 cybersecurity-taxonomy subset. The v0.2 expansion adds Art. 6–8 with 13 atomic clauses.
| T3 clause | T3 article | v0.2 clause | v0.2 article | Notes |
|---|---|---|---|---|
| (none) | — | CRA-CL01 | Art. 6(a) | T3 omitted; v0.2 adds. |
| (none) | — | CRA-CL02 | Art. 6(a) proviso | T3 omitted; v0.2 adds. |
| (none) | — | CRA-CL03 | Art. 6(b) | T3 omitted; v0.2 adds. |
| (none) | — | CRA-CL04 | Art. 7(1) sentence 1 | T3 omitted; v0.2 adds. |
| (none) | — | CRA-CL05 | Art. 7(1) sentence 2 | T3 omitted; v0.2 adds. |
| (none) | — | CRA-CL06 | Art. 7(2)(a) | T3 omitted; v0.2 adds. |
| (none) | — | CRA-CL07 | Art. 7(2)(b) | T3 omitted; v0.2 adds. |
| (none) | — | CRA-CL08 | Art. 7(3) | T3 omitted; v0.2 adds. |
| (none) | — | CRA-CL09 | Art. 7(4) | T3 omitted; v0.2 adds. |
| (none) | — | CRA-CL10 | Art. 8(1) | T3 omitted; v0.2 adds. |
| (none) | — | CRA-CL11 | Art. 8(2)(a)–(b) | T3 omitted; v0.2 adds. |
| (none) | — | CRA-CL12 | Art. 8(1) fallback | T3 omitted; v0.2 adds. |
| (none) | — | CRA-CL13 | Art. 8(2) | T3 omitted; v0.2 adds. |
---
**End of Art. 6–8 file. Next: `03_CRA_Art13_Manufacturers.md` (the heart of CRA).**
## CRA v0.2 — Annex I Essential Cybersecurity Requirements
> **Source.** OJ L, 20.11.2024, p. 68–69. `03_REFERENCE_MATERIAL/Regulatory_References/CRA.txt`, lines ~4153–4234.
>
> **Pattern.** Each Part quoted verbatim with highlighting, then per-clause analysis. Universal `[recital NN]` convention.
>
> **Annex I is the binding normative core of CRA.** Part I defines security properties for products; Part II defines vulnerability-handling obligations for manufacturers. These are referenced by Art. 6, 7, 8, 13, 27, 28, 32, and are the ultimate compliance target. 21 of the 26 T2 clauses lived in Annex I.
---
### 1. Annex I — full text

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/CRA.ambiguity.md

1. **Art. 6 is the essential-requirements gate.** The two-part structure (Part I for product properties; Part II for processes) mirrors GDPR's two-tier obligation (Art. 25 design + Art. 32 security). The installation-condition proviso (CL02) is CRA-unique and operationally consequential: a non-conforming product that is "properly installed" satisfies Art. 6(a).

### from regs/CRA.ambiguity.md

4. **The Art. 7/8/Alex III/IV architecture is a 3-tier classification** (analogous to AI Act's risk tiers):

<!-- aegis:purity: own_reg=CRA; demoted=2; core_cross_mentions=0 -->