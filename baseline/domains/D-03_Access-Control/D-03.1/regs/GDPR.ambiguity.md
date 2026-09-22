# D-03.1 — Relevant Ambiguity (GDPR)

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
##### Art. 6(1)(a) — Consent
**Clause: GDPR-CL08** | type: lawfulness base | obligatedParty: CONTROLLER | obligationType: PER-PURPOSE (continuous)
**Berry anchor:** §3.3.1 (polysemy of `consent` — see Art. 4(11) reference); §5.4.7 (coordination `for one or more specific purposes`).
**Instance 1 — POLY / S3 / `consent`**
`consent` inherits all Art. 4(11) ambiguities (freely given + specific + informed + unambiguous). Additionally, `consent to the processing of his or her personal data for one or more specific purposes` couples consent with purpose-binding — the `one or more specific purposes` wording has the Berry §5.4.7 menu-card ambiguity (does a single-purpose consent bind the controller? does a multi-purpose consent require fresh consent for any new purpose?).
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Consent = single-purpose. Multi-purpose consent must be granular (each purpose requires distinct affirmative action). | EDPB Guidelines 05/2020 §3.6 (granularity). |
| R2 | Consent = single document with multiple purposes listed, if freely given to each. | EDPB Guidelines 05/2020 §3.7 (bundling). |
| R3 | Consent = single document with one general purpose covering a coherent processing activity. | Loose reading; certain national DPA practices. |
R1 vs R3 yield materially distinct consent-collection UI requirements.
---
##### Art. 7(1) — Demonstrability of consent
**Clause: GDPR-CL15** | type: consent-specific | obligatedParty: CONTROLLER | obligationType: CONTINUOUS
**Berry anchor:** §5.1 (`able to demonstrate`).
**Instance 1 — VAG / S2 / `able to demonstrate`**
The standard for `demonstrating` is undefined; Art. 5(2) accountability and Art. 30 records-of-processing provide partial anchors. S2 because both reading converge on record-keeping.
---
##### Art. 7(2) — Bundled consent
**Clause: GDPR-CL16** | type: consent-specific | obligatedParty: CONTROLLER | obligationType: PER-CONSENT-COLLECTION
**Berry anchor:** §5.1 (`clearly`, `intelligible`, `easily accessible`, `clear and plain`).
**Instance 1 — VAG / S3 / `clearly distinguishable`, `intelligible and easily accessible form`, `clear and plain language`**
Four conjunctive vague modifiers on consent-presentation form. EDPB Guidelines 05/2020 §3.6 fix `clearly distinguishable` as requiring separate tick-boxes for separate purposes, but `intelligible and easily accessible form` and `clear and plain language` remain inquiry-resistant.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Compliance requires visible, separate consent UI (no pre-ticked boxes; layered notice). | EDPB Guidelines 05/2020 §3.6. |
| R2 | Compliance requires the consent text to be at a defined reading-age level. | ICO consent guidance. |
| R3 | Compliance requires absence of manipulative design patterns (dark patterns). | EDPB Guidelines on dark patterns 03/2022. |
R1 vs R3 yield materially distinct UI/UX requirements.
**Instance 2 — VAG / S2 / `Any part ... which constitutes an infringement ... shall not be binding`**
The cascading-invalidation rule: if part of the declaration infringes GDPR, only that part is unenforceable. Berry §5.5 parallelism: structurally parallels the severability doctrine. S2 because judicial application is reasonably settled.
---
##### Art. 7(3) — Withdrawal of consent
**Clause: GDPR-CL17** | type: consent-specific (data-subject right) | obligatedParty: CONTROLLER | obligationType: CONTINUOUS
**Berry anchor:** §5.1 (`at any time`, `as easy to withdraw as to give`).
**Instance 1 — VAG / S2 / `as easy to withdraw as to give`**
The standard `as easy` is undefined. EDPB Guidelines 05/2020 §3.7 fix it as: at most 2-3 clicks to reach withdrawal UI. S2 because the EDPB guideline is de facto binding on supervisory authorities.
---
##### Art. 7(4) — Conditional consent and contract
**Clause: GDPR-CL18** | type: consent-specific (anti-coupling) | obligatedParty: CONTROLLER | obligationType: PER-CONSENT-COLLECTION
**Berry anchor:** §5.1 (`utmost account`, `not necessary`).
**Instance 1 — VAG / S3 / `utmost account`, `not necessary for the performance of that contract`**
`utmost account` is the standard (Berry §5.1: `utmost` appears in similar formulations). `not necessary for the performance of that contract` couples with Art. 6(1)(b) — but the boundary of `necessary for contract performance` was already ambiguous (Clause-CL09). The two clauses together create a recursive ambiguity.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Bundling consent with contract is per se non-compliant unless the processing is genuinely `necessary` under Art. 6(1)(b) strict reading. | EDPB Guidelines 05/2020 §3.5; CJEU Bundeskartellamt (C-252/21). |
| R2 | Bundling is acceptable if the consent mechanism is clearly distinguishable. | Pre-Bundeskartellamt industry reading. |
R1 vs R2 yield materially distinct consent-collection UI requirements.
---
### Article 8 — Conditions applicable to child's consent
#### Verbatim (with highlighting)
> **Article 8**
> **Conditions applicable to child's consent in relation to information society services**
>
> 1. Where point (a) of Article 6(1) applies, in relation to the offer of information society services directly to a child, the processing of the personal data of a child shall be lawful where the child is **at least 16 years old**. Where the child is below the age of **16 years**, such processing shall be lawful only if and to the extent that consent is given or authorised by the holder of **parental responsibility** over the child.
>
> Member States may provide by law for a lower age for those purposes provided that such lower age is not below **13 years**.
>
> 2. The controller shall make **reasonable efforts** to verify in such cases that consent is given or authorised by the holder of parental responsibility over the child, taking into consideration available technology.
> 3. Paragraph 1 shall not apply to **preventive or counselling services** offered directly to a child.
#### Clause breakdown
##### Art. 8(1) — Age threshold for consent
**Clause: GDPR-CL19** | type: consent-specific (children) | obligatedParty: CONTROLLER (information-society services to children) | obligationType: PER-OFFERING
**Berry anchor:** §3.3.1 (`parental responsibility` polysemy), §5.2.1 (Member State age override).
**Instance 1 — POLY / S3 / `parental responsibility`**
`parental responsibility` is a legal term of art imported from family law; the GDPR does not define it. Recital 38 hints at it. Different Member State legal systems define it differently (sole vs joint custody; unmarried parents; same-sex parents; surrogacy). The data controller must determine responsibility for each user but has no general-purpose source of truth.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Parental responsibility = legal custody per Member State family law. | Member State family law; Hague Convention. |
| R2 | Parental responsibility = any adult presenting as parent (self-attestation). | Loose reading; ICO age-appropriate design code. |
| R3 | Parental responsibility = the parent whose contact details are available. | Industry shortcut; not in OJ. |
R1 vs R3 yield materially distinct age-verification system design.
**Instance 2 — SCOPE-Q / S2 / Member State age override**
Member States may lower the age threshold to no less than 13 — multi-jurisdictional deployments must track each Member State's threshold. S2 because the rules converge on per-Member-State age checking.
---
##### Art. 8(2) — Reasonable verification efforts
**Clause: GDPR-CL20** | type: consent-specific (children) | obligatedParty: CONTROLLER | obligationType: PER-CHILD-ACCESS
**Berry anchor:** §5.1 (`reasonable efforts`).
**Instance 1 — VAG / S3 / `reasonable efforts ... taking into consideration available technology`**
`reasonable efforts` is the recurring vague phrase. The `available technology` qualifier shifts the standard over time (2024 technology vs 2026 vs 2028). EDPB Guidelines on children's consent provide factors but not a closed list.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Reasonable efforts = best-available technical age-verification at time of design. | EDPB Guidelines on virtual age of consent 2024. |
| R2 | Reasonable efforts = whatever was state-of-the-art at time of processing (rolling standard). | EDPB Guidelines on Art. 8(2). |
| R3 | Reasonable efforts = no specific technical measure required; self-declaration sufficient. | Loose reading. |
R1 vs R3 yield materially distinct age-verification infrastructure requirements.
---
### Article 9 — Processing of special categories of personal data
#### Verbatim (with highlighting)
> **Article 9**
> **Processing of special categories of personal data**
>
> 1. Processing of personal data revealing **racial or ethnic origin**, **political opinions**, **religious or philosophical beliefs**, **trade union membership**, and processing of **genetic data**, **biometric data** for the purpose of uniquely identifying a natural person, **data concerning health** or data concerning a natural person's **sex life** or **sexual orientation** shall be prohibited.
> 2. Paragraph 1 shall not apply if one of the following applies:
> (a) the data subject has given **explicit consent** to the processing of those personal data for one or more specified purposes, unless Union or Member State law provide that the prohibition in paragraph 1 may not be lifted by the data subject;
> (b) processing is necessary for the purposes of carrying out the **obligations and exercising specific rights** of the controller or of the data subject in the field of **employment and social security and social protection law**;
> (c) processing is necessary to protect the **vital interests** of the data subject or of another natural person where the data subject is **physically or legally incapable of giving consent**;
> (d) processing is carried out in the **legitimate activities** of a foundation, association or any other not-for-profit body, with a **political, philosophical, religious or trade-union aim** ... and on condition that the processing relates solely to the members or to former members of the body or to persons who have regular contact with it in connection with its purposes and that the personal data are not disclosed outside that body without the consent of the data subjects;
> (e) processing relates to personal data which are **manifestly made public** by the data subject;
> (f) processing is necessary for the establishment, exercise or defence of **legal claims**;
> (g) processing is necessary for reasons of **substantial public interest**, on the basis of Union or Member State law, which shall be proportionate to the aim pursued, respect the essence of the right to data protection and provide for suitable and specific measures to safeguard the fundamental rights and the interests of the data subject;
> (h) processing is necessary for the purposes of **preventive or occupational medicine**, ... medical diagnosis, the provision of health or social care or treatment or the management of health or social care systems and services on the basis of Union or Member State law or pursuant to contract with a health professional and subject to professional secrecy;
> (i) processing is necessary for reasons of **public interest in the area of public health**, such as protecting against serious cross-border threats to health or ensuring high standards of quality and safety of health care and of medicinal products or medical devices;
> (j) processing is necessary for **archiving purposes in the public interest, scientific or historical research purposes or statistical purposes** in accordance with Article 89(1) based on Union or Member State law which shall be proportionate to the aim pursued, respect the essence of the right to data protection and provide for suitable and specific measures to safeguard the fundamental rights and interests of the data subject.
> 3. Personal data referred to in paragraph 1 may be processed for the purposes referred to in point (h) of paragraph 2 when those data are processed by or under the responsibility of a professional subject to the obligation of professional secrecy under Union or Member State law or rules established by national competent bodies or by another person also subject to an obligation of secrecy under Union or Member State law or rules established by national competent bodies.
> 4. Member States may maintain or introduce further conditions, including limitations, with regard to the processing of genetic data, biometric data or data concerning health.
#### Clause breakdown
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
##### Art. 12(6) — Identity verification for requests
**Clause: GDPR-RT04** | type: data-subject-facing | obligatedParty: CONTROLLER | obligationType: PER-REQUEST
**Berry anchor:** §5.1 (`reasonable doubts`, `additional information`).
**Instance 1 — VAG / S3 / `reasonable doubts`, `additional information`**
`reasonable doubts` is the recurring vague phrase; `additional information` is undefined. Art. 12(6) permits asking for more info but does not bound the scope. Combined with the controller's data-minimisation duty (Art. 5(1)(c)), the controller should ask minimally.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Controller may request minimal identity verification (e.g. authenticated login). | EDPB Guidelines 5/2019 §6. |
| R2 | Controller may request identity document copy. | Industry practice. |
| R3 | Controller must accept self-declaration if any doubt exists. | Strict pro-data-subject reading. |
R1 vs R3 yield materially distinct identity-verification systems.
---
### Article 13 — Information when collected from data subject
#### Verbatim (with highlighting)
> **Article 13**
> **Information to be provided where personal data are collected from the data subject**
>
> 1. Where personal data relating to a data subject are collected from the data subject, the controller shall, at the time when personal data are obtained, provide the data subject with <u>all of the following information</u>:
> (a) the identity and the contact details of the controller and, where applicable, of the controller's representative;
> (b) the contact details of the data protection officer, where applicable;
> (c) the purposes of the processing for which the personal data are intended as well as the legal basis for the processing;
> (d) where the processing is based on point (f) of Article 6(1), the legitimate interests pursued by the controller or by a third party;
> (e) the recipients or categories of recipients of the personal data, if any;
> (f) where applicable, the fact that the controller intends to transfer personal data to a third country or international organisation and the existence or absence of an adequacy decision by the Commission, or in the case of transfers referred to in Article 46 or 47, or the second subparagraph of Article 49(1), reference to the appropriate or suitable safeguards and the means by which to obtain a copy of them or where they have been made available.
> 2. In addition to the information referred to in paragraph 1, the controller shall, at the time when personal data are obtained, provide the data subject with the following further information necessary to ensure fair and transparent processing:
> (a) the period for which the personal data will be stored, or if that is not possible, the criteria used to determine that period;
> (b) the existence of the right to request from the controller access to and rectification or erasure of personal data or restriction of processing concerning the data subject or to object to processing as well as the right to data portability;
> (c) where the processing is based on point (a) of Article 6(1) or point (a) of Article 9(2), the existence of the right to withdraw consent at any time, without affecting the lawfulness of processing based on consent before its withdrawal;
> (d) the right to lodge a complaint with a supervisory authority;
> (e) whether the provision of personal data is a statutory or contractual requirement, or a requirement necessary to enter into a contract, as well as whether the data subject is obliged to provide the personal data and of the possible consequences of failure to provide such data;
> (f) the existence of automated decision-making, including profiling, referred to in Article 22(1) and (4) and, at least in those cases, meaningful information about the logic involved, as well as the significance and the envisaged consequences of such processing for the data subject.
> 3. Where the controller intends to further process the personal data for a purpose other than that for which the personal data were collected, the controller shall provide the data subject prior to that further processing with information on that other purpose and with any relevant further information as referred to in paragraph 2.
> 4. Paragraphs 1, 2 and 3 shall not apply where and insofar as the data subject already has the information.
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

<!-- aegis:purity: own_reg=GDPR; demoted=0; core_cross_mentions=0 -->