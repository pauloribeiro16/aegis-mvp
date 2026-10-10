---
document_id: AEGIS-PIPE-06
title: 'Phase 3 Part 1 — review of the pipeline proposal, and what it must satisfy'
version: 0.1.0
created: 2026-10-10
status: DRAFT — review record; not a decision to build
sources: 'docs/pipeline/00_PIPELINE_MASTER_DESIGN.md'
upstream: '[00_PIPELINE_MASTER_DESIGN.md](00_PIPELINE_MASTER_DESIGN.md) · [01_PHASE1_PIPELINE.md](01_PHASE1_PIPELINE.md) · [05_PHASE2_DETERMINISM_LEDGER.md](05_PHASE2_DETERMINISM_LEDGER.md) · [ADR-006](../decisions/ADR-2026-09-28_phase3-two-part-structure.md) · [ADR-007](../decisions/ADR-2026-09-28_requirement-objective-fulfillment-semantics.md) · [ADR-008](../decisions/ADR-2026-09-28_phase3-organizational-lane.md) · [ADR-009](../decisions/ADR-2026-10-01_phase3-level2-use-cases-process-threats-and-strict-neutrality.md) · [ADR-010](../decisions/ADR-2026-10-01_pipeline-architecture.md)'
---

# Phase 3 Part 1 — review of the pipeline proposal

A pipeline design for Phase 3 Part 1 was proposed and reviewed against the
corpus, the governance layer and the measured record. This document records what
survived, what did not, and what a build would have to satisfy. It does not
authorise a build; the quality instrument that would make one measurable is
still open ([L2-00](../experiments/00_RESULTS.md)).

## 1. What the proposal got right

The framing is sound and should not be rewritten.

- **The determinism split.** Generation of prose to the model; relational
  skeleton, id allocation, control anchoring, absorption and gate scoring to
  code. This is what `phase2.py` already does and what ADR-010 D1 requires.
- **Anchors are never model-invented.** Restricting the model to the published
  anchor set and deriving anchors in code is the R2/T6 mechanism as implemented
  — `phase2.derive_objective` re-derives via `controls.goal_anchors()` rather
  than reading Phase 1's values back, because reading them back would make the
  check circular.
- **V0 isolation with an on-disk freeze.** Matches ADR-006 and Step 5b.
- **The three Level-2 use-case criteria.** Matches ADR-009 D1 as written.
- **Refusing a monolithic orchestrating prompt and a free agent.** Matches
  Master Design §3 and ADR-010 D1.
- **The risk list** names the right failure classes: pre-baking, invented
  anchors, technology leakage, clam-level decomposition, organizational loss.

## 2. The seven corrections

### 2.1 Declare the A9 signpost — fired

