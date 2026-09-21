# D-09.4 — Relevant Ambiguity (CRA)

> Part 4 ambiguity analysis for CRA, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## CRA
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
#### 3.5 CRA-CL18 — Art. 13(3) sentence 1 — Risk-assessment documentation
**Source locus:**
> The cybersecurity risk assessment shall be **documented and updated as appropriate during a support period** to be determined in accordance with paragraph 8 of this Article.
**Instance 1 — VAG — S2 — `documented`**
`documented` — written? digital? structured?
- **R1:** Written (paper or PDF).
- **R2:** Digital (in product or in management system).
- **R3:** Either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Written | In-Directive: Art. 13(4) `technical documentation` (paper or electronic) |
| R2 | Digital | None in OJ |
| R3 | Either | In-Directive: literal |
R3 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`documented`).
**Instance 2 — VAG — S2 — `updated as appropriate`**
`as appropriate` — soft hedge. When is updating appropriate?
- **R1:** Material change in product.
- **R2:** Material change in threat landscape.
- **R3:** Periodic (annual).
- **R4:** Any of the above.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Material change in product | In-Directive: Art. 13(7) update on becoming aware of vulnerability |
| R2 | Material change in threats | In-Directive: Art. 13(14) changes in harmonised standards |
| R3 | Periodic | None in OJ |
| R4 | Any | In-Directive: literal `as appropriate` |
R4 is the literal reading. S2.
*Berry anchor:* §5.1 (`as appropriate`).
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
#### 3.7 CRA-CL20 — Art. 13(3) sentence 3 — Annex I Part I(2) applicability
**Source locus:**
> The cybersecurity risk assessment shall indicate whether and, if so in what manner, the security requirements set out in Part I, point (2), of Annex I are applicable to the relevant product with digital elements and how those requirements are implemented as informed by the cybersecurity risk assessment.
**Instance 1 — VAG — S2 — `whether and, if so in what manner`**
Conditional + extension.
- **R1:** Apply some Part I(2) requirements (whichever apply).
- **R2:** Apply all Part I(2) requirements (uniformly).
- **R3:** Apply none (with justification).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Selective | In-Directive: literal `whether and, if so in what manner` |
| R2 | Uniform | None in OJ |
| R3 | None with justification | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §5.1 (`whether and, if so in what manner`).
---
#### 3.8 CRA-CL21–CL22 — Art. 13(4) — Technical documentation inclusion + AI carve-out
(Summarised — full analysis in dedicated file.)
**Instance 1 — VAG — S2 — `technical documentation required pursuant to Article 31 and Annex VII`**
Cross-reference. Inherits Art. 31 + Annex VII specifications.
*Berry anchor:* §3.3.1 (`technical documentation`).
**Instance 2 — POLY — S2 — `cybersecurity risk assessment may be part of the risk assessment required by those Union legal acts`**
- **R1:** Optional (entity choice).
- **R2:** Encouraged but not required.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Optional | In-Directive: literal `may` |
| R2 | Encouraged | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`may`).
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
#### 3.13 CRA-CL29 — Art. 13(8) sentence 3 — 5-year minimum support period
**Source locus:**
> Without prejudice to the second subparagraph, the support period shall be **at least five years**. Where the product with digital elements is expected to be in use for less than five years, the support period shall correspond to the expected use time.
**Instance 1 — VAG — S2 — `at least five years`**
Hard anchor (5 years) but with `at least` allowing extension.
- **R1:** Exactly 5 years.
- **R2:** 5+ years (depending on factors).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Exactly 5 | None in OJ |
| R2 | 5+ | In-Directive: literal `at least` |
R2 is the literal reading. S2.
*Berry anchor:* §5.7 (hard temporal anchor).
**Instance 2 — VAG — S2 — `expected to be in use`**
`expected` — by whom? Manufacturer? User? Regulators?
- **R1:** Manufacturer's expectation.
- **R2:** Reasonable user's expectation.
- **R3:** Industry-standard expectation.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Manufacturer | In-Directive: literal `expected to be in use` (manufacturer determines) |
| R2 | User | None in OJ |
| R3 | Industry | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`expected`).
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
#### 3.16 CRA-CL46 — Art. 13(21) — Corrective measures
**Source locus:**
> From the placing on the market and for the support period, manufacturers who know or have reason to believe that the product with digital elements or the processes put in place by the manufacturer are not in conformity with the essential cybersecurity requirements set out in Annex I shall **immediately take the corrective measures** necessary to bring that product with digital elements or the manufacturer's processes into conformity, or to withdraw or recall the product, as appropriate.
**Instance 1 — VAG — S2 — `immediately take`**
`immediately` — without delay? Same as `without undue delay`?
- **R1:** Without delay (any operational time).
- **R2:** Within 24h (same as Art. 14).
- **R3:** As soon as discovered.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Without delay | In-Directive: literal `immediately` |
| R2 | 24h | None in OJ |
| R3 | As soon as discovered | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`immediately`).
**Instance 2 — POLY — S2 — `corrective measures`**
What kind of measures?
- **R1:** Fix the product.
- **R2:** Update documentation.
- **R3:** Withdraw the product.
- **R4:** Recall the product.
- **R5:** Any combination.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Fix | In-Directive: literal `bring … into conformity` |
| R2 | Update docs | None in OJ |
| R3 | Withdraw | In-Directive: literal |
| R4 | Recall | In-Directive: literal |
| R5 | Any | In-Directive: literal `as appropriate` |
R5 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`corrective measures`); §5.4.7 (OR).
---
### 4. Cross-clause structural observations (Art. 13)
1. **Art. 13(2) is the operational core of the manufacturer's risk-assessment duty.** The 6-phase lifecycle propagation (CL16) is the **longest single coordination pattern in CRA** — 6 phases coordinated by AND. Berry §5.5 parallelism admits partial-compliance readings.
2. **Art. 13(8) is the support-period architecture.** Three layered obligations: (a) handle vulnerabilities during support (CL27), (b) determine support period based on factors (CL28), (c) minimum 5 years (CL29). Combined with Art. 13(9) 10-year update availability (CL33), the **effective manufacturer obligation is a 10-year tail** that survives the support period.
3. **Art. 13(5) is the supply-chain due-diligence hook (Q6=b split).** T2 misattributed this clause to Art. 13(13)'s 10-year documentation retention. The v0.2 split places the actual Art. 13(5) due-diligence analysis here (CL23a) and the 10-year retention in CL38.
5. **`reasonable user expectations` (CL28) is the cross-regulation Berry-classic.** Same term-pattern as `reasonable foreseeability` in Art. 3(24)/(25). Layer 1 catalogues; Layer 2 must adjudicate against product-liability case law.
6. **6 S3 clauses (CL15, CL16, CL18, CL19, CL23a, CL27, CL28, CL33, CL42):** risk assessment, 6-phase propagation, documentation, intended purpose + foreseeability, due diligence, support-period factors, 10-year updates, single point of contact. **No S1 instances.**
7. **The Q6=b split resolves the T2-C24 mapping error.** T2-C24's "10-year documentation" substance is actually Art. 13(13) (CL38), not Art. 13(5). T2-C24's "due diligence" substance (which it didn't capture) is actually Art. 13(5) (CL23a). The v0.2 split surfaces both clauses.
---
### 5. T3-to-v0.2 mapping
| T3 clause | T3 article | v0.2 clause | v0.2 article | Notes |
|---|---|---|---|---|
| CRA-C22 | Art. 13(1) | CRA-CL14 | Art. 13(1) | Same locus. |
| CRA-C22 (continued) | Art. 13(2) | CRA-CL15, CL16, CL17 | Art. 13(2) | v0.2 expands 6-phase + health/safety. |
| CRA-C23 | Art. 13(3)–(4) | CRA-CL18, CL19, CL20, CL21, CL22 | Art. 13(3)–(4) | v0.2 expands risk-assessment content. |
| **CRA-C24** | **Art. 13(5)** (T2 mis-attributed: it described Art. 13(13)) | **CRA-CL23a (Art. 13(5) due diligence) + CRA-CL38 (Art. 13(13) 10-year retention)** | Art. 13(5) and Art. 13(13) | **Per Q6=b: v0.2 splits T2-C24 mapping error into two clauses.** |
| (none) | — | CRA-CL24, CL25 | Art. 13(6) | T3 omitted; v0.2 adds. |
| (none) | — | CRA-CL26 | Art. 13(7) | T3 omitted; v0.2 adds. |
| (none) | — | CRA-CL27, CL28, CL29, CL30, CL31, CL32 | Art. 13(8) | T3 omitted; v0.2 expands into 6 atomic clauses. |
| (none) | — | CRA-CL33 | Art. 13(9) | T3 omitted; v0.2 adds. |
| (none) | — | CRA-CL34, CL35 | Art. 13(10), (11) | T3 omitted; v0.2 adds. |
| (none) | — | CRA-CL36, CL37 | Art. 13(12) | T3 omitted; v0.2 adds. |
| (T2 mis-attributed to 13(5)) | (T2 mis-attributed) | CRA-CL38 | Art. 13(13) | **Per Q6=b: substance migrated here from T2-C24.** |
| (none) | — | CRA-CL39–CL50 | Art. 13(14)–(25) | T3 omitted; v0.2 adds 12 clauses. |
**Net: 3 T3 clauses → 36 v0.2 clauses (T3 missed 33 of the 36 Article 13 clauses; 1 T3 mapping error resolved via Q6=b).**
---
**End of Art. 13 file. Pilot complete.**
- `05_CRA_Art15-17_OtherReporting.md`
- `06_CRA_Art18-23_EconomicOperators.md`
- `07_CRA_Art24-26_OSS.md`
- `08_CRA_Art27-32_Conformity.md`
- `09_CRA_AnnexI_EssentialRequirements.md` (the binding core)
- `10_CRA_AnnexII_Instructions.md`
- `11_CRA_AnnexVII_TechDocumentation.md`
- `12_CRA_AnnexVIII_ConformityModules.md`
- `99_CRA_Synthesis.md`
- Global `00_Index.md` update + legacy `../Regulation/CRA/Ambiguity/03_CRA.md` annotation
#### 3.3 CRA-CL54 — Art. 14(2)(b) — Vulnerability notification 72h (AEV)
**Source locus:**
> **(b)** unless the relevant information has already been provided, a vulnerability notification, **without undue delay and in any event within 72 hours** of the manufacturer becoming aware of the actively exploited vulnerability, which shall provide general information, as available, about the product with digital elements concerned, the general nature of the exploit and of the vulnerability concerned as well as any corrective or mitigating measures taken, and corrective or mitigating measures that users can take, and which shall also indicate, where applicable, how sensitive the manufacturer considers the notified information to be;
**Instance 1 — VAG — S3 — 72h twin-trigger**
Same pattern as CL53 at 72h. S3.
**Instance 2 — VAG — S2 — `unless the relevant information has already been provided`**
Conditional (avoids duplicate reporting).
- **R1:** Same information (technical duplicate).
- **R2:** Sufficient information (enough for CSIRT assessment).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Same | In-Directive: literal |
| R2 | Sufficient | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`relevant information`).
**Instance 3 — VAG — S2 — `how sensitive the manufacturer considers the notified information to be`**
Sensitivity assessment.
- **R1:** High sensitivity (restrict dissemination).
- **R2:** Low sensitivity (normal dissemination).
- **R3:** Discretionary.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | High | None in OJ |
| R2 | Low | None in OJ |
| R3 | Discretionary | In-Directive: literal `how sensitive` |
R3 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`sensitive`).
---
#### 3.4 CRA-CL55 — Art. 14(2)(c) — Final report 14 days (AEV)
**Source locus:**
> **(c)** unless the relevant information has already been provided, a final report, **not later than 14 days after a corrective or mitigating measure is available**, including at least the following:
> (i) a description of the vulnerability, including its severity and impact;
> (ii) where available, information concerning any malicious actor that has exploited or that is exploiting the vulnerability;
> (iii) details about the security update or other corrective measures that have been made available to remedy the vulnerability.
**Instance 1 — VAG — S2 — `14 days after a corrective or mitigating measure is available`**
Hard anchor (14 days) but the clock starts when the measure `is available`.
- **R1:** Measure is available = measure is released/published.
- **R2:** Measure is available = measure is distributed to users.
- **R3:** Measure is available = measure is installable.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Released | In-Directive: literal |
| R2 | Distributed | None in OJ |
| R3 | Installable | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`available`).
**Instance 2 — POLY — S2 — `corrective or mitigating measure`**
- **R1:** Corrective only (fix).
- **R2:** Mitigating only (workaround).
- **R3:** Either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Corrective | In-Directive: literal |
| R2 | Mitigating | In-Directive: literal |
| R3 | Either | In-Directive: literal `or` |
R3 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`corrective`/`mitigating`); §5.4.7 (OR).
**Instance 3 — VAG — S2 — `description of the vulnerability, including its severity and impact`**
*Berry anchor:* §5.1 (`severity and impact`).
---
#### 3.7 CRA-CL61 — Art. 14(5)(a) — Severe-incident test A
**Source locus:**
> **(a)** it **negatively affects or is capable of negatively affecting** the ability of a product with digital elements to protect the availability, authenticity, integrity or confidentiality of **sensitive or important data or functions**; or
**Instance 1 — VAG — S3 — `negatively affects or is capable of negatively affecting`**
- **R1:** Past only (already affected).
- **R2:** Potential only (capable of affecting).
- **R3:** Either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Past | In-Directive: literal |
| R2 | Potential | In-Directive: literal |
| R3 | Either | In-Directive: literal `or` |
R3 is the literal reading. S3.
*Berry anchor:* §5.4.7 (OR).
**Instance 2 — POLY — S2 — `sensitive or important data or functions`**
`data or functions` (same as Art. 3(44)) + `sensitive or important` (undefined qualifier).
- **R1:** `sensitive` = personal data.
- **R2:** `sensitive` = critical business data.
- **R3:** `sensitive` = any data whose loss has consequences.
- **R4:** `important` = essential to product function.
- **R5:** `important` = significant to user operations.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Personal data | None in OJ |
| R2 | Critical business | None in OJ |
| R3 | Consequential | None in OJ |
| R4 | Essential to product | None in OJ |
| R5 | Significant to user | None in OJ |
R5 is the broadest reading. S2.
*Berry anchor:* §3.3.1 (`sensitive`/`important`).
**Instance 3 — COORD — S3 — `sensitive OR important` (OR of two qualifiers)**
- **R1:** `sensitive` only.
- **R2:** `important` only.
- **R3:** Either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Sensitive | In-Directive: literal |
| R2 | Important | In-Directive: literal |
| R3 | Either | In-Directive: literal `or` |
R3 is the literal reading. S3.
*Berry anchor:* §5.4.7 (OR).
**Instance 4 — POLY — S2 — `availability, authenticity, integrity or confidentiality`**
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
#### 2.1 CRA-CL96 — Art. 21 — Manufacturer-equivalent trigger
**Source locus:**
> An importer or distributor shall be considered to be a manufacturer for the purposes of this Regulation and shall be subject to Articles 13 and 14, where that importer or distributor places a product with digital elements on the market **under its name or trademark** or carries out a **substantial modification** of a product with digital elements already placed on the market.
**Instance 1 — VAG — S3 — `under its name or trademark`**
`name or trademark` — what constitutes "under its name"?
- **R1:** Rebranding (white-label).
- **R2:** Co-branding.
- **R3:** Either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | White-label | In-Directive: literal |
| R2 | Co-brand | None in OJ |
| R3 | Either | In-Directive: literal `under its name or trademark` |
R3 is the literal reading. S3.
*Berry anchor:* §3.3.1 (`name or trademark`).
**Instance 2 — VAG — S3 — `substantial modification`**
Inherits Art. 3(30) D30. Same POLY (affects compliance / modifies intended purpose). Propagates.
- **R1:** Any non-compliance change.
- **R2:** Material compliance change.
- **R3:** Intended-purpose modification.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Any | In-Directive: Art. 3(30) literal |
| R2 | Material | None in OJ |
| R3 | Intended-purpose | In-Directive: Art. 3(30) OR |
R1/R3 are the literal reading (OR). S3.
*Berry anchor:* §3.3.1; §5.4.7 (OR).
---
#### 2.1 CRA-CL124 — Art. 32(2) — Class I conformity assessment
**Source locus:**
> Where, in assessing the compliance of an important product with digital elements that falls under class I as set out in Annex III and the processes put in place by its manufacturer with the essential cybersecurity requirements set out in Annex I, the manufacturer has not applied or has applied only in part harmonised standards, common specifications or European cybersecurity certification schemes at assurance level at least 'substantial' as referred to in Article 27, or where such harmonised standards, common specifications or European cybersecurity certification schemes do not exist, the product with digital elements concerned and the processes put in place by the manufacturer shall be submitted with regard to those essential cybersecurity requirements to either of the following procedures: (a) the EU-type examination procedure (based on module B) … followed by conformity to EU-type based on internal production control (based on module C) …; or (b) a conformity assessment based on full quality assurance (based on module H) ….
**Instance 1 — VAG — S3 — `has not applied or has applied only in part`**
The trigger for third-party assessment.
- **R1:** Not applied at all.
- **R2:** Applied only in part.
- **R3:** Either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Not at all | In-Directive: literal |
| R2 | Only in part | In-Directive: literal |
| R3 | Either | In-Directive: literal `or` |
R3 is the literal reading. S3.
*Berry anchor:* §3.3.1 (`applied only in part`).
**Instance 2 — POLY — S2 — `harmonised standards, common specifications or European cybersecurity certification schemes`**
Three alternative conformity routes (OR).
- **R1:** Harmonised standards only.
- **R2:** Common specifications only.
- **R3:** Certification schemes only.
- **R4:** Any combination.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Standards | In-Directive: Art. 27(1) |
| R2 | Common specs | In-Directive: Art. 27(2) |
| R3 | Certification | In-Directive: Art. 27(8) |
| R4 | Any | In-Directive: literal `or` |
R4 is the literal reading. S2.
*Berry anchor:* §5.4.7 (OR).
---
#### 2.2 CRA-CL125 — Art. 32(3) — Class II conformity assessment
**Source locus:**
> Where the product is an important product with digital elements that falls under class II as set out in Annex III, the manufacturer shall demonstrate conformity with the essential cybersecurity requirements set out in Annex I by using any of the following procedures: (a) EU-type examination procedure (based on module B) … followed by conformity to EU-type based on internal production control (based on module C) …; (b) a conformity assessment based on full quality assurance (based on module H) …; or (c) where available and applicable, a European cybersecurity certification scheme pursuant to Article 27(9) of this Regulation at assurance level at least 'substantial' ….
**Instance 1 — VAG — S3 — `at assurance level at least 'substantial'`**
The assurance-level threshold.
- **R1:** Level "substantial" is the minimum.
- **R2:** Higher levels may be required.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Substantial minimum | In-Directive: literal `at least` |
| R2 | Higher per Commission | In-Directive: Art. 27(9) delegated acts |
R1 is the literal reading. S3.
*Berry anchor:* §5.1 (`at least`).
---
#### 2.3 CRA-CL127 — Art. 32(5) — FOSS simplified conformity assessment
**Source locus:**
> Manufacturers of products with digital elements qualifying as free and open-source software, which fall under the categories set out in Annex III, shall be able to demonstrate conformity with the essential cybersecurity requirements set out in Annex I by using one of the procedures referred to in paragraph 1 of this Article, provided that the technical documentation referred to in Article 31 is made available to the public at the time of the placing on the market of those products.
**Instance 1 — VAG — S2 — `made available to the public`**
`to the public` — any public? or a specific public?
- **R1:** Any public access (website, repository).
- **R2:** MSA-accessible (on request).
- **R3:** Both.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Any public | In-Directive: literal |
| R2 | MSA | None in OJ |
| R3 | Both | In-Directive: literal |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`to the public`).
---
### 3. T3-to-v0.2 mapping
T3 had no clauses for Art. 27–32. The v0.2 expansion adds 21 atomic clauses (CL108–CL128).
---
**End of Art. 27–32 file. Next: `09_CRA_AnnexI_EssentialRequirements.md`.**
## CRA v0.2 — Annex I Essential Cybersecurity Requirements
> **Source.** OJ L, 20.11.2024, p. 68–69. `03_REFERENCE_MATERIAL/Regulatory_References/CRA.txt`, lines ~4153–4234.
>
> **Pattern.** Each Part quoted verbatim with highlighting, then per-clause analysis. Universal `[recital NN]` convention.
>
> **Annex I is the binding normative core of CRA.** Part I defines security properties for products; Part II defines vulnerability-handling obligations for manufacturers. These are referenced by Art. 6, 7, 8, 13, 27, 28, 32, and are the ultimate compliance target. 21 of the 26 T2 clauses lived in Annex I.
---
### 1. Annex I — full text
#### 3.7 CRA-CL143 — Part II (1) — SBOM
**Source locus:**
> identify and document vulnerabilities and components contained in products with digital elements, including by drawing up a **software bill of materials** in a commonly used and machine-readable format covering at the very least the **top-level dependencies** of the products;
**Instance 1 — VAG — S3 — `commonly used and machine-readable format`**
`commonly used` — which formats?
- **R1:** CycloneDX (OWASP).
- **R2:** SPDX (Linux Foundation).
- **R3:** Any machine-readable format.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | CycloneDX | None in OJ |
| R2 | SPDX | None in OJ |
| R3 | Any | In-Directive: literal `commonly used` |
R3 is the literal reading. S3 because R1 vs R3 admit materially different compliance populations.
*Berry anchor:* §3.3.1 (`commonly used`).
**Instance 2 — VAG — S2 — `top-level dependencies`**
`top-level` — shallow vs deep.
- **R1:** First-level dependencies only (direct).
- **R2:** Transitive (all nested).
- **R3:** Critical dependencies only.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | First-level | In-Directive: literal `top-level` |
| R2 | Transitive | None in OJ |
| R3 | Critical | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`top-level`).
---
#### 3.9 CRA-CL145 — Part II (3) — Security testing
**Source locus:**
> apply **effective and regular tests and reviews** of the security of the product with digital elements;
**Instance 1 — VAG — S3 — `effective and regular`**
Two qualifiers.
- **R1:** `effective` = test detects real vulnerabilities. `regular` = periodic.
- **R2:** `effective` = test is comprehensive. `regular` = ad-hoc.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Detect + periodic | None in OJ |
| R2 | Comprehensive + ad-hoc | None in OJ |
S3.
*Berry anchor:* §5.1 (`effective`, `regular`).
**Instance 2 — VAG — S2 — `tests and reviews`**
Two activities (AND).
- **R1:** Both (automated tests + manual reviews).
- **R2:** Either (automated tests OR manual reviews).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Both | In-Directive: literal `and` |
| R2 | Either | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §5.4.7 (AND).
---
## CRA v0.2 — Annex II Information and Instructions to the User
> **Source.** OJ L, 20.11.2024, p. 70. `03_REFERENCE_MATERIAL/Regulatory_References/CRA.txt`, lines ~4240–4275.
>
> **Pattern.** Each point quoted verbatim, then per-clause analysis.
---
### 1. Annex II — full text
> At minimum, the product with digital elements shall be accompanied by:
>
> **1.** the name, registered trade name or registered trademark of the manufacturer, and the postal address, the email address or other digital contact as well as, where available, the website at which the manufacturer can be contacted;
>
> **2.** the single point of contact where information about vulnerabilities of the product with digital elements can be reported and received, and where the manufacturer's policy on coordinated vulnerability disclosure can be found;
>
> **3.** name and type and any additional information enabling the unique identification of the product with digital elements;
>
> **4.** the intended purpose of the product with digital elements, including the security environment provided by the manufacturer, as well as the product's essential functionalities and information about the security properties;
>
> **5.** any known or foreseeable circumstance, related to the use of the product with digital elements in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, which may lead to significant cybersecurity risks;
>
> **6.** where applicable, the internet address at which the EU declaration of conformity can be accessed;
>
> **7.** the type of technical security support offered by the manufacturer and the end-date of the support period during which users can expect vulnerabilities to be handled and to receive security updates;
>
> **8.** detailed instructions or an internet address referring to such detailed instructions and information on:
> **(a)** the necessary measures during initial commissioning and throughout the lifetime of the product with digital elements to ensure its secure use;
> **(b)** how changes to the product with digital elements can affect the security of data;
> **(c)** how security-relevant updates can be installed;
> **(d)** the secure decommissioning of the product with digital elements, including information on how user data can be securely removed;
> **(e)** how the default setting enabling the automatic installation of security updates, as required by Part I, point (2)(c), of Annex I, can be turned off;
> **(f)** where the product with digital elements is intended for integration into other products with digital elements, the information necessary for the integrator to comply with the essential cybersecurity requirements set out in Annex I and the documentation requirements set out in Annex VII.
>
> **9.** If the manufacturer decides to make available the software bill of materials to the user, information on where the software bill of materials can be accessed.
---
### 2. Atomic clause map
| Clause ID | Locus | Type | Highest Sev. | Gist |
|---|---|---|---|---|
| CRA-CL151 | Ann. II §1 (manufacturer contact) | Contact info | **S2** | Name, address, email, website. |
| CRA-CL152 | Ann. II §2 (SPOC + CVD) | SPOC + CVD | **S2** | Single point of contact; CVD policy location. |
| CRA-CL153 | Ann. II §3 (product identification) | Identification | **S2** | Name, type, unique identification. |
| CRA-CL154 | Ann. II §4 (intended purpose + security) | Purpose + security | **S3** | Intended purpose, security environment, functionalities, security properties. |
| CRA-CL155 | Ann. II §5 (foreseeable risks) | Foreseeable risks | **S2** | Known/foreseeable circumstances leading to significant cybersecurity risks. |
| CRA-CL156 | Ann. II §6 (EU declaration) | Declaration | **S2** | Internet address for EU declaration. |
| CRA-CL157 | Ann. II §7 (support period) | Support period | **S2** | Technical security support type; end-date of support period. |
| CRA-CL158 | Ann. II §8 (instructions) | Instructions | **S2** | Detailed instructions for secure use, data changes, updates, decommissioning, auto-update opt-out, integration. |
| CRA-CL159 | Ann. II §9 (SBOM) | SBOM | **S2** | Where SBOM can be accessed (if manufacturer decides). |
**Total: 9 atomic clauses for Annex II.**
---
### 3. Detailed cards (selected)
#### 3.1 CRA-CL154 — Ann. II §4 — Intended purpose + security properties
**Source locus:**
> the intended purpose of the product with digital elements, including the security environment provided by the manufacturer, as well as the product's essential functionalities and information about the security properties;
**Instance 1 — VAG — S2 — `security environment`**
`security environment` — what constitutes the security environment?
- **R1:** Threat model.
- **R2:** Trust boundaries.
- **R3:** Both.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Threat model | None in OJ |
| R2 | Trust boundaries | None in OJ |
| R3 | Both | In-Directive: literal `security environment` |
R3 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`security environment`).
**Instance 2 — VAG — S2 — `security properties`**
`security properties` — which properties?
- **R1:** Confidentiality, integrity, availability (CIA).
- **R2:** Authentication, authorisation, non-repudiation (AAN).
- **R3:** Any security property.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | CIA | None in OJ |
| R2 | AAN | None in OJ |
| R3 | Any | In-Directive: literal `security properties` |
R3 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`security properties`).
---
#### 3.2 CRA-CL155 — Ann. II §5 — Foreseeable risks
**Source locus:**
> any known or foreseeable circumstance, related to the use of the product with digital elements in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, which may lead to significant cybersecurity risks;
**Instance 1 — VAG — S2 — `known or foreseeable`**
Two qualifiers (OR).
- **R1:** Known only.
- **R2:** Foreseeable only.
- **R3:** Either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Known | In-Directive: literal |
| R2 | Foreseeable | In-Directive: literal |
| R3 | Either | In-Directive: literal `or` |
R3 is the literal reading. S2.
*Berry anchor:* §5.4.7 (OR).
**Instance 2 — POLY — S2 — `reasonably foreseeable misuse`**
Inherits Art. 3(25) D25. Same case-law-laden term.
*Berry anchor:* §3.3.1.
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
## CRA v0.2 — Annex VII Content of the Technical Documentation
> **Source.** OJ L, 20.11.2024, p. 75. `03_REFERENCE_MATERIAL/Regulatory_References/CRA.txt`, lines ~4379–4420.
>
> **Pattern.** Each point quoted verbatim, then per-clause analysis.
---
### 1. Annex VII — full text
> The technical documentation referred to in Article 31 shall contain at least the following information, as applicable to the relevant product with digital elements:
>
> **1.** a general description of the product with digital elements, including: (a) its intended purpose; (b) versions of software affecting compliance with essential cybersecurity requirements; (c) where the product with digital elements is a hardware product, photographs or illustrations showing external features, marking and internal layout; (d) user information and instructions as set out in Annex II;
>
> **2.** a description of the design, development and production of the product with digital elements and vulnerability handling processes, including: (a) necessary information on the design and development of the product with digital elements, including, where applicable, drawings and schemes and a description of the system architecture explaining how software components build on or feed into each other and integrate into the overall processing; (b) necessary information and specifications of the vulnerability handling processes put in place by the manufacturer, including the software bill of materials, the coordinated vulnerability disclosure policy, evidence of the provision of a contact address for the reporting of the vulnerabilities and a description of the technical solutions chosen for the secure distribution of updates; (c) necessary information and specifications of the production and monitoring processes of the product with digital elements and the validation of those processes;
>
> **3.** an assessment of the cybersecurity risks against which the product with digital elements is designed, developed, produced, delivered and maintained pursuant to Article 13, including how the essential cybersecurity requirements set out in Part I of Annex I are applicable;
>
> **4.** relevant information that was taken into account to determine the support period pursuant to Article 13(8) of the product with digital elements;
>
> **5.** a list of the harmonised standards applied in full or in part … or common specifications … or European cybersecurity certification schemes … and, where those … have not been applied, descriptions of the solutions adopted to meet the essential cybersecurity requirements set out in Parts I and II of Annex I, including a list of other relevant technical specifications applied;
>
> **6.** reports of the tests carried out to verify the conformity of the product with digital elements and of the vulnerability handling processes with the applicable essential cybersecurity requirements as set out in Parts I and II of Annex I;
>
> **7.** a copy of the EU declaration of conformity;
>
> **8.** where applicable, the software bill of materials, further to a reasoned request from a market surveillance authority provided that it is necessary in order for that authority to be able to check compliance with the essential cybersecurity requirements set out in Annex I.
---
### 2. Atomic clause map
| Clause ID | Locus | Type | Highest Sev. | Gist |
|---|---|---|---|---|
| CRA-CL160 | Ann. VII §1 (general description) | Documentation | **S2** | Product description: purpose, SW versions, hardware features, Annex II user info. |
| CRA-CL161 | Ann. VII §2 (design + vuln handling) | Documentation | **S3** | Design/dev/production description: architecture, vuln handling processes, SBOM, CVD, update distribution. |
| CRA-CL162 | Ann. VII §3 (risk assessment) | Documentation | **S3** | Cybersecurity risk assessment per Art. 13; Annex I applicability mapping. |
| CRA-CL163 | Ann. VII §4 (support period info) | Documentation | **S2** | Support-period determination factors. |
| CRA-CL164 | Ann. VII §5 (standards + alternatives) | Documentation | **S2** | Standards applied; alternatives where not applied. |
| CRA-CL165 | Ann. VII §6 (test reports) | Documentation | **S2** | Test reports for Annex I Part I + Part II compliance. |
| CRA-CL166 | Ann. VII §7 (EU declaration copy) | Documentation | **S2** | Copy of EU declaration of conformity. |
| CRA-CL167 | Ann. VII §8 (SBOM on request) | Documentation | **S2** | SBOM provided on MSA request. |
**Total: 8 atomic clauses for Annex VII.**
---
### 3. Selected instance
#### CRA-CL161 — Ann. VII §2(a) — System architecture
**Source locus:**
> a description of the system architecture explaining how software components build on or feed into each other and integrate into the overall processing;
**Instance 1 — VAG — S2 — `build on or feed into each other`**
Architectural description depth.
- **R1:** Component dependency graph.
- **R2:** Data flow diagram.
- **R3:** Both.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Dependency | In-Directive: literal `build on` |
| R2 | Data flow | In-Directive: literal `feed into` |
| R3 | Both | In-Directive: literal `or` |
R3 is the literal reading. S2.
---
**End of Annex VII file. Next: `12_CRA_AnnexVIII_ConformityModules.md`.**
## CRA v0.2 — Annex VIII Conformity Assessment Procedures
> **Source.** OJ L, 20.11.2024, p. 75–80. `03_REFERENCE_MATERIAL/Regulatory_References/CRA.txt`, lines ~4426–4769.
>
> **Pattern.** Key clauses quoted, then per-clause analysis.
>
> **Annex VIII defines three conformity-assessment modules:** Module A (internal control), Module B+C (EU-type examination + internal production control), Module H (full quality assurance). Art. 32 routes products to modules based on classification.
---
### 1. Module architecture
| Module | Part | Name | Role |
|---|---|---|---|
| **A** | I | Internal control | Manufacturer self-assessment. |
| **B** | II | EU-type examination | Notified body examines design + vuln handling. |
| **C** | III | Internal production control | Manufacturer controls production per EU-type. |
| **B+C** | II + III | EU-type + production control | Notified body examines design; manufacturer controls production. |
| **H** | IV | Full quality assurance | Notified body audits QMS. |
---
### 2. Atomic clause map
| Clause ID | Locus | Type | Highest Sev. | Gist |
|---|---|---|---|---|
| CRA-CL168 | Ann. VIII Part I (1) | Module A duty | **S2** | Manufacturer self-declares compliance; sole responsibility. |
| CRA-CL169 | Ann. VIII Part I (2) | Tech docs (Module A) | **S2** | Draw up Annex VII documentation. |
| CRA-CL170 | Ann. VIII Part I (3) | Design/production/vuln (Module A) | **S2** | Manufacturer takes all measures for design/dev/production/vuln compliance. |
| CRA-CL171 | Ann. VIII Part II (1) | Module B definition | **S2** | Notified body examines design + vuln handling; attests compliance. |
| CRA-CL172 | Ann. VIII Part II (3) | Module B application | **S2** | Application to single notified body. |
| CRA-CL173 | Ann. VIII Part II (6) | EU-type certificate | **S2** | Notified body issues certificate; may refuse and inform. |
| CRA-CL174 | Ann. VIII Part II (8) | Module B periodic audits | **S2** | Periodic audits of vuln handling processes. |
| CRA-CL175 | Ann. VIII Part III (1) | Module C definition | **S2** | Manufacturer controls production per EU-type. |
| CRA-CL176 | Ann. VIII Part IV (1) | Module H definition | **S2** | Full quality assurance; notified body audits QMS. |
**Total: 9 atomic clauses for Annex VIII.**
---
### 3. Selected instance
#### CRA-CL173 — Ann. VIII Part II (6) — EU-type certificate
**Source locus:**
> Where the type and the vulnerability handling processes meet the essential cybersecurity requirements set out in Annex I, the notified body shall issue an EU-type examination certificate to the manufacturer. The certificate shall contain the name and address of the manufacturer, the conclusions of the examination, the conditions (if any) for its validity and the necessary data for identification of the approved type and vulnerability handling processes. The certificate may have one or more annexes attached. … Where the type and the vulnerability handling processes do not satisfy the applicable essential cybersecurity requirements set out in Annex I, the notified body shall refuse to issue an EU-type examination certificate and shall inform the applicant accordingly, giving detailed reasons for its refusal.
**Instance 1 — VAG — S2 — `conditions (if any) for its validity`**
`conditions` — what conditions?
- **R1:** Periodic review conditions.
- **R2:** Change-management conditions.
- **R3:** Both.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Periodic review | None in OJ |
| R2 | Change-management | In-Directive: Ann. VIII Part II (7) modifications |
| R3 | Both | None in OJ |
R2 is the dominant reading (Part II (7) covers modifications). S2.
---
### 4. T3-to-v0.2 mapping
T3 had no clauses for Annex VIII. The v0.2 expansion adds 9 atomic clauses (CL168–CL176).
---
**End of Annex VIII file. Next: `99_CRA_Synthesis.md`.**

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/CRA.ambiguity.md

