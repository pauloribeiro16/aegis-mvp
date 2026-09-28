# D-04.2 — Relevant Ambiguity (NIS 2)

> Part 4 ambiguity analysis for NIS 2, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## NIS2
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
#### 3.1 NIS2-CL07 — Art. 21(1) sentence 1 — Risk-management core obligation
**Source locus:**
> Member States shall ensure that essential and important entities take **<mark>appropriate and proportionate technical, operational and organisational measures</mark>** to manage the risks posed to the security of network and information systems which those entities use for their operations or for the provision of their services, and to prevent or minimise the **impact** of incidents on recipients of their services and on other services.
**Instance 1 — VAG — S3 — `appropriate and proportionate`**
The opening qualifier. Three materially distinct readings:
- **R1:** `appropriate` and `proportionate` are independent (entity must satisfy both tests, separately).
- **R2:** `appropriate` modifies `proportionate` (entity must satisfy proportionality, with `appropriate` as a placeholder synonym).
- **R3:** `appropriate and proportionate` is a single compound qualifier (a fixed phrase).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Independent | None in OJ |
| R2 | Hierarchical | None in OJ |
| R3 | Compound | In-Directive: Art. 21(1) sentence 2 operationalises proportionality by specific factors (exposure, size, likelihood, severity) |
R1 and R3 produce materially distinct compliance obligations (R1 admits two separate failure modes; R3 admits one composite test). S3.
This is the dominant VAG trigger of NIS 2. **It propagates to all 10 sub-points of Art. 21(2)(a)–(j) and to Art. 21(3) and Art. 21(4).** Every measure listed in Art. 21(2) inherits the `appropriate and proportionate` qualifier by reference to "The measures referred to in paragraph 1".
*Berry anchor:* §5.1 (`appropriate`, `proportionate`).
**Instance 2 — POLY — S2 — `technical, operational and organisational measures`**
Three-term coordination. Three readings:
- **R1:** Three distinct categories of measures (entity must implement at least one of each).
- **R2:** Cumulative description (a measure is "technical, operational and organisational" if it has all three characteristics).
- **R3:** Open list (entity may add more categories).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Distinct categories | In-Directive: literal `technical, operational and organisational` |
| R2 | Cumulative single measure | None in OJ |
| R3 | Open list | In-Directive: recital 56 (proportionality) |
R1 is the literal reading. R3 is the dominant reading (recital 56 implies entity-discretion on additional categories). S2.
*Berry anchor:* §5.5 (three-way coordination).
**Instance 3 — VAG + POLY — S2 — `manage the risks`**
`manage the risks` — what counts as `management`? Reading:
- **R1:** Identify + assess + mitigate.
- **R2:** Treat (avoid, accept, transfer, mitigate).
- **R3:** Continuous monitoring + adjustment.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Identify-assess-mitigate | None in OJ; ISO/IEC 27005 |
| R2 | ISO 27005 risk-treatment | None in OJ; ISO/IEC 27005 |
| R3 | Continuous monitoring | None in OJ; NIST RMF |
*Berry anchor:* §3.3.1 (`manage`).
**Instance 4 — POLY — S2 — `impact`**
`impact` — on recipients of services (downstream effect) or on other services (cascading effect)?
- **R1:** Impact on direct recipients.
- **R2:** Impact on other services (cascade).
- **R3:** Both.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Recipients | In-Directive: literal `recipients of their services` |
| R2 | Other services | In-Directive: literal `on other services` |
| R3 | Both | In-Directive: literal `recipients … and … other services` |
R3 is the literal reading (coordinated by `and`). The fact that the two objects are coordinated by AND rather than OR means the entity must consider impact on both. S2 because the surface ambiguity is between "focus on direct recipients" and "consider cascading effects".
*Berry anchor:* §3.3.1 (`impact`); §5.4.7 (AND).
---
#### 3.5 NIS2-CL11 — Art. 21(2)(b) — Incident handling
**Source locus:**
> **(b)** incident handling;
**Instance 1 — POLY — S2 — `incident handling`**
The phrase is defined in Art. 6(8): `any actions and procedures aiming to prevent, detect, analyse, and contain or to respond to and recover from an incident`. The 6-action list is illustrative (`aiming to`).
- **R1:** The 6-action list is exhaustive.
- **R2:** The 6-action list is a floor; entity must add more actions.
- **R3:** `incident handling` is process-only (NIST SP 800-61 model).
- **R4:** `incident handling` is team-only (CSIRT/SOC personnel).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Exhaustive | None in OJ |
| R2 | Floor | In-Directive: `aiming to` (illustrative) |
| R3 | Process | None in OJ; NIST SP 800-61 |
| R4 | Team | None in OJ; ENISA CSIRT-services guidance |
R2 is the literal reading. R3 vs R4 is a Layer 1 polysemy. S2.
*Berry anchor:* §3.3.1 (`incident handling`); §5.1 (`aiming to`).
---

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/NIS2.ambiguity.md

1. **Art. 20(1) is the only direct personal-liability provision in NIS 2.** No other article in Chapter IV imposes liability on natural persons. The provision is short but materially consequential. National implementations have begun diverging (e.g. Belgium's transposition law, France's transposition law) on which liability types attach.
2. **Art. 20(2) creates a two-tier training obligation:** mandatory (for members) + encouraged (for employees). The asymmetry is intentional in the Directive; the operational impact is that entities may be judged on management-body training compliance but not on employee training.
3. **The management-body training obligation is the second cross-regulation `training` polysemy hotspot** (the first was GDPR Art. 39 DPO training; the third is CRA Annex I Part II §2(c) `security update procedures` which includes training). All three share the same POLY pattern.
4. **The `essential and important entities` classification propagates through every Chapter IV clause.** Resolving it is the prerequisite for any other finding.

<!-- aegis:purity: own_reg=NIS2; demoted=1; core_cross_mentions=0 -->