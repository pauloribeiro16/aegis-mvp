# D-10.3 — Relevant Ambiguity (DORA)

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
## DORA v0.2 — Chapter IV: Digital Operational Resilience Testing (Art. 24–27)
> **Source.** OJ L 333, 27.12.2022, p. 45–48. `03_REFERENCE_MATERIAL/Regulatory_References/DORA.txt`, lines **2595–2850**.
>
> **Pattern.** Each article quoted in full, then per-clause analysis. Universal `[recital NN]` convention. DORA-specific fields: `definitional-anchor`, `proportionality-status: Art. 4 applies`, `RTS-pending: Art. 20` (where applicable), `definitional-anchor: DORA Art. 26(11) → TIBER-EU` (non-binding guidance).
>
> **Chapter IV establishes the testing programme.** Art. 24 sets the general programme as an integral part of the Art. 6 ICT risk-management framework. Art. 25 enumerates (in an open list) the test modalities. Art. 26 mandates Threat-Led Penetration Testing (TLPT) on a hard 3-year cadence, anchored to the **TIBER-EU** framework (non-binding). Art. 27 specifies requirements for testers (NEW in v0.2; T3 omitted Art. 27 entirely).
>
> **Articles in this file:** 4 articles, 24 paragraphs, 17 atomic clauses (CL24-1 … CL27-3).
---
### 1. Articles covered
| Article | Title | Paragraphs | New in v0.2? | T3 clause |
|---|---|---|---|---|
| Art. 24 | General requirements for the performance of digital operational resilience testing | 6 | No (extended) | **C32** |
| Art. 25 | Testing of ICT tools and systems | 3 | No (extended) | **C33** |
| Art. 26 | Advanced testing of ICT tools, systems and processes based on TLPT | 11 | No (extended) | **C34** |
| Art. 27 | Requirements for testers for the carrying out of TLPT | 3 | **YES** | — (not in T3) |
**Note on Art. 4 (Proportionality):** every clause card in this file carries `proportionality-status: Art. 4 applies` (per pilot convention).
**Note on Art. 20 (RTS-pending):** no RTS mandate in Ch. IV specifically (the RTS mandate is in Art. 26(11) for TLPT details, addressed inline).
---
### 2. Atomic clause map
| Clause ID | Locus | Type | Highest Sev. | Gist |
|---|---|---|---|---|
| CL24-1 | Art. 24(1)+(2) chapeau | Programme establishment | **S3** | Testing programme as integral part of Art. 6 ICT risk-management framework. |
| CL24-2 | Art. 24(3) | Risk-based approach | **S3** | Risk-based approach per Art. 4(2); `evolving landscape of ICT risk`; `criticality of information assets`. |
| CL24-3 | Art. 24(4) | Independence + conflicts of interest | **S3** | Tests by independent parties (internal or external); conflicts of interest avoided. |
| CL24-4 | Art. 24(5) | Remediation procedures | **S2** | Procedures to prioritise, classify and remedy issues; internal validation. |
| CL24-5 | Art. 24(6) | Yearly testing cadence | **S2** | At least yearly tests on ICT systems supporting critical or important functions. |
| CL25-1 | Art. 25(1) | Open-list test modalities | **S3** | 12 enumerated modalities (`such as vulnerability assessments … penetration testing`). |
| CL25-2 | Art. 25(2) | CSD/CCP pre-deployment | **S2** | Vulnerability assessments before any deployment/redeployment. |
| CL25-3 | Art. 25(3) | Microenterprise exception | **S3** | Microenterprises combine risk-based with strategic planning of ICT testing. |
| CL26-1 | Art. 26(1) | TLPT cadence | **S2** | **Every 3 years**; competent authority may reduce/increase. |
| CL26-2 | Art. 26(2) | TLPT scope | **S3** | Live production systems; critical or important functions. |
| CL26-3 | Art. 26(3)+(4) | CTPP participation + pooled TLPT | **S3** | Pooled testing across multiple entities when CTPPs are in scope. |
| CL26-4 | Art. 26(5)+(6)+(7) | Risk-mgmt controls + attestation | **S3** | Risk controls during TLPT; attestation + mutual recognition between CAs. |
| CL26-5 | Art. 26(8) | Identification of TLPT entities | **S3** | Three criteria: impact, financial stability, ICT risk profile. |
| CL26-6 | Art. 26(11) | ESAs RTS per TIBER-EU | **S2** | Draft RTS developed in agreement with ECB; **non-binding TIBER-EU anchor**. |
| CL27-1 | Art. 27(1)(a)–(e) | Tester requirements (external) | **S3** | Five sub-requirements: suitability, expertise, certification, assurance, insurance. |
| CL27-2 | Art. 27(2)(a)–(c) | Internal-tester additional conditions | **S3** | Approval by CA; sufficient resources; threat intelligence provider external. |
| CL27-3 | Art. 27(3) | Data processing in contracts | **S2** | Contracts require sound management of TLPT results and data. |
**Total: 17 atomic clauses (Art. 24: 5; Art. 25: 3; Art. 26: 6; Art. 27: 3).**
---
### 3. Verbatim OJ text — Art. 24–27
#### 4.1 CL24-1 — Art. 24(1)+(2) chapeau — Programme establishment
**Source locus:** Art. 24(1) and 24(2).
> For the purpose of assessing preparedness for handling ICT-related incidents, of identifying weaknesses, deficiencies and gaps in digital operational resilience, and of promptly implementing corrective measures, financial entities, other than microenterprises, shall, taking into account the criteria set out in Article 4(2), **establish, maintain and review** a **sound and comprehensive digital operational resilience testing programme** as an integral part of the ICT risk-management framework referred to in Article 6.
**Instance 1 — VAG — S3 — `sound and comprehensive`**
The qualifier `sound and comprehensive` is undefined.
- **R1:** Strict reading: tests must cover every component and every modality (exhaustive).
- **R2:** Risk-proportional reading: tests must cover enough of the system to detect material weaknesses.
- **R3:** Methodology-based reading: tests must apply an industry-recognised methodology (e.g. NIST SP 800-115, OWASP WSTG, TIBER-EU).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Exhaustive | None in OJ |
| R2 | Risk-proportional | In-Directive: Art. 4(2) proportionality |
| R3 | Methodology-based | None in OJ |
R1 vs R3 admit materially distinct compliance populations (exhaustive vs. methodology-defined). S3.
*Berry anchor:* §5.1 (`sound`, `comprehensive`).
**Instance 2 — COORD — S2 — `establish, maintain and review`**
Three coordinated verbs. Same pattern as DORA-D01 `build, assure and review` (see pilot file §2.1). S2.
*Berry anchor:* §5.4.7 (three-way coordination); cf. pilot §2.1.
**Instance 3 — POLY — S2 — `promptly`**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Immediately upon test completion | In-Directive: literal `promptly` |
| R2 | Within a reasonable period | None in OJ |
| R3 | Per entity-defined SLA | None in OJ |
S2 (each reading yields a different remediation SLA, but the obligation is to remediate regardless).
*Berry anchor:* §5.1 (`promptly`).
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
#### 6.1 Art. 25(1) — 12-modality open list (POLY/S3)
- **Structural implication:** the 12 modalities are illustrative, not exhaustive. Financial entities may add (e.g. red team, social engineering, fuzz testing) but should not omit any of the 12 without justification.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/DORA.ambiguity.md

