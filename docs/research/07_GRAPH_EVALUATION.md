---
document_id: AEGIS-RES-07
title: 'Graph evaluation — metrics, judges, and the traps that invert conclusions'
version: 0.1.0
created: 2026-10-04
status: ACTIVE
survey_date: 2026-10-04
sources: 'docs/research/sources.yaml'
upstream: 'AEGIS-RES-05, AEGIS-RES-06'
---

# Graph evaluation — an annotated catalogue

**What this document is.** The catalogue for "how do we know the graph system
works?" — `KG-020`..`KG-026`. It covers benchmarks, the metrics that survive
contact with a real corpus, LLM-judge validity, determinism, cheap deterministic
proxies, and the negative results that other papers do not publish.

**Method.** Web survey, 2026-10-04. Every factual claim carries an `[S-nnn]`
token resolving into [sources.yaml](sources.yaml); verify with `python
scripts/check_research_refs.py --strict`. The literature is heavily skewed
positive, so **the negative results are given the most space** — a survey that
only finds wins is worth little to a pipeline deciding whether to build
something.

**The headline, stated up front.** *The measurement choice, not the
architecture, drove the ranking in at least two independent cases — and the
benchmarks themselves are wrong about half the time.* A defensible graph
evaluation therefore needs three things the field mostly lacks: a stated noise
floor, a coverage metric that can be computed before answering, and abstention
measured as a pair with hallucination.

---

## 1. The benchmarks are the first casualty

### KG-020 — Task-dependent strengths, and the split is clean

**Definition.** RAG and GraphRAG do not compete on a single axis; they have
**distinct task-dependent strengths**, and hybrids combine them.

**The source and the numbers.** [S-171] (KDD 2026) is the standard reference and
was read in full. With Llama-3.1-8B under a unified protocol:

| Task | RAG | Best GraphRAG | Winner |
|---|---|---|---|
| NQ (single-hop) F1 | **64.78** | 63.01 (Community-Local) | RAG |
| HotpotQA F1 | 60.04 | **63.01** (HippoRAG2) | GraphRAG |
| MultiHop-RAG overall | 67.02 | **70.27** (HippoRAG2) | GraphRAG |
| MultiHop-RAG **Null** | **96.01** | 19.27 (Community-Global) | RAG, massively |
| QMSum ROUGE-2 F1 | **6.32** | 3.23 (Community-Global) | RAG |

**Construction cost, same paper.** MultiHop-RAG: construction **135s (RAG) vs
5,560s (Community) vs 7,702s (KG-GraphRAG)**; retrieval 1,724s / 1,249s /
14,434s. And [S-230]'s per-1M-token figures: GraphRAG 1.72h and $13.19 at 22,160
context tokens per query, versus RAPTOR 1.70h and $6.38 at 814 tokens, versus
LinearRAG 0.68h and $0 at 4,600 tokens. GraphRAG's query context is **17–27×**
longer than RAPTOR's for comparable construction cost.

**The routing reading.** [S-234] (ICLR 2026) turns this into a question about
*when* rather than *whether*: "GraphRAG frequently underperforms vanilla RAG on
many real-world tasks", and the fix is a router keyed on query complexity rather
than applying graph retrieval uniformly. Its own replication of the negative
result: on Fact Retrieval, RAG-with-rerank 60.92 beats every GraphRAG method
(best GraphRAG HippoRAG2 at 60.14) on one corpus and effectively ties on the
other (64.73 vs 66.28). GraphRAG wins on Complex Reasoning, Contextual
Summarize, and Creative Generation.

**The unsolved part of the routing answer, which is worth stating plainly.** The
complexity scorer is itself a learned component with its own failure modes, and
**no source found validates a router's accuracy against gold complexity labels**.
For a practitioner, the honest position is that the decision "graph or no graph"
is currently made by a heuristic nobody has validated.

### KG-021 — The benchmarks are wrong about half the time

**Definition.** Before designing an evaluation, know the state of the ones you
might reuse.

**The audit.** [S-233] hand-evaluated over 1,000 question-answer pairs across 16
popular KGQA datasets. Per-dataset factual correctness: **WebQSP 52.00%, CWQ
49.33%, CFQ 71.67%; average across all 16 datasets = 57%.** Roughly half the
errors one would attribute to a system are in the labels. About 30 KG-RAG papers
published 2022–2025 used WebQSP and/or CWQ.

**Three specific traps.**

