# D-07.1 — Relevant Ambiguity (DORA)

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
## DORA v0.2 — Chapter III: ICT-Related Incident Management, Classification, and Reporting (Art. 17–23)
> **Source.** OJ L 333, 27.12.2022, p. 39–44. `03_REFERENCE_MATERIAL/Regulatory_References/DORA.txt`, lines **2275–2591**.
>
> **Pattern.** Each article quoted in full (paragraph by paragraph), then per-clause analysis. Universal `[recital NN]` convention. DORA-specific fields: `definitional-anchor`, `proportionality-status: Art. 4 applies`, `RTS-pending: Art. 18(3) | Art. 20` (the defining characteristic of Ch. III — hard deadlines and classification thresholds live in RTS, not OJ), `scope: regulator→financial-entity` (for client-notification and CA-routing clauses).
>
> **Chapter III is the operational reporting arm of DORA.** It operationalises the Art. 3(8) `ICT-related incident` and Art. 3(10) `major ICT-related incident` definitions. Art. 17 establishes the management process. Art. 18 enumerates 6 multiplicative criteria for classifying incidents (and 3 for cyber threats) and delegates the **combination rule + materiality thresholds** to an ESA RTS (Art. 18(3)). Art. 19 mandates reporting of major ICT-related incidents in 3 tiers (initial / intermediate / final), plus voluntary cyber-threat notification and mandatory client notification. Art. 20 is a pure RTS/ITS delegation — content, time limits, and templates are **wholly dependent** on the ESAs Joint Committee output (deadline 17 July 2024). Art. 21 is a feasibility-report mandate on centralisation (a single EU Hub). Art. 22 specifies supervisory feedback. Art. 23 extends Ch. III to operational/security payment-related incidents for credit institutions, payment institutions, AISPs, and EMIs.
>
> **Articles in this file:** 7 articles, ~30 paragraphs, **31 atomic clauses** (CL17-1 … CL23-1).
---
### 1. Articles covered
| Article | Title (OJ) | Paragraphs | New in v0.2? | T3 clause |
|---|---|---|---|---|
| Art. 17 | **ICT-related incident management process** | 3 (1, 2, 3 with 6 sub-points (a)–(f)) | No (extended) | **C29** |
| Art. 18 | **Classification of ICT-related incidents and cyber threats** | 4 (1 with 6 sub-points (a)–(f), 2, 3 with 3 sub-points (a)–(c), 4) | No (extended) | **C30** |
| Art. 19 | **Reporting of major ICT-related incidents and voluntary notification of significant cyber threats** | 8 (1, 2, 3, 4 with 3 sub-points (a)–(c), 5, 6 with 5 sub-points (a)–(e), 7, 8) | No (extended) | **C31** |
| Art. 20 | **Harmonisation of reporting content and templates** | 1 (RTS+ITS) | No (extended) | — (RTS meta — T3 omitted) |
| Art. 21 | **Centralisation of reporting of major ICT-related incidents** (single EU Hub feasibility) | 3 (1, 2 with 7 sub-points (a)–(g), 3) | **YES** | — (not in T3) |
| Art. 22 | **Supervisory feedback** | 2 (1, 2) | **YES** | — (not in T3) |
| Art. 23 | **Operational or security payment-related incidents concerning credit institutions, payment institutions, account information service providers, and electronic money institutions** (extension of Ch. III to payment-sector entities) | 1 | **YES** | — (not in T3) |
**Note on Art. 4 (Proportionality):** every clause card in this file carries `proportionality-status: Art. 4 applies`. Art. 18(4) explicitly names microenterprises and SMEs.
**Note on Art. 20 (RTS-pending — THE defining characteristic of Ch. III):** Ch. III is structurally dependent on RTS/ITS acts. The hard reporting deadlines and classification thresholds do not live in OJ text — they are mandated to the ESAs Joint Committee. As of mid-2025:
| RTS/ITS | Mandate locus | OJ deadline | Status (mid-2025) |
|---|---|---|---|
| Art. 18(3) RTS (criteria + materiality thresholds) | Art. 18(3)(a)–(c) | **17 January 2024** | Deadline **passed**; ESAs Joint Committee RTS in adoption pipeline. Implementing Regulation (EU) 2024/2956 of 18 July 2024 partially addresses content. |
| Art. 20 RTS (content + time limits) | Art. 20(a)(i)–(iii) | **17 July 2024** | Deadline **passed**; partly addressed by Reg. (EU) 2024/2956. |
| Art. 20 ITS (forms, templates, procedures) | Art. 20(b) | **17 July 2024** | **Adopted** as Implementing Regulation (EU) 2024/2956 (Annex I–IV templates). |
| Art. 21(3) joint report (single EU Hub) | Art. 21(1)–(3) | **17 January 2025** | Deadline **passed**; ESAs Joint Committee report published in Q1 2025. |
**Note on v0.2 expansion:** T3 (T4 taxonomy) covered Ch. III as 3 clauses (C29, C30, C31) corresponding to Arts 17, 18, 19 in compressed form. v0.2 expands this to 31 atomic clauses and **adds 4 articles** (Art. 20, 21, 22, 23) that T3 entirely omitted (T3 dropped them as "procedural" or "payment-specific").
---
### 2. Atomic clause map
| Clause ID | Locus | Type | Highest Sev. | Gist |
|---|---|---|---|---|
| CL17-1 | Art. 17(1) | Process establishment | **S2** | `define, establish and implement` an ICT-related incident management process. |
| CL17-2 | Art. 17(2) | Recording + follow-up | **S2** | Record all incidents and significant cyber threats; identify root causes. |
| CL17-3 | Art. 17(3)(a) | Early warning indicators | **S2** | Put in place early warning indicators. |
| CL17-4 | Art. 17(3)(b) | Classification procedures | **S3** | `identify, track, log, categorise and classify` per Art. 18(1) criteria. |
| CL17-5 | Art. 17(3)(c) | Roles and responsibilities | **S2** | Assign roles for different incident types and scenarios. |
| CL17-6 | Art. 17(3)(d) | Communication plans | **S3** | Plans for staff/media/client notification (Art. 14 cross-ref). |
| CL17-7 | Art. 17(3)(e) | Senior management escalation | **S3** | Major incidents → senior mgmt + management body (impact, response, controls). |
| CL17-8 | Art. 17(3)(f) | Response procedures | **S3** | `timely manner` services become operational and secure. |
| CL18-1 | Art. 18(1)(a) | Criterion 1 of 6 | **S3** | Clients/counterparts/transactions/reputational impact. |
| CL18-2 | Art. 18(1)(b) | Criterion 2 of 6 | **S3** | Duration including service downtime. |
| CL18-3 | Art. 18(1)(c) | Criterion 3 of 6 | **S3** | Geographical spread, particularly >2 Member States. |
| CL18-4 | Art. 18(1)(d) | Criterion 4 of 6 | **S3** | Data losses (4 CIA+A dimensions). |
| CL18-5 | Art. 18(1)(e) | Criterion 5 of 6 | **S3** | Criticality of services including transactions/operations. |
| CL18-6 | Art. 18(1)(f) | Criterion 6 of 6 | **S3** | Economic impact (direct/indirect, absolute/relative). |
| CL18-7 | Art. 18(2) | Significant cyber threats classification | **S3** | 3 sub-criteria for significant cyber threats. |
| CL18-8 | Art. 18(3) | ESAs RTS mandate | **S3** | RTS specifying criteria + materiality thresholds (3 sub-points). |
| CL18-9 | Art. 18(4) | RTS development considerations + deadline | **S3** | Proportionality; microenterprise/SME consideration; 17 January 2024 deadline. |
| CL19-1 | Art. 19(1) | Major incident reporting | **S3** | Report to relevant CA per Art. 46; single-CA designation; significant CIs → ECB. |
| CL19-2 | Art. 19(2) | Voluntary cyber-threat notification | **S2** | Voluntary notification by entity; CA may forward. |
| CL19-3 | Art. 19(3) | Client notification | **S3** | `without undue delay` notify clients + protection measures. |
| CL19-4 | Art. 19(4) | Three-tier reporting | **S3** | Initial notification + intermediate + final report. |
| CL19-5 | Art. 19(5) | Outsourcing of reporting | **S2** | May outsource; financial entity remains responsible. |
| CL19-6 | Art. 19(6) | CA→other authorities forwarding | **S3** | 5 recipient categories (EBA/ESMA/EIOPA, ECB, NIS 2 CAs/SPOCs/CSIRTs, resolution authorities, other public authorities). |
| CL19-7 | Art. 19(7) | ESAs/ECB cross-MS assessment | **S3** | ESAs/ECB assess cross-MS relevance; ESAs notify other MS CAs. |
| CL19-8 | Art. 19(8) | ESMA + host MS transmission | **S2** | ESMA transmission to host MS CAs; CSD cross-border activity carve-out. |
| CL20-1 | Art. 20 | ESAs RTS/ITS mandate | **S3** | RTS content (a)(i)–(iii) + ITS forms/templates/procedures (b). |
| CL21-1 | Art. 21(1)+(2) | Single EU Hub feasibility mandate | **S3** | Joint ESA report (in consultation with ECB, ENISA); 7 enumerated elements (a)–(g). |
| CL21-2 | Art. 21(3) | Report submission deadline | **S2** | Submission to EP/Council/Commission by 17 January 2025. |
| CL22-1 | Art. 22(1) | Supervisory feedback | **S3** | CA feedback on receipt of notification/reports; anonymised threat intel; remedies discussion. |
| CL22-2 | Art. 22(2) | ESAs yearly aggregated report | **S3** | Yearly anonymised-aggregated ESA report; warnings + high-level statistics. |
| CL23-1 | Art. 23 | Ch. III extension to payment-sector entities | **S3** | Ch. III applies to operational/security payment incidents for CIs, PIs, AISPs, EMIs. |
**Total: 31 atomic clauses (Art. 17: 8; Art. 18: 9; Art. 19: 8; Art. 20: 1; Art. 21: 2; Art. 22: 2; Art. 23: 1).**
---
### 3. Verbatim OJ text — Art. 17–23
#### 4.1 CL17-1 — Art. 17(1) — Process establishment
**Source locus:** Art. 17(1).
> Financial entities shall **define, establish and implement** an ICT-related incident management process to detect, manage and notify ICT-related incidents.
**Instance 1 — COORD — S2 — `define, establish and implement`**
Three coordinated verbs; the standard for each is undefined. Same pattern as DORA-D01 `build, assure and review` and Art. 24(1) `establish, maintain and review` (CL24-1 in Ch. IV file).
- **R1:** Three discrete lifecycle phases (define-then-establish-then-implement).
- **R2:** Three aspects of a single continuous process.
- **R3:** Three independent control families (define policy, establish system, implement operationally).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Discrete phases | In-Directive: literal three-verb coordination |
| R2 | Continuous | None in OJ |
| R3 | Independent families | None in OJ |
R1 vs R3 admit materially distinct compliance populations. S2.
*Berry anchor:* §5.4.7 (three-way coordination).
**Instance 2 — COORD — S2 — `detect, manage and notify`**
Three coordinated purposes of the process. Same Berry pattern.
*Berry anchor:* §5.4.7 (three-way coordination).
---
#### 4.27 CL21-1 — Art. 21(1)+(2) — Single EU Hub feasibility mandate
**Source locus:** Art. 21(1) and 21(2).
> 1. The ESAs, through the Joint Committee, and in consultation with the ECB and ENISA, shall prepare a joint report assessing the **feasibility of further centralisation of incident reporting through the establishment of a single EU Hub for major ICT-related incident reporting** by financial entities. The joint report shall explore ways to facilitate the flow of ICT-related incident reporting, reduce associated costs and underpin thematic analyses with a view to enhancing supervisory convergence.
>
> 2. The joint report referred to in paragraph 1 shall comprise at least the following elements:
>
> (a) prerequisites for the establishment of a single EU Hub;
>
> (b) benefits, limitations and risks, including risks associated with the high concentration of sensitive information;
>
> (c) the necessary capability to ensure interoperability with regard to other relevant reporting schemes;
>
> (d) elements of operational management;
>
> (e) conditions of membership;
>
> (f) technical arrangements for financial entities and national competent authorities to access the single EU Hub;
>
> (g) a preliminary assessment of financial costs incurred by setting-up the operational platform supporting the single EU Hub, including the requisite expertise.
**Instance 1 — VAG — S3 — `single EU Hub`**
`single` + `Hub` — the architectural choice is undefined.
- **R1:** Single centralised data platform (one location, all CAs access).
- **R2:** Single API gateway (each CA holds data, common API).
- **R3:** Single standard (distributed but interoperable).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Centralised platform | In-Directive: literal `single EU Hub` |
| R2 | API gateway | None in OJ |
| R3 | Single standard | None in OJ |
S3.
*Berry anchor:* §3.3.1 (`single`, `Hub`); §5.1 (`single`).
**Instance 2 — VAG — S3 — `feasibility`**
`feasibility` of centralisation is broad — technical + legal + operational + financial + governance. S3.
*Berry anchor:* §5.1 (`feasibility`).
**Instance 3 — VAG — S3 — `thematic analyses with a view to enhancing supervisory convergence`**
`thematic analyses` + `supervisory convergence` — undefined. S3.
*Berry anchor:* §3.3.1 (`thematic analyses`, `supervisory convergence`).
**Instance 4 — VAG — S2 — `high concentration of sensitive information`**
`high concentration` is undefined. Same Berry pattern as DORA-D29 `ICT concentration risk`. S2.
*Berry anchor:* §5.1 (`high concentration`); cf. DORA-D29.
**Instance 5 — POLY — S2 — 7 enumerated elements**
Each element admits its own internal ambiguity:
| Element | Key ambiguity | Berry anchor |
|---|---|---|
| (a) `prerequisites` | Hard vs. soft preconditions | §3.3.1 (`prerequisites`) |
| (b) `benefits, limitations and risks` | Three-way comparison standard | §5.4.7 (three-way) |
| (c) `interoperability` | Technical vs. semantic | §3.3.1 (`interoperability`) |
| (d) `operational management` | Undefined scope | §3.3.1 (`operational management`) |
| (e) `conditions of membership` | Who becomes a member? | §3.3.1 (`membership`) |
| (f) `technical arrangements` | Read-only vs. write access | §3.3.1 (`technical arrangements`) |
| (g) `preliminary assessment of financial costs` | Method-based vs. estimate-based | §3.3.1 (`preliminary`) |
S2 (per-element); aggregate S3 due to the open-ended `at least` qualifier.
*Berry anchor:* §5.4.5 (illustrative use — `at least`); §3.3.1.
**Definitional anchor:** DORA-D29 `ICT concentration risk`; DORA Art. 50 (administrative penalties context).
**Scope:** regulator-internal (between ESAs and NCA institutional architecture, not directly entity-facing).
**Proportionality-status:** Art. 4 applies.
---
#### 4.28 CL21-2 — Art. 21(3) — Report submission deadline
**Source locus:** Art. 21(3).
> The ESAs shall submit the report referred to in paragraph 1 to the European Parliament, to the Council and to the Commission by **17 January 2025**.
**Instance 1 — POLY — S2 — submission recipients (EP + Council + Commission)**
Three recipients. S2.
**Definitional anchor:** DORA-D29.
**Proportionality-status:** Art. 4 applies.
**Status note:** as of mid-2025, the deadline (17 January 2025) has passed; the ESAs Joint Committee report was published in Q1 2025 (per Council Document 5572/25 of 7 February 2025).
---
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

**Note on definitional anchors:** every ICT-related clause in Ch. III inherits from DORA Art. 3(2) → NIS 2 Art. 6(1) (`network and information system`). Major-incident classification inherits from Art. 3(10) `major ICT-related incident` (DORA-D10, S3 regress — see pilot file §2.4), which inherits from Art. 3(22) `critical or important function` (DORA-D22 tautology, S3).

### from regs/DORA.ambiguity.md

**Definitional anchor:** DORA Art. 3(2) → NIS 2 Art. 6(1) `network and information system`; DORA Art. 3(8) `ICT-related incident`.
**Proportionality-status:** Art. 4 applies.

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


<!-- aegis:purity: own_reg=DORA; demoted=10; core_cross_mentions=0 -->