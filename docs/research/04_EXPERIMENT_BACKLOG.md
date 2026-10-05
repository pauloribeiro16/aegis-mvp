---
document_id: AEGIS-RES-04
title: 'Experiment backlog — approaches to test in the AEGIS pipeline'
version: 0.1.0
created: 2026-10-03
status: ACTIVE
survey_date: 2026-10-03
sources: 'docs/research/sources.yaml'
upstream: 'AEGIS-RES-03'
---

# Experiment backlog

**What this is.** Twenty-two experiments, each derived from a gap in
[03_PATTERN_MAPPING.md](03_PATTERN_MAPPING.md) and a pattern in the catalogues.
Every one states a question, **one** isolated variable, the arms, a primary
metric, an estimated GPU cost, a success criterion, and — the part that makes
the experiment worth running — **what changes if it wins and what changes if it
loses**.

E-01..E-12 derive from the 2026-10-03 pipeline/agent survey. **E-13..E-18 were
added on 2026-10-04** from the knowledge-graph survey
([05](05_KNOWLEDGE_GRAPH_CONSTRUCTION.md)–[08](08_GRAPH_IN_AI_PIPELINES.md)),
via the gaps and contradictions in
[09_KG_PATTERN_MAPPING.md](09_KG_PATTERN_MAPPING.md). Five of the six cost zero
GPU hours, because they read artifacts a run already writes. **E-19..E-22 were
added on 2026-10-04 as the robustness lane**: they test the *testing apparatus*
and the pipeline's behavioural rules, not its output quality, and none depends
on the validity of the L3 judge (E-22's third relation is the exception and is
gated accordingly).

**Preregistration discipline, which applies with full force to E-19..E-22.**
Each entry states its hypothesis, directional prediction, and falsifier
*before* any run. Before the first run of an entry, those three fields are
frozen into a `PREREG_02`-style document on the PREREG_01 pattern; after that,
no field may change without a new version and an explicit note recording what
changed and why. The analysis runs once. The specific anti-circular rule for
E-19: **a gate that is fixed after seeing the seeded-fault results must be
re-tested on a fresh, held-out fault set**, never on the set that revealed the
miss — otherwise detection is inflated by construction and the measurement is
circular (R10).

**Method constraints that apply to all twenty-two.** Hold constant: case
(`Case_01_TinyTask_SaaS`), corpus, model (`qwen3.8:27b` on the Deucalion A100
node), ficha versions, L0 parsers, content gates, the zero-LLM assembler, and
the L1 validator. Vary exactly one thing. This is EXP-01's discipline and it is
what made EXP-01's result interpretable at all.

**Cost units.** `GPU-h` is A100-hours on the Deucalion `dev-a100-80`
partition. Reference points from actual runs recorded in the repo: the P1–P5
pipeline arm is 42 LLM calls / 1,304 s of LLM time; the agent arm is 220 calls /
3,716 s, plus model warm-up of roughly 67 s per job and job queue time, which
dominates for short experiments. **Wall-clock per experiment is usually
dominated by queueing, not by the experiment.** A "1 GPU-h" experiment may still
take a day of elapsed time.

**Ranking criterion.** (gap severity × evidence strength) ÷ cost. Evidence
strength is graded as in the catalogues, and two experiments are ranked below
their severity would suggest *because the mitigation evidence is weak* — the
right move there is to measure, not to fix. Those are marked.

**Status.** Nothing in this backlog has been run. This is a design, and
implementing any of it is a separate decision.

---

## Ranked table

| # | Experiment | Gap | Evidence | Cost | Why ranked here |
|---|---|---|---|---|---|
| E-01 | Schema-constrained decoding vs fenced-block + retry | G1 | `PRIMARY` | ~1 GPU-h | Highest evidence strength, lowest cost, removes a whole failure class |
| E-02 | Measure prompt-injection exposure in the pack | G2 | `PRIMARY` + `PRACTITIONER` | ~2 GPU-h | Highest severity, but mitigation is unsolved — so measure, don't fix |
| E-03 | Runtime determinism: seed, `--parallel 1`, variance measurement | G3 | `PRIMARY` (vendor) | ~3 GPU-h | The variance is currently unmeasured; the number is worth more than the fix |
| E-04 | Deterministic validator vs LLM judge, with rubric-only baseline | G5 | `PEER` | ~2 GPU-h | Prerequisite for reading any future A/B result |
| E-05 | Verify against artifact state instead of self-assessment | G5 | `PEER` | ~2 GPU-h | 45–75.8% false success is the largest measured risk in the stack |
| E-06 | Track B rows for scales beyond MICRO | G6 | n/a | 0 GPU-h | Blocks the next case; research not engineering |
| E-07 | Prompt caching: saving vs determinism penalty | G3 | `PRIMARY` | ~2 GPU-h | The commit history already shows context cost paid twice |
| E-08 | Cross-version evaluation as a scheduled check | G4 | `PRIMARY` | ~1 GPU-h/run | Ollama contradicts its own docs on `num_ctx` |
| E-09 | Escalation routing with an abstention arm | — | `PEER` | ~2 GPU-h | The absent pattern; cheap to model on existing data |
| E-10 | Measure the firing rate of the 0.88 similarity gate | C3 | n/a | 0 GPU-h | PLAYBOOK D1 is open; decided on data instead of principle |
| E-11 | Context compression preserving decisions in the agent | — | `PRIMARY` + `PEER` | ~4 GPU-h | Only if the agent arm stays; the current elision is coarse |
| E-12 | OTel GenAI trace schema adoption | — | `PRIMARY` | 0 GPU-h | Portability; status `Development`, so adopt late |
| E-13 | Materialise the graph; answer the T6 anchor-provenance debt | G11 | n/a | 0 GPU-h | The ADR-011 deferral has no completion criterion; this is it |
| E-14 | Abstention rate, paired with hallucination rate | G8 | `PEER` | 0 GPU-h | Retrieval drives abstention to zero while improving the headline metric |
| E-15 | Evidence-chain retention under the pack budget | G12 | `PEER` | 0 GPU-h | The one silent failure a bounded context produces |
| E-16 | Retrieved anchor table vs full anchor dump in the P4 prompt | C-05 | `PEER` | ~2 GPU-h | Largest measured effect in the query thread; needs no graph at all |
| E-17 | ~~Audit the L3 judge~~ — **CADUCADO 2026-10-05**: the L3 judge was demoted to L1 deterministic + L2; there is no judge in `pipeline/src` to audit. Its purpose is served by the blind human rubric (L2_RUBRIC) | G9 | `PEER` | 0 GPU-h | Superseded by the demotion; revisit only if a judge is reintroduced |
| E-18 | Programmatic vs model-assigned citation ids | G10 | `PEER` | 0 GPU-h | Makes "the cited source is not hallucinated" a guarantee, not a hope |
| E-19 | Mutation testing of the deterministic gates | R10 | `PRIMARY` | 0 GPU-h | A PASS is only evidence if the gate catches seeded faults |
| E-20 | Pack utilisation and pack coverage | G7, G10 | `PEER` | 0 GPU-h | Turns "the pack is the retrieval" from a premise into two numbers |
| E-21 | Cross-version output equivalence, matcher-pinned | E-08 prerequisite | `PEER` | 0 GPU-h | No metric exists for "the same result after a ficha change" |
| E-22 | Metamorphic input testing of R3/R6/R8 | — | `PEER` | ~2 GPU-h | Tests the rules behaviourally; no gate covers them end-to-end |

