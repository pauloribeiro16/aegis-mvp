---
document_id: AEGIS-RES-02
title: 'Agent orchestration patterns — an annotated catalogue'
version: 0.1.0
created: 2026-10-03
status: ACTIVE
survey_date: 2026-10-03
sources: 'docs/research/sources.yaml'
---

# Agent orchestration patterns — annotated catalogue

**What this document is.** A catalogue of patterns for systems in which a model
decides part of the control flow, each with definition, sources, when it
applies, named failure modes, countermeasure, and evidence grade. Pipeline
patterns that assume code owns the control flow are in
[01_PIPELINE_PATTERNS.md](01_PIPELINE_PATTERNS.md); the boundary between the two
is AO-001, and it is the most contested boundary in the field.

**Method and evidence grades** are as in [01_PIPELINE_PATTERNS.md](01_PIPELINE_PATTERNS.md):
web survey of 2026-10-03, ~123 registered sources in
[sources.yaml](sources.yaml), every claim carrying an `[S-nnn]` token. Verify
with `python scripts/check_research_refs.py --strict`.

**The headline finding of this catalogue is negative**, and it is stated up
front because it governs everything below: the empirical literature on
multi-agent systems is broadly unfavourable to multi-agent systems as a default.
Three independent primary sources recommend starting with a single agent
([S-001], [S-010], [S-060]), and [S-062] puts it more bluntly still — "If you
can write a function to handle the task, do that instead of using an AI agent."
The one strong pro-multi-agent production result is conditional on task shape
and architecture, and the reconciliation is set out in AO-006.

---

## 1. The boundary

### AO-001 — Agent versus workflow

**The canonical formulation.** [S-001]: "Workflows are systems where LLMs and
tools are orchestrated through predefined code paths. **Agents**, on the other
hand, are systems where LLMs dynamically direct their own processes and tool
usage, maintaining control over how they accomplish tasks."

Two details in that paragraph are routinely lost. First, Anthropic brands
*both* categories as "agentic systems" and draws the distinction inside that
family, because customers define "agent" inconsistently — some mean full
autonomy, some mean a prescriptive workflow. Second, the guidance is a ladder,
not a dichotomy: single LLM call with retrieval and in-context examples →
workflow → agent. "For many applications, however, optimizing single LLM calls
with retrieval and in-context examples is usually enough."

**The 2025 simplification.** [S-004] reports the vocabulary collapsing: "Since
we wrote that post, we've gravitated towards a simple definition for agents:
**LLMs autonomously using tools in a loop.**" What replaces the workflow/agent
split as the live question is pre-inference retrieval versus just-in-time
retrieval.

**OpenAI's framing, with an explicit build test.** [S-010] defines agents as
"systems that independently accomplish tasks on your behalf," excludes "simple
chatbots, single-turn LLMs, or sentiment classifiers," and gives two defining
properties: the model manages workflow execution and can halt and hand control
back, and tool selection happens "always operating within clearly defined
guardrails." The build test is three conditions — complex decision-making,
difficult-to-maintain rules, heavy reliance on unstructured data — and the
fallthrough is the important part: "Otherwise, a deterministic solution may
suffice." They are also explicitly anti-hype about autonomy: "customers
typically achieve greater success with an incremental approach."

**The counter-position, stated by the team shipping a production coding agent.**
[S-080] argues against multi-agent decomposition on two principles: "Share
context, and share full agent traces, not just individual messages," and
"Actions carry implicit decisions, and conflicting decisions carry bad results."
The worked failure decomposes a Flappy Bird clone across two subagents: one built
a Super-Mario-looking background, the other built a non-asset bird, and the
synthesiser inherited both miscommunications. Copying the original task into the
subagents does not fix it — the subagents then make conflicting aesthetic
decisions.

**Do not conflate the two taxonomies.** [S-100] organises the field
ontologically as brain / perception / action across single-agent, multi-agent
and human-agent settings. That is a different scheme from [S-001]'s prescriptive
design patterns. They are complementary, not competing, and citing one as if it
were the other is a category error. Note also that the widely-quoted
six-archetype breakdown of [S-100] was not confirmed from the paper body in this
survey and is therefore not asserted anywhere in this catalogue.

**Evidence.** `PRIMARY` for both vendor formulations; `PRACTITIONER` for
[S-080]; `PEER` for the ontological taxonomy, whose specific archetype list is
unverified.

---

## 2. Topologies

### AO-002 — Orchestration topologies

The union of the vendor pattern catalogues [S-001], [S-010], [S-060], [S-063],
[S-061], [S-011], [S-012], [S-162], and the empirical literature.

