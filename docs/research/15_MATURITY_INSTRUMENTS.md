---
document_id: AEGIS-RES-15
title: 'Measuring maturity — the NIST CSF 2.0 Maturity Tool read against our QNRCS instrument'
version: 0.1.0
created: 2026-10-11
status: ACTIVE
artefact: docs/research/maturity/NIST-CSF2.0-Maturity-Tool-v1.0.3.xlsx
---

# 15 — Measuring maturity: the NIST tool read against our QNRCS instrument

The investigator supplied the workbook he had been looking at while asking for a
maturity comparison [S-384]. This document records what the artefact actually is,
what its measurement model is, and — the reason it matters here — four defects it
exposes in the instrument this repo built on 2026-10-11
(`scripts/qnrcs_maturity.py`, `pipeline/src/aegis_pipeline/phases/phase3/maturity.py`).

Everything below is read from the workbook's own cells. Cell addresses are given
so each claim can be re-checked without re-deriving it.

---

## 1. What the artefact is — and is not

| Property | Value | Where |
|---|---|---|
| Title | NIST CSF 2.0 Maturity Tool | file name |
| Version / date | v1.0.3, released 1 March 2024 | `Introduction!A2`, `Introduction!Q3` |
| Author | John Masserini (`JohnMasserini.com`) | `Introduction!A2` |
| Published by NIST | **No** | — |
| Sheets | Introduction, Maturity Levels, NIST CSF Summary, CSF 2.0, Privacy Summary, Privacy Framework Core, References | `workbook.xml` |
| Sheets | 7 visible, 0 hidden | `workbook.xml` |

**It is a third-party practitioner tool, not a NIST publication.** The
Introduction says so in its own words: *"This is in no way intended to infringe
upon any work the good folks over at NIST have done. All of the questions and
associated information on the 'NIST CSF Details' tab is completely owned by
NIST."* (`Introduction!A2`.) The References sheet points at GRC vendor
frameworks (NIST 800-53, CIS CSC, COBIT 5, ISA 62443, ISO/IEC 27001), which is
the register of a consultancy spreadsheet.

Consequence for this repo: it may be **cited as a method reference**. It may not
be cited as an authority for what NIST says, and it carries no weight in
`docs/experiments/METRICS.md` as a threshold basis.

**It contains nothing about Portugal.** There is no QNRCS, no tier, no
entity-size classification anywhere in the seven sheets. The tier logic this repo
uses is not borrowed from here.

---

## 2. The measurement model, in full

This is the part that matters, because it is a complete and internally
consistent answer to "how do you score maturity on a 1-to-5 scale".

### 2.1 The scale is 1–5, with names (`Maturity Levels!A2:A6`)

| Level | Name |
|---|---|
| 1 | Initial |
| 2 | Repeatable |
| 3 | Defined |
| 4 | Managed |
| 5 | Optimizing |

There is no level 0. Partial values are permitted — *"you are not locked into a
hard 0-5 value; partial values (i.e. 2.5) are permitted"* (`Introduction!A31`).

### 2.2 Two independent axes, not one (`Introduction!A2`)

> *Policy Maturity: How well do your corporate policies, procedures, standards,
> and guidelines satisfy the NIST CSF requirements?*
> *Practice Maturity: How well do your actual operational practices satisfy the
> NIST CSF requirements **regardless of what your policies & standards say**?*

Every subcategory carries a Policy score, a Practice score, and **a free-text
reasoning field for each** (`CSF 2.0!G:J`, `Privacy Framework Core!L:O`). The
axis definitions are different questions, not two views of one answer.

### 2.3 The level criteria are quantitative, not adjectival

Policy expectations turn on an **exception rate**: <5% of activity at Level 3,
<3% at Level 4, <0.5% at Level 5 (`Maturity Levels!B4:B6`). Practice
expectations turn on **evidence availability**: Level 3 is evidence "for most
activities" with <10% exceptions; Levels 4 and 5 require evidence "for all
activities" with process metrics captured and reported (`Maturity Levels!C4:C6`).

### 2.4 The target is per-category and editable

