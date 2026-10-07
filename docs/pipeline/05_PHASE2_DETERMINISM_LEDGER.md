---
document_id: AEGIS-PIPE-05
title: 'Phase 2 determinism ledger — what the pipeline can derive, and what it cannot'
version: 0.1.0
created: 2026-10-07
status: DRAFT
upstream:
  - SPEC.md
  - AGENTS.md
  - docs/pipeline/00_PIPELINE_MASTER_DESIGN.md
  - docs/decisions/ADR-2026-09-22_pipeline-io-contract.md
scope: >
  Diagnosis only. This document classifies every column of the two Phase 2
  deliverables by whether it is derivable from the Phase 1 deliverable plus the
  corpus, and records the defects found while doing so. It specifies no stage,
  no prompt and no schema change; §5 states what it deliberately leaves out.
evidence:
  script: scripts/phase2_ledger_scan.py
  corpus: cases/Case_0{1,2,3}_*/02_PHASE2_RULES/
---

# Phase 2 determinism ledger

## 1. The question and the answer

Before writing a Phase 2 pipeline, each output column has to be classified: can
code derive it from the Phase 1 deliverable and the frozen corpus, or does it
need a model? This document answers that per column, against the three case
deliverables.

The answer is uncomfortable, and it is not the one the phase structure implies.

**The `Operational Statement` column is a verbatim copy of the Phase 1 `Adjusted
Goal` column.** Sorting both columns and comparing the resulting multisets:
Case 01 `bc33181d` = `bc33181d`, Case 02 `3474612a` = `3474612a`. Case 03
differs on 4 rows, and §4.2 shows those are not omissions but corruptions. The
column that carries the phase's entire semantic payload is a byte-for-byte
transcript of the previous phase.

**The `RULE-*` tail — the one artefact SPEC assigns to Phase 2 that Phase 1 does
not produce — does not exist.** `RULE-` occurs 0 times in all six Phase 2
documents. ADR-004 calls it "the bridge artifact, still Phase 2"; AGENTS.md §6
calls it the tail that makes objectives testable.

So roughly 85–90% of Phase 2 is already deterministic, and the deterministic part
is a rename. That is the finding. It does not argue against building a pipeline;
it argues that the design question — *what is Phase 2 for* — comes first, because
a pipeline that automates the copy reproduces the finding at scale.

## 2. Method and its limits

The classification rests on three hand-authored case deliverables written before
any pipeline existed. That bounds what the ledger can claim:

- A column measured as deterministic is deterministic **given these three
  cases**. Three cases cannot prove a rule holds; they can only show a rule was
  followed.
- A column measured as *no rule found* is not *not derivable*. For `Verification
  Method` and `Responsible Owner` in particular, a rule may exist that three
  hand-written documents do not exercise. The ledger says "no rule found" and
  means it.
- All three deliverables were authored by the same executor under the same
  conventions. Agreement between them is evidence of consistency, not of
  correctness.

Every number below comes from `scripts/phase2_ledger_scan.py`. Re-run it after
any case edit; if this document and the scan disagree, the scan is right.

## 3. The ledger

Verdict vocabulary:

| Verdict | Meaning |
|---|---|
| **Deterministic** | A function of the Phase 1 deliverable and the corpus. No model. |
| **Mechanical + lookup** | Deterministic, but reads a per-case table (`case.yaml` overrides, as Phase 1 §5 Track B already does). Cheap, and it names where the human input goes. |
| **No rule found** | No derivation rule was found in the three cases. Not a proof of non-derivability (§2). |
| **Absent** | The phase structure assigns it to Phase 2 and it does not exist. |

### 3.1 `Doc01_Operational_Objectives.md` — objective table

Row counts: Case 01 62, Case 02 100, Case 03 134.

