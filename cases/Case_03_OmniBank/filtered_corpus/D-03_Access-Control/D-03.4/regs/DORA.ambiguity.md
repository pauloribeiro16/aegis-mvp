# D-03.4 — Relevant Ambiguity (DORA)

> Part 4 ambiguity analysis for DORA, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## DORA
#### 4.4 CL5-1 — Art. 5(1) — Internal governance and control framework chapeau
**Source locus:** Art. 5(1).
> Financial entities shall have in place an **internal governance and control framework** that ensures an **effective and prudent** management of ICT risk, in accordance with Article 6(4), in order to achieve a high level of digital operational resilience.
**Instance 1 — VAG — S3 — `internal governance and control framework`**
The framework chapeau. Three materially distinct readings:
- **R1:** Three lines of defence model (per Art. 6(4) cross-reference).
- **R2:** Two lines of defence (business + control, common in some Member States).
- **R3:** Composite: any recognised internal-control model.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Three lines of defence | In-Directive: Art. 6(4) `according to the three lines of defence model` |
| R2 | Two lines of defence | None in OJ |
| R3 | Any model | In-Directive: Art. 6(4) `or an internal risk management and control model` |
R3 is the literal reading (Art. 6(4) gives the option). S3 (the choice between R1 and R3 yields materially distinct control populations).
*Berry anchor:* §3.3.1 (`governance and control framework`); §5.4.7 (AND/OR structure).
**Instance 2 — VAG — S3 — `effective and prudent`**
Two vague qualifiers (AND). Both are Berry classics.
- **R1:** Effective (outcome-based) AND prudent (process-based, conservative).
- **R2:** Hendiadys (single concept: risk-management discipline).
- **R3:** Either, per entity judgment.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Distinct qualifiers | In-Directive: literal `and` |
| R2 | Hendiadys | None in OJ |
| R3 | Either | None in OJ |
R1 is the literal reading. R1 vs R3 admit materially distinct compliance populations (R1 requires both outcome and process; R3 allows either). S3.
**Instance 3 — POLY — S2 — `a high level of digital operational resilience`**
The target standard. Inherits DORA-D01 `digital operational resilience` (S3 `build, assure and review`).
- **R1:** All three lifecycle phases per R1 of DORA-D01.
- **R2:** Continuous process per R2 of DORA-D01.
- **R3:** All three control families per R3 of DORA-D01.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Lifecycle phases | In-Directive: DORA-D01 |
| R2 | Continuous process | In-Directive: DORA-D01 |
| R3 | Control families | In-Directive: DORA-D01 |
S2 (the target is propagated from the definition).
*Berry anchor:* §3.3.1 (`high level`); §3.3.1 (`digital operational resilience`).
**Definitional anchor:** DORA Art. 3(1) `digital operational resilience` (DORA-D01); DORA Art. 3(5) `ICT risk` (DORA-D05).
**Proportionality-status:** Art. 4 applies.
**Scope:** financial entity.
---
#### 6.3 Art. 6 chapeau — the framework's three-attribute triad
Art. 6(1) opens with `sound, comprehensive and well-documented` (three attributes, AND). This is the **framework-level analog** of:
- **Art. 24(1) `sound and comprehensive`** (testing programme, two attributes; CL24-1)
- **Berry anchor:** §5.1 (`sound`, `comprehensive`, `well-documented`); §5.4.7 (AND); §5.5 (parallelism).
- **Structural implication:** the framework's three attributes set the bar for every Ch. II–V Sec. I clause. Any clause that fails one of the three (e.g. a framework that is `comprehensive and well-documented` but not `sound`) would be non-compliant.
#### 4.6 CL25-1 — Art. 25(1) — Open-list test modalities
**Source locus:** Art. 25(1).
> The digital operational resilience testing programme referred to in Article 24 shall provide, in accordance with the criteria set out in Article 4(2), for the execution of **appropriate tests, such as vulnerability assessments and scans, open source analyses, network security assessments, gap analyses, physical security reviews, questionnaires and scanning software solutions, source code reviews where feasible, scenario-based tests, compatibility testing, performance testing, end-to-end testing and penetration testing**.
**Instance 1 — POLY — S3 — `appropriate tests, such as …` (open list of 12 modalities)**
The list is **explicitly open** (`such as …`) but enumerates 12 specific modalities. Three readings of how to treat the list:
- **R1:** Closed list (the 12 are exhaustive; financial entities must conduct all of them).
- **R2:** Open list (the 12 are illustrative; entities must choose from these or add others).
- **R3:** Open list with 12-floor (entities must conduct at least these 12).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Closed list | None in OJ |
| R2 | Open list | In-Directive: literal `such as` (Berry §5.1 open-list signal) |
| R3 | Open with floor | None in OJ |
R2 is the literal reading. R1 vs R2 admit materially distinct compliance populations (R1: entity conducts only the 12; R2: entity adds modalities e.g. red team, social engineering, fuzz testing). S3.
**Instance 2 — POLY — S2 — 12 individual modalities**
Each modality admits internal ambiguity (e.g. `vulnerability assessments and scans` could mean automated-only, manual-only, or hybrid; `penetration testing` could be black-box, grey-box, or white-box).
| Modality | Key ambiguity | Berry anchor |
|---|---|---|
| `vulnerability assessments and scans` | Automated vs. manual scope | §3.3.1 (`assessments`) |
| `open source analyses` | OSS code review vs. OSS dependency analysis | §3.3.1 (`open source`) |
| `network security assessments` | External vs. internal network | §3.3.1 (`network`) |
| `gap analyses` | Compliance-gap vs. capability-gap | §3.3.1 (`gap`) |
| `physical security reviews` | Premises-only vs. hardware-inclusive | §3.3.1 (`physical security`) |
| `questionnaires and scanning software solutions` | Self-assessment vs. auditor-driven | §3.3.1 (`questionnaires`) |
| `source code reviews where feasible` | `feasible` undefined; static vs. dynamic | §5.1 (`feasible`) |
| `scenario-based tests` | Adversary-emulation vs. failure-mode | §3.3.1 (`scenario`) |
| `compatibility testing` | Interoperability vs. backward-compat | §3.3.1 (`compatibility`) |
| `performance testing` | Load vs. stress vs. soak | §3.3.1 (`performance`) |
| `end-to-end testing` | Business-process vs. data-flow | §3.3.1 (`end-to-end`) |
| `penetration testing` | Black-box vs. grey-box vs. white-box | §3.3.1 (`penetration`) |
Each row is S2 on its own (the modality is recognised; the specific implementation is open). The aggregate is the open-list pattern at S3.
---
#### 4.7 CL25-2 — Art. 25(2) — CSD/CCP pre-deployment vulnerability assessments
**Source locus:** Art. 25(2).
> Central securities depositories and central counterparties shall perform vulnerability assessments **before any deployment or redeployment of new or existing applications and infrastructure components, and ICT services supporting critical or important functions** of the financial entity.
**Instance 1 — POLY — S2 — `deployment or redeployment`**
`deployment` vs. `redeployment`:
- **R1:** Strict: redeployment = re-installation of existing component.
- **R2:** Broad: redeployment = any configuration change to a previously deployed component.
- **R3:** Either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Strict (reinstall) | None in OJ |
| R2 | Broad (config change) | In-Directive: literal `redeployment` (broad) |
| R3 | Either | In-Directive: literal `or` |
R2 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`deployment`, `redeployment`).
**Instance 2 — COORD — S2 — `new or existing applications and infrastructure components, and ICT services`**
Three categories (OR) coordinated. Compound scope:
- **R1:** Each category tested separately.
- **R2:** Compound scope: any combination tested.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Separate | None in OJ |
| R2 | Compound | In-Directive: literal `or` |
R2 is the literal reading. S2.
*Berry anchor:* §5.4.7 (multi-way OR).
---
#### 6.1 Art. 25(1) — 12-modality open list (POLY/S3)
- **Structural implication:** the 12 modalities are illustrative, not exhaustive. Financial entities may add (e.g. red team, social engineering, fuzz testing) but should not omit any of the 12 without justification.
#### 6.5 Art. 25(2) — Sectoral carve-out for CSD/CCP
Art. 25(2) imposes a **pre-deployment vulnerability assessment obligation on two specific entity types** (CSDs and CCPs). This is a sectoral carve-out unique in Ch. IV — no other clause names specific entity types.
- **Berry anchor:** §3.3.1 (`central securities depositories`, `central counterparties`).
- **Structural implication:** CSDs and CCPs are **financial market infrastructures (FMIs)** with systemic importance. The pre-deployment assessment obligation reflects the FMI-specific risk profile (a deployment-induced vulnerability could cascade to the entire clearing or settlement system).

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/DORA.ambiguity.md