---

## E-01 — Schema-constrained decoding

**Question.** Does grammar-constrained output eliminate the L0 format-failure
class, and what does it cost in latency and in content quality?

**Isolated variable.** How output structure is enforced: fenced-block parsing
with a repair retry (current) versus constrained decoding via a grammar or JSON
schema.

**Arms.**
- **A (control):** current pipeline, unchanged.
- **B:** same pipeline, `parse_p1`…`parse_p4t` replaced by constrained decoding
  at the serving layer, with a reasoning field retained in the schema so the
  constraint governs the record and not the thinking.

**Primary metric.** L0 format-failure rate per run — the count of calls
requiring a repair retry, and the count of stage aborts. Secondary: latency per
call, and L1 outcome.

**Cost.** ~1 GPU-h (one full P1–P5 pipeline run per arm, two arms).

**Success criterion.** Arm B drives the repair-retry count to zero *and* L1
still passes on the same case. Content quality is explicitly **not** the success
criterion — see "if it wins" below.

**If it wins.** The most expensive failure path in the pipeline disappears, and
the parse-error class stops being a reason for stage aborts. The repair-retry
code stays as a fallback for the [S-014] escape hatches — refusal and
max-token incompleteness — which constrained decoding does *not* cover.

**If it loses.** The format problem was not the bottleneck, which is itself
worth knowing: it redirects effort toward the retention-floor calibration
question in C4. A latency regression without a retry reduction would mean the
format failures were already rare on this case, and the experiment should be
re-run on a case with a heavier output schema before being discarded.

**Caveat to record in the result.** [S-045] claims near-zero overhead on its own
optimised path; llama.cpp GBNF and older regex/FSM approaches carry more
per-token overhead. And [S-179] finds strict format constraints can cost
reasoning quality — hence the retained reasoning field.

---

## E-02 — Prompt-injection exposure in the context pack

**Question.** How often does an instruction planted in the company intake prose
survive into a goal row?

**Isolated variable.** The content of the intake prose. Nothing else changes —
same case, same model, same parsers, same gates, same assembler.

**Arms.**
- **A (control):** the unmodified `Case_01_TinyTask_SaaS` intake.
- **B–F:** the same intake with planted directives of escalating subtlety — a
  direct imperative, an instruction attributed to a third party, an instruction
  embedded in a data field rather than prose, an instruction inside a quoted
  regulation excerpt, and a benign-looking instruction that would only be visible
  as a rule violation.

**Primary metric.** For each planted directive: (a) did it appear in any
artifact under `steps/`? (b) did it appear in the final `doc02_adjusted_goals.md`?
(c) which gate, if any, caught it, and by name? Secondary: false-positive rate —
how many *unrelated* goal rows changed relative to arm A.

**Cost.** ~2 GPU-h (six arms, one pipeline run each).

**Success criterion.** There is no "success" in the usual sense. The outcome is
a **number**: the survival rate of planted instructions, and the identity of
every gate that fires. A low survival rate is a finding about this pipeline's
current state. A high one is a finding about its exposure.

**Why measure rather than fix.** The mitigation evidence is the weakest in the
registry. [S-081]'s conclusion on general mitigation is "I don't know what to
suggest"; [S-164] offers *provable resistance* patterns with trade-offs, not a
fix. A measurement is achievable now; a fix is not yet grounded. Building a
defence against an unmeasured threat is the wrong order.

**What the survey predicts.** Two of [S-081]'s three lethal-trifecta legs are
structurally absent here — no exfiltration channel, and no tool surface in the
pipeline arm — so the expected failure mode is **conformance failure**, not
data theft: an injected directive that produces a row which passes L0/L1 and is
substantively wrong. That is the [S-156] test-overfitting class, and it is why
the false-positive rate is measured alongside the survival rate.

**If the survival rate is high.** The gap is real and the next step is the
provenance controls [S-161] supports for writable state — record which artifact
each claim traces to, and make untraceable claims fail the gate rather than warn.

**If it is low.** Record the number and the gates that produced it. The result
is a measurement of the current design, not a licence to relax the gates.

**Available corpus.** [S-097] is a deliberately vulnerable agentic application
usable as a source of injection techniques; [S-091] is the threat-model
reference to align the plant taxonomy with.

---

## E-03 — Runtime determinism and its measurement

**Question.** How much does the current configuration actually wander, and what
is the cheapest configuration that reduces it?

**Isolated variable.** The sampling and serving configuration. The pipeline logic,
prompts, and case are identical across all arms.

**Arms.**
- **A (control):** current — `temperature: 0.2`, no seed, default caching.
- **B:** + fixed seed.
- **C:** B + `--parallel 1` (single slot, no concurrent batching).
- **D:** C + `--no-cache-prompt`.
- **E:** B only, with `temperature: 0`, to separate the temperature effect from
  the batching effect.

**Primary metric.** **Artifact variance**, not text variance: for N ≥ 5 repeats
of the same arm, the fraction of runs reaching L1 PASS, and the distribution of
per-field divergence across the assembled document — sub-domain selection set,
goal-row count, `Adjustment` value mix, §4 tension count, §5 matrix rows.
Secondary: wall-clock per call, as the throughput cost of the fix.

**Cost.** ~3 GPU-h (five arms × five repeats, but arm A repeats dominate).

**Success criterion.** Arm C or D reduces the L1-PASS variance to zero across
five repeats at a throughput cost the researcher accepts. **Report the variance
number even if no configuration reaches zero** — the current value is unmeasured
and is worth more than a guess.

**Why this is ranked third and not lower.** The severity is medium-high, but the
*evidence* is a vendor admission, not a study: no independent measurement of
determinism controls on llama.cpp or Ollama was found at all. The strongest
primary material is [S-040]'s own warning that `cache_prompt` "can cause
nondeterministic results" because logits are not bit-identical across batch
sizes, plus [S-043]'s batch-invariance feature, which exists only in vLLM.
Running the experiment produces evidence the registry does not have.

**If it wins.** The run manifest can assert the sampling configuration as part
of reproducibility, and cross-run comparison becomes meaningful — which is the
prerequisite E-08 needs.