| Column | Verdict | Evidence | Derivation |
|---|---|---|---|
| Objective ID | Deterministic | All rows resolve; prefix `PO-`/`SO-` present on every row | Slot `NNN` inherited from the Phase 1 goal; prefix from the regulation ambit |
| Parent Goal | Deterministic | Literal Phase 1 `AG-` ID in every row | Copy of the Phase 1 goal's ID |
| Regulation | Deterministic | 2 / 4 / 5 distinct values, exactly the confirmed-regulation count | Function of the confirmed verdict set |
| **Operational Statement** | **Deterministic — and this is the finding** | md5-identical multiset to Phase 1 (Cases 01, 02) | Verbatim copy of the Phase 1 `Adjusted Goal` |
| Control Anchors | Deterministic | 62/62 set-identical (C01); C02 89/100 and C03 88/134 differ only by a `(primary)` marker; 1 real change (§4.4) | Inherited from Phase 1, which derives them by `controls.py` |
| Operational Scope (Ambit) | Mechanical + lookup | 2 / 4 / 5 distinct values, keyed on regulation | Per-regulation template + per-case scope nouns from `company_input.md` |
| Verification Criteria | Mechanical + lookup | 62 / 100 / 134 distinct — one per row, but only because the sub-domain slug varies | Template: `<evidence> confirms <slug> is enforced <scope>` |
| Verification Method | No rule found | 2 / 3 / 2 distinct values (`TEST`/`INSPECT`/`DEMONSTRATE`) | — |
| Responsible Owner | No rule found | 7 / 29 / 9 distinct values; no derivation from the domain-lead line or the governance matrix | — |
| Operational Translation | Mechanical + lookup | 35 blocks, one per active sub-domain, from one fixed sentence | Template + sub-domain ID + slug |
| **RULE-* tail** | **Absent** | 0 occurrences in 6 documents | Assigned by SPEC §6 / ADR-004; never built |

Two of these deserve the R10b scrutiny rather than a pass.

**Verification Criteria** renders one distinct string per row, which makes it
look bespoke. It is not: the template is fixed and the only variable is the
sub-domain slug, which the objective ID already carries. The R10b invariance
test — *would this read identically for a completely different company?* — it
would. It is compliance theater that happens to be mechanically generated.

**Operational Translation** is one sentence repeated 35 times, varying only in
the sub-domain ID and the slug inside it. It names no mechanism, no artefact and
no party.

### 3.2 `Doc02_Secure_Design_Principles.md` — engineering spine

7 principles (`PRIN-ENG-01..07`) in 3 cases, each appearing twice — once in the
§2–§5 category tables and once in the §6 skill-mapping table, hence 14 rows per
document. The scan compares all 14; the column verdicts below hold for the
principle tables. Column comparison across all three cases:

| Column | Verdict | Evidence |
|---|---|---|
| Principle ID, name | Deterministic | Identical across 3 cases |
| Academic Source | Deterministic | Identical across 3 cases, all 7 principles |
| Definition | Deterministic with 2 exceptions | Identical for 5 of 7; `PRIN-ENG-06` and `-07` embed case nouns (§3.3) |
| Constraint | **No rule found** | Varies across 3 cases, all 7 principles |
| Verification Method & Lead | **No rule found** | Varies across 3 cases, all 7 principles |
| §6 Skill + Path | Deterministic | Identical across 3 cases, all 7 principles |
| §6 Evaluation Scope | **No rule found** | Varies across 3 cases |

The `Definition` column is largely a baseline asset — the same text in three
unrelated companies for 5 of 7 principles. It belongs in `baseline/` and should
be copied, not regenerated.

The `Constraint` column is the genuine Phase 2 work in Doc02: Case 01 names
`Client, DMZ/Ingress, Application Core, and Storage`; Case 02 names
`Traveller-Facing Edge (eGate), Government Integration, Cloud Back-Office, and
Administration`. Reading a company's architecture off its intake is an LLM job.

§6 links to 7 absolute `file:///c:/Users/paulo.ribeiro/…` paths, identical in
all three cases. `baseline/skills/` holds all 7 directories, so the targets
resolve; the absolute form is a portability defect, recorded in §4.5.

### 3.3 The two definitions that are not baseline assets

Both are the same principle with the case's own vocabulary substituted into the
final clause:

| Principle | Case 01 | Case 02 | Case 03 |
|---|---|---|---|
| `PRIN-ENG-06` | "strictly scoped **DTOs**" | "strictly scoped **data views**" | "strictly scoped **data views**" |
| `PRIN-ENG-07` | "across **primary tables, caches, object stores**, and disaster recovery backups" | "across **edge caches, primary stores, archives**, and disaster-recovery copies" | identical to Case 02 |

`PRIN-ENG-06`'s `DTOs` is a technology-class term (R5/R13 territory) that the
other two cases avoid. `PRIN-ENG-07` in Case 03 is byte-identical to Case 02 —
Case 02's architecture, verbatim, in a bank's document (§4.6).

These two cells are the difference between *principle* and *principle applied to
this company*, and they are the only place in Doc02 where that distinction is
made. That is the shape a real Phase 2 column should have.

## 4. Defects found

Recorded with evidence, not repaired here (§5).

### 4.1 Phase 2 does not differentiate itself from Phase 1

