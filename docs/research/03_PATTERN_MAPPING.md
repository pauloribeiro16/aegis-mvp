---
document_id: AEGIS-RES-03
title: 'Pattern mapping — external evidence against the AEGIS implementation'
version: 0.1.0
created: 2026-10-03
status: ACTIVE
survey_date: 2026-10-03
sources: 'docs/research/sources.yaml'
upstream: 'AEGIS-RES-01, AEGIS-RES-02'
---

# Pattern mapping — external evidence against the AEGIS implementation

**What this document does.** It reads the two catalogues — pipeline patterns
(PP-nnn) and agent orchestration patterns (AO-nnn) — against the code that
actually runs, and answers four questions:

1. Does the external evidence support the architecture this repo chose?
2. Which named patterns are already implemented, and on what basis?
3. What is genuinely missing, and how bad is it?
4. Where is this implementation *ahead* of the literature, and where does it
   contradict the literature or itself?

**Verdict up front.** The architecture is on the right side of the evidence.
The workflow-over-agent decision, the deterministic context packs, the
zero-LLM assembly, the layered validation and the file-state gates are all
convergent with — and in several cases stronger than — the published guidance.
The gaps are real but narrow: **six of them, listed in §3.** The single largest
is that the pipeline has no defence against prompt injection, which the
literature treats as unsolved in general and therefore not excusable in a
pipeline that embeds untrusted prose verbatim.

**A note on scope.** This document reads the *implementation*, not the intent.
Where the two diverge, the implementation is what the finding says. Verdicts use
three values:

| Verdict | Meaning |
|---|---|
| `ADOPTED (convergent)` | the repo implements it, and the literature recommends it — the two arrived independently |
| `ADOPTED (independent)` | the repo implements it; the literature has no direct statement, or reaches it by a different route |
| `DIVERGENCE` | the repo does something the literature counsels against, on stated grounds |

---

## 1. The architecture the literature would have recommended

**The central decision** is ADR-010 D1: the pipeline is a prompt-chaining
workflow with deterministic gates and human gates, not an autonomous agent. Four
independent primary sources converge on exactly this for a predefined, auditable
procedure:

- [S-001] gives the distinction and the ladder, and says workflows are the right
  choice "for predictable and consistent" tasks.
- [S-010]'s three-condition build test ends with a fallthrough: "Otherwise, a
  deterministic solution may suffice."
- [S-060] states the conservative version outright: "a single agent with the
  right (sometimes dynamic) tools and prompt can often achieve similar results."
- [S-062] is the bluntest: "If you can write a function to handle the task, do
  that instead of using an AI agent."

**The strongest support for the decision is empirical, not rhetorical.**
[S-133] finds a single LLM call with six few-shot examples achieving MCC 0.888
and F1 0.983, "outperforming the evaluated structured and multi-stage
alternatives," multi-agent verification included. [S-132] finds a single agent
matches homogeneous multi-agent workflows *and* is cheaper, via KV-cache reuse.
[S-143] finds multi-agent workflows "reorganize, rather than consistently
enhance" model performance.

**The AEGIS pipeline run supports the same conclusion from the inside.**
EXP-01, the controlled A/B over the same case, corpus, model, parsers, gates,
assembler and validator, varying only who decides the working order: both arms
reached 65 goal rows and neither dropped an obligation. The pipeline did it in
**42 calls against the agent's 220**, and 1,304 s against 3,716 s. EXP-01's own
conclusion is the right one: the contract, not the orchestration, determines the
output. That is [S-130]'s finding that one in three multi-agent failures is a
verification failure, arriving from the other direction.

**One honest qualification.** [S-002] reports a +90.2% multi-agent result and
[S-163] reports 65.1% on AlpacaEval 2.0. Those are not noise, and [S-002]'s own
scope limit is the reconciliation: multi-agent does not fit "domains that require
all agents to share the same context or involve many dependencies." AEGIS is
precisely a shared-context task — 38 sub-domains against one frozen corpus, one
fact sheet, one set of confirmed regulations. ADR-010 D1 is right *for this
task*, and the reason it is right is that this task is not breadth-first.

**Conclusion: no change of direction is warranted.** The gaps in §3 are gaps of
rigour, not gaps of architecture.

---

## 2. Patterns already implemented

