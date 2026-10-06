---
document_id: AEGIS-RES-09
title: 'KG pattern mapping — the three questions, answered against the AEGIS implementation'
version: 0.1.0
created: 2026-10-04
status: ACTIVE
survey_date: 2026-10-04
sources: 'docs/research/sources.yaml'
upstream: 'AEGIS-RES-05, AEGIS-RES-06, AEGIS-RES-07, AEGIS-RES-08'
---

# KG pattern mapping — the three questions, answered

**What this document does.** The three catalogues (construction `KG-001..KG-010`,
query `KG-011..KG-019`, evaluation `KG-020..KG-026`, pipelines `KG-027..KG-032`)
are references. This is the verdict. It answers three questions in order —
**what can we experiment with, how do we build a knowledge graph, how do we
evaluate a model's use of one** — and reads the evidence against what this repo
already does.

**The verdict up front.** *ADR-011's "schema now, materialise later" is the right
call, and this survey strengthens it on three independent grounds.* The
literature's own verdict is that a graph **loses on answer quality** when it is
adopted for recall and **wins on traceability and deterministic queries** — which
is exactly the split ADR-011 D4 already drew from weaker evidence. The new
survey supplies the mechanism the earlier review could not: the graph's gain is
bounded by extraction recall, and on a curated corpus extraction recall is
**100% by construction**, so the dominant failure mode of the published systems
does not exist here. The graph is cheap to build correctly *because* the corpus
is already graph-shaped.

**What changes, and what does not.** No ADR is reversed. One ADR is
**strengthened** with a mechanism, one gap the mapping document recorded as
"the largest" is **re-scoped** on new evidence, and six gaps (G7–G12) are added.
Five of the six new gaps cost **zero GPU hours** and are deterministic checks.

---

## 1. Question one: what can we experiment with?

### 1.1 The constraint that decides the experiment list

Before any experiment list: **[S-171] measured that only ~65.8% of gold answer
entities appear in an LLM-built graph**, and [S-205] measured GraphRAG's
constructed graph at **0% valid triples** under hand-scoring. The dominant
failure mode of every published graph-RAG system is that *the answer is not in
the graph*. A curated corpus has no such failure mode, because the entities are
canonical by construction. So the published results do not transfer as a prior
about what a graph buys here — but the *measurement instruments* transfer
perfectly, and those are what an experiment list should be built from.

### 1.2 What the evidence says a graph experiment should and should not measure

| Measure | Verdict | Source |
|---|---|---|
| Answer quality (F1/EM) of a KG system | **The wrong headline.** Graphs lose on single-hop, lose on summarisation against a gold reference, and the one published win is judge-scored on unreleased data | [S-171], [S-234], [S-236], [S-225] |
| Global "sensemaking" quality | **Do not use.** Every positive result is reference-free judging; every reference-based replication reverses it | [S-170] vs [S-171], [S-236] |
| Answer-entity coverage in the graph | **Use as a gate.** Cheap, deterministic, no judge, and predicts downstream failure | [S-171] |
| Citation resolution at context level and at answer level | **Use both.** Reporting one inverts the architecture ranking | [S-242] |
| Abstention rate paired with hallucination rate | **Use both.** Advanced retrieval drives abstention to zero | [S-244] |
| Structural graph metrics as "quality" | **Do not use.** No gold standard, monotonic in verbosity, direction empirically backwards | [S-234] vs [S-205] |
| Link prediction (MRR/Hits@k) as QA proxy | **Do not use.** Structurally cannot detect the failure that matters | KG-035 |
| A single LLM-judge score | **Do not use.** One judge call, no floor, no pinned snapshot, is not a measurement | [S-241], [S-242], [S-240] |
| Provenance: can the pipeline say *which step* produced an unsupported claim | **Use.** This is where the graph has no competition | [S-247], [S-248] |

### 1.3 The experiment list

Six experiments, `E-13`..`E-18`, detailed in
[04_EXPERIMENT_BACKLOG.md](04_EXPERIMENT_BACKLOG.md). Five cost **zero GPU
hours** because they read artifacts the pipeline already writes.

