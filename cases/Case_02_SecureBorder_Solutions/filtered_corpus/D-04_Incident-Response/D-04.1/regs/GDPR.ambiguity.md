# D-04.1 — Relevant Ambiguity (GDPR)

> Part 4 ambiguity analysis for GDPR, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## GDPR
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

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/GDPR.ambiguity.md

The awareness trigger is polysemous (cf. CRA C25, NIS 2 C25 — same pattern across regulations).

<!-- aegis:purity: own_reg=GDPR; demoted=1; core_cross_mentions=0 -->
<!-- aegis:control-anchors: generated by scripts/uniformize_control_anchors.py from baseline/MAPPINGS/sr_control_mappings; not part of the verbatim Part 4 body -->
