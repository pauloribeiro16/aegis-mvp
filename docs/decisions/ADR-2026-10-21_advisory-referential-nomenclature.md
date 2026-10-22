---
document_id: AEGIS-MVP-ADR-014
title: 'Advisory referential nomenclature — the identifiers must point at the section the standard publishes'
status: 'ACCEPTED — authorized by the researcher, 2026-10-21'
date: 2026-10-21
phase: 'Fase 0 (Baseline) — advisory referential layer'
author: 'Decision: PhD researcher; verification + formalization: Executor session'
upstream: 'AGENTS.md §3 (baseline read-only, amended by decision), §-2 rule 5 (signpost), R2b (advisory citation), scripts/specs/iso_42001_2023.yaml, scripts/specs/bsi_grundschutz.yaml'
---

# ADR-014 — Advisory referential nomenclature

> Registered decision (2026-10-21): an amendment to the frozen baseline's
> **advisory** referential layer, authorized by the researcher after an external
> review identified two classes of defect in the identifiers themselves. The
> amendment is made in the **generator specs** — the source of truth — and the
> JSON tree is regenerated deterministically. No generated file is hand-edited.

---

## 1. The decision

**D1 — ISO/IEC 42001:2023 identifiers are section-aligned.** The published Annex A
sections run **A.2 … A.10**. Every one of the referential's 33 controls is now
aligned to the published *section* whose theme its own text carries: A.2 Policies
related to AI, A.3 Internal organization, A.4 Resources, A.5 Assessing impacts,
A.6 AI system life cycle, A.7 Data for AI systems, A.8 Information for interested
parties. Three controls that were filed under a section they do not belong to
(AI-specific roles, resource allocation, top-management oversight, the
accountability chain, model documentation, configuration management, operational
procedures, secure-by-design, intended purpose) were re-filed by their content.

**D2 — The intra-section ordinal is a local subset ordinal and is not asserted
to be the published control ordinal.** `informative_references` therefore cite
the **section** (`"ISO/IEC 42001:2023 Annex A.2"`), never a published control
number this repository cannot verify against the published Annex A. The qualifier
is carried in every leaf's `source_version` and in the spec header, so it travels
with the artifact rather than living only in this record.

**D3 — BSI IT-Grundschutz: the family that contradicted a published module code
stops asserting one.** The `DER` family carried the code `DER` — the published
layer for *detection and response* — over three cards whose content is an
identity directory, a public-key infrastructure and a federation. Rather than
re-file that content against a mapping this repository cannot verify against the
published Kompendium, the family was renamed to a content-derived namespace
(`IDM`, `IDENTITY_AND_KEYS/`) and no published Baustein id is asserted for it.
Separately, the `CON` family's hyphenated ids (`CON-1`, `CON-2`, `CON-3`) were
corrected to the dot convention every other module uses and that the cards'
own reference strings already used (`CON.1`).

**D4 — The amendment lives in the specs.** `scripts/specs/iso_42001_2023.yaml`
and `scripts/specs/bsi_grundschutz.yaml` are edited;
`scripts/generate_advisory_framework.py` regenerates the tree. Regeneration from
the *unmodified* specs was verified byte-for-byte against the committed tree
before the amendment, so the specs are demonstrably the source of truth and the
generator is demonstrably deterministic.

## 2. Why

The external review's normative findings were checked against the tree and
**confirmed**, while its architectural findings were **refuted** (the review had
been made against a filtered, truncated export). The confirmed class is the one
this ADR addresses: **an identifier that resolves to a file but points at the
wrong place in the standard.**