Twenty-two named patterns, each mapped to the catalogue entry and the code
carrying it.

| # | Pattern in the repo | Catalogue | Where | Verdict |
|---|---|---|---|---|
| 1 | Fixed LLM step sequence, code owns control flow | PP-001, AO-001 | `pipeline/src/run_pipeline.py` | `ADOPTED (convergent)` [S-001] |
| 2 | Deterministic routing on regulation/sub-domain presence | PP-002 | `pipeline/src/compose.py` (`candidate_subdomains`) | `ADOPTED (convergent)` [S-001] allows a non-LLM classifier; deterministic beats LLM routing on cost, audit and reproducibility |
| 3 | One LLM call per sub-domain (sectioning) | PP-003 | `pipeline/src/steps.py` (`stage_p4`) | `ADOPTED (convergent)` [S-001]'s sectioning rationale applies directly |
| 4 | Versioned prompt artefact, one per step | PP-021 #2 | `docs/pipeline/prompts/` | `ADOPTED (convergent)` [S-001], [S-002] |
| 5 | Deterministic context pack, no vector retrieval | PP-015, PP-014 | `pipeline/src/compose.py` (`build_pack`) | `ADOPTED (independent)` — see §4 |
| 6 | Programmatic gate between every step, error text is the repair prompt | PP-001, PP-016 | `pipeline/src/steps.py` (L0 repair retry) | `ADOPTED (convergent)` [S-077]'s single highest-leverage idea |
| 7 | Fenced-block parsing as the output contract | PP-008 tier 1 | `pipeline/src/steps.py` (`parse_p1`…`parse_p4t`) | `DIVERGENCE` — see §3 G1 |
| 8 | Deterministic assembly; the model emits no structural content | PP-020 | `pipeline/src/steps.py` (`assemble_doc`) | `ADOPTED (convergent)` [S-005], [S-137] |
| 9 | Control anchors derived by code, never emitted by the model | PP-020 | `pipeline/src/controls.py` | `ADOPTED (convergent)` [S-005] |
| 10 | Artifact-presence resume, not checkpoint replay | PP-018 | `pipeline/src/steps.py` (`stage_p4`) | `ADOPTED (convergent)` [S-002], [S-136] |
| 11 | Human gates as filesystem state, hard-refused by the runner | PP-018 | `pipeline/deucalion/gate.sh`, `steps.py` | `ADOPTED (convergent)` [S-007] |
| 12 | Layered validation L0/L1/L2/L4 with L3 demoted | PP-016 | `pipeline/src/validate.py`, `quality.py` | `ADOPTED (convergent)` [S-076] |
| 13 | Content gates derived from a red-team suite | PP-016 | `pipeline/src/quality.py`, `tests/quality_gate_test.py` | `ADOPTED (independent)` — see §4 |
| 14 | Flag-not-drop, repo-wide | PP-015 | across `steps.py`, `tools.py`, `compose.py` | `ADOPTED (independent)` — see §4 |
| 15 | Trim banners naming what retrieval omitted | PP-015 | `pipeline/src/compose.py` | `ADOPTED (independent)` — see §4 |
| 16 | Non-circular few-shot (example always from a different sub-domain) | PP-016 | `pipeline/src/compose.py`, `agent/tools.py` | `ADOPTED (independent)` — see §4 |
| 17 | Code-owned plan; deterministic next-step directive | AO-002, PP-013 | `pipeline/src/agent/loop.py` (`_plan`) | `ADOPTED (convergent)` [S-061], and the placement follows [S-116] |
| 18 | Anti-repetition at the code layer + progress watchdog | AO-004 | `pipeline/src/agent/loop.py` | `ADOPTED (convergent)` [S-002] |
| 19 | History elision so nothing remains imitable | AO-003 | `pipeline/src/agent/loop.py` | `ADOPTED (convergent)` [S-004] compaction, with a sharper threat model — see §4 |
| 20 | Phase-scoped tool surface (13 tools → 2–5 per phase) | AO-004 | `pipeline/src/agent/loop.py` | `ADOPTED (convergent)` [S-006]'s bloated-tool-set failure mode |
| 21 | One trace line per LLM call, with the failure named in the key | PP-017 | `pipeline/src/trace.py` | `ADOPTED (independent)` — see §4 |
| 22 | Version pinning and assertion of runtime values per run | PP-021 #7 | `pipeline/deucalion/phase1.sbatch`, `manifest.json` | `ADOPTED (convergent)` [S-042], [S-002] |

