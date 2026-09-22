# D-09.1 — Relevant Ambiguity (GDPR)

> Part 4 ambiguity analysis for GDPR, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## GDPR
##### Art. 5(1)(a) — Lawfulness, fairness, transparency
**Clause: GDPR-CL01** | type: principle | obligatedParty: CONTROLLER | obligationType: CONTINUOUS
**Berry anchor:** §3.3.5 (vagueness), §5.1 (lists `lawful`, `fair`).
**Instance 1 — VAG / S3 / `lawful`, `fair`, `transparent`**
Three conjunctive vague adjectives. Each is inquiry-resistant:
- `lawful` — refer to Art. 6 (which is itself ambiguous; see Clause-CL06)
- `fair` — undefined; Recital 47 attempts to fix but is non-binding; balance of interests test
- `transparent` — Art. 12 attempts to fix at the implementation level (concise, easily accessible, plain language)
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | `fair` = no deception about purpose or use; balance-of-interests test on data-subject impact. | Recital 47 (non-binding); ICO fairness guidance. |
| R2 | `fair` = no significant detrimental consequence for the data subject unless proportionate and transparent. | CJEU Rīgas satiksme (C-13/16). |
| R3 | `fair` = a procedural requirement (notice, consent mechanism, complaint channel). | EDPB Guidelines 04/2019 on transparency. |
R1 vs R2 yield materially distinct compliance obligations (R1 requires substantive impact assessment; R2 requires procedural safeguards).
---
##### Art. 5(1)(b) — Purpose limitation
**Clause: GDPR-CL02** | type: principle | obligatedParty: CONTROLLER | obligationType: CONTINUOUS
**Berry anchor:** §5.1 (`specified`, `explicit`, `legitimate`), §5.4.7 (coordination).
**Instance 1 — VAG / S2 / `specified`, `explicit`, `legitimate`**
Three conjunctive qualifiers on the `purposes` noun. Berry §5.5: structural parallelism invites distinct readings, but the clause is anchored by Art. 6 (lawful bases) and Art. 13/14 (information to data subjects), which require purpose specification in the privacy notice.
**Instance 2 — COORD / S2 / `incompatible`**
`not further processed in a manner that is incompatible with those purposes` — Art. 6(4) provides a 6-factor compatibility test, anchoring the reading. S2 because Art. 6(4) provides partial disambiguation, but the test is itself qualitative.
**Instance 3 — VAG / S3 / `public interest, scientific or historical research purposes or statistical purposes`**
The 5 enumerated sub-purposes are disjunctive (OR). The boundary between them (especially `historical research` vs `archiving purposes in the public interest`) is undefined in Art. 5 and partially anchored by Art. 89(1) (research-specific safeguards).
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | The 5 purposes are exhaustive; further processing under any is compatible; other purposes require fresh consent. | Strict textual reading. |
| R2 | The 5 purposes are illustrative; further processing under analogous purposes is compatible if Art. 6(4) factors are met. | Art. 6(4) general compatibility test. |
R1 vs R2 yield materially distinct compliance obligations (R1 requires fresh consent for analogous processing; R2 does not).
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
##### Art. 6(1)(b) — Contract performance
**Clause: GDPR-CL09** | type: lawfulness base | obligatedParty: CONTROLLER | obligationType: PER-CONTRACT
**Berry anchor:** §5.1 (`necessary`).
**Instance 1 — VAG / S3 / `necessary for the performance of a contract`**
`necessary` is the recurring vague term. `or in order to take steps at the request of the data subject prior to entering into a contract` extends the basis to pre-contractual steps. The boundary between `necessary for performance` and `optional but useful for performance` is undefined.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | `necessary` = objectively required for the contract to function (e.g. shipping address for delivery). | EDPB Guidelines 02/2019 on Art. 6(1)(b). |
| R2 | `necessary` = reasonably incidental to the contract (e.g. fraud detection). | EDPB Guidelines 02/2019. |
| R3 | `necessary` = any processing that the contract reasonably anticipates. | Loose reading. |
R1 vs R3 yield materially distinct compliance obligations (R1 requires per-processing purpose justification; R3 allows blanket contract-based processing).
---
##### Art. 6(1)(c) — Legal obligation
**Clause: GDPR-CL10** | type: lawfulness base | obligatedParty: CONTROLLER | obligationType: PER-OBLIGATION
**Berry anchor:** §5.1 (`necessary`, `legal obligation`).
**Instance 1 — VAG / S2 / `legal obligation to which the controller is subject`**
`legal obligation` is bounded (must be Union or Member State law) per Art. 6(3) but the `necessary` qualifier is still open. Art. 6(3) specifies the form of the legal basis but not the necessary-processing test. S2 because Art. 6(3) partially anchors the reading.
---
##### Art. 6(1)(d) — Vital interests
**Clause: GDPR-CL11** | type: lawfulness base | obligatedParty: CONTROLLER | obligationType: PER-INCIDENT
**Berry anchor:** §3.3.1 (`vital interests` polysemy), §5.1 (`necessary`).
**Instance 1 — POLY / S2 / `vital interests`**
`vital interests` is undefined. Recital 46 attempts to fix as `life-critical` situations; EDPB Guidelines interpret as life OR health (interchangeable). S2 because Recital 46 (non-binding) constrains the reading to life-critical emergencies.
---
##### Art. 6(1)(e) — Public interest / official authority
**Clause: GDPR-CL12** | type: lawfulness base | obligatedParty: CONTROLLER (public authority) | obligationType: PER-TASK
**Berry anchor:** §5.1 (`necessary`, `task carried out in the public interest`), §3.3.1 (`official authority` polysemy).
**Instance 1 — VAG / S3 / `task carried out in the public interest or in the exercise of official authority`**
The disjunctive is wide. `Public interest` is undefined at EU level; Member State law determines it per Art. 6(2). `Official authority` typically requires a public-law empowerment but the boundary with `public interest` (private entities performing public-interest tasks) is contested.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Applies only to public-sector controllers. | Art. 6(1) final subparagraph excludes public authorities from (f) but not (e). |
| R2 | Applies also to private-sector controllers explicitly entrusted with public-interest tasks (e.g. healthcare providers under contract). | EDPB Guidelines on Art. 6(1)(e). |
| R3 | Applies to any controller with a `public interest` mandate, including NGOs. | Loose reading. |
R1 vs R2 yield materially distinct compliance obligations (R1 limits applicability; R2 expands it to contracted private entities).
---
##### Art. 6(1)(f) — Legitimate interests
**Clause: GDPR-CL13** | type: lawfulness base | obligatedParty: CONTROLLER (non-public) | obligationType: PER-PURPOSE
**Berry anchor:** §3.3.1 (`legitimate interests` polysemy), §5.1 (`necessary`).
**Instance 1 — POLY+VAG / S3 / `legitimate interests` + balancing test**
`legitimate interests` is undefined. The clause includes a built-in balancing test: `except where such interests are overridden by the interests or fundamental rights and freedoms of the data subject`. The Recital 47 attempt to fix the meaning of `legitimate` is non-binding. The `in particular where the data subject is a child` sentence triggers Art. 8 protection.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | `Legitimate interest` = any lawful commercial interest (broad). | Pre-GDPR EU law (Directive 95/46/EC Art. 7(f)). |
| R2 | `Legitimate interest` = a narrow set of recognised interests (fraud prevention, IT security, internal administration). | EDPB Guidelines on legitimate interests. |
| R3 | `Legitimate interest` = requires positive identification against a closed list. | Strict reading. |
R1 vs R3 yield materially distinct compliance obligations (R1 allows any commercial interest; R3 requires justification against a closed list).
**Instance 2 — POLY / S2 / `in particular where the data subject is a child`**
Children are singled out as requiring additional protection, but the operationalisation is undefined. Art. 8 (parental consent) anchors partially; the balancing test for legitimate interests in children's cases remains qualitative.
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
##### Art. 9(1) — General prohibition on special-category processing
**Clause: GDPR-CL21** | type: principle (sensitive data) | obligatedParty: CONTROLLER | obligationType: PER-CATEGORY
**Berry anchor:** §3.3.1 (polysemy of each special category), §5.4.7 (long OR enumeration).
**Instance 1 — POLY+COORD / S3 / enumerated categories**
9 categories connected by commas and `and`: `racial or ethnic origin, political opinions, religious or philosophical beliefs, trade union membership, and ... genetic data, biometric data ..., data concerning health or data concerning ... sex life or sexual orientation`. Each term has a poly reference (Art. 4(13)–(15)) but the boundaries are contested.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Biometric data within scope only when used `for the purpose of uniquely identifying` (Art. 9(1) caveat). | Strict text. |
| R2 | Biometric data within scope regardless of purpose; the caveat is descriptive not limiting. | Loose reading. |
| R3 | Sex life/sexual orientation includes inferred orientation (algorithmic derivation). | LOI Guidelines on processing employee data 2022. |
R1 vs R2 yield materially distinct biometric-processing scope.
---
##### Art. 9(2)(a) — Explicit consent for special categories
**Clause: GDPR-CL22** | type: lawfulness base (special category) | obligatedParty: CONTROLLER | obligationType: PER-CATEGORY-CONSENT
**Berry anchor:** §5.1 (`explicit` vs `specific` — consent Art. 4(11) requires `specific`; Art. 9(2)(a) adds `explicit`).
**Instance 1 — POLY / S3 / `explicit consent` vs `specific consent`**
The Art. 9(2)(a) consent requires `explicit` (a stronger qualifier than the Art. 4(11) `specific`). The boundary between `explicit` and `specific` is undefined; EDPB Guidelines 05/2020 attempt to fix but do not exhaust the gap. S3 because the standard of consent collection differs materially.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | `Explicit` = written or otherwise documented (not oral). | EDPB Guidelines 05/2020. |
| R2 | `Explicit` = requires a separate, unambiguous statement (not bundled). | EDPB Guidelines 05/2020. |
| R3 | `Explicit` = both written and separate. | Strict reading. |
R1 vs R3 yield materially distinct consent-collection UI.
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
##### Art. 23(1) — Permissible restriction grounds
**Clause: GDPR-RT20** | type: principle (restrictions scope) | obligatedParty: MEMBER STATE | obligationType: PER-RESTRICTION
**Berry anchor:** §5.1 (`essence of the fundamental rights and freedoms`, `necessary and proportionate`), §5.4.7 (10-element OR-list).
**Instance 1 — VAG / S3 / `essence of the fundamental rights and freedoms`**
`Essence` is Charter Art. 52(1) terminology. CJEU case law (Schrems I/II, Digital Rights Ireland) uses `essence` as a hard-test threshold but does not specify the operational test. S3 because Member State restrictions on Charter rights depend on the essence-test being met.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | `Essence` = the absolute core of the right (cannot be touched). | CJEU Charter interpretation. |
| R2 | `Essence` = the proportionality balance of the right. | Loose reading. |
R1 vs R2 yield materially distinct restriction-scrutiny standards.
**Instance 2 — COORD / S2 / `(a) OR (b) OR (c) OR ... (j)`**
10 disjunctive grounds (Berry §5.4.7 menu-card pattern). S2 because all 10 grounds converge on the same scrutiny mechanism.
---
### Chapter III synthesis
#### Counts
| Category | Instances | Clauses affected |
|---|---|---|
| VAG | 27 | 20 / 20 |
| POLY | 11 | 11 / 20 |
| COORD | 12 | 12 / 20 |
| SCOPE-Q | 3 | 3 / 20 |
| **Total** | **53** | **20 / 20** |
| Severity | Instances |
|---|---|
| S1 — Low | 0 |
| S2 — Medium | 34 |
| S3 — High | 19 |
#### Recurring patterns
- `Reasonable` (Berry-flagged) appears in 8 of 20 clauses — dominant vague term of Chapter III.
- 1-month + 2-month temporal pair (Art. 12(3)) is the only hard numeric anchor in the chapter; all other timelines are vague.
#### Cross-clause structural observations
#### Anti-pattern notes for downstream files
- Chapter IV inherits Chapter III rights via Art. 24(1) "implement appropriate technical and organisational measures" + Art. 25 by-design. `Appropriate measures` for rights-exercise includes consent-collection UIs, SAR portals, rectification workflows.
- Chapter V transfer mechanisms do not create new Chapter III rights but the Art. 15(2) right to be informed of transfer safeguards cross-references Chapter V.
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
##### Art. 27(2)(a) — Occasional-processing exception
**Clause: GDPR-CP06** | type: extraterritoriality exception | obligatedParty: NON-EU CONTROLLER/PROCESSOR | obligationType: PER-PROCESSING-ACTIVITY
**Berry anchor:** §5.1 (`occasional`, `large scale`, `unlikely`).
**Instance 1 — VAG / S3 / `occasional`, `large scale`, `unlikely to result in a risk`**
Three inquiry-resistant qualifiers combined with AND. The exception requires all three to fail (i.e., occasional AND small-scale AND low-risk). The boundary of each is undefined.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | `Occasional` = not regular/periodic; one-off processing. | EDPB Guidelines 3/2018. |
| R2 | `Occasional` = not in the controller's core business activity. | Recital 23 (non-binding). |
R1 vs R2 yield materially distinct representative-designation policies.
**Instance 2 — SCOPE-Q / S2 / `large scale`**
`large scale` is undefined; EDPB Guidelines 9/2022 (DPO designation context) attempt to fix factors (number of data subjects, volume of data, geographic range). S2 because the factors converge on the same compliance practice (large-scale determination documentation).
---
### Article 28 — Processor
#### Verbatim (with highlighting)
> **Article 28**
> **Processor**
>
> 1. Where processing is to be carried out on behalf of a controller, the controller shall use only processors providing **sufficient guarantees** to implement **appropriate technical and organisational measures** in such a manner that processing will meet the requirements of this Regulation and ensure the protection of the rights of the data subject.
> 2. The processor shall not engage another processor without **prior specific or general written authorisation** of the controller. In the case of general written authorisation, the processor shall inform the controller of any intended changes concerning the addition or replacement of other processors, thereby giving the controller the opportunity to object to such changes.
> 3. Processing by a processor shall be governed by a **contract or other legal act** under Union or Member State law, that is binding on the processor with regard to the controller and that sets out the subject-matter and duration of the processing, the nature and purpose of the processing, the type of personal data and categories of data subjects and the obligations and rights of the controller. That contract or other legal act shall stipulate, in particular, that the processor:
> (a) processes the personal data only on **documented instructions** from the controller (...)
> (b) ensures that persons authorised to process the personal data have committed themselves to **confidentiality** or are under an **appropriate statutory obligation of confidentiality**;
> (c) takes all measures required pursuant to Article 32;
> (d) respects the conditions referred to in paragraphs 2 and 4 for engaging another processor;
> (e) taking into account the nature of the processing, assists the controller by appropriate technical and organisational measures, insofar as this is possible, for the fulfilment of the controller's obligation to respond to requests for exercising the data subject's rights laid down in Chapter III;
> (f) assists the controller in ensuring compliance with the obligations pursuant to Articles 32 to 36 taking into account the nature of processing and the information available to the processor;
> (g) at the choice of the controller, **deletes or returns all the personal data** to the controller after the end of the provision of services relating to processing, and **deletes existing copies** unless Union or Member State law requires storage of the personal data;
> (h) makes available to the controller all information necessary to demonstrate compliance with the obligations laid down in this Article and allow for and contribute to **audits, including inspections**, conducted by the controller or another auditor mandated by the controller.
#### Clause breakdown
##### Art. 30(1)+(2) — Records content
**Clause: GDPR-CP12** | type: documentation | obligatedParty: CONTROLLER + PROCESSOR | obligationType: CONTINUOUS
**Berry anchor:** §5.1 (`where possible` × 2), §5.4.7 (closed AND-list).
**Instance 1 — VAG / S2 / `where possible` × 2**
Soft hedge on retention-period documentation and security-measure documentation. `Where possible` defers to controller judgement. S2 because the same documentation practice applies.
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
##### Art. 38(2) — DPO resources
**Clause: GDPR-CP26** | type: DPO independence | obligatedParty: CONTROLLER + PROCESSOR | obligationType: CONTINUOUS
**Berry anchor:** §5.1 (`necessary`).
**Instance 1 — VAG / S2 / `resources necessary`**
Inherits Art. 28(1) `sufficient` ambiguity. S2 because the same compliance practice (provide-adequate-resources) applies.
---
##### Art. 38(6) — No conflict of interests
**Clause: GDPR-CP27** | type: DPO independence | obligatedParty: CONTROLLER + PROCESSOR | obligationType: CONTINUOUS
**Berry anchor:** §5.1 (`conflict of interests`).
**Instance 1 — VAG / S2 / `conflict of interests`**
Undefined; EDPB Guidelines 3/2018 attempt to fix factors (e.g. DPO cannot also be CISO in some configurations). S2 because the factors converge on the same DPO-role separation.
---
### Article 39 — Tasks of the DPO
#### Verbatim (with highlighting)
> **Article 39**
> **Tasks of the data protection officer**
>
> 1. The data protection officer shall have at least the following tasks:
> (a) to **inform and advise** the controller or the processor and the employees who carry out processing of their obligations pursuant to this Regulation and to other Union or Member State data protection provisions;
> (b) to monitor compliance with this Regulation, with other Union or Member State data protection provisions and with the policies of the controller or processor in relation to the protection of personal data, including the **assignment of responsibilities**, **awareness-raising and training of staff** involved in processing operations, and the related audits;
> (c) to provide advice where requested as regards the data protection impact assessment and monitor its performance pursuant to Article 35;
> (d) to cooperate with the supervisory authority;
> (e) to act as the contact point for the supervisory authority on issues relating to processing, including the prior consultation referred to in Article 36, and to consult, where appropriate, with regard to any other matter.
> 2. The data protection officer shall in the performance of his or her tasks have due regard to the **risk associated with processing operations**, taking into account the nature, scope, context and purposes of processing.
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