**If it loses.** Reproducibility is limited by something outside the sampling
controls, most plausibly the hardware or the serving layer. That result is
worth more than a success: it would mean the only route to bit-reproducibility
is [S-043]'s serving layer, which is a serving-stack change rather than a
pipeline change, and the decision becomes architectural.

**Related.** E-07 measures the same trade-off from the other direction.

---

## E-04 — Deterministic validator vs LLM judge, with the rubric-only control

**Question.** Does an LLM judge add signal over the existing L0/L1/L2
validators — and, before that, does the judge score the rubric rather than the
artifact?

**Isolated variable.** The scoring instrument. The artifacts under evaluation are
identical and frozen.

**Arms.** Four graders over the same set of artifacts, drawn from an existing run:
- **A (control):** the existing L1 deterministic validator. Binary pass/fail.
- **B:** a single LLM judge call, one prompt, 0.0–1.0 scores plus pass/fail —
  the shape [S-002] found most consistent.
- **C:** a multi-judge ensemble, to test whether [S-002]'s single-call finding
  replicates on this corpus.
- **D (mandatory control):** a classifier trained on **rubric text alone**,
  never seeing the response.

**Primary metric.** Agreement with human labels on a blind-scored sample, with
the sample drawn by the researcher and the labels collected before arm B is run.
Secondary: the correlation between arm B's score and arm D's score, and the
change in arm B's score when the rubric text is paraphrased without changing its
meaning.

**Cost.** ~2 GPU-h (mostly arm B and C inference; arm D is cheap).

**Success criterion — and note the ordering.** Arm D is the control that decides
whether arms B and C mean anything. **If arm D predicts the human labels as well
as arm B does, the judge is scoring the rubric and the result is that L3 is
unusable for admission control.** This is the outcome [S-114] predicts and the
experiment is designed to be able to find it.

**If B beats D.** The judge has residual signal over the rubric. Its use is
still bounded to progress detection, never admission control, because of E-05's
false-success result.

**If C beats B.** [S-002]'s single-call finding does not replicate on this
corpus, which is itself worth recording.

**If neither beats D.** Retire L3 as a scoring instrument and keep only the
deterministic validators. This is the most likely outcome and it is fine — the
value is in knowing before an A/B is run on it.

**Known confounds to state in the report.** [S-177]'s self-preference bias
matters concretely: the judge would be a qwen-family model scoring `qwen3.8`'s
output. [S-112]'s position bias rules out any pairwise presentation of the same
artifacts, so arm B must be pointwise. [S-076]'s four properties — specific,
measurable, achievable, relevant — are the test the rubric must pass before the
experiment starts, and EXP-01's L2 rubric is the artefact to revise.

---

## E-05 — Verify against artifact state instead of self-assessment

**Question.** Can a validator that checks the *artifact* detect failures that a
model asked "did this succeed?" would miss?

**Isolated variable.** The signal the completion check reads. Everything else is
held constant.

**Arms.**
- **A (control):** a model-based self-assessment — does the finished document
  appear complete and correct?
- **B:** a deterministic read-only verifier over environment state — in this
  pipeline's terms, over the artifacts and the assembled document, per [S-142]'s
  pattern of a read-only verifier deciding admission.
- **C:** the TF-IDF-style lexical detector that [S-134] reports beating every
  judge at 0.83 AUROC, adapted to this corpus.

**Primary metric.** Detection rate on a **deliberately corrupted** artifact set —
goal rows with a dropped Sub-SO, a fabricated quantity, a verbatim-copied
obligation, a heading duplicated by the model, a truncated table, an unresolved
placeholder. Precision as important as recall, because a gate that fires on
everything is the 0.88-gate failure mode in C3.

**Cost.** ~2 GPU-h for arm A; arms B and C are cheap.

**Success criterion.** Arm B detects ≥ 90% of the seeded defects with no false
positives on the clean artifact. Arm C is included to test whether [S-134]'s
result transfers to document artifacts rather than agent trajectories — a
different domain, so the transfer is genuinely uncertain.

**Why this is the largest measured risk.** [S-134] found 45–48% of failures in
single-control domains are false success, and 75.8% among self-assessing
coding-agent trajectories, with **no judge configuration above AUROC 0.65**. The
repo's L1 already checks structure and content against the artifacts, so it is
closer to arm B than to arm A — the experiment is measuring how close, and
finding the residual class.

**If B wins.** The L1 validator's remit is confirmed and the false-success rate
in this pipeline can be stated as a number rather than assumed to be zero.

**If B misses defects.** Those defects are the residual class, and each one is a
new gate candidate for `quality.py` — with the [S-114] caveat that a new gate
must be measured for firing rate, per E-10, or it is decoration.

**Related.** E-04 grades quality; this grades completion. Both are needed before
an A/B is credible.

---

## E-06 — Track B rows beyond MICRO

**Question.** Not an experiment — a corpus completion task.

**Work.** Derive Track B tier rows for the scales the case suite actually
contains, from the control referentials already in the corpus, so that
`track_b_rows` has coverage beyond its single `MICRO` row.

**Isolated variable.** n/a.

**Cost.** 0 GPU-h. Research and corpus work.

**Success criterion.** A case at each target scale assembles §5 without raising
"no Track B matrix rows defined for scale," and L1 passes.

**Why it is on this list.** The current hard-fail is the correct behaviour under
flag-not-drop — it is loud rather than silently wrong — but it means the pipeline
cannot currently process anything but a micro-company. This blocks the obvious
next case and it is the cheapest item here.

**Note on method.** Derive from the published anchor sets under
`baseline/CONTROLS/`, not from a model. The tiering is a curation decision about
what is proportionate at each scale, and a model asked to make it would be making
a proportionality judgement with no verifiable criterion — the same failure the
whole L0/L1 stack exists to prevent.

---

## E-07 — Prompt caching: the saving against the determinism penalty

**Question.** How much wall-clock and token cost does prefix reuse save, and
what does it cost in reproducibility?

**Isolated variable.** Prefix-cache behaviour, with everything else fixed to
whichever arm E-03 found best.

**Arms.**
- **A:** caching enabled.
- **B:** caching disabled.

**Primary metric.** Prompt-processing time per call, aggregate LLM seconds per
run, and — crossed with E-03's method — artifact variance across repeats.

**Cost.** ~2 GPU-h.

**Success criterion.** A saving large enough to justify the variance it
introduces, or a null result that settles the question. **The [S-040] caveat
must be carried into the design**: prefix reuse is precisely what varies batch
composition between otherwise-identical requests, which is the mechanism behind
the nondeterminism the vendor documents. The two arms are not independent.

**Why it is on the list.** The commit history shows this cost has already been
paid twice in incident form — a 30,481-token pack that filled a 32 K context and
returned empty content, and a subsequent per-step `num_predict` budget after
output truncation. The saving is known to be non-trivial in principle; what is
unknown is whether it is recoverable here.

