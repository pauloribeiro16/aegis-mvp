---
document_id: AEGIS-MVP-ADR-012
title: 'Pack budget and context policy — decompose p4t, separate the two budgets, measure the overflow instead of engineering around it'
status: 'ACCEPTED (D1, D3, D4, D5, D6) — decided by the researcher, 2026-10-05; D2 recorded as PROPOSED and not decided'
date: 2026-10-05
phase: 'Cross-phase (0–3), pipeline layer'
author: 'Decision: PhD researcher; formalization + record: Executor session'
---

# ADR-012 — Pack budget and context policy

> Registered decision (2026-10-05): after Case 03 (OmniBank — 5 confirmed
> regulations, 38 selected sub-domains, 49 MB corpus) the researcher asked that
> the context problem be **registered before any code change lands** — *"regista
> isso"*. This ADR is that registration. It fixes the policy and the shape of the
> fix; it does not implement it. D2 is deliberately left **PROPOSED**, because
> whether to prune the pairwise `cross/` fan-out at all is an open question
> (E-16) and this ADR records the *rule for deciding it*, not the cut.

## 1. Context

Every figure below was re-measured on 2026-10-05 against the artefacts named, and
is cited with the file, the line, or the job that produced it. Prose without an
anchor is not in this document.

### 1.1 p4t is one monolithic call and it is the largest prompt in the pipeline

- `pipeline/src/steps.py:1151-1161` (`stage_p4t`) issues a single
  `self._call("p4t", None)` — no sub-domain argument, one call for the whole
  selection. The pack is assembled at `pipeline/src/compose.py:569-587`, one
  `cross/_interactions.md` tension block per selected sub-domain, concatenated.
- Measured (Case 03, job **1983144**, `muse-glimmer:30b`): `attempt1_prompt_tokens`
  = **44,826**, `system_chars` + `user_chars` = 189,174, `num_ctx` escalated
  32,768 → **65,536**.
- The pack's size tracks the **selection**, not the regulation count. Recomputed
  2026-10-05 with `compose.compose_call` on the current corpus: Case 01 (2 regs)
  **190,078 B** · Case 02 (4 regs) **190,762 B** · Case 03 (5 regs) **190,882 B**
  — a **0.4 % spread across a 2→4→5 regulation change**. Case 01 and Case 02 both
  select all 38 sub-domains, and each of the 38 contributes a block whether one
  regulation is confirmed or five.
- The ladder is exercised, but only just: the largest prompt token count ever sent
  in this programme is **50,054** (`p4_D-09_1`, `run_sec03_p1_1979371`), and the
  65,536 rung absorbed the p4t step at 46,978 real prompt tokens (jobs 1979370,
  1979371).

### 1.2 Pairwise cross-regulation text is the largest single block of a p4 pack, and it is quadratic

- `pipeline/src/compose.py:527-531` enumerates
  `["-".join(sorted((a, b))) + ".md" for i, a in enumerate(confirmed) for b in
  confirmed[i + 1:]]` — every unordered pair of confirmed regulations, so the pack
  cost is **C(n,2)**. Five confirmed regulations (Case 03, `verdicts.json`: GDPR,
  CRA, NIS2, DORA, AI_Act) → **10 pair files**. Eight would be 28.
- Measured on the Case 03 **D-04.3** pack (5 regs, 10 pairs), recomputed
  2026-10-05: total call **135,955 B**, of which

  | Block | Bytes | Share |
  |---|---|---|
  | `cross/<R1>-<R2>.md` (10 files) | 61,299 | **45.1 %** |
  | `regs/<REG>.md` (5 modules) | 51,516 | 37.9 % |
  | system prompt + instruction + output schema + self-checks | 6,902 | **5.1 %** |
  | `objective.md`, §3 table contract, worked example, SPEC §7, framing, fact sheet, build manifest | 16,238 | 11.9 % |

  (Bytes are UTF-8, measured as `len(text.encode("utf-8"))` per wrapped file, so
  they include the per-file provenance header that `wrap_file` adds.)

