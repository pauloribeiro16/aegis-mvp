# D-09.1 — Relevant Ambiguity (CRA)

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
#### 3.9 CRA-CL10 — Art. 8(1) sentence 1 — Critical-product certification requirement
**Source locus:**
> …products with digital elements that have the core functionality of a product category that is set out in Annex IV to this Regulation are to be required to obtain a **European cybersecurity certificate at assurance level at least 'substantial'** …
**Instance 1 — VAG — S3 — `European cybersecurity certificate`**
Cross-reference to Cybersecurity Act (Reg. 2019/881) Art. 49. The certification scheme must be adopted pursuant to the CSA and available to manufacturers. Inherits the CSA's ambiguities (certification-scheme availability is itself a moving target).
*Berry anchor:* §3.3.1 (`European cybersecurity certificate`).
**Instance 2 — VAG — S3 — `at least 'substantial'`**
The assurance level threshold. Three readings:
- **R1:** Level "substantial" is the minimum.
- **R2:** Level "substantial" is the default.
- **R3:** Higher levels may be required by delegated acts.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Substantial minimum | In-Directive: literal `at least` |
| R2 | Default | None in OJ |
| R3 | Higher per IA | In-Directive: Art. 8(1) specifying |
R1 is the literal reading; R3 is the delegated-acts reading. S3.
*Berry anchor:* §5.1 (`at least`).
**Instance 3 — SCOPE-Q — S2 — `provided that a European cybersecurity certification scheme covering those categories of products with digital elements has been adopted … and is available to manufacturers`**
Conditional on scheme availability.
- **R1:** Strict (scheme must be in OJ + applicable to that product category).
- **R2:** Liberal (scheme in any state of adoption suffices).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Strict | In-Directive: literal `has been adopted … and is available` |
| R2 | Liberal | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §5.1 (`provided that`).
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
## CRA v0.2 — Article 13 Obligations of Manufacturers (THE HEART)
---
### 1. Article 13 — full text (key paragraphs)
> **Article 13 — Obligations of manufacturers**
>
> **1.** When placing a product with digital elements on the market, manufacturers shall ensure that it has been designed, developed and produced in accordance with the essential cybersecurity requirements set out in Part I of Annex I.
> **2.** For the purpose of complying with paragraph 1, manufacturers shall undertake an assessment of the cybersecurity risks associated with a product with digital elements and take the outcome of that assessment into account during the **planning, design, development, production, delivery and maintenance phases** of the product with digital elements with a view to minimising cybersecurity risks, preventing incidents and minimising their impact, **including in relation to the health and safety of users**.
> **3.** The cybersecurity risk assessment shall be documented and updated as appropriate during a support period to be determined in accordance with paragraph 8 of this Article. That cybersecurity risk assessment shall comprise at least an analysis of cybersecurity risks based on the **intended purpose and reasonably foreseeable use, as well as the conditions of use, of the product with digital elements**, such as the operational environment or the assets to be protected, taking into account the length of time the product is expected to be in use. The cybersecurity risk assessment shall indicate whether and, if so in what manner, the security requirements set out in Part I, point (2), of Annex I are applicable to the relevant product with digital elements and how those requirements are implemented as informed by the cybersecurity risk assessment. It shall also indicate how the manufacturer is to apply Part I, point (1), of Annex I and the vulnerability handling requirements set out in Part II of Annex I.
> **4.** When placing a product with digital elements on the market, the manufacturer shall include the cybersecurity risk assessment referred to in paragraph 3 of this Article in the technical documentation required pursuant to Article 31 and Annex VII. …
> **5.** For the purpose of complying with paragraph 1, manufacturers shall **exercise due diligence when integrating components sourced from third parties** so that those components do not compromise the cybersecurity of the product with digital elements, including when integrating components of free and open-source software that have not been made available on the market in the course of a commercial activity.
> **6.** Manufacturers shall, upon identifying a vulnerability in a component, including in an open source-component, which is integrated in the product with digital elements report the vulnerability to the person or entity manufacturing or maintaining the component, and **address and remediate** the vulnerability in accordance with the vulnerability handling requirements set out in Part II of Annex I. …
> **7.** The manufacturers shall systematically document, in a manner that is proportionate to the nature and the cybersecurity risks, **relevant cybersecurity aspects** concerning the products with digital elements, including vulnerabilities of which they become aware and any relevant information provided by third parties, and shall, where applicable, update the cybersecurity risk assessment of the products.
> **8.** Manufacturers shall ensure, when placing a product with digital elements on the market, and for the support period, that vulnerabilities of that product, including its components, are handled effectively and in accordance with the essential cybersecurity requirements set out in Part II of Annex I.
>
> Manufacturers shall determine the support period so that it reflects the length of time during which the product is expected to be in use, taking into account, in particular, **reasonable user expectations, the nature of the product, including its intended purpose**, as well as **relevant Union law determining the lifetime** of products with digital elements. When determining the support period, manufacturers may also take into account the support periods of products with digital elements offering a similar functionality placed on the market by other manufacturers, the availability of the operating environment, the support periods of integrated components that provide core functions and are sourced from third parties as well as relevant guidance provided by the dedicated administrative cooperation group (ADCO) established pursuant to Article 52(15) and the Commission. **The matters to be taken into account in order to determine the support period shall be considered in a manner that ensures proportionality.**
>
> Without prejudice to the second subparagraph, the support period shall be **at least five years**. Where the product with digital elements is expected to be in use for less than five years, the support period shall correspond to the expected use time.
>
> …
>
> **9.** Manufacturers shall ensure that each security update, as referred to in Part II, point (8), of Annex I, which has been made available to users during the support period, **remains available after it has been issued for a minimum of 10 years or for the remainder of the support period, whichever is longer**.
> **10.** Where a manufacturer has placed subsequent substantially modified versions of a software product on the market, that manufacturer may ensure compliance with the essential cybersecurity requirement set out in Part II, point (2), of Annex I only for the version that it has last placed on the market, provided that theusers of the versions that were previously placed on the market have access to the version last placed on the market free of charge and do not incur additional costs to adjust the hardware and software environment in which they use the original version of that product.
> **11.** Manufacturers may maintain public software archives enhancing user access to historical versions. In those cases, users shall be clearly informed in an easily accessible manner about risks associated with using unsupported software.
> **12.** Before placing a product with digital elements on the market, manufacturers shall draw up the technical documentation referred to in Article 31. They shall carry out the chosen conformity assessment procedures as referred to in Article 32 or have them carried out. Where compliance … has been demonstrated by that conformity assessment procedure, manufacturers shall draw up the EU declaration of conformity in accordance with Article 28 and affix the CE marking in accordance with Article 30.
> **13.** Manufacturers shall **keep the technical documentation and the EU declaration of conformity at the disposal of the market surveillance authorities for at least 10 years** after the product with digital elements has been placed on the market or for the support period, whichever is longer.
> **14.** Manufacturers shall ensure that procedures are in place for products with digital elements that are part of a series of production to remain in conformity with this Regulation. …
> **15.** Manufacturers shall ensure that their products with digital elements bear a **type, batch or serial number or other element allowing their identification** …
> **16.** Manufacturers shall indicate the **name, registered trade name or registered trademark of the manufacturer, and the postal address, email address or other digital contact details**, as well as, where applicable, the website where the manufacturer can be contacted, on the product with digital elements …
> **17.** For the purposes of this Regulation, manufacturers shall designate a **single point of contact** to enable users to communicate directly and rapidly with them, including in order to facilitate reporting on vulnerabilities of the product with digital elements. …
> **18.** Manufacturers shall ensure that products with digital elements are accompanied by the **information and instructions to the user set out in Annex II**, in paper or electronic form. …
> **19.** Manufacturers shall ensure that the **end date of the support period** referred to in paragraph 8, including at least the month and the year, is clearly and understandably specified at the time of purchase …
> **20.** Manufacturers shall either provide a copy of the EU declaration of conformity or a **simplified EU declaration of conformity** with the product with digital elements. …
> **21.** From the placing on the market and for the support period, manufacturers who know or have reason to believe that the product with digital elements or the processes put in place by the manufacturer are not in conformity with the essential cybersecurity requirements set out in Annex I shall **immediately take the corrective measures** necessary to bring that product with digital elements or the manufacturer's processes into conformity, or to withdraw or recall the product, as appropriate.
> **22.** Manufacturers shall, upon a reasoned request from a market surveillance authority, provide that authority, in a language which can be easily understood by that authority, with all the information and documentation, in paper or electronic form, necessary to demonstrate the conformity …
> **23.** A manufacturer that ceases its operations and, as a result, is not able to comply with this Regulation shall inform, before the cessation of operations takes effect, the relevant market surveillance authorities as well as, by any means available and to the extent possible, the users of the relevant products with digital elements placed on the market, of the impending cessation of operations.
> **24.** The Commission may, by means of implementing acts taking into account European or international standards and best practices, specify the format and elements of the **software bill of materials** referred to in Part II, point (1), of Annex I. …
> **25.** In order to assess the dependence of Member States and of the Union as a whole on software components and in particular on components qualifying as free and open-source software, ADCO may decide to conduct a Union wide **dependency assessment** for specific categories of products with digital elements. …
---
### 2. Atomic clause map (Art. 13)
| Clause ID | Locus | Type | Highest Sev. | Gist |
|---|---|---|---|---|
| CRA-CL14 | Art. 13(1) (design/development/production duty) | Core obligation | **S2** | Designed, developed, produced per Annex I Part I. |
| CRA-CL15 | Art. 13(2) sentence 1 (risk-assessment duty) | Risk-assessment core | **S3** | Undertake cybersecurity risk assessment. |
| CRA-CL16 | Art. 13(2) sentence 1 (6-phase propagation) | Lifecycle | **S3** | Take outcome into account in 6 phases. |
| CRA-CL17 | Art. 13(2) sentence 2 (health/safety of users) | Health-and-safety | **S2** | Minimise impact including on users' health and safety. |
| CRA-CL18 | Art. 13(3) sentence 1 (risk assessment documented) | Documentation | **S3** | Document risk assessment; update during support period. |
| CRA-CL19 | Art. 13(3) sentence 2 (intended purpose + foreseeability) | Risk-assessment content | **S3** | Intended purpose + reasonably foreseeable use. |
| CRA-CL20 | Art. 13(3) sentence 3 (Annex I Part I(2) applicability) | Annex-I mapping | **S2** | Indicate which Annex I Part I(2) requirements apply. |
| CRA-CL21 | Art. 13(4) sentence 1 (technical-documentation inclusion) | Documentation | **S2** | Include risk assessment in technical documentation. |
| CRA-CL22 | Art. 13(4) sentence 2 (carve-out for AI products) | AI Act carve-out | **S2** | Risk assessment may be part of AI Act risk assessment. |
| CRA-CL23a | Art. 13(5) (due diligence on third-party components) | Supply-chain due-diligence | **S3** | Exercise due diligence when integrating third-party components. |
| CRA-CL24 | Art. 13(6) sentence 1 (vulnerability reporting + remediation) | Component-vulnerability handling | **S2** | Report + address + remediate component vulnerabilities. |
| CRA-CL25 | Art. 13(6) sentence 2 (sharing with component supplier) | Information sharing | **S2** | Share code/documentation with component supplier. |
| CRA-CL26 | Art. 13(7) (documentation duty) | Documentation | **S2** | Systematically document cybersecurity aspects. |
| CRA-CL27 | Art. 13(8) sentence 1 (vulnerability-handling during support) | Support-period obligation | **S3** | Handle vulnerabilities during support period. |
| CRA-CL28 | Art. 13(8) sentence 2 (support-period factors) | Support-period determination | **S3** | Factors: user expectations, nature, Union law, ADCO guidance. |
| CRA-CL29 | Art. 13(8) sentence 3 (5-year minimum) | Hard anchor | **S2** | Minimum 5-year support period (or expected use time). |
| CRA-CL30 | Art. 13(8) sentence 4 (delegated acts on support period) | Delegated acts | **S2** | Commission may specify minimum support period by category. |
| CRA-CL31 | Art. 13(8) sentence 5 (documentation of support period) | Documentation | **S2** | Include support-period factors in technical documentation. |
| CRA-CL32 | Art. 13(8) sentence 6 (CVD policy) | Policy | **S2** | Have appropriate policies including CVD. |
| CRA-CL33 | Art. 13(9) (10-year update-availability) | Hard anchor | **S2** | Security updates remain available for 10 years or remainder. |
| CRA-CL34 | Art. 13(10) (substantial modification — last-version compliance) | Substantial-modification scope | **S2** | May comply with Part II(2) only for last-placed version if conditions met. |
| CRA-CL35 | Art. 13(11) (public software archives) | Optional practice | **S2** | Maintain public archives; inform users of risks. |
| CRA-CL36 | Art. 13(12) sentence 1 (technical documentation + conformity) | Pre-market duty | **S2** | Draw up tech docs; carry out conformity assessment before placing on market. |
| CRA-CL37 | Art. 13(12) sentence 2 (EU declaration + CE marking) | Pre-market duty | **S2** | Draw up EU declaration; affix CE marking. |
| CRA-CL38 | Art. 13(13) (10-year documentation retention) | Retention | **S2** | Keep tech docs + EU declaration for 10 years or support period. |
| CRA-CL39 | Art. 13(14) (series-of-production compliance) | Series-production | **S2** | Procedures for series-production to remain in conformity. |
| CRA-CL40 | Art. 13(15) (identification) | Identification | **S2** | Type/batch/serial number or other element. |
| CRA-CL41 | Art. 13(16) (manufacturer contact info) | Contact info | **S2** | Name, trade name, address, email, website. |
| CRA-CL42 | Art. 13(17) (single point of contact) | Single point of contact | **S3** | Designate SPOC; allow non-automated means. |
| CRA-CL43 | Art. 13(18) (Annex II information and instructions) | User info | **S2** | Accompany with Annex II info; accessible for 10 years. |
| CRA-CL44 | Art. 13(19) (support-period end-date display) | Support-period transparency | **S2** | Display end date of support period at purchase; notify users at end. |
| CRA-CL45 | Art. 13(20) (EU declaration of conformity provision) | Declaration provision | **S2** | Provide full or simplified EU declaration. |
| CRA-CL46 | Art. 13(21) (corrective measures) | Corrective measures | **S2** | Immediately take corrective measures on non-conformity. |
| CRA-CL47 | Art. 13(22) (cooperation with MSAs) | Cooperation | **S2** | Provide info and documentation to MSAs on request. |
| CRA-CL48 | Art. 13(23) (cessation of operations notification) | Cessation | **S2** | Notify MSAs and users before ceasing operations. |
| CRA-CL49 | Art. 13(24) (SBOM implementing acts) | Commission implementing acts | **S2** | Commission may specify SBOM format. |
| CRA-CL50 | Art. 13(25) (Union-wide dependency assessment) | ADCO assessment | **S2** | ADCO may conduct dependency assessment on FOSS components. |
**Total: 36 atomic clauses for Art. 13 alone** (35 if CRA-CL23b is merged into CL23a; the v0.2 split per Q6=b places CRA-C24a on Art. 13(5)).
**Note on Q6=b (CRA-C24 split):** T2 CRA-C24 was mapped to Art. 13(5) but described the 10-year documentation retention (which is actually Art. 13(13)). Per Q6=b, v0.2 splits this:
- CRA-CL23a (this file) = Art. 13(5) **due-diligence on third-party components** (the OJ-literal mapping).
- CRA-CL38 (this file) = Art. 13(13) **10-year documentation retention** (the substance T2 misattributed).
---
### 3. Detailed cards
(Selected highlights — full analysis is below.)
#### 3.1 CRA-CL14 — Art. 13(1) — Design/development/production duty
**Source locus:**
> When placing a product with digital elements on the market, manufacturers shall ensure that it has been **designed, developed and produced** in accordance with the essential cybersecurity requirements set out in Part I of Annex I.
**Instance 1 — COORD — S2 — `designed AND developed AND produced`**
The 3-phase coordination. Three readings:
- **R1:** Three distinct phases (each must comply).
- **R2:** Composite description (one process).
- **R3:** Each independently required.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Distinct | In-Directive: literal `designed, developed and produced` |
| R2 | Composite | None in OJ |
| R3 | Independent | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §5.5 (three-way coordination).
**Instance 2 — POLY — S2 — `placing on the market`**
Inherits Art. 3(21) definition: `first making available of a product with digital elements on the Union market`. Same POLY as Art. 3(21) D21.
*Berry anchor:* §3.3.1 (`placing on the market`).
---
#### 3.12 CRA-CL28 — Art. 13(8) sentence 2 — Support-period factors
**Source locus:**
> Manufacturers shall determine the support period so that it reflects the length of time during which the product is expected to be in use, taking into account, in particular, **reasonable user expectations, the nature of the product, including its intended purpose**, as well as **relevant Union law determining the lifetime** of products with digital elements. When determining the support period, manufacturers may also take into account the support periods of products with digital elements offering a similar functionality placed on the market by other manufacturers, the availability of the operating environment, the support periods of integrated components that provide core functions and are sourced from third parties as well as relevant guidance provided by the dedicated administrative cooperation group (ADCO) … The matters to be taken into account in order to determine the support period shall be considered in a manner that ensures proportionality.
**Instance 1 — VAG — S3 — `reasonable user expectations`**
`reasonable user expectations` — case-law-laden term.
- **R1:** Subjective (what the specific user expects).
- **R2:** Objective (what a reasonable user in the sector expects).
- **R3:** Industry-standard.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Subjective | None in OJ |
| R2 | Objective | In-Directive: literal `reasonable` |
| R3 | Industry | None in OJ |
R2 is the literal reading. R1/R3 admit materially different compliance populations. S3.
*Berry anchor:* §5.1 (`reasonable`).
**Instance 2 — VAG — S2 — `nature of the product, including its intended purpose`**
`nature` — what dimension?
- **R1:** Technical (hardware vs software; consumer vs industrial).
- **R2:** Functional (purpose).
- **R3:** Both.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Technical | In-Directive: literal |
| R2 | Functional | In-Directive: literal `including its intended purpose` |
| R3 | Both | In-Directive: literal |
R3 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`nature`).
**Instance 3 — POLY — S2 — `relevant Union law determining the lifetime`**
Which Union laws?
- **R1:** Product-specific (e.g. automotive type-approval).
- **R2:** Sector-specific (e.g. medical-device lifetime rules).
- **R3:** All relevant.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Product | None in OJ |
| R2 | Sector | None in OJ |
| R3 | All | In-Directive: literal `relevant` |
R3 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`Union law`).
**Instance 4 — POLY — S2 — `ADCO guidance`**
ADCO = Administrative Cooperation Group per Art. 52(15). The guidance is non-binding but referenced.
*Berry anchor:* §3.3.1 (`ADCO`).
**Instance 5 — VAG — S3 — `in a manner that ensures proportionality`**
- **R1:** Quantitative (proportional to size/revenue).
- **R2:** Qualitative (proportional to risk).
- **R3:** Both.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Quantitative | In-Directive: Rec. 2003/361/EC size |
| R2 | Qualitative | None in OJ |
| R3 | Both | In-Directive: literal |
R3 is the literal reading. S3.
*Berry anchor:* §5.1 (`proportionality`).
---
#### 3.15 CRA-CL42 — Art. 13(17) — Single point of contact
**Source locus:**
> For the purposes of this Regulation, manufacturers shall designate a **single point of contact** to enable users to communicate directly and rapidly with them … The single point of contact shall allow users to **choose their preferred means of communication and shall not limit such means to automated tools**.
**Instance 1 — VAG — S3 — `single point of contact`**
`single` — one contact only? Single channel, multiple contacts?
- **R1:** Single contact (one email/phone/URL).
- **R2:** Single channel (one method, multiple addresses).
- **R3:** Functional role (a contact person or team, not necessarily a single address).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | One address | In-Directive: literal `single` |
| R2 | One channel | None in OJ |
| R3 | Functional role | None in OJ |
R1 vs R3 admit materially different compliance populations (R1 requires one email; R3 allows a team). S3.
*Berry anchor:* §3.3.1 (`single`).
**Instance 2 — VAG — S3 — `shall not limit such means to automated tools`**
The non-automation clause. Three readings:
- **R1:** At least one non-automated channel required.
- **R2:** No automated tools allowed.
- **R3:** Mixed (some automated, some not).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | At least one non-automated | In-Directive: literal `not limit … to automated tools` |
| R2 | No automated | None in OJ |
| R3 | Mixed | None in OJ |
R1 is the literal reading. R1 vs R3 admit materially different compliance populations. S3.
*Berry anchor:* §3.3.1 (`not limit … to automated tools`).
---
#### 3.6 CRA-CL58 — Art. 14(4)(a) — Early warning 24h (SI)
**Source locus:**
> **(a)** an early warning notification of a severe incident having an impact on the security of the product with digital elements, **without undue delay and in any event within 24 hours** of the manufacturer becoming aware of it, including at least whether the incident is suspected of being caused by unlawful or malicious acts, which shall also indicate, where applicable, the Member States on the territory of which the manufacturer is aware that their product with digital elements has been made available;
**Instance 1 — VAG — S3 — 24h twin-trigger**
Same pattern as CL53/CL54 at 24h. S3.
**Instance 2 — POLY — S2 — `unlawful or malicious acts`**
Hendiadys or distinct?
- **R1:** Hendiadys.
- **R2:** Distinct (unlawful = illegal; malicious = intentional harm).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Hendiadys | None in OJ |
| R2 | Distinct | In-Directive: literal `or` |
R2 is the literal reading. S2.
*Berry anchor:* §5.4.7 (OR).
---
#### 3.9 CRA-CL65 — Art. 14(8) sentence 1 — User notification
**Source locus:**
> After becoming aware of an actively exploited vulnerability or a severe incident having an impact on the security of the product with digital elements, the manufacturer shall inform the impacted users of the product with digital elements, and where appropriate all users, of that vulnerability or incident and, where necessary, of any risk mitigation and corrective measures that the users can deploy to mitigate the impact of that vulnerability or incident, where appropriate in **a structured, machine-readable format that is easily automatically processable**.
**Instance 1 — VAG — S3 — `impacted users`**
`impacted` — who is impacted?
- **R1:** Users of the affected product version.
- **R2:** All users of the product.
- **R3:** Users whose data is at risk.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Affected version | In-Directive: literal |
| R2 | All users | In-Directive: literal `where appropriate all users` |
| R3 | Data-at-risk | None in OJ |
R1 is the literal reading. R2 admits a broader population. S3.
*Berry anchor:* §3.3.1 (`impacted`).
**Instance 2 — VAG — S3 — `where appropriate in a structured, machine-readable format`**
`structured, machine-readable format` — which format?
- **R1:** JSON.
- **R2:** XML.
- **R3:** CSAF (Common Security Advisory Framework).
- **R4:** Any machine-readable format.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | JSON | None in OJ |
| R2 | XML | None in OJ |
| R3 | CSAF | None in OJ |
| R4 | Any | In-Directive: literal `machine-readable` |
R4 is the literal reading. S3.
*Berry anchor:* §3.3.1 (`structured, machine-readable format`).
**Instance 3 — VAG — S2 — `where appropriate`**
Soft hedge on format requirement.
- **R1:** Always (format is mandatory).
- **R2:** When the nature of the data allows.
- **R3:** Discretionary.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Always | None in OJ |
| R2 | Conditional | In-Directive: literal `where appropriate` |
| R3 | Discretionary | None in OJ |
R2 is the literal reading. S2.
*Berry anchor:* §5.1 (`where appropriate`).
---
### 4. Cross-clause structural observations (Art. 14)
6. **T3-vs-text gaps in Art. 14:** T3 had CRA-C25 (Art. 14(1) reporting) and CRA-C26 (Art. 14(3) reporting). The v0.2 expands these into 18 atomic clauses (CL51–CL68). T3's coverage was thin (2 clauses for 10 paragraphs). v0.2 captures the full article.
---
### 5. T3-to-v0.2 mapping
| T3 clause | T3 article | v0.2 clause | v0.2 article | Notes |
|---|---|---|---|---|
| CRA-C25 | Art. 14(1) | CRA-CL51, CL52, CL53, CL54, CL55 | Art. 14(1)–(2) | v0.2 splits AEV notification into 5 clauses (duty + platform + 3 tiers). |
| CRA-C26 | Art. 14(3) | CRA-CL56, CL57, CL58, CL59, CL60 | Art. 14(3)–(4) | v0.2 splits SI notification into 5 clauses (duty + platform + 3 tiers). |
| (none) | — | CRA-CL61, CL62 | Art. 14(5) | T3 omitted severe-incident definition; v0.2 adds 2 clauses. |
| (none) | — | CRA-CL63, CL64 | Art. 14(6)–(7) | T3 omitted intermediate report and routing; v0.2 adds. |
| (none) | — | CRA-CL65, CL66 | Art. 14(8) | T3 omitted user notification; v0.2 adds 2 clauses. |
| (none) | — | CRA-CL67, CL68 | Art. 14(9)–(10) | T3 omitted delegated/implementing acts; v0.2 adds. |
**Net: 2 T3 clauses → 18 v0.2 clauses (T3 missed 16 of the 18 Article 14 clauses).**
---
**End of Art. 14 file. Next: `05_CRA_Art15-17_OtherReporting.md`.**
#### 2.1 CRA-CL101 — Art. 24(1) — OSS steward cybersecurity policy
**Source locus:**
> Open-source software stewards shall put in place and document in a verifiable manner a cybersecurity policy to foster the development of a secure product with digital elements as well as an effective handling of vulnerabilities by the developers of that product. That policy shall also foster the voluntary reporting of vulnerabilities as laid down in Article 15 by the developers of that product and take into account the specific nature of the open-source software steward and the legal and organisational arrangements to which it is subject. That policy shall, in particular, include aspects related to documenting, addressing and remediating vulnerabilities and promote the sharing of information concerning discovered vulnerabilities within the open-source community.
**Instance 1 — VAG — S3 — `foster the development of a secure product`**
`foster` — encourage? require? enable?
- **R1:** Encourage (soft obligation).
- **R2:** Require (hard obligation).
- **R3:** Enable (provide means).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Encourage | In-Directive: literal `foster` |
| R2 | Require | None in OJ |
| R3 | Enable | None in OJ |
R1 is the literal reading. R2/R3 produce materially distinct compliance populations. S3.
*Berry anchor:* §3.3.1 (`foster`).
**Instance 2 — VAG — S3 — `document in a verifiable manner`**
`verifiable manner` — verified by whom?
- **R1:** Self-verification (internal audit).
- **R2:** Third-party verification.
- **R3:** MSA verification.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Self | None in OJ |
| R2 | Third-party | None in OJ |
| R3 | MSA | In-Directive: Art. 24(2) cooperation with MSAs |
R1 is the literal reading. S3.
*Berry anchor:* §3.3.1 (`verifiable manner`).
**Instance 3 — VAG — S2 — `effective handling of vulnerabilities`**
Same Berry POLY as Art. 3(20) `support period` definition. Remediation vs mitigation.
---
#### 2.2 CRA-CL103 — Art. 24(3) — OSS steward Art. 14 extension
**Source locus:**
> The obligations laid down in Article 14(1) shall apply to open-source software stewards **to the extent that they are involved in the development of the products with digital elements**. The obligations laid down in Article 14(3) and (8) shall apply to open-source software stewards to the extent that severe incidents having an impact on the security of products with digital elements affect network and information systems provided by the open-source software stewards for the development of such products.
**Instance 1 — VAG — S3 — `to the extent that they are involved in the development`**
`involved in the development` — how involved?
- **R1:** Commit access (direct code contribution).
- **R2:** Maintainer role (code review, merge).
- **R3:** Advisory role (guidance, policy).
- **R4:** Any involvement.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Commit | None in OJ |
| R2 | Maintainer | None in OJ |
| R3 | Advisory | None in OJ |
| R4 | Any | In-Directive: literal `involved` |
R4 is the literal reading. R1/R2/R3 admit materially different compliance populations. S3.
*Berry anchor:* §3.3.1 (`involved`).
**Instance 2 — SCOPE-Q — S2 — `affect network and information systems provided by the open-source software stewards`**
The Art. 14(3)/(8) extension applies only if the severe incident affects the steward's own NIS.
- **R1:** Steward's NIS only.
- **R2:** Any NIS used for the product's development.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Steward's | In-Directive: literal |
| R2 | Any | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`provided by`).
---
### 3. T3-to-v0.2 mapping
T3 had no clauses for Art. 24–26. The v0.2 expansion adds 7 atomic clauses (CL101–CL107).
---
**End of Art. 24–26 file. Next: `08_CRA_Art27-32_Conformity.md`.**
## CRA v0.2 — Articles 27–32 Conformity
> **Source.** OJ L, 20.11.2024, p. 46–50. `03_REFERENCE_MATERIAL/Regulatory_References/CRA.txt`, lines ~2878–3121.
>
> **Pattern.** Articles quoted in full, then per-clause analysis.
>
> **Articles 27–32 define the conformity machinery:** Art. 27 (presumption of conformity via harmonised standards/common specs/certification), Art. 28 (EU declaration), Art. 30 (CE marking), Art. 31 (technical documentation), Art. 32 (conformity assessment procedures — modules A/B+C/H).
---
### 1. Atomic clause map
| Clause ID | Locus | Type | Highest Sev. | Gist |
|---|---|---|---|---|
| CRA-CL108 | Art. 27(1) (presumption — harmonised standards) | Presumption | **S2** | Products conforming to harmonised standards are presumed compliant. |
| CRA-CL109 | Art. 27(2) (common specifications) | Common specs | **S2** | Commission may adopt implementing acts establishing common specifications. |
| CRA-CL110 | Art. 27(5) (common-specs presumption) | Presumption | **S2** | Products conforming to common specs are presumed compliant. |
| CRA-CL111 | Art. 27(8) (certification presumption) | Certification | **S2** | Products with EU statement/certificate under CSA presumed compliant. |
| CRA-CL112 | Art. 27(9) (delegated acts — certification schemes) | Delegated acts | **S2** | Commission specifies which CSA schemes demonstrate conformity. |
| CRA-CL113 | Art. 28(1) (EU declaration content) | Declaration | **S2** | EU declaration states fulfilment of Annex I requirements. |
| CRA-CL114 | Art. 28(2) (declaration format) | Format | **S2** | Declaration follows Annex V model; simplified follows Annex VI. |
| CRA-CL115 | Art. 28(3) (single declaration) | Single declaration | **S2** | Single EU declaration for products under multiple Union acts. |
| CRA-CL116 | Art. 28(4) (manufacturer responsibility) | Responsibility | **S2** | By drawing up declaration, manufacturer assumes responsibility for compliance. |
| CRA-CL117 | Art. 30(1) (CE marking affixing) | CE marking | **S2** | CE marking affixed visibly, legibly, indelibly; for software, on declaration or website. |
| CRA-CL118 | Art. 30(3) (CE marking timing) | Timing | **S2** | CE marking affixed before placing on market. |
| CRA-CL119 | Art. 30(6) (labels/pictograms) | Labels | **S2** | Commission may adopt implementing acts for labels/pictograms related to security. |
| CRA-CL120 | Art. 31(1) (technical documentation content) | Tech docs | **S2** | Tech docs contain all data/details demonstrating Annex I compliance; at least Annex VII. |
| CRA-CL121 | Art. 31(2) (tech docs timing) | Timing | **S2** | Tech docs drawn up before placing on market; updated during support period. |
| CRA-CL122 | Art. 31(3) (single tech docs) | Single docs | **S2** | Single tech doc set for products under multiple Union acts. |
| CRA-CL123 | Art. 32(1) (default conformity assessment) | Default CA | **S2** | Manufacturers choose module A, B+C, H, or certification. |
| CRA-CL124 | Art. 32(2) (Class I CA) | Class I CA | **S3** | Class I important products: module B+C or H (when harmonised standards not fully applied). |
| CRA-CL125 | Art. 32(3) (Class II CA) | Class II CA | **S3** | Class II important products: module B+C, H, or certification (substantial level). |
| CRA-CL126 | Art. 32(4) (critical products CA) | Critical CA | **S3** | Critical products: certification (Art. 8(1)) or module B+C/H fallback. |
| CRA-CL127 | Art. 32(5) (FOSS simplified CA) | FOSS CA | **S2** | FOSS in Annex III categories: module A if tech docs are public. |
| CRA-CL128 | Art. 32(6) (fee reduction for micro/small) | Fee reduction | **S2** | Fees reduced proportionately for micro/small enterprises. |
**Total: 21 atomic clauses for Art. 27–32.**
---
### 2. Detailed cards (selected)
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