**Reading the table.** Eighteen of twenty-two are convergent, meaning the repo
did not need the literature to get them right and would have got them right if it
had never read it. Four are `ADOPTED (independent)` — the repo has a pattern the
literature does not name, covered in §4. One is a divergence, covered in §3.

---

## 3. The six gaps

### G1 — No schema-constrained generation

**Severity: high. Cost to close: low. Evidence: strong.**

The pipeline parses a fenced block out of free text and, on failure, retries with
the parser's own error message appended. That is PP-008 tier 1, which [S-046]
names as the anti-pattern: "Most solutions attempt to fix bad outputs after
generation using parsing, regex, or fragile code that breaks easily."

Three things make this worth closing now rather than later. First, the L0 repair
retry is the most expensive failure path in the pipeline, and format failures are
the failures it exists for. Second, the repair loop has a documented failure
mode of its own: a truncated response can still parse as L0 and be stored as the
artifact of record, which is why `done_reason == "length"` is now treated as a
retryable failure rather than a valid artifact. Third, [S-045] establishes that
constrained decoding is model-agnostic *by construction* — Qwen, Llama, DeepSeek,
Phi, Gemma — so the change is not a bet on the model.

**Caveat to carry into the experiment.** [S-014] documents two escape hatches —
refusal and max-token incompleteness — so constrained decoding removes the format
failure mode, not the truncation failure mode. And [S-179] finds strict format
constraints can cost reasoning quality; the mitigation that survives is to keep a
reasoning field in the schema. **Expect no improvement in goal quality. Expect
elimination of a whole class of retries.** If the experiment shows otherwise, the
finding is that the format problem was not the bottleneck.

### G2 — No prompt-injection defence

**Severity: high. Cost to close: medium. Evidence: strong that the problem is real, weak on mitigations.**

The pipeline embeds verbatim into the context pack: the company intake prose
(free-text, written by whoever filled the form), and large quantities of
regulatory corpus text. There is no treatment of either as untrusted content. A
grep for injection hardening across the pipeline source returns nothing; the only
structural defences present are source-anchoring, the retention floors, and file
delimiters.

**Why this is not excusable by appeal to "unsolved".** The literature's position
is that prompt injection is unsolved *in general* — [S-081]'s conclusion is "I
don't know what to suggest," and [S-164] offers *provable resistance* patterns
rather than a fix. But two things narrow the problem for this pipeline, and both
are structural rather than defensive:

1. **There is no exfiltration channel.** The lethal trifecta [S-081] names
   requires access to private data, exposure to untrusted content, *and* ability
   to communicate externally. The pipeline has no network egress from the model,
   no tool that sends data anywhere, and no tool surface at all in the pipeline
   arm. Two of the three legs are structurally absent.
2. **The blast radius is bounded by the gates.** The worst realistic outcome is a
   goal row that fails an L0/L1 check, or one that passes conformance and is
   substantively wrong — which is the [S-156] test-overfitting class, not a
   novel failure mode.

**So the correct reading is not "we are exposed" but "we have an unquantified
conformance-failure surface."** The experiment should measure how often injected
instructions in intake prose survive into a goal row, because that number is the
one thing currently unknown, and it is cheap to obtain.

**What the protocol says is worth reading anyway.** [S-030] makes it normative
that tool descriptions "should be considered **untrusted**, unless obtained from
a trusted server." A pipeline that embeds untrusted prose is running the same
class of exposure by a different route, and the protocol's own framing is the
clearest statement that this is the default assumption, not an edge case.

### G3 — No determinism control at the runtime level

**Severity: medium-high. Cost to close: low. Cost of closing: throughput.**

The pipeline runs `temperature: 0.2`, no seed, and no control over prefix reuse.
Three separate sources bear on this:

- [S-040] documents llama.cpp's default seed as `-1`, meaning random. A server
  given no seed is nondeterministic by configuration.
- [S-040] documents that `cache_prompt` "can cause nondeterministic results"
  because logits are not bit-identical across batch sizes — and prefix reuse is
  exactly what varies batch composition.