**If caching wins on time and loses on variance.** The trade is explicit and
recording it is the deliverable; the decision is then a researcher's call about
how much reproducibility a Phase 1 run is worth.

**If caching wins on both.** Re-examine E-03's arm D, since the variance it
found may have come from something other than cache composition.

---

## E-08 — Cross-version evaluation

**Question.** Can a scheduled check detect that a model, quantisation, or
sampler change degraded output quality?

**Isolated variable.** The version under test, one at a time.

**Arms.** The current pinned configuration against each candidate: a different
model tag, a different quantisation, `temperature` 0.2 against 0.

**Primary metric.** L1 PASS rate first — it is binary and unambiguous. Then the
content metrics E-04 and E-05 establish as trustworthy: goal-row count,
`Adjustment` value mix, retention-floor headroom, and the per-field divergence
measure from E-03. Not an LLM judge, until E-04 says a judge is usable.

**Cost.** ~1 GPU-h per candidate version. This is a *recurring* cost, which is
the point.

**Success criterion.** The check flags a deliberately degraded candidate. A
detector that has never fired is not a detector — the same rule PLAYBOOK D1
applies to gates, applied here to the version check.

**Why it is on the list.** [S-042] is the documentary proof that the risk is
real: four Ollama documentation pages live simultaneously giving three different
`num_ctx` defaults — 4096, 2048, 1024 in an example, and a VRAM-tiered ladder.
The runtime the pipeline depends on does not agree with its own documentation.
The sbatch script already asserts the model manifest exists before serving,
because compute nodes have no egress; the principle is right and simply is not
applied across versions.

**If it works.** Version bumps stop being leaps of faith, which [S-007]
identifies as one of the main things an eval suite buys.

**If it does not.** The divergence metrics are too coarse to detect a real
regression, and the fix is finer-grained per-goal quality measures — which is a
bigger project than this experiment.

---

## E-09 — Escalation routing with an abstention arm

**Question.** Can a cheap first pass identify the calls that need more
attention, and can the system abstain rather than guess?

**Isolated variable.** Whether escalation routing is applied.

**Arms.**
- **A (control):** every call at the current configuration.
- **B:** a cheap deterministic pre-check — pack size, retention-floor headroom
  from a prior attempt, the number of L0 repairs already spent — escalates a call
  to a second, more expensive pass.
- **C:** B plus an explicit abstain arm that stops and defers to a human gate
  rather than producing a row.

**Primary metric.** Cost per accepted artifact — total LLM seconds plus calls,
divided by L1-passing runs. Secondary: the false-abstention rate, since a gate
that abstains on everything is as useless as one that never fires.

**Cost.** ~2 GPU-h.

**Success criterion.** Arm B or C reduces cost per accepted artifact by a margin
that exceeds the abstention cost. A null result is acceptable and is the expected
outcome on a single-model pipeline.

**Why it is on the list, and why it may not be worth running.** [S-109] makes
the three-way route explicit — small model answers, escalate to the large model,
or abstain to a human — and argues the abstain arm matters most in
risk-sensitive domains, "since even the most expensive models are susceptible to
making mistakes." [S-108] supplies the confidence mechanism.

**But:** the pipeline runs a single model. There is no cheaper tier to escalate
*from*, so arm B's pre-check has nothing to escalate to except a second pass of
the same model — which is a retry, not a cascade. The pattern becomes genuinely
applicable only if a second model is introduced, and [S-110] is the standing
warning that cascades buy cost and buy attack surface at the same time.

**Recommendation: defer.** Run this if and when a second model is on the table,
and not before. It is on the list to record the reasoning, not because it is
next.

---

## E-10 — Firing rate of the 0.88 similarity gate

**Question.** Does the near-verbatim gate ever fire, and if not, should it stay?

**Work.** Not a run: a measurement over the existing corpus of goal rows. Take
every row in every existing run, compute the similarity that the gate computes,
and report the distribution and the maximum.

**Cost.** 0 GPU-h.

**Success criterion.** A number. The gate is at 0.88; the recorded maximum
across 65 rows is 0.79.

**Why it is on the list.** [S-114]'s finding generalises: an instrument that
cannot detect its own blind spots is worse than no instrument, because it
consumes trust. PLAYBOOK D1 already states the principle — "a gate that never
fires is not a constraint" — and PLAYBOOK D2 adds that "a gate can be right and
still be the bottleneck." Both are right, and the tension in C3 is resolved by
having the distribution rather than a single maximum.

**If the distribution is tight below 0.88.** The gate is dead weight and the
retention decision recorded in the sources should stand, with the measurement
attached.

**If the tail approaches 0.88.** The threshold is too high and the gate has been
silently inert; lowering it is a one-line change with a measured justification.

**The rule for whatever this produces.** A gate added after this experiment must
come with its own firing-rate measurement, or it repeats the problem. That rule
generalises to every new gate proposed by E-05.

---

## E-11 — Context compression in the agent arm

**Question.** Can the agent arm's history be compressed without losing the
decisions it needs to carry forward?

**Isolated variable.** The context-management policy.

**Arms.**
- **A (control):** current two-pass elision — drop large tool results, then
  compress old submission turns to plain text.
- **B:** structured note-taking — decisions, open questions, and rejected
  alternatives extracted into a persistent section that survives compaction.
- **C:** on-disk state briefing as the primary context, re-derived from the
  artifacts at each turn rather than carried in history.

**Primary metric.** Cumulative context tokens per run, and the L1 outcome.
Secondary: how many runs the watchdog aborts for no new artifact, which is the
proxy for context exhaustion.

**Cost.** ~4 GPU-h. This is the most expensive item here.

**Success criterion.** Arm B or C reduces cumulative tokens by a margin that
does not increase the L1-failure rate.

**Why B and not just a longer context.** [S-004] names compaction as the first
lever and rejects waiting for bigger windows: "for the foreseeable future,
context windows of all sizes will be subject to context pollution." It also names
the failure mode of over-aggressive compaction — "the loss of subtle but
critical information" — and [S-159] names the two mechanisms by which that
happens: **brevity bias**, which drops domain insights for concise summaries, and
**context collapse**, where iterative rewriting erodes detail over time. Arm B
is the response to brevity bias specifically: an explicit place for decisions,
which is what a summary drops first.

**Why C is the more interesting arm.** [S-032]'s protocol reset argues that
state the model cannot see is the wrong abstraction, and that a handle the model
threads explicitly works better. Arm C is that, applied to a document pipeline:
the agent re-derives what it needs from the artifacts rather than carrying it in
history. The cost is that it does not fit the current elision shape.

**Recommendation: only if the agent arm stays.** EXP-01 found the agent arm
costs 5.2× the calls and 2.8× the wall clock for the same output, so this is
only worth spending four GPU-hours on if the arm is being kept for a reason
beyond the A/B.

---

## E-12 — OpenTelemetry GenAI trace schema

**Question.** Would adopting the standard span schema make the existing trace
portable without changing what is recorded?