### from regs/CRA.ambiguity.md

> **Source.** OJ L, 20.11.2024, p. 34–37. `03_REFERENCE_MATERIAL/Regulatory_References/CRA.txt`, lines ~2177–2370.
>
> **Pattern.** Article quoted in full (paragraph by paragraph), then per-clause analysis. Universal `[recital NN]` convention applied.
>
> **Article 13 is the operational core of CRA** — 25 paragraphs, ~35 atomic clauses. It is the analog of GDPR Art. 32 and NIS 2 Art. 21. It defines the 6-phase product-lifecycle obligations (planning, design, development, production, delivery, maintenance), the cybersecurity risk assessment, the due-diligence duty on third-party components, the support period, the technical documentation, and the corrective-measures duty.

### from regs/CRA.ambiguity.md

Proportionality principle. Same Berry `appropriate and proportionate` pattern as GDPR Art. 5(1)(c), NIS 2 Art. 21(1), DORA Art. 4.

### from regs/CRA.ambiguity.md

1. **Art. 14 has a dual-track architecture:** Track A = actively exploited vulnerabilities (¶1–2, 24h/72h/14d); Track B = severe incidents (¶3–4, 24h/72h/1m). The two tracks have identical temporal tiers but different clock starts (14d vs 1m). This is structurally parallel to GDPR Art. 33 (controller notification) vs Art. 34 (data-subject communication).

