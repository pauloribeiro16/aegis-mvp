---
document_id: AEGIS-PIPE-07
title: 'Phase 3 Part 1 — corrected pipeline plan'
version: 0.1.0
created: 2026-10-10
status: DRAFT — corrected plan; NOT authorised for construction
sources: 'docs/pipeline/00_PIPELINE_MASTER_DESIGN.md'
upstream: '[00_PIPELINE_MASTER_DESIGN.md](00_PIPELINE_MASTER_DESIGN.md) · [06_PHASE3_PART1_REVIEW.md](06_PHASE3_PART1_REVIEW.md) · [03_PROMPT_CATALOG.md](03_PROMPT_CATALOG.md) · [ADR-004](../decisions/ADR-2026-09-22_pipeline-io-contract.md) · [ADR-005](../decisions/ADR-2026-09-24_phase4-threat-analysis-and-iterative-risk-acceptance.md) · [ADR-006](../decisions/ADR-2026-09-28_phase3-two-part-structure.md) · [ADR-007](../decisions/ADR-2026-09-28_requirement-objective-fulfillment-semantics.md) · [ADR-008](../decisions/ADR-2026-09-28_phase3-organizational-lane.md) · [ADR-009](../decisions/ADR-2026-10-01_phase3-level2-use-cases-process-threats-and-strict-neutrality.md) · [ADR-010](../decisions/ADR-2026-10-01_pipeline-architecture.md) · [ADR-013](../decisions/ADR-2026-10-09_phase2-objective-bridge.md#51-signpost-status--condition-2-fired-2026-10-10)'
---

# Phase 3 Part 1 — corrected pipeline plan

This is the proposal's plan with the seven defects from
[06_PHASE3_PART1_REVIEW.md](06_PHASE3_PART1_REVIEW.md) corrected, and with the
engineering contract the proposal left implicit. **It is not authorisation to
build** — §5 states the three gates that stand between this document and code.

## 1. What does not change

The division of labour is correct and stays: the model writes prose; code owns
the relational skeleton, id allocation, control anchoring, absorption and gate
scoring. That is what `phase2.py` does and what ADR-010 D1 requires. Anchors are
**re-derived** from the published set by code, never copied from Phase 1 (reading
them back would make the check circular) and never emitted by the model. V0 is
isolated and frozen on disk. Level-2 use cases require all three ADR-009 D1
criteria.

## 2. Stage design

The proposal's `p3a_1_v0` emits Doc00 + Doc01 V0 + Doc02 V0 in one call. It
cannot: Case 02's V0 Doc01 is 788 lines and Case 03's is 836, against a Phase 1
`p4` call that emits **one 9-cell row** per sub-domain and still reserves 16384
predict tokens. The recorded failure for exceeding the cap is
`done_reason == "length"` → empty content. The fix is the one `p4` already uses:
**decompose by the unit of work**, which here is the requirement card.

| Stage | Calls | Model writes | Code owns |
|---|---|---|---|
| `p3a_1a_inventory` | 1 | The card inventory — names as active verb phrases, one row per relevant sub-domain | Card / PUC / use-case id allocation, `R<n.m> ↔ PUC n.m ↔ {U.C. n.m}` parity |
| `p3a_1b_card` | **N** (28–43) | One 7-row card + its PUC + its use case main success scenario | Per-card validation, altitude check, freeze into `v0_functional_baseline/` |
| `p3a_2_map` | 38 (per sub-domain) | Carrier, skill, verdict, discharge statement | Exhaustive skeleton pre-loaded — every Phase 2 objective, so G1 cannot fail by omission |
| `p3a_3_propose` | 38 (per sub-domain) | EARS constraint, fit criterion, risk addressed | Chain assembly: article and objective from Phase 2, anchors restricted to the published set, method enum |
| `p3a_4_round` | 0 | — | Register + convergence. **Does not close unattended** (§3.5) |
| `p3a_5_org` | **D** (≈16, not 32) | One organizational requirement per **duty** | Duty grouping, `ORG-D-XX.Y-NNN` allocation, GOVERN + advisory anchors |
| `p3a_6_weave` | N | Security preconditions and exception extensions on use cases | Injection of accepted constraint blocks into `Doc01`; summary tables |
| `p3a_7_gate` | 0 | — | **T1–T6** + `doc_lint.py --strict` + G1–G6 |

`D` is the organizational-duty count, not the organizational-verdict count —
see §3.3.

Call budget: ~150–200 per case, against Phase 1's 42 and Phase 2's 99–129. Same
order of magnitude, and no call carries a whole document.

Budgets follow the measured reservation pattern, not the cap: `p4` reserves
16384 and produces a mean of 2762 (max 4059) over 39 calls — 5.9× the mean. A
per-card call producing ~1.5k tokens warrants `num_predict` 8192, and the
per-sub-domain stages 8192. **Declare both in `METRICS.md`** with their basis
before running (AGENTS.md §-2 rule 2).

## 3. The seven corrections

### 3.1 The A9 signpost is declared, not silently inherited

The chain runs `article → PO-/SO- → requirement → control`, skipping the
rule-level artefact that ADR-013 D1 defers. That skipping is what ADR-013 §5
names as the trigger to revisit D1, and it has now fired and been recorded. A
Phase 3 build inherits the decision **explicitly**: the seam is named in the
preregistration as a gap in the chain, not quietly filled.

### 3.2 The coverage matrix is Case 01's schema, and the migration re-verifies

