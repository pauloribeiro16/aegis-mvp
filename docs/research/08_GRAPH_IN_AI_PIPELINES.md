---
document_id: AEGIS-RES-08
title: 'Knowledge graphs in AI pipelines — architectures, memory, provenance, and negative evidence'
version: 0.1.0
created: 2026-10-04
status: ACTIVE
survey_date: 2026-10-04
sources: 'docs/research/sources.yaml'
upstream: 'AEGIS-RES-05, AEGIS-RES-06, AEGIS-RES-07'
---

# Knowledge graphs in AI pipelines — an annotated catalogue

**What this document is.** The catalogue for "where does the graph go, and what
does it cost?" — `KG-027`..`KG-032`. Five architectural slots, graph-as-memory
with its negative results, provenance and audit, the graph as a constraint, the
security surface, and a consolidated anti-pattern list.

**Method.** Web survey, 2026-10-04. Every factual claim carries an `[S-nnn]`
token resolving into [sources.yaml](sources.yaml). Vendor claims and measured
results are separated explicitly, and the negative evidence is given the most
space — including the cases where a graph lost to a flat store under matched
budget.

**A structural finding that belongs in the summary, because it is uncomfortable.**
The literature separates the graph into five architectural slots. The dominant
*production* pattern is that **only one of them is a graph at all**, and it is
usually the least glamorous: a deterministic query tool. Where the graph is
adopted for *recall*, it repeatedly loses to a flat store. Where it is adopted for
*traceability* and *determinism*, the case is strong.

**A coverage caveat stated up front, because it shapes §2 and §3.** General web
search was unavailable in the underlying survey. The vendor-blog and
practitioner-write-up layer is therefore thinner than intended: the Neo4j,
LangChain, LlamaIndex and Zep blogs returned 404, and no practitioner
post-mortem of a failed KG deployment was found. The negative evidence below is
almost entirely academic. Where a source is a vendor's own documentation it is
marked as such rather than treated as measurement.

---

## 1. Five slots

### KG-027 — The provenance slot: the strongest case for a graph

**Definition.** Use a graph to record *where every generated claim came from*, not
to retrieve it. The graph is competing with nothing, because the alternatives —
a citation list, a log — are strictly worse for the job.

**The finding that should govern the design.** [S-248] decomposes transparency
into three **independently measured** layers — answer correctness, citation
fidelity against benchmark gold, and **per-document influence under
leave-one-resource-out intervention** — and demonstrates that they dissociate. Its
worked example surfaces "the citation-influence gap: a clean citation audit
co-occurring with a profile in which one cited source registers only weak
influence while seven uncited sources demonstrably shift the output." Numbers:
53.53% answer accuracy, 71.55% citation fidelity on 7,405 HotpotQA-distractor
examples.

**The operative rule for a regulated deployment.** *Citation presence, citation
correctness, and causal influence are three different properties, and all three
must be measured.* A clean citation audit is not evidence that any cited source
did the work.

**The strongest single mechanism, and it is a DAG rather than a knowledge
graph.** [S-247] (VeriTrail, ICLR 2026) represents a generative process as a
**directed acyclic graph where each node is a piece of text** — source,
intermediate, or final — "and each edge from node A to node B indicates that A was
used as an input to produce B." It renders a six-stage GraphRAG run as such a DAG
and, on corpora over 100K tokens with an average of 114,368 nodes, beats
AlignScore, INFUSE, RAG-as-detector, Gemini 1.5 Pro and GPT-4.1 mini.

Three design details transfer directly, and the second is the important one:

1. Claims are verified in **reverse** of generative order, walking back to source.
2. **Sentence ids are assigned programmatically and any model-returned id that
   does not match is discarded** — "This approach guarantees that the sentences
   included in the evidence trail are not hallucinated."
3. The search space narrows: only the input nodes of nodes-from-which-evidence-
   was-selected are checked.

**The product insight that follows from (3).** *Traceability and error
localisation are separate products.* A supported claim gets a path; an
unsupported one gets a **stage number** — and that stage number, not the path, is
the operationally valuable output, because it tells you which pipeline step to
fix.

