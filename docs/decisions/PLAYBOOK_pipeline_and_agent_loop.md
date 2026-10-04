---
document_id: AEGIS-PLAYBOOK-01
title: 'Building a Phase-1 pipeline and a directed agent loop on a local LLM'
version: 1.0.0
created: 2026-10-03
status: ACTIVE
---

# Playbook — pipeline and agent loop on a local LLM

Lessons from building and running both arms on Deucalion with `qwen3.8:27b` via
Ollama. Written so the next iteration does not re-derive them. Each item says
what happened, so it can be recognised.

---

## A. Orientation — start here, it saves the most time

**A1. Compare against a baseline of the same size, or don't compare at all.**
The pipeline produced 63/65 rows with `unchanged` adjustments; a hand-written
4-row example had zero. That looked like a systematic calibration failure. It
was not: the 4-row example was a *different company* (its app was run by an
external software house, so every duty genuinely narrows to a delegation),
and n=4 cannot support a distribution claim. Read the actual rows before
concluding anything from a statistic.

**A2. Verify the file you are being shown actually exists and is current.**
Several conclusions here were wrong because the analysed file was a legacy
artefact (an 8-column run from before the current contract). Diff the artefact
against the current contract before analysing it.

**A3. When a stage aborts repeatedly on the same unit, suspect the corpus, not
the model.** 11 of 38 sub-domain modules carry a `regs/<REG>.md` file with *no
Sub-SO card* (the file literally ends `_(no ... Sub-SO or requirements in this
sub-domain)_`) while its header says "applies when GDPR is in scope". The model
reads "applies", writes a row, and the gate rejects it — correctly. The fix is
to tell the model the concrete list of Sub-SO ids the module declares.

---

## B. Prompt design for a mid-size local model

**B1. Absolute counts beat percentages.** "Keep at least 9 of these 30 terms"
is followed; "keep ≥30% of the terms" is not. Aggregate numeric ratios are the
encoding small models handle worst, and the failing behaviour is systematic:
27B-class models are biased short against length-type constraints.

**B2. Never make the model see a list that is an example of a different
serialisation format near a structured-output turn.** A YAML/bullet template
inlined in a prompt gets copied into the JSON arguments. An elision placeholder
`[elided — …]` in the history was re-emitted verbatim as a tool argument and
killed the call. Anything you put in context can be imitated; put nothing
imitatable in context.

**B3. A worked example from a *different* work unit is the strongest single
calibration signal — and it must not be the unit being written.** Inject a
completed block of another sub-domain. Never the current one: that is handing
over the answer, and it makes the run unevaluable.

**B4. Give a decision rule, not a menu.** For a three-valued field, "use
`unchanged` only when X, otherwise `narrowed` when Y, `flagged` when Z" works;
listing the three values and calling them a vocabulary does not — the model
defaults to the first.

**B5. Do not tell the model "don't shorten" or "don't loop".** Constraint-
reflection and chain-of-thought measurably *reduce* faithfulness on summarisation
tasks and can make constraint-following worse. Put the requirement in the
artifact to be produced, not in an admonition.

**B6. Show the model the source it must cover, at the moment it must cover it.**
A rejection that names missing *words* but not the source text produces
identical retries. Carrying the baseline verbatim in the rejection fixed a
loop where both arms sat at 11–27 % retention forever.

---

## C. Agent loop mechanics

**C1. Repetition is a code problem. Prompt instructions do not prevent it.**
163 byte-identical read calls in a row, every one returning success. Guard it
with a canonical `(tool, normalised args)` signature, and refuse the repeat with
the **next step**, not a warning — a warning appended to a 12 KB result
drowns and the model re-latches.

**C2. Own the plan in code when the work is enumerable.** With 38 discrete
units, "is this a repeat?" becomes a set membership test. The model never gets
to answer it, which is the point. Directive is appended at the *end* of the
context each turn, where long-context models attend best.

**C3. Break loops in band.** Return the refusal as the tool's normal observation
with two concrete exits. Raising loses the model's ability to recover. Add a
progress watchdog on the on-disk artifact set: no new artifact for N turns is
a degenerate loop — abort cleanly so the resume re-anchors.

**C4. Long tool-call arguments are the single most common hard failure.** A
truncated argument yields malformed JSON and the server rejects the call with
no usable response. One row per call, not a table. Raise the output budget
rather than hoping.

**C5. Phase-scope the tool surface.** 13 tools every turn → 2–5 per phase the
planner already knows. Fewer visible tools measurably improves selection
accuracy at this model class; cost is zero.

**C6. Compact what the model reads.** Return the output-schema section of a
spec, not the whole document (11 475 → 2 272 chars here). Prose it does not act
on competes for attention with the directive.

**C7. Handle a malformed-arguments rejection by re-asking, not by crashing.**
Drop the turn, append a one-line re-emit request, and give up after two — the
same turn usually recovers.

**C8. Resume must re-anchor.** State on disk is authoritative; the transcript
is a checkpoint. On re-entry, restate the artifact state and the next move
before the model sees its own last context.

**C9. Do not let history grow unbounded.** Clear old tool results and compress
old submission turns. Keep the last few turns intact so the model has a
continuity anchor.

---

## D. Gates and validation

**D1. A gate that never fires is not a constraint.** The 0.88 near-verbatim
similarity gate had a maximum observed value of 0.79 across 65 rows — dead
weight. Measure each gate's firing rate before trusting it.

**D2. A gate can be right and still be the bottleneck.** The retention floor is
correct in intent; the friction was that the error message did not let the
model act. Fix the message before loosening the gate.

**D3. Content gates must run at the granularity they measure.** Per-row gates
belong on the row; a row submitted alone is not gated until the set closes, so
a defect can be overwritten before anyone looks at it.

**D4. Validate table *structure*, not just table *cells*.** A header wider than
its separator row leaves the table as literal pipe text. Every content check
that drops separator rows is blind to this class. It shipped through a green
validation.

**D5. Record failures, not just successes.** An aborted stage that leaves no
manifest entry makes the run look cleaner than it was.

---

## E. Operating the cluster arm

**E1. One stage per job, resumable by artifact.** A stage that aborts part-way
resumes at the first unit without a validated artifact. Design for resubmission
as the normal path, not the exception.

**E2. Read `done_reason` on every response.** A truncated answer can parse
cleanly and be stored as the artifact of record.

**E3. Disable the model's thinking channel when you need a hard output budget.**
Reasoning tokens share the same budget as the answer; a pack that fills the
context can spend it all reasoning and return empty content.

**E4. Ship the whole corpus the code reads, not the part you remember.** The
control referential was never in the sync payload; the pipeline only discovered
it needed the referential when the new anchor derivation made it load-bearing.
A run that passed locally failed on the compute node for a missing directory.

**E5. If a deliverable is written on the compute node, pull it explicitly.**
The run folder syncing down does not imply `output/` did.

---

## F. Do not do

- Do not conclude a quality regression from a distribution over a handful of
  hand-written rows.
- Do not tune prompts against a legacy artefact.
- Do not let the model see the answer for the unit it is producing.
- Do not rely on the model to stop repeating itself.
- Do not append a warning to a large tool result and expect it to be read.
- Do not ship a corpus directory to the cluster because the pipeline used to
  work without it.
- Do not treat a green validation as proof the document renders.
