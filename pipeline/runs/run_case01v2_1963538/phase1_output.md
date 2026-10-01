---
document_id: MVP-P1-OUT-001
title: "Phase 1 Output — TinyTask Lda. (Contextual Definition, MVP)"
version: 0.1
created: 2026-10-01
status: DRAFT
input: pipeline/cases/Case_01_TinyTask_SaaS/company_input.md
corpus: baseline
---


# Phase 1 Output — TinyTask Lda.



## §1 Company Profile Echo

TinyTask Lda. — Technology / Software (B2B SaaS productivity tools), 8 employees (micro-enterprise; revenue <€2M), Portugal (EU), Lisbon HQ, Private Limited Company (Lda.).
Develops and operates a rule-based task management platform sold by commercial subscription to business customers; develops the software itself and places the product (web + mobile interface) on the EU market as manufacturer, default class, self-assessment conformity.
No AI/ML systems developed, deployed or integrated.
Processes EU personal data: as controller — customer account metadata (names, emails, passwords); as processor — task data containing personal data of customers' own users under standard DPAs.
No health, payment-card or minors' data processed in-house; payments handled by an external payment provider.
Hosted SaaS; access via customer accounts with individual logins.
Third-party: external payment provider (sub-processor, payment metadata only); managed cloud hosting.
No formal SBOM; supplier evaluations ad-hoc via standard contracts/DPAs; vulnerability remediation manual, triggered during routine updates or security advisories.
DPO appointment not triggered (small-scale processing; no regular systematic large-scale monitoring).

## §2 Applicable Regulations

| Regulation | Verdict | Rationale |
|---|---|---|
| GDPR | `applies` | Established in Portugal (EU) per `jurisdictions`; processes personal data per `data_categories` (names, emails, passwords, task data with personal data). |
| CRA | `applies` | `develops_software: true`; `product_summary` states TinyTask develops the software and places the product (SaaS + web/mobile interface) on the EU market as manufacturer. |
| NIS2 | `does not apply` | `sector` is Technology/Software (B2B SaaS) — not an Annex I/II essential/important sector; `size_employees: 8` is below the NIS2 size threshold. |
| DORA | `does not apply` | `sector` is Technology/Software (B2B SaaS productivity tools); the company is not a financial entity nor an ICT provider to financial entities. |
| AI_Act | `does not apply` | `product_summary` states "no AI/ML systems developed, deployed or integrated — the platform is rule-based"; no AI system is placed on the market or deployed. |

## §3 Applicable Sub-domain Subset

| Sub-domain | Name | Trigger rationale |
|---|---|---|
| D-01.1 | Data at Rest Encryption | customer PII (names, emails, passwords, task data) stored on managed cloud → GDPR Art. 32 security of processing (encryption at rest) |
| D-01.2 | Data in Transit Encryption | PII transmitted via SaaS web/mobile interface and payment-provider API → GDPR Art. 32 security of processing (encryption in transit) |
| D-02.1 | Vulnerability Identification | TinyTask develops and places SaaS product on EU market as manufacturer → CRA Art. 13(1) vulnerability identification |
| D-02.3 | Coordinated Vulnerability Disclosure | TinyTask places product with digital elements on EU market as manufacturer → CRA Art. 13(1) coordinated vulnerability disclosure |
| D-03.1 | Identity Lifecycle Management | customer accounts with individual logins for business customers and their end-users → GDPR Art. 32 identity lifecycle management |
| D-03.2 | Multi-Factor Authentication | individual login accounts with stored passwords → GDPR Art. 32 authentication strength |
| D-04.1 | Incident Detection & Triage | processing of PII (names, emails, passwords, task data) on managed cloud → GDPR Art. 33 breach detection and triage |
| D-04.3 | Incident Notification & Reporting | personal data breach involving customer PII → GDPR Art. 33(1) 72-hour notification to supervisory authority |
| D-05.1 | Data Minimisation | collection of customer names, emails, passwords, and task data → GDPR Art. 5(1)(c) data minimisation |
| D-05.2 | Retention & Archiving | storage of customer PII and task data on managed cloud → GDPR Art. 5(1)(e) storage limitation |
| D-05.3 | Right to Erasure | customer and end-user PII stored in SaaS → GDPR Art. 17 right to erasure |
| D-05.4 | Data Portability | customer PII (names, emails, task data) held in structured format → GDPR Art. 20 data portability |
| D-06.1 | Vendor Risk Assessment | external payment provider as sub-processor + managed cloud hosting → GDPR Art. 28 processor due diligence |
| D-06.2 | Software Bill of Materials (SBOM) | TinyTask develops SaaS product and places on EU market as manufacturer → CRA Art. 13(1) SBOM |
| D-06.3 | Contractual Security Obligations | external payment provider and managed cloud as processors → GDPR Art. 28(3) contractual security obligations |
| D-07.1 | Secure-by-Design Principles | TinyTask develops SaaS product from scratch → GDPR Art. 25 data protection by design + CRA security by design |
| D-07.2 | Secure Coding Practices | in-house development of SaaS product with digital elements → CRA secure coding practices |
| D-09.1 | Information Security Policies | 8-person SaaS company processing PII → GDPR Art. 32 documented security measures |
| D-09.2 | Impact & Risk Assessments | processing of PII (names, emails, passwords, task data) → GDPR Art. 35 risk assessment |
| D-09.4 | Records of Processing | controller and processor roles for PII → GDPR Art. 30 records of processing activities |
| D-10.1 | Continuous Security Monitoring | SaaS product processing PII on managed cloud → GDPR Art. 32 continuous security monitoring |
| D-10.2 | Audit Logging & Traceability | processing of PII with individual logins → GDPR Art. 32 audit logging and traceability |

## §4 Adjusted Goals



**Framing (company context conditioning every goal below):**

> 8-employee micro-enterprise (revenue <€2M), Portugal (EU), B2B SaaS for business customers.
> Regulatory roles: GDPR controller (customer accounts) and processor (customer task data); CRA manufacturer (default class, self-assessment conformity).
> Inherited/managed capabilities: managed cloud hosting; external payment provider (sub-processor for payment metadata only).
> Explicit exclusions: no AI/ML systems; NIS2, DORA, AI Act do not apply; no health, payment-card, or minors' data in-house; DPO not triggered.



### D-01.1 — Data at rest: encryption and key custody

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-01.1-001 | Personal data at rest in TinyTask's managed-cloud storage (customer account metadata and customer task data) is maintained under encryption with key custody logically separated from data access, calibrated to the five Art. 32(1) preamble factors in the company's risk assessment. | maintain | C | SO-D-01.1.HL | GDPR Art. 5(1)(f); Art. 32(1)(a); Art. 32(1)(b) | PR.DS-01, PR.DS-10 | Restated from the corpus "appropriate technical measures" to TinyTask's 8-person managed-cloud deployment where the company acts as both controller (customer accounts) and processor (customer task data); the "appropriate" threshold is operationalised through the five Art. 32(1) preamble factors in the company's risk assessment, and managed-cloud hosting means technical implementation is partly delegated while the obligation remains with TinyTask. |
| AG-D-01.1-002 | The TinyTask SaaS product (web and mobile interface) maintains state-of-the-art encryption of all stored data — personal or other — at the product level, rendering data unintelligible to any person not authorised to access it, with key custody functionally separated by role-based access control. | maintain | C | SO-D-01.1.HL | CRA Annex I Part I (1); Annex I Part I (2)(e) | PR.DS-01 | Restated from the corpus baseline to TinyTask's role as manufacturer of a default-class product with digital elements under self-assessment conformity; the state-of-the-art floor is a product-level obligation distinct from the GDPR deployment-level obligation, and the "render unintelligible" test applies to all data stored by the product (not only personal data). |

### D-01.2 — Data in transit (confidentiality and integrity)

**Framing (company context):** TinyTask Lda. is an 8-employee B2B SaaS company in Portugal (EU) developing and operating a rule-based task-management platform. It acts as GDPR controller for customer account data (names, emails, passwords) and processor for customer task data containing personal data of the customers' own users, and as CRA manufacturer (default product class, self-assessment conformity) placing the product with digital elements on the EU market. Hosting is managed cloud; no AI/ML systems are present. DORA, NIS 2, and AI Act are out of scope.

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-01.2-001 | Personal data transmitted across the company's network paths, inter-service channels, and third-party API connections remains confidential and unaltered in transit, with the level of protection proportionate to the risk of the five Art. 32(2) event classes (accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to, personal data transmitted). | maintain | C | SO-D-01.2.HL | Art. 32(1)(b); Art. 32(2) | PR.DS-02, PR.IR-01 | Scope narrowed from all data in transit to personal data (Art. 4(1)); protection level anchored to GDPR's risk-based "appropriate" standard with the five-event risk enumeration as the assessment frame; applies to an 8-person controller/processor operating managed-cloud channels. |
| AG-D-01.2-002 | Data transmitted by the product with digital elements is rendered unintelligible to any person not authorised to access it via state-of-the-art encryption in transit, and the product's exposed interfaces through which such data could leak are minimised. | maintain | C | SO-D-01.2.HL | Annex I Part I (2)(e); Annex I Part I (2)(j) | PR.DS-02, PR.IR-01 | Threshold raised from GDPR's risk-anchored "appropriate" to CRA's "state-of-the-art" (harmonised-standards-conformant); attack-surface-limitation leg (2)(j) added as a distinct manufacturer obligation; scope is product-level (all data the product transmits, not only personal data); applies to a default-class manufacturer with self-assessment conformity. |

