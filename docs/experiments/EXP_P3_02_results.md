---
prereg: PREREG_P3_02.md
prereg_version: 1.2.0
status: H1 SUPPORTED · H2 FALSIFIER FIRED (qwen38 c1) · H3 PROPOSED honest, gate awaits the human round
---

# EXP_P3_02 results — the Onda C calibration matrix (multi-model, ficha repaired)

Prereg: [PREREG_P3_02.md](PREREG_P3_02.md) **v1.2.0** — the version in force when
every counted job ran (Adenda 1.2.0 recorded the instrument repair and the two
aborted submissions before this one; no result predates it). All numbers below
are aggregated server-side from the runs' own stores; no artifact was read
whole (the analysis contract with the operator).

## Run inventory (before any verdict)

| Jobs | Runs | Model(s) | Outcome |
|---|---|---|---|
| 2160106–2160111 | `run_p302_*` (1st submission) | qwen38/muse/gemma4 | **ABORTED — zero model calls.** The pack builders for the Onda B/D steps lived in `compose_call` instead of `build_pack`; every arm died at `p3a_org_cluster` with `unknown step`. Fixed in `9946610`. |
| 2160351–2160356 | same dirs, after the fix | same | **ABORTED at ~1 min, zero valid calls.** The cluster imports the `phase3.py` SHIM, which re-exports names explicitly; the new `verdict_defects` was package-only → `AttributeError` on the first `_validate`. Shim fixed + shim guard test added. |
| **2160543–2160548** | same dirs, upstream pinned per Adenda 1.1.0 | qwen3.8:27b · muse-glimmer:30b · gemma4:31b | **COMPLETED — the counted run.** 6/6 arms walked `cards → map → org_cluster → propose → prin → round` and stopped PROPOSED (two-states). |

Seed 42 / temp 0.2 / `v0_source=frozen` in every arm (config read back from the
forks; the forks carry the pinned qwen3.8 upstream per case).

## The headline matrix (Etapa 1.2, complete rows)

| Arm | Rows | Global `ROUTE_ORG` (band 25–60%) | M-26 D-02..D-07 (alert >65%) | L0 first-attempt | Proposals (objective + principle) |
|---|---|---|---|---|---|
| qwen38 c1 | 65/65 | **66%** | 65% (n=40) | 93% (54/58) | 30 + 9 |
| qwen38 c3 | 129/129 | 9% | 6% | 96% (78/81) | 118 + 6 |
| qwen38 c2 | 99/99 | 8% | 9% | 96% (79/82) | 95 + 8 |
| muse c1 | 65/65 | **58%** | 55% | 87% (55/63) | 33 + 6 |
| muse c3 | 129/129 | 16% | 11% | 89% (62/70) | 60 + 0 |
| gemma4 c1 | 65/65 | 65% | **68% — alert fires** | 95% (59/62) | 32 + 9 |

The two prior submissions of this same matrix measured 77% (qwen c1) and 82%
(muse c1) global `ROUTE_ORG` with **zero proposals** — the ficha repair is the
difference between those numbers and these.

## H1 — L0 first-attempt (qwen ≥90% all cases; muse ≥85% both): **SUPPORTED**

qwen 93/96/96%, muse 87/89%, gemma4 95% (contrast arm, no threshold). The
falsifier (qwen <90% anywhere) did not fire. Sending the ficha's whole body —
the five verdicts, the Action coupling rule, the R5 table, `RN (a derivar)` —
did not weaken the output contract; the repair rounds that fired (4–7% of
calls) were absorbed without dropping a sub-domain: **326/326 objectives
across the four complete-partition arms carry a verdict** (the old code
shedded 11 in qwen c2 alone).

## H2 — routing balance: **FALSIFIER FIRED (qwen38 c1)**; the signal reopens the ficha

- **qwen38 c1 at 66% global `ROUTE_ORG` exceeds the 60% ceiling** — the prereg's
  falsifier. Per the prereg's own rule (§H2), the ficha review reopens; this
  document records the firing, it does not defend the ficha.
- **Where the intervention worked (measured, per domain):** D-01 — the ficha's
  explicit target (`RN (a derivar)` for transversal data protection + the
  coupling rule) — fell from 62–75% organizational (aborted run) to **0–25%**
  across the three models, against a hand-written gabarito of ~0%. The repair
  did exactly what it was built to do where it was aimed.
- **Where the residual overshoot lives (measured against the hand-written
  gabarito):** D-05 (data lifecycle) 57% org vs gabarito 14%, D-07 (secure
  development) 80% vs gabarito 20%, D-08 100% vs gabarito 67%, D-06 (supply
  chain) 100% vs gabarito 80% — the models route the product's data-lifecycle
  and development-process obligations organizational almost wholesale. The D4
  coupling rule names product data, session, access, logging and error
  behaviour; the data lifecycle (retention, backup, deletion) and the
  software's own secure-update/dependency/release duties apparently still
  read as "not product" to every model. **This is the next ficha revision's
  target** (D-05/D-07 carry the largest gabarito deltas), and it is a
  vocabulary gap (the coupling rule's product list), not a parsing defect.
- **The band itself is Case-01-shaped:** Cases 02/03 sit at 3–16% for every
  model — far below 25%. The prediction "qwen in band in all three cases" is
  not sustained as written; the falsifier (only >60%) did not fire there. A
  band that fits one company's shape is a convention awaiting E-calibration,
  not a quality floor.

## M-26 — the registered collapse alert

Fires on gemma4 c1 only (68% > 65%). qwen c1 lands at exactly 65% (strict
inequality, silent). The scope D-02..D-07 discriminates as measured on
2026-10-28 (collapsed arms 55–68%, healthy arms 0–11%).

## H3 — honest closure: **PROPOSED in 6/6**; G1–G6 await the human round

No arm produced a round state without human verdicts; every `p3a_all` stopped
before the organizational/weave stages with the two-states message. The G1–G6
application and the T1–T6 chain checks run after G-P3-A (the investigator's
round) — the prereg's declared human dependency, not a deviation.

## What this does NOT claim

Mirrors prereg §6: no model ranking (different convergence stages per case);
no quality verdict on the proposals themselves (that is the round's and the
L2's business); no claim about Part 2 (gated on the accepted Part 1 package).

## Next

1. The G-P3-A round on the arm(s) the investigator picks — the round
   registers are on disk per run (`outputs/phase3/synthesis_rounds/ROUND1_REGISTER.md`).
2. The H2 signal: a ficha revision extending the coupling rule's product list
   to procurement/dev-process obligations (D-06..D-08), versioned, before any
   re-run of the Case 01 arms.
