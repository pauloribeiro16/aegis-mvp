---
document_id: AEGIS-RES-14
title: 'Context, orchestration and prompting — the verdict against this repo'
version: 0.1.0
created: 2026-10-05
status: ACTIVE
survey_date: 2026-10-05
sources: 'docs/research/sources.yaml'
---

# Context, orchestration and prompting — the verdict against this repo

**What this document is.** The mapping layer for the three new catalogues:
[11_CONTEXT_MANAGEMENT.md](11_CONTEXT_MANAGEMENT.md) (`CX-001..008`),
[12_PROMPT_ENGINEERING.md](12_PROMPT_ENGINEERING.md) (`PE-001..014`),
[13_ORCHESTRATION.md](13_ORCHESTRATION.md) (`OR-001..009`). It answers three
questions the earlier mappings answered for their own catalogues: what the
implementation already does that the literature supports, where the literature
contradicts a position this repo holds, and what is worth experimenting on.

The pattern of this document is [03_PATTERN_MAPPING.md](03_PATTERN_MAPPING.md)
and [09_KG_PATTERN_MAPPING.md](09_KG_PATTERN_MAPPING.md). The 2026-10-05 pass
registered 100 sources (S-284..S-383) across the three fronts; 98 of them are
new to the registry and two are re-pointed pre-existing entries.

---

## 1. What the implementation already has that the literature supports

Six positions the repo took on its own now have external anchors. Two of them
are strengthened, one is materially qualified, and the qualification is the
most useful output of this pass.

| Repo position | Anchor | Effect |
|---|---|---|
| `seed=42, temperature=0.2` as a correctness property (`AGENTS.md` §-1) | [S-363] derives the same rule from **replayability**; [S-376] measures that unseeded agentic evaluation carries sd > 1.5 pp at temperature 0 | **Strengthened.** The rule stops being a measured preference and becomes the price of durable execution. The external derivation is independent of the repo's EXP-02. |
| Minimal context, code-owned control flow (ADR-010) | [S-374]: removing redundant inter-agent traffic *improved* accuracy by 3.5–10.8% at 28–72% fewer tokens | **Strengthened.** Not merely cheaper — measurably no worse. Corroborates EXP-03's 4.8× calls / 6.4× context from outside. |
| Verify-gated completion (`AO-007`) | [S-368], [S-369]: approval gates are not barriers and the dialog is agent-authored | **Strengthened, for a reason the catalogue did not record.** The repo's gate is evaluated by pipeline code with no model in the loop, which is the materially better position. That should be the stated reason. |
| Flags-not-drop, anchors copied never re-derived (`PP-015`) | [S-249]: compressed claims score 0.86 precision against their own summaries, 0.12 against source spans | **Strengthened with a number.** The repo held this as a hypothesis; it now has the measurement and the audit finding that a self-consistent check inflates apparent grounding ~7×. |
| `PP-010` — prompt caching breaks determinism | [S-356]: BF16 diverges on 166/200 suffixes, **FP32 produces no decoded disagreement** (Wilson upper bound 1.88%); cache transplant makes divergence follow the donor 24/24 and 43/43 | **Qualified, and the qualification is the useful part.** It is the *precision* and the *key identity*, not the presence of a cache. See §2. |
| EXP-03's 53% clean-termination disclosure | [S-383]: across 50 popular repositories, *"none report how many runs failed, errored, or were skipped"* | **A strength to claim, not a weakness to fix.** By this standard the repo's reporting is rare, and the denominator is what makes the other number interpretable. |

---

## 2. Where the literature contradicts a position this repo holds

### 2.1 `PP-010` is over-stated as written

**Current text:** caching breaks determinism. **What the measurement supports:**
divergence is *caused* by the cache, is *attributable* to it, and is *moderated*
by numerical precision [S-356]. The failure that should actually worry a
pipeline is cross-context key collision — accuracy 0.94 → 0.64 under
cross-adapter collision, and 93% prompt identification from timing when the salt
is omitted [S-355].

**The consequence is a narrower and more actionable claim**, and it does not
require abandoning caching. Restate `PP-010` as a precision-and-key-identity
condition. This is the one place in this pass where a repo position should be
edited rather than merely annotated.

