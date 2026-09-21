---
document_id: AEGIS-PREPROC-CRA-ART-13
title: CRA Art. 13 — SecurityObjectives & SecurityRules
regulation: CRA
article: Art. 13
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-01_Data-Protection/D-01.1.md
  - ../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.1.md
  - ../../CrossRegulation/DomainAnalysis/D-01_Data-Protection/D-01.2.md
  - ../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.2.md
  - ../../CrossRegulation/DomainAnalysis/D-01_Data-Protection/D-01.4.md
  - ../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.4.md
  - ../../CrossRegulation/DomainAnalysis/D-02_Vulnerability-Management/D-02.1.md
  - ../../CrossRegulation/DeepAnalysis/D-02_Vulnerability-Management/D-02.1.md
  - ../../CrossRegulation/DomainAnalysis/D-02_Vulnerability-Management/D-02.2.md
  - ../../CrossRegulation/DeepAnalysis/D-02_Vulnerability-Management/D-02.2.md
  - ../../CrossRegulation/DomainAnalysis/D-02_Vulnerability-Management/D-02.3.md
  - ../../CrossRegulation/DeepAnalysis/D-02_Vulnerability-Management/D-02.3.md
  - ../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.1.md
  - ../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.1.md
  - ../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.3.md
  - ../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.3.md
  - ../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.4.md
  - ../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.4.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.1.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.1.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.2.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.2.md
  - ../../CrossRegulation/DomainAnalysis/D-05_Data-Lifecycle/D-05.1.md
  - ../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.1.md
  - ../../CrossRegulation/DomainAnalysis/D-05_Data-Lifecycle/D-05.2.md
  - ../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.2.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.1.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.1.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.2.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.2.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.3.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.3.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.4.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.4.md
  - ../../CrossRegulation/DomainAnalysis/D-07_Secure-Development/D-07.1.md
  - ../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.1.md
  - ../../CrossRegulation/DomainAnalysis/D-07_Secure-Development/D-07.4.md
  - ../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.4.md
  - ../../CrossRegulation/DomainAnalysis/D-08_Human-Factors/D-08.1.md
  - ../../CrossRegulation/DeepAnalysis/D-08_Human-Factors/D-08.1.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.2.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.2.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.4.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.4.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.1.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.1.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.2.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.2.md
status: DRAFT
---

