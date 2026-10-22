# AEGIS — context briefing for an external review

**Date:** 2026-10-21 · **Repository:** https://github.com/pauloribeiro16/aegis-mvp
**For:** a model with access to the public GitHub repository only.
**Why this file exists:** you can see the repository. You cannot see the run
artifacts, the cluster, the measured experiment logs that live outside the repo,
or the working notes of the people who built it. This file carries what is missing.

---

## 1. What we want from you

You already reviewed this repository once and returned a set of architectural
opinions. We have since verified every claim you made against the actual tree.
The result is that **your normative-comparison findings were correct and
valuable** (four real defects in the frozen control-referential layer that our own
validators pass, because they check that a path resolves, not that an identifier
points at the right section of a standard), while **your architectural findings
were about a tree that is not published** — you described a root containing only
`audit_runner.py`, no Python package and no tests; the repository actually
contains a 47-module package (`pipeline/src/aegis_pipeline/`), twelve test files
with 102 test functions, and `audit_runner.py` is a legacy one-shot script with a
hardcoded Windows path that cannot run on this machine.

So we are not asking you for a roadmap in the abstract. We are asking for five
things, in priority order:

- **A1 — Normative fidelity of the frozen referential layer.** For every
  control-referential under `baseline/CONTROLS/`, compare the identifier space
  the repository asserts against the published identifier space of the standard
  it names. Four defects of this class were confirmed; two have since been
  corrected and two remain open (see §7 — read it before you start, so you do not
  re-report a closed defect). What your answer must settle is whether the class
  has more members, and what the *published* identifier space is for the
  referentials we could not verify. For each defect: the exact file and line, the
  published value, where the defective identifier is consumed, and the
  machine-checkable invariant that would have caught it.
- **A2 — Where the architecture is weak in a way a doctoral examiner would
  find.** Not "what would you refactor" — the repository has contracts that
  refactoring would break (R2a, the case-corpus composition, the n-ary
  interaction layer). We want the load-bearing weaknesses: the ones where a
  correct-looking document rests on something the system never measured.
- **A3 — A falsification battery for the Phase 3 exit gates.** The exit gate is
  a pure function of the artifacts on disk — it calls the model zero times —
  so iterating it is free. Five of its six checks measured file existence rather
  than substance in the published code. We want, for each gate, the mutation
  that must make it fail, written as a test spec we can implement.
- **A4 — A roadmap that respects the constraints we actually work under.** The
  chain has three phases and no Phase 4 (researcher ruling). One decision is
  waiting on a human and blocks the whole downstream. Most experiments are
  frozen pre-registrations. Tell us what order to attack things in, and what
  we should stop doing.
- **A5 — The thesis-facing risk list.** What a jury attacks first, what we
  should fix, and what we should reframe and stop claiming.

**Ground rules for your answer (§9).** Anchor every claim to `path:line` in the
published tree, or mark it `NOT VERIFIABLE`. Distinguish what the repository
says (certain: you quote it) from what a standard says (your knowledge: grade
it ALTA/MÉDIA/BAIXA). A plausible but unverified identifier is noise, and we
will count it against the report. If you cannot cite a line, do not assert the
thing. The previous pass failed on inference-from-structure; that is the one
failure mode we are guarding against.

---

## 2. What this project is

**AEGIS** is a doctoral research project: a methodology plus an executable
pipeline that turns a small company's profile into a defensible, traceable
regulatory compliance specification. It exists because the manual process —
read the regulation, decide what applies, derive requirements, anchor them to
controls, and justify every choice — is slow, inconsistently applied, and
usually undocumented in the part that matters: *why* a requirement exists and
what would count as satisfying it.

The methodological claim of the thesis is not "the pipeline works". It is that
**a compliance derivation can be made auditable and reproducible**, and that
the instruments used to claim it can themselves be measured rather than
asserted. That second half is why the repository is as full of preregistrations,
falsifiers, negative results and instrument-validity experiments as it is of
pipeline code.

### 2.1 The chain

There are **three phases and no Phase 4** (researcher ruling, 2026-09-30; the
master design and manuscript #05 say so; `AGENTS.md` and ADR-006 still say
otherwise in four places — an uncorrected contradiction, see §6.8).

| Phase | Input | Output | Identifier scheme |
|---|---|---|---|
| **Fase 0 — Baseline** (frozen, inherited by reference) | Regulatory corpus, verbatim articles, ambiguity analysis | Baseline Goals (regulation-neutral + per-regulation) | `SO-D-XX.Y.HL`, `SO-D-XX.Y.<REG>` |
| **Fase 1 — Contextual Definition** | Baseline Goals + company context | Adjusted Goals | `AG-D-XX.Y-NNN` (9-column table) |
| **Fase 2 — Operationalization** | Adjusted Goals + obligations + tensions | Security & Privacy Operational Objectives, with testable verification criteria | `PO-/SO-D-XX.Y-NNN`, `PRIN-ENG-01..07` |
| **Fase 3 — Specification** | Objectives + rules | **Part 1**: Security & Compliance requirements + Organizational requirements. **Part 2** (gated): Threat & Risk analysis | Part 1: `REQ-D-XX.Y-NNN` (practice `R<n>`); Org: `ORG-D-XX.Y-NNN`; Part 2: `TM-D-XX.Y-NNN` |

Each phase's output is the only unit the next phase consumes. Company context
enters exactly once, in Fase 1. Regulations and control anchors ride the chain
as citations, never as work units.

### 2.2 The baseline layer (`baseline/`, frozen)

- **10 domains, 38 sub-domains** (`D-01.1` … `D-10.3`), each in a modular,
  regulation-pure layout: `objective.md` (the regulation-neutral Baseline Goal),
  `regs/<REG>.md` + `regs/<REG>.ambiguity.md` (per-regulation Sub-SO card,
  security requirements, verbatim regulatory basis), `cross/<R1>-<R2>.md` +
  `cross/_interactions.md`, and `articles/` (verbatim article copies).
- **5 regulations** treated as active: GDPR, CRA, NIS2, DORA, AI_Act.
- **Ambiguity registry**: 49 clause cards, each obligation that touches an
  ambiguity must point at a card rather than re-derive an interpretation.
