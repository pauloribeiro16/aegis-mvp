---
document_id: AEGIS-RES-06
title: 'Graph query patterns — how to make a model search a knowledge graph'
version: 0.1.0
created: 2026-10-04
status: ACTIVE
survey_date: 2026-10-04
sources: 'docs/research/sources.yaml'
upstream: 'AEGIS-RES-05'
---

# Graph query patterns — how to make a model search a knowledge graph

**What this document is.** The catalogue for the question "how do we say to the
model: go and look in the knowledge graph?" — `KG-011`..`KG-019`. It covers the
mechanics of model-driven graph retrieval: generating a query, deciding what
schema to show, reasoning over paths, the retrieval *modes*, the tool surface,
and the failure modes. It is a *reference*; the recommendation is in
[09_KG_PATTERN_MAPPING.md](09_KG_PATTERN_MAPPING.md).

**Method.** Web survey, 2026-10-04. Preference for peer-reviewed evaluation
papers with numbers over framework documentation, and for measured over claimed.
Every factual claim carries an `[S-nnn]` token resolving into
[sources.yaml](sources.yaml). Several of the strongest sources here are *negative*
results, which is itself the headline finding.

**The one-sentence answer to the section title.** *Do not make the model write a
query language; make it write a plan, give it a linearised projection of a
retrieved subgraph, and let a deterministic checker reject what cannot execute —
and never let a budget silently truncate the evidence path.*

**A caveat that shapes the whole catalogue.** General web search was unavailable
during the underlying survey; discovery ran through the arXiv API, direct
retrieval of official docs and benchmark sites, and PDF extraction. Coverage of
arXiv and vendor documentation is broad. Coverage of practitioner write-ups is
thin, and the Neo4j / LangChain / LlamaIndex / Zep blog layers were largely
inaccessible — so the *tool-surface* patterns (KG-015, KG-016) rest on
specifications and SDK documentation rather than on production post-mortems, and
that is stated where it matters.

---

## 1. The two problems that are not one problem

### KG-011 — Syntactic validity and semantic correctness are separate, with separate fixes

**Definition.** There are two independent failure modes in model-generated graph
queries: the query does not parse, and the query parses but means the wrong
thing. Treating them as one problem — "make the query better" — conflates a
grammar problem with a grounding problem.

**The measurement that separates them.** [S-216] (PICARD, EMNLP 2021): a T5-3B
baseline emits **12% of Spider dev queries that fail to execute at all**;
grammar-constrained decoding cuts that to **2%** — and the constrained model is
*simultaneously* state of the art at 75.5 exact-match / 79.3 execution accuracy
on dev. The mechanism decomposes cleanly: incremental **lexing** removes most of
the invalid-query problem; semantic **guards** (e.g. an alias-alias pattern that
must resolve to a real table) buy the extra accuracy. Constrained decoding is
therefore not a robustness patch — it *is* an accuracy mechanism, because an
invalid query is an unreachable answer. Cost: 2.5s → 3.1s per sample at beam 4 on
an A100, about 24%.

**The production reference concedes the same gap.** [S-218] (Neo4j's
`Text2CypherRetriever`): "The LLM-generated query is not guaranteed to be
syntactically correct. In case it can't be executed, a `Text2CypherRetrievalError`
is raised." Notably, the vendor's default is to treat this as a **hard error for
the caller to handle**, not as a self-correction opportunity. That is a design
decision worth copying or consciously rejecting, not inheriting by default.

**Where the difficulty actually lives: the query language's surface area.**
[S-224] documents where the grammar bites. The construct that makes graph queries
tractable for a model is **property paths**, which express arbitrary-length
traversal in one compact expression instead of N nested optional joins the model
will get wrong. If a pipeline hand-writes the traversal — as a template, per
KG-016 — this whole problem class disappears.

