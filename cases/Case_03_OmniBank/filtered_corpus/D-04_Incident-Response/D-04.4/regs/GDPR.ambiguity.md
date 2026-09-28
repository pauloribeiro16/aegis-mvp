# D-04.4 — Relevant Ambiguity (GDPR)

> Part 4 ambiguity analysis for GDPR, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## GDPR
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
##### Art. 21(1) — Objection grounds and overriding
**Clause: GDPR-RT16** | type: data subject right (object) | obligatedParty: CONTROLLER | obligationType: PER-OBJECTION
**Control anchors:** CSF: — · PF 1.1: — · AI RMF: — (no consuming SR in dashboard mappings)
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

<!-- aegis:purity: own_reg=GDPR; demoted=0; core_cross_mentions=0 -->
<!-- aegis:control-anchors: generated by scripts/uniformize_control_anchors.py from baseline/MAPPINGS/sr_control_mappings; not part of the verbatim Part 4 body -->