# CRA Art. 13

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-CRA-006 | A product with digital elements is made available on the market without known exploitable vulnerabilities, and vulnerabilities contained in the product are identified and documented on a continuing basis throughout the support period. | `CRA-CL130` (Annex I Part I (2)(a) — known exploitable); `CRA-CL143` (Annex I Part II (1) — identify and document); `CRA-CL18` (Art. 13(3) sentence 1 — documented and updated); `CRA-CL26` (Art. 13(7) — systematically document) | D-02.1, D-02.2 |
| SO-CRA-010 | Vulnerabilities of a product with digital elements, including those of integrated components, are handled effectively and in accordance with the Annex I Part II vulnerability-handling requirements throughout the support period determined by the manufacturer (minimum 5 years, or the expected use time if shorter). | `CRA-CL27` (Art. 13(8) sentence 1 — handle vulnerabilities during support); `CRA-CL28` (Art. 13(8) sentence 2 — factors); `CRA-CL29` (Art. 13(8) sentence 3 — 5-year floor) | D-02.2, D-04.2 |
| SO-CRA-010 | D-02.2, D-04.2 | Art. 13(8) sentence 1–3 | Effective vulnerability handling during support period (min 5 years) |
| SO-CRA-011 | Each security update made available to users during the support period remains available after it has been issued for at least 10 years or for the remainder of the support period, whichever is longer. | `CRA-CL33` (Art. 13(9) — 10-year update availability) | D-02.2 |
| SO-CRA-011 | D-02.2 | Art. 13(9) | 10-year update availability after support period |
| SO-CRA-012 | The manufacturer puts in place, documents and enforces a policy on coordinated vulnerability disclosure for its products with digital elements, and — once a security update has been made available — shares and publicly discloses information about fixed vulnerabilities, including description, affected-product identification, impacts, severity, and remediation guidance, subject to a duly-justified delay exception where security risks of publication outweigh security benefits. | `CRA-CL147` (Annex I Part II (5) — CVD policy); `CRA-CL146` (Annex I Part II (4) — public disclosure of fixed vulnerabilities); `CRA-CL75` (Art. 16(2) — CSIRT dissemination with delay grounds); `CRA-CL31` (Art. 13(8) sentence 5 — documentation of support period factors); `CRA-CL32` (Art. 13(8) sentence 6 — CVD policy) | D-02.3, D-09.1 |
| SO-CRA-012 | D-02.3, D-09.1 | Annex I Part II (4)/(5) + Art. 13(8) sentence 6 + Art. 16(2) | CVD policy + public disclosure with duly-justified delay exception |
| SO-CRA-013 | The manufacturer facilitates the sharing of information about potential vulnerabilities in its products with digital elements and in third-party components contained therein, including by providing a publicly identifiable contact address for the reporting of vulnerabilities. | `CRA-CL148` (Annex I Part II (6) — sharing + contact address); `CRA-CL42` (Art. 13(17) — single point of contact) | D-02.3, D-09.1 |
| SO-CRA-013 | D-02.3, D-09.1 | Annex I Part II (6) + Art. 13(17) | Vulnerability-sharing + contact address |
| SO-CRA-014 | Effective and regular tests and reviews of the security of a product with digital elements are applied on a continuing basis throughout the support period, with the tests and reviews producing evidence of conformity with the Annex I Part I cybersecurity requirements. | `CRA-CL145` (Annex I Part II (3) — effective and regular tests and reviews); `CRA-CL165` (Annex VII §6 — test reports); `CRA-CL27` (Art. 13(8) sentence 1 — handle effectively); `CRA-CL26` (Art. 13(7) — systematically document) | D-02.4, D-10.3, D-09.4 |
| SO-CRA-014 | D-02.4, D-10.3, D-09.4 | Annex I Part II (3) + Annex VII §6 + Art. 13(7)/(8) | Effective and regular tests and reviews of security |
| SO-CRA-015 | Identities, credentials and access entitlements for users, services, and integrated components of the product with digital elements are managed in a verifiable manner throughout the operational lifetime of the product. | `CRA-CL133` (Annex I Part I (2)(d) — appropriate control mechanisms, including authentication, identity or access management); `CRA-CL40` (Art. 13(15) — identification: type, batch, serial); `CRA-CL42` (Art. 13(17) — single point of contact) | D-03.1, D-03.3, D-09.4 |
| SO-CRA-015 | D-03.1, D-03.3, D-09.4 | Annex I Part I (2)(d) + Art. 13(15)/(17) | Identity/credential management in verifiable manner |
| SO-CRA-021 | The availability of essential functions of a product with digital elements is protected also after an incident, through resilience and mitigation measures including resistance to and recovery from denial-of-service attacks, and the manufacturer reduces the impact of an incident using appropriate exploitation-mitigation mechanisms and techniques. | `CRA-CL137` (Annex I Part I (2)(h) — availability + resilience + DoS); `CRA-CL140` (Annex I Part I (2)(k) — reduce impact via exploitation mitigation); `CRA-CL138` (Annex I Part I (2)(i) — minimise cascading impact on other devices / networks); `CRA-CL46` (Art. 13(21) — corrective measures on non-conformity) | D-04.2, D-04.4, D-07.1 |
| SO-CRA-021 | D-04.2, D-04.4, D-07.1 | Annex I Part I (2)(h) + (2)(i) + (2)(k) + Art. 13(21) | Availability after incident + DoS resilience + exploitation mitigation |
| SO-CRA-034 | Data processed by a product with digital elements — personal or other — is limited to what is adequate, relevant, and necessary in relation to the intended purpose of the product (data minimisation). | `CRA-CL136` (Annex I Part I (2)(g) — adequate, relevant, necessary); `CRA-CL19` (Art. 13(3) sentence 2 — intended purpose + reasonably foreseeable use); `CRA-CL3` (Art. 3(23) — intended purpose definition) | D-05.1 |
| SO-CRA-034 | D-05.1 | Annex I Part I (2)(g) + Art. 13(3) sentence 2 + Art. 3(23) | Data minimisation: adequate, relevant, necessary for intended purpose |
| SO-CRA-035 | Security updates and supporting advisory messages remain available to users across the support period and the 10-year (or remainder-of-support-period) update-availability tail, ensuring continuity of protective capability beyond the support period. | `CRA-CL149` (Annex I Part II (7) — secure update distribution); `CRA-CL150` (Annex I Part II (8) — dissemination without delay, free of charge); `CRA-CL33` (Art. 13(9) — 10-year update availability) | D-05.2, D-02.2 |
| SO-CRA-035 | D-05.2, D-02.2 | Annex I Part II (7)/(8) + Art. 13(9) | Update availability across support period + 10-year tail |
| SO-CRA-037 | The manufacturer exercises due diligence when integrating components sourced from third parties — including components of free and open-source software not made available on the market in the course of a commercial activity — so that those components do not compromise the cybersecurity of the product with digital elements. | `CRA-CL23a` (Art. 13(5) — due diligence on third-party components); `CRA-CL24` (Art. 13(6) sentence 1 — component vulnerability reporting + address & remediate); `CRA-CL25` (Art. 13(6) sentence 2 — sharing with component supplier) | D-06.1, D-02.2 |
| SO-CRA-037 | D-06.1, D-02.2 | Art. 13(5)/(6) | Due diligence on third-party components (incl. FOSS) + component vuln reporting |
| SO-CRA-038 | The manufacturer draws up and maintains a software bill of materials (SBOM) covering the components and dependencies contained in the product with digital elements in a commonly used and machine-readable format that includes, at minimum, the top-level dependencies; on a reasoned request from a market surveillance authority, the SBOM is provided where necessary for the authority to check compliance with the Annex I cybersecurity requirements. | `CRA-CL39` (Art. 3(39) — SBOM definition); `CRA-CL143` (Annex I Part II (1) — SBOM); `CRA-CL49` (Art. 13(24) — SBOM implementing acts); `CRA-CL159` (Annex II §9 — SBOM location for user); `CRA-CL161` (Annex VII §2(b) — SBOM in technical documentation); `CRA-CL167` (Annex VII §8 — SBOM on MSA request) | D-06.2 (CRA sole authority per taxonomy §4.1), D-02.1 |
| SO-CRA-038 | D-06.2 (CRA sole authority), D-02.1 | Art. 3(39) + Annex I Part II (1) + Annex II §9 + Art. 13(24) + Annex VII §2(b)/§8 | SBOM content + format + on-request |
| SO-CRA-041 | A manufacturer established outside the Union may appoint an authorised representative established in the Union by written mandate to perform specified tasks on behalf of the manufacturer; the manufacturer's obligations under Art. 13(1)–(11), Art. 13(12) first subparagraph, and Art. 13(14) are not delegable to the authorised representative, who retains the technical documentation and cooperates with market surveillance authorities. | `CRA-CL84` (Art. 18(1) — AR appointment); `CRA-CL85` (Art. 18(2) — AR carve-out of non-delegable obligations); `CRA-CL86` (Art. 18(3) — AR tasks); `CRA-CL13` (Art. 3(13) — manufacturer definition) | D-06.4, D-09.4 |
| SO-CRA-045 | A product with digital elements is designed, developed, and produced in accordance with the essential cybersecurity requirements set out in Annex I Part I, with the cybersecurity risk assessment taken into account across the planning, design, development, production, delivery, and maintenance phases of the product — with a view to minimising cybersecurity risks, preventing incidents, and minimising their impact including in relation to the health and safety of users. | `CRA-CL14` (Art. 13(1) — design, develop, produce per Annex I Part I); `CRA-CL15` (Art. 13(2) sentence 1 — risk assessment); `CRA-CL16` (Art. 13(2) sentence 1 — 6-phase propagation); `CRA-CL17` (Art. 13(2) sentence 2 — health + safety of users); `CRA-CL129` (Annex I Part I (1) — chapeau) | D-07.1, D-09.2 |
| SO-CRA-045 | D-07.1, D-09.2 | Art. 13(1)/(2) + Annex I Part I (1) | Design/development/production per Annex I across 6 lifecycle phases |
| SO-CRA-047 | Procedures are in place for products with digital elements that are part of a series of production to remain in conformity with this Regulation; changes to the product are assessed against the conformity assessment, and where a change is a substantial modification under Art. 3(30), the entity making the modification is treated as the manufacturer with the attendant obligations. | `CRA-CL39` (Art. 13(14) — series-of-production conformity); `CRA-CL96` (Art. 21 — manufacturer-equivalent trigger); `CRA-CL97` (Art. 22(1) — third-party substantial modification = manufacturer); `CRA-CL30` (Art. 3(30) — substantial modification definition); `CRA-CL34` (Art. 13(10) — substantial modification compliance for the last-placed version) | D-07.4, D-06.4 |
| SO-CRA-047 | D-07.4, D-06.4 | Art. 13(14) + Art. 21 + Art. 22(1) + Art. 3(30) + Art. 13(10) | Series-production conformity + substantial-modification consequences |
| SO-CRA-048 | A product with digital elements is accompanied by detailed instructions — or an internet address referring to such detailed instructions — covering the necessary measures during initial commissioning and throughout the lifetime of the product to ensure its secure use; how changes to the product can affect the security of data; how security-relevant updates can be installed; the secure decommissioning of the product including how user data can be securely removed; how the default setting enabling automatic installation of security updates may be turned off; and — for products intended for integration into other products with digital elements — the information necessary for the integrator to comply with the Annex I cybersecurity requirements and the Annex VII documentation requirements. | `CRA-CL158` (Annex II §8(a)–(f) — detailed instructions); `CRA-CL43` (Art. 13(18) — accompany with Annex II info + accessibility for 10 years) | D-08.1, D-09.4 |
| SO-CRA-048 | D-08.1, D-09.4 | Annex II §8(a)–(f) + Art. 13(18) | Detailed user-facing instructions for secure use over product lifetime |
| SO-CRA-051 | The manufacturer establishes policies, processes and procedures necessary to implement its CRA cybersecurity obligations, including — but not limited to — the coordinated vulnerability disclosure policy (Annex I Part II §5 + Art. 13(8) sentence 6), the secure update distribution mechanism (Annex I Part II §7), the support-period determination methodology (Art. 13(8) sentence 2), and the cessation-of-operations communication procedure (Art. 13(23)). | `CRA-CL32` (Art. 13(8) sentence 6 — CVD policy); `CRA-CL147` (Annex I Part II (5) — CVD policy); `CRA-CL28` (Art. 13(8) sentence 2 — support-period factors); `CRA-CL48` (Art. 13(23) — cessation of operations) | D-09.1, D-02.3 |
| SO-CRA-051 | D-09.1, D-02.3 | Art. 13(8) sentence 6 + Annex I Part II (5) + Art. 13(8) sentence 2 + Art. 13(23) | Manufacturer policies, processes, procedures for CRA obligations |
| SO-CRA-053 | The manufacturer documents the cybersecurity risk assessment referred to in Art. 13(2) and updates it as appropriate during a support period determined in accordance with Art. 13(8); the risk assessment comprises at least an analysis of cybersecurity risks based on the intended purpose and reasonably foreseeable use (including operational environment and assets to be protected) and indicates whether and in what manner the Annex I Part I (2) requirements apply to the relevant product and how those requirements are implemented as informed by the risk assessment. | `CRA-CL18` (Art. 13(3) sentence 1 — documented and updated); `CRA-CL19` (Art. 13(3) sentence 2 — intended purpose + reasonably foreseeable use); `CRA-CL20` (Art. 13(3) sentence 3 — Annex I Part I (2) applicability mapping); `CRA-CL21` (Art. 13(4) sentence 1 — include risk assessment in technical documentation); `CRA-CL162` (Annex VII §3 — risk-assessment documentation) | D-09.2, D-09.4, D-07.1 |
| SO-CRA-053 | D-09.2, D-09.4, D-07.1 | Art. 13(3) sentence 1–3 + Art. 13(4) + Annex VII §3 | Cybersecurity risk assessment documentation + Annex I Part I (2) applicability |
| SO-CRA-054 | The cybersecurity risk assessment is reviewed and updated as appropriate when there is a change of the risk represented by the product with digital elements (e.g. material change in product, material change in threat landscape, or upon becoming aware of a previously unidentified vulnerability). | `CRA-CL18` (Art. 13(3) sentence 1 — `updated as appropriate`); `CRA-CL26` (Art. 13(7) — update on becoming aware of vulnerability); `CRA-CL14` (Art. 13(8) — ADCO guidance and harmonised-standards changes) | D-09.2, ID.IM-04 |
| SO-CRA-054 | D-09.2, ID.IM-04 | Art. 13(3) sentence 1 + Art. 13(7)/(8) + Art. 13(14) | Risk-assessment review/update on material change |
| SO-CRA-055 | A manufacturer designates a single point of contact to enable users — including security researchers — to communicate directly and rapidly with the manufacturer, including to facilitate reporting on vulnerabilities of the product with digital elements; the single point of contact allows users to choose their preferred means of communication and does not limit such means to automated tools. | `CRA-CL42` (Art. 13(17) — single point of contact); `CRA-CL152` (Annex II §2 — SPOC for vulnerability reporting) | D-09.4, D-02.3 |
| SO-CRA-055 | D-09.4, D-02.3 | Art. 13(17) + Annex II §2 | Single point of contact (with non-automated option) |
| SO-CRA-056 | A product with digital elements bears a type, batch, or serial number, or other element allowing identification of the product and its version; the manufacturer's name, registered trade name or registered trademark, and postal address, email address or other digital contact details (and, where applicable, website) are indicated on the product. | `CRA-CL40` (Art. 13(15) — product identification: type/batch/serial); `CRA-CL41` (Art. 13(16) — manufacturer contact info on product); `CRA-CL151` (Annex II §1 — manufacturer contact on product); `CRA-CL153` (Annex II §3 — product unique identification) | D-09.4 |
| SO-CRA-056 | D-09.4 | Art. 13(15)/(16) + Annex II §1/§3 | Product identification + manufacturer contact info |
| SO-CRA-057 | The manufacturer keeps the technical documentation and the EU declaration of conformity at the disposal of the market surveillance authorities for at least 10 years after the product has been placed on the market, or for the support period, whichever is longer. | `CRA-CL38` (Art. 13(13) — 10-year documentation retention); `CRA-CL91` (Art. 19(6) — importer 10-year retention); `CRA-CL100` (Art. 23(2) — supply-chain 10-year retention) | D-09.4 |
| SO-CRA-057 | D-09.4 | Art. 13(13) + Art. 19(6) + Art. 23(2) | 10-year technical documentation + EU declaration retention |
| SO-CRA-058 | The manufacturer draws up, before placing a product with digital elements on the market, the technical documentation referred to in Art. 31; carries out (or has carried out) the chosen conformity assessment procedure referred to in Art. 32; and — where compliance with the applicable cybersecurity requirements has been demonstrated — draws up the EU declaration of conformity in accordance with Art. 28 and affixes the CE marking in accordance with Art. 30. | `CRA-CL36` (Art. 13(12) sentence 1 — tech docs + conformity assessment before placing); `CRA-CL37` (Art. 13(12) sentence 2 — EU declaration + CE marking); `CRA-CL120` (Art. 31(1) — tech docs contain Annex I compliance evidence); `CRA-CL121` (Art. 31(2) — tech docs drawn up before placing and updated during support); `CRA-CL113` (Art. 28(1) — EU declaration content); `CRA-CL114` (Art. 28(2) — declaration format per Annex V/VI); `CRA-CL116` (Art. 28(4) — manufacturer's responsibility); `CRA-CL117` (Art. 30(1) — CE marking affixing); `CRA-CL118` (Art. 30(3) — CE marking before placing) | D-09.4 |
| SO-CRA-058 | D-09.4 | Art. 13(12) + Art. 31(1)/(2) + Art. 28(1)/(2)/(4) + Art. 30(1)/(3) | Pre-market technical documentation + EU declaration + CE marking |
| SO-CRA-060 | Where the manufacturer has placed subsequent substantially modified versions of a software product on the market, the manufacturer may ensure compliance with Annex I Part II (2) (vulnerability remediation) only for the version last placed on the market, provided that the users of previously placed versions have access to the last-placed version free of charge and do not incur additional costs to adjust the hardware and software environment in which they use the original version. | `CRA-CL34` (Art. 13(10) — substantial-modification compliance scope) | D-09.4, D-07.4, D-02.2 |
| SO-CRA-060 | D-09.4, D-07.4, D-02.2 | Art. 13(10) | Substantial-modification compliance scope (last-placed version) |
| SO-CRA-061 | The manufacturer provides the end date of the support period — including at least the month and the year — clearly and understandably at the time of purchase of the product; the support period end-date information is also referenced in Annex II §7 (type of technical security support + end-date) and the technical documentation (Annex VII §4). | `CRA-CL44` (Art. 13(19) — support-period end-date display); `CRA-CL157` (Annex II §7 — support-period type + end-date) | D-09.4, D-05.2 |
| SO-CRA-061 | D-09.4, D-05.2 | Art. 13(19) + Annex II §7 | Support-period end-date communication |
| SO-CRA-062 | The manufacturer either provides a copy of the EU declaration of conformity or a simplified EU declaration of conformity with the product with digital elements. | `CRA-CL45` (Art. 13(20) — full or simplified EU declaration with product); `CRA-CL156` (Annex II §6 — internet address for EU declaration) | D-09.4 |
| SO-CRA-062 | D-09.4 | Art. 13(20) + Annex II §6 | EU declaration provision (full or simplified) with product |
| SO-CRA-063 | Where the manufacturer knows or has reason to believe that the product with digital elements or the processes put in place by the manufacturer are not in conformity with the Annex I cybersecurity requirements, the manufacturer — from placing on the market and for the support period — immediately takes the corrective measures necessary to bring the product or processes into conformity, or to withdraw or recall the product, as appropriate. | `CRA-CL46` (Art. 13(21) — immediate corrective measures + withdrawal + recall) | D-09.4, D-04.2, D-07.4 |
| SO-CRA-063 | D-09.4, D-04.2, D-07.4 | Art. 13(21) | Immediate corrective measures on non-conformity + withdrawal/recall |
| SO-CRA-064 | Upon a reasoned request from a market surveillance authority, the manufacturer provides that authority — in a language easily understood by the authority — with all information and documentation, in paper or electronic form, necessary to demonstrate the conformity of the product and the manufacturer's processes with the Regulation. | `CRA-CL47` (Art. 13(22) — MSA cooperation); `CRA-CL22` (Art. 13(4) sentence 2 — AI Act carve-out for unified risk assessment) | D-09.4 |
| SO-CRA-064 | D-09.4 | Art. 13(22) + Art. 13(4) sentence 2 | Cooperation with MSAs + AI Act carve-out |
| SO-CRA-065 | Where a manufacturer ceases its operations and — as a result — is not able to comply with this Regulation, the manufacturer informs, before the cessation takes effect, the relevant market surveillance authorities, and — by any means available and to the extent possible — the users of the relevant products with digital elements placed on the market, of the impending cessation of operations. | `CRA-CL48` (Art. 13(23) — cessation of operations notification) | D-09.4 |
| SO-CRA-065 | D-09.4 | Art. 13(23) | Cessation of operations notification (MSAs + users) |
| SO-CRA-067 | The Commission may adopt implementing acts specifying the format and elements of the software bill of materials referred to in Annex I Part II (1); ADCO may conduct a Union-wide dependency assessment on the Union's dependence on software components (in particular FOSS components) for specific categories of products with digital elements. | `CRA-CL49` (Art. 13(24) — SBOM implementing acts); `CRA-CL50` (Art. 13(25) — Union-wide dependency assessment by ADCO); `CRA-CL67` (Art. 14(9) — delegated acts on delay-dissemination grounds); `CRA-CL68` (Art. 14(10) — implementing acts on notification format/procedures); `CRA-CL8` (Art. 7(3) — delegated acts amending Annex III); `CRA-CL9` (Art. 7(4) — implementing acts specifying technical descriptions); `CRA-CL119` (Art. 30(6) — implementing acts on labels/pictograms) | D-09.4 |
| SO-CRA-067 | D-09.4 | Art. 13(24)/(25) + Art. 14(9)/(10) + Art. 7(3)/(4) + Art. 30(6) | Commission implementing / delegated acts (SBOM, delay grounds, labels, technical descriptions) |
| SO-CRA-070 | The cybersecurity risk-assessment documentation is preserved, updated as appropriate during the support period, and made available — together with the technical documentation as a whole — to market surveillance authorities on reasoned request (Art. 13(4) sentence 1 + Annex VII §3). | `CRA-CL21` (Art. 13(4) sentence 1 — include risk assessment in technical documentation); `CRA-CL162` (Annex VII §3 — risk-assessment documentation); `CRA-CL47` (Art. 13(22) — MSA cooperation) | D-10.2, D-09.4 |
| SO-CRA-070 | D-10.2, D-09.4 | Art. 13(4) sentence 1 + Annex VII §3 + Art. 13(22) | Risk-assessment documentation preservation + availability to MSAs |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-001
  title: "State-of-the-art cryptographic confidentiality baseline"
  source_clauses:
    - { clause_id: CRA-CL129, article_ref: "Annex I Part I (1) — chapeau" }
    - { clause_id: CRA-CL134, article_ref: "Annex I Part I (2)(e) — confidentiality + encryption" }
    - { clause_id: CRA-CL14, article_ref: "Art. 13(1) — design/development/production duty" }
  linked_objectives: [SO-CRA-001, SO-CRA-045]
  sub_domain: [D-01.1, D-01.2]
  nist_csf_mapping:
    - { id: PR.DS-01, title: "The confidentiality, integrity, and availability of data-at-rest are protected" }
    - { id: PR.DS-02, title: "The confidentiality, integrity, and availability of data-in-transit are protected" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 13(1) lays the umbrella design-and-development duty on manufacturers, executed in the three sequenced phases described in CRA-CL14 (designed, developed, produced) and tied to the Annex I risk-based baseline through Recital 49. On top of that umbrella, Annex I Part I (1) requires that products with digital elements ensure an appropriate level of cybersecurity based on the risks presented by the product across its life cycle, and Annex I Part I (2)(e) carries that umbrella into a concrete property: stored, transmitted, or otherwise processed data — personal or other — must be protected in its confidentiality by state-of-the-art mechanisms, illustrated as encrypting relevant data at rest or in transit, "or by using other technical means." The triangular architecture — chapeau, Art. 13 umbrella, sub-clause property — is what makes (2)(e) operationally actionable; the manufacturer cannot meet "appropriate cybersecurity" without addressing confidentiality, and cannot address confidentiality without choosing a recognised cryptographic baseline. For a compliance officer this means documenting the cryptographic choice and the underlying risk rationale in the conformity dossier under Annex VII §3, retaining that justification for the support period established under Art. 13(8)–(9) (cf. Recital 49 for the support-period rationale).
  security_rationale: |
    The obligation in Annex I Part I (1)+(2)(e) is operationalised in NIST CSF 2.0 through **PR.DS-01 (data-at-rest confidentiality, integrity, and availability protected)** and **PR.DS-02 (data-in-transit confidentiality, integrity, and availability protected)**. PR.DS-01 anchors the cryptographic protection of stored data -- keys, certificates, key-management material -- so that an attacker who bypasses storage-layer controls (insider access, lost device, misconfigured bucket) still meets ciphertext without the corresponding key, the structural defence against offline exfiltration and ransomware plaintext-theft. PR.DS-02 anchors the in-transit leg: end-to-end confidentiality on data flowing across network paths, service-to-service calls, and external APIs, where network-position adversaries and misconfigured peering make the in-transit stratum the most frequently observed breach vector in published incident telemetry. Together PR.DS-01 and PR.DS-02 form the substrate on which every other Annex I Part I control is laid -- without them, authentication tokens can be intercepted, audit logs exfiltrated, and incident forensics become inadmissible -- and they enable the manufacturer to demonstrate ex post, through documented cipher-suite choices, key-handling evidence in the technical documentation under Annex VII sections 2/3, and conformity-assessment records under Art. 13, that the state-of-the-art baseline required by (2)(e) has been met across the support period under Art. 13(8).
  ambiguity_notes: |
    The source clause carries two distinct ambiguity stacks. First, the term state of the art is VAG-S3 in the Berry-classic sense — temporal and benchmark-relative, much like "state of the art" in GDPR Art. 32(1). Reading chosen: R2, anchoring the benchmark to harmonised standards adopted under Art. 27 (when present) and, in their absence, to industry-standard cryptographic mechanisms as of the product's support-period commencement date. Alternative readings: R1 would require continuous R&D reassessment on a literal "instant of evaluation" basis, generating unbounded compliance churn and effectively compelling a never-finished redesign cycle; R3 (any mechanism chosen by the manufacturer) would dilute the floor to "any algorithm that compiles," breaking the cross-Member-State level playing field that Annex I is designed to deliver. An additional reading, R0, would treat state-of-the-art as a forward-looking duty that anticipates the next regulatory or standards step beyond support-period commencement, structurally similar to R2 but materially more demanding; R0 is rejected on the literal bench-anchored reading preserved by Annex I. Second, the phrase at rest or in transit is POLY-S2 because the boundary between persistent storage, transient caches, and inter-process transfers is technical rather than legal; Reading chosen: R3 — both contexts are protected, with the Art. 13(2) risk assessment selecting the appropriate primitive for each technical layer. Remain open: (a) when harmonised cryptography standards under Art. 27 are slow to be adopted, can a manufacturer rely on industry-led profiles (NIST SP 800-131A, BSI TR-02102) without violating the "state of the art" baseline; (b) does post-quantum migration obligation attach to legacy products within their support period, or only to newly placed-on-the-market versions after a determined cut-over date?
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-002
  title: "Confidentiality of stored data via state-of-the-art encryption"
  source_clauses:
    - { clause_id: CRA-CL134, article_ref: "Annex I Part I (2)(e) — at-rest encryption" }
    - { clause_id: CRA-CL129, article_ref: "Annex I Part I (1) — chapeau" }
  linked_objectives: [SO-CRA-002, SO-CRA-001]
  sub_domain: [D-01.1]
  nist_csf_mapping:
    - { id: PR.DS-01, title: "The confidentiality, integrity, and availability of data-at-rest are protected" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Annex I Part I (2)(e) requires that the confidentiality of stored data — personal or other — be protected by encrypting relevant data at rest using state-of-the-art mechanisms, illustrated together with the residual "or by using other technical means"; the data-scope qualifier "personal or other" ties back to the Art. 3(47) definition, which imports the GDPR Art. 4(1) notion of personal data and so extends the obligation to any non-personal data stored alongside. The Annex I Part I (1) chapeau fixes the baseline as an appropriate level of cybersecurity based on the risks, which sets the proportionality lever for choosing encryption coverage (which fields, what granularity, what key model). In practice the manufacturer documents a per-storage-class mapping — which logical stores hold which data categories, which cipher suites apply, and which keys protect which classes — in the technical documentation under Annex VII §2 and Annex VII §3.
    [OJ-corrective note (v0.2 audit, traceability): the OJ text reads verbatim — Definitions live in Article 3 of Regulation (EU) 2024/2847 (CRA). Annex II of CRA contains the information and instructions to the user (a documentary-scope annex), not definitions. Personal data is defined by Art. 3(47) (with the cross-reference to GDPR Art. 4(1)) — there is no `Annex II definitions` anchor.]
  security_rationale: |
    The at-rest branch of the Annex I Part I (2)(e) obligation is operationalised in NIST CSF 2.0 through **PR.DS-01 (data-at-rest confidentiality, integrity, and availability protected)**. PR.DS-01 captures the structural defence against the persistent-attack-target pattern: backups, snapshots, lost disks, cloud-bucket misconfiguration -- all of which remain unreadable without the corresponding key, transforming a storage-layer bypass (insider with read access, stolen laptop, misconfigured access policy) into a ciphertext-only exposure rather than a plaintext disclosure. The encryption-at-rest control also functions as the upstream mitigation against the modern exfiltration-then-encrypt ransomware pattern, because ransomware that exfiltrates plaintext before encrypting depends directly on plaintext-at-rest exposures. PR.DS-01 feeds upward into the broader PR.DS family (integrity under PR.DS-10, access-control under PR.AA-05), and together with the manufacturer's documented per-storage-class mapping -- cipher suite, key custodian, granularity decisions -- it enables the manufacturer to demonstrate ex post, in the conformity dossier under Annex VII sections 2/3 and the Annex I Part I (1) risk assessment under Art. 13(2), that the chosen at-rest cryptographic mechanisms satisfy the state-of-the-art baseline across the support period under Art. 13(8).
  ambiguity_notes: |
    The phrase relevant data in the literal Annex I Part I (2)(e) text — "encrypting relevant data at rest or in transit" — is POLY-S2 because "relevant to what?" admits at least two materially distinct populations. Reading chosen: R2, where "relevant" means data tied to the product's intended purpose plus any data classified by the manufacturer as in-scope under the cybersecurity risk assessment conducted under Art. 13(2). Alternative reading: R1 would limit relevance strictly to data declared in the intended-purpose statement, leaving residual classes (telemetry, logs, derived metadata) outside the obligation and creating an enforcement gap. The state-of-the-art S3 ambiguity on the encryption primitive itself is carried by the umbrella SR-CRA-001 and not duplicated here.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-003
  title: "Confidentiality of data in transit across network paths"
  source_clauses:
    - { clause_id: CRA-CL134, article_ref: "Annex I Part I (2)(e) — in-transit encryption" }
    - { clause_id: CRA-CL139, article_ref: "Annex I Part I (2)(j) — limit attack surfaces incl. external interfaces" }
  linked_objectives: [SO-CRA-003, SO-CRA-001]
  sub_domain: [D-01.2]
  nist_csf_mapping:
    - { id: PR.DS-02, title: "The confidentiality, integrity, and availability of data-in-transit are protected" }
    - { id: PR.IR-01, title: "Networks and environments are protected from unauthorized logical access and usage" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Annex I Part I (2)(e) requires that the confidentiality of transmitted data — personal or other — be protected by encrypting relevant data in transit using state-of-the-art mechanisms, again illustrated together with "or by using other technical means"; the same Annex I Part I (2)(e) also covers "stored or otherwise processed," so in-transit protection is one channel of a wider obligation. Annex I Part I (2)(j) — the attack-surface limitation duty, captured for SR-CRA-039 and following — supports the in-transit protection scope by constraining the external interfaces through which data could otherwise be exposed. For a compliance officer the operational consequence is documenting the transport-security profile (TLS configurations, mTLS for service-to-service, message-bus encryption) in the technical documentation under Annex VII §2(b) and re-evaluating it against the support-period boundary.
  security_rationale: |
    The in-transit branch of the Annex I Part I (2)(e) obligation is operationalised in NIST CSF 2.0 through **PR.DS-02 (data-in-transit confidentiality, integrity, and availability protected)** and **PR.IR-01 (networks and environments protected from unauthorised logical access and usage)**. PR.DS-02 anchors the cryptographic protection of data in motion -- across network paths, inter-service calls, and third-party APIs -- where the in-transit stratum is uniquely suited to network-position adversaries, misconfigured peering, and side-channel interception, making it the most frequently observed breach vector in published incident data. PR.IR-01 captures the attack-surface-limitation side supplied by Annex I (2)(j): restricting exposed interfaces, hardening ingress paths, and aligning the network posture with the protective primitive choices so that the cipher's strength is not undermined by a permissive network surface. Together PR.DS-02 and PR.IR-01 form the pair that the (2)(e)+(j) combination operationalises, and they enable the manufacturer to demonstrate ex post, through documented transport-security profiles and network-posture evidence in the technical documentation under Annex VII section 2(b), that the in-transit confidentiality floor -- including across both internal-network and external-boundary segments -- has been sustained across the support period under Art. 13(8).
  ambiguity_notes: |
    The Annex I (2)(e) "at rest or in transit" POLY-S2 is shared with SR-CRA-001 and SR-CRA-002; this rule isolates the in-transit branch and applies the same R3 chosen reading (both contexts protected, risk-assessment-driven selection of primitive). The transmitted stratum is captured separately from stored to honour the OJ-literal conjunction. No new S3 instance is introduced on this branch, but the relationship with (j) introduces a SCOPE-Q-S2 question on whether in-transit protection covers purely internal east-west traffic or only the externally-exposed transport edges; the compliance-officer-friendly answer is both, with the risk assessment modulating primitive strength per segment.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-005
  title: "Data integrity protection and corruption reporting"
  source_clauses:
    - { clause_id: CRA-CL135, article_ref: "Annex I Part I (2)(f) — integrity + report on corruptions" }
    - { clause_id: CRA-CL141, article_ref: "Annex I Part I (2)(l) — logging + monitoring" }
  linked_objectives: [SO-CRA-005]
  sub_domain: [D-01.4, D-10.2]
  nist_csf_mapping:
    - { id: PR.DS-01, title: "The confidentiality, integrity, and availability of data-at-rest are protected" }
    - { id: PR.DS-10, title: "The confidentiality, integrity, and availability of data-in-use are protected" }
    - { id: PR.PS-04, title: "Log records are generated and made available for continuous monitoring and analysis" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Annex I Part I (2)(f) requires the manufacturer to protect the integrity of stored, transmitted, or otherwise processed data — personal or other — as well as the integrity of commands, programs, and configuration, against any manipulation or modification not authorised by the user; the clause additionally obliges the manufacturer to report on corruptions, transforming silent-tampering failures into observable events. Annex I Part I (2)(l) carries the same data into a recording and monitoring duty, so that any integrity event has a corresponding audit-trail record (further developed in SR-CRA-027). The two clauses together map to NIST CSF PR.DS-01 (data-at-rest integrity), PR.DS-10 (data-in-use integrity), and PR.PS-04 (log records made available for continuous monitoring).
  security_rationale: |
    The Annex I Part I (2)(f)+(l) integrity duty is operationalised in NIST CSF 2.0 through **PR.DS-01 (data-at-rest CIA protected)**, **PR.DS-10 (data-in-use CIA protected)**, and **PR.PS-04 (log records generated and made available for continuous monitoring and analysis)**. PR.DS-01 captures the data-at-rest integrity leg: cryptographic hashes, MACs, and integrity-checked storage ensure that an adversary cannot silently tamper with stored data, commands, programs, or configuration without invalidating the integrity check on the next read. PR.DS-10 anchors the data-in-use leg -- runtime integrity controls such as signed firmware, control-flow integrity, and tamper-detection instrumentation -- covering the firmware implants, command injection, configuration drift, and supply-chain backdoors that have dominated real-world incident data. PR.PS-04 closes the detection loop by ensuring that the integrity events become observable log records suitable for continuous monitoring, so that the "report on corruptions" obligation transforms silent tampering into observable events rather than silent failures. Together PR.DS-01, PR.DS-10, and PR.PS-04 enable the manufacturer to demonstrate ex post, through documented integrity-check evidence, log-records in the technical documentation under Annex VII sections 2/6, and corruption-report records to users, that the Annex I (2)(f)+(l) integrity duty -- including the universal-quantifier "any manipulation or modification not authorised by the user" -- has been met across the support period under Art. 13(8).
  ambiguity_notes: |
    The compound "data, personal or other, commands, programs and configuration" is COORD-S2 — a four-element list with nested OR/AND — and admits materially distinct protection scopes; Reading chosen: R1, treating the conjunction as inclusive of all four classes, in line with the OJ-literal listing. The "report on corruptions" phrase is VAG-S2; Reading chosen: R1, where the report goes to the device user or administering party in a manner proportionate to severity, rather than to an external authority (the integrity-breach case differs from the actively-exploited-vulnerability case under Art. 14). The phrase "any manipulation or modification not authorised by the user" is POLY-S2 with the "any" universal-quantifier meaning, and the literal reading is preserved — integrity protection is unconditional.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-006
  title: "Pre-market elimination of known exploitable vulnerabilities"
  source_clauses:
    - { clause_id: CRA-CL130, article_ref: "Annex I Part I (2)(a) — no known exploitable vulnerabilities" }
    - { clause_id: CRA-CL129, article_ref: "Annex I Part I (1) — chapeau" }
  linked_objectives: [SO-CRA-006, SO-CRA-008]
  sub_domain: [D-02.1, D-02.2]
  nist_csf_mapping:
    - { id: ID.RA-01, title: "Vulnerabilities in assets are identified, validated, and recorded" }
    - { id: PR.PS-02, title: "Software is maintained, replaced, and removed commensurate with risk" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS, TRIGGERED]
  regulatory_rationale: |
    Annex I Part I (2)(a) requires that products with digital elements be made available on the market without known exploitable vulnerabilities, anchoring a market-placement baseline that complements the post-market remediation duty under Annex I Part II (2). The chapeau in Annex I Part I (1) propagates the appropriate-level-of-cybersecurity qualifier into all 13 sub-points, so (2)(a) inherits the risk-based modulation: where a product handles a more severe threat model, the "without known exploitable" floor is correspondingly higher. For a compliance officer this means that the release-engineering pipeline must close out identified vulnerabilities before market placement, and a documented risk-based justification is retained in the technical documentation under Annex VII §3 and Annex VII §6 (test reports) for the duration of the support period.
  security_rationale: |
    The Annex I Part I (2)(a) "without known exploitable vulnerabilities" market-placement baseline is operationalised in NIST CSF 2.0 through **ID.RA-01 (vulnerabilities in assets identified, validated, and recorded)** and **PR.PS-02 (software maintained, replaced, and removed commensurate with risk)**. ID.RA-01 captures the upstream vulnerability-discovery gate: vulnerabilities must be systematically identified, validated (exploitable or merely theoretical), and recorded in a queryable form before the product leaves the manufacturer's release engineering pipeline, so that "known" status can be anchored to documented evidence rather than subjective judgement. PR.PS-02 captures the maintenance posture: software is maintained and (where appropriate) replaced commensurate with risk, with the market-placement baseline interpreted as the initial state in the broader maintenance lifecycle. Together ID.RA-01 and PR.PS-02 enable the manufacturer to demonstrate ex post, through documented vulnerability-gate evidence, release-pipeline records, and risk-based justification in the technical documentation under Annex VII sections 3/6, that the (2)(a) baseline was met at the moment of placement under Art. 13(1) and that the constructive-knowledge threshold (per the chosen R2 ambiguity reading) was exercised across all relevant threat-intelligence inputs available before market placement.
  ambiguity_notes: |
    The term known exploitable vulnerabilities is VAG+POLY S3 because "known" is inquiry-resistant (known to whom: the manufacturer, the public CVE database, the adversary community?), and "exploitable" admits both public-exploit and theoretical-exploit readings. Reading chosen: R2, where "known" means known to the manufacturer exercising the due diligence of the Annex VII §3 risk assessment, which is what the harmonised-standards interpretations typically anchor. Alternative readings: R1 (knowledge relative to the public CVE database) is the conservative-easy-compliance reading and would let manufacturers off the hook for non-CVE-listed weaknesses; R3 (subjective manufacturer-only) is rejected as failing the inquiry-resistant test. An additional reading, R4, would extend the inquiry-resistant baseline to threat-intelligence feeds beyond CVE databases — including vendor advisories, ISACs, and CERT-EU alerts — turning the obligation into a continuous monitoring duty; R4 is more demanding than R2 and is rejected on the literal "known" qualifier, but it deserves recording because harmonised-standards interpretations may converge toward it in critical-infrastructure sectors. The result is a "constructive knowledge" baseline: knowledge that a reasonable manufacturer exercising Annex VII §3 due diligence should have, regardless of whether the CVE has been published. Remain open: (a) does the constructive-knowledge baseline extend to vulnerabilities disclosed in confidential peer-manufacturer channels that the manufacturer has not joined; (b) when "exploitable" admits a public-PoC reading without observed-in-the-wild exploitation, is the day-zero remediated-or-disclosed duty triggered at PoC publication or at observed exploitation.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-007
  title: "Vulnerability and component identification with SBOM"
  source_clauses:
    - { clause_id: CRA-CL143, article_ref: "Annex I Part II (1) — identify and document vulnerabilities and components + SBOM" }
    - { clause_id: CRA-CL26, article_ref: "Art. 13(7) — systematically document relevant cybersecurity aspects" }
    - { clause_id: CRA-CL18, article_ref: "Art. 13(3) sentence 1 — risk assessment documented and updated" }
  linked_objectives: [SO-CRA-006, SO-CRA-007]
  sub_domain: [D-02.1]
  nist_csf_mapping:
    - { id: ID.RA-01, title: "Vulnerabilities in assets are identified, validated, and recorded" }
    - { id: ID.AM-02, title: "Inventories of software, services, and systems managed by the organization are maintained" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Annex I Part II (1) requires manufacturers of products with digital elements to identify and document the vulnerabilities and components contained in the product, including by drawing up a software bill of materials in a commonly used and machine-readable format covering at least the top-level dependencies of the product. Art. 13(7) extends the documentation duty to all relevant cybersecurity aspects observed by the manufacturer, including vulnerabilities that surface after market placement. Art. 13(3) sentence 1 imposes a separate, parallel duty to document and keep up-to-date the risk assessment itself, so the SBOM and the risk record sit in the same documentation bundle but as two distinct artefacts.
  security_rationale: |
    The Annex I Part II (1) identification-and-documentation duty is operationalised in NIST CSF 2.0 through **ID.RA-01 (vulnerabilities in assets identified, validated, and recorded)** and **ID.AM-02 (inventories of software, services, and systems managed by the organisation are maintained)**. ID.RA-01 captures the upstream discovery and recording leg: vulnerabilities -- whether surfaced by internal testing, third-party research, or Art. 14 reporting triggers -- are identified, validated (exploitable or merely theoretical), and recorded in a queryable form that survives across the support period under Art. 13(8) and the 10-year update-availability tail under Art. 13(9). ID.AM-02 anchors the component inventory: software, services, and systems are maintained as a current inventory -- the SBOM is the operational instantiation of this Subcategory -- without which "is this product affected by CVE-X published in year three?" cannot be answered by automated lookup. Together ID.RA-01 and ID.AM-02 form the precondition for every downstream control (patching under PR.PS-02, supply-chain risk management under GV.SC-02, coordinated vulnerability disclosure under SR-CRA-019), and they enable the manufacturer to demonstrate ex post, through documented vulnerability records, SBOM artefacts in the technical documentation under Annex VII section 2(b), and Art. 13(7) cybersecurity-aspects registers, that the Annex I Part II (1) identification duty has been discharged across the support period.
  ambiguity_notes: |
    The phrase "top-level dependencies" in Annex I Part II (1) is POLY-S2, because depth admits at least three materially distinct readings. Reading chosen: R1, where "top-level" maps to first-level direct dependencies with depth-1 look-through; this honours the OJ literal "at the very least the top-level dependencies" without forbidding deeper SBOMs at the manufacturer's discretion. Alternative readings: R2 (full transitive closure) is operationally heavier and not strictly required by the OJ text, though some sector profiles (medical devices, automotive) may exceed this baseline; R3 (critical-path-only) would let vendors omit categories that may matter under coordinated vulnerability disclosure timelines. The "commonly used and machine-readable" VAG+POLY S3 ambiguity is carried up into SR-CRA-008.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-008
  title: "Machine-readable SBOM format for supply-chain transparency"
  source_clauses:
    - { clause_id: CRA-CL143, article_ref: "Annex I Part II (1) — SBOM format" }
    - { clause_id: CRA-CL39, article_ref: "Art. 3(39) — SBOM definition (details and supply chain relationships)" }
  linked_objectives: [SO-CRA-007, SO-CRA-038]
  sub_domain: [D-06.2, D-02.1]
  nist_csf_mapping:
    - { id: ID.AM-02, title: "Inventories of software, services, and systems managed by the organization are maintained" }
    - { id: GV.SC-02, title: "Suppliers and other third parties are known, prioritized, and assessed using a cybersecurity supply chain risk management process" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Annex I Part II (1) requires the SBOM to be drawn up in a commonly used and machine-readable format covering at least the top-level dependencies. The CRA-defined SBOM artefact under Art. 3(39) is a formal record containing details and supply-chain relationships of the components included in the software elements of the product, so the format obligation in Annex I Part II (1) sits downstream of the definitional anchor in Art. 3(39). Art. 13(24) authorises the Commission to adopt implementing acts further specifying the format and elements of the SBOM, providing the formal route by which the "commonly used and machine-readable" floor will become binding. For a compliance officer this means selecting a format that supports automated downstream consumption, documenting the choice in the conformity dossier, and being prepared to migrate when the implementing acts specify a baseline.
  security_rationale: |
    The SBOM-format obligation in Annex I Part II (1) is operationalised in NIST CSF 2.0 through **ID.AM-02 (inventories of software, services, and systems managed by the organisation are maintained)** and **GV.SC-02 (suppliers and other third parties known, prioritised, and assessed using a cybersecurity supply-chain risk-management process)**. ID.AM-02 captures the format-side leg: the inventory must be queryable and automatable -- a "commonly used and machine-readable format" is the structural requirement that turns the inventory from a static artefact into an input to vulnerability-management automation, CVE matching, and downstream supply-chain risk assessment. GV.SC-02 anchors the supply-chain dimension: the format must encode supplier and supply-chain relationships (per the Art. 3(39) definition), so that the SBOM supports both vulnerability lookup and supplier-prioritisation under the broader cybersecurity supply-chain risk-management process. Together ID.AM-02 and GV.SC-02 enable the manufacturer to demonstrate ex post, through a queryable SBOM artefact, format-choice documentation in the conformity dossier, and supplier-prioritisation records, that the Annex I Part II (1) format obligation has been met in a manner interoperable with the CSIRT-side and MSA-side verification workflow.
  ambiguity_notes: |
    The phrase "commonly used and machine-readable format" is POLY+VAG S3 and admits three materially distinct readings tied to format families. Reading chosen: R3, treating the obligation as "any commonly-used machine-readable format that supports automated component identification," pending the Commission implementing acts under Art. 13(24). Alternative readings: R1 (a specific sector format such as SPDX or CycloneDX) and R2 (a different specific sector format) are both currently common in the market but neither is OJ-mandated at present; the executing-acts-dependent choice lets manufacturers pick what interoperates best with their tooling while preparing for the eventual binding specification. An additional reading, R5, would set the format floor to a domain-agnostic cryptographic manifest that any SBOM-aware toolchain can ingest regardless of origin sector, achieving interoperability through shared primitives rather than shared schemas; R5 is admitted as the long-run consensus direction but rejected for current OJ reading because Annex I does not specify such a manifest, leaving the implementing-acts route to harmonise rather than the SR body to import. Format names are intentionally not introduced into the SR body to honour the V12 tech-stack denylist. Remain open: (a) when the implementing acts specify a single binding format, does the choice bind retroactively across previously-published SBOMs or only prospectively for new releases; (b) does Annex I Part II (1) require that the SBOM be human-readable in addition to machine-readable, or is the format-agnostic floor purely automated.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-009
  title: "SBOM lifecycle retention and market-surveillance disclosure"
  source_clauses:
    - { clause_id: CRA-CL143, article_ref: "Annex I Part II (1) — SBOM contents" }
    - { clause_id: CRA-CL161, article_ref: "Annex VII §2(b) — SBOM in technical documentation" }
    - { clause_id: CRA-CL167, article_ref: "Annex VII §8 — SBOM on MSA request" }
  linked_objectives: [SO-CRA-007, SO-CRA-038]
  sub_domain: [D-06.2, D-02.1, D-09.4]
  nist_csf_mapping:
    - { id: ID.AM-02, title: "Inventories of software, services, and systems managed by the organization are maintained" }
    - { id: GV.SC-03, title: "Contracts with suppliers and other third parties are used to implement appropriate measures designed to meet the objectives of an organization's cybersecurity program and the organization's Cybersecurity Supply Chain Risk Management Plan" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS, TRIGGERED]
  regulatory_rationale: |
    Annex I Part II (1), Annex VII §2(b), and Annex VII §8 together require the manufacturer to draw up the SBOM in a commonly used and machine-readable format, retain it in the technical documentation across the support period under Annex VII §4, and — on reasoned request from a market surveillance authority — provide the SBOM where necessary for compliance checking. This three-anchored architecture separates authoring (Annex I Part II (1)), retention (Annex VII §2(b)), and regulatory disclosure (Annex VII §8), and the manufacturer must satisfy all three. For a compliance officer the operational consequence is an SBOM lifecycle: produced at product release, versioned across the support period, and made available to MSAs on request under the scope of what is "necessary."
  security_rationale: |
    The combined SBOM authoring / retention / disclosure architecture is operationalised in NIST CSF 2.0 through **ID.AM-02 (inventories of software, services, and systems managed by the organisation are maintained)** and **GV.SC-03 (contracts with suppliers and other third parties used to implement appropriate measures designed to meet the objectives of an organisation's cybersecurity program and the Cybersecurity Supply Chain Risk Management Plan)**. ID.AM-02 captures the persistent-inventory leg: the SBOM is not a snapshot at release but a maintained artefact that survives through the support period under Annex VII section 4 and the 10-year update-availability tail under Art. 13(9), with versioning evidence demonstrating that newly-disclosed CVEs can be matched against any historical release. GV.SC-03 anchors the regulatory-disclosure dimension: the contractual and procedural obligations owed to MSAs in their surveillance role -- including the Annex VII section 8 reasoned-request pathway -- are themselves elements of the supply-chain risk-management plan, and the SBOM-on-request capability is the audit trail that closes the loop between private inventory and third-party-verifiable compliance. Together ID.AM-02 and GV.SC-03 enable the manufacturer to demonstrate ex post, through documented SBOM versioning, retention records in the technical documentation under Annex VII section 2(b), and MSA-request response logs under Annex VII section 8, that the three-anchored SBOM lifecycle has been sustained across the support period.
  ambiguity_notes: |
    The Annex VII §8 phrase "where necessary in order for that authority to be able to check compliance" is VAG-S2 — necessary to what scope? Reading chosen: R1, where "necessary" is the subset of the SBOM directly relevant to the compliance question under investigation, not a comprehensive dump of every component. Alternative reading: R2 (full SBOM disclosure without scope filter) would over-disclose proprietary supply-chain relationships unrelated to the question and create an IP tension that Annex VII §8 does not require. The remaining S2/S3 ambiguities from SR-CRA-007 and SR-CRA-008 (top-level depth, format selection) carry up unchanged.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-010
  title: "Vulnerability remediation without delay after awareness"
  source_clauses:
    - { clause_id: CRA-CL144, article_ref: "Annex I Part II (2) — address and remediate without delay" }
    - { clause_id: CRA-CL132, article_ref: "Annex I Part I (2)(c) — vulnerabilities addressed through security updates" }
    - { clause_id: CRA-CL24, article_ref: "Art. 13(6) sentence 1 — component vulnerability address + remediate" }
  linked_objectives: [SO-CRA-008]
  sub_domain: [D-02.2]
  nist_csf_mapping:
    - { id: PR.PS-02, title: "Software is maintained, replaced, and removed commensurate with risk" }
    - { id: ID.RA-06, title: "Risk responses are chosen, prioritized, planned, tracked, and communicated" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Annex I Part II (2) requires manufacturers to address and remediate vulnerabilities without delay in relation to the risks posed to the product, including by providing security updates; the clause further specifies that, where technically feasible, security updates shall be provided separately from functionality updates. Annex I Part I (2)(c) carries the same address-via-updates duty into the part I properties and pairs it with user-facing update notification. Art. 13(6) sentence 1 applies the address-and-remediate duty to component vulnerabilities identified in integrated third-party components, so the obligation is not evaded by externalising components. For a compliance officer the operational reading is: a vulnerability, once identified, triggers a documented timeline running from awareness to remediation and to user-dissemination (the latter covered in SR-CRA-017), with the technical-feasibility carve-out logged in the conformity dossier.
  security_rationale: |
    The Annex I Part II (2) "address and remediate without delay" duty is operationalised in NIST CSF 2.0 through **PR.PS-02 (software maintained, replaced, and removed commensurate with risk)** and **ID.RA-06 (risk responses chosen, prioritised, planned, tracked, and communicated)**. PR.PS-02 captures the maintenance and replacement leg: software is maintained (patched, mitigated, or where necessary replaced) commensurate with the risk that the vulnerability poses, and the address-and-remediate timeline is a sub-stream of the broader software-maintenance lifecycle. ID.RA-06 anchors the response-management dimension: risk responses are chosen (patch versus mitigation), prioritised (by severity and exploit availability), planned (with milestone evidence), tracked (with progress records), and communicated (upstream to the SBOM owners, downstream to users under SR-CRA-017). Together PR.PS-02 and ID.RA-06 enable the manufacturer to demonstrate ex post, through documented remediation timelines, technical-feasibility carve-out records in the conformity dossier under Annex VII, and addressed-component evidence under Art. 13(6), that the "without delay" anchor has been exercised continuously from the awareness moment through to user-dissemination, and that the Art. 13(2) risk-assessment prioritisation remains in force as the pipeline progresses.
  ambiguity_notes: |
    The phrase "without delay" is VAG-S3 in the Berry-classic sense, structurally identical to "without undue delay" in GDPR Art. 33 and NIS 2 Art. 23(4)(a). Reading chosen: R1, where remediation action commences immediately on awareness and the ceiling is determined by the duration of the technical remediation pipeline, with record-keeping and advisory messages to users accompanying each remediation step. Alternative readings: R2 (delay permitted up to a calendar ceiling of N days regardless of pipeline duration) would risk creating a licence to delay beneath the headline obligation; R3 (subjective manufacturer discretion) is rejected as failing the inquiry-resistant test. An additional reading, R4, would characterise "without delay" as beginning at the moment of developer handoff rather than the moment of awareness, shifting the clock upstream to internal triage; R4 is rejected because the OJ text anchors the trigger at the manufacturer's knowledge rather than at developer assignment, but the operational consequence is identical where the manufacturer's process is tightly coupled. The COORD-S2 "address and remediate" conjunction is treated literally as both required, with "address" denoting the acknowledgement, triage, and communication step and "remediate" denoting the patch or mitigation. Remain open: (a) does the awareness clock pause while the manufacturer awaits confirmation from the reporter (CVD step), or does it run continuously from initial receipt; (b) when remediation requires changes that exceed a single release cycle (schema migration, dependency removal), does the literal "without delay" require partial mitigations to be deployed in the interim.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-012
  title: "Effective vulnerability handling across support period"
  source_clauses:
    - { clause_id: CRA-CL27, article_ref: "Art. 13(8) sentence 1 — handle vulnerabilities during support period" }
    - { clause_id: CRA-CL143, article_ref: "Annex I Part II (1) — identify + document" }
  linked_objectives: [SO-CRA-010]
  sub_domain: [D-02.2, D-04.2]
  nist_csf_mapping:
    - { id: ID.RA-06, title: "Risk responses are chosen, prioritized, planned, tracked, and communicated" }
    - { id: PR.PS-02, title: "Software is maintained, replaced, and removed commensurate with risk" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 13(8) sentence 1 requires manufacturers to ensure — at the moment of placing a product on the market and for the support period — that vulnerabilities of the product, including its components, are handled effectively and in accordance with the Annex I Part II cybersecurity requirements. The "including its components" phrase imports the SBOM-derived component boundary under Annex I Part II (1), so the handling obligation is not evaded by the integration of third-party libraries; the manufacturer's handling extends to weaknesses that surface inside any component within the SBOM scope. This rule frames the entire post-market handling lifecycle; SR-CRA-010 covers the remediation-by-update avenue, SR-CRA-022 covers periodic testing, SR-CRA-019 covers CVD policy, and SR-CRA-013 / SR-CRA-014 cover the temporal envelope.
  security_rationale: |
    The Art. 13(8) sentence 1 "handled effectively" obligation is operationalised in NIST CSF 2.0 through **ID.RA-06 (risk responses chosen, prioritised, planned, tracked, and communicated)** and **PR.PS-02 (software maintained, replaced, and removed commensurate with risk)**. ID.RA-06 anchors the response-tracking backbone: every vulnerability surfaced through the Annex I Part II (1) identification pipeline is associated with a chosen response (patch or mitigation), a priority level (driven by Art. 13(2) risk assessment), a plan (with milestone evidence), and tracked progress, with upstream and downstream communication nodes that bind the handling cycle together. PR.PS-02 anchors the maintenance leg: software is maintained across the support period under Art. 13(8) sentence 1's precommitment, including its components under the SBOM-derived component boundary, so the effective-handling duty is sustained for as long as the support period runs. Together ID.RA-06 and PR.PS-02 enable the manufacturer to demonstrate ex post, through documented vulnerability-handling records, response-tracking evidence in the technical documentation under Annex VII, and Art. 13(7) cybersecurity-aspects registers, that the Art. 13(8) "handled effectively" duty has been exercised across the support period and through the SBOM-derived component boundary, providing the operational foundation for the Annex VII section 6 test reports and Module B periodic audits under Annex VIII Part II (8).
  ambiguity_notes: |
    The phrase "handled effectively" is VAG-S3 because the criterion of effectiveness is not defined in the OJ text and admits materially different operational interpretations (R1 remediation always, R2 mitigation acceptable, R3 either). Reading chosen: R3, where the manufacturer selects the appropriate response (patch or workaround mitigation) and documents the choice in the risk-assessment update under Art. 13(7) and (14). Alternative readings: R1 (remediation-only) would prohibit interim mitigations that are often the only safe-path response in critical-infrastructure settings; R2 (mitigation-only) would let vendors skip patching indefinitely. An additional reading, R4, would treat "handled effectively" as a single composite — the manufacturer decides for each vulnerability whether patching or mitigation is the operative response, and the choice itself counts as handling; R4 is materially equivalent to R3 and is rejected as introducing no distinct compliance population beyond R3. The SCOPE-Q-S2 "including its components" is read under R2 (transitive dependency) as the dominant reading, anchored in Annex I Part II (1) SBOM inventory scope. Remain open: (a) does "handled effectively" require measurable service-level objectives (e.g., patch-deployment cadence, mitigation-effectiveness verification) or is procedural compliance with the risk-assessment update sufficient; (b) when a component goes end-of-life upstream during the product's support period, does the manufacturer inherit a duty to vendor-fix or migrate.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-013
  title: "Support-period determination using eight-factor methodology"
  source_clauses:
    - { clause_id: CRA-CL28, article_ref: "Art. 13(8) sentence 2 — support-period determination factors" }
    - { clause_id: CRA-CL29, article_ref: "Art. 13(8) sentence 3 — 5-year minimum" }
    - { clause_id: CRA-CL163, article_ref: "Annex VII §4 — support-period determination info" }
  linked_objectives: [SO-CRA-010, SO-CRA-061]
  sub_domain: [D-02.2, D-09.4]
  nist_csf_mapping:
    - { id: ID.IM-02, title: "Improvement processes for cybersecurity risk management are implemented across organizational tiers" }
    - { id: GV.OV-02, title: "The organizational cybersecurity risk management strategy is reviewed and adjusted to address changes in the organization's risk landscape (e.g., the threat environment, technology, regulations, standards)" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 13(8) sentence 2 requires manufacturers to determine the support period so that it reflects the length of time the product is expected to be in use, taking into account reasonable user expectations, the nature of the product including its intended purpose, relevant Union law determining the lifetime of products with digital elements, support periods of similar products by other manufacturers, the availability of the operating environment, the support periods of integrated components that provide core functions and are sourced from third parties, ADCO guidance, and Commission guidance. Art. 13(8) sentence 3 sets a hard minimum of five years, and Annex VII §4 carries the determination into the technical documentation so that the rationale is auditable. For a compliance officer this means a written support-period methodology that walks through each factor and lands on a documented number that meets or exceeds the 5-year floor.
  security_rationale: |
    The Art. 13(8) sentence 2/3 support-period determination obligation is operationalised in NIST CSF 2.0 through **ID.IM-02 (improvement processes for cybersecurity risk management implemented across organisational tiers)** and **GV.OV-02 (organisational cybersecurity risk-management strategy reviewed and adjusted to address changes in the risk landscape -- threat environment, technology, regulations, standards)**. ID.IM-02 captures the methodology-as-process leg: the support-period determination is not a snapshot but an institutionalised improvement process -- the eight factors in Art. 13(8) sentence 2 are a deliberation set rather than a checklist, and the methodology itself is reviewed across organisational tiers so that the determination remains defensible as deployment patterns evolve. GV.OV-02 anchors the strategic-review dimension: the support period interacts with the broader risk-management strategy, and as the threat landscape, technology baseline, regulatory environment, and standards posture change -- including the 10-year update-availability tail under Art. 13(9) -- the determination must remain aligned with the strategy. Together ID.IM-02 and GV.OV-02 enable the manufacturer to demonstrate ex post, through a written support-period methodology that walks through each factor, and through ongoing strategy-review records in the technical documentation under Annex VII section 4, that the determination meets or exceeds the 5-year floor and that the methodology has been exercised across the support period itself.
  ambiguity_notes: |
    The phrase "reasonable user expectations" is VAG-S3 because the criterion is case-law-laden and Berry-classic (cf. CRA-C28 in the v0.1 ambiguity catalogue, §3.2). Reading chosen: R2, anchoring expectations to what a reasonable user in the same product sector would expect, with the harmonised-standards layer and ADCO guidance as the structural benchmark. Alternative readings: R1 (subjective to the specific user) is rejected because it makes the obligation unenforceable; R3 (industry-standard) is materially equivalent to R2 and is admitted as a non-strict alternative under the same OJ literal. An additional reading, R4, would anchor expectations to the consumer-warranty norms of the relevant Member State, importing consumer-protection vocabulary into a cybersecurity obligation; R4 is rejected because consumer-warranty law varies across the Union and would compromise the level playing field that Annex I plus the support-period minimum is designed to deliver; harmonised standards and ADCO guidance remain the structurally sound anchor. Remain open: (a) where Art. 27 harmonised standards specify a category-specific support-period baseline (e.g., a 7-year default for industrial control), does the manufacturer's shorter determination bind or does the standard override; (b) does the support-period determination need to be re-justified at each substantial-modification event under Art. 13(10), or is the initial determination sufficient for the product family.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-014
  title: "Five-year minimum support period with end-date disclosure"
  source_clauses:
    - { clause_id: CRA-CL29, article_ref: "Art. 13(8) sentence 3 — at least five years" }
    - { clause_id: CRA-CL44, article_ref: "Art. 13(19) — end date at time of purchase" }
    - { clause_id: CRA-CL157, article_ref: "Annex II §7 — type of technical support + end-date" }
  linked_objectives: [SO-CRA-010, SO-CRA-061]
  sub_domain: [D-02.2]
  nist_csf_mapping:
    - { id: GV.PO-01, title: "Organizational cybersecurity policy is established, communicated, and enforced" }
    - { id: GV.OC-04, title: "Critical objectives, capabilities, and services that stakeholders depend on or expect from the organization are understood and communicated" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 13(8) sentence 3 fixes a hard minimum of five years for the support period — or the expected use time if shorter than five years — establishing a Union-wide floor that lifts the worst-case user-experience to a meaningful baseline. Art. 13(19) requires the end date, including at least the month and year, to be clearly and understandably specified at the time of purchase, so users enter the transactional relationship with full visibility of the timeline. Annex II §7 carries the same end-date into the user-facing information as part of the type of technical support offered, harmonising the back-end legal record with the front-end commercial disclosure. For a compliance officer the operational consequence is a support-period determination recorded in the technical documentation, with the end date published in the purchase-time materials under Annex II §7.
  security_rationale: |
    The Art. 13(8) sentence 3 + Art. 13(19) + Annex II section 7 hard-floor and end-date disclosure duty is operationalised in NIST CSF 2.0 through **GV.PO-01 (organisational cybersecurity policy established, communicated, and enforced)** and **GV.OC-04 (critical objectives, capabilities, and services that stakeholders depend on or expect from the organisation are understood and communicated)**. GV.PO-01 captures the policy-establishment and enforcement leg: the support period is anchored by an organisational cybersecurity policy that communicates and enforces the 5-year floor and the risk-assessment-modulated extensions beyond the floor, so that downstream users receive a consistent commitment regardless of which business unit is responsible. GV.OC-04 anchors the communication dimension: the support-period end date is one of the critical commitments that stakeholders depend on, and the Art. 13(19) + Annex II section 7 disclosure pathways ensure the end date is communicated to the user at the transactional moment with the month-and-year granularity required. Together GV.PO-01 and GV.OC-04 enable the manufacturer to demonstrate ex post, through documented policy enforcement records, Annex VII section 4 retention evidence, and Annex II section 7 user-facing materials, that the 5-year minimum has been met and that the end date has been disclosed with the granularity Art. 13(19) requires.
  ambiguity_notes: |
    The phrase "at least five years" in Art. 13(8) sentence 3 is VAG-S2: literal "at least" anchors the floor but does not cap it. Reading chosen: R2, where the duration is 5+ years depending on the Art. 13(8) sentence 2 factors, with the literal "at least" preserving a manufacturer choice to extend beyond the floor. R1 (exactly 5 years) is rejected on the literal "at least," and the "expected use time" carve-out for shorter-lived products is anchored in the manufacturer's risk-assessment-documentation record under Art. 13(3) + Annex VII §3/§4 — the carve-out does not lower the bar so much as it acknowledges a class of products where the support period is determined by usage rather than by the regulatory floor.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-015
  title: "Migration-only remediation carve-out for substantially modified versions"
  source_clauses:
    - { clause_id: CRA-CL34, article_ref: "Art. 13(10) — substantial-modification compliance scope (last version)" }
    - { clause_id: CRA-CL30, article_ref: "Art. 3(30) — substantial modification" }
  linked_objectives: [SO-CRA-060, SO-CRA-047]
  sub_domain: [D-02.2, D-07.4, D-09.4]
  nist_csf_mapping:
    - { id: PR.PS-02, title: "Software is maintained, replaced, and removed commensurate with risk" }
    - { id: GV.SC-04, title: "Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 13(10) provides that, where a manufacturer has placed subsequent substantially modified versions of a software product on the market, the manufacturer may ensure compliance with the Annex I Part II (2) vulnerability remediation requirement only for the version last placed on the market — provided that users of previously placed versions have access to the last-placed version free of charge and do not incur additional costs to adjust the hardware and software environment in which they use the original version. Art. 3(30) defines substantial modification through a disjunctive test covering both compliance impact and intended-purpose modification. For a compliance officer the carve-out permits a "migration-only" remediation strategy but the free-of-charge / no-adjustment-required constraint protects users from being coerced into migration, so the practical scope of the carve-out is narrower than the headline suggests.
  security_rationale: |
    The Art. 13(10) + Art. 3(30) substantial-modification carve-out is operationalised in NIST CSF 2.0 through **PR.PS-02 (software maintained, replaced, and removed commensurate with risk)** and **GV.SC-04 (suppliers and other third parties routinely assessed using audits, test results, or other forms of evaluation to confirm contractual obligations are met)**. PR.PS-02 captures the migration-only remediation strategy: rather than maintaining N parallel versions in parallel, the manufacturer consolidates remediation effort on the latest version and offers migration as the protection path for users on earlier versions -- the "replacement" leg of the Subcategory applies at the version level rather than the patch level. GV.SC-04 anchors the free-of-charge and no-adjustment-required dimension: third-party assessment (and self-assessment against the same standard) verifies that the migration offer is genuinely low-friction and that no user is operationally coerced into migration through hidden cost or hardware-software-environment adjustment burdens. Together PR.PS-02 and GV.SC-04 enable the manufacturer to demonstrate ex post, through documented version-management records, free-migration-offer evidence, and third-party assessment records, that the substantial-modification carve-out has been applied within its protective scope and that the user-coercion safeguard has been honoured.
  ambiguity_notes: |
    The phrase "substantial modification" inherits the Art. 3(30) definition, which is VAG+POLY S3 with three materially distinct readings. Reading chosen: R1 combined with R3, treating the Art. 3(30) literal disjunctive "affects compliance OR modifies intended purpose" as the operative test, so any change that crosses either threshold is substantial. Alternative readings: R1 alone (compliance impact only) would miss the intended-purpose dimension, where R3 alone (intended-purpose only) would miss the compliance dimension. An additional reading, R5, would apply "substantial modification" only at the boundary where compliance verification triggers anew under Annex VIII, importing the conformity-assessment notion into the modification definition; R5 reads the Art. 3(30) disjunction through a conformity lens and is admitted as a non-strict equivalent to R1+R3 when the implementation of substantial-modification checks already runs through conformity re-verification. The "free of charge" qualifier is POLY-S2 with R1 (no monetary cost) as the literal reading, which the SR preserves without imported carve-outs. Remain open: (a) how ADCO and the Commission interpret "additional costs to adjust the hardware and software environment" when a migration imposes modest operational friction that is hard to monetise; (b) whether the free-migration access must be perpetual or only for the residual support period of the original version.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-016
  title: "Ten-year update-availability tail beyond support period"
  source_clauses:
    - { clause_id: CRA-CL33, article_ref: "Art. 13(9) — 10-year update availability" }
  linked_objectives: [SO-CRA-011]
  sub_domain: [D-02.2, D-05.2]
  nist_csf_mapping:
    - { id: PR.PS-02, title: "Software is maintained, replaced, and removed commensurate with risk" }
    - { id: GV.OV-02, title: "The organizational cybersecurity risk management strategy is reviewed and adjusted to address changes in the organization's risk landscape (e.g., the threat environment, technology, regulations, standards)" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS, TRIGGERED]
  regulatory_rationale: |
    Art. 13(9) requires the manufacturer to ensure that each security update made available to users during the support period remains available after it has been issued for a minimum of 10 years or for the remainder of the support period, whichever is longer. The clause therefore creates a 10-year availability tail measured from the date of issue, layered on top of the support-period minimum under Art. 13(8). For a compliance officer this means: even when a product exits active support, the previously-issued security updates remain download-accessible to users who continue operating the product, and this availability survives product end-of-life as a Union-level baseline.
  security_rationale: |
    The Art. 13(9) 10-year-or-remainder update-availability tail is operationalised in NIST CSF 2.0 through **PR.PS-02 (software maintained, replaced, and removed commensurate with risk)** and **GV.OV-02 (organisational cybersecurity risk-management strategy reviewed and adjusted to address changes in the risk landscape -- threat environment, technology, regulations, standards)**. PR.PS-02 captures the artefact-availability leg: previously-issued security updates remain available to users who continue operating the product past the support period, with the maintained-software Subcategory interpreted at the artefact level (signed packages, version archives, integrity-protected catalogues) rather than at the active-patching level. GV.OV-02 anchors the strategic-review dimension: as the technology baseline and threat landscape evolve, the manufacturer must review its retention strategy against the Art. 13(9) floor, ensuring long-lived products (industrial, automotive, medical-device) remain within the operative availability envelope. Together PR.PS-02 and GV.OV-02 enable the manufacturer to demonstrate ex post, through documented update-archive records, retention-strategy reviews, and Annex VII section 4 retention evidence, that each issued security update has remained available for the maximum of its ten-year floor or its support-period remainder, whichever is longer.
  ambiguity_notes: |
    The phrase "whichever is longer" creates a twin-anchor (VAG-S2) pattern where the 10-year floor and the support-period remainder are compared, and the longer of the two applies in each case. Reading chosen: R2, where the calculation is performed case-by-case on a per-update basis — a long-support product may have many updates subject to the support-period remainder rather than the fixed 10-year floor. R1 (always 10 years) is rejected because it ignores the "whichever is longer" qualifier; the alternative R3 (always the support-period remainder) is similarly rejected because it ignores the 10-year floor when the support period is shorter than 10 years.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-017
  title: "Free-of-charge update dissemination with advisory messages"
  source_clauses:
    - { clause_id: CRA-CL150, article_ref: "Annex I Part II (8) — disseminate without delay, free of charge" }
    - { clause_id: CRA-CL132, article_ref: "Annex I Part I (2)(c) — notification of available updates" }
  linked_objectives: [SO-CRA-009]
  sub_domain: [D-02.2]
  nist_csf_mapping:
    - { id: PR.PS-02, title: "Software is maintained, replaced, and removed commensurate with risk" }
    - { id: RS.CO-03, title: "Information is shared with designated internal and external stakeholders consistent with the established information-sharing rules" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Annex I Part II (8) requires that, where security updates are available to address identified security issues, they are disseminated without delay, free of charge — unless otherwise agreed for a tailor-made product — accompanied by advisory messages providing users with the relevant information, including on potential action to be taken. Annex I Part I (2)(c) provides the symmetric counterpart on the user-facing notification side: vulnerabilities must be addressed through security updates, including — where applicable — through automatic security updates and through notification of available updates. For a compliance officer the dual architecture (Part II dissemination + Part I notification) means that the release process must publish both the binary artefact and the user-readable advisory, with the tailor-made carve-out documented at the contractual level.
  security_rationale: |
    The Annex I Part II (8) + Annex I Part I (2)(c) dissemination-with-advisory obligation is operationalised in NIST CSF 2.0 through **PR.PS-02 (software maintained, replaced, and removed commensurate with risk)** and **RS.CO-03 (information shared with designated internal and external stakeholders consistent with the established information-sharing rules)**. PR.PS-02 anchors the binary-artefact side: the security update itself is maintained in a form that is ready for dissemination (signed, packaged, integrity-protected) and the availability tail under Art. 13(9) covers it across the post-support window. RS.CO-03 captures the advisory-message leg: dissemination is not silent patch deployment but information-sharing with designated stakeholders -- users, integrators, downstream operators -- consistent with established sharing rules (CVD timelines, tailored-free dissemination rules, confidentiality of pre-disclosure information). Together PR.PS-02 and RS.CO-03 enable the manufacturer to demonstrate ex post, through documented dissemination records, advisory-archive evidence in the technical documentation under Annex VII, and information-sharing logs consistent with the CVD policy under SR-CRA-019, that the binary-and-advisory pair has been delivered without delay and free of charge across the user population subject to the tailor-made exception.
  ambiguity_notes: |
    The phrase "without delay" inherits the S3 ambiguity addressed in SR-CRA-010 and is treated identically — action commences immediately on awareness, with the ceiling set by the technical pipeline. The "unless otherwise agreed" carve-out in Annex I Part II (8) is POLY-S2 because "agreed" admits at least two materially distinct populations: Reading chosen: R1, the literal tailor-made product business-user agreement is the dominant reading, and consumer-product updates cannot be subject to charge under the carve-out. An additional reading, R3, would treat "without delay" as beginning at the moment the security update is technically ready, independent of any corporate release-cycle cadence — a stricter reading that effectively bans bundling security updates with feature releases; R3 is rejected where Annex I Part II (2) explicitly permits bundling under the "where technically feasible" qualifier, but the literal "without delay" from awareness remains the operative anchor. Remain open: (a) does "tailor-made" map onto the same Art. 6(a) proviso population used in SR-CRA-026, or is Annex I Part II (8) carving out a wider product class that lets enterprises negotiate subscription-based security-update access; (b) does Annex I Part II (8) require the advisory message to mention the option to file an Art. 14(8) user notification independently of the manufacturer's dissemination.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-018
  title: "Automatic security updates with user opt-out capability"
  source_clauses:
    - { clause_id: CRA-CL132, article_ref: "Annex I Part I (2)(c) — automatic security updates + opt-out + postponement" }
    - { clause_id: CRA-CL158, article_ref: "Annex II §8(e) — how the automatic-update default setting can be turned off" }
  linked_objectives: [SO-CRA-019, SO-CRA-009]
  sub_domain: [D-03.4, D-02.2]
  nist_csf_mapping:
    - { id: PR.PS-01, title: "Configuration management practices are established, documented, and applied to assets" }
    - { id: PR.DS-12, title: "Data is managed consistent with the organization's risk strategy to protect the confidentiality, integrity, and availability of data" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Annex I Part I (2)(c) requires vulnerabilities to be addressed through security updates, including — where applicable — through automatic security updates installed within an appropriate timeframe enabled as a default setting, with a clear and easy-to-use opt-out mechanism, through notification of available updates to users, and with the option to temporarily postpone them. Annex II §8(e) obliges the manufacturer to inform the user how the automatic-update default can be turned off, lifting the user's path from implication (the setting exists) to discoverability (the setting is documented). For a compliance officer the operational consequence is: auto-update on by default, opt-out discoverable and single-click, postponement available, and Annex II §8(e) disclosure present in the user-facing materials.
  security_rationale: |
    The Annex I Part I (2)(c) + Annex II section 8(e) auto-update-default and opt-out architecture is operationalised in NIST CSF 2.0 through **PR.PS-01 (configuration management practices established, documented, and applied to assets)** and **PR.DS-12 (data managed consistent with the organisation's risk strategy to protect the confidentiality, integrity, and availability of data)**. PR.PS-01 anchors the configuration-management dimension: the auto-update default is itself a configuration baseline that must be established, documented (in the technical documentation and the Annex II section 8(e) user-facing materials), and applied consistently across deployed instances -- the secure-by-default principle operationalised at the update channel level. PR.DS-12 captures the data-management side: the auto-update mechanism exists to preserve data CIA over time, and the opt-out and postponement options are risk-modulated choices that allow enterprise users and regulated industries to operate within controlled update windows without sacrificing the baseline. Together PR.PS-01 and PR.DS-12 enable the manufacturer to demonstrate ex post, through documented default configurations, configuration-change audit trails, and Annex II section 8(e) user-information records, that the auto-update default has been implemented consistent with Annex I Part I (2)(c) and that the user-autonomy safeguards (opt-out, postponement) have been preserved.
  ambiguity_notes: |
    The phrase "within an appropriate timeframe" in Annex I Part I (2)(c) is VAG-S3 in the Berry-classic "appropriate" sense (cf. GDPR Art. 32, NIS 2 Art. 21). Reading chosen: R2, anchoring the timeframe to the severity of the addressed vulnerability and the user's operational environment, modulated by the Art. 13(2) risk assessment. Alternative readings: R1 (a single quantitative ceiling for all vulnerabilities) is rejected because severity modulation is the operative sanity check; R3 (manufacturer discretion) is rejected as failing the inquiry-resistant test. The "clear and easy-to-use" qualifier is VAG-S2 with R1 (UI discoverable + single-click) as the literal reading, anchored in harmonised standards and Art. 7(4) Commission implementing acts. An additional reading, R5, would tie the timeframe to harmonised-standards baselines that specify a category-specific deployment window (industrial control, medical device, consumer IoT); R5 is admitted as the long-run consensus direction but is rejected for current OJ reading because Annex I Part I (2)(c) leaves the timeframe to the manufacturer's risk assessment, pending Art. 7(4) implementing acts that may specify defaults. Remain open: (a) does the opt-out obligation require that disabling auto-update also disable any active update channel that could silently re-enable, or merely that the toggle be respected once flipped; (b) when updates are bundled (security + functionality), must Annex I Part II (2)'s "where technically feasible" separation route the entire bundle through opt-in for the functionality part.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-019
  title: "Coordinated vulnerability disclosure policy publication"
  source_clauses:
    - { clause_id: CRA-CL147, article_ref: "Annex I Part II (5) — CVD policy" }
    - { clause_id: CRA-CL32, article_ref: "Art. 13(8) sentence 6 — CVD policy" }
    - { clause_id: CRA-CL103, article_ref: "Art. 24(3) — OSS steward Art. 14 extension cross-ref to CVD" }
  linked_objectives: [SO-CRA-012, SO-CRA-049]
  sub_domain: [D-02.3, D-09.1]
  nist_csf_mapping:
    - { id: GV.PO-01, title: "Organizational cybersecurity policy is established, communicated, and enforced" }
    - { id: GV.SC-04, title: "Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Annex I Part II (5) requires manufacturers to put in place and enforce a policy on coordinated vulnerability disclosure. Art. 13(8) sentence 6 lists the CVD policy among the appropriate policies a manufacturer shall have, integrating it with the wider support-period duty. OSS-steward policies under Art. 24(1) include CVD aspects per Art. 24(3), which extends the same architecture to stewards of open-source projects in scope. For a compliance officer this means a published, enforceable CVD policy that names intake channels, triage SLAs, disclosure expectations, and post-disclosure verification — typically aligned with ISO 29147 / ISO 30111 conventions or with sector-specific variants.
  security_rationale: |
    The Annex I Part II (5) + Art. 13(8) sentence 6 CVD policy obligation is operationalised in NIST CSF 2.0 through **GV.PO-01 (organisational cybersecurity policy established, communicated, and enforced)** and **GV.SC-04 (suppliers and other third parties routinely assessed using audits, test results, or other forms of evaluation to confirm contractual obligations are met)**. GV.PO-01 captures the published-and-enforced dimension: the CVD policy is a documented organisational cybersecurity policy that is communicated to researchers, integrators, and downstream operators, and the enforcement leg is what differentiates a real CVD programme from a static disclosure page. GV.SC-04 anchors the third-party-interaction leg: researcher interactions are a third-party channel that benefits from contractual clarity, and the CVD architecture (intake to triage to publication to verification) is the assessment pathway that confirms researcher-side expectations are met consistently with manufacturer-side commitments. Together GV.PO-01 and GV.SC-04 enable the manufacturer to demonstrate ex post, through a documented CVD policy, intake-channel evidence, triage-log records, and post-disclosure verification artefacts, that the Annex I Part II (5) policy-on-CVD duty has been put in place and enforced across the support period and that the policy meets the upstream enablement needs of the SR-CRA-021 contact-address and SR-CRA-020 public-disclosure rules.
  ambiguity_notes: |
    The phrase "policy on coordinated vulnerability disclosure" is POLY-S2 because three materially distinct policy architectures are admissible. Reading chosen: R3, a structured receive + triage + publish + post-disclosure verification pipeline, anchored in the implementing acts under Art. 14(9) and in Art. 17(5) EU vulnerability database integration. Alternative readings: R1 (ISO 29147 + ISO 30111-style structured policy, which is admissible) is a non-strict equivalent to R3; R2 (lighter disclosure-statement policy) is rejected because it fails the "enforce" element by omitting the triage and verification phases. The downstream contact-address expectation is developed separately in SR-CRA-021.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-021
  title: "Vulnerability contact address and single point of contact"
  source_clauses:
    - { clause_id: CRA-CL148, article_ref: "Annex I Part II (6) — vulnerability sharing + contact address" }
    - { clause_id: CRA-CL42, article_ref: "Art. 13(17) — single point of contact (manufacturer)" }
    - { clause_id: CRA-CL152, article_ref: "Annex II §2 — SPOC for vulnerability reporting" }
  linked_objectives: [SO-CRA-013]
  sub_domain: [D-02.3, D-09.1, D-09.4]
  nist_csf_mapping:
    - { id: GV.SC-04, title: "Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations" }
    - { id: RS.CO-03, title: "Information is shared with designated internal and external stakeholders consistent with the established information-sharing rules" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Annex I Part II (6) requires the manufacturer to take measures to facilitate the sharing of information about potential vulnerabilities in its product and in third-party components, including by providing a contact address for the reporting of vulnerabilities. Art. 13(17) requires a single point of contact, consolidating the manufacturer's external interface. Annex II §2 carries the SPOC and CVD-policy location into the user-facing information, harmonising the manufacturer's operational interface with what users see on the product label. For a compliance officer this means a stable, machine-discoverable contact address (security.txt / well-known URI being the typical implementation) plus a SPOC name and reference in the user information under Annex II §2.
  security_rationale: |
    The Annex I Part II (6) + Art. 13(17) + Annex II section 2 contact-address and SPOC architecture is operationalised in NIST CSF 2.0 through **GV.SC-04 (suppliers and other third parties routinely assessed using audits, test results, or other forms of evaluation to confirm contractual obligations are met)** and **RS.CO-03 (information shared with designated internal and external stakeholders consistent with the established information-sharing rules)**. GV.SC-04 anchors the third-party-conformance leg: the SPOC and contact address are the manufacturer's third-party-conformance anchors in the sense that researchers, integrators, and end users are operating under published contractual-equivalent expectations (intake channel, triage cadence, disclosure timeline), and the routine-assessment Subcategory ensures the contact surfaces remain stable and discoverable. RS.CO-03 captures the information-sharing dimension: the SPOC is the consolidated node through which vulnerability information flows -- the information-sharing-rules frame (CVD policy under SR-CRA-019, security.txt conventions, the Art. 13(17) external-interface anchor) -- providing the operational channel that turns a third-party report into a coordinated-disclosure pipeline. Together GV.SC-04 and RS.CO-03 enable the manufacturer to demonstrate ex post, through a stable SPOC record, machine-discoverable contact-address evidence (security.txt / well-known URI), and Annex II section 2 user-information records, that the intake architecture has been maintained in a form discoverable by automated researcher tooling.
  ambiguity_notes: |
    The phrase "contact address for the reporting of vulnerabilities" is POLY-S2 because three materially distinct channel types are admissible. Reading chosen: R3, requiring at minimum an email address published in a machine-discoverable location (security.txt or the well-known URI), with the freedom to expand into a secure web form or PGP-key-protected drop. Alternative readings: R1 (email only) is admitted as the floor; R2 (web form only without an email alternative) is rejected because it impairs automated researcher-tooling compatibility.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-023
  title: "Authentication identity and unique product identification"
  source_clauses:
    - { clause_id: CRA-CL133, article_ref: "Annex I Part I (2)(d) — appropriate control mechanisms incl. authentication, identity or access management" }
    - { clause_id: CRA-CL40, article_ref: "Art. 13(15) — type/batch/serial number or other element" }
    - { clause_id: CRA-CL153, article_ref: "Annex II §3 — name and type and unique identification" }
  linked_objectives: [SO-CRA-015, SO-CRA-056]
  sub_domain: [D-03.1, D-03.3, D-09.4]
  nist_csf_mapping:
    - { id: PR.AA-01, title: "Identities and credentials for authorized users, services, and hardware are managed by the organization" }
    - { id: ID.AM-01, title: "Inventories of hardware managed by the organization are maintained" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS, TRIGGERED]
  regulatory_rationale: |
    Annex I Part I (2)(d) requires protection from unauthorised access by appropriate control mechanisms, including but not limited to authentication, identity, or access-management systems; the "including but not limited to" clause keeps the floor open to other technical means while naming the three substantive control families. Art. 13(15) requires the product to bear a type, batch, or serial number or other element allowing identification. Annex II §3 requires name, type, and unique identification to be communicated to the user, harmonising the back-end physical marking with the front-end user information. For a compliance officer the operational reading is: pick an identification scheme that lets the SBOM and any security update be tied back to the specific unit, document the scheme under Annex VII, and disclose enough to the user that the user knows what they bought.
  security_rationale: |
    The Annex I Part I (2)(d) + Art. 13(15) + Annex II section 3 identification and authentication-control architecture is operationalised in NIST CSF 2.0 through **PR.AA-01 (identities and credentials for authorised users, services, and hardware managed by the organisation)** and **ID.AM-01 (inventories of hardware managed by the organisation are maintained)**. PR.AA-01 captures the identity-management leg: identities and credentials for users, services, and hardware are managed -- the Annex I Part I (2)(d) authentication + identity + access-management triad is the substantive control family that PR.AA-01 anchors, and the "including but not limited to" residual in (2)(d) is preserved through the Subcategory's identity-management rather than access-control scope. ID.AM-01 anchors the hardware-inventory dimension: the Art. 13(15) type/batch/serial-number marking plus Annex II section 3 unique-identification disclosure supply the identification backbone that downstream SBOM entries (under SR-CRA-007), vulnerability records (under SR-CRA-006), and security-update addressing (under SR-CRA-017) all depend on. Together PR.AA-01 and ID.AM-01 enable the manufacturer to demonstrate ex post, through documented identity-management records, hardware-inventory evidence in the technical documentation under Annex VII, and Annex II section 3 user-information records, that the identification backbone has been maintained in a form that supports authentication, authorisation, and audit across the deployed product population.
  ambiguity_notes: |
    The phrase "authentication, identity or access management systems" in Annex I Part I (2)(d) is COORD-S2, with three terms bound by OR. Reading chosen: R3, treating the three terms as distinct concepts rather than as synonyms (industry usage tends to collapse identity and access management into a single IAM discipline, but the OJ text preserves the distinction). R1 (closed list — only these three) is rejected on the literal "including but not limited to." No S3 instance is introduced on this rule; the SCOPE-Q question of whether "authentication" includes MFA-typical mechanisms or merely single-factor is a downstream issue that the harmonised-standards layer will eventually resolve without being a literal misquote in the SR.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-025
  title: "Secure-by-default configuration with reset capability"
  source_clauses:
    - { clause_id: CRA-CL131, article_ref: "Annex I Part I (2)(b) — secure by default configuration" }
    - { clause_id: CRA-CL2, article_ref: "Art. 6(a) proviso — properly installed, intended purpose, reasonably foreseeable" }
    - { clause_id: CRA-CL3, article_ref: "Art. 3(23) — intended purpose" }
  linked_objectives: [SO-CRA-018, SO-CRA-045]
  sub_domain: [D-03.4]
  nist_csf_mapping:
    - { id: PR.PS-01, title: "Configuration management practices are established, documented, and applied to assets" }
    - { id: PR.DS-12, title: "Data is managed consistent with the organization's risk strategy to protect the confidentiality, integrity, and availability of data" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS, TRIGGERED]
  regulatory_rationale: |
    Annex I Part I (2)(b) requires products to be made available on the market with a secure-by-default configuration — including the possibility to reset the product to its original state — unless otherwise agreed between manufacturer and business user in relation to a tailor-made product with digital elements. Art. 6(a) proviso anchors the configuration to intended purpose and reasonably foreseeable use, framing "secure" against the operational context the manufacturer reasonably anticipated. Art. 3(23) defines the intended purpose, providing the lexical anchor for what counts as "use" in the proviso. The combination addresses three obligations in one clause: default configuration, reset capability, and tailor-made carve-out.
  security_rationale: |
    The Annex I Part I (2)(b) + Art. 6(a) + Art. 3(23) secure-by-default obligation is operationalised in NIST CSF 2.0 through **PR.PS-01 (configuration management practices established, documented, and applied to assets)** and **PR.DS-12 (data managed consistent with the organisation's risk strategy to protect the confidentiality, integrity, and availability of data)**. PR.PS-01 anchors the configuration-baseline leg: the secure-by-default configuration is itself a documented configuration baseline, applied at first power-up to every unit leaving the manufacturing pipeline, with the configuration-change history auditable as part of the broader configuration-management practice. PR.DS-12 captures the data-management side: the secure-by-default configuration is the protective posture that determines which data CIA properties hold by default, with the reset-to-original-state capability providing the recovery path when a user has driven the configuration away from the secure baseline. Together PR.PS-01 and PR.DS-12 enable the manufacturer to demonstrate ex post, through documented baseline-configuration records, configuration-change audit trails, and reset-capability evidence in the technical documentation under Annex VII sections 2/6, that the secure-by-default floor has been applied at the point of market placement and that the reset capability has been preserved as the recovery path.
  ambiguity_notes: |
    The phrase "secure by default configuration" is VAG-S3 because three materially distinct configurations produce materially different compliance populations. Reading chosen: R2 — the security features (authentication, access control, audit logging, network segmentation, secure-update mechanism) are enabled by default at first power-up. Alternative readings: R1 (deny-all initial state, with the user explicitly enabling required services) and R3 (zero-config security, the product works securely without any user configuration) are operationally convergent with R2: all three require security features on at delivery, and only the configuration-management user-experience differs. An additional reading, R4, would extend the "secure by default" floor to the post-deployment configuration surface: any change the user makes from the default is documented and reversible through the reset mechanism; R4 is admitted as a strengthening of the chosen R2 reading and is rejected where it would conflict with the tailor-made carve-out, which permits negotiated non-default configurations in business-user settings. Remain open: (a) when a user explicitly changes a setting from the secure default and a subsequent vulnerability surfaces, does the manufacturer retain responsibility for the as-configured state or does the configuration shift break the Art. 13(2) risk-assessment chain; (b) does the "reset to original state" obligation require preserving user data through the reset (R3) or wiping it (R1/R2).
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-027
  title: "Product internal-activity recording with user opt-out"
  source_clauses:
    - { clause_id: CRA-CL141, article_ref: "Annex I Part I (2)(l) — recording + monitoring + user opt-out" }
    - { clause_id: CRA-CL158, article_ref: "Annex II §8 — detailed instructions" }
  linked_objectives: [SO-CRA-020, SO-CRA-068]
  sub_domain: [D-10.1, D-04.1]
  nist_csf_mapping:
    - { id: PR.PS-04, title: "Log records are generated and made available for continuous monitoring and analysis" }
    - { id: DE.AE-08, title: "Incidents are declared when adverse events meet the defined incident criteria" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Annex I Part I (2)(l) requires products with digital elements to provide security-related information by recording and monitoring relevant internal activity — including the access to or modification of data, services, or functions — with an opt-out mechanism for the user. The clause is the product-side mirror of the manufacturer-side access reporting under Annex I (2)(d) (SR-CRA-024) and is supported by Annex II §8, which requires the manufacturer to provide the user with detailed instructions on how the product records and monitors activity and how the opt-out can be exercised. For a compliance officer the operational reading is: log generation on by default, opt-out discoverable, instructions published under Annex II §8, and the security-event lifecycle properly interfaced with downstream incident-management obligations under Art. 14.
  security_rationale: |
    The Annex I Part I (2)(l) + Annex II section 8 internal-activity recording obligation is operationalised in NIST CSF 2.0 through **PR.PS-04 (log records generated and made available for continuous monitoring and analysis)** and **DE.AE-08 (incidents declared when adverse events meet the defined incident criteria)**. PR.PS-04 anchors the log-generation leg: the manufacturer instruments the product to generate log records covering the relevant-internal-activity data class identified by the Art. 13(2) risk assessment, with logs made available for the continuous-monitoring pipeline that consumes them. DE.AE-08 captures the incident-declaration dimension: the recorded events feed into the incident-criteria-evaluation pipeline so that events meeting the criteria are declared as incidents and routed into the Art. 14 reporting architecture (SR-CRA-028 / SR-CRA-031), closing the loop from local product-side recording to upstream regulatory notification. Together PR.PS-04 and DE.AE-08 enable the manufacturer to demonstrate ex post, through documented log-retention evidence, monitoring-pipeline records, and incident-declaration timestamps, that the (2)(l) recording duty has been exercised across the support period and that the upstream declaration pathway is operable when the recorded events meet the criteria.
  ambiguity_notes: |
    The phrase "opt-out mechanism for the user" in Annex I Part I (2)(l) is VAG-S2 because "opt-out" admits at least three materially distinct operational readings. Reading chosen: R1 (the user can disable logging entirely), preserving the literal OJ text. The opt-out creates a privacy-by-design tension: GDPR Art. 25 emphasises by-default-on privacy controls under certain readings, but the OJ CRA text on this clause is opt-out; rule preserves the OJ-literal opt-out interpretation rather than importing non-CRA framings. No S3 instance is introduced on this rule.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-045
  title: "Non-conformity corrective measures, withdrawal, or recall"
  source_clauses:
    - { clause_id: CRA-CL46, article_ref: "Art. 13(21) — corrective measures on non-conformity" }
    - { clause_id: CRA-CL30, article_ref: "Art. 3(30) — substantial modification (cross-ref for trigger)" }
  linked_objectives: [SO-CRA-063]
  sub_domain: [D-04.2, D-07.4, D-09.4]
  nist_csf_mapping:
    - { id: RS.MI-01, title: "Incidents are contained" }
    - { id: RS.MI-02, title: "Incidents are mitigated" }
    - { id: GV.OV-02, title: "The organizational cybersecurity risk management strategy is reviewed and adjusted to address changes in the organization's risk landscape (e.g., the threat environment, technology, regulations, standards)" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 13(21) requires manufacturers — from the placing on the market of the product and for the support period — who know or have reason to believe that the product with digital elements or the processes put in place by the manufacturer are not in conformity with the Annex I cybersecurity requirements to immediately take the corrective measures necessary to bring the product or processes into conformity, or to withdraw or recall the product, as appropriate. The text expressly covers both product-side and process-side non-conformity, recognising that a product can be Annex-I-conformant on its own merits even where the manufacturer's vulnerability-handling processes are deficient, and vice versa. The `know or have reason to believe` trigger mirrors the Article 14(1) awareness trigger language (cf. SR-CRA-039) — the same constructive-knowledge debate applies. The `or withdraw or recall` formulation gives the manufacturer the choice of remedy, but the choice is governed by the proportionality principle articulated across the Regulation.
  security_rationale: |
    The Article 13(21) non-conformity corrective-measures duty is operationalised in NIST CSF 2.0 through **RS.MI-01 (incidents contained)**, **RS.MI-02 (incidents mitigated)**, and **GV.OV-02 (organisational cybersecurity risk management strategy reviewed and adjusted to address changes in the risk landscape)**. RS.MI-01 captures the immediate-containment response: once non-conformity is known, the manufacturer isolates the affected product or process from further exposure, applying the corrective measure that brings the product or process back to conformity or removes it from the market. RS.MI-02 captures the mitigation dimension: the corrective measure is applied, and the residual risk is brought within acceptable bounds — fix, withdraw, or recall as appropriate, with the proportionality principle setting the choice. GV.OV-02 closes the strategic loop: the manufacturer's risk-management strategy is reviewed and adjusted against the change in circumstances that triggered the non-conformity, ensuring the same root cause does not recur. Together RS.MI-01, RS.MI-02, and GV.OV-02 enable the manufacturer to demonstrate ex post, through documented containment records, mitigation evidence, and strategy-review minutes, that the Article 13(21) duty has been discharged and that the proportionality of the chosen remedy (fix vs. withdraw vs. recall) is evidentially supported.
  ambiguity_notes: |
    `Immediately take the corrective measures necessary` is VAG+POLY-S2 — R1 (`immediately` = upon knowledge of non-conformity, in line with Article 14 awareness trigger; `corrective measures necessary` = the minimum set needed to restore conformity). `Withdraw or recall` is POLY-S2 — R1 (literal OR — either is admissible; the choice is the manufacturer's, governed by proportionality). The cross-reference to Article 3(30) substantial modification is significant: if the corrective measure requires a substantial modification, the Art. 22(1) third-party-modifier trigger may engage as well, transferring liability downstream. Remain open: (a) what regulatory practice crystallises around `have reason to believe` — i.e. whether constructive knowledge attaches upon receipt of an upstream-CVD report from a component supplier (per Article 13(6) in SR-CRA-051) or only upon internal verification of the non-conformity; (b) whether withdrawal versus recall is itself a proportionality determination that must be evidenced ex ante in the technical documentation under Annex VII.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-046
  title: "Product-design data minimisation adequate to intended purpose"
  source_clauses:
    - { clause_id: CRA-CL136, article_ref: "Annex I Part I (2)(g) — adequate, relevant, necessary = data minimisation" }
    - { clause_id: CRA-CL19, article_ref: "Art. 13(3) sentence 2 — intended purpose + reasonably foreseeable use" }
    - { clause_id: CRA-CL3, article_ref: "Art. 3(23) — intended purpose" }
  linked_objectives: [SO-CRA-034, SO-CRA-072]
  sub_domain: [D-05.1, D-07.1]
  nist_csf_mapping:
    - { id: PR.DS-12, title: "Data is managed consistent with the organization's risk strategy to protect the confidentiality, integrity, and availability of data" }
    - { id: ID.AM-03, title: "Inventories of data and corresponding metadata for designated data types are maintained" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Annex I Part I (2)(g) requires products with digital elements to process only data — personal or other — that are adequate, relevant, and limited to what is necessary in relation to the intended purpose of the product with digital elements. This is the CRA's data-minimisation principle, borrowing the GDPR Article 5(1)(c) language (`adequate, relevant and limited to what is necessary`) and applying it at the product-design level rather than at the controller-side processing level. Article 13(3) sentence 2 anchors the minimisation to the intended purpose (Article 3(23)) and to the reasonably foreseeable use derived from the cybersecurity risk assessment. Article 13(3) sentence 3 (cf. SR-CRA-066) requires the assessment to indicate whether and how the Annex I Part I (2) requirements apply and how they are implemented — providing the documented basis for the `necessary in relation to the intended purpose` determination.
  security_rationale: |
    The Annex I Part I (2)(g) data-minimisation principle is operationalised in NIST CSF 2.0 through **PR.DS-12 (data managed consistent with the organisation's risk strategy to protect confidentiality, integrity, and availability)** and **ID.AM-03 (inventories of data and corresponding metadata for designated data types maintained)**. PR.DS-12 captures the strategic-posture dimension: data is managed consistent with the manufacturer's risk strategy, with the Article 13(2) risk assessment supplying the proportionality bar that determines which data classes are adequate, relevant, and necessary for the product's intended purpose. ID.AM-03 anchors the operational-traceability dimension: inventories of data and corresponding metadata for designated data types are maintained, providing the demonstrable record that the manufacturer knows which data classes are present in the product and on what basis each class was admitted under the minimisation principle. Together PR.DS-12 and ID.AM-03 enable the manufacturer to demonstrate ex post, through risk-strategy alignment and data-inventory records in the technical documentation under Annex VII §2, that the (2)(g) minimisation principle has been discharged and that the product's data footprint is no broader than its intended purpose requires.
  ambiguity_notes: |
    The three coordinated adjectives — `adequate, relevant and limited to what is necessary` — carry VAG+POLY+COORD-S3 ambiguity. Reading chosen: R2 (proportionate to purpose, demonstrable ex ante via the Annex VII §3 risk-assessment record). R1 (literal reading of each adjective as an independent gate) and R3 (any single reading satisfies all three) are the alternative readings. The `intended purpose` term inherits the Article 3(23) D23 POLY-S2 classification — the intended purpose is a product-class-relative determination that the manufacturer documents in the technical documentation (Annex VII §3). Remain open: (a) whether the EDPB's forthcoming guidance on the CRA's intersection with GDPR Article 25 (data protection by design and by default) will supply a harmonised reading of `necessary in relation to intended purpose`; (b) the operational handling of minimisation when downstream integrators extend the intended purpose (e.g. via third-party plugins or configuration) — i.e. whether the manufacturer's documented minimisation suffices, or whether the integrator inherits a re-evaluation duty.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-047
  title: "Free, timely security-update dissemination across support period"
  source_clauses:
    - { clause_id: CRA-CL149, article_ref: "Annex I Part II (7) — secure update distribution" }
    - { clause_id: CRA-CL150, article_ref: "Annex I Part II (8) — dissemination without delay, free of charge" }
    - { clause_id: CRA-CL43, article_ref: "Art. 13(18) — accompany with Annex II info, accessible for 10 years" }
  linked_objectives: [SO-CRA-035, SO-CRA-009]
  sub_domain: [D-05.2, D-02.2]
  nist_csf_mapping:
    - { id: PR.PS-02, title: "Software is maintained, replaced, and removed commensurate with risk" }
    - { id: GV.OC-04, title: "Critical objectives, capabilities, and services that stakeholders depend on or expect from the organization are understood and communicated" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS, TRIGGERED]
  regulatory_rationale: |
    Annex I Part II (7) requires the manufacturer to securely distribute updates for products with digital elements — covering all applicable security updates. Annex I Part II (8) requires the manufacturer to disseminate security updates without delay, free of charge — accompanied by advisory messages — unless the manufacturer has duly justified and the user has agreed to a paid-for model in the context of a commercial relationship. Article 13(18) requires that the product be accompanied by the information and instructions specified in Annex II — including the secure-update and dissemination information — in paper or electronic form, accessible for the support period. The Article 13(9) `at least 10 years` tail applies by extension: the information must remain accessible for the support period or 10 years from the placing on the market, whichever is longer.
  security_rationale: |
    The Annex I Part II (7)+(8) secure-update-distribution duty is operationalised in NIST CSF 2.0 through **PR.PS-02 (software maintained, replaced, and removed commensurate with risk)** and **GV.OC-04 (critical objectives, capabilities, and services that stakeholders depend on or expect from the organisation are understood and communicated)**. PR.PS-02 captures the durability-of-protective-capability dimension: the manufacturer maintains the product's software across the support period and the 10-year update-availability tail, with security updates distributed as soon as they are available and the proportional bar set by the risk assessment. GV.OC-04 anchors the user-as-stakeholder dimension: the manufacturer understands and communicates to users the critical capabilities the user depends on, with the advisory messages required by (8) supplying the per-update communication channel and the Annex II information deliverable supplying the durable instruction layer. Together PR.PS-02 and GV.OC-04 enable the manufacturer to demonstrate ex post, through update-distribution logs and user-communication records, that the (7)+(8) secure-update duty has been discharged and that the free-of-charge / duly-justified dichotomy has been applied consistent with the proportionality principle.
  ambiguity_notes: |
    `Accessible for 10 years` is POLY-S2: R1 — the literal text of Article 13(18) reads `accessible for the support period + at least 10 years`, and the chosen reading preserves the conjunction (the longer of the two periods governs). R2 (10 years from the placing-on-market date, full stop) is rejected as narrower than the literal. The `without delay` qualifier from (8) is VAG+POLY-S3 — see SR-CRA-010 for the analysis; it carries forward consistently here. The `duly justified and agreed` (paid-update exception) is POLY-S2 — R1 (justification + bilateral agreement + commercial-relationship context — all three required). Remain open: (a) what facts constitute `duly justified` — whether harmonised criteria under Article 27 will constrain the use of the paid-update exception, particularly for critical-product categories covered by Annex III; (b) the operationalisation of `accompanied by advisory messages` — whether the minimum content is machine-readable CVSS vector, plain-language summary, or both, pending Commission implementing acts.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-050
  title: "Third-party component due diligence including non-commercial OSS"
  source_clauses:
    - { clause_id: CRA-CL23a, article_ref: "Art. 13(5) — due diligence on third-party components" }
    - { clause_id: CRA-CL48, article_ref: "Art. 3(48) — free and open-source software definition" }
  linked_objectives: [SO-CRA-037]
  sub_domain: [D-06.1, D-07.1]
  nist_csf_mapping:
    - { id: GV.SC-01, title: "A cybersecurity supply chain risk management program, strategy, objectives, policies, and processes are established and agreed to by organizational stakeholders" }
    - { id: GV.SC-02, title: "Suppliers and other third parties are known, prioritized, and assessed using a cybersecurity supply chain risk management process" }
    - { id: ID.RA-02, title: "Threat and vulnerability information received from internal and external sources is collected and used to support risk identification" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 13(5) requires manufacturers to exercise due diligence when integrating components sourced from third parties — including components of free and open-source software not made available on the market in the course of a commercial activity — so that those components do not compromise the cybersecurity of the product with digital elements. The phrase `due diligence` is a Berry-classic: it is a case-law-laden term imported from company law and M&A practice, and its operational content is supplied by the Annex VII §2 technical-documentation record and by the Article 13(2) risk assessment. The CRA's express inclusion of non-commercial OSS in the due-diligence scope — Article 3(48) — closes the largest supply-chain risk gap in modern software products: an upstream OSS dependency that is maintained by volunteers on a non-commercial basis is still subject to the manufacturer's due-diligence exercise, without converting the maintainer into a manufacturer. This is the key CRA-Unique reading: the OSS community's non-commercial posture does not transfer risk to the community; it transfers the duty to assess to the integrating manufacturer.
  security_rationale: |
    The Article 13(5) due-diligence duty is operationalised in NIST CSF 2.0 through **GV.SC-01 (cybersecurity supply chain risk management programme, strategy, objectives, policies, and processes established and agreed)**, **GV.SC-02 (suppliers and other third parties known, prioritised, and assessed using a cybersecurity supply chain risk management process)**, and **ID.RA-02 (threat and vulnerability information received from internal and external sources collected and used to support risk identification)**. GV.SC-01 captures the programme-governance layer: the manufacturer establishes and maintains a documented supply-chain risk management programme covering commercial and non-commercial OSS components. GV.SC-02 anchors the supplier-prioritisation and assessment process: components are inventoried, prioritised by criticality, and assessed against documented cybersecurity criteria. ID.RA-02 closes the threat-intelligence loop: external vulnerability information (CVE feeds, advisories, OSS-security mailing lists) is collected and used to refresh the risk picture for integrated components. Together GV.SC-01, GV.SC-02, and ID.RA-02 enable the manufacturer to demonstrate ex post, through documented programme governance, supplier-assessment records, and threat-intelligence feeds, that the (5) due-diligence duty has been discharged for both commercial and non-commercial OSS components.
  ambiguity_notes: |
    `Due diligence` carries VAG+POLY-S3 ambiguity. The reading chosen is R3 — both procedural (a documented vetting process, evidenced in Annex VII §2) and substantive (positive verification of supplier / component security posture). R1 (procedural only — paper-based) is rejected as insufficient; R2 (substantive only, without documentation) is rejected as falling short of the conformity-assessment evidentiary requirements. The Article 7 reference to OSS in Article 3(48) — and the Article 24 steward provisions (SR-CRA-072 to SR-CRA-074) — together draw the perimeter at which due-diligence gives way to the steward-policy interface. Remain open: (a) whether the implementing acts under Article 13(24) (cf. SR-CRA-052) will specify minimum due-diligence evidentiary content — e.g. signed attestations of CVE-monitoring posture, vulnerability-handling SLA disclosure — beyond what is recorded in Annex VII §2 today; (b) the operational status of `due diligence` for indirect dependencies (transitive depth beyond the SBOM top-level floor) where the manufacturer has no visibility — pending implementing-acts guidance.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-051
  title: "Component vulnerability reporting, remediation, and OSS sharing"
  source_clauses:
    - { clause_id: CRA-CL24, article_ref: "Art. 13(6) sentence 1 — report + address + remediate component vulnerabilities" }
    - { clause_id: CRA-CL25, article_ref: "Art. 13(6) sentence 2 — share with component supplier" }
  linked_objectives: [SO-CRA-037]
  sub_domain: [D-06.3, D-02.2]
  nist_csf_mapping:
    - { id: GV.SC-04, title: "Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations" }
    - { id: RS.MI-02, title: "Incidents are mitigated" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 13(6) sentence 1 requires the manufacturer — upon identifying a vulnerability in a component (including in an open-source component) integrated in the product with digital elements — to report the vulnerability to the person or entity manufacturing or maintaining the component and to address and remediate the vulnerability in accordance with the Annex I Part II vulnerability-handling requirements. Sentence 2 requires sharing of relevant code and documentation with the component supplier where the manufacturer has integrated an open-source software component. The two sentences together cover: (a) the upstream feedback path (report), (b) the in-product remediation (address + remediate per Annex I Part II), and (c) the OSS-specific cooperative path (share). The OSS-sharing limb recognises that an open-source maintainer may need code-level context to develop a fix, whereas a commercial supplier typically operates under a bilateral support contract.
  security_rationale: |
    The Article 13(6) component-vulnerability feedback loop is operationalised in NIST CSF 2.0 through **GV.SC-04 (suppliers and other third parties routinely assessed against contractual obligations)** and **RS.MI-02 (incidents mitigated)**. GV.SC-04 captures the upstream-feedback dimension: the manufacturer notifies the component maintainer of an identified vulnerability and supplies the cooperative code / documentation context where the component is open-source, with the assessment record showing that the upstream-feedback duty has been discharged consistent with the contract / community norm. RS.MI-02 anchors the in-product mitigation dimension: the manufacturer addresses and remediates the vulnerability in their own product per Annex I Part II, with the patch publication and the deployed-fix evidence in the technical documentation supplying the mitigation record. Together GV.SC-04 and RS.MI-02 enable the manufacturer to demonstrate ex post, through upstream-notification logs and in-product remediation evidence, that the (6) feedback loop has been closed and that the CVD coordination upstream has been matched by the patch publication downstream.
  ambiguity_notes: |
    `Address AND remediate` is COORD-S2: R1 (both — distinct actions; `address` encompasses risk evaluation and the planned response, `remediate` is the deployment of the fix). `In an open-source component` is POLY-S2 — R1 (broad — any open-source component integrated into the product, regardless of licensing model). The relationship between Article 13(6) and Article 14 reporting is residual-and-not-reported: an isolated component vulnerability is the Article 13(6) duty; a vulnerability that becomes an actively-exploited vulnerability or a severe incident in the manufacturer's own product is the Article 14 reporting duty. Remain open: (a) the practical interplay with Article 14 where the upstream component vulnerability materialises into an incident affecting the manufacturer's product — whether two separate notification streams are required, or whether a single incident-report discharges both; (b) the treatment of legally-protected vulnerability disclosures (e.g. third-party bug-bounty findings) under sentence 2's cooperative-sharing limb — i.e. whether the manufacturer can withhold code-level diagnostic information without breaching the duty.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-052
  title: "Machine-readable SBOM covering top-level dependencies"
  source_clauses:
    - { clause_id: CRA-CL143, article_ref: "Annex I Part II (1) — SBOM covering at least top-level dependencies" }
    - { clause_id: CRA-CL49, article_ref: "Art. 13(24) — Commission implementing acts on SBOM format" }
  linked_objectives: [SO-CRA-038]
  sub_domain: [D-06.2]
  nist_csf_mapping:
    - { id: ID.AM-02, title: "Inventories of software, services, and systems managed by the organization are maintained" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Annex I Part II (1) requires the manufacturer to draw up an SBOM in a commonly used and machine-readable format covering at least the top-level dependencies of the product with digital elements. Article 13(24) authorises the Commission to adopt implementing acts further specifying the format and elements of the SBOM — a forward-looking clause that anticipates standardisation work under the Cyber Resilience Act (cf. the European standards organisations' CEN/CENELEC mandate under Article 27 and Recital 60 on harmonised standards). The Annex I Part II (1) floor is `top-level dependencies`; the implementing acts may raise the floor for specific product categories. The obligation extends across Annex VII §2(b) (technical-documentation inclusion — see SR-CRA-053) and Annex II §9 (manufacturer's discretion on user-facing accessibility — see SR-CRA-053).
  security_rationale: |
    The Annex I Part II (1) SBOM duty is operationalised in NIST CSF 2.0 through **ID.AM-02 (inventories of software, services, and systems managed by the organisation are maintained)**. ID.AM-02 is the operative Subcategory here: the SBOM is the most specific operational expression of the software-inventory principle in the product-side cybersecurity domain, with the machine-readable format qualifier (SPDX, CycloneDX, SWID) supplying the queryable interface that defenders use to correlate upstream CVEs against the product's dependency surface. ID.AM-02 anchors the SBOM as a maintained, current inventory — not a one-time generation but a continuously-updated artefact that tracks dependency changes across the support period. The implementation gap (top-level vs. transitive depth) is filled by the Article 13(24) implementing-acts process; until that process crystallises, ID.AM-02 with the literal `top-level` floor is the proportionate baseline. The ID.AM-02 inventory enables the manufacturer to demonstrate ex post, through the documented SBOM in the technical documentation under Annex VII §2(b), that the (1) SBOM duty has been discharged and that downstream vulnerability matching can be performed against the maintained dependency surface.
  ambiguity_notes: |
    `Top-level dependencies` is POLY-S2 — R1 (depth-1 — the immediate dependencies of the product, not transitive chains). R2 (transitive to N levels) is rejected as exceeding the literal `top-level` text. R3 (risk-based depth) is preserved as the rationale behind future implementing-acts expansion. Article 13(24) implementing acts will expand the floor to deeper depths for specific product categories — noted in the SR record but not asserted here. The `commonly used and machine-readable format` qualifier is POLY-S2 — R1 (formats accepted by the day-to-day tooling ecosystem; SPDX/CycloneDX/SWID satisfy this). Remain open: (a) whether the implementing acts will mandate a single format or accept the existing multi-format ecosystem, and whether backward-compatibility requirements will govern format migration; (b) the operational threshold for `top-level` in products with non-trivial dynamic-linking or runtime-fetched modules — i.e. whether `top-level` extends to dynamic dependencies resolved at install time, or only to statically declared direct dependencies.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-064
  title: "Three-phase design, development, and production of products"
  source_clauses:
    - { clause_id: CRA-CL14, article_ref: "Art. 13(1) — design/development/production per Annex I Part I" }
    - { clause_id: CRA-CL129, article_ref: "Annex I Part I (1) — chapeau" }
  linked_objectives: [SO-CRA-045]
  sub_domain: [D-07.1, D-09.2]
  nist_csf_mapping:
    - { id: PR.PS-06, title: "Secure software development practices are integrated, and their performance is monitored throughout the SDLC" }
    - { id: GV.PO-02, title: "Cybersecurity processes and procedures for implementing the cybersecurity policy are established, communicated, and enforced" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 13(1) requires the manufacturer — when placing a product with digital elements on the market — to ensure that the product has been designed, developed, and produced in accordance with the essential cybersecurity requirements set out in Part I of Annex I. Annex I Part I (1) sets the chapeau of `appropriate level of cybersecurity based on the risks`, which propagates to the 13 sub-points (2)(a)–(m) treated in SR-CRA-001 onwards. The chapeau is the proportionality anchor: the level of cybersecurity implemented must be appropriate to the risks, with the risk assessment supplied by Article 13(2) and the documentation under Article 13(3) read with Annex VII §3. The three coordinated verbs — `designed, developed and produced` — map to three lifecycle phases and the obligation must be discharged at each.
  security_rationale: |
    The Article 13(1) umbrella design-and-development duty is operationalised in NIST CSF 2.0 through **PR.PS-06 (secure software development practices integrated, and their performance monitored throughout the SDLC)** and **GV.PO-02 (cybersecurity processes and procedures for implementing the cybersecurity policy established, communicated, and enforced)**. PR.PS-06 is the operative Subcategory: the three coordinated verbs — `designed, developed, produced` — map to three lifecycle phases of the SDLC, and PR.PS-06 requires secure-development practices to be integrated and their performance monitored throughout. GV.PO-02 anchors the process-and-procedure layer: the implementation of the cybersecurity policy is operationalised through documented processes that span the three lifecycle phases, with the policy implementation evidence recorded in the technical documentation under Annex VII §2. Together PR.PS-06 and GV.PO-02 enable the manufacturer to demonstrate ex post, through documented SDLC evidence and process records, that the (1) umbrella duty has been discharged at each of the three lifecycle phases and that every Annex I Part I (2) sub-point is anchored in a documented process.
  ambiguity_notes: |
    `Designed, developed and produced` is COORD-S2 — three coordinated verbs. Reading chosen: R1 (three distinct phases — each must comply with Annex I Part I). R2 (composite description of a single integrated activity) is rejected as vulnerable to a partial-compliance reading — a manufacturer who only addressed the design phase and not the production phase could invoke the composite reading. The Article 13(2) risk assessment (SR-CRA-065) is the operational anchor for the proportionality of the level implemented. Remain open: (a) whether ongoing production-process drift (cf. Article 13(14), SR-CRA-069) re-fires the Article 13(1) requirement, or whether Article 13(14) is a separate continuous-conformity anchor — pending harmonised practice; (b) the demarcation between `produced` (the manufacturer's own production) and the supply-chain-incorporation of third-party components, which is treated separately in Article 13(5) (SR-CRA-050).
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-065
  title: "Lifecycle cybersecurity risk assessment including health-and-safety impact"
  source_clauses:
    - { clause_id: CRA-CL15, article_ref: "Art. 13(2) sentence 1 — cybersecurity risk assessment" }
    - { clause_id: CRA-CL16, article_ref: "Art. 13(2) sentence 1 — 6-phase lifecycle propagation" }
    - { clause_id: CRA-CL17, article_ref: "Art. 13(2) sentence 2 — health + safety of users" }
  linked_objectives: [SO-CRA-045, SO-CRA-053]
  sub_domain: [D-07.1, D-09.2]
  nist_csf_mapping:
    - { id: ID.RA-05, title: "Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response decisions" }
    - { id: PR.PS-06, title: "Secure software development practices are integrated, and their performance is monitored throughout the SDLC" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [PERIODIC, CONTINUOUS]
  regulatory_rationale: |
    Article 13(2) sentence 1 requires the manufacturer — for the purpose of complying with paragraph 1 — to undertake an assessment of the cybersecurity risks associated with the product and to take the outcome of that assessment into account during the planning, design, development, production, delivery, and maintenance phases of the product, with a view to minimising cybersecurity risks, preventing incidents, and minimising their impact. Sentence 2 adds the impact-to-health-and-safety-of-users qualifier — CRA-unique (no direct GDPR / NIS 2 / DORA equivalent). The six phases — planning through maintenance — propagate the same risk picture from initial threat model (planning) through maintenance (post-market updates). The health-and-safety qualifier is the cyber-physical bridge: physical harm arising from a compromised product (e.g. a vulnerable medical device or industrial controller) is in scope.
  security_rationale: |
    The Article 13(2) lifecycle risk-assessment duty is operationalised in NIST CSF 2.0 through **ID.RA-05 (threats, vulnerabilities, likelihoods, and impacts used to understand inherent risk and inform risk response decisions)** and **PR.PS-06 (secure software development practices integrated throughout the SDLC)**. ID.RA-05 is the operative Subcategory: threats, vulnerabilities, likelihoods, and impacts are identified, recorded, and used to understand inherent risk and inform the manufacturer's risk-response decisions, with the health-and-safety qualifier ensuring that physical-harm scenarios are within the impact assessment. PR.PS-06 anchors the six-phase lifecycle propagation: the risk picture is integrated into each of the six phases (planning, design, development, production, delivery, maintenance), with the SDLC-process evidence recorded per phase in the technical documentation. Together ID.RA-05 and PR.PS-06 enable the manufacturer to demonstrate ex post, through documented threat-vulnerability-impact records and per-phase SDLC evidence, that the (2) lifecycle risk-assessment duty has been discharged and that the health-and-safety impact qualifier has been considered across all six phases.
  ambiguity_notes: |
    `Planning, design, development, production, delivery and maintenance` is COORD-S3 — six coordinated phases. Reading chosen: R1 (all six required). R3 (`take into account` preserves partial compliance — some phases may not require full integration) is rejected in favour of the Annex I literal — each phase must take the assessment outcome into account. `Health and safety` is POLY-S2: R3 (both — physical + psychological harm arising from a compromised product). `Users` is SCOPE-Q-S2: R3 (natural + legal persons). The relationship to the GDPR DPIA (Article 35) is illustrative — the CRA risk assessment is broader in scope (product-cybersecurity) but narrower in audience (users of the product) than the GDPR DPIA. Remain open: (a) whether the Commission's implementing-acts guidance will crystallise what counts as `taking into account` at each phase — i.e. a minimum evidentiary step per phase; (b) the operational interaction with the GDPR DPIA when the product processes personal data — whether the CRA risk assessment can substitute for the GDPR DPIA's data-protection-specific subset, or whether both must be conducted.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-066
  title: "Documented, updated risk assessment in technical documentation"
  source_clauses:
    - { clause_id: CRA-CL18, article_ref: "Art. 13(3) sentence 1 — documented and updated" }
    - { clause_id: CRA-CL19, article_ref: "Art. 13(3) sentence 2 — intended purpose + reasonably foreseeable use" }
    - { clause_id: CRA-CL20, article_ref: "Art. 13(3) sentence 3 — Annex I Part I (2) applicability" }
    - { clause_id: CRA-CL162, article_ref: "Annex VII §3 — risk-assessment documentation in technical documentation" }
  linked_objectives: [SO-CRA-053, SO-CRA-054]
  sub_domain: [D-09.2, D-09.4, D-07.1]
  nist_csf_mapping:
    - { id: ID.RA-05, title: "Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response decisions" }
    - { id: GV.OV-02, title: "The organizational cybersecurity risk management strategy is reviewed and adjusted to address changes in the organization's risk landscape (e.g., the threat environment, technology, regulations, standards)" }
    - { id: GV.PO-02, title: "Cybersecurity processes and procedures for implementing the cybersecurity policy are established, communicated, and enforced" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [PERIODIC, CONTINUOUS]
  regulatory_rationale: |
    Article 13(3) sentence 1 requires the cybersecurity risk assessment to be documented and updated as appropriate during the support period. Sentence 2 requires the assessment to comprise at least an analysis of risks based on the intended purpose and reasonably foreseeable use, as well as the conditions of use — operational environment, assets to be protected, expected lifetime. Sentence 3 requires the assessment to indicate whether and, if so in what manner, the Annex I Part I (2) requirements are applicable and how they are implemented. Annex VII §3 requires the assessment to be in the technical documentation. The three sentences together operationalise the documentation and content-of-record requirements; Annex VII §3 supplies the storage destination.
  security_rationale: |
    The Article 13(3) documented-and-updated risk-assessment duty is operationalised in NIST CSF 2.0 through **ID.RA-05 (threats, vulnerabilities, likelihoods, and impacts used to understand inherent risk and inform risk response decisions)**, **GV.OV-02 (organisational cybersecurity risk management strategy reviewed and adjusted to address changes in the risk landscape)**, and **GV.PO-02 (cybersecurity processes and procedures for implementing the cybersecurity policy established, communicated, and enforced)**. ID.RA-05 anchors the risk-driven-response function: the documented assessment comprises the threat-vulnerability-likelihood-impact analysis that informs the manufacturer's risk-response decisions. GV.OV-02 captures the update dimension: the strategy is reviewed and adjusted against changes in the threat environment, technology, regulations, and standards — operationalising the `updated as appropriate` duty. GV.PO-02 anchors the process layer: the assessment-and-update cycle is implemented through documented processes, with the resulting artefact recorded in the technical documentation under Annex VII §3. Together ID.RA-05, GV.OV-02, and GV.PO-02 enable the manufacturer to demonstrate ex post, through documented risk-assessment records, update-decision evidence, and process artefacts in the technical documentation, that the (3) documentation duty has been discharged and that the assessment has remained current across the support period.
  ambiguity_notes: |
    `Documented and updated as appropriate during a support period` carries VAG-S2: R4 (material change in product / threat landscape / on becoming aware of vulnerability — Article 13(14) update anchor). R1 (fixed-period update — annual review) is rejected as over-prescriptive; R2 (`as appropriate` only at the manufacturer's initiative) is rejected as failing to operationalise the duty; R3 (any material change as the manufacturer determines) is rejected as under-prescriptive. `Intended purpose AND reasonably foreseeable use` (COOR-S3): R1 (both required — cumulative). `Whether and, if so in what manner` is POLY-S2: R1 (selective applicability of Annex I Part I (2) requirements — not all 13 sub-points apply to every product class, and the assessment must show the selection rationale). Remain open: (a) the operational frequency of `as appropriate` — i.e. whether harmonised practice will specify minimum review triggers beyond material change; (b) the relationship to the manufacturer's information-society obligations under NIS 2 (entity-level risk assessment) — whether the CRA product-side assessment supplies evidence that can be carried into the NIS 2 entity-level assessment.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-069
  title: "Series-of-production conformity and harmonised-standards monitoring"
  source_clauses:
    - { clause_id: CRA-CL39, article_ref: "Art. 13(14) — series-of-production conformity" }
  linked_objectives: [SO-CRA-047]
  sub_domain: [D-07.4, D-09.4]
  nist_csf_mapping:
    - { id: GV.OV-01, title: "Cybersecurity risk management strategy outcomes are reviewed and adjusted to ensure they adequately address organizational risks" }
    - { id: GV.PO-02, title: "Cybersecurity processes and procedures for implementing the cybersecurity policy are established, communicated, and enforced" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 13(14) requires the manufacturer to ensure that procedures are in place for products with digital elements that are part of a series of production to remain in conformity with this Regulation, and to keep the regulator informed of relevant changes in harmonised standards and common specifications. The duty has two limbs: (a) a procedural limb (procedures in place for series-production conformity); (b) an informational limb (inform regulator of relevant changes in harmonised standards / common specifications). Each limb has distinct evidence requirements — the procedural limb must be evidenced in the technical documentation (Annex VII), and the informational limb is delivered via the regulator-information channel.
  security_rationale: |
    The Article 13(14) series-of-production conformity duty is operationalised in NIST CSF 2.0 through **GV.OV-01 (cybersecurity risk management strategy outcomes reviewed and adjusted to ensure they adequately address organisational risks)** and **GV.PO-02 (cybersecurity processes and procedures for implementing the cybersecurity policy established, communicated, and enforced)**. GV.OV-01 captures the strategy-outcomes-review dimension: the manufacturer reviews the strategy outcomes — including the series-production conformity procedure — and adjusts them to ensure the conformity obligation is met across production runs. GV.OV-01 also anchors the informational limb: harmonised-standards monitoring is part of the strategy review, and the regulator is informed of relevant changes through the documented oversight channel. GV.PO-02 anchors the process layer: the series-production conformity procedure is implemented as a documented process with operational discipline, with the procedural evidence recorded in the technical documentation under Annex VII §2. Together GV.OV-01 and GV.PO-02 enable the manufacturer to demonstrate ex post, through documented strategy-review records and process artefacts, that the (14) series-production conformity duty has been discharged and that the regulator-information channel has been maintained across the support period.
  ambiguity_notes: |
    `Series of production` is POLY-S2: R1 (lot / batch — narrow) or R2 (continuous production — broad). Reading chosen: R2 (continuous production — captures modern software-as-a-service delivery where every release is a new production event). R1 is rejected as too narrow for the software product context that the CRA explicitly includes. `Remain in conformity` is VAG-S2: R1 (conformity preserved via a documented process — i.e. process discipline, not per-unit re-examination). Remain open: (a) the operational threshold for `relevant changes in harmonised standards` — i.e. whether the manufacturer must inform of every OJ publication or only those that alter the presumption of conformity for the product class; (b) the operational interface with the substantial-modification trigger (Article 13(10), SR-CRA-070) — i.e. when does a series-of-production improvement become `substantial`.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-070
  title: "Substantial-modification compliance scope across supply chain"
  source_clauses:
    - { clause_id: CRA-CL34, article_ref: "Art. 13(10) — substantial-modification compliance scope" }
    - { clause_id: CRA-CL96, article_ref: "Art. 21 — manufacturer-equivalent trigger" }
    - { clause_id: CRA-CL97, article_ref: "Art. 22(1) — third-party substantial modification" }
    - { clause_id: CRA-CL30, article_ref: "Art. 3(30) — substantial modification definition" }
  linked_objectives: [SO-CRA-047, SO-CRA-060]
  sub_domain: [D-07.4, D-06.4]
  nist_csf_mapping:
    - { id: PR.PS-02, title: "Software is maintained, replaced, and removed commensurate with risk" }
    - { id: GV.SC-04, title: "Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations" }
  applies_to_role: [MANUFACTURER, IMPORTER, DISTRIBUTOR]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    The Articles 13(10), 21, and 22 architecture treats substantial modification as the trigger for manufacturer-equivalent status, with the Article 13(10) carve-out allowing compliance with Annex I Part II (2) for the last-placed version of the product where the user-migration conditions are met (i.e. the user is given the choice to migrate to the modified product or to retain the last-placed version). Article 21 (SR-CRA-061) addresses the importer/distributor trigger; Article 22 (SR-CRA-062) addresses the third-party modifier trigger; Article 13(10) provides the manufacturer's own substantial-modification compliance scope.
  security_rationale: |
    The Article 13(10) + 21 + 22 substantial-modification architecture is operationalised in NIST CSF 2.0 through **PR.PS-02 (software maintained, replaced, and removed commensurate with risk)** and **GV.SC-04 (suppliers and other third parties routinely assessed against contractual obligations)**. PR.PS-02 captures the version-management dimension: the substantial-modification threshold is the boundary between normal-version-update and manufacturer-equivalent liability transfer, and PR.PS-02 supplies the risk-commensurate maintenance discipline that distinguishes the two. GV.SC-04 anchors the supply-chain-coordination dimension: the importer, distributor, and third-party modifier assessments (Articles 21, 22) are operationalised through the supply-chain contractual-and-procedural tests that determine when the manufacturer-equivalent status fires. Together PR.PS-02 and GV.SC-04 enable the manufacturer, importer, distributor, or third-party modifier to demonstrate ex post, through documented version-management records and supply-chain assessment evidence, that the substantial-modification boundary has been correctly applied and that the manufacturer-equivalent status has been appropriately assumed or retained.
  ambiguity_notes: |
    `Substantial modification` inherits Article 3(30) D30 — VAG+POLY+COORD-S3. See SR-CRA-061/R-CRA-015 for the full reading across this threshold. R1 (any non-compliance change) + R3 (intended-purpose modification) admitted as the disjunctive literal reading. The Article 13(10) carve-out — allowing Annex I Part II (2) compliance for the last-placed version subject to user-migration — is POLY-S2 — R1 (the carve-out is conditional on user choice; the manufacturer cannot unilaterally apply it). Remain open: (a) the operational demarcation between security updates (which rarely meet the substantial-modification threshold) and security features whose modification would meet the substantial-modification threshold — pending harmonised practice; (b) whether the substantial-modification test must be re-run at every release (formal), or only at material risk-relevant changes (substantive) — the BERs harmonised standards under Article 27 will likely converge on the latter.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-071
  title: "User-facing and integrator-facing secure-use instructions"
  source_clauses:
    - { clause_id: CRA-CL158, article_ref: "Annex II §8(a)–(f) — detailed instructions" }
    - { clause_id: CRA-CL43, article_ref: "Art. 13(18) — accompany with Annex II info" }
  linked_objectives: [SO-CRA-048]
  sub_domain: [D-08.1, D-09.4]
  nist_csf_mapping:
    - { id: PR.AT-01, title: "All users are informed and trained on cybersecurity topics (e.g. recognition of phishing, social engineering, and other relevant risks)" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS, TRIGGERED]
  regulatory_rationale: |
    Annex II §8 requires the product to be accompanied by detailed instructions — or an internet address referring to such detailed instructions and information — covering: (a) the necessary measures during initial commissioning and throughout the lifetime of the product to ensure its secure use; (b) how changes to the product can affect the security of data; (c) how security-relevant updates can be installed; (d) the secure decommissioning of the product, including information on how user data can be securely removed; (e) how the default setting enabling the automatic installation of security updates, as required by Annex I Part I (2)(c), can be turned off; (f) — where the product is intended for integration into other products — the information necessary for the integrator to comply with the Annex I cybersecurity requirements and the Annex VII documentation requirements. Article 13(18) extends this to a duty to provide the instructions in paper or electronic form, accessible for the support period.
  security_rationale: |
    The Annex II §8 detailed-instructions duty is operationalised in NIST CSF 2.0 through **PR.AT-01 (all users informed and trained on cybersecurity topics — including recognition of phishing, social engineering, and other relevant risks)**. PR.AT-01 captures the workforce-side awareness function for the Annex II §8(f) integrator dimension: integrators who incorporate the product into a downstream system are informed of the cybersecurity measures required to maintain Annex I compliance, with the awareness channel being the Annex II §8(f) information deliverable. The downside — flagged in the unmapped_csf_justification — is that PR.AT-01 scopes the workforce, not the end user; the SR retains the mapping for the workforce-side (integrator) of Annex II §8(f) and marks the user-side as UNMAPPED_CSF. The Annex II §8(a)–(e) user-side instructions remain documented as the device-side analogue of workforce awareness, with the support-period accessibility of Article 13(18) ensuring the information deliverable is durable. PR.AT-01 — applied to the integrator scope — enables the manufacturer to demonstrate ex post, through the documented Annex II §8(f) integrator information, that the workforce-awareness dimension of the instructions duty has been discharged.
  ambiguity_notes: |
    `Detailed instructions or an internet address` carries POLY+SCOPE-Q-S2: R3 (either — paper OR URL — both are admitted). `Throughout the lifetime of the product` is POLY-S2: R1 (the entire supported lifetime + 10-year update tail). The user-as-recipient framing is distinct from PR.AT-01 (workforce); PR.AT-01 is a stretch but defensible for the integrator-side (f) of Annex II §8 — flagged for downstream review in `unmapped_csf_justification`. Remain open: (a) the operational threshold for `detailed` — i.e. whether harmonised standards will specify minimum content elements per sub-clause (a)–(f); (b) the lifecycle demarcation when the 10-year update-availability tail (cf. SR-CRA-047) requires the instructions to remain accessible past the support period — pending Annex VII retention guidance.
  unmapped_csf_justification: |
    Annex II §8 instructions address the USER (a product's end-user), not the WORKFORCE (the manufacturer's or operator's employees). NIST CSF 2.0 PR.AT-01 trains the workforce; there is no direct CSF 2.0 Subcategory for end-user instructions on secure product use. The closest analogue is PR.AT-01 (workforce awareness) — the security rationale holds but the scope is workforce, not customer. Marking SR-CRA-071 as UNMAPPED_CSF for the user-facing side while retaining the workforce-side mapping would be a more honest interpretation. The SR retains the PR.AT-01 mapping for the integrator-side (f) of Annex II §8 (which addresses workforce integrators).
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-075
  title: "Manufacturer CVD policy and support-period documentation cluster"
  source_clauses:
    - { clause_id: CRA-CL32, article_ref: "Art. 13(8) sentence 6 — appropriate policies including CVD" }
    - { clause_id: CRA-CL147, article_ref: "Annex I Part II (5) — CVD policy" }
    - { clause_id: CRA-CL28, article_ref: "Art. 13(8) sentence 2 — support-period factors" }
  linked_objectives: [SO-CRA-051]
  sub_domain: [D-09.1, D-02.3]
  nist_csf_mapping:
    - { id: GV.PO-01, title: "Organizational cybersecurity policy is established, communicated, and enforced" }
    - { id: GV.PO-02, title: "Cybersecurity processes and procedures for implementing the cybersecurity policy are established, communicated, and enforced" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 13(8) sentence 6 requires the manufacturer to have appropriate policies including a CVD policy. Annex I Part II (5) requires the CVD policy itself — with the manufacturer to publish and promote a coordinated vulnerability disclosure policy. Article 13(8) sentence 2 requires the support-period determination methodology, including the factors enumerated. Together these constitute the manufacturer's policies cluster: CVD policy + support-period methodology + the documentary basis on which Annex VII §2(b) records both. The CVD policy under Annex I Part II (5) is the operational instrument that defines how external security researchers, users, and other stakeholders report vulnerabilities to the manufacturer.
  security_rationale: |
    The Article 13(8) + Annex I Part II (5) policies cluster duty is operationalised in NIST CSF 2.0 through **GV.PO-01 (organisational cybersecurity policy established, communicated, and enforced)** and **GV.PO-02 (cybersecurity processes and procedures for implementing the cybersecurity policy established, communicated, and enforced)**. GV.PO-01 captures the policy-instrument layer: the CVD policy under Annex I Part II (5) and the support-period-determination methodology under Article 13(8) sentence 2 are both established, communicated (to security researchers, users, and other stakeholders via publication and promotion), and enforced through the documented policy framework. GV.PO-02 anchors the implementation-process layer: the policies are operationalised through documented processes — the CVD coordination workflow, the support-period calculation procedure, the policy-update mechanism — with the implementation evidence recorded in the technical documentation under Annex VII §2(b). Together GV.PO-01 and GV.PO-02 enable the manufacturer to demonstrate ex post, through the documented policy bundle and the process artefacts, that the Article 13(8) + Annex I Part II (5) policies-cluster duty has been discharged and that the CVD coordination function is operative.
  ambiguity_notes: |
    `Policies` is POLY-S2: R1 (the CVD + support-period-determination policies, plus any other policies the manufacturer chooses to document — minimum is the CVD and support-period). No S3 in this SR. The interplay with Article 24(1) OSS-steward policy (SR-CRA-072) is residual — the steward's policy and the manufacturer's policy are distinct instruments with distinct evidentiary purposes. Remain open: (a) the operational threshold for `appropriate` CVD policies — i.e. whether harmonised standards under Article 27 will specify minimum CVD-policy elements (e.g. security.txt, SLA for acknowledgement, time-to-triage target), analogous to ISO/IEC 29147 / 30111; (b) the relationship between this SR's CVD policy and Article 14 reporting — i.e. whether the CVD policy is the upstream funnel whose output feeds the Article 14 reporting tiers.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-076
  title: "Cessation-of-operations notification to MSAs and users"
  source_clauses:
    - { clause_id: CRA-CL48, article_ref: "Art. 13(23) — cessation of operations notification" }
  linked_objectives: [SO-CRA-065, SO-CRA-051]
  sub_domain: [D-09.4]
  nist_csf_mapping:
    - { id: GV.OC-04, title: "Critical objectives, capabilities, and services that stakeholders depend on or expect from the organization are understood and communicated" }
    - { id: GV.OV-02, title: "The organizational cybersecurity risk management strategy is reviewed and adjusted to address changes in the organization's risk landscape (e.g., the threat environment, technology, regulations, standards)" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 13(23) requires a manufacturer that ceases its operations — and as a result is not able to comply with this Regulation — to inform, before the cessation of operations takes effect, the relevant market surveillance authorities and — by any means available and to the extent possible — the users of the relevant products with digital elements placed on the market, of the impending cessation. The duty is the lifecycle-end counterpart to the placing-on-market duty under Article 13: a manufacturer that has placed products on the market has a continuing responsibility that survives the manufacturer's operational continuity, and the failure mode of an unannounced cessation is the trigger.
  security_rationale: |
    The Article 13(23) cessation-of-operations notification duty is operationalised in NIST CSF 2.0 through **GV.OC-04 (critical objectives, capabilities, and services that stakeholders depend on or expect from the organisation are understood and communicated)** and **GV.OV-02 (organisational cybersecurity risk management strategy reviewed and adjusted to address changes in the risk landscape)**. GV.OC-04 captures the stakeholder-communication dimension: the manufacturer understands and communicates to MSAs and users the cessation of critical capabilities and services the user depends on, with the pre-cessation notification supplying the durable record that downstream defenders and users can rely on for continued product stewardship. GV.OV-02 anchors the strategy-review dimension: the cessation is itself a change in the risk landscape, and the manufacturer's risk-management strategy must be reviewed and adjusted to reflect the operational exit — operationalising the proportionality principle and the orderly-wind-down requirements. Together GV.OC-04 and GV.OV-02 enable the manufacturer to demonstrate ex post, through documented cessation-notification records and strategy-review evidence, that the Article 13(23) duty has been discharged and that downstream stakeholders have been informed in time to arrange alternative stewardship.
  ambiguity_notes: |
    `Before the cessation takes effect` is POLY-S2: R1 (no fixed temporal anchor — literal `before` + `as appropriate`). R2 (e.g. 30 days before) is rejected as introducing an unstated numerical floor; the literal phrasing preserves flexibility. The `to the extent possible` qualifier (user notification) is POLY-S2 — R1 (the manufacturer uses the means reasonably available; the duty does not require a heroic outreach effort). Remain open: (a) the operational handling when the manufacturer has ceased operations before the notification could be made — i.e. whether the insolvency practitioner / liquidator inherits the duty; (b) the interface with Article 23(1) economic-operator identification (SR-CRA-063) — i.e. whether the manufacturer must identify to the MSA the next-in-line economic operator (importer, AR) responsible for ongoing supply-chain information, enabling continued MSA contact.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-079
  title: "Documented and updated cybersecurity risk assessment"
  source_clauses:
    - { clause_id: CRA-CL18, article_ref: "Art. 13(3) sentence 1 — documented and updated" }
    - { clause_id: CRA-CL21, article_ref: "Art. 13(4) sentence 1 — include risk assessment in technical documentation" }
  linked_objectives: [SO-CRA-053]
  sub_domain: [D-09.4, D-09.2]
  nist_csf_mapping:
    - { id: GV.PO-02, title: "Cybersecurity processes and procedures for implementing the cybersecurity policy are established, communicated, and enforced" }
    - { id: ID.RA-05, title: "Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response decisions" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 13(3) sentence 1 requires the manufacturer to document the
    cybersecurity risk assessment referred to in Article 13(2) and to keep
    that assessment updated as appropriate during the support period.
    Article 13(4) sentence 1 then requires the manufacturer — when placing
    a product on the market — to include that risk assessment in the
    technical documentation required under Article 31 and Annex VII. The
    assessment is therefore both a documented activity and an artefact
    sitting inside the technical-documentation package that a notified
    body, market-surveillance authority, or conformity-assessment body may
    inspect [Recital 23].
  security_rationale: |
    The Art. 13(3)/(4) documented-and-updated risk assessment is
    operationalised in NIST CSF 2.0 through GV.PO-02 and ID.RA-05. GV.PO-02
    (Cybersecurity processes and procedures for implementing the
    cybersecurity policy are established, communicated, and enforced)
    anchors the process discipline of writing the assessment down,
    retaining version history, and re-running it on material-change
    triggers during the support period. ID.RA-05 (Threats, vulnerabilities,
    likelihoods, and impacts are used to understand inherent risk and
    inform risk response decisions) anchors the substantive content of the
    assessment — the threat-vulnerability-impact reasoning that selects
    which Annex I Part I requirements apply. Together, GV.PO-02 and ID.RA-05
    give the manufacturer a single document that can be re-opened at any
    point in the support period and used to demonstrate ex post that the
    Annex I applicability selection tracked both the product evolution and
    the threat-landscape evolution.
  ambiguity_notes: |
    The phrase "as appropriate during a support period" introduces a
    trigger question: which events warrant a re-write versus an addendum?
    Operational practice anchors to material changes in the product, its
    threat environment, the regulatory landscape, or new vulnerability
    awareness, but the regulation does not prescribe a cadence. The S2
    qualifier inherits from the parallel reading chosen at SR-CRA-066 for
    the same phrase.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-081
  title: "Systematic always-current cybersecurity record"
  source_clauses:
    - { clause_id: CRA-CL26, article_ref: "Art. 13(7) — systematic documentation of cybersecurity aspects" }
    - { clause_id: CRA-CL14, article_ref: "Art. 13(14) — series-of-production changes in harmonised standards" }
  linked_objectives: [SO-CRA-054]
  sub_domain: [D-09.2, D-09.4]
  nist_csf_mapping:
    - { id: GV.OV-02, title: "The organizational cybersecurity risk management strategy is reviewed and adjusted to address changes in the organization's risk landscape (e.g., the threat environment, technology, regulations, standards)" }
    - { id: ID.IM-04, title: "Cybersecurity risk management improvements are informed by awareness of related developments and context (e.g., threat intelligence, incidents, technology evolution)" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 13(7) requires the manufacturer to systematically document, in
    a manner proportionate to the nature and the cybersecurity risks of the
    product, relevant cybersecurity aspects — including vulnerabilities of
    which the manufacturer becomes aware and relevant information provided
    by third parties — and to update the cybersecurity risk assessment
    where applicable. Article 13(14) obliges the manufacturer to keep the
    market-surveillance authorities informed of any changes to the
    harmonised standards supporting its conformity assessment. Both
    provisions together construct an "always-current" record duty that
    connects the SDLC risk process to the published regulatory landscape
    [Recital 24, Recital 26].
  security_rationale: |
    The Art. 13(7)/(14) always-current record duty is operationalised in
    NIST CSF 2.0 through GV.OV-02 and ID.IM-04. GV.OV-02 (The organizational
    cybersecurity risk management strategy is reviewed and adjusted to
    address changes in the organization's risk landscape) anchors the
    periodic re-baselining of the risk assessment when the threat
    environment, technology, regulations, or standards shift. ID.IM-04
    (Cybersecurity risk management improvements are informed by awareness
    of related developments and context) anchors the intake of new
    third-party information — vulnerability advisories, OSS-steward
    disclosures, CSIRT alerts, CVD reports — into the record. Together,
    GV.OV-02 and ID.IM-04 give the manufacturer a controlled-update loop
    that can demonstrate ex post that every relevant change in the
    threat, regulatory, or standards landscape was captured and reflected
    in the technical documentation.
  ambiguity_notes: |
    "As appropriate" is the standard update-trigger qualifier across
    Article 13 — it covers material changes in the product, the threat
    landscape, the regulatory catalogue, and new vulnerability awareness,
    treated in combination rather than as separate triggers. "Relevant
    third-party information" includes integrator disclosures, OSS-steward
    advisories, CSIRT alerts, and coordinated-vulnerability-disclosure
    (CVD) reports received through the single point of contact.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-082
  title: "Single point of contact for vulnerability reporting"
  source_clauses:
    - { clause_id: CRA-CL42, article_ref: "Art. 13(17) — single point of contact" }
    - { clause_id: CRA-CL152, article_ref: "Annex II §2 — SPOC for vulnerability reporting" }
  linked_objectives: [SO-CRA-055]
  sub_domain: [D-09.4, D-02.3]
  nist_csf_mapping:
    - { id: GV.SC-04, title: "Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations" }
    - { id: RS.CO-03, title: "Information is shared with designated internal and external stakeholders consistent with the established information-sharing rules" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 13(17) requires the manufacturer to designate a single point of
    contact to enable users to communicate directly and rapidly with the
    manufacturer — including to facilitate the reporting of vulnerabilities
    of the product with digital elements. The single point of contact must
    allow users to choose their preferred means of communication and shall
    not limit those means to automated tools. Annex II §2 makes the SPOC
    address — and the location of the manufacturer's coordinated-
    vulnerability-disclosure (CVD) policy — part of the information that
    must accompany the product [Recital 25].
  security_rationale: |
    The Art. 13(17)/Annex II §2 single point of contact is operationalised
    in NIST CSF 2.0 through GV.SC-04 and RS.CO-03. GV.SC-04 (Suppliers and
    other third parties are routinely assessed using audits, test results,
    or other forms of evaluation to confirm they are meeting their
    contractual obligations) anchors the SPOC as a third-party-facing
    interface that is monitored for its effectiveness in receiving
    external security signals — the manufacturer evaluates whether the
    SPOC channel is actually being used or whether researchers are
    routing around it. RS.CO-03 (Information is shared with designated
    internal and external stakeholders consistent with the established
    information-sharing rules) anchors the SPOC's role inside the
    information-sharing rules defined by the CVD policy. Together,
    GV.SC-04 and RS.CO-03 give the manufacturer a public, auditable
    entry point that the CSA-EU and CSIRT can test for reachability and
    that the manufacturer can demonstrate ex post was operational
    throughout the support period.
  ambiguity_notes: |
    Two structural ambiguities shape the implementation. "Single point of
    contact" reads literally as one address (postal, email, or URL), not
    one channel with multiple addresses, and not a functional role spread
    across teams. "Shall not limit such means to automated tools" reads
    literally as a requirement that at least one non-automated channel
    (typically an inbox reachable by a human within a publishable SLA) be
    offered, alongside any automated intake. Both choices are anchored in
    the OJ-literal text and the recital's emphasis on user choice.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-083
  title: "Bidirectional product and manufacturer identification"
  source_clauses:
    - { clause_id: CRA-CL40, article_ref: "Art. 13(15) — product identification (type/batch/serial)" }
    - { clause_id: CRA-CL41, article_ref: "Art. 13(16) — manufacturer contact info on product" }
    - { clause_id: CRA-CL151, article_ref: "Annex II §1 — manufacturer contact info" }
    - { clause_id: CRA-CL153, article_ref: "Annex II §3 — product unique identification" }
  linked_objectives: [SO-CRA-056]
  sub_domain: [D-09.4]
  nist_csf_mapping:
    - { id: PR.AA-01, title: "Identities and credentials for authorized users, services, and hardware are managed by the organization" }
    - { id: GV.OC-04, title: "Critical objectives, capabilities, and services that stakeholders depend on or expect from the organization are understood and communicated" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS, TRIGGERED]
  regulatory_rationale: |
    Article 13(15) requires products to bear a type, batch, or serial
    number or other element allowing their identification. Article 13(16)
    requires the product to indicate the manufacturer's name, registered
    trade name, or registered trademark, and a postal address, email or
    other digital contact, and — where applicable — a website. Annex II §1
    and §3 carry the same content into the user-facing information that
    accompanies the product, including in the case of software products
    that are delivered without physical media. Together they establish a
    bidirectional identification chain: every unit of the product is
    traceable, and every unit can be traced back to its manufacturer.
  security_rationale: |
    The Art. 13(15)/(16) and Annex II §1/§3 identification chain is
    operationalised in NIST CSF 2.0 through PR.AA-01 and GV.OC-04. PR.AA-01
    (Identities and credentials for authorized users, services, and
    hardware are managed by the organization) anchors the manufacturer's
    duty to maintain a stable, verifiable product identity — type, batch,
    or serial number — that can be referenced in incident reports, recall
    campaigns, and CSA re-certifications. GV.OC-04 (Critical objectives,
    capabilities, and services that stakeholders depend on or expect from
    the organization are understood and communicated) anchors the
    manufacturer-identity leg of the chain — name, trademark, postal and
    digital contact — as a critical, expected-to-be-communicated element
    of the manufacturer's stakeholder interface. Together, PR.AA-01 and
    GV.OC-04 give the manufacturer a bidirectional identification record
    that the CSA-EU or CSIRT can use to route Art. 14 reports and that the
    manufacturer can demonstrate ex post as the source-of-truth for
    supply-chain attribution.
  ambiguity_notes: |
    The coordination "type, batch or serial number or other element"
    admits any one of those identifiers as the minimum, though multiple
    identifiers strengthen forensic traceability. The coordination "name,
    registered trade name or registered trademark" admits any one of the
    three as the legal-identity anchor; the rest are optional supplements.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-084
  title: "Ten-year documentation retention for economic operators"
  source_clauses:
    - { clause_id: CRA-CL38, article_ref: "Art. 13(13) — 10-year documentation retention" }
    - { clause_id: CRA-CL91, article_ref: "Art. 19(6) — importer 10-year retention" }
    - { clause_id: CRA-CL100, article_ref: "Art. 23(2) — economic-operator 10-year retention" }
  linked_objectives: [SO-CRA-057]
  sub_domain: [D-09.4]
  nist_csf_mapping:
    - { id: GV.OC-03, title: "Legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed" }
    - { id: GV.SC-04, title: "Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations" }
  applies_to_role: [MANUFACTURER, IMPORTER, DISTRIBUTOR]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 13(13) requires the manufacturer to keep the technical
    documentation and the EU declaration of conformity at the disposal of
    the market-surveillance authorities for at least 10 years after the
    product has been placed on the market, or for the support period,
    whichever is longer. Article 19(6) applies the same retention duty to
    the importer — Art. 19(6) covers the EU declaration + technical
    documentation, anchored to the manufacturer's package. Article 23(2)
    applies a parallel 10-year retention to economic operators for
    supply-chain identification information (their suppliers and
    recipients).
  security_rationale: |
    The Art. 13(13)/19(6)/23(2) 10-year retention is operationalised in
    NIST CSF 2.0 through GV.OC-03 and GV.SC-04. GV.OC-03 anchors the
    legal-recordkeeping posture: the manufacturer, importer, and
    distributor each know which artefacts they must hold for the
    retention window and can produce them on a reasoned MSA request.
    GV.SC-04 (Suppliers and other third parties are routinely assessed
    using audits, test results, or other forms of evaluation to confirm
    they are meeting their contractual obligations) anchors the
    cross-economic-operator chain — the importer's and distributor's
    recordkeeping is treated as a third-party evidence base that the
    manufacturer can rely on for its own retention duty, and vice versa.
    Together, GV.OC-03 and GV.SC-04 give each economic operator a clear
    accountability line for the documents in their possession and let
    the chain as a whole demonstrate ex post that conformity evidence
    remained available across the full 10-year (or longer) window
    regardless of which entity ceased operations first.
  ambiguity_notes: |
    "Whichever is longer" resolves to the longer of the two periods (the
    10-year floor or the support period). "At the disposal of the market
    surveillance authorities" means available on request — not necessarily
    pre-submitted, but retrievable on a reasoned request. The Article
    19(6) importer retention covers the manufacturer's documentation
    chain; Article 23(2) covers the importer's own supply-chain
    identification record (different artefact, same 10-year floor).
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-085
  title: "Pre-market documentation, declaration, and CE marking chain"
  source_clauses:
    - { clause_id: CRA-CL36, article_ref: "Art. 13(12) sentence 1 — technical documentation + conformity assessment before placing" }
    - { clause_id: CRA-CL37, article_ref: "Art. 13(12) sentence 2 — EU declaration + CE marking" }
    - { clause_id: CRA-CL113, article_ref: "Art. 28(1) — EU declaration content" }
    - { clause_id: CRA-CL114, article_ref: "Art. 28(2) — declaration format per Annex V/VI" }
    - { clause_id: CRA-CL116, article_ref: "Art. 28(4) — manufacturer responsibility" }
  linked_objectives: [SO-CRA-058, SO-CRA-063]
  sub_domain: [D-09.4]
  nist_csf_mapping:
    - { id: GV.PO-02, title: "Cybersecurity processes and procedures for implementing the cybersecurity policy are established, communicated, and enforced" }
    - { id: GV.OC-03, title: "Legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 13(12) sentence 1 requires the manufacturer — before placing
    the product on the market — to draw up the technical documentation
    referred to in Article 31, carry out (or have carried out) the
    conformity-assessment procedure referred to in Article 32, and, where
    compliance has been demonstrated, draw up the EU declaration of
    conformity in accordance with Article 28 and affix the CE marking in
    accordance with Article 30. Article 28(1) sets the declaration content
    (statement of Annex I fulfilment). Article 28(2) sets the format:
    Annex V model for the full declaration, Annex VI template for the
    simplified form. Article 28(4) attributes sole responsibility for the
    compliance claim to the entity that drew up the declaration.
  security_rationale: |
    The Art. 13(12)/(28) pre-market chain is operationalised in NIST CSF
    2.0 through GV.PO-02 and GV.OC-03. GV.PO-02 anchors the procedural
    discipline of executing the four sequential gates (technical
    documentation, conformity assessment, EU declaration, CE marking) in
    the correct order, with a process artefact produced at each gate.
    GV.OC-03 anchors the legal-claim content of the EU declaration — the
    Annex I fulfilment statement and the Annex V/VI format selection —
    as a managed regulatory requirement. Together, GV.PO-02 and GV.OC-03
    give the manufacturer a single, end-to-end control set that the SDLC
    can be audited against, and that the manufacturer can demonstrate
    ex post cleared every gate before the first placement, with no gate
    compressed or skipped.
  ambiguity_notes: |
    "Before placing on the market" is a temporal anchor: every gate must
    be cleared before the first placement, not after the fact. Article
    28(4) — "the manufacturer assumes responsibility for the compliance
    of the product with digital elements" by virtue of drawing up the
    declaration — reads literally as the entity that signed the
    declaration bears the obligation; if a third party draws up the
    declaration on the manufacturer's behalf without becoming a
    manufacturer under Articles 21–22, the underlying responsibility
    chain remains with the manufacturer [Art. 13(12) literal].
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-086
  title: "CE marking affixed and EU declaration accompanies product"
  source_clauses:
    - { clause_id: CRA-CL117, article_ref: "Art. 30(1) — CE marking affixing" }
    - { clause_id: CRA-CL118, article_ref: "Art. 30(3) — CE marking before placing on market" }
    - { clause_id: CRA-CL119, article_ref: "Art. 30(6) — implementing acts for labels/pictograms" }
    - { clause_id: CRA-CL45, article_ref: "Art. 13(20) — full or simplified EU declaration with product" }
  linked_objectives: [SO-CRA-058, SO-CRA-062]
  sub_domain: [D-09.4]
  nist_csf_mapping:
    - { id: GV.OC-03, title: "Legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 30(1) requires the CE marking to be affixed visibly, legibly,
    and indelibly to the product and its packaging; for software products
    and products supplied without packaging, the marking may be placed on
    the EU declaration or on a website accessible with the product.
    Article 30(3) requires the CE marking to be affixed before the product
    is placed on the market. Article 30(6) authorises the Commission to
    adopt implementing acts on labels and pictograms related to the
    security of products with digital elements. Article 13(20) requires
    the manufacturer to provide the EU declaration — full or simplified —
    with the product [Recital 47, Recital 49].
  security_rationale: |
    The Art. 30(1)/(3)/(6)/(13)(20) CE marking and EU-declaration
    accompaniment is operationalised in NIST CSF 2.0 through GV.OC-03.
    GV.OC-03 (Legal, regulatory, and contractual requirements regarding
    cybersecurity are understood and managed) anchors the manufacturer's
    standing duty to know the current CE-marking format requirements —
    visible/legible/indelible for physical products, declaration-or-
    website for software — and to keep the EU declaration accessible
    for the Art. 13(13) retention window. The single-Subcategory mapping
    reflects that the obligation is essentially a regulatory-evidence
    delivery duty, not a new control surface. GV.OC-03 gives the
    manufacturer a managed-requirements framework that can demonstrate
    ex post that the marking was affixed before the first placement and
    that the declaration remained available throughout the support
    period.
  ambiguity_notes: |
    "Visibly, legibly, indelibly" is a conjunctive stack: all three must
    hold for the affixed marking. "Simplified EU declaration" refers to
    the Annex VI template format — the same compliance claim, expressed
    in a short form intended for products where the full Annex V
    declaration would be disproportionate.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-089
  title: "Public archives and substantial-modification conformity perimeter"
  source_clauses:
    - { clause_id: CRA-CL35, article_ref: "Art. 13(11) — public software archives + user risk communication" }
    - { clause_id: CRA-CL34, article_ref: "Art. 13(10) — substantial-modification last-version compliance" }
  linked_objectives: [SO-CRA-060, SO-CRA-035]
  sub_domain: [D-02.2, D-07.4, D-09.4]
  nist_csf_mapping:
    - { id: PR.PS-02, title: "Software is maintained, replaced, and removed commensurate with risk" }
    - { id: GV.OC-04, title: "Critical objectives, capabilities, and services that stakeholders depend on or expect from the organization are understood and communicated" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 13(11) authorises the manufacturer to maintain public software
    archives that enhance user access to historical versions; in such
    cases, the users must be clearly informed — in an easily accessible
    manner — of the risks associated with using unsupported versions of
    the product. Article 13(10) provides that when substantial
    modifications are made to a software product, only the modified
    version (not the prior version) needs to undergo the Article 32
    conformity-assessment procedure (interpreting existing
    manufacturer-guidance and Annex II §4). The two clauses together
    construct the durable-version-archiving cluster for software products
    [Recital 22].
  security_rationale: |
    The Art. 13(10)/(11) archives-and-substantial-modification cluster is
    operationalised in NIST CSF 2.0 through PR.PS-02 and GV.OC-04.
    PR.PS-02 (Software is maintained, replaced, and removed commensurate
    with risk) anchors the lifecycle posture: the manufacturer continues
    to maintain, replace, and remove older versions in line with the
    evolving risk picture, and the modified version replaces the prior
    version in the conformity perimeter. GV.OC-04 (Critical objectives,
    capabilities, and services that stakeholders depend on or expect from
    the organization are understood and communicated) anchors the
    user-side risk communication about unsupported archived versions.
    Together, PR.PS-02 and GV.OC-04 give the manufacturer a lifecycle
    control set that keeps the conformity perimeter bounded to the
    modified version while ensuring that users of the archives are
    told they have left the security-update envelope, and that the
    manufacturer can demonstrate ex post.
  ambiguity_notes: |
    "Maintain public software archives" reads as a discretionary
    activity — the manufacturer chooses whether to archive older
    versions. Where the manufacturer does, the user-communication duty
    attaches. "Clearly informed in an easily accessible manner" reads as
    a UI discoverability expectation, rather than a buried reference
    inside an EULA.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-090
  title: "Support-period end-date disclosed to users"
  source_clauses:
    - { clause_id: CRA-CL44, article_ref: "Art. 13(19) — support-period end-date display" }
    - { clause_id: CRA-CL157, article_ref: "Annex II §7 — support-period type + end-date in user info" }
    - { clause_id: CRA-CL61, article_ref: "Art. 21 — manufacturer-equivalent inherits obligation" }
  linked_objectives: [SO-CRA-061]
  sub_domain: [D-09.4, D-05.2]
  nist_csf_mapping:
    - { id: GV.OC-04, title: "Critical objectives, capabilities, and services that stakeholders depend on or expect from the organization are understood and communicated" }
    - { id: GV.PO-01, title: "Organizational cybersecurity policy is established, communicated, and enforced" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 13(19) requires the manufacturer to ensure that the end date
    of the support period — including at least the month and year — is
    clearly and understandably specified at the time of purchase; the
    manufacturer shall also inform users when the support-period end-date
    approaches. Annex II §7 carries the type of technical security support
    and the end-date into the user-facing information that accompanies the
    product. Article 21 makes any actor that takes on the manufacturer
    role (under its name/trademark or through substantial modification)
    inherit the same end-date display obligation.
  security_rationale: |
    The Art. 13(19)/Annex II §7 support-period end-date disclosure is
    operationalised in NIST CSF 2.0 through GV.OC-04 and GV.PO-01.
    GV.OC-04 (Critical objectives, capabilities, and services that
    stakeholders depend on or expect from the organization are
    understood and communicated) anchors the support-period end-date as
    a critical, expected-to-be-communicated element of the
    manufacturer's stakeholder interface. GV.PO-01 (Organizational
    cybersecurity policy is established, communicated, and enforced)
    anchors the manufacturer-equivalent inheritance (Art. 21) — the
    policy that determines who assumes the display obligation when
    ownership of the product changes hands. Together, GV.OC-04 and
    GV.PO-01 give the manufacturer a communication-and-policy control
    set that the manufacturer (or its Art. 21 successor) can
    demonstrate ex post kept the end-date visible from the time of
    purchase through the approach-and-arrival window.
  ambiguity_notes: |
    "Clearly and understandably" reads as a UI-discoverability,
    plain-language expectation — anchored in the harmonised-standards
    specifications for product marking and in the Article 13(11)
    archives-discoverability baseline.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-091
  title: "EU declaration accompanies or is web-accessible with product"
  source_clauses:
    - { clause_id: CRA-CL45, article_ref: "Art. 13(20) — full or simplified EU declaration with product" }
    - { clause_id: CRA-CL156, article_ref: "Annex II §6 — internet address for EU declaration" }
  linked_objectives: [SO-CRA-062]
  sub_domain: [D-09.4]
  nist_csf_mapping:
    - { id: GV.OC-03, title: "Legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 13(20) requires the manufacturer to provide the EU declaration
    of conformity — either the full text or the simplified form — with
    the product. Annex II §6 confirms the optional alternative: the
    manufacturer may provide an internet address at which the EU
    declaration can be accessed, instead of supplying the declaration in
    paper or bundled electronic form. This optionality applies in
    parallel with the software-product CE-marking rule under Article 30(1)
    [Recital 47].
  security_rationale: |
    The Art. 13(20)/Annex II §6 declaration-accompaniment rule is
    operationalised in NIST CSF 2.0 through GV.OC-03. GV.OC-03 (Legal,
    regulatory, and contractual requirements regarding cybersecurity are
    understood and managed) anchors the manufacturer duty to provide
    the declaration in one of two admissible forms (Annex V model or
    Annex VI template, paper or web-accessible URL) and to keep the URL
    live for the duration of the Art. 13(13) retention period. The
    single-Subcategory mapping reflects that the obligation is a
    regulatory-evidence delivery duty, not a new control surface.
    GV.OC-03 gives the manufacturer a managed-requirements framework
    that can demonstrate ex post that the declaration was available in
    an admissible form throughout the support and retention windows.
  ambiguity_notes: |
    "Full or simplified" admits either the Annex V model or the
    Annex VI template; both are valid forms. "Internet address" reads
    literally as a URL — the manufacturer is responsible for keeping
    that URL live for the duration of the Article 13(13) retention
    period.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-092
  title: "Corrective measures, withdrawal, or recall on non-conformity"
  source_clauses:
    - { clause_id: CRA-CL46, article_ref: "Art. 13(21) — corrective measures on non-conformity + withdrawal + recall" }
    - { clause_id: CRA-CL96, article_ref: "Art. 21 — manufacturer-equivalent trigger (cross-ref)" }
  linked_objectives: [SO-CRA-063]
  sub_domain: [D-09.4, D-04.2, D-07.4]
  nist_csf_mapping:
    - { id: RS.MI-01, title: "Incidents are contained" }
    - { id: RS.MI-02, title: "Incidents are mitigated" }
    - { id: GV.OV-02, title: "The organizational cybersecurity risk management strategy is reviewed and adjusted to address changes in the organization's risk landscape (e.g., the threat environment, technology, regulations, standards)" }
  applies_to_role: [MANUFACTURER, IMPORTER, DISTRIBUTOR]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 13(21) requires the manufacturer — from the placing on the
    market and for the duration of the support period — who knows or has
    reason to believe that the product or its processes are not in
    conformity with the Annex I cybersecurity requirements to immediately
    take the corrective measures necessary to bring the product or
    processes into conformity, or to withdraw or recall the product, as
    appropriate. Article 21 makes Article 13(21) inheritable by
    manufacturer-equivalents (importer or distributor placing under own
    name, or substantial modifier) [Recital 33].
  security_rationale: |
    The Art. 13(21)/Art. 21 corrective-measures duty is operationalised
    in NIST CSF 2.0 through RS.MI-01, RS.MI-02, and GV.OV-02. RS.MI-01
    (Incidents are contained) and RS.MI-02 (Incidents are mitigated)
    anchor the immediate response: a non-conformity discovered (or
    constructively known) is contained and mitigated, with the
    withdrawal-or-recall option available where mitigation cannot
    restore conformity. GV.OV-02 (The organizational cybersecurity risk
    management strategy is reviewed and adjusted to address changes in
    the organization's risk landscape) anchors the post-response
    re-baselining — the manufacturer updates the risk picture that
    failed to prevent the non-conformity. Together, RS.MI-01, RS.MI-02,
    and GV.OV-02 give the manufacturer a three-stage control set
    (contain, mitigate, re-baseline) that the manufacturer (or its
    Art. 21 successor) can demonstrate ex post was triggered on each
    "knows or has reason to believe" event.
  ambiguity_notes: |
    "Immediately take the corrective measures necessary" reads as
    action upon knowledge (or constructive knowledge) of non-conformity;
    "necessary" measures are the minimum set to restore conformity
    rather than a maximalist clean-sheet re-engineering. Recital 33
    frames the "immediately" bound by what is technically and
    organisationally feasible, not by what is commercially convenient.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-093
  title: "MSA cooperation on reasoned request for conformity evidence"
  source_clauses:
    - { clause_id: CRA-CL47, article_ref: "Art. 13(22) — manufacturer cooperation with MSAs" }
  linked_objectives: [SO-CRA-064]
  sub_domain: [D-09.4]
  nist_csf_mapping:
    - { id: GV.OC-03, title: "Legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed" }
    - { id: RS.CO-04, title: "Coordination with stakeholders occurs consistent with applicable rules and regulations" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 13(22) requires the manufacturer — upon a reasoned request
    from a market-surveillance authority — to provide that authority, in
    a language which can be easily understood by the authority, all
    information and documentation, in paper or electronic form, necessary
    to demonstrate the conformity of the product and the manufacturer's
    processes with this Regulation. The duty is anchored to the
    reasoned request, not to a generic standing obligation to publish
    [Recital 37].
  security_rationale: |
    The Art. 13(22) MSA cooperation duty is operationalised in NIST CSF
    2.0 through GV.OC-03 and RS.CO-04. GV.OC-03 anchors the
    legal-disclosure content of the cooperation duty — the manufacturer
    knows which information and documentation in the technical dossier
    responds to a conformity-verification request and provides it in
    the official language of the requesting MSA's Member State.
    RS.CO-04 (Coordination with stakeholders occurs consistent with
    applicable rules and regulations) anchors the procedural posture —
    cooperation follows the rules of the requesting authority, with
    the reasoned-request gate respected. Together, GV.OC-03 and
    RS.CO-04 give the manufacturer a content-and-procedure control
    set that can demonstrate ex post that every reasoned MSA request
    was answered in the correct language, scope, and form.
  ambiguity_notes: |
    "In a language which can be easily understood by that authority"
    reads as the official EU-language of the MSA's Member State. The
    Member State may agree to accept submissions in another official
    EU language under Regulation No 1/1958, in which case the "easily
    understood" benchmark is satisfied by the language the authority
    has agreed to accept.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-094
  title: "Cross-regulation risk-assessment consolidation permitted"
  source_clauses:
    - { clause_id: CRA-CL22, article_ref: "Art. 13(4) sentence 2 — AI Act carve-out for unified risk assessment" }
  linked_objectives: [SO-CRA-064]
  sub_domain: [D-09.4, D-09.2]
  nist_csf_mapping:
    - { id: GV.OC-03, title: "Legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed" }
    - { id: ID.RA-05, title: "Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response decisions" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 13(4) sentence 2 allows the cybersecurity risk assessment
    referred to in Article 13(3) to be part of — or combined with — the
    risk assessment required by other Union legal acts applicable to the
    product with digital elements. The provision is permissive: the
    manufacturer may integrate the CRA risk assessment with another
    Union-acts risk assessment (for example, the AI Act risk assessment
    for high-risk AI systems, the Machinery Regulation risk assessment,
    or the Radio Equipment Directive risk assessment), but is not
    obliged to do so [Recital 23].
  security_rationale: |
    The Art. 13(4) s.2 cross-regulation consolidation is operationalised
    in NIST CSF 2.0 through GV.OC-03 and ID.RA-05. GV.OC-03 anchors the
    regulatory-mapping content of the consolidated assessment: the
    manufacturer maps which clauses from which Union acts apply to
    the product, and documents the cross-walk in a way that satisfies
    each regime's review separately. ID.RA-05 anchors the
    threat-model-and-applicability content — the substantive risk
    reasoning that is shared across regimes. Together, GV.OC-03 and
    ID.RA-05 give the manufacturer a cross-regulation control set
    that allows a single assessment to discharge multiple
    Union-acts risks without loss of fidelity, and that can be
    demonstrated ex post as consistent across the regimes it covers.
  ambiguity_notes: |
    "May be part of the risk assessment required by those Union legal
    acts" reads as a permissive conjunction — manufacturer discretion
    rather than a regulator-driven integration mandate. There is no S3
    ambiguity in the structural language; the practical question is
    whether the receiving Union legal act permits cross-integration in
    the relevant form, which is evaluated regime-by-regime.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-099
  title: "Commission implementing and delegated acts operationalisation"
  source_clauses:
    - { clause_id: CRA-CL49, article_ref: "Art. 13(24) — SBOM implementing acts" }
    - { clause_id: CRA-CL67, article_ref: "Art. 14(9) — delegated acts on delay grounds" }
    - { clause_id: CRA-CL68, article_ref: "Art. 14(10) — implementing acts on notification format/procedures" }
    - { clause_id: CRA-CL8, article_ref: "Art. 7(3) — delegated acts amending Annex III" }
    - { clause_id: CRA-CL9, article_ref: "Art. 7(4) — implementing acts on technical descriptions" }
    - { clause_id: CRA-CL119, article_ref: "Art. 30(6) — implementing acts on labels/pictograms" }
    - { clause_id: CRA-CL50, article_ref: "Art. 13(25) — Union-wide dependency assessment by ADCO" }
  linked_objectives: [SO-CRA-067, SO-CRA-070]
  sub_domain: [D-09.4]
  nist_csf_mapping:
    - { id: GV.PO-02, title: "Cybersecurity processes and procedures for implementing the cybersecurity policy are established, communicated, and enforced" }
    - { id: GV.OV-01, title: "Cybersecurity risk management strategy outcomes are reviewed and adjusted to ensure they adequately address organizational risks" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 13(24), 13(25), 14(9), 14(10), 7(3), 7(4), and 30(6)
    collectively establish the Commission and ADCO implementing and
    delegated acts machinery that operationalises, refines, and
    supplements the body of the Regulation. Article 13(24) authorises
    implementing acts on the SBOM format and elements; Article 13(25)
    authorises ADCO to conduct a Union-wide dependency assessment on
    the dependence of Member States and the Union on software
    components, in particular on free and open-source software
    components [Recital 25]; Article 14(9) authorises delegated acts on
    cybersecurity-related grounds for delaying notification
    dissemination; Article 14(10) authorises implementing acts on
    notification format and procedures; Article 7(3) authorises
    delegated acts amending Annex III; Article 7(4) authorises
    implementing acts specifying the technical descriptions of Annex III
    and Annex IV product categories; Article 30(6) authorises
    implementing acts on labels and pictograms related to security.
  security_rationale: |
    The Art. 7(3)/(4), 13(24)/(25), 14(9)/(10), 30(6) Commission and ADCO
    acts machinery is operationalised in NIST CSF 2.0 through GV.PO-02
    and GV.OV-01. GV.PO-02 (Cybersecurity processes and procedures for
    implementing the cybersecurity policy are established, communicated,
    and enforced) anchors the process discipline of tracking Commission
    publication cadence and folding each act into the SDLC and
    documentation package as it is adopted. GV.OV-01 (Cybersecurity risk
    management strategy outcomes are reviewed and adjusted to ensure
    they adequately address organizational risks) anchors the
    review-and-adjust loop triggered by each new act. Together, GV.PO-02
    and GV.OV-01 give the manufacturer a tracking-and-incorporation
    control set that can demonstrate ex post that the body of
    implementing and delegated acts in force at the time of placing was
    correctly reflected in the technical documentation and conformity
    posture.
  ambiguity_notes: |
    The implementing acts referenced by Articles 7(4), 13(24), and 14(9)
    — together with the Art. 7(4) technical descriptions and the Art.
    14(9) delegated acts on delay grounds — are scheduled for adoption by
    11 December 2025. As of mid-2025, several of these acts remain
    unpublished. The standing compliance duty attaches once the acts are
    published; manufacturers that have discharged their pre-July
    obligations on the basis of draft technical descriptions should
    re-verify against the adopted text within a reasonable window after
    publication.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-102
  title: "Risk assessment as durable MSA-reviewable record"
  source_clauses:
    - { clause_id: CRA-CL21, article_ref: "Art. 13(4) sentence 1 — risk assessment in technical documentation" }
    - { clause_id: CRA-CL162, article_ref: "Annex VII §3 — risk-assessment documentation" }
    - { clause_id: CRA-CL47, article_ref: "Art. 13(22) — MSA cooperation" }
  linked_objectives: [SO-CRA-070, SO-CRA-053]
  sub_domain: [D-10.2, D-09.4]
  nist_csf_mapping:
    - { id: ID.RA-05, title: "Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response decisions" }
    - { id: GV.OC-03, title: "Legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS, TRIGGERED]
  regulatory_rationale: |
    Article 13(4) sentence 1 and Annex VII §3 require the
    cybersecurity risk assessment to be included in the technical
    documentation package. Article 13(22) makes that package — including
    the risk assessment as a component — available to a market-
    surveillance authority on a reasoned request [Recital 23, Recital 37].
  security_rationale: |
    The Art. 13(4)/(22) + Annex VII §3 risk-assessment-as-record duty is
    operationalised in NIST CSF 2.0 through ID.RA-05 and GV.OC-03.
    ID.RA-05 (Threats, vulnerabilities, likelihoods, and impacts are
    used to understand inherent risk and inform risk response decisions)
    anchors the substantive content of the assessment — the
    threat-vulnerability-impact reasoning that informs Annex I
    applicability. GV.OC-03 anchors the legal-recordkeeping and
    disclosure posture: the assessment is held in the technical
    documentation package and produced to the MSA on a reasoned request
    under Art. 13(22). Together, ID.RA-05 and GV.OC-03 give the
    manufacturer a content-and-disclosure control set that lets the MSA
    verify Annex I applicability against the threat profile, and that
    the manufacturer can demonstrate ex post has been maintained and
    disclosed correctly throughout the support period.
  ambiguity_notes: |
    The text carries no major S2/S3 ambiguity beyond those inherited
    from SR-CRA-066 (risk-assessment timing) and SR-CRA-080 (Annex VII
    §3 documentation).
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-107
  title: "User-facing lifecycle security instructions package"
  source_clauses:
    - { clause_id: CRA-CL158, article_ref: "Annex II §8(a)–(f) — detailed instructions over product lifetime" }
    - { clause_id: CRA-CL43, article_ref: "Art. 13(18) — accompany product with Annex II information" }
  linked_objectives: [SO-CRA-048]
  sub_domain: [D-08.1, D-09.4]
  nist_csf_mapping:
    - { id: PR.AT-01, title: "All users are informed and trained on cybersecurity topics (e.g. recognition of phishing, social engineering, and other relevant risks)" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS, TRIGGERED]
  regulatory_rationale: |
    Annex II §8 requires the product to be accompanied by detailed
    instructions or an internet address referring to such detailed
    instructions covering: (a) the necessary measures during initial
    commissioning and throughout the lifetime of the product with
    digital elements to ensure its secure use; (b) how changes to the
    product can affect the security of data; (c) how security-relevant
    updates can be installed; (d) the secure decommissioning of the
    product, including how user data can be securely removed; (e) how
    the default setting enabling automatic installation of security
    updates can be turned off; (f) where the product is intended for
    integration into other products with digital elements, the
    information necessary for the integrator to comply with the Annex I
    requirements and the Annex VII documentation requirements. Article
    13(18) extends the Annex II package to a duty to provide the
    information in paper or electronic form, accessible for the support
    period [Recital 25].
  security_rationale: |
    The Annex II §8 (a)-(f) user-facing instructions package is
    operationalised in NIST CSF 2.0 — though imperfectly — through
    PR.AT-01. PR.AT-01 (All users are informed and trained on
    cybersecurity topics) is the closest Function-level match because
    the user-facing instructions package performs a workforce-analog
    function for end users: it informs them about phishing-class risks
    (auto-update opt-out, decommissioning, secure-update installation)
    that they need to recognise and act on. The gap is that PR.AT-01 is
    framed for INTERNAL workforce training, not for end-user-facing
    product documentation — CSF 2.0 has no dedicated Subcategory for
    end-user lifecycle instructions. The mapping covers the closest
    analog only; see `unmapped_csf_justification`. The PR.AT-01 anchor
    lets the manufacturer demonstrate ex post that the §8 package
    carried the workforce-analog content, even though the user-side
    framing remains partially unmapped.
  ambiguity_notes: |
    "Or an internet address referring to such detailed instructions" is
    a literal disjunction — a physical document and a URL are both
    admissible; the choice is the manufacturer's. The §8 cluster
    inherits the Annex II user-side UNMAPPED_CSF framing (see
    unmapped_csf_justification below); (f) is the integrator-side
    element that maps more cleanly to PR.AT-01 / GV.SC-03 under the
    workforce-supplier framing.
  unmapped_csf_justification: |
    Annex II §8 user-facing instructions are addressed in the dedicated
    UNAA-71 mapping; the integrator-side (f) component maps defensibly
    under PR.AT-01 for the workforce framing. The user-side instructions
    (a)–(e) remain a partial fit.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-114
  title: "ENISA biennial report, EU vulnerability database, CSIRT helpdesk"
  source_clauses:
    - { clause_id: CRA-CL76, article_ref: "Art. 16(3) — CSIRT provides notification info to market-surveillance authorities" }
    - { clause_id: CRA-CL80, article_ref: "Art. 17(3) — ENISA biennial report on cybersecurity risks in products" }
    - { clause_id: CRA-CL82, article_ref: "Art. 17(5) — EU vulnerability database (writes back to NIS 2 Art. 12(2))" }
    - { clause_id: CRA-CL83, article_ref: "Art. 17(6) — CSIRT helpdesk for manufacturers on reporting obligations" }
  linked_objectives: [SO-CRA-073, SO-CRA-074]
  sub_domain: [D-09.4]
  nist_csf_mapping:
    - { id: RS.CO-04, title: "Coordination with stakeholders occurs consistent with applicable rules and regulations" }
    - { id: ID.IM-04, title: "Cybersecurity risk management improvements are informed by awareness of related developments and context (e.g., threat intelligence, incidents, technology evolution)" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 16(3) provides that CSIRTs designated as coordinators shall
    provide notification information to the relevant market-surveillance
    authorities. Article 17(3) requires ENISA to prepare a biennial
    report on cybersecurity risks in products with digital elements.
    Article 17(5) requires ENISA to add publicly known vulnerabilities
    to the EU vulnerability database established under NIS 2 Article
    12(2). Article 17(6) requires CSIRTs designated as coordinators to
    provide helpdesk support to manufacturers on the reporting
    obligations under Articles 14 and 15 [Recital 38, Recital 39].
  security_rationale: |
    The Art. 16(3)/17(3)/(5)/(6) ENISA-CSIRT coordination cluster is
    operationalised in NIST CSF 2.0 through RS.CO-04 and ID.IM-04.
    RS.CO-04 (Coordination with stakeholders occurs consistent with
    applicable rules and regulations) anchors the multi-institutional
    coordination posture — CSIRTs pass notification information to
    MSAs (Art. 16(3)) and ENISA populates the EU vulnerability database
    (Art. 17(5)). ID.IM-04 (Cybersecurity risk management improvements
    are informed by awareness of related developments and context)
    anchors the improvement-loop input that the biennial report
    (Art. 17(3)) and the vulnerability database provide — the
    manufacturer's risk-assessment refresh can cite ENISA's outputs
    as evidence of current threat context. Together, RS.CO-04 and
    ID.IM-04 give the cluster a coordination-and-improvement control
    set that lets the manufacturer consume ENISA outputs in its own
    Art. 13(2) risk picture and demonstrate ex post that those outputs
    were considered.
  ambiguity_notes: |
    "Biennial" reads literally as every two years. "Publicly known
    vulnerabilities" reads as already publicly disclosed vulnerabilities
    — the database is curation rather than original publication; the
    threshold is ENISA's curated-vs-undisclosed judgement. The
    helpdesk support is a guidance channel rather than a binding
    interpretation service: written ENISA guidance and the formal
    Regulation text remain the controlling sources.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

