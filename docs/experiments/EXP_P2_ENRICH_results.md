---
document_id: AEGIS-EXP-P2-ENRICH
title: 'Phase 2 enriched — the four increments on production runs'
version: 1.0.0
created: 2026-10-09
status: 'COMPLETE — PARTIAL, with three registered defects'
prereg: PREREG_P2_02.md
prereg_version: 1.0.0
upstream: 'docs/experiments/EXP_PHASE2_results.md (P2-01); docs/pipeline/05_PHASE2_DETERMINISM_LEDGER.md'
---

# EXP_P2_ENRICH — Phase 2 enriched

**Results for [PREREG_P2_02.md](PREREG_P2_02.md) v1.0.0, frozen 2026-10-09 before the
first enriched Phase 2 job was submitted.** Deucalion, `qwen3.8:27b`, seed 42,
temperature 0.2, pipeline rev `3a9c0fb` + the wrapper fix that followed it, n=1
per case. Phase 1 inputs are copies of the M07 runs (`b2fe2aa`) — deviation D1 of
P2-01, unchanged.

| Run | Case | Job | Outcome |
|---|---|---|---|
| `run_p2c2` | Case_02_SecureBorder_Solutions | 1996917 | **ok** — 99 objectives, 38/38 operationalized |
| `run_p2c3` | Case_03_OmniBank | 1996898 | **ok** — 129 objectives, 37/38 operationalized |
| `run_p2c1` | Case_01_TinyTask_SaaS | 1996859 (p4 repair) → 1996860 (phase2) | **aborted at G0** — registered as D1, see §Case 01 |
| `run_p2d_c1` | Case_01_TinyTask_SaaS | 1997413 (p3) → 1997414 (all) → 1997492 (phase2) | **ok after the P3 filter fix** — 65 objectives, 37/37 operationalized, see §Resolution |

---

## Verdict: **PARTIAL**

Q1–Q3 and Q5 and Q7 hold on both completed cases. Two preregistered bars fired:
**Q4 on Case 03** (one sub-domain not operationalized) and **Q6's padding bar on
both cases** (the model writes ~3 rules per objective where the ficha specifies
1–2). Under the decision rule this is PARTIAL: the deterministic spine is sound,
the increments produce substance, and two specific properties of that substance
fell short of what was registered before the runs.

| ID | Prediction | Bar | Measured (c2 / c3) | |
|---|---|---|---|---|
| Q1 | Doc01 is exactly the Phase 1 goal set, 0 G0–G4 | 0 findings | **0** / **0** | pass |
| Q2 | Every control anchor resolves (R2b) | 0 unresolved | **0** / **0** | pass |
| Q3 | Doc02 clean, `grounding_ratio` ≥ 0.50 | 0 G5–G7; ≥0.50 | **0, ratio 1.0** / **0, ratio 1.0** | pass |
| Q4 | Seams ≥ 95%, all 38 sub-domains operationalized | ≥95%, 38/38 | **100%, 38/38** / **96.9%, 37/38** | **fail (c3)** |
| Q5 | No method above the 60% collapse ceiling | ≤0.60 | **0.339** / **0.393** | pass |
| Q6 | Catalogue exists: ≥1 rule/objective, mean ≤ 2.5 | 1.0–2.5 | **3.07** / **3.16** | **fail (both)** |
| Q7 | New cells carry the company, not a template | mean ≤0.60 | **0.044** (translations), **0.065** (rules) | pass |
| Q8 | Case 01 repair derives goals for D-08.3 | ≥1 goal | **0 goals** — and no goal exists to derive (D-08.3 has Sub-SOs only for DORA/NIS2, confirmed by nobody) | **refuted, for the wrong reason** |

## The four increments, measured

