---
document_id: AEGIS-PIPE-10
title: 'Pipeline Orientation — what each phase does, and where the seams are'
version: 0.1.0
created: 2026-10-22
status: ACTIVE
upstream:
  - docs/pipeline/00_PIPELINE_MASTER_DESIGN.md
  - docs/pipeline/01_PHASE1_PIPELINE.md
  - pipeline/AGENTS.md
---

# Pipeline Orientation

A functional reference for the execution pipeline: what each phase consumes,
what it produces, which guard measures what, and which seams are known. Written
to be re-read after time away from the repository.

Every claim below carries a `file:line` anchor. Statements without one are
narrative and are marked as such.

## 1. The chain in one view

```
company_input.md
      │
      ├─ p1 ────► fact_sheet.yaml            (LLM)   [G-P1-A]
      ├─ p2 ────► verdicts.md + verdicts.json (LLM)   [G-P1-B]
      ├─ p3 ────► selection.md + .json        (LLM)   [G-P1-B]
      ├─ p3f ───► framing.md                  (LLM)   [G-P1-B]
      ├─ p4 ────► goals/<sd>.md + .json       (LLM)   [G-P1-C]
      ├─ p4t ───► tensions/<sd>.{md,json}     (LLM)   [G-P1-C]
      ├─ p5 ────► doc02_adjusted_goals.md     (code)  [G-P1-C]
      │
      ├─ phase2 ► Doc01_Operational_Objectives.md    (LLM + code)
      │          Doc02_Secure_Design_Principles.md   (LLM + code)
      │
      └─ p3a_cards ► card inventory + V0 baseline     (LLM)
          p3a_map   ► verdicts_<sd>.json + OBJECTIVE_MAPPING.md   (LLM)
          p3a_propose ► proposals_<sd>.json            (LLM)
          p3a_prin  ► proposals_prin_NN.json          (LLM × 7)
          p3a_round ► round1_state.json + ROUND1_REGISTER.md     (code + human)
          p3a_org   ► Doc03_Organizational_Requirements.md       (LLM)
          p3a_weave ► woven cards + Doc01_Requirements_Specification.md  (LLM)
          p3a_gate  ► gate_report.md (G1–G6)          (code)
```

Stage order is fixed in `pipeline/src/aegis_pipeline/phases/phase1/runner.py:1664`
(`P3A_ORDER`). Every Phase 1 and Phase 3 stage is a method of the same
`StepRunner`; Phase 1's orchestrator is 1,830 lines.

## 2. Phase cards

### Phase 1 — Contextual Definition

**Consumes** `company_input.md`, the frozen corpus under `baseline/domains/`,
and the mapping store under `baseline/MAPPINGS/sr_control_mappings/`.

**Produces** `doc02_adjusted_goals.md` — the Adjusted Goals (`AG-D-XX.Y-NNN`),
one per sub-domain per confirmed regulation, each with its regulatory source,
proportionality adjustment, company implication and control anchors.

**What is genuinely load-bearing**

| Element | Where | Why it cannot be removed |
|---|---|---|
| Control-anchor derivation | `guards/controls.py:147-164` | The mapping store is the only source of published anchors; derived in code, zero LLM in the path. PF 1.1 anchors attach only to GDPR rows, AI RMF only to AI_Act rows (R8). |
| Sub-domain partition check | `phase1/selection.py:54-59` | Rejects a candidate that is neither selected nor excluded — a silent drop. |
| L1 differential validator | `guards/l1_validation.py:168-441` | Re-derives §3–§6 from the corpus and diffs them against the assembled document. This is what catches doc-vs-artefact drift. |
| Deterministic assembler | `phase1/assembly.py:57-207` | Zero LLM. Table headers, section order, export. |
| Doc02 assembler's `UNVALIDATED_DRAFT` block | `phase1/assembly.py:76-80` | A sub-domain whose goals failed validation is marked, not omitted. |

**What is thin**

- The L0 parsers for `p1`, `p2`, `p3` and `p3f` (`phase1/facts.py:33-47`,
  `regulations.py:26-38`, `selection.py:48-59`, `framing.py:29-45`) check table
  shape, enum membership and partition completeness. None compares a value
  against the source input.
