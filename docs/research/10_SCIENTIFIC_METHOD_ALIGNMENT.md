---
document_id: AEGIS-RES-10
title: 'Scientific-method alignment — what the literature prescribes, where the repo stands, and the plan'
version: 0.1.0
created: 2026-10-04
status: ACTIVE — plan awaiting ratification
survey_date: 2026-10-04
sources: 'docs/research/sources.yaml'
upstream: 'AEGIS-RES-03, AEGIS-RES-04, AEGIS-EXP-05-RESULTS'
---

# Scientific-method alignment — survey, audit, and plan

**What this document is.** The researcher's directive: *everything done in this
repo should go through the scientific method, aligned with informatics and
cybersecurity.* This document (1) catalogues what the literature prescribes for
making engineering work scientifically valid (`SM-001`..`SM-011`), (2) audits
this repo's governance layer against that catalogue, and (3) proposes the
improvement plan. It is a *design*: nothing here changes behaviour until
ratified — the P3 policy amendment needs the researcher's approval like any
other.

**Method.** Web survey, 2026-10-04. Every factual claim carries an `[S-nnn]`
token resolving into [sources.yaml](sources.yaml); verify with `python
scripts/check_research_refs.py --strict`.

**The verdict up front.** *The repo already runs a scientifically valid core —
and its gap is asymmetric.* The experiment layer is stronger than what the
literature demands of most artefacts (preregistration with falsifiers,
measured defaults gating policy, mutation-tested checkers, negative results
recorded). The *normative layer* is the weak flank: rules and gate thresholds
in `AGENTS.md`/`SPEC.md` are enforced conventions whose parameters mostly have
**no measured basis**, and the decision layer (13 ADRs) records consequences
but **no falsifiable prediction, no signpost, no revisit date** — a gap the
literature itself names as unsolved in canonical ADR practice and closes only
by transplanting RAND's assumption-based planning. The plan targets exactly
these two flanks and deliberately does not touch what is already ahead of the
literature.

---

## 1. What the literature prescribes

### SM-001 — Falsifiability as the admission gate

A claim earns "scientific" only if it is "capable of conflicting with possible,
or conceivable observations" [S-276]. The engineering translation, and the one
this repo already uses in PREREG_01/02: every hypothesis names its falsifier
*before* the run, and the analysis runs once. The surviving operational test
(the TDD-as-Popper framing is practitioner folklore with academic footnotes, so
stated at PRACTITIONER grade): a check encodes a refutable prediction only if
failure is possible, observable, and diagnosable — otherwise it is ceremony.

### SM-002 — Preregistration, with its evidence honestly graded

Registered Reports review the plan and pre-accept before results exist;
Stage II explicitly welcomes "negative, non-conclusive, positive or unexpected
findings" [S-265]; COS defines preregistration as "specifying your research
plan in advance of your study and submitting it to a registry" [S-266]; the
RR lineage pre-dates results-conditional review [S-264]. **The strong claim is
CONTESTED, and the catalogue keeps it that way:** a 2024 matched comparison
found benefits for statistical power and impact but "we did not find robust
evidence that preregistration prevents p-hacking and HARKing" [S-267]. ML
operationalised the idea as a reproducibility checklist plus code submission
plus a community reproducibility challenge [S-268]. So the justified position
is: preregister to *structure* the prediction and enable deviation detection —
not because it is proven to eliminate bias.

### SM-003 — Artifact evaluation and reproduction badges

ACM's policy states "an experimental result is not fully established unless it
can be independently reproduced", with badges for artifacts that are
"documented, consistent, complete, exercisable" (Functional) and Reusable
"significantly exceeds minimal functionality" [S-269]. Security venues run the
same triad — Available / Functional / Results Reproduced — with independent
committees that *run* the artifact [S-270]; NDSS requires the committee to
"obtain the main results presented in the paper" with stated tolerance [S-271],
and formal artifact evaluation now spans USENIX Security (2020–), NDSS
(2024–) and IEEE S&P (from 2026) [S-272]. The transferable rule: results the
repo claims should be re-runnable by someone else from recorded state —
manifests, configs, prompts — without tribal knowledge.

### SM-004 — Chain of evidence and validity checklists

Runeson & Höst's case-study guidelines (the SE reference for case research:
"Case study is a suitable research methodology for software engineering
research since it studies contemporary phenomena in its natural context" [S-273])
require explicit construct/internal/external validity and reliability
checklists with a chain of evidence. This repo's standing limitation — one
case, one model, one rater — is exactly what those checklists exist to
declare; the requirement is not to fix it but to *carry the declaration on
every claim that is bounded by it*.

### SM-005 — Goal-Question-Metric: metrics derive from questions, not habit

GQM (Basili et al. [S-281]) derives each metric from a question that serves a stated
goal. The repo's inverse gap: `retention`, `grounding`, `calibration`,
`stability` are used across gates and results, but no single document chains
goal → question → metric → instrument → floor → *basis of the floor*. Where a
floor is a measured value (the R6 gate) versus a convention (the 0.88
similarity gate — E-10 still open, PLAYBOOK D1 unresolved) is recorded nowhere
as a system.