1. **Exact match manufactures false negatives.** For "What is the Australian
   dollar called?" gold is `AUD` and the prediction "Australian dollar" is
   scored wrong [S-233]. Exact set match systematically punishes correct answers
   whose surface form differs.
2. **Unanswerable and subjective questions sit in the gold.** "What to do today
   in Atlanta with kids?" is in WebQSP [S-233].
3. **Freebase was officially dumped in 2016**, so gold answers are checked
   against a dead graph [S-233]. [S-245] makes the general point across 25
   datasets: GrailQA "is limited to Freebase, a discontinued and outdated
   knowledge graph."

**The cost saving for a bespoke corpus.** [S-245] proposes **re-splitting**
existing datasets to expose weak splits "at near-zero cost" rather than
re-annotating. Given that hand-labelling is both expensive and — per
[S-233] — error-prone, re-splitting is the right first move. It is also the only
way to get the compositional / zero-shot generalisation split that [S-245] shows
GrailQA is the sole major benchmark to treat as first-class.

**What no benchmark has.** No benchmark simultaneously offers correct labels, a
live graph, compositional/zero-shot generalisation splits, unanswerable
questions, and multiple valid traversal paths with a gold *answer set* rather
than a gold *path*. That combination is precisely the gap a domain corpus would
fill.

**A related instability, in the scored credit itself.** [S-259]: switching only
*which derived form gets the credit* changes nDCG on **83.4–94.0% of shared
queries**, flips target orderings on Mem0 and MemoryOS transfer runs, and
reverses parser-density recommendations. The credit assignment is a
first-order measurement decision, not bookkeeping.

### KG-026 — Structural metrics are diagnostic, never normative

**Definition.** NodeCount, EdgeCount, AverageDegree, and
AverageClusteringCoefficient describe a graph's shape. They are not quality
scores.

**Why.** [S-234] defines them as *graph-quality* metrics; the problem is that they
have **no gold standard attached** and move monotonically with extraction
verbosity. Raising them is trivial. The clearest evidence that the direction is
backwards: [S-205] (KGGen) *improves* measured quality while **shrinking** the
graph — entities 4,602 → 3,573 and edges 3,180 → 2,448 at 1M characters.

**The tell that they are not quality metrics.** The field's own survey taxonomy
does not list any structural metric among its evaluation metrics — it lists EM,
F1, BERT4Score, GPT4Score, Accuracy, BLEU/ROUGE-L/METEOR, answer-coverage ratio,
relevance, diversity, and faithfulness. Their absence from the field's own
taxonomy is the evidence.

**Legitimate use.** Comparing two pipelines' graph shapes; detecting degenerate
hubs. Anything else is a scoring vector with no direction.

---

## 2. The metric that predicts failure, and the one that does not

### KG-022 — Answer-entity coverage: compute it before you query

**Definition.** The fraction of gold answer entities that actually appear in the
constructed graph. Cheap, deterministic, no judge, and *predictive* of downstream
failure.

**The measurement.** [S-171]'s appendix, which is the most important part of that
paper: only **65.8% of HotpotQA answer entities and 65.5% of NQ answer entities**
appear in the constructed KG. So on roughly a third of questions the answer is
simply not in the graph.

**Why this is the right first metric.** It is computed once, at index time, costs
no per-query tokens, requires no judge, and it *explains* the downstream results
rather than merely tracking them: the Null-query collapse (KG-020), the low
retrieval accuracy, and the incomplete-entry-point failure [S-225] names
explicitly. It is a **gate**, not a score — below a threshold nothing else is
worth measuring.