**Caveats, all load-bearing.** [S-247]'s guarantee covers sentence *ids*, not the
truth of the verdicts — every verifier in this area is an LLM or an NLI model, and
**no source establishes calibrated human-grade entailment**. The tool is "research
purposes only and is not available commercially".

**Compression silently destroys provenance, measurably.** [S-249] is the warning
that should govern any context-budget decision: a RECOMP-style compressor scores
**0.86 citation precision against its own summaries but 0.12 against source
spans**, and claim verification after source recovery shows an unsupported rate
of 0.88 versus 0.17. Extractive selection grounds at 0.43–0.49. The authors'
own caveat: shared-NLI evaluator, no human calibration. The consequence is
uncomfortable and general — **token-budget decisions are simultaneously
provenance-budget decisions, and summary-level provenance metrics will look
excellent while telling you nothing.**

### KG-028 — The constraint slot: the graph reduces the expressible space

**Definition.** Use a graph not to retrieve facts but to *restrict what the
generator is allowed to produce*. This is a stronger guarantee than anything in
the retrieval lane, and it is the slot most often overlooked.

Four mechanisms, in increasing order of hardness.

**(i) Hard syntactic constraint — grammar-constrained decoding.** Output
structure becomes a guarantee rather than a hope. See KG-012 for the measurement
and the decomposition into lexing and guards. Two design elements transfer: an
*input-dependent grammar* (the grammar is a function of the input, so different
inputs can admit different output shapes — this is how a taxonomy *selects* the
output shape), and the finding that constrained LMs "substantially outperform
unconstrained LMs or even beat task-specific finetuned models."

**(ii) Soft constraint — schema restriction via graph routing.** [S-252]
(DisasterLex) inserts an Expert Knowledge Graph of curated concepts and typed
causal edges between the query and the database, with four stages: identify query
entities, route to operational domain, plan over causal edges, ground the SQL —
"restricting the schema passed to the model at each stage." The mechanism is the
point: **the graph reduces the expressible space, not merely the retrieved
space.** This is the closest published analogue to constraining a
requirements-derivation step with a regulatory taxonomy, which is the AEGIS
situation almost exactly. Honest limitation: schema restriction is only as good
as the graph's coverage, which is curated by hand.

**(iii) Rule-engine-over-graph — logical forms.** [S-250] (KAG, Ant Group) is
the only production-deployed instance found, and it is the strongest result in
this document: a *logical-form-guided hybrid reasoning engine* composes retrieval
results through rule-like forms rather than concatenating them. Its motivating
gap is stated precisely — the distance between vector similarity and the relevance
of knowledge reasoning, plus LLM insensitivity to "**numerical values, temporal
relations, expert rules**". Those three categories are what a regulatory corpus
is made of. Reported: **+19.6% F1 on 2Wiki, +33.5% on HotpotQA**, deployed in two
Ant Group domains. The architecture also uses **mutual indexing between the graph
and the original chunks**, so every node keeps a source pointer — which is KG-027
sitting inside KG-028.

**(iv) Deterministic post-hoc verification.** [S-251] (EviGraph) has a
deterministic checker establish whether a recommendation is supported, over a
temporal knowledge graph whose *state* is selected to match the query's temporal
scope.

**And the hard lesson of the slot (KG-029).**

### KG-029 — Verification can remove correct answers without improving decisions

**Definition.** Adding a checker is not a safety improvement by default. What
makes it one is a *written specification of what must be established*, which
exists before the checker does.

**The finding.** [S-251]: "Additional verification, however, can withdraw
supported recommendations without improving decision quality." The corrective is
the design principle, and it is the right spec discipline for any deterministic
gate: "reliable evidence-based navigation depends on **specifying what must be
established for a decision**, rather than simply adding more verification."

[S-251] does exactly this — it "distinguishes critical decision requirements from
information that can remain unresolved", and only the former is checked. The
design failure mode is therefore specific and nameable: **building a verifier
whose requirement set is implicit.** A verifier with no enumerated contract
either checks too little or over-rejects.

**Why this is the most transferable finding in the pipeline thread.** It is the
published counterpart to spec-first gate design in general: the requirement list
*is* the specification, and the checker is downstream of it. A checker written
before the requirement list is a guess with good test coverage.

---

## 2. Graph as memory: the weakest evidence, the strongest marketing

### KG-030 — Memory graphs: what is published, what is marketing, and what is negative