**Second, independent mechanism: generate then resolve.** [S-231] (ChatKBQA)
inverts the order: emit a logical form whose entities and relations may be wrong,
then replace them with ground-truth graph identifiers using an unsupervised
retriever. No grammar is needed at all — only a resolver over canonical IDs. This
is the cheapest of the patterns in this section to adopt and the one most likely
to fit a pipeline whose graph is a small, fixed, canonical set.

### KG-012 — Constrained decoding for a query language

**Definition.** Compile a formal grammar to a decoding-time mask so that emitted
output is structurally valid by construction, rather than repairing invalid output
after the fact.

**Sources.** [S-216] is the reference measurement (12% → 2% unexecutable, SOTA
alongside it). The pipeline's own gap analysis records the same finding from the
opposite direction: post-hoc parse-and-retry is the anti-pattern, and the repair
loop is the most expensive failure path in the pipeline.

**What transfers beyond queries.** Two design elements from [S-216] generalise to
any structured output: *lexing* (reject at the token level, fail fast) separates
most of the validity win from the semantic win, and *guards* (predicate checks
against the actual schema) are what buy accuracy beyond validity. A structured
output layer that has only the first is a formatting fix; one with both is a
quality mechanism.

**A caveat the pipeline's own gap analysis already carries.** Format constraints
remove the *format* failure mode, not the *truncation* failure mode — a response
cut off mid-object can still be schema-valid. And strict format constraints can
cost reasoning quality; the mitigation that survives is to keep a reasoning field
alongside the constrained one.

---

## 2. What to show the model: the schema question

### KG-013 — Schema grounding is a precondition; retrieval past that has diminishing returns

**Definition.** How the graph schema reaches the model is the single largest
controllable factor in query quality — but only up to a point, after which the
bottleneck moves to reasoning.

**The strongest evidence, and it is stark.** [S-215] (KnowledgeNLP 2025), with
open-weight backbones only (Mixtral 8x7B, Llama-3 70B, CodeLlama 70B) across
QALD-9/10, LC-QUAD 2.0 and QALD-9 DB. **A plain question with no entity or
relation grounding scores F1 0.08 / 0.02 / 12.00 / 16.42** across the four
benchmarks. Not degraded — collapsed. Dynamic few-shot with entity-and-relation-
encoded demonstration retrieval (DFSL) lifts the same backbones to
**76.59 / 57.69 / 85.45 / 75.14**. The ablation is the load-bearing part:
removing relations from the retrieval key costs **16.12 F1** on QALD-9 DB;
removing entities costs **18.52**; removing both costs **25.55** on QALD-9 Plus.
Even with *no* schema information at all, dynamic demonstrations still beat the
plain-question baseline by 33+ and 25+ F1 — so retrieval and grounding are
partly substitutable but strongly complementary.

**The decision-theoretic form of subgraph selection.** [S-224] casts "which part
of the graph do I show the model" as **Prize-Collecting Steiner Tree** — a
budgeted optimisation in which every omitted node or edge costs and the model's
own answer scores the prize terms. That is a principled answer to top-k
sampling. The paper also names why the naive alternative fails: linearising a
large graph "results in an excessive number of tokens, surpassing the input
capacity of many LLMs", and truncating "leads to loss of information".

**The other side, and it is the more important half.** [S-223] (GraphWalk, J.P.
Morgan) ran the cleanest test of the whole premise. Its **no-tool baseline is fed
the complete 100-node graph in context** — exhaustive schema, *zero* retrieval
error — and models still fail, "suggesting that the core challenge lies in the
reasoning step itself, not retrieval quality." The scalability result is sharper
still: **o4-mini collapses from 59 correct answers at 100 nodes to 5 at 500
nodes, despite the graph still fitting in the context window.** A retrieval system
with 100% subgraph recall still failed, because a longer linearised context
degrades reasoning even when nothing is missing.

