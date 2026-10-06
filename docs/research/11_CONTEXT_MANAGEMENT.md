---
document_id: AEGIS-RES-11
title: 'Context management — annotated catalogue of the open gaps'
version: 0.1.0
created: 2026-10-05
status: ACTIVE
survey_date: 2026-10-05
sources: 'docs/research/sources.yaml'
---

# Context management — annotated catalogue of the open gaps

**What this document is, and how it differs from what already exists.**
[01_PIPELINE_PATTERNS.md](01_PIPELINE_PATTERNS.md) §4 already carries
`PP-013` (context engineering), `PP-014` (retrieval) and `PP-015` (corpus
composition); [02_AGENT_ORCHESTRATION_PATTERNS.md](02_AGENT_ORCHESTRATION_PATTERNS.md)
§3 carries `AO-003` (compaction and memory). Those are not rewritten here.

This catalogue covers the eight sub-questions the existing entries *name but do
not evidence*. Each was confirmed absent from the 222-entry registry before
this pass. `CX-001`..`CX-008`.

**Method.** 100 sources registered across three fronts this pass
(S-284..S-383); the context front contributed `CX-001`..`CX-008` plus two
re-pointed pre-existing entries (S-249, S-282). The same declared bias as
[12_PROMPT_ENGINEERING.md](12_PROMPT_ENGINEERING.md) applies: `WebSearch` was
unavailable, so discovery ran through the arXiv API and direct canonical
fetches, which favours papers over practitioner write-ups.

**The headline is corrective, and it is stated up front.** Two bodies of
literature make claims that this pass found to be materially overstated — KV
cache compression's "negligible loss", and prompt caching's incompatibility with
determinism. Both corrections point the same way: the interesting quantity is
never the aggregate score, it is what happens to *instructions* and to
*provenance* under the intervention.

---

## 1. Serving-layer context compression

### CX-001 — The eviction family and its central claim

Evicting tokens from the KV cache is the cheapest way to buy context. The
founding method reports 29× throughput over three inference systems at a 20%
heavy-hitter budget [S-336]. The most-cited result in the literature is
PyramidKV's: matching full-cache performance at 12% of the cache, and at just
**128 KV entries, LLAMA-3-70B scores 100.0 on needle-in-a-haystack** [S-337].

Read those as what they are: throughput and memory measurements, validated on a
retrieval probe. `CX-002` is what happened when anyone checked the instructions.

### CX-002 — "Negligible loss" does not survive a multi-instruction evaluation

**This is the finding that should govern any decision to touch the serving
layer.** Evaluating five eviction methods on two open models under
multi-instruction prompting with IFEval: *"certain instructions degrade much
more rapidly with compression, effectively causing them to be completely
ignored by the LLM"*, with **system prompt leakage** as the case study [S-338].

The failure concentrates in exactly the behaviour an unattended compliance
pipeline depends on. An R6 grounding gate is an instruction that must be
obeyed; under aggressive eviction it is among the first things silently dropped,
and the aggregate task score does not move much because the task itself is
mostly retrieval.

**The correct evaluation protocol is now published, and it is specific:** a
per-source full-cache control, with correct-under-full-cache / wrong-under-
compression rows selected *per method-setting* so that no compressor defines
another's test set. On that protocol, 63.2% of failure rows have low or partial
diagnostic coverage [S-339] — meaning most published comparisons are underpowered
for the question they are being used to answer.

**One result is directly actionable for this repo.** When the evicted tokens hold
the answer-bearing evidence, *"the model may hallucinate instead of recognizing
that the compressed context is insufficient"* [S-340]. Compression does not
produce a visible error; it converts missing evidence into **confident** output.
A 10.1M-parameter adapter trained on ~2,600 examples cuts that hallucination by
97%. For a pipeline whose defence is a grounding gate, this says the gate must
be able to fire on *insufficient context*, not only on *wrong output*.

---

## 2. Window extension, and what a window is worth

### CX-003 — The extend / retrieve / compress triangle

Extension is not free and its cost is named. LongRoPE reaches 2,048K tokens,
and its third listed innovation is that it *"readjust[s] LongRoPE on 8k length
to recover the short context window performance"* [S-344] — the short-context
regression is a separate repair pass, paid for out of the regime a short-context
pipeline actually runs in. RoPE's base parameter bounds achievable context
absolutely, which is the falsifiable form of the claim [S-341].

