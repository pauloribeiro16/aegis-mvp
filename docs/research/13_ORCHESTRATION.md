---
document_id: AEGIS-RES-13
title: 'LLM orchestration — annotated catalogue of the open gaps'
version: 0.1.0
created: 2026-10-05
status: ACTIVE
survey_date: 2026-10-05
sources: 'docs/research/sources.yaml'
---

# LLM orchestration — annotated catalogue of the open gaps

**What this document is, and what it is not.**
[02_AGENT_ORCHESTRATION_PATTERNS.md](02_AGENT_ORCHESTRATION_PATTERNS.md) is a
complete catalogue of orchestration *patterns* — `AO-001`..`AO-013`, topologies,
protocols, multi-agent failure modes, benchmarks, observability, security. It
is not rewritten here, and nothing below contradicts it.

This catalogue covers the seven gaps `AO-013` itself listed as open, plus one it
did not: durable execution semantics, scheduling, human-in-the-loop as a
primitive, the framework landscape read on execution and state rather than on
marketing, cost and latency as measurements, agent-to-agent communication
semantics, agent identity, and evaluation methodology. `OR-001`..`OR-009`.

**Method.** Same pass and same declared bias as
[12_PROMPT_ENGINEERING.md](12_PROMPT_ENGINEERING.md): `WebSearch` unavailable
throughout, discovery via arXiv API, direct canonical fetches and GitHub raw
document sources. That bias is *milder* here than on prompt engineering, because
this front is documentation-heavy rather than blog-heavy — the framework and
protocol sections were read at official docs, not at secondary summaries.

**The two findings that most affect this repo, stated up front.** First,
durable execution vendors do not claim exactly-once for an LLM call, and the
one that is most explicit about it derives the repo's own seeding discipline from
replayability [S-362, S-363]. Second, human-in-the-loop approval gates do not
have barrier semantics in any of six surveyed frameworks [S-368] — which
exposes the repo's verify-gated completion pattern to a threat its catalogue
does not currently name.

---

## 1. Durable execution

### OR-001 — Durability is per-step memoisation, not exactly-once

Every vendor in this survey converged on the same split, and it is a split on
determinism rather than on retries. Temporal: *"Workflow code must be
deterministic because Temporal reruns it to rebuild state after a failure"*, and
anything external belongs in an Activity [S-361]. DBOS: *"once a step completes
and is checkpointed, it is never re-executed"*, while steps *"should be
idempotent"* [S-364]. Inngest is the most explicit, and its honesty is the
useful part: **"A step does not make an external action exactly once"**, with an
idempotency key prescribed for effects that must not repeat [S-362].

**This is the answer to "what does durability mean when a step is a
nondeterministic LLM call" — and the answer is that the guarantee is bounded by
the step boundary.** No vendor surveyed claims exactly-once for the call itself.

**The strongest external corroboration the repo's seeding default lacked.**
Inngest's guidance is to keep *"random values, the current time, and API
calls"* inside durable steps so that *"a resumed run makes the same
decisions"* [S-363]. That is the same content as AGENTS.md §-1's `seed=42`
requirement, reached from a **replayability** rationale rather than a sampling
one. It converts the seeding default from a measured preference into the price
of resumable execution, which is the stronger claim and the one §-1 was already
reaching for.

**The framework that took the other route** re-executes instead of demanding
determinism: *"Nodes after the checkpoint re-execute, including any LLM calls,
API requests, and interrupts… Replay re-executes nodes — it doesn't just read
from cache"* [S-365]. That is a legitimate design, and it is also a bill the
user pays; the point for the repo is that a durable layer can be had *without*
reproducible calls, provided the cost is known rather than discovered.

### OR-002 — Durability has become a pluggable axis, and two primitives matter

