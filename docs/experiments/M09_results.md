---
document_id: AEGIS-M09
title: 'M09 results — the calibration-instruction ablation: H1 refuted, and the one effect with a clean sign ran backwards'
version: 1.0.0
created: 2026-10-07
status: COMPLETE — H1 REFUTED (3 of 4 preregistered falsifiers fired)
prereg: 'PREREG_M09_CALIBRATION.md'
prereg_version: 1.0.0
upstream: '[PREREG_M09_CALIBRATION.md](PREREG_M09_CALIBRATION.md), [00_RESULTS.md](00_RESULTS.md)'
---

# M09 — Calibration instruction: literal exemplars in, literal exemplars out

**Results for [PREREG_M09](PREREG_M09_CALIBRATION.md), frozen 2026-10-07 before
the first run of either arm.**
**Run: 2026-10-07 21:57–22:59 UTC · Deucalion · rev `4a00413` · qwen3.8:27b ·
seed 42 · temperature 0.2 · n=1 per cell.**

---

## Verdict: **H1 REFUTED**

Three of the four preregistered falsifiers fired. The one that held is the
safety downside (P4). And the single effect with a consistent sign across both
cases ran **opposite** to the hypothesis.

## The cells

| run | arm | case | p4 carried | rows | `[UNVALIDATED_DRAFT]` | lost sub-domains | L1 |
|---|---|---|---|---|---|---|---|
| `run_m09_c2_ctrl_1991134` | ctrl | 02 SecureBorder | **36/38** | 93 | 2 | D-06.3, D-06.4 | fail (exit 1) |
| `run_m09_c2_meta_1991136` | meta | 02 SecureBorder | **35/38** | 90 | 3 | D-06.1, D-06.3, D-06.4 | fail (exit 1) |
| `run_m09_c3_ctrl_1991138` | ctrl | 03 OmniBank | **34/38** | 112 | 4 | D-04.3, D-04.4, D-06.1, D-06.3 | fail (exit 1) |
| `run_m09_c3_meta_1991140` | meta | 03 OmniBank | **37/38** | 125 | 1 | D-06.4 | fail (exit 1) |

All four produced a complete 38-block document via the `c2745f6` soft fallback,
with an `[UNVALIDATED_DRAFT]` block wherever p4 lost the sub-domain. The exit-1
is the gate refusing the run, which is the correct behaviour: *uma falha do gate
é um dado, não um contratempo*.

## The metrics

| | C2 ctrl | C2 meta | C3 ctrl | C3 meta |
|---|---|---|---|---|
| retention mean (M-02 floor 0.30) | 0.757 | **0.770** | 0.763 | **0.778** |
| retention min | 0.342 | **0.395** | **0.432** | 0.333 |
| near-verbatim mean (M-03 ceiling 0.88) | 0.378 | **0.333** | 0.354 | 0.362 |
| rows above the 0.88 ceiling | 0 | 0 | 0 | 0 |
| `max_peer_similarity` median (M-16) | 0.241 | **0.229** | **0.220** | 0.242 |
| `max_peer_similarity` max | 0.476 | **0.400** | **0.398** | 0.567 |
| `ratio_verbatim` (M-14, WARN > 0.70) | 0.978 | 0.989 | 0.964 | 0.984 |
| adjustment mix | 91 `unchanged`, 1 `narrowed`, 1 `flagged` | 89, **0**, 1 | 108, 3, 1 | 123, **1**, 1 |

## The four falsifiers, as written before the data

| # | Prediction | Falsifier | Outcome |
|---|---|---|---|
| **P1** | B delivers no fewer sub-domains than A on either case | B < A on either case | **FIRED on C2** (35 < 36). C3 went the other way (37 > 34). |
| **P2** | B's median peer similarity lower than A's on both | P ≥ B on either case | **FIRED on C3** (0.242 ≥ 0.220). C2 improved (0.229 < 0.241). |
| **P3** | B's `ratio_verbatim` no higher than A's on either | X > B on either case | **FIRED on BOTH** (0.989 > 0.978; 0.984 > 0.964). |
| **P4** | B's mean retention within 0.05 of A's | B mean < A mean − 0.05 | **DID NOT FIRE.** Means rose +0.013 and +0.015. |