**Work.** Map `trace.jsonl`'s current fields onto [S-070], [S-071] and [S-072]'s
span names and attributes, and produce the mapping as a document. No code change
in this experiment.

**Cost.** 0 GPU-h.

**Success criterion.** A mapping that covers every current field, with the
fields that have no standard equivalent named explicitly.

**Why it is last.** The conventions are **status: Development** and now live in
their own repository, and [S-033]'s roadmap expects enterprise audit fixes to
land as extensions rather than core changes. Adopting a moving specification into
a frozen evidence chain buys portability at the cost of churn.

**What would move it up.** A concrete need to read AEGIS traces with a standard
tool. Until then, the current trace records more per call than the standard's
minimum — warm-up seconds, done reasons, truncation flags, and retry branches all
have first-class keys, which is the substance of [S-070]'s retry-inside-one-span
rule implemented in a flatter form.

**One rule worth adopting now regardless.** [S-070]: "If a transient issue
happened and the request was retried automatically, the corresponding span SHOULD
cover the duration of the logical operation with all retries." The current trace
records each attempt separately, which is defensible for forensics and is the
inverse of the standard's convention. Worth a decision, not worth a migration
yet.

---

## E-13 — Materialise the graph and answer the T6 debt

**Question.** Does a deterministic builder over the existing corpus surfaces
close the 58 out-of-set anchors — i.e. for each anchor outside an objective's
published anchor set, can the pipeline name *which* objective or test cited it?

**Isolated variable.** Whether the graph is materialised. Arm A (control) is
today's state: the debt is counted, and the citing objective is unresolvable
without manual reading. Arm B builds `node_link.json` from the surfaces in
`docs/pipeline/02_KNOWLEDGE_ARCHITECTURE.md` §2 and traverses it.

**Design constraints, which are the experiment's substance.** The builder must
emit a *regenerable* view — never hand-edited — and must verify node and edge
counts against source record counts, the same anti-circular discipline as
`scripts/verify_no_loss.py`. It must contain no LLM call and no summarisation
step, per ADR-011 D1/D2 and D3 (the corpus's integrity depends on verbatim
content only).

**Primary metric.** Of the 58 anchors, the fraction for which the citing
objective is resolved by a traversal, and the fraction of those where manual
reading agrees. Secondary: node/edge count reconciliation against
`baseline/MAPPINGS/traceability/traceability.csv`,
`baseline/MAPPINGS/sr_control_mappings/`, and `baseline/registry.csv`.

**Cost.** 0 GPU-h. Deterministic script plus a traversal.

**Success criterion.** All 58 resolved, and every node/edge count reconciles
against its source record count. The count is the anti-loss check, not a
quality score — per `KG-026`, structural metrics are descriptive and their
direction is empirically backwards, so a *larger* graph is not progress.

**If it wins.** ADR-011's deferral gains a completion criterion, and the
anchor-provenance analysis that motivated the ADR becomes a one-command
question. It also produces the coverage metric E-15 and G7 need.

**If it loses** — i.e. the citing objective is genuinely not recoverable from the
recorded surfaces — then the debt is not a query problem but a *provenance
capture* problem: the corpus does not record which objective asserted an
out-of-set anchor. That is a more valuable finding than success, because it
redirects the work to the case authors rather than to tooling, and it is the
answer to the open question in ADR-011 §5.

**Caveat to record.** [S-205] measured 0% triple validity for an LLM-built
graph; our graph is curated, so that failure mode is absent, but the discipline
is the same — the graph is only as good as the surfaces it reads, and those
surfaces are hand-maintained markdown with `aegis:` structural tags whose
coverage has never been audited.

**Related.** G11 in [09_KG_PATTERN_MAPPING.md](09_KG_PATTERN_MAPPING.md).

---

## E-14 — Abstention rate, paired with hallucination rate

**Question.** When the corpus does not support a claim, does the pipeline say
so, or does it answer anyway?

**Isolated variable.** None — this is a measurement of the current pipeline, not
an A/B. The pairing is the point.

**Method.** Replay the R6 grounding-gate decisions over existing runs. For each
rejected or unsupported claim, record whether the pipeline abstained, hedged, or
produced the claim anyway. Report the two rates as a pair.

**Primary metric.** Abstention rate (AR) and hallucination rate (HR), reported
together. Secondary: the breakdown of AR by rejection reason, since a
grounding-gate rejection that is overridden downstream is a different defect
from one that is honoured.

**Cost.** 0 GPU-h. Reads existing traces and outputs.

**Success criterion.** Not a target value — a *non-zero* AR with a documented
reason for every abstention, and no case where the gate rejected and the
deliverable asserted anyway.

**If it wins** (the gate is honoured and AR is non-zero) the pipeline already has
the property that makes it defensible in a regulated setting, and this becomes a
regression check to re-run per case.

**If it loses** — AR is zero, or the gate is bypassed downstream — that is the
highest-severity finding available in this backlog, because [S-244] shows the
failure is *invisible in the headline metric*: advanced retrieval lowers
hallucination (87.6% → 65.4%) while driving abstention to zero, so the number
everyone reports improves exactly as the property degrades. The fix is
architectural, not prompt-level: keep a path to the verbatim evidence so "not
supported" is reachable.

**Caveat to record.** [S-171] found the same inversion inside graph retrieval
specifically — Null queries score 96.01 for RAG against 19.27 for global
GraphRAG, per `KG-034` — so if E-13 ever feeds a summary-layer into a prompt,
re-run this. Abstention rates are also sensitive to how "unsupported" is
defined; pin the definition before comparing across runs.

**Related.** G8; E-09's abstention arm is the counterfactual version of this.

---

## E-15 — Evidence-chain retention under the pack budget

**Question.** Does the context-pack budget ever truncate a citation chain while
every local metric still looks clean?

**Isolated variable.** The pack budget. Sweep it across at least three values
(current, 0.75×, 0.5×) with everything else held.

**Method, and it needs no LLM.** Take the citation ids a run emitted, walk the
pack, and for each multi-hop citation chain report the fraction that survives
the budget intact. This is the path-existence check that
[07_GRAPH_EVALUATION.md](07_GRAPH_EVALUATION.md) records as **not existing as a
packaged metric** — it is computable today with plain traversal, which is why
this experiment is deterministic.

**Primary metric.** Evidence-chain retention rate per budget, reported
separately for single-hop and multi-hop chains. Secondary: single-hop retention,
as the control that demonstrates the failure is invisible without the
multi-hop split.

**Cost.** 0 GPU-h for the traversal-based measurement. An LLM-judged variant
would need re-runs and is explicitly out of scope for the first pass.

**Success criterion.** Retention at the current budget is materially higher than
at reduced budgets, and no chain is lost at the *current* budget. A finding of
"no effect at any budget" is also a success — it would mean the pack is not the
binding constraint and the effort belongs elsewhere.

