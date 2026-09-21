# D-10.2 — Relevant Ambiguity (GDPR)

> Part 4 ambiguity analysis for GDPR, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## GDPR
##### Art. 5(1)(c) — Data minimisation
**Clause: GDPR-CL03** | type: principle | obligatedParty: CONTROLLER | obligationType: CONTINUOUS
**Berry anchor:** §3.3.5 (vagueness), §5.1 (`adequate`, `relevant`, `necessary`).
**Instance 1 — VAG / S3 / `adequate`, `relevant`, `necessary`**
Three inquiry-resistant adjectives; no measurement criterion. Art. 5(2) accountability shifts burden of demonstration to controller; Art. 35(7)(b) DPIA requires necessity assessment.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Adequate iff it serves the designed purpose; necessity presumed by default. | None in OJ; industry self-regulation. |
| R2 | Adequate iff proportionate to purpose; demonstrable ex ante. | Art. 5(2) accountability; Art. 35(7)(b) DPIA. |
| R3 | Adequate iff least-intrusive among equivalent means under Art. 52(1) Charter necessity test. | CJEU C-62/14 Gasket; Charter Art. 52(1). |
R1 vs R3 yield materially distinct compliance obligations (R1 permits default collection patterns; R3 requires per-field justification).
**Instance 2 — SCOPE-Q / S2 / `purposes` (plural)**
`purposes` is plural — the minimisation test applies to each purpose. Berry §5.2.1 (plural-scope `purposes`). S2 because Art. 5(2) accountability and Art. 35(7)(b) DPIA partially anchor the reading.
---
##### Art. 5(1)(e) — Storage limitation
**Clause: GDPR-CL05** | type: principle | obligatedParty: CONTROLLER | obligationType: CONTINUOUS
**Berry anchor:** §5.1 (`necessary`, `appropriate`), §3.3.1 (polysemy of `form which permits identification`).
**Instance 1 — VAG / S3 / `no longer than is necessary`**
Temporal vague phrase with no upper bound; same pattern as `without undue delay` (Berry §5.1). Art. 5(1)(e) further conditions on `appropriate technical and organisational measures required by this Regulation` — the cross-reference is itself ambiguous.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Necessity = strict purpose-bound retention; deletion mandatory at purpose-end. | Strict textual reading. |
| R2 | Necessity = risk-based; indefinite retention allowed with adequate safeguards (pseudonymisation, anonymisation). | EDPB Guidelines 05/2020 on storage limitation. |
R1 vs R2 yield materially distinct compliance obligations (R1 requires deletion workflows; R2 requires pseudonymisation pipelines).
**Instance 2 — POLY / S3 / `form which permits identification`**
The `identification` threshold is the same Art. 4(1) `identifiable` question. Pseudonymised data (Art. 4(5)) is in a grey zone: `permits identification` only via additional information. S3 because pseudonymisation workflow design differs across readings.
---
##### Art. 5(2) — Accountability
**Clause: GDPR-CL07** | type: principle (controller-specific) | obligatedParty: CONTROLLER | obligationType: CONTINUOUS
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
##### Art. 24(1) — General controller responsibility
**Clause: GDPR-CP01** | type: controller-specific | obligatedParty: CONTROLLER | obligationType: CONTINUOUS
**Berry anchor:** §5.1 (`appropriate`, `where necessary`), §5.4.7 (`technical and organisational`).
**Instance 1 — VAG / S3 / `appropriate technical and organisational measures`**
Same pattern as Art. 5(1)(f) and Art. 32(1) — `appropriate` is the recurring Berry-flagged vague term. Art. 32 anchors the specific security measures but the cross-clause `appropriate` chain remains qualitatively undefined.
**Instance 2 — VAG / S3 / `where necessary`**
`Where necessary` triggers the review-and-update obligation. The trigger threshold is undefined. EDPB Guidelines on accountability 07/2019 suggest materiality threshold (change in processing, change in risk landscape, periodic) but the OJ text does not bind.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | `Where necessary` = any material change in risk. | EDPB Guidelines 07/2019. |
| R2 | `Where necessary` = periodic review (annual). | Industry reading. |
R1 vs R2 yield materially distinct review-cadence policies.
---
### Article 25 — Data protection by design and by default
#### Verbatim (with highlighting)
> **Article 25**
> **Data protection by design and by default**
>
> 1. Taking into account the **state of the art**, the cost of implementation and the nature, scope, context and purposes of processing as well as the risks of varying likelihood and severity for rights and freedoms of natural persons posed by the processing, the controller shall, both at the time of the determination of the means for processing and at the time of the processing itself, implement appropriate technical and organisational measures, such as **pseudonymisation**, which are designed to implement data-protection principles, such as data minimisation, in an effective manner and to integrate the **necessary safeguards** into the processing in order to meet the requirements of this Regulation and protect the rights of data subjects.
> 2. The controller shall implement appropriate technical and organisational measures for ensuring that, by default, only personal data which are necessary for each specific purpose of the processing are processed. That obligation applies to the amount of personal data collected, the extent of their processing, the period of their storage and their accessibility. In particular, such measures shall ensure that by default personal data are not made accessible without the individual's intervention to an indefinite number of natural persons.
> 3. An approved certification mechanism pursuant to Article 42 may be used as an element to demonstrate compliance with the requirements set out in paragraphs 1 and 2 of this Article.
#### Clause breakdown
##### Art. 30(1)+(2) — Records content
**Clause: GDPR-CP12** | type: documentation | obligatedParty: CONTROLLER + PROCESSOR | obligationType: CONTINUOUS
**Berry anchor:** §5.1 (`where possible` × 2), §5.4.7 (closed AND-list).
**Instance 1 — VAG / S2 / `where possible` × 2**
Soft hedge on retention-period documentation and security-measure documentation. `Where possible` defers to controller judgement. S2 because the same documentation practice applies.
---
##### Art. 30(5) — 250-employee exception
**Clause: GDPR-CP13** | type: documentation exception | obligatedParty: CONTROLLER + PROCESSOR (<250 persons) | obligationType: CONTINUOUS
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

<!-- aegis:purity: own_reg=GDPR; demoted=0; core_cross_mentions=0 -->