`Operational Statement` is a copy of `Adjusted Goal` (Case 01 and Case 02, whole
multisets). The only artefact SPEC assigns here that Phase 1 does not produce —
the testable `RULE-*` tail — has 0 occurrences across 6 documents.

This is a methodology question, not an engineering one. `RULE-*` is what would
make an objective verifiable rather than restated, and it is precisely what is
missing. Building a pipeline before answering it would automate the copy.

### 4.2 Four Case 03 objective cells contain raw baseline content

`SO-D-01.3-003`, `SO-D-01.4-002`, `SO-D-01.4-004`, `SO-D-05.2-002` have an
`Operational Statement` cell that swallowed unrendered baseline text: a fenced
```` ```yaml ```` block, `## Security Requirements` headings, `req_id:` fields
and CSF-anchor rationale. Example, `SO-D-01.4-002` runs to a full YAML
requirement record inside the cell, then closes with a duplicate copy of the row's
own remaining columns.

These 4 rows are what makes Case 03's statement multiset differ from Phase 1.
They are corruptions, not omissions — the row count is 134 in both phases.

### 4.3 The slot-numbering rule differs between cases

Case 03 numbers objectives by rank among the regulations applicable to that
sub-domain; Cases 01 and 02 use the global canonical position of the regulation.
The scan reports both rules and they do not agree:

| Case | global-canonical | rank-among-applicable |
|---|---|---|
| Case 01 | 35/35 sub-domains | 35/35 |
| Case 02 | 35/35 | 35/35 |
| Case 03 | **23/38** | **38/38** |

In Cases 01/02 the two rules coincide, because with 2 regulations GDPR is always
present where CRA is. Case 03 has 5 regulations and sub-domains that skip GDPR —
`D-02.2` starts at `001` for CRA.

**Resolved by measurement (§5.1):** the running Phase 1 pipeline numbers by rank
among the regulations a sub-domain carries, and the hand-authored deliverables
left gaps for absent regulations. The pipeline's convention is the one in force;
the deliverables are the outliers. They remain valid for content and invalid as
id goldens.

### 4.4 `PO-`/`SO-` prefix is not a function of regulation in Case 01

| Case | `PO-` | `SO-` |
|---|---|---|
| Case 01 | GDPR 12 | CRA 34, **GDPR 16** |
| Case 02 | GDPR 29 | CRA 34, NIS 2 22, AI Act 15 |
| Case 03 | GDPR 29 | CRA 36, NIS 2 24, DORA 30, AI Act 15 |

Case 01 puts 16 GDPR rows under the `SO-` prefix where Cases 02 and 03 put all
GDPR rows under `PO-`. The §2 tension table cites these ids consistently with its
own objective table (e.g. it cites `SO-D-04.3-001`, which is the id the
objective table also uses), so the tension table is not the defect — the prefix
assignment is. Left unfixed, this makes the prefix a per-case judgement that no
pipeline rule reproduces.

### 4.5 Doc02 §6 uses absolute machine-local paths

`file:///c:/Users/paulo.ribeiro/OneDrive - Instituto CCG ZGDV/Ambiente de
Trabalho/Projetos_PhD/aegis-mvp/baseline/skills/…` — 7 per document, 21 total,
identical in all three cases. All targets exist in `baseline/skills/`. Under R12
these are cited control paths that must resolve; they resolve only on the
author's machine.

### 4.6 Case 03's Doc02 carries Case 02's architecture

`PRIN-ENG-01`, `-02` and `-07` in `cases/Case_03_OmniBank/` name `eGate`,
traveller and border assets — Case 02's subject, not a bank's. `PRIN-ENG-07`'s
`Definition` is byte-identical to Case 02's, so the contamination reaches the
definition column too, not only the constraint. The §6 skill-mapping rows are
clean of it.

This is the `Constraint` column, the one column the ledger marks *no rule
found* — the column that is supposed to carry the company's own architecture and
in one case carries another company's instead.

### 4.7 `DTOs` appears once in the whole Phase 2 corpus

`PRIN-ENG-06` in Case 01 reads "egress models must project strictly scoped
**DTOs**"; Cases 02 and 03 read "strictly scoped data views". `DTO` occurs in
exactly one document of the three (`grep -c` = 2 on that line, 0 elsewhere).

A data-transfer object is a technology-class term, and R5/R13 keep Phase 0–3
technology-neutral. It appears once, unreviewed, in the same column where the
other two cases chose the neutral phrasing. Under the R10b invariance test this
cell is *more* calibrated than its siblings — it says something specific — but
the specificity is a level-descent without a warrant, which
`templates/phase3_functional_spec_guidelines.md` §2.5 forbids.

