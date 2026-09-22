# D-10.3 — Relevant Ambiguity (GDPR)

> Part 4 ambiguity analysis for GDPR, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## GDPR
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
##### Art. 35(1) — DPIA trigger
**Clause: GDPR-CP21** | type: impact assessment | obligatedParty: CONTROLLER | obligationType: PER-PROCESSING (pre-launch)
**Berry anchor:** §5.1 (`new technologies`, `likely`, `high risk`), §3.3.1 (`new` polysemy).
**Instance 1 — POLY+VAG / S3 / `new technologies` + `high risk`**
`New technologies` is the recurring time-dependent vague phrase (cf. Art. 25 `state of the art`). Was cloud `new` in 2018? Is generative AI `new` in 2026? EDPB Guidelines 4/2019 attempt to fix but `new` is inherently time-relative.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | `New technologies` = technologies not widely deployed in the industry at time of assessment. | EDPB Guidelines 4/2019. |
| R2 | `New technologies` = listed in supervisory-authority Art. 35(4) lists. | EDPB reading. |
R1 vs R2 yield materially distinct DPIA-trigger classification.
---
##### Art. 35(7) — DPIA content
**Clause: GDPR-CP22** | type: impact assessment content | obligatedParty: CONTROLLER | obligationType: PER-DPIA
**Berry anchor:** §5.1 (`systematic description`, `necessity and proportionality`).
**Instance 1 — POLY / S2 / `necessity and proportionality`**
Three different `necessity` senses across GDPR (5(1)(c) data-minimisation, 6(1)(b) contract, 35(7)(b) DPIA) — same term, different operationalisation. S2 because Art. 35(7)(b) is internally anchored.
---
### Article 36 — Prior consultation
#### Verbatim (with highlighting)
> **Article 36**
> **Prior consultation**
>
> 1. The controller shall consult the supervisory authority **prior to processing** where a data protection impact assessment under Article 35 indicates that the processing would result in a **high risk** in the absence of measures taken by the controller to mitigate the risk.
> 2. Where the supervisory authority is of the opinion that the intended processing referred to in paragraph 1 would infringe this Regulation, in particular where the controller has insufficiently identified or mitigated the risk, the supervisory authority shall, **within period of up to eight weeks** of receipt of the request for consultation, provide written advice to the controller and, where applicable to the processor (...).
#### Clause breakdown

<!-- aegis:purity: own_reg=GDPR; demoted=0; core_cross_mentions=0 -->