Each category carries its own `Target Score` (`NIST CSF Summary!D4:D25`,
`Privacy Summary!C4:C21`), defaulting to 3. The Instructions are explicit that
*"In most cases, the target of some controls will be different than others"* and
that this is *"an 'end goal' of what you think the right level of control for
your organization"* (`Introduction!A31`).

### 2.5 Roll-up is an unweighted arithmetic mean

`NIST CSF Summary!E4` is literally `=SUM('CSF 2.0'!$G$5:$G$9)/COUNTA('CSF 2.0'!$C$5:$C$9)`.
Subcategory → category → `Overall Average Score` (`E3` = `SUM(E4:E25)/COUNT(E4:E25)`).
No weighting by risk, criticality, or control count.

### 2.6 The radar is three series over the categories

`xl/charts/chart1.xml` and `chart2.xml` are `radarChart`, `radarStyle="marker"`,
with three series each — `Target Score`, `Policy Score`, `Practice Score` — over
23 axes (the CSF categories) and 18 axes (the PF categories). No explicit
min/max is set, so the radial scale auto-ranges.

### 2.7 The sample numbers are synthetic — do not read them as a result

`CSF 2.0!H1`: *"The numerical values in columns G and I are for demonstration
purposes only. Clear all values before starting your assessment."* In the
Privacy sheet every row satisfies `policy + practice = 5` exactly (5/1, 4/2, 3/3,
2/4, 1/5) — a generated demonstration pattern, not an assessment. The CSF sheet's
values do not even follow that pattern.

---

## 3. Inventory comparison: ours is identical, so nothing to import

Counting the subcategories in the workbook against the referentials in
`baseline/CONTROLS/`:

| Referential | Workbook | Ours | Only in workbook | Only in ours |
|---|---|---|---|---|
| NIST CSF 2.0 | 106 | 106 | — | — |
| NIST Privacy Framework | 100 | 100 | — | — |

**Zero differences in both directions.** The workbook contributes no control
that `baseline/CONTROLS/` lacks, and misses none that it has. It is a *scoring
sheet over an inventory we already hold*, not a source to reconcile against.

Its coverage confirms two things independently:

- The CSF core is 23 categories / 106 subcategories across 6 functions
  (`CSF 2.0`), matching our 106 JSONs.
- **The Privacy Framework tab is titled "NIST Privacy 1.0 Categories"**
  (`Privacy Summary!B2`) and the Introduction dates it *"NIST Privacy Framework
  1.0 (January, 2020)"* (`Introduction!A2`). See §6.

---

## 4. What this exposes in our own instrument — four defects

`scripts/qnrcs_maturity.py` and `maturity.py` were built earlier today on the
QNRCS tier semantics. Read against this workbook, four things are wrong or weak.

### D1 — the level names were missing, and our level 5 was an invention

Our scale is 0–4 with *"5 reserved for external certification (art. 27.º)"*
(`maturity_levels()` docstring; emitted as `maturidade.escala`). The workbook's
level 5 is **Optimizing** — continuous improvement — and has nothing to do with
certification. There is no source for the certification reading; it was inferred
from the QNRCS article and is not how anyone else uses a 1–5 maturity scale.

The named levels are also worth having for a reason beyond tidiness: *Initial*,
*Repeatable*, *Defined*, *Managed*, *Optimizing* are interpretable without the
tool, which a bare integer is not.

### D2 — one axis where the domain has two

Our radar plots a single series per objective. The workbook's central design
move is that policy and practice are **different questions with different
evidence**. For AEGIS this is not a nicety:

- The **policy** axis is what Phase 3 Part 1 produces. `Doc01`, `Doc02` and
  `Doc03` are statements of what must be written down and by whom.
- The **practice** axis is what Phase 4 verifies. Nothing in a requirements
  document is evidence that the thing happens.

So at Fase 3 the honest report is *one axis measured, one axis structurally out
of reach* — and our single polygon silently claims both.

### D3 — ours measures coverage, and calls it maturity

This is the substantive one. Our `nivel_atingido` is a step function of a
coverage fraction: does the run's artifact cite an anchor that maps to this
QNRCS control. The workbook's score is an **assessment** — a value judged per
subcategory, with written reasoning, against stated criteria.