- **15 control referentials** under `baseline/CONTROLS/`. Three are *enforced*
  (NIST CSF 2.0, NIST PF 1.1, NIST AI RMF 1.0) and twelve are *advisory*
  (NIST SP 800-53r5, NIST SSDF, NIST AI SSDF, OWASP ASVS, OWASP SAMM,
  ISO/IEC 27001:2022, ISO/IEC 27701:2019, ISO/IEC 42001:2023, CIS Controls v8,
  BSI IT-Grundschutz, ENISA, QNRCS). Rule R2b: a cited advisory identifier must
  exist as a JSON file under the corresponding subtree. **R2b checks existence,
  not correctness** — that is precisely how the four defects in §7 survived.
- **SR↔control mapping store**: 282 security requirements (`SR-<REG>-NNN`)
  extracted verbatim from the frozen per-regulation dashboards, each with its
  source clauses, published NIST CSF / NIST PF / NIST AI RMF anchors, and
  unmapped markers. A flat `traceability.csv` view exists with 134 rows.
- **Control referentials are generated**: `scripts/specs/<framework>.yaml` is
  the source of truth; `scripts/generate_advisory_framework.py` emits the JSON
  tree. The specs are where the defects in §7 live, which means each fix is a
  spec edit plus a deterministic regeneration, not a hand edit of 33 files.

### 2.3 The executable layer (`pipeline/`)

`pipeline/src/aegis_pipeline/` — a package with six sub-packages:
`core/` (config, trace, llm_client), `observability/`, `guards/`
(control resolution, L1 validation, quality gates), `phases/phase1/`,
`phases/phase2/`, `phases/phase3/`, `cli/`. Twelve legacy flat modules remain
as back-compatibility shims because the Slurm launch scripts and the test
suites import them.

Tests: twelve files under `pipeline/tests/`, 102 `test_*` functions, executed by
per-file `__main__` runners (there is **no pytest** and **no `pyproject.toml`**
in this repository — both facts are true and both matter; see §6.9).

Execution: the pipeline runs on a Slurm cluster (Deucalion, A100 nodes) serving
`qwen3.8:27b` through Ollama / vLLM. Every run is seeded (`seed=42`,
`temperature=0.2`) — a *measured* default, not a preference: EXP-02 showed
that a fixed seed makes the pipeline bit-reproducible, that all variance is
sampling-driven, and that unseeded runs abort at 40% on a grounding gate.

### 2.4 The three cases

`cases/Case_01_TinyTask_SaaS` (8 people, 2 regulations), `Case_02_SecureBorder_Solutions`
(450 people, 4 regulations), `Case_03_OmniBank` (5 000 people, 5 regulations).
Each carries hand-written reference deliverables that are **frozen ground
truth** for comparison, plus a deterministically composed `filtered_corpus/`
slice (regulation-pure, verbatim, no summaries).

---

## 3. The reading plan

Read the published tree: branch `master` (default) and
`feat/phase3-part1-coverage-mapping`. The baseline layer is identical on both;
the pipeline code differs by roughly eight days of work from the current local
tree, and the uncommitted local changes are **not** published — treat
`pipeline/` as eight days stale and say so where it matters.

Read in this order:

1. `AGENTS.md` — the operational contract. §-1 (sampling defaults), §-2
   (scientific conduct, six numbered rules), §3 (three natures of information),
   §4 (the Phase 1 workflow), §5 (rules R1–R13), §6 (phase boundary and the
   pipeline I/O contract).
2. `SPEC.md` — the pipeline specification and the derivation rules.
3. `docs/pipeline/00_PIPELINE_MASTER_DESIGN.md` and
   `docs/pipeline/07_PHASE3_PART1_PLAN.md` — the architecture and the corrected
   Phase 3 Part 1 plan.
4. `docs/experiments/00_RESULTS.md` — the results panel: every experiment, what
   it tested, how, what came out, what it means. Then the individual
   `*_results.md` documents for the ones named in §5.
5. `docs/research/10_SCIENTIFIC_METHOD_ALIGNMENT.md` — the method alignment
   (SM-001..SM-011), and `docs/research/sources.yaml` — the source registry
   (323 entries, each with `id`, `kind`, `evidence` grade, `url`, `supports`,
   `status`, `recheck_after`). `scripts/check_research_refs.py` enforces its
   integrity (rules R1–R7).
6. `docs/decisions/` — 13 ADRs, `ASSUMPTIONS.md` (A1–A7 with signposts), and a
   pending decision packet.
7. `pipeline/src/aegis_pipeline/phases/phase3/` — the Phase 3 modules, and
   `pipeline/tests/phase3_gate_test.py` (unpublished in the working tree; the
   published branch has the older gate).
8. `baseline/CONTROLS/` and `scripts/specs/` — for A1.

---

## 4. The methodology contract you are auditing against

This is not decoration; these rules are enforced by code and by CI-style
checkers, and several of them exist because the corresponding failure was
measured.

1. **Anchors are mandatory.** Every claim about the pipeline or the corpus
   carries a verifiable anchor: `[S-nnn]` from `docs/research/sources.yaml`, an
   `EXP-xx` measured result, or a checker verdict. Prose without an anchor is
   opinion and says so.
2. **Thresholds declare their basis.** Every parameter a gate applies has a row
   in `docs/experiments/METRICS.md` stating its basis: `measured: EXP-xx`,
   `incident-calibrated: job-xxxx`, or `convention, unmeasured → E-xx`. A
   threshold with no declared basis may not be cited as evidence of quality.
   (Today, the flagship 0.88 near-verbatim limit and the 0.30 retention floor
   are tagged `convention → E-10`; they are conventions, not measurements.)
3. **Preregistration before data.** Every experiment runs under a frozen
   preregistration with a version; deviations are recorded in the results
   document, never silently. `scripts/check_results_prereg.py` enforces that
   results documents cite the preregistration and its version.
4. **A negative result is a result.** A fired falsifier, a refuted hypothesis
   or an aborted run enters `00_RESULTS.md` in the same session as the
   analysis, with the same prominence as a positive result.
5. **Decisions carry a signal.** Every ADR has a falsifiable predicted
   consequence and a *signpost* — a pre-agreed condition that reopens the
   decision rather than defending it. Assumptions live in
   `docs/decisions/ASSUMPTIONS.md`.