- [S-043] is the only first-class control found in any ecosystem, and it ships
  with vLLM. **There is no llama.cpp or Ollama equivalent.**

[Ollama exposes no equivalent of `cache_prompt`], so the achievable target is
PP-011 level 1: fixed seed, `--parallel 1`, explicit `num_ctx`. That is a real
guarantee improvement and it is not free in throughput.

**The honest framing, and it matters for how the result is read.** [S-040]'s
warning is a *vendor admission* and no independent study of determinism on
llama.cpp/Ollama was found at all. So the pipeline is currently in the state
[PP-011](01_PIPELINE_PATTERNS.md) calls level 0 — "None: defaults" — and the
question of how far it actually wanders is **unmeasured**. The experiment is as
valuable for the variance number as for the fix.

**One thing already done right.** Dynamic `num_ctx` escalation with an explicit
`num_predict` per step is PP-009 implemented properly, and treating
`done_reason == "length"` as a retryable failure rather than an artifact is
PP-012's countermeasure applied correctly. The commitment to this gap is about
the *sampling* controls, not the context controls.

### G4 — No evaluation across model and tool versions

**Severity: medium. Cost to close: low. Evidence: strong.**

`manifest.json` records the model string and the per-step `num_predict`/`num_ctx`
policy, and the trace records latency and token counts. Nothing compares runs
across a model, quantisation, or sampler change, and nothing would notice if
upgrading the model silently degraded goal quality.

**The documentary proof that this is a real risk, not a theoretical one:** four
Ollama documentation pages are live simultaneously and give three different
`num_ctx` defaults — 4096, 2048, 1024 in an example, and a VRAM-tiered ladder
[S-042]. The runtime this pipeline depends on does not agree with its own
documentation. The operational consequence is already adopted in the sbatch
script (assert the model manifest exists before serving, because compute nodes
have no egress) — the principle is right, it is just not applied across versions.

### G5 — L3 exists but is uninterpretable without a control

**Severity: medium. Cost to close: low. Evidence: strong, and it invalidates the current design.**

The validation stack is L0 (in-call) → L1 (deterministic) → L2 (in-prompt
self-checks) → L3 (LLM judge, demoted to advisory) → L4 (human gates). The
demotion of L3 was the right call, and the survey says it should be demoted
*further*, for two reasons that compound:

- [S-134]: across five judges, five prompt strategies and full task
  specifications, **no configuration exceeds AUROC 0.65** on agent outcomes, and
  0.54 on application traces. A lightweight TF-IDF detector beats all of them at
  0.83. A judge cannot reliably tell success from confident failure.
- [S-114]: a classifier trained on **rubric text alone**, never seeing the
  response, achieves nontrivial predictive power on judge outputs. The judge may
  be scoring the rubric. **A rubric-text-only baseline is now a mandatory
  control** — and it has never been run.
- [S-177] adds self-preference, which matters concretely here: the judge would be
  a qwen-family model scoring qwen3.8's output.
- [S-112] adds the killer for any A/B: reordering candidates in the context made
  a 13B model "beat" a frontier model on 66 of 80 queries. **Any future pairwise
  A/B between the pipeline arm and the agent arm runs on an instrument with a
  demonstrated failure mode that large.**

**The one positive result worth adopting** is [S-002]'s: a single well-shaped
judge call — one prompt, 0.0–1.0 scores plus pass/fail — was more consistent and
better aligned with human judgement than multi-judge ensembles. Ensembles are
not the answer; a cheap deterministic validator is.

**The visible symptom in the repo:** EXP-01's L2 human blind-scoring table is
empty. The quantitative half of the experiment was never run, and the L2 rubric
is exactly the artefact [S-114] says cannot be trusted without its control.

### G6 — Track B has no rows beyond MICRO

**Severity: medium. Cost to close: low (research, not engineering). Evidence: n/a — this is a completeness gap, not a design error.**

The Track B matrix has a single `MICRO` row. A case at any other scale raises
"no Track B matrix rows defined for scale" and hard-fails — which is the correct
behaviour (fail loudly, per the flag-not-drop invariant) but it means the pipeline
cannot currently process anything but a micro-company.

No source in the registry speaks to this, because it is not a literature
question. It is a corpus-completeness question, and it is listed here because it
blocks the obvious next case.

---

### The gaps in one table

