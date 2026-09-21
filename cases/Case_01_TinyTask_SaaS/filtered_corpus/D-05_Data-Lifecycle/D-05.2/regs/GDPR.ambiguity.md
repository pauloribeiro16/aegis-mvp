# D-05.2 — Relevant Ambiguity (GDPR)

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
##### Art. 10 — Processing of criminal convictions
**Clause: GDPR-CL25** | type: principle (criminal data) | obligatedParty: CONTROLLER (official authority only for comprehensive registers) | obligationType: PER-RECORD
**Berry anchor:** §5.1 (`appropriate safeguards`, `comprehensive register`).
**Instance 1 — VAG / S3 / `comprehensive register`**
`comprehensive register` is undefined; the term encompasses national criminal-record databases but the boundary with sectoral registers (e.g. fraud registers, sanctions lists, AML/KYC databases) is contested.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | `Comprehensive register` = national criminal-records database (e.g. UK's Police National Computer). | Recital 50 (non-binding); Member State practice. |
| R2 | `Comprehensive register` = any database covering all convictions of a population segment (including fraud registers, sex-offender registers). | EDPB Guidelines on criminal-conviction data. |
| R3 | `Comprehensive register` = any database whose coverage exceeds sectoral purpose. | Loose reading. |
R1 vs R3 yield materially distinct scope of `official authority` control.
---
### Article 11 — Processing not requiring identification
#### Verbatim (with highlighting)
> **Article 11**
>
> 1. The controller shall not be obliged to maintain, acquire or process **additional information** to identify the data subject for the sole purpose of complying with this Regulation in order to comply with the obligations laid down in Articles 5 to 9 (...).
> 2. Where in cases referred to in this Article the controller is able to demonstrate that it is not in a position to identify the data subject, the controller shall inform the data subject accordingly, if possible. In such cases, Articles 15 to 20 do not apply except where the data subject, for the purpose of exercising his or her rights under those articles, provides **additional information** enabling his or her identification.
#### Clause breakdown
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
##### Art. 30(1)+(2) — Records content
**Clause: GDPR-CP12** | type: documentation | obligatedParty: CONTROLLER + PROCESSOR | obligationType: CONTINUOUS
**Berry anchor:** §5.1 (`where possible` × 2), §5.4.7 (closed AND-list).
**Instance 1 — VAG / S2 / `where possible` × 2**
Soft hedge on retention-period documentation and security-measure documentation. `Where possible` defers to controller judgement. S2 because the same documentation practice applies.
---

<!-- aegis:purity: own_reg=GDPR; demoted=0; core_cross_mentions=0 -->

