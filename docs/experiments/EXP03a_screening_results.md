---
document_id: AEGIS-MODELS-M01-RESULTS
title: 'M01 screening results — four Deucalion models on the AEGIS pipeline'
version: 1.0.0
created: 2026-10-03
status: PARTIAL — screening closed, deep dive pending
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
- The two screening survivors' remaining runs (r04/r05 gemma4) were still in
  flight at analysis time; the numbers here are from the runs that closed.
- The comparison is single-case (TinyTask) by design (researcher decision);
  H4's version-isolation question needs the qwen3.5 re-run with a contract
  variant before it can be answered.