### 2.2 The zero-residual-variance claim has a scope it does not state

`AGENTS.md` §-1 records that the 15 seeded runs showed *"zero residual from the
serving layer"*. That is true and it is measured — but [S-375] shows the
mechanism by which seeded generation still varies: batch-dependent GPU execution
changes kernel tiling and reduction orders, reproducing 22 of 55 label flips
under standard vLLM against 0 under batch-invariant kernels.

**So the claim is a property of the endpoint configuration, not of seeded
sampling.** It is true against a hosted API and is not a general law. The fix is
one field: record the serving configuration in `config.json`, because the scope
of the determinism claim depends on it. Nothing in the pipeline changes.

### 2.3 The seeded result is one point in an unmeasured distribution

This is the largest qualification and it is not a flaw in EXP-02 — it is the
next experiment. `sd = 0.0000` controls **sampling** variance. Two further axes
exist that seeding does not touch: prompt format, where open models show *"up to
76 accuracy points"* of difference from formatting alone and a single
semantics-preserving perturbation **alters model rankings in 63% of cases**
[S-307, S-308]; and access surface, worth 3.4 accuracy points [S-310].

The number that bounds it: semantics-preserving perturbations *"can account for
up to half of the performance variance for a given model"* [S-308]. The honest
statement is that the repo has measured one point in a distribution of unknown
width — and one source argues much of that width is an artefact of the scorer
rather than the model [S-309], so the measurement must hold the scorer fixed and
say so.

### 2.4 A CoT trace is not an audit record

Not a contradiction of a stated position, but a constraint the repo has never
written down: reasoning traces systematically misrepresent the true cause of a
prediction — a biasing feature was followed without being mentioned in the
rationale, costing up to 36 points [S-286] — and **larger models are less
faithful, not more** [S-287]. On current frontier models the raw trace is not
even retrievable [S-289]. Anything in `trace.jsonl` that reads a reasoning field
as corroboration is unsound.

### 2.5 Few-shot examples are a poor place to encode a compliance requirement

*"Randomly replacing labels in the demonstrations barely hurts performance"*
across 12 models [S-296] — what demonstrations actually supply is the label
space, the input distribution and the format. So a demonstration that encodes a
regulatory requirement may cost almost nothing to get wrong. Requirements belong
in the instruction and the output contract (`PE-005`), which is where the
fichas already put them. The repo's "anti-circular few-shot" practice is
unaffected; its *justification* now has a reason.

---

## 3. The gaps this pass opened

Six new gaps, continuing the `G1`..`G12` numbering from
[09_KG_PATTERN_MAPPING.md](09_KG_PATTERN_MAPPING.md).

**G13 — No measurement of prompt-format variance.** The repo measures sampling
variance and nothing else. The literature puts the unmeasured axis at up to half
of total variance [S-308]. Cost: 0 GPU-h beyond re-running an existing
configuration under paraphrased templates.

**G14 — The serving configuration is not recorded.** The determinism claim's
scope depends on it and it is not in `config.json` [S-375]. Cost: one field.

**G15 — No accounting rule for cost.** A reported number without a declared
reporting rule is not a measurement; changing only the rule has moved published
scores by 20.9 points [S-383]. `trace.jsonl` records values but not the rule.
Cost: one documented rule plus a field.

**G16 — Instruction count has an unmeasured collapse point.** Perfect-response
rate reaches zero by N=80 instructions for every model, format and placement
[S-358]. The repo's fichas carry multiple constraints and nobody has counted
them.

**G17 — No measurement of context's effect on the model's own verification
behaviour.** The corpus may silently shorten reasoning by up to 74% and suppress
self-verification [S-311]. This is the highest-value unclaimed threat in the
three-front survey, because the R6 gate depends on the model checking itself.
Single small-author paper, so it is a hypothesis, not a result.

**G18 — No position-effect evidence on structured input.** The repo's U-curve
evidence is prose-only; lexical density is the measured variable for dense
structured corpora [S-350], and no source isolates schema placement
specifically. Declared gap in the repo's own catalogue, still open.

---

## 4. Experiments this pass justifies

