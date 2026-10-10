---
document_id: AEGIS-PIPE-08
title: 'Phase 3 Part 1 — construction plan'
version: 0.1.0
created: 2026-10-10
status: DRAFT — build plan; wave 0–1 unblocked, waves 2–6 gated
sources: 'docs/pipeline/00_PIPELINE_MASTER_DESIGN.md'
upstream: '[07_PHASE3_PART1_PLAN.md](07_PHASE3_PART1_PLAN.md) — the corrected design this builds · [06_PHASE3_PART1_REVIEW.md](06_PHASE3_PART1_REVIEW.md) · [05_PHASE2_DETERMINISM_LEDGER.md](05_PHASE2_DETERMINISM_LEDGER.md) · [ADR-010](../decisions/ADR-2026-10-01_pipeline-architecture.md) · [ADR-013](../decisions/ADR-2026-10-09_phase2-objective-bridge.md)'
---

# Phase 3 Part 1 — construction plan

The design is settled in [07_PHASE3_PART1_PLAN.md](07_PHASE3_PART1_PLAN.md). This
document is the **build**: what lands, in what order, what proves each piece, what
it costs, and what would stop it.

## 1. The order is the argument

The proposal this replaces front-loaded the model. This plan does not, for one
reason measured on this codebase: **85–90% of Phase 2 was deterministic, and the
deterministic part is what made it testable.** Every architecture defect found in
the Phase 3 review — the impossible single call, the organizational lane that
could only count verdicts, the exit gate that could not fail — is a defect of
skeleton-before-prose, not of prose.

So the build starts where no model is needed and ends where one is unavoidable.

A feasibility probe settles that waves 0–1 are executable **today**: from
`cases/Case_01_TinyTask_SaaS/02_PHASE2_RULES/Doc01_Operational_Objectives.md`,
with zero model calls, the pipeline can already derive 62 objectives across 35
sub-domains, **62 of 62 carrying a published control-anchor set** (55 distinct),
read from column 9. Nothing in wave 0 or wave 1 needs a GPU.

## 2. Entry conditions

| Gate | State on 2026-10-10 |
|---|---|
| **G-a** A quality instrument that can score Phase 3 | **Open.** The L2 instrument scores Phase 1 documents; Phase 3 has no stage, so no corpus exists to score. Its own §6.1 test–retest has not run either. |
| **G-b** Coverage classification settled across the three cases | **Half.** Case 01 is settled — 10 organizational requirements specified, 6 duties held, 1 closed against `ORG-INT-03`. Case 02 and Case 03 still use the non-discharge schema. |
| **G-c** Organizational proportionality decided | **Open.** 6 SCALE duties in Case 01 await a judgement; Case 02 and Case 03 have not been audited at all. |

**What this means for the build.** Waves 0–1 are unblocked and cost nothing.
Waves 2–6 produce artefacts that no judge has ever scored. That is not a reason
not to build them — it is a reason to say plainly that the build's first output
is a corpus waiting for an instrument, and that G-a should be scheduled
alongside wave 2 rather than after it.

## 3. The waves

### Wave 0 — contracts, no model

**Lands:** `pipeline/src/phase3.py`, `pipeline/tests/phase3_test.py`.

Nothing generates prose yet. What it fixes are the decisions every later stage
inherits, which is why they come first:

- ID allocation — `ORG-D-XX.Y-NNN` by duty, not by verdict row; `R<n.m> ↔ PUC
  n.m ↔ {U.C. n.m}` parity enforced at allocation time.
- Duty grouping — collapse the organizational verdicts to obligations. The
  measured shape: 32 verdicts are 16 duties, because the taxonomy organises by
  sub-domain and the duties cut across it. Grouping is by
  `(regulation, obligation)`, never by sub-domain.
- Anchor resolution — `controls.goal_anchors()` re-derivation, never inheritance.
- The coverage-matrix schema — Case 01's five-verdict vocabulary, with the
  `VC discharge` column mandatory and non-empty for any row claiming a carrier.
- L2 ceiling — the altitude check, replacing any word list.

**Check:** `phase3_test.py` asserts the duty grouping reproduces the measured
Case 01 shape (32 verdicts → 16 duties) from the matrix alone, and that anchor
resolution returns only ids that rglob under `baseline/CONTROLS/`.

**Exit:** tests green, zero model calls, zero GPU.

