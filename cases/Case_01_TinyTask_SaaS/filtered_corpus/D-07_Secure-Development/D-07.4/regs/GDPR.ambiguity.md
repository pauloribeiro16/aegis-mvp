# D-07.4 — Relevant Ambiguity (GDPR)

> Part 4 ambiguity analysis for GDPR, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## GDPR
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

<!-- aegis:purity: own_reg=GDPR; demoted=0; core_cross_mentions=0 -->