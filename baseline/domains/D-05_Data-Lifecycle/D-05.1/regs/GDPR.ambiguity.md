# D-05.1 — Relevant Ambiguity (GDPR)

> Part 4 ambiguity analysis for GDPR, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## GDPR
##### Art. 5(1)(a) — Lawfulness, fairness, transparency
**Clause: GDPR-CL01** | type: principle | obligatedParty: CONTROLLER | obligationType: CONTINUOUS
**Control anchors:** CSF: GV.OC-03, GV.PO-01, GV.PO-02, PR.AA-02 · PF 1.1: GV.PO-P5, CM.PO-P1, GV.PO-P1, CM.AW-P1, CM.AW-P3 · AI RMF: — · from `SR-GDPR-026`, `SR-GDPR-065` (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
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
**Control anchors:** CSF: ID.AM-08, ID.AM-03, GV.OC-03, GV.PO-01 · PF 1.1: CT.PO-P4, CT.DP-P4, ID.RA-P3, GV.PO-P5, CM.PO-P1, GV.PO-P1 · AI RMF: — · from `SR-GDPR-025`, `SR-GDPR-026` (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
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
##### Art. 5(1)(c) — Data minimisation
**Clause: GDPR-CL03** | type: principle | obligatedParty: CONTROLLER | obligationType: CONTINUOUS
**Control anchors:** CSF: PR.DS-10, ID.AM-08, PR.AA-02, PR.PS-01, ID.AM-03, GV.SC-04 · PF 1.1: CT.DM-P3, CM.AW-P5, PR.AC-P6, CT.DP-P4, CT.PO-P4, ID.RA-P3, CT.DM-P5, CT.DM-P4, ID.DE-P3 · AI RMF: — · from `SR-GDPR-006`, `SR-GDPR-010`, `SR-GDPR-013`, +4 more (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
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
**Control anchors:** CSF: PR.DS-01, ID.AM-08, PR.DS-10 · PF 1.1: CT.DM-P1, CT.DM-P3, CM.AW-P5 · AI RMF: — · from `SR-GDPR-005`, `SR-GDPR-006` (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
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
**Control anchors:** CSF: PR.DS-01, PR.DS-10, ID.AM-08, ID.RA-01, PR.PS-02, PR.IR-04, PR.DS-11, RC.RP-04, PR.PS-06 · PF 1.1: PR.DS-P1, PR.PO-P3, CT.DM-P1, CT.DM-P3, GV.MT-P3, CT.DM-P10, GV.PO-P2, CT.PO-P4 · AI RMF: — · from `SR-GDPR-001`, `SR-GDPR-005`, `SR-GDPR-007`, +2 more (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
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
##### Art. 6(1)(a) — Consent
**Clause: GDPR-CL08** | type: lawfulness base | obligatedParty: CONTROLLER | obligationType: PER-PURPOSE (continuous)
**Control anchors:** CSF: GV.OC-03, GV.PO-01, PR.AA-02 · PF 1.1: GV.PO-P5, CM.PO-P1, GV.PO-P1, CT.PO-P3, CM.AW-P2 · AI RMF: — · from `SR-GDPR-026`, `SR-GDPR-051` (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
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
**Control anchors:** CSF: GV.OC-03, GV.PO-02 · PF 1.1: GV.PO-P5, CT.PO-P1 · AI RMF: — · from `SR-GDPR-027` (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
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
**Control anchors:** CSF: GV.OC-03, GV.PO-02 · PF 1.1: GV.PO-P5, CT.PO-P1 · AI RMF: — · from `SR-GDPR-027` (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
**Berry anchor:** §5.1 (`necessary`, `legal obligation`).
**Instance 1 — VAG / S2 / `legal obligation to which the controller is subject`**
`legal obligation` is bounded (must be Union or Member State law) per Art. 6(3) but the `necessary` qualifier is still open. Art. 6(3) specifies the form of the legal basis but not the necessary-processing test. S2 because Art. 6(3) partially anchors the reading.
---
##### Art. 6(1)(d) — Vital interests
**Clause: GDPR-CL11** | type: lawfulness base | obligatedParty: CONTROLLER | obligationType: PER-INCIDENT
**Control anchors:** CSF: GV.OC-03, GV.PO-02 · PF 1.1: GV.PO-P5, CT.PO-P1 · AI RMF: — · from `SR-GDPR-027` (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
**Berry anchor:** §3.3.1 (`vital interests` polysemy), §5.1 (`necessary`).
**Instance 1 — POLY / S2 / `vital interests`**
`vital interests` is undefined. Recital 46 attempts to fix as `life-critical` situations; EDPB Guidelines interpret as life OR health (interchangeable). S2 because Recital 46 (non-binding) constrains the reading to life-critical emergencies.
---
##### Art. 6(1)(e) — Public interest / official authority
**Clause: GDPR-CL12** | type: lawfulness base | obligatedParty: CONTROLLER (public authority) | obligationType: PER-TASK
**Control anchors:** CSF: GV.OC-03, GV.PO-02 · PF 1.1: GV.PO-P5, CT.PO-P1 · AI RMF: — · from `SR-GDPR-027` (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
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
**Control anchors:** CSF: GV.OC-03, GV.PO-02 · PF 1.1: GV.PO-P5, CT.PO-P1 · AI RMF: — · from `SR-GDPR-027` (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
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
##### Art. 6(4) — Compatibility test for further processing
**Clause: GDPR-CL14** | type: cross-cutting | obligatedParty: CONTROLLER | obligationType: PER-PURPOSE-CHANGE
**Control anchors:** CSF: ID.AM-08, ID.AM-03 · PF 1.1: CT.PO-P4, CT.DP-P4, ID.RA-P3 · AI RMF: — · from `SR-GDPR-025` (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
**Berry anchor:** §5.4.7 (5-element list with `inter alia`).
**Instance 1 — COORD+VAG / S2 / `inter alia` + 5 elements**
The 5 elements (a)–(e) are connected by `inter alia` (Berry §5.1 open-list pattern). The `necessary and proportionate measure in a democratic society` clause in the precondition is borrowed from ECHR Art. 8(2) terminology but its interpretation under GDPR is not anchored.
S2 because the 5 factors converge on the same controller practice (compatibility assessment), even though the threshold is qualitative.
---
### Article 7 — Conditions for consent
#### Verbatim (with highlighting)
> **Article 7**
> **Conditions for consent**
>
> 1. Where processing is based on consent, the controller shall be able to demonstrate that the data subject has consented to processing of his or her personal data.
> 2. If the data subject's consent is given in the context of a written declaration which also concerns other matters, the request for consent shall be presented in a manner which is clearly distinguishable from the other matters, in an intelligible and easily accessible form, using clear and plain language. Any part of such a declaration which constitutes an infringement of this Regulation shall not be binding.
> 3. The data subject shall have the right to withdraw his or her consent at any time. The withdrawal of consent shall not affect the lawfulness of processing based on consent before its withdrawal. Prior to giving consent, the data subject shall be informed thereof. It shall be as easy to withdraw as to give consent.
> 4. When assessing whether consent is freely given, **utmost account** shall be taken of whether, inter alia, the performance of a contract, including the provision of a service, is conditional on consent to the processing of personal data that is **not necessary** for the performance of that contract.
#### Clause breakdown
##### Art. 9(1) — General prohibition on special-category processing
**Clause: GDPR-CL21** | type: principle (sensitive data) | obligatedParty: CONTROLLER | obligationType: PER-CATEGORY
**Control anchors:** CSF: GV.OC-03, ID.AM-08, PR.AA-02 · PF 1.1: GV.PO-P5, CT.DP-P2, ID.RA-P3, CT.PO-P3 · AI RMF: — · from `SR-GDPR-028`, `SR-GDPR-053` (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
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
**Control anchors:** CSF: GV.OC-03, ID.AM-08, PR.AA-02 · PF 1.1: GV.PO-P5, CT.DP-P2, ID.RA-P3, CT.PO-P3 · AI RMF: — · from `SR-GDPR-028`, `SR-GDPR-053` (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
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
**Control anchors:** CSF: — · PF 1.1: — · AI RMF: — (no consuming SR in dashboard mappings)
**Berry anchor:** §5.1 (`substantial public interest`, `proportionate`, `essence of the right to data protection`, `suitable and specific measures`).
**Instance 1 — VAG / S3 / `substantial public interest`**
`substantial public interest` inherits the Art. 6(1)(e) `public interest` ambiguity plus the `substantial` qualifier. The clause cross-references Charter Art. 52(1) via `essence of the right`.
S3 — same family of ambiguity as Art. 6(1)(e), but more severe because `substantial` is undefined.
---
##### Art. 9(2)(j) — Research/statistics/archiving (with Art. 89(1) safeguards)
**Clause: GDPR-CL24** | type: lawfulness base (special category, research) | obligatedParty: CONTROLLER | obligationType: PER-MEMBER-STATE-LAW
**Control anchors:** CSF: — · PF 1.1: — · AI RMF: — (no consuming SR in dashboard mappings)
**Berry anchor:** §5.1 (`archiving purposes in the public interest`, `proportionate`, `essence`).
The clause cross-references Art. 89(1) for the substantive safeguards (pseudonymisation, no decisions about data subjects, etc.). The Art. 89(1) reference provides partial anchoring but does not define `archiving`.
---
### Article 10 — Criminal convictions and offences
#### Verbatim
> **Article 10**
>
> Processing of personal data relating to criminal convictions and offences shall be carried out only under the control of official authority or when the processing is authorised by Union or Member State law providing for appropriate safeguards for the rights and freedoms of data subjects. Any **comprehensive register** of criminal convictions shall be kept only under the control of official authority.
#### Clause breakdown
##### Art. 10 — Processing of criminal convictions
**Clause: GDPR-CL25** | type: principle (criminal data) | obligatedParty: CONTROLLER (official authority only for comprehensive registers) | obligationType: PER-RECORD
**Control anchors:** CSF: — · PF 1.1: — · AI RMF: — (no consuming SR in dashboard mappings)
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
##### Art. 12(6) — Identity verification for requests
**Clause: GDPR-RT04** | type: data-subject-facing | obligatedParty: CONTROLLER | obligationType: PER-REQUEST
**Control anchors:** CSF: PR.AA-03, PR.AA-02, ID.AM-08, GV.PO-02 · PF 1.1: PR.AC-P6, PR.AC-P3, CT.DP-P4, GV.PO-P1, CM.PO-P1 · AI RMF: — · from `SR-GDPR-009`, `SR-GDPR-010`, `SR-GDPR-067` (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
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
##### Art. 16 — Rectification right
**Clause: GDPR-RT12** | type: data subject right (rectification) | obligatedParty: CONTROLLER | obligationType: PER-REQUEST
**Control anchors:** CSF: PR.DS-10, ID.AM-08, RS.CO-02 · PF 1.1: CT.DM-P3, CM.AW-P5 · AI RMF: — · from `SR-GDPR-006`, `SR-GDPR-022` (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
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
**Control anchors:** CSF: PR.DS-10, ID.AM-08, RS.CO-02 · PF 1.1: CT.DM-P3, CM.AW-P5 · AI RMF: — · from `SR-GDPR-006`, `SR-GDPR-022` (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
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
##### Art. 25(1) — Privacy by design
**Clause: GDPR-CP02** | type: design obligation | obligatedParty: CONTROLLER | obligationType: CONTINUOUS
**Control anchors:** CSF: PR.PS-01, ID.AM-08, PR.PS-06, PR.DS-01 · PF 1.1: CT.DP-P4, CT.PO-P4, GV.PO-P2, CT.DP-P2 · AI RMF: — · from `SR-GDPR-013`, `SR-GDPR-039`, `SR-GDPR-040`, +1 more (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
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
**Control anchors:** CSF: PR.PS-01, ID.AM-08, PR.PS-06 · PF 1.1: CT.DP-P4, CT.PO-P4, GV.PO-P2 · AI RMF: — · from `SR-GDPR-013`, `SR-GDPR-039`, `SR-GDPR-041` (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
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
##### Art. 32(1) — Security measures (open list)
**Clause: GDPR-CP15** | type: security | obligatedParty: CONTROLLER + PROCESSOR | obligationType: CONTINUOUS
**Control anchors:** CSF: PR.DS-01, PR.DS-10, PR.DS-02, PR.IR-01, PR.IR-03, ID.RA-01, PR.PS-02, ID.RA-05, ID.IM-02, PR.AA-05, PR.AA-06, PR.AT-02, DE.CM-01, DE.CM-09, RS.MA-02, RS.MI-01, RS.MI-02, PR.IR-04, PR.DS-11, RC.RP-04, GV.SC-03, GV.SC-04, DE.CM-06, PR.PS-06, ID.AM-08 · PF 1.1: PR.DS-P1, PR.PO-P3, PR.DS-P2, PR.AC-P5, CT.DP-P2, GV.MT-P3, CT.DM-P10, ID.RA-P3, ID.RA-P5, PR.AC-P1, PR.AC-P2, CT.PO-P1, GV.AT-P2, GV.MT-P5, CM.AW-P7, PR.PO-P7, ID.DE-P5, CT.DM-P9, GV.PO-P2, CT.PO-P4 · AI RMF: — · from `SR-GDPR-001`, `SR-GDPR-002`, `SR-GDPR-003`, +11 more (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
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
<!-- aegis:control-anchors: generated by scripts/uniformize_control_anchors.py from baseline/MAPPINGS/sr_control_mappings; not part of the verbatim Part 4 body -->
