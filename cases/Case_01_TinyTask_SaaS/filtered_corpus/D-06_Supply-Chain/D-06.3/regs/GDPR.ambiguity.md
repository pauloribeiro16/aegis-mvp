# D-06.3 — Relevant Ambiguity (GDPR)

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
##### Art. 28(2) — Sub-processor authorisation
**Clause: GDPR-CP08** | type: processor-side obligation | obligatedParty: PROCESSOR | obligationType: PER-SUB-PROCESSOR
**Berry anchor:** §5.1 (`prior specific or general`).
**Instance 1 — VAG+SCOPE-Q / S2 / `prior specific or general written authorisation`**
`Specific` vs `general` are polar alternatives (the same `or` question as Art. 6(1)(a) consent specificity). S2 because both readings converge on written authorisation.
---
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
##### Art. 33(1) — 72-hour notification
**Clause: GDPR-CP17** | type: breach notification | obligatedParty: CONTROLLER | obligationType: TRIGGERED (per breach)
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
##### Art. 44 — General transfer principle
**Clause: GDPR-TR01** | type: principle (transfers) | obligatedParty: CONTROLLER + PROCESSOR | obligationType: PER-TRANSFER
**Berry anchor:** §5.1 (`not undermined`).
**Instance 1 — VAG / S3 / `not undermined`**
`Undermined` is qualitative. The clause establishes an outcome obligation (level-of-protection equivalence) without specifying the test for equivalence. EDPB Recommendations 01/2020 on supplementary measures attempt to operationalise.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | `Not undermined` = substantial equivalence in essential content. | Schrems II (C-311/18) C-311/18 `essentially equivalent` standard. |
| R2 | `Not undermined` = additional safeguards (technical + contractual) achieve substantial equivalence. | EDPB Recommendations 01/2020. |
| R3 | `Not undermined` = data subject's substantive rights remain enforceable. | Schrems II practical reading. |
R1 vs R3 yield materially distinct transfer-engineering requirements.
**Instance 2 — POLY / S3 / `onward transfers`**
`Onward transfers` is undefined. The Schrems II decision highlights the practical problem: post-transfer the controller has limited enforcement capability.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | `Onward transfers` = any subsequent transfer from the initial recipient onward. | Strict text. |
| R2 | `Onward transfers` = subsequent transfers to a different third country (excluding within-country transfers). | Schrems II practical reading. |
R1 vs R2 yield materially distinct onward-transfer assessment scope.
---
### Article 45 — Adequacy decisions
#### Verbatim (with highlighting)
> **Article 45**
> **Transfers on the basis of an adequacy decision**
>
> 1. A transfer of personal data to a third country or to an international organisation may take place where the Commission has decided that the third country, a territory or one or more specified sectors within that third country, or the international organisation in question ensures an **adequate level of protection**. Such a transfer shall not require any specific authorisation.
> 2. When assessing the adequacy of the level of protection, the Commission shall, in particular, take account of the following elements:
> (a) the rule of law, respect for human rights and fundamental freedoms, relevant legislation, both general and sectoral, including concerning public security, defence, national security and criminal law and the access of public authorities to personal data (...)
> (b) the existence and effective functioning of one or more **independent supervisory authorities** in the third country or to which an international organisation is subject (...)
> (c) the international commitments the third country or international organisation concerned has entered into (...)
> 3. The Commission, after assessing the adequacy of the level of protection, may decide, by means of implementing act, that a third country (...) ensures an adequate level of protection within the meaning of paragraph 2 of this Article. The implementing act shall provide for a mechanism for a periodic review, **at least every four years**, which shall take into account all relevant developments in the third country or international organisation.
#### Clause breakdown
##### Art. 45(1) — Adequacy-based transfer
**Clause: GDPR-TR02** | type: transfer mechanism (adequacy) | obligatedParty: CONTROLLER + PROCESSOR | obligationType: PER-TRANSFER (to adequacy-decision country)
**Berry anchor:** §5.1 (`adequate level of protection`).
**Instance 1 — VAG / S3 / `adequate level of protection`**
`Adequate level of protection` is the central transfer concept, derived from Schrems II's `essentially equivalent` test. The Commission decides (Art. 45(3)) but the substantive standard is undefined in the OJ text.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Adequacy = substantively equivalent protection (Schrems II). | CJEU C-311/18 Schrems II. |
| R2 | Adequacy = acceptable local law + practice. | Original Commission practice pre-Schrems II. |
R1 vs R2 yield materially distinct third-country-selection policies.
---
##### Art. 45(3) — Periodic review
**Clause: GDPR-TR03** | type: adequacy maintenance | obligatedParty: EUROPEAN COMMISSION | obligationType: PERIODIC (4 years)
**Berry anchor:** §5.1 (`at least every four years`).
**Instance 1 — VAG / S2 / `at least every four years`**
Hard numeric anchor (4 years) reduces temporal ambiguity. `At least` permits earlier review. S2 because the same review-practice applies.
---
### Article 46 — Transfers subject to appropriate safeguards
#### Verbatim (with highlighting)
> **Article 46**
> **Transfers subject to appropriate safeguards**
>
> 1. In the absence of a decision pursuant to Article 45(3), a controller or processor may transfer personal data to a third country or to an international organisation only if the controller or processor has provided **appropriate safeguards**, and on condition that **enforceable data subject rights and effective legal remedies** for data subjects are available.
> 2. The appropriate safeguards referred to in paragraph 1 may be provided for, without requiring any specific authorisation from a supervisory authority, by:
> (a) a **legally binding and enforceable instrument between public authorities or bodies**;
> (b) **binding corporate rules** in accordance with Article 47;
> (c) **standard data protection clauses** adopted by the Commission (...) (SCCs);
> (d) standard data protection clauses adopted by a supervisory authority and approved by the Commission (...);
> (e) an **approved code of conduct** pursuant to Article 40 together with binding and enforceable commitments of the controller or processor in the third country to apply the appropriate safeguards (...);
> (f) an **approved certification mechanism** pursuant to Article 42 together with binding and enforceable commitments of the controller or processor in the third country to apply the appropriate safeguards (...).
#### Clause breakdown
##### Art. 46(1) — General safeguards requirement
**Clause: GDPR-TR04** | type: transfer mechanism (safeguards) | obligatedParty: CONTROLLER + PROCESSOR | obligationType: PER-TRANSFER (without adequacy)
**Berry anchor:** §5.1 (`appropriate safeguards`, `enforceable`, `effective legal remedies`).
**Instance 1 — VAG / S3 / `appropriate safeguards`, `enforceable data subject rights and effective legal remedies`**
Two vague qualifiers combined with AND. Schrems II invalidated the Privacy Shield but upheld SCCs (then EU-US Data Privacy Framework). The `appropriate safeguards` standard post-Schrems II requires case-by-case assessment of third-country law.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | `Appropriate` = technical + contractual safeguards achievable for the specific transfer. | EDPB Recommendations 01/2020. |
| R2 | `Appropriate` = essential equivalence with EU protection level. | Schrems II. |
R1 vs R2 yield materially distinct transfer-assessment workflows.
---
##### Art. 46(2) — Closed list of safeguards mechanisms
**Clause: GDPR-TR05** | type: transfer mechanism (closed list) | obligatedParty: CONTROLLER + PROCESSOR | obligationType: PER-TRANSFER
**Berry anchor:** §5.4.7 (6-element closed OR-list (a)–(f)).
**Instance 1 — COORD / S3 / `(a) OR (b) OR (c) OR (d) OR (e) OR (f)`**
6 disjunctive mechanisms. Each is independent. Schrems II implicitly tightened the assessment for SCCs (c)/(d); the Binding Corporate Rules route (b) requires supervisory-authority approval.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Any one mechanism suffices; assess independently. | Strict text. |
| R2 | Multiple mechanisms stack; Schrems II requires supplementary measures. | Schrems II practical reading. |
R1 vs R2 yield materially distinct transfer-mechanism combinations.
---
### Article 47 — Binding corporate rules
#### Verbatim (with highlighting)
> **Article 47**
> **Binding corporate rules**
>
> 1. The competent supervisory authority shall approve binding corporate rules in accordance with the consistency mechanism set out in Article 63, provided that they:
> (a) are **legally binding and apply to and are enforced by every member** concerned of the group of undertakings (...) including their employees;
> (b) expressly confer **enforceable rights on data subjects** with regard to the processing of their personal data;
> (c) fulfil the requirements laid down in paragraph 2.
> 2. The binding corporate rules referred to in paragraph 1 shall specify at least: (a) structure and contact details; (b) data transfers; (c) legally binding nature; (d) general data protection principles (...) including onward transfers to bodies not bound by the binding corporate rules; (e) data subject rights; (f) acceptance of liability by EU controller/processor for breaches by non-EU members; (g) how info is provided to data subjects; (h) DPO tasks; (i) complaint procedures; (j) verification mechanisms including data protection audits; (k) mechanisms for reporting and recording changes; (l) cooperation mechanism with the supervisory authority; (m) mechanisms for reporting conflicting legal requirements in third countries; (n) data protection training.
#### Clause breakdown
##### Art. 47(2)(f) — Liability acceptance
**Clause: GDPR-TR06** | type: BCR component | obligatedParty: EU CONTROLLER/PROCESSOR | obligationType: CONTINUOUS
**Berry anchor:** §5.1 (`shall be exempt from that liability, in whole or in part, only if it proves that that member is not responsible for the event giving rise to the damage`).
**Instance 1 — VAG / S3 / `shall be exempt ... only if it proves that that member is not responsible`**
The standard of proof (`proves`) and the standard of responsibility (`not responsible for the event`) are both qualitative. BCRs typically include dispute-resolution and insurance mechanisms to operationalise this clause.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | `Proves` = demonstrates on balance of probabilities. | Standard civil-law reading. |
| R2 | `Proves` = strict liability unless rebutted by clear evidence. | Strict reading. |
R1 vs R2 yield materially distinct BCR liability-engineering scope.
---
### Article 48 — Transfers or disclosures not authorised by Union law
#### Verbatim (with highlighting)
> **Article 48**
> **Transfers or disclosures not authorised by Union law**
>
> Any judgment of a court or tribunal and any decision of an administrative authority of a third country requiring a controller or processor to transfer or disclose personal data may only be recognised or enforceable in any manner if based on an international agreement, such as a mutual legal assistance treaty, in force between the requesting third country and the Union or a Member State, without prejudice to other grounds for transfer pursuant to this Chapter.
#### Clause breakdown
##### Art. 48 — Third-country legal-request filter
**Clause: GDPR-TR07** | type: anti-overreach | obligatedParty: CONTROLLER + PROCESSOR | obligationType: PER-REQUEST
**Berry anchor:** §3.3.1 (`mutual legal assistance treaty` polysemy).
**Instance 1 — POLY / S3 / `international agreement, such as a mutual legal assistance treaty`**
The `such as` opens the list (Berry §5.1). Other international agreements (e.g. UN treaties, regional human rights instruments) may qualify. The CLOUD Act conflict with GDPR is the canonical example.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Only formal mutual legal assistance treaties qualify. | Strict reading. |
| R2 | Any binding international agreement between the third country and EU/Member State qualifies. | Broad reading. |
R1 vs R2 yield materially distinct third-country-request-handling policies (especially post-CLOUD Act for US).
---
### Article 49 — Derogations for specific situations
#### Verbatim (with highlighting)
> **Article 49**
> **Derogations for specific situations**
>
> 1. In the absence of an adequacy decision pursuant to Article 45(3), or of appropriate safeguards pursuant to Article 46, including binding corporate rules, a transfer or a set of transfers of personal data to a third country or an international organisation shall take place only on one of the following conditions:
> (a) the data subject has **explicitly consented** to the proposed transfer, after having been informed of the possible risks of such transfers for the data subject due to the absence of an adequacy decision and appropriate safeguards;
> (b) the transfer is necessary for the performance of a contract between the data subject and the controller or the implementation of pre-contractual measures taken at the data subject's request;
> (c) the transfer is necessary for the conclusion or performance of a contract concluded in the interest of the data subject between the controller and another natural or legal person;
> (d) the transfer is necessary for **important reasons of public interest**;
> (e) the transfer is necessary for the **establishment, exercise or defence of legal claims**;
> (f) the transfer is necessary in order to protect the **vital interests** of the data subject or of other persons, where the data subject is physically or legally incapable of giving consent;
> (g) the transfer is made from a register which according to Union or Member State law is intended to provide information to the public and which is open to consultation either by the public in general or by any person who can demonstrate a legitimate interest, but only to the extent that the conditions laid down by Union or Member State law for consultation are fulfilled in the particular case.
>
>    Where a transfer could not be based on a provision in Article 45 or 46, including the provisions on binding corporate rules, and none of the derogations for a specific situation referred to in the first subparagraph of this paragraph is applicable, a transfer to a third country or to an international organisation may take place only if the transfer is **not repetitive**, concerns only a **limited number of data subjects**, is necessary for the purposes of **compelling legitimate interests** pursued by the controller which are not overridden by the interests or rights and freedoms of the data subject, and the controller has assessed all the circumstances surrounding the data transfer and has on the basis of that assessment provided **suitable safeguards** with regard to the protection of personal data.
#### Clause breakdown
##### Art. 49(1)(a) — Explicit consent for transfer
**Clause: GDPR-TR08** | type: derogation (consent) | obligatedParty: CONTROLLER + PROCESSOR | obligationType: PER-TRANSFER (no adequacy + no safeguards)
**Berry anchor:** §3.3.1 (`explicitly consented` polysemy — vs Art. 4(11) `specific` and Art. 9(2)(a) `explicit`).
**Instance 1 — POLY / S3 / `explicitly consented ... after having been informed of the possible risks`**
The clause requires explicit consent AND informed-of-risks. The `explicitly` qualifier's relationship to Art. 4(11) `unambiguous` and Art. 9(2)(a) `explicit` is unclear — three different qualifiers across three articles for transfer consent.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | `Explicitly consented` = the strongest consent form (cf. Art. 9(2)(a) for special categories). | Strict reading. |
| R2 | `Explicitly consented` = any affirmative consent (cf. Art. 4(11) `unambiguous indication`). | Loose reading. |
R1 vs R2 yield materially distinct consent-collection UI for transfers.
---
##### Art. 49(1)(d) — Important reasons of public interest
**Clause: GDPR-TR09** | type: derogation (public interest) | obligatedParty: CONTROLLER + PROCESSOR | obligationType: PER-TRANSFER
**Berry anchor:** §5.1 (`important reasons of public interest`).
**Instance 1 — POLY+VAG / S2 / `important reasons of public interest`**
Cross-clause propagation: Art. 6(1)(e) `public interest` + Art. 23(1)(e) `other important objectives of general public interest` + Art. 49(1)(d) `important reasons of public interest`. S2 because Art. 49(1)(d) explicitly defers to Union or Member State law for recognition.
---
##### Art. 49(1)(second subparagraph) — Compelling legitimate interests (catch-all)
**Clause: GDPR-TR10** | type: derogation (last-resort) | obligatedParty: CONTROLLER + PROCESSOR | obligationType: PER-TRANSFER (no other mechanism available)
**Berry anchor:** §5.1 (`not repetitive`, `limited number`, `compelling legitimate interests`, `suitable safeguards`).
**Instance 1 — VAG+SCOPE-Q / S3 / `not repetitive, limited number, compelling legitimate interests, suitable safeguards`**
Four conjunctive qualifiers. The catch-all derogation requires ALL to be met. EDPB Guidelines 2/2018 attempt to operationalise but the thresholds are qualitative.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | The 4 conditions are cumulative; all must hold. | EDPB Guidelines 2/2018. |
| R2 | Some conditions can be relaxed in compelling cases. | Loose reading. |
R1 vs R2 yield materially distinct catch-all derogation eligibility assessment.
**Instance 2 — POLY / S3 / `compelling legitimate interests`**
Cross-clause propagation: Art. 21(1) `compelling legitimate grounds` (objection) + Art. 49(1) `compelling legitimate interests` (transfer). The two `compelling legitimate` qualifiers may or may not share interpretation.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | `Compelling` = strictly necessary (lex specialis). | Schrems II reading. |
| R2 | `Compelling` = materially more weighty than the data subject's interests. | Loose reading. |
R1 vs R2 yield materially distinct catch-all transfer-eligibility assessment.
---
### Chapter V synthesis
#### Counts
| Category | Instances | Clauses affected |
|---|---|---|
| VAG | 11 | 10 / 10 |
| POLY | 7 | 7 / 10 |
| COORD | 5 | 5 / 10 |
| SCOPE-Q | 2 | 2 / 10 |
| **Total** | **25** | **10 / 10** |
| Severity | Instances |
|---|---|
| S1 — Low | 0 |
| S2 — Medium | 14 |
| S3 — High | 11 |
#### Recurring patterns
- `appropriate` and `adequate` appear in 5 of 10 clauses — the Chapter's twin Berry-flagged qualifiers.
- `compelling legitimate interests` (Art. 49) propagates from Art. 21(1) — cross-chapter POLY.
- Schrems II is the dominant interpretive anchor for Chapter V but is non-textual.
#### Cross-clause structural observations
1. **Art. 44 is the umbrella principle.** All transfers (Art. 45–49) must comply with Chapter V conditions AND with Art. 44's `not undermined` outcome obligation.
2. **Art. 45–46 are the primary mechanisms.** Adequacy (Art. 45) and safeguards (Art. 46) cover the majority of legitimate transfers. Art. 49 derogations are narrow last-resort exceptions.
3. **Schrems II decision cascade.** The Schrems II (C-311/18) ruling invalidated Privacy Shield, requiring SCCs to be supplemented with case-by-case transfer impact assessments. This non-textual standard shapes Chapter V application.
4. **`essentially equivalent` test vs `appropriate safeguards` standard.** Schrems II uses `essentially equivalent` for adequacy assessment; Art. 46(1) uses `appropriate safeguards`. The relationship between the two standards is judicially established but textually ambiguous.
5. **Art. 49(1)(a) consent three-way inconsistency.** Art. 4(11) `unambiguous` + Art. 9(2)(a) `explicit` + Art. 49(1)(a) `explicitly` — three different consent qualifiers for three different consent scenarios. Layer 2 would resolve.
#### Anti-pattern notes for synthesis
- Chapter V is the only chapter whose compliance depends on non-OJ-text anchors (Schrems II). The drafter's intent is sometimes inferred from CJEU jurisprudence rather than from the regulation text.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/GDPR.ambiguity.md

The awareness trigger is polysemous (cf. CRA C25, NIS 2 C25 — same pattern across regulations).

### from regs/GDPR.ambiguity.md

- Cross-regulation: DORA Art. 28(8) ICT third-party risk management overlaps with GDPR Chapter V for financial entities transferring data to non-EU ICT providers.


<!-- aegis:purity: own_reg=GDPR; demoted=2; core_cross_mentions=0 -->

