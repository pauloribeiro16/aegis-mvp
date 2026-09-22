# D-04.3 — Relevant Ambiguity (CRA)

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
## CRA v0.2 — Article 14 Reporting Obligations of Manufacturers
---
### 1. Article 14 — full text
> **Article 14 — Reporting obligations of manufacturers**
>
> **1.** A manufacturer shall notify any actively exploited vulnerability contained in the product with digital elements that it becomes aware of simultaneously to the CSIRT designated as coordinator, in accordance with paragraph 7 of this Article, and to ENISA. The manufacturer shall notify that actively exploited vulnerability via the single reporting platform established pursuant to Article 16.
>
> **2.** For the purposes of the notification referred to in paragraph 1, the manufacturer shall submit:
>
> **(a)** an early warning notification of an actively exploited vulnerability, **<mark>without undue delay and in any event within 24 hours</mark>** of the manufacturer becoming aware of it, indicating, where applicable, the Member States on the territory of which the manufacturer is aware that their product with digital elements has been made available;
>
> **(b)** unless the relevant information has already been provided, a vulnerability notification, **without undue delay and in any event within 72 hours** of the manufacturer becoming aware of the actively exploited vulnerability, which shall provide general information, as available, about the product with digital elements concerned, the general nature of the exploit and of the vulnerability concerned as well as any corrective or mitigating measures taken, and corrective or mitigating measures that users can take, and which shall also indicate, where applicable, how sensitive the manufacturer considers the notified information to be;
>
> **(c)** unless the relevant information has already been provided, a final report, **not later than 14 days after a corrective or mitigating measure is available**, including at least the following:
>
> (i) a description of the vulnerability, including its severity and impact;
>
> (ii) where available, information concerning any malicious actor that has exploited or that is exploiting the vulnerability;
>
> (iii) details about the security update or other corrective measures that have been made available to remedy the vulnerability.
>
> **3.** A manufacturer shall notify any **severe incident having an impact on the security of the product with digital elements** that it becomes aware of simultaneously to the CSIRT designated as coordinator, in accordance with paragraph 7 of this Article, and to ENISA. The manufacturer shall notify that incident via the single reporting platform established pursuant to Article 16.
>
> **4.** For the purposes of the notification referred to in paragraph 3, the manufacturer shall submit:
>
> **(a)** an early warning notification of a severe incident having an impact on the security of the product with digital elements, **without undue delay and in any event within 24 hours** of the manufacturer becoming aware of it, including at least whether the incident is suspected of being caused by unlawful or malicious acts, which shall also indicate, where applicable, the Member States on the territory of which the manufacturer is aware that their product with digital elements has been made available;
>
> **(b)** unless the relevant information has already been provided, an incident notification, **without undue delay and in any event within 72 hours** of the manufacturer becoming aware of the incident, which shall provide general information, where available, about the nature of the incident, an initial assessment of the incident, as well as any corrective or mitigating measures taken, and corrective or mitigating measures that users can take, and which shall also indicate, where applicable, how sensitive the manufacturer considers the notified information to be;
>
> **(c)** unless the relevant information has already been provided, a final report, **within one month** after the submission of the incident notification under point (b), including at least the following:
>
> (i) a detailed description of the incident, including its severity and impact;
>
> (ii) the type of threat or root cause that is likely to have triggered the incident;
>
> (iii) applied and ongoing mitigation measures.
>
> **5.** For the purposes of paragraph 3, an incident having an impact on the security of the product with digital elements **shall be considered to be severe** where:
>
> **(a)** it **negatively affects or is capable of negatively affecting** the ability of a product with digital elements to protect the availability, authenticity, integrity or confidentiality of **sensitive or important data or functions**; or
>
> **(b)** it has **led or is capable of leading** to the introduction or execution of **malicious code** in a product with digital elements or in the network and information systems of a user of the product with digital elements.
>
> **6.** Where necessary, the CSIRT designated as coordinator initially receiving the notification may request manufacturers to provide an intermediate report on relevant status updates about the actively exploited vulnerability or severe incident having an impact on the security of the product with digital elements.
>
> **7.** The notifications referred to in paragraphs 1 and 3 of this Article shall be submitted via the single reporting platform referred to in Article 16 using one of the electronic notification end-points referred to in Article 16(1). The notification shall be submitted using the electronic notification end-point of the CSIRT designated as coordinator of the Member State where the manufacturers have their main establishment in the Union and shall be simultaneously accessible to ENISA. …
>
> **8.** After becoming aware of an actively exploited vulnerability or a severe incident having an impact on the security of the product with digital elements, the manufacturer shall inform the impacted users of the product with digital elements, and where appropriate all users, of that vulnerability or incident and, where necessary, of any risk mitigation and corrective measures that the users can deploy to mitigate the impact of that vulnerability or incident, where appropriate in **a structured, machine-readable format that is easily automatically processable**. Where the manufacturer fails to inform the users of the product with digital elements in a timely manner, the notified CSIRTs designated as coordinators may provide such information to the users when considered to be proportionate and necessary for preventing or mitigating the impact of that vulnerability or incident.
>
> **9.** By 11 December 2025, the Commission shall adopt delegated acts in accordance with Article 61 of this Regulation to supplement this Regulation by specifying the terms and conditions for applying the cybersecurity-related grounds in relation to delaying the dissemination of notifications as referred to in Article 16(2) of this Regulation. …
>
> **10.** The Commission may, by means of implementing acts, specify further the format and procedures of the notifications referred to in this Article as well as in Articles 15 and 16. …
---
### 2. Atomic clause map (Art. 14)
| Clause ID | Locus | Type | Highest Sev. | Gist |
|---|---|---|---|---|
| CRA-CL51 | Art. 14(1) sentence 1 | AEV notification duty | **S3** | Manufacturer shall notify actively exploited vulnerability to CSIRT + ENISA. |
| CRA-CL52 | Art. 14(1) sentence 2 (single platform) | Platform | **S2** | Via single reporting platform (Art. 16). |
| CRA-CL53 | Art. 14(2)(a) (early warning 24h) | Reporting tier 1 (AEV) | **S3** | 24h early warning for actively exploited vulnerability. |
| CRA-CL54 | Art. 14(2)(b) (vulnerability notification 72h) | Reporting tier 2 (AEV) | **S3** | 72h vulnerability notification. |
| CRA-CL55 | Art. 14(2)(c) (final report 14d) | Reporting tier 3 (AEV) | **S2** | Final report 14 days after corrective/mitigating measure. |
| CRA-CL56 | Art. 14(3) sentence 1 | Severe-incident notification duty | **S3** | Manufacturer shall notify severe incident to CSIRT + ENISA. |
| CRA-CL57 | Art. 14(3) sentence 2 (single platform) | Platform | **S2** | Via single reporting platform. |
| CRA-CL58 | Art. 14(4)(a) (early warning 24h) | Reporting tier 1 (SI) | **S3** | 24h early warning for severe incident. |
| CRA-CL59 | Art. 14(4)(b) (incident notification 72h) | Reporting tier 2 (SI) | **S3** | 72h incident notification. |
| CRA-CL60 | Art. 14(4)(c) (final report 1m) | Reporting tier 3 (SI) | **S2** | Final report 1 month after (b). |
| CRA-CL61 | Art. 14(5)(a) (severe-incident test A) | Severe-incident definition | **S3** | Affects CIA of sensitive or important data/functions. |
| CRA-CL62 | Art. 14(5)(b) (severe-incident test B) | Severe-incident definition | **S3** | Introduction or execution of malicious code. |
| CRA-CL63 | Art. 14(6) (intermediate report) | Reporting tier 4 | **S2** | Intermediate report on CSIRT request. |
| CRA-CL64 | Art. 14(7) (main establishment routing) | Routing | **S2** | Notification via CSIRT of Member State of main establishment. |
| CRA-CL65 | Art. 14(8) sentence 1 (user notification) | User notification | **S3** | Inform impacted users; machine-readable format if appropriate. |
| CRA-CL66 | Art. 14(8) sentence 2 (CSIRT fallback) | CSIRT fallback | **S2** | CSIRT may provide info to users if manufacturer fails. |
| CRA-CL67 | Art. 14(9) (delegated acts — delay grounds) | Delegated acts | **S2** | Commission specifies cybersecurity-related grounds for delaying dissemination. |
| CRA-CL68 | Art. 14(10) (implementing acts — format) | Implementing acts | **S2** | Commission specifies format and procedures. |
**Total: 18 atomic clauses for Art. 14.**
---
### 3. Detailed cards
#### 3.1 CRA-CL51 — Art. 14(1) sentence 1 — AEV notification duty
**Source locus:**
> A manufacturer shall notify any actively exploited vulnerability contained in the product with digital elements that it becomes aware of simultaneously to the CSIRT designated as coordinator, in accordance with paragraph 7 of this Article, and to ENISA.
**Instance 1 — VAG — S3 — `becomes aware of`**
- **R1:** Actual knowledge.
- **R2:** Constructive knowledge.
- **R3:** Either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Actual | In-Directive: literal |
| R2 | Constructive | CJEU case law |
| R3 | Either | None in OJ |
R1 is the literal reading; R2 is the dominant judicial reading. S3.
*Berry anchor:* §3.3.1 (`becomes aware`).
**Instance 2 — POLY — S2 — `actively exploited vulnerability`**
Inherits Art. 3(42) `actively exploited vulnerability` definition. Same POLY (D42) — `reliable evidence` + `without permission`. Propagates.
*Berry anchor:* §3.3.1.
**Instance 3 — VAG — S3 — `simultaneously`**
`simultaneously` — to both CSIRT and ENISA at the same time.
- **R1:** Same notification, same timestamp.
- **R2:** Same notification, same day.
- **R3:** Same notification, within a short window (hours).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Same timestamp | In-Directive: literal |
| R2 | Same day | None in OJ |
| R3 | Short window | None in OJ |
R1 is the literal reading. R2/R3 are operational concessions. S3.
*Berry anchor:* §3.3.1 (`simultaneously`).
---
#### 3.2 CRA-CL53 — Art. 14(2)(a) — Early warning 24h (AEV)
**Source locus:**
> **(a)** an early warning notification of an actively exploited vulnerability, **<mark>without undue delay and in any event within 24 hours</mark>** of the manufacturer becoming aware of it, indicating, where applicable, the Member States on the territory of which the manufacturer is aware that their product with digital elements has been made available;
**Instance 1 — VAG + COORD — S3 — `without undue delay AND in any event within 24 hours`**
- **R1:** `without undue delay` is primary; 24h is hard ceiling.
- **R2:** 24h is primary; `without undue delay` is softer prior.
- **R3:** Both are independent (satisfy either).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Primary + ceiling | In-Directive: literal |
| R2 | 24h primary | None in OJ |
| R3 | Either | None in OJ |
R1 is the dominant reading. S3.
*Berry anchor:* §5.1 (`undue`); §5.7 (temporal); §5.4.7 (temporal AND).
**Instance 2 — POLY — S2 — `indicating, where applicable, the Member States`**
`where applicable` — soft hedge.
- **R1:** Always (indicate all MS where product is available).
- **R2:** Only where known.
- **R3:** Only where relevant.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Always | None in OJ |
| R2 | Only where known | In-Directive: literal `where applicable` |
| R3 | Only where relevant | None in OJ |
R2 is the literal reading. S2.
*Berry anchor:* §5.1 (`where applicable`).
---
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
#### 3.5 CRA-CL56 — Art. 14(3) sentence 1 — Severe-incident notification duty
**Source locus:**
> A manufacturer shall notify any **severe incident having an impact on the security of the product with digital elements** that it becomes aware of simultaneously to the CSIRT designated as coordinator, in accordance with paragraph 7 of this Article, and to ENISA.
**Instance 1 — VAG — S3 — `severe incident`**
- **R1:** Severity = operational disruption.
- **R2:** Severity = data compromise.
- **R3:** Severity = malicious code execution.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Operational | In-Directive: Art. 14(5)(a) |
| R2 | Data | In-Directive: Art. 14(5)(a) |
| R3 | Malicious code | In-Directive: Art. 14(5)(b) |
R1 vs R2 vs R3 produce materially distinct compliance populations. S3.
*Berry anchor:* §3.3.1 (`severe`).
**Instance 2 — VAG — S3 — `becomes aware of`**
Same awareness trigger as CL51. S3.
**Instance 3 — VAG — S3 — `simultaneously`**
Same as CL51. S3.
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
#### 3.8 CRA-CL62 — Art. 14(5)(b) — Severe-incident test B
**Source locus:**
> **(b)** it has **led or is capable of leading** to the introduction or execution of **malicious code** in a product with digital elements or in the network and information systems of a user of the product with digital elements.
**Instance 1 — VAG — S3 — `led or is capable of leading`**
Same actual-vs-potential pattern as CL61. S3.
**Instance 2 — POLY — S2 — `malicious code`**
`malicious code` — what counts?
- **R1:** Malware (traditional).
- **R2:** Exploit code.
- **R3:** Backdoor.
- **R4:** Any code with malicious intent.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Malware | None in OJ |
| R2 | Exploit | None in OJ |
| R3 | Backdoor | None in OJ |
| R4 | Any | In-Directive: literal `malicious code` |
R4 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`malicious code`).
**Instance 3 — POLY — S2 — `introduction or execution`**
Two modes (OR).
- **R1:** Introduction only (presence).
- **R2:** Execution only (activity).
- **R3:** Either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Presence | In-Directive: literal |
| R2 | Activity | In-Directive: literal |
| R3 | Either | In-Directive: literal `or` |
R3 is the literal reading. S2.
*Berry anchor:* §5.4.7 (OR).
**Instance 4 — SCOPE-Q — S2 — `in a product with digital elements or in the network and information systems of a user`**
Two targets (OR).
- **R1:** In the product.
- **R2:** In the user's NIS.
- **R3:** Either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Product | In-Directive: literal |
| R2 | User's NIS | In-Directive: literal |
| R3 | Either | In-Directive: literal `or` |
R3 is the literal reading. S2.
*Berry anchor:* §5.4.7 (OR); §3.3.1 (`user`).
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
#### 2.1 CRA-CL75 — Art. 16(2) — Dissemination with delay grounds
**Source locus:**
> After receiving a notification, the CSIRT designated as coordinator initially receiving the notification shall, without delay, disseminate the notification via the single reporting platform to the CSIRTs designated as coordinators on the territory of which the manufacturer has indicated that the product with digital elements has been made available. In exceptional circumstances and, in particular, upon request by the manufacturer and in light of the level of sensitivity of the notified information as indicated by the manufacturer under Article 14(2), point (a), of this Regulation, the dissemination of the notification **may be delayed based on justified cybersecurity-related grounds** for a period of time that is strictly necessary, including where a vulnerability is subject to a coordinated vulnerability disclosure procedure as referred to in Article 12(1) of Directive (EU) 2022/2555. …
**Instance 1 — VAG — S3 — `justified cybersecurity-related grounds`**
The delay test. Three materially distinct readings:
- **R1:** Active exploitation in progress (delay to prevent mass exploitation).
- **R2:** Coordinated vulnerability disclosure in progress (CVD procedure).
- **R3:** National security grounds.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Active exploitation | In-Directive: Art. 16(2) + Art. 14(9) delegated acts |
| R2 | CVD in progress | In-Directive: literal `including where a vulnerability is subject to a coordinated vulnerability disclosure procedure` |
| R3 | National security | None in OJ |
R2 is the literal reading (illustrative). S3.
*Berry anchor:* §5.1 (`justified`).
**Instance 2 — VAG — S2 — `strictly necessary`**
`strictly necessary` — EU law proportionality test.
- **R1:** Minimum time required to address the cybersecurity ground.
- **R2:** Until the cybersecurity ground is resolved.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Minimum time | In-Directive: literal `strictly necessary` |
| R2 | Until resolved | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §5.1 (`strictly necessary`).
---
#### 2.2 CRA-CL79 — Art. 17(2) — Public disclosure
**Source locus:**
> Where public awareness is necessary to prevent or mitigate a severe incident having an impact on the security of the product with digital elements or to handle an ongoing incident, or where disclosure of the incident is otherwise in the public interest, the CSIRT designated as coordinator of the relevant Member State may, after consulting the manufacturer concerned and, where appropriate, in cooperation with ENISA, inform the public about the incident or require the manufacturer to do so.
**Instance 1 — VAG — S2 — `public awareness is necessary`**
- **R1:** Necessary per CSIRT assessment.
- **R2:** Necessary per ENISA assessment.
- **R3:** Either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | CSIRT | In-Directive: literal |
| R2 | ENISA | In-Directive: `where appropriate, in cooperation with ENISA` |
| R3 | Either | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`necessary`).
---
#### 2.3 CRA-CL81 — Art. 17(4) — No-increased-liability shield
**Source locus:**
> The mere act of notification in accordance with Article 14(1) and (3) or Article 15(1) and (2) shall not subject the notifying natural or legal person to increased liability.
**Instance 1 — VAG — S2 — `mere act of notification`**
---
### 3. T3-to-v0.2 mapping
T3 had no clauses for Art. 15–17. The v0.2 expansion adds 15 atomic clauses (CL69–CL83).
---
**End of Art. 15–17 file. Next: `06_CRA_Art18-23_EconomicOperators.md`.**
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