### D-02.1 — Vulnerability Identification

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-02.1-001 | TinyTask, as controller of customer-account personal data and processor of customer task data in its B2B SaaS platform, maintains a documented process for regularly testing, assessing, and evaluating the effectiveness of the technical and organisational measures ensuring the security of that processing, and reviews its data-protection impact assessment whenever a change in the risk represented by the processing operations is identified. | maintain | accountability | SO-D-02.1.HL | GDPR Art. 32(1)(d); GDPR Art. 35(11) | ID.RA-01, PR.PS-02 | Restated from the five-regulation, AI-inclusive baseline to TinyTask's 8-person managed-cloud SaaS context: AI-specific attack categories (data poisoning, model evasion, etc.) and NIS2/DORA/AI Act legs excluded (no AI/ML systems; not a financial entity; not an essential/important entity); the "regularly" cadence is discharged by a documented periodic testing programme scaled to the Art. 32(1) preamble factors; DPIA review trigger retained as the Art. 35(11) material-change condition. |
| AG-D-02.1-002 | TinyTask, as manufacturer of a product with digital elements (SaaS platform with web and mobile interfaces) placed on the EU market in the default product class, ensures the product is made available without known exploitable vulnerabilities and maintains a continuing identification process — including a machine-readable software bill of materials covering at least the top-level dependencies and a vulnerability register — throughout the product's support period, exercising the constructive-knowledge due-diligence baseline. | maintain | I | SO-D-02.1.HL | CRA Annex I Part I (2)(a); CRA Annex I Part II (1) | ID.RA-01, ID.AM-02 | Restated from the five-regulation baseline to TinyTask's CRA manufacturer role on a default-class (self-assessment) SaaS product: NIS2/DORA/AI Act legs excluded (not applicable per fact sheet); the R2 constructive-knowledge baseline (inquiry-resistant, Annex VII §3 due-diligence floor) retained as the identification standard; SBOM scope limited to top-level dependencies per Annex I Part II (1); no AI-specific threat-model overlay (no AI/ML systems). |

### D-02.3 — Coordinated Vulnerability Disclosure

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-02.3-001 | Maintain a documented, published, and operationally enforced coordinated vulnerability disclosure policy for the company's SaaS product with digital elements, covering intake, triage, and post-disclosure verification across the product's support period. | maintain | Accountability | SO-D-02.3.HL | CRA Annex I Part II (5); CRA Art. 13(8) sentence 6 | GV.PO-01 | Restated from the CRA Sub-SO (SG-D-02.3.CRA) for a single-product, 8-person manufacturer; the "enforce" element (intake-channel evidence, triage-log records, post-disclosure verification artefacts) is retained at the scale of one product line rather than a multi-product portfolio; the NIS 2 Art. 12(1) CSIRT-coordinated pathway referenced in the baseline HL is inapplicable because NIS 2 is not confirmed for this entity. |
| AG-D-02.3-002 | Achieve public disclosure of information about fixed vulnerabilities (description, affected products, impacts, severity, remediation guidance) once a security update is made available, with any delay recorded under the duly justified delay-justification framework. | achieve | Accountability | SO-D-02.3.HL | CRA Annex I Part II (4); CRA Art. 14(9) | RS.CO-03 | Restated from the CRA Sub-SO for a single-product manufacturer; the disclosure content set is unchanged; the delay exception is categories-based per Art. 14(9) delegated acts rather than a blanket deferral; no NIS 2 Art. 23(4) incident-reporting cascade applies (NIS 2 not confirmed). |
| AG-D-02.3-003 | Maintain a publicly identifiable contact address for vulnerability reporting and a designated single point of contact enabling security researchers and users to communicate directly and rapidly with the manufacturer. | maintain | Accountability | SO-D-02.3.HL | CRA Annex I Part II (6); CRA Art. 13(17); CRA Annex II §2 | GV.SC-04 | Restated from the CRA Sub-SO for a single-product, 8-person manufacturer; the SPOC is a named individual or small team rather than a dedicated researcher-relations unit; the contact address is machine-discoverable (security.txt or well-known URI) at the scale of one product domain. |

### D-03.1 — Identity Lifecycle Management

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-03.1-001 | When a natural person (business customer or end-user of a customer) submits a data-subject rights request (Art. 15–22) to TinyTask as controller, the identity of the requester is verified using reasonable means proportionate to the risk of mis-identification before the request is actioned; the controller may request additional information necessary to confirm identity, and the verification scope is limited to the minimum information required (Art. 5(1)(c) minimisation), with a documented graduated-verification standard and proportionality justification per request class. | achieve | privacy-right | SO-D-03.1.HL | GDPR Art. 12(6); Art. 11(2); Art. 5(1)(c) | PR.AA-03, PR.AA-02 | Restated for an 8-employee B2B SaaS controller handling low-volume rights requests from business customers and their end-users; graduated verification and minimisation register scaled to the company's data categories (customer account metadata, task data) and managed-cloud hosting context. |
| AG-D-03.1-002 | Identities, credentials, and access entitlements for product users, service identities, and integrated components of TinyTask's SaaS platform are managed in a verifiable manner throughout the product's operational lifetime, with type/batch/serial unique identification backing the identity register and a documented single point of contact for identity-related queries (Art. 13(17)). | maintain | accountability | SO-D-03.1.HL | CRA Annex I Part I (2)(d); Art. 13(15); Art. 13(17); Annex II §3 | PR.AA-01, ID.AM-01 | Restated for an 8-employee manufacturer of a default-class B2B SaaS product; verifiable-manner obligation applied to the product's user accounts, internal service identities, and third-party integrated components (e.g., external payment provider); operational-lifetime scope aligned with the SaaS subscription model and self-assessment conformity path. |

### D-03.2 — Authentication of users, services, and hardware

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-03.2-001 | The 8-person internal team and the external payment sub-processor act only on documented instructions from TinyTask as controller (or as processor for customer task data) and remain bound by a confidentiality obligation; no authentication-strength threshold is imposed by this obligation — the surrounding instruction-and-confidentiality architecture is the operative duty. | maintain | C | SO-D-03.2.HL | GDPR Art. 28(3)(b); Art. 29; Art. 32(4) | PR.AA-05, PR.AA-06 | Restated from the GDPR Sub-SO staff-side obligation for an 8-employee SaaS controller/processor with one external sub-processor; the "documented instructions" chain is scoped to the internal team plus the payment sub-processor rather than a large enterprise hierarchy; the absence of an authentication-strength threshold is preserved verbatim from the OJ. |
| AG-D-03.2-002 | When a customer's own user (data subject) exercises a GDPR right through the customer (controller), TinyTask as processor verifies the requester's identity using reasonable means proportionate to the risk of mis-identification, given the non-sensitive, small-scale B2B data context. | achieve | privacy-right | SO-D-03.2.HL | GDPR Art. 12(6); Art. 11(2) | PR.AA-06, PR.AT-02 | Restated from the GDPR Sub-SO data-subject-side verification obligation; proportionality is anchored to the fact-sheet context (non-sensitive data, B2B SaaS, 8 employees) rather than a generic enterprise scale; the verification trigger is "reasonable doubt" per Art. 12(6), not a blanket MFA mandate. |
| AG-D-03.2-003 | The TinyTask SaaS product (web and mobile interface, default class, self-assessment conformity) protects against unauthorised access through appropriate control mechanisms — which may include authentication, identity, or access-management systems — commensurate with the identified cybersecurity risk of the product; the mechanism choice is at the manufacturer's discretion under the 3-way OR. | maintain | C | SO-D-03.2.HL | CRA Annex I Part I (2)(d) | PR.AA-01, ID.AM-01 | Restated from the CRA Sub-SO for a default-class SaaS product with individual customer logins; the "may include" permissive language is preserved verbatim from the OJ; no MFA or continuous-authentication phrase is imposed; the risk-assessment anchor is scoped to the product's default-class self-assessment conformity procedure. |

### D-04.1 — Incident Detection & Triage

> TinyTask Lda. is an 8-employee B2B SaaS company (Portugal, EU) developing and operating a rule-based task management platform. Regulatory roles: controller for customer account data (names, emails, passwords); processor for customer task data; manufacturer of products with digital elements (CRA default product class, self-assessment). Hosting: managed cloud. Explicit exclusions: no AI/ML systems developed, deployed, or integrated; NIS 2 and DORA not applicable; AI Act not applicable.

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-04.1-001 | Personal-data breaches affecting customer account data and task data are detected at the data-flow boundary of the managed-cloud environment, and the moment of "becoming aware" by a designated breach-handling role is documented to anchor the Art. 33(1) 72-hour notification clock. | maintain | C | SO-D-04.1.HL | Art. 32(1)(b); Art. 33(1); Art. 4(12) | DE.CM-01, RS.MA-02 | Scope narrowed from a generic controller to TinyTask's two data categories (customer account metadata as controller; task data as processor) at the managed-cloud data-flow boundary; the "becoming aware" documentation obligation and 72-hour clock anchor are retained in full per the corpus. |
| AG-D-04.1-002 | Relevant internal activity of the TinyTask SaaS platform — including access to or modification of task data, services, or functions — is recorded and monitored on a continuing basis throughout the product support period, with a user-visible opt-out for non-security-critical events, and any corruption or unauthorised modification is reported to the user. | maintain | I | SO-D-04.1.HL | Annex I Part I (2)(l); Annex I Part II (6); Art. 13(8) | PR.PS-04, DE.CM-09 | Scope narrowed from a generic manufacturer to TinyTask's B2B SaaS platform (web + mobile interface) under the CRA default product class; the user opt-out is limited to non-security-critical events; the product-internal detection layer is distinct from and does not substitute for the GDPR data-flow detection layer (DIFFERENT-PERSPECTIVE per CRDA-deep). |

### D-04.3 — Regulatory Notification

**Framing (company context conditioning every goal below):**