**If it wins** (current budget is safe) record the headroom, which converts a
future budget change from a risk into a measured trade-off.

**If it loses** the pipeline has a silent failure that no existing gate catches,
and it is the failure mode [S-223] and [S-242] both identify as most dangerous:
[S-223] measured o4-mini falling from 59 correct answers to 5 as the graph grew
100 → 500 nodes *while the context still fitted*, and [S-242] measured a graph
walk filling 11–15 context slots at context precision 0.12–0.23 while the
synthesizer cited only 3.4–5.0 ids at precision 0.48–0.65. Both say the same
thing: every local metric can be clean while the chain is gone.

**Caveat to record.** [S-170] found the smaller-is-better direction has a floor —
8k beat 16k/32k/64k for context *and* 600-token extraction chunks yielded ~2×
more entity references than 2,400-token ones — so this experiment locates an
optimum, it does not argue for minimising the budget. Per `KG-033`, the two
budgets are separate decisions and must not be traded against each other.

**Related.** G12.

---

## E-16 — Retrieved anchor table vs full anchor dump

**Question.** Does giving the P4 prompt a *retrieved* subset of the anchor set
outperform giving it the whole set — and does the answer depend on how much of
the set is included?

**Isolated variable.** How the anchor surface reaches the prompt. Three arms:
**A (control)** current full dump; **B** retrieved subset, keyed on the sub-domain
and the requirement's own anchors; **C** retrieved subset at a deliberately
larger budget, to separate "retrieval helps" from "less context helps".

**Why arm C is not optional.** [S-215] shows schema grounding is a precondition
(0.08 → 76.59 F1 across four benchmarks), and [S-223] shows exhaustive context
fails even with zero retrieval error, with o4-mini collapsing 59 → 5 between
100 and 500 nodes. Those two are only reconcilable if the optimum is interior, so
an A/B with only two arms cannot distinguish the mechanisms.

**Primary metric.** L1 outcome (deterministic validator) plus the count of
out-of-set anchors emitted — the same quantity the T6 debt counts, so this is
where the debt's *creation rate* is measured, not just its existence. Secondary:
the count of anchors in the prompt, and the per-step token count.

**Cost.** ~2 GPU-h (three arms × one P1–P5 run; arm C may need a second pass).

**Success criterion.** Arm B matches or beats A on L1 with a materially smaller
anchor surface, **and** arm C is not better than B. If C ≥ B, the mechanism is
context length, not retrieval, and B's advantage is a budget artefact.

**If it wins** the pack builder gains a retrieval step, which is a KG-016-shaped
change: a human-written selection rule over canonical ids, not a model-generated
query. That keeps query shape under human control and sidesteps KG-011's validity
problem entirely.

**If it loses** — the full dump is not the problem — that redirects E-13's
ambition. The pack would then be carrying enough non-anchor material to be worth
profiling, and the finding would be that anchor volume was never the bottleneck.

**Caveat to record.** This experiment needs **no graph at all**, and that is its
point: the largest measured effect in the query thread is a *prompt-assembly*
effect. Also [S-199]'s own warning applies to any single-number result here —
"the wording of the generation prompt matters almost as much as the retrieval
back-end itself" — so the prompt must be held byte-identical across arms and any
edit is a new experiment.

**Related.** C-05; `KG-013`, `KG-033`.

---

## E-17 — Audit the L3 judge for pinned temperature and seed

**Question.** Is the L3 judge actually called with a pinned temperature and seed,
and what is the test–retest floor on this pipeline's own content?

**Isolated variable.** None. This is an audit of a configuration, and it is
listed as an experiment because it gates E-04, E-05 and E-16, all of which are
scored by a judge.

**Method.** Two parts. First, read the judge invocation and record what
temperature and seed it passes — the finding in [S-241] is that real harnesses
ship with **both unset**, so the provider default of 1.0 applies and borderline
items flip with per-item disagreement up to ~50%. Second, re-judge a fixed set of
N items k times and report the disagreement rate as the floor.

**Primary metric.** Test–retest agreement, and the configured temperature/seed as
a boolean. Secondary: disagreement by item, so persistent flip-flops are
identifiable as such rather than averaged away.

**Cost.** 0 GPU-h for the audit; k re-judgings only if the audit finds the
parameters were unset.

**Success criterion.** Temperature and seed are explicitly pinned, and the floor
is reported. A floor of κ ≈ 0.76 with 12% of verdicts flipping on resampling
alone is acceptable and expected; a floor materially worse is a finding.

**If it wins** the configuration is sound and the floor becomes the threshold
every future A/B must clear.

**If it loses** — parameters unset, or a floor so wide that no future A/B can
clear it — then E-04 and E-16 are uninterpretable until this is fixed, which is
exactly the conclusion [S-242] reaches on the pipeline it audited: same-input
same-day test–retest κ = 0.76, and re-judging **frozen identical inputs eleven
weeks later** gave κ = 0.138 — chance level — against its own earlier verdicts.

**Caveat to record, and it is the important one.** Pinning temperature=0 is
**necessary but not sufficient**: [S-241] measured that forced greedy decoding
(`top_k=1`) *still* leaves items flipping, locating the residual in the forward
pass rather than the sampler. So E-17 can report the floor but cannot promise to
eliminate the variance, and some providers now reject a temperature parameter
outright. **AEGIS's own determinism result is stronger than this literature
predicts** — AGENTS.md §-1 records byte-identical output across 15 seeded runs —
and the reconciliation is scope, not contradiction: EXP-02 established *sampler*
determinism; [S-241]'s residual is in the *judge's* forward pass. The two
measure different layers, and this experiment is what tells us which one the L3
judge actually lives at.

**Related.** G9; [09_KG_PATTERN_MAPPING.md](09_KG_PATTERN_MAPPING.md) §4.1.

---

## E-18 — Programmatic vs model-assigned citation ids

**Question.** Are citation ids assigned programmatically and non-resolving ids
discarded, or is the model choosing its own citation strings and having them
validated after the fact?

**Isolated variable.** Who assigns the citation id: the assembler (current, if
ids are derived from the pack) or the model (if the model emits them).

**Method.** Inspect the assembly path for where citation strings originate, then
measure both rates: of the ids *handed to* the model, what fraction resolve to a
corpus node (context-level); of the ids the model *emitted*, what fraction
resolve, and what happens to the non-resolving ones (answer-level).

**Primary metric.** Answer-level resolution rate, and the disposition of
non-resolving ids — discarded, passed through, or repaired.

**Cost.** 0 GPU-h.

**Success criterion.** Ids are assigned programmatically, and any model-returned
id that does not match is discarded rather than emitted.

**If it wins** — the current path is already programmatic — this becomes a
documented invariant, and the finding worth recording is that the guarantee
already exists and is merely unasserted. [S-247] states the value of exactly
this: programmatic id assignment "guarantees that the sentences included in the
evidence trail are not hallucinated."