**The number that should govern any window assumption:** *"the effective context
lengths of open-source LLMs often fall short, typically not exceeding half of
their training lengths"* [S-342]. A nominal window is a marketing figure; the
effective one is routinely half. The recovery requires no training, so this is a
property of the checkpoint, not of the serving configuration — which means it
cannot be fixed downstream.

**On the extend-versus-retrieve question, the independent measurement is
narrower than the vendor claim.** After filtering out questions answerable
without external context: *"LC generally outperforms RAG in question-answering
benchmarks… Summarization-based retrieval performs comparably to LC, while
chunk-based retrieval lags behind. However, RAG has advantages in dialogue-based
and general question queries"* [S-343]. This is the external anchor
`PP-014`'s "under ~200k tokens, no RAG" currently lacks — and note that
**summarisation-based** retrieval, not chunk-based, is what matches full
context. `CX-004` is why that qualifier turns out to be the whole argument.

### CX-004 — Compression destroys provenance, and the number is worse than expected

The repo already holds a claim here as a hypothesis: a compressed claim loses
its citation, so a token budget is simultaneously a provenance budget. This pass
found the quantitative measurement.

On ASQA at a nominal 0.25 budget, a RECOMP-style compressor's citations score
**0.86 precision against its own summaries but 0.12 against source spans**, and
claim verification after source recovery yields an **unsupported rate of 0.88
versus 0.17 when checking summaries** [S-249].

**Read that pair carefully, because it is an audit finding and not a quality
finding.** A verifier that checks a compressed claim against the same
compressed material will pass it roughly seven times more often than a verifier
that checks it against the source. The compression did not make the answer
worse; it made the answer *look* grounded to any check that shares its blind
spot.

The same property appears at the serving layer. In a shared KV cache, *"cross-
adapter collisions reduce accuracy from 0.94 to 0.64, incompatible KV
representations reduce reasoning accuracy to zero, and salt omission enables
93% prompt identification from timing"* [S-355]. Identity by token content is
what makes a cache fast and is also what erases provenance; the repair is a KV
provenance contract costing under 0.34 ms on the hit path.

**The compounding result, and it connects directly to the compaction step.**
Memory-poisoning defences that base authority on content or lineage "fail
exactly where the theory predicts (up to 68% laundering attack-success)," and
one of the three named laundering channels is **the agent's own summarisation**
[S-346]. A memory entry that passes review because it is a faithful summary of a
poisoned document *is* a laundering success.

So the two results in this section compose into one uncomfortable conclusion:
summarisation is simultaneously the cheapest safe compression for *content*
[S-343] and the most dangerous compression for *trust* [S-346]. The axis that
separates them is not accuracy — it is whether the compression is
**extractive-verbatim** or **abstractive**. For a regulatory corpus whose entire
value is verbatim article text, that distinction is not a tuning knob.

---

## 3. Evaluating context

### CX-005 — Four benchmarks that changed what "long context" means

- **RULER**: of models claiming ≥32K, *"only half of them can maintain
  satisfactory performance at the length of 32K"*, despite near-perfect vanilla
  needle scores [S-282].
- **HELMET**, over 59 models: *"synthetic tasks like NIAH do not reliably
  predict downstream performance"*, and — the finding that matters most for this
  repo — open-source models lag closed ones precisely *"when tasks require
  full-context reasoning or following complex instructions — the gap widens as
  length increases"* [S-348]. That is the AEGIS configuration exactly.
- **The audit**: across 11 long-context benchmarks, *"none jointly controls task
  position, filler content, and context length for reasoning."* In the initial
  five-model set, **76% of middle-position errors match the surrounding filler
  text, versus 22% at the end position**, and a probe that appends a copy of the
  target task at the end restores middle accuracy to within ±4 points across all
  nine models [S-349]. Filler interference is a separable error mode from
  position, and the probe is the causal evidence.

### CX-006 — Memory across sessions, and drift as a measurable quantity

Long-term memory is a security surface, and the numbers are severe. Poisoned
memories were written in up to **99.8%** of attacks, and among successful
retrievals they produced attacker-intended actions in **60–89%** of evaluations
[S-351]. The payload stays dormant across later conversations, which means a
grounding check that passes today is not evidence about tomorrow — the
per-run gate has no purchase on this class of failure.