**Definition.** Persist agent state as a structured graph rather than a flat
store. The most-invested slot in the literature and the one with the weakest
evidence base.

**The published positives, in order of strength.**

- **[S-229] (HippoRAG, NeurIPS 2024)** is the load-bearing peer-reviewed result:
  up to 20% over SOTA on multi-hop QA at **10–30× lower cost and 6–13× lower
  latency** than iterative retrieval. The economic argument is strong, and it is
  about *replacing LLM turns with a symbolic operator*, which is a different
  claim from "graphs are better memory".
- **[S-253] is the cleanest positive and nobody else measured the axis**: a
  fixed-schema knowledge graph survives a swap of the model that writes into it,
  accuracy changing by **+0.0004 ± 0.0020**, while model-compressed note stores
  are highly model-coupled. This is an argument about the **write path** being
  decoupled from the reader, not about retrieval quality — and for a pipeline
  that will change models, it is the one that survives.
- **[S-212]** (from KG-006) shows small specialised agents beat larger monolithic
  models for construction, which is the write-side analogue of the same finding.

**The marketing claims, and what happens under scrutiny.**

- **Zep / Graphiti** claims DMR 94.8% vs MemGPT 93.4% — a 1.4pp margin **on a
  benchmark the competitor's own team established as their primary metric** — and
  "up to 18.5% accuracy improvement while reducing response latency by 90%".
  Independently, [S-255] finds the lead "**disappears** after controlling for
  retrieval budget" (Graphiti was spending 2.6M characters of context per query),
  and a separate measurement puts Graphiti at **76.4× more ingestion prompt
  tokens** than a speaker-indexed alternative. The *architecture* is sound and
  well-specified; the *published accuracy advantage* does not survive budget
  control, and the write path is expensive.
- **Mem0**'s own paper reports the graph as a marginal add-on: "~2% higher overall
  score than the base configuration" — at the edge of measurability given a ~1
  point effective judge resolution on a 10-point scale. The product then changed
  such that the typed relations are gone and the shipped "Graph Memory" is a
  schema-free co-occurrence graph used as a ranking boost, with the default
  open-source stack being a vector store plus SQLite, no graph database. **Anyone
  citing "Mem0 uses a knowledge graph" is citing a retracted design.**

**The three negative results that should govern the decision.**

1. **Budget-controlled, graph memory does not beat flat vector memory.**
   [S-256], matched at five retrieval roots, LongMemEval, 500 questions: token F1
   **0.417 against 0.468**, Δ = −0.050, **95% CI [−0.085, −0.016] — excludes
   zero.** The diagnostic is the most useful sentence in the memory literature:
   the deficit concentrates on questions "that require recalling a specific prior
   assistant turn, where judged correctness falls from 0.911 to 0.607, suggesting
   that **decomposing a turn into entities discards the surface form these
   questions depend on**." The generalisable form: **a graph is a lossy
   compressor for utterances whose identity is their wording.** If the query is
   about what a document literally says, a typed edge over extracted facts is the
   wrong store and verbatim text must stay reachable.
2. **The benefit is recoverable without structure.** A speaker-indexed design
   that builds *no* semantic structure — turn-granularity lexical index,
   iterative keyword search — **beats HippoRAG 2 (58.2 against 53.2)** on ~2,800
   MemoryAgentBench questions under a matched backbone.
3. **The field's own headline metric does not measure what practitioners care
   about.** LoCoMo/LongMemEval "measure question answering over dialogue history,
   **not whether remembered facts change what a tool-using agent does**."

**The failure mode nobody prices in: growth.** Holding task evidence fixed and
adding irrelevant sessions, HippoRAG stays inside its two-call budget but **loses
16–20 percentage points in budget-compliant reliability**. Crucially the
degradation is *agent-dependent* — a small model blows the budget, larger ones do
not. The correct epistemics: scalable-memory claims are conditional on agent,
interface, scale range, and interaction budget.

**The retrieval-budget lesson, which generalises past memory.** [S-255] across 8
memory systems: "the sparse-dense hybrid is the single most significant
intervention: hybrid variants of Simple RAG, Mem0, and Theoria tie for the lead
within 0.03 points." Three architectures with completely different memory designs
reach the same score once BM25 is added — so **the retrieval modality mattered
and the memory architecture did not.** The paper is emphatic that the protocol
must be reported in full: "ingestion granularity, raw-text preservation, retrieval
budget, retrieval modality, rubric audit, and judge choice all affect the
outcome."

