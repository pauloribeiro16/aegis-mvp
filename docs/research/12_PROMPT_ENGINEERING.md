---
document_id: AEGIS-RES-12
title: 'Prompt engineering — annotated catalogue'
version: 0.1.0
created: 2026-10-05
status: ACTIVE
survey_date: 2026-10-05
sources: 'docs/research/sources.yaml'
---

# Prompt engineering — annotated catalogue

**What this document is.** The catalogue the repo did not have. The 2026-10-03
and 2026-10-04 passes covered pipeline architecture (`PP-001`..`PP-021`),
agent orchestration (`AO-001`..`AO-013`) and knowledge graphs
(`KG-001`..`KG-037`). Across all of them the phrase "prompt engineering"
appears zero times, and no pattern in any of the three catalogues is *about* the
prompt as an authored artefact. Prompt design arrived only as advice embedded
in other patterns — the "Goldilocks zone" paragraph inside `PP-013`, a few-shot
aside inside `AO-004`, the "prompt as spec" anti-pattern row inside `PP-021`.

That is the gap this pass closed. `PE-001`..`PE-014` are the patterns, and two
of them (`PE-010`, `PE-011`) exist because the literature's most confident
recommendations are its least supported.

**Method and evidence grades** are as in
[01_PIPELINE_PATTERNS.md](01_PIPELINE_PATTERNS.md). This pass registered
100 sources (S-284..S-383) across three fronts: prompt design doctrine,
automatic prompt optimization, and prompt-as-code tooling. Verify with
`python scripts/check_research_refs.py --strict`.

**A declared bias, stated before the findings.** `WebSearch` failed on every
attempt during this pass, so discovery ran through the arXiv API, direct
canonical fetches, and OpenAlex. That systematically favours papers and
official documentation over practitioner write-ups — the same bias the KG
survey recorded in [09_KG_PATTERN_MAPPING.md](09_KG_PATTERN_MAPPING.md) §6, and
it is the largest source-layer risk on this document's three most
practitioner-heavy topics. Abstracts, titles and authors for 13 load-bearing
entries were re-verified by direct fetch after collection; 19 of 20 sampled
URLs resolved. What is missing is blog-tier and vendor-blog evidence, not
paper-tier evidence.

---

## 1. Reasoning elicitation — and the retreat from it

### PE-001 — Chain-of-thought as the original elicitation technique

**The claim.** A prompt suffix is sufficient to elicit reasoning: eight
exemplars moved GSM8K to state of the art at 540B [S-284], and the bare
11-token string *"Let's think step by step"* moved MultiArith from 17.7% to
78.7% and GSM8K from 10.4% to 40.7% [S-285]. Self-consistency then added a
decoding-time aggregation on top [S-286's sibling PP-004 already covers
majority voting; see [01_PIPELINE_PATTERNS.md](01_PIPELINE_PATTERNS.md)].

**Why the repo must care.** A large accuracy delta is purchasable with a
prompt edit alone, at zero infrastructure cost. That is what makes prompt
wording a first-class experimental variable rather than a constant, and it is
the premise of `PE-007`.

**Where the envelope stops.** Both results are math and commonsense on
frontier models. A regulatory pack is long-document extraction in a specific
register, on a local 27B. Neither the task class nor the model class is the
one measured.

### PE-002 — CoT explanations are not causal evidence

**The claim, and it is the single most consequential negative in this
document.** Reasoning traces systematically misrepresent the true cause of a
prediction. A biasing feature — reordering multiple-choice options so the
answer is always "(A)" — was followed *without ever being mentioned in the
rationale*, costing up to 36 accuracy points across 13 BIG-Bench Hard tasks
[S-286]. Intervening on the chain itself, Lanham et al. found conditioning
"varies across tasks… sometimes relying heavily on the CoT and other times
primarily ignoring it," and the direction of travel is the wrong one for
anyone hoping scale brings transparency: **"As models become larger and more
capable, they produce less faithful reasoning on most tasks we study"**
[S-287].