- `check_obligation_retention` (`guards/quality_gates.py:62-107`) compares
  token-set overlap against the baseline.
- `check_adjustment_vocab` (`quality_gates.py:150-161`) accepts any string of
  ≥3 words.
- `check_implication_specific` (`quality_gates.py:164-171`) requires ≥5 words
  and <0.95 similarity to peers.
- `check_grounded` (`quality_gates.py:110-138`) scans digit sequences of ≥3
  characters and substring-matches them against the concatenation of all digits
  found in the sources.
- `check_no_technology` (`quality_gates.py:141-147`) matches a word list of
  roughly 40 entries.

### Phase 2 — Operationalization

**Consumes** Phase 1's `steps/goals/*.json`.

**Produces** `Doc01_Operational_Objectives.md` (9 columns × N objective rows,
plus a `RULE-*` tail per sub-domain) and `Doc02_Secure_Design_Principles.md`
(7 principles × constraint / method_lead / eval_scope).

**What is genuinely load-bearing**

| Element | Where | Why |
|---|---|---|
| Additive columns | `phase2/parsers.py:125-147` | Verification Criteria, Method, Owner and the `RULE-*` tail are model-authored and are Phase 2's only material output beyond the rename. |
| Method-distribution ceiling | `phase2/parsers.py:80-89` | R10b invariant 3; a 0.60 ceiling on the method distribution. |
| Technology-neutrality gate | `phase2/derivation.py:196-201` → `quality_gates.py:141-147` | R5, enforced on the Phase 2 output. |
| Cross-case grounding | `phase2/derivation.py:150-167` | G7; flags vocabulary belonging to another case's intake form. |
| Canonical rule-id allocation | `phase2/parsers.py:165-168` | Rules are renumbered in code, not by the model. |

**What is thin or unconsumed**

- The `Operational Statement` column is `goal.get("goal")` copied by code
  (`phase2/derivation.py:85`) and rendered at `phase2/renderers.py:160`. It is a
  rename of Phase 1's `Adjusted Goal` column by construction.
- Five fields are populated per row and never read: `implication`, `source`,
  `pattern`, `property`, `adjustment` (`phase2/derivation.py:91-95`).
- Of ~10 named checks in `phase2/derivation.py`, five recompute a value the
  producer derived from the same source: G2 prefix-vs-regulation
  (`derivation.py:125-129` vs `objective_id()` at `derivation.py:41-46`), the
  "goal has no objective" check (`:142-145`), the "parent is not an `AG-` id"
  check (`:138-141`), the duplicate-id check (`:131-136`), and G5 Doc02
  completeness (`:178-183`).
- `steps/principles.json` is read by exactly one function, in the module that
  wrote it (`phase2/principles.py:133`). Phase 3's principle pack is built from
  the baseline definitions and never reads the company's instantiated constraint.
- The `RULE-*` tail is invisible to Phase 3: `phase3/skeleton.py:36-59` filters
  rows by a 9-cell shape keyed on `PO-/SO-` ids, and RULE rows have 4 cells.

### Phase 3 Part 1 — Specification & coverage

**Consumes** Phase 2's `Doc01_Operational_Objectives.md`, the case's frozen
hand-authored V0 baseline (`cases/<case>/03_PHASE3_SPEC/part1_security_privacy/
v0_functional_baseline/`), the human duty audit, and the human round verdicts.

**Produces** `OBJECTIVE_MAPPING.md` (the coverage matrix, 7 columns, 5 verdict
values), `PROCEDURAL`/`Doc03_Organizational_Requirements.md` (`ORG-D-XX.Y-NNN`),
`Doc01_Requirements_Specification.md`, `synthesis_rounds/` registers, and
`gate_report.md`.

**What is genuinely load-bearing**