**The reconciled claim, which is weaker and more useful than either side.** Schema
grounding is a *precondition* for non-trivial performance (0.08 F1 → 76 F1), and
beyond that, better retrieval has diminishing returns while the binding
constraint becomes the model's ability to execute multi-step traversal over
whatever it is shown. The two regimes are not on one axis. *Why* long linearised
graph context degrades reasoning — attention dilution, position bias, or task
interference — is **not established** in any source found.

**Corroboration from an adjacent field.** [S-217] (Spider 2.0, ICLR 2025 Oral)
supplies the generalisation-gap number for schema-supplied query generation over
realistic schemas: **o1-preview solves 17.1%** of 632 enterprise tasks (databases
over 1,000 columns, SQL often over 100 lines) against **86.6% on Spider 1.0**.
Even *with* ground-truth tables supplied, o1-preview reaches only 12.60% — so
about 7 points come from schema access and the rest is lost to exploration and
multi-step reasoning. The same shape as [S-223]: schema access necessary, nowhere
near sufficient.

---

## 3. How to express the search

### KG-014 — Emit a plan, not a query

**Definition.** Have the model produce a *declarative traversal plan* — a
sequence of relations, or a partial logical form — which is then grounded against
the actual graph before execution, rather than a finished query in a query
language.

**The strongest form.** [S-220] (Reasoning on Graphs, ICLR 2024): the model emits
a **relation path in a special token format** (`<PATH> r1 <SEP> r2 <SEP> </PATH>`),
beam search top-3, and those relation names are used to query the graph for
valid paths *before any reasoning happens*. That ordering is the point: the plan
becomes falsifiable against the schema prior to execution, so a plan that names a
non-existent relation fails at the grounding step rather than returning a
confidently wrong empty result. Results: +4.4% Hits@1 over DECAF on WebQSP;
+22.3% Hits@1 / +14.4% F1 over UniKGQA on CWQ.

**The transferable result is the plug-and-play property.** Attaching [S-220]'s
planner to *frozen* models lifted Hits@1 by **8.5% (ChatGPT), 15.3%
(Alpaca/LLaMA2), 119.3% (Flan-T5)** without retraining any of them. (The paper's
sentence names four models and gives three deltas — an apparent typo in the
original, reported rather than silently reconciled.) For a pipeline that must not
train, this is the decisive property: the planner is a separate, swappable
component.

**The zero-grammar variant.** [S-231] (ChatKBQA) is the minimal version — generate
the logical form, then resolve its entity and relation slots to canonical IDs.
For a graph with a small fixed vocabulary of identifiers, this needs no grammar,
no query language, and no schema dump beyond an ID list.

### KG-015 — A tool surface, not a query language

**Definition.** Expose traversal to the model as a small set of orthogonal
operations it calls in a loop, rather than as text it must render into a query
language.

