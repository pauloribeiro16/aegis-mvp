# D-07.1 — Relevant Ambiguity (GDPR)

> Part 4 ambiguity analysis for GDPR, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## GDPR
##### Art. 5(1)(f) — Integrity and confidentiality
**Clause: GDPR-CL06** | type: principle | obligatedParty: CONTROLLER | obligationType: CONTINUOUS
**Control anchors:** CSF: PR.DS-01, PR.DS-10, ID.AM-08, ID.RA-01, PR.PS-02, PR.IR-04, PR.DS-11, RC.RP-04, PR.PS-06 · PF 1.1: PR.DS-P1, PR.PO-P3, CT.DM-P1, CT.DM-P3, GV.MT-P3, CT.DM-P10, GV.PO-P2, CT.PO-P4 · AI RMF: — · from `SR-GDPR-001`, `SR-GDPR-005`, `SR-GDPR-007`, +2 more (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
**Berry anchor:** §5.1 (`appropriate`), §5.4.7 (`or` coordination).
**Instance 1 — VAG / S3 / `appropriate security`, `appropriate technical or organisational measures`**
`appropriate` is the recurring Berry-flagged term. `appropriate technical or organisational measures` uses OR whose inclusivity is unspecified. Art. 32 (security of processing) anchors `appropriate` to a risk-based test but does not resolve the OR.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | `or` is inclusive: at least one of technical OR organisational measures required. | Strict grammatical reading. |
| R2 | `or` is inclusive: both required in combination (despite `or`). | Industry reading; ISO 27001 control set interpretation. |
| R3 | `or` is exclusive: the controller chooses which category. | Loose reading. |
R1 vs R2 yield materially distinct compliance obligations (R1 permits policy-only compliance for low-tech processing; R2 requires both).
**Instance 2 — COORD / S3 / `unauthorised or unlawful processing`, `accidental loss, destruction or damage`**
Two OR coordinations enumerating breach types. The 5-fold enumeration (unauthorised / unlawful / loss / destruction / damage) is similar to Art. 4(12) `personal data breach` but not identical (Art. 4(12) adds `alteration`, `disclosure of`, `access to`).
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Any of the 5 events triggers `appropriate security` obligations. | Strict text. |
| R2 | The 5 events are illustrative; the controller judges which events trigger obligations. | Loose reading. |
R1 vs R2 yield materially distinct compliance obligations on breach response.
---
##### Art. 13(2)(f) — Automated decision-making information
**Clause: GDPR-RT06** | type: information duty (ADM-specific) | obligatedParty: CONTROLLER | obligationType: PER-COLLECTION
**Control anchors:** CSF: — · PF 1.1: — · AI RMF: — (no consuming SR in dashboard mappings)
**Berry anchor:** §5.1 (`meaningful information`).
**Instance 1 — VAG / S3 / `meaningful information about the logic involved, as well as the significance and the envisaged consequences`**
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | `meaningful` = accurate, intelligible, sufficient for the data subject to challenge. | EDPB Guidelines on ADM 2018. |
| R2 | `meaningful` = a description of categories of decisions and main criteria. | Industry reading; partial disclosure. |
| R3 | `meaningful` = the full logic including weights and thresholds. | Strict pro-data-subject reading. |
R1 vs R3 yield materially distinct explainability engineering scope.
---
### Article 14 — Information when not collected from data subject
#### Verbatim (with highlighting)
> **Article 14**
> **Information to be provided where personal data have not been obtained from the data subject**
>
> 1. Where personal data have not been obtained from the data subject, the controller shall provide the data subject with the following information:
> (a) the identity and the contact details of the controller and, where applicable, of the controller's representative;
> (b) the contact details of the data protection officer, where applicable;
> (c) the purposes of the processing for which the personal data are intended as well as the legal basis for the processing;
> (d) the categories of personal data concerned;
> (e) the recipients or categories of recipients of the personal data, if any;
> (f) where applicable, that the controller intends to transfer personal data to a recipient in a third country or international organisation and the existence or absence of an adequacy decision by the Commission (...)
> 2. In addition to the information referred to in paragraph 1, the controller shall provide the data subject with the following further information necessary to ensure fair and transparent processing in respect of the data subject:
> (a) the period for which the personal data will be stored, or if that is not possible, the criteria used to determine that period;
> (b) where the processing is based on point (f) of Article 6(1), the legitimate interests pursued by the controller or by a third party;
> (c) the existence of the right to request from the controller access to and rectification or erasure of personal data or restriction of processing concerning the data subject and to object to processing as well as the right to data portability;
> (d) where processing is based on point (a) of Article 6(1) or point (a) of Article 9(2), the existence of the right to withdraw consent at any time (...);
> (e) the right to lodge a complaint with a supervisory authority;
> (f) from which source the personal data originate, and if applicable, whether it came from publicly accessible sources;
> (g) the existence of automated decision-making, including profiling, referred to in Article 22(1) and (4) and, at least in those cases, meaningful information about the logic involved, as well as the significance and the envisaged consequences of such processing for the data subject.
> 3. The controller shall provide the information referred to in paragraphs 1 and 2:
> (a) within a reasonable period after obtaining the personal data, but at the latest within one month, having regard to the specific circumstances in which the personal data are processed;
> (b) if the personal data are to be used for communication with the data subject, at the latest at the time of the first communication to that data subject; or
> (c) if a disclosure to another recipient is envisaged, at the latest when the personal data are first disclosed.
> 4. Where the controller intends to further process the personal data for a purpose other than that for which the personal data were obtained, the controller shall provide the data subject prior to that further processing with information on that other purpose (...)
> 5. Paragraphs 1 to 4 shall not apply where and insofar as:
> (a) the data subject already has the information;
> (b) the provision of such information proves impossible or would involve a disproportionate effort, in particular for processing for archiving purposes in the public interest, scientific or historical research purposes or statistical purposes, subject to the conditions and safeguards referred to in Article 89(1) (...);
> (c) obtaining or disclosure is expressly laid down by Union or Member State law (...); or
> (d) where the personal data must remain confidential subject to an obligation of professional secrecy (...).
#### Clause breakdown
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
##### Art. 25(1) — Privacy by design
**Clause: GDPR-CP02** | type: design obligation | obligatedParty: CONTROLLER | obligationType: CONTINUOUS
**Control anchors:** CSF: PR.PS-01, ID.AM-08, PR.PS-06, PR.DS-01 · PF 1.1: CT.DP-P4, CT.PO-P4, GV.PO-P2, CT.DP-P2 · AI RMF: — · from `SR-GDPR-013`, `SR-GDPR-039`, `SR-GDPR-040`, +1 more (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
**Berry anchor:** §5.1 (`state of the art`, `appropriate`, `effective`, `necessary`).
**Instance 1 — VAG / S3 / `state of the art`**
`state of the art` is the canonical Berry-flagged vague term (Berry §5.1). Time-dependent (2024 vs 2026 vs 2028), jurisdiction-dependent, sector-dependent. No objective anchor in the OJ text.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | `State of the art` = ISO 27001 + sector-specific best practices at design time. | Industry reading. |
| R2 | `State of the art` = ENISA / EDPB-published state-of-the-art guidance. | Strict reading. |
| R3 | `State of the art` = any reasonable technical measure documented at design time. | Loose reading. |
R1 vs R3 yield materially distinct by-design engineering scope.
**Instance 2 — POLY / S2 / `effective manner`**
`effective` is inquiry-resistant but inherits Art. 32(1)(d) testing obligation. S2 because the compliance practice (test + document) is the same.
---
##### Art. 25(2) — Privacy by default
**Clause: GDPR-CP03** | type: default-setting obligation | obligatedParty: CONTROLLER | obligationType: CONTINUOUS
**Control anchors:** CSF: PR.PS-01, ID.AM-08, PR.PS-06 · PF 1.1: CT.DP-P4, CT.PO-P4, GV.PO-P2 · AI RMF: — · from `SR-GDPR-013`, `SR-GDPR-039`, `SR-GDPR-041` (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
**Berry anchor:** §5.1 (`appropriate`, `necessary`), §5.4.7 (`amount AND extent AND period AND accessibility`).
**Instance 1 — VAG+COORD / S3 / `necessary for each specific purpose` + 4 coordinated dimensions**
`Necessary` propagates; `each specific purpose` requires per-purpose default-setting; the 4 dimensions (amount/extent/period/accessibility) are AND-coordinated.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | All 4 dimensions must individually be minimised. | EDPB Guidelines 04/2019. |
| R2 | Some dimensions can be relaxed if others are tightened. | Loose reading. |
R1 vs R2 yield materially distinct default-setting engineering.
---
### Article 26 — Joint controllers
#### Verbatim (with highlighting)
> **Article 26**
> **Joint controllers**
>
> 1. Where two or more controllers **jointly determine** the purposes and means of processing, they shall be **joint controllers**. They shall in a **transparent** manner determine their respective responsibilities for compliance with the obligations under this Regulation, in particular as regards the exercising of the rights of the data subject and their respective duties to provide the information referred to in Articles 13 and 14, by means of an **arrangement** between them unless, and in so far as, the respective responsibilities of the controllers are determined by Union or Member State law to which the controllers are subject. The arrangement may designate a contact point for data subjects.
> 2. The arrangement referred to in paragraph 1 shall **duly reflect** the respective roles and relationships of the joint controllers vis-à-vis the data subjects. **The essence of the arrangement** shall be made available to the data subject.
> 3. Irrespective of the terms of the arrangement referred to in paragraph 1, the data subject may exercise his or her rights under this Regulation in respect of and against each of the controllers.
#### Clause breakdown
##### Art. 32(1) — Security measures (open list)
**Clause: GDPR-CP15** | type: security | obligatedParty: CONTROLLER + PROCESSOR | obligationType: CONTINUOUS
**Control anchors:** CSF: PR.DS-01, PR.DS-10, PR.DS-02, PR.IR-01, PR.IR-03, ID.RA-01, PR.PS-02, ID.RA-05, ID.IM-02, PR.AA-05, PR.AA-06, PR.AT-02, DE.CM-01, DE.CM-09, RS.MA-02, RS.MI-01, RS.MI-02, PR.IR-04, PR.DS-11, RC.RP-04, GV.SC-03, GV.SC-04, DE.CM-06, PR.PS-06, ID.AM-08 · PF 1.1: PR.DS-P1, PR.PO-P3, PR.DS-P2, PR.AC-P5, CT.DP-P2, GV.MT-P3, CT.DM-P10, ID.RA-P3, ID.RA-P5, PR.AC-P1, PR.AC-P2, CT.PO-P1, GV.AT-P2, GV.MT-P5, CM.AW-P7, PR.PO-P7, ID.DE-P5, CT.DM-P9, GV.PO-P2, CT.PO-P4 · AI RMF: — · from `SR-GDPR-001`, `SR-GDPR-002`, `SR-GDPR-003`, +11 more (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
**Berry anchor:** §5.1 (`state of the art`, `appropriate`, `as appropriate`), §5.4.7 (4-element list), §3.3.1 (CIA+R polysemy).
**Instance 1 — VAG / S3 / `state of the art`**
Cross-clause propagation — same as Art. 25(1). S3 because security-engineering scope is material to compliance.
**Instance 2 — COORD / S3 / `(a) AND (b) AND (c) AND (d)`**
The 4-element list `(a) pseudonymisation/encryption, (b) CIA+R, (c) restore-in-timely-manner, (d) regular-testing` is closed (and). All 4 required.
**Instance 3 — POLY+VAG / S3 / `in a timely manner` (Art. 32(1)(c))**
`Timely manner` is the textbook Berry-flagged temporal vague phrase. Recital 49 (non-binding) attempts to fix: "restore the availability and access as soon as possible". The cross-reference is non-binding and the operational meaning drifts.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | `Timely` = RTO defined per processing activity (objective measure). | Industry standard (BCP/DRP best practice). |
| R2 | `Timely` = as-soon-as-practicable for the specific incident. | EDPB Guidelines 7/2019 (generic). |
R1 vs R2 yield materially distinct BCP/DRP engineering scope.
---
##### Art. 34(3) — Exceptions to data-subject communication
**Clause: GDPR-CP20** | type: breach communication exception | obligatedParty: CONTROLLER | obligationType: PER-BREACH
**Control anchors:** CSF: PR.DS-01, PR.IR-03, RS.MI-01, RS.MI-02, RS.CO-03, PR.PS-06 · PF 1.1: PR.DS-P1, CT.DP-P2, PR.PO-P7, CT.DM-P10, CM.AW-P7, CM.PO-P1 · AI RMF: — · from `SR-GDPR-004`, `SR-GDPR-015`, `SR-GDPR-020`, +2 more (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
**Berry anchor:** §5.1 (`appropriate`, `unintelligible`, `disproportionate effort`), §5.4.7 (`OR (a) OR (b) OR (c)`).
**Instance 1 — VAG / S3 / `render the personal data unintelligible`**
`Unintelligible` (typically achieved via encryption) inherits the encryption-key-management question. If keys are lost, data is unintelligible in one sense but inaccessible to legitimate users too.
**Instance 2 — VAG / S3 / `disproportionate effort`**
Same Berry-flagged phrase as Art. 14(5)(b). S3 because the exception triggers instead-of notification duty, materially distinct compliance outcome.
---
### Article 35 — Data protection impact assessment
#### Verbatim (with highlighting)
> **Article 35**
> **Data protection impact assessment**
>
> 1. Where a type of processing in particular using **new technologies**, and taking into account the nature, scope, context and purposes of the processing, is likely to result in a **high risk** to the rights and freedoms of natural persons, the controller shall, prior to the processing, carry out an assessment of the impact of the envisaged processing operations on the protection of personal data. A single assessment may address a set of similar processing operations that present similar high risks.
> 2. The controller shall seek the advice of the data protection officer, where designated, when carrying out a data protection impact assessment.
> 3. A data protection impact assessment referred to in paragraph 1 shall in particular be required in the case of:
> (a) a systematic and extensive evaluation of personal aspects relating to natural persons which is based on automated processing, including profiling, and on which decisions are based that produce legal effects concerning the natural person or similarly significantly affect the natural person;
> (b) processing on a large scale of special categories of data referred to in Article 9(1), or of personal data relating to criminal convictions and offences referred to in Article 10; or
> (c) a systematic monitoring of a publicly accessible area on a large scale.
> 4. The supervisory authority shall establish and make public a list of the kind of processing operations which are subject to the requirement for a data protection impact assessment pursuant to paragraph 1. The supervisory authority shall communicate those lists to the Board referred to in Article 68.
> 5. The supervisory authority may also establish and make public a list of the kind of processing operations for which no data protection impact assessment is required.
> 6. Prior to the adoption of the lists referred to in paragraphs 4 and 5, the competent supervisory authority shall apply the consistency mechanism referred to in Article 63 where such lists involve processing activities which are related to the offering of goods or services to data subjects or to the monitoring of their behaviour in several Member States, or may substantially affect the free movement of personal data within the Union.
> 7. The assessment shall contain at least:
> (a) a **systematic description** of the envisaged processing operations and the purposes of the processing, including, where applicable, the legitimate interest pursued by the controller;
> (b) an assessment of the **necessity and proportionality** of the processing operations in relation to the purposes;
> (c) an assessment of the risks to the rights and freedoms of data subjects referred to in paragraph 1;
> (d) the measures envisaged to address the risks, including safeguards, security measures and mechanisms to ensure the protection of personal data and to demonstrate compliance with this Regulation taking into account the rights and legitimate interests of data subjects and other persons concerned.
> 8. Compliance with approved codes of conduct referred to in Article 40 by the relevant controllers or processors shall be taken into due account in assessing the impact of the processing operations performed by such controllers or processors, in particular for the purposes of a data protection impact assessment.
> 9. Where appropriate, the controller shall seek the views of data subjects or their representatives on the intended processing, without prejudice to the protection of commercial or public interests or the security of processing operations.
> 10. Where processing pursuant to point (c) or (e) of Article 6(1) has a legal basis in Union law or in the law of the Member State to which the controller is subject, that law regulates the specific processing operation or set of operations in question, and a data protection impact assessment has already been carried out as part of a general impact assessment in the context of the adoption of that legal basis, paragraphs 1 to 7 shall not apply unless Member States deem it to be necessary to carry out such an assessment prior to processing activities.
> 11. Where necessary, the controller shall carry out a review to assess if processing is performed in accordance with the data protection impact assessment at least when there is a change of the risk represented by processing operations.
#### Clause breakdown

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/GDPR.ambiguity.md

`meaningful information` + `the logic involved` are partially self-contradictory: full logic disclosure would expose trade secrets; meaningful-but-not-full disclosure has no threshold. This is the central automated-decision-making transparency question (cf. AI Act Art. 13, Art. 14 cross-over).

<!-- aegis:purity: own_reg=GDPR; demoted=1; core_cross_mentions=0 -->
<!-- aegis:control-anchors: generated by scripts/uniformize_control_anchors.py from baseline/MAPPINGS/sr_control_mappings; not part of the verbatim Part 4 body -->