- The p4 instruction does not ask for pairwise analysis. It asks for one
  nine-column adjusted-goal table per Sub-SO, with the tension material trimmed
  to the operative sections (`compose.py:392`, `interactions_trim`). The pair
  files enter the pack whole.

### 1.3 The output reservation, not the output usage, is what pushes the ladder up a rung

- `pipeline/src/steps.py:40-41` (`NUM_PREDICT`) reserves **16,384** output tokens
  for every p4 call — **25 % of a 65,536 window** — as a *step-level* constant,
  applied to each of the 38 sub-domain calls identically.
- Measured (Case 03, job **1983144**, a complete 43-call run): 39 p4 calls,
  **107,753** total output tokens, mean **2,762**, max **4,059**
  (`p4_D-06_1`). The reservation is **5.9× the run mean** and **4.0× the run
  maximum**; over the run it reserves 638,976 output tokens against 107,753
  produced — a 5.9× overhead on a budget that is a ceiling, not a forecast.
- The honest counterweight, which is why this is not a free lunch: the
  programme-wide p4 maximum is **15,733** tokens (`p4_D-09_3`, job **1978919**,
  `done_reason=stop`) — 1.04× the reservation. So 16,384 is **not** an arbitrary
  number; it is set by the worst sub-domain and then charged to every
  sub-domain. The shape of the problem is a per-call worst case applied
  uniformly, not an oversized constant.

### 1.4 The budget estimate is a single scalar on top of a model-blind divisor

- `pipeline/src/steps.py:935-936`:
  `est_tokens = (len(system) + len(user)) // 4` then
  `needed = est_tokens * 1.15 + num_predict + 2000`. The comment at `:929`
  concedes that "chars/4 underestimates the real tokenizer" and applies a flat
  1.15 to compensate.
- Measured chars/token on the p4/p4t class of packs (>100 kB, all runs, read
  from `attempt1_prompt_tokens` against `system_chars + user_chars`):

  | Model | n | median | range |
  |---|---|---|---|
  | `gemma4:31b` | 53 | 3.87 | 3.55 – 3.98 |
  | `qwen3.8:27b` | 225 | 3.89 | 3.62 – 4.05 |
  | `muse-glimmer:30b` | 80 | 4.18 | 3.91 – 4.27 |

  The medians differ by 8.0 % and the observed range spans 20.2 % (3.55–4.27) on
  the same corpus. The guard's effective safety factor is 0.2875·c: **1.021** at
  c=3.55 (2 % spare) and **1.228** at c=4.27. One scalar does not cover a
  model-dependent tokenizer, and the code does not model that it is model-dependent.

### 1.5 The ladder cap is a policy literal

- `pipeline/src/steps.py:937` — `while needed > num_ctx and num_ctx < 131072:`.
  The value is a bare integer in the source. It is not read from
  `aegis-models/MODELS.yaml` (which records `native_ctx` 32768 for the reference
  `qwen3.8`, 16384 for several candidates, and `unknown` for five) nor from any
  model manifest, and no measurement in this programme records the window ceiling
  of any model. It is a policy choice, and §-2 rule 2 requires it to say so.

### 1.6 A ladder-exhausted step leaves no forensics

- `pipeline/src/steps.py:939-942` raises `LLMError` **before** the call. The
  `inputs/` files are written at `:944-948` and the trace record is opened at
  `:950` — both downstream of the raise. An exhausted ladder therefore produces
  no `inputs/`, no `trace.jsonl` line, and no manifest stage entry: only the
  exception string, which names an estimated token count and points at a
  mitigation ("trim the pack") that is not the evidence.

### 1.7 What is **not** a context problem — the correction

This is registered deliberately, because the current instrument points the other
way and the misreading is expensive.