*Berry anchor:* §5.1 (`effective`, `prudent`); §5.4.7 (AND); cf. CRA-CL27 `handled effectively` (same pattern).

### from regs/DORA.ambiguity.md

**Note on definitional anchors:** every ICT-related clause in Ch. IV inherits from DORA Art. 3(2) → NIS 2 Art. 6(1) (`network and information system`). The TLPT definitional anchor is DORA Art. 26(11) → **TIBER-EU** (non-binding ECB framework) — same **binding-to-non-binding definitional regress** pattern as CRA Annex I → ISO standards.

### from regs/DORA.ambiguity.md

`promptly implementing corrective measures` — same Berry-flagged vague temporal term as GDPR Art. 33 and CRA Art. 14 (C25).

### from regs/DORA.ambiguity.md

**Definitional anchor:** DORA Art. 3(2) → NIS 2 Art. 6(1) `network and information system`.
**Proportionality-status:** Art. 4 applies (proportionality recurs 3 times in Art. 24(1), (3), (6)).

### from regs/DORA.ambiguity.md

*Berry anchor:* §5.1 (`such as`); cf. CRA-C05 (Annex I Part I §2(d) `including but not limited to`).

### from regs/DORA.ambiguity.md

**Definitional anchor:** DORA Art. 3(2) → NIS 2 Art. 6(1) `network and information system`; DORA-D17 `TLPT` (for the penetration-testing sub-modality when elevated to TLPT, see CL26-*).
**Proportionality-status:** Art. 4 applies.

### from regs/DORA.ambiguity.md

Art. 25(1) enumerates 12 specific test modalities under the `such as …` open-list signal. The structural pattern is **identical to CRA Annex I Part I §2(d)** (`authentication, identity or access management systems` under `including but not limited to`) and to the CRA Annex I enumeration generally.

### from regs/DORA.ambiguity.md

- **Berry anchor:** §5.1 `such as` open-list marker; same pattern as CRA-C05 (Annex I Part I §2(d)).

### from regs/DORA.ambiguity.md

- **Cross-regulation consistency:** CRA, NIS 2 (Art. 21(2)(e) `secure system development and maintenance` includes similar open enumerations), and DORA all converge on the open-list pattern. This is a **regulatory-drafting convention**, not an artefact of any single regulation.


<!-- aegis:purity: own_reg=DORA; demoted=9; core_cross_mentions=0 -->