**The same failure measured as precision during a walk.** [S-242] measures
GraphRAG's graph walk filling 11–15 context slots at **context precision
0.12–0.23** — five in six retrieved chunks are off-gold — while the synthesizer
cites only 3.4–5.0 ids at **citation precision 0.48–0.65**. The graph produces a
noisy superset that the generator filters. So the graph's win is a *recall*
effect (citation recall 0.68–0.74 vs vanilla's 0.46–0.65), and the noise it
injects is paid for in context length.

**A standing contamination warning.** [S-223] documents that Freebase- and
Wikidata-based KGQA leaderboards are inflated by parametric memory — LLMs score
**above 30% by prompting alone**. Any number on those graphs overstates the
graph's contribution. This is the graph analogue of the general requirement that
a seeded run be separable from an unseeded one, and it applies to the *model* the
way seeding applies to the *sampler*.

**The structural control nobody runs.** [S-217] supplies the generalisation-gap
counterpart: 17.1% (o1-preview) on Spider 2.0 against 86.6% on Spider 1.0.
Whatever Spider 1.0 measures, it is not the same capability. A benchmark's
difficulty determines what its score means, so a coverage metric should be
reported next to any retrieval score.

### KG-035 — Link prediction is a poor proxy for QA utility

**Definition.** MRR / Hits@k over the graph's own edges do not predict whether
the graph can answer questions, and cannot detect the failure that matters.

**Why, in two steps.** First, link prediction measures the wrong target: it
asks whether a *held-out* edge can be recovered, whereas a GraphRAG system needs
to *find* an existing edge and verbalise it. A system can have perfect MRR and
fail every query by retrieving the right neighbourhood and answering the wrong
question; conversely it can have mediocre MRR — the answer edge being a
low-confidence tail prediction — and answer correctly by traversing from the
other end.

Second, and decisively, the coverage gate comes first. With 65.8% of answer
entities absent [S-171], link-prediction metrics computed over the graph's own
edge set are **structurally incapable of detecting the failure that matters
most**, because that failure is in the *discarded* material. A graph can have
excellent link-prediction metrics and be useless for QA.

**Status of this argument.** The reasoning is assembled here from [S-171]'s
coverage number plus the standard definition of link prediction; no source states
it in this form. Recorded as an inference, not a finding.

### KG-025 — Cheap deterministic proxies, and how far to trust them

**Definition.** The metrics that need no LLM and no judge, and the honest state of
evidence for each.

**The instrument catalogue.** [S-237] (T2S-Metrics) is the reference, offering
over 20 metrics across six dimensions: lexical (token-level P/R/F1, BLEU, ROUGE,
METEOR, CodeBLEU, SP-BLEU, SP-F1), structural/URI exact match, **answer-set
based** (F1-QALD, Jaccard), ranking (MRR, NDCG, P@k, Hit@k), and LLM-as-judge. It
states the motivation precisely: n-gram metrics "penalize valid SPARQL queries
that" are semantically equivalent via different surface forms (FILTER vs
VALUES), and query correctness "cannot be assessed independently of" the graph.

**Ranked by cost and predictive value:**

1. **Execution / answer-set match against gold.** Cheapest, fully deterministic,
   the field's own primary metric. Failure modes: the 57% label-error rate
   [S-233] and EM's false negatives. Mitigation: relaxed / denotation matching.
2. **Gold answer-entity coverage in the graph** (KG-022). Deterministic, computed
   once, no per-query cost, predictive. Strongest cost/benefit ratio found.
3. **Typed missingness perturbations with paired ΔF1** — the protocol from
   [S-238] (MissDiag): hold question and gold fixed, apply structurally typed
   interventions (Random, Source-context, Relation-level, **Answer-adjacent**) at
   severity α ∈ {0.1, 0.3, 0.5}, and report paired per-system deltas. At α=0.3,
   Qwen2.5-7B exact-F1 degradation: Random 11.1, Source 3.0, Relation 7.4,
   **Answer-adjacent 21.3**. Four system families, 1,050 items.
4. **Citation resolution rate, at context *and* at answer level** — see KG-024
   for why reporting only one of these inverts conclusions. [S-242] provides the
   form and shows the two differ by 3–5×.
5. **Abstention rate paired with hallucination rate** (KG-024).

**The one piece of correlation evidence that licenses the cheap metrics.**
[S-238] tested it directly: switching from exact F1 to semantic F1 "changes
degradation magnitudes but not the main typed pattern". So **the choice between
cheap exact-set match and expensive semantic matching changes the numbers but not
the conclusions** — for graph robustness evaluation. That is a licence to use the
cheap metric, from a study that ran both.

**The honest limit on all of it.** No published correlation study between a
*graph-specific* deterministic proxy and human-judged answer quality was found.
What exists is: the metric catalogue [S-237], one study showing matching-rule
choice does not change diagnostic conclusions [S-238], and general evidence that
all automatic proxies are weak. [S-243] bounds how weak — classical Precision@k
and nDCG@k correlate only **0.286 and 0.141** with a human composite score on
close-ended queries, and *no* available automatic proxy exceeds 0.43. **The
correct epistemic position: deterministic proxies are well-defined and cheap;
their trustworthiness for graph QA is largely untested, with one partial
exception.**