### Wave 1 — the coverage skeleton, no model

**Lands:** `stage_p3a_2_map` skeleton half; writes
`outputs/phase3/synthesis_rounds/OBJECTIVE_MAPPING.md` and `PRINCIPLE_MAPPING.md`.

Reads the Phase 2 objectives and the seven principles, emits **every row with
its carrier, verdict and discharge columns empty**, and the totals table computed
by code.

This is the single largest architectural win available and it should be stated
plainly: **G1 becomes unfalsifiable.** G1 asks for exhaustive mapping with zero
silent objectives. When the skeleton is generated, a silent objective is not a
judgement call — it is a row the generator would have had to skip. The check
becomes "every Phase 2 objective has a row", which is a set comparison.

**Check:** row count equals the Phase 2 objective count; every id resolves; the
totals table sums; a deliberately dropped objective makes the check fail.

**Exit:** tests green, the Case 01 skeleton writes and validates, zero GPU.

### Wave 2 — the functional baseline, first model stage

**Lands:** `PROM-P3A-01` (inventory) and `PROM-P3A-02` (per-card), the
`build_pack` branch, the L0 parser, `store_parsed`.

One call for the card inventory, then **one call per card** producing the 7-row
card + its PUC + its use case main scenario. This is the correction to the
proposal's impossible single call: Case 02's V0 Doc01 is 788 lines against a
Phase 1 call that emits one row.

Budgets: `num_predict` 8192 per card call, `num_ctx` 32768, basis declared in
`METRICS.md` before the first run.

**Check:** per-card validation on arrival — 7-row anatomy, active-verb title,
technology terms absent (`check_no_technology`), altitude ≤ L2. A card that fails
is re-driven once with a targeted correction, never a blanket retry.

**Failure policy: isolate, do not stop.** A piece that fails its repair is
recorded as failed and the sweep continues — Phase 2's `_sweep` already does this,
and the M02 evidence is why: 5 of 5 runs aborted at the same sub-domain, where
isolation would have delivered 34 of 35 calls plus the diagnosis. The stage result
records the graded outcome (`context-fail | L0 | transport | error`) so a partial
run is still evidence. Stopping the whole execution is reserved for the gates, not
for individual pieces.

**Exit:** all cards accepted on the first attempt for ≥ 90% of cards on the
reference model, seeded. Below that, the instruction is wrong and the stage is
not ready to move on — this is the M09 lesson applied in advance.

### Wave 3 — coverage mapping, verdicts

**Lands:** the model half of `stage_p3a_2_map`; the `VC discharge` requirement.

The model fills carrier, verdict, and discharge. Code checks that every
discharge is non-empty for any row claiming a carrier, and that each cited
anchor belongs to the published set of an objective that row also cites (T6).

**Deliberate omission.** The ADR-007 D2 reconstruction test is **not**
implemented, because it is not executable on the current Phase 2 data — all 62
Verification Criteria are two template sentences (measured, ADR-013 §3). The
`Fully covered` label says `anchored`, and the reason is written into the
matrix. Building the test anyway would produce a check that passes vacuously,
which is the failure mode G-V0 was going to have.

### Wave 4 — constraint proposal and acceptance

**Lands:** `stage_p3a_3_propose`, `stage_p3a_4_round`.

The round **requires a human marker**, exactly as `p1` requires `G-P1-A`. Until
`steps/gates/<G>.approved` exists the stage records `partial` and stops. An
unattended round that accepts everything makes G2 green by construction — the
same shape as the Phase 1 gates that the record measures as measuring non-collapse
rather than quality.

### Wave 5 — the organizational lane

**Lands:** `stage_p3a_5_org`.

Iterates **duties**, not verdict rows. For Case 01 that is 16 duties, of which
10 are already specified by hand in `Doc03_Organizational_Requirements.md` —
which makes this the one wave with a golden to test against before any run.

**Doc00 is composed, not generated.** It is assembled from the Phase 1 fact sheet
plus a PUC catalogue derived from the V0 cards — deterministic composition, like
`phase2.render_doc01`. No model call. The failure this avoids is recorded in the
ledger: a model rewriting company input restates it, and Case 03's Phase 2 Doc02
carrying Case 02's architecture is what that looks like.

### Wave 6 — weave and exit gate