6. **Adversarial review is mandatory, anti-sycophancy is a rule.** No review
   may conclude "everything looks conformant" without stating the stress tests
   and friction points. The council lenses are Contrarian, First Principles,
   Expansionist, Outsider, Executor. Mechanical passes (`doc_lint.py`, regexes,
   table checks) verify syntax, never substance.

And the invariants that matter for your review: R2 (anchor integrity — no
invented anchors), R5 (strict technology neutrality in Phases 0–3), R6 (no fact
invention; assumptions prefixed), R9 (case-level composed corpus slices, zero
summaries), R10 (physical inspection of generated files; anti-circular testing),
R10b (the four universal optimization invariants: operational delta, separation
of classification from narrative, mode-collapse ceiling 60–70%, cross-field
consistency), R11 (no editorial meta-commentary in documents), R12 (no
unresolved placeholders, every cited control path must resolve).

**The core tension you should keep in mind:** the repository is rigorous about
*process* (preregistration, anchors, falsifiers) and comparatively weak about
*substance* (whether the produced requirement is actually a good requirement).
Several of the sharpest findings in §5 and §6 are exactly that asymmetry: a
document passes every gate and rests on something nobody measured.

---

## 5. The measured state (what the experiments established)

All of these are in `docs/experiments/`, preregistered, with the falsifiers
frozen in advance. Numbers are quoted as measured.

**Pipeline behaviour**
- *EXP-02 (seed as reproducibility).* 3 arms × 15 runs. Seeded runs produced
  **byte-identical goal sets** (retention 0.7171490955644458 to full float
  precision); the unseeded arm spread 0.7131 ± 0.0086 and **aborted at 40%**
  on the R6 grounding gate. Zero residual serving-layer variance.
- *EXP-01 (pipeline vs agent).* Same case, same model, same gates: the
  tool-calling agent needed **5.2× the calls** (220 vs 42) and 2.8× the wall
  time, and produced the same structure. The *output contract*, not the
  orchestration, determines the document's shape.
- *EXP-03.* At n=15 the agent arm does not produce the same document
  (retention 0.7851 ± 0.0182 vs 0.7171 ± 0.0000) and terminates cleanly in
  **7/15** runs. It is off the production path on the researcher's decision,
  for reproducibility semantics rather than cost.
- *M02 matrix (6 models × 3 cases).* Only the reference cleared all three
  cases. Every remaining failure is a gate working, not infrastructure.

**Instrument validity** — the calibration claims rest on one number, so the
number was audited.
- *M07 (badge instrument matrix).* 7 of 18 cells delivered; the reference
  cleared all three cases for the first time. But the `(unchanged+verbatim)`
  share is **0.86–1.00, median 0.99**, with **zero** `proportional` and zero
  `inherited` rows in the entire matrix. A richer classification vocabulary
  changed nothing about default collapse.
- *M09 (removing the literal exemplars).* **H1 refuted**: three of four
  falsifiers fired; collapse got *worse* in both cases (0.978→0.989,
  0.964→0.984) while retention rose. The exemplars were load-bearing for the
  retention floor.
- *M10 (is the instrument measuring anything?).* Against a cross-sectional
  placebo (same model, same company, genuinely different duty): the
  `Adjusted goal` column separates the company **+0.188** (0.249 vs 0.061); the
  `Company implication` column separates it **+0.002** (0.062 vs 0.061). The
  replication floor — same model, same duty, same company, written twice — is
  0.295. The badge classifier itself is correct 15/15 on known-answer vectors.
  So the badge is sound, and `unchanged` is an accurate report about a column
  that genuinely has little company-specific content.
- *M11 (asking for a named artefact).* **Refuted**: divergence +0.031 against
  its own control's +0.042. Two prompt interventions in that column have now
  failed to move it. The remaining hypotheses are structural, not prompt-shaped.