**The default framework has no graph-native metric at all.** Ragas is the
framework this repo's registry already records ([S-074]) and the one a practitioner
would reach for first. Its published metric list ([S-246]) shows that "KG
Building" appears **only under Test Data Generation** — there is no
path-existence check, no triple-level precision/recall, no answer-set-versus-graph
comparison anywhere in it. **Evaluating a graph-retrieval system with Ragas means
measuring it with chunk-level instruments**, which is the concrete reason this
catalogue specifies its own metrics rather than composing existing ones.

**A gap worth naming as an opportunity.** There is **no packaged, published
path-existence / answer-adjacency-reachability metric** — "does a connected
subgraph of the index exist whose traversal from the question's anchors reaches
the gold answer set?" All the components are computable today with plain graph
traversal, no LLM, no judge, and [S-238]'s answer-adjacent result (ΔF1 21.3 vs
Random 11.1) says it is the measurement that matters most. For a bespoke corpus
this is the highest-value metric available and it does not exist yet.

**Also missing.** No quantification of **verbosity bias versus concreteness bias
on graph answers**, where the two documented biases point in *opposite*
directions: graph retrieval produces short entity-anchored answers, verbosity
bias favours longer ones, while concreteness bias favours fluent paragraphs with
numbers and citations over a bare triple that is *more* precisely correct. Both
push against the graph-native answer format, and no source measures the net
effect.

---

## 3. Judges

### KG-024 — Never report a single judge call

**Definition.** The practical rule, and the three failures that produce it.

