---
document_id: AEGIS-RES-01
title: 'AI pipeline patterns — an annotated catalogue'
version: 0.1.0
created: 2026-10-03
status: ACTIVE
survey_date: 2026-10-03
sources: 'docs/research/sources.yaml'
---

# AI pipeline patterns — annotated catalogue

**What this document is.** A catalogue of named patterns for building multi-step
LLM pipelines, each with its definition, the sources that establish it, when it
applies, its named failure mode, its countermeasure, and a grade for how strong
the evidence behind it is. It is a *reference*, not a recommendation — the
recommendation lives in [03_PATTERN_MAPPING.md](03_PATTERN_MAPPING.md), which
maps this catalogue onto what the AEGIS pipeline already does.

**Method.** Web survey, 2026-10-03, two independent passes with different scopes
(pipeline architecture; agent orchestration). ~123 sources registered in
[sources.yaml](sources.yaml). Preference for vendor primary documentation,
specifications, and preprints over practitioner opinion; where a claim is
contested the disagreement is recorded rather than smoothed. Every factual claim
below carries an `[S-nnn]` token resolving into the registry. Verify with
`python scripts/check_research_refs.py --strict`.

**Evidence grades used throughout.**

| Grade | Meaning |
|---|---|
| `PRIMARY` | vendor or standards-body documentation, or a technical report, read directly |
| `PEER` | preprint or paper; peer status not established — strong but provisional |
| `PRACTITIONER` | named expert writing from experience. Opinion, with detail |
| `CONTESTED` | credible sources disagree; both sides are recorded |

**A caveat that shapes the whole catalogue.** No controlled study was found
isolating schema-following ability against model size for local open-weight
models, and no independent study of determinism controls on llama.cpp or Ollama
was found at all — the only primary material on the latter is llama.cpp's own
admission about `cache_prompt` and vLLM's batch-invariance feature, both vendor
documentation. Where this catalogue gives operational guidance in that gap, it
is guidance derived from vendor statements, not from measurement.

---

## 1. Architecture and decomposition

### PP-001 — Prompt chaining with programmatic gates

**Definition.** Decompose a task into a fixed sequence in which each LLM call
processes the previous call's output, with programmatic checks on intermediate
steps. The gate is code, not a model.

**Sources.** [S-001] names it the first of five workflow patterns; [S-180] is
the academic antecedent and is the origin of the observation that *realistic*
applications need data transformation between chain steps.

**When it applies.** When the task decomposes cleanly into fixed subtasks.
[S-001] is explicit that this "trade[s] off latency for higher accuracy, by
making each LLM call an easier task" — the latency is the price, paid
deliberately.

**Named failure mode.** Error compounding down the chain, and fixed
decomposition that cannot adapt when a step surprises you. [S-139] names the
mechanism for the first in multi-agent settings: "erroneous information from the
former agent will be propagated to the latter through prompts."

**Countermeasure.** Put a deterministic gate between steps, and make the gate's
rejection message self-describing enough to serve as the repair prompt.

**Evidence.** `PRIMARY` for the pattern, `PEER` for the antecedent.

### PP-002 — Routing

**Definition.** Classify the input, then dispatch to a specialised follow-up
task — a different prompt, a different model, or a different path.

