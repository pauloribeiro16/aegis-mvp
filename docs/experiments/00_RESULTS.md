---
document_id: AEGIS-EXP-RESULTS
title: 'Results — the programme at a glance'
version: 0.4.0
created: 2026-10-03
updated: 2026-10-05
status: LIVE — updated as data lands
sources: 'docs/research/sources.yaml'
---

# Results — the programme at a glance

> **Validity (SM-004).** Every number in this panel is bounded by three standing
> limits, declared once here rather than repeated per claim: **one model per
> cell** (a cell is a model × case × instrument — never two models averaged);
> **one seed** (42 — every pipeline run here is seeded, so its repeats are
> *confirmations of a fixed point*, not a sample: an n is a reproducibility
> count and the pipeline's seeded spread is 0.0000. The two arms deliberately
> left unseeded carry their own spread where measured — EXP-02 arm A, EXP-03's
> agent arm); and **three cases** (TinyTask / SecureBorder / OmniBank — 2, 4
> and 5 confirmed regulations). External validity stops at the fourth company.
> Per SM-004 the declaration is carried, not fixed
> (`docs/research/10_SCIENTIFIC_METHOD_ALIGNMENT.md`).

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

**How it was designed.** One full run per model × case cell at the then-current instrument (rev `ad76979`, `p1` + `p2`–`p5`, gates A/B/C pre-approved), then n=5 for the reference on Cases 02 and 03 so every other cell has something to be compared against. Seed 42, temperature 0.2 throughout; the p4 arm is read from `config.json → ficha_overrides`, never from the run tag. Two cells predate the instrument and are marked as such below: the reference's Case 01 and Case 02 clearances are `run_sec02_p1_1979370` and the Case 01 battery. Ground truth in `aegis-models/results/matrix_m02.tsv`; per-cell table in [EXP03a §9](EXP03a_screening_results.md).

**Results.** Under the pre-`ad76979` instrument the reference cleared all three cases and bracketed the two survivors on retention — gemma4 0.628 on Case 02 and muse 0.793 on Case 03 against the reference's 0.720 / 0.736. Every other failure in the matrix is a gate working: R6 (invented quantity), over-compression, the p2 format contract. ornith is runtime-incompatible (CUDA, reproduced on two nodes) and is out of the matrix per the pre-registration.

### The negative result — the reference does not deliver Case 03 (rev `ad76979`, seed 42)

Five runs, arm `m04_qwen38_c3`, all `ficha_overrides: {}` (the shipped **decision-rule** p4 arm), all `EXIT_CODE=1`, all aborting at the same p4 sub-domain on the same L0 verdict:

| Run | Job | p4 job | Aborting step | L0 verdict (first → repair) | Prompt tok | Exit |
|---|---|---|---|---|---|---|
| `run_m04_qwen38_c3_r01_1983224` | 1983224 | 1983225 | `p4_D-03_3` (seq 15) | `AG-D-03.3-004` 93% → `AG-D-03.3-001` 99% | 29 808 | 1 |
| `run_m04_qwen38_c3_r02_1983226` | 1983226 | 1983227 | `p4_D-03_3` (seq 15) | `AG-D-03.3-004` 93% → `AG-D-03.3-001` 99% | 29 808 | 1 |
| `run_m04_qwen38_c3_r03_1983228` | 1983228 | 1983229 | `p4_D-03_3` (seq 15) | `AG-D-03.3-004` 93% → `AG-D-03.3-001` 99% | 29 808 | 1 |
| `run_m04_qwen38_c3_r04_1983230` | 1983230 | 1983231 | `p4_D-03_3` (seq 15) | `AG-D-03.3-004` 93% → `AG-D-03.3-001` 99% | 29 808 | 1 |
| `run_m04_qwen38_c3_r05_1983232` | 1983232 | 1983233 | `p4_D-03_3` (seq 15) | `AG-D-03.3-004` 93% → `AG-D-03.3-001` 99% | 29 808 | 1 |

The verdict verbatim: *adjusted goal is a near-verbatim copy of the Sub-SO objective (93% / 99% similar) — it restates nothing about this company; calibrate it against the §2 framing*. Three nodes (gnx505, gnx508, gnx532), five identical aborts — this is what a seeded determinism looks like from the outside (AGENTS.md §-1): the instrument and the seed fixed the outcome, r01 revealed it and the other four only confirm it. **The reference's Case 03 cell under rev `ad76979` is `no`, 5/5**; the one Case 03 delivery in the matrix is muse-glimmer's.