Decision rule, fixed in advance: *H1 REFUTED if P1 or P4 fails on either case.*
P1 fails on C2 → **H1 REFUTED**.

## What the result actually says

**The one effect with a clean sign ran the wrong way.** `ratio_verbatim` rose in
both cases, and by more in C3 than C2. The hypothesis was that removing the
literal exemplars would break the default-collapse the M07 reference showed
(0.99); the measurement says removing them made collapse **worse**, and it lost
the single `narrowed` row on C2 and two of three on C3. At n=1 on one model
this is a signal, not a law — but the sign is consistent across both cases,
which is more than any other cell in this matrix manages.

The reading that fits: the literal goal exemplars were not driving the copy
behaviour. They were **modelling the restatement the retention floor demands**
("keep the Sub-SO's own obligation vocabulary, restructure the sentence"), and
removing them left the instruction to carry that alone — which is why retention
*rose* while calibration *fell*. The two moved in opposite directions, the same
pattern M07 recorded when it found delivery and calibration trading places.

**Delivery split by case and does not aggregate.** C2 −1, C3 +3. Two cases at
n=1 cannot turn that into a direction; it is recorded as unresolved.

**The ctrl arm produced the most extreme defect in the matrix.** On C3, `p4`
D-06.1 failed at **100% similarity to its own Sub-SO** — a row that is not a
restatement at all. The arm being measured as the baseline produced the
baseline's worst case. That is worth noting for a reason unrelated to the
verdict: it is direct evidence that the collapse M07 measured is real and
reproducible on this instrument, and it arrived with a second ctrl failure of
the same family on D-04.4 at 90%.

**A failure unrelated to either arm.** C2 ctrl and meta both lost D-06.3 and
D-06.4, the first on retention (9/42 and 12/42 against a floor of 13) and the
second on retention or verbatim embedding. This is the same D-06.3 locus that
took down the EXP-04 rule arm, on this harder case, and it is a property of the
sub-domain rather than of the instruction — **D-06.3 is the standing
reproducible failure point and should be treated as the E-01 of the p4 content
gates.**

## What this does not show

- **n=1, one model, one seed.** Separates the two prompt locations *for
  qwen3.8:27b*. Does not replicate M07, whose falsifier was between-model.
- **Two changes in one arm** (prereg §7.2). Both exemplar sets share one span.
  If the retention rise is real, the next cell splits them.
- **All metrics are mechanical.** Whether the rows that survived are faithful
  restatements or compliance theatre is still the pending L2 blind judgement
  (`PLANO_FECHO.md` §4.1). `ratio_verbatim` moved the "wrong" way under the
  hypothesis and still does not tell us which document is better.
- **M-16 under-reports on short rows** (`cached_ratio` returns 0.0 for pairs
  whose length ceiling cannot reach 0.95). Same bias in both arms, so the
  comparison stands; the absolute values do not mean "this much duplication".

## Decision

**The `meta` variant does not ship.** The prereg's decision rule says a safety
regression refutes regardless of what the other predictions do, and C2 lost a
sub-domain. The shipped instruction stays as it is.

**The next cell is not another arm of the same span.** The finding that the
exemplars were *load-bearing for retention* predicts the opposite intervention:
keep the goal-style exemplars (they model restatement, and P4 shows removal
costs nothing on the mean but the C3 retention *min* fell 0.432 → 0.333) and
vary only the three adjustment rationales, which is where the TinyTask-derived
supplier vocabulary actually sits. That is a one-span ablation of the other
half, and it is testable against P3 in the direction this matrix found.

**The D-06.3 retention failure is the bigger fish.** It took the EXP-04 rule arm,
and it takes both M09 arms on C2. Its 42-term Sub-SO against a 0.30 floor is the
hardest constraint in the matrix and it is independent of prompt wording.