> TinyTask Lda. is an 8-employee B2B SaaS company in Portugal (EU) developing rule-based productivity tools. It acts as GDPR controller for customer account data (names, emails, passwords) and processor for customer task data, and as CRA manufacturer of products with digital elements (SaaS + web/mobile interface, default product class, self-assessment conformity). No AI/ML systems are developed, deployed, or integrated. NIS 2, DORA, and AI Act are excluded per the fact sheet. The company operates on managed cloud hosting with individual customer logins and one external payment sub-processor.

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-04.3-001 | A personal data breach affecting customer account data or task data is notified to the competent supervisory authority without undue delay and, where feasible, no later than 72 hours after TinyTask becomes aware of the breach, unless the breach is unlikely to result in a risk to data subjects' rights and freedoms, with the Art. 33(3) content template (nature, categories, approximate numbers, consequences, measures, DPO contact) filed. | achieve | accountability | SO-D-04.3.HL | GDPR Art. 33(1); Art. 33(3); Art. 4(12) | RS.CO-02; CM.AW-P7 | Restated for an 8-person B2B SaaS controller/processor; the `where feasible` softening and `unlikely risk` carve-out are preserved as GDPR-unique conditions per the corpus; the Art. 33(3) content template is the operative filing requirement; no mechanism or tool prescribed. |
| AG-D-04.3-002 | An actively-exploited vulnerability or severe incident in TinyTask's SaaS product with digital elements is notified to the designated CSIRT and ENISA on the three-tier temporal pattern — early warning within 24 hours, vulnerability or incident notification within 72 hours with progressive disclosure content, and final report within 14 days (AEV) or 1 month (SI) — with the Art. 15 coordinated vulnerability disclosure process operating in parallel without replacing the Art. 14 tiers. | achieve | accountability | SO-D-04.3.HL | CRA Art. 14(1); Art. 14(2)(a); Art. 14(2)(b); Art. 14(2)(c); Art. 14(3); Art. 14(4) | RS.MA-02; RS.CO-02 | Restated for an 8-person manufacturer of default-class SaaS products; the three-tier AEV pathway (24h/72h/14d) and parallel SI pathway (24h/72h/1m) are preserved verbatim from the corpus; the Art. 15 CVD process coordinates but does not replace the Art. 14 notification tiers; no mechanism or tool prescribed. |

### D-05.1 — Data Minimisation

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-05.1-001 | The company, as controller of customer account data and processor of task data containing end-user personal data, maintains that personal data collected and processed is limited to what is adequate, relevant, and necessary in relation to the declared processing purpose, with a documented necessity assessment per data class. | maintain | privacy-right | SO-D-05.1.HL | Art. 5(1)(c) GDPR | ID.AM-08, ID.AM-03 | Narrowed from the regulation-neutral baseline to the company's two personal-data classes (customer account metadata; task data with end-user personal data) under its dual controller/processor roles; necessity assessment scoped to the 8-employee B2B SaaS operation rather than an enterprise-wide programme. |
| AG-D-05.1-002 | When the purpose for which personal data is processed changes, the company achieves a documented Art. 6(4) five-factor compatibility assessment confirming the new purpose is consistent with the original before the new processing begins. | achieve | accountability | SO-D-05.1.HL | Art. 6(4) GDPR | ID.AM-08 | Restated as a discrete trigger-based assessment (achieved on each purpose change) rather than a continuous obligation; scoped to the company's B2B SaaS data flows where purpose changes are bounded by the subscription contract and infrequent at 8-employee scale. |
| AG-D-05.1-003 | The company avoids processing special-category personal data absent a valid Art. 9(2) exception basis, and documents any such basis to the effect that the narrow exception applies. | avoid | privacy-right | SO-D-05.1.HL | Art. 9(1) GDPR; Art. 9(2) GDPR | GV.OC-03 | Restated as a pure guardrail: the company currently processes no special-category data and operates no AI/ML systems, so the AI Act Art. 10(5) gateway is inapplicable; the obligation reduces to never processing special-category data without an independently documented Art. 9(2) basis. |
| AG-D-05.1-004 | The company, as manufacturer of the SaaS product with digital elements, maintains that data processed by the product (personal or other) is limited to what is adequate, relevant, and necessary in relation to the product's intended purpose, with proportionality calibrated by the Art. 13(2) risk assessment and the reasonably foreseeable use per Art. 13(3) sentence 2. | maintain | privacy-right | SO-D-05.1.HL | Annex I Part I (2)(g) CRA; Art. 3(23) CRA; Art. 13(3) sentence 2 CRA | ID.AM-08, ID.AM-03 | Narrowed from the regulation-neutral baseline to the company's single B2B SaaS product (rule-based task management platform) in the default CRA product class; the intended purpose is the task-management function as declared in the product's technical documentation; no AI/ML training pipeline applies. |

