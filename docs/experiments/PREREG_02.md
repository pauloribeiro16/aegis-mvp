---
document_id: AEGIS-EXP-PREREG-02
title: 'Pre-registration EXP-05a/b/c/d — the robustness lane: gates, packs, equivalence, metamorphic inputs'
version: 1.0.0
created: 2026-10-04
status: REGISTERED — before any run
sources: 'docs/research/sources.yaml'
upstream: 'AEGIS-RES-04, AEGIS-RES-09'
---

# Pre-registration — EXP-05 (robustness lane)

**Registered before any experimental run**, on the PREREG_01 pattern: this
document fixes the hypotheses, predictions, falsifiers, fault taxonomies,
metrics, exclusions and stopping rules in advance. Nothing here may change
after the first run without a new version and an explicit note in §9 recording
what changed and why. The analysis runs **once**.

**Known limitations, stated first because they bound every claim.**

1. **One case** (`Case_01_TinyTask_SaaS`) and one case tree for the mutation
   faults. Nothing generalises to another company profile beyond what PREREG_01
   already bounds.
2. **05a tests three mechanical gates** — `doc_lint.py` (R11/R12),
   `check_traceability.py` (T1–T6), and `validate.py` (the L1 layer, offline
   mode `--run-dir`). The **L0 format gates and any check requiring a live LLM
   call are out of scope** — they cannot be mutated without a serving stack,
   and pretending otherwise would produce a false coverage claim.
3. **05c has one real ficha-change pair** (v2→v3). The repo has no second pair
   with an assembled `doc02` on both sides (`run_case01_1963504` aborted at P1;
   `case01↔v2` share identical fichas). The matcher-invariance claim is
   therefore tested on **one** real diff, n=1, and is stated as such.
4. **05d runs on the cluster** (4 seeded runs, seed=42, temp=0.2, current
   fichas). If the cluster is unavailable for the session, 05d stays
   registered-not-run and is reported as such — no local substitute is
   accepted, because the relations require the real serving stack.

---

## 1. EXP-05a — mutation testing of the deterministic gates (E-19)

**H1.** Each of the three gates detects ≥ 90% of seeded fault instances of the
classes it claims to cover, with a 0% false-positive rate on clean artifacts.

**Prediction (frozen).** Detection ≥ 90% per (gate × fault class); zero
findings on the unmutated sandbox baseline. Thresholds set before any fault is
seeded.

**Falsifier.** Any (gate × fault class) cell below 90%, or any clean-baseline
finding. The first under-covers; the second over-rejects.

**Design.**

- **Sandbox.** Full repo copy to `/tmp/aegis_exp05a_sandbox` (excluding
  `.git/`). All three gates run from the sandbox copy; `REPO` anchors resolve
  inside it. **Precondition:** the clean sandbox must pass all three gates
  (`doc_lint.py --strict` exit 0; `check_traceability.py --strict` exit 0;
  `validate.py --run-dir <clean run copy>` exit 0). If the clean baseline does
  not pass, that is recorded as a finding **before** any seeding and the
  affected gate's cells are reported against the pre-existing noise.
- **Seeding.** One fault per artifact copy; never combined. Every fault
  instance carries a unique marker string so detection is attributable.
  Detection = gate exit ≠ 0 **and** a finding naming the seeded artifact (or
  its marker) — a gate that fails for an unrelated reason on a seeded copy is
  recorded as *indeterminate*, not detected.