**Sources.** [S-223] states the thesis directly: "GraphWalk equips the LLM with a
minimal set of orthogonal graph operations sufficient to traverse any graph
structure", explicitly *not* encoding domain knowledge into specialised tools.
[S-219] (StructGPT, EMNLP 2023) is the invoking-linearization-generation loop —
the model emits a Python-like API call, the host executes it and returns a
**linearised projection** for the next turn, and the loop repeats until an answer
is emitted. On WebQSP zero-shot it lifts GPT-3.5 by +11.4% Hits@1; on MetaQA
1/2/3-hop 71.9/94.4/59.5 zero-shot, rising to 71.0/97.1/**93.5** with few-shot
exemplars — the 3-hop jump is the multi-hop payoff, and few-shot exemplars are
what produce it. The design point that matters for a controlled pipeline: **the
model never sees raw graph structure, only a linearised projection of what the
interface returns.**

[S-222] (KG-Agent, ACL 2025) is the third independent implementation of the same
bet, and the cheapest to adopt: express the multi-hop traversal in a *programming
language* rather than a graph query language, then synthesise a code-based SFT
set. 10K synthesised samples tuning LLaMA-7B outperforms methods using larger LLMs
or more data, in- and out-of-domain.

**On MCP as the transport.** The protocol is a standard for exposing tools, not
for querying graphs, and the graph ecosystem on it is second-order. The launch
shipped pre-built servers for Google Drive, Slack, GitHub, Git, **Postgres** and
Puppeteer — **no graph database at launch**. [S-261] measures the shape of what
followed: of 116 official servers analysed, **88.6% are REST-backed and 92%
implement tools as bare API wrappers**, and the **median server exposes only 19%
of available operations**. Two readings: the "semantically-designed graph tool"
thesis is aspiration rather than description; and the 19% median is evidence *for*
deliberate curation and *against* exposing a whole graph API.

**The error channel is the design surface.** [S-260] (MCP tools spec) separates
**protocol errors** (unknown tool, invalid arguments, JSON-RPC `-32602`) from
**in-band tool execution errors** (`isError: true` with readable content). For a
graph query tool this distinction is load-bearing: a malformed query is an
execution error the model can read and correct from, whereas a `-32602` is a shape
failure it frequently retries verbatim. The spec's own guidance is to
prompt-engineer error responses to give "specific and actionable improvements,
rather than opaque error codes or tracebacks" — and this repo's existing repair
loop already reuses the parser's error message as a repair prompt, which is the
right shape.

### KG-016 — Mode selection: route by question type, and prefer the template

**Definition.** Graph retrieval has distinct modes for distinct question classes;
the mode is chosen by the question, not by the system.

**The taxonomy.** [S-226] (GraphRAG query-engine docs) gives the canonical five:
**Local** (entity-specific), **Global** (whole-dataset sensemaking, map-reduce
over community reports), **DRIFT** (hybrid, recursive), **Basic** (plain vector
RAG), and **Question Generation**. Two things are worth stealing. First, Basic
Search is honestly framed as a *control*, not a product: "GraphRAG includes a
rudimentary implementation of basic vector RAG to make it easy to compare
different search results based on the type of question you are asking." Second,
the intended routing is **by question type** — Local for "What are the healing
properties of chamomile?", Global for "What are the most significant values of
the herbs mentioned in this notebook?"

**The most prompt-centric mechanism, and the best model of a self-limiting
search.** [S-227] (DRIFT docs): a **Primer** compares the query against the top-K
community reports and produces a broad answer *plus generated follow-up
questions*; **Follow-Up** feeds those into local search recursively; the output
is a ranked hierarchy of Q&A. Each node carries a **confidence value the algorithm
uses to decide whether to continue expanding** — the model is its own stopping
rule, with configurable model, context_builder, config, tokenizer for budget
tracking, and query_state. The confidence-glyph design is directly transferable
to a pipeline that must not fan out unboundedly.

**The safe variant, and it is the one to prefer for a controlled pipeline.**
[LlamaIndex's `PropertyGraphIndex`](https://docs.llamaindex.ai/en/stable/module_guides/indexing/lpg_index_guide/)
offers both `TextToCypherRetriever` (the model writes the query) and
**`CypherTemplateRetriever`** — a human-written query template whose parameters
are inferred by the LLM, so the *query shape is fixed by a human* and only the
bindings are generated. [S-218] exposes the analogous Neo4j surface. The template
form is the one that makes KG-011's validity problem structurally unreachable,
because the model is never in a position to produce an invalid query — only a
valid one with wrong parameters, which is a different and much cheaper failure.

**On the "just build a bigger graph" reflex.** [S-263] and the GraphRAG docs
carry the operational cost, and [S-230] shows a stronger backbone erodes the
graph's advantage: the GraphRAG-minus-dense gap **shrinks from 14.70 to 9.75**
going from a 3B to a 7B model under RL training, and from **7.80 to 7.19**
training-free from 7B to 32B. A better model buys back some of what the graph was
supposed to buy.

---

## 4. Reasoning over the result

### KG-017 — Interleave retrieval and reasoning, and price the depth

**Definition.** Alternate between querying the graph and reasoning about the
result, letting the model prune branches — with an explicit, acknowledged cost.

**Sources.** [S-221] (Think-on-Graph, ICLR 2024) is the reference: beam search
*over the graph* with depth = width = 3, temperature 0.4 for exploration and 0
for reasoning, 5-shot, 256 max generated tokens. Training-free. GPT-4 reaches
82.6% WebQSP, 81.4% GrailQA (SOTA at the time), 69.5% CWQ; with ChatGPT, +39.3%
on GrailQA and +25.8% average over CoT.

**The result that matters for a regulated corpus.** [S-221]'s error analysis: on
GrailQA it cuts **hallucination and refusal-to-answer errors by 50% and 60%**
versus IO/CoT prompting. Grounding the reasoning in retrieved paths does not only
improve answers; it measurably reduces the two failure modes a compliance
pipeline cannot tolerate.

**The cost, stated rather than hidden.** "Considering the computational cost
(which increases exponentially with depth), we set both depth and width to 3."
No source in the survey gives the accuracy-versus-depth curve with token costs —
**the frontier is uncharacterised**.

**The ablation that identifies the lever.** Replacing the LLM's relevance
judgement with BM25 or SentenceBERT costs **8.4% (CWQ) / 15.1% (WebQSP)**. So
search *quality* is the lever, not the search *algorithm* — which means a better
retriever, not a better index structure, is what buys accuracy here.

**Non-chain questions.** Chain-structured retrieval fails on branching and
conjunctive questions. [PDRR](https://arxiv.org/abs/2505.14099) (AAAI 2026)
adds a Predict → Decompose → Retrieve → Reason layer that explicitly handles
them: "Chain-based KG-RAG methods … are limited to simple chain-structured
questions due to the absence of planning and logical structuring."

### KG-033 — Context window and chunk size are measured design variables, not defaults

**Definition.** Two parameters that are usually set by habit were measured, and
both ablations point the same way: **smaller is better**, and the reason is
recall rather than cost.

**The measurements.** [S-170], read in full, reports two ablations that transfer
to any extraction-and-retrieval pipeline:

- **Context window: 8k beat 16k / 32k / 64k.** Not a cost saving — a quality
  win at the smaller setting.
- **Extraction chunk size: 600-token chunks extracted roughly 2× more entity
  references than 2,400-token chunks** (GPT-4, HotpotQA). The paper's own
  framing of the trade-off is that chunk size is "a fundamental design
  decision: longer text chunks require fewer LLM calls for such extraction
  (which reduces cost) but suffer from degraded recall of information that
  appears early in the chunk."

**Why this sits next to KG-013 and not next to cost.** The mechanism is
recall, and it is the same mechanism [S-171] measures from the other side — a
graph that is missing a third of the answer entities cannot be rescued at query
time. The two findings compose into one rule: **budget the extraction pass for
recall, then budget the query pass for concision, and never spend the second
budget to buy back what the first one lost.**

**The counterweight.** [S-223] shows there is a floor on how far "smaller is
better" goes: an over-truncated linearised graph is worse than a complete one,
because a longer context degrades reasoning even when nothing is missing. The
optimum is not the smallest setting; it is the point where extraction recall
stops falling while context length is still short enough to reason over. No
source gives that point for a regulatory corpus, which is why the pack budget is
an experiment here (E-15) rather than an adopted constant.

### KG-018 — Replace LLM turns with a symbolic traversal operator

**Definition.** Where a multi-hop path can be found by a graph algorithm, use the
graph algorithm and spend the saved turns on reasoning.

**Source.** [S-229] (HippoRAG, NeurIPS 2024) is the strongest argument in the
survey that agentic graph-search loops do work a graph algorithm should do: LLM +
graph + **Personalized PageRank** reaches up to 20% improvement over SOTA
multi-hop QA while being **10–30× cheaper and 6–13× faster** than iterative
retrieval such as IRCoT.

**Why this suits a local-model pipeline.** The saving is not only tokens — it is
turns, and turns are latency on a single local model. A symbolic traversal step
(PPR, bounded BFS) is deterministic, auditable, and free of the compounding
reliability loss described in KG-019.

### KG-019 — Depth, false success, and the scoring artefacts

**Definition.** The failure modes of model-driven graph search, and the reason
published tool-loop numbers are only as trustworthy as their scoring rule.

**Compounding loss.** [S-260]'s general point plus the measurement in
[S-262]'s sibling thread: by depth 6 a model retains only ~**70% of its own
clean-context capability**. Any deep-loop number is therefore a claim about a
degraded regime.

**False success — the most serious finding, and it is graph-specific.**
[S-262] (Oracle Poisoning) corrupts the *data* an agent queries rather than its
instructions: nine models, three providers, N=30/model, against a **production
42-million-node code knowledge graph** with real SDK tool use. **100% trust at
moderate attacker sophistication, 269 of 270 trials accepting fabricated security
claims** under directed queries. Two methodological warnings: there is a
**discrete attacker-skill break point where trust flips 0% → 100%**, and
**delivery mode is a first-order confound** — "GPT-5.1 shows 0% trust inline but
100% under both simulated and real agentic tool-use" — so inline, prompt-based
evaluation *systematically understates* the risk. Of five defences tested, **only
read-only access control eliminates the mutation vector**; the other four are
partial and model-dependent.

**Measurement artefacts.** Under exact-match scoring against a fixed gold
trajectory, error-propagation severity and recovery are **not estimable** — they
are fixed by the scoring rule, because post-divergence gold values depend on tool
constants the model never observes — yet a naive fit still reports "0.92 and 0.73
for a quantity that is exactly 1.000". A related study finds failures under tool
hazards are driven "less by tool-use volume or inference budget than by limited
hazard diagnosis and ineffective recovery", and that **targeted recovery hints
beat test-time scaling**.

**Self-correction: works with environmental feedback, fails without.** The
literature converges on a reconciled position. [S-232] (MAGIC, AAAI 2025) shows a
self-correction *guideline* auto-generated from a model's own observed failures
**outperforms human-written guidelines**, and improves the interpretability of
corrections. Against that, BIRD's own team reports that "LLMs always struggle with
self-correction due to self-enhancement bias, a problem particularly pronounced in
SQL generation where declarative syntax and concise logs would provide limited
guidance." The reconciliation: **self-correction works when the loop receives real
environmental feedback — execution results, retrieved paths, validator output —
and fails when it asks the model to critique its own text.** For a graph pipeline
this is a design instruction: the loop must be closed against a *checker*, not
against a second opinion.

---

## 5. Curated versus LLM-built: the variable that decides it

### KG-036 — Curation, not graph-ness, is what buys the gain

**Definition.** Two comparable sources point in opposite directions, and the
contrast — not either result — is the finding.

**The LLM-built result (negative).** [S-225] builds a graph from raw web snippets
and traverses it. On ComplexWebQuestions, 100 dev questions: **EM 19 / F1 25 /
accuracy 32, against plain Embedding-RAG at EM 28 / F1 37 / accuracy 46.** The
graph pipeline is *worse* on answer quality, and far behind leaderboard baselines
(human 63 EM, best machine 33.2 EM). Its single win is **faithfulness:
hallucination 15% versus 30%, roughly halved.** The paper names its own failure
mode: starting nodes are missed whenever the evidence span containing the answer
was filtered out, so **the graph is incomplete at the entry point** and traversal
never begins correctly. *Setup caveats stated so the negative result is not
over-read: n=100, 11 questions discarded, single author, arXiv preprint, not
peer-reviewed.*

**The curated result (positive).** [S-173] (Soman et al., Bioinformatics 2024)
uses SPOKE, a hand-curated biomedical knowledge graph, as the retrieval substrate
for Llama-2-13b / GPT-3.5 / GPT-4: **>50% token reduction with no accuracy loss**,
**+71% for Llama-2-13b** on a challenging biomedical MCQ benchmark, gains on the
larger models too, plus per-claim provenance with statistical evidence. The
mechanism: "minimal graph schema for context extraction" plus embedding-based
context pruning.

**The reading that follows.** *The graph's value is bounded by its completeness
at the entry point.* A curated graph is complete by construction, so retrieval
from it is reliable and cheap. An LLM-extracted graph inherits the recall of its
extraction and filtering steps, and a single missing anchor node fails the whole
traversal — which is exactly why [S-225] halves hallucination (it constrains
generation to what the graph contains) while losing accuracy (the answer often
is not in the graph and the model cannot fall back).

**How far this can be pushed, honestly.** This is a *synthesis of two papers*,
not a claim either makes, and the two are not commensurable — different domains,
tasks, graph sizes, metric definitions, and vastly different publication standing
(peer-reviewed journal versus single-author preprint on 100 questions). **A
head-to-head study isolating curation — same benchmark, same model, same retrieval
algorithm, graph curated versus LLM-built — was NOT FOUND.** That is the most
obvious missing experiment in the area.

### KG-037 — Hybrid wins; graph-only loses

**Definition.** In a real corpus, the combination of graph and text retrieval
beats either alone, and graph-only underperforms.

**Sources.** [S-200] compares four architectures on 3,300 CTI QA pairs: vector
RAG, graph-only over a CTI knowledge graph, an agentic variant that **repairs
failed graph queries**, and hybrid graph+text. Hybrid improves multi-hop answer
quality by **up to 35%** over vector RAG while "maintaining more reliable
performance than graph-only systems". The agentic-repair arm is the tell: it
concedes that graph queries fail, which is a realistic statement about the
substrate. [S-199] gives a clean controlled comparison — same report, same
generation instructions, same model, only the retrieval step differing — and
finds the graph plan kept firing at **100% of detections after every IP,
domain and file hash in an APT28 report was rotated, where Naive RAG kept firing
at 29%**, repeated across nine real reports from four vendors.

**Two caveats [S-199] states in its own abstract, which must travel with the
number.** "Even when the two systems end up close on total score", and "the
wording of the generation prompt matters almost as much as the retrieval
back-end itself" — a direct prompt-confound warning that qualifies the headline.

---

## 6. What the survey could not establish

| Sought | Result |
|---|---|
| Head-to-head study isolating **curation** as the variable (same benchmark, graph curated vs LLM-built) | **NOT FOUND.** The most obvious missing experiment in the field (KG-036). |
| Standardised benchmark for graph **query generation** per se | **NOT FOUND.** Spider 2.0 and BIRD are relational SQL; the Cypher/SPARQL literature has no equivalent. |
| Any official Neo4j text-to-Cypher accuracy figure | **NOT FOUND** — the benchmarking page is JS-gated. No figure is claimed. |
| Why long linearised graph context degrades reasoning | **NOT ESTABLISHED.** Attention dilution, position bias, task interference — none demonstrated. |
| Accuracy-versus-depth curve for iterative graph search, with token costs | **NOT FOUND.** [S-221] fixes depth 3 as a compute compromise and stops. |
| Practitioner post-mortem of a *failed* KG deployment | **NOT FOUND.** All negative evidence here is academic. |
| Whether WebQSP/GrailQA-class KGQA results are contaminated by parametric memory | **NOT MEASURED**, but [S-223] reports LLMs scoring above 30% on those graphs by prompting alone, which is a direct inflation warning. |

**Names to watch for collisions.** `REBEL` is overloaded (relation-extraction
model [S-209] versus an unrelated 2026 preprint). `GRBench` names at least two
unrelated papers, one a database-systems benchmark and one an LLM
graph-reasoning benchmark. `MetaQA` names a widely-reused KGQA dataset that is
*not* the arXiv paper of that name. `crawl4ai` is **not** a graph tool — it is a
web crawler producing LLM-ready Markdown, relevant only as the upstream text
acquisition layer.
