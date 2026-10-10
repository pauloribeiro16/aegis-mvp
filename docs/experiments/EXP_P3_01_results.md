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
| 2001126 | `p3a_propose` | `run_p2enr_c1` | qwen3.8:27b | 42 | submitted; result pending |

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

## Pending (the chain stops at the human round by design)

- `p3a_propose` (job 2001126) → then **the human round**: verdicts
  Accept/Reject/Adjust per item in `steps/phase3/round1_verdicts.json` + the
  `G-P3-A` marker (not pre-approvable).
- After convergence: `p3a_org` (needs F1's duty audit) → `p3a_weave` →
  `p3a_gate`; H2/H4/H5 recorded here as they land.
- The six SCALE duties: decision memo at
  [09_SCALE_PROPORTIONALITY_MEMO.md](../pipeline/09_SCALE_PROPORTIONALITY_MEMO.md).