**Failure 1 — judges are not deterministic even when asked to be.** [S-241]
audits a real production harness (Japan AISI's `aisev`): the grader is invoked
with temperature *and* seed unset, so the provider default of 1.0 applies; 4 of 7
items are non-reproducible over 20 runs with per-item disagreement up to ~50%.
Pinning temperature=0 fixes two and leaves 2/7 flipping. `top_p` does nothing.
**Forced greedy decoding (`top_k=1`) still leaves 1/7 flipping** — which locates
the non-determinism in the *forward pass*, not the sampler, so no sampling-side
knob reaches it. A governance note: Claude Opus 4.7/4.8 now reject temperature
outright (HTTP 400), so the conventional mitigation is being withdrawn by the
vendors while the underlying variance remains.

**Failure 2 — judges drift, so a published number is not comparable to itself
over time.** [S-242]'s most alarming result: re-judging **frozen, identical
inputs eleven weeks later** gives κ=0.138 (GPT-5.4) and κ=−0.05 (GPT-4.1)
against its own earlier verdicts — chance-level — with a +41pp leniency shift,
rejecting stationarity at binomial p<10⁻⁴⁴. Two papers eleven months apart using
the same judge and rubric may be measuring different standards. And stability on
one axis does not transfer to the other: GPT-4.1 is more stable across embedders
but *less* stable across time.

**Failure 3 — the measurement point inverts the architecture ranking.** This is
the most epistemically dangerous of the three. [S-242]: "scoring the retrieved
set as the attribution set ranks GraphRAG **last**; scoring the answer's own
citations ranks it **best or tied-best**." Not a bias result — a result that the
graph produces a noisy superset which the generator then filters. Two studies
reporting contradictory GraphRAG-versus-RAG verdicts may simply have measured at
different points. This is a very cheap thing to check and almost nobody checks it.

**The noise floor must be measured before believing any difference.**
[S-242]'s protocol: same-input same-day test–retest gives **κ=0.76, i.e. 12% of
verdicts flip on resampling alone**; re-judging after an embedder swap gives
κ=0.14 (41% flip). **Any claimed difference smaller than that floor is not a
result.** The studies that do not establish a floor — most of the graph benchmark
papers — cannot be compared to it.

**Where judges cap out.** [S-240] (RAGChecker) supplies the ceiling numbers:
best automatic metric reaches Pearson 0.62 (Overall) against a **human–human**
upper bound of 0.70 — roughly 75–86% of human inter-annotator correlation, with a
substantial gap remaining. The best general-purpose judge in [S-242]'s thread
reaches 64.29% accuracy. **Caveat for a local-model pipeline:** [S-243] shows
backbone matters enormously — Llama-3.1-8B scores Completeness/Conciseness/
Verifiableness of 0.14/0.16/0.07 against GPT-5-mini's 0.51/0.50/0.45, a 3–7×
swing from backbone choice alone. A local judge may not be able to score what the
pipeline produces, and that failure is silent.

**What to do instead of fixing the judge — replace it.** [S-239] (ARES)
fine-tunes lightweight judges on synthetic data and wraps them in
**prediction-powered inference**, giving statistically valid confidence bounds
from a few hundred human-labelled examples. Small calibrated judges with stated
bounds are more reproducible than one big judge call, and PPI makes residual
uncertainty explicit. The pattern generalises: **convert a single uncalibrated
judge call into a distribution with a stated uncertainty.**

**Abstention must be measured as a pair with hallucination.** [S-244] introduces
the dual metric, and the finding is the sharpest warning in this catalogue for a
compliance pipeline: advanced RAG lowers hallucination (65.4% vs 87.6% for naive
RAG) but drives abstention from 5.0% to **zero** — **retrieval makes the system
always answer, whether or not evidence supports it.** A system that cannot say
"the corpus does not say" is worse than one that can, and an abstention rate alone
will not reveal it. Human evaluation of 1,000 outputs at κ=0.78 found a 12.7:1
ratio of factual hallucinations to acceptable paraphrases, so surface paraphrase
is minor relative to fabrication. (Read via abstract; no claim beyond the
abstract is made from [S-244].)

### KG-034 — Global/summary retrieval destroys abstention

**Definition.** A specific, reproducible failure of the *global* (community
summary) retrieval mode: when the retrieval path is a pre-generated summary of a
whole community rather than the underlying passages, the system becomes
*structurally unable to say "the corpus does not answer this"*.

**The measurement.** [S-171], MultiHop-RAG's Null-query condition, where the
correct answer is literally "insufficient information":

| System | Null-query score |
|---|---|
| RAG | **96.01** |
| Community-GraphRAG (Global) | **19.27** |

This is not a marginal regression. A benchmark whose correct response is
abstention is answered *confidently and wrongly* by the global graph mode, four
out of five times.

**Why the mechanism is structural rather than a tuning failure.** Global search
answers by map-reducing over community reports — pre-generated summaries whose
whole purpose is to be a faithful compression of many passages at once. A summary
is, by construction, an assertion that a coherent account exists. The
fine-grained evidence that would license "nothing here supports this" has been
aggregated away before the model ever sees it, so there is nothing left to
abstain *from*. [S-236] reports the complementary effect from the same cause:
aggregation "may overemphasize high-level statements at the expense of
fine-grained details, leading to weaker performance on summarization tasks."

**The independent mechanism, from the other direction.** [S-244] finds the same
inversion in ordinary advanced RAG: hallucination falls (87.6% → 65.4%) while
**abstention falls further, from 5.0% to zero** — retrieval makes the system
always answer. Two different retrieval designs, one shared behaviour, and in both
cases the headline metric *improves* while the property a regulated system needs
gets worse.

**The operational rule.** Any system that aggregates before answering must
report abstention as a first-class metric, measured as a pair with
hallucination. Reporting either alone produces a favourable-looking number that
hides the regression. The mitigation is architectural rather than
prompt-level: keep a path from the model to the underlying verbatim evidence, so
"not supported" is a conclusion the model can reach from something it was
actually shown.

### KG-023 — The scorer is an uncontrolled variable

**Definition.** Recalled from KG-009 because it is the same defect one level up:
in evaluation, the *scorer* — not the system under test — determines published
numbers.

**The evidence.** [S-202]: no mechanical matching protocol agrees with human
reviewers more than 71%, and an LLM judge reaches 0.860; one fixed prediction set
spans F1 0.1577 to 0.6994 depending on the protocol. [S-259]: the credited target
alone changes nDCG on 83–94% of shared queries. [S-233]: the labels are wrong 43%
of the time. Three independent uncontrolled variables in the same measurement
chain.

**The rule that follows.** A graph evaluation that does not name (a) the answer
matching rule, (b) the credited form, and (c) the judge's model *and pinned
snapshot date* is not a measurement. [S-242] pinned `gpt-5.4-2026-03-05` and
`gpt-4.1-2025-04-14` and reported κ between them — that is the standard.

---

## 4. The negative results other papers do not publish

Reported in full, because the literature is skewed positive and a survey that
smooths this is misleading.

**1. GraphRAG loses on simple lookups — replicated three times independently.**
[S-171] NQ F1 64.78 vs KG-GraphRAG(triplets) 34.28. [S-234] RAG-with-rerank
beats all GraphRAG methods on fact retrieval, and cites 13.4% lower accuracy on
NQ and 16.6% on time-sensitive queries. [S-225]: an LLM-built graph scores 32
accuracy against plain Embedding-RAG's 46. The most robust negative result in the
field.

**2. Graph construction cost exceeds the benefit, and is quantified.** 5,560–7,702s
vs 135s [S-171]; $13.19 and 22,160 context tokens per 1M tokens vs RAPTOR's
$6.38 and 814 [S-230]. And [S-230] finds the gap *shrinks* with a stronger
backbone (14.70 → 9.75, and 7.80 → 7.19) — a better model buys back some of what
the graph was supposed to buy.

**3. The graph loses on summarisation once a gold reference exists.** [S-171] with
ROUGE-2/BERTScore: RAG beats Community-GraphRAG(global) on all four QFS
datasets (QMSum 6.32 vs 3.23). [S-236] independently: graph pipelines "may
overemphasize high-level statements at the expense of fine-grained details,
leading to weaker performance on summarization tasks". **This reverses [S-170]'s
headline result** — see C-01.

**4. GraphRAG fails catastrophically at abstention.** [S-171]: Null queries 19.27
(Community-Global) against RAG's 96.01, on a benchmark where the correct answer
is "insufficient information." Not a marginal regression — a qualitative safety
inversion.

**5. The claimed global-sensemaking advantage may be an artefact of reference-free
judging.** Every positive result on that task class is judge-scored on unreleased
data with no gold reference. Every *reference-based* replication finds the
opposite. **No paper was found showing GraphRAG beating vector RAG on global
sensemaking against a gold reference.** That is a load-bearing NOT FOUND.

**6. The benchmarks are benchmark-shaped.** [S-235] argues current GraphRAG
methods are "overly tailored to KGQA benchmarks, which are biased towards a few
specific question patterns"; it partially restores deterministic gold-standard
evaluation by hand-authoring Cypher for the ⟨s,p,∗⟩ patterns while acknowledging
the rest fall back to LLM judging. [S-236] finds existing benchmarks "rely on
short, curated passages, failing to adequately evaluate systems in realistic
settings involving long contexts."

**7. Hybrid gains are ~2pp, not 160%.** [S-257] measures calibrated graph+vector
fusion at **+1.9pp LastHop@10 on MuSiQue (69.1 → 71.0, p=0.041)** and **+1.9pp
LastHop@5 on 2Wiki (51.7 → 53.6, p=0.023)**. [S-258] claims +160% / +177% by
bundling vector search, GraphRAG, Leiden clustering *and* a cross-encoder
against an unstated baseline. **Two orders of magnitude apart** — which is why
KG-031 requires reading the baseline before believing any percentage in this
field.

**8. Larger context makes reasoning worse, not better.** [S-223]: o4-mini falls
from 59 correct to 5 as the graph grows 100 → 500 nodes, *while still fitting in
the context window*. [S-242] measures the same effect operationally: the graph
walk fills 11–15 context slots at context precision 0.12–0.23.

**9. The graph is incomplete at the entry point, which is what breaks traversal.**
[S-225] names it, [S-171] measures it (65.8% coverage), and [S-205] shows the
GraphRAG-constructed graph scores **0% valid triples** under hand-scoring.

---

## 5. What the survey could not establish

| Sought | Result |
|---|---|
| Correlation between a **graph-specific** deterministic proxy and human-judged quality | **NOT FOUND** — the largest genuine gap. Partial exception: [S-238]. |
| GraphRAG beating vector RAG on global sensemaking **against a gold reference** | **NOT FOUND.** Every positive result is reference-free judging. |
| Packaged path-existence / answer-adjacency-reachability metric | **NOT FOUND**, despite being the correct "does the graph carry the answer path" measure and being computable today. |
| Validation of a **complexity router's** accuracy against gold labels | **NOT FOUND.** [S-234] proposes one; nobody has checked it. |
| Quantification of verbosity vs concreteness bias on graph answers | **NOT FOUND.** The two biases point in opposite directions on this answer format. |
| Ablation separating **"graph"** from **"community-summary hierarchy"** as the source of GraphRAG's multi-hop gains | **NOT FOUND.** This is the field's central confound and it is unaddressed. |
| Whether the retrieval budget or the credited form explains a given published memory result | **NOT FOUND** as a systematic practice; [S-255] and [S-259] show it should be. |

**Coverage caveat.** General web search engines were blocked throughout the
underlying survey, so coverage of practitioner blogs and vendor engineering
write-ups is thinner than intended — the practitioner-blog layer is
under-represented. Classic pre-2020 ACL/EMNLP benchmark papers (WebQSP, GrailQA,
CWQ, CronQuestions, MetaQA) are mostly not on arXiv and their primary pages could
not be opened; they are referenced here through [S-233] and [S-245], which audited
them, rather than cited directly.