The constructive side is more useful to the repo. Drift can be formalised as the
turn-wise KL divergence between the model and a goal-consistent reference, and
its evolution has *"stable, noise-limited equilibria rather than runaway
degradation"*, with simple interventions reliably reducing it [S-352]. That
offers a principled replacement for a binary pass/fail grounding gate: a
quantity, measured against a reference, with a known equilibrium.

---

## 4. Position, structure, and the factor the repo has not named

### CX-007 — For structured input, the operative variable is density, not position

The repo's existing evidence for position effects is prose-only, and this pass
confirms that gap is real while partly redirecting it.

The third factor, alongside length and position, is **lexical density** — the
rate at which a context introduces distinct information. Holding length (~12K
tokens) and needle position fixed and varying only density, across open-weight
models from 9B to 685B: *"models that are near-perfect in sparse contexts drop
below 60% retrieval score on denser ones"* [S-350]. The stated conclusion is
that effective context capacity is a function of lexical density.

**This is a direct challenge to how the repo reads its own U-curve.** Dense
structured regulatory text is the regime where the classical
position-dominated account is least predictive, and where the measured effect is
density. A regulatory corpus is high-density structured text by construction.

The supporting evidence on structure is strong and in the same direction: on a
legal corpus, well-structured formats improve exact-match accuracy by ~20
points, and adding a structural advisory to the system prompt adds a further
~10–13 [S-357]. And the failure mode of a JSON-emitting pipeline is not schema
conformance — compliance is near-perfect while leaf-value accuracy reaches only
83.0% on text, and it *"makes extraction substantially harder"* as context grows
[S-359]. The output contract is not the risky part; the values inside it are.

### CX-008 — Cost attribution, and what caching is actually worth

The strongest measured attribution in this space: across MCP topologies,
**56–72% of total tokens and 60–67% of latency go to planning and schema
injection**, and *"actual tool execution constitutes a negligible fraction of the
total cost"* [S-360]. The authors' own conclusion — optimise schema
orchestration and transport, not execution speed — is the right place for a
pipeline to look before tuning anything else.

**On prefix caching, the repo's `PP-010` is over-stated as written and this pass
says so with a measurement.** `PP-010` records that prompt caching breaks
determinism. The measured version is narrower: with an exact replica on both
sides, BF16 constructions differ on 166 of 200 suffixes while replicas remain
exact, and **FP32 produces no decoded disagreement (95% Wilson upper bound
1.88%)**; transplanting the cache between runs makes divergent continuations
follow their donor in 24/24 and 43/43 trials [S-356]. The cache is the cause, it
is attributable, and **numerical precision moderates its expression**. The
failure that should actually worry a pipeline is cross-context key collision
(0.94 → 0.64 accuracy) [S-355], not caching as such.

**The mechanism, so the cost claim is bounded.** Automatic prefix caching
works by keeping the KV cache of existing queries so a new query *"can skip the
computation of the shared part"* [S-353] — with two limits stated in the same
document: it reduces **prefill only, not decode**, and a hit can resume only at
a block boundary. So the saving is real, bounded, and unrelated to the
divergence question in the previous paragraph.

**On eviction policy, the calibration is that it barely matters here.** Across 14
policies on production traces from two companies, *"sophisticated policies
designed for traditional caches provide little benefit over LRU"*, because
prefix reuse is dominated by regular session pacing which makes recency
unusually predictive [S-354]. A batch pipeline satisfies exactly that
precondition — so "fancy eviction does not help here" is a preregisterable
negative prediction rather than an opinion, and a cheap experiment to run
before investing in it.

---

## 5. What this survey could not establish

1. **Position effects on a JSON/YAML *schema* placed at start vs middle vs end.**
   The closest work controls position and filler [S-349] or format and placement
   across four renderings [S-358]; nothing isolates schema placement. This is a
   real, publishable gap and it is the repo's own declared extension to
   `S-116`.
2. **Cost attribution to a regulatory anchor.** Every attribution method in this
   block attributes cost to token *types* or template *sections* [S-360].
   None attributes it to a citation. The repo's thesis has exactly one external
   quantitative anchor [S-249] and no competitor — a defensible niche.
3. **Whether eviction loss and the R6 gate interact in this specific
   pipeline.** `CX-002` establishes the mechanism in general and [S-340]
   establishes the failure shape; nobody has measured the AEGIS case, and it is
   measurable.