### SM-006 — Negative results are structurally protected

The RR format's in-principle acceptance is a "provisional guarantee that your
work will be published regardless of the final outcomes" [S-265], and
matched comparisons report positive-result rates dropping from 0.96 to 0.44
in registered formats (cited within [S-267]). The repo's analog already
exists de facto — EXP-05c's falsifier fired and is a headline finding, not a
footnote — but the protection is convention, not structure: nothing requires
that a fired falsifier or a failed experiment be written up in `00_RESULTS`.

### SM-007 — Decision records: consequences listed, but canon has no revisit

Nygard's canonical ADR format requires consequences with "all consequences…
not just the 'positive' ones" and makes supersession first-class [S-277]. The
gap, confirmed by the survey: **no canonical ADR format carries a revisit
date or an invalidation trigger** — those exist only in secondary practitioner
templates. Recording a predicted, observable consequence plus a signpost is
therefore *ahead of published practice*, and cheap.

### SM-008 — Assumption registers with signposts

RAND's Assumption-Based Planning: identify load-bearing assumptions, attach
*signposts* — pre-agreed warning events or thresholds that trigger
contingency planning [S-279]. NASA now argues assumption management "should be
treated as a formal safety and systems discipline" [S-280]. For this repo the
load-bearing assumptions are already known and written in prereg limitation
sections (one case, one model, one rater; judge determinism unproven); what
is missing is one register that makes each assumption's signpost explicit.

### SM-009 — Verifiable-practice drafting

NIST SSDF is the model of codifying practice so compliance is *checkable
against named evidence* rather than paperwork assertions: "a core set of
high-level secure software development practices… a common vocabulary for
secure software development" [S-278]. The repo's checker layer
(`doc_lint`, `check_traceability` T1–T6, `verify_no_loss`) is this pattern —
and EXP-05a is the part most security venues do not even require: the
checkers themselves were mutation-tested (36/36, 0 false positives). (One
correction for the record: NIST SP 1270 is the AI-bias standard, not a
software-metrics standard — do not cite it for measurement.)

### SM-010 — Evaluation pitfalls specific to learning-based security

Arp et al. (USENIX Security '22, Distinguished Paper) reviewed 30 top-tier
papers and codified the recurring traps — sampling and temporal bias, spurious
correlations, unrealistic robustness testing — with actionable recommendations
[S-274]. This repo's temporal-split concern is already served by the
CTIConnect protocol ([S-198]); the residual obligation is that any future
model-matrix or judge experiment runs the Arp checklist explicitly.

### SM-011 — Codified, evidence-graded bodies of knowledge

CyBOK codifies "the foundational knowledge of cyber security" as 21 knowledge
areas [S-275] — the institutional version of what `docs/research/` does for
this pipeline's design decisions: a curated, graded, drift-alarm registry. The
repo's sources registry (204 entries, verbatim quotes only when opened — R7 —
evidence grades, `recheck_after` drift alarms) already implements this
pattern; the survey adds no gap here, only confirmation.

---

## 2. Audit: where the repo stands

| Dimension (from §1) | Repo state | Verdict |
|---|---|---|
| Falsifiability of experiments (SM-001) | PREREG_01/02: hypotheses, directional predictions, falsifiers, analysis-once; EXP-05c falsifier fired and reported | **Ahead of practice** |
| Preregistration (SM-002) | Two-stage design (PREREG before run, results after) since 2026-10-03 | `ADOPTED (convergent)` — adopt the [S-267] caveat in any future claim about prereg's power |
| Artifact/reproduction story (SM-003) | Bit-reproducible runs (EXP-02) with manifests + configs + prompt catalogue; **no one-command external reproduction** | Partial — gap A3 |
| Validity declarations (SM-004) | Limitations stated per-prereg (one case/model/rater) but not carried on downstream claims | Partial — gap A4 |
| Metrics derive from goals (SM-005) | L2_RUBRIC formal; `retention`/`grounding`/`calibration` operationalised ad hoc across gates | **Gap — the weak flank** (A1) |
| Negative results (SM-006) | Recorded in results docs and catalogues; protection is convention | Partial (A5) |
| Decision records (SM-007) | 13 ADRs with Nygard-style consequences; **no predicted observable consequence, signpost, or revisit date** | **Gap** (A2) |
| Assumption register (SM-008) | Assumptions written per-prereg, scattered | Gap (A2, same fix) |
| Verifiable practice (SM-009) | Checker layer + mutation-tested gates (EXP-05a: 36/36) | **Ahead of practice** |
| Security-ML evaluation pitfalls (SM-010) | Temporal-split and contamination concerns raised where relevant | Partial — make the Arp checklist explicit in future model experiments |
| Evidence-graded knowledge (SM-011) | sources.yaml R1–R7, drift alarms | **Ahead of practice** |

