---
document_id: MVP-SPEC-01
title: AEGIS MVP — Minimum Phase 1 Pipeline Specification
version: 0.1.0
created: 2026-09-17
status: ACTIVE
inputs: [input/<company>/company_input.md]
outputs: [output/<company>/phase1_output.md]
related_documents: [README.md, config.yaml, templates/company_input.md, templates/phase1_output.md]
---

# AEGIS MVP — Minimum Phase 1 Pipeline Specification

This document is the **contract** for the MVP pipeline. It defines the minimum
information required to run AEGIS Phase 1 (Contextual Definition) on a brand-new
company, the procedure that transforms it, and the shape of the result. It is
deliberately **reduced**: everything not defined here is deferred to a later
increment (§9) or inherited from the frozen baseline corpus (§2).

Any LLM agent (or human) capable of reading files and following steps can execute
a run. There is no code to deploy in Increment 0.

---

## 1. Scope of the MVP

**In scope (Increment 0):**

- One input file, five short prose sections (§4).
- One output file: company profile echo + applicable regulations + applicable
  sub-domain subset + adjusted objectives with regulatory and NIST anchors (§6).
- The sub-domain axis is a **subset of the 38 AEGIS sub-domains** `D-XX.Y` —
  only those that apply to the company (§7, rule R1).

**Out of scope (all deferred):** full intake questionnaire, RACI/stakeholders,
architecture & data inventory documents, third-party landscape, proportionality
profile with tier gate, clause mapping matrix, structured compliance matrix,
graph/ontology/dashboard infrastructure. See §9.

## 2. The three natures of Phase 1 information

| Nature | Content | Obligation of the executor |
|---|---|---|
| **Inherited** | Sub-domain corpus (`D-01.1` … `D-10.3`, merged Parts 1–4 with hierarchical objectives and per-regulation Sub-SOs), verbatim article copies (`articles/`), control referentials (`CONTROLS/`), ambiguity baseline (`AMBIGUITY_REGISTRY/`) | **Read by reference** via `config.yaml`. Never modify, never copy into this repo, never re-derive interpretations the corpus already contains. |
| **Company input** | Company profile, product, data handled, systems, regulations assumed | **Provided once** as `company_input.md` (§4). This is the *only* thing a new project must supply. |
| **Generated** | Applicability reasoning + adjusted objectives with anchors | **Produced by the procedure** (§5) into `phase1_output.md` (§6). |

Rationale: in the full methodology, "controls" (NIST/OWASP referentials) and
regulatory interpretation are frozen Phase-0 baseline shared by all cases; a new
project inherits them at zero cost. "Objectives" are an *output* of Phase 1, not
an input — only business goals enter through the input file.

## 3. Configuration

All paths live in `config.yaml` (see that file). The executor must resolve:

- `corpus.domains` — sub-domain corpus root (10 domain directories, each with
  `D-XX.Y/` sub-directories containing `D-XX.Y.md` + `articles/`).
- `corpus.controls` — control referentials (`NIST_CSF_2.0/CSF_2.0.json`,
  `NIST_PF/`, `NIST_AI_RMF/`, `NIST_80053R5/`, `NIST_SSDF/`, `OWASP_ASVS/`,
  `OWASP_SAMM/`).
- `ambiguity_registry.path` — canonical ambiguity baseline (`registry.md`).
- `pipeline.output_language` — output language (default `en`).

If a path does not resolve, **stop and report** — do not guess locations.

## 4. Input contract — `company_input.md`

One Markdown file, five sections, plain prose. **No questionnaire.** Each section
may be 2–10 lines; brevity is a feature. The template is `templates/company_input.md`.

| Section | Must contain |
|---|---|
| `§1 Company Profile` | Name, sector, size (employees), jurisdiction(s) of operation, legal form |
| `§2 Product / Service` | What the company sells or operates, in 2–5 sentences |
| `§3 Data Handled` | Categories of personal/other regulated data, subjects (customers, employees…), rough volumes/sensitivity |
| `§4 Systems & Cloud` | Main systems, hosting (own/cloud, provider), authentication, third-party services (5–10 lines) |
| `§5 Regulations Assumed` | The regulation list the company (or its advisor) believes applies, each with **one line of justification** |