*Berry anchor:* §5.1 (`effective`, `prudent`); §5.4.7 (AND); cf. CRA-CL27 `handled effectively` (same pattern).

### from regs/DORA.ambiguity.md

- **CRA Annex I Part I §1 chapeau** `products with digital elements shall be designed, developed and produced …` (manufacturing lifecycle, three verbs; CRA-CL14)

### from regs/DORA.ambiguity.md

- **NIS 2 Art. 21(1) `appropriate and proportionate technical, operational and organisational measures`** (measures chapeau)


### from regs/DORA.ambiguity.md

The 3-attribute triad (`sound, comprehensive and well-documented`) is **the most demanding framework chapeau in the 5-regulation corpus** — it requires three distinct qualities (effectiveness, completeness, traceability). CRA Annex I Part I §1 has three verbs (design, develop, produce) but they describe **processes** not qualities. DORA's triad describes **qualities of an artifact** (the framework itself), which is a different kind of obligation.

### from regs/DORA.ambiguity.md

- **Cross-regulation consistency:** the triad is the most explicit framework-quality specification in the corpus. NIS 2 Art. 21(1) uses `appropriate and proportionate` (2 qualifiers); CRA Annex I Part I uses process verbs; GDPR Art. 24 uses `appropriate` (1 qualifier). DORA's 3-attribute triad is the most demanding.


