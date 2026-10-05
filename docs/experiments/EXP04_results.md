---
document_id: AEGIS-EXP04-RESULTS
title: 'EXP-04 — the prompt ablation: decision rule vs menu, under the current instrument'
version: 1.0.0
created: 2026-10-05
status: COMPLETE — with an instrument-regression finding
sources: 'docs/research/sources.yaml'
upstream: '[PREREG_01.md](PREREG_01.md) · [PLANO_FECHO.md](PLANO_FECHO.md)'
---

# EXP-04 — prompt ablation: decision rule vs menu

**Question (registered in PREREG_01 H-series; arms in
`pipeline/src/steps.py` `P4_ADJUSTMENT_VARIANTS`).** The `Adjustment` column of
every §3 goal row is decided by either (a) the **decision rule** — a procedure
with a calibration test ("would this row read the same for a different company?
then you have not calibrated it") — or (b) the **menu** — three values, pick the
best fit, no procedure. Does the procedure change how the model calibrates?

## Design

Same pipeline, same case (TinyTask), same gates; the only variable is the
`p4_adjustment` slot. Seed 42, temperature 0.2. The arm actually run is read
from `config.json → ficha_overrides` — never from the run tag (see the
mislabeled-launch note below).

## Results

**Delivery under the current instrument (rev ad76979+, with the TERMINATION
clause):**

| Arm | Runs | Delivered | Where it fails |
|---|---|---|---|
| menu | 5 | **5/5** | — |
| decision rule | 5 | **0/5** | D-06.3 over-compression: `AG-D-06.3-002 keeps 12 of 46 terms`, deterministic at seed 42 |

**Calibration mix (goal rows):**

| Arm | rows | `unchanged` | `narrowed` | `flagged` |
|---|---|---|---|---|
| menu (current instrument) | 325 | 91% | 6% | 3% |
| rule (old instrument, EXP-02-B) | 975 | 86% | 12% | 2% |

**The finding the ablation was not designed for.** The rule arm delivered
**15/15 under the old instrument** (EXP-02-B, pre-TERMINATION) and fails 0/5
under the current one — same seed, same case. The prompt change regressed the
rule arm specifically: gemma4 (15/15) and muse (15/15) deep dives deliver under
the same current instrument, so the interaction is qwen3.8 × the longer
combined instruction. The two instrument versions are proven by the runs'
`prompt_digests`, and both run sets are kept.

## What they say

1. **Under the current instrument, the menu arm is the robust one** — 5/5
   against a rule arm that cannot deliver. If the shipped prompt stays as-is,
   the menu is the arm that works.
2. **The rule's calibration advantage is now unmeasurable in production**: its
   higher `narrowed` share (12% vs 6%) was measured under the OLD instrument,
   and the cross-instrument comparison is confounded by construction. EXP-01's
   n=1 preview (17 vs 1 `narrowed`) measured the old pair too.
3. **The termination clause and the decision rule compete.** The plausible
   mechanism is instruction dilution: the rule arm carries the longest
   ADJUSTMENT text plus the TERMINATION clause, and the model's restatements
   compress. This is a hypothesis — falsifying it needs one probe run with a
   shortened rule text, which is cheap (~40 min) and worth it before rewriting
   the shipped prompt.

## Decision pending (researcher)

- **(a)** Ship the menu as the default arm (robust, less calibrated), or
- **(b)** shorten the decision-rule text to coexist with TERMINATION and rerun
  both arms cleanly — restores the calibration advantage if the hypothesis
  holds, costs one design pass + 10 runs.

The experiment itself is closed: both arms have complete batteries under the
current instrument, and the regression is documented with its digests.

## Honest notes

- The first menu battery was launched **without the arm knob** and ran the rule
  arm; the 5 runs were kept and re-labelled as the control battery from
  `ficha_overrides` — the mislabelled launch is what made the regression
  measurable, since it produced a fresh rule-arm battery under the current
  instrument.
- The rule-arm delivery failure is deterministic (seed 42): all 5 runs fail at
  the same row with the same term count. No retry can change it.
- n=5 per arm, one case, one model. The delivery verdict is solid (deterministic
  5/5 vs 0/5); the calibration-mix comparison across instruments is context, not
  evidence.