| ID | Question | Cost | Isolated variable |
|---|---|---|---|
| **E-13** | Does materialising the graph answer the T6 anchor-provenance debt? | 0 GPU-h | graph materialised vs not |
| **E-14** | Does the pipeline abstain when the corpus does not support a claim? | 0 GPU-h | abstention rate, paired with hallucination rate |
| **E-15** | Does the context-pack budget break evidence chains while single-hop metrics stay clean? | 0 GPU-h | pack budget as the variable |
| **E-16** | Does a retrieved anchor table beat a full anchor dump in the P4 prompt? | ~2 GPU-h | schema presentation — dump vs retrieve |
| **E-17** | Is the L3 judge's temperature and seed actually pinned? | 0 GPU-h | audit, not experiment |
| **E-18** | Does every emitted citation resolve, and is a model-returned id that fails to resolve discarded? | 0 GPU-h | programmatic vs model-assigned ids |

**E-16 is the one that answers your second question empirically rather than by
citation.** [S-215] measured that a plain question with no entity or relation
grounding scores F1 **0.08 / 0.02 / 12.00 / 16.42** across four benchmarks, and
that adding entity-and-relation-encoded retrieval takes the same backbones to
**76.59 / 57.69 / 85.45 / 75.14**. That is the largest single measured effect in
the query thread, and it is a *prompt-assembly* effect — it needs no graph at
all. AEGIS already assembles prompts from a pack; E-16 tests whether the pack
should carry a **retrieved** subset of the anchor set instead of all of it.
[S-223] is the necessary counterweight and is why E-16 is an experiment rather
than a conclusion: a larger linearised context degrades reasoning even when
nothing is missing, with o4-mini collapsing 59 → 5 between 100 and 500 nodes.

**Why the rest cost nothing.** E-13, E-14, E-15 and E-18 read the trace, the
output, and the corpus — the artifacts a run already produces. They are the
"measure first" experiments: the evidence says the *measurement point* and the
*scorer* dominate published graph results, so establishing our own floors before
building anything is the correct order.

---

## 2. Question two: how do we build a knowledge graph?

### 2.1 The short answer: this repo is the easy case, and the literature says why it is easy

A curated corpus removes the three hardest problems in the published literature
outright. Stating this explicitly matters, because the survey's strongest
findings are all about problems this repo does not have:

| Published hard problem | Status here | Why |
|---|---|---|
| **Entity resolution** — 57% metric invisibility [S-202]; exact-string matching in the reference implementation [S-170]; hierarchical cluster-aware merging needed [S-197], [S-204], [S-195] | **Absent.** Every entity is a canonical ID written by a human in the corpus. | The `AG-`/`PO-`/`SR-`/`D-XX.Y` id space *is* the resolution output. There is nothing to merge. |
| **Extraction recall** — 65.8% of answer entities present [S-171]; 0% triple validity for LLM-built graphs [S-205] | **Absent by construction.** 100%, and checkable by id set comparison against `baseline/registry.csv`. | No extraction step exists. The nodes are already typed fields. |
| **Table-expansion artefacts** — a transitive taxonomy chain gave a median CVE 8 techniques and 19% got ≥20 [S-201] | **Absent.** Rule R2 forbids the agent to re-derive anchors, so derived edges cannot be introduced by the model. | The failure mode was never available. |

This is the mechanism the earlier literature review could not supply when it
called the KG-vs-pack choice "a reasoned bet, not settled science"
(`docs/pipeline/04_LITERATURE_REVIEW.md` §3). The bet is now better grounded: the
published systems lose because their graphs are incomplete at the entry point,
and ours is complete at the entry point by construction.

### 2.2 The build, in the order the evidence supports

**Step 1 — materialise, do not model.** A deterministic builder script reads the
surfaces already enumerated in
[`docs/pipeline/02_KNOWLEDGE_ARCHITECTURE.md`](../pipeline/02_KNOWLEDGE_ARCHITECTURE.md)
§2 — `baseline/MAPPINGS/traceability/traceability.csv`,
`baseline/MAPPINGS/sr_control_mappings/*.json`, `baseline/registry.csv`,
`baseline/CONTROLS/**/*.json`, the `regs/<REG>.md` YAML blocks, and the `aegis:`
structural tags — and emits `node_link.json` plus a GraphML export. The node and
edge schema is already designed in §3.1/§3.2 of that document; **the builder
implements that schema, not the reverse** (ADR-011 C1).

Two properties the evidence requires, both already the repo's convention:

- **Regenerable, never hand-edited.** The graph is a derived view; consistency
  is checked by comparing node and edge counts against source record counts —
  the same anti-circular discipline as `scripts/verify_no_loss.py`, and the same
  reason [S-202] matters: a derived view that is not checked against its sources
  drifts silently.