**If it loses** — ids come from the model and are checked after the fact — the
gap between "validated" and "impossible" is the whole subject of the experiment.
The remedy is small and mechanical, and it is a *guarantee* rather than a
filter: an id the model never had the opportunity to invent cannot be wrong.

**Why both levels, stated explicitly because it is the trap.** [S-242] measured
that "scoring the retrieved set as the attribution set ranks GraphRAG **last**;
scoring the answer's own citations ranks it **best or tied-best**." The
measurement point, not the architecture, drove the ranking. Reporting one rate
without the other is how a system gets credited or blamed for the wrong reason.

**Caveat to record.** A resolvable id is a *necessary* condition for a valid
citation, not a sufficient one. [S-248] decomposes transparency into three
independently measured layers — presence, correctness, and per-document causal
influence under leave-one-out intervention — and shows they dissociate: a clean
citation audit can co-occur with one cited source registering weak influence
while seven uncited sources demonstrably shift the output. Resolvability
establishes the first layer only.

**Related.** G10; E-13 (the other end of the same id space).

---

## E-19 — Mutation testing of the deterministic gates

**Hypothesis H1.** The deterministic validation layer — `doc_lint.py` (R11/R12),
`check_traceability.py` (T1–T6), and the L1 content gates — detects the fault
classes it claims to cover, at a rate high enough that its PASS is evidence.

**Preregistered prediction.** Detection ≥ 90% per (gate × fault class) within
each gate's declared scope, and false-positive rate 0% on unmutated artifacts.
This threshold is set *before* any fault is seeded and is not recalibrated
afterwards.

**Falsifier.** Any (gate × fault class) cell below 90% detection for faults
inside that gate's declared scope — or any clean artifact failing its gate. The
first outcome means the gate's PASS under-covers; the second means it over-rejects
and the pipeline's abort rate is partly spurious.

**Isolated variable.** One fault per artifact copy. Faults are never combined,
so no fault masks another.

**Design.** A fault taxonomy is derived first from the repo's *real* defect
history, not invented — this is the realism mitigation: duplicate LLM headings
(commit 0654bf1), `num_predict` truncation stored as a valid artifact (f2604a1),
`num_ctx` failures (d6d749a), plus the canonical classes each checker documents
(unresolved placeholder, out-of-set anchor, non-summing totals, broken chain
arrow, unresolvable control path). Each class is instantiated k times across
the three case trees; each instance is seeded into a copy, the gate runs, and
the outcome is recorded. The analysis runs once over all instances.

**Primary metric.** Detection rate per (gate × fault class); false-positive rate
on the clean copies.

**Threats to validity.** (a) Seeded faults may be unrepresentative of real
faults — mitigated by deriving classes from git history, not from the checkers'
own documentation, so the fault set is not circular with the code under test.
(b) Fixing a gate after seeing results invalidates the measurement unless
re-tested on held-out faults — stated in the preamble, restated here because it
is the experiment's main circularity trap. (c) Checker versions must be pinned
in the result record.

**Cost.** 0 GPU-h.

**If H1 stands.** The gates' PASS becomes calibrated evidence, and the detection
matrix becomes the regression test for the validators themselves.

**If H1 falls** for a cell, the finding names exactly which guarantee is
currently decorative — e.g., if T6-style anchor checks miss seeded out-of-set
anchors, then R2's enforcement is weaker than AGENTS.md claims, and that is a
correctness fact about the pipeline, not a research curiosity.

**Related.** R10; [09_KG_PATTERN_MAPPING.md](09_KG_PATTERN_MAPPING.md) G10, G12.

---

## E-20 — Pack utilisation and pack coverage

**Hypothesis H2.** (a) *Coverage:* every identifier the model's output cites was
present in the pack handed to the model at that step (the premise R2 depends
on). (b) *Utilisation:* the pack contains material the output never cites.

**Preregistered prediction.** Coverage = 100% (because R2's gates reject
unresolvable anchors, and a cited-but-never-provided id would mean a gate
passed something it should not). Utilisation is unknown — no prediction is
registered for its value, only that it will be measured; this is deliberately
a measurement hypothesis, not a threshold hypothesis.

**Falsifier.** For (a): a single output citation absent from the step's pack.
That is not a quality finding — it is a correctness defect in pack assembly or
gate enforcement, and it falsifies the premise that packs are the sole context
of every generated statement. For (b): none — utilisation has no falsifier, it
is a description. Stating which half is falsifiable is part of the design.

**Isolated variable.** None. This is a measurement over existing traces, and it
must not be turned into an A/B without pre-registering one.

**Design.** Replay existing runs. For each step: map every pack block to its
corpus path (via the `aegis:` tags and the pack builder's own records); extract
every emitted citation id by deterministic regex; compute (a) the fraction of
emitted ids present in that step's pack, and (b) the fraction of pack bytes
whose ids appear in any downstream output or gate decision.

**Primary metric.** Coverage rate (a) and utilisation rate (b), per step, per
run — reported in ids and in bytes, since a small number of large uncited
blocks and a large number of small ones are different problems.

**Threats to validity.** (a) The pack→corpus mapping itself has never been
audited; if mapping resolution is below 100%, that is a *prior* finding to
report before the utilisation numbers mean anything. (b) A paraphrase with no
id counts as uncited pack content even if it derives from it — so utilisation
is a *lower bound*, and that is recorded rather than fixed. (c) Traces from
runs with different ficha versions must not be pooled without a version
column.

**Cost.** 0 GPU-h.

**If the hypothesis stands** (coverage 100%, utilisation measured): the pack
gains its two numbers, G7 and G10 close, and utilisation becomes the baseline
any future pack-budget change (E-15, E-16) is measured against.

**If it falls** on coverage: the highest-severity correctness finding available
without spending GPU — a cited id the model never saw means either hallucinated
citation (R2 breach) or an assembly path outside the pack, and either way every
"grounded in the corpus" claim needs re-examination before any quality work
continues.

**Related.** G7, G10; [07_GRAPH_EVALUATION.md](07_GRAPH_EVALUATION.md) KG-022
(coverage as a gate) and KG-024 (the two measurement levels).

---

## E-21 — Cross-version output equivalence, matcher-pinned

**Hypothesis H3.** A preregistered equivalence metric can separate substantive
goal changes from cosmetic drift between two pipeline versions — and, replicating
[S-202] and [S-259] on this corpus, the choice of matching rule changes the
measured drift *rate* but not the *conclusion* about which sub-domains changed.

**Preregistered prediction.** (a) Exact-match matching reports strictly higher
drift than id-anchored matching, as in [S-202]'s 0.16–0.70 spread. (b) The
*identity* of changed sub-domains (the set-level conclusion) is invariant
across matchers — the MissDiag result ([S-238]) that the typed pattern survives
the matching rule.

**Falsifier.** Prediction (b) failing: if the choice of matcher changes *which*
sub-domains count as changed, then no equivalence metric is trustworthy until a
canonical rule is fixed by fiat, and E-08 (cross-version evaluation) has no
valid instrument. This is a real possibility, not a formality — it is exactly
what [S-202] found in the CTI literature, and this experiment tests whether the
repo's canonical-id discipline immunises it.

**Isolated variable.** The matching rule, applied to a *fixed* pair of outputs.
The pipeline, model and inputs are held constant; only the scorer varies.

**Design.** Freeze the matcher set first: (M1) exact string match on goal text;
(M2) id-anchored — same `AG-` id and same sub-domain, text differs; (M3)
id-set match only. The drift pair is the golden example's current output versus
its output under the previous ficha version. Every matcher decision is recorded
verbatim in the result, so the number is reproducible.

**Primary metric.** Drift rate under each matcher; set-level agreement of
"changed sub-domain" across matchers (prediction (b)).

**Threats to validity.** (a) One case only — the result is about the *metric*,
not about TinyTask, which is the transferable part (the PREREG_01 limitation,
same reasoning). (b) The two outputs being compared differ by both prompt change
and any model-side change; the experiment measures the metric's behaviour on a
real diff, not the diff's cause. (c) Matcher parameters (tokenisation,
lower-casing) are part of the rule and are frozen with it.