- ADM (Art. 22) overlaps with AI Act Art. 13 — Chapter III Art. 22(3) `meaningful information about the logic` is the foundational obligation that the AI Act operationalises for high-risk AI.


### from regs/GDPR.ambiguity.md

1. **Art. 12 is the procedural backbone.** All other rights (Art. 13–22) depend on Art. 12's response-time, identity-verification, and refusal grounds.
2. **Art. 13/14 split** — collection-source vs third-party-source information duties are structurally parallel but with different timing rules (immediate vs 1-month). The third-party-source timing is the more lenient and more often waived.
3. **Art. 15–22 cascade.** Each right (access, rectification, erasure, restriction, portability, object, ADM) inherits Art. 12's procedural rules and Art. 5(1)(d) accuracy / Art. 5(1)(c) minimisation anchors. Cross-clause implementations can reuse components.
4. **Art. 22 ADM** — the most software-impact-relevant right in GDPR, with direct overlap to AI Act's high-risk transparency requirements. Cross-regulatory coordination required.
5. **Art. 23 restrictions** — the Member State's escape valve from Chapter III. The `essence` test (Charter Art. 52(1)) is the constitutional backstop but its operationalisation is CJEU-driven.

### from regs/GDPR.ambiguity.md

- Cross-regulation: DORA Art. 28(8) ICT third-party risk management overlaps with GDPR Chapter V for financial entities transferring data to non-EU ICT providers.


<!-- aegis:purity: own_reg=GDPR; demoted=3; core_cross_mentions=0 -->