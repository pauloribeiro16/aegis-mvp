---
document_id: AEGIS-EXP-RESULTS
title: 'Results — the programme at a glance'
version: 0.3.0
created: 2026-10-03
updated: 2026-10-04
status: LIVE — updated as data lands
sources: 'docs/research/sources.yaml'
---

# Results — the programme at a glance

**How to read this.** One block per experiment, always the same four sections:
*what it tested · how it was designed · results so far · what they say*. This
panel is the quick view; the depth lives one click away — the design in the
pre-registration ([PREREG_01.md](PREREG_01.md)), the original comparison in
[EXP01_pipeline_vs_agent.md](EXP01_pipeline_vs_agent.md), the human instrument
in [L2_RUBRIC.md](L2_RUBRIC.md). Live per-run numbers (calls, tokens, LLM
seconds, validation verdicts) are on the **Corridas** and **Comparar** pages of
this site — this panel links them rather than duplicating them.

**Programme status.** **EXP-02 COMPLETE** (bit-reproducibility under a fixed
seed). **EXP-03 objective half COMPLETE** — at n=15 the agent arm does *not*
produce the same document (higher retention, near-zero calibration) and fails
to terminate cleanly in 8 of 15 runs; the blind rubric that adjudicates "which
is better" is prepared and waiting. **EXP-04** is staged and ready. **M01
screening COMPLETE**. Model-matrix retries for glm/nemotron (prompt-engineered
p3 variant) are queued. Long-form results: [EXP02](EXP02_results.md),
[EXP03](EXP03_results.md), [M01 screening](EXP03a_screening_results.md).
**EXP-02 COMPLETE** — headline: a fixed seed makes the
pipeline **bit-reproducible** (15/15 byte-identical goal sets), the entire
variance is sampling-driven, and unseeded runs abort at **40%** on an R6 gate
firing. Full verdicts in [EXP02_results.md](EXP02_results.md). EXP-03: the 15
pipeline-arm runs are the EXP-02 arm-B runs (same configuration); the **15
seeded agent runs are queued**. Model screening: glm47 and nemotron
**screened-out** (deterministic selection-contract failures), gemma4 and
muse-glimmer screened-in; 12/20 screening runs closed.

---

## EXP-01 — Pipeline vs agent (COMPLETE)

**What it tested.** Can a tool-calling *agent* (a model that decides its own
working order) do the same compliance-analysis job as the *fixed pipeline*
(five predetermined steps), and which produces the better result?

**How it was designed.** One run per arm, everything else identical: same case
(TinyTask, an 8-person SaaS), same regulatory corpus, same model
(qwen3.8:27b on a Deucalion A100), same output parsers, same quality gates,
same document assembler, same validator. The only difference was *who decides
the working order*.

**Results.** Both arms produced a valid document — 65 adjusted goals each,
zero dropped obligations, both passed every structural and content check. The
agent needed **5.2× the LLM calls** (220 vs 42) and **2.8× the wall time** for
the same output. A one-line prompt change (replacing a pick-one menu with a
calibration decision rule) moved the `narrowed` adjustments from **1 to 17**
out of 65 rows.

**What they say.** The output *contract* — parsers, gates, assembler — not the
orchestration, determines the document's structure; paying 5× for
model-directed control bought nothing measurable here. **But this is one run
per arm**: it is an illustrated hypothesis, not evidence. EXP-02 and EXP-03
exist to turn it into one.

---

## EXP-02 — The noise floor (COMPLETE — read [EXP02_results.md](EXP02_results.md))

**What it tested.** Nobody had measured how much this pipeline varies when
*nothing varies*. If run-to-run variation exceeds the differences EXP-01
reported, those differences are noise.

**How it was designed.** 3 arms × 15 runs, registered in advance
([PREREG_01.md](PREREG_01.md)): A = as-is (no seed), B = +seed 42, C = +seed
+temperature 0. Same case, corpus, prompts, gates, assembler, validator
everywhere; gates pre-approved as a declared fixed condition.

**Results.** **Seeding makes the pipeline bit-reproducible**: all 15 arm-B runs
produced byte-identical goal sets (retention 0.7171490955644458 to full float
precision; `narrowed` 8–8; the deliverables differ only in the run-id line).
Arm C is equally deterministic at its own fixed point (0.7159). Arm A
(unseeded) spreads 0.7131 ± 0.0086 — and **aborts at 40%**: the R6 grounding
gate fires on numeric tokens in prose (`05.2`, `001.`) that seeded runs never
emit. All four registered hypotheses resolved: H1 supported (seed = full
determinism), H2 falsified (zero residual serving-layer variance — the vendor
warning never manifested), H3 supported (greedy neither helps nor harms), H4
supported (selection 100% stable under the current prompt; the historical
selection variance came from older prompts).