**This is not the EXP-04 failure.** The rule-arm regression in [EXP04_results.md](EXP04_results.md) is a Case 01 result: job 1983154 aborts at `p4_D-06_3` on an *obligation-vocabulary* verdict (`AG-D-06.3-002 keeps 12 of the Sub-SO's 46 obligation terms`) at 15 818 prompt tokens — different case, different sub-domain, different gate message, roughly half the pack. EXP-04's claim is about Case 01 and stands; this is a second and independent failure of the same arm on a harder case.

**And it is not one model's bug.** Same rev, same seed, every Case 03 model dies on an L0 gate at a *different* sub-domain — the failure is distributed:

| Model | Job | Abort | L0 verdict | Prompt tok | p4 calls reached |
|---|---|---|---|---|---|
| qwen3.8:27b (ref.) | 1983224 | `p4_D-03_3` | near-verbatim 93% → 99% | 29 808 | 11 |
| glm-4.7-flash | 1983146 | `p4_D-01_1` | near-verbatim 94% → 94% | 22 581 | 1 |
| nemotron-3.5-lightning | 1983148 | `p4_D-01_3` | obligation terms 11/51 → 10-column row | 19 659 | 3 |
| gemma4:31b | 1983142 | `p4_D-05_2` | R8 — row cites `AI_Act` with no `AI_Act` Sub-SO | 27 527 | 18 |
| gemma4:31b (m05, rev `1b6d04d`) | 1983343 | `p4_D-03_2` | R6 — quantity 800, then 2022, not in the intake | 27 711 | 10 |
| qwen3.5:27b | 1983152 | `p2` | p2 format contract — no fenced block | 2 070 | 0 |
| **muse-glimmer:30b** | **1983144, 1983314** | **delivered** | — | up to 47 272 | **38, both runs** |

**What they say.** The L0 quality gates meet a hard case, and where they meet it the failure lands where a model's own calibration is weakest rather than on one sub-domain. Three measurements carry that, one bounds it:

- *The gate discriminates.* In the reference's own trace the near-verbatim gate (M-03, similarity limit 0.88) fires on 4 of the 11 p4 sub-domains it reached — `D-01.2`, `D-03.1`, `D-03.2`, `D-03.3`. The repair call rescued three; `D-03.3` failed twice and took the run. The other seven sub-domains in the same run did not fire at all.
- *Pack size is not the discriminator.* The same run cleared `D-02.1` at **34 013** prompt tokens — larger than the 29 808 that killed it — and the two delivered muse runs reached 47 272 on the same seed.
- *Nothing was truncated.* The aborting call ran at 29 808 prompt tokens against a 65 536 `num_ctx` and returned `done_reason=stop` after 1 314 of 16 384 `num_predict`; every failing p4 call in the matrix reads the same way. This is not a context ceiling.
- *Boundary.* All five reference runs carry `ficha_overrides: {}`. No menu-arm Case 03 run of the reference exists, so on this case the EXP-04 arm comparison is **untested, not resolved** — nothing below rests on it.

**The falsifiable reading.** *Case 03 breaks models at the L0 quality gates, and it breaks them where their calibration is weakest, which is why the sub-domain differs per model.* Refuted by: (a) a reference Case 03 run on the menu arm that delivers — the break would be arm-specific, not gate-vs-case; (b) a model that reaches `D-03.3` and delivers, or one model dying at the same sub-domain on two different cases — the distribution is then a shared cause wearing two hats; (c) E-10 measuring the M-03 firing rate on a *delivered* Case 03 document (muse, 2 runs on disk) and finding it materially different from the rate the failing runs show — the 0.88 limit would be a convention with the wrong shape for 5-regulation packs, and the honest repair would be the prompt, not the threshold.

**What this does not show.** It is not an argument for relaxing a gate. [PLANO_FECHO.md](PLANO_FECHO.md) §4 fixes the rule — *uma falha do gate é um dado, não um contratempo*, and lowering a threshold so a run passes is the circular validation R10 forbids. The M-03 limit's own basis is already declared, honestly, as a convention awaiting E-10 ([METRICS.md](METRICS.md) M-03): a gate firing is a measurement, not an argument against the gate. Nor does it impeach the reference — under the *same* rev and the *same* seed the reference delivers Case 02 5/5 (jobs 1980154, 1983216–1983222, `EXIT_CODE=0`). Nor does it re-open EXP-04. What it establishes is the cell this panel previously reported as a delivery: **under rev `ad76979`, qwen3.8:27b, seed 42, Case 03 is `no`.**

### Follow-up (2026-10-05 evening) — refuter (a) is answered: no (run m06, menu arm, graded)