The 2026 architecture is agent-framework × durability-engine. Pydantic AI states
it most directly: *"Durability is not storage… Each engine wraps every model
request and tool call as its own durable unit"* [S-367]. Temporal ships
first-party adapters for LangGraph, OpenAI Agents SDK, Mastra, Pydantic AI and
several more.

**The consequence for ADR-010 is that the repo's decision is one axis of a
two-axis decision it has not named.** "Workflow versus agent" and "which
durability engine" are independent choices, and only the first is currently
written down.

**Two primitives from LangGraph are worth stealing on their own merits** [S-366]:
the **super-step**, a single tick of the graph in which all nodes scheduled for
that step execute, with a checkpoint at each boundary — a coarse, named resume
granularity that suits a staged pipeline; and **pending writes**, where a
failing node's siblings' writes survive and are not re-run on resume — the
partial-failure-recovery primitive the current catalogue lacks.

---

## 2. Scheduling and concurrency

### OR-003 — Parallelising independent calls is safe at the DAG layer and unsafe at the serving layer

**Good news first.** The orchestration layer can parallelise freely: branches
execute concurrently and *"the results are still correct"* regardless of
completion order, provided the aggregator reads declared position rather than
arrival order. Haystack corroborates from the other side — components run in
parallel when dependencies allow, and in-flight work is cancelled and drained
before the original error is re-raised.

**The hazard is one layer down, and it is a measured one.** Batch-dependent GPU
execution changes kernel tiling and floating-point reduction orders, so seeded
generation can still vary: standard vLLM reproduced **22 of 55** label flips on
known score-flip candidates, while batch-invariant kernels reduced the same test
to **0 of 55** [S-375].

**This bounds AGENTS.md §-1 and should be stated there.** "Zero residual
variance from the serving layer" is a property of the **endpoint
configuration**, not of seeded sampling. It is true against a hosted API and is
not a general law. The actionable consequence is small and concrete: record the
serving configuration in `config.json`, because the determinism claim's scope
depends on it.

### OR-004 — Human-in-the-loop gates are a narration, not a barrier

**This is the most uncomfortable finding in the block.** Control primitives in
production agent frameworks carry names and documentation implying barrier
semantics — *while a run is paused, cancelled, or timed out, no gated side
effect executes*. *"This contract holds on none of six widely used open-source
frameworks."* The specific leak is a **sibling effect executing during a
sibling's pause**, defeating rejection [S-368].

**A second, independent failure class: the dialog is agent-authored.** *"The
human approves a summary the agent writes"*, and that summary is forgeable, so a
compromised agent can display a benign description while a different action runs
[S-369].