| Topology | Control flow owner | Context propagation | Named failure modes | When it wins |
|---|---|---|---|---|
| **Single agent with tools** | the model | one continuous context | compounding errors over long horizons; context overflow; wrong-tool selection; runaway loops | most of the time |
| **Sequential / chain** | code | each step consumes the last | fixed decomposition cannot adapt; latency is the sum; early errors poison downstream | well-understood task; auditability required |
| **Router / triage** | classifier, then dispatch | only the routed branch | misclassification is silent and catastrophic downstream | distinct categories genuinely better handled separately, and a reliable classifier exists |
| **Supervisor / orchestrator-workers** | a central model | orchestrator holds synthesis; workers are isolated | over/under-delegation; thin instructions; orchestrator context saturation; one bottleneck model | subtasks cannot be predicted in advance |
| **Peer handoff** | the model, per transfer | truncated at each boundary; filtered by an input filter | context truncated at the handoff; no global owner of the final answer; routing errors user-visible | conversation triage; the specialist should own the rest of the turn |
| **Subagents as a context device** | main agent, which routes all | workers get a clean context; only condensed results return | extra model call per invocation; results flow back through the main agent | long-horizon investigation where history is the enemy |
| **Multi-layer hierarchy** | layered | compounding truncation | failures compound multiplicatively with depth; thin evidence at depth > 2 | untested at scale |
| **Blackboard / shared state** | the store, plus an orchestrator | all participants read/write shared state | write conflicts; semantic conflicts where divergent edits both "succeed"; stale reads; unclear write ownership | teams owning separate components; emergent ordering |
| **Society / debate / layered aggregation** | layer structure | each layer consumes all prior outputs | shared priors make layers converge rather than diversify; cost | `CONTESTED` — see AO-006 |
| **Swarm / dynamic topology** | emergent, no fixed topology | per-interaction | live in MARL; no major production vendor ships a swarm-native runtime | research direction |

**Notes on the ones that matter most here.**

*Single agent with tools* is described by [S-001] as "typically just LLMs using
tools based on environmental feedback in a loop." [S-010]'s order of escalation
is single → multi.

*Sequential* is crewAI's [S-063] first process: "Task execution follows the
predefined order in the task list, with the output of one task serving as context
for the next."

*Supervisor* in [S-011] is the manager pattern, best when "one agent to own the
final answer, combine outputs from multiple specialists, or enforce shared SDK
guardrails in one place." [S-163]'s layered aggregation is the canonical society
topology, and is deliberately retained as the strongest pro-aggregation result in
this registry so the AO-006 conclusion is stated as contested rather than
settled.

*Handoff* is [S-012]'s mechanism: handoffs are tools to the LLM, with
`on_handoff` callbacks, custom `input_type` schemas, and **input filters**
controlling what crosses the boundary. That filter is the direct mechanism behind
the context-truncation failure — the same failure [S-080] describes as sharing
messages instead of sharing context and traces.

*Subagents as a context device* is the thesis [S-080] endorses after reading
Claude Code: the subagent "is usually only tasked with answering a question, not
writing code… The benefit of having a subagent in this case is that all the
subagent's investigative work does not need to remain in the history of the main
agent." [S-060] states the same rationale as context management first,
distributed development second, parallelisation third.

*Blackboard* is [S-061]'s position, and the auditability claim is the reason it
is on this list: "Fine-grained control to mix deterministic, hand-coded steps
with LLM-driven agentic steps in the same graph. Parts of the logic are fully
predictable and auditable while other parts are flexible and model-driven." The
graph *is* the shared state. The coordination cost is measured by [S-138], which
reports 5–10% semantic conflict rates and up to 21.1% speedup *and* up to 39.4%
slowdown depending on the task — coordination is not free even in its best
observed form.

*Swarm* is worth one line only because it is a live research direction [S-162]
and not an absence.

**The cost of topology, measured.** [S-060] gives the cleanest published data:
on an identical two-turn scenario, subagents cost 8 model calls against handoffs 5
and router 6. The mechanism is stated: "Subagents adds one extra call because
results flow back through the main agent — this overhead provides centralized
control." [S-002]'s ratios are the industry reference point: agents ≈ 4× chat
tokens, multi-agent ≈ 15×.

**Evidence.** `PRIMARY` for the topologies, `PEER` for the coordination cost.

---

## 3. Context and memory

### AO-003 — Context budget, compaction, and memory

**The physical constraint.** [S-004]: as the number of tokens in the context
window increases, "the model's ability to accurately recall information from
that context decreases… this characteristic emerges across **all models**."
Context "must be treated as a finite resource with diminishing marginal returns,"
with an "'attention budget'" the model draws on. The recommendation is
"the smallest possible set of high-signal tokens that maximize the likelihood of
some desired outcome."

**Long-horizon techniques, named exhaustively by [S-004]:** compaction,
structured note-taking, and multi-agent architectures. Compaction is "taking a
conversation nearing the context window limit, summarizing its contents, and
reinitiating a new context window with the summary," and is "the first lever."
The art is in what survives: Claude Code's implementation preserves
"architectural decisions, unresolved bugs, and implementation details while
discarding redundant tool outputs." The failure mode is named too — "overly
aggressive compaction can result in the loss of subtle but critical information."
Waiting for bigger windows is explicitly rejected: "for the foreseeable future,
context windows of all sizes will be subject to context pollution."

**Compaction is now a runtime feature, not an application concern.** [S-009]
documents the agent SDK; [S-062] lists "context compaction" among the Microsoft
harness agent's built-ins.