`E-01`..`E-22` live in [04_EXPERIMENT_BACKLOG.md](04_EXPERIMENT_BACKLOG.md) and
are unchanged. These are new, ordered by expected value per GPU-hour. All are
proposals: none is preregistered, none is run, and per `AGENTS.md` §-2 rule 3 a
preregistro must be frozen before any run.

**E-23 — FormatSpread on the existing pipeline.** *Variable:* prompt template
paraphrase, 5 formats. *Metric:* goal-set retention and gate pass rate, reported
as a range. *Cost:* 0 GPU-h beyond re-running one existing configuration.
*Falsifier:* spread < 2 points falsifies G13 and retires the concern.
*Why first:* it qualifies the repo's best result with the cheapest possible
experiment, and [S-309] means the scorer must be held fixed and named.

**E-24 — Context load vs self-verification.** *Variable:* corpus present /
absent. *Metric:* whether the model requests or accepts fewer corrections, and
trace length. *Cost:* 0 GPU-h, same runs re-scored. *Falsifier:* no
measurable change falsifies G17. *Caveat to state in advance:* [S-311] is a
reasoning-model result and the AEGIS model is not a reasoning model, so a null
is genuinely informative rather than a failed replication.

**E-25 — Instruction-count ladder.** *Variable:* the number of simultaneous
constraints in one prompt, 4 → 12 → 20 → 40 → 80. *Metric:* adherence, not
retention. *Cost:* 0 GPU-h. *Falsifier:* no collapse below 80 falsifies G16 in
this regime and retires it.

**E-26 — Provenance audit at two baselines.** *Variable:* whether grounding is
checked against source spans or against compressed material. *Metric:* apparent
versus actual grounding. *Cost:* 0 GPU-h, a re-scoring pass over existing runs.
*Why it matters:* [S-249] predicts a ~7× inflation, and if it reproduces on
this corpus it is a finding about the repo's own verifier rather than a
literature citation.

**E-27 — APO against a hand-written baseline, properly powered.** *Variable:*
DSPy/GEPA optimisation of one ficha against the hand-written version, with a
held-out company and n from the ICC convergence figures [S-377]. *Falsifier:*
no gain on held-out data, or gain below 2–3 points (the noise floor [S-376]).
*Stated in advance:* [S-321] uses a weak baseline and [S-330] shows the
optimiser overfits its own selection set, so the expected result is null and
the experiment is worth running precisely because a null here is a *recorded*
answer rather than an unexamined assumption.

---

## 5. Two things this pass could not settle

1. **Whether any of it transfers to a 27B open-weight model.** Every
   prompt-design claim originates from frontier-model vendor documentation.
   [S-348] makes the general version of the point for context — open models lag
   closed ones exactly on complex instruction following at length — and nothing
   yet makes it for prompts. `E-23` is the cheapest probe.
2. **Register as a manipulated variable.** No source isolates statutory versus
   explanatory prose. [S-315] is a capability benchmark, not a prompt-design
   study. This is a gap in the literature rather than in the search, and a
   defensible place for the repo to contribute: register-controlled paraphrase
   over `baseline/domains/` articles with goal IDs held fixed.

---

## 6. Method, and what would falsify this document

This pass had `WebSearch` unavailable throughout. Discovery ran through the
arXiv API, direct canonical fetches and OpenAlex, which favours papers and
official documentation over practitioner write-ups. For prompt engineering
specifically — the most practitioner-heavy of the three topics — that is a
material bias and it is declared rather than discovered later.

Verification performed: 19 of 20 sampled URLs resolved; titles, authors and
abstracts were re-verified by direct fetch for 13 load-bearing entries; the
registry parses clean at 322 entries with no duplicate keys. Two sources that
turned out to be already registered were removed rather than duplicated, and
their existing entries re-pointed at the new pattern families.

**What would falsify the verdicts above.** `E-23` returning a spread under 2
points retires G13 and weakens §2.3 to a footnote. A null `E-24` retires G17
and removes the most alarming claim in this document. A GEPA run on this corpus
that beats a hand-written prompt by more than the noise floor on held-out
companies would falsify §2.5's practical reading and make APO a live option —
which, on [S-363] and [S-331], would then require the optimised prompt to land
as an immutable versioned artefact with the regeneration step recorded as
explicitly non-deterministic.