> **Source.** OJ L, 20.11.2024, p. 38–40. `03_REFERENCE_MATERIAL/Regulatory_References/CRA.txt`, lines ~2371–2501.
>
> **Pattern.** Article quoted in full (paragraph by paragraph), then per-clause analysis.
>
> **Article 14 is the operational consequence of the manufacturer's obligation.** It defines the reporting architecture for actively exploited vulnerabilities (24h/72h/14d) and severe incidents (24h/72h/1m) — running parallel to GDPR Art. 33/34 and NIS 2 Art. 23.

### from regs/CRA.ambiguity.md

Same awareness-trigger pattern as NIS 2 Art. 23(4)(a)(b) and GDPR Art. 33(1).

### from regs/CRA.ambiguity.md

Same twin-trigger temporal pattern as NIS 2 Art. 23(4)(a) and GDPR Art. 33(1).

### from regs/CRA.ambiguity.md

Same as NIS 2 Art. 23(4)(d)(iii) `applied and ongoing mitigation measures`. OR.

### from regs/CRA.ambiguity.md

Same as NIS 2 Art. 23(4)(d)(i) `detailed description`.

### from regs/CRA.ambiguity.md

Inherits Art. 14(5) definition (CL61/CL62). Same definitional regress as NIS 2 Art. 23(3) `significant incident`.

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

### from regs/CRA.ambiguity.md

**Layer 1 observation** — The Commission's Art. 14(9) delegated acts (expected by 11 December 2025) will specify `the terms and conditions for applying the cybersecurity-related grounds in relation to delaying the dissemination`. As of mid-2025, these acts are not yet published. Same implementing-acts normative gap as NIS 2 Art. 23(11).

### from regs/CRA.ambiguity.md

Same pattern as NIS 2 Art. 23(7). `necessary` — by whom?

### from regs/CRA.ambiguity.md

Same as NIS 2 Art. 23(1) `mere act of notification`.

<!-- aegis:purity: own_reg=CRA; demoted=17; core_cross_mentions=0 -->