**Leaderboards are not rankings.** [S-259]: changing only which derived form gets
credit changes nDCG on 83–94% of shared queries and flips orderings. One system
moved 44 points in one month on a public leaderboard. A viral claim of 96.6%
Recall@5 for a 47k-star project in two weeks was independently attributed to
verbatim storage plus a default embedder, with the elaborate "spatial metaphor"
reducing to ordinary vector metadata filtering.

### KG-031 — The cost ledger, and the break-even that actually decides it

**Definition.** The numbers, and the variable that determines whether a graph pays
for itself.

**Build cost.** Microsoft reports graph extraction is "**roughly 75% of
indexing cost**" and warns that indexing is expensive with a standing instruction
to "start small." Academic corroboration: cheaper constructions reach 3–11% of
output tokens for ≥80% of the accuracy, and entity-only storage reduces token
consumption by up to 94%. A vendor comparison puts full GraphRAG indexing at
roughly **1000× vector RAG** ([S-263] and the LazyGraphRAG figure of 0.1%).
Then there is the persistent maintenance tax: the docs require re-init between
minor version bumps and a migration notebook between major bumps, "which will
overwrite your configuration and prompts" — so **prompts are part of the index
state**.

**Query cost.** Root-level community summaries need **9×–43× fewer context
tokens** than map-reduce over source text [S-170] — a genuine saving, and the
reason community hierarchies exist. The cost sink is the high-degree hubs those
hierarchies create, and one independent ablation reproduces the break-even shape:
replacing retrieval-time LLM control with algorithmic exploration cut per-query
latency **over 100×** and cost **over 99%** relative to GraphRAG Global and DRIFT
at best quality.

**Context-injection cost, for completeness.** ~100 generated context tokens per
800-token chunk is a **12.5% overhead**, one-time, and only affordable via prompt
caching.

**The break-even is the decision variable.** [S-230] concludes GraphRAG "remains
advantageous for complex multi-hop reasoning, exhibiting more stable agentic
search behavior **when its offline cost is amortized**." That clause is the
decision. The question is not "is the graph better" but "does this corpus get
queried enough times, or vary enough between versions, to amortise a build that
costs 40–1000× a vector index?" For a frozen corpus queried in a small number of
audit cycles, the arithmetic is unfavourable by construction.

**The closest published negative result in a matching domain.** [S-254] reports a
GraphRAG attempt in a **regulated technical domain** that ended in a performance
inversion, where a small QLoRA fine-tuned model beat the graph-retrieval stack.
That is the closest available situation to AEGIS — a regulated corpus, a local
model, and a choice between building structure and adapting the model. **It is
registered with an explicit caveat and must be read that way:** the retrieved
abstract truncated mid-sentence at the decisive comparison, so the exact scores
are **not verified** and the direction of the inversion should be confirmed from
the paper's results section before the source is cited for anything. It is held
here because a negative result in the closest matching domain is worth knowing
even when its numbers are not yet legible.

**What the realistic hybrid win is.** **~2pp**, not 160%. [S-257] measures
calibrated graph+vector fusion at +1.9pp LastHop@10 on MuSiQue (69.1 → 71.0,
15W/5L, p=0.041, n=514) and +1.9pp LastHop@5 on 2Wiki (51.7 → 53.6, 11W/2L,
p=0.023, n=491). The mechanism generalises usefully: graph and vector scores
have different distributions and are not directly comparable, so normalising
before fusion is what makes the combination work. **Most naive hybrid
implementations are miscalibrated, which is why they underperform.**

**What the graph contributes when it contributes anything:** seed-anchored
traversal to reach bridge passages similarity misses; per-edge quality tiers as a
retrieval weight; a reranking prior over dense representations rather than a
separate channel. **What it does not contribute:** recall of the underlying
surface form ([S-256], Δ = −0.050), or a lead that survives budget control
([S-255]).

### KG-032 — The graph is an attack surface, and the write path is the boundary