### from regs/CRA.ambiguity.md

2. **`severe incident` is the definitional regress.** Art. 14(5) defines it via `sensitive or important data or functions` (CL61) and `malicious code` (CL62). Both terms are undefined. Same pattern as NIS 2 Art. 23(3) `significant incident` and DORA Art. 18 `major ICT-related incident`.

### from regs/CRA.ambiguity.md

3. **`becomes aware of` (CL51, CL56) is the cross-regulation awareness-trigger pattern.** Same as NIS 2 Art. 23(4)(a)(b) and GDPR Art. 33(1). National implementations have begun diverging on when awareness attaches (R1 actual vs R2 constructive knowledge).

### from regs/CRA.ambiguity.md

4. **`simultaneously` (CL51, CL56) is CRA-unique.** No other regulation requires simultaneous notification to two bodies (CSIRT + ENISA). NIS 2 requires notification to the CSIRT only (or competent authority). GDPR requires notification to the supervisory authority only.

### from regs/CRA.ambiguity.md

5. **`structured, machine-readable format that is easily automatically processable` (CL65) is CRA-unique.** No other regulation in the corpus requires machine-readable user notification. NIS 2 Art. 23(4)(a)(b) uses the same temporal pattern but does not specify format.

<!-- aegis:purity: own_reg=CRA; demoted=9; core_cross_mentions=0 -->