| Element | Where | Why |
|---|---|---|
| Five-verdict enum | `phase3/schemas.py:20-26`, enforced at `verdicts.py:43-45` | Pure enum, parse-time. The one part of the matrix contract that is airtight. |
| Two-state rule (proposed ≠ concluded) | `phase3/weave.py:234-252` | G2 requires register + human marker + converged state + ≥1 item. The strongest of the six. |
| Objective set-comparison | `phase3/runner.py:28-44` | Every Phase 2 objective has exactly one matrix row. |
| Gate staleness choke point | `phase1/runner.py:749-758` | A later `p3a_*` stage marks an earlier gate verdict stale. |
| R5 pre-check on organizational warrants | `phase1/runner.py:1417-1431` | Blocks a violating warrant before spending model calls. |

**What is thin**

- `G3` (`phase3/weave.py:273-275`) reads only the presence of a non-empty
  inherited anchor list, and closes vacuously when the matrix or the Phase 2
  document is absent — in which case `findings` holds no `T6` entry.
- The `T6` anchor-provenance check (`phase3/verdicts.py:92-101`) compares the
  skeleton's published anchors against those same published anchors
  (`verdicts.py:117`), so `used - allowed` is empty by construction.
- `G5` (`phase3/weave.py:163-188`) sums over a `set` of distinct count-triples,
  so two regulations with identical counts are counted once; it also counts only
  three of the five verdict values.
- `G6` (`phase3/weave.py:191-198`) checks that a table written by the same stage
  has one row per accepted constraint.
- `PRINCIPLE_MAPPING.md` is read by no stage and by no guard.
- `scripts/check_traceability.py` (T1–T7) is never invoked by the pipeline; it
  is rooted at `cases/<case>/` and cannot be pointed at a run directory.

## 3. Stage reference

| Stage | LLM calls | Reads | Writes | Guard before it |
|---|---|---|---|---|
| `p1` | 1 | `company_input.md` | `steps/fact_sheet.yaml` | — |
| `p2` | 1 | fact sheet, input §5 | `steps/verdicts.md` + `.json` | G-P1-A |
| `p3` | 1 | fact sheet, verdicts, corpus index | `steps/selection.md` + `.json` | G-P1-B |
| `p3f` | 1 | fact sheet, verdicts | `steps/framing.md` | G-P1-B |
| `p4` | 1 per sub-domain | corpus module, framing, fact sheet | `steps/goals/<sd>.md` + `.json` | G-P1-C |
| `p4t` | 1 per sub-domain | corpus tensions | `steps/tensions/<sd>.{md,json}` | G-P1-C |
| `p5` | 0 | all of `steps/` | `doc02_adjusted_goals.md`, `RUN_NOTES.md` | G-P1-C |
| `phase2` | 1 per sub-domain + 1 | Phase 1 goals | `Doc01_…`, `Doc02_…` | G-P1-A |
| `p3a_cards` | 1 + N | fact sheet, Phase 2 doc | card inventory, V0 baseline | G-P1-A |
| `p3a_map` | 1 per sub-domain | Phase 2 doc, frozen V0 | `verdicts_<sd>.json`, `OBJECTIVE_MAPPING.md` | G-P1-A |
| `p3a_propose` | 1 per sub-domain | verdicts | `proposals_<sd>.json` | G-P1-A |
| `p3a_prin` | 7 | verdicts, cards | `proposals_prin_NN.json` | G-P1-A |
| `p3a_round` | 0 | proposals + human verdicts + marker | `round1_state.json`, `ROUND1_REGISTER.md` | — |
| `p3a_org` | 1 per duty | round state, human duty audit | `Doc03_…` | G-P1-A |
| `p3a_weave` | 1 per accepted carrier | round state, cards | woven cards, mapping, `Doc01_Requirements_Specification.md` | G-P1-A |
| `p3a_gate` | 0 | everything | `gate_report.md` | — |

Human gates are marker files under `steps/gates/`. `_require`
(`phase1/runner.py:1818-1830`) checks that the artefact and the marker both
exist. It does not parse the marker, and it does not bind the marker to a
digest of the artefact.

`G-P1-D` is documented in `SPEC.md:140`, `pipeline/README.md:46` and
`docs/pipeline/00_PIPELINE_MASTER_DESIGN.md:73`; no `_require` call references
it (`phase1/runner.py:789,794,799,830,866,1700,1714` cover A, B and C only).

## 4. Known seams

Functional ledger. Each row is a location and the observable behaviour there.

