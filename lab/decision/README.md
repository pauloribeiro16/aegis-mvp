# lab/decision — the d1 decision models, measured

> **What this is:** a lane that measures two open-weight decision models
> (`LiquidAI/d1-3B`, `LiquidAI/d1-omni-600M`) against the question that
> matters for this architecture: **does a decision model earn a place in the
> AEGIS pipeline, and where?**
> **What this is never:** part of the production pipeline.

## Hard rules of this lane

1. **The production pipeline is not touched.** Nothing in `pipeline/src/`,
   `pipeline/deucalion/`, the fichas, the gates or the parsers changes
   because of this lane. **There are zero overlays** — the lane adds no step,
   swaps no prompt and moves no threshold.
2. **The measurement is a pure function of the disk.** `p3a_gate` makes
   `n_calls: 0`, and the same is true here: the harness writes JSONL and the
   checker reads it. Nothing in the scoring depends on the state of the run
   that produced it.
3. **Ground truth is never self-declared.** Every label in the L3 layer
   comes from the corpus or from a deterministic artefact of the pipeline,
   and the cases where two of the project's own artefacts disagree are
   declared `contested` and reported separately.
4. **Unlabelled is not wrong.** A case without a label is measured and
   reported, and never enters the accuracy figure.
5. **A failing checker is a finding.** `check_suite.py` is written to fail
   when the answer shape is wrong; a green run that hides a shape violation
   is a broken checker, not a good model.

## The subject

Both models are **decision models**, not chat models: they do not write text.
They take a `state` and a set of typed `questions`, and return one answer per
question with a probability distribution and `output_tokens: 0`.

| | `d1-3B` | `d1-omni-600M` |
|---|---|---|
| parameters | 3.12 B | 587 M |
| built on | LFM2.5-VL-3B | LFM2.5-Encoder-350M |
| modalities | text, image | text, image, audio |
| context | 32 768 | 16 384 (896 text tokens with images) |
| trained in | bfloat16 | **float32** |
| vLLM route | **yes** — `/v1/systemone`, vLLM ≥ 0.32.0 | **no** — `D1OmniModel` is in no upstream vLLM release |

The question types are `noul` (a probability of yes), `choice` (a named
option with a distribution) and `score` (an expected level on an ordered
rubric). There is no OpenAI chat-completions route for these models: the
decision index is a top-level `questions` field on `POST /v1/systemone`.

## The arms, and why there are three

| Arm | Model | Route | Answers |
|---|---|---|---|
| **A1** | `d1-3B` | in-process (`trust_remote_code`) | what the checkpoint says |
| **A2** | `d1-3B` | vLLM 0.32.0 `/v1/systemone` | is the server faithful? |
| **A3** | `d1-omni-600M` | in-process, fp32 / fp16 / bf16 | which model, at equal accuracy? |

A1 exists because **vLLM does not run the checkpoint**. Its `LiquidStrategy`
rebuilds the checkpoint's prompt and reads next-token logprobs over the label
tokens; the checkpoint itself runs a tree-batched forward pass. Upstream
measured a maximum probability gap of 0.031 on one case. That gap is the
difference between a server you can put in front of the pipeline and one you
cannot, so it is measured here rather than assumed.

A1 vs A2 is therefore a **serving** comparison, and A1 vs A3 a **model**
comparison. Comparing A2 with A3 would confound the two.

## The four layers

- **L1 — contract.** The answer shape the Decision Index defines: a `noul`
  carries no confidence and no probabilities; a `choice` carries no legend;
  a `score` is zero-based, continuous, and carries both legend and
  probabilities; every distribution sums to 1; `output_tokens` is 0. Plus
  every error path — including the one where `d1-3B` **silently defaults an
  unknown question type to `choice`** while `d1-omni` raises.
- **L2 — fidelity.** A1 vs A2 on identical inputs: pick agreement and
  max |Δp|.
- **L3 — domain.** Four AEGIS decision sites on real content: regulation
  applicability, sub-domain trigger, tension activation, principle
  constraint, coverage verdict. Labels come from the corpus and from the
  pipeline's deterministic artefacts.
- **L4 — robustness.** The System-1 jaggedness, on our content: irrelevant
  content in the state, prompt injection through the state, a paraphrased
  question, repeat determinism, batch-shape sensitivity, and the context
  ceiling.

## Layout

```
lab/decision/
  README.md               this file
  PREREG_LAB03_D1.md      frozen before the measured runs
  backends.py             HttpBackend (/v1/systemone) + InProcBackend
  run_suite.py            one arm over one case file -> JSONL
  check_suite.py          JSONL -> contract invariants + accuracy
  report.py               arms -> the comparison report
  build_domain_cases.py   generates cases_domain.json from the artefacts
  preflight.py            the whole chain against a stub, no model, no GPU
  cases_smoke.json        four cases: proves the route works
  cases_protocol.json     L1 + L4
  cases_domain.json       L3, generated — do not hand-edit
  labelling_sheet.md      the cases that need a human label
  deucalion/
    build_venv.sbatch     vLLM 0.32.0 + transformers 5.16.1 (dev-x86)
    stage_weights.sh      hf download, on the login node
    serve_vllm.sbatch     arm A2: serve + run
    run_inproc.sbatch     arms A1 / A3: load + run
    sync.sh               push the lane to the cluster
```