**Definition.** Where an adversary goes when the graph is the retrieval substrate
but the instructions are not the target.

**The core result.** [S-262] (Oracle Poisoning) defines an attack class distinct
from prompt injection: the adversary corrupts the **data** the agent queries
rather than its instructions. Nine models, three providers, N=30/model, against a
**production 42-million-node code knowledge graph** with real SDK tool use:
**100% trust at moderate attacker sophistication, 269 of 270 trials accepting
fabricated security claims** under directed queries. Under open-ended prompts
trust falls to 3–55%, which the authors correctly report as a confound.

**Two methodological warnings that generalise to any evaluation.** There is a
**discrete attacker-skill break point where trust flips 0% → 100%**, so a study
at low sophistication will report a reassuring number that means nothing. And
**delivery mode is a first-order confound** — "GPT-5.1 shows 0% trust inline but
100% under both simulated and real agentic tool-use" — meaning **inline,
prompt-based evaluation systematically understates this class of risk.**

**The defence result.** Of five defences tested, **only read-only access control
eliminates the mutation vector**; the other four are partial and model-dependent.

**Adjacent, graph-specific poisoning.** A separate line finds that
relation-channel conflicts bypass the naive defence: malicious relations in
graph memory often fail to be extracted, merged into the target anchor
neighborhood, or retrieved for the victim query, so poisoning attacks designed
for flat text stores do not transfer — but a channel-conflict variant does.

**The general form, and it is the one to internalise.** A shared graph needs an
**authorisation layer, not a relevance layer**. Relevance-filtered retrieval does
not stop retrieving semantically-relevant-but-inappropriate content, and a graph
is no better than a vector store at that. The write path is the boundary: a
version-controlled, read-only corpus with a human review gate has no
model-writable edge, which is the one mitigation the literature found to be
complete.

---

## 3. Consolidated anti-patterns

Ranked by how much each should change a plan. The first two are the ones that
most often turn out, in hindsight, to have been the whole story.

1. **Pre-built graph structure for a query-diverse workload.** The failure mode
   is not that graphs fail — it is that *one pre-built graph cannot serve all
   query shapes*, and a graph built per query costs tokens that may not be
   available. Fragment-level extraction yields "thematically inconsistent,
   logically conflicting, and structurally fragmented graphs". Fixed
   index-time transition probabilities ignore query-dependent edge relevance, so
   random walks are "diverted into high-degree hub nodes before reaching critical
   downstream evidence", yielding "high partial recall but failure to retrieve the
   complete evidence chain". See KG-013 and KG-016.

2. **A vector-RAG baseline that is actually just bad RAG.** [S-258] claims
   +160%/+177% by bundling vector search, GraphRAG, Leiden clustering and a
   cross-encoder against an unstated baseline; the controlled ablation [S-257]
   measures **+1.9pp**. **Check the baseline before believing any percentage
   improvement in this field.** Two orders of magnitude separate a real
   measurement from a bundled one.

3. **Entity decomposition as a lossy compressor for utterances.** [S-256]:
   judged correctness 0.911 → 0.607 on questions about recalling a specific prior
   turn, "because decomposing a turn into entities discards the surface form
   these questions depend on". **If the questions are about what was said, a
   graph is the wrong store.**

4. **Optimising memory architecture when the metric is retrieval modality.**
   [S-255]: hybrid sparse+dense is the significant intervention and three
   architectures tie within 0.03 points. Spend the effort on lexical retrieval
   and reranking first.

5. **Retrieval budget as a hidden variable.** [S-255] (2.6M characters per query),
   [S-257] (score calibration), and the omission of build cost from published
   numbers. **Always read the budget before the score.**

6. **Single-hop metrics certifying a graph pipeline.** The most dangerous silent
   failure, and it has a cheap test: a graph walk can fill 11–15 context slots at
   context precision 0.12–0.23 while every single-hop metric looks fine, and
   o4-mini collapses 59 → 5 between 100 and 500 nodes. A bounded-context test
   that checks *evidence-chain retention* is the direct instrument.

7. **Spending LLM calls on write-time consolidation.** 76.4× ingestion tokens
   for one design, a no-structure design that wins outright, and — in the
   adjacent Anthropic guidance — a deliberate preference for just-in-time loading
   with prompt caching *rather* than a complex index, on the stated grounds that
   agents otherwise "waste context by misusing tools, chasing dead-ends, or
   failing to identify key information".

