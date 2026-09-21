# D-09.2 — Relevant Ambiguity (AI Act)

> Part 4 ambiguity analysis for AI Act, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## AI_Act
## Ambiguity Analysis — AI Act (Regulation (EU) 2024/1689)
> Layer 1 (linguistic) analysis of the 29 atomic clauses mapped to the AEGIS taxonomy in T5 (`AIA-C01` … `AIA-C29`).
>
> **Methodology:** see `01_Framework.md`. Categories VAG, SCOPE-Q, POLY, COORD. Severity S1/S2/S3.
>
> **Source text:** `03_REFERENCE_MATERIAL/Regulatory_References/AI_Act.txt` (OJ L, 12.7.2024).
>
> **Article references** use the form `Art. NN(p)(a)`.
---
### 1. Summary table
| Clause ID | Article | Sub-Domain | Types Found | Highest Sev. | Gist |
|---|---|---|---|---|---|
| AIA-C01 | Art. 9(1) | D-09.2 Risk assessment | VAG, POLY, COORD | **S2** | `established, implemented, documented and maintained` — 4-way AND of framework verbs |
| AIA-C02 | Art. 9(2) | D-09.2 Risk assessment | VAG, SCOPE-Q, POLY, COORD | **S3** | `known and reasonably foreseeable risks` + `reasonably foreseeable misuse` — `reasonably foreseeable` is the central undefined standard |
| AIA-C03 | Art. 9(6) | D-02.1 Vuln. identification | VAG, POLY, COORD | **S2** | `most appropriate and targeted risk management measures` |
| AIA-C04 | Art. 9(7) | D-02.4 TLPT | POLY | **S2** | `testing in real-world conditions` — distinct from lab testing; scope undefined |
| AIA-C05 | Art. 10(1) | D-05.1 Data minimisation | VAG, POLY, COORD | **S2** | `quality criteria` + `training, validation and testing data sets` |
| AIA-C06 | Art. 10(2) | D-05.1 Data minimisation | VAG, POLY, COORD | **S3** | 8-element list (a)–(h) of data governance practices; `biases` undefined; `detect, prevent and mitigate` is 3-way AND |
| AIA-C07 | Art. 10(3) | D-05.2 Retention | VAG, POLY, COORD | **S3** | `relevant, sufficiently representative, and to the best extent possible, free of errors and complete` — soft hedge on hard requirements |
| AIA-C08 | Art. 10(5) | D-05.1 Special category data | VAG, POLY, COORD | **S3** | `strictly necessary` + `state-of-the-art security and privacy-preserving measures` + 6 cumulative conditions (a)–(f) |
| AIA-C09 | Art. 12(1) | D-10.2 Logging | VAG, POLY | **S2** | `automatic recording of events (logs) over the lifetime of the system` |
| AIA-C10 | Art. 12(2) | D-10.2 Logging | VAG, POLY, COORD | **S2** | `level of traceability … appropriate to the intended purpose` |
| AIA-C11 | Art. 12(4) (T5 ref) | D-09.4 Records | VAG, POLY | **S2** | **T5 mapping mismatch**: Art. 12 has only paragraphs 1–3 in the OJ; the 6-month retention rule is in Art. 19(1) (cf. AIA-C19) |
| AIA-C12 | Art. 13(1) | D-09.1 Policies | VAG, POLY | **S3** | `sufficiently transparent` + `appropriate type and degree of transparency` — the central undefined term for AI explainability |
| AIA-C13 | Art. 13(3) | D-09.1 Policies | VAG, POLY, COORD | **S2** | `concise, complete, correct and clear information that is relevant, accessible and comprehensible` — twin 4-way and 3-way adjective coordinations |
| AIA-C14 | Art. 14(1) | D-08.2 Oversight | VAG, POLY | **S2** | `appropriate human-machine interface tools` + `effectively overseen` |
| AIA-C15 | Art. 14(4) | D-08.2 Oversight | VAG, POLY, COORD | **S2** | `as appropriate and proportionate` + 5-way list of oversight abilities (a)–(e) |
| AIA-C16 | Art. 15(1) | D-02.1 Accuracy | VAG, POLY, COORD | **S3** | `appropriate level of accuracy, robustness, and cybersecurity` — three undefined AI-technical terms in 3-way AND |
| AIA-C17 | Art. 15(3) | D-01.4 Robustness | VAG, POLY, COORD | **S2** | `as resilient as possible` + `errors, faults or inconsistencies` |
| AIA-C18 | Art. 15(4)-(5) | D-01.4 Adversarial | VAG, POLY, COORD | **S3** | 5-way AND (`prevent, detect, respond to, resolve and control`) + 6-way OR (`data poisoning, model poisoning, adversarial examples, model evasion, confidentiality attacks, model flaws`) |
| AIA-C19 | Art. 19(1) | D-10.2 Log retention | VAG, POLY | **S2** | `period appropriate to the intended purpose … of at least six months` — hard numeric floor reduces temporal ambiguity |
| AIA-C20 | Art. 17(1) | D-09.1 QMS | VAG, POLY, COORD | **S2** | `systematic and orderly manner` + 13-element QMS list (a)–(m) |
| AIA-C21 | Art. 17(1)(c) | D-10.3 Testing | POLY, COORD | **S2** | `design, design control and design verification` — 3-way AND of near-synonyms |
| AIA-C22 | Art. 17(1)(g) | D-09.2 Risk assessment | POLY, COORD | **S2** | `examination, test and validation procedures` |
| AIA-C23 | Art. 26(1) | D-09.1 Deployer measures | VAG, POLY, COORD | **S2** | `appropriate technical and organisational measures` — same pattern as GDPR Art. 5(1)(f) |
| AIA-C24 | Art. 26(2) | D-08.2 Deployer oversight | VAG, POLY, COORD | **S2** | `necessary competence, training and authority, as well as the necessary support` |
| AIA-C25 | Art. 72(1)-(2) | D-10.1 Monitoring | VAG, POLY, COORD | **S2** | `proportionate to the nature` + `actively and systematically collect, document and analyse` |
| AIA-C26 | Art. 73(1)-(4) | D-04.3 Notification | VAG, SCOPE-Q, POLY, COORD | **S3** | 4 differentiated timelines (immediate / 15 days / 10 days / 2 days) with undefined triggers; `serious incident` multi-category definition |
| AIA-C27 | Art. 74(1) | D-10.3 Surveillance | POLY | **S2** | `market surveillance` — borrows Regulation (EU) 2019/1020 definitions |
| AIA-C28 | Art. 55(1)(a) | D-09.2 GPAI evaluation | VAG, POLY, COORD | **S3** | `standardised protocols` + `state of the art` + `systemic risks` — three undefined anchors in one sub-point |
| AIA-C29 | Art. 55(1)(c) | D-04.3 GPAI notification | VAG, POLY, COORD | **S3** | `without undue delay` + `serious incidents` (AI-specific, distinct from Art. 73 serious incidents) |
**Clause counts:** 29/29 analysed. 0 clauses with no ambiguity found.
---
### 2. Detailed cards
#### 2.1 AIA-C01 — Art. 9(1) Risk management system
**Source locus:** `A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems`.
* **VAG — S2** — implicit (no explicit vague term in this sub-point, but `risk management system` defers to Art. 9(2)–(10) which are VAG-loaded).
* **POLY — S2** — `risk management system` — ISO 31000:2018 vs. NIST AI RMF 1.0 vs. internal bespoke system. The clause does not signal which.
* **COORD — S2** — `established, implemented, documented AND maintained`: 4-way verb coordination. Berry §5.5 parallelism: distinct activities (each must be performed) or facets of one composite duty?
**Berry anchor:** §5.5 (4-way verb coordination), §3.3.1 (`risk management system`).
#### 2.2 AIA-C02 — Art. 9(2) Risk management steps
**Source locus:** `(a) the identification and analysis of the known and the reasonably foreseeable risks … (b) … under conditions of reasonably foreseeable misuse … (d) the adoption of appropriate and targeted risk management measures`.
* **VAG — S3** — `reasonably foreseeable` recurs 4 times in Art. 9 (in 9(2)(a), 9(2)(b), and variants). The phrase imports a foresight standard without anchoring it: objective (industry consensus) vs. subjective (provider's expectation) vs. hybrid (court-determined). Berry §5.1 lists `foreseeable` as inquiry-resistant.
* **VAG — S2** — `appropriate and targeted`.
* **SCOPE-Q — S2** — `the known AND the reasonably foreseeable risks` — universal over both risk categories; the boundary between `known` and `reasonably foreseeable` is itself unclear.
* **POLY — S2** — `reasonably foreseeable misuse` — distinct from `reasonably foreseeable use` but the demarcation (when does use become misuse?) is undefined.
* **COORD — S2** — 4-step list (a)–(d) coordinated via the framework `It shall comprise the following steps:`.
**Berry anchor:** §5.1 (`foreseeable`, `appropriate`), §5.2.1 (`known`/`foreseeable` scope), §3.3.1 (`misuse`).

<!-- aegis:purity: own_reg=AI_Act; demoted=0; core_cross_mentions=0 -->