Validation gates for the input: all 5 sections present and non-empty; §5 lists at
least one regulation with a justification. If a section is empty, **stop and ask
for a completed input** — do not invent company facts (rule R6).

Regulation identifiers used throughout: `GDPR`, `CRA`, `NIS2`, `DORA`, `AI_Act`.

## 5. Procedure (LLM-assisted)

Execute in order. Steps P1–P3 are reasoning over the input; P4 is corpus-grounded
derivation; P5 renders and validates.

- **P1 — Extract facts.** From input §1–§4, build an internal fact sheet: sector,
  size, jurisdictions, product, data categories, subjects, hosting, auth model,
  third parties. Nothing is inferred beyond the text (R6).
- **P2 — Confirm applicable regulations.** For each regulation in input §5, check
  its material/territorial scope against the fact sheet (e.g. GDPR: personal-data
  processing by an established entity; CRA: placing products with digital elements
  on the market; NIS2: essential/important entity sectors and size; DORA: financial
  entities; AI Act: placing AI systems on the market / deploying high-risk AI).
  Output §2 records each as *applies / does not apply* with a one-line rationale.
  A regulation the company listed but that fails the scope check is **flagged,
  not silently dropped**.
- **P3 — Select the sub-domain subset.** Scan the 38 sub-domains (names in each
  `D-0X_*/_index.md`; definitions in Part 1 of each `D-XX.Y.md`). A sub-domain is
  **in scope** when an applicable regulation imposes obligations whose subject
  matter matches the sub-domain *and* the company's facts trigger them (e.g. a
  company storing client personal data in a cloud DB → `D-01.1 Data at Rest
  Encryption` is in scope via GDPR Art. 32). Record each selected sub-domain with
  a one-line trigger rationale in output §3. Target size: as small as the facts
  allow (typical small company: 4–10 sub-domains).
- **P4 — Derive adjusted objectives.** For each in-scope sub-domain:
  1. Read `D-XX.Y.md` **Part 1** — the High-level Security Objective and the
     Sub-SO of each participating regulation; the security requirements section.
  2. Keep only the Sub-SOs / requirements of regulations confirmed in P2.
  3. Restate each as a company-proportional objective (rule R3) with ID
     `AG-D-XX.Y-NNN` (rule R4).
  4. Anchor it: cite regulation article(s) that **exist as copies** in the
     sub-domain's `articles/` directory (rule R2a) and optionally 1–2 control
     IDs from `CONTROLS/` referentials that clearly match (rule R2b).
  5. If the cited clause has a card in the ambiguity registry, reference the
     card instead of resolving silently (rule R7).
- **P5 — Render and validate.** Render output §1–§6 per `templates/phase1_output.md`
  and run the checklist in §8. Write the file to
  `output/<company>/phase1_output.md`.

## 6. Output contract — `phase1_output.md`

One Markdown file with light AEGIS-style frontmatter and six sections. Skeleton:
`templates/phase1_output.md`.

```
§1  Company Profile Echo        (≤15 lines, verbatim-faithful condensation of input §1–§4)
§2  Applicable Regulations      (table: Regulation | Verdict | Rationale)
§3  Applicable Sub-domain Subset (table: Sub-domain | Name | Trigger rationale)
§4  Adjusted Objectives         (one table per sub-domain:
                                 | ID | Adjusted objective | Regulatory source | Control anchor |
                                 IDs: AG-D-XX.Y-NNN)
§5  Ambiguities & Open Questions (registry card refs + company-specific doubts)
§6  Handoff Notes to Phase 2    (≤10 lines: what the next phase should start from)
```

Frontmatter fields (minimum): `document_id` (`MVP-P1-OUT-<n>`), `title`, `version`
(`0.1`), `created` (ISO date), `status` (`DRAFT` until §8 passes), `input` (path of
the `company_input.md` used), `corpus` (the `corpus.root` value from config).

## 7. Derivation rules

- **R1 — Subset axis.** The analysis axis is always the AEGIS sub-domain codes
  `D-XX.Y` with their canonical names. Never invent sub-domains; never merge them.