- **Verbatim-only, no LLM-derived content.** The corpus's integrity depends on
  verbatim content, so no summarisation step. This is also what [S-263] implies
  operationally: prompt and configuration files are part of the index state, so
  a hand-maintained, reviewable builder is preferable to an LLM-built index
  whose behaviour depends on a model version.

**Step 2 — resolve the T6 debt first, because it is the named query need.**
[ADR-011](../decisions/ADR-2026-10-01_knowledge-representation.md) D4 identifies
exactly one concrete question the packs cannot answer: the 58 out-of-set
anchors, i.e. *which objective or test cited each anchor that is not in the
objective's published anchor set*. That is a two-hop graph traversal
(anchor → control → citing objective). It is the whole justification for the
graph, and it should be the acceptance criterion for the builder rather than a
demonstration of query elegance.

**Step 3 — add coverage as a gate before anything else is measured.** Per
KG-022, compute the fraction of corpus identifiers that appear as graph nodes,
and treat it as a precondition rather than a score. On a curated corpus this
should be 100% and *stay* 100%; a drop is a builder bug, not a finding. Its
value is that it makes the graph's own completeness auditable in the same way
`verify_no_loss.py` makes the corpus's.

**Step 4 — only then consider a model-facing surface, and prefer the template.**
If a prompt ever needs to consult the graph, KG-016's `CypherTemplateRetriever`
shape is the one to copy: a human-written traversal with model-inferred
parameters, so the query *shape* is fixed by a human. That makes KG-011's
validity problem structurally unreachable — the model is never in a position to
emit an invalid query, only a valid one with wrong bindings, which is a cheaper
and more diagnosable failure. The alternative, emitting a traversal plan in a
special token format and grounding it against the graph before execution
(KG-014), is the strongest published form if more flexibility is ever needed.

**What not to do, from the evidence:**

- Do not derive edges by traversing taxonomies — [S-201] measured that doing so
  gives a median subject 8 derived labels with 53% of the corpus carrying the
  same one, and calls it an artefact of the tables.
- Do not build a community-summary hierarchy. [S-170]'s Leiden hierarchy is
  designed to make *unstructured* corpora summarisable; a corpus with 38
  sub-domains already *is* a hierarchy, hand-curated, and [S-234] shows the
  summarisation advantage reverses under reference-based metrics anyway.
- Do not add entity resolution, merge logic, or an LLM extraction step. They
  solve problems this corpus does not have and would introduce a failure mode
  that [S-202] shows is invisible to the metrics used to evaluate it.

---

## 3. Question three: how do we evaluate a model's use of a knowledge graph?

### 3.1 The framing that matters: do not evaluate the graph by answer quality

This is the recommendation most likely to be resisted and the one the evidence
supports most strongly. The literature's verdict on graph-vs-vector answer
quality, after three independent replications, is:

- Single-hop: the graph **loses** — NQ F1 64.78 (RAG) vs 34.28
  (KG-GraphRAG triplets) [S-171]; RAG-with-rerank beats all GraphRAG methods on
  fact retrieval [S-234].
- Summarisation against a gold reference: the graph **loses** — all four QFS
  datasets, ROUGE-2 F1 6.32 vs 3.23 [S-171]; independently confirmed [S-236].
- Abstention: the graph **loses catastrophically** — Null queries 19.27 vs 96.01
  [S-171], where the correct answer is "insufficient information".
- Multi-hop: the graph wins, by **about 2pp** once hybrid fusion is calibrated
  [S-257] — not by the multiples reported elsewhere.

So a QA-score experiment would, on the literature's prior, most likely *fail* —
and would tell us little, because the failure would be the published one rather
than an AEGIS-specific finding. The evaluation that is both cheaper and more
informative measures the properties the graph is actually being used for.

### 3.2 The metrics to add, in priority order

**First: answer-entity coverage, as a gate (KG-022).** What fraction of the
corpus's canonical identifiers appear as graph nodes? Deterministic, computed
once, no judge, no per-query cost. On this corpus the expected value is 100% and
the interesting output is the *diff* when it is not.

**Second: citation resolution, measured at both levels (KG-024).** This is the
highest-value addition and it is nearly free. [S-242]'s finding is the sharpest
epistemological caution in the survey: "scoring the retrieved set as the
attribution set ranks GraphRAG **last**; scoring the answer's own citations ranks
it **best or tied-best**." The measurement point, not the architecture, drove the
ranking. So report both:

- *context-level* resolution — of the ids handed to the model, what fraction
  resolve to a corpus node;
- *answer-level* resolution — of the ids the model emitted, what fraction
  resolve, and whether a non-resolving id was **discarded** rather than passed
  through.

The second half is [S-247]'s design detail and it is the one that matters here:
sentence ids are assigned **programmatically** and any model-returned id that
does not match is discarded, which "guarantees that the sentences included in the
evidence trail are not hallucinated". AEGIS can adopt this verbatim — it already
has the id space to do it with.

**Third: abstention paired with hallucination (KG-024, E-14).** [S-244]'s result
is the one a compliance pipeline should take most seriously: advanced retrieval
lowers hallucination but **drives abstention from 5.0% to zero** — retrieval
makes the system always answer, whether or not evidence supports it. The R6
grounding gate is the mechanism that should prevent this, and E-14 is the
measurement that says whether it does. Report the pair; an abstention rate alone
will not reveal the inversion.

**Fourth: evidence-chain retention under the pack budget (E-15).** [S-223] and
[S-242] both identify the same silent failure: a bounded context destroys the
evidence chain for multi-hop claims while every single-hop metric stays clean
(graph walk at context precision 0.12–0.23 while the synthesizer cites at
0.48–0.65; o4-mini 59 → 5 between 100 and 500 nodes). A cheap deterministic
test: take the emitted citations from a run, walk the pack, and report the
fraction of citation chains that survive the budget intact. No LLM required.

**Fifth, and only if a judge is used at all: a stated noise floor.** [S-242]
measured same-input same-day test–retest at **κ=0.76, i.e. 12% of verdicts flip
on resampling alone**, and re-judging frozen identical inputs eleven weeks later
gave **κ=0.138 — chance level — against its own earlier verdicts**. So: never
report a single judge call, pin the model *and* its snapshot date, and report the
test–retest floor next to any claimed difference. Note also that temperature=0
is **necessary but not sufficient** — forced greedy decoding still leaves items
flipping, because the residual is in the forward pass, not the sampler
([S-241]) — and that some providers now reject a temperature parameter
outright, so the conventional mitigation is not universally available.

**Sixth: the scorer itself (KG-023).** Any comparison must name its answer
matching rule, its credited form, and its judge model plus snapshot date.
[S-202] showed a fixed prediction set spanning F1 0.1577–0.6994 depending only on
the matcher, and reversing 11 of 45 pairwise orderings; [S-259] showed the
credited form alone changes nDCG on 83–94% of shared queries. A graph result
without those three named is not a measurement.

### 3.3 What the literature does *not* license, stated so it is not assumed later

- **No published head-to-head isolates curation** as the variable — same
  benchmark, same model, same retrieval algorithm, graph curated vs LLM-built.
  The curated-positive ([S-173]: >50% token reduction with no accuracy loss, +71%
  for Llama-2-13b) and the LLM-built-negative ([S-225]: 32 vs 46 accuracy) are
  not commensurable. AEGIS's inference that curation is the deciding variable is
  a *reasoned* position, and this remains the single most obvious missing
  experiment in the field.
- **No packaged path-existence metric exists.** "Does a connected subgraph link
  the question's anchors to the required control ids?" is the correct question
  and is computable today with plain traversal and no judge — which is why E-15
  can be deterministic.
- **No correlation study** between any graph-specific deterministic proxy and
  human-judged quality. The metrics in §3.2 are well-defined and cheap; their
  trustworthiness is largely untested, with one partial exception ([S-238] found
  the *conclusion* of typed-perturbation diagnostics is invariant to the
  answer-matching rule, which is a licence to use the cheap matcher).
- **No study of a router's accuracy.** [S-234] proposes routing by query
  complexity; nobody has validated the router itself against gold labels. So any
  future "use the graph only for hard questions" logic is a heuristic, not a
  measured policy.

---

## 4. The verdict against the implementation

