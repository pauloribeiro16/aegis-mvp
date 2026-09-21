# D-09.2 — Relevant Ambiguity (CRA)

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
#### 3.2 CRA-CL15 — Art. 13(2) sentence 1 — Cybersecurity risk-assessment core duty
**Source locus:**
> For the purpose of complying with paragraph 1, manufacturers shall undertake an **assessment of the cybersecurity risks** associated with a product with digital elements …
**Instance 1 — VAG — S3 — `cybersecurity risks`**
Cross-references Art. 3(37) `cybersecurity risk`. The term's ambiguity propagates here.
- **R1:** Risks to the product (incoming threats).
- **R2:** Risks from the product (outgoing to users).
- **R3:** Both.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Incoming | None in OJ |
| R2 | Outgoing | In-Directive: Art. 13(2) `impact … including in relation to the health and safety of users` |
| R3 | Both | In-Directive: literal `associated with a product with digital elements` |
R3 is the literal reading. S3.
*Berry anchor:* §3.3.1 (`cybersecurity risks`).
**Instance 2 — POLY — S2 — `assessment`**
`assessment` — methodology?
- **R1:** Quantitative (FAIR, NIST 800-30).
- **R2:** Qualitative (heat-map).
- **R3:** Either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Quantitative | None in OJ |
| R2 | Qualitative | None in OJ |
| R3 | Either | In-Directive: literal `assessment` (no methodology specified) |
R3 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`assessment`).
---
#### 3.3 CRA-CL16 — Art. 13(2) sentence 1 — 6-phase lifecycle propagation
**Source locus:**
> …and take the outcome of that assessment into account during the **planning, design, development, production, delivery and maintenance phases** of the product with digital elements …
**Instance 1 — COORD — S3 — 6-phase coordination**
The 6-phase chain is the **longest single coordination pattern in CRA**. Six distinct lifecycle phases coordinated by AND. Three readings:
- **R1:** All six required.
- **R2:** Phases are illustrative (entity may organise differently).
- **R3:** The risk assessment applies to each phase but the obligation is to "take into account" the outcome.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | All six | In-Directive: literal `during the planning, design, development, production, delivery and maintenance phases` |
| R2 | Illustrative | None in OJ |
| R3 | Take-into-account | In-Directive: literal `take the outcome of that assessment into account` |
R1 is the literal reading. R3 admits partial compliance (some phases may not require full outcome-integration). R1 vs R3 produce materially distinct compliance populations. S3.
*Berry anchor:* §5.5 (six-way coordination); §5.1 (`take into account`).
**Instance 2 — POLY — S2 — `delivery`**
`delivery` — to distributor? to end-user? to installer?
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Distributor | None in OJ |
| R2 | End-user | None in OJ |
| R3 | Installer | None in OJ |
| R4 | Any | In-Directive: literal `delivery` |
R4 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`delivery`).
**Instance 3 — POLY — S2 — `maintenance`**
`maintenance` — post-market only? Includes security updates?
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Post-market only | None in OJ |
| R2 | Includes security updates | In-Directive: Art. 13(9) security updates |
| R3 | Both | In-Directive: literal `maintenance` |
R3 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`maintenance`).
---
#### 3.4 CRA-CL17 — Art. 13(2) sentence 2 — Health-and-safety of users
**Source locus:**
> …with a view to minimising cybersecurity risks, preventing incidents and minimising their impact, **including in relation to the health and safety of users**.
**Instance 1 — POLY — S2 — `health and safety`**
`health` + `safety` — two dimensions.
- **R1:** Health only (physical/psychological harm).
- **R2:** Safety only (physical danger).
- **R3:** Both.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Health | In-Directive: literal |
| R2 | Safety | In-Directive: literal |
| R3 | Both | In-Directive: literal `and` |
R3 is the literal reading. S2.
*Berry anchor:* §5.4.7 (AND).
**Instance 2 — SCOPE-Q — S2 — `users`**
`users` — natural persons only? Includes legal persons?
- **R1:** Natural persons (consumers + employees).
- **R2:** Legal persons (businesses).
- **R3:** Both.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Natural | In-Directive: Art. 3(18) `consumer` |
| R2 | Legal | None in OJ |
| R3 | Both | In-Directive: literal `users` (broader than `consumer`) |
R3 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`users`).
**Layer 1 observation** — The `health and safety of users` clause is CRA-unique (no other regulation in the corpus has it). It bridges cybersecurity to physical safety. Layer 2 must adjudicate whether software-compliance analysis must include physical-safety risk assessment (probably no, but the boundary is contested).
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
## CRA v0.2 — Annex I Essential Cybersecurity Requirements
> **Source.** OJ L, 20.11.2024, p. 68–69. `03_REFERENCE_MATERIAL/Regulatory_References/CRA.txt`, lines ~4153–4234.
>
> **Pattern.** Each Part quoted verbatim with highlighting, then per-clause analysis. Universal `[recital NN]` convention.
>
> **Annex I is the binding normative core of CRA.** Part I defines security properties for products; Part II defines vulnerability-handling obligations for manufacturers. These are referenced by Art. 6, 7, 8, 13, 27, 28, 32, and are the ultimate compliance target. 21 of the 26 T2 clauses lived in Annex I.
---
### 1. Annex I — full text
#### Part II — Vulnerability handling requirements
> Manufacturers of products with digital elements shall:
>
> **(1)** identify and document vulnerabilities and components contained in products with digital elements, including by drawing up a **software bill of materials** in a commonly used and machine-readable format covering at the very least the **top-level dependencies** of the products;
>
> **(2)** in relation to the risks posed to products with digital elements, **address and remediate vulnerabilities without delay**, including by providing security updates; where technically feasible, new security updates shall be provided **separately from functionality updates**;
>
> **(3)** apply **effective and regular tests and reviews** of the security of the product with digital elements;
>
> **(4)** once a security update has been made available, **share and publicly disclose** information about fixed vulnerabilities, including a description of the vulnerabilities, information allowing users to identify the product with digital elements affected, the impacts of the vulnerabilities, their severity and clear and accessible information helping users to remediate the vulnerabilities; in duly justified cases, where manufacturers consider the security risks of publication to outweigh the security benefits, they may **delay making public information** regarding a fixed vulnerability until after users have been given the possibility to apply the relevant patch;
>
> **(5)** put in place and enforce a **policy on coordinated vulnerability disclosure**;
>
> **(6)** take measures to **facilitate the sharing of information** about potential vulnerabilities in their product with digital elements as well as in third-party components contained in that product, including by providing a **contact address** for the reporting of the vulnerabilities discovered in the product with digital elements;
>
> **(7)** provide for mechanisms to **securely distribute updates** for products with digital elements to ensure that vulnerabilities are fixed or mitigated in a timely manner and, where applicable for security updates, in an automatic manner;
>
> **(8)** ensure that, where security updates are available to address identified security issues, they are **disseminated without delay** and, unless otherwise agreed between a manufacturer and a business user in relation to a tailor-made product with digital elements, **free of charge**, accompanied by advisory messages providing users with the relevant information, including on potential action to be taken.
---
### 2. Atomic clause map
| Clause ID | Locus | Type | Highest Sev. | Gist |
|---|---|---|---|---|
| CRA-CL129 | Ann. I Part I (1) | Chapeau | **S3** | Appropriate level of cybersecurity based on risks. |
| CRA-CL130 | Ann. I Part I (2)(a) | No known exploitable vulns | **S2** | No known exploitable vulnerabilities at market placement. |
| CRA-CL131 | Ann. I Part I (2)(b) | Secure by default | **S3** | Secure default configuration; reset-to-original-state. |
| CRA-CL132 | Ann. I Part I (2)(c) | Security updates | **S3** | Vulnerabilities addressed via security updates; auto-update default; opt-out. |
| CRA-CL133 | Ann. I Part I (2)(d) | Access control | **S3** | Protection from unauthorised access via authentication/IAM; report on access. |
| CRA-CL134 | Ann. I Part I (2)(e) | Confidentiality + encryption | **S3** | Protect confidentiality; encrypt at rest and in transit by state of the art. |
| CRA-CL135 | Ann. I Part I (2)(f) | Integrity | **S2** | Protect integrity of data/commands/configs; report on corruptions. |
| CRA-CL136 | Ann. I Part I (2)(g) | Data minimisation | **S3** | Process only data adequate, relevant, necessary for intended purpose. |
| CRA-CL137 | Ann. I Part I (2)(h) | Availability + DoS | **S3** | Protect availability of essential functions after incident; DoS resilience. |
| CRA-CL138 | Ann. I Part I (2)(i) | Cascading impact | **S2** | Minimise negative impact on other devices/networks. |
| CRA-CL139 | Ann. I Part I (2)(j) | Attack surfaces | **S2** | Limit attack surfaces including external interfaces. |
| CRA-CL140 | Ann. I Part I (2)(k) | Exploitation mitigation | **S2** | Reduce impact of incident via exploitation mitigation. |
| CRA-CL141 | Ann. I Part I (2)(l) | Logging + monitoring | **S3** | Record and monitor access/modification; opt-out for user. |
| CRA-CL142 | Ann. I Part I (2)(m) | Secure deletion | **S3** | User can securely and permanently remove all data/settings. |
| CRA-CL143 | Ann. II (1) | SBOM | **S3** | Identify/document vulnerabilities + components; SBOM in machine-readable format. |
| CRA-CL144 | Ann. II (2) | Vulnerability remediation | **S3** | Address/remediate without delay; security updates separated from functionality. |
| CRA-CL145 | Ann. II (3) | Security testing | **S3** | Effective and regular tests and reviews. |
| CRA-CL146 | Ann. II (4) | Public vulnerability disclosure | **S2** | Disclose fixed vulnerabilities; may delay if security risk outweighs benefit. |
| CRA-CL147 | Ann. II (5) | CVD policy | **S2** | Coordinated vulnerability disclosure policy. |
| CRA-CL148 | Ann. II (6) | Vulnerability sharing | **S2** | Facilitate sharing of potential vulnerabilities; provide contact address. |
| CRA-CL149 | Ann. II (7) | Secure update distribution | **S2** | Securely distribute updates; automatic if technically feasible. |
| CRA-CL150 | Ann. II (8) | Update dissemination | **S3** | Disseminate security updates without delay; free of charge (unless agreed). |
**Total: 22 atomic clauses for Annex I.**
---
### 3. Detailed cards
#### 3.1 CRA-CL129 — Part I (1) — Chapeau
**Source locus:**
> Products with digital elements shall be designed, developed and produced in such a way that they ensure an **appropriate level of cybersecurity based on the risks**.
**Instance 1 — VAG — S3 — `appropriate level of cybersecurity based on the risks`**
- **R1:** Quantitative risk threshold.
- **R2:** Qualitative risk judgment.
- **R3:** Sector-specific calibration.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Quantitative | None in OJ |
| R2 | Qualitative | In-Directive: Art. 13(2) risk assessment |
| R3 | Sector-specific | None in OJ |
S3.
*Berry anchor:* §5.1 (`appropriate level`, `based on the risks`).
**Instance 2 — COORD — S2 — `designed, developed and produced`**
Same 3-phase coordination as Art. 13(1) CRA-CL14. S2.
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

Same `appropriate` + `risks` double VAG as GDPR Art. 32(1) and NIS 2 Art. 21(1).

### from regs/CRA.ambiguity.md

**Layer 1 observation** — This is the CRA analog of NIS 2 Art. 21(1) opening and GDPR Art. 32(1) opening. The `appropriate level` qualifier propagates to all 13 sub-points of Part I (2)(a)–(m). Every sub-point inherits this VAG.

<!-- aegis:purity: own_reg=CRA; demoted=4; core_cross_mentions=0 -->