### D-05.2 — Retention & Archiving

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-05.2-001 | Personal data held by the company (customer account metadata and task data containing personal data of customers' users) is retained for no longer than is necessary for its declared processing purpose; any retention beyond purpose end is lawful and subject to Art. 89(1) safeguards (pseudonymisation, aggregation, access limitation); the RoPA documents the envisaged time limits for erasure per data category. | maintain | privacy-right | SO-D-05.2.HL | Art. 5(1)(e); Art. 30(1)(f); Art. 89(1) | ID.AM-08, ID.AM-03 | Narrowed to the company's two data classes (customer account metadata; task data with personal data of customers' users); no sensitive-data categories; processor role for customer task data acknowledged; no AI/ML logs in scope. |
| AG-D-05.2-002 | Security updates and supporting advisory messages for the company's SaaS product remain available to users across the support period (≥ 5 years) and the 10-year-or-remainder-of-support-period update-availability tail; Annex II information remains accessible for at least 10 years from placing on market; the support-period end-date is communicated clearly and understandably at the time of purchase. | maintain | A | SO-D-05.2.HL | Art. 13(8); Art. 13(9); Art. 13(18); Art. 13(19); Annex I Part II (7); Annex I Part II (8) | PR.PS-02, GV.OV-02 | Narrowed to the company's SaaS product (web + mobile interface) as a default-class product with self-assessment conformity; no AI/ML systems; the 10-year tail applies to update artefacts and Annex II information, not to personal data. |

### D-05.3 — Erasure and Secure Removal

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-05.3-001 | Personal data concerning a data subject is erased without undue delay upon the data subject's request where any of the six Art. 17(1) grounds applies, and the controller confirms the action taken to the data subject. | achieve | privacy-right | SO-D-05.3.HL | Art. 17(1)(a)–(f); Art. 17(2) | PR.DS-10, ID.AM-08 | Restated for an 8-person B2B SaaS controller over customer account data (names, emails, passwords); "without undue delay" retained as VAG per corpus; no sensitive data in scope narrows the operational surface; Art. 17(3) carve-outs apply as exception structure without relaxing the duty. |
| AG-D-05.3-002 | Upon end of processing services, the processor deletes or returns all personal data to the controller and deletes existing copies, unless Union or Member State law requires storage, with evidentiary confirmation available to the controller. | achieve | accountability | SO-D-05.3.HL | Art. 28(3)(g) | PR.DS-10, GV.SC-04 | Restated for TinyTask's processor role over customer task data; the deletion-or-return obligation activates at contract end; GV.SC-04 evidentiary confirmation (audit, test result, or independent inspection) retained so the controller can discharge Art. 5(2) accountability. |
| AG-D-05.3-003 | The product exposes a discoverable user-interface affordance allowing the user to securely and easily remove, on a permanent basis, all data and settings of the product, with decommissioning instructions supplied; where data can be transferred to other products or systems, the transfer is done in a secure manner. | achieve | accountability | SO-D-05.3.HL | Annex I Part I (2)(m); Annex II §8(d) | PR.DS-10, ID.AM-08 | Restated for a default-class SaaS product with self-assessment conformity; "securely and easily" retained as VAG (both required via discoverable affordance); "permanent basis" = recovery-infeasible; the second limb (secure cross-product transfer) is structurally relevant to D-03.3 per corpus and is included here as part of the Sub-SO objective; the affordance is independent of GDPR Art. 17(3) carve-outs. |

### D-05.4 — Data Portability

**Framing (company context conditioning every goal below):**

> TinyTask Lda. is an 8-employee B2B SaaS company (Portugal, EU) operating a rule-based task-management platform on managed cloud. It acts as **controller** for customer account metadata (names, emails, passwords) and as **processor** for customer task data containing personal data of the customers' own users. No AI/ML systems are developed, deployed, or integrated. The platform is placed on the EU market under CRA default product class (self-assessment conformity). NIS 2, DORA, and AI Act are out of scope. The portability obligation under GDPR Art. 20 applies to TinyTask in its controller role (customer account data) and, in its processor role, as an assistance duty under Art. 28(3)(e) for the business-customer controller's task-data portability requests.

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-05.4-001 | On a valid Art. 20(1) request, deliver the portability-eligible personal data in a structured, commonly used, machine-readable format (Art. 15(3) companion copy), reflecting current processing truth rather than a stale snapshot. | achieve | privacy-right | SO-D-05.4.HL | Art. 20(1); Art. 15(3) | PR.DS-10; ID.AM-08 | Restated for TinyTask's B2B SaaS context where portability-eligible data comprises customer account metadata and task data processed on consent/contract basis via automated means; the structural format floor (machine-readable, structured, commonly used, interoperable downstream) is preserved without prescribing a specific serialization format. |
| AG-D-05.4-002 | Where technically feasible, transmit the portability-eligible data directly to the receiving controller on the data subject's behalf, with destination authentication and integrity protection on the transfer. | achieve | privacy-right | SO-D-05.4.HL | Art. 20(2) | PR.DS-10 | Restated to reflect that for an 8-employee B2B SaaS on managed cloud, "technically feasible" is assessed per request; the obligation is conditional and does not mandate a standing cross-controller pipeline infrastructure; the data subject retains the right to transmit themselves where direct transmission is infeasible. |
| AG-D-05.4-003 | Respond to a valid Art. 20 portability request within one month (extendable to two months for complex requests with reasoned extension notice delivered within the original period), free of charge. | maintain | privacy-right | SO-D-05.4.HL | Art. 12(3); Art. 12(5) | ID.AM-08 | Restated to reflect that for a small B2B SaaS with manageable data volumes, the one-month service-level is the operational commitment; the two-month extension applies to genuinely complex multi-source requests; no fee may be charged regardless of the data volume. |
| AG-D-05.4-004 | Do not export personal data where the Art. 20(3) qualifying conditions (consent or contract basis AND automated means) are not met, where Art. 20(4) exclusions (public-interest-task or legitimate-interest processing) apply, or where the export would adversely affect third-party rights and freedoms. | avoid | privacy-right | SO-D-05.4.HL | Art. 20(3); Art. 20(4) | — | Restated to make explicit that scope qualifiers are pre-conditions checked before any export action; for TinyTask's B2B SaaS, the consent/contract basis is the dominant processing ground making most data portability-eligible, while legitimate-interest processing (e.g., fraud detection) would be excluded; the third-party-rights carve-out is a rare-but-honest structural qualifier. |
| AG-D-05.4-005 | Inform the data subject of the Art. 20 portability right at the time of data collection (Art. 13(2)(b)) or within a reasonable period where data are collected from another source (Art. 14(2)(c)). | achieve | accountability | SO-D-05.4.HL | Art. 13(2)(b); Art. 14(2)(c) | — | Restated to reflect that for a B2B SaaS with customer accounts, the information-supply occurs at account registration (Art. 13) and for data collected indirectly from the business customer (Art. 14); the notice is a standard clause in the privacy policy and terms of service. |
| AG-D-05.4-006 | Record the categories of data subjects and personal data subject to portability in the Record of Processing Activities (Art. 30(1)(b)), and conduct a DPIA where the portability pipeline introduces high-risk processing (Art. 35(7)), as part of the Art. 5(2) accountability duty. | maintain | accountability | SO-D-05.4.HL | Art. 30(1)(b); Art. 35(7); Art. 5(2) | ID.AM-08 | Restated to reflect that for an 8-employee B2B SaaS, the RoPA entry is a single record covering the portability-eligible data categories; a DPIA is triggered only if the portability pipeline introduces high-risk processing (unlikely for a rule-based platform without AI/ML systems). |

### D-06.1 — Vendor Risk Assessment (Supply-Chain Due Diligence)

> TinyTask Lda. is an 8-employee B2B SaaS productivity-tools company (Portugal, EU) that develops and places a rule-based task-management platform on the EU market as **manufacturer** (CRA default class, self-assessment conformity) and acts as **controller** for customer-account personal data and **processor** for customers' task data (GDPR). One external payment provider operates as a sub-processor for payment metadata only. NIS 2, DORA, and AI Act are excluded per the fact sheet. No AI/ML systems are developed, deployed, or integrated.

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-06.1-001 | Before engaging the external payment provider as a sub-processor, the controller verifies that the provider offers sufficient guarantees to implement appropriate technical and organisational measures so that processing meets GDPR requirements and protects data-subject rights; the Art. 28(3) closed-list DPA clauses (a)–(h) are documented in the processor contract and the Art. 28(2) sub-processor authorisation chain is maintained in the Art. 30(2) RoPA processor record. | achieve | accountability | SO-D-06.1.HL | Art. 28(1); Art. 28(2); Art. 28(3)(a)–(h) | GV.SC-02, GV.SC-03 | Proportionally scoped to the single external payment-provider sub-processor relationship at 8-employee SaaS scale; the EDPB Guidelines 07/2020 4-factor assessment operationalises the qualitative `sufficient guarantees` threshold for that one processor engagement rather than a multi-processor portfolio. |
| AG-D-06.1-002 | When integrating components sourced from third parties — including components of free and open-source software not made available on the market in the course of a commercial activity — the manufacturer exercises due diligence (procedural and substantive) so that those components do not compromise the cybersecurity of the product with digital elements; on becoming aware of a component vulnerability, the manufacturer addresses and remediates it without delay and shares relevant information with the component supplier. | achieve | I | SO-D-06.1.HL | Art. 13(5); Art. 13(6); Art. 3(48) | GV.SC-01, GV.SC-02 | Proportionally scoped to the self-assessment-class SaaS platform's third-party component set (commercial libraries and non-commercial OSS) at 8-employee manufacturer scale; the R3 procedural + substantive due-diligence reading applies with OSS-specific calibration (stewardship, CVD policy, vulnerability-disclosure channel) rather than a multi-tier enterprise supply-chain programme. |

### D-06.2 — Software Bill of Materials (SBOM)

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-06.2-001 | The manufacturer draws up and maintains a software bill of materials (SBOM) covering the components and dependencies in the product with digital elements, in a commonly used and machine-readable format including at minimum the top-level dependencies; the SBOM is retained in the technical documentation through the support period and the 10-year retention tail; on a reasoned request from a market surveillance authority, the SBOM is provided where necessary for the authority to check compliance with the Annex I cybersecurity requirements. | maintain | accountability | SO-D-06.2.HL | Annex I Part II (1); Annex VII §2(b); Annex VII §8; Art. 3(39) | ID.AM-02, GV.SC-02 | Restated from the corpus baseline for TinyTask's 8-employee B2B SaaS scale — the three-anchored SBOM architecture (authoring, retention, MSA disclosure) is discharged with a documented technical-documentation artefact bundle and an MSA-request log; the optional Annex II §9 user-facing access is at manufacturer's discretion and not enabled by default for B2B products; GDPR confirmed in pack but carries no SBOM obligation in this sub-domain (CRA sole authority per AEGIS taxonomy §4.1). |

### D-06.3 — High-level Security Objective (regulation-neutral)

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-06.3-001 | Maintain a processor contract with each sub-processor (currently the external payment provider) containing the Art. 28(3)(a)–(h) eight-element closed-list clauses (documented instructions, confidentiality, Art. 32 measures, sub-processor authorisation, data-subject-rights assistance, incident assistance, deletion-or-return, audit/inspection); maintain an Art. 46 appropriate-safeguards instrument for any third-country transfer lacking an adequacy decision; apply an Art. 48 filter that recognises third-country court or administrative requests for personal-data disclosure only through an international-agreement basis. | maintain | accountability | SO-D-06.3.HL | Art. 28(3)(a)–(h); Art. 46; Art. 48 | GV.SC-03 | Restated from corpus requirement 6.3.1 to the company's single-sub-processor (payment-provider) scale; the DPA matrix reduces to one processor contract; Art. 46/48 apply conditionally on hosting or payment-provider jurisdiction outside the EEA. |
| AG-D-06.3-002 | As manufacturer of a default-class product with digital elements, upon identifying a vulnerability in an integrated component, report it to the person or entity manufacturing or maintaining that component and address and remediate it in accordance with Annex I Part II; Art. 19 importer pre-market verification and Art. 20 distributor due-care and non-conformity escalation duties apply to downstream economic operators in the supply chain, not to the manufacturer. | achieve | accountability | SO-D-06.3.HL | Art. 13(6); Art. 19(1)–(3); Art. 20(1)–(4) | GV.SC-04 | Restated from corpus requirement 6.3.3 to the manufacturer role; Art. 13(6) is the directly operative obligation for TinyTask; Art. 19/20 are scoped to downstream importers/distributors and retained for supply-chain completeness per the DIFFERENT-PERSPECTIVE CRDA classification. |

### D-07.1 — Secure-by-Design Principles

**Framing (company context conditioning every goal below):**

> TinyTask Lda. is an 8-employee B2B SaaS company in Portugal (EU) developing and operating a rule-based task-management platform sold by commercial subscription. It acts as **controller** for customer account data (names, emails, passwords) and **processor** for customer task data. It develops the software itself and places the product (web + mobile interface) on the EU market as a **CRA manufacturer** in the default product class with self-assessment (internal-production-control) conformity. No AI/ML systems are developed, deployed, or integrated. Hosting is managed cloud. NIS2, DORA, and AI Act are not applicable to this entity.

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-07.1-001 | The controller implements appropriate technical and organisational measures — such as pseudonymisation — designed to implement data-protection principles (data minimisation) in an effective manner and to integrate the necessary safeguards into the processing at the time of means-determination and at the time of processing, and ensures that by default only personal data necessary for each specific purpose are processed, calibrated to the state of the art, cost of implementation, nature/scope/context/purposes of processing, and risks of varying likelihood and severity for an 8-person SaaS platform on managed cloud. | achieve | privacy-right | SO-D-07.1.HL | Art. 25(1) GDPR; Art. 25(2) GDPR | PR.PS-06, ID.AM-08 | Restated from the corpus controller-side by-design + by-default obligation (req 7.1.1) to the company's scale: the 4-factor qualitative proportionality is applied to a small SaaS controller/processor on managed cloud; by-default limits (amount, extent, storage period, accessibility) are operationalised through the platform's minimal-data-collection and minimal-access design; no mechanism prescribed beyond the OJ text. |
| AG-D-07.1-002 | The manufacturer ensures that the product with digital elements (SaaS platform + web/mobile interface) has been designed, developed and produced in accordance with the essential cybersecurity requirements set out in Annex I Part I, with the cybersecurity risk assessment taken into account across the planning, design, development, production, delivery and maintenance phases, with a view to minimising cybersecurity risks, preventing incidents, and minimising their impact including in relation to the health and safety of users, at the scale of a default-class self-assessment manufacturer. | achieve | I | SO-D-07.1.HL | Art. 13(1) CRA; Art. 13(2) CRA | PR.PS-06, GV.PO-02 | Restated from the corpus manufacturer-side product by-design + 6-phase risk-assessment-propagation obligation (req 7.1.3) to the company's scale: the 6-phase propagation applies to the SaaS + web/mobile product lifecycle; Annex I Part I essential requirements are applied at the default-class self-assessment conformity level; no AI/ML components are present, so AI-Act-specific attack categories do not apply. |

### D-07.2 — Secure Coding Practices

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-07.2-001 | The product with digital elements is designed, developed, and produced to limit its attack surfaces, including external interfaces, and to reduce the impact of an incident using appropriate exploitation-mitigation mechanisms and techniques, demonstrated through the design/development documentation and risk-assessment record | achieve | I | SO-D-07.2.HL | CRA Annex I Part I (2)(j); CRA Annex I Part I (2)(k); CRA Art. 13(1); CRA Art. 13(2) | PR.PS-01, PR.PS-02 | Restated for 8-FTE rule-based SaaS manufacturer (no AI/ML, no DORA, no AI Act); CRA participation is partial (outcome-level mandates only, no coding-standard prescription in OJ); coding-practices baseline from industry frameworks demonstrated against Annex I Part I (2)(j)+(k) via Annex VII §2/§3 records; HL SO not activated (single-regulation scope, no Conditional-Y overlap) |

### D-09.1 — Information Security Policies

**Framing (company context):** TinyTask Lda. is an 8-employee B2B SaaS company in Portugal (EU) that develops and operates a rule-based task-management platform sold by commercial subscription. Regulatory roles: **controller** (customer account data: names, emails, passwords) and **processor** (customer task data) under GDPR; **manufacturer** under CRA (self-developed product with digital elements placed on the EU market, default product class, self-assessment conformity). No AI/ML systems developed, deployed, or integrated. NIS 2, DORA, and AI Act are out of scope. Hosting is managed cloud.

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-09.1-001 | The controller maintains documented data-protection policies designed to implement data-protection principles in an effective manner, reviewed and updated where necessary in light of the nature, scope, context, and purposes of processing and the associated risks, and is able to demonstrate continuous compliance to the supervisory authority. | maintain | accountability | SO-D-09.1.HL | Art. 24(1); Art. 5(2) | GV.PO-01 | DPO designation (Art. 37–39) assessed as not triggered for an 8-employee B2B SaaS with no special-category processing and no large-scale systematic monitoring; policy content remains entity-discretionary per the Art. 24(1) "such as" formulation; review cadence is a material-change-of-risk trigger supplemented by periodic review. |
| AG-D-09.1-002 | The manufacturer maintains documented policies, processes, and procedures necessary to implement its CRA cybersecurity obligations, including a coordinated vulnerability disclosure policy, a secure-update distribution mechanism, a support-period determination methodology, and a cessation-of-operations communication procedure, with the presumption-of-conformity machinery tracked via harmonised standards, common specifications, or CSA certification. | maintain | accountability | SO-D-09.1.HL | Art. 13(8); Art. 27(1) | GV.PO-01 | OSS-steward policy (Art. 24(1)) applicability not confirmed in the fact sheet — recorded as open question; manufacturer-side obligations (Art. 13(8) + Art. 27 presumption) are the operative carrier for a self-developed SaaS product in the default product class with self-assessment conformity. |

### D-09.2 — Impact and Risk Assessments

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-09.2-001 | Where processing is likely to result in a high risk to the rights and freedoms of natural persons, a documented data-protection impact assessment covering the four Art. 35(7) content items (systematic description of envisaged processing and purposes; necessity and proportionality assessment; risks to data-subject rights and freedoms; measures to address those risks) is in place before processing begins; where residual risk remains high, prior consultation with the supervisory authority is sought. | achieve | privacy-right | SO-D-09.2.HL | Art. 35(1); Art. 35(7); Art. 36(1) | ID.RA-05; ID.RA-P4 | Restated for an 8-employee B2B SaaS controller processing customer account metadata and task data; the four Art. 35(7) content items are mandatory regardless of entity size; no mechanism or tool prescribed. |
| AG-D-09.2-002 | The data-protection impact assessment is reviewed where there has been a change of the risk represented by the processing operations, with the review records identifying the trigger event, date, assessment of the change, residual-risk recalculation, and any updated measures. | maintain | privacy-right | SO-D-09.2.HL | Art. 35(11) | ID.IM-04; ID.RA-P5 | Restated for a small B2B SaaS controller; the on-change review trigger is mandatory; a documented periodic-review cadence supplements the material-change trigger per the corpus interpretation; no mechanism prescribed. |
| AG-D-09.2-003 | Before placing the product with digital elements on the EU market, a documented cybersecurity risk assessment covering the intended purpose and reasonably foreseeable use (including operational environment and assets to be protected) is in place, indicating whether and in what manner Annex I Part I (2) requirements apply and how those requirements are implemented as informed by the risk assessment, recorded in the Annex VII §3 risk-assessment record. | achieve | I | SO-D-09.2.HL | Art. 13(2); Art. 13(3) sentence 1; Art. 13(3) sentence 2; Art. 13(3) sentence 3; Annex VII §3 | ID.RA-05; GV.PO-02 | Restated for a default-class manufacturer (self-assessment conformity) of a rule-based SaaS product; the Annex I Part I (2) applicability mapping is mandatory; the CRA Art. 13(4) sentence 2 consolidation rule does not apply (no AI Act applicability for this entity); no mechanism prescribed. |
| AG-D-09.2-004 | The cybersecurity risk assessment is updated during the support period as appropriate, including upon becoming aware of a previously unidentified vulnerability, with the Annex VII §3 risk-assessment record kept current and available to market surveillance authorities for the retention period. | maintain | I | SO-D-09.2.HL | Art. 13(3) sentence 1; Art. 13(7) | GV.OV-02; ID.IM-04 | Restated for a small manufacturer with a defined support period; the update obligation is mandatory regardless of entity size; the 10-year retention per Art. 13(13) applies; no mechanism prescribed. |

### D-09.4 — Records of Processing Activities and Technical Documentation

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-09.4-001 | TinyTask, as controller of customer account data and processor of customer task data, maintains a single record of processing activities covering both roles, in writing or electronic form, containing the Art. 30(1)(a)–(g) content items, made available to the supervisory authority on request; the Art. 30(5) 250-employee exception does not apply because processing is continuous (SaaS) and not occasional. | maintain | accountability | SO-D-09.4.HL | Art. 30(1); Art. 30(2); Art. 30(3); Art. 30(4); Art. 30(5) | ID.AM-03, GV.PO-02 | Restated at 8-employee scale: one entity holds both controller and processor roles, so a single RoPA suffices; the 250-employee exception is explicitly assessed and inapplicable (continuous SaaS processing of names, emails, passwords, task data); no special-category data per fact sheet. |
| AG-D-09.4-002 | TinyTask, as manufacturer of a default-class product with digital elements (SaaS platform + web/mobile interface) placed on the EU market under self-assessment (Module A), draws up the Annex VII §1–§8 technical documentation before placing on the market, draws up the EU declaration of conformity, affixes the CE marking, and keeps the technical documentation and EU declaration at the disposal of market surveillance authorities for at least 10 years or the support period, whichever is longer. | maintain | accountability | SO-D-09.4.HL | Art. 13(12); Art. 13(13); Annex VII §1–§8 | GV.PO-02, GV.OC-03 | Restated for default-class self-assessment manufacturer: no notified-body involvement; Annex VII 8-item content list applies in full; 10-year or support-period retention (whichever longer) is the continuing obligation; no AI/ML components to document (rule-based platform per fact sheet). |

### D-10.1 — Continuous Security Monitoring

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-10.1-001 | The company maintains continuous monitoring of its personal-data processing systems (customer account metadata and task data on managed-cloud hosting) for the five Art. 32(2) risk types — accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to personal data — and defines the moment of becoming aware of a breach to anchor the Art. 33(1) 72-hour notification clock. | maintain | C | SO-D-10.1.HL | Art. 32(1)(b); Art. 32(1)(d); Art. 32(2); Art. 33(1) | RS.CO-03, RS.MA-04 | Scope narrowed from a generic entity-level 5-risk-type monitoring to the company's specific B2B SaaS processing systems (8-employee, managed-cloud, two data categories); the 5-risk-type enumeration and 72-hour clock are unchanged; no enterprise-wide multi-system monitoring is required at this scale. |
| AG-D-10.1-002 | The product with digital elements (rule-based task management platform, web and mobile interfaces) records and monitors relevant internal activity — access to or modification of data, services, or functions — and provides a user opt-out mechanism; the manufacturer facilitates the sharing of information about potential vulnerabilities through a single contact address. | achieve | I | SO-D-10.1.HL | Annex I Part I (2)(l); Annex I Part II (6) | DE.CM-09, DE.CM-01 | Scope narrowed to a single-product B2B SaaS platform in the default product class (self-assessment conformity); on-device monitoring covers the platform's web and mobile interfaces; the user opt-out applies to the business customer's end-users; the vulnerability contact address is a single point for one product. |

### D-10.2 — Audit Logging & Traceability

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-10.2-001 | The company maintains compliance records — records of processing activities, consent records, processor contract records, breach notification records, and DPIA records — in writing or in electronic form with integrity and traceability sufficient to demonstrate compliance and to support supervisory-authority inspections, made available to the supervisory authority on request. | maintain | accountability | SO-D-10.2.HL | Art. 30(3); Art. 5(2); Art. 31 | GV.PO-02; GV.OV-03 | Scope narrowed to an 8-employee B2B SaaS controller (customer account metadata) and processor (customer task data); no special-category data; processor-role records (Art. 28(3) contracts with the external payment sub-processor) are the primary processor-side artefact; the 250-employee Art. 30(5) exception is inapplicable because processing is a core, non-occasional business activity. |
| AG-D-10.2-002 | The manufacturer maintains the technical documentation (general product description, design and development information, harmonised standards applied, test reports, EU declaration of conformity, and the software bill of materials on MSA reasoned request), preserves the cybersecurity risk-assessment documentation with updates as appropriate during the support period, and ensures test reports demonstrating conformity with Annex I Part I and Part II are part of the technical documentation and available on reasoned request from market surveillance authorities. | maintain | accountability | SO-D-10.2.HL | Annex VII §5–§8; Annex VII §3; Annex I Part II (3); Art. 13(4) sentence 1; Art. 13(22) | GV.OC-03; ID.RA-04 | Scope narrowed to an 8-employee manufacturer of a rule-based SaaS platform (default product class, self-assessment conformity); no AI/ML components; SBOM scope limited to the platform's software components; support-period retention (10 years or support period, whichever longer) applies to the SaaS product lifecycle. |

### §4.1 Control Anchor Mapping (applicable regulations only — rule R8)

| ID | Regulation | CSF 2.0 | NIST PF 1.1 | NIST AI RMF | Source |

|---|---|---|---|---|---|

| AG-D-01.1-001 | GDPR | PR.DS-01, PR.DS-10 | PR.DS-P1, PR.PO-P3 | — | SR-GDPR-001 |

| AG-D-01.1-002 | CRA | PR.DS-01 | — | — | SR-CRA-002 |

| AG-D-01.2-001 | GDPR | PR.DS-02, PR.IR-01 | PR.DS-P2, PR.AC-P5 | — | `SR-GDPR-002` |

| AG-D-01.2-002 | CRA | PR.DS-02, PR.IR-01 | — | — | `SR-CRA-003` |

| AG-D-02.1-001 | GDPR | ID.RA-01, PR.PS-02 | GV.MT-P3, CT.DM-P10 | — | SR-GDPR-007 |

| AG-D-02.1-002 | CRA | ID.RA-01, ID.AM-02 | — | — | SR-CRA-006 |

| AG-D-02.3-001 | CRA | GV.PO-01, GV.SC-04 | — | — | SR-CRA-019 |

| AG-D-02.3-002 | CRA | RS.CO-03, GV.SC-04 | — | — | SR-CRA-020 |

| AG-D-02.3-003 | CRA | GV.SC-04, RS.CO-03 | — | — | SR-CRA-021 |

| AG-D-03.1-001 | GDPR | PR.AA-03, PR.AA-02, ID.AM-08 | PR.AC-P6, PR.AC-P3, CT.DP-P4 | — | SR-GDPR-009, SR-GDPR-010 |

| AG-D-03.1-002 | CRA | PR.AA-01, ID.AM-01, PR.AA-05, PR.AA-06, DE.CM-09 | — | — | SR-CRA-023, SR-CRA-024 |

| AG-D-03.2-001 | GDPR | PR.AA-05, PR.AA-06 | PR.AC-P1, PR.AC-P2, CT.PO-P1 | — | SR-GDPR-011, SR-GDPR-012 |

| AG-D-03.2-002 | GDPR | PR.AA-06, PR.AT-02 | PR.AC-P1, PR.AC-P2, CT.PO-P1 | — | SR-GDPR-011, SR-GDPR-012 |

| AG-D-03.2-003 | CRA | PR.AA-01, ID.AM-01 | — | — | SR-CRA-023, SR-CRA-024 |

| AG-D-04.1-001 | GDPR | DE.CM-01, DE.CM-09, RS.MA-02 | GV.MT-P5, GV.MT-P3, CM.AW-P7 | — | SR-GDPR-014 |

| AG-D-04.1-002 | CRA | PR.PS-04, DE.AE-08, DE.CM-09, DE.CM-01 | — | — | SR-CRA-027; SR-CRA-100 |

| AG-D-04.3-001 | GDPR | RS.CO-02, RS.MA-04, RS.MA-03 | CM.AW-P7, CM.PO-P2 | — | SR-GDPR-016 |

| AG-D-04.3-002 | CRA | RS.MA-02, RS.CO-02, RS.AN-03, RS.AN-07 | — | — | SR-CRA-029; SR-CRA-030 |

| AG-D-05.1-001 | GDPR | ID.AM-08, ID.AM-03 | CT.PO-P4, CT.DP-P4, ID.RA-P3 | — | SR-GDPR-025 |

| AG-D-05.1-002 | GDPR | ID.AM-08 | CT.PO-P4, CT.DP-P4, ID.RA-P3 | — | SR-GDPR-025 |

| AG-D-05.1-003 | GDPR | GV.OC-03 | GV.PO-P5, CT.DP-P2, ID.RA-P3 | — | SR-GDPR-028 |

| AG-D-05.1-004 | CRA | ID.AM-08, ID.AM-03 | — | — | SR-CRA-046 |

| AG-D-05.2-001 | GDPR | ID.AM-08, ID.AM-03 | CT.PO-P4, CT.DM-P5 | — | SR-GDPR-029 |

| AG-D-05.2-002 | CRA | PR.PS-02, GV.OV-02 | — | — | SR-CRA-016; SR-CRA-047 |

| AG-D-05.3-001 | GDPR | PR.DS-10, ID.AM-08 | CT.DM-P4, CT.DM-P5 | — | SR-GDPR-030 |

| AG-D-05.3-002 | GDPR | PR.DS-10, GV.SC-04 | CT.DM-P4, CT.DM-P5, ID.DE-P3 | — | SR-GDPR-031 |

| AG-D-05.3-003 | CRA | PR.DS-10, ID.AM-08 | — | — | SR-CRA-048 |

| AG-D-05.4-001 | GDPR | PR.DS-10; ID.AM-08 | CT.DM-P1; CT.DM-P6 | — | SR-GDPR-032 |

| AG-D-05.4-002 | GDPR | PR.DS-10; ID.AM-08 | CT.DM-P1; CT.DM-P6 | — | SR-GDPR-032 |

| AG-D-05.4-003 | GDPR | PR.DS-10; ID.AM-08 | CT.DM-P1; CT.DM-P6 | — | SR-GDPR-032 |

| AG-D-05.4-004 | GDPR | PR.DS-10; ID.AM-08 | CT.DM-P1; CT.DM-P6 | — | SR-GDPR-032 |

| AG-D-05.4-005 | GDPR | PR.DS-10; ID.AM-08 | CT.DM-P1; CT.DM-P6 | — | SR-GDPR-032 |

| AG-D-05.4-006 | GDPR | PR.DS-10; ID.AM-08 | CT.DM-P1; CT.DM-P6 | — | SR-GDPR-032 |

| AG-D-06.1-001 | GDPR | GV.SC-02, GV.SC-03 | ID.DE-P5, ID.IM-P2 | — | SR-GDPR-033 |

| AG-D-06.1-002 | CRA | GV.SC-01, GV.SC-02, ID.RA-02 | — | — | SR-CRA-050 |

| AG-D-06.2-001 | GDPR | — | — | — | — |

| AG-D-06.2-001 | CRA | ID.AM-02, GV.SC-02 | — | — | SR-CRA-008 |

| AG-D-06.3-001 | GDPR | GV.SC-03 | ID.DE-P3 | — | SR-GDPR-034 |

| AG-D-06.3-002 | CRA | GV.SC-04, RS.MI-02 | — | — | SR-CRA-051 |

| AG-D-07.1-001 | GDPR | PR.PS-06, ID.AM-08 | GV.PO-P2, CT.PO-P4 | — | SR-GDPR-039 |

| AG-D-07.1-002 | CRA | PR.PS-06, GV.PO-02 | — | — | SR-CRA-064 |

| AG-D-07.2-001 | CRA | PR.PS-01, PR.PS-02 | — | — | SR-CRA-067 |

| AG-D-09.1-001 | GDPR | GV.PO-01, GV.PO-02, GV.RM-04 | GV.PO-P1, GV.PO-P6 | — | SR-GDPR-043 |

| AG-D-09.1-002 | CRA | GV.PO-01, GV.SC-01 | — | — | SR-CRA-075 |

| AG-D-09.2-001 | GDPR | ID.RA-01; ID.RA-05; ID.RA-06 | ID.RA-P3; ID.RA-P4; ID.RA-P5 | — | SR-GDPR-045 |

| AG-D-09.2-002 | GDPR | ID.IM-04; ID.RA-06 | ID.RA-P5; GV.MT-P2 | — | SR-GDPR-047 |

| AG-D-09.2-003 | CRA | PR.PS-06; GV.PO-02; ID.RA-05 | — | — | SR-CRA-066 |

| AG-D-09.2-004 | CRA | GV.OV-02; ID.IM-04 | — | — | SR-CRA-081 |

| AG-D-09.4-001 | GDPR | ID.AM-03, GV.PO-02 | ID.IM-P1, ID.IM-P4, ID.IM-P6, ID.IM-P8 | — | SR-GDPR-048 |

| AG-D-09.4-002 | CRA | GV.PO-02, GV.OC-03 | — | — | SR-CRA-085 |

| AG-D-10.1-001 | GDPR | RS.CO-03, RS.MA-04 | CM.AW-P7, CM.AW-P8 | — | SR-GDPR-014 |

| AG-D-10.1-002 | CRA | DE.CM-09, DE.CM-01 | — | — | SR-CRA-100 |

| AG-D-10.2-001 | GDPR | GV.PO-02, GV.OV-03 | GV.MT-P3, GV.PO-P5 | — | SR-GDPR-050 |

| AG-D-10.2-002 | CRA | GV.OC-03, ID.RA-04 | — | — | SR-CRA-088 |

## §5 Ambiguities & Open Questions

> ASSUMPTION: The cross-regulation analysis (CRDA-deep, all 6 pairs SAME) confirms that meeting the CRA state-of-the-art floor discharges the GDPR "appropriate" obligation on the at-rest dimension for the same product artefact; however, the GDPR controller's deployment-side risk assessment and cipher-strength selection remain TinyTask's own obligation independent of the CRA product-level baseline (scope caveat in cross/_interactions.md).
> ASSUMPTION: TinyTask's managed-cloud hosting arrangement means the physical encryption implementation is partly delegated to the cloud provider; the obligation to ensure "appropriate technical measures" (GDPR) and "state-of-the-art mechanisms" (CRA) remains with TinyTask as controller/processor and manufacturer respectively, and the company's risk assessment must evidence that the delegated implementation meets the applicable threshold.
> OPEN QUESTION: Data scale (rough figure) is not stated in the intake (fact_sheet open_questions); the "appropriate" threshold under the Art. 32(1) preamble factors (costs of implementation, nature, scope, context, purposes, risks) may be affected by data volume, and the company's risk assessment should record the scale assumption.
> ASSUMPTION: The cross-regulation corpus (CRDA-deep, all 3 pairs verified SAME) states that a CRA-compliant in-transit configuration discharges the GDPR Art. 32(1)(b)/(2) in-transit obligation on the same channel. Both goals are retained independently because TinyTask's GDPR obligation (controller/processor on its own deployment channels) and CRA obligation (manufacturer on the product) are separate compliance tracks per the scope caveat in `cross/_interactions.md`; the discharge relationship is noted for Phase 2 verification design but does not eliminate either goal.
> Open question (from fact sheet): `data_scale` is not stated in the intake. This does not alter the goal wording (the obligation is risk-anchored, not volume-anchored) but will affect the Phase 2 risk-assessment evidence pack under GDPR Art. 32(2).
> ASSUMPTION: The CRA "support period" (Art. 13(8)) under which the vulnerability register and SBOM must be maintained is assumed to correspond to the commercial subscription lifecycle defined in TinyTask's terms of service; the specific duration is not stated in the intake fact sheet.
> ASSUMPTION: The GDPR Art. 32(1) preamble factor "costs of implementation" is interpreted at the scale of an 8-employee company using managed-cloud hosting; the periodic testing cadence (e.g., at least semi-annual vulnerability scans plus event-triggered re-testing on material change) is the proportionate discharge of "regularly" for this scale, consistent with the cross-regulation note that any tighter cadence discharges the obligation.
> OPEN QUESTION: The fact sheet records `data_scale: not stated in the intake`. A rough data-volume or data-subject-count figure would allow calibration of the Art. 32(1) "nature, scope, context, purposes, risks" factors and the DPIA review trigger granularity; the goal is stated at the regulation's altitude pending that input.
> ASSUMPTION: GDPR is confirmed as applicable to the company (controller/processor for EU personal data) but carries no CVD obligation in D-02.3; regs/GDPR.md explicitly states "No CVD mandate; CRA sole authority per taxonomy §4.1" and "(no GDPR Sub-SO or requirements in this sub-domain)." No GDPR-derived goal is produced for this sub-domain.
> ASSUMPTION: The baseline HL (SG-D-02.3.HL) references the NIS 2 Art. 12(1) CSIRT-coordinated pathway for the integrated manufacturer-as-NIS-2-entity stack. NIS 2 is not confirmed for this entity (excluded per fact_sheet: 8 employees, non-critical service, not in Annex I/II essential sectors); the NIS 2 leg of the baseline HL is therefore inapplicable and no NIS 2-derived goal is produced.
> ASSUMPTION: Per the cross-regulation aggregation logic (cross/_interactions.md), the CRA "verifiable manner" floor discharges the GDPR "reasonable means proportionate to risk" on the identity-management dimension when TinyTask operates both manufacturer-side and controller-side roles on the same identity substrate; the evidence layer must document which artefacts support which regulatory role.
> ASSUMPTION: The boundary between the GDPR data-subject verification discipline (AG-D-03.1-001) and the CRA product-user identity-management discipline (AG-D-03.1-002) is a controlled hand-off at the rights-exercise endpoint; the two goals are layered, not collapsed, and the identity-subject divergence (external data subjects vs. product users/services/components) is preserved in separate evidence templates.
> OPEN QUESTION: Data scale (rough volume of rights requests and records) is not stated in the intake; the proportionality calibration of the graduated-verification standard in AG-D-03.1-001 (e.g., which request classes trigger document verification vs. strong authentication) depends on this figure and should be confirmed before Phase 2 objective refinement.
> ASSUMPTION: The external payment provider is treated as a sub-processor under GDPR Art. 28(3)(b) for payment metadata only, per the fact-sheet `third_party_processing` entry; no additional sub-processor chain is assumed.
> ASSUMPTION: The product's "individual logins" access model (fact-sheet `access_model`) is the authentication substrate to which the CRA Annex I Part I (2)(d) "appropriate control mechanisms" obligation attaches; no service-to-service or machine-identity authentication is in scope for this 8-employee SaaS product.
**Open question:** `data_scale` is not stated in the intake (fact-sheet `open_questions`); the proportionality calibration of AG-D-03.2-002 (Art. 12(6) verification means) and the risk-assessment depth of AG-D-03.2-003 (CRA Annex I Part I (2)(d)) cannot be quantitatively refined until a rough record-volume or user-count figure is provided.
> ASSUMPTION: The managed-cloud hosting environment constitutes the "data-flow boundary" for GDPR Art. 32(1)(b) detection purposes; the corpus does not further specify the boundary topology, and the fact sheet states only "managed cloud" without naming a provider or architecture.
> OPEN QUESTION (from fact sheet): `data_scale` — rough figure not stated in the intake. This does not alter the detection obligation but may affect the proportionality of monitoring coverage and the evidence-pack scope for the "becoming aware" timestamp records.
> ASSUMPTION: TinyTask's processor role for customer task data triggers GDPR Art. 33(2) (processor-to-controller notification without undue delay), which is a distinct obligation from the controller→DPA notification captured in AG-D-04.3-001. The D-04.3 module's requirement set (4.3.1) addresses only the controller→DPA leg; the processor→controller leg is outside this sub-domain's scope as defined in the corpus and is not restated here.
> ASSUMPTION: The fact sheet does not state a data-scale figure. The 72-hour GDPR clock and the CRA 24h/72h/14d tiers are absolute regulatory deadlines independent of data volume; no proportional relaxation is applied or assumed.
> OPEN QUESTION: When a single event simultaneously triggers both the GDPR personal-data-breach notification (AG-D-04.3-001) and the CRA AEV/SI notification (AG-D-04.3-002) — e.g., a vulnerability in the SaaS platform that also exposes customer personal data — the corpus (cross/_interactions.md) confirms the GDPR↔CRA relationship as SAME and mandates parallel notification to both DPA and CSIRT+ENISA on their respective clocks. The corpus defers the binding-procedure principle for simultaneous multi-recipient routing to Phase 1C Doc 07. No operationalisation principle is supplied at this step.
> ASSUMPTION: The company's CRA "intended purpose" (Art. 3(23)) is the rule-based task-management function as declared in the product's technical documentation under Annex VII §2; no AI/ML capability is present, so the intended purpose does not extend to training or inference functions.
> ASSUMPTION: The company's dual GDPR role (controller for customer account data; processor for task data containing end-user personal data) means the Art. 5(1)(c) minimisation obligation applies to both roles, but in the processor role the company is constrained by the controller's (business customer's) instructions and the necessity assessment is performed at the controller level.
**Open question:** The fact sheet does not state the approximate data scale (number of data subjects, volume of task data). The proportionality of the necessity-assessment documentation and the Art. 6(4) compatibility-assessment records depends on this figure; a rough order-of-magnitude is needed to confirm that the 8-employee-scale documentation burden is appropriate.
> ASSUMPTION: The company's SaaS platform (web + mobile interface) is treated as a single "product with digital elements" under CRA for the purposes of the support-period and update-availability obligations; no separate hardware or embedded-component retention duties arise.
**Open question (from fact sheet):** data_scale — rough volume figure not stated in the intake; the retention architecture must be scalable, but no specific volume threshold can be derived for the Art. 30(1)(f) RoPA time-limit documentation or the CRA Annex II information-accessibility evidence.
> ASSUMPTION: TinyTask's dual role (controller for customer account data; processor for customer task data) means both the Art. 17(1) controller-side erasure (AG-D-05.3-001) and the Art. 28(3)(g) processor-side mirror (AG-D-05.3-002) are operative on the same party; the processor mirror applies to the task-data processing relationship with business customers, and the controller-side Art. 17 path executes through the manufacturer's (2)(m) affordance at the architectural layer per the corpus layer-stacking pattern.
> ASSUMPTION: The CRA Annex I Part I (2)(m) second limb (secure cross-product transfer, SR-CRA-049) is included in AG-D-05.3-003 as part of the Sub-SO objective, but its dedicated requirement is not present in the D-05.3 CRA module; the corpus notes it is "structurally relevant to D-03.3 as well." No separate goal is emitted here for the second limb to avoid double-counting; the D-03.3 module is expected to carry its own requirement.
Open question: data_scale is not stated in the intake (fact_sheet.yaml); the operational calibration of the erasure procedure (backup retention windows, replica count, query-cache purge scope) depends on this figure and cannot be fixed at Phase 1A altitude.
> ASSUMPTION: TinyTask's dual role (controller for customer account metadata; processor for customer task data) means the Art. 20 portability obligation is directly binding in the controller capacity and arises as an Art. 28(3)(e) assistance duty in the processor capacity. The corpus requirement 5.4.1 is framed as a controller obligation; the processor-assistance dimension is not separately stated in the pack and is assumed to be subsumed under the same operational export pipeline.
> ASSUMPTION: CRA is confirmed in the pack (BUILD_MANIFEST) but the CRA module (regs/CRA.md) explicitly states "no CRA Sub-SO or requirements in this sub-domain." The CRA Annex I Part I (2)(m) second-limb secure cross-product transfer (SR-CRA-049) is a complementary technical anchor only and does not ground a CRA sub-SO or generate a separate adjusted goal on D-05.4. No CRA row appears in §4.1 because no CRA requirement or SR mapping exists for this sub-domain.
> ASSUMPTION: The "technically feasible" qualifier on Art. 20(2) sentence 2 cross-controller direct transmission is interpreted per the corpus as a per-request feasibility assessment rather than a standing infrastructure mandate; for an 8-employee B2B SaaS on managed cloud, this is expected to be feasible for the dominant use case (single-tenant SaaS export to another SaaS controller) but may be infeasible for edge cases (e.g., data spanning multiple storage backends).
> ASSUMPTION: The fact sheet states one external payment provider as the sole sub-processor; no additional processor engagements are assumed. If further processors are added, AG-D-06.1-001 extends to each new engagement without structural change.
> ASSUMPTION: The CRA component set is assumed to comprise the third-party libraries and non-commercial OSS dependencies declared in the product's build manifest; no transitive-depth-beyond-SBOM-top-level obligation is assumed beyond what Art. 13(5) sentence 1 requires for components the manufacturer integrates.
> OPEN QUESTION: The fact sheet does not state a rough data-scale figure; the proportionality calibration of the Art. 28(1) `sufficient guarantees` assessment (EDPB 4-factor) may shift if the customer base or task-data volume grows materially beyond the current 8-employee SaaS baseline.
> ASSUMPTION: GDPR is confirmed in the pack for sub-domain D-06.2 but the module explicitly states "no GDPR Sub-SO or requirements in this sub-domain" and "No SBOM mandate in GDPR; CRA sole authority per AEGIS taxonomy §4.1." The GDPR row in §4.1 therefore carries no anchors and no source; no GDPR-derived goal is emitted.
> ASSUMPTION: The optional Annex II §9 user-facing SBOM access is at the manufacturer's discretion ("if the manufacturer decides to make available"). For TinyTask's B2B SaaS product, this optional anchor is assumed not to be enabled by default; it does not generate a separate obligation or goal.
> ASSUMPTION: TinyTask Lda. acts as manufacturer (not importer or distributor) under CRA; therefore Art. 19 and Art. 20 obligations in requirement 6.3.3 are not directly applicable to the company and are retained in the goal only as supply-chain context for downstream economic operators. The directly operative CRA obligation in D-06.3 for TinyTask is Art. 13(6) component-vulnerability reporting.
> ASSUMPTION: The single sub-processor relationship (external payment provider for payment metadata) is the sole Art. 28(3) DPA in scope for D-06.3; no additional processors or sub-processors are identified in the fact sheet.
**Open question:** Data scale (volume of personal data processed) is not stated in the intake; this does not change the applicability of the goals above but may affect the proportionality of Art. 46 supplementary-measures assessment depth.
> ASSUMPTION: The company's dual GDPR role (controller for customer account data; processor for customer task data) means Art. 25(1) by-design obligations attach to the controller-side processing (account data). The processor-side obligation for customer task data is governed by Art. 28 and the controller's instructions; the adjusted goal AG-D-07.1-001 is scoped to the controller role as stated in the corpus baseline.
> ASSUMPTION: The data scale (volume of personal data processed) is not stated in the intake. The 4-factor proportionality under Art. 25(1) includes "nature, scope, context and purposes of processing" as a calibration factor; the absence of a stated data volume does not alter the obligation but may affect the depth of the documented necessity assessment. This is recorded as an open intake item, not a goal modification.
> ASSUMPTION: The CRA default-class self-assessment conformity path means the manufacturer performs its own conformity assessment (no notified body). The 6-phase risk-assessment propagation and Annex I Part I essential-requirement conformance are self-documented and retained in the Annex VII §2/§3 technical documentation for market-surveillance-authority inspection.
> ASSUMPTION: GDPR is confirmed as an applicable regulation for TinyTask Lda. (controller/processor for EU personal data), but the D-07.2 GDPR module explicitly states "(no GDPR Sub-SO or requirements in this sub-domain)" — GDPR is process- and outcome-oriented and does not specify secure-coding practices. No GDPR-derived goal is produced for D-07.2; this is a scope-exclusion by the OJ text, not a silent drop.
> ASSUMPTION: The high-level SO (SG-D-07.2.HL) is not activated for TinyTask Lda. per the objective.md activation rule: the company has CRA applicability only (no DORA, no AI Act), so no ≥2-regulation Conditional-Y scope overlap exists on a single coding event. The CRA Sub-SO (SG-D-07.2.CRA) applies independently and is restated as AG-D-07.2-001.
> ASSUMPTION: DORA and AI Act are excluded per the fact sheet (not a financial entity; no AI/ML systems developed, deployed, or integrated). Their D-07.2 modules are not confirmed and are not restated.
> ASSUMPTION: DPO designation under Art. 37(1) GDPR is not triggered for TinyTask based on the fact sheet (8 employees, no special-category data, no large-scale systematic monitoring of data subjects). If the processing profile changes (e.g., scale increases or special-category data enters scope), DPO designation and the Art. 38–39 independence and resourcing obligations would additionally apply.
> ASSUMPTION: TinyTask's status as an "open-source software steward" (Art. 3(14) CRA) is not confirmed in the fact sheet. If TinyTask maintains or stewards open-source software projects, the Art. 24(1) OSS-steward cybersecurity policy and Art. 24(2) MSA-cooperation obligations would additionally apply alongside the manufacturer obligations.
> ASSUMPTION: The Art. 30(5) 250-employee exception is assessed as inapplicable to TinyTask (8 employees) because the processing of customer account metadata (names, emails, passwords) and task data is continuous and not occasional, satisfying the Art. 30(5)(b) carve-out condition; no special-category or criminal-conviction data is processed per the fact sheet.
> ASSUMPTION: TinyTask's SaaS product is classified as a default-class product with digital elements under CRA, subject to Module A (internal production control / self-assessment) conformity; no notified-body or third-party conformity-assessment route is engaged.
> OPEN QUESTION: The exact data volume (number of data subjects, volume of task records) is not stated in the intake; this does not change the RoPA obligation (which is activity-based, not volume-based) but may affect the granularity of the Art. 30(1)(c) "categories of data subjects and of personal data" description.
> ASSUMPTION: TinyTask Lda. is simultaneously a GDPR controller (customer account metadata) and a CRA manufacturer (SaaS product with digital elements). The CRDA-flagged GENUINE TENSION — CRA Annex I Part I (2)(l) user opt-out vs. GDPR Art. 32(2) mandatory monitoring — applies to this company. Per the corpus, the two regimes stack on a layered architecture (entity-layer mandatory + product-layer with opt-out); the user's opt-out from CRA product-level monitoring does not exempt the company from GDPR Art. 32(2) entity-level monitoring. Layer 2 OJ-level resolution is deferred to Phase 1C Doc 07.
> ASSUMPTION: The data_scale (rough volume of personal data processed) is not stated in the intake; the monitoring proportionality under Art. 32(1) chapeau ("cost of implementation … nature, scope, context and purposes of processing") is assessed qualitatively at the 8-employee, two-data-category scale without a quantitative threshold.
> OPEN QUESTION: The exact boundary between "relevant internal activity" under CRA Annex I Part I (2)(l) and the GDPR Art. 32(2) 5-risk-type monitoring on the same SaaS platform is not further specified in the corpus for a single-product, single-tenant B2B SaaS; the layered stacking (entity-layer vs. product-layer) is assumed but the operational demarcation of which monitoring events are "product-level" (CRA) vs. "entity-level" (GDPR) requires Phase 2 refinement.
> ASSUMPTION: The GDPR Art. 30(5) 250-employee derogation does not apply to TinyTask Lda. because, although the company has 8 employees, the processing of personal data (customer account metadata, task data) is a core, continuous business activity and therefore not "occasional" within the meaning of Art. 30(5); the full RoPA obligation under Art. 30(1)–(3) applies.
> ASSUMPTION: The CRA support-period retention (10 years or the declared support period, whichever is longer) applies to the SaaS product lifecycle as a whole; no separate per-release documentation retention schedule is prescribed by the regulation, and the company's operational support-period declaration governs the concrete duration.
Open question (inherited from fact sheet): the approximate data volume (number of data subjects, volume of task records) is not stated in the intake; this does not alter the goals above but will affect the operational sizing of the records-integrity and traceability controls in Phase 2.

## §6 Handoff Notes to Phase 2

Applicable regulations: GDPR (controller + processor), CRA (manufacturer, default class).
Sub-domain scope (22): D-01.1, D-01.2, D-02.1, D-02.3, D-03.1, D-03.2, D-04.1, D-04.3, D-05.1, D-05.2, D-05.3, D-05.4, D-06.1, D-06.2, D-06.3, D-07.1, D-07.2, D-09.1, D-09.2, D-09.4, D-10.1, D-10.2.
Open questions: data scale (rough figure) not stated in intake; no formal SBOM yet; supplier evaluations ad-hoc.
Phase 2 should refine each sub-domain into measurable objectives with verification criteria, starting from the adjusted goals in §4.