`run_m06_qwen38_c3_menu_1983666` (jobs 1983666 p1 / 1983667 all — the `all` job ends `FAILED` by design, see below), seed 42, `ficha_overrides: {'p4_adjustment': 'menu'}` read back from `config.json` (the arm is the override, never the tag). **Arm verified against the artifact, not the config alone:** the synced `inputs/*_p4_D-01_1_user.md` carries the menu text verbatim — *"ADJUSTMENT — pick exactly one of three values: `unchanged — fits as stated` | `narrowed: <what> — because <company fact>` | `flagged: <open question>`"* — so this run measured the **menu** instrument. (An earlier draft of this entry claimed it measured the badge vocabulary; that was wrong — the badge rewrite of the base instruction landed in the working tree *after* the cluster sync, and the prompt bytes are the record of what ran.) Provenance caveat, stated because it matters: the manifest stamps `aegis_git_rev = b2fe2aa`, but the code was the uncommitted working tree (p4t per-sub-domain decomposition + fault isolation per ADR-012 D1/D5). The full artifact story is the `inputs/` directory, which carries every prompt verbatim.

This was also the first live run of per-sub-domain fault isolation, and the stage behaved as designed: **p4 swept all 38 sub-domains and reported `36/38 carried, 2 failed (L0)`** in `steps/stage_result.json` — `D-01.2` (near-verbatim 95%, and the repair degraded the row to 8 columns) and `D-03.2`. **`D-03.3` — the sub-domain that killed the rule arm five times — passed under the menu arm.** p5 then refused to assemble a deliverable with 2 selected sub-domains short and failed with attribution, which is the recorded behaviour, not a malfunction: a partial delivery is now a *graded* cell (36/38 + named failures) instead of a binary abort that discards 36 validated sub-domains.

**Refuter (a) of the reading above is closed: the menu arm does not deliver Case 03 for the reference either** — the break is not arm-specific. Refuters (b) and (c) remain open.

**And the run sharpens the menu picture on Case 03.** 121/122 rows (ratio 0.99) are `unchanged`, 1 `flagged`, **0 `narrowed`** — the highest verbatim ratio measured on any run in the programme (delivered comparators: 0.91 menu/C1 with 6% `narrowed`, 0.94 rule/C2, 0.92 ref/C3 with 9% `narrowed`, against 0.35 gemma4/C1 and 0.45 muse/C3). On Case 03 the menu arm collapses to its passive value *harder* than on Case 01 — the case, not the arm, drives the collapse. **The badge instrument (`verbatim | proportional | inherited | flagged`, now the shipped base instruction) remains unmeasured** — the follow-up matrix does that.

**A recording gap this run exposed, now closed.** `prompt_digests` hashed the ficha files plus the golden example — not the `steps.py` instruction — so nothing in the manifest distinguished this instrument from the previous two; only the `inputs/` prompts disambiguate. `compose.prompt_digests` now also records `p4_instruction` and `p4t_instruction` digests (first run to carry them: the m07 matrix), and `_p4_instruction`'s swap anchor was updated to the current base marker — with the old anchor gone, any variant override would have been *silently ignored* while `config.json` recorded it; it now refuses loudly instead.

## EXP-04 — the prompt ablation (COMPLETE — read [EXP04_results.md](EXP04_results.md))

**What it tested.** Whether the Adjustment column's decision procedure (rule with calibration test vs closed 3-value menu) changes what the model produces.

**How it was designed.** Same pipeline/case/gates, seed 42, n=5 per arm; the arm actually run read from `ficha_overrides`, not the run tag.

**Results.** Under the current instrument: **menu 5/5 delivered, rule 0/5** (deterministic over-compression at D-06.3). And the regression finding: the rule arm delivered 15/15 under the pre-TERMINATION instrument (EXP-02-B) — the prompt change regressed it, model-specifically (gemma4/muse deep dives deliver under the same instrument). The rule's calibration advantage (12% vs 6% `narrowed`) was only ever measured under the old instrument.

**What it says.** The menu is the robust arm under the shipped prompt; the ablation cannot be run cleanly until either the menu is shipped or the rule text is shortened. Decision pending with the researcher (EXP04_results.md §Decision).

## M07 — the badge-instrument matrix (COMPLETE — 6 models × 3 cases, preregistered as [PREREG-M07](../../../Work/aegis-models/PREREG-M07.md))

**What it tested.** The full matrix under the new instrument: badge-vocabulary p4 default (`verbatim | proportional | inherited | flagged`), p4t decomposed per sub-domain, graded fault isolation, seed 42, n=1 per cell — the researcher's directive to run every model on every case with the new prompts.