**1. Methods and falsifiable criteria (Increment 1).** The three columns ADR-013
D3 left as `UNSET` seams are now filled on **99/99** (c2) and **125/129** (c3)
objectives, with every method inside the published vocabulary. The
mode-collapse ceiling does not fire: the top method takes 33.9% (c2) and 39.3%
(c3) of its batch, and all four are used in every case — the batch is a
classification, not a default. Criteria name artefacts, not adjectives ("the
cryptography policy SHALL be reviewed...", "quarterly configuration audit
reviews encryption settings against the published baseline checklist").

**2. Operational translation (Increment 2).** 38/38 and 37/37 paragraphs, and
every one of them contains vocabulary from its own fact sheet (38/38 and 37/37
measured). They are not the baseline restated with a company name swapped in:
the D-01.3 translation for OmniBank separates key custody from "the operational
environments (mobile banking, web banking, OmniScore)" because that is the
company's declared architecture.

**3. Strategic tensions (Increment 3).** The 9 tensions Phase 1 recorded under
`D-04.3`, `D-05.1`, `D-05.2`, `D-06.3`, `D-06.4`, `D-09.2`, `D-09.4` and
`D-10.1` render into Doc01 §2 with their conflict and resolution strategy. This
increment is a deterministic re-render — its quality is inherited from `p4t`,
not re-measured here, exactly as the preregistration declared.

**4. The RULE-* tail (Increment 4).** **304 rules** (c2) and **395** (c3) reach
the rendered documents. Every one contains `SHALL` or `MUST`, every id is
canonical and unique within its sub-domain, and every `verification_target` is
inside the vocabulary — zero violations of any kind across 699 rules. This is
the artefact the ledger recorded as *absent from all six hand-authored
deliverables* (§4.1: "0 occurrences in 6 documents"), and it now exists as a
first-class output.

## The two bars that fired

### Q6 — the catalogue is padded, not missing

Every objective carries **at least 2** rules (minimum observed: 2 on both
cases), against a ficha that specifies 1–2. The distribution is 2:18/3:64/4:11/5:4/6:2
on c2 and 2:20/3:76/4:21/5:6/6:1/7:1 on c3 — mean **3.07** and **3.16** against a
registered ceiling of 2.5. The rules are individually valid EARS statements and
none duplicate an id; the defect is volume, not syntax. A rule set that is
uniformly longer than specified is the same shape as a checkbox that is uniformly
ticked: the gate cannot see it because each rule is a real sentence. This is
recorded, not patched — the padding bar is preregistered and fired.

### Q4 — one sub-domain lost on Case 03

`D-03.3` (Authorisation & Least Privilege) has no `RULE-*` block and `—` in all
three enriched columns. The mechanism is in the trace and fully diagnosed — see
the repair-message defect below. The four objectives render with their Phase 1
statements and their derived control anchors (`PR.AA-05`, `PR.AA-06`,
`DE.CM-09`, `PR.PS-02`, `RS.CO-03`), so the document is complete as a
regulatory spine; it is the operational layer that is missing for that
sub-domain.

## Three defects the runs exposed

### 1. The L0 repair message is tuned for p4 and damages p2o answers

`D-03.3`'s first attempt put a `RULE-*` id in the objective-id field
(`p2o: objective 0 id 'RULE-D-03.3-001' is not a PO-/SO-D-XX.Y-NNN id`). The
repair message (`steps.py:1471-1478`) says:

> *Re-emit the SAME answer with only that defect corrected. … Do not add
> material, do not restate the baseline, do not elaborate — the answer must come
> out the same length or shorter.*

For p4's tabular extraction that is correct advice. For p2o the model over-complied:
it renamed `objective_id` to `id`, prefixed all four objectives `PO-`, and
**dropped the `rules` array entirely** — a shorter answer that fails a second
time. The stage records it and continues (37/38 operationalized), but the
sub-domain is lost.

Three of the four L0 repairs in this matrix were the same benign class — a
two-digit slot (`SO-D-04.4-01`) where R4 requires zero-padded three digits — and
all three recovered. The message is not useless; it is wrong for this step. The
fix is a p2o-specific repair clause that restates the schema rather than
minimising length. **Not applied**: the preregistration is frozen and c2/c3 ran
under this message, so changing it now would make the two cases incomparable.

### 2. An R6 fabrication reached the Doc02 constraint column

OmniBank's `PRIN-ENG-04` constraint ends: *"…all state transitions in the
**transactional email service** must fail closed."* OmniBank's fact sheet
declares four product lines — mobile banking application, web banking platform,
payment processing services, OmniScore — and contains **no email service at
all** (`grep -ci email` on the fact sheet: 0). `email` and `transactional` are
the only two tokens in that constraint absent from both the fact sheet and the
principle definition. G7 did not catch it because G7 reads *other cases'*
intake forms: it detects cross-case contamination, not invention.

The same scan over all 7 constraints of Case 02 finds **no** fabricated
component — its undeclared tokens are ordinary English (`boundary`, `central`,
`systems`). One fabricated component in seven, in the one generative column of
Doc02, is the honest size of this defect: rare, and invisible to every gate that
ran.

**What does not work as a gate:** a token-level "declared in the fact sheet"
test. Measured over the 37 operational translations of Case 03 it fires on
**37 of 37** — `ensure`, `implement`, `shall`, `testing` are not in a two-page
fact sheet either. That is the same failure as G7's original bug (firing on
`boundary`, `including`, `within` — fixed in `aa2600e`): a fact sheet declares a
company's *assets*, not the English used to describe them. A narrow check on
named compound components is the only shape left, and it is registered as future
work rather than shipped on the strength of one example.