**Structured external memory has no standard.** [S-158] is the origin —
virtual context management drawn from hierarchical memory systems, using
interrupts to manage control flow. [S-159] (ACE) treats contexts as "evolving
playbooks that accumulate, refine, and organize strategies through a modular
process of generation, reflection, and curation," and names the two failure modes
of naive memory that matter for any compaction policy: **brevity bias**, which
drops domain insights for concise summaries, and **context collapse**, where
iterative rewriting erodes details over time. [S-160] is the honest field
assessment — memory is "fragmented, oscillating between operating system
engineering and cognitive science," and write policies, forgetting, and rollback
are unsolved.

**The consequence for a pipeline that does not want an agent memory.** If memory
write policy is unsolved, then *not having agent memory is a legitimate design*,
not a gap. File-state gates over immutable artefacts satisfy the same audit
requirement without the write-policy problem. [S-161] characterises writable
cross-session memory as "a qualitatively different threat landscape from
conventional input-centric security concerns" — persistence, statefulness, and
propagation across six lifecycle phases — which is the strongest argument
against introducing it casually.

**Sub-agent isolation, and its economics.** The thesis is [S-080]'s (above);
the economic argument is [S-002]'s — subagents "facilitate compression by
operating in parallel with their own context windows… and each subagent also
provides **separation of concerns**—distinct tools, prompts, and exploration
trajectories—which reduces path dependency." The countervailing cost is the 15×
token ratio and the extra call per invocation.

**Evaluation of growing context is unsolved.** [S-118] argues existing
long-context benchmarks "primarily focus on single-step settings" while agents
need evaluation "under a dynamically growing context."

**Evidence.** `PRIMARY` for the constraint and the techniques, `PEER` for
memory, and the memory-is-unsolved conclusion is a synthesis across [S-158],
[S-159], [S-160], [S-161].

---

## 4. Tools and protocols

### AO-004 — Tool design and tool-result economics

**The framing.** [S-006]: "Tools are a new kind of software which reflects a
contract between deterministic systems and non-deterministic agents."

**Design principles from [S-006]:** choose the right tools ("More tools don't
always lead to better outcomes" — prefer `search_contacts` over
`list_contacts`); namespace tools for clear functional boundaries; return
meaningful context optimised for token efficiency; and prompt-engineer the
descriptions.

**A measured demonstration that tool descriptions are the lever.** [S-006] built
an agent that, given a flawed tool, uses it and then rewrites the description —
"resulted in a **40% decrease in task completion time** for future agents using
the new description." Their shipped bug is the concrete case: the web-search tool
needlessly appended 2025 to the `query` parameter, biasing results, and the fix
was the description, not the model.

**The failure mode that predicts agent failure.** [S-006] and [S-004] both give
it: "bloated tool sets" that "cover too much functionality or lead to ambiguous
decision points." The test is human-decided: "If a human engineer can't
definitively say which tool should be used in a given situation, an AI agent
can't be expected to do better."

**Few-shot, narrowly.** [S-006] continues to "strongly advise" few-shot, but
against the enumerated-edge-case form: "teams will often stuff a laundry list of
edge cases into a prompt… We do not recommend this. Instead… curate a set of
diverse, canonical examples."