## Running it

```bash
# Stage 0 — the whole chain against a stub, on the workstation.
python3 lab/decision/preflight.py          # -> PREFLIGHT OK

# Push the lane and the weights.
bash lab/decision/deucalion/sync.sh
ssh login 'bash .../aegis-d1-exp/deucalion/stage_weights.sh'

# Stage 2 — build the vLLM 0.32.0 venv (dev-x86, no GPU).
sbatch deucalion/build_venv.sbatch

# Stage 3 — smoke: does the serving route work at all?
sbatch --export=ARM=A2,CASES=cases_smoke.json deucalion/serve_vllm.sbatch

# Stage 4 — the arms.
sbatch --export=ARM=A2,CASES=cases_protocol.json deucalion/serve_vllm.sbatch
sbatch --export=ARM=A1,DTYPE=bfloat16,CASES=cases_protocol.json deucalion/run_inproc.sbatch
sbatch --export=ARM=A3,MODEL_DIR=.../LiquidAI_d1-omni-600M,DTYPE=float32,AUDIO_CAPABLE=1 \
        deucalion/run_inproc.sbatch
```

## The cluster, and what it cost to learn

- The cluster's only vLLM is **0.10.0**, whose registry has neither
  `Lfm2VlForConditionalGeneration` nor `D1OmniModel`. Serving d1 needs
  **0.32.0**, so this lane builds a **second** venv and leaves the old one
  alone: the old one serves the Qwen FP8 scout.
- `llguidance` publishes no `manylinux_2_28` wheel — its Linux wheels are
  `manylinux_2_31` and this cluster is glibc 2.28 — so pip falls back to a
  Rust sdist build. The build must keep `CARGO_HOME` on local disk: the
  default (`$HOME/.cache`, quota-limited) dies with *"Disk quota exceeded"*.
- `/home/paulinho` has a 20 GB quota with the file-count soft limit already
  exceeded. The venv and the weights live on `/projects`.
- Compute nodes have **no egress**. Weights are downloaded on the login
  node; pip resolves from the internal mirror `http://sn02:9191/index/`.
- `grep … | head -1` under `set -o pipefail` + `set -e` aborts a script
  silently (SIGPIPE → 141). The staging script uses `grep -m1`.
- **gnx520's A100 is in an error state.** `nvidia-smi` reports `ERR!` with
  50 GB held by a process Slurm has lost track of; torch sees
  `device_count=1` but every CUDA init fails with *"No CUDA GPUs are
  available"*, and vLLM dies with an opaque engine-core traceback that
  blames the model. The lane excludes that node and every job opens with a
  CUDA health gate that fails with the real reason.
- The two routes do not return the same shape: the checkpoint's `noul` is
  `{type, noul}` with `output_tokens: 0`, and the vLLM route returns the
  full typed answer with `output_tokens` counting the label tokens it read.
  The checker holds each route to its own shape; the difference is a
  finding, recorded in `PREREG_LAB03_D1.md` §7.

## What came out

**[`RESULTS_LAB03_D1.md`](RESULTS_LAB03_D1.md)** — the results doc, with the
ten preregistered verdicts (five hold, four are refuted, one is a compound
result), the findings, the negative results and the deviations.

The machine artefacts behind it:

| file | what |
|---|---|
| `results/REPORT.md` | the generated report: per-arm summary, per-site tables, pairwise comparisons, contrast pairs, per-case answers |
| `results/predictions.md` | the preregistered verdicts, computed from the records |
| `results/summary.json` | the checker's per-arm summary |
| `results/A*_cases_*.jsonl` | the raw records — one per arm per case file |
| `results/cluster_run_logs.txt` | the five arms' run logs from the cluster |

The numbers that decide whether a decision model enters the architecture are
the **agreement between the server and the checkpoint** (P1) and the
**accuracy on the labelled AEGIS sites** (P2, P3) — not the latency.

The short version of what was found:

- The **vLLM route is faithful** to the checkpoint (97.25 % pick agreement,
  max |Δp| 0.031 on labelled cases) and **refuses** an over-long state that
  the checkpoint silently truncates and answers confidently about.
- The **smaller model is the more accurate one** on our content
  (d1-omni-600M 0.714 vs d1-3B 0.643), and the two fail on **opposite**
  sites, each with a one-sided bias.
- The **irrelevant-content** and **prompt-injection** effects are present,
  and they hit the two models in opposite directions.
- The **adjusted-goal badge collapse** (0.99 `unchanged`) is reproduced by a
  completely independent instrument — which points at the Phase 1 goal text
  rather than at the instrument that reads it.