**Lands:** `stage_p3a_6_weave`, `stage_p3a_7_gate`.

Constraint injection into cards is mechanical. The gate runs **T1–T6** (T7 reads
Part 2 files and belongs to Part 2's gate) plus `doc_lint.py --strict`, and
evaluates G1–G6. G1 and G6 are already guaranteed by construction from waves 1
and 0; the gate evaluates G2–G5.

### Which registers the pipeline writes

Six are consequences of the chain and are written mechanically: `OBJECTIVE_MAPPING`,
`PRINCIPLE_MAPPING`, `UC_OBJECTIVE_CORRESPONDENCE`, `STEP2` (regulatory
cross-cutting), `STEP4` (absorption weaving), `SUFFICIENCY_ASSESSMENT`.

Five record **reasoning** and stay with the researcher: `STEP1` (the V0 audit —
the pipeline auditing a human-authored input produces the machine's opinion of the
researcher's work), `STEP3` (formulation decisions), `STEP5` (the D1–D4 register
including its "evaluated, no change" rows), and the two `ROUND<n>_REGISTER`
verdict ledgers — the file a generated register would erase is the one that records
the verdicts themselves.

A generated reasoning record is a log of what the machine did, not a record of
reasoning. If the pipeline fills these as *data*, they may be written; the
judgement stays human.

### Two states, not one

A run whose acceptance round has no verdicts is **proposed**, not **concluded**. The
exit gate closes only on the concluded state. Without this distinction G2 closes by
construction — the round converges because nothing has answered it yet.

## 4. The rehearsal

Before any multi-case run: **one case, seeded, reference model**. Case 01 is the
smallest at 20 cards and 62 objectives, and it is the only case with a
hand-written `Doc03` and a `PROPORTIONALITY_AUDIT` to compare against.

The rehearsal's success criterion is not "it ran". It is:

- every Phase 2 objective appears in the matrix (wave 1, deterministic)
- ≥ 90% of cards accepted on first attempt (wave 2)
- the generated `Doc03` differs from the hand-written one in **prose** and
  agrees in **structure** — same duties, same id allocation, same anchor sets

That last one is the only end-to-end quality claim available before the scoring
instrument exists, and it is worth having.

## 5. Cost

| Waves | Model calls | GPU | Note |
|---|---|---|---|
| 0–1 | **0** | 0 | runnable today |
| 2 | ~21 per case (1 + 20 cards) | comparable to one Phase 1 run | |
| 3 | ~35 per case (per sub-domain) | | |
| 4 | ~35 | | plus human verdicts |
| 5 | ~16 (per duty) | | |
| 6 | ~20 | | |
| **Total** | **~130 per case** | | Phase 2 is 99–129 per case; same order |

Nothing here needs the cluster until wave 2.

## 6. Deliberately not built

- **Part 2** (threat and risk) — gated by G1–G6 per ADR-006 D2; no design here.
- **The HITL mechanics beyond the marker** — the round needs a verdict, not a UI.
- **A third case.** Two cases with the same classification is one data point.
- **Any automation of the organizational proportionality judgement.** It is R3
  applied to a specific company, and it is the researcher's.

## 7. What would stop this

Each wave carries a falsifier, and a fired one stops the build rather than
triggering a threshold change — `PLANO_FECHO` §4: *a gate failure is data, not an
inconvenience*.

| Wave | Falsifier |
|---|---|
| 1 | The skeleton cannot express a Phase 2 objective without loss — then the Phase 2 schema is the defect, not the generator |
| 2 | First-attempt acceptance below 90% on the reference model — the instruction is wrong; do not lower the bar |
| 3 | A verdict cannot be produced for an objective that plainly has a carrier — the verdict vocabulary is incomplete |
| 4 | Verdicts arrive mechanically identical across cases — the round is not doing work, whatever G2 says |
| 5 | Generated duty grouping disagrees with the hand-written Case 01 `Doc03` in structure — the grouping rule is wrong |

## 8. The standing question

Wave 2 onward produces requirements **no judge has ever scored**. The two
prompt interventions already tried on this codebase's semantics (M09, M11) both
failed, and the recorded conclusion is that the next cell is not another prompt
clause. Building now is defensible — wave 1 alone closes G1 by construction and
costs nothing — but the honest framing is that waves 2–6 produce a corpus, and
what makes them evidence is G-a, which is still open.