**Sources.** [S-001] (with the caveat that it "allows for separation of
concerns, and building more specialized prompts"); [S-060] documents it as a
first-class 2026 pattern with its own cost profile.

**The stated precondition is the whole pattern.** [S-001] qualifies routing as
suited to cases "where classification can be handled accurately, either by an
LLM or a more traditional classification model." Routing is only as good as its
classifier.

**Design consequence.** If the routing signal is extractable *deterministically*
— a regulation identifier, a jurisdiction, a sub-domain key, a case field — then
deterministic routing beats LLM routing on all three axes: cost, auditability,
and reproducibility. This is stated as a design recommendation, not a finding;
no source measures it head-to-head, but [S-001] explicitly allows a
"more traditional classification model/algorithm" in place of the LLM.

**Evidence.** `PRIMARY`.

### PP-003 — Parallelization: sectioning

**Definition.** Break a task into independent subtasks and run them in parallel.

**Sources.** [S-001], with the reasoning that matters and is routinely
mis-cited: "For complex tasks with multiple considerations, LLMs generally
perform better when each consideration is handled by a separate LLM call,
allowing focused attention on each specific aspect."

**Named failure mode.** Requires genuine independence. If subtasks share state
or one can invalidate another, parallelising produces an ordering problem that
the pattern does not solve.

**Evidence.** `PRIMARY`.

### PP-004 — Parallelization: voting and self-consistency

**Definition.** Run the same task N times to get diverse outputs, then select
the most consistent answer by marginalising over the reasoning paths.

**Sources.** [S-101] is the origin; [S-001] lists voting as the second
parallelisation variant.

**When it applies.** Where several attempts are worth more than one good
attempt. Cost is N× by construction.

**Caution on the numbers.** The widely-quoted GSM8K figures for
self-consistency were not verified from the paper abstract and are not repeated
here. The *mechanism* — sample diverse paths, marginalise — is the part that
transfers.

**Evidence.** `PEER`.

### PP-005 — LLM-as-a-judge

**Definition.** A model call scores another model's output against a rubric.

**Sources.** [S-111] establishes the named biases — position, verbosity,
self-enhancement, and limited reasoning ability. [S-112] quantifies the worst of
them: a reordering of candidates in the context made a 13B model "beat" a
frontier model on 66 of 80 tested queries. [S-177] adds self-preference.
[S-113] reports that LLM evaluators have lower human correspondence than
medium-size neural evaluators. [S-076] is the vendor doctrine, including the
specific vs measurable distinction.

**The result that should govern any judge design.** [S-114] shows that
classifiers trained on rubric text *alone*, never seeing the evaluated response,
achieve nontrivial predictive performance on judge outputs. The consequences are
direct: a judge may be scoring the rubric rather than the answer; changing the
rubric's wording is a confound rather than a neutral refactor; and a
**rubric-text-only baseline is now a mandatory control** in any judge experiment.

**The counter-intuitive production result.** [S-002] reports that a single
well-shaped judge call — one prompt, scores from 0.0–1.0 plus a pass-fail grade
— was *more* consistent and better aligned with human judgement than
multi-judge ensembles. The mechanism they identify: when the test case has a
clear correct answer, the judge degenerates into a deterministic answer-check,
which is the right design.

**When it applies.** Only for the open-ended residue after deterministic
validation. Prefer a cheap deterministic validator; use one judge call; reserve
ensembles for genuinely open-ended output. Pairwise comparison of a contested
pair is the case where [S-112] says the instrument is actively broken.

**Evidence.** `PEER`, with `PRIMARY` vendor corroboration.

### PP-006 — Orchestrator-workers

**Definition.** A central LLM breaks the task down dynamically, delegates to
workers, and synthesises their results. The distinguishing property is that
subtasks are *not* pre-defined but determined by the orchestrator per input.

**Sources.** [S-001]; [S-011] (manager pattern, `Agent.as_tool`); [S-063]
(hierarchical process with a required `manager_llm`); [S-162] (an Orchestrator
that plans, tracks progress, and re-plans to recover from errors).

**When it applies.** When you *cannot predict* the subtasks needed.
Topographically similar to PP-003; the difference is flexibility.

**Named failure modes.** Over- and under-delegation; instructions too thin for
the worker to act on; the orchestrator's own context saturating; everything
funnelling through one bottleneck model.

**Evidence.** `PRIMARY`.

### PP-007 — Evaluator-optimizer

**Definition.** One call generates, another evaluates and feeds back in a loop.

**Sources.** [S-001], which also states the two fit tests: responses must be
demonstrably improvable when a human articulates feedback, *and* the LLM must
be able to supply that feedback. Unbounded loops need explicit stopping
conditions.

**The 2026 caveat.** [S-134] measures the ceiling on LLM judges of agent
outcomes at AUROC ≤ 0.65. Combined with [S-114], the honest position is that
LLM judges are acceptable for *progress detection* and not for *admission
control*.

**Evidence.** `PRIMARY`, with a `PEER` boundary condition.

---

## 2. Output structure

### PP-008 — Structured output and constrained generation

Three tiers exist, and only the top one is a guarantee.

| Tier | Mechanism | Guarantee | Where |
|---|---|---|---|
| 1 | Post-hoc parsing — generate, then parse/validate | none; needs a retry loop | everywhere; the anti-pattern |
| 2 | Prompt-level JSON mode | valid JSON, *not* schema adherence | [S-014] |
| 3 | Constrained decoding — mask logits against a grammar or schema each step | 100% structural correctness | [S-045], [S-046], [S-047], [S-048], [S-040] |

**The anti-pattern, stated by a vendor.** [S-046]: "Most solutions attempt to
fix bad outputs after generation using parsing, regex, or fragile code that
breaks easily."

**The guarantee has two escape hatches.** [S-014] documents both, and they are
the reason tier 3 is not the whole answer: a model may refuse, and a response
may be incomplete because it hit a max-tokens limit. Both must be handled in
code. A pipeline that treats schema adherence as implying completeness will
silently ship truncated artifacts.

**Reality check on the small-model case.** No controlled study was found
isolating schema-following from model size. What *is* established is that
constrained decoding is model-agnostic by construction — [S-045] enumerates
Qwen, Llama, DeepSeek, Phi and Gemma — because it removes the failure mode
rather than hoping the model avoids it. The cost of constrained decoding on a
weak model is latency and constraint-induced degeneration, not format failure.
**The real small-model risk is content, not syntax:** a 7B model will emit
perfectly valid JSON containing an invented regulation article.

**Format-vs-reasoning, contested.** [S-179] finds strict format constraints can
cost reasoning quality. The resolution that survives is to keep a reasoning
field in the schema, so constrained decoding governs the *record* and not the
*thinking*.

**The portability trap.** [S-044] documents that the regex dialect differs by
backend — "xgrammar, guidance, and outlines use Rust-style regex, while
lm-format-enforcer uses Python's `re` module" — and that seven `guided_*`
parameters were all removed in v0.12.0.

**Evidence.** `PRIMARY` for the tiers; `CONTESTED` for format-vs-reasoning.

---

## 3. Resource management

### PP-009 — Token and context budgeting

Token budget is a *correctness* constraint, not a cost optimisation.

**Sources.** [S-005] makes this concrete: an intermediate result that "must
pass through the model" for a 2-hour transcript means ~50,000 extra tokens, and
larger inputs mean "**breaking the workflow**". [S-102] is the serving-side
background (per-request KV memory, fragmentation, paging). [S-003] reports
prompt caching reducing latency >2× and cost up to 90% on their retrieval stack.
[S-105] records the negative result that speculation does not help MoE models.
[S-009] documents context compaction as a first-class runtime feature rather than
an application concern.

**Local-inference specifics.** [S-040] documents the serving knobs:
`--ctx-size`, `-n/--n-predict` (default `-1`, infinite), `--batch-size`,
`--ubatch-size`, `--keep`, and `t_max_predict_ms` as a wall-clock cap on
generation. The `n_predict` contract has a useful edge: "When 0, no tokens will
be generated but the prompt is evaluated into the cache" — a clean
cache-priming primitive.

**Context-window growth is not free.** [S-004] gives the attention-budget
framing, and [S-115] measures that "model performance degrades as input length
increases, often in surprising and non-uniform ways" — under a design that holds
task complexity constant and varies only length, which is the rare correct
version of that experiment.

**Evidence.** `PRIMARY`, with a vendor research interest in [S-115] disclosed.

### PP-010 — Prompt caching and prefix reuse

**This is the sharpest tension in the catalogue, and it is the vendor's own
words.** [S-040], on `cache_prompt`:

> "Because (depending on the backend) the logits are not guaranteed to be
> bit-for-bit identical for different batch sizes (prompt processing vs. token
> generation) enabling this option can cause nondeterministic results."

**Why that is true, mechanistically.** Prompt evaluation is a GEMM over a batch
of N tokens; token generation is a GEMM over a batch of 1. Different shapes
select different kernels and different reduction orders, which changes
floating-point rounding and therefore the logits, which at any non-zero
temperature changes the sampled token. Prefix caching is precisely what makes
batch composition vary between otherwise-identical requests. This is not a bug;
it is a direct consequence of reuse.

**The consequence for pipeline design.** A multi-step pipeline with a stable
system prompt gets different numerics on step 1 depending on slot occupancy.
Steps are therefore not independent, and per-step caching is not only a cost
optimisation — it is a determinism control.

[Ollama's documentation](sources.yaml) exposes no equivalent of
`cache_prompt`; `keep_alive` controls residency, not prefix reuse.

**Evidence.** `PRIMARY`.

### PP-011 — The determinism ladder

Six levels, ordered by what they actually buy. The distinction that matters most
is at the end: **levels 1–3 buy reproducibility of the *text*; levels 4–6 buy
reproducibility of the *artifact*.** A document-generation pipeline needs 4–6.

| # | Guarantee | Mechanism | Source | Cost |
|---|---|---|---|---|
| 0 | None | defaults: `--temp 0.80`, `--seed -1`, concurrency on | [S-040], [S-041] | free |
| 1 | Seeded, single request | fixed seed, `--temp 0`, `--parallel 1`, `--no-cache-prompt` | [S-040], [S-041], [S-050] | ~1× throughput |
| 2 | Batch-invariant | `VLLM_BATCH_INVARIANT=1` | [S-043] | throughput + hardware constraints; **beta** |
| 3 | Distribution-preserving decode | speculative decoding | [S-103] | draft-model cost |
| 4 | Structural | constrained decoding / JSON schema | [S-045] | near-zero overhead claimed |
| 5 | Assembly | deterministic code: the model judges, code assembles | [S-005], [S-137] | engineering cost |
| 6 | Artefact-level | verify outcome against environment state, fail-closed | [S-142] | engineering cost |

**The seeding caveat, stated by vendors.** [S-040] documents the llama.cpp
default seed as `-1`, meaning random — *a server given no seed is nondeterministic
by configuration*, and there is no safe default. [S-041] documents Ollama's
default as `0` and states "For reproducible outputs, set `seed` to a number".
[S-050] (Hugging Face) is deliberately loose: temperature values "lead to more
focused, deterministic outputs" — determinism-*seeking*, not
determinism-*guaranteeing*.

**The cascade-versus-spec-decode distinction that must not be blurred.** [S-104]:
"cascades employ a deferral rule that invokes the larger model only for 'hard'
inputs, while speculative decoding uses speculative execution to primarily
invoke the larger model in parallel verification mode." The two offer different
guarantees — "empirically, cascades offer better cost-quality trade-offs, often
even outperforming the large model, while theoretically, speculative decoding
offers a **guarantee of quality-neutrality**." If a regression guarantee is
needed, spec-decode; if a cost win is needed, cascade.

**The only first-class determinism control found anywhere in this survey, and
where it does not exist.** [S-043]: "Batch invariance ensures that the output of
a model is deterministic and independent of the batch size or the order of
requests in a batch." It ships with vLLM. There is no llama.cpp or Ollama
equivalent — the local stack's only route to bit-reproducibility is level 1, and
that route collides with [S-040]'s own admission that `cache_prompt` breaks it.
Note also that [S-043]'s example still passes both `temperature=0.7` and
`seed=42`: batch invariance and seeding are orthogonal controls.

**The vendor-endorsed framing of the whole problem.** [S-002]: "We combine the
adaptability of AI agents built on Claude with deterministic safeguards like
retry logic and regular checkpoints." The model navigates; code guarantees.

**Evidence.** `PRIMARY` for the mechanism, `PRIMARY` (vendor admission) for the
gap, `PEER` for the cascade analysis.

### PP-012 — Sampling semantics and silent truncation

**Truncation has four distinct mechanisms, all real, and all documented.**

1. **Provider-side.** [S-014]: `incomplete_details.reason === "max_output_tokens"`.
2. **Local decode cap.** [S-040]: `-n/--n-predict`, with the caveat that it "may
   exceed the set limit slightly if the last token is a partial multibyte
   character".
3. **Local context overflow.** [S-040] documents a `truncated` boolean in the
   response — "indicating if the context size was exceeded during generation" —
   and that `--context-shift` is **disabled by default**, so the default
   behaviour is not a graceful shift. This boolean is the primary-source
   detector, and it is the one most pipelines do not read.
4. **Upstream exhaustion.** [S-005]: oversized documents "may exceed context
   window limits, **breaking the workflow**."

**Countermeasure.** Make truncation a *first-class asserted state*, not a parse
failure. Assert `truncated == false`; assert the response is not `incomplete`;
never let a truncated artifact be assembled into the deliverable. Set
`num_predict` deliberately per step rather than leaving the `-1` default.

**Evidence.** `PRIMARY`, from three independent vendor sources.

---

## 4. Context and retrieval

### PP-013 — Context engineering

**The core constraint.** [S-004]: "Given that LLMs are constrained by a finite
attention budget, good context engineering means finding the smallest possible
set of high-signal tokens that maximize the likelihood of some desired outcome."
The mechanistic explanation offered is that full attention yields n² pairwise
relations while models train disproportionately on shorter sequences, so they
have "less experience with, and fewer specialized parameters for, context-wide
dependencies." The result is "a performance gradient rather than a hard cliff."

**Position effects, contested.** [S-116] finds "performance is often highest
when relevant information is at the beginning or end of the context." [S-117]
argues the same U-curve is an adaptation to training-distribution retrieval
demands rather than a defect — a long-memory versus short-memory split. **Both
readings fit the data.** The practical advice is identical; the framing decides
whether you treat it as a benchmark artifact or a law, so it is recorded as
`CONTESTED` rather than resolved.

**The benchmark caveat worth carrying.** [S-115]'s critique of
needle-in-a-haystack is the load-bearing part: NIAH "assesses direct lexical
matching, which may not be representative of flexible, semantically oriented
tasks." A pipeline that validates its long-context behaviour with NIAH has not
validated it.

**The just-in-time shift.** [S-004] documents the move from pre-inference
embedding retrieval toward lightweight identifiers loaded at runtime, with
progressive disclosure ("file sizes suggest complexity; naming conventions hint
at purpose; timestamps can be a proxy for relevance") and a recommended hybrid.
Cost, stated honestly: "runtime exploration is slower than retrieving
pre-computed data… an agent can waste context by misusing tools, chasing
dead-ends."

**Prompt altitude.** [S-004] names a "Goldilocks zone" between brittle hardcoded
if-else logic in the prompt and vague guidance that "falsely assumes shared
context." It also rejects enumerating edge cases in favour of "a set of diverse,
canonical examples."

**Growing-context evaluation is an open area.** [S-118] argues existing
long-context benchmarks "primarily focus on single-step settings" while agents
need evaluation "under a dynamically growing context."

**Evidence.** `PRIMARY`, with the position-effect claim `CONTESTED`.

### PP-014 — Retrieval: hybrid, rerank, and the no-RAG option

**The decision that may not need making at all.** [S-003]: "If your knowledge
base is smaller than 200,000 tokens… you can just include the entire knowledge
base in the prompt that you give the model, with no need for RAG or similar
methods." Combined with prompt caching, the honest 2026 position is that for a
curated corpus under a few hundred thousand tokens, *no RAG* plus caching is a
legitimate and often superior architecture. RAG earns its complexity past that.

**When retrieval is in play, hybrid is not optional in a compliance corpus.**
[S-003] gives the complementary-failure argument: embeddings "can miss crucial
exact matches," BM25 "is particularly effective for queries that include unique
identifiers or technical terms." A regulatory corpus is queried by exact article
number, control ID, and standard clause. Pure dense retrieval is a bug there.
[S-172] confirms it in the legal domain specifically: snippet-level retrieval
precision is the bottleneck.

**Late interaction.** [S-121] is the primitive (per-token document embeddings
scored with MaxSim). [S-122] explains its edge — MaxSim "can exactly replicate
the inner product between any two non-negative k-sparse vectors," making it
strictly more expressive than a single-vector dot product. [S-123] is the
caveat: the winner-take-all pooling rule induces higher gradient concentration
than smoother alternatives, which is a documented attack surface and a reason not
to treat MaxSim robustness as free.

**The instrument is uncalibrated.** Two 2026 preprints ([S-119], [S-120]) both
treat chunk granularity as critical and under-explored, and [S-119] reports that
"RAGAs based faithfulness shows limited reliability in this setup." There is no
settled answer to optimal chunk size, and the measuring instrument is itself
unreliable on structured text. Any chunking default inherited from a vendor is
weaker than it looks.

**The graph option, and the evidence for it.** [S-170] finds vector RAG fails at
corpus-level sensemaking. [S-171] is the systematic evaluation: neither paradigm
dominates — RAG better at factual/detail QA, GraphRAG at relationship-dependent
reasoning, and "hybrids win consistently". [S-173] adds that in a high-stakes
domain, grounding in a *curated* graph consistently improves answers, which
supports the reading that curation quality, not graph-ness, drives the gain.

**Evidence.** `PRIMARY` for the vendor claims, `PEER` for the comparisons.

### PP-015 — Corpus composition and flag-not-drop retrieval

Not a named pattern in the literature — a synthesis of [S-003] (retrieval
*removes* context, which is the defect to design against), [S-119] (retrieval
quality is unmeasured), and [S-180] (data transformation between chain steps is
where the real work lives).

The derived principle: **compose the context deterministically and record what
was left out**, rather than retrieving it. A curated, verbatim, deterministic
file list with a visible trimming banner is auditable in a way that a
similarity-scored top-k is not — and the trimming banner makes the omission
itself a reviewable artefact instead of an invisible property of the prompt.

**Evidence.** `PRIMARY` components; the synthesis is this catalogue's own.

---

## 5. Evaluation

### PP-016 — Evals: assertions, ladders, and self-checks

**The single highest-leverage design idea in this catalogue** is [S-077]:
"Unlike typical unit tests, you want to organize these assertions for use in
places beyond unit tests, such as data cleaning and automatic retries (using
the assertion error to course-correct) during model inference." One assertion
library, three consumers: the test runner, the retry handler, the data cleaner.
In pipeline terms, the L0 rejection text *is* the repair prompt.

**The three-level ladder.** [S-077] orders unit tests, model-and-human
evaluation, and A/B testing by cost, and prescribes the cadence that follows:
level 1 on every code change, level 2 on a set cadence, level 3 only after
significant changes. He also advises conquering most of level 1 before moving to
model-based tests.

**Failure-mode analysis that reads like a diagnosis of a pipeline without
evals.** [S-077] on a plateau project: "Addressing one failure mode led to the
emergence of others, resembling a game of whack-a-mole"; and "Prompts expanded
into long and unwieldy forms, attempting to cover numerous edge cases and
examples." The third item is practitioner-side evidence for the one-giant-prompt
anti-pattern in PP-021.

**Success criteria must be specific and measurable.** [S-076] is the vendor
doctrine, and its bad-vs-good table is the citable artefact: "The model should
classify sentiments well" versus a metric, a threshold, a corpus size, and a
baseline delta. The four properties are specific, measurable, achievable,
relevant. The doc also preconditions its own guidance on having a clear success
definition first — which is itself a defence against building evals that measure
nothing.

**Convert a recurrence into a regression test.** [S-073]: "Add real traces to a
dataset so a failure you saw once becomes a test you run every time." The
companion statement is about what the eval harness then gives you for free:
baselines, regression tests, latency, token usage, cost per task, error rates.

**Judge calibration is a prerequisite, not a detail.** [S-111], [S-112], [S-113],
[S-114], and [S-177] collectively mean that an uncalibrated judge is an
instrument of unknown validity. [S-114] adds the mandatory control: a judge that
does not beat a classifier trained on rubric text alone is not reading the
response.

**Tooling is a matter of fit, not authority.** [S-073] (trace-centric,
offline/online), [S-074] (metric inventory — RAG metrics, agent/tool metrics,
and notably non-LLM string metrics and exact match *alongside* judge metrics),
[S-075] (the one eval CLI whose provider matrix includes Ollama), [S-096]
(executable security regression testing for agentic systems), [S-097] (a
vulnerable-by-design app usable as a test corpus). [S-175] is the domain data
point: LLM-elicited security requirements reached 98.5% necessity and 44.4%
testability across five expert raters — useful early, with mandatory human
review, and testability as the weak flank. [S-174] is the shape of an
eval-driven optimisation loop; [S-181] and [S-176] are recorded for the later
threat and NFR lanes rather than for Phase 1.

**Evidence.** `PRIMARY` for the doctrine, `PRACTITIONER` for the ladder,
`PEER` for the biases.

### PP-017 — Tracing and observability

**The standard worth adopting** is [S-070], [S-071], [S-072] — OpenTelemetry
GenAI semantic conventions, which have moved to their own repository. Spans
defined: `create_agent`, `invoke_agent` (client and internal), `invoke_workflow`,
`plan`, `execute_tool`, plus agent-skills sub-spans. Both agent and MCP documents
are **status: Development** — cite as maturing, not settled.

Three rules from these documents that change design:

1. **Retries belong inside one span.** [S-070]: "If a transient issue happened
   and the request was retried automatically, the corresponding span SHOULD
   cover the duration of the logical operation with all retries." This is the
   canonical encoding of a step-level retry, and it pairs directly with
   checkpoint/resume (PP-018).
2. **`invoke_workflow` exists as a first-class traced operation** [S-071] — the
   standard's own name for what a pipeline stage is.
3. **Same-process models are `INTERNAL` spans** [S-070] — the convention's own
   acknowledgement that these conventions are not cloud-only.

**What "inspectable" obliges.** [S-094] states the requirement as: "We can trace
back any action taken to the reasoning behind it and the originating task. Even
if the thread goes through multiple agents and software systems." That is a
higher bar than recording inputs and outputs, and it is the bar a PhD evidence
chain has to meet.

**Evidence.** `PRIMARY`.

---

## 6. Reliability

### PP-018 — Retry, checkpoint, resume, and version pinning

**The primary source is unusually explicit about what broke.** [S-002]: "Agents
are stateful and errors compound… When errors occur, we can't just restart from
the beginning: restarts are expensive and frustrating for users. Instead, we
built systems that can resume from where the agent was." And: "We combine the
adaptivity of AI agents built on Claude with deterministic safeguards like retry
logic and regular checkpoints."

**The derived requirement for a resumable pipeline.** A durable artefact written
by deterministic code at each step boundary, and a resume path that re-enters *at
the artefact* rather than re-prompting the model. The model is the least reliable
component and should never be the thing holding state. [S-136] supplies the
argument: single-step or single-agent attribution is often ill-posed, because
multiple distinct interventions can independently repair a failed task, so
log-only localisation produces untested hypotheses. A resume that re-enters at a
known-good artefact does not need to localise anything.

**Graded degradation beats hard failure.** [S-002] reports that "letting the
agent know when a tool is failing and letting it adapt works surprisingly well."

**Pin versions, and never update mid-run.** [S-002] describes rainbow
deployments for exactly this: agent systems "are highly stateful webs of
prompts, tools, and execution logic that run almost constantly," and a version
bump would otherwise leave every in-flight job somewhere different. Record the
model, quantisation, context size, sampler chain, seed, and prompt versions per
run.

**Fail closed on ambiguity.** [S-142]: "agents may **propose** completion, but a
read-only verifier decides whether the claim is **admitted**. Ambiguous or
weakly evidenced cases resolve fail-closed." A bounded case study, self-described
as such — a design pattern, not a validated result.

**Evidence.** `PRIMARY`, with `PEER` for the fail-closed pattern.

### PP-019 — Cost/quality routing and abstention

**The origin.** [S-106] (FrugalGPT) gives three strategy families — prompt
adaptation, LLM approximation, and cascade — and the counterintuitive headline
that a learned cascade can *improve accuracy*, because the small model intercepts
cases the large one handles badly. The specific numbers were not verified from
the abstract and are not repeated.

**A verified headline from a later result.** [S-107] (RouteLLM) reports cost
reduction "by over 2 times in certain cases — without compromising the quality
of responses." Note the routing signal is *preference data*, not a difficulty
classifier — a different design from FrugalGPT's learned combinator.

**The mechanism that makes routing a correctness feature.** [S-108] (confidence
tokens): "it becomes vital to know when the output of an LLM may be unreliable.
Depending on whether an answer is trustworthy, a system can then **route the
question to another expert, or otherwise fall back on a safe default behavior.**"
That fallback arm is the abstention path, and it is strictly more expressive than
a two-way route.

**The three-way route, made explicit.** [S-109]: small model answers / escalate
to the large model / abstain to a human. "Since even the most expensive models
are susceptible to making mistakes, applications in these domains benefit from
**allowing LLM systems to completely abstain from answering**." For a regulated
domain this is the arm that matters, and it is the arm most designs omit.

**The cost of the cost optimisation.** [S-110] is the counterweight: cascade
design "introduces new vulnerabilities through an expanded attack surface"
because the lightweight models are part of it. For a regulated domain that is a
design input, not a footnote.

**The operating form.** [S-001] names it plainly: "Routing easy/common questions
to smaller, cost-efficient models… and hard/unusual questions to more capable
models." The precondition stands — accurate classification, LLM or otherwise.

**Evidence.** `PEER` for the research, `PRIMARY` for the production form.

### PP-020 — Shifting work out of the LLM

**The pattern, and the number.** [S-005] reports reducing 150,000 tokens to
2,000 — "a time and cost saving of 98.7%" — by exposing MCP servers as a
filesystem of code modules the agent writes against, instead of as direct tool
calls.

**The rule underneath it, and the reason it is not only about cost.**
[S-005]: "Then, when the data is shared in another MCP tool call, it is
**untokenized via a lookup in the MCP client**. The real email addresses, phone
numbers, and names flow from Google Sheets to Salesforce, but **never through the
model**." And the same post's correctness argument: "With large documents or
complex data structures, **models may be more likely to make mistakes when
copying data between tool calls**."

[S-137] reaches the same conclusion independently and from the other direction:
workflow performance "is not robust as code generation **depends on the
performance of each agent**," and the fix is pruning intermediate outputs to
reduce propagation.

**The generalisation.** *Wherever a value must pass from step A to step B and
both steps are under your control, pass a reference through the model and the
value through deterministic code.* This converts an LLM determinism problem into
an ordinary I/O problem. A language model is a lossy, stochastic channel; using
it where a byte-exact channel is required is the defect, not the tuning.

[S-005] also notes the security corollary, which is easy to miss: routing data
around the model lets you "define deterministic security rules, choosing where
data can flow to and from."

**Evidence.** `PRIMARY`.

---

## 7. Anti-patterns

### PP-021 — The anti-pattern catalogue

Each stated with the source that documents it, then the mechanism, then the
countermeasure.

| # | Anti-pattern | Documented by | Countermeasure |
|---|---|---|---|
| 1 | Pre-baked domain assumptions hardcoded in prompts | [S-004] | version the knowledge as a queryable artefact, not prose |
| 2 | Prompt-as-spec: behaviour specified only in prompt prose | [S-001], [S-002] | promote every rule to a versioned, diffable, testable artefact |
| 3 | One giant prompt enumerating edge cases | [S-004], [S-077] | diverse canonical examples + deterministic validators for the rest |
| 4 | Implicit, unverifiable acceptance criteria | [S-076] | specific/measurable/achievable/relevant, per step |
| 5 | Non-deterministic assembly of deterministic content | [S-005], [S-137] | reference through the model, value through code (PP-020) |
| 6 | Silent truncation | [S-040], [S-014], [S-005] | assert truncation state as a first-class value |
| 7 | Drift across model and tool versions | [S-042], [S-001] | pin and record per run; assert runtime values, not documented defaults |
| 8 | An evaluation that cannot detect its own blind spots | [S-114] | rubric-text-only baseline as a mandatory control |
| 9 | "Add more judges" | [S-002] | prefer deterministic validators; one well-shaped judge call |
| 10 | Bloated or ambiguous tool sets | [S-006], [S-004] | if an engineer cannot say which tool applies, the agent cannot either |
| 11 | Path dependence in golden tests | [S-007], [S-002] | outcome-based assertions, not step-based |

**Two of these deserve expanding, because they are the ones most likely to be
alive in a pipeline that has none of them.**

**Drift (7) has a documentary proof.** Ollama's own documentation gives three
different `num_ctx` defaults across four simultaneously-live pages: 4096 in
`faq.mdx`, 2048 in `modelfile.mdx`, 1024 in an `api.md` example, and a
VRAM-tiered ladder in `context-length.mdx` [S-042]. The documentation was not
wrong about the intent; it was stale relative to itself. That is the exact shape
of version drift, in a project whose runtime the pipeline depends on. The
operational rule that follows is narrow and cheap: **never rely on an implicit
runtime default — set it explicitly and assert it**, and treat the docs as
advisory about what the default *should* be rather than what it *is*.

**Path dependence (11) explains why golden-file tests flake on anything
non-deterministic.** [S-002]: "traditional evaluations often assume that the AI
follows the same steps each time… But multi-agent systems don't work this way.
Even with identical starting points, agents might take completely different valid
paths." The corresponding rule from [S-007] is that a grader checks the
*outcome*, not the transcript: "A flight-booking agent might say 'Your flight has
been booked' at the end of the transcript, but **the outcome is whether a
reservation exists in the environment's SQL database**."

**Evidence.** `PRIMARY` throughout, except #11 which is `PRIMARY` on the
transcript/outcome rule and `PRIMARY` on the path-dependence observation.

---

## 8. What this catalogue could not establish

Recorded so the gaps are visible rather than filled with plausible prose.

| Open question | Status |
|---|---|
| Schema-following ability vs model size for local open-weight models | No controlled study found. Constrained decoding is model-agnostic *by construction* [S-045]; the cost on a weak model is latency, not format failure. The real risk is content, not syntax |
| Independent measurement of determinism controls on llama.cpp / Ollama | None found. The only primary material is [S-040]'s own admission about `cache_prompt` and [S-043]'s batch-invariance feature — both vendor documentation, not studies |
| Optimal chunk size for a structured regulatory corpus | Unsettled. [S-119] and [S-120] are both small and preliminary, and [S-119] finds its own measuring instrument (RAGAS faithfulness) unreliable on structured text |
| Whether the U-curve in [S-116] is a defect or a training-distribution prior | `CONTESTED` — [S-117] argues the latter. Both fit the data |
| Whether multi-agent aggregation transfers to a shared-context task | `CONTESTED` — [S-002] reports +90.2% on its own eval; [S-132] finds a single agent matches homogeneous workflows via KV-cache reuse. See `02_AGENT_ORCHESTRATION_PATTERNS.md` AO-006 |
| Whether format-constrained decoding costs reasoning quality | `CONTESTED` — [S-179] against, with the mitigation of keeping a reasoning field in the schema |

**On the survey's own coverage.** General web search engines were CAPTCHA-blocked
from the survey environment, so discovery ran through direct fetches of canonical
URLs, the arXiv API, and GitHub. The consequence is a bias toward sources already
known to be canonical, and a likely miss of any 2025–2026 practitioner essay not
in that set. Two sources in the registry are recorded as unverified for the same
reason — an OpenAI landing page returning HTTP 403, and a vendor blog cited by
another source but not read directly — and the checker forbids either from
carrying a quotation, so their claims cannot launder into the documents.
