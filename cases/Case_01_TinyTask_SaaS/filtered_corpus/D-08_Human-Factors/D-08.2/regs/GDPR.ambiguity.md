# D-08.2 — Relevant Ambiguity (GDPR)

> Part 4 ambiguity analysis for GDPR, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## GDPR
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

<!-- aegis:purity: own_reg=GDPR; demoted=0; core_cross_mentions=0 -->