Those are different constructs. Anchor presence is evidence about the
*specification*, not about the organisation's maturity. The measured result on
`run_p2enr_c1` shows the consequence: coverage of the tier-básico set is 31.8%
(34/107), and the step rule then puts **all six objectives at level ≤ 1** —
ID 1, PR 1, GR 1, DE 1, RS 1, **RC 0**. The radar is a flat hexagon near the
centre. The number is not wrong; it is the number a coverage-derived level
produces, and it carries no resolution between "one control of twenty-three" and
"half of them".

### D4 — unweighted means of ordinal levels, over unequal denominators

The workbook's roll-up is a plain mean of ordinal levels. Two consequences it
partly mitigates and we do not:

- **Averaging ordinals treats Initial→Repeatable as the same distance as
  Managed→Optimizing.** The workbook is honest about this being adjustable
  advice, not a validated instrument.
- **Granularity varies with category size.** `NIST CSF Summary!C` makes this
  visible — PR.AT has 2 subcategories, GV.SC has 10 — so PR.AT's score moves in
  steps of 0.5 while GV.SC's moves in steps of 0.1. We hit the same defect
  earlier today in QNRCS, where RS and RC carry only 2 controls at the básico
  tier, and the workbook's `# Controls` column is the mitigation we lack.

---

## 5. Measured finding: the PF mapping reaches 54 of 100 controls

This is the answer to "não vejo nada aqui naquilo que produziste de controlos
do PF". The PF controls are not missing from the referential — all 100 exist.
They are mostly unreachable from the requirement chain.

Walking the `nist_pf` arrays in `baseline/MAPPINGS/sr_control_mappings/*.json`:

| Regulation | Distinct PF controls reachable |
|---|---|
| GDPR | 54 |
| CRA, NIS2, DORA, AI_Act | 0 |

The zero is correct and expected — R8 confines PF anchors to GDPR-derived
obligations. The GDPR figure is the finding: **46 of 100 PF 1.0 controls are
cited by no security requirement in the corpus**, concentrated as:

| Category | Unreached | Of |
|---|---|---|
| PR.PO — Data Protection Policies, Processes, Procedures | 8 | 10 |
| PR.DS — Data Security | 6 | 8 |
| PR.PT — Protective Technology | 4 | 4 |
| GV.MT — Monitoring and Review | 4 | 7 |
| ID.BE — Business Environment | 3 | 3 |
| CT.DP — Disassociated Processing | 3 | 5 |

`PR.PT` is the sharpest: the entire protective-technology lane has no requirement
pointing at it, and `ID.BE` likewise. Whether that is a real hole in the corpus
or a real absence of privacy risk at this scale is a judgement for the
investigator — it is a finding, not a defect claim.

(The run's own maturity report shows 51/100 PF controls covered, which is *wider*
than the 54 in the mappings because goal anchors are collected from the phase
output as well as the mapping store.)

---

## 6. Measured finding: "PF 1.1" is the wrong version label, and it is inherited

266 files under `baseline/` label the referential **PF 1.1**. The correct
version is **NIST Privacy Framework 1.0** (January 2020). The workbook
corroborates this independently: the tab header reads *"NIST Privacy 1.0
Categories"* (`Privacy Summary!B2`) and the Introduction dates it *"NIST Privacy
Framework 1.0 (January, 2020)"* (`Introduction!A2`).

The label is not ours. It is inherited verbatim from the frozen dashboards the
baseline was extracted from (`00_VISUALISATIONS/GDPR/GDPR_Dashboard.html`), and
`baseline/` is read-only by rule. The correction therefore belongs in the
governance documents that describe the corpus, not in the corpus.

**Not applied.** Changing a label that 266 baseline files agree on is a
methodological decision with a blast radius across `AGENTS.md`, `SPEC.md`,
`README.md`, R2, R2b and R13, and it is the investigator's call, not a silent
correction made while reading a spreadsheet.

---

## 7. Measured finding: QNRCS control ids cannot be matched to CSF by id