| Finding | Verdict | Basis |
|---|---|---|
| Deterministic context packs as the retrieval mechanism | `ADOPTED (convergent)` | [S-225] (graph loses on answer quality), [S-234], [S-171] |
| Prompt-chaining workflow with deterministic gates, not an autonomous agent | `ADOPTED (convergent)` | [S-251] on verification without a spec; [S-247] on reverse verification |
| Schema designed now, materialised on demand | `ADOPTED (convergent)` — **strengthened** | The bet is now grounded in the extraction-recall mechanism, not asserted |
| Text2Cypher-style free query generation | `DIVERGENCE (deliberate)` | Prefer the template form (KG-016): shape fixed by a human, only bindings generated |
| Keeping a scoped, curated corpus rather than a live CTI feed | `ADOPTED (independent)` | Nothing in the literature covers this; KG-010's drift problem is bounded by the corpus review cycle |
| L1 deterministic guards as the strong validation layer | `ADOPTED (convergent)` | [S-251]: the requirement list *is* the spec, the checker is downstream |
| **Determinism of the pipeline, by seed** | **Ahead of the literature** | See §5 — the strongest finding in this mapping |

### 4.1 Where the implementation is ahead

**The determinism result is stronger than the judge-layer literature supports,
and the discrepancy is worth recording rather than smoothing.** AGENTS.md §-1
records EXP-02's finding that 15 seeded runs produced byte-identical goal sets
with retention sd 0.0000. [S-241] measured that even with temperature pinned to 0
**and** forced greedy decoding, items still flipped, locating the residual
non-determinism in the **forward pass rather than the sampler** — so no
sampling-side knob reaches it.

The two results are compatible, and the compatibility is itself the finding. The
repo's determinism is scoped to what EXP-02 measured — the *sampler*, with a
fixed seed, at the serving layer it used — while [S-241]'s residual is
attributed to a *judge* forward pass. So the honest reading is: **the pipeline's
sampling determinism is established; the L3 judge layer's determinism is not, and
by [S-241] probably cannot be established by seeding alone.** That is exactly
what E-17 is for, and it costs nothing.

This is the second place in this survey where the repo's design reached a
conclusion independently, as in the earlier mapping's finding that the
deterministic guards are stronger than the literature requires.

---

## 5. Contradictions and gaps

### Contradictions recorded

**C-01 — Does the graph win on global sensemaking?** `CONTESTED`, and this is the
most consequential one. [S-170] reports comprehensiveness win rates of 72–83%
(p<.001) for global search over vector RAG. [S-171] re-ran the *idea* with
**reference-based** metrics and got the opposite sign on every QFS dataset, and
[S-236] independently found graph aggregation "may overemphasize high-level
statements at the expense of fine-grained details". **No paper was found showing
GraphRAG beating vector RAG on global sensemaking against a gold reference.**
The reconciliation is that [S-170]'s result is judge-scored on unreleased data;
[ADR-011] D3's rejection of GraphRAG-style community summarization for this
corpus is therefore better supported than the earlier review could state.

**C-02 — Does a graph improve answers?** `CONTESTED`. [S-173] (curated,
peer-reviewed): +71% for Llama-2-13b, >50% token reduction with no accuracy loss.
[S-225] (LLM-built): 32 vs 46 accuracy, *worse* than plain Embedding-RAG. Not a
true contradiction — the graphs differ in curation, domain, size, metric
definitions, and publication standing — but the field treats them as competing
and no head-to-head exists. AEGIS's position is that curation is the variable
([S-206] on ontology-conformance, [S-197] on anchoring), and that position is
reasoned, not established.

**C-03 — Do structural graph metrics indicate quality?** `CONTESTED`.
[S-234] defines NodeCount/EdgeCount/AverageDegree/AverageClusteringCoefficient
as graph-quality metrics; [S-205] shows quality *improving* while the graph
*shrinks* (entities 4,602 → 3,573), so the direction is empirically backwards.
Resolution: descriptive only, never normative (KG-026).

**C-04 — How large is the hybrid graph+vector win?** `CONTESTED`. [S-258] claims
+160% / +177%; [S-257] measures **+1.9pp** under a controlled ablation with
significance tests and a stated normalisation. The gap is baseline disclosure,
not a measurement dispute. Use +1.9pp.

**C-05 — How much schema should the model see?** `CONTESTED`, and the resolution
is the useful part. [S-215] shows schema grounding is a *precondition* (0.08 →
76.59 F1) and that retrieval beats a bare question. [S-223] shows that feeding
the *complete* 100-node graph — exhaustive schema, zero retrieval error — still
fails, and that o4-mini collapses 59 → 5 between 100 and 500 nodes while the
graph still fits the context window. Reconciled: **grounding is necessary;
retrieval past that point has diminishing returns; and the binding constraint
becomes the model's ability to execute traversal over whatever it is shown.**
That is why E-16 is an experiment on this pipeline rather than an adoption of
either published recipe.