- **R2 — Anchor integrity (the golden rule).**
  - *R2a:* Every regulatory citation must exist as an article copy in the cited
    sub-domain's `articles/` directory (e.g. `D-01.1/articles/GDPR_Art_32.md`) or
    be quotable verbatim from that sub-domain's merged file. Cite as
    `REG Art. N` exactly as the file names it.
  - *R2b:* Every control anchor must exist in the cited referential file under
    `CONTROLS/` (grep-verifiable ID). Maximum 2 anchors per objective; omit the
    column content (`—`) rather than stretch a match.
  - **No invented anchors, ever.** If no anchor can be found, the objective is
    suspect — re-derive or drop it.
- **R3 — Proportionality.** Objectives are restated to company size: a 15-employee
  clinic chain gets "encrypt the client database at rest", not an enterprise
  key-management programme. No tier scores in Increment 0 — proportionality lives
  in the phrasing only.
- **R4 — IDs.** `AG-D-XX.Y-NNN`, zero-padded three digits, sequential per
  sub-domain within the run (`AG-D-01.1-001`, `AG-D-01.1-002`, …). This matches
  the AEGIS adjusted-goal scheme so later absorption into Doc13-like documents is
  mechanical.
- **R5 — Language.** Output in `pipeline.output_language` (default English).
  Input may be any language; the output §1 echo preserves proper nouns as-is.
- **R6 — No invention of company facts.** Every statement about the company in
  §1, §2 and §3 must trace to input text or be marked as an explicit assumption
  (`> ASSUMPTION:` blockquote) in §5.
- **R7 — Ambiguity deference.** When a clause cited for an objective has a card in
  the ambiguity registry, cite the card (registry ID) in §5 and follow its canonical
  resolution; do not re-litigate the ambiguity in the output.
- **R8 — Regulation discipline.** Obligations are derived only from regulations
  confirmed applicable in P2. If an in-scope sub-domain's corpus material references
  other regulations, ignore those parts for this run.

## 8. Run validation checklist

A run is **valid** when all of the following hold:

1. Input: 5 sections present, §5 has ≥1 regulation with justification.
2. Output §2 covers every regulation listed in input §5 (apply **or** flagged
   non-appliance with rationale — none silently missing).
3. Output §3 sub-domain codes exist in the corpus (`grep -r "D-XX.Y" corpus domains`).
4. Every `AG-D-XX.Y-NNN` in §4 is unique; sub-domain part matches its §3 row.
5. Every regulatory source in §4 resolves to a file in the cited sub-domain's
   `articles/` (rule R2a) — spot-check with `ls <subdomain>/articles/ | grep <Reg>`.
6. Every control anchor resolves in the cited referential (rule R2b).
7. No company statement in §1/§2/§3 lacks an input trace or an `ASSUMPTION` mark.
8. Frontmatter fields complete; `status` set to `ACTIVE` only after this checklist
   passes.

## 9. Absorption roadmap (increments)

Each increment adds one slice of the full methodology, in absorption order:

| Inc. | Adds | Absorbs from `Methodology_compact` |
|---|---|---|
| **0 (this)** | 1 input → 1 output, subset axis, real anchors | corpus by reference (already wired) |
| 1 | Split the output into two documents: applicability report (Doc08-like) + adjusted objectives (Doc13-like) | `01_PHASE1_CONTEXT_RICH/Doc08`, `Doc13` structure |
| 2 | Architecture & data inventory + third-party landscape as inputs | `Doc04`, `Doc06` sections |
| 3 | Clause mapping matrix, compliance matrix, proportionality tier + gate | `Doc10`, `Doc11`, `Doc12`; gate thresholds (LOW ≥60% / MEDIUM ≥75% / HIGH ≥80%) |
| 4 | Full intake (decision trees, conditional blocks, readiness, RACI, posture) | `Doc02_INTAKE_FORM` §1–§11 |
| 5 | Infra: ontology, graph, dashboards; multi-run master view | `phase1_ontology.yaml`, `build_p1_graph.py`, P1 dashboards |

Rule of growth: an increment is only started when the previous one has produced at
least one **valid** run (§8 checklist green) on a real company input.

## 10. Out-of-scope notes

- No code, no linting, no CI in Increment 0. If a scripts/ need emerges, it serves
  the §8 checklist first (anchor greps), nothing else.
- No writes into `Methodology_compact`. If absorption seems to require editing the
  corpus, the design is wrong — escalate instead.