The QNRCS extract carries its **own category codes**, not NIST's. Only 6 of its
107 controls resolve to a NIST CSF 2.0 subcategory after zero-padding; 101 do
not. 19 of its 22 category codes have no NIST counterpart at all.

All 22 QNRCS categories against the NIST category each mirrors:

| QNRCS (n controls) | NIST CSF 2.0 (n) | QNRCS (n controls) | NIST CSF 2.0 (n) |
|---|---|---|---|
| `GR.CA` (10) | `GV.SC` (10) | `GR.SP` (3) | `GV.OV` (3) |
| `GR.CO` (6) | `GV.OC` (5) | `DE.MC` (7) | `DE.CM` (5) |
| `GR.FR` (4) | `GV.RR` (4) | `DE.AE` (6) | `DE.AE` (6) |
| `GR.GR` (5) | `GV.RM` (7) | `ID.GA` (9) | `ID.AM` (7) |
| `GR.PP` (3) | `GV.PO` (2) | `ID.AR` (7) | `ID.RA` (10) |
| `PR.GA` (7) | `PR.AA` (6) | `ID.MC` (3) | `ID.IM` (4) |
| `PR.SD` (5) | `PR.DS` (4) | `PR.SP` (4) | `PR.PS` (6) |
| `PR.FC` (2) | `PR.AT` (2) | `PR.RI` (5) | `PR.IR` (4) |
| `RC.PR` (6) | `RC.RP` (6) | `RS.GI` (5) | `RS.MA` (5) |
| `RC.CO` (2) | `RC.CO` (2) | `RS.AI` (4) | `RS.AN` (4) |
| `RS.NC` (2) | `RS.CO` (2) | `RS.MI` (2) | `RS.MI` (2) |

The two halves of the table are a continuation of the same list, not
cross-referenced to each other. Exactly three of the 22 categories keep their
NIST code verbatim — `DE.AE`, `RC.CO`, `RS.MI` — and those three account for all
six of the apparent id matches.

Five of the six objectives keep their NIST initials; `GV` becomes `GR`. Eleven of
the 22 QNRCS categories have exactly the same size as the NIST category they
mirror, which is the structural signature of a re-cut: same framework, renamed
and regrouped, 107 controls against 106.

**All six apparent id matches are false friends.** They break down as four from
`DE.AE` (`-02`, `-03`, `-04`, `-06`; `DE.AE-05` matches nothing in CSF) and two
from `RS.MI` (`-01`, `-02`). `RC.CO` yields none at all despite the verbatim
code, because QNRCS numbers them 1–2 while CSF numbers them `RC.CO-03`/`RC.CO-04`.

This **independently confirms** the design of `scripts/build_qnrcs_referential.py`,
which maps QNRCS controls to CSF through the explicit `mapped_nist_csf` field
and not by string-matching ids.

It corroborates the investigator's own statement that *"o QNRCS é basicamente o
NIST CSF 2"*.

---

## 8. Decisions this leaves open

None of these are applied. They are ordered by how much they move the instrument.

1. **Rename the scale, drop the certification reading.** Adopt 1–5 with the
   named levels, or keep 0–4 but stop writing that 5 is certification. If the
   QNRCS tiers are mapped onto named levels, that mapping has no measured basis
   and must be registered in `METRICS.md` as `convention, unmeasured → E-xx`
   before it can be cited as anything.
2. **Split the radar into Policy and Practice.** My recommendation: report
   Policy with the coverage-derived figure and mark Practice *"not assessable
   before Phase 4"* rather than plotting a value. It converts an overclaim into
   a precise boundary statement, and it is the axis separation the workbook
   exists to demonstrate.
3. **Rename what we measure.** `nivel_atingido` is coverage, not maturity. The
   cheapest honest fix is to plot the coverage fraction and keep the level as an
   annotation — no new data needed, and the radar stops collapsing to the centre.
4. **Show denominators next to every score**, as `NIST CSF Summary!C` does.
5. **PF 1.0 vs "PF 1.1"** — correct the governance documents, or record the
   label as inherited and leave it (§6).
6. **The 46 unreached PF controls** — audit, or record as a scoped finding (§5).