**Results.** 7 of 18 cells delivered: **the reference (qwen3.8) delivers ALL THREE cases for the first time** — including Case 03 at 38/38, the sub-domains that killed the rule arm five times (D-03.3) and cost the menu arm two others (D-01.2, D-03.2) all pass under the badge instruction. muse delivers 3/3 (38/38 each), gemma4 1/3. The 11 failures are all gate-working, no infrastructure: qwen3.5 ×3 at the p2 format contract (7/7 systematic now — the standing E-01 test case), glm-4.7 ×3 and nemotron ×3 over-compression at p4 (10–31 of 38 sub-domains carried before the final assembly refused), gemma4 ×2 exactly 1–2 sub-domains short (graded cells — the old matrix would have recorded them as plain `no`).

**Preregistered verdicts (H1, H2 — both as frozen):**
- **H1 (mode collapse survives the badge vocabulary) HELD.** The `(verbatim+unchanged)` ratio is 0.86–1.00 across all 18 runs (median 0.99), with **zero `proportional` and zero `inherited` rows in the entire matrix** — the models never used the new escape options. The falsifier (any model < 0.50 with ≥ 25% proportional/inherited) did not fire. Giving the model a richer classification vocabulary changed nothing about default collapse; M-14's WARN fired on all 18.
- **H2 (the decomposed p4t preserves the tension layer) HELD.** Delivered runs produce 1–11 T-rows; muse C3 yields 5 against the monolith's 6 on the same case and model. The cross-sub-domain synthesis cost (ADR-012 C7b) did not materialise in this matrix. (The failing models emit 33–56 rows — the C7c duplicate shape — but their cells abort regardless.)

**What it says.** The badge instruction is the first p4 text under which the reference clears all three cases — but it is also the instrument with the *highest* measured default-collapse (0.99 unchanged on the reference, 0 `narrowed` on 15 of 18 runs). Delivery and calibration moved in opposite directions: the same explicit "full company-proportional RESTATEMENT" instruction that helps rows pass the L0 gates also invites verbatim restatement. What the delivered rows *are* — faithful restatement or compliance theatre — is precisely the question the blind L2 scoring owns (M-14's 0.70 threshold stays `convention` until then). The `prompt_digests` now carry `p4_instruction`/`p4t_instruction`, so this instrument is self-identifying for every future run.

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

*Rewritten 2026-10-05. Every item the previous version of this section listed as
pending has since landed; the list below is what is actually open.*

- **EXP-03's blind rubric is the one thing still pending** — the objective half is
  complete and written up ([EXP03_results.md](EXP03_results.md)): at n=15 the
  agent arm does **not** produce the same document (retention 0.7851 ± 0.0182 vs
  0.7171 ± 0.0000, `narrowed` 0–2 vs 8) and terminates cleanly in **7/15** runs
  against 15/15. What is not done is the researcher's blind scoring of the two
  arms (L2_RUBRIC.md). The arm is already off the production path on the
  researcher's decision (AGENTS.md §-1) — and the decisive reason was
  reproducibility *semantics*, not cost: pipeline calls are context-independent
  so a fixed seed reproduces a whole run, while the agent accumulates state
  across jobs. The rubric is what would answer "which document is better", not
  "may we use it".
- **The two screening cuts were reclassified, not confirmed.** glm-4.7-flash and
  nemotron-3.5-lightning were cut for deterministic p3 selection-contract
  failures; the root cause is a prompt defect in PROM-P1-03 v1.1.0, fixed in
  v1.2.0, and the p3 failure rate went **10/10 → 0/4** in the m03 re-test
  ([EXP03a §6–§7](EXP03a_screening_results.md)). Neither model is back in: both
  still die inside p4, and neither survives the M02 matrix across all three
  cases.
- **EXP-04 is closed; its decision is not.** Under the current instrument the
  menu arm delivers 5/5 and the rule arm 0/5 (deterministic over-compression at
  D-06.3), and the rule arm delivered 15/15 under the pre-TERMINATION instrument
  — the prompt change regressed it, model-specifically. Which arm ships is a
  researcher decision ([EXP04_results.md §Decision](EXP04_results.md)).
- **The reference's Case 03 menu-arm cell is unfilled.** All five `m04_qwen38_c3`
  runs ran the shipped decision-rule arm (`ficha_overrides: {}`); the menu arm
  has no Case 03 run of the reference. That cell — not a re-run of the arm that
  fails deterministically — is the one measurement that would say whether the
  `D-03.3` abort is arm-specific or case-specific (see §M02 above).
- **The context policy is registered and un-implemented.**
  [ADR-2026-10-05](../decisions/ADR-2026-10-05_pack-budget-and-context-policy.md)
  settles the shape (p4t decomposed per sub-domain; input and output budgets are
  separate decisions; no summarisation into the corpus) and routes the overflow
  question to E-15, which is preregistered, costs 0 GPU-h and has not run. Its
  D2 — whether to prune the pairwise `cross/` fan-out — is deliberately left
  **undecided** pending E-16.