- **Fault taxonomy (frozen).** Classes are derived from the checkers'
  implemented checks and the repo's real defect history — not from invention:

  | Gate | Class | Instances |
  |---|---|---|
  | doc_lint | `R12 placeholder-cell` (`?` table cell) | 2 |
  | doc_lint | `R12 placeholder-path` (`?` inside a control path) | 2 |
  | doc_lint | `R12 todo-fixme` (TODO marker in body) | 2 |
  | doc_lint | `R11 meta-commentary` ("formerly known as … deprecated") | 2 |
  | doc_lint | `R12 unresolved control path` (well-formed `CONTROLS/` path, absent file) | 2 |
  | check_traceability | T1 (cited id does not resolve in the case's own Phase 1/2) | 2 |
  | check_traceability | T2 (chain-arrow left side lacks a driver of its own regulation) | 2 |
  | check_traceability | T3 (totals table does not sum; carried claim exceeds M) | 2 |
  | check_traceability | T4 (G1–G6 evidence file does not exist) | 2 |
  | check_traceability | T5 (matrix binds a driver no carrier cites) | 2 |
  | check_traceability | T6 (anchor outside the cited objective's published set) | 2 |
  | validate (L1) | non-canonical sub-domain id in `selection.json` | 2 |
  | validate (L1) | duplicated `AG-` id in goal rows | 2 |
  | validate (L1) | `AG-` id whose sub-domain part mismatches selection | 2 |
  | validate (L1) | unresolvable article citation in a Regulatory source cell | 2 |
  | validate (L1) | missing `§` section in `doc02` | 2 |
  | validate (L1) | tampered `§2` framing cell (≠ `framing.md`) | 2 |
  | validate (L1) | goal row with a dropped column | 2 |

  36 fault instances total (10 + 12 + 14). T2/T5/T6 instances are crafted against the real
  Case_02 deliverable structures (the only case with G-evidence and a coverage
  matrix), so the faults are realistic rather than synthetic strings.

**Anti-circular rule (binding).** If a gate is found to miss a class and is
subsequently fixed, the fix is validated on a **fresh, held-out fault set**
(new files, new marker strings) — never on the instances that revealed the
miss.

**Primary metric.** Detection rate per (gate × class); false positives on the
clean baseline; indeterminate count.

**Cost.** 0 GPU-h.

---

## 2. EXP-05b — pack coverage and utilisation (E-20)

**H2a (coverage, falsifiable).** Every corpus-inherited identifier in a step's
output was present in that step's pack. Prediction: coverage = 100%.
**Falsifier:** a single emitted corpus-inherited id absent from the paired
pack.

**H2b (utilisation, descriptive).** Packs contain corpus-inherited ids that
never reach any downstream artifact. No threshold is registered; the value is
measured and recorded as a lower bound.

**Runs under test.** EXP-02 **arm B** (`run_exp02_b_r01..r15`): the seeded
production configuration, complete at 15 runs.

**Citation grammar (frozen).**

- *Corpus-inherited ids* (coverage and utilisation apply to these):
  `SG-D-XX.Y.<TOKEN>` / `SO-D-XX.Y.*` / `SR-<REG>-NNN` via
  `\(SG\|SO\|SR\)-[A-Z0-9]+(?:\.[A-Z0-9]+)+`, and sub-domain ids via
  `D-\d{2}\.\d(?!\d)`.
- *Minted ids* (`AG-D-XX.Y-NNN`) are **excluded** from coverage — they are
  outputs of P4, not citations; their grounding is tested indirectly by 05a's
  L1 class V3 (sub-domain part vs selection).
- *Article references* (`Art./Artigo N` with a regulation name nearby) are a
  **secondary, lower-confidence** measurement — regex-resolved against pack
  text, never treated as a falsifier on their own.

**Scope per step.** Coverage is measured where corpus ids flow: **P3**
(selection output vs pack `003_p3_user.md`) and **P4** (per sub-domain, output
vs its `NNN_p4_D-XX_Y_user.md` pack). P1/P2 packs carry company input, not
corpus ids, and are excluded from coverage (declared). Utilisation is measured
on the **P4 packs** (the corpus-bearing packs): ids extracted per pack file,
searched downstream in the paired output, `doc02_adjusted_goals.md`,
`phase1_output.md`, `steps/*.json|yaml`.

**Metrics.** Coverage rate per step (ids; articles secondary). Utilisation per
P4 pack (a) id-level — pack ids appearing downstream; (b) file-bytes level —
bytes of pack files whose ids are all absent downstream. Utilisation is a
**lower bound** (paraphrase without an id counts as unused); this is recorded,
not fixed.

**Exclusions.** Runs with missing paired files are excluded per-instance and
counted. `*_attempt2` outputs: only the final (non-attempt) file is the step
output.

**Cost.** 0 GPU-h.

---

## 3. EXP-05c — cross-version equivalence, matcher-pinned (E-21)

**H3.** On a real ficha-change diff, the choice of answer-matching rule changes
the measured drift **rate** (replicating [S-202]/[S-259] on this corpus) but
not the **conclusion** about which sub-domains changed (the [S-238]
invariance).

**Predictions (frozen).** (a) drift rate under M1 (exact text) > drift rate
under M2 (id-anchored), strictly, unless both are zero. (b) The set of
sub-domains classified "changed" is **identical** under M1 and M2.

**Falsifier.** Prediction (b): if the matchers disagree on *which* sub-domains
changed, no equivalence metric is trustworthy until a rule is fixed by fiat,
and E-08 has no valid instrument.

**The pair.** `run_case01v2_1963538` → `run_case01v3_1969943`, assembled
`doc02_adjusted_goals.md` on both sides. Fichas changed between them
(p1 1.0→1.1, p3 1.0→1.1, p4 1.1→1.5, p5 1.0→1.2) — **declared confound**: this
measures cumulative ficha-generation drift, not the effect of any single ficha.

**Matchers (frozen).** Goal rows parsed from the §3 tables (columns `ID |
Adjusted goal | …`):

- **M1 — exact text:** row is *unchanged* iff same `AG-` id **and**
  byte-identical goal text after whitespace normalisation.
- **M2 — id-anchored:** row is *unchanged* iff same `AG-` id and same
  `D-XX.Y` parent; text differences are *wording drift*, not change.
- **M3 — sub-domain set:** the set of sub-domains having ≥1 goal row.

**Primary metrics.** Drift rate per matcher (changed rows / rows); the
symmetric difference of "changed sub-domain" sets between M1 and M2
(prediction (b)).

**Secondary (bonus pair, declared).** `run_exp02_b_r01` vs `run_case01v3`:
fichas differ only on p1 (v1.0.0 vs v1.1.0) — a near-replication pair. If
EXP-02's byte-identity extends here, M1/M2/M3 drift ≈ 0 and the matchers are
also validated on the null case.

**Limitations.** One diff pair (limitation 3); goal-text normalisation rules
(whitespace, unicode dashes) are frozen in the analysis script and listed in
the results.

**Cost.** 0 GPU-h.

---

## 4. EXP-05d — metamorphic input relations (E-22)

**H4.** The pipeline's output obeys the metamorphic relations implied by R6/R8
even though no gate tests them end-to-end:

- **M1 (R6, invariance):** reordering the sections of `company_input.md`
  leaves `steps/fact_sheet.yaml` byte-identical.
- **M2 (R8, invariance):** adding the preregistered irrelevant product line
  (below) leaves `steps/verdicts.json` and `steps/selection.json` sets
  unchanged.

(M3 — R3 monotonicity MICRO→SMALL — is **not run** in this battery: it is
judge-scored and gated on E-17's noise floor, per the backlog entry.)

**Predictions (frozen).** M1: fact sheet byte-identical (seed=42; EXP-02
established that identical inputs give byte-identical runs, so any difference
is input sensitivity, not sampling). M2: verdict set and selection set
identical.

**Falsifiers.** M1: any byte difference. M2: any verdict flip or selection
delta. (M1's comparison excludes only the run-id line, per the EXP-02
convention.)

**The M2 perturbation (preregistered verbatim).** Appended to the intake's
products section:

> TinyTask also resells refurbished office furniture (physical goods, no
> software component, no data processing) to local businesses.

**Declared rationale for irrelevance:** none of the five scope criteria in
SPEC §5 (GDPR, CRA, NIS2, DORA, AI_Act) fires on physical goods without a
digital element, data processing, or a service role; the line therefore must
not change P2 verdicts or the sub-domain selection. If it does, R8's behavioural
enforcement fails.

**Design.** Four fresh runs under the **current** fichas, seed=42, temp=0.2,
on the cluster: (control, M1-perturbed), (control, M2-perturbed). Controls are
fresh runs, not reused historical ones, so arm and condition are fully
crossed. Each pair compared at the named artifact.

**Threats.** n=1 case; M2's irrelevance judgement is the weakest point and is
mitigated only by this preregistration; a positive result does not prove R6/R8
in general — scoped to the tested relations.

**Cost.** ~2 GPU-h (4 runs × ~42 calls).

**Stopping rule.** If the cluster is unreachable or the queue exceeds the
session, 05d is reported registered-not-run with the submission state recorded.
No local re-implementation is accepted.

---

## 5. Analysis plan

Each sub-experiment's analysis runs **once**, scripted, over all instances, no
post-hoc exclusions beyond those declared above. Every result row carries its
raw evidence (file, marker, gate output excerpt). Results land in
`docs/experiments/EXP05_robustness_results.md` and `00_RESULTS.md` is updated
in the same session.

## 6. Exclusions

Declared above per sub-experiment and nowhere else. Any instance that cannot
be executed as designed (e.g., a fault class whose host artifact does not
exist) is recorded as *not seedable* with the reason — silently dropping it is
not permitted, because the denominators of the detection rates are the
preregistered instance counts.

## 7. Held-out rule (restated because it binds future work)

A gate modified after seeing EXP-05a results must be re-evaluated on a fresh,
held-out fault set. The seeded instances in this battery are spent the moment
their results are recorded.

## 8. What changes if hypotheses fall

- H1 falls → the named gate's PASS is downgraded from *evidence* to
  *heuristic* in the mapping document, and the specific class becomes a bug
  ticket with a held-out re-test.
- H2a falls → correctness investigation before any further quality work (a
  cited id the model never saw breaks the grounding premise).
- H3 falls → E-08 blocked; the canonical matcher is fixed by convention and
  recorded in the mapping document as a design decision, not a measurement.
- H4 falls → the violated relation becomes a new gate (M1/M2 are mechanically
  checkable post-hoc), converting the metamorphic test into a permanent
  invariant.

## 9. Change log

- v1.0.0 — 2026-10-04 — registered before any run. No changes.