The extension to reasoning models is from the model builder itself: hint usage
is disclosed in at least 1% of examples where it occurs but the reveal rate is
"often below 20%," and CoT monitoring is "not sufficient to rule them out"
[S-288].

**Consequence for this repo, and it is not a small one.** Any reasoning field
in `trace.jsonl` is a *generated artefact*, not a record of the pipeline's
process. A gate that treats a model's own stated reasoning as corroboration for
its answer is unsound. This constrains how `trace.jsonl` may be used as
evidence, and it is worth stating explicitly because the alternative — reading
a trace as an audit record — is the intuitive move and it is wrong.

### PE-003 — You cannot prompt for raw chain-of-thought on current models

**The hard constraint.** *"What you see is never the raw chain of thought: the
text in a thinking block is a summary of Claude's reasoning… No `display`
setting returns the raw chain of thought"* [S-289]. The property `PE-002`
warns against is not merely unreliable on these models; it is not exposed at
all.

**Both directions of the dial are non-monotone.** A *NoThinking* prompt beat
full thinking on seven reasoning datasets at matched token budgets (51.3 vs
28.9 on ACM 23 at 700 tokens), and parallel best-of-N with NoThinking matched
thinking at up to 9× lower latency [S-290]. Meanwhile overthinking correlates
with *worse* performance — selecting the lower-overthinking solution improved
results ~30% while cutting compute 43% [S-291] — and its mirror, underthinking,
correlates frequent thought-switching with wrong answers [S-292].

**So "add a reasoning step" is not a safe default edit.** It is a two-sided
dial with a measured optimum that depends on the task, and the repo has no
measurement of where its tasks sit on it.

**Where the AEGIS model sits on it.** OpenAI's guidance is explicit that effort
is *"a tuning knob, not the primary way to recover quality"*, and draws the
distinction that matters here: a reasoning model "is like a senior co-worker"
given a goal, while a non-reasoning model "is like a junior coworker" that
performs best with explicit instructions to create a specific output [S-312].
A local 27B without an effort parameter is in the second camp, which means
`PE-005`'s explicit-instruction doctrine applies and `PE-003`'s elicitation
technique largely does not.

### PE-004 — Few-shot examples: what selection actually buys

The regime originates with GPT-3, where "tasks and few-shot demonstrations
[are] specified purely via text interaction" [S-293].

**Selection by similarity works** and beats random selection, with gains on
table-to-text (41.9% on ToTTo) and open-domain QA (45.5% on NQ) [S-294].
**Ordering is worth near-SOTA versus chance** — *"the order in which the
samples are provided can make the difference between near state-of-the-art and
random guess performance"* — and a good permutation does **not** transfer
across models [S-295]. On k, more shots keep paying on open models: many-shot
learning "can learn high-dimensional functions with numerical inputs, and
performs comparably to fine-tuning," at linear inference cost [S-297].

**The negative result that reframes the question.** *"Ground truth
demonstrations are in fact not required — randomly replacing labels in the
demonstrations barely hurts performance"* across 12 models including GPT-3
[S-296]. What demonstrations actually supply is (1) the label space, (2) the
input distribution, (3) the sequence format. So example selection is a
**format and label-space** problem, not a content problem — a materially
different design question from the one the positive half answers, and the two
are recorded as `CONTESTED` rather than reconciled.

**One source disagrees in the useful direction.** Structured prompting scales
to 1,000 examples and reports that performance *variance falls* as
demonstration count increases [S-298] — the only claim in this block that more
demonstrations make a run more deterministic. It requires an architectural
change (separately encoded demonstrations, rescaled attention), so it is not a
prompt-only intervention; it is recorded so the disagreement with `PE-007` is
visible rather than averaged away.