**The honest reading.** Three layers here are already ahead of what the
literature requires (experiments, checkers, evidence registry). Two layers
trail: the **normative layer** (rule thresholds enforced by gates but
unmeasured — the 0.88 similarity gate, retention floors, L2 calibration) and
the **decision layer** (ADRs without falsifiable predictions or signposts).
Both gaps are closed by conventions and small scripts, not by new science.

---

## 3. The plan

Phased cheap-first. Nothing here requires new infrastructure beyond scripts
the repo's conventions already assume.

### P0 — Conventions, zero cost (this week, on ratification)

- **A1 — docs/experiments/METRICS.md (to create) (GQM one-pager).** One table:
  goal → question → metric → instrument → floor → **basis of the floor**
  (`measured: EXP-02` / `convention, unmeasured → E-10`). Every gate
  parameter in the pipeline gets a row; every future A/B cites a row. This
  single document converts the normative layer's unmeasured parameters from
  invisible to *declared* — the precondition for measuring them.
- **A2 — docs/decisions/ASSUMPTIONS.md (to create) + ADR field additions.** One
  assumption register: load-bearing assumption → signpost → contingency →
  owner. Seed with the four already written in prereg limitation sections
  (one case, one model, one rater, judge determinism) plus ADR-011's
  materialisation trigger. New ADRs add three fields: *Consequência prevista
  (falsificável)*, *Sinal de revisão*, *Revisar quando*. Retrofit the three
  load-bearing ADRs (pipeline-architecture, knowledge-representation,
  threat-knowledge-layer).
- **A4 — carry the validity declaration.** One sentence, templated: any
  result doc or panel entry that depends on the single-case/single-rater
  limit states it in the blockquote header. Already done in EXP-05; make it
  the convention.

### P1 — Mechanical guards, script-scale (cheap, after P0)

- **A5 — results-layer guard.** Extend the checking convention with one
  strict rule (candidate: extend `check_research_refs.py` or a small sibling):
  every `EXP0x_*_results.md` must cite its prereg document and its prereg
  version — the analog of the [S-269] requirement that results be consistent
  with a registered artifact. Fires on the next mismatched doc; ~50 lines.
- **A3 — reproduction harness.** One script, candidate name scripts/reproduce_run.py (to create) that
  takes a run's `manifest.json` + `config.json` and re-executes the same
  stages against the same case with the same seed, then diffs the artifacts.
  This is the repo's own Available/Functional badge, and EXP-02 made the
  underlying claim (bit-identical) already measured — the harness just makes
  the claim *executable by someone else*.

### P2 — Close the measurement gaps (existing backlog, in order)

The experiment sequence is unchanged from the established ranking, now with
its GQM justification: **E-17** (judge noise floor — gates A/B
interpretation), **E-14** (abstention/hallucination pair), **E-13** (graph +
T6 debt), then E-15/E-16/E-18, plus **E-10** (similarity-gate firing rate),
which A1 will have exposed as the flagship *convention, unmeasured* row. Any
new model-matrix work runs the Arp checklist [S-274] explicitly (temporal
split, sampling bias, baseline disclosure).

### P3 — Policy amendment (needs ratification)

Proposed `AGENTS.md` section **"-2. Conduta científica"**, five rules, each
already de facto:

1. Aclaim about the pipeline or corpus carries an anchor: `[S-nnn]`, an
   `EXP-xx`, or a checker verdict — prose without anchor is opinion and says
   so.
2. Every enforced threshold carries a basis tag (`measured: EXP-xx` /
   `convention, unmeasured → E-xx`) in `METRICS.md`; a threshold with no
   basis tag may not be cited as evidence of quality.
3. Every experiment runs under a frozen prereg; deviations are recorded in
   the results doc, never silently.
4. A fired falsifier or a negative result lands in `00_RESULTS.md` in the
   same session as the analysis — same rule as positive results.
5. Every decision (ADR) carries a falsifiable predicted consequence and a
   signpost; a decision whose signpost fires is revisited, not defended.

**What this plan deliberately does not do:** it does not add process for its
own sake (no new committees, no review gates on every edit), does not
retrofit evidence grades onto the frozen methodology layer (SPEC/baseline
stay frozen per R5 — the scientific layer is the pipeline/research layer),
and does not promise multi-case replication before Case_02/03 enter the
programme (A2's signposts cover the interim).

---

## 4. What the survey could not establish

- No definitive longitudinal measurement of badge-uptake effects was opened
  (the [S-272] hub is the actionable dataset, unread here).
- The strong preregistration claims (eliminates p-hacking/HARKing) remain
  CONTESTED — [S-267] is the citation that keeps them honest.
- "TDD as Popperian falsification" is practitioner folklore with academic
  footnotes; no canonical primary source was found, so SM-001's engineering
  translation is graded accordingly.
- NSA Science of Security primary pages were not opened (search quota
  exhausted); CyBOK [S-275] carries the codification claim alone.