- **The Case 03 aborts are L0 quality-gate failures, not context failures.** All
  five `qwen3.8` runs (jobs **1983224, 1983226, 1983228, 1983230, 1983232**)
  abort at `p4_D-03_3` with `attempt1_prompt_tokens` = **29,808** on a
  `num_ctx` = 65,536 window, `done_reason` = `stop`, and `l0_final_error` =
  *"adjusted goal is a near-verbatim copy of the Sub-SO objective (99 %
  similar)"*. `gemma4:31b` (job **1983343**) aborts at `p4_D-03_2` at **27,711**
  prompt tokens on an R6 untraceable-quantity verdict. `nemotron-3.5` (job
  **1983148**) aborts at `p4_D-01_3` at **19,659** prompt tokens on the
  retention floor (11 of 51 obligation terms) and then a column-count failure.
  All three are at ≤ 46 % of the window with a clean `done_reason=stop`.
- **The original 136 kB blocker was an output failure.** `p4_D-04_3` in
  `run_sec03_p1_1979371` returned `done_reason=length` at `eval_count` = 16,384
  — the cap — with `response_chars` = **76,612**, of which **71,378** sit after
  the `## §5` heading (which begins at offset 5,234). The TERMINATION clause
  (commit `ad76979`) fixed it: the same sub-domain re-ran to `done_reason=stop`,
  `eval_count` = **1,614**, `response_chars` = 6,524. The pack changed by **+310
  chars** (`user_chars` 135,656 → 135,966) — the clause itself; the 137 kB of
  context files are what shipped both times.
- **The ladder was added for a guard, not for a model that ran out of room.** The
  code's own comment (`steps.py:930-932`) records job **1980137**: a ~42 k-token
  D-07.1 pack that "cleared 64K with the safety margin by 1.4k tokens and died on
  the guard". Commit `1b6d04d` added the rungs in response. That run's artefacts
  are not in the workstation's runs directory, so this one claim rests on the
  code comment, not on a trace read in this pass.

### 1.8 The literature, and the one citation that carries the argument

- **[S-004]** frames the whole problem: *"Given that LLMs are constrained by a
  finite attention budget, good context engineering means finding the smallest
  possible set of high-signal tokens that maximize the likelihood of some desired
  outcome"*, and explains the gradient as n² pairwise relations against
  disproportionately shorter training sequences. (The registry entry for S-004
  does **not** carry the stronger claim that the source "explicitly rejects
  waiting for larger windows"; that phrasing is not recorded and is not asserted
  here.)
- **[S-115]** (context rot) holds task complexity constant while varying input
  length, and supplies the load-bearing methodological caveat: NIAH "assesses
  direct lexical matching, which may not be representative of flexible,
  semantically oriented tasks."
- **[S-116] / [S-117]** are already recorded as `CONTESTED` against each other
  in the registry (see the S-117 `notes`): both find the U-curve, one framing it
  as a defect to engineer around and the other as an adaptation to
  training-distribution retrieval demands. The disagreement is left visible, not
  smoothed.
- **[S-223] is the load-bearing citation.** Its no-tool baseline is fed the
  *complete* 100-node graph — exhaustive schema, zero retrieval error — and
  o4-mini collapses **59 → 5** between 100 and 500 nodes **while the graph still
  fits the context window**. That is the empirical form of "fitting is not being
  read", and it is what makes a window size a ceiling rather than an answer.
- **[S-242]** measures the same shape in a traceability corpus: a graph walk
  filling 11–15 context slots at **context precision 0.12–0.23** while the
  synthesizer cites only 3.4–5.0 ids at precision 0.48–0.65 — every local metric
  clean while most of the retrieved material is unused. It also shows the
  measurement *point* ranking architectures, not the architecture.
- **[S-282] / [S-283]** (added 2026-10-05, closing the registry's acknowledged
  gap) measure *effective* rather than advertised length: "only half of them can
  maintain satisfactory performance at the length of 32K" over 17 models, and "At
  32K, for instance, 11 models drop below 50% of their strong short-length
  baselines" over 13 models on needles with **minimal lexical overlap** — with
  reasoning models and CoT prompting in the comparison, so "spend more reasoning
  on it" is not the repair. A regulatory pack is the harder case, because its
  material is by construction not lexically matched to the row being written.
- **[S-040]** matters as a rejected lever, not an adopted one: llama.cpp
  documents `cache_prompt` as breaking bit-for-bit reproducibility because prefix
  reuse varies batch composition. EXP-02 measured **zero** residual variance
  from the serving layer (`AGENTS.md` §-1), so prompt caching buys nothing this
  pipeline is not already getting and takes a documented reproducibility risk.