### 3. The method distribution is measured over a population the document does not contain

`method_distribution` counts every objective in the stored `p2o` blobs:
135 for Case 03, against 125 objectives that actually render. The model emits
**10 objectives for slots Phase 1 never derived** (`D-01.1-005`, `D-04.3-006`,
`D-04.3-007`, `D-05.1-003`, `D-05.2-003/004`, `D-05.3-003`, `D-05.4-002`, …).
They are silently dropped by the row-driven render and their rules never reach
the document, but they are counted by the distribution that feeds the diversity
gate. Measured both ways, the verdict is unchanged:

| Population | n | INSPECT share |
|---|---|---|
| all stored objectives | 135 | 39.3% |
| objectives that reach Doc01 | 125 | 40.8% |

Both are far below the 60% ceiling, so no prediction changes. The metric should
count what the document contains; that is a one-line change deferred to the next
revision for the same reason as the repair message.

## Case 01: the repair failed, and that is the result

PREREG_P2_01 §2 registered Case 01 as excluded (X1) because
`steps/goals/D-08_3.json` carries an empty `goals` array. The researcher
rejected that exclusion (2026-10-09): a case that does not complete is a result,
not a reason to swap it. Case 01 was therefore attempted, with the upstream
repair the preregistration specified.

**Two repair rounds, two zero-goal outcomes.** Job 1996849 was submitted after
deleting the empty artifacts and reported `38/38 carried` in 12 seconds with
**zero model calls** — the resume marker had found the sub-domain already done.
The marker tests `steps/goals/D-08.3.md` (dotted) while the JSON artifact is
`D-08_3.json` (underscored); deleting only the underscored files does not force
re-derivation. Job 1996859, after deleting the dotted file, made **one real
call** and still derived zero goals.

The model's answer is explicit (`steps/goals/D-08.3.md`, preserved on the fork):

> ### D-08.3 — High-level Security Objective (regulation-neutral)
> None — no Sub-SO for the confirmed regulations.