**ISO/IEC 42001:2023 — a section shift of +3, in the data.** The spec hardcoded
six themes numbered A.5–A.10 while the published Annex A sections are A.2–A.7
for the same six themes. The shift was not only in the folder names: the
generated leaf `A5_POLICIES/A.5.1.json` carried `control_id: A.5.1` and
`informative_references: ["ISO/IEC 42001:2023 Annex A.5.1"]` over the text of the
published **A.2.1** control ("Define an AI policy aligned with the
organisation's purpose…"). Every one of the 33 identifiers was wrong in its
section. The published sections A.8 (Information for interested parties), A.9
(Use of AI) and A.10 (Third-party and customer relationships) were absent
entirely. **Why our own checks did not catch it:** R2b requires that a cited
advisory id *exist as a JSON file* in the referential's subtree, and it does.
The check is about resolvability, not about correctness — and `verify_no_loss.py`
does not cover the advisory tier at all. A referential can therefore be
mechanically clean and normatively wrong, which is the same shape as the Phase 3
finding in §6.3 of the external briefing: the checker verified the artefact's
form and never its substance.

**BSI IT-Grundschutz — a module code that contradicted its content.** `CON` and
`DER` are BSI layer codes; the cards filed under `DER` describe identity
management, not detection and response. The `CON` family's three files also
broke the referential's own naming convention (`CON-1.json` against `APP.1.json`
everywhere else) while citing "BSI IT-Grundschutz CON.1" in their own
reference strings — an internal contradiction inside a single file.

**Why D1/D2 and not a wholesale re-authoring.** The published Annex A and the
published Kompendium are not available in this repository, and the ADR must not
invent normative content it cannot verify (R6, R2). The amendment therefore
removes every claim the repository cannot support, and reduces the remaining
claim to the granularity it can support: the section. The residual is explicit
(D2) rather than silent.

## 3. What changed on disk

| | Before | After |
|---|---|---|
| ISO 42001 families | 6 (`A5_POLICIES` … `A10_DATA`), sections off by +3 | 7 (`A2_POLICIES`, `A3_INTERNAL_ORG`, `A4_RESOURCES`, `A5_IMPACT`, `A6_LIFECYCLE`, `A7_DATA`, `A8_TRANSPARENCY`) |
| ISO 42001 ids | `A.5.1` … `A.10.4` | `A.2.1` … `A.8.1` (33 controls, same count) |
| ISO 42001 references | `"ISO/IEC 42001:2023 Annex A.5.1"` (a published control number, wrong) | `"ISO/IEC 42001:2023 Annex A.2"` (the section) |
| BSI `CON` ids | `CON-1`, `CON-2`, `CON-3` | `CON.1`, `CON.2`, `CON.3` |
| BSI `DER` family | `DER.1`–`DER.3`, asserting a published module code over identity content | `IDM.1`–`IDM.3`, no published Baustein id asserted |
| BSI `source_version` | `2023 Compendium Edition` | `2023 Compendium Edition (one-line advisory summaries of the published Bausteine; published text not reproduced)` |

**Nothing outside the two referentials cited the retired identifiers.** A
repository-wide grep for the ISO 42001 ids and folder paths and for
`CON-1`/`DER.1`/`CON_CONTAINERS`/`DER_DIRECTORY` returned no consumer outside
`baseline/CONTROLS/` and the two specs: `AGENTS.md`, `SPEC.md` and `config.yaml`
name the *referential directory* (unchanged), and the case deliverables and
templates cite BSI at **layer** granularity ("BSI IT-Grundschutz OPS layer"),
which this amendment does not touch.

## 4. Consequence, falsifiable

**C1 — Section alignment holds.** Every leaf under
`baseline/CONTROLS/ISO_42001_2023/` has an id whose section prefix is in A.2–A.8
and whose `informative_references` contains the matching
`"ISO/IEC 42001:2023 Annex A.<section>"` string; no leaf cites a published
42001 control ordinal. *Falsifier: a leaf whose cited section differs from its
id's section, or any leaf citing an `Annex A.x.y` ordinal.*

**C2 — No dangling reference.** Every 42001 and BSI identifier that any
artifact in the repository cites resolves to a file in the referential, and no
artifact cites a retired identifier. *Falsifier: any grep hit on the retired
ids, or any cited id without a file.*

**C3 — The amendment is reproducible.** Regenerating both referentials from the
committed specs reproduces the committed tree byte-for-byte. *Falsifier: any
diff after `python3 scripts/generate_advisory_framework.py --spec …`.*