- **[S-170] / [S-171]** remain `CONTESTED` and **C-01** in
  `docs/research/09_KG_PATTERN_MAPPING.md:335` records the reversal: GraphRAG's
  judge-scored global-sensemaking win does not survive reference-based metrics.
  That reversal is what makes D4's rejection of community summarisation an
  evidence-backed rejection rather than a preference.
- **C-05 / C-05a** (`docs/research/09_KG_PATTERN_MAPPING.md:366` and `:377`) hold
  the reconciled position: grounding is necessary, retrieval past it has
  diminishing returns, and the binding constraint becomes the model's ability to
  execute traversal over whatever it is shown. **KG-033** supplies the
  operational rule this ADR turns into D3: the two budgets are separate decisions
  and must not be traded against each other
  (`docs/research/04_EXPERIMENT_BACKLOG.md:746`).

## 2. Decisions

- **D1 — p4t is decomposed per sub-domain.** One LLM call per selected
  sub-domain, as p4 already is; `T-NNN` identifiers are renumbered at merge so
  the artifact is byte-stable for the reader. *Rationale:* the p4t pack is the
  largest prompt in the pipeline and its size is a function of the selection
  (§1.1), so decomposition is the only lever that changes the per-call cost
  rather than the aggregate. It also brings p4t onto the same forensic footing as
  p4 — per-sub-domain `inputs/`, per-sub-domain trace lines — instead of one
  190 kB call whose failure is not attributable to a sub-domain.
- **D2 — PROPOSED, NOT DECIDED: if the pairwise `cross/` fan-out is pruned, the
  selection rule is human-written over canonical ids, never a model-generated
  query.** This records E-16's "if it wins" clause as a constraint on the shape
  of any future change, and **not** the cut. Whether to prune is open:
  EXP-05b measured **86.4 %** pack-id utilisation (3,135/3,630) with **zero**
  fully-unused pack files, so the 13.6 % of uncited material is *distributed*
  across every pack — a budget-refinement question, not a deletion one. A
  model-written query is rejected on `KG-011`'s terms (a generated query has two
  independent failure modes — it can fail to parse, or parse and mean the wrong
  thing); the preferred form is a fixed template whose bindings are inferred,
  which "makes KG-011's validity problem structurally unreachable, because the
  model is never in a position to produce an invalid query"
  (`docs/research/06_GRAPH_QUERY_PATTERNS.md:270-276`). E-16 decides whether to
  prune; D2 decides who writes the rule if it does.
- **D3 — The input budget and the output budget are separate decisions and must
  not be traded against each other.** Per `KG-033`: "budget the extraction pass
  for recall, then budget the query pass for concision, and never spend the second
  budget to buy back what the first one lost." Concretely, raising `num_predict`
  to relieve an input-side problem (§1.3) is a mistake dressed as a fix, and
  trimming the pack to relieve an output-side problem would corrupt the evidence
  the output is made of. The two are diagnosed and reported independently.
- **D4 — No summarisation into the corpus.** The corpus stays verbatim-only
  (ADR-011 D1/D2/D3); the Fase 0 baseline remains the source of truth. This ADR
  **explicitly rejects GraphRAG-style community summarisation** as a context
  lever: [S-170]'s headline result is reversed by [S-171] once reference-based
  metrics replace LLM judging (C-01, `09_KG_PATTERN_MAPPING.md:335`), and the
  same review that produced the reversal also explains why summarisation would be
  structurally wrong here — on a curated corpus the cluster identity *is* the
  analytic output, which is exactly what community summarisation dissolves.
- **D5 — `num_predict` is right-sized per step from measurement, and a
  ladder-exhausted step must leave a trace record.** The 16,384 p4 reservation
  (§1.3) is a worst-case constant charged 38 times; after D1 it becomes
  per-sub-domain and the basis row for each value is a measured distribution, not
  a single incident. Independently: the `raise` at `steps.py:939-942` moves
  **after** the `inputs/` write and the trace record is opened, so an exhausted
  ladder produces the same forensics every other failure does. This adds no gate
  and relaxes none.
