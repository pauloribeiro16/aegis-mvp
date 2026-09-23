# D-01.3 — Relevant Ambiguity (GDPR)

> Part 4 ambiguity analysis for GDPR, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## GDPR
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
##### Art. 34(1) — High-risk threshold
**Clause: GDPR-CP19** | type: breach communication | obligatedParty: CONTROLLER | obligationType: TRIGGERED (per high-risk breach)
**Control anchors:** CSF: RS.CO-03, RS.MA-04, PR.DS-01, PR.IR-03 · PF 1.1: CM.AW-P7, CM.AW-P8, PR.DS-P1, CT.DP-P2, CM.PO-P1 · AI RMF: — · from `SR-GDPR-019`, `SR-GDPR-020`, `SR-GDPR-021` (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
**Berry anchor:** §3.3.1 (`high risk` polysemy — vs Art. 33 `risk` vs Art. 35 `high risk`).
**Instance 1 — POLY+VAG / S3 / `likely to result in a high risk`**
Three undefined qualifiers. The cross-clause threshold distinction (`risk` Art. 33 vs `high risk` Arts. 34, 35) is the central notification-litigation question.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | `High risk` = objectively elevated above ordinary processing risk. | EDPB Guidelines 9/2022. |
| R2 | `High risk` = severe impact on data subject's rights. | CNIL guidance. |
R1 vs R2 yield materially distinct breach-classification systems.
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

<!-- aegis:purity: own_reg=GDPR; demoted=0; core_cross_mentions=0 -->
<!-- aegis:control-anchors: generated by scripts/uniformize_control_anchors.py from baseline/MAPPINGS/sr_control_mappings; not part of the verbatim Part 4 body -->