> **Source.** OJ L, 20.11.2024, p. 34–37. `03_REFERENCE_MATERIAL/Regulatory_References/CRA.txt`, lines ~2177–2370.
>
> **Pattern.** Article quoted in full (paragraph by paragraph), then per-clause analysis. Universal `[recital NN]` convention applied.
>
> **Article 13 is the operational core of CRA** — 25 paragraphs, ~35 atomic clauses. It is the analog of GDPR Art. 32 and NIS 2 Art. 21. It defines the 6-phase product-lifecycle obligations (planning, design, development, production, delivery, maintenance), the cybersecurity risk assessment, the due-diligence duty on third-party components, the support period, the technical documentation, and the corrective-measures duty.

### from regs/CRA.ambiguity.md

The AI Act carve-out: risk assessment can be unified across CRA + AI Act.

### from regs/CRA.ambiguity.md

Proportionality principle. Same Berry `appropriate and proportionate` pattern as GDPR Art. 5(1)(c), NIS 2 Art. 21(1), DORA Art. 4.

### from regs/CRA.ambiguity.md

4. **Art. 13(2) sentence 2 is CRA-unique.** The `health and safety of users` clause bridges cybersecurity to physical safety. No other regulation in the corpus (GDPR, NIS 2, DORA, AI Act) has this.

### from regs/CRA.ambiguity.md

Per the NIS 2 pattern, pausing here for your review before continuing with:

### from regs/CRA.ambiguity.md

- `04_CRA_Art14_Reporting.md` (the "Art. 23 NIS 2" analog)

### from regs/CRA.ambiguity.md

Same as NIS 2 Art. 23(4)(d)(iii) `applied and ongoing mitigation measures`. OR.

### from regs/CRA.ambiguity.md

Same as NIS 2 Art. 23(4)(d)(i) `detailed description`.

### from regs/CRA.ambiguity.md

Same pattern as NIS 2 Art. 23(3) `caused or is capable of causing`. Actual vs potential.

### from regs/CRA.ambiguity.md

Same four dimensions as NIS 2 Art. 6(2) D02. Inherits same POLY (authenticity undefined).

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

<!-- aegis:purity: own_reg=CRA; demoted=15; core_cross_mentions=0 -->