- *2026-10-21 (today's laboratory finding).* Two open-weight decision models
  reproduce the badge collapse with an **independent instrument** — both
  classify the three baseline→goal pairs as "verbatim", including the one that
  drops a mandatory leg. The collapse is in the Phase 1 goal text, not in the
  badge parser. The same run found the pipeline emitting tension rows whose
  conditions do not activate, contradicting its own contract, where the
  decision models were right 2/2.

**Phase 2**
- *P2-01.* Supported. 99 and 129 objectives, `grounding_ratio` 1.0, mean
  cross-case similarity 0.072 — Doc02's `Constraint` column names each
  company's own architecture and nothing shared.
- *P2-02.* **Partial.** The `RULE-*` tail now exists (699 rules, zero EARS
  violations). Two registered bars fired: the rule catalogue is **padded**
  (every objective carries ≥2 rules against a spec of 1–2; mean 3.07/3.16
  against a ceiling of 2.5 — each rule is a valid sentence, so no gate can see
  the excess), and `D-03.3` was lost on Case 03 because the p4 repair message
  (tuned for tabular extraction) pressured the model into dropping the whole
  `rules` array. A token-level grounding gate was measured and **rejected**:
  it fires on 37 of 37 good translations.

**Phase 3 Part 1** — see §6.

---

## 6. The open problems, ranked, with evidence

### 6.1 The gate is honest, the system is not closed
The exit gate says `PROPOSED`, not `CONCLUDED`, and it is blocked on a human.
`weave.run_gate()` reads seven artifacts from disk, calls the model **zero**
times, and hashes its inputs into an `inputs_digest`. Its verdict is a pure
function of the disk. As of the last run (`run_p2enr_c1`):

| Gate | State | Why |
|---|---|---|
| G1 | **OPEN** | 7 principles unplaced (the ADR requires every objective *and every principle* placed) |
| G2 | **OPEN** | 7 verdicts missing — the round has not converged |
| G3 | CLOSED | the only gate that measured substance (anchor provenance, T6) |
| G4 | CLOSED | document lint over the run's own deliverables |
| G5 | OPEN | per-regulation verdict lines identical (the renderer emitted the global total twice) |
| G6 | CLOSED | one absorption row per accepted constraint |

The root cause of the original false green was **not** the gate logic — the
branch was correct — it was the absence of **invalidation**: a `CONCLUDED`
verdict stayed readable after its inputs changed, so `manifest.json` carried
`p3a_gate: ok` and `p3a_round: partial / 7 open` side by side. The fix is a
digest plus a single choke point that marks a gate stale when another stage
writes afterwards.

### 6.2 Five of six gates measured existence, not substance
In the published code: G5 and G6 were `is_file()`. G4 invoked
`doc_lint.py --strict` with no positional scope, so it linted the hand-written
corpus and **zero bytes of the run**. G1 counted objectives and was blind to
principles. G2 counted a verdict file that had been superseded. The working
tree (unpublished) hardens G1, G4, G5 and G6, and adds the falsification
battery. **This is where A3 applies.** The lesson generalizes: *a gate that
validates the existence of a file or the shape of an enum does not validate the
deliverable; the test of a gate is that it fails when it should — and that has
to be proven by running the new test against the old code.*

### 6.3 The judge is asked to measure against an input it never receives
This is the most important measured finding in Phase 3, and it is not a model
bias. The first real run of the coverage matrix carried 37/37 sub-domains with
zero findings — and produced:

| Verdict | Generated | Hand-written reference |
|---|---|---|
| Fully covered | **0** | 6 |
| Partially covered | 13 (20%) | 19 (31%) |
| No functional carrier (organizational) | **52 (80%)** | 32 (52%) |

Agreement by verdict family: **21/62**. Grepping all 89 packs for
"verification criteria" returns **zero occurrences**: ADR-007 defines coverage
as *the union of the carriers' fit criteria reconstitutes the objective's
verification criteria*, and the criteria were never in the pack. "No carrier" is
the honest, literal answer to that input. Re-aggregating the 75 verdict files
later reproduced the distribution exactly (52/13/0/0/0).

**No judge recovers information that is absent from its input.** Before
changing the model, widen the pack. A vocabulary patch (`RN (a derivar)`) was
tried and **refuted by measurement**: 52→51 organizational, 0 uses of the new
value. A closed vocabulary without a value for "pending / not yet derived"
pushes the model to the nearest wrong member, and the result looks like model
conviction when it is a hole in the schema.

### 6.4 The product-vs-organization split is a methodology decision, and it is open
Under the CRA the manufacturer answers for the product it places on the market;
in a hosted SaaS the protection belongs to the infrastructure. Two independent
readings (in different sessions, different stages) chose the infrastructure
reading. Both are defensible; the methodology does not decide between them; and
`check_traceability` T5 flags the inconsistency between the generated Doc03 and
the hand-written matrix. This one is the researcher's, not a prompt fix.

### 6.5 The badge collapse is a contradiction inside our own prompt (measured 2026-10-21)
The `unchanged` collapse is not a model problem. For the *same column*, the
template (`templates/doc02_adjusted_goals.md:63`) declares the vocabulary
`unchanged | narrowed | flagged`, the worked example uses that form, and the
instruction (`pipeline/src/aegis_pipeline/phases/phase1/goals.py:267-272`)
requires `proportional | inherited | flagged | —` and says explicitly *"Do not
paste empty 'unchanged' labels without rationale"*. The gate
(`guards/quality_gates.py:44`) accepts `unchanged`. A measurement with a
different hosted model: 5 of 6 rows came out `unchanged`, and the single
`narrowed` row used the template's exact wording. **The model follows the
example, not the instruction.** The repair is to make template, example and
instruction say the same vocabulary — and to decide explicitly whether
`unchanged` is legal.

### 6.6 Phase 2 is mostly a rename of Phase 1
Phase 2's `Operational Statement` column is a byte-for-byte copy of Phase 1's
`Adjusted Goal` (sorted-multiset md5 identical across two cases). The `RULE-*`
tail that the SPEC assigns to Phase 2 — the only artifact that would
differentiate it — had **zero occurrences in six hand-written deliverables**.
ADR-013 de-scoped `RULE-*` and named Doc02's `Constraint` column as the
generative cell. The three columns left without a rule (`criteria`, `method`,
`owner`) were resolved **by measurement, never by prompt**: the best candidate
rule reached 0.82 on one case and 0.55/0.57 on the other two — three cases
show that a rule was *followed*, not that a rule exists. Those three columns
stay `—`.

### 6.7 The verification criteria are template text
The 62 Phase 2 `Verification Criteria` in Case 01 are two boilerplate sentences
with the objective's own name substituted ("automated check or audit confirms
that *<name>* is enforced for all personal data flows") — 62/62 in Case 01,
63% in Case 02, 48% in Case 03. The ADR-007 D2 reconstruction is therefore
not executable with the data we have. The term "discharge-verified" was
demoted to "discharge-anchored" in the matrix, with the reason in its preamble.

### 6.8 The repository contradicts itself about Phase 4
The master design and manuscript #05 say the chain ends at Phase 3; `AGENTS.md`
(lines 329, 341, 355) and ADR-006 D3 still describe a "Fase 4 — Verification &
Implementation". `AGENTS.md` is the first contract an agent reads. Four
one-line amendments would fix it; they have not been made.

### 6.9 The test harness has no safety net
No `pyproject.toml`, no pytest, no shared fixtures: each test file is a script
with its own runner, and **the position of the runner is part of the contract**.
A test file once had its `__main__` block in the middle, so two tests defined
below it never ran — and the suite printed `OK`. When the runner was moved to
the end, one of the two failed on the first execution: a real defect
(`maturity.py` did not clamp `nivel_atingido` to the assessed tier). The
transferable rule: *count the tests that ran against the tests that exist before
quoting a green suite.*

### 6.10 The referential layer's normative fidelity
See §7. Four defects were confirmed, all in the frozen layer, all passing our
own checks — because R2b verifies that a cited advisory id *resolves to a file*,
not that it points at the right place in the standard. Two were corrected on
2026-10-21 (ADR-014: the ISO/IEC 42001 section shift and the BSI family that
contradicted a published module code); two remain open and need the published
text: the synthetic ISO/IEC 27701 identifiers and the uninstantiated CIS
safeguards. This is A1.

### 6.11 Other known gaps, for completeness
- The Phase 3 Part 2 (threat and risk) is parked behind the Part 1 exit gate.
- The blind L2 scoring instrument is rebuilt and verified, but **no scores have
  been entered** — so the programme has no independent quality verdict on the
  documents it has produced. This is the researcher's own work, ~2 hours, and it
  is the single missing piece of the quality claim.
- The `nivel 1` share (83.3%) sits below the ADR-009 expectation (>85%).
- `PROC-01..PROC-05`, named by ADR-009 D3, do not exist in the Doc00; `RN29` is
  orphaned.

---

## 7. Verification of the first external review

Every claim from the earlier review, checked against the actual tree. This is
recorded so you do not repeat the disproved ones, and so the confirmed ones get
the attention they deserve.

> **Two of the confirmed defects were corrected after this table was first
> written** (ADR-014, 2026-10-21). The corrections are in the generator specs and
> the tree was regenerated deterministically. Read rows 3, 4, 5 and 6 carefully:
> two of them are closed with a stated residual, and two are still open and are
> the ones we need you to settle.

| # | Claim | Verdict | Evidence | Action |
|---|---|---|---|---|
| 1 | Root contains only `audit_runner.py`; no Python package; no tests | **REFUTED** | `pipeline/src/aegis_pipeline/` — 47 modules in 6 sub-packages; `pipeline/tests/` — 12 files, 102 `test_*`; `audit_runner.py` is a legacy one-shot with a hardcoded `C:/Users/…` path | discard the architecture review |
| 2 | No `pyproject.toml`, no `schemas/` directory | **CONFIRMED** | never existed in git history; `phase3/schemas.py` is a module, not a directory | noted; packaging is not the gap (§6.9) |
| 3 | ISO/IEC 42001:2023 annex numbering shifted by +3 (A5–A.10 instead of A.2–A.7) | **CONFIRMED — and the error was inside the data, not just the folder names** | `scripts/specs/iso_42001_2023.yaml:4` hardcoded the wrong scheme; the generated `A5_POLICIES/A.5.1.json` carried `control_id: A.5.1` and `informative_references: ["ISO/IEC 42001:2023 Annex A.5.1"]` while its text is the published **A.2.1** control. Published sections A.8 (Information for interested parties), A.9 (Use of AI) and A.10 (Third-party and customer relationships) were absent entirely. 33 controls, none with a correct id. | **CLOSED 2026-10-21 (ADR-014 D1–D2).** Every control is now aligned to the published **section** its own text carries (A.2–A.8), references cite the section rather than a published control number, and the intra-section ordinal is declared a **local subset ordinal**. **Residual, and the question for you:** the published Annex A control list. Sections A.9 and A.10 are still unrepresented, and the ordinals within A.6 (13 local controls) need the published list to become real. |
| 4 | BSI IT-Grundschutz: CON renamed `CON_CONTAINERS`, DER renamed `DER_DIRECTORY` | **PARTLY CONFIRMED — and the claim about CON was itself wrong** | `scripts/specs/bsi_grundschutz.yaml` mapped `CON → CON_CONTAINERS / "Containerisation"` and `DER → DER_DIRECTORY / "Directory Service"`. The `DER` half holds: the published layer covers detection and response, while the cards describe an identity directory, a PKI and a federation. **The `CON` half does not hold**: the 2023 Compendium's `CON` layer is the containerisation layer, and the cards (Kubernetes, registry, service mesh) are consistent with it — the folder name was right and the claim about it was not. What *was* wrong in `CON`: hyphenated ids (`CON-1.json`) against `APP.1.json` everywhere else, in a card that itself cites "BSI IT-Grundschutz CON.1". | **CLOSED 2026-10-21 (ADR-014 D3).** `CON.1`–`CON.3` use the dot convention; the `DER` family was renamed `IDM` (`IDENTITY_AND_KEYS/`) with no published Baustein id asserted. **Assumption A10** registers the CON layer reading as unverified-here, with a signpost. **Question for you:** where identity, PKI and federation actually live in the published Compendium, so the family can be re-filed against a real Baustein. |
| 5 | ISO/IEC 27701:2019 numbering is synthetic | **CONFIRMED (ids are synthesized; the correct published ids still need the standard)** | `A5_PII_CONTROLLERS/A.5.34.1.1 … A.5.34.8.1` and `A6_PII_PROCESSORS/A.6.34.1.1 … A.6.34.11.1` — a four-level scheme that exists in no published standard, and it collides with ISO 27001:2022's own `A.5.34`. The generator spec even miscounts itself ("26 controls" for 22 present). | **needs the published text** |
| 6 | CIS Controls v8: 18 top-level files, none of the 153 safeguards | **CONFIRMED** | `baseline/CONTROLS/CIS_CONTROLS_V8/01_INVENTORY/01.json` … `18_PEN_TESTING/18.json`; ids are the bare strings `"01"`…`"18"`; the Implementation-Group split survives only as three strings inside `implementation_examples` | scope decision |
| 7 | OWASP ASVS: only the `.1` requirement of each subsection exists | **REFUTED (over-generalized from V12)** | 83 leaf files; 16 ids have a non-`.1` third component (`V1.1.2`–`V1.1.5`, `V2.1.2/3`, `V4.1.2/3`, `V4.2.2`, `V5.1.2`, `V6.2.2/3`, `V7.2.2`, `V8.2.2`, `V9.1.2`, `V11.1.2`); 10 subsections carry siblings. V10, V12, V13, V14 are `.1`-only. | corrected |
| 8 | `NIST_AI_RMF` and `NIST_PF` have neither an aggregator nor a `_MANIFEST.json`; `NIST_CSF_2.0`'s aggregator is `CSF_2.0.json` | **CONFIRMED** | 13 of 15 frameworks have `<FRAMEWORK>.json` + `_MANIFEST.json`; NIST_AI_RMF and NIST_PF have neither — and they are two of the three *enforced* referentials. `scripts/verify_no_loss.py:440` loads `CONTROLS/NIST_CSF_2.0/CSF_2.0.json` by that exact name. | housekeeping |
| 9 | `ENISA/NIS2_BASELINE/` turns NIS2 Art. 21(2) into ENISA "controls" | **CONFIRMED in kind** | 11 files `NIS2-21-1.json`…`NIS2-21-11.json`, each `framework: "ENISA Advisory"`, `source_url` a topic landing page, `informative_references` pointing back at NIS2 Art. 21(2) — legal text wearing the control schema. Nothing outside the folder consumes these ids (the real NIS2 chain uses `SR-NIS2-001..045`). | decide |
| 10 | `baseline/MAPPINGS/OVERLAYS/` mixes a binding regulation with three voluntary frameworks | **PARTLY TRUE, wrong reason** | The four overlays are scope-modifier + mapping tables, and their headers *do* distinguish "Camada 2 — legal, obrigatório" from "Camada 3 — best practice, optional". The real defects: the declared `Source-of-truth:` paths do not resolve inside this repository, no code reads the directory, and the binding AI Act overlay is the one with no catalog behind it (there is no `AI_ACT` directory under `CONTROLS/`; the three NIST ones duplicate existing catalogs under a different schema). | fix provenance |
| 11 | Legal articles are physically duplicated across sub-domains (single-source-of-truth violation) | **TRUE as fact, WRONG as diagnosis** | 623 article files, 137 unique basenames, 137 unique hashes — byte-identical everywhere, up to 28 copies of one article; 37.7 MB total vs 3.5 MB unique (90.8% redundant). But the copies are frozen corpus material, the case slices are composed by a deterministic script, and `scripts/verify_no_loss.py` verifies article content equality per file. This is storage bloat and path coupling, not hand-maintained drift. | not now |
| 12 | `regs/` holds empty ~80-byte stubs for regulations that do not apply | **REFUTED on both details, but the substance survives** | No file under `regs/` is under 250 bytes (smallest 281). 101 of 374 are explicit not-applicable records (`_(no AI Act Sub-SO or requirements in this sub-domain)_` / `_No applicable AI_Act ambiguity._`), D-06.4 carries only 4 of the usual 10, and every `D-XX.manifest.json` records the sparse intent. The real residue: 30 of the 55 `.md` stubs carry no reason. | minor |
| 13 | Pairwise `cross/` files explode combinatorially and lose n-ary information | **REFUTED** | 238 files = 200 pairs + 38 `_interactions.md`. The pairs are bounded at C(5,2)=10 per sub-domain, and `_interactions.md` *is* the n-ary layer: all 38 contain a "Scope-overlap matrix (5×5)" with real cells, "Aggregation logic", and "Emergent tensions" sections; 23 files carry explicit n-ary machine tags (`<!-- emergent: GDPR,NIS2,CRA,DORA,AI_Act -->`). The structure you proposed already exists. | discard |
| 14 | Only D-01 has a manifest | **REFUTED** | All ten `D-XX.manifest.json` exist with a uniform 15–16 key schema including `modular_layout` (per sub-domain: files, per-regulation `regs` counts, `cross_pairs`, `demoted_units`, `dedup_lines`, `balanced`). | discard |
| 15 | The MAPPINGS sidecars are leftover intermediates | **PARTLY REFUTED** | `_m9_partial_coverage_sidecar.json`, `_uniformization_changes.json` and `_control_uniformization.md` are **load-bearing inputs of `scripts/verify_no_loss.py`**; removing them breaks the no-loss check. `_nomenclature_sidecar.json` is a genuine orphan (0 consumers, 0 rewrites). | delete one orphan |
| 16 | The regulation-pivot in `sr_control_mappings/` discards the sub-domain abstraction | **PARTLY REFUTED** | The pivot is real and hard-coded at two call sites, but every record retains `sub_domain[]` and `linked_objectives[]`, and a flat regulation-as-column view already exists (`traceability.csv`, 134 rows against 282 SRs — incomplete). | partial |

**The lesson from this table.** The findings that survived are the ones where
you compared a *published external artifact* against the repository's claim
about it. The findings that died are the ones where you inferred structure
from directory listings. That is where your comparative advantage lies, and it
is also where the risk of a confident, wrong answer lies.

---

## 8. What we know that the repository does not show

These are the distilled lessons of two months of work. They are the difference
between advice that fits this project and advice that reads like advice for
any project. **Please read them as constraints on your answer, not as
background.** Several of them describe failures that cost real runs, real
cluster time, or real results.

### 8.1 How to work with the researcher (how to write your answer for him)

- **Register matters as much as volume.** Four separate reporting failures had
  the same shape: the report was accurate, used the repository's own
  vocabulary (`Doc03`, `T5`, `signpost`, `ORG`, `RN18`), and was therefore
  unreadable to the one person it was written for. A fifth failure was the
  opposite: a long list of real edits read as substantial work when the named
  target was never in scope. **Open with the answer to the question that was
  asked, in plain words. If the question was "did you build it?", the answer is
  "No. Zero lines." — then the inventory.** Never leave a bare acronym in a
  summary; expand the repository's terms on first use.
- **A status report must be readable as an answer to "what is going on?"**
  Open with three lines: what the programme is, whether it is finished, and
  what is waiting on him. Only then the delta.
- **Inventory before verdict.** When reporting an experiment, give the run
  inventory first — model, case, arm, job ids, commit/rev, n — one line per
  cell, *before* any interpretation. He tracks which model ran, because the
  model is the variable that decides everything in the matrices. Close by tying
  the verdict back to the concern he originally raised, not merely to the
  falsifier.
- **When you answer a question twice, stop offering menus and measure.** Three
  options with "I recommend #1" are still three options; a measurement that
  eliminates the alternatives is one answer. If the answer needs a number you
  do not have, go and measure it — it is almost always cheaper than asking and
  almost always changes the conclusion. When a measurement destroys your
  previous hypothesis, say that first, without hedging.
- **"I don't know" and "I decided by instinct" both delegate the judgement to
  you.** Do not offer a menu. Give the recommendation with the reasoning, and
  when he asks you to evaluate decisions he made by instinct, separate them
  into *right*, *defensible*, and *what I would not do* — the last one with the
  concrete failure mode, not a vague "that could be problematic".
- **Never register your own exclusions.** If the scope (which cases, which
  arms) came from him, do not reduce it — not even by stamping the reduction
  as a "registered exclusion" in the preregistration. A preregistration is
  where a *researcher's* decision is recorded, not where an agent archives its
  own. A case that does not complete is a result, not a reason to swap it for
  one that does. And when a prerequisite looks blocked, check whether valid
  artifacts from that stage already exist elsewhere — twice, the real cost was
  re-running a whole upstream phase instead of using the runs that were
  already on the machine.
- **A premise in the instruction can be false; correct it and still do the
  work.** Do both, in that order, and say explicitly which part the false
  premise blocks and which part it does not.
- **Dispatch, do not leave pending.** When the deliverable includes a cluster
  run, submit it before the day ends, and report what is actually running and
  what failed — with the scheduler's own account (`sacct`: `CANCELLED /
  Reason: Dependency` means the dependent never started; `FAILED` means it ran
  and died). Those are opposite conclusions about whether a stage was tested.
- **"It is gated" is not permission to stop.** Do the part that is unblocked and
  declare what is blocked. Do not use a gate as a reason to do nothing.

### 8.2 Method, instruments, anti-sycophancy

- **Never optimise for passing a gate without asking what the gate measures.**
  A council of five lenses concluded that the two Phase 1 adjustment gates do
  not measure the objective at all: both compare a row against its *own*
  baseline objective, neither mentions the company, and one has 58 points of
  slack with no measured line ever approaching it. Three successive prompt
  experiments then re-found the same number without varying the *measurement*.
  A gate that is always green is not evidence — it is an absence of
  discriminating power.
- **A check that cannot fail is worse than no check.** Three occurrences:
  a `tsc` invocation that verified zero files because the workspace config had
  `"files": []`; a test runner positioned mid-file so the tests below it never
  ran while the suite printed `OK`; and five tests written against a defect that
  had already been fixed, which passed on first execution and proved nothing
  until the *old* renderer was run against the same input and failed. **The
  test of a gate is that it fails when it should, and that has to be proven by
  running it against the old code.**
- **A verifier is a hypothesis about the format, not the format.** We once
  accused a source of dangling references when it actually wrote `GR. SP-1`
  with a space. When a check accuses a source, verify against the source
  before publishing the accusation.
- **Naming a prohibition without offering the replacement does not move the
  model.** The repair message that said only "technology vocabulary" left the
  model to fetch a solution from memory; adding the ratified prohibited →
  mandatory table (with the substitution in bold) fixed it. And **do not show
  the forbidden form in order to forbid it** — displaying `GV.RR-2` to say
  "not this" is an invitation to copy it, which was the cause of the first
  failure.
- **Before blaming the instruction, ask what valid content was on the page.**
  This happened three times: the anchor-resolution stage failed 21/21 because
  the pack carried no anchors at all (the code comment claimed it did — the
  comment was false); the coverage matrix diverged because the pack lacked the
  verification criteria the judge was told to measure against; a candidate
  filter offered a sub-domain whose regulation module declared no
  sub-objective, and the model's answer ("none") was *correct*. The hole was
  the schema or the pack, never the wording.
- **Never normalize a spelling by computation — always by a search against the
  corpus.** A one-digit suffix is tolerated only if the two-digit form exists as
  a file. Aligning `PR.IP-1` (a CSF 1.1 identifier) to `PR.IP-01` would dress a
  wrong-framework id as a typo and let it pass the anchor rule. An invented
  anchor that looks anchored is worse than a missing one.
- **Instrument validity before content.** The badge classifier was audited
  against known-answer vectors (15/15) before any conclusion was drawn about
  the 0.99 collapse. The subsequent audit showed the *goal text* carries the
  company and the *implication column* does not — so the collapse is an
  accurate observation, not a parser artefact.
- **Changing the instrument and the object in the same pass makes both
  illegible.** The anchor fix had to inject the anchors first, run, and
  measure, because normalizing digits first would have fixed 9 of 19 failures
  and destroyed the ability to tell whether the pack fix worked.
- **Mode collapse has a ceiling.** A passive default may not exceed 60–70% of
  an evaluated batch without an explicit calibration-collapse warning. The
  badge collapse sits at 0.99 and fires the warning on all 18 runs.

### 8.3 Architecture and harness traps we have already paid for

- **The prompt is four pieces and the site only showed one.** The system prompt
  is *generated in code* (role + mission + a general discipline block); the
  user message is assembled from a task header, the *ficha* (prompt body +
  output schema + self-checks), and the attached pack. Six Phase 3 fichas had
  **zero** mention of technology neutrality, because that rule lived only in the
  code-generated block. If you propose prompt changes, remember the ficha is
  only one of the four pieces.
- **Two state sources, and the derived one becomes the only living
  reference.** A stage wrote both the parsed slice and the accepted verdicts;
  the resume marker was the second. Archiving the first and resubmitting
  reported "37/37 carried, 0 failed" **without a single model call** — the run
  was honest, it ratified what it had on hand. **An artifact a stage consumes
  is that stage's definition of done.**
- **The fact sheet has exactly one reader.** It is not strict YAML (a scalar
  containing `: ` without quotes); Phase 1 validates it with a simple parser
  while a different module used a strict loader and broke the stage. Do not
  introduce a strict-YAML dependency without confirming the artifact is strict
  YAML.
- **File naming splits.** The goal files are `steps/goals/*.json` (underscores)
  but `*.md` (dotted); the resume marker checks the dotted one. Deleting only
  the underscored files does not force re-derivation, and a repair that failed
  on the first attempt was caused by exactly this.
- **Models wrap enum values in backticks or bold as often as bare.** The
  repair round reproduced the marking. Clean all marks at the cell boundary
  and never compare the raw string.
- **Non-Latin characters leak into generated prose and every checker passes.**
  Five occurrences in one session (in strings and comments). `tsc`, `vitest`,
  `eslint` and `doc_lint` catch none of them. **Re-read what you wrote.**
- **A failed hook discards the edit silently.** After a large `Edit`, re-read
  the file: the import succeeding does not mean the write landed.
- **The "scale proportionality" judgements are human, not thresholds.** Six
  organizational obligations had to be judged by the researcher (R3), and the
  judgment is not derivable from a rule.
- **The NIST PF axis was silently dropped for a week.** `goal_anchors()` read
  only `nist_csf`, so the whole chain (goals → Phase 2 → matrix → packs →
  verdicts → proposals) was born CSF-only, despite 100 PF JSONs existing and
  68/68 GDPR mappings carrying PF anchors. The PF axis only accompanies
  GDPR-derived obligations and the AI RMF axis only AI-Act-derived ones — that
  is a published dashboard property, not a free choice.
- **The technology-term guard has a blind spot, by construction.** It is a list
  of *named* technologies (vendors, frameworks, protocols). It cannot see
  pre-baked security ("MFA, encryption, access restrictions" listed as
  things-to-verify), method prescription ("static analysis"), or invented
  identifiers (`key_management`, `operational_execution`). A clean guard is
  not a clean requirement.

### 8.4 Operating the cluster (for context; you have no access to it)

Deucalion is Slurm with A100 nodes serving `qwen3.8:27b` (Ollama, and a
second vLLM 0.32.0 environment). The traps that cost submissions: `STAGE=p1`
is *not* the Phase 1 sweep (the sweep is `STAGE=all`); `--dependency=afterok`
**cancels** the dependent rather than failing it (a cancelled job leaves no log
file at all, which is the forensic signature of a stage that never executed);
a watcher must reach the login node over `ssh`; `sync_up.sh` must carry every
artifact an instrument invokes (the gate failed with `ENOENT` because
`scripts/doc_lint.py` was not in the payload); commit **before** syncing and
check the `.cluster_sync_rev` stamp **before** submitting (twice, a job ran
stale code that reproduced the very error the fix removed); a node that dies
during warm-up burns five retries per call, so cancel and resubmit pinned to a
known-good node; `qwen3.8:27b` will not load on `gnx520` (the API answers in
2 s and the chat endpoint never answers — 175 attempts over 45 minutes); the
login node's Python is 3.6.8 and needs `module load`; `/tmp` is node-local;
and continuing an existing run requires `MVP_RUN_TAG` **and** `MVP_RUN_ID`.

### 8.5 Research threads that exist but are outside this review's scope

Listed so you know they exist and do not re-propose them: a **threat knowledge
graph** in a separate repository (files-first, NeoNeo4j, 3 411 nodes, 16 drift
findings, the LLM phase never run); an evaluation of a **decision model** (Jev —
a TypeSafe System-1 model that reads literal and does not calculate) whose
conclusion survives the open-weight replication: only the tension-activation
step is a real candidate; the **Inspector** (a separate React + API application
that reads the repository and the run directory, showing the pipeline by phase
with the real prompts recorded); the **QNRCS** (Portuguese national
cybersecurity reference framework, Reg. 756/2026, 107 controls, tiered by
entity size — now an advisory referential and the project's maturity
instrument); a **laboratory lane** (`lab/`) for mechanism experiments, whose
conclusion is that text, orchestration and serving schema do not move a
failure; an unrelated civic-tech project (a municipal chamber process); and a
personal knowledge repository of annotated conference talks.

### 8.6 The one decision that is currently blocking everything

Seven principle constraints were proposed by the Phase 3 principle step
(`p3a_prin`, 7/7, zero invented anchors), and each was read by hand: two are
wrong in substance (one authenticates but does not encrypt the channel it
protects; one dresses *our own* EARS writing convention as a client
obligation, which would put a non-existent requirement into the compliance
record), and five need rewording (absolute quantifiers that cannot be
verified, a prescribed mechanism where an objective is required, two invented
identifiers, and a proportionality question about role separation in an
eight-person company). The decision packet is written; the verdicts are not
entered. Until they are, the round does not converge, G1 and G2 stay OPEN, the
`PRINCIPLE_MAPPING` stays a skeleton, and the Phase 3 Part 1 gate stays
`PROPOSED`. **This is the researcher's decision, not an engineering one.**

---

## 9. The output contract

**Format.** Answer in this order, with these headings, no preamble and no
closing summary:

1. **A1 — Referential fidelity.** A coverage table
   (`framework | ids in repo | published ids known | divergences | confidence |
   externally verifiable?`), then one line per finding:
   `ID | framework | type | path:line | literal quote | published value | confidence |
   consumed where | invariant | severity`, then the list of what you could not
   verify and why.
2. **A2 — Architectural weaknesses visible to an examiner.** One paragraph per
   weakness: the claim, the `path:line` that shows it, the mechanism, and the
   consequence for the reader of the produced document. No refactoring
   proposals for the sake of tidiness — a proposal must name the contract it
   would break.
3. **A3 — Gate falsification spec.** For each of G1–G6: the artifact it reads,
   the mutation that must make it fail, the assertion that expresses it, and
   the current failure mode. Then the same for the traceability checks T1–T6
   and the document linter, if you find the same class of weakness there.
4. **A4 — Roadmap.** Ordered, with the cheapest-first rationale, respecting the
   constraints: three phases and no Phase 4; the human decision in §8.6 blocks
   the downstream; preregistrations are frozen and cannot be edited; the
   baseline is frozen and can only be amended by a recorded decision. For each
   item: what it unblocks, what it costs, and what would make it unnecessary.
   Include a short "what we should stop doing" list.
5. **A5 — Thesis risk list.** Ranked. For each: the single sentence an
   examiner would say, whether the answer is to fix, to reframe, or to withdraw
   the claim, and what the fix costs.
6. **Where you were wrong before.** If you disagree with any verdict in §7,
   say so with your own `path:line`. Do not silently comply: §7 is our
   reading, not a script.

**Evidence rules.**
- Every repository claim carries `path:line` and the literal quoted line.
- Every claim about a standard carries a confidence grade (ALTA / MÉDIA / BAIXA)
  and, where you can, the published identifier. If you are unsure, write
  `NOT VERIFIABLE` and move on — a wrong identifier is worse than a missing
  one, because we will act on it.
- Never assert a structural fact you inferred from a directory listing. If the
  only evidence you have is the shape of the tree, that is exactly the failure
  mode of the previous review.
- Separate **what the repository says** (certain — you quote it) from **what
  you infer** (label it as an inference) from **what you recommend**
  (label it as a recommendation).
- When you cannot verify something, say so in one line and continue. Do not
  pad the answer to look complete.

**Style.** No "best practice", no "I would modernise", no restatement of this
briefing, no generic architecture advice. One line per finding. If a
referential is clean, write "no findings" — a clean referential is information.
Assume the reader knows the domain (EU regulation and requirements
engineering) and does not need either explained.

---

*Prepared 2026-10-21 from the repository at `master` +
`feat/phase3-part1-coverage-mapping` (HEAD `3244355`), with eight days of
unpublished working-tree changes excluded from the pipeline description. Every
number in §5 and §6 is traceable to `docs/experiments/` and to the run
artifacts; the parts that are not in the repository are the parts we had to
write down here.*
