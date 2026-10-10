# PREREG_P3_01 — Phase 3 Part 1 build: do the remaining waves produce evidence on Case 01?

Version: 1.0.0
Status: FROZEN 2026-10-10, before the first `p3a_cards` job is submitted.
Frozen by: aegis-mvp executor, after the build plan `docs/pipeline/08_PHASE3_PART1_CONSTRUCTION.md` was approved for construction and before any GPU time for waves 2–6.
Upstream: [08_PHASE3_PART1_CONSTRUCTION.md](../pipeline/08_PHASE3_PART1_CONSTRUCTION.md) (waves §3, rehearsal §4, falsifiers §7) · [07_PHASE3_PART1_PLAN.md](../pipeline/07_PHASE3_PART1_PLAN.md) §2 (stage contracts) · prior evidence: `p3a_map` first run (`run_p2enr_c1`, job 1999885 — 65/65 verdicts, 0 infra failures, content divergence recorded).
Budgets declared before running: METRICS.md M-21..M-24 (`convention, unmeasured → E-15`).

---

## 1. What this preregisters

The construction of waves 2, 4, 5 and 6 of Phase 3 Part 1 (`p3a_cards`,
`p3a_propose`, `p3a_round`, `p3a_org`, `p3a_weave`, `p3a_gate`) and their first
end-to-end execution — the **rehearsal** — on one case (Case 01 TinyTask SaaS),
seeded (42), temperature 0.2, reference model `qwen3.8:27b`.

One configuration, no arms, n=1. This is a **build rehearsal**, not a model
comparison: its purpose is to produce the first Phase 3 corpus and the first
structural quality claim, not to compare models or prompts.

## 2. Hypotheses, predictions, falsifiers (per wave)

### Wave 2 — `p3a_cards` (V0 baseline per card)

- **H1:** With the inventory + per-card fichas and the L0 validators built
  before the run, ≥ 90% of the 18 cards are accepted on the **first** attempt
  (no L0 repair, no targeted re-drive).
- **Prediction:** 17–18 of 18 first-attempt (the pack is small: company input +
  Phase 2 objectives + inventory row; one card ≈ 1.5k tokens against an 8192
  budget).
- **Falsifier (stops the build):** first-attempt acceptance < 90% — the
  instruction is wrong; the bar does not move (doc 08 §7).

### Wave 4 — `p3a_propose` + `p3a_round`

- **H2:** For the objectives whose first `p3a_map` verdict was
  `No functional carrier (organizational)` but whose discharge names a
  functional leg (encryption in transit, at rest, access control — the measured
  52-row block), the proposal stage produces an EARS constraint with a binary
  fit criterion and a chain whose anchors stay inside the objective's published
  set for **≥ 90% of those objectives**.
- **Prediction:** ~46–50 of 52 proposals structurally valid at first attempt.
- **Falsifier:** a proposal cannot be produced for an objective that plainly
  has a carrier — the verdict vocabulary is incomplete (doc 08 §7), which
  reopens the wave 3 vocabulary, not this stage's threshold.
- **Round (human, G-P3-A):** the round is measured for *work done*, not
  acceptance rate. **Falsifier:** verdicts arrive mechanically identical across
  cases (Accept-everything) — the round is not doing work whatever G2 says.
  Recorded per item: Accept / Reject (= explicit risk acceptance) / Adjust.

### Wave 5 — `p3a_org`

- **H3:** The duty grouping code reproduces the measured Case 01 shape —
  **32 verdict rows → 16 duties (17 ORG / 13 SCALE / 2 CARRIED)** — from the
  matrix alone.
- **H4:** The generated `Doc03` agrees with the hand-written golden in
  **structure** — same duty set, same ORG-ID allocation rule, same anchor sets
  — and differs only in prose.
- **Falsifier:** structural disagreement with the hand-written `Doc03` — the
  grouping rule is wrong (doc 08 §7). Prose divergence is expected and is not
  a failure.

### Wave 6 — `p3a_weave` + `p3a_gate`

- **H5:** The gate stage, run on a run whose round register has unresolved
  verdicts, reports the **proposed** state and does NOT close G2; after the
  verdicts land and the marker exists, it reports **concluded** and closes
  G1–G6 (or names the failing gate explicitly).
- **Falsifier:** the gate closes G2 on a register with open verdicts — the
  same by-construction failure mode the Phase 1 gates already exhibit.

## 3. What is fixed before running

- Fichas `PROM-P3A-02/03/04/05/06` versioned 1.0.0, frozen at commit of record;
  prompt digests recorded in the run manifest.
- Budgets M-21..M-24 (32768 context / 8192 output per stage) declared in
  METRICS.md before the first job.
- L0 validators (7-row anatomy, anti-nominalisation, `check_no_technology`,
  MoSCoW enum, EARS shape, published-anchor membership) written and tested
  before the run — the M09 lesson applied in advance: the validators define the
  contract; the model is not shown a moving target.
- Golden references: Case 01 hand-written `v0_functional_baseline/` (18 cards,
  18 PUCs, 18 use cases), `Doc03_Organizational_Requirements.md` (10 ORG
  requirements across 8 duties), `ROUND1_REGISTER.md` (13 items) — used only
  for structural comparison, never as model input.
- The six SCALE duties are marked `pending-scale` by the pipeline and are NOT
  resolved by any model call (G-c stays human).

## 4. Outcomes recorded either way

A wave that hits its falsifier stops the build and is recorded in
`docs/experiments/00_RESULTS.md` the same session, with the same prominence as
a pass (AGENTS.md §-2.4). Partial runs record graded per-piece outcomes
(`context-fail | L0 | transport | error`) in `stage_result` — a partial run is
still evidence.

## 5. Out of scope

Part 2 (threats), multi-case execution (blocked on G-b: Cases 02/03 schema
migration + G-c: the six SCALE duties), third case, HITL mechanics beyond the
G-P3-A marker, and any automation of the proportionality judgement.
