# D-08.3 — Relevant Ambiguity (NIS 2)

> Part 4 ambiguity analysis for NIS 2, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## NIS2
#### 3.3 NIS2-CL03 — Art. 20(2) sentence 1 — Mandatory management-body training
**Source locus:**
> Member States shall ensure that the **<u>members of the management bodies</u>** of essential and important entities **are required to follow training**.
**Instance 1 — VAG — S3 — `are required to follow training`**
`required to follow training` — required by whom? Member States (the obligation target of the sentence is Member States) or the entity itself? Three materially distinct readings:
- **R1:** Member States must legislate a statutory training requirement for management-body members.
- **R2:** Member States must ensure the entity itself requires its management-body members to follow training.
- **R3:** Both (Member States must legislate AND ensure the entity requires it).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Statutory training requirement | In-Directive: literal `Member States shall ensure` is directed to MS, not entities |
| R2 | Entity-internal requirement | In-Directive: literal `are required to follow` is directed to members |
| R3 | Both | In-Directive: standard MS-implementation pattern |
R1 and R2 yield materially different compliance obligations (R1 is a national-law requirement; R2 is an entity-internal governance requirement). S3.
*Berry anchor:* §5.1 (`required`).
**Instance 2 — VAG — S2 — `training`**
Polysemy inherited from the cybersecurity-vocabulary ecosystem. Three readings:
- **R1:** Formal certified curriculum (e.g. ISO/IEC 27001 lead-auditor, CISSP, CISM).
- **R2:** Awareness briefing (annual cybersecurity overview).
- **R3:** Tabletop exercise (incident simulation).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Formal curriculum | None in OJ; ENISA training guidance |
| R2 | Awareness briefing | None in OJ; recital 50 (cyber hygiene) |
| R3 | Tabletop exercise | None in OJ |
*Berry anchor:* §3.3.1 (`training`).
**Instance 3 — SCOPE-Q — S2 — `members of the management bodies`**
The Directive says `members` (universal). The reading:
- **R1:** Every individual member of every management body.
- **R2:** The management body as a collective (i.e. some members must be trained).
- **R3:** A designated cybersecurity-knowledgeable subset.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Every member | In-Directive: literal `members` (plural) |
| R2 | At least one member (collective) | None in OJ |
| R3 | Designated subset | None in OJ |
R1 is the literal reading. R2 and R3 are operational concessions. S2 because the difference is between training-100% and training-a-subset.
*Berry anchor:* §5.2.1 (`members`).
---
#### 3.4 NIS2-CL04 — Art. 20(2) sentence 1 — Purpose clause
**Source locus (continued):**
> …in order that they gain **<mark>sufficient knowledge and skills</mark>** to enable them to **identify risks and assess cybersecurity risk-management practices and their impact on the services provided by the entity**.
**Instance 1 — VAG — S2 — `sufficient knowledge and skills`**
`sufficient` — sufficient for what? Sufficient to perform the management-body function generally, or sufficient to perform the cybersecurity-governance function specifically?
- **R1:** General-management sufficiency.
- **R2:** Cybersecurity-specific sufficiency.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | General management | None in OJ; recital 50 |
| R2 | Cybersecurity-specific | In-Directive: literal `cybersecurity risk-management practices` qualifier |
R2 is the dominant reading. S2 because the difference affects training scope.
*Berry anchor:* §5.1 (`sufficient`).
**Instance 2 — VAG — S2 — `identify risks and assess cybersecurity risk-management practices`**
`identify risks` — risks to what? Risks to the entity? Risks to recipients of services? Risks to other entities?
- **R1:** Risks to the entity.
- **R2:** Risks to recipients of services.
- **R3:** Both.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Entity only | In-Directive: literal context |
| R2 | Recipients only | None in OJ |
| R3 | Both | In-Directive: Art. 21(1) covers `incidents on recipients of their services` |
R1 and R3 are operative; R2 is rejected by Art. 21(1) context. S2.
*Berry anchor:* §3.3.1 (`risks`).
**Instance 3 — COORD — S2 — `identify risks AND assess cybersecurity risk-management practices AND their impact on the services provided by the entity`**
Three coordinated activities. Three readings:
- **R1:** All three must be performed (cumulative).
- **R2:** Two distinct activities (risk identification + impact assessment) bundled.
- **R3:** Single activity: assess risk-management practices including their impact.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Three distinct | In-Directive: literal `identify … and assess … and their impact` |
| R2 | Two distinct | None in OJ |
| R3 | One composite | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §5.5 (three-way coordination).
---
#### 3.6 NIS2-CL06 — Art. 20 chapeau — Implicit proportionality / scope hook
**Source locus (chapeau of Art. 20, paraphrased from sentence 1):**
> Member States shall ensure that [the obligations] apply to essential and important entities.
**Instance 1 — VAG + POLY — S2 — `essential and important entities`**
The term is defined in Art. 3 but Art. 3's own classification criteria (size thresholds, sectoral lists, Member State discretion) are open. Three layers of indeterminacy:
- Layer A: `essential` vs. `important` — different supervisory regimes (Art. 32 fines, Art. 33 enforcement measures).
- Layer B: size thresholds (medium vs. large per Recommendation 2003/361/EC).
- Layer C: sectoral coverage (Annex I/II).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Two-tier binary (essential OR important) | In-Directive: Art. 3(1)–(2) |
| R2 | Member-State-discretionary boundary | In-Directive: Art. 3(1)(e), (g) — Member States may identify additional essential entities |
| R3 | Annex I/II sector lists are exhaustive | In-Directive: Art. 2(1) + Annex I/II |
R1 is the structural reading. R2 is the Member-State-discretion reading. R3 is the sectoral-exhaustive reading. S2 because the surface ambiguity drives whether an entity falls in the scope of Art. 20 (R1/R2/R3 may give different answers for borderline cases like cloud-computing providers with mixed sectoral exposure).
*Berry anchor:* §3.3.1 (`essential and important entities`); §5.2.1 (Annex lists).
**Layer 1 observation** — The Art. 3 classification of an entity is a **prerequisite** for all of Art. 20, 21, 22, 23, 24, 25 obligations. If an entity is not classified as essential or important, none of these apply. The classification itself is ambiguous (R2: Member-State discretion; R3: Annex I/II exhaustive). This is the **single most important scope-defining layer of NIS 2** — flagged in synthesis.
---
### 4. Cross-clause structural observations (Art. 20)
---
### 5. T3-to-v0.2 mapping
| T3 clause | T3 article | v0.2 clause | v0.2 article | Notes |
|---|---|---|---|---|
| NIS2-C01 | Art. 20(1) | NIS2-CL01 + NIS2-CL02 | Art. 20(1) | v0.2 splits sentence 1 (CL01) from sentence 2 carve-out (CL02); T3 only analysed sentence 1. |
| NIS2-C02 | Art. 20(2) | NIS2-CL03 + NIS2-CL04 + NIS2-CL05 | Art. 20(2) | v0.2 splits the three coordinated sub-phrases; T3 treated sentence 2 as a single clause. |
| (none) | — | NIS2-CL06 | Art. 20 chapeau | v0.2 adds the Art. 3 classification-propagation analysis that T3 omitted. |
---
**End of Art. 20 file. Next: `03_NIS2_Art21_RiskManagement.md` (the heart of NIS 2).**

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/NIS2.ambiguity.md

Same polysemy as GDPR C27/C28 (training in data-protection context). The variant readings converge in practice (entities do all three) but the Directive does not specify which is required.

### from regs/NIS2.ambiguity.md

1. **Art. 20(1) is the only direct personal-liability provision in NIS 2.** No other article in Chapter IV imposes liability on natural persons. The provision is short but materially consequential. National implementations have begun diverging (e.g. Belgium's transposition law, France's transposition law) on which liability types attach.
2. **Art. 20(2) creates a two-tier training obligation:** mandatory (for members) + encouraged (for employees). The asymmetry is intentional in the Directive; the operational impact is that entities may be judged on management-body training compliance but not on employee training.
3. **The management-body training obligation is the second cross-regulation `training` polysemy hotspot** (the first was GDPR Art. 39 DPO training; the third is CRA Annex I Part II §2(c) `security update procedures` which includes training). All three share the same POLY pattern.
4. **The `essential and important entities` classification propagates through every Chapter IV clause.** Resolving it is the prerequisite for any other finding.

<!-- aegis:purity: own_reg=NIS2; demoted=2; core_cross_mentions=0 -->