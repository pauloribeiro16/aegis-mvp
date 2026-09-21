# D-01.2 — Relevant Ambiguity (GDPR)

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
##### Art. 32(2) — Risk-enumeration for security assessment
**Clause: GDPR-CP16** | type: security risk assessment | obligatedParty: CONTROLLER + PROCESSOR | obligationType: CONTINUOUS
**Berry anchor:** §5.4.7 (`accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to` — 5-way OR chain).
**Instance 1 — COORD / S3 / 5-way OR**
The 5-event enumeration (Berry §5.4.7 menu-card pattern). Each OR is inclusive; the OR-chain admits ≥5 distinct threat-model scopes.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Any of the 5 events triggers the security assessment obligation. | Strict reading. |
| R2 | The 5 events are illustrative; controller determines in-scope events. | Loose reading. |
R1 vs R2 yield materially distinct threat-modelling scope.
---
### Article 33 — Breach notification to supervisory authority
#### Verbatim (with highlighting)
> **Article 33**
> **Notification of a personal data breach to the supervisory authority**
>
> 1. In the case of a personal data breach, the controller shall **without undue delay** and, **where feasible**, **not later than 72 hours after having become aware of it**, notify the personal data breach to the supervisory authority competent in accordance with Article 55, unless the personal data breach is **unlikely to result in a risk** to the rights and freedoms of natural persons. Where the notification to the supervisory authority is not made within 72 hours, it shall be accompanied by reasons for the delay.
> 2. The processor shall notify the controller **without undue delay** after becoming aware of a personal data breach.
> 3. The notification referred to in paragraph 1 shall at least:
> (a) describe the nature of the personal data breach including **where possible**, the categories and **approximate number** of data subjects concerned and the categories and approximate number of personal data records concerned;
> (b) communicate the name and contact details of the data protection officer or other contact point where more information can be obtained;
> (c) describe the **likely consequences** of the personal data breach;
> (d) describe the measures taken or proposed to be taken by the controller to address the personal data breach, including, where appropriate, measures to mitigate its possible adverse effects.
#### Clause breakdown

<!-- aegis:purity: own_reg=GDPR; demoted=0; core_cross_mentions=0 -->

