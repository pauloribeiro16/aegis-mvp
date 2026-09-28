# D-04.3 — Relevant Ambiguity (GDPR)

> Part 4 ambiguity analysis for GDPR, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## GDPR
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
##### Art. 11(1) — No identification obligation
**Clause: GDPR-CL26** | type: principle (identification exemption) | obligatedParty: CONTROLLER | obligationType: PER-REQUEST
**Control anchors:** CSF: PR.AA-03, PR.AA-02, RS.CO-02, ID.AM-08 · PF 1.1: PR.AC-P6, PR.AC-P3, CM.AW-P5, CT.DM-P3 · AI RMF: — · from `SR-GDPR-009`, `SR-GDPR-022` (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
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
##### Art. 14(5)(b) — Disproportionate effort exception
**Clause: GDPR-RT08** | type: information duty (exception) | obligatedParty: CONTROLLER | obligationType: PER-CASE
**Control anchors:** CSF: — · PF 1.1: — · AI RMF: — (no consuming SR in dashboard mappings)
**Berry anchor:** §5.1 (`disproportionate effort`).
**Instance 1 — VAG / S3 / `proves impossible or would involve a disproportionate effort`**
`disproportionate effort` is the recurring vague phrase. Recital 62 attempts to fix as cost-vs-risk assessment. S3 because the exception is widely used to skip Article 14 notification in practice (e.g. large-scale behavioural advertising).
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Exception applies narrowly to research/archiving; controllers must demonstrate efforts. | Recital 62 (non-binding). |
| R2 | Exception applies broadly; controllers judge what is disproportionate. | Industry reading. |
R1 vs R2 yield materially distinct notification workflows in research/archiving operations.
---
### Article 15 — Right of access
#### Verbatim (with highlighting)
> **Article 15**
> **Right of access by the data subject**
>
> 1. The data subject shall have the right to obtain from the controller confirmation as to whether or not personal data concerning him or her are being processed, and, where that is the case, access to the personal data and the following information:
> (a) the purposes of the processing;
> (b) the categories of personal data concerned;
> (c) the recipients or categories of recipient to whom the personal data have been or will be disclosed (...);
> (d) where possible, the envisaged period for which the personal data will be stored (...);
> (e) the existence of the right to request from the controller rectification or erasure (...);
> (f) the right to lodge a complaint with a supervisory authority;
> (g) where the personal data are not collected from the data subject, any available information as to their source;
> (h) the existence of automated decision-making (...) meaningful information about the logic involved (...)
> 2. Where personal data are transferred to a third country or to an international organisation, the data subject shall have the right to be informed of the appropriate safeguards pursuant to Article 46 relating to the transfer.
> 3. The controller shall provide a copy of the personal data undergoing processing. For any further copies requested by the data subject, the controller may charge a reasonable fee based on administrative costs. Where the data subject makes the request by electronic means, and unless otherwise requested by the data subject, the information shall be provided in a <u>commonly used electronic form</u>.
> 4. The right to obtain a copy referred to in paragraph 3 shall not adversely affect the rights and freedoms of others.
#### Clause breakdown
##### Art. 15(4) — Third-party rights
**Clause: GDPR-RT11** | type: data subject right (scope limitation) | obligatedParty: CONTROLLER | obligationType: PER-REQUEST
**Control anchors:** CSF: RS.CO-02, ID.AM-08 · PF 1.1: CM.AW-P5, CT.DM-P3 · AI RMF: — · from `SR-GDPR-022` (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
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
##### Art. 23(1) — Permissible restriction grounds
**Clause: GDPR-RT20** | type: principle (restrictions scope) | obligatedParty: MEMBER STATE | obligationType: PER-RESTRICTION
**Control anchors:** CSF: — · PF 1.1: — · AI RMF: — (no consuming SR in dashboard mappings)
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
##### Art. 32(2) — Risk-enumeration for security assessment
**Clause: GDPR-CP16** | type: security risk assessment | obligatedParty: CONTROLLER + PROCESSOR | obligationType: CONTINUOUS
**Control anchors:** CSF: PR.DS-02, PR.IR-01, RS.CO-02, RS.MA-04, RS.MA-03, RS.CO-03, PR.IR-04, PR.DS-11, RC.RP-04, DE.CM-01, DE.CM-03, DE.AE-02 · PF 1.1: PR.DS-P2, PR.AC-P5, CM.AW-P7, CM.PO-P2, CM.AW-P8, PR.PO-P3, ID.RA-P3, GV.MT-P3 · AI RMF: — · from `SR-GDPR-002`, `SR-GDPR-016`, `SR-GDPR-019`, +2 more (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
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
##### Art. 33(1) — 72-hour notification
**Clause: GDPR-CP17** | type: breach notification | obligatedParty: CONTROLLER | obligationType: TRIGGERED (per breach)
**Control anchors:** CSF: DE.CM-01, DE.CM-09, RS.MA-02, RS.CO-02, RS.MA-04, RS.MA-03, RS.AN-03, RS.AN-07, DE.CM-03, DE.AE-02 · PF 1.1: GV.MT-P5, GV.MT-P3, CM.AW-P7, CM.PO-P2, ID.DE-P3, CM.PO-P1, ID.RA-P3 · AI RMF: — · from `SR-GDPR-014`, `SR-GDPR-016`, `SR-GDPR-017`, +2 more (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
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
##### Art. 34(1) — High-risk threshold
**Clause: GDPR-CP19** | type: breach communication | obligatedParty: CONTROLLER | obligationType: TRIGGERED (per high-risk breach)
**Control anchors:** CSF: RS.CO-03, RS.MA-04, PR.DS-01, PR.IR-03 · PF 1.1: CM.AW-P7, CM.AW-P8, PR.DS-P1, CT.DP-P2, CM.PO-P1 · AI RMF: — · from `SR-GDPR-019`, `SR-GDPR-020`, `SR-GDPR-021` (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
**Berry anchor:** §3.3.1 (`high risk` polysemy — vs Art. 33 `risk` vs Art. 35 `high risk`).
**Instance 1 — POLY+VAG / S3 / `likely to result in a high risk`**
Three undefined qualifiers. The cross-clause threshold distinction (`risk` Art. 33 vs `high risk` Arts. 34, 35) is the central notification-litigation question.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | `High risk` = objectively elevated above ordinary processing risk. | EDPB Guidelines 9/2022. |
| R2 | `High risk` = severe impact on data subject's rights. | CNIL guidance. |
R1 vs R2 yield materially distinct breach-classification systems.
---
##### Art. 34(3) — Exceptions to data-subject communication
**Clause: GDPR-CP20** | type: breach communication exception | obligatedParty: CONTROLLER | obligationType: PER-BREACH
**Control anchors:** CSF: PR.DS-01, PR.IR-03, RS.MI-01, RS.MI-02, RS.CO-03, PR.PS-06 · PF 1.1: PR.DS-P1, CT.DP-P2, PR.PO-P7, CT.DM-P10, CM.AW-P7, CM.PO-P1 · AI RMF: — · from `SR-GDPR-004`, `SR-GDPR-015`, `SR-GDPR-020`, +2 more (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
**Berry anchor:** §5.1 (`appropriate`, `unintelligible`, `disproportionate effort`), §5.4.7 (`OR (a) OR (b) OR (c)`).
**Instance 1 — VAG / S3 / `render the personal data unintelligible`**
`Unintelligible` (typically achieved via encryption) inherits the encryption-key-management question. If keys are lost, data is unintelligible in one sense but inaccessible to legitimate users too.
**Instance 2 — VAG / S3 / `disproportionate effort`**
Same Berry-flagged phrase as Art. 14(5)(b). S3 because the exception triggers instead-of notification duty, materially distinct compliance outcome.
---
### Article 35 — Data protection impact assessment
#### Verbatim (with highlighting)
> **Article 35**
> **Data protection impact assessment**
>
> 1. Where a type of processing in particular using **new technologies**, and taking into account the nature, scope, context and purposes of the processing, is likely to result in a **high risk** to the rights and freedoms of natural persons, the controller shall, prior to the processing, carry out an assessment of the impact of the envisaged processing operations on the protection of personal data. A single assessment may address a set of similar processing operations that present similar high risks.
> 2. The controller shall seek the advice of the data protection officer, where designated, when carrying out a data protection impact assessment.
> 3. A data protection impact assessment referred to in paragraph 1 shall in particular be required in the case of:
> (a) a systematic and extensive evaluation of personal aspects relating to natural persons which is based on automated processing, including profiling, and on which decisions are based that produce legal effects concerning the natural person or similarly significantly affect the natural person;
> (b) processing on a large scale of special categories of data referred to in Article 9(1), or of personal data relating to criminal convictions and offences referred to in Article 10; or
> (c) a systematic monitoring of a publicly accessible area on a large scale.
> 4. The supervisory authority shall establish and make public a list of the kind of processing operations which are subject to the requirement for a data protection impact assessment pursuant to paragraph 1. The supervisory authority shall communicate those lists to the Board referred to in Article 68.
> 5. The supervisory authority may also establish and make public a list of the kind of processing operations for which no data protection impact assessment is required.
> 6. Prior to the adoption of the lists referred to in paragraphs 4 and 5, the competent supervisory authority shall apply the consistency mechanism referred to in Article 63 where such lists involve processing activities which are related to the offering of goods or services to data subjects or to the monitoring of their behaviour in several Member States, or may substantially affect the free movement of personal data within the Union.
> 7. The assessment shall contain at least:
> (a) a **systematic description** of the envisaged processing operations and the purposes of the processing, including, where applicable, the legitimate interest pursued by the controller;
> (b) an assessment of the **necessity and proportionality** of the processing operations in relation to the purposes;
> (c) an assessment of the risks to the rights and freedoms of data subjects referred to in paragraph 1;
> (d) the measures envisaged to address the risks, including safeguards, security measures and mechanisms to ensure the protection of personal data and to demonstrate compliance with this Regulation taking into account the rights and legitimate interests of data subjects and other persons concerned.
> 8. Compliance with approved codes of conduct referred to in Article 40 by the relevant controllers or processors shall be taken into due account in assessing the impact of the processing operations performed by such controllers or processors, in particular for the purposes of a data protection impact assessment.
> 9. Where appropriate, the controller shall seek the views of data subjects or their representatives on the intended processing, without prejudice to the protection of commercial or public interests or the security of processing operations.
> 10. Where processing pursuant to point (c) or (e) of Article 6(1) has a legal basis in Union law or in the law of the Member State to which the controller is subject, that law regulates the specific processing operation or set of operations in question, and a data protection impact assessment has already been carried out as part of a general impact assessment in the context of the adoption of that legal basis, paragraphs 1 to 7 shall not apply unless Member States deem it to be necessary to carry out such an assessment prior to processing activities.
> 11. Where necessary, the controller shall carry out a review to assess if processing is performed in accordance with the data protection impact assessment at least when there is a change of the risk represented by processing operations.
#### Clause breakdown
##### Art. 35(1) — DPIA trigger
**Clause: GDPR-CP21** | type: impact assessment | obligatedParty: CONTROLLER | obligationType: PER-PROCESSING (pre-launch)
**Control anchors:** CSF: GV.OC-03, ID.RA-06, ID.RA-01, ID.RA-05, ID.IM-04 · PF 1.1: ID.RA-P5, GV.PO-P3, ID.RA-P3, ID.RA-P4, GV.MT-P2 · AI RMF: — · from `SR-GDPR-023`, `SR-GDPR-045`, `SR-GDPR-047` (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
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
**Control anchors:** CSF: ID.RA-05, ID.IM-02, GV.OC-03, ID.RA-06, ID.RA-01, RS.AN-03, ID.IM-04 · PF 1.1: ID.RA-P3, ID.RA-P5, GV.PO-P3, ID.RA-P4, GV.MT-P2 · AI RMF: — · from `SR-GDPR-008`, `SR-GDPR-023`, `SR-GDPR-045`, +2 more (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
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
##### Art. 36(1) — Prior consultation trigger
**Clause: GDPR-CP23** | type: supervisory consultation | obligatedParty: CONTROLLER | obligationType: PER-PROCESSING (pre-launch)
**Control anchors:** CSF: GV.OC-03, ID.RA-06, ID.RA-01, ID.RA-05 · PF 1.1: ID.RA-P5, GV.PO-P3, ID.RA-P3, ID.RA-P4 · AI RMF: — · from `SR-GDPR-023`, `SR-GDPR-045` (00_VISUALISATIONS/GDPR/GDPR_Dashboard.html)
**Berry anchor:** §3.3.1 (`high risk` — Art. 35 inheritance).
**Instance 1 — POLY+VAG / S2 / `high risk in the absence of measures`**
Inherits Art. 35(1) `high risk` threshold. S2 because the trigger is the same DPIA outcome.
---

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

The awareness trigger is polysemous (cf. CRA C25, NIS 2 C25 — same pattern across regulations).

<!-- aegis:purity: own_reg=GDPR; demoted=3; core_cross_mentions=0 -->
<!-- aegis:control-anchors: generated by scripts/uniformize_control_anchors.py from baseline/MAPPINGS/sr_control_mappings; not part of the verbatim Part 4 body -->