### 4.8 One Case 03 objective lost its anchors

`PO-D-06.4-001` has anchors `—` in Phase 2 where Phase 1 carries
`GV.PO-P3, GV.PO-P4`. The Phase 1 value is itself malformed (`/ PF`), so this is
most likely an upstream rendering fault that Phase 2 passed through — but the row
now silently loses its control anchoring.

## 5. The prototype, and what it measured

`pipeline/src/phase2.py` implements the derivable half of §3 against a real
Phase 1 run directory. It re-derives anchors through `controls.goal_anchors`
rather than reading Phase 1's, inherits the objective slot, and emits `—` for
every cell with no rule. `pipeline/tests/phase2_test.py` holds the derivations
still.

### 5.1 The goldens cannot be a byte-golden

Run against `run_m08_musec2_1985228` (99 objectives, 38 sub-domains), the
prototype's ids do not line up with the Case 02 deliverable: 87 ids in common,
12 differing. The cause is §4.3, and it is now resolved by measurement rather
than left open — **the two use different slot conventions**:

| | D-01.4 in the run | D-01.4 in the Case 02 golden |
|---|---|---|
| GDPR | `001` | `001` |
| CRA | `002` | `002` |
| NIS 2 | absent | `003` (absent from the goal set) |
| AI Act | `003` | `004` |

The running Phase 1 pipeline numbers by rank among the regulations a
sub-domain actually carries; the hand-authored deliverable left a gap for an
absent regulation. Comparing the two by id therefore compares *different
objectives* — which is how `SO-D-02.4-002` first looked like an anchor
divergence and was not one.

**Consequence:** the case deliverables are a valid reference for content and
invalid as a reference for ids. Any Phase 2 gate that diffs against them by id
will fire on every row.

### 5.2 Anchor agreement, on the convention-independent key

Compared on `(sub-domain, regulation)` — the pair that means the same thing
under either convention — across the 63 pairs both artefacts carry:

| | Count |
|---|---|
| Anchor sets identical | 48 |
| Golden set is a strict subset of the derived set | 15 |
| Derived set missing an anchor the golden carries | **0** |
| Genuinely divergent | **0** |

All 69 distinct anchors the prototype emits resolve to a real file under
`baseline/CONTROLS/`, checked by `pipeline/tests/phase2_test.py`. R2b holds by
construction rather than by review, and the prototype is strictly more complete
than the deliverable it was checked against — consistent with §4.8, where a
hand-authored row lost its anchors.

### 5.3 A gate the hand-authored deliverables never had

`G0 — upstream completeness`. `run_m09_c2_meta_1991136` records 38 selected
sub-domains in `selection.json` but carries goal artifacts for 35: D-06.1,
D-06.3 and D-06.4 were selected and never derived. The prototype reports the
run as failed rather than rendering the 90 objectives it does have, because a
total that is wrong by 10% is invisible in a table this size and visible only
downstream, in Phase 3, as a coverage gap nobody can explain.

This is the shape of defect §4.2 and §4.8 share: a structurally valid document
carrying a silently wrong content. `doc_lint.py` cannot see any of them, and the
prototype's gates exist to.

## 6. What this document does not do

- No pipeline stage, prompt, ficha or `case.yaml` field. A column marked *no rule
  found* is a finding to act on later, not a prompt to write now.
- No repair of §4. Each defect is its own increment; §4.1 in particular is a
  methodology decision that should not be bundled with a text fix.
- No claim about Phase 3 feasibility. Phase 3 consumes `PO-`/`SO-` ids and cites
  them as chains; if the id scheme changes (§4.3, §4.4), Phase 3 chains must be
  re-anchored per R12b.
- No verdict on whether Phase 2 should exist in its current form. That question
  is §4.1 and it belongs to the researcher, not to this scan.

## 7. Reproducing

```bash
python3 scripts/phase2_ledger_scan.py                    # the measurements in §1-§4
python3 pipeline/src/phase2.py --run-dir <phase1 run> --out <dir>   # the prototype
python3 pipeline/tests/phase2_test.py                     # the derivations
```

The script is a diagnostic, not a gate: it exits 0 whatever it finds. If its
checks are worth keeping permanently — the polluted-cell detector (§4.2) and the
anchor-set comparison (§4.8) both catch defects `doc_lint.py` misses — they
belong in `scripts/check_traceability.py`, promoted deliberately rather than
grown here.