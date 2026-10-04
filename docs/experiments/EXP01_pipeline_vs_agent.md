---
document_id: AEGIS-EXP-01
title: 'EXP-01 — Fixed-prompt pipeline vs directed agent (Case_01 TinyTask)'
version: 0.1.0
created: 2026-10-03
status: DRAFT
---

# EXP-01 — Pipeline (fixed prompts) vs directed agent

**Question.** Can a tool-calling agent produce a `doc02_adjusted_goals.md` of the
same genre as the fixed-prompt pipeline, and which produces the better result?

**Controlled comparison.** Same case (`Case_01_TinyTask_SaaS`), same corpus, same
model (`qwen3.8:27b` on the Deucalion A100 node), same L0 parsers, same content
gates, same zero-LLM assembler (`assemble_doc`) and the same L1 validator. The
only variable is who decides the working order and granularity.

**Honest asymmetry, stated up front.** The agent can call `finalize`, see the L1
findings and repair before finishing; the pipeline gets one L0 repair retry per
call and no post-assembly loop. That difference is part of what is being
measured, and is reported as such below.

---

## 1. Result — both arms complete, both L1 PASS

Identical case, corpus, model, parsers, content gates, assembler and validator.
The only variable is who decides the working order and granularity.

| | **A — pipeline** (`run_v2_1971142`) | **B — agent** (`run_agent03_1971145`) |
|---|---|---|
| L1 validation | **PASS** | **PASS** |
| Sub-domains selected / goal rows | 37 / 65 | 38 / 65 |
| Tension resolutions (§4) | 2 | 3 |
| Document size | 228,130 chars | 215,602 chars |
| LLM calls / turns | **42** | **220** |
| Context tokens (est., cumulative) | 717,698 | **4,640,784** |
| Output tokens generated | 28,176 | 30,802 |
| LLM time | **1,304 s** | 3,716 s |
| Pattern mix | maintain 48 / achieve 17 | maintain 62 / achieve 3 |
| Adjustment mix | unchanged 48 / **narrowed 17** | unchanged 64 / narrowed 1 |
| Goal length (median) | 79 words | 64 words |
| Technology leaks | 0 | 0 |

Both reach 65 goal rows and neither drops an obligation, which is the strongest
evidence that the contract — not the orchestration — determines the output. The
pipeline's P3 selected 37 sub-domains and the agent's 38; that single unit is a
selection judgement, not a defect, and both selections are L1-valid.

They diverge on three axes:

- **Cost** — 5.2× the calls and 2.8× the wall clock for the agent, for the same
  output.
- **Context** — the agent's cumulative prompt is **6.5× the pipeline's**
  (4.64 M vs 718 k tokens). Its per-turn history carries the whole conversation,
  so the cost compounds with every turn. This is the concrete cost of the
  context-management problem, and it is why the pipeline wins on economics.
- **Judgement mix** — the pipeline reaches for `achieve` and `narrowed` far more
  often (17 narrowed against 1), which is the visible effect of the
  per-step decision rule in its pack.

## 1b. The prompt change is measurable

The same pipeline code, same model, same case, one prompt change — the
`Adjustment` menu replaced by a decision rule:

| | v1 (menu) | v2 (decision rule) |
|---|---|---|
| `unchanged` | 63 | 48 |
| `narrowed` | 1 | **17** |
| `flagged` | 1 | 0 |