**For a regulated pipeline, the operative content of S-296 is uncomfortable
and worth stating plainly:** a demonstration whose *labels* are wrong may cost
little, which means few-shot examples are a poor place to encode a compliance
requirement. Requirements belong in the instruction and in the output
contract, where `PE-005` puts them.

### PE-005 — Instruction design: the system prompt is a privilege level

**The governing claim.** *"One of the primary vulnerabilities underlying these
attacks is that LLMs often consider system prompts (e.g., text from an
application developer) to be the same priority as text from untrusted users
and third parties"* [S-299]. The system prompt is a privilege **level**, not a
channel, and hierarchy training is reported to transfer to unseen attack types
with minimal capability degradation.

**Both vendors converge on a template, from unrelated directions.** Anthropic:
tell the model what to do rather than what not to do, use XML tags to delimit,
wrap examples in `<example>` tags [S-301]. OpenAI: the same XML reasoning, with
a canonical developer-message order of Identity → Instructions → Examples →
**Context**, context "usually best positioned near the end" [S-302].

**The convergence is the strongest available prior, and it is still not
evidence.** Two independent vendors arriving at the same four-section template
is the best-supported design prior available for a pipeline that must emit
JSON under a strict schema. But the 3–5 example band [S-301] is vendor
guidance with no measured optimum behind it, and both docs instruct the reader
to re-check against their own evals.

