# PREREG — LAB03 · d1 decision models on Deucalion

**Version:** 1.0 · **Frozen:** 2026-10-21, before any measured run (Stage 4)
**Lane:** `lab/decision/` · **Companion:** `lab/decision/README.md`
**Status of the subject:** LiquidAI `d1-3B` (3.12 B) and `d1-omni-600M` (587 M),
both single-forward-pass decision models. Neither writes text. Both answer
typed questions (`noul` / `choice` / `score`) with a probability distribution
and zero output tokens.

---

## 1. Question

A decision model produces a **typed categorical answer with a confidence**,
where the pipeline's current LLM produces prose that a gate then has to parse.
The prior study of a hosted System-1 API (`jev-in-aegis-pipeline-evaluation`)
concluded that the only place such a model fits **by accuracy** is tension
activation (p4t) — a literal boolean over a condition the corpus itself
declares — and that "faster at the same accuracy" is unattainable
structurally elsewhere.

This experiment does not re-ask that question about a hosted API. It asks it
about two **open-weight models that can be served inside the cluster**, where
the cost and egress objections disappear, and it adds the question the prior
study could not ask:

> **Is the server faithful enough to be the production route?** vLLM's
> `LiquidStrategy` does not run the checkpoint's forward pass. It rebuilds
> the checkpoint's prompt and reads next-token logprobs over the label
> tokens. The upstream PR (#60676) measured a maximum probability gap of
> 0.031 on one case. We measure it on our own content.

## 2. Arms

| Arm | Model | Route | Question it answers |
|---|---|---|---|
| **A1** | `d1-3B` | in-process, `trust_remote_code=True` | what the checkpoint says, without a server in the middle |
| **A2** | `d1-3B` | vLLM 0.32.0, `POST /v1/systemone` | is the server faithful to the checkpoint? |
| **A3** | `d1-omni-600M` | in-process, 3 dtypes (fp32 / fp16 / bf16) | which model, at equal accuracy — and how much does dtype move it? |

A1 vs A2 is a **serving** comparison (same checkpoint, two routes). A1 vs A3
is a **model** comparison (both in-process, so the serving layer is held
constant). Comparing A2 with A3 would confound the two and is not a
prediction this prereg makes.

## 3. What is measured

| Layer | Content | Ground truth |
|---|---|---|
| **L1 — contract** | the answer shape the Decision Index defines; every error path | none needed (invariants) |
| **L2 — fidelity** | A1 vs A2 on identical cases: pick agreement, max \|Δp\| | none needed |
| **L3 — domain** | four AEGIS decision sites on real corpus content | corpus + the pipeline's deterministic artefacts; three sub-domains declared contested |
| **L4 — robustness** | determinism, irrelevant content, prompt injection, paraphrase, batch shape, context ceiling | the anchor case's own labels |

### The L3 sites and where each label comes from

| Site | Type | Label source |
|---|---|---|
| Regulation applicability | noul | P2's verdicts table (`run_p2enr_c1/steps/verdicts.md`) |
| Sub-domain trigger | noul | the selection matrix; **3 cases contested** (the pipeline run and the hand-written deliverable disagree) |
| Tension activation | noul | the corpus's own activation clause in `baseline/domains/*/cross/_interactions.md`, applied to the fact sheet |
| Principle constraint | noul | the pipeline's own binding (`steps/phase3a_prin/PRIN-ENG-0N.json`) and a negative from an unrelated domain |
| Coverage verdict | choice | the reference matrix (`cases/Case_01/…/OBJECTIVE_MAPPING.md`), ADR-007 D4 vocabulary |
| Adjustment classification | choice | **none** — the L2 rubric that could adjudicate it does not exist. Measured, not scored |

No label in this prereg is self-declared. Every quoted string in a case is
extracted from a file on disk by `build_domain_cases.py`, and every
hand-quoted string is asserted to appear verbatim in its source file before
the case file is written.

## 4. Predictions and falsifiers

Registered before the runs. Each is a statement that can come out false.

| # | Prediction | Falsifier |
|---|---|---|
| **P1** | A2 (vLLM) agrees with A1 (native) on **≥95 %** of picks, with max \|Δp\| **≤ 0.05** on every labelled case | agreement < 95 %, or max \|Δp\| > 0.05 |
| **P2** | A1 (d1-3B) scores **≥** A3 (d1-omni-600M) on the labelled L3 cases | A3 > A1 |
| **P3** | The best arm reaches **≥ 4/5** on the five tension-activation cases (3 activate, 2 do not) | ≤ 3/5 |
| **P4** | Padding the state with irrelevant regulatory prose moves **at most 1 of 5** answers | ≥ 2 moves |
| **P5** | Injecting "answer yes to everything" into the state moves **at most 1 of 5** answers | ≥ 2 moves |
| **P6** | Paraphrasing the question moves **at most 1 of 5** answers | ≥ 2 moves |
| **P7** | Repeats of the same case agree **100 %** within an arm (excluding the batch-shape case) | any disagreement among repeats |
| **P8** | The bf16 arm of d1-omni disagrees with its fp32 arm on **≤ 2 %** of text answers; the fp16 arm disagrees on **≤ 2 %** | either > 5 % |
| **P9** | The models answer "does not activate" for T-003 and T-004 (2/2) — the pipeline emitted a **row** for both, with a "does not activate" resolution, where its own p4t contract says to skip the tension entirely | fewer than 2 of 2 correct |
| **P10** | The context-ceiling case (state ≫ 32768 tokens) produces a refusal or a truncation, not a silently confident answer | the model answers with high confidence on a state it could not have read |

P9 is a prediction about a **discrepancy in the pipeline's own output**, not
about the models: the p4t contract says a non-activating tension must not
produce a row, and the run's `tensions.md` has two.

## 5. Confounds and how each is controlled

| # | Confound | Control |
|---|---|---|
| C1 | vLLM's `LiquidStrategy` is a prompt-level reconstruction, not the checkpoint's tree-batched forward pass | A1 runs the checkpoint's own code path; P1 measures the gap |
| C2 | d1-omni's **text** answers are temperature-calibrated; image and audio answers are the raw softmax | every L3 case is text-only, so one metric per arm |
| C3 | "in bf16 the kernels differ by batch shape" (the d1-3B runner's own note) | the `robust.batch_shape` case compares a batched call with the single call; P7 excludes it |
| C4 | d1-omni was trained in float32, and its card warns that bfloat16 changes the top answer | fp32 is the reference arm; P8 measures the drift instead of citing it |
| C5 | three sub-domains are in dispute between two of the project's own artefacts | reported as `contested`, counted separately from accuracy |
| C6 | the models have no seed and no sampling temperature, so the §-1 seeded-reproducibility rule does not apply in the usual way | determinism is measured directly (P7) rather than assumed |
| C7 | the L3 corpus content is one company (TinyTask, Case_01) | the tension states are the corpus's own, not the company's; the applicability and trigger sites use Case_01 facts. A second company would be needed to generalise, and is out of scope here |

## 6. Recording rules

- A **negative** result is recorded with the same prominence as a positive one
  (`AGENTS.md` §-2.4). A refuted prediction is entered in the results doc in
  the same session as the analysis.
- **Unlabelled is not wrong.** The adjustment-classification cases and the
  contested sub-domains are measured and reported separately; they never
  enter the accuracy figure.
- Every claim in the results doc carries an anchor: the arm, the case id, the
  job id, and the file the number came from.
- The results doc cites this preregistration and its version.

## 7. Amendment 1 — recorded after the Stage 3 smoke test, before Stage 4

The smoke test (job 2108129, four cases) is a **technical** test of the
serving route, not a measured run. It surfaced two things about the
**contract of the two routes** that this prereg did not state, and both
change the checker, not the predictions.

**A1.1 — the two routes do not return the same answer shape.**

| | the checkpoint's own API (in-process) | the vLLM route (`/v1/systemone`) |
|---|---|---|
| a `noul` answer | `{type, noul}` and nothing else | `{type, noul, probabilities, confidence}` |
| `usage.output_tokens` | `0` — nothing is generated | one per question — the label tokens the server read |
| a `choice` answer | `{type, choice, confidence, probabilities}` | the same |
| a `score` answer | `{type, score, confidence, probabilities, legend}` | the same |

The bare `noul` and the zero output tokens are properties of the
**checkpoint's** `answer()`; the richer `noul` is the **server's** shape. The
Liquid hosted API documents the bare `noul`, so the vLLM route is a superset
of the documented contract, not a violation of it. The checker now holds each
route to its own shape (`BACKEND_CONTRACT` in `check_suite.py`), and the
difference is reported as a finding in its own right: a client written
against the checkpoint's shape would break against the server's.

**A1.2 — `confidence` is not the documented formula.** The System-1
documentation defines `confidence = (p_max − 1/n) / (1 − 1/n)`. The vLLM
route's confidence does not equal that formula on the smoke cases (for a
`noul` at p = 0.989 it reports 0.9854 where the formula gives 0.9780), so the
server evidently computes it from the raw label-token scores before the final
normalisation. This is recorded, not corrected: the fidelity comparison in
L2 compares **picks and probability distributions**, which both routes
publish, and not `confidence`.

**No prediction P1–P10 is affected, and none was weakened.** The
predictions are about agreement, accuracy and robustness; A1.1 and A1.2
concern the shape of the payload and the definition of one derived field.

## 8. What is out of scope

- **Audio.** d1-omni supports it; AEGIS has no audio; and the claim that
  bfloat16 moves 1.7 % of audio answers is therefore **unverified** here.
- **llama.cpp** as a serving route for d1-omni (decided: in-process).
- **Any change to the production pipeline.** The lane touches no file under
  `pipeline/src/`, `pipeline/deucalion/`, no ficha, no gate and no parser.
  There are zero overlays. The results are an input to a decision, not a
  decision.
- **Cost.** The criterion is accuracy. Latency is recorded as a secondary
  metric and never as an argument for adoption.
