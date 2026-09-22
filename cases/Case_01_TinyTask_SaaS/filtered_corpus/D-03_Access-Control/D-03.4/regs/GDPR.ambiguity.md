# D-03.4 — Relevant Ambiguity (GDPR)

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
##### Art. 25(1) — Privacy by design
**Clause: GDPR-CP02** | type: design obligation | obligatedParty: CONTROLLER | obligationType: CONTINUOUS
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

<!-- aegis:purity: own_reg=GDPR; demoted=0; core_cross_mentions=0 -->