**What they say.** The pipeline's variance is entirely sampling-driven and one
`seed` removes it — the reproducibility envelope every later comparison reads
against is now *zero* for seeded runs. And reproducibility is not cosmetic:
without a seed, an unattended pipeline loses 40% of its runs to a gate a
seeded run never trips.

---
---

## M01 — The model matrix (SCREENING CLOSED — see [EXP03a_screening_results.md](EXP03a_screening_results.md))

**What it tested.** A new lab ([aegis-models](../../../aegis-models/README.md)
— separate repo, no pipeline fork) runs **other models available on Deucalion**
through the same pipeline, same case, same prompts: the model is the only
variable. Before any battery, each model passes a **smoke** — a
harness-correctness test (`p1`+`p2` only): can this model produce output the
contract accepts, does it tolerate the payload, and how much context does it
*really* consume (measured with the tokenizer's own counts, not estimates)?

**How it was designed.** 7 models in the matrix: qwen3.8 (the reference), plus
qwen3.5 (same family, one version back — isolates version from architecture),
gemma4:31b, glm-4.7-flash (the cost contrast), nemotron-3.5-lightning,
muse-glimmer, ornith-1.5. Smoke → screening (5 runs each) → deep dive (15
runs, finalists only). Registered in [PREREG-M01](../../../aegis-models/PREREG-M01.md).

**Results so far.** Screening is closed — read
[EXP03a_screening_results.md](EXP03a_screening_results.md) for the full write-up.
Headline: **4 of 6 models run the pipeline (smoke), 2 of those 4 survive the
full chain** (glm-4.7-flash and nemotron are cut by *deterministic* selection
contract failures, 5/5 runs aborting at p3 — not noise). Against the qwen3.8
reference (retention 0.7171, 43 calls):

| Model | retention | calls | LLM s | `narrowed` / 65 | vs reference |
|---|---|---|---|---|---|
| gemma4:31b | 0.6532 | 42 | 1,391 | 40–43 | −0.064, δ = −1.00 |
| muse-glimmer:30b | **0.8036** | 42 | 2,481 | 15–21 | **+0.087**, δ = +1.00 |

**What they say.** The contract generalises (every survivor reaches L1 PASS at
42–43 calls, same structure); the *behaviour* does not. muse-glimmer retains 14%
more of the regulatory duty than the reference and runs at 1.9× the wall time;
gemma4 retains the least and calibrates hardest. Neither is "better" on the
objective metrics — retention measures survival, not correctness or
calibration quality — which is exactly the question the blind rubric answers,
and muse-glimmer is now a third arm worth scoring.

**Correction to the record (2026-10-04).** The two cuts were booked as model
incompatibilities. Reading the aborted answers shows a **shared cause in the
prompt**: PROM-P1-03 v1.1.0 presented the exclusion line only in its non-empty
form, never said a sub-domain may not appear in both lists, and never allowed
an empty list — so glm-4.7-flash duplicated D-02.4 across both lists and
nemotron invented the id `D-06.5`, then repeated it on the repair retry *with
the reason it was wrong in the same line*. Both were filling a slot with no
legal empty value. The prompt is revised to **v1.2.0** (explicit partition,
empty form given, uncertain ids left IN the table), and the re-test runs as a
**new tier `m02`**, not as a re-run of `m01`: a prompt revision changes the
instrument. Runs now carry `prompt_digests` in `config.json` so that split is
provable from the artefacts. Detail in
[EXP03a_screening_results.md §6](EXP03a_screening_results.md).

## The three cases (COMPLETE — all three delivered with the reference model)

**What it tested.** Whether the pipeline generalises past TinyTask: 2 regulations and 8 employees, versus Case_02 (4 regulations, 450 employees) and Case_03 (5 regulations, 5 000 employees).

**How it was designed.** Same pipeline, prompts, gates and assembler; only the case binding changes. Seeded 42. It is a correctness lane, not a measurement lane.

**Results — all three delivered.** Adding the cases paid for itself immediately: they exposed four latent defects that ~30 TinyTask runs could not reach (unguarded corpus reads, the `SR-AIACT` token, model spellings, and the p4 stub trap), and the two structural limits the MVP never had to face — a 136 kB pack with 5 regulations where the model would not stop writing, and a 42k-token pack that needed a 131 072 context rung. Both are fixed and verified; the 38-sub-domain taxonomy needed no change.

**What they say.** The MVP was never wrong on TinyTask; it was untested past it. One added case paid for itself by finding three latent defects and a fourth variant, and each fix generalises because it is derived from the corpus rather than from the case.

## M02 — the coverage matrix (COMPLETE — 6 models × 3 cases, seeded)

**What it tested.** Whether model and case generalise together — the variable M01 never varied at the same time.

**Results.** Only the reference clears all three cases. gemma4 clears Case 02 and muse clears Case 03, bracketing the reference's retention from both sides (0.628 / 0.793 vs 0.720 / 0.736). Every other failure is a gate working: R6 (invented quantity), over-compression, the p2 format contract. ornith is runtime-incompatible (CUDA, reproduced on two nodes) and is out of the matrix per the pre-registration. Full per-cell table in [EXP03a §8](EXP03a_screening_results.md), ground truth in `aegis-models/results/matrix_m02.tsv`.

## EXP-04 — the prompt ablation (COMPLETE — read [EXP04_results.md](EXP04_results.md))

**What it tested.** Whether the Adjustment column's decision procedure (rule with calibration test vs closed 3-value menu) changes what the model produces.

**How it was designed.** Same pipeline/case/gates, seed 42, n=5 per arm; the arm actually run read from `ficha_overrides`, not the run tag.

**Results.** Under the current instrument: **menu 5/5 delivered, rule 0/5** (deterministic over-compression at D-06.3). And the regression finding: the rule arm delivered 15/15 under the pre-TERMINATION instrument (EXP-02-B) — the prompt change regressed it, model-specifically (gemma4/muse deep dives deliver under the same instrument). The rule's calibration advantage (12% vs 6% `narrowed`) was only ever measured under the old instrument.

**What it says.** The menu is the robust arm under the shipped prompt; the ablation cannot be run cleanly until either the menu is shipped or the rule text is shortened. Decision pending with the researcher (EXP04_results.md §Decision).

## Registered decisions (2026-10-04)

**Scale band: the code's threshold governs (EU 2003/361).** `controls.py` bands
are `<50 MICRO`, `<250 MEDIUM`, else `LARGE`. Case_02 has 450 employees, so it
resolves to **LARGE** — even though its own Doc02 §2 Size framing says "MEDIUM
scale" and its intake writes "450 | >250 = Large". The band and the word disagree
inside the same case. The **threshold is kept** (it is the regulatory one) and
the LARGE tier rows are the researcher's own vocabulary from that same Doc02
(`RIGOROUS` / `STANDARD`, with `DEFERRED` unavailable once there is a real
security team). Recorded here and in `controls.py` so the choice is visible to
whoever next meets the mismatch.

**Regulation-id spelling is normalised at the L0 gate; the gate stays strict.**
Observed: qwen3.8 wrote `SG-D-07.2.AIACT` for `AI_Act` on a 4-regulation case,
qwen3.5 the same class of mangling at the smoke. `_one_reg` now maps the
regulation spelling (`AIACT`/`AIAct`/`AI-ACT` → `AI_Act`, `NIS_2` → `NIS2`) and
stores the canonical id. **Only the regulation token is normalised**: the
sub-domain must still match exactly, an unknown regulation is still rejected,
and a row naming a regulation the module does not carry is still caught by
`check_subso_coverage` and the L1 phantom-regulation check. Spelling no longer
costs a whole run; substance still does.

## What lands here next

- **EXP-03 is running**: its pipeline arm is EXP-02's arm B (same seeded
  configuration, 15 runs, already validated); the **15 seeded agent runs are
  queued**. When they close: the blind scoring pack goes to the researcher
  (L2_RUBRIC.md, ~2 h) and the paired verdict lands here.
- **Screening analysis** when the 20 model runs settle: gemma4 and
  muse-glimmer screened-in, glm47 and nemotron screened-out on deterministic
  selection-contract failures (both recorded in the lab's MODELS.yaml with
  their cuts).
- **EXP-04** (the prompt ablation) launches on the seeded configuration once
  the exemplar-freeze code change is in.