**Tool-result economics.** [S-005] names two pathologies: tool definitions that
overload the context window ("with thousands of tools, they'll need to process
**hundreds of thousands of tokens** before reading a request"), and intermediate
results that consume tokens on every pass ("Every intermediate result must pass
through the model. In this example, the full call transcript flows through
twice"). The same post's security corollary — routing data around the model
lets you "define deterministic security rules" — is why this is a design
constraint and not an optimisation.

**Evidence.** `PRIMARY`.

### AO-005 — Protocols: function calling, MCP, A2A, and the interop landscape

**Function calling** is the language-model-to-tool contract underneath
everything: schemas in, structured results out, the model choosing when to call.

**MCP**, launched [S-008] in November 2024, is the vertical layer — agent to
capability. Three dated revisions in roughly fourteen months:

| Revision | Date | What changed that matters |
|---|---|---|
| [S-030] | 2025-06-18 | JSON-RPC 2.0, capability negotiation, Resources/Prompts/Tools; normative: tool descriptions "should be considered **untrusted**, unless obtained from a trusted server"; sampling requires explicit user approval |
| [S-031] | 2025-11-25 | OIDC discovery; icons as metadata; incremental scope consent; first normative guidance on tool naming; elicitation rework incl. URL mode; **SEP-1303: input validation errors return as Tool Execution Errors, not Protocol Errors, "to enable model self-correction"**; JSON Schema 2020-12 default; experimental durable tasks |
| [S-032] | 2026-07-28 | **Core goes stateless** — `initialize`/`initialized` and `Mcp-Session-Id` retired, so any request can land on any instance behind round-robin; MRTR replaces server-initiated elicitation; header-based routing; cacheable lists; `Tasks` promoted to an extension; 12-month minimum deprecation window |

**SEP-1303 is the most transferable single decision in the protocol history.**
Treating recoverability as a protocol requirement rather than a courtesy — the
error must come back in a form the model can act on — is the same design as a
validation layer whose rejection message is the repair prompt.

**The stateless reset carries an admission relevant to AO-012.** [S-032]: "If
your server needs to carry state across calls, mint an explicit handle from a
tool and have the model pass it back as an argument. We found this works better
than session state hidden in the transport — the model can see the handle and
thread it between tools." Hidden orchestration state in the transport is the
wrong abstraction; state that the model can see and thread is a better one.

**A2A** is the horizontal layer. Launched by [S-034] with 50+ partners; the
current [S-035] v1.0 specification defines three bindings (JSON-RPC, gRPC,
HTTP+JSON/REST), IANA registrations, protocol negotiation, and **Agent Card
signing** — the first real agent-identity primitive in either protocol.

**The split, stated by the standards themselves.** [S-036]: "MCP is vertical. It
deepens a single agent. A2A is horizontal. It connects agents across that
boundary." With a usable domain test: MCP-domain things are stateless functions
with well-defined structured inputs and outputs; A2A-domain things "reason,
plan, and use multiple tools. They keep state over longer interactions and hold
complex, often multi-turn dialogues."

**Interop consolidated by merger, not coexistence.** [S-037] (ACP, the IBM/BeeAI
Agent Communication Protocol) now leads its own landing page with "ACP is now
part of A2A under the Linux Foundation" — absorbed within roughly eighteen
months. Recorded here as ecosystem evidence rather than as a technical claim.

**Ecosystem scale and governance.** [S-032] reports close to half-a-billion
monthly SDK downloads across Tier 1 SDKs, with TypeScript and Python each past
one billion cumulative, now governed under the Linux Foundation. [S-033]'s
2026 roadmap names **audit trails** as one of four top-priority enterprise gaps,
with the explicit expectation that fixes "will land as **extensions** rather than
core spec changes" — an acknowledgement that both A2A and MCP agree audit is not
yet solved.

**Observability for MCP exists but is immature.** [S-072] defines MCP
semantic conventions, with W3C Trace Context injected into `params._meta` and
traceparent/tracestate/baggage unprefixed per MCP SEP-414. Status: Development.
The non-obvious rule: MCP and transport contexts are independent, and if outer
GenAI instrumentation already traces the tool execution, MCP instrumentation
SHOULD NOT create a duplicate span.

**Security governance is being built in parallel.** [S-095] is the OWASP
governance framework for MCP adoption; [S-092] remains the canonical LLM risk-ID
vocabulary that everything else cross-walks to.

**Evidence.** `PRIMARY` throughout; the timeline is three frozen specifications.

---

## 5. Why multi-agent usually does not pay

### AO-006 — Multi-agent failure modes

**The central study.** [S-130] (MAST) is built on 1,600+ annotated traces across
seven MAS frameworks, with a 14-mode taxonomy in three categories — system
design, inter-agent misalignment, task verification — constructed from 150
expert-annotated traces at Cohen's κ = 0.88 and then scaled with an LLM-as-judge
pipeline. Its framing: "Despite enthusiasm for Multi-Agent LLM Systems (MAS),
their **performance gains on popular benchmarks are often minimal**."

**The load-bearing finding is the three-way split, not the headline.** One in
three MAS failures is a **verification** failure rather than a reasoning
failure. That is why the field's answer is verify-gated design (AO-007) rather
than better decomposition.

**The controlled scaling study.** [S-131] runs 260 configurations across six
agentic benchmarks, five architectures (single-agent plus independent,
centralized, decentralized, hybrid), and three model families, with tools,
prompts and compute standardised to isolate the architectural effect. Its
predictive model reaches cross-validated R² = 0.373, and it reports a **capability
saturation effect**: coordination yields diminishing returns once single-agent
performance is already high. This is the best available answer to "does
multi-agent help" — it helps in a specific, bounded region.

**Simple baselines are hard to beat.** [S-132] finds "a single agent can reach
the performance of **homogeneous** workflows with an efficiency advantage from
**KV cache reuse**, and can even match the performance of an automatically
optimized **heterogeneous** workflow," across seven benchmarks. [S-133] is
sharper still: a single LLM call with six few-shot examples achieves MCC 0.888
and F1 0.983, "outperforming the evaluated structured and multi-stage
alternatives," multi-agent verification included. [S-143] adds the process-model
version: across three different LLMs, multi-agent workflows "**reorganize,
rather than consistently enhance**, model performance."

**Five distinct failure mechanisms, each with its own paper.**

| Mechanism | Source | Statement |
|---|---|---|
| Coordination overhead | [S-138] | parallel speedups unrealised "due to costly coordination"; still 5–10% semantic conflict in the best observed form |
| Error propagation | [S-139], [S-137], [S-141], [S-140] | "erroneous information from the former agent will be propagated to the latter through prompts"; workflow performance "depends on the performance of each agent"; iterative debate is distilled into a *single* agent precisely because of "high computational cost and error propagation" |
| Ill-posed attribution | [S-136] | "multiple distinct interventions can independently repair the failed task" — log-only localisation yields untested hypotheses |
| Silent semantic failure | [S-135] | coordination over unstructured natural language "propagate[s] silently without raising runtime exceptions"; 15-type fault taxonomy |
| Correlated failure | [S-132] | homogeneous workers share priors, so the "diversity" multi-agent appears to supply is often not real diversity |

**Cost.** [S-002]'s ratios — agents 4× chat, multi-agent 15× — plus [S-060]'s
per-topology call counts, plus [S-138]'s finding that coordination can be *net
negative*. [S-002] draws the economic conclusion: "For economic viability,
multi-agent systems require tasks where the value of the task is high enough to
pay for the increased performance."

**The pro-multi-agent result, stated fairly.** [S-002] reports multi-agent
(an Opus-class lead with Sonnet-class subagents) outperforming single-agent by
**90.2%** on their internal research eval, and [S-163] reports 65.1% on
AlpacaEval 2.0 with open models against 57.5% for GPT-4o. These are real and
are not dismissed here.

**The reconciliation, which is the actual state of the debate.** Six points,
each traceable:

1. Multi-agent is not a default. [S-001], [S-010], [S-060] and [S-062] all say
   start with a single agent or a plain function.
2. Where it pays, the mechanism is **token expenditure on parallel independent
   exploration**, not collective intelligence. [S-002] is explicit: on
   BrowseComp, token usage alone explains 80% of performance variance, and
   "Multi-agent systems work mainly because they help spend enough tokens to
   solve the problem." The society-of-agents framing in that post is
   motivational, not causal.
3. It pays on breadth-first tasks with many independent directions, and does not
   pay when participants need shared context or tight dependencies — [S-002]'s own
   explicit exclusion, matching [S-080]'s two principles and [S-130]'s
   inter-agent-misalignment category.
4. It stops paying once base capability saturates [S-131].
5. Where the ensemble is homogeneous, a single agent with better context
   management reproduces most of the benefit [S-132], and the simplest
   configuration beats structured ones outright [S-133].
6. Heterogeneous ensembles are the configuration that survives scrutiny — which
   is what [S-002] actually ships, and is not what most multi-agent frameworks
   default to.

**Evidence.** `PEER` throughout, and the reconciliation is a synthesis across
[S-002], [S-130], [S-131], [S-132], [S-080].

---

## 6. The measurement problem

### AO-007 — False success and verify-gated completion

**This is the most important result in the catalogue for anyone designing an
agent harness.** [S-134] analyses 9,876 τ²-bench trajectories across 8 model
families and 1,879 AppWorld trajectories:

- **45–48%** of failures in single-control τ²-bench domains are false success
- **3%** in the dual-control telecom domain
- **75.8%** among AppWorld self-assessing coding-agent trajectories that make
  explicit status claims

**And LLM judges cannot detect it.** Across 5 judges, 5 prompt strategies, and
full task specifications, **no configuration exceeds AUROC 0.65** on τ²-bench;
the same judges reach only **0.54 AUROC** on AppWorld API-call traces. The judges
"rely on surface completion proxies — confident closing language and coarse
action-sequence volume — rather than verified state changes." A lightweight
TF-IDF detector reaches 0.83 AUROC, beating every judge.

**The rule that follows.** You cannot detect silent failure by asking the model
whether it succeeded. Verify against environment state.

**The independent convergence.** [S-130]'s "task verification" category is the
same finding from a different direction, and together they are why the field's
answer is verify-gated design rather than better planning.

**What a verify gate looks like.** [S-142]: "agents may **propose** completion,
but a read-only verifier decides whether the claim is **admitted**. Ambiguous or
weakly evidenced cases resolve **fail-closed**." Reported 1,791/1,800 = 99.5% on
the released known-outcome slice, with ambiguous cases the open problem. The
authors' own framing is a bound on what the released evidence supports — a
design pattern, not a validated result.

**Where abstention fits.** [S-108] supplies the complementary half: confidence
estimation lets a system "route the question to another expert, or otherwise
fall back on a safe default behavior." A verify gate *is* the safe default arm,
implemented deterministically.

**Evidence.** `PEER`, with `PRIMARY` convergence on the architecture.

### AO-008 — Benchmarks and their integrity

| Benchmark | What it isolates | Headline | Source |
|---|---|---|---|
| GAIA | reasoning + multimodality + browsing + tool use on "conceptually simple" questions | humans 92% vs GPT-4 + plugins 15%; 466 questions | [S-150] |
| AgentBench | agent behaviour across 8 interactive environments | "poor long-term reasoning, decision-making, and instruction following abilities are the main obstacles" | [S-151] |
| τ-bench | tool–agent–**user** interaction; policy adherence; **DB-state grading** | gpt-4o under 50% pass; under 25% pass^8 in retail; introduces pass^k | [S-152] |
| τ²-bench | dual-control environment; the user also mutates shared world state | the trajectory corpus [S-134] analyses | [S-153] |
| SWE-bench family | issue resolution in real repos | 32.67% of successful patches involve solution leakage, plus weak tests | [S-154] |
| SWE-bench-Live | continuously refreshed tasks | 1,319 tasks, 93 repos, one Docker task each | [S-155] |
| MCP-AgentBench | agent performance in MCP-mediated tool interaction | 33 servers, 188 tools, 600 queries | [S-157] |

**The three design decisions in τ-bench are the transferable ones** [S-152]:
grade against database state rather than transcript text, and treat reliability
across repeated trials (`pass^k`) as a metric distinct from capability. Both are
answers to the same problem [S-134] poses.

**The integrity lessons, which generalise past benchmarks.** [S-154] found that
a third of "successful" patches were leaks. [S-155] exists because static
benchmarks rot through staleness, narrow coverage, and contamination. [S-156] adds
test overfitting — "code that technically passes observed tests but actually
misses important cases" — which is the direct analogue of a pipeline artifact
that passes every automated check while being substantively wrong. [S-157] is the
2026 consequence: the harness and transports are now part of what is being
measured, because "existing benchmarks often fail to capture real-world agent
performance within this new paradigm."

**None of these numbers transfer to a document-generation pipeline.** They are
recorded to show what a serious agentic evaluation looks like, not as a
performance target.

**Evidence.** `PEER`.

### AO-009 — Eval harness design

**The distinction everything else hangs on.** [S-007]: "A flight-booking agent
might say 'Your flight has been booked' at the end of the transcript, but **the
outcome is whether a reservation exists in the environment's SQL database**."
The same post's warning is the reason agentic benchmarks are non-stationary:
Opus 4.5 "solved a τ²-bench problem about booking a flight by **discovering a
loophole in the policy**. It 'failed' the evaluation as written, but actually came
up with a better solution for the user." A benchmark can be defeated without
being broken, and no harness distinguishes the two.

**The shared vocabulary** [S-007]: *task* (test case), *trial* (one run — trials
exist because "model outputs vary between runs"), *grader* (logic scoring, with
assertions or checks), *transcript* (full trajectory), *outcome* (final
environment state), *evaluation harness* (runs tasks, records steps, grades,
aggregates), *agent harness* (makes the model an agent), *evaluation suite*
(tasks sharing a goal). Graders are code-based, model-based, or human, each
evaluating a portion of transcript *or* outcome.

**The framing sentence that should govern any A/B claim.** [S-007]: "**When we
evaluate 'an agent,' we're evaluating the harness and the model working
together.**" An A/B that varies orchestration while holding the harness fixed is
measuring what it says it measures; an A/B that varies both is measuring the
pair, and must say so.

**Judge reliability is the limiting factor, not judge sophistication.**
[S-134]'s AUROC ceiling is a property of the task, not of the judge
configuration. [S-002] found a single well-shaped judge call beat ensembles. The
consistent reading: when the test case has a known correct answer, the grader
should be deterministic code, and the LLM judge is for the open-ended residue.

**What an eval suite buys once it exists** [S-007]: baselines and regression
tests for free — latency, token usage, cost per task, error rates — and faster
model adoption, because a change stops being a leap of faith.

**Domain evidence that human review is not optional.** [S-175]: LLM-elicited
security requirements reached 98.5% on necessity but **44.4% on testability**
across five expert raters.

**Evidence.** `PRIMARY` for the framework, `PEER` for the judge ceiling.

### AO-010 — Observability and audit standards

**The span inventory that exists today.** [S-070] and [S-071] define
`create_agent`, `invoke_agent` (client and internal), `invoke_workflow`, `plan`,
and `execute_tool`, plus agent-skills sub-spans. [S-072] adds the MCP
conventions. **All three documents are status: Development** and now live in
their own repository. The trajectory is mature; the specification is not.

**Two rules with design consequences.** Retries belong inside a single span
[S-070] — the canonical encoding of a step-level retry. And `invoke_workflow`
existing as a first-class traced operation [S-071] is the standard's own name for
a pipeline stage.

**The security-side requirement is stronger than observability.** [S-094] (OWASP
Agent Observability Standard) requires three properties — inspectable,
traceable, instrumentable — and states the trace obligation as: "We can trace
back any action taken to the reasoning behind it and the originating task. Even
if the thread goes through multiple agents and software systems." It pairs this
with a Guardian Agent / Observed Agent split, OpenTelemetry plus OCSF, and an
AgBOM (Agent Bill of Materials) via CycloneDX / SWID / SPDX.

**This is a governance document, not a telemetry document.** Its reasoning is
that an agent nobody can inspect is a black box, and black boxes cannot be
audited. For an evidence-grade pipeline that is the governing requirement, and
it is higher than "log the inputs and outputs."

**Evidence.** `PRIMARY`.

---

## 7. Security

### AO-011 — Injection, tool poisoning, guardrails, and the limits of all three

**The core mechanism.** [S-081] names it: "LLMs follow instructions in content.
They don't just follow our instructions. They will happily follow any
instructions that make it to the model, whether or not they came from its
operator or from some other source." The *lethal trifecta* is three
co-occurring capabilities — access to private data, exposure to untrusted
content, and ability to communicate externally. Remove any one and the attack
does not work.

**The MCP-specific attack classes** [S-082]:

| Class | Statement |
|---|---|
| Rug pull / silent redefinition | "MCP tools can mutate their own definitions after installation. You approve a safe-looking tool on Day 1, and by Day 7 it's quietly rerouted your API keys to an attacker" |
| Cross-server tool shadowing | a malicious server overrides or intercepts calls made to a trusted one |
| Tool poisoning | malicious instructions hidden in tool *descriptions* — "visible to the LLM, not normally displayed to users" |
| Confused deputy | "any time you mix together tools that can perform actions on the user's behalf with exposure to potentially untrusted input" |

**The protocol's own position is the strongest evidence that this is unsolved.**
[S-030] makes it normative: tool descriptions "should be considered **untrusted**,
unless obtained from a trusted server." The protocol tells integrators that the
surface most tools present their behaviour through is untrusted input.

**Academic framing.** [S-164] offers design patterns with **provable
resistance** to prompt injection, with utility/security trade-offs worked through
case studies. That is the honest word: *provable resistance*, not a fix.
[S-081] on guardrail products is the correct scepticism to carry: confident
"95% capture" claims are "very much a failing grade" in application security, and
his verdict on the general mitigation problem is "I don't know what to suggest."

**Guardrail architecture that transfers.** [S-010] and [S-013]: guardrails are
layered — "While a single one is unlikely to provide sufficient protection, using
multiple, specialized guardrails together creates more resilient agents." The
part that is easy to get wrong in a multi-agent system is scope: **input
guardrails run only for the first agent, output guardrails only for the agent
producing the final output, and tool guardrails on every guarded invocation.** In
a workflow with managers, handoffs or delegated specialists, agent-level
input/output guards leave the intermediate calls unguarded; tool guards are the
ones that cover them.

**The allowlist primitive.** [S-013] rates each tool low / medium / high by
read-only vs write access, reversibility, required permissions, and financial
impact, then triggers automated action on high-risk tools. Execution modes matter:
**blocking** guarantees the expensive model never starts, whereas
parallel/optimistic execution may already have run. Tripwires are typed
non-model-mediated aborts.

**Escalation triggers.** [S-010] names two: exceeding failure thresholds, and
high-risk actions — "sensitive, irreversible, or have high stakes should trigger
human oversight **until confidence in the agent's reliability grows**."

**Sandboxing and bounded approval.** [S-011] documents Sandbox agents with a
Manifest, Permissions, SnapshotSpec and declared Capabilities (filesystem, shell,
memory, skills, compaction). [S-062] ships "don't-ask-again tool approval" as a
bounded-approval primitive.

**Supplies-chain governance.** [S-093] (OWASP Agentic Skills Top 10) treats
skills as a first-class attack surface because they "define how agents orchestrate
multi-step workflows"; its self-reported scan of 3,984 skills found 36.82% with
security flaws and 13.4% critical. Those are the project's own numbers — treat
them as indicative, not as independent measurement. [S-092] remains the canonical
risk-ID vocabulary, of which LLM05 improper output handling and LLM06 excessive
agency bear most directly on pipeline design. [S-090] is the 2026 agentic
top-level framework; note that its itemised ASI01–ASI10 entries are behind a
download and were not verified here, so no item names are asserted. [S-091] is the
threat-model-based reference. [S-182] records that a guardrail framework category
exists and is treated here as a survey, not as evidence. [S-096] and [S-097] are
the practical instruments: an executable security regression harness, and a
vulnerable-by-design application usable as a test corpus.

**Memory as an attack surface.** [S-161] characterises writable cross-session
memory by persistence, statefulness and propagation, across six lifecycle phases
including Forget and Rollback. Write-time controls — provenance, approval gates,
rollback — are the only mitigations the literature supports; there is no
consensus standard.

**The status of the problem.** Treat agent security as risk management, not a
solved problem. There are provable-resistance patterns [S-164], a deprecation and
consent regime in the protocol [S-030], [S-031], [S-032], and governance
standards [S-093], [S-094], [S-095], [S-096] — and a practitioner whose honest
conclusion is that he cannot suggest a general mitigation [S-081].

**Evidence.** `PRIMARY` for the protocol and vendor positions, `PEER` for the
academic framing, `PRACTITIONER` for the attack catalogue and the scepticism.

---

## 8. Determinism, auditability, and what remains open

### AO-012 — Constraining autonomy in a production system

**The consensus is not "make the agent deterministic."** It is: surround the
non-deterministic parts with deterministic, typed, auditable structure.

**The clearest commercial statement** is [S-061]: mix "deterministic steps with
agentic steps in a single graph," giving "fine-grained control over exactly where
and how AI is applied." The mechanisms that make it real are durable execution,
checkpointers, stores, fault tolerance, interrupts for human-in-the-loop, and
time travel.

**Declarative graphs versus code-first control flow is a genuine fork.**
[S-010] names it: declarative graphs give visual clarity and a constrained state
space but "can quickly become cumbersome"; its own SDK adopts a code-first
approach instead. The auditability argument pulls toward the graph; the
don't-pre-define-the-graph argument pulls toward code. Neither is wrong and
neither is settled.

**Allowlisted transitions, implemented in code rather than by the model.**
[S-013]'s guardrail scope rules are exactly this: which checks apply where is
decided by the harness, not negotiated by the LLM. A transition that aborts via a
raised tripwire was never a model decision.

**Tool risk ratings as an allowlist** [S-013] are the same mechanism one level
down: read-only tools run freely, write / irreversible / high-financial-impact
tools route to a human or a stricter check.

**State belongs where the model can see it.** The MCP 2026-07-28 reset [S-032]
is the clearest external statement: hidden transport session state is the wrong
abstraction, and an explicit handle the model threads between tools "works
better." For a pipeline this argues for artifacts the agent must name and
reference, rather than state it merely observes.

**What "harness" means has become a named layer** distinct from both the model
and the framework — [S-007] ("Claude Code is a flexible agent harness"),
[S-009] for the SDK, [S-062] for Microsoft's harness agent, [S-011] for sandbox
agents. Frameworks have converged on the same feature set: durable execution,
persistence, human-in-the-loop, compaction, sandboxing, tracing, skills.

**Determinism cannot be achieved by constraining reasoning.** [S-130]'s
verification category and [S-134]'s false-success rates together mean the only
credible route is verifying outcomes against environment state. [S-142]'s
fail-closed default is the shape of that route.

**Evidence.** `PRIMARY` for the architecture claims, `PEER` for the
verification argument.

### AO-013 — Open problems and unsettled ground

**Where there is genuinely no consensus:**

| Question | State of the field |
|---|---|
| Is multi-agent necessary? | Contested, trending no-by-default. [S-001], [S-010], [S-060], [S-062] all say start single. Against: [S-130], [S-131], [S-132], [S-133], [S-080]. For: [S-002] (+90.2%, conditional), [S-163] |
| What is the right unit of decomposition? | Unsettled. [S-001] splits pre-defined vs dynamically determined subtasks; [S-080] says do not decompose along output boundaries unless subtasks are independently answerable |
| How should memory work? | No standard. [S-160] calls the field fragmented between OS engineering and cognitive science; write policies, forgetting and rollback unsolved |
| Does self-correction work? | Weak. [S-134]'s judge ceiling undercuts using the same model as its own verifier; [S-159]'s context collapse is the mechanism by which iterative rewriting degrades |
| Model capability versus scaffolding? | Being measured. [S-002] reports a model upgrade as a larger gain than doubling the token budget; [S-131] finds capability saturation. Both say scaffolding has diminishing marginal value as models improve |
| Can silent failure be detected? | **No, and the negative result is strong.** [S-134]: 45–75.8% false success, no judge above AUROC 0.65, TF-IDF beats all of them |
| Is prompt injection solvable? | Consensus: not fully. [S-164] offers provable resistance patterns; [S-081]'s conclusion is "I don't know what to suggest" |

**What is maturing:** MCP (three dated revisions in fourteen months, ~500M
monthly SDK downloads, Linux Foundation governance, a 12-month deprecation
policy); A2A (v1.0 with three bindings, Agent Card signing, Linux Foundation
governance, ACP merged in); OpenTelemetry GenAI conventions (agent and MCP spans,
own repository, still `Development`); agent harness standardisation; and OWASP's
parallel governance stack.

**Where the ecosystem is actively split, and the split will not resolve soon:**

1. Harness vs framework vs runtime — [S-001] warns frameworks obscure prompts;
   every vendor now ships a harness layer.
2. Declarative graphs vs code-first control flow — [S-010] names the fork.
3. Centralized vs decentralized — [S-002] ships supervisor-workers, [S-010]
   documents both, [S-080] argues for neither.
4. Direct tool calls vs code execution for tools — [S-005] argues the latter on
   cost and context, and most framework docs have not caught up.
5. Session state in the transport vs in the model — [S-032] chose the
   model-visible handle; A2A keeps server-side context and task identifiers.
   These are incompatible philosophies and they will collide.
6. Agent identity and authorisation — A2A has Agent Cards and signing [S-035];
   MCP has OAuth and CIMD [S-032]; OpenTelemetry has `gen_ai.agent.id` as
   application-provided [S-071]. No cross-protocol answer exists.
7. Whether LLM judges are usable at all for agentic grading — [S-134]'s ceiling
   is a strong negative result the industry has not fully absorbed.

**Audit is the acknowledged open gap in both protocols.** [S-033] names it for
MCP; [S-035] does not claim to have solved it for A2A.

**Evidence.** Synthesis across the whole registry; each row is traceable to the
sources named in it.

---

## 8b. Survey coverage and unverified sources

Two sources in the registry could not be opened during this pass and are
therefore recorded as unverified and barred from carrying a quotation: an OpenAI
landing page that returned HTTP 403 on every attempt (its content is assumed to
be the PDF at S-010, which *was* read), and a vendor blog that S-005 cites as
independent corroboration but which was not read directly. `scripts/check_research_refs.py`
check R7 enforces that neither can acquire the authority of a citation, so no
claim in this catalogue rests on them.

General web search engines were CAPTCHA-blocked from the survey environment;
discovery ran through direct fetches of canonical URLs, the arXiv API, and
GitHub. The bias is toward sources already known to be canonical, and a 2025–2026
practitioner essay outside that set may have been missed. [S-100]'s
six-archetype breakdown was not confirmed from the paper body and is not asserted
anywhere above. The OWASP itemised agentic risk identifiers are behind a
download and are not asserted either.
