# D-09.2 — Relevant Ambiguity (GDPR)

> Part 4 ambiguity analysis for GDPR, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## GDPR
##### Art. 9(2)(g) — Substantial public interest
**Clause: GDPR-CL23** | type: lawfulness base (special category) | obligatedParty: CONTROLLER | obligationType: PER-MEMBER-STATE-LAW
**Berry anchor:** §5.1 (`substantial public interest`, `proportionate`, `essence of the right to data protection`, `suitable and specific measures`).
**Instance 1 — VAG / S3 / `substantial public interest`**
`substantial public interest` inherits the Art. 6(1)(e) `public interest` ambiguity plus the `substantial` qualifier. The clause cross-references Charter Art. 52(1) via `essence of the right`.
S3 — same family of ambiguity as Art. 6(1)(e), but more severe because `substantial` is undefined.
---
##### Art. 9(2)(j) — Research/statistics/archiving (with Art. 89(1) safeguards)
**Clause: GDPR-CL24** | type: lawfulness base (special category, research) | obligatedParty: CONTROLLER | obligationType: PER-MEMBER-STATE-LAW
**Berry anchor:** §5.1 (`archiving purposes in the public interest`, `proportionate`, `essence`).
The clause cross-references Art. 89(1) for the substantive safeguards (pseudonymisation, no decisions about data subjects, etc.). The Art. 89(1) reference provides partial anchoring but does not define `archiving`.
---
### Article 10 — Criminal convictions and offences
#### Verbatim
> **Article 10**
>
> Processing of personal data relating to criminal convictions and offences shall be carried out only under the control of official authority or when the processing is authorised by Union or Member State law providing for appropriate safeguards for the rights and freedoms of data subjects. Any **comprehensive register** of criminal convictions shall be kept only under the control of official authority.
#### Clause breakdown
##### Art. 13(2)(f) — Automated decision-making information
**Clause: GDPR-RT06** | type: information duty (ADM-specific) | obligatedParty: CONTROLLER | obligationType: PER-COLLECTION
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
##### Art. 22(1) — General prohibition on solely-automated decisions
**Clause: GDPR-RT18** | type: data subject right (ADM protection) | obligatedParty: CONTROLLER | obligationType: PER-DECISION
**Berry anchor:** §3.3.1 (`solely`, `significantly`).
**Instance 1 — POLY / S3 / `solely`, `similarly significantly affects`**
`Solely` excludes hybrid decisions (human review with AI recommendation) but the boundary (when does human review break the `solely` qualifier?) is undefined. `Similarly significantly affects` is undefined — what level of significance crosses the threshold?
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | `Solely` = no human involvement in the decision-making chain. | Strict text. |
| R2 | `Solely` = human involvement is rubber-stamping, not substantive review. | EDPB Guidelines on ADM. |
| R3 | `Solely` = human can override but AI makes the default decision. | Loose reading. |
R1 vs R3 yield materially distinct HITL (human-in-the-loop) engineering requirements.
**Variant readings for `significantly`:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Significant = financial impact, access to services, reputation. | EDPB Guidelines on ADM 2018. |
| R2 | Significant = any non-trivial impact on the data subject's life. | Strict pro-data-subject reading. |
R1 vs R2 yield materially distinct decision-classification systems.
---
##### Art. 26(1) — Joint-controller determination
**Clause: GDPR-CP04** | type: multi-controller | obligatedParty: CONTROLLER (joint) | obligationType: CONTINUOUS
**Berry anchor:** §3.3.1 (`jointly determine` — see Art. 4(7) ambiguity), §5.1 (`transparent`).
**Instance 1 — POLY / S3 / `jointly determine`**
Inherits Art. 4(7) `alone or jointly with others` ambiguity. The CJEU IAB Europe case (C-604/22, 2024) held that joint controllership can exist even when one party lacks direct influence on processing purposes — extending the scope of `jointly determine` beyond the original EDPB reading.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | `Jointly determine` = shared decision-making authority on purposes. | EDPB Guidelines 07/2020 (original). |
| R2 | `Jointly determine` = either party having determinative influence on purposes. | CJEU IAB Europe (C-604/22). |
R1 vs R2 yield materially distinct joint-controller assignment.
---
##### Art. 26(2) — Joint-controller arrangement essentials
**Clause: GDPR-CP05** | type: multi-controller transparency | obligatedParty: CONTROLLER (joint) | obligationType: CONTINUOUS
**Berry anchor:** §5.1 (`duly reflect`, `essence`).
**Instance 1 — VAG / S2 / `duly reflect`**
`duly` is the recurring vague adverb. S2 because the substantive obligation (reflect roles in arrangement) is unambiguous.
---
### Article 27 — Representatives of non-EU controllers/processors
#### Verbatim (with highlighting)
> **Article 27**
> **Representatives of controllers or processors not established in the Union**
>
> 1. Where Article 3(2) applies, the controller or the processor shall designate **in writing** a **representative** in the Union.
> 2. The obligation laid down in paragraph 1 of this Article shall not apply to:
> (a) processing which is **occasional**, does not include, on a large scale, processing of special categories of data as referred to in Article 9(1) or processing of personal data relating to criminal convictions and offences referred to in Article 10, and is unlikely to result in a risk to the rights and freedoms of natural persons, taking into account the nature, context, scope and purposes of the processing; or
> (b) a public authority or body.
#### Clause breakdown
##### Art. 32(1) — Security measures (open list)
**Clause: GDPR-CP15** | type: security | obligatedParty: CONTROLLER + PROCESSOR | obligationType: CONTINUOUS
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
##### Art. 35(1) — DPIA trigger
**Clause: GDPR-CP21** | type: impact assessment | obligatedParty: CONTROLLER | obligationType: PER-PROCESSING (pre-launch)
**Berry anchor:** §5.1 (`new technologies`, `likely`, `high risk`), §3.3.1 (`new` polysemy).
**Instance 1 — POLY+VAG / S3 / `new technologies` + `high risk`**
`New technologies` is the recurring time-dependent vague phrase (cf. Art. 25 `state of the art`). Was cloud `new` in 2018? Is generative AI `new` in 2026? EDPB Guidelines 4/2019 attempt to fix but `new` is inherently time-relative.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | `New technologies` = technologies not widely deployed in the industry at time of assessment. | EDPB Guidelines 4/2019. |
| R2 | `New technologies` = listed in supervisory-authority Art. 35(4) lists. | EDPB reading. |
R1 vs R2 yield materially distinct DPIA-trigger classification.
---
##### Art. 35(7) — DPIA content
**Clause: GDPR-CP22** | type: impact assessment content | obligatedParty: CONTROLLER | obligationType: PER-DPIA
**Berry anchor:** §5.1 (`systematic description`, `necessity and proportionality`).
**Instance 1 — POLY / S2 / `necessity and proportionality`**
Three different `necessity` senses across GDPR (5(1)(c) data-minimisation, 6(1)(b) contract, 35(7)(b) DPIA) — same term, different operationalisation. S2 because Art. 35(7)(b) is internally anchored.
---
### Article 36 — Prior consultation
#### Verbatim (with highlighting)
> **Article 36**
> **Prior consultation**
>
> 1. The controller shall consult the supervisory authority **prior to processing** where a data protection impact assessment under Article 35 indicates that the processing would result in a **high risk** in the absence of measures taken by the controller to mitigate the risk.
> 2. Where the supervisory authority is of the opinion that the intended processing referred to in paragraph 1 would infringe this Regulation, in particular where the controller has insufficiently identified or mitigated the risk, the supervisory authority shall, **within period of up to eight weeks** of receipt of the request for consultation, provide written advice to the controller and, where applicable to the processor (...).
#### Clause breakdown
##### Art. 36(1) — Prior consultation trigger
**Clause: GDPR-CP23** | type: supervisory consultation | obligatedParty: CONTROLLER | obligationType: PER-PROCESSING (pre-launch)
**Berry anchor:** §3.3.1 (`high risk` — Art. 35 inheritance).
**Instance 1 — POLY+VAG / S2 / `high risk in the absence of measures`**
Inherits Art. 35(1) `high risk` threshold. S2 because the trigger is the same DPIA outcome.
---
##### Art. 37(1)(b) — DPO designation (monitoring threshold)
**Clause: GDPR-CP25** | type: DPO designation | obligatedParty: CONTROLLER + PROCESSOR | obligationType: CONTINUOUS
**Berry anchor:** §5.1 (`core activities`, `regular and systematic`, `large scale`).
**Instance 1 — VAG / S3 / `core activities`**
`Core activities` is the Berry-flagged term. EDPB Guidelines 3/2018 attempt to fix as primary business activities (vs ancillary/supporting).
**Instance 2 — VAG+POLY / S3 / `regular and systematic`, `large scale`, `nature, scope and/or purposes`**
Three qualifiers combined with AND (`regular AND systematic AND large scale`) for monitoring-threshold determination. The `and/or` in the secondary clause (nature/scope/purposes) is the Berry §5.1 explicitly-flagged `and/or` problem.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | `Core activities` = main revenue-driving business activities. | EDPB Guidelines 3/2018. |
| R2 | `Core activities` = activities that are essential to achieving the controller's purpose. | Loose reading. |
R1 vs R2 yield materially distinct DPO-designation policies.
---
### Article 38 — Position of the DPO
#### Verbatim (with highlighting)
> **Article 38**
> **Position of the data protection officer**
>
> 1. The controller and the processor shall ensure that the data protection officer is involved, **properly and in a timely manner**, in all issues which relate to the protection of personal data.
> 2. The controller and processor shall support the data protection officer in performing the tasks referred to in Article 39 by providing **resources necessary** to carry out those tasks and access to personal data and processing operations, and to maintain his or her expert knowledge.
> 3. The controller and processor shall ensure that the data protection officer does not receive any instructions regarding the exercise of those tasks. He or she shall not be dismissed or penalised by the controller or the processor for performing his tasks. The data protection officer shall **directly report to the highest management level** of the controller or the processor.
> 4. Data subjects may contact the data protection officer with regard to all issues related to processing of their personal data and to the exercise of their rights under this Regulation.
> 5. The data protection officer shall be bound by **secrecy or confidentiality** concerning the performance of his or her tasks, in accordance with Union or Member State law.
> 6. The data protection officer may fulfil other tasks and duties. The controller or processor shall ensure that any such tasks and duties do not result in a **conflict of interests**.
#### Clause breakdown
##### Art. 39(1)(b) — DPO monitoring and training
**Clause: GDPR-CP28** | type: DPO tasks | obligatedParty: DPO | obligationType: CONTINUOUS
**Berry anchor:** §5.1 (`awareness-raising`, `training`).
**Instance 1 — POLY+VAG / S2 / `awareness-raising and training`**
Inherits the GDPR/T1 `training` polysemy. S2 because the same training-practice applies.
---
### Chapter IV synthesis
#### Counts
| Category | Instances | Clauses affected |
|---|---|---|
| VAG | 32 | 28 / 28 |
| POLY | 16 | 16 / 28 |
| COORD | 19 | 18 / 28 |
| SCOPE-Q | 8 | 8 / 28 |
| **Total** | **75** | **28 / 28** |
| Severity | Instances |
|---|---|
| S1 — Low | 0 |
| S2 — Medium | 50 |
| S3 — High | 25 |
#### Recurring patterns
- `appropriate` appears in 11 of 28 clauses — cross-clause Berry-flagged term.
- `state of the art` appears in 2 clauses (Art. 25(1), Art. 32(1)) — propagates from Art. 5(1)(f) `appropriate security`.
- `high risk` appears in 4 clauses (Art. 34, 35, 36, 33 with different threshold) — three-threshold polysemy.
- `and/or` appears in 1 clause (Art. 37(1)(b)) — Berry §5.1 explicitly flagged.
#### Cross-clause structural observations
1. **Art. 24–28 (responsibility allocation)** — open by design. Each article cross-references Art. 5(1) principles and Art. 6 lawfulness bases. Controller/processor identification (Art. 4(7)/(8)) is the prerequisite.
2. **Art. 30–32 (documentation and security)** — the operational backbone. Art. 30 records + Art. 32 security measures + Art. 33/34 breach notifications form the compliance evidence chain.
3. **Art. 33–34 (breach notification)** — three-tier threshold architecture (`risk` Art. 33, `high risk` Art. 34, `high risk` Art. 35). EDPB Guidelines 9/2022 attempt to fix.
4. **Art. 35–36 (DPIA + consultation)** — pre-launch governance. Mandatory for high-risk processing (Art. 35(3) list).
5. **Art. 37–39 (DPO regime)** — independent oversight mechanism. Three designation triggers (Art. 37(1)(a)/(b)/(c)). EDPB Guidelines 3/2018 set operational threshold.
#### Anti-pattern notes for downstream files
- Chapter V inherits Art. 28 processor obligations (transfer is processing via a processor). Art. 28(3) DPA clauses must include transfer safeguards.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/GDPR.ambiguity.md

`meaningful information` + `the logic involved` are partially self-contradictory: full logic disclosure would expose trade secrets; meaningful-but-not-full disclosure has no threshold. This is the central automated-decision-making transparency question (cf. AI Act Art. 13, Art. 14 cross-over).

<!-- aegis:purity: own_reg=GDPR; demoted=1; core_cross_mentions=0 -->

