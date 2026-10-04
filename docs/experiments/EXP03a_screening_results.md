---
document_id: AEGIS-MODELS-M01-RESULTS
title: 'M01 screening results — four Deucalion models on the AEGIS pipeline'
version: 1.1.0
created: 2026-10-03
status: PARTIAL — screening closed, p3 root cause found, m02 re-test in flight
sources: 'docs/research/sources.yaml'
upstream: '[00_RESULTS.md](00_RESULTS.md)'
---

# M01 — model matrix: screening results

**Question (registered in `aegis-models/PREREG-M01.md` before any run).** With
the model as the *only* variable — same case, corpus, prompts, gates,
assembler, validator — which models can run the pipeline at all, and how do
they differ from the qwen3.8 reference?

**Design.** Tier 0 smoke (`p1`+`p2`, harness correctness) → Tier 1 screening
(5 full runs per smoke-pass model) → Tier 2 deep dive (n=15, finalists).
All runs seeded (42) per the EXP-02 decision; unseeded runs abort ~40% of the
time on the R6 gate, so an unseeded model matrix would measure abort rates, not
models.

---

## 1. Smoke: 4 of 6 candidates run the pipeline

| Model | Smoke | Evidence |
|---|---|---|
| gemma4:31b | pass | both steps L0-valid, ~2.0k prompt tokens, no escalation |
| glm-4.7-flash | pass | both steps L0-valid, ~1.9k tokens |
| muse-glimmer:30b | pass | both steps L0-valid, ~1.9k tokens |
| nemotron-3.5-lightning:30b | pass | both steps L0-valid, ~1.9k tokens |
| qwen3.5:27b | **fail — contract** | free prose; never wrapped the answer in the required fenced block, even after the repair retry |
| ornith-1.5:35b | **fail — runtime** | CUDA illegal-memory-access inside the model on the first call (HTTP 500) |

**Two distinct failure classes.** qwen3.5 is a *contract* failure — the model
answers plausibly but does not follow the output-format instruction, which is
the failure class the research attributes to post-hoc parsing (registry S-046)
and the strongest argument for schema-constrained decoding. ornith is a
*runtime* failure — the model itself crashes; nothing in the harness could fix
it.

## 2. Screening: 2 of 4 cut, for a deterministic reason

| Model | Screening | Cause |
|---|---|---|
| gemma4:31b | in | — |
| muse-glimmer:30b | in | — |
| glm-4.7-flash | **cut** | 5/5 runs abort at p3: "sub-domain D-02.4 appears both selected and excluded" — the same sub-domain in both lists, every time |
| nemotron-3.5-lightning | **cut** | 5/5 runs abort at p3: "excluded sub-domain D-10.4 is not in the candidate set" — excludes an id outside the pool, every time |

Both cuts are **deterministic selection-contract incompatibilities, not noise**:
a different sampling seed would not change the outcome. They are recorded with
their cuts in `aegis-models/MODELS.yaml`. Revisiting them requires a
P3-contract variant (schema-constrained selection output), not more runs.

## 3. What the two surviving models do (n=4 and n=3 closed)

| Model | runs closed | L1 | retention mean [95% CI] | calls | LLM s | `narrowed` range |
|---|---|---|---|---|---|---|
| **qwen3.8:27b** (reference) | 15 | 15/15 | 0.7171 [—] sd 0.0000 | 43 | 1,299 | 8–8 |
| **gemma4:31b** | 4 | 4/4 | 0.6532 [0.6498, 0.6554] sd 0.0035 | 42 | 1,391 | 40–43 |
| **muse-glimmer:30b** | 3 | 3/3 | 0.8036 [0.7961, 0.8147] sd 0.0098 | 42 | 2,481 | 15–21 |

Against the reference (whose within-arm sd is exactly 0, so every difference
is detectability-bound):

| Comparison | Δ retention | effect | detectability | Cliff's δ | verdict |
|---|---|---|---|---|---|
| gemma4 − qwen3.8 | **−0.064** | −25.6 sd | 45.4 | −1.00 | distinguishable |
| muse-glimmer − qwen3.8 | **+0.087** | +12.5 sd | 19.8 | +1.00 | distinguishable |

**The contract generalises; the behaviour does not.** All three models reach
L1 PASS with 42–43 calls — the harness is model-agnostic in structure. But the
two differences that matter are large and opposite:

- **gemma4 retains the least** of the baseline obligation (0.653 vs 0.717) and
  **calibrates hardest** — `narrowed` on 40–43 of 65 rows versus qwen3.8's 8.
  It is rewriting the regulatory duty more aggressively in the company's terms.
- **muse-glimmer retains the most** (0.804, +14% over the reference) at
  **1.9× the wall time** (2,481 s vs 1,299 s) with the same call count — it
  generates longer answers per call.

**None of this says which is better.** Retention measures how much of the
baseline survives, not whether the surviving text is correct or well-calibrated;
a high retention could equally mean faithful restatement or copying. This is
exactly the question the blind human rubric (EXP-03, `L2_RUBRIC.md`) is
designed to answer, and it now has a third arm worth scoring: muse-glimmer is
the only model so far that looks materially *different* from qwen3.8 on the
substance metrics rather than merely on cost.

## 4. Next: deep dive on the two finalists

Tier 2 (n=15 per model, same seeded config) is the next step for gemma4 and
muse-glimmer, and it buys the error bars the screening cut cannot provide at
n=3–4. The EXP-03 blind-scoring pack should include both of them alongside the
qwen3.8 pipeline and agent arms.

## 5. Honest notes

- n=4 (gemma4) and n=3 (muse) are screening numbers: enough to rank, not
  enough to report as estimates. The intervals are bootstrap CIs on 3–4 points
  and are optimistic by construction.
- The comparison is single-case (TinyTask) by design (researcher decision);
  H4's version-isolation question needs the qwen3.5 re-run with a contract
  variant before it can be answered.

## 6. Root cause of the two cuts — a prompt defect, not (only) a model defect

The two cuts were recorded as "deterministic selection-contract
incompatibilities". Reading the two aborted answers side by side
(`run_m01_glm47_r01_1979027/outputs/003_p3_response.json` and
`run_m01_nemotron_r01_1979047/outputs/003_p3_response.json`) shows a shared
cause in the prompt, PROM-P1-03 v1.1.0.

Both models wrote a correct §3 table covering the candidate set, then filled
the exclusion slot:

- **glm-4.7-flash** selected D-02.4 in the table and then wrote
  `Excluded candidates: D-02.4 — no company fact triggers it`. The two lists
  are disjoint by construction, so the gate was right to refuse.
- **nemotron** wrote `Excluded candidates: D-06.5 — N/A (no D-06.5 in candidate
  set)` — an id that does not exist anywhere in the corpus. On the repair retry
  it repeated the id **and the reason it was wrong, in the same line**.

v1.1.0 showed the exclusion line only in its non-empty form, never stated that
a sub-domain may not appear in both lists, and never said the list could be
empty. It presented a slot with no legal empty value; two models filled it
rather than leaving it blank. That is a defect in the instrument, and a model
comparison run on it measures the prompt as much as the model.

**Revision PROM-P1-03 → v1.2.0 (2026-10-04):** the §3 table and the exclusion
list are stated as an explicit partition of the candidate set; the empty form
`Excluded candidates: (none — every candidate is triggered)` is given; the
exclusion step says "move … remove its row from the §3 table in this same
answer"; and rule 1 now says an unsure id must be left IN the table rather than
named, because an invented id is a hard failure.

**What this does and does not license.** It does not license re-scoring the
m01 runs as glm47/nemotron failures — those runs are evidence of what the
pipeline did with v1.1.0, and they are kept. The re-test is a **new tier
(`m02`), not a re-run of `m01`**, because a prompt revision changes the
instrument: filing both under one tier would make the pre-fix and post-fix
answers indistinguishable. Since m01 recorded only `git rev` — which a prompt
edit does not change — that split was previously unprovable from the run
directory. Every run now carries `prompt_digests` in `config.json` (sha256,
truncated, of all seven fichas plus the golden exemplar), so the instrument is
machine-checkable from the artefacts. The `m02` launches record the v1.2.0
digest; the `m01` runs predate the field.

**Read the cut as it now stands:** 0/5 for each model under v1.1.0, with a
named, fixed, and now testable cause. Whether that cause was the whole story is
what the m02 tier measures.

## 7. A reproducibility gap this experiment exposed

Before the digest field existed, a run recorded its model, its sampler, and its
`git rev` — and nothing about the prompt *text*. Three findings in this
experiment would have been silently incomparable across a prompt edit: the p3
revision above, the EXP-04 ablation, and the per-step instruction variants.
`prompt_digests` closes that; runs predating it are marked by the absent field
rather than by a guess.