The rule ("`unchanged` only when the duty applies verbatim with no scope change;
otherwise scope it to a surface the company actually has; flag it when it turns
on something unreviewed") moved 16 rows out of the default answer. The agent
received the same rule in its system brief and moved 0 — the per-step
instruction in the pipeline's pack is the stronger delivery channel for this
model.

## 1c. The agent arm's one real advantage: the missing-tension catch

The agent's first complete run produced **zero** tension resolutions where the
pipeline produced two. The cause was not the model's judgement: the tool
description offered `None.` as an equal option and the model took it, without
ever reading the corpus. Adding `list_corpus_tensions` — and rejecting a bare
`None.` unless a `none_reason` is supplied — moved it from 0 to **3**, more than
the pipeline.

This is the clearest case in the experiment of the agent pattern paying off: a
tool surface that forces the model to *look before deciding* catches something
the fixed pipeline's step-ordering happened to get right by construction.

 A calibration finding that turned out NOT to be a defect

The pipeline run produced 63 of 65 rows with `Adjustment = unchanged`, against a
hand-written 4-row example (`example/doc02_adjusted_goals.md`) where every row is
`narrowed` or `flagged`. Read at face value that is a systematic loss of
calibration.

It is not, and the two are consistent with their companies:

- The hand-written example is **VetCare**, whose appointment app is *built and
  operated by an external software house*. Almost every duty therefore has a
  scope to delegate away, and the `Adjustment` field is where that delegation is
  recorded — `narrowed` is the correct answer for that company.
- The pipeline run is **TinyTask**, which *is* the manufacturer and operator of
  its own SaaS. There is less inherited capability to narrow away, so
  `unchanged — fits as stated` is often correct, and the company calibration
  lives in the `Adjusted goal` and `Company implication` columns instead — where
  it is present and specific (named data categories, the controller/processor
  split, the payment sub-processor, the 8-person scale, the 72-hour clock).

Reading the actual rows confirms the calibration: `AG-D-01.1-001` retains the
full Art. 5(1)(f)/32 duty and narrows it to the company's actual holdings;
`AG-D-06.1-001` names the Art. 28(3) closed list and the sub-processor
authorisation chain; `AG-D-10.1-001` enumerates the five Art. 32(2) risk types.

**Method note.** `output/TinyTask/doc02_adjusted_goals.md` (38 sub-domains, 65
rows, L1 PASS) is the quality reference for the current contract. The 4-row
VetCare file is a hand-authored cross-company sample, useful for showing the
method generalises, but n=4 is far too small to support any distribution claim —
and it is deliberately not injected into the TinyTask pack, because the model
producing a given run must never see that run's own output.

The prompt change that survived this exercise is therefore not "narrow more" but
a *decision rule*: `unchanged` only when the duty applies verbatim with no scope
change; `narrowed` when it must be scoped to a surface/role the company actually
has; `flagged` when it turns on something not yet reviewed.

## 2. What the agent arm exposed (design findings, not just failures)

These are the reusable results of the experiment, independent of which arm wins:

1. **Repetition is a code problem, not a prompt problem.** The first agent run
   issued 163 byte-identical `read_regulation_module` calls. Guarding in the
   prompt does not stop it; the loop was broken by (a) a canonical
   `(tool, args)` signature with a refusal that carries the *next step*, and
   (b) a progress watchdog on the on-disk artifact set.
2. **Long tool-call arguments must not carry the artifact.** The pipeline arm
   itself died twice on `p4_D-08_3` with a truncated L0 repair at the
   `num_predict` cap — the same class as the agent's malformed calls. Fixed on
   both sides (per-row submission for the agent; 16k budget for the pipeline).
3. **History is imitation bait.** An elision placeholder in context was copied
   verbatim into a tool call's arguments, producing a permanently invalid call.
   Submission turns are now compressed to a plain-text note, leaving nothing to
   imitate.
4. **Sequenced work must be enumerated in code.** 38 sub-domains is a natural
   plan; with ground truth about what remains, "is this a repeat?" becomes a set
   membership test the model cannot argue with.
5. **The gates, not the model, are the binding constraint on goal prose.** Both
   arms converge on the same failure: the 30 % obligation-retention floor versus
   a rubric that asks for a company-proportional restatement rather than a copy.
   Measured on the run that passed: retention median 73 % (min 32 %), so the
   floor is reachable — but only after retries, and the agent arm never got past
   11–27 % on its own. The instruction is now an **absolute count with the
   missing terms listed** rather than a percentage, because aggregate numeric
   ratios are the encoding mid-size models handle worst.
6. **The 0.88 near-verbatim gate never fires.** Across all 65 rows of the passing
   run the maximum similarity to the baseline is **0.79**. It is currently dead
   weight; it is left in place (removing a safety gate is a human call) but it
   should not be read as an active constraint.
7. **Tool surface size matters.** The agent's 13 tools are now phase-scoped to
   2–5 per phase. Fewer visible tools measurably improves selection accuracy for
   this model class, and the planner already knows the phase, so it costs
   nothing.

---

## 3. Changes made to the pipeline arm as a result

- `p4_extra_instruction(sd, carries_subso=False)` states the valid answer for a
  module with no Sub-SO under the confirmed regulations, instead of letting the
  model invent rows and fail L0 twice per call.
- `NUM_PREDICT["p4"]` 8192 → 16384 (the P4 answer is a full table, not a
  sentence).
- The obligation-retention rejection now carries the Sub-SO objective verbatim.
- `think: false` on every call (qwen's reasoning tokens otherwise share the
  answer's `num_predict` budget — job 1963648 returned empty content).
- `done_reason == "length"` is a retryable failure, not a silently accepted
  artifact.
- Failed stages are recorded in `manifest.json` instead of leaving no trace.

---

## 4. L2 human scoring rubric (superseded by L2_RUBRIC.md)

Both deliverables are scored without knowing which arm produced them. Per unit,
1–5:

| Unit | Criterion | Score A | Score B |
|---|---|---|---|
| Framing (§2, per dimension) | every claim traced to the intake; correct tier consequence | | |
| Goal row (per row) | obligation legs all retained | | |
| | company-proportional (right altitude, real company facts) | | |
| | implication says something true and specific to *this* company | | |
| | pattern/property correct, not just in-vocabulary | | |
| | adjustment honest (`unchanged` justified, `narrowed` names a warrant) | | |
| Tension resolution (§4) | correct set of activating tensions | | |
| | binding rule auditable and enforceable | | |

Aggregate: mean score, share of rows at 4+, worst-5 counts, and a count of
rows where the implication would be equally true of a different company (the
"reusable sentence" defect the content gate only approximates).

---

## 5. How to see this

```bash
cd ~/Work/aegis-inspector && pnpm dev      # http://localhost:5173
```

`/runs/<id>` for stage history, per-call forensics and live L1 validation;
`/runs/<id>/deliverable` for the rendered document; `/compare?a=…&b=…` for the two
arms side by side with their trace metrics.