### from regs/DORA.ambiguity.md

*Berry anchor:* §5.1 (`such as`); cf. CRA-C05 (Annex I Part I §2(d) `including but not limited to`).

### from regs/DORA.ambiguity.md

**Definitional anchor:** DORA Art. 3(2) → NIS 2 Art. 6(1) `network and information system`; DORA-D17 `TLPT` (for the penetration-testing sub-modality when elevated to TLPT, see CL26-*).
**Proportionality-status:** Art. 4 applies.

### from regs/DORA.ambiguity.md

**Definitional anchor:** DORA Art. 3(2) → NIS 2 Art. 6(1) `network and information system`; DORA-D22 `critical or important function` (S3 tautology).
**Proportionality-status:** Art. 4 applies (with sectoral specificity: only CSDs and CCPs, two specific entity types).

### from regs/DORA.ambiguity.md

Art. 25(1) enumerates 12 specific test modalities under the `such as …` open-list signal. The structural pattern is **identical to CRA Annex I Part I §2(d)** (`authentication, identity or access management systems` under `including but not limited to`) and to the CRA Annex I enumeration generally.

### from regs/DORA.ambiguity.md

- **Berry anchor:** §5.1 `such as` open-list marker; same pattern as CRA-C05 (Annex I Part I §2(d)).

### from regs/DORA.ambiguity.md

- **Cross-regulation consistency:** CRA, NIS 2 (Art. 21(2)(e) `secure system development and maintenance` includes similar open enumerations), and DORA all converge on the open-list pattern. This is a **regulatory-drafting convention**, not an artefact of any single regulation.


### from regs/DORA.ambiguity.md

- **Cross-regulation consistency:** CRA does not impose pre-deployment obligations. NIS 2 Art. 21(2)(f) requires `policies and procedures for cryptography` but not pre-deployment assessments. **DORA Art. 25(2) is a sectoral specificity.**


<!-- aegis:purity: own_reg=DORA; demoted=12; core_cross_mentions=0 -->