ADR-013 §5 names three conditions that reopen D1 (no `RULE-*` tail); the second
is *"Phase 3 declares it cannot cite a rule-level artefact."* The proposal's
chain runs `article → PO-/SO- → requirement → control` and skips the rule level
without saying so. The three hand-authored cases skip it too — 0 occurrences
across six documents — but by recorded choice. The revisit is recorded in
[ADR-013 §5.1](../decisions/ADR-2026-10-09_phase2-objective-bridge.md#51-signpost-status--condition-2-fired-2026-10-10);
D1 stands, and the seam is named as a gap in the chain rather than filled.

### 2.2 The coverage matrix must be Case 01's schema, and the migration is a re-verification

The three cases do not agree. Case 01 carries the ADR-007 five-verdict
vocabulary with a `VC discharge` column — the only one of the three that
satisfies D2, "placement of an RN name next to an objective is not
fulfillment." Case 02 and Case 03 use a different totals schema and carry no
discharge column; Case 02's own `SUFFICIENCY_ASSESSMENT.md` states that
per-objective discharge verification *"has been performed in Case_01 only."*

The migration cannot be mechanical, and the case carries its own proof: Case 01's
Round 2 re-audit found that of 26 rows labelled "Covered", **4 were FULL, 20
PARTIAL, 2 MISMATCH**. A translation rule of "has a carrier → Fully covered"
would overstate coverage roughly fourfold.

### 2.3 Organizational routing is measured, not a rule

Case 01 routes 32 of 62 objectives (52%) to the organizational lane and ships no
`Doc03` at all, while Case 02 and Case 03 route 2 each out of 100 and 134. A
1:1 rule emits 32 requirements for an 8-person company.

The measured position is in
[`PROPORTIONALITY_AUDIT_ORGANIZATIONAL_LANE.md`](../../cases/Case_01_TinyTask_SaaS/03_PHASE3_SPEC/part1_security_privacy/analysis_v0_to_v1/PROPORTIONALITY_AUDIT_ORGANIZATIONAL_LANE.md):
32 rows are **16 obligations**, because the taxonomy organises by sub-domain and
the duties cut across it — update distribution appears in D-02.2, D-05.2 and
D-07.3; the breach runbook spans four rows. Dispositions are 17 ORG / 13 SCALE /
2 CARRIED, collapsing to ~15 requirements, of which 6 cannot be written as EARS
until the proportional form is decided per duty.

Any pipeline encoding this classification needs the three cases to agree first.
If they still disagree by more than ~3× after disposition, `realization_class`
(ADR-003) is not stable across cases — that is the result to record.

### 2.4 G-V0 is the wrong instrument, and half of it already exists

The proposal specifies a lexical gate rejecting technology and security-mechanism
words from the V0 cards. Two problems:

- **Half of it is `check_no_technology` already.** R5's `L4_TERMS` regex is in
  `quality.py` and runs clean across 18+ runs. Reuse it; do not rebuild it.
- **The security-mechanism half is a vocabulary test standing in for an altitude
  test.** The V0/V1 boundary is specificity (R13 §2.5, the L0→L4 scale with
  W1–W5 warrants), not words. "Encrypt at rest" is L4; "Verify the traveller's
  biometric identity against the watchlist" is a legitimate V0 card and contains
  no mechanism term. A wordlist errs on function and misses altitude. The
  instrument already exists in `templates/phase3_functional_spec_guidelines.md`
  §2.5.

The measured precedent is against lexical substitution: a token-level R6 gate
fires on **37 of 37** rows, and `check_grounded` once read a legal citation as a
fabrication. A gate that fires on everything is not a gate.

### 2.5 `p3a_1_v0` cannot be one call

The proposal elicits Doc00 + Doc01 V0 + Doc02 V0 in a single stage. Case 02's V0
Doc01 is 788 lines; Case 03's is 836. A Phase 1 `p4` call emits **one 9-cell
row** per sub-domain and still reserves `num_predict=16384`. The recorded
failure mode for exceeding the cap is exactly `done_reason == "length"` →
empty content. Decompose per card, as `p4` decomposes per sub-domain.

### 2.6 G2 must not close on its own

The proposal's risk-acceptance round accepts regulatory items automatically in
unattended mode. That makes the convergence gate green by construction — the
round converges because nothing can dissent. The risk-acceptance cycle is the
substance of ADR-005 and ADR-007, and G2 is its only evidence. This is the same
shape as the Phase 1 content gates, which the record measures as measuring
non-collapse rather than quality: they are blind to compliance theatre and to
check-box placement (`M10_results.md`, the badge re-score).

### 2.7 T7 belongs to Part 2

The proposal runs "T1 to T6". `check_traceability.py` registers T1–T7; **T7 is the
threat-ledger reconciliation and it reads Part 2 files**. Part 1's gate is T1–T6
plus `doc_lint.py --strict`. (The module docstring also omits T6 from its own
check list — a documentation defect worth fixing separately.)

## 3. What a build must additionally satisfy

Not in the proposal, and all of it load-bearing:

| Requirement | Where |
|---|---|
| A versioned ficha `PROM-P3A-*` in the 14-field anatomy | `docs/pipeline/prompts/`; Master Design §7 |
| An entry in `compose.FICHA_FILES` — without it `compose_call` raises `KeyError` | `compose.py:23` |
| `NUM_CTX` / `NUM_PREDICT` for the stage, with the basis declared | `steps.py:35,43`; `METRICS.md` §-2 rule 2 |
| A `build_pack` branch — the ficha's `Context pack` table is documentation, not enforcement | `compose.py:579` |
| A `parse_<stage>` L0 parser + a `store_parsed` branch (mind the `.md` dotted / `.json` underscored split) | `steps.py:517` |
| A `stage_<id>` method, a `--stage` choice, and the sbatch entry | `steps.py`, `run_pipeline.py:289`, `pipeline/deucalion/` |
| Prompt digests carried in the run | `compose.prompt_digests` |
| **A preregistration** with a hypothesis and a falsifier | AGENTS.md §-2.3 |

**On the last row.** Two prompt interventions on the same Phase 1 column have now
failed — M09 (removing the exemplars) and M11 (demanding a named artefact). The
recorded conclusion is *"The next cell is not another prompt clause."* A Phase 3
build is entirely prompt-level intervention on this codebase's semantics, and it
inherits that verdict unless something structural changes.

## 4. Sequencing

Three gates stand between the proposal and a build:

1. **A quality instrument that can score Phase 3.** None exists; Phase 3 has no
   pipeline stage to produce a corpus. Until then a build produces requirements
   no judge has ever scored.
2. **The coverage classification settled across the three cases** (§2.2, §2.3).
3. **The organizational lane's proportionality decided** — a researcher's call
   on R3, not a threshold to be chosen.

Each is cheaper than the build it gates, and each changes the build's shape.