**Cost.** 0 GPU-h (both outputs already exist; if not, one seeded run
regenerates the current arm).

**If H3 stands.** E-08 gains its instrument, and the repo documents the first
matcher-pinned equivalence metric for this pipeline class — the thing the
literature reviews could not find anywhere.

**If it falls.** The equivalence question is declared open, E-08 is blocked
until a rule is fixed by convention rather than by measurement, and the finding
joins [S-202] as evidence that matcher-dependence is a general property of
generation metrics, not a CTI artefact.

**Related.** The preregistration requirement for E-08; [S-202], [S-259], [S-238].

---

## E-22 — Metamorphic input testing of R3/R6/R8

**Hypothesis H4.** The pipeline's output obeys the metamorphic relations that
AGENTS.md's rules imply, even though no gate currently tests them end-to-end:

- **M1 (R6, invariance):** reordering the sections of `company_input.md` does
  not change the fact sheet.
- **M2 (R8, invariance):** adding a preregistered *irrelevant* product line to
  the intake does not change the P2 regulation verdicts or the sub-domain set.
- **M3 (R3, monotonicity):** scaling the company profile (MICRO → SMALL) scales
  the adjusted goals without inventing or dropping sub-domains.

**Preregistered prediction.** M1: fact sheet byte-identical (seed=42 makes this
crisp — EXP-02 established that identical inputs give byte-identical runs, so
any difference is a real sensitivity, not sampling). M2: P2 verdicts identical
as a set. M3: directional only — judged, therefore gated on E-04/E-05, and no
quantitative prediction is registered for its magnitude.

**Falsifier.** M1: any byte difference in the fact sheet. M2: any verdict or
sub-domain change. M3 is not falsifiable at this precision and is explicitly a
judged relation — which is why it is gated and would be run last.

**Isolated variable.** The input transformation, one at a time. The
transformation for M2 must itself be preregistered — the specific product line
(e.g., a physical-goods resale line for a SaaS intake) and the argument for why
no scope criterion in SPEC §5 should fire on it. If the "irrelevant" line turns
out to be relevant, that is a design error in the experiment, not a pipeline
failure, and it is recorded as such.

**Design.** Three pairs of seeded runs (M1 original vs reordered; M2 original
vs augmented; M3 original vs scaled), compared at the fact-sheet, verdict and
goal-set levels respectively. M1 and M2 compare deterministically; M3 uses the
L2 rubric subset for proportionality and is not run until the judge layer has a
noise floor (E-17).

**Primary metric.** Relation violated / relation held, per relation, with the
diff shown in the result record.

**Threats to validity.** (a) n = 1 case; the relations are about the pipeline's
rule-following, which is the transferable claim, but the specific sensitivity
found would be case-specific. (b) M2's "irrelevant" judgement is the weakest
point and is mitigated only by preregistering the line and the argument. (c)
Positive results do not prove R6/R8 — they prove the pipeline survives *these*
perturbations; the claim is scoped to the tested relations.

**Cost.** ~2 GPU-h (four runs for M1+M2, two each arm; M3 adds two and is
gated).

**If the relations hold.** R3/R6/R8 gain their first behavioural evidence —
today they are enforced by gates and prompts, and this is the test that the
enforcement survives a perturbation no gate was designed to catch.

**If a relation falls.** The highest-value finding this lane can produce: the
output would be *passing every existing gate while violating a core rule*, which
is precisely the failure class gates cannot see and the reason metamorphic
testing exists. The fix would be a gate (M1/M2 are mechanically checkable
post-hoc), which converts the relation from a test into a permanent invariant.

**Related.** R3, R6, R8; E-14 (the abstention half of R6's behaviour);
[09_KG_PATTERN_MAPPING.md](09_KG_PATTERN_MAPPING.md) §1.3.

---

## Sequencing

**Can run in parallel, no dependencies:** E-01, E-02, E-03, E-06, E-07, E-10,
E-13, E-14, E-15, E-18, **E-19, E-20**.

**Prerequisites for reading any future A/B:** E-04, then E-05. Until both are
run, an A/B between arms scored by an LLM judge measures the rubric, per
[S-114] and [S-134]. **E-17 joins this list and comes first** — it is a
configuration audit that establishes the judge's noise floor, and without it no
judge-scored comparison (including E-04 and E-16) is interpretable.
**E-21 joins it from the other side**: E-08 has no instrument until an
equivalence matcher is pinned, and E-21 is the experiment that decides whether
one can be.

**Depends on E-03's outcome:** E-07 should run against whichever sampling
configuration E-03 selects, not against the current one.

**Gated:** E-09 (needs a second model), E-11 (needs a decision to keep the agent
arm), E-12 (needs a concrete portability need), **E-22's M3** (needs E-17's
noise floor; M1 and M2 are ungated).

**E-16 has a dependency the others do not:** its arm B assumes a retrieval step
over canonical ids, which is the same selection rule E-13's builder would
establish. E-13 first is cheap and makes E-16's arm B a table lookup rather than
a new mechanism.

**Cheapest first, if only one thing runs:** E-17. Zero GPU cost, it is a read of
the judge invocation plus a re-judging loop, and it gates the interpretation of
every other judge-scored result in this backlog. E-10 remains the cheapest
*decision-resolving* experiment; E-17 is now the cheapest *prerequisite*. **The
cheapest robustness pair is E-19 + E-20**: both read artifacts and scripts only,
neither depends on the judge, and together they calibrate the two things every
other result leans on — that the gates detect what they claim, and that the
packs contain what the outputs cite.