- **D6 — The context-overflow question is measured by E-15, not fixed by a new
  mechanism.** E-15 (`docs/research/04_EXPERIMENT_BACKLOG.md:704-750`) is
  already preregistered, costs **0 GPU-h** for its traversal-based pass, has no
  dependencies, and is the destination `docs/experiments/PLANO_FECHO.md:124`
  already routes `context-fail` cells to. This ADR does not invent a packing
  strategy, a retrieval layer, or a summariser; it routes the question to the
  experiment that was already written to answer it.

## 3. Alternatives considered

- **Raise the ladder cap / buy a bigger window** — rejected: the constraint is
  not the window. [S-223]'s collapse happened *while the material fit*; [S-282]
  and [S-283] measure half the models below 50 % of short-context baseline at
  32K on non-lexical needles; [S-115] degrades with length holding task
  constant. It also violates the measured headroom: the largest prompt ever sent
  is 50,054 tokens (§1.1), so a higher cap buys an unexercised rung.
- **Prune the `cross/` fan-out now** — rejected *as a decision*, not as an idea:
  it is E-16's to make, with three arms and a stated reason why arm C is not
  optional. EXP-05b's zero-fully-unused-files result is the constraint that keeps
  this from being a simple deletion. D2 records the rule; E-16 records the verdict.
- **Model-generated retrieval over the corpus for p4t** — rejected: `KG-011`'s
  validity/grounding split, and the fixed-template alternative
  (`06_GRAPH_QUERY_PATTERNS.md:270-276`) reaches the same surface without making
  the model able to emit an invalid query.
- **Summarise or cluster the corpus to shrink the pack** — rejected: D4, on
  [S-171]'s reversal of [S-170] and on the verbatim-only integrity of the
  baseline (R9's composed-slice discipline is what makes the corpus auditable).
- **Materialise the KG to get a smaller context surface** — not rejected, but not
  adopted here either: ADR-011 D2 already defers it and `ASSUMPTIONS.md` A6
  already carries E-13 as its signpost. This ADR does not pre-empt that signal.
- **Adopt prompt caching (`cache_prompt`) as a context lever** — rejected: [S-040]
  documents it as a reproducibility break, and EXP-02 measured zero serving-layer
  residual (`AGENTS.md` §-1), so the upside is already banked and the downside is
  documented.
- **Do nothing and let E-15 decide** — rejected as insufficient: E-15 measures
  whether the budget *truncates a citation chain*; it does not decompose a
  monolithic call, and it cannot be run on a pipeline whose p4t step has no
  per-sub-domain forensics. D1 and D5 are prerequisites for E-15 being
  interpretable, not substitutes for it.

## 4. Consequences

- **C1:** p4t's largest single-call prompt falls from 44,826 real tokens (job
  1983314) to ~3,780 (measured, Case 03, 38 selected sub-domains) — 11.9×. The
  residual is dominated by ~6.9 kB of fixed per-call scaffolding (system,
  instruction, output schema, self-checks, fact sheet, build manifest), not by
  the tension corpus, so the floor does not fall with the selection. Each call
  carries its own `inputs/` and trace line; the difference is that a failure
  becomes attributable.
- **C2:** the p4t pack stops being a function of the *selection size* alone. The
  0.4 % spread across 2/4/5 confirmed regulations (§1.1) is what makes the
  quadratic `cross/` fan-out (§1.2) affordable rather than alarming; D2's
  decision becomes per-sub-domain and therefore answerable by E-16.
- **C3:** `docs/experiments/METRICS.md` gains six declared basis rows covering
  the four thresholds that were being applied by a gate without one — the
  `num_predict` values (M-09 cites one incident for `p4` and none at all for
  `p1`/`p2`/`p3`/`p3f`/`p4t`; M-09b now carries the measured per-call
  distribution), the `num_ctx` ladder (M-08 is `incident-calibrated` with no job
  named), the `// 4` divisor and its 1.15 factor (M-10b/M-10c), and the 131072
  cap (M-10e) — plus M-10d (the +2000 constant) and M-10f (the absence of
  forensics on ladder exhaustion), which were unstated entirely. Every one of the
  new rows is `convention` and names E-15 as the experiment that would convert
  it. That was a standing §-2 rule 2 violation, not a documentation nicety: a
  threshold with no declared basis may not be cited as evidence of quality.
