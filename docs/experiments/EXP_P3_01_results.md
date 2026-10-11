---
prereg: PREREG_P3_01.md
prereg_version: 1.0.0
status: PARTIAL — wave 2 SUPPORTED; chain in course
---

# EXP_P3_01 results — Phase 3 Part 1 build rehearsal (wave 2 complete; chain in course)

Prereg: [PREREG_P3_01.md](PREREG_P3_01.md) v1.0.0 (FROZEN 2026-10-10, before any GPU time).
Status: **PARTIAL — wave 2 delivered and SUPPORTED; waves 4–6 in course.** This
document records outcomes as they land (AGENTS §-2.3/2.4); it is updated in the
same session as each stage completes.

## Run inventory (before any verdict)

| Job | Stage | Run dir | Model | Seed | Outcome |
|---|---|---|---|---|---|
| 2001072 | `p3a_cards` (attempt 1) | `run_p2enr_c1` (continue) | qwen3.8:27b | 42 (run config) | FAILED — 0/20 cards, **executor parser defect, not model quality** (see deviation D1) |
| 2001112 | `p3a_cards` (attempt 2) | `run_p2enr_c1` | qwen3.8:27b | 42 | **COMPLETED — 20/20 cards, 0 failures** |
| 2001126 | `p3a_propose` | `run_p2enr_c1` | qwen3.8:27b | 42 | COMPLETED — 18/19 proposals valid (1 isolated failure) |
| 2001149 | `p3a_propose` (re-drive D-04.1) | `run_p2enr_c1` | qwen3.8:27b | 42 | COMPLETED — the same target failed again; failure stays recorded |
| 2001153 | `p3a_round` | `run_p2enr_c1` | — (0 calls) | — | COMPLETED — ROUND1_REGISTER scaffold, 18 items, state PROPOSED |

## H1 — first-attempt card acceptance (wave 2): **SUPPORTED**

- **Measurement:** the corrected run's 20 card calls: 20 ok, 0 with L0 repair →
  **first-attempt 20/20 = 100%** (frozen threshold ≥90%; falsifier not fired).
- The cards: 20 across packages R1–R8 (the hand-written golden V0 has 18 — the
  generated surface is 2 cards larger; the structural comparison at the
  rehearsal's Doc03/coverage step will judge whether the delta is a split or an
  invention), all Priority=Must, PUC ids and `{U.C. n.m}` ids aligned per card.
- Deliverables composed: `outputs/phase3/v0_functional_baseline/Doc01…` +
  `Doc02…` (status PROPOSED — V0 until the acceptance round).

## Deviation D1 — the first attempt failed on the executor's parser, not the model

The 20 model answers of job 2001072 were structurally correct; the L0 parser
(a) searched the `{U.C. n.m}` id only in the section body while the ficha puts
it in the heading, and (b) truncated multi-line scenario fields. Fixed in
`ea39d81` and validated against the stored responses: **20/20 parse**. The H1
measurement is taken from the re-run (job 2001112) only. Additional finding:
the wave tests had been appended after the test runner's `__main__` block and
never executed — the "29 OK" before the rehearsal was a suite running 19 of 39
tests. Fixed (runner catches every exception; block moved to file end).

## Deviation D2 — H3's mechanical grouping yields 26 duties, not 16

The duty grouping canonicalizes the audit's explicit merge references
(union-find over objective ids + identical duty text): **26 duties** from the
32 rows (6 merged pairs; 20 singletons), row-level dispositions intact
(17 ORG / 13 SCALE / 2 CARRIED). The audit's §4 claims 16 canonical duties —
the 10 remaining merges exist only in prose ("same runbook as the row above")
and are not mechanically derivable. Consequence: the canonical 16-duty shape
stays a human input; `p3a_org` refuses unmapped rows either way (never silent
1:1). Test pins the measured shape with the delta documented
(`test_duty_grouping_reproduces_the_measured_32_to_16_shape`).

## Finding F1 — the run's objective ids differ from the hand-written case ids

The audit maps the hand-written matrix's 32 objectives; the pipeline run
assigned its own objective numbering, so 39 of the run's 52 organizational
verdicts are not in the audit's map. The rehearsal's `p3a_org` needs the duty
audit re-entered against the run's ids (`steps/phase3/duty_audit.md`, same §3
table format) — human input by design; the stage refuses to invent it.

## H2 — proposal validity (wave 4): **SUPPORTED, with a scope deviation**

- **Measurement:** 18/19 targeted sub-domains produced structurally valid
  proposals on the first attempt (94.7%; threshold ≥90%). Physical inspection:
  **60/60 anchor citations sit inside the objective's published sets** (T6 held
  without a single finding).
- **Scope deviation (recorded):** H2 as frozen speaks of "the measured 52-row
  block"; the executed selector reads the model's OWN Action column, which
  requested proposals for 19 rows — not all 52 organizational verdicts name a
  proposal in their action. The round can add items by hand; the deviation is
  the selector's scope, not a gate failure.
- **The isolated failure:** D-04.1 (`PO-D-04.1-001`) failed 4 model calls
  across two jobs (omitted target, then out-of-target blocks) — recorded per
  the failure policy; the round may add the item manually.

## Round state (the chain stopped here by design)

`p3a_round` wrote the register scaffold: **18 items, all pending**, state
PROPOSED. Closing it needs the human verdicts
(`steps/phase3/round1_verdicts.json`) + the `G-P3-A` marker, then
`p3a_org` → `p3a_weave` → `p3a_gate` complete the rehearsal.

## Finding F2 — the proposals skipped the secure-design principles layer (researcher observation)

The generated proposals connect objective → published anchors directly; the
**PRIN-ENG-01..07 principles layer** (Phase 2's Doc02 principles, present in the
matrix as `PRINCIPLE_MAPPING.md` with unset judgement columns) was not
attributed. The researcher flagged it on the decision packet. Fix applied: every
packet item now names the principle(s) it serves (or states "process duty — no
design principle"), and the full principle attribution enters at the weave —
each accepted constraint is absorbed by a product card and takes the principle
mark there. The 18 hand-made attributions are PROPOSALS the round validates.

## Pending (the chain stops at the human round by design)

- `p3a_propose` (job 2001126) → then **the human round**: verdicts
  Accept/Reject/Adjust per item in `steps/phase3/round1_verdicts.json` + the
  `G-P3-A` marker (not pre-approvable).
- After convergence: `p3a_org` (needs F1's duty audit) → `p3a_weave` →
  `p3a_gate`; H2/H4/H5 recorded here as they land.
- The six SCALE duties: decision memo at
  [09_SCALE_PROPORTIONALITY_MEMO.md](../pipeline/09_SCALE_PROPORTIONALITY_MEMO.md).