**C-05a — Is the window the binding constraint, or the model?** `CONTESTED` in
the literature, and the new evidence (2026-10-05 pass) tilts it. Everything
above treats `num_ctx` as a capacity to be raised. [S-282] and [S-283] measure
the *effective* length instead of the advertised one: only about half the tested
models hold satisfactory performance at 32K, and at 32K 11 of 13 models fall
below half their short-context baseline on needles with minimal lexical overlap
— with reasoning models and CoT in the comparison, so "spend more reasoning on
it" is not the repair. [S-223] is the decisive form, because its collapse was
measured *while the material still fit the context window*. Read together the
three say the same thing: **a prompt that fits is not a prompt that is read**,
so the pack budget cannot be justified by the size of the window available. This
is the anchor for `KG-033`'s framing and for the decomposition decision in
`docs/decisions/ADR-2026-10-05_pack-budget-and-context-policy.md` D1/D3.

### Gaps (G7–G12)

**G7 — No coverage metric.** The pipeline never computes whether a required
identifier is present in the corpus it was given, in a form that would catch a
builder or pack regression. Severity: medium. Cost: low. Evidence: strong (KG-022).

**G8 — Abstention is not measured.** R6 has a grounding gate, but the
*abstention rate* is never recorded, and [S-244] shows retrieval drives it to
zero while lowering hallucination — the exact inversion the gate exists to
prevent. Severity: **high** for a compliance deliverable. Cost: low. Evidence:
strong (KG-024).

**G9 — No judge noise floor is reported.** §4.1 is the finding: seeding
establishes sampler determinism, not judge forward-pass determinism, and no run
reports a test–retest figure. Until it does, any future A/B scored by the L3
judge measures the rubric. Severity: high. Cost: low. Evidence: strong (KG-024,
[S-241]).

**G10 — Citation resolution is asserted by rule but never measured at both
levels.** Rule R2 forbids unresolvable anchors, and the CHECKS enforce it, but
no run reports the *rate* at context level versus answer level — and [S-242]
shows reporting one of those inverts the ranking. Severity: medium. Cost: low.
Evidence: strong.

**G11 — The T6 debt has no tool.** The single query the graph exists to answer
has no interface, so the ADR-011 deferral has no completion criterion. Severity:
medium. Cost: low (a deterministic builder plus a traversal). Evidence: strong
on the need, **absent on the tooling** — no published source addresses
anchor-provenance analysis specifically, which is a small original
contribution available here.

**G12 — The evidence chain is never checked for retention under the pack
budget.** Every metric in the pipeline is single-goal or single-step, and
[S-223]/[S-242] identify the failure mode where a bounded context silently
breaks multi-hop evidence while every local metric stays clean. Severity: medium.
Cost: low. Evidence: strong.

**Gaps G1–G6 from the earlier mapping are unchanged**; the KG survey neither
re-scopes nor closes any of them. In particular **G1 (schema-constrained
decoding) is reinforced rather than replaced**: [S-216] measures the same effect
the pipeline is missing — 12% of queries fail to execute at all without grammar
constraint, 2% with it — and adds the decomposition (lexing buys validity,
guards buy accuracy) that should shape E-01's implementation.

---

## 6. Honest notes

- **The strongest evidence is about systems we are not building.** Much of this
  survey concerns LLM-extracted graphs over unstructured text, which AEGIS does
  not do. The transferable material is the *measurement* literature and the
  negative results, and those are what the experiments in §1.3 use. The
  positive results mostly do not transfer, and the mapping says so rather than
  borrowing them.
- **No controlled study of a curated graph versus a pack on a regulatory corpus
  was found** — the gap the earlier review named, unchanged. This survey's
  contribution to that gap is indirect: it explains *why* the published graph
  systems fail (extraction recall) and therefore why the prior from that
  literature is not a prior about this corpus.
- **Three of the load-bearing negative results are single-team or small-team
  preprints** ([S-225] single author, n=100; [S-256]; [S-202]). They are recorded
  at the weight they deserve — prominent, with their setup caveats attached, and
  not as settled.
- **Coverage of the underlying surveys was uneven.** General web search was
  unavailable throughout all four threads, so arXiv and official documentation
  are well covered and practitioner write-ups are thin. No practitioner
  post-mortem of a failed KG deployment was found, which means every negative
  result here is academic. For a practitioner planning a first KG, that is a real
  gap in the evidence, and it is the same gap the earlier mapping recorded for the
  pipeline.