**C4 — The amendment is confined to the advisory tier, and the no-loss check's
scope is untouched.** `scripts/verify_no_loss.py` compares `baseline/domains`
against the external frozen corpus; this amendment touches only
`baseline/CONTROLS/`, and `git status baseline/domains` is empty after it. The
advisory tier's control counts are unchanged (33 for ISO/IEC 42001, 35 for BSI).
*Falsifier: any modification under `baseline/domains/`, or a changed control
count.* **Evidence status, stated plainly:** the no-loss script **was not
executed** — it requires `--original ../methodology-main/…`, a corpus that does
not exist on this workstation. The claim here rests on the scope argument and on
the counts, not on a run. Re-run it wherever the original corpus is mounted.

## 5. Signpost — when this decision reopens

Per AGENTS.md §-2 rule 5, any one of these reopens D1–D3; the decision is
revisited, not defended:

- **The published ISO/IEC 42001:2023 Annex A becomes available** (a licensed
  copy, or the published control list returned by the external normative audit).
  Then D2 is retired: the intra-section ordinals are aligned to the published
  control ids and the references return to control granularity.
- **The published BSI Compendium becomes available.** Then the `IDM` family is
  re-filed under the Baustein that actually covers identity, key and federation
  management — if one exists — and the reference string regains a Baustein id.
- **The published Compendium shows the `CON` layer is not the containerisation
  layer.** Then the `CON` family is renamed as well, exactly as `DER` was.
  Registered as assumption **A10** in `docs/decisions/ASSUMPTIONS.md`.
- **Any deliverable cites a 42001 or BSI identifier that does not resolve, or
  an examiner reconciles one of these cards against the published standard and
  finds a mismatch.** The referential is then not usable as a citation target
  and the ADR reopens.

## 6. What this decision does not settle

- **ISO/IEC 27701:2019 keeps synthetic identifiers.** `A.5.34.n.m` and
  `A.6.34.n.m` exist in no published standard, and the `A.5.34` root collides
  with ISO/IEC 27001:2022's own A.5.34. Fixing it requires the published
  standard; it is recorded, not fixed.
- **CIS Controls v8 keeps 18 aggregated cards and none of its 153 safeguards.**
  Instantiating them is a scope decision, not a correction.
- **The advisory tier's relationship to `verify_no_loss.py` is unchanged.** The
  enforced tier is still the only tier whose preservation is mechanically
  checked; the residual risk that a future amendment repeats this class of
  defect is addressed by the signpost, not by a new check.
- **The referentials are still locally authored prose, not reproduced
  normative text.** That was true before and is true now; what changed is that
  the identifiers no longer assert a fidelity the text does not have.

## 7. Linked evidence

| Claim | Source |
|---|---|
| The ISO 42001 ids were shifted +3, in the data | `scripts/specs/iso_42001_2023.yaml:4` (pre-amendment header: "Six themes (A.5–A.10)"); the pre-amendment leaf `A5_POLICIES/A.5.1.json` carried `control_id: A.5.1` and `informative_references: ["ISO/IEC 42001:2023 Annex A.5.1"]` over the published A.2.1 text |
| The BSI `DER` cards contradicted their module code | `scripts/specs/bsi_grundschutz.yaml` (pre-amendment): `function: "DER"`, `function_dir: "DER_DIRECTORY"`, `category_name: "Directory Service (DER)"` over identity-directory, PKI and federation text |
| The `CON` ids contradicted the referential's own convention | pre-amendment `CON-1.json` … `CON-3.json` against `APP.1.json` … `OPS.4.json`; the same file citing "BSI IT-Grundschutz CON.1" |
| The specs are the source of truth and the generator is deterministic | regeneration from the unmodified specs produced zero diff against the committed tree, for both referentials |
| Section alignment holds after the amendment | programmatic check over all 33 leaves: the section prefix of every `control_id` matches the `Annex A.<section>` string in its `informative_references`, and no leaf cites a published control ordinal — 0 violations |
| The no-loss check's scope is untouched | `git status baseline/domains` empty after the amendment; the check itself was not run (see C4) |
| R2b checks resolvability, not correctness | `AGENTS.md` §5 rule R2b; `scripts/verify_no_loss.py` (`enforced_by_verify_no_loss: false` on every advisory manifest) |
| No external consumer of the retired identifiers | repository-wide grep over `*.md`, `*.json`, `*.py`, `*.yaml` on 2026-10-21, before and after the amendment |