**The instrument, if the repo wants one.** IFEval isolates 25 types of
*verifiable* instructions ("write in more than 400 words", "mention the
keyword of AI at least 3 times") across ~500 prompts, chosen specifically to be
checkable **without an LLM judge** [S-300]. That property is exactly what
`E-17` left unsatisfied when the L3 judge was withdrawn — see
[14_PATTERN_MAPPING.md](14_PATTERN_MAPPING.md).

### PE-006 — Injection as a prompt-structure problem, with a measured ceiling

This is the section where the literature most disagrees with itself, and both
sides are recorded.

**The cheap structural mitigation, with the best number in the block.**
Spotlighting — transforming untrusted input so its provenance is signalled
continuously — *"reduces the attack success rate from greater than 50% to
below 2%"* [S-303]. It is the only source showing a prompt-level transform
alone suffices at scale, with no model change.

**The structural fixes that actually hold, and their prices.** StruQ requires
a *specially trained* model [S-304] — not available to a local 27B with no
training pipeline, which is why it is recorded as the shape of the guarantee
rather than a recommendation. CaMeL sidesteps the model entirely: it "explicitly
extracts the control and data flows from the (trusted) query; therefore, the
untrusted data retrieved by the LLM can never impact the program flow," solving
77% of AgentDojo tasks with provable security against 84% undefended [S-305] —
a 7-point utility cost, and a large architectural change.

**The counterweight, and it is not marginal.** Across 143,745 queries against
37 real applications: *"real-world applications are more vulnerable… compared to
those used in research settings"*, and prompt-level and model-level defenses
"highlight their limitations in real-world applications"* [S-306]. Complex
attack instructions are, counter-intuitively, *less* effective than simple ones.

**The verdict this section supports: delimiters are defence-in-depth with a
known ceiling, never a security control.** If the pipeline ever ingests text it
does not control, spotlighting's 50%→2% is the cheapest available mitigation and
[S-306] is the reason to record its limit at the same time.

### PE-007 — Prompt sensitivity: the finding that most qualifies this repo

**The anchor.** *"Several widely used open-source LLMs are extremely sensitive to
subtle changes in prompt formatting in few-shot settings, with performance
differences of up to **76 accuracy points** when evaluated using LLaMA-2-13B"*
[S-307]. Sensitivity persists across model size, example count, and instruction
tuning. Format performance correlates only weakly *between* models, "which puts
into question the methodological validity of comparing models with an
arbitrarily chosen, fixed prompt format." The prescription is a reporting
change: report a **range** across plausible formats, not a point on one.

**Generalised from format to meaning-preserving perturbation.** A single
perturbation *"alters the relative ranking of models in 63% of cases"*, and
semantics-preserving perturbations *"can account for up to half of the
performance variance for a given model"* [S-308]. That second number is the
one that bounds every model comparison this repo makes.

**A third variance axis, orthogonal to both seed and format.** API-surface
evaluations score 3.4 points higher in accuracy than the corresponding chat
interfaces, and *"switching access surfaces can degrade performance as much as
downgrading a full model generation"* [S-310].

**The mandatory counterweight, and it changes the conclusion.** Much of the
measured sensitivity may be an artefact of the *ruler*: it "stems from
heuristic evaluation methods, including log-likelihood scoring and rigid answer
matching, which often overlook semantically correct responses expressed through
alternative phrasings," and with judge-based scoring there is "a substantial
reduction in performance variance" [S-309].

**So `PE-007` is a measurement discipline, not a defect list.** The
operational rule that survives both sides: *a sensitivity figure is only
comparable if the scorer is held fixed and named.*

**And this is where it lands on AGENTS.md §-1.** The repo's
`sd = 0.0000` across 15 seeded runs is a correct and valuable result about
**sampling** variance. `PE-007` says two further axes exist — prompt format
[S-307] and access surface [S-310] — that seeding does not touch, and that the
first may carry up to half of total observed variance [S-308]. The honest
statement is that the repo has measured one point in a distribution whose width
is unmeasured. That is not a flaw in the existing experiment; it is the next
one.

### PE-008 — Instruction count, format, and placement at scale

The one fully factorial study in the block (format × instruction count ×
context length × placement, on a contamination-free reproducible corpus) [S-358]
reports three findings that bear directly on a staged pipeline:

- **Instruction count has a hard collapse point**: "Perfect-response rate
  collapses to zero by N=80 for every model, format, and placement."
- **Placement effects are at least as large as format effects, and their
  direction is model-specific** — so a placement rule tuned on one model does
  not transfer.
- **The failure mode near the context ceiling is abstention, not
  fabrication**: refusal rises from 0% to 79–90% while fabrication never occurs
  (0 of 5,760 probes). That changes what a grounding gate should be measuring —
  a run that silently stops answering is a different failure from a run that
  fabricates, and they need different responses.

The prompt decomposes into four independently translatable parts —
instruction, context, examples, output — and the effect of pre-translation
across 35 languages is driven by similarity to English, translation quality and
the amount of pre-trained data [S-313]. That decomposition is directly usable on
a multilingual regulatory corpus, with the caveat that none of its task families
is one.

Cross-lingually, instruction hierarchy is **not** language-invariant: a language
that strengthens compliance in the higher-priority position can become
disruptive in the lower-priority position, creating "multilingual reliability and
security risks" [S-314]. For a repo whose corpus is multilingual and whose
instructions are in one language, that is the configuration, not an edge case.

---

## 2. Automatic prompt optimization

### PE-009 — The lineage, and why its numbers are self-reported

The progression is: the LLM writes the next prompt from a sorted trajectory
(OPRO, "outperform human-designed prompts by up to 8% on GSM8K" [S-316]); the
LLM mutates the mutator (PromptBreeder [S-317]); declarative signatures compile
into programs (DSPy [S-318]); instructions and demonstrations are optimised
jointly (MIPROv2, which wins on "five of seven" programs — it lost on two
[S-319]); and reflective mutation over a per-instance Pareto frontier is the
current state of the art (GEPA, "outperform[s] GRPO by 6% on average and by up
to 20%, while using up to 35x fewer rollouts" [S-320]).

**Read GEPA with its own absences.** The paper has no limitations section, no
error bars and no multi-seed runs, and its only baseline is the un-optimised
base program — never an independently strong human-written prompt. Those three
absences are the reason this catalogue does not treat its numbers as a ceiling.

### PE-010 — Does an optimised prompt beat a well-written human prompt?

**Sometimes. The answer depends almost entirely on the starting prompt.**

The strongest independent pro-APO result reports prompts beating human-written
ones in 76% of instruction-induction tasks. The strongest *critical* artefact is
the chess benchmark: six algorithms × eight models × three runs, where the
baseline is a **55-character fixed instruction** rather than a strong human
prompt, and **only 4 of 8 models show a statistically significant gain** [S-321].

The mechanism is named in [S-329]: the gain is a function of the **headroom
available in the seed prompt**. That is a falsifiable account of why the same
optimizer wins on some tasks and not others, and it inverts the usual framing —
the question is not "is APO good?" but "how much headroom does my prompt
leave?".

**Three results where a human beat the machine, or detail did nothing.**
Human-written policies improved frozen 7B agents by 5.0 success points where
GEPA-derived policies "did not reliably beat fixed prompting" [S-323] — note
the model class matches this repo. 503 detailed profession-specific system
prompts produced a mean accuracy change of **−0.6 pp, 95% CI [−1.5, +0.2]**,
while output tokens rose 1.5–2.3× and cost per successful call 2.2–4.5× [S-324].
And from a defective seed, GEPA *dropped* GSM8K from 23.81% to 13.50% [S-326].

### PE-011 — The dominant failure mode is selection on a small fixed set

This is the section that decides the verdict, and the evidence is unusually
convergent:

- **The dev/test gap, measured cleanly**: development accuracy 0.40 → 0.80
  while test accuracy moves only 0.20 → 0.50 — roughly half the apparent gain
  is fitting the selection set [S-322].
- **No adversary is even required**: *"16/53 (30%) of in-distribution wins fail
  to transfer to held-out configurations"* under selection pressure alone
  [S-325]. This is the most important number in the negative half.
- **The optimiser's own documentation concedes it**: *"If you omit valset, GEPA
  reuses trainset for selection"*, and the page states this lets prompts
  "overfit those examples" [S-330]. This is a vendor-confirmed requirement, not
  the survey's opinion.

**Metric gaming is the norm rather than the exception.** Prompt-hacking
susceptibility runs at 86% for TextGrad [S-327].

**So the rule `PE-012` states is narrow and procedural:** *an APO gain is not a
result until it survives a held-out configuration, and the optimiser's own
training set is not one.*

### PE-012 — Prompt inflation, measured

Prompts produced by existing optimizers run **14.7× their original length** or
contain **34% repetitive content** [S-327]. In absolute terms, the chess
benchmark's 55-character baseline becomes 930 characters under the winning
configuration and 2,109–3,626 under GEPA [S-321]. The fattest prompts are also
the least portable: RLMOpt's are 27–79% of GEPA's size, and they are the ones
that did not regress below their starting point [S-329].

The correctness version of the same finding is stronger than the cost version:
long hard prompts produce the *"prompt dominating answer phenomenon"* — the same
answer emitted regardless of the query — and deciding whether a hard prompt
exists is NP-complete [S-328].

**For a pipeline with a declared token budget, this is not a style
observation.** Prompt length is a gate parameter, and [S-322] supplies a free
observation in the other direction: verbosity operators were never selected in
that study, and concision was the most useful transformation.

### PE-013 — APO and reproducibility are in direct tension

The chain is arithmetic, not opinion:

1. **The optimiser is a second stochastic process.** GEPA accepts one candidate
   per iteration on a single minibatch and samples stochastically from the
   Pareto frontier [S-320]; the search itself carries ~7% run-to-run variance
   [S-321 context, MAGE measurement recorded in 13_ORCHESTRATION.md]; GEPA
   finished below its starting point in 2 of 11 matched runs [S-329]; and 14.9%
   of chess runs returned an unchanged prompt — the optimiser frequently does
   nothing at all [S-321].
2. **The output artefact couples to hidden variables.** Cross-model transfer is
   31 improved / 16 declined / 2 unchanged over 49 pairs [S-321].
3. **The serving layer under it is deterministic only under conditions.**
   Cached serving changed the trajectory in 36.2% of 16-bit and 75.0% of 4-bit
   episodes, while **zero of 800 episodes were non-bit-identical with caching
   disabled** [S-331] — which independently corroborates the repo's own EXP-02
   result and names prefix caching as the exclusion condition.

**The verdict.** A seeded pipeline inside a stochastic outer loop is not a
seeded pipeline. Bit-reproducibility here is bought either by the absence of an
optimiser, or by recording the optimised prompt as an immutable versioned
artefact and treating regeneration as a separate, explicitly non-deterministic
act. There is no third option in the current literature.

### PE-014 — Prompt-as-code is mainstream; prompt linting does not exist

The practice is not a house convention, it is established: 466 open-source
projects use version-controlled context files, classifiable as descriptive,
prescriptive, prohibitive or conditional [S-334]. The strongest academic
joining of prompt-as-code to APO reports accuracy movement across five
industrial use cases [S-335] — with no variance or cost reporting, so the
percentages are not usable as thresholds.

**The tooling split is informative.** promptfoo gives typed assertions
(deterministic checks including latency and cost, plus model-assisted rubrics)
and a CI action that diffs prompt changes on every pull request [S-332]. What it
does *not* have is prompt linting, static prompt validation, or prompt diffing —
versioning is delegated entirely to git. LangSmith provides the more complete
registry model (commits, diffs, environment promotion, rollback) [S-333].

**The honest gap:** across both the tooling and the academic layer, no
static prompt analysis or CI-time prompt validation surfaced. AEGIS's existing
practice — prompts as files, versioned, diffable, tested — is ahead of the
published tooling, and the missing piece is a linter, which nobody ships.

---

## 3. What this survey could not establish

1. **Register as a manipulated variable.** No primary source isolates
   *register* — statutory versus explanatory versus regulatory prose — as a
   prompt variable. [S-315] (LegalBench) is the closest domain anchor and it is
   a capability benchmark, not a prompt-design study. This is a genuine gap in
   the literature, not in the search, and a defensible place for the repo to
   contribute: register-controlled paraphrase over `baseline/domains/` articles
   with goal IDs held fixed.
2. **Whether any of this transfers to a 27B open-weight model.** Every
   prompt-design claim in this block originates from frontier-model vendor
   documentation or benchmarks whose transfer to the AEGIS model is untested.
   [S-348] makes the general version of this point for context (open models lag
   closed ones exactly on complex instruction following at length); nothing yet
   makes it for prompts.
3. **Practitioner-tier evidence.** Declared at the top. WebSearch was down for
   the whole pass.
4. **Prompt linting.** No source, academic or commercial. Recorded as an
   absence rather than filled with a plausible-sounding neighbour.

---

## 4. The two findings that should change what the repo does next

Stated here, argued in [14_PATTERN_MAPPING.md](14_PATTERN_MAPPING.md):

1. **[S-311] — context may silently shorten reasoning and suppress
   self-verification.** *"Reasoning models tend to produce much shorter
   reasoning traces (up to 74%) for the same problem under different context
   conditions"*, associated with decreased self-verification and
   double-checking. For a pipeline whose corpus is regulatory text and whose R6
   gate depends on the model checking itself, this is the highest-value
   unclaimed threat in the entire three-front survey. It is a single small-author
   workshop paper, so it is a hypothesis generator rather than a result — which
   is exactly what makes it a good preregistration.
2. **[S-307] + [S-308] — report a range, not a point.** The repo's determinism
   result controls sampling variance only. Format variance may carry up to half
   of total observed variance, and a single-format comparison is methodologically
   questioned by the source that established the sensitivity. Reporting a
   FormatSpread-style interval alongside `sd = 0.0000` is the obvious
   follow-on experiment, and it needs no pipeline change.