| ID | Gap | Severity | Cost | Experiment | Evidence grade |
|---|---|---|---|---|---|
| G1 | No schema-constrained generation | high | low | E-01 | `PRIMARY` |
| G2 | No prompt-injection defence | high | medium | E-02 | `PRIMARY` + `PRACTITIONER` |
| G3 | No runtime determinism control | medium-high | low (throughput) | E-03, E-07 | `PRIMARY` (vendor admission) |
| G4 | No cross-version evaluation | medium | low | E-08 | `PRIMARY` |
| G5 | L3 uninterpretable without a control | medium | low | E-04, E-05 | `PEER` |
| G6 | Track B beyond MICRO | medium | low (research) | E-06 | n/a |

**Not a gap, worth stating explicitly:** multi-agent orchestration. The evidence
is against it for this task shape (§1), the internal A/B agrees, and the agent
arm is a working but non-recommended comparison point. It stays as an arm in
EXP-01 because the controlled comparison is valuable, not because the agent is
the better path.

---

## 4. Where this implementation is ahead of the literature

Seven things the repo does that the surveyed literature either does not name, or
names only as a passing observation. This section exists because a gap analysis
that only lists deficits misrepresents the state of the work.

**1. Flag-not-drop, as a repo-wide invariant rather than a local convention.**
Anything that fails a check is recorded and flagged: excluded sub-domains need a
why-not, `None.` tension results need a reason (the agent path rejects a bare
`None.` without a `none_reason`), failed stages get a `status: "aborted"` manifest
entry, retrieval trims carry a visible banner, and retained failed calls stay in
`trace.jsonl` as history. The literature's nearest neighbours — [S-073]'s "add
real traces to a dataset so a failure you saw once becomes a test" and [S-135]'s
finding that semantic failures "propagate silently without raising runtime
exceptions" — describe the *problem* this invariant solves. None of them
prescribes the invariant.

**2. Content gates derived from a red team, and a test that asserts each gate
fires by name.** `quality.py` exists because a red team injected defects that
passed every automated check. `tests/quality_gate_test.py` then injects each
defect class and asserts it is rejected *by name* — meta-goals, verbatim Sub-SO
copies, technology leakage, invented quantities, phantom regulations, silent Sub-SO
drops, out-of-vocabulary Adjustments. [S-096] argues that security checks which
run once are not a control, and [S-114] shows why a validator that cannot detect
its own blind spots is worse than none. A gate suite whose every case is named is
the mechanism that makes blind spots enumerable.

**3. Gate-firing-rate auditing.** PLAYBOOK D1's rule is "a gate that never fires
is not a constraint" — and the 0.88 near-verbatim similarity gate was measured at
a maximum of 0.79 across 65 rows, then *documented as inactive* rather than
silently retained. No source in the registry proposes measuring whether a
validator ever fires. [S-077]'s eval discipline is the closest, and it measures
model output quality, not validator liveness. This is a small idea with a large
expected payoff and it is already in the repo's vocabulary.

**4. The obligation-retention floor uses an absolute count, not a ratio.** The
30% retention gate is expressed as an absolute proportion of terms retained, with
the reason recorded in the code: mid-size models handle absolute counts, not
aggregate ratios. The error message lists the missing terms and embeds the
baseline text verbatim, so the model is told what it dropped rather than being
told a percentage. This is [S-077]'s "using the assertion error to course-correct"
taken one step further, into the *content* of the assertion. The literature has
the general principle; the specific calibration is this repo's own.

**5. Anti-circular few-shot.** The worked example injected into the P4 pack is
always drawn from a *different* sub-domain than the one being written, with an
explicit instruction not to copy its text and to match its calibration. [S-133]
makes the strongest empirical case for few-shot — six examples in a single call
beating structured multi-stage alternatives — and [S-001] and [S-006] both advise
few-shot with canonical examples. None of them address the case where the example
and the target are the same unit of work, which is precisely the self-plagiarism
hazard in a per-sub-domain loop.

**6. Anti-circular testing as a stated rule.** R10 requires that no task be
declared complete without physical evidence from the target files, that automated
tests are "necessary but never sufficient on their own," and that a test must not
merely confirm the assumptions of the code just written. `verify_no_loss.py` is
written to re-derive the corpus proof *without* reusing the generator's parsing
logic. `assemble_real_test.py` exists because the synthetic end-to-end test could
not show what real prose renders like. [S-136] supplies the reason from the
agentic side — single-intervention attribution is ill-posed, because multiple
distinct interventions can independently repair a failed task. R10 is the
methodological answer.