8. **Adding a verification layer without specifying its requirement set.**
   [S-251]: verification can withdraw supported answers without improving
   decisions. Enumerate what must be established; then write the checker.

9. **Using the retrieval lane as a security boundary.** [S-262] plus the
   manufactured-confidence line: consolidation steps can turn a hedged statement
   into a flat confident fact, and "no attacker is needed" for that outcome.
   Authorisation and provenance-preserving writes are the boundaries.

10. **Model-coupled memory.** [S-253]: compressed summaries are highly
    model-coupled; a fixed schema survives a writer swap at +0.0004 ± 0.0020. If
    the model will change, this is the argument for the typed record.

11. **Version-locked persisted indices.** [S-263]: re-init between minor bumps,
    migration between major bumps. Prompt files are index state.

12. **Adopting a leaderboard position as a ranking.** [S-259] and the 44-point
    monthly swings. There is no stable cross-paper ranking of memory systems.

13. **Ignoring agent-dependent degradation under growth.** 16–20pp of
    budget-compliant reliability lost as irrelevant sessions accumulate, and
    *whether an agent stays inside budget depends on model size*.

14. **Structured metrics as quality scores.** KG-026: no gold standard, monotonic
    in verbosity, and the direction is empirically backwards.

---

## 4. Where the graph is genuinely the right tool

Stated as a positive summary, because a catalogue that only lists failures is
unusable. On this evidence, the defensible uses are:

- **Provenance and audit** — the derivation-DAG pattern with programmatic
  sentence ids and reverse verification (KG-027), plus logical-form composition
  over an index that retains source pointers (KG-028).
- **Deterministic query** — a human-written query template with LLM-inferred
  parameters, so the query *shape* is fixed by a human and only bindings are
  generated (KG-016); schema restriction via a curated graph, which reduces the
  expressible space (KG-028).
- **Multi-hop bridge discovery** where similarity genuinely fails — seed-anchored
  traversal, under an explicit budget, calibrated against a vector channel
  (KG-031), with the expectation of ~2pp rather than a multiple.
- **Constraint and validation** — enumerated requirement sets checked
  deterministically, where the specification precedes the checker (KG-029).
- **Write-path decoupled from the model** — a typed record that survives a reader
  swap, which is a durability property rather than a retrieval one (KG-030).

And the one place this survey found the graph clearly *wrong*: as a replacement
for verbatim text when the question is about what a source literally says, under
a matched retrieval budget [S-256].

---

## 5. What the survey could not establish

| Sought | Result |
|---|---|
| Practitioner post-mortem of a **failed** KG deployment | **NOT FOUND.** All negative evidence here is academic; no practitioner voice on "we built one and it did not pay off". |
| Azure AI Search GraphRAG integration | **NOT VERIFIED** — the canonical documentation URL returns 404. |
| MCP as a graph-tool protocol | **NOT OPENED** in this pass. Graph MCP servers exist and ship an MCP server, but the protocol-as-graph-substrate question is unexplored here. |
| Blackboard architectures over a shared graph | **NOT FOUND** with strong evidence. The nearest published items are thin. |
| Head-to-head controlled comparison of **shared-graph coordination vs message passing** | **NOT FOUND.** The two bodies of work use different tasks and metrics and neither baselines the other. |
| **Write-time verification** of graph edges — what stops a wrong or malicious edge entering | **NOT FOUND.** Open, and it is the gap that KG-032's only complete mitigation leaves open. |
| Whether graph memory degrades gracefully with corpus growth *independently of the reader model* | **NOT FOUND.** Growth effects are reported as agent-dependent, so the two are confounded. |
| A production regulated deployment of claim-level entailment with published error rates | **NOT FOUND.** |

**Names to watch for collisions when following this thread.** `MetaQA` names a
widely-reused KGQA dataset that is not the arXiv paper of that name. `GRBench`
names at least two unrelated papers. `REBEL` is overloaded. These are the same
hazards recorded in [06_GRAPH_QUERY_PATTERNS.md](06_GRAPH_QUERY_PATTERNS.md) §6
and they recur because the field reuses names faster than it defines them.