| # | Location | Observable |
|---|---|---|
| S1 | `cli/commands.py:191` | `"all": ["p2","p3","p3f","p4","p4t","p5"]` — `p1` is absent, so `--stage all` on a fresh run directory aborts on the missing `steps/fact_sheet.yaml`. |
| S2 | `guards/l1_validation.py:190-192` | `not (repo/…).glob(…)` — `Path.glob` returns a generator, always truthy, so the on-disk half of the "sub-domain code exists in the corpus" check never fires. The same file uses `list(…)` correctly at `:81` and `:89`. |
| S3 | `scripts/reproduce_run.py:72-73` | Reads `config["sampler_seed"]` / `["sampler_temperature"]`; `cli/commands.py:97-98` writes `"temperature"` / `"seed"`. The reproduction script aborts on every run. |
| S4 | `phase1/assembly.py:70,159` | The current date is written into the deliverable's frontmatter, so the byte comparison in the reproduction script cannot succeed across calendar days. |
| S5 | `phase3/verdicts.py:117` vs `:92-101` | `anchors_used` is assigned the skeleton's published anchors, then compared against the same published set. The check cannot produce a finding. |
| S6 | `phase3/weave.py:215,273-275` | G3 collects only `T6`-prefixed findings; when the matrix or Phase 2 document is missing, `findings` holds none, and G3 closes. |
| S7 | `phase3/weave.py:178,186` | G5 sums distinct count-triples, so two regulations with identical counts are counted once; the sum then falls short of the matrix row count. |
| S8 | `phase3/weave.py:106-109,186` | The renderer counts three of the five verdict values; a row verdicted `Design guidance` or `N/A` makes the G5 sum fall short permanently. |
| S9 | `phase1/runner.py:1491-1599` vs `phase3/verdicts.py` | `p3a_weave` re-routes principle-derived rows in memory and re-renders `OBJECTIVE_MAPPING.md`, without writing the mutated rows back to the verdict store. `p3a_org` (`runner.py:1381`), `p3a_weave` (`runner.py:1499`) and the gate (`weave.py:219-221`) all rebuild from the store. |
| S10 | `phase1/runner.py:257-262`, `compose.py:300-308,612` | `verdicts.md` and `verdicts.json` are written from one parse; the model reads the `.md`, the code reads the `.json`. Same shape for `selection.md`/`.json` and `goals/<sd>.md`/`.json`. |
| S11 | `phase1/runner.py:1818-1830` | Human gate markers carry no digest. Re-running `p1` replaces the fact sheet and leaves `G-P1-A.approved` standing. Phase 3 has this mechanism (`phase3/weave.py:130-160`, `runner.py:749-758`); Phase 1 does not. |
| S12 | `phase1/runner.py:784-801` | `stage_p1`/`p2`/`p3`/`p3f` return a hardcoded `1` for `n_calls`. |
| S13 | `cli/commands.py:239` | `status` is written as `"ok"` for any stage that returns normally, including one whose `stage_result` recorded `"partial"`. |
| S14 | `core/trace.py:58-62` | `count_calls` counts trace lines, not model calls. The trace ledger holds one record per stage attempt, not per call — `core/llm_client.py:68-87` issues an unseeded, untraced warm-up call before every real call. |
| S15 | `phase1/goals.py:99-105` | The deterministic `AG-D-XX.Y-NNN` allocator is unreachable: `expect_id` is `True` at every call site, so the model is asked to allocate ids and a mismatch costs a repair round-trip. |
| S16 | `phase1/tensions.py:44-49` vs `:68-82` | The model must emit sequential `T-NNN` ids and the call fails on a gap; `merge_tensions` then discards the model's numbering. |
| S17 | `phase1/tensions.py:36-38` | A tension row whose id does not match the pattern is skipped without a finding. |
| S18 | `compose.py:1030,1082-1084` | `p3`, `p3f` and `p4t` inherit the Phase 1 goal-writing clause "restate its full duty, do not drop a leg", which has no meaning for a selection, a framing table or a tension resolution. |
| S19 | `phase3/principles_constraints.py:234` vs `phase3/skeleton.py:127-137` | The split is on a `"## Coverage Totals"` heading that `render_principles` does not emit, so the filled `PRINCIPLE_MAPPING.md` keeps the skeleton's footer and appends a second totals table. |
| S20 | `phase3/org.py:244` | `render_doc03` zips duties with cards positionally; a duty whose card call failed receives the previous duty's card text. |
| S21 | `phase3/principles_constraints.py:211` | `reroute_objectives` reads `["principle"]` from the proposal; an accepted objective-driven proposal routed organizational raises `KeyError`. |
| S22 | `phase3/proposals.py:114` | The propose-time anchor check substring-matches against a stringified list, so `PR.AC-0` passes against `['PR.AC-01']`. |
| S23 | `docs/pipeline/prompts/PROM-P3A-04_PROPOSE.md:66` | The worked example shows `PR.AC-1` and `PR.DS-1`; the corpus publishes two-digit ids, and the check at `proposals.py:114-119` rejects the single-digit form. |
| S24 | `phase1/runner.py:1188-1190`, `:1104-1106`, `:1436-1438`, `:1549-1551` | On resume, `p3a_cards`, `p3a_propose`, `p3a_org` and `p3a_weave` skip their own re-validation of artefacts already present. |
| S25 | `phase1/runner.py:1687` | `p3a_all` breaks before `p3a_org`, `p3a_weave` and `p3a_gate` whenever the round has not converged, so the sweep cannot produce the standing the gate exists to report. |
| S26 | `pipeline/src/aegis_pipeline/observability/` | 110 lines, imported by nothing in `pipeline/`, `scripts/` or `pipeline/tests/`. |
| S27 | `phase3/schemas.py:78-82` | `schemas.org_id` is never called; the format is re-implemented inline at `phase3/org.py:245`. |
| S28 | `pipeline/deucalion/submit.sh:44` | The stage whitelist omits `p3a_all` and `p4tp5`, so neither can be queued although the CLI offers both. |
| S29 | `pipeline/AGENTS.md` §2 | Documents the `phase3` package with 5 modules (14 exist), omits `pipeline/src/agent/` entirely, and lists 6 test files (12 exist). §5's pre-flight mandates 4 suites and omits the exit-gate and measurement suites. |
| S30 | `docs/pipeline/00_PIPELINE_MASTER_DESIGN.md` | Dated 2026-10-01; describes Phase 3 as a skeleton and lists an L3 LLM-as-judge layer that `docs/decisions/ASSUMPTIONS.md:62-67` records as demoted to L1+L2. |