**That answer was correct, and this section originally said it was not.** An
earlier reading of this document claimed the model was wrong because
`baseline/domains/D-08_Human-Factors/D-08.3/regs/DORA.md` carries
**`SG-DORA-014`** ("Members of the management body shall actively keep up to
date with sufficient knowledge and skills…", DORA Art. 5(4)) and sits unused.
DORA is **not** confirmed for Case 01 — the verdicts are GDPR *and CRA only*,
with NIS2, DORA and AI Act all recorded as *does not apply* (`size_employees: 8`,
no financial entity, no high-risk AI). D-08.3's Sub-SOs exist for DORA and NIS 2
and for nothing else, so with GDPR and CRA confirmed there was nothing to derive,
and the model said so precisely.

The defect was upstream of the model and above it. `candidate_subdomains` — the
deterministic P3 pre-filter — tested whether the module **file** `regs/<REG>.md`
existed. The corpus modularises all five regulations into every sub-domain, so
D-08.3 has a `regs/GDPR.md` that declares no `SG-D-08.3.GDPR`: file presence
said "candidate", the pack carried two regulation modules with no cards in them,
and P3 had selected D-08.3 on a rationale ("GDPR Art. 39(1)(b) management
awareness") that has no baseline source here. R2 forbids deriving an obligation
the corpus does not ground, so the honest outcome was an unclosable run, caught
by G0 rather than shipped as a silently short document. Fixed in `compose.py`
after this matrix closed — see the correction note below.

Phase 2 then did what the gate exists for: **aborted** at G0 with
`upstream incomplete: 1 selected sub-domain(s) have no Phase 1 goal artifact:
D-08.3` (jobs 1996856 and 1996860). This is deviation D1 of the preregistration,
written before submission. Notably, a weaker G0 that accepted the file's
existence rather than its contents was drafted during this work and **reverted**
before the runs — with the file-count gate, Case 01 would have produced a
document whose objective total was quietly one sub-domain short, with no marker
that anything was missing.

## Resolution — Case 01 closes after the P3 filter fix

`run_p2c1` is preserved as the P2-02 record. The repair ran on a fresh fork,
`run_p2d_c1`, against the corrected code (`compose.py`, rev `55f675c`):

| Stage | Job | Result |
|---|---|---|
| `p3` | 1997413 | **37 selected** (D-08.3 absent — the filter now requires a Sub-SO card) |
| `all` (p2, p4, p4t, p5) | 1997414 | p4 **37/37 carried**, p5 assembled, rc=0 |
| `phase2` | 1997492 | **65 objectives, 37/37 operationalized, 65/65 seams, rc=0** |

Two jobs on the way there were infrastructure, not pipeline: 1997453 and
1997460 each landed on a node where `ollama serve` stopped responding during
warm-up (the log went silent for ~20 minutes with 81 GiB free on the GPU, and
every `p2o` call burned its five 180-second retries). Both were cancelled and
resubmitted; pinning `--nodelist=gnx509`, where the OmniBank run had already
succeeded, loaded the model in minutes and completed 38 calls with **zero
failures**.

Case 01's own numbers, and what they say:

- **65 objectives over 37 sub-domains**, 65/65 seams filled — the seam fill
  that P2-01 could not produce at all.
- **251 `RULE-*`**, zero EARS violations, zero duplicate ids within or across
  sub-domains.
- **Method distribution** `INSPECT 40, DEMONSTRATE 28, ANALYZE 23, TEST 7` —
  top method **40.8%**, far below the 60% ceiling. `TEST` falls to 7 of 65
  (16%) where the two bank cases ran 15–18: an eight-person SaaS has fewer
  things a CI suite can prove than a financial entity, and the distribution
  moved in the direction the company's size predicts. That is the opposite of
  mode collapse, and it is the first cross-case evidence that the method
  assignment is reading the company rather than picking a favourite.
- `grounding_ratio` **1.0**, 7/7 principles bound.
- Doc01 722 lines / 76 tables, Doc02 64 lines; 0 column deviations, 0 glued
  headings, 0 `?` cells (R10/R12 inspection).

The three cases now cover the full range: 37/38/38 sub-domains, 65/99/129
objectives, two to five confirmed regulations. Every prediction this document
records was measured on two cases and not adjudicated by Case 01's
preregistered cell — the P2-02 matrix stays as recorded, and this fork is a
post-hoc resolution with its own provenance.

## Deviations from the preregistration

1. **D1 (registered, pre-run):** Case 01 attempted via the upstream `p4`
   repair; a second zero-goal repair aborts the cell at G0. Outcome recorded in
   full above.
2. **D2 (harness, post-run, mine):** `steps.parse_p2o` was a one-argument
   wrapper that dropped the sub-domain when delegating to `phase2.parse_p2o`.
   Jobs 1996847/1996848/1996890/1996891 died in ~45 seconds with
   `TypeError: parse_p2o() takes 1 positional argument but 2 were given`. The
   phase2-level test suite never exercised the `steps` route and a `--dry-run`
   never reaches `_validate`, so both local checks passed. Fixed, committed, and
   pinned by two new assertions on the wrapper itself.
3. **D3 (infrastructure):** job 1996897 spent 26 minutes with zero progress —
   `warm-up failed after 5 attempts: connection error … timed out` — and was
   cancelled and resubmitted as 1996917, which completed in 35:46. No data from
   the cancelled job is used.

## Deliverables

| Company | Run | Files |
|---|---|---|
| TinyTask | `run_p2d_c1` | Doc01 (722 lines, 76 tables) · Doc02 (64 lines) — in the run directory; `output/` is gitignored |
| SecureBorder | `run_p2c2` | [`Doc01`](../../../output/SecureBorder/phase2/run_p2c2/Doc01_Operational_Objectives.md) (897 lines, 78 tables) · [`Doc02`](../../../output/SecureBorder/phase2/run_p2c2/Doc02_Secure_Design_Principles.md) (64 lines) |
| OmniBank | `run_p2c3` | [`Doc01`](../../../output/OmniBank/phase2/run_p2c3/Doc01_Operational_Objectives.md) (1012 lines, 77 tables) · [`Doc02`](../../../output/OmniBank/phase2/run_p2c3/Doc02_Secure_Design_Principles.md) |

Inspected physically per R10: table column integrity 0 deviations across 77/78
tables, no glued headings, no `?` cells, no TODO/FIXME/`<>` (R12). One rendering
defect was found this way and fixed — a sub-domain with no `RULE-*` block ran its
objectives table straight into the next `###` heading without a blank separator
(`D-03.3`, the one failed call).