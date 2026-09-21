# D-01.4 — Relevant Ambiguity (GDPR)

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
##### Art. 5(1)(d) — Accuracy
**Clause: GDPR-CL04** | type: principle | obligatedParty: CONTROLLER | obligationType: CONTINUOUS
**Berry anchor:** §3.3.5 (vagueness), §5.1 (`reasonable`, `accurate`, `necessary`).
**Instance 1 — VAG / S3 / `accurate`, `reasonable step`, `necessary`**
`accurate` has no defined threshold; `reasonable step` is open-ended; `where necessary` and `without delay` are inquiry-resistant. Art. 16 (right to rectification) provides partial anchoring but does not define accuracy standard.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Accurate iff matches the source from which the data was collected (input-accuracy). | Strict textual reading. |
| R2 | Accurate iff reflects the data subject's current real-world state at the time of processing (output-accuracy). | Recital 39 (non-binding); ICO accuracy code. |
R1 vs R2 yield materially distinct compliance obligations (R1 requires input-validation; R2 requires periodic refresh).
**Instance 2 — VAG / S2 / `inaccurate` (Berry §3.3.5)**
Whether data is `inaccurate` admits borderline cases (e.g. stale data, contested data). S2 because Art. 16's rectification mechanism handles disputes.
---
##### Art. 5(1)(f) — Integrity and confidentiality
**Clause: GDPR-CL06** | type: principle | obligatedParty: CONTROLLER | obligationType: CONTINUOUS
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
##### Art. 16 — Rectification right
**Clause: GDPR-RT12** | type: data subject right (rectification) | obligatedParty: CONTROLLER | obligationType: PER-REQUEST
**Berry anchor:** §5.1 (`without undue delay`, `inaccurate`, `incomplete`).
**Instance 1 — VAG / S2 / `inaccurate`, `incomplete`**
Inherits the Art. 5(1)(d) `accuracy` ambiguity (Clause CL04). S2 because the implementation test is the same as Art. 5(1)(d).
**Instance 2 — POLY / S3 / `supplementary statement`**
A supplementary statement is a distinct mechanism from rectification: it preserves the original data and adds the data subject's version. EDPB Guidelines on Art. 16 treat this as required when factual dispute exists.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Supplementary statement required only when factual dispute exists. | EDPB Guidelines on Art. 16. |
| R2 | Supplementary statement required upon data-subject request, regardless of factual dispute. | Strict reading. |
R1 vs R2 yield materially distinct rectification workflows.
---
### Article 17 — Right to erasure (already covered in v0.1)
> Already analysed in `../Regulation/GDPR/Ambiguity/02_GDPR.md` v0.1 as GDPR-C06. Reference only — cross-chapter inheritance applies.
---
### Article 18 — Right to restriction
#### Verbatim (with highlighting)
> **Article 18**
> **Right to restriction of processing**
>
> 1. The data subject shall have the right to obtain from the controller restriction of processing where one of the following applies:
> (a) the accuracy of the personal data is contested by the data subject, for a period enabling the controller to verify the accuracy of the personal data;
> (b) the processing is unlawful and the data subject opposes the erasure of the personal data and requests the restriction of their use instead;
> (c) the controller no longer needs the personal data for the purposes of the processing, but they are required by the data subject for the establishment, exercise or defence of legal claims;
> (d) the data subject has objected to processing pursuant to Article 21(1) pending the verification whether the legitimate grounds of the controller override those of the data subject.
> 2. Where processing has been restricted under paragraph 1, such personal data shall, with the exception of storage, only be processed with the data subject's consent or for the establishment, exercise or defence of legal claims or for the protection of the rights of another natural or legal person or for reasons of important public interest of the Union or of a Member State.
> 3. A data subject who has obtained restriction of processing pursuant to paragraph 1 shall be informed by the controller before the restriction of processing is lifted.
#### Clause breakdown
##### Art. 19 — Recipient notification
**Clause: GDPR-RT15** | type: data subject right (cascade notification) | obligatedParty: CONTROLLER | obligationType: PER-ACTION
**Berry anchor:** §5.1 (`impossible`, `disproportionate effort`).
**Instance 1 — VAG / S3 / `impossible` or `disproportionate effort`**
Two escape clauses (Berry §5.1). `impossible` is binary; `disproportionate effort` is qualitative.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Both clauses narrow; either suffices. | Strict reading; logical OR. |
| R2 | Both clauses must hold (impossible AND disproportionate). | Strict pro-data-subject reading. |
R1 vs R2 yield materially distinct cascade-notification policies.
---
### Article 20 — Right to data portability (already covered in v0.1)
> Already analysed in `../Regulation/GDPR/Ambiguity/02_GDPR.md` v0.1 as GDPR-C07. Reference only.
---
### Article 21 — Right to object
#### Verbatim (with highlighting)
> **Article 21**
> **Right to object**
>
> 1. The data subject shall have the right to object, on grounds relating to his or her particular situation, at any time to processing of personal data concerning him or her which is based on point (e) or (f) of Article 6(1), including profiling based on those provisions. The controller shall no longer process the personal data unless the controller demonstrates **compelling legitimate grounds** for the processing which override the interests, rights and freedoms of the data subject or for the establishment, exercise or defence of legal claims.
> 2. Where personal data are processed for direct marketing purposes, the data subject shall have the right to object at any time to processing of personal data concerning him or her for such marketing, which includes profiling to the extent that it is related to such direct marketing.
> 3. Where the data subject objects to processing for direct marketing purposes, the personal data shall no longer be processed for such purposes.
> 4. At the latest at the time of the first communication with the data subject, the right referred to in paragraphs 1 and 2 shall be **explicitly brought to the attention of the data subject** and shall be presented clearly and separately from any other information.
> 5. In the context of the use of information society services, and notwithstanding Directive 2002/58/EC, the data subject may exercise his or her right to object by automated means using technical specifications.
> 6. Where personal data are processed for scientific or historical research purposes or statistical purposes pursuant to Article 89(1), the data subject, on grounds relating to his or her particular situation, shall have the right to object to processing of personal data concerning him or her, unless the processing is necessary for the performance of a task carried out for reasons of public interest.
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

<!-- aegis:purity: own_reg=GDPR; demoted=0; core_cross_mentions=0 -->

