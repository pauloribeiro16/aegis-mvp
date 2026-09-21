# D-03.3 — Relevant Ambiguity (GDPR)

> Part 4 ambiguity analysis for GDPR, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## GDPR
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
##### Art. 28(3) — Processor contract content (8 mandatory clauses)
**Clause: GDPR-CP09** | type: processor-side obligation | obligatedParty: PROCESSOR | obligationType: PER-CONTRACT
**Berry anchor:** §5.4.7 (8-element closed AND-list (a)–(h)).
**Instance 1 — COORD / S2 / 8-element AND-list**
Each sub-clause is mandatory. S2 because all 8 sub-clauses are substantive obligations with the same compliance practice.
---
##### Art. 29 — Instructions-only processing
**Clause: GDPR-CP11** | type: instruction-bound | obligatedParty: PROCESSOR + AUTHORISED PERSONS | obligationType: CONTINUOUS
**Berry anchor:** §3.3.1 (`instructions` polysemy).
**Instance 1 — POLY / S2 / `instructions`**
`Instructions` is undefined — formal written only? Verbal? Implied via workflow? S2 because the same instruction-documentation practice applies.
---
### Article 30 — Records of processing activities
#### Verbatim (with highlighting)
> **Article 30**
> **Records of processing activities**
>
> 1. Each controller and, where applicable, the controller's representative, shall maintain a **record** of processing activities under its responsibility. That record shall contain <u>all of the following information</u>:
> (a) the name and contact details of the controller and, where applicable, of the joint controller, the controller's representative and the data protection officer;
> (b) the purposes of the processing;
> (c) a description of the categories of data subjects and of the categories of personal data;
> (d) the categories of recipients to whom the personal data have been or will be disclosed including recipients in third countries or international organisations;
> (e) where applicable, transfers of personal data to a third country or an international organisation, including the identification of that third country or international organisation and, in case of transfers referred to in the second subparagraph of Article 49(1), the documentation of suitable safeguards;
> (f) **where possible**, the envisaged time limits for erasure of the different categories of data;
> (g) **where possible**, a general description of the technical and organisational security measures referred to in Article 32(1).
> 2. Each processor and, where applicable, the processor's representative shall maintain a record of all categories of processing activities carried out on behalf of a controller, containing: (a)–(d) similarly (b)–(d) below.
> 3. The records referred to in paragraphs 1 and 2 shall be **in writing, including in electronic form**.
> 4. The controller or the processor and, where applicable, the controller's or the processor's representative, shall make the record available to the supervisory authority on request.
> 5. The obligations referred to in paragraphs 1 and 2 shall not apply to an enterprise or an organisation employing **fewer than 250 persons** unless the processing it carries out is likely to result in a risk to the rights and freedoms of data subjects, the processing is not occasional, or the processing includes special categories of data as referred to in Article 9(1) or personal data relating to criminal convictions and offences referred to in Article 10.
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

