# D-05.3 — Relevant Ambiguity (GDPR)

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
##### Art. 11(1) — No identification obligation
**Clause: GDPR-CL26** | type: principle (identification exemption) | obligatedParty: CONTROLLER | obligationType: PER-REQUEST
**Berry anchor:** §3.3.1 (`additional information` polysemy), §5.1.
**Instance 1 — POLY / S2 / `additional information`**
`additional information` is used in two senses within the same article: (i) information the controller would need to *maintain or acquire* for identification; (ii) information the data subject would need to *provide* for exercising rights. The two senses overlap but are not identical. S2 because both readings converge on the controller's identification-exemption decision.
---
### Chapter II synthesis
#### Counts
| Category | Instances | Clauses affected |
|---|---|---|
| VAG | 38 | 26 / 26 |
| POLY | 22 | 24 / 26 |
| COORD | 18 | 21 / 26 |
| SCOPE-Q | 7 | 7 / 26 |
| **Total** | **85** | **26 / 26** |
| Severity | Instances |
|---|---|
| S1 — Low | 0 |
| S2 — Medium | 53 |
| S3 — High | 32 |
#### Recurring patterns
- `necessary` appears in **6 of 26 clauses** — the dominant vague term of Chapter II (consistent with Berry's identification of `necessary` as one of the most-frequent vague terms in legal text).
- 6 lawfulness bases in Art. 6(1)(a)–(f) — each independently enumerated, each with `necessary` qualifier. The 6-fold enumeration creates a coordination question (any single basis, or all must hold?) — Berry §5.4.7 menu-card pattern.
- `explicit consent` (Art. 9(2)(a)) vs `specific consent` (Art. 4(11)) — POLY between `explicit` and `specific`. EDPB Guidelines attempt to fix but the OJ text does not.
- Art. 4(1) `identifiable` ambiguity propagates throughout the chapter (Art. 5(1)(e) `form which permits identification`, Art. 11 `additional information`).
#### Cross-article structural observations
1. **Art. 5 is the foundational principle layer; Art. 6 is the lawfulness-anchor layer.** Every downstream clause derives its binding force from one of these two anchors. Berry §5.5 parallelism: the 7 sub-principles of Art. 5 are structurally parallel and admit parallel interpretation issues.
2. **Art. 6(1) is a 6-fold disjunction.** The phrase `at least one of the following applies` (Art. 6(1) intro) anchors the inclusive-OR reading, but the cross-clause interplay (Art. 6(1)(f) final subparagraph excludes public authorities from (f); Art. 6(2) introduces Member State derogations for (c) and (e)) creates a layered structure.
3. **Art. 8 is incomplete.** The 16/13-age gating is fixed by Member State law per Art. 8(1); Art. 8(2) `reasonable efforts` is the operative controller obligation. The `available technology` qualifier shifts the standard over time.
4. **Art. 9 is the densest special-category provision.** The 10 sub-exceptions (a)–(j) of Art. 9(2) each open a distinct pathway for special-category processing. Several cross-reference Charter Art. 52(1) proportionality (the `essence of the right` phrasing).
5. **Art. 11 is under-utilised.** The identification-exemption applies only to Art. 5–9 obligations; data subject rights (Art. 15–20) are exempted only when the data subject cannot provide `additional information` for re-identification. Many controllers over-rely on Art. 11 to refuse SARs (the practical reading is narrower than the headline).
#### Anti-pattern notes for downstream files
- Chapter III (Rights, Art. 12–23) inherits Art. 5(1)(a) `transparent`, Art. 6 lawfulness bases, and Art. 7 consent conditions. Disambiguation chains should refer back to Chapter II anchors.
- Chapter IV (Controller/Processor, Art. 24–39) inherits Art. 5(2) accountability, Art. 6 lawfulness, Art. 7 demonstrability, Art. 8 child consent, Art. 9 special categories, Art. 10 criminal convictions. Art. 24's `appropriate technical and organisational measures` is structurally parallel to Art. 5(1)(f) and Art. 32(1).
- Chapter V (Transfers, Art. 44–49) inherits Art. 4(1) `identifiable`, Art. 5(1)(f) `appropriate security`, Art. 9 special categories. Transfer mechanisms reference Art. 6 lawfulness bases.
##### Art. 15(4) — Third-party rights
**Clause: GDPR-RT11** | type: data subject right (scope limitation) | obligatedParty: CONTROLLER | obligationType: PER-REQUEST
**Berry anchor:** §5.1 (`rights and freedoms of others`).
**Instance 1 — VAG / S3 / `shall not adversely affect the rights and freedoms of others`**
Whose `rights and freedoms`? Other data subjects (whose data appears in shared records), the controller, third parties (employees, partners)? The clause does not differentiate.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Redact only data identifying other natural persons. | EDPB reading. |
| R2 | Redact any data that could affect other parties (incl. commercial confidentiality). | Broad reading. |
R1 vs R2 yield materially distinct redaction workflows.
---
### Article 16 — Right to rectification
#### Verbatim
> **Article 16**
> **Right to rectification**
>
> The data subject shall have the right to obtain from the controller **without undue delay** the rectification of **inaccurate** personal data concerning him or her. Taking into account the purposes of the processing, the data subject shall have the right to have **incomplete personal data completed**, including by means of providing a **supplementary statement**.
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
##### Art. 28(3) — Processor contract content (8 mandatory clauses)
**Clause: GDPR-CP09** | type: processor-side obligation | obligatedParty: PROCESSOR | obligationType: PER-CONTRACT
**Berry anchor:** §5.4.7 (8-element closed AND-list (a)–(h)).
**Instance 1 — COORD / S2 / 8-element AND-list**
Each sub-clause is mandatory. S2 because all 8 sub-clauses are substantive obligations with the same compliance practice.
---
##### Art. 28(3)(g) — Data return or deletion
**Clause: GDPR-CP10** | type: processor-side obligation | obligatedParty: PROCESSOR | obligationType: PER-CONTRACT-END
**Berry anchor:** §3.3.1 (`deletes` polysemy — cf. Art. 17), §5.4.7 (`deletes or returns ... and deletes existing copies`).
**Instance 1 — POLY / S3 / `deletes`**
`deletes` has three operational senses: physical destruction, logical deletion (recoverable), cryptographic erasure. GDPR does not specify which.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | `Deletes` = cryptographic erasure (key destruction). | EDPB Guidelines 5/2020 on storage limitation. |
| R2 | `Deletes` = logical deletion with reasonable recovery effort. | Industry reading. |
| R3 | `Deletes` = physical destruction. | Strict reading. |
R1 vs R3 yield materially distinct deletion-engineering requirements.
**Instance 2 — SCOPE-Q / S2 / `all the personal data` + `existing copies`**
`All` is the dangerous universal quantifier (Berry & Kamsties 2000). Includes backups? Includes derived datasets? Includes logs? S2 because the same backup-deletion policy applies.
---
### Article 29 — Processing under authority
#### Verbatim (with highlighting)
> **Article 29**
> **Processing under the authority of the controller or processor**
>
> The processor and any person acting under the authority of the controller or of the processor, who has access to personal data, shall not process those data except on **instructions** from the controller, unless required to do so by Union or Member State law.
#### Clause breakdown

<!-- aegis:purity: own_reg=GDPR; demoted=0; core_cross_mentions=0 -->