## 5. How to re-enter the work

| To work on | Start reading | The check that decides it |
|---|---|---|
| Phase 1 content quality | `phase1/goals.py:84-214`, `guards/quality_gates.py` | `pipeline/tests/quality_gate_test.py` |
| Phase 1 document assembly | `phase1/assembly.py`, `guards/l1_validation.py` | `pipeline/tests/assemble_real_test.py` |
| Phase 2 enrichment | `phase2/parsers.py`, `phase2/derivation.py` | `pipeline/tests/phase2_test.py` |
| Phase 3 coverage mapping | `phase3/skeleton.py`, `phase3/verdicts.py` | `pipeline/tests/phase3_test.py` |
| The exit gate G1–G6 | `phase3/weave.py:201-319` | `pipeline/tests/phase3_gate_test.py` |
| The organizational lane | `phase3/org.py` | `pipeline/tests/phase3_org_test.py` |
| The principle path | `phase3/principles_constraints.py` | `pipeline/tests/phase3_prin_test.py` |
| Reproducibility and accounting | `core/config.py`, `core/trace.py`, `core/llm_client.py` | `pipeline/tests/measurement_test.py` |

The phase-2 and phase-3 stage methods in `phase1/runner.py` have no test
coverage: `stage_phase2`, `stage_p3a_map`, `stage_p3a_cards`,
`stage_p3a_propose`, `stage_p3a_prin`, `stage_p3a_round`, `stage_p3a_org`,
`stage_p3a_weave`, `stage_p3a_gate` and `stage_p3a_all` are never called by a
test. A change there is unverified until a test exists.
