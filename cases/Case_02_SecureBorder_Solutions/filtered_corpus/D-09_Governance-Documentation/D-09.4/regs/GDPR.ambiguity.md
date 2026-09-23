# D-09.4 — Relevant Ambiguity (GDPR)

> Part 4 ambiguity analysis for GDPR, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## GDPR
##### Art. 5(1)(a) — Lawfulness, fairness, transparency
**Clause: GDPR-CL01** | type: principle | obligatedParty: CONTROLLER | obligationType: CONTINUOUS
**Control anchors:** CSF: GV.OC-03, GV.PO-01, GV.PO-02, PR.AA-02 · PF 1.1: GV.PO-P5, CM.PO-P1, GV.PO-P1, CM.AW-P1, CM.AW-P3 · AI RMF: — · from `SR-GDPR-026`, `SR-GDPR-065` (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
**Berry anchor:** §3.3.5 (vagueness), §5.1 (lists `lawful`, `fair`).
**Instance 1 — VAG / S3 / `lawful`, `fair`, `transparent`**
Three conjunctive vague adjectives. Each is inquiry-resistant:
- `lawful` — refer to Art. 6 (which is itself ambiguous; see Clause-CL06)
- `fair` — undefined; Recital 47 attempts to fix but is non-binding; balance of interests test
- `transparent` — Art. 12 attempts to fix at the implementation level (concise, easily accessible, plain language)
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | `fair` = no deception about purpose or use; balance-of-interests test on data-subject impact. | Recital 47 (non-binding); ICO fairness guidance. |
| R2 | `fair` = no significant detrimental consequence for the data subject unless proportionate and transparent. | CJEU Rīgas satiksme (C-13/16). |
| R3 | `fair` = a procedural requirement (notice, consent mechanism, complaint channel). | EDPB Guidelines 04/2019 on transparency. |
R1 vs R2 yield materially distinct compliance obligations (R1 requires substantive impact assessment; R2 requires procedural safeguards).
---
##### Art. 5(2) — Accountability
**Clause: GDPR-CL07** | type: principle (controller-specific) | obligatedParty: CONTROLLER | obligationType: CONTINUOUS
**Control anchors:** CSF: GV.PO-01, GV.PO-02, GV.RM-04, GV.OV-03, PR.PS-04, DE.AE-03, RS.AN-07 · PF 1.1: GV.PO-P1, GV.PO-P6, GV.MT-P3, GV.PO-P5, CT.DM-P9, ID.IM-P8 · AI RMF: — · from `SR-GDPR-043`, `SR-GDPR-044`, `SR-GDPR-050` (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
**Berry anchor:** §5.1 (`responsible`, `able to demonstrate`).
**Instance 1 — VAG / S3 / `able to demonstrate compliance`**
The accountability principle is the foundational obligation of GDPR. The standard for `demonstrating` is undefined.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Demonstrate = maintain records sufficient for supervisory authority inspection on request (records-of-processing Art. 30, DPIA Art. 35). | Art. 30 + Art. 35 collectively. |
| R2 | Demonstrate = continuous evidentiary trail (logs, audit reports, certifications). | EDPB Guidelines on accountability 07/2019. |
| R3 | Demonstrate = outcome-based — no specific evidentiary form prescribed. | Loose reading. |
R1 vs R2 yield materially distinct compliance obligations (R1 requires documented records; R2 requires live audit trails).
**Instance 2 — POLY / S2 / `compliance with paragraph 1`**
`compliance` is a technical compliance-management term but is undefined. Art. 24(1) partially anchors but uses the same vague `appropriate measures`. S2 because both readings converge on the same controller practice (record + demonstrate).
---
### Article 6 — Lawfulness of processing
#### Verbatim (with highlighting)
> **Article 6**
> **Lawfulness of processing**
>
> 1. Processing shall be lawful only if and to the extent that at least one of the following applies:
> (a) the data subject has given **consent** to the processing of his or her personal data for one or more specific purposes;
> (b) processing is **necessary** for the performance of a contract to which the data subject is party or in order to take steps at the request of the data subject prior to entering into a contract;
> (c) processing is necessary for compliance with a **legal obligation** to which the controller is subject;
> (d) processing is **necessary** in order to protect the **vital interests** of the data subject or of another natural person;
> (e) processing is necessary for the performance of a **task carried out in the public interest** or in the exercise of **official authority** vested in the controller;
> (f) processing is **necessary** for the purposes of the **legitimate interests** pursued by the controller or by a third party, except where such interests are overridden by the interests or fundamental rights and freedoms of the data subject which require protection of personal data, in particular where the data subject is a child.
>
> Point (f) of the first subparagraph shall not apply to processing carried out by public authorities in the performance of their tasks.
>
> 2. Member States may maintain or introduce more specific provisions to adapt the application of the rules of this Regulation with regard to processing for compliance with points (c) and (e) of paragraph 1 by determining more precisely specific requirements for the processing and other measures to ensure lawful and fair processing including for other specific processing situations as provided for in Chapter IX.
> 3. The basis for the processing referred to in point (c) and (e) of paragraph 1 shall be laid down by:
> (a) Union law; or
> (b) Member State law to which the controller is subject.
>
>    The purpose of the processing shall be determined in that legal basis or, as regards the processing referred to in point (e) of paragraph 1, shall be necessary for the performance of a task carried out in the public interest or in the exercise of official authority vested in the controller. That legal basis may contain specific provisions to adapt the application of rules of this Regulation, inter alia: the general conditions governing the lawfulness of processing by the controller; the types of data which are subject to the processing; the data subjects concerned; the entities to, and the purposes for which, the personal data may be disclosed; the purpose limitation; storage periods; and processing operations and processing procedures, including measures to ensure lawful and fair processing such as those for other specific processing situations as provided for in Chapter IX. The Union or the Member State law shall meet an objective of public interest and be proportionate to the legitimate aim pursued.
>
> 4. Where the processing for a purpose other than that for which the personal data have been collected is not based on the data subject's consent or on a Union or Member State law which constitutes a necessary and proportionate measure in a democratic society to safeguard the objectives referred to in Article 23(1), the controller shall, in order to ascertain whether processing for another purpose is compatible with the purpose for which the personal data are initially collected, take into account, inter alia:
> (a) any link between the purposes for which the personal data have been collected and the purposes of the intended further processing;
> (b) the context in which the personal data have been collected, in particular regarding the relationship between data subjects and controller;
> (c) the nature of the personal data, in particular whether special categories of personal data are processed, pursuant to Article 9, or whether personal data related to criminal convictions and offences are processed, pursuant to Article 10;
> (d) the possible consequences of the intended further processing for data subjects;
> (e) the existence of appropriate safeguards, which may include encryption or pseudonymisation.
#### Clause breakdown
##### Art. 12(1) — Transparency modalities
**Clause: GDPR-RT01** | type: data-subject-facing | obligatedParty: CONTROLLER | obligationType: PER-INTERACTION
**Control anchors:** CSF: GV.PO-02, PR.AA-02 · PF 1.1: CM.PO-P1, CM.AW-P1, CM.AW-P3 · AI RMF: — · from `SR-GDPR-065` (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
**Berry anchor:** §5.1 (`appropriate`, `concise`, `transparent`, `intelligible`, `easily accessible`, `clear and plain`).
**Instance 1 — VAG / S3 / six adjectives on information form**
`appropriate measures` AND `concise, transparent, intelligible and easily accessible form` AND `clear and plain language` — six inquiry-resistant modifiers. EDPB Guidelines on transparency 03/2018 attempt to fix but the bar varies by data-subject category (child vs expert; vulnerable vs general).
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Compliance requires layered notices (just-in-time + full privacy policy) meeting WCAG 2.1 AA accessibility. | EDPB Guidelines 03/2018 §4. |
| R2 | Compliance requires reading-level standard (e.g. CEFR B2). | ICO guidance. |
| R3 | Compliance requires both layered notices AND specific linguistic accessibility. | Combination reading. |
R1 vs R2 yield materially distinct UI/UX requirements.
---
##### Art. 12(3) — Response time and extension
**Clause: GDPR-RT02** | type: data-subject-facing | obligatedParty: CONTROLLER | obligationType: PER-REQUEST
**Control anchors:** CSF: RS.MA-02, RS.CO-02 · PF 1.1: CT.DM-P1, CT.DM-P2, CM.AW-P5 · AI RMF: — · from `SR-GDPR-066` (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
**Berry anchor:** §5.1 (`without undue delay`, `where necessary`).
**Instance 1 — VAG / S3 / `without undue delay and in any event within one month` + `two further months where necessary`**
Twin temporal operators (Berry §5.1, §5.7). The 1-month anchor reduces temporal ambiguity; the extension to 3 months via `where necessary` reopens it.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | `where necessary` = demonstrably complex cases (e.g. cross-border processing). | Strict text + EDPB guidance. |
| R2 | `where necessary` = any reason the controller judges sufficient. | Loose reading; controller discretion. |
R1 vs R2 yield materially distinct SLA targets (R1 allows ~6 weeks p95; R2 allows up to 3 months routinely).
**Instance 2 — COORD / S2 / `one month of receipt ... together with the reasons for the delay`**
The controller must inform within one month AND include reasons. Berry §5.4.7: AND coordination. S2 because both requirements converge on the same notification practice.
---
##### Art. 12(5) — Manifestly unfounded or excessive requests
**Clause: GDPR-RT03** | type: data-subject-facing (anti-abuse) | obligatedParty: CONTROLLER | obligationType: PER-REQUEST
**Control anchors:** CSF: GV.PO-02 · PF 1.1: GV.PO-P1, CM.PO-P1 · AI RMF: — · from `SR-GDPR-067` (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
**Berry anchor:** §5.1 (`manifestly unfounded or excessive`, `reasonable fee`).
**Instance 1 — VAG / S3 / `manifestly unfounded or excessive`**
The standard is undefined; the `in particular because of their repetitive character` example is illustrative. EDPB Guidelines 5/2019 attempt to fix but `manifestly unfounded` has high disagreement threshold.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | `manifestly unfounded` = clearly frivolous on its face (no investigation needed). | EDPB Guidelines 5/2019 §4. |
| R2 | `manifestly unfounded` = requires substantive review of the request merits. | Recital 59 (non-binding). |
R1 vs R2 yield materially distinct request-handling workflows (R1 allows automated rejection; R2 requires human review).
---
##### Art. 12(6) — Identity verification for requests
**Clause: GDPR-RT04** | type: data-subject-facing | obligatedParty: CONTROLLER | obligationType: PER-REQUEST
**Control anchors:** CSF: PR.AA-03, PR.AA-02, ID.AM-08, GV.PO-02 · PF 1.1: PR.AC-P6, PR.AC-P3, CT.DP-P4, GV.PO-P1, CM.PO-P1 · AI RMF: — · from `SR-GDPR-009`, `SR-GDPR-010`, `SR-GDPR-067` (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
**Berry anchor:** §5.1 (`reasonable doubts`, `additional information`).
**Instance 1 — VAG / S3 / `reasonable doubts`, `additional information`**
`reasonable doubts` is the recurring vague phrase; `additional information` is undefined. Art. 12(6) permits asking for more info but does not bound the scope. Combined with the controller's data-minimisation duty (Art. 5(1)(c)), the controller should ask minimally.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Controller may request minimal identity verification (e.g. authenticated login). | EDPB Guidelines 5/2019 §6. |
| R2 | Controller may request identity document copy. | Industry practice. |
| R3 | Controller must accept self-declaration if any doubt exists. | Strict pro-data-subject reading. |
R1 vs R3 yield materially distinct identity-verification systems.
---
### Article 13 — Information when collected from data subject
#### Verbatim (with highlighting)
> **Article 13**
> **Information to be provided where personal data are collected from the data subject**
>
> 1. Where personal data relating to a data subject are collected from the data subject, the controller shall, at the time when personal data are obtained, provide the data subject with <u>all of the following information</u>:
> (a) the identity and the contact details of the controller and, where applicable, of the controller's representative;
> (b) the contact details of the data protection officer, where applicable;
> (c) the purposes of the processing for which the personal data are intended as well as the legal basis for the processing;
> (d) where the processing is based on point (f) of Article 6(1), the legitimate interests pursued by the controller or by a third party;
> (e) the recipients or categories of recipients of the personal data, if any;
> (f) where applicable, the fact that the controller intends to transfer personal data to a third country or international organisation and the existence or absence of an adequacy decision by the Commission, or in the case of transfers referred to in Article 46 or 47, or the second subparagraph of Article 49(1), reference to the appropriate or suitable safeguards and the means by which to obtain a copy of them or where they have been made available.
> 2. In addition to the information referred to in paragraph 1, the controller shall, at the time when personal data are obtained, provide the data subject with the following further information necessary to ensure fair and transparent processing:
> (a) the period for which the personal data will be stored, or if that is not possible, the criteria used to determine that period;
> (b) the existence of the right to request from the controller access to and rectification or erasure of personal data or restriction of processing concerning the data subject or to object to processing as well as the right to data portability;
> (c) where the processing is based on point (a) of Article 6(1) or point (a) of Article 9(2), the existence of the right to withdraw consent at any time, without affecting the lawfulness of processing based on consent before its withdrawal;
> (d) the right to lodge a complaint with a supervisory authority;
> (e) whether the provision of personal data is a statutory or contractual requirement, or a requirement necessary to enter into a contract, as well as whether the data subject is obliged to provide the personal data and of the possible consequences of failure to provide such data;
> (f) the existence of automated decision-making, including profiling, referred to in Article 22(1) and (4) and, at least in those cases, meaningful information about the logic involved, as well as the significance and the envisaged consequences of such processing for the data subject.
> 3. Where the controller intends to further process the personal data for a purpose other than that for which the personal data were collected, the controller shall provide the data subject prior to that further processing with information on that other purpose and with any relevant further information as referred to in paragraph 2.
> 4. Paragraphs 1, 2 and 3 shall not apply where and insofar as the data subject already has the information.
#### Clause breakdown
##### Art. 13(1) — Initial information on collection
**Clause: GDPR-RT05** | type: information duty (collection-time) | obligatedParty: CONTROLLER | obligationType: PER-COLLECTION
**Control anchors:** CSF: ID.AM-03, ID.AM-08 · PF 1.1: ID.IM-P4, ID.IM-P5, ID.IM-P6, CM.AW-P1 · AI RMF: — · from `SR-GDPR-068` (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
**Berry anchor:** §5.4.7 (6-element closed AND-list (a)–(f)).
**Instance 1 — COORD / S2 / `(a) AND (b) AND (c) AND (d) AND (e) AND (f)`**
The 6-element list is closed (and). Each must be present. S2 because all 6 requirements converge on the same privacy-notice template.
---
##### Art. 14(1)–(2) — Third-party-source information
**Clause: GDPR-RT07** | type: information duty (third-party-source) | obligatedParty: CONTROLLER | obligationType: PER-COLLECTION
**Control anchors:** CSF: ID.AM-03, ID.AM-08 · PF 1.1: ID.IM-P4, ID.IM-P5, ID.IM-P6, CM.AW-P1 · AI RMF: — · from `SR-GDPR-068` (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
**Berry anchor:** §5.1 (`reasonable period`, `within one month`).
**Instance 1 — VAG / S3 / `within a reasonable period after obtaining the personal data, but at the latest within one month`**
Twin temporal operators (Berry §5.7) where `reasonable period` is soft and `within one month` is hard — interaction undefined.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Notify at first communication or first disclosure, whichever comes first; 1-month hard cap. | Strict text. |
| R2 | Notify within a reasonable period post-collection; 1-month is the upper bound, not the rule. | EDPB reading. |
R1 vs R2 yield materially distinct notification timing rules.
**Instance 2 — VAG / S3 / `from which source the personal data originate`**
`the source` is undefined. Controllers may source from public registries, third-party brokers, web scraping, purchase of data sets — each requires different disclosure detail.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Source = the immediate upstream provider. | Strict text. |
| R2 | Source = the entire chain of acquisition. | Strict pro-data-subject reading. |
| R3 | Source = the type/category (e.g. commercial data broker). | EDPB reading. |
R1 vs R2 yield materially distinct due-diligence documentation requirements.
---
##### Art. 21(1) — Objection grounds and overriding
**Clause: GDPR-RT16** | type: data subject right (object) | obligatedParty: CONTROLLER | obligationType: PER-OBJECTION
**Control anchors:** CSF: — · PF 1.1: — · AI RMF: — (no consuming SR in dashboard mappings)
**Berry anchor:** §5.1 (`compelling legitimate grounds`).
**Instance 1 — VAG / S3 / `compelling legitimate grounds`**
`compelling` is stronger than Art. 6(1)(f) `legitimate interests`. The `overriding` test for compelling grounds is undefined.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | `Compelling` = strictly necessary (lex specialis to legitimate interests). | EDPB Guidelines on legitimate interests. |
| R2 | `Compelling` = materially more weighty than legitimate interests. | Loose reading. |
R1 vs R2 yield materially distinct balance-tests in objection handling.
---
##### Art. 21(3) — Absolute bar on direct-marketing after objection
**Clause: GDPR-RT17** | type: data subject right (absolute) | obligatedParty: CONTROLLER | obligationType: PER-OBJECTION
**Control anchors:** CSF: — · PF 1.1: — · AI RMF: — (no consuming SR in dashboard mappings)
**Berry anchor:** none — Art. 21(3) is a clear absolute obligation.
**Instance 1 — none** — the clause is unambiguous: once the data subject objects to direct-marketing processing, the processing must cease. No variant readings.
---
### Article 22 — Automated individual decision-making
#### Verbatim (with highlighting)
> **Article 22**
> **Automated individual decision-making, including profiling**
>
> 1. The data subject shall have the right not to be subject to a decision based solely on automated processing, including profiling, which produces legal effects concerning him or her or similarly significantly affects him or her.
> 2. Paragraph 1 shall not apply if the decision:
> (a) is necessary for entering into, or performance of, a contract between the data subject and a data controller;
> (b) is authorised by Union or Member State law to which the controller is subject and which also lays down suitable measures to safeguard the data subject's rights and freedoms and legitimate interests; or
> (c) is based on the data subject's explicit consent.
> 3. In the cases referred to in points (a) and (c) of paragraph 2, the data controller shall implement **suitable measures** to safeguard the data subject's rights and freedoms and legitimate interests, at least the right to obtain **human intervention** on the part of the controller, to express his or her point of view and to contest the decision.
> 4. Decisions referred to in paragraph 2 shall not be based on special categories of personal data referred to in Article 9(1), unless point (a) or (g) of Article 9(2) applies and suitable measures to safeguard the data subject's rights and freedoms and legitimate interests are in place.
#### Clause breakdown
##### Art. 23(1) — Permissible restriction grounds
**Clause: GDPR-RT20** | type: principle (restrictions scope) | obligatedParty: MEMBER STATE | obligationType: PER-RESTRICTION
**Control anchors:** CSF: — · PF 1.1: — · AI RMF: — (no consuming SR in dashboard mappings)
**Berry anchor:** §5.1 (`essence of the fundamental rights and freedoms`, `necessary and proportionate`), §5.4.7 (10-element OR-list).
**Instance 1 — VAG / S3 / `essence of the fundamental rights and freedoms`**
`Essence` is Charter Art. 52(1) terminology. CJEU case law (Schrems I/II, Digital Rights Ireland) uses `essence` as a hard-test threshold but does not specify the operational test. S3 because Member State restrictions on Charter rights depend on the essence-test being met.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | `Essence` = the absolute core of the right (cannot be touched). | CJEU Charter interpretation. |
| R2 | `Essence` = the proportionality balance of the right. | Loose reading. |
R1 vs R2 yield materially distinct restriction-scrutiny standards.
**Instance 2 — COORD / S2 / `(a) OR (b) OR (c) OR ... (j)`**
10 disjunctive grounds (Berry §5.4.7 menu-card pattern). S2 because all 10 grounds converge on the same scrutiny mechanism.
---
### Chapter III synthesis
#### Counts
| Category | Instances | Clauses affected |
|---|---|---|
| VAG | 27 | 20 / 20 |
| POLY | 11 | 11 / 20 |
| COORD | 12 | 12 / 20 |
| SCOPE-Q | 3 | 3 / 20 |
| **Total** | **53** | **20 / 20** |
| Severity | Instances |
|---|---|
| S1 — Low | 0 |
| S2 — Medium | 34 |
| S3 — High | 19 |
#### Recurring patterns
- `Reasonable` (Berry-flagged) appears in 8 of 20 clauses — dominant vague term of Chapter III.
- 1-month + 2-month temporal pair (Art. 12(3)) is the only hard numeric anchor in the chapter; all other timelines are vague.
#### Cross-clause structural observations
#### Anti-pattern notes for downstream files
- Chapter IV inherits Chapter III rights via Art. 24(1) "implement appropriate technical and organisational measures" + Art. 25 by-design. `Appropriate measures` for rights-exercise includes consent-collection UIs, SAR portals, rectification workflows.
- Chapter V transfer mechanisms do not create new Chapter III rights but the Art. 15(2) right to be informed of transfer safeguards cross-references Chapter V.
##### Art. 30(1)+(2) — Records content
**Clause: GDPR-CP12** | type: documentation | obligatedParty: CONTROLLER + PROCESSOR | obligationType: CONTINUOUS
**Control anchors:** CSF: ID.AM-08, ID.AM-03, GV.PO-02, GV.OV-03, PR.PS-04, DE.AE-03, RS.AN-07 · PF 1.1: CT.PO-P4, CT.DM-P5, GV.MT-P3, GV.PO-P5, ID.IM-P1, ID.IM-P4, ID.IM-P6, ID.IM-P8, CT.DM-P9 · AI RMF: — · from `SR-GDPR-029`, `SR-GDPR-044`, `SR-GDPR-048`, +1 more (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
**Berry anchor:** §5.1 (`where possible` × 2), §5.4.7 (closed AND-list).
**Instance 1 — VAG / S2 / `where possible` × 2**
Soft hedge on retention-period documentation and security-measure documentation. `Where possible` defers to controller judgement. S2 because the same documentation practice applies.
---
##### Art. 30(5) — 250-employee exception
**Clause: GDPR-CP13** | type: documentation exception | obligatedParty: CONTROLLER + PROCESSOR (<250 persons) | obligationType: CONTINUOUS
**Control anchors:** CSF: ID.AM-03, GV.PO-02 · PF 1.1: ID.IM-P1, ID.IM-P4, ID.IM-P6, ID.IM-P8 · AI RMF: — · from `SR-GDPR-048` (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
**Berry anchor:** §5.1 (`likely`, `occasional`), §3.3.1 (`risk` polysemy).
**Instance 1 — VAG / S3 / `likely to result in a risk`, `occasional`**
Two qualifying exceptions. `Likely` is qualitative; `occasional` inherits Art. 27(2)(a) ambiguity. The exception requires the 3 conditions to ALL fail (risk OR not-occasional OR special categories).
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | `Likely` = more probable than not. | Recital 91 (non-binding). |
| R2 | `Likely` = non-negligible probability. | Loose reading. |
R1 vs R2 yield materially distinct risk-thresholds for small-organisation documentation.
---
### Article 31 — Cooperation with supervisory authority
#### Verbatim
> **Article 31**
> **Cooperation with the supervisory authority**
>
> The controller and the processor and, where applicable, their representatives, shall cooperate, on request, with the supervisory authority in the performance of its tasks.
#### Clause breakdown
##### Art. 31 — Cooperation duty
**Clause: GDPR-CP14** | type: supervisory cooperation | obligatedParty: CONTROLLER + PROCESSOR | obligationType: PER-REQUEST
**Control anchors:** CSF: PR.PS-04, DE.AE-03, RS.AN-07 · PF 1.1: CT.DM-P9, ID.IM-P8 · AI RMF: — · from `SR-GDPR-050` (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
**Berry anchor:** none — clause is unambiguous. Cooperation on request.
---
### Article 32 — Security of processing
#### Verbatim (with highlighting)
> **Article 32**
> **Security of processing**
>
> 1. Taking into account the **state of the art**, the costs of implementation and the nature, scope, context and purposes of processing as well as the risk of varying likelihood and severity for the rights and freedoms of natural persons, the controller and the processor shall implement **appropriate technical and organisational measures** to ensure a level of security appropriate to the risk, including inter alia as appropriate:
> (a) the **pseudonymisation and encryption** of personal data;
> (b) the ability to ensure the **ongoing confidentiality, integrity, availability and resilience** of processing systems and services;
> (c) the ability to **restore** the availability and access to personal data **in a timely manner** in the event of a physical or technical incident;
> (d) a process for **regularly testing, assessing and evaluating** the effectiveness of technical and organisational measures for ensuring the security of the processing.
> 2. In assessing the appropriate level of security account shall be taken in particular of the risks that are presented by processing, **in particular from accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to** personal data transmitted, stored or otherwise processed.
> 3. Adherence to an approved code of conduct as referred to in Article 40 or an approved certification mechanism as referred to in Article 42 may be used as an element by which to demonstrate compliance with the requirements set out in paragraph 1 of this Article.
> 4. The controller and processor shall take steps to ensure that any natural person acting under the authority of the controller or the processor who has access to personal data does not process them except on instructions from the controller, unless he or she is required to do so by Union or Member State law.
#### Clause breakdown
##### Art. 33(1) — 72-hour notification
**Clause: GDPR-CP17** | type: breach notification | obligatedParty: CONTROLLER | obligationType: TRIGGERED (per breach)
**Control anchors:** CSF: DE.CM-01, DE.CM-09, RS.MA-02, RS.CO-02, RS.MA-04, RS.MA-03, RS.AN-03, RS.AN-07, DE.CM-03, DE.AE-02 · PF 1.1: GV.MT-P5, GV.MT-P3, CM.AW-P7, CM.PO-P2, ID.DE-P3, CM.PO-P1, ID.RA-P3 · AI RMF: — · from `SR-GDPR-014`, `SR-GDPR-016`, `SR-GDPR-017`, +2 more (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
**Berry anchor:** §5.1 (`without undue delay`, `where feasible`, `unlikely`), §5.7 (temporal operators), §3.3.1 (`becoming aware` polysemy).
**Instance 1 — VAG / S3 / `without undue delay and, where feasible, not later than 72 hours`**
Twin temporal operators (Berry §5.1, §5.7) — `without undue delay` is soft, `72 hours` is hard, `where feasible` softens the hard. Interaction undefined.
**Instance 2 — SCOPE-Q / S3 / `becoming aware of it`**
**Instance 3 — POLY+VAG / S3 / `unlikely to result in a risk`**
`Unlikely` is qualitative; `risk` is the recurring polysemy (multiple threshold definitions across GDPR).
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Notification required unless certainty-of-no-risk; precautionary principle. | EDPB Guidelines 9/2022 on breach notification. |
| R2 | Notification required only when risk threshold is met; controller assessment suffices. | Industry reading. |
R1 vs R2 yield materially distinct breach-response workflows.
---

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/GDPR.ambiguity.md

- ADM (Art. 22) overlaps with AI Act Art. 13 — Chapter III Art. 22(3) `meaningful information about the logic` is the foundational obligation that the AI Act operationalises for high-risk AI.


### from regs/GDPR.ambiguity.md

1. **Art. 12 is the procedural backbone.** All other rights (Art. 13–22) depend on Art. 12's response-time, identity-verification, and refusal grounds.
2. **Art. 13/14 split** — collection-source vs third-party-source information duties are structurally parallel but with different timing rules (immediate vs 1-month). The third-party-source timing is the more lenient and more often waived.
3. **Art. 15–22 cascade.** Each right (access, rectification, erasure, restriction, portability, object, ADM) inherits Art. 12's procedural rules and Art. 5(1)(d) accuracy / Art. 5(1)(c) minimisation anchors. Cross-clause implementations can reuse components.
4. **Art. 22 ADM** — the most software-impact-relevant right in GDPR, with direct overlap to AI Act's high-risk transparency requirements. Cross-regulatory coordination required.
5. **Art. 23 restrictions** — the Member State's escape valve from Chapter III. The `essence` test (Charter Art. 52(1)) is the constitutional backstop but its operationalisation is CJEU-driven.

### from regs/GDPR.ambiguity.md

The awareness trigger is polysemous (cf. CRA C25, NIS 2 C25 — same pattern across regulations).

<!-- aegis:purity: own_reg=GDPR; demoted=3; core_cross_mentions=0 -->
<!-- aegis:control-anchors: generated by scripts/uniformize_control_anchors.py from baseline/MAPPINGS/sr_control_mappings; not part of the verbatim Part 4 body -->