- **C4:** `docs/decisions/ASSUMPTIONS.md` gains a row for this ADR's own
  load-bearing assumption, and gains corrections to four rows whose signposts had
  fired or whose contingency had gone void without the register being updated.
- **C5:** nothing about the corpus, the gates, the fichas or the methodology
  changes. No gate is lowered, relaxed or re-baselined; D5 adds forensics, not a
  threshold.
- **C6:** E-15 gains a precondition it did not have — with D1 and D5 landed, a
  `context-fail` cell recorded under `PLANO_FECHO.md:124` carries a trace line
  and per-sub-domain packs, so the traversal E-15 performs has real inputs.
- **C7 — the cost of fan-out, recorded.** Three measured consequences of D1 that
  the decision buys rather than avoids. **(a)** Aggregate p4t input *rises* from
  188,812 to 446,741 characters (+137 %): 38 calls re-send the shared scaffolding
  that one call sent once. This is the token-ratio cost [S-002] measures on
  sub-agent fan-out, and it is the price of C1's per-call attribution.
  **(b)** *Cross-sub-domain synthesis is lost.* The monolithic call read all 38
  Emergent-tensions sections together; a per-sub-domain call reads one. A tension
  that only becomes visible by reading two sub-domains' sections against each
  other can no longer be resolved, and no compensating pass was added. It did not
  occur in the measured run — all 6 tensions in `run_m04_muse_c3_r02_1983314` name
  a single sub-domain — but it is a real narrowing of what §4 can contain, and it
  is untested against a case where it does. **(c)** *Duplicates are not
  deduplicated.* A tension co-located in N sub-domains' sections now yields N
  rows where the monolith might have yielded 1. No dedup rule was added: dropping
  a row is a silent content loss, and a dedup rule is a gate, which D5's scope
  excludes. **(b)** and **(c)** are open content decisions for the researcher, not
  code defects, and neither is measured.

> **Previsto (falsificável):** decompor o p4t por sub-domínio **não** altera o
> veredicto de qualidade (retention, cobertura, L1) e torna cada falha
> atribuível a um sub-domínio; a conta de contexto que se resolve não é a causa
> dos abortos actuais do Case 03.
> **Sinal:** E-15 correr e a retenção da cadeia ser **materialmente igual** nos
> orçamentos current / 0.75× / 0.5× (a cabeça livre existe ⇒ o orçamento nunca
> foi a restrição) **ou** qualquer célula `context-fail` registada
> (`PLANO_FECHO.md:124`) persistir depois de D1.
> **Revisar:** com o relatório do E-15 em mão — e, antes disso, com a próxima
> matriz que produza um pack acima de 50 k tokens reais (ver
> `docs/decisions/ASSUMPTIONS.md` A8).

## 5. Ratification checklist (P7)

1. D1 (p4t decomposed per sub-domain, T-NNN renumbered at merge) — **decided by
   researcher** (2026-10-05).
2. D3 (input and output budgets are separate decisions) — **decided by
   researcher** (2026-10-05).
3. D4 (no summarisation into the corpus; GraphRAG community summaries rejected) —
   **decided by researcher** (2026-10-05). Restates ADR-011 D1/D2/D3; no
   reversal.
4. D5 (`num_predict` right-sized from measurement; ladder exhaustion leaves a
   trace record) — **decided by researcher** (2026-10-05). D5's second half adds
   forensics and no gate.
5. D6 (the overflow question is E-15's, not a new mechanism's) — **decided by
   researcher** (2026-10-05).
6. **D2 (human-written selection rule over canonical ids, if the fan-out is ever
   pruned) — PROPOSED, not decided.** The *shape* is settled; the *cut* waits on
   E-16. Confirm: ______
