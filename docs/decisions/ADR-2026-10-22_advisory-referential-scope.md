---
document_id: AEGIS-MVP-ADR-016
title: 'The active control referential is CSF + PF + AI RMF + QNRCS; the rest is archive'
status: 'ACCEPTED — decided by the researcher, 2026-10-22'
date: 2026-10-22
phase: 'Fase 0 (Baseline) — control referential layer'
author: 'Decision: PhD researcher; formalization + record: Executor session'
upstream: 'ADR-014 (advisory nomenclature); ADR-015 §5; AGENTS.md R2b, R13; scripts/specs/*.yaml'
---

# ADR-016 — The scope of the control referential

> Registered decision (2026-10-22), stated by the researcher, on reading the
> adversarial review of the pipeline: of the 1 073 control files the referential
> carried, **794 (74%) were unreachable** — the resolver knew three families,
> the mapping store carried three axes, and the delivered organizational
> document cited **zero** advisory anchors while the rules told it to. The
> active referential is now what the pipeline can actually reach.

---

## 1. The decision

**D1 — The active referential is NIST CSF 2.0, NIST PF 1.1, NIST AI RMF and
QNRCS.** The eleven remaining families move to `baseline/CONTROLS_ARCHIVE/<FW>/`:
NIST SP 800-53 Rev 5, NIST SSDF v1.1, NIST AI SSDF Profile, OWASP ASVS, OWASP
SAMM, ISO/IEC 27001:2022 Annex A, ISO/IEC 27701:2019 Annex A, ISO/IEC 42001:2023
Annex A, CIS Critical Security Controls v8, BSI IT-Grundschutz and ENISA
advisory guidance.

**D2 — The archive is a location, not a deletion.** Every archived family is
regenerable from its spec in `scripts/specs/`; the generator writes to
`baseline/CONTROLS_ARCHIVE/<FW>/` when the spec carries `archive: true`. The
move is deterministic and re-runnable, and the file count is unchanged: 387
active + 686 archived = 1 073.

**D3 — Citing an archived anchor is a fabrication.** The rules (R2b) no longer
list the archived families as citable. `doc_lint.py` still resolves a path
into the archive, so a reference to archived material is reported as
unresolved rather than as a broken path.

**D4 — The QNRCS anchors are derived, not authored.**
`scripts/derive_qnrcs_anchors.py` computes the objective → QNRCS measure
linkage as a set intersection over data already in the repository:

    objective → SR → NIST CSF 2.0 id → the QNRCS measure whose
    `mapped_nist_csf` contains it

The result is written to `MAPPINGS/advisory_anchor_mappings/QNRCS.json` and
rendered in the §6 control tables. **What the derivation produces is a
proposal.** That a QNRCS measure implementing CSF id X is the right anchor
for an objective whose SR maps to X is a normative judgement, and it is the
researcher's; the machine contributes the candidates.

**D5 — The maturity a run attains becomes a deliverable.**
`outputs/phase3/QNRCS_MATURITY.md` reports, per objective, the QNRCS maturity
level the run reaches, with the coverage per level and the ceiling imposed by
the entity's assessed tier. `phase3/maturity.py` — which computes the level
and had **no importer at all** — is now the producer of a deliverable instead
of a module nobody called.

**D6 — NIST AI RMF stays active, with the decision open.** The researcher has
not settled whether the AI RMF axis should remain. It is left exactly as it
was, and this ADR does not touch it.

## 2. What the decision measured

| What | How | Value |
|---|---|---|
| Files the referential carried | `find baseline/CONTROLS -name '*.json'` | 1 073 |
| Files the resolver could reach | `guards/controls.py` `REF_DIRS` | 279 (3 families) |
| Files that were decoration | the difference | **794 (74%)** |
| Advisory anchors in the delivered organizational document | `grep -c` over `Doc03_Organizational_Requirements.md` | **0** |
| QNRCS measures the CSF bridge reaches | `scripts/derive_qnrcs_anchors.py --report` | 47 of 108 |
| Objectives reachable through those measures | the same | 129 |
| Maturity levels of `run_p2enr_c1` | `phase3/maturity.py` | 5 objectives at level 1, 1 at level 0 (expected 2 at Básico) |

## 3. Why the archive rather than a deletion

The 794 files are not junk. ISO 27001 Annex A and NIST SP 800-53 Rev 5 are
the frameworks an external reviewer reached for, and ADR-014's renormalisation
of the ISO 42001 and BSI identifiers was real work. The problem was never
their quality; it was that the pipeline could not cite them, so their
maintenance looked like pipeline work and nobody could say what it bought.

Archiving keeps them verifiable and regenerable while making the contract
true: what `AGENTS.md` R2b lists is what the pipeline reaches. The 61 QNRCS
measures the CSF bridge does not reach are the same kind of fact — a measure
with no CSF path is a process measure, and the maturity instrument already
says so by leaving it out of the level computation.

## 4. The signal for re-opening

The decision is reviewed, not defended, when **any** of these fires:

- **(a)** The archived families are cited by a deliverable — the archive is
  then wrong, or the pipeline needs the axis.
- **(b)** The QNRCS linkage is found to be wrong in a case a reviewer checks:
  a measure implementing CSF id X is attached to an objective X has nothing to
  do with. The derivation is set-based, so it over-approximates by
  construction.
- **(c)** The maturity level is reported where the entity's tier was never
  assessed — the ceiling is then imposed on nothing, and the number is
  decorative.
- **(d)** The AI RMF axis is decided, either way. That decision is open and
  this ADR does not close it.

## 5. What this decision does not settle

- **The AI RMF axis** (D6) — open, unchanged.
- **The 61 QNRCS measures with no CSF path.** They stay out of the level
  computation; whether they need a path of their own is a separate question.
- **The `RULE-D-XX.X-NNN` id space** reserved for the good-practice layer at
  +100, which collides with the Phase 2 counter's per-sub-domain restart.
  Recorded in ADR-015 §3, not fixed here.

Related: [[phase3-gate-is-a-pure-function-of-disk]], [[gates-are-not-goals]],
[[qnrcs-national-framework]], [[advisory-referential-nomenclature]].