**A third: more oversight can be less safe.** Reviewers "only moderately agree on
what is risky (Fleiss' kappa = 0.52)," and *"realized safety becomes an
inverted-U in the escalation rate: more human oversight can make a system less
safe"* [S-370]. A kappa of 0.52 also means human review of a grounding decision
has no ground truth, which bounds any human arm the repo might add.

**What the field does agree on** is the positive pattern, and it is
well-specified: block with a timeout, capture the decision as **structured
data rather than a boolean** — *"the approval decision, approver details, and
comments"* — and route timeout expiry to an explicit branch [S-371]. Capturing
who approved and why is an audit requirement, and it is exactly what a boolean
gate omits.

**The verdict for this repo: `AO-007`'s verify-gated completion is exposed.** A
gate that the pipeline's own code evaluates and that no model participates in is
in a materially better position than one narrated through an approval dialog —
which is the design the repo already chose. That should be stated as the reason,
because the current catalogue records verify-gating as good practice without
recording that the alternative is worse than documented.

---

## 3. Cost, latency, and the accounting rule

### OR-005 — Cost and latency have different optima, and a cost number needs an accounting rule

**The asymmetry.** *"In MAS, end-to-end latency is governed by the critical
execution path, so reducing total cost alone does not reliably reduce latency"*
[S-373]. The repo's EXP-03 reports calls and context as cost proxies and
records no critical path, so its cost result is not yet a latency result.

**A routing number is a property of the router, not of the model pair.** The
transfer result is the operative clause: routers "maintain their performance
even when the strong and weak models are changed at test time" [S-372]. Any
threshold in `METRICS.md` citing a routing saving must carry the model-lineup
dependency, because the number is void the moment the lineup changes.

**The cost column `AO-002`'s topology table lacks exists.** AgentPrune reaches
comparable results to state-of-the-art topologies at $5.6 against their $43.7,
with 28.1–72.8% token reduction — and *improves* accuracy by 3.5–10.8% by
removing adversarial messages [S-374]. **Removing redundant inter-agent traffic
made the system better, not worse**, which is the strongest external
corroboration available for the repo's minimal-context workflow arm, and it
sits comfortably alongside EXP-03's own 4.8× calls / 6.4× context measurement.

**And the accounting rule is not optional.** Across a structured audit of 50
popular repositories, *"changing only the reporting rule can change reported
scores by 20.9 absolute percentage points and, in some cases, invert rankings
of frontier models"*, and *"none report how many runs failed, errored, or were
skipped alongside headline scores"* [S-383].

**Two consequences, one in each direction.** A cost number without a declared
accounting rule is not a measurement — so `trace.jsonl` should record the rule
(what counts as a call, whether replayed or aborted steps are counted), not
only the values. And in the other direction: **EXP-03's disclosure of a 53%
clean-termination rate is a rarity by this standard and should be claimed as a
methodological strength**, because the denominator is what makes the other
number interpretable.

---

## 4. Communication, identity, and protocols

### OR-006 — The field converged on state-in-model; `AO-013`'s split #5 is narrower than stated

`AO-013` lists "session state in the transport vs in the model" as an unsettled
split. A2A v1.0 read directly resolves it for the A2A class: a `contextId`
"logically groups multiple related Task and Message objects," server-generated
values "SHOULD be treated as opaque identifiers by clients," and agents "MAY
use the `contextId` to maintain internal state, conversational history, or LLM
context" [S-379]. **State lives server-side behind an opaque handle, never in
the payload.** The spec also mandates rejection of mismatched `contextId`/
`taskId` — a referential-integrity guarantee, the same class of check the repo's
own `check_traceability.py` performs.

**Two positive facts to record, because the registry's tone on A2A is mostly
negative.** The schema-evolution story is mature: renames keep old names
"available, but marked deprecated, until the next major release," removal
"SHOULD NOT" precede the next major version, and a renames appendix with a
deprecation schedule is mandatory. That is stronger than the equivalent
provision in MCP, and it is worth having on record.

**The live split is A2A versus MCP-local-process designs, not transport versus
model** — which is a correction to `AO-013` rather than a defence of it, and
the kind of correction a one-page-per-protocol catalogue cannot detect.

### OR-007 — Seeded sampling plus batching is a configuration, not a guarantee

Covered with its measurement in `OR-003`; recorded separately because it is the
one place where the orchestration layer and the serving layer produce the same
failure from opposite directions, and the repo's determinism claim depends on
which one is in play. The paired protocol is the instrument: 55 known score-flip
candidates, 22 reproduced under standard vLLM, 0 under batch-invariant kernels
[S-375].

### OR-008 — Evaluation methodology, and the noise floor for any future A/B

**The number that governs the repo's next experiment.** Over 60,000 trajectories
on SWE-Bench-Verified: *"single-run pass@1 estimates vary by 2.2 to 6.0
percentage points depending on which run is selected, with standard deviations
exceeding 1.5 percentage points even at temperature 0"*, and therefore
*"reported improvements of 2--3 percentage points may reflect evaluation noise
rather than genuine algorithmic progress"* [S-376].

**This is the paper pair with EXP-02 that lets ADR-010 be defended on
measurement grounds rather than only cost grounds** — pipeline sd = 0.0000
versus agentic sd > 1.5 pp at temperature 0 is now an *empirical* difference
between the two arms, not an assumption. Note the scope limit honestly: the
noise floor was measured on scaffolded agents, so it bounds what an agentic arm
can be expected to deliver rather than contradicting the repo's own pipeline
result.

**The instrument the backlog lacks.** Intraclass correlation decomposes
observed variance into between-query and within-query components, converges by
**n = 8–16 trials for structured tasks and n ≥ 32 for complex reasoning**, and
yields the rule that *"accuracy improvements are only trustworthy if ICC also
improves"* [S-377]. The repo's EXP-03 ran n = 15 per arm with no power
argument; these are the figures that would have supplied one.

**The caveat ADR-010 needs attached before it is cited anywhere.** Across 66
model × harness configurations, model rankings **reverse** between harnesses —
Claude leads GPT by 7.94 points in one and trails by 30.16 in another — and
"higher cost does not reliably buy a higher score" [S-378]. The harness is a
confound large enough to invert a comparison. This does not change ADR-010; it
says the ADR must be defended on harness-controlled grounds, which EXP-03
already is, and the pre-emptive citation belongs in the ADR itself.

### OR-009 — Agent identity: the substrate is settled, the deployment is broken

`AO-013` says "no cross-protocol answer exists" for agent identity. That remains
true, and it is now precisely characterisable in four parts:

1. **The substrate is settled.** RFC 8693 token exchange is the only normative
   delegation grant, and its delegation semantics are unambiguous: *"With
   delegation semantics, principal A still has its own identity separate from
   B"* [S-381].
2. **A2A delegates authorization out and reinvents it in-task.** *"Authorization
   boundaries are defined by each agent's authorization model, not prescribed by
   the protocol"*, and payloads carry no identity — the client obtains
   secondary credentials "through a process external of the A2A protocol
   itself" [S-380]. That is RFC 8693 token exchange in all but name.
3. **MCP forbids exactly what A2A requires.** MCP's confused-deputy defence is
   explicit and includes a hard negative constraint: clients must not send
   tokens the server's own authorization server did not issue, and servers must
   not accept or transit any other token. **The two models are directly
   incompatible**, and that incompatibility is the concrete content of
   `AO-013`'s open problem.
4. **The deployment is measurably broken.** Across four frameworks and a
   reference agent runtime, three provide no built-in confinement and one only
   partial; *"no existing standard alone covers the requirement set"*. The
   governing standard offered is the right one to adopt: *"a correct system is
   one in which a fully prompt-injected agent still cannot exceed the authority
   explicitly delegated to it"* [S-382].

**The regime-mismatch warning is the line worth keeping.** Authorization
enforced *inside the model* is not an authorization decision, because the threat
model assumes the component driving each agent is a language model an adversary
can hijack. This is orthogonal to the workflow-versus-agent choice — **both**
arms must keep authorization outside the model, and saying so costs nothing.

---

## 5. What this survey could not establish

1. **Whether replayed LLM steps actually diverge under a fixed seed.** No
   vendor has published that measurement. The repo's own EXP-02 result
   (retention sd = 0.0000) is, as far as this pass found, a stronger empirical
   claim than anything in the vendor literature — which is worth stating in the
   registry rather than leaving implicit.
2. **Rate-limit-aware orchestration.** Essentially undocumented academically; the
   vendor pages are step-level and function-level respectively, and neither
   substitutes for a provider-side contract. AEGIS would have to preregister
   its own overflow behaviour.
3. **A framework that satisfies all three HITL constraints simultaneously** —
   a real barrier, a non-agent-authored dialog, and a reviewer with capacity.
   The field has a consensus implementation and a consensus refutation; nobody
   has published a design meeting both.
4. **The cost of context to a regulatory anchor** rather than to a token type —
   carried over from [11_CONTEXT_MANAGEMENT.md](11_CONTEXT_MANAGEMENT.md) §5.