Case 01 carries the five-verdict vocabulary with a `VC discharge` column — the
only one of the three satisfying ADR-007 D2. The migration of Case 02 and
Case 03 cannot be mechanical: Case 01's own Round 2 re-audit found **4 FULL, 20
PARTIAL, 2 MISMATCH** out of 26 rows labelled "Covered", so a "has carrier →
Fully covered" rule would overstate coverage roughly fourfold. **Build does not
start until both matrices carry a discharge column.** Until then `p3a_2_map`'s
output schema has no stable target and the T5 driver-symmetry check has nothing
to bind against.

### 3.3 Organizational routing counts duties, not verdicts

Case 01 routes 32 of 62 objectives (52%) to the organizational lane and ships no
organizational requirements document; Case 02 and Case 03 route 2 each out of
100 and 134. A 1:1 rule emits 32 requirements for an 8-person company.

The measured position: the 32 rows are **16 obligations**, because the taxonomy
organises by sub-domain and the duties cut across it — update distribution
appears in D-02.2, D-05.2 and D-07.3, the breach runbook spans four rows.
Dispositions are 17 ORG / 13 SCALE / 2 CARRIED, collapsing to ~15 requirements,
of which **6 cannot be written as an EARS statement until the proportional form
is decided per duty**. `p3a_5_org` therefore iterates duties, and the 6 SCALE
duties are a researcher's proportionality judgement, not a threshold to pick.

### 3.4 V0 neutrality is checked by altitude, not by a word list

`check_no_technology` already implements the technology half (R5's `L4_TERMS`,
clean across 18+ runs) — reuse it. The security-mechanism half is replaced: the
V0/V1 boundary is specificity (R13 §2.5, the L0→L4 scale with W1–W5 warrants),
not vocabulary. "Encrypt at rest" is L4; "Verify the traveller's biometric
identity against the watchlist" is a legitimate V0 card containing no mechanism
term. A word list errs on function and misses altitude, and the measured
precedent is against lexical substitution — a token-level R6 gate fires on **37
of 37** rows. The instrument exists: `templates/phase3_functional_spec_guidelines.md` §2.5.

### 3.5 The acceptance round cannot close unattended

The proposal accepts regulatory items automatically in batch mode, which makes
convergence green by construction — the round converges because nothing can
dissent. G2 is the only evidence that risk acceptance happened. `_require()` a
human marker exactly as `p1` does for `G-P1-A`; until it exists the stage
records `partial` and does not proceed. This mirrors the Phase 1 finding: the
content gates measure non-collapse, not quality, and are blind to compliance
theatre and check-box placement.

### 3.6 Part 1 runs T1–T6, not T1–T7

`check_traceability.py` registers T7 as the threat-ledger reconciliation and it
reads Part 2 files. Part 1's exit gate is T1–T6 plus `doc_lint.py --strict`,
which is also what G4 names. (The module docstring omits T6 from its own check
list — fix separately.)

### 3.7 Stage ids do not collide with Phase 1's

Phase 1 already owns `p1`, `p2`, `p3`, `p3f`, `p4`, `p4t`, `p5`. `p3a_*` reads as
Phase 1's `p3` and invites exactly the mistake that happened with the goal-file
naming split. Rename to `f3a_*` or `ph3_*` and state the choice in
`03_PROMPT_CATALOG.md`.

## 4. Engineering contract

Absent from the proposal, all of it load-bearing:

| Requirement | Where |
|---|---|
| Versioned ficha `PROM-P3A-*`, 14-field anatomy | `docs/pipeline/prompts/` |
| `compose.FICHA_FILES` entry — without it `compose_call` raises `KeyError` | `compose.py:23` |
| `NUM_CTX` / `NUM_PREDICT` per stage, basis declared | `steps.py:35,43` + `METRICS.md` |
| `build_pack` branch — the ficha's `Context pack` table is documentation, not enforcement | `compose.py:579` |
| `parse_<stage>` L0 parser; `EXTRA_INSTRUCTION` passing the dangling-preposition assert | `steps.py` |
| `store_parsed` branch — `.md` dotted, `.json` underscored | `steps.py:517` |
| `stage_<id>` returning a call count; `--stage` choice; sbatch entry | `steps.py`, `run_pipeline.py:289`, `pipeline/deucalion/` |
| Prompt digests in the run | `compose.prompt_digests` |
| `done_marker` per card/sub-domain so a sweep resumes | `steps.py:_sweep` |
| **A preregistration** with hypothesis, prediction and falsifier | AGENTS.md §-2.3 |

**On the last row.** Two prompt interventions on the same Phase 1 column have
failed — M09 (removing the exemplars) and M11 (demanding a named artefact). The
recorded conclusion is *"The next cell is not another prompt clause."* A Phase 3
build is prompt-level intervention throughout, and inherits that verdict unless
something structural changes. The preregistration is where the structural claim
gets made falsifiable; without one there is no result, only an artefact.

## 5. Gates before construction

Three, each cheaper than the build it gates and each changing its shape:

1. **A quality instrument that can score Phase 3.** None exists. Phase 3 has no
   pipeline stage, so there is no corpus to score, and the current instrument
   scores Phase 1 documents only. Building first produces requirements no judge
   has ever scored.
2. **The coverage classification settled across the three cases** (§3.2, §3.3).
3. **Organizational proportionality decided** — the 6 SCALE duties are a
   researcher's R3 judgement.

Gate 1 additionally requires the scoring itself to have happened (currently 0
notes entered) and its §6.1 test–retest to have run — the interpretation
thresholds are already fixed and none of them has been evaluated.

## 6. Scope

Part 1 only. Part 2 (threat and risk analysis) is gated by G1–G6 per ADR-006 D2
and has no pipeline design here; ADR-009 D2's feedback loop from Part 2 back into
Part 1 is out of scope until Part 1 exists. Nothing in this document touches the
cluster: a build is the first stage that would.