**7. Egress-free stdlib discipline as a constraint that improved the design.**
Every module under `pipeline/src/` is standard-library only, including a
hand-written YAML subset parser and a hand-written ficha parser, because compute
nodes have no pip egress. The side effect is that the trace and manifest schemas
have no schema-validation dependency at all, which means they are readable and
checkable by hand — which is what makes R10's physical inspection practical. This
is the rare case where a constraint improved the artefact.

---

## 5. Contradictions, stated honestly

Four places where the repo, the literature, or the repo's own documents disagree.
None is resolved here; each is stated so it can be decided deliberately.

**C1 — ADR-010 D1 rejected agents; an agent arm exists; D4 is unratified.**
`docs/decisions/ADR-2026-10-01_pipeline-architecture.md` D1 records "Workflow,
not agent… No LLM-directed control flow, no cross-phase autonomous loops." D4
records the orchestration runtime as deferred, and the ratification checklist
still has a blank line for it — while the runtime was built and the agent arm
runs in EXP-01. The architecture is not wrong; the record is behind the code.
This is a documentation decision the researcher owes, not a technical finding.
Note that §1 and [S-002] both indicate the D1 decision was correct, so the
ratification should be of D4's *existence*, not of D1's reversal.

**C2 — L3 was demoted to "advisory, and only where calibrated"; the survey says
it should be nearly removed.** The demotion was a correct reading of [S-111],
[S-112] and [S-113]. [S-114] and [S-134] are stronger still and arrived later:
the judge cannot reliably detect false success at all (AUROC ≤ 0.65), and a
rubric-only classifier can predict its scores. The remaining defensible use is
progress detection on open-ended residue, never admission control. G5 and E-04
are how this gets closed; until then L3 should be described as unvalidated
rather than as advisory.

**C3 — The 0.88 gate is retained but known to be dead weight.** The design
principle is flag-not-drop, which argues for keeping it. The measurement says
it never fires (max 0.79 over 65 rows). Both positions are defensible and they
are in genuine tension. PLAYBOOK D1 records the decision to retain and document
rather than remove, with the reason "removing a safety gate is a human call" —
which is the right resolution of the tension, and E-10 exists to close the
measurement so the next decision is made on data rather than on principle.

**C4 — "0.30 retention floor versus a company-proportional restatement" is the
binding constraint, and it may be the rubric's fault.** EXP-01's finding 5 is
that both arms converge on the same failure: the retention floor asks for enough
of the baseline obligation to survive, while the rubric asks for a restatement
proportional to the company. Median observed retention is 73% with a minimum of
32%, so the floor is reachable — but only after retries, and the agent never got
past 11–27% alone. PLAYBOOK D2's formulation is the right one: "A gate can be
right and still be the bottleneck." This is a genuine open question about the
gate's calibration, not a defect in either arm, and it is not resolved by
anything in the current registry.

---

## 6. What follows from this

The backlog in [04_EXPERIMENT_BACKLOG.md](04_EXPERIMENT_BACKLOG.md) carries
twelve experiments, ranked by (gap severity × evidence strength) ÷ cost, each
with one isolated variable, a primary metric, an estimated GPU cost, a success
criterion, and a statement of what changes if it wins and if it loses.

Three framing notes for whoever picks it up:

**The ranking is by evidence strength as much as by severity.** G2 has the
highest severity but the weakest *mitigation* evidence — [S-164] offers provable
resistance patterns and [S-081] offers nothing. E-02 is therefore scoped to
*measuring* the exposure rather than to eliminating it, because a number is
achievable and a fix is not yet.

**E-04 and E-05 are prerequisites for reading any future A/B result.** A judge
that cannot detect false success at AUROC 0.65, and a rubric-only classifier that
predicts the score, mean an A/B between arms scored by that rubric measures the
rubric. Both experiments exist to make a later comparison credible.

**E-03 is worth running even if the fix is rejected.** The pipeline's current
reproducibility is unmeasured. Knowing the variance is worth more than assuming
it, and the measurement is cheap.
