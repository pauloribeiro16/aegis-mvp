---
document_id: AEGIS-P1-RICH-README
title: Phase 1 Rich Mode — Case 01 (TinyTask SaaS)
phase: 1
version: 1.1
created: 2026-08-06
updated: 2026-09-14
author: Fase de Especificação 0 Skeleton / Fase de Especificação 1 reconciliation / Fase de Especificação 2 enrichment / Fase de Especificação 3 finalisation
status: ACTIVE
case: Case_01_TinyTask_SaaS
sibling_of: 01_PHASE1_CONTEXT/
corpus_source: 00_METHODOLOGY/PREPROCESSING_by_domain/domains/
reading_order_added: 2026-09-14
---

# Phase 1 Rich Mode — Case 01 (TinyTask SaaS)

> **Rich version of Phase 1 — enriched with corpus data from `00_METHODOLOGY/PREPROCESSING_by_domain/domains/`.**
> Fase de Especificação 3 status: **COMPLETE** (all sprints complete, 6/6 lints pass, Validator verdict = PASS).

## 0. Reading Order (canonical — post-2026-09-14 fold)

> **How to read this phase in 5 minutes.** After the F1-pilot C1 fold (2026-09-14), Phase 1 has
> **9 deliverables** in the canonical reading order below. The 4 folded documents and 1 baseline-cited
> register follow — they remain on disk as preserved historical instances (graph/parser/dashboard
> liveness) but are no longer part of the deliverable count.

### 0.1 Deliverables in this case folder (clean sequential naming)

| # | Doc | What it answers | Original ID |
|---|-----|-----------------|-------------|
| 1 | `Doc01_Taxonomy_Reference.md` | Which sub-domain taxonomy (D-01..D-10) does this methodology use? | Doc01 |
| 2 | `Doc02_INTAKE_FORM.md` | **Who is this company?** — profile, regulatory tree, systems, data | Doc02 |
| 3 | `Doc03_Regulatory_Applicability.md` | Which regulations apply and in what role? | Doc08 |
| 4 | `Doc03b_Ambiguity_Register_Case_Filter.md` | Filtered case-level ambiguity cards (CITES `00_COMMON/04_Ambiguity_Registry.md`) | Doc09 |
| 5 | `Doc04_Clause_Mapping_Matrix.md` | Which clauses map to which sub-domains? | Doc10 |
| 6 | `Doc05_Proportionality_Profile.md` | How heavy should compliance be for this company's tier? (Track B) | Doc12 |
| 7 | `Doc06_Adjusted_Objectives.md` | The adjusted objectives per sub-domain — primary handoff artefact to Phase 2 | Doc13 |

> **Note on Baseline Ambiguity Analysis:** The authoritative baseline ambiguity registry has been moved to `00_COMMON/04_Ambiguity_Registry.md` (Fase 0 baseline). Phase 1 (`Doc03b`) merely filters and cites those canonical interpretations for this specific company.

## 1. Purpose

This folder is the **Rich Mode** counterpart to the legacy `01_PHASE1_CONTEXT/`. It contains the same 10 Phase 1 documents (plus 2 new artifacts and 2 orchestration files) at **10× enrichment depth**, with each document explicitly linked to:

- The **canonical 10×38 sub-domain taxonomy** (D-XX.Y notation)
- The **4-layer corpus** under `00_METHODOLOGY/PREPROCESSING_by_domain/domains/`:
  - **L1**: Domain manifests `D-XX_<Domain>/D-XX.manifest.json` (10 files)
  - **L2**: Sub-domain manifests `D-XX.Y/D-XX.Y.manifest.json` (38 files)
  - **L3**: JSON sidecars `D-XX.Y/D-XX.Y.json` (38 files)
  - **L4**: Verbatim regulatory articles `D-XX.Y/articles/<REG>_Art_<N>.md` (623 files)

The Rich folder is a **sibling, NOT a replacement** of the legacy folder. Both folders coexist; the Rich folder is the authoritative reference for reviewers examining the corpus linkage. The legacy `01_PHASE1_CONTEXT/` remains the as-shipped artefact for backwards compatibility (Phase 2/3 readers point to legacy paths).

## 2. Sprint Status Dashboard

| Sprint | Status | Output |
|--------|--------|--------|
| 0 — Planning + Skeleton | COMPLETE | 17 files (14 placeholders + 3 scripts + README) + 7 validation reports |
| 1 — Reconciliation | COMPLETE | 11 docs copied + 6 inconsistencies fixed (I-01, I-02, I-05/06, I-07, I-10, I-13) + lint 31W→10W |
| 2 — Corpus Enrichment | COMPLETE | 4 docs enriched (135 cells) + 2 NEW docs filled (417 ambiguity cards + 18 citations) + 4 status flips to CORPUS_ENRICHED |
| 3 — Final Validation | COMPLETE | 3 new docs (RICH_VS_LEGACY, PROJECT_STATE, VALIDATOR_SPRINT3) + README v1.0 + 07b §11 cross-check (10/10 PASS) + SPRINT3_REPORT |
| 4 — Adjusted Objectives | COMPLETE | NEW Doc 07c (74 adjusted objectives = 37 PG + 37 SG) + Doc 07b §12-§14 (decision table + tensions + corpus provenance) + Doc 04 BG cross-refs (5 BGs linked) + 4 tensions resolved with max-SLA routing |

**Overall:** Rich folder is **READY** (6/6 Phase 1 lints pass, 0 errors, 44 warnings — all in legacy meta-docs not introduced by Fase de Especificação 2 enrichment). Validator verdict: **PASS** (see `validation/VALIDATOR_SPRINT3.md`).

## 3. Navigation

### 3.1 Phase 1 Documents (14 files)

| File | Size | Status | One-line description |
|------|-----:|--------|----------------------|
| `00_Taxonomy_Reference.md` | 11.4KB | RECONCILED v1.1 | 10×38 sub-domain taxonomy with corpus manifest paths |
| `01_INTAKE_FORM.md` | 28.4KB | RECONCILED v2.1 | Company context intake form (renamed from `01_Company_Context.md`) |
| `04_Company_Context_Assessment.md` | 9.4KB | RECONCILED v2.1 | Consolidated company facts (S=MICRO, FTE=0.85, applicable_regs=[GDPR, CRA]) |
| `04a_Architecture_DataInventory.md` | 26.7KB | CORPUS_ENRICHED v1.1 | 5 systems, 3 stores, 5 flows + Compliance Mapping (37 rows + Corpus Manifest Path + NIST CSF Anchors) |
| `04b_Security_Posture.md` | 25.2KB | CORPUS_ENRICHED v1.1 | 10 macro-domain posture + Target fit_criterion + Verification Method per representative sub-domain |
| `04c_ThirdParty_Landscape.md` | 30.1KB | CORPUS_ENRICHED v1.1 | Cloud vendors + GDPR Art. 28 verbatim + CRA Art. 7 + Art. 13(5)/(6) verbatim + 4 D-06.x mapping rows |
| `04d_Org_Roles_RACI.md` | 31.7KB | CORPUS_ENRICHED v1.1 | 30 RACI rows + 7 Compliance Mapping rows + Corpus Reg Req + Corpus Manifest Path (37 cells) |
| `05_Regulatory_Applicability.md` | 14.4KB | RECONCILED v1.1 | Native vs Inherited per regulation (GDPR + CRA only; NIS2 + DORA + AI Act out-of-scope) |
| `05b_Ambiguity_Register.md` | 38.0KB | CORPUS_ENRICHED v1.0 | 417 ambiguity cards (276 GDPR + 141 CRA) — top 20 sorted by severity with R1/R2/R3 readings |
| `06_Clause_Mapping_Matrix.md` | 14.9KB | RECONCILED v1.1 | 28 GDPR + 26 CRA clauses + Cross-Reference shim (case-form ↔ corpus-form) |
| `07_Structured_Compliance_Matrix.md` | 15.7KB | RECONCILED v1.1 | Consolidated matrix + complementarity analysis (5 regs × 38 sub-domains) |
| `07b_Proportionality_Profile.md` | 33.1KB | ACTIVE v1.1 | 37-row per-sub-domain tier table (Track B proportionality: 5 attributes) + Fase de Especificação 3 corpus cross-check |
| `Citation_Index.md` | 7.4KB | CORPUS_ENRICHED v1.0 | 18 unique (reg, ref) pairs + 3 coverage gaps + per-doc citation map |
| `phase1_ontology.yaml` | 38.2KB | RECONCILED v1.1 | Canonical ontology (38 sub-domains × 5 regs × attributes; D-08.3 INACTIVE) |

### 3.2 Orchestration Files

| File | Size | Purpose |
|------|-----:|---------|
| `README.md` | (this file) | Orientation + Sprint Status Dashboard + Navigation |
| `corpus_field_map.md` | 45.2KB | 515-line case ↔ corpus field mapping (per-doc × per-corpus-field) |
| `RICH_VS_LEGACY.md` | NEW | Side-by-side Rich vs Legacy diff summary for reviewers |
| `PROJECT_STATE.md` | NEW | Localized project state for the Rich version |

### 3.3 Generated Artefacts

| File | Size | Purpose |
|------|-----:|---------|
| `Case_01_Phase1_RICH.xlsx` | 41.2KB | 14-sheet Excel workbook (parallel to legacy `Case_01_Phase1.xlsx`) |

### 3.4 Scripts (3 stubs)

| File | Purpose |
|------|---------|
| `scripts/filter_ambiguity_cards.py` | Filter corpus ambiguity cards on `regulation ∈ {GDPR, CRA}` |
| `scripts/generate_corpus_links.py` | Extract L1/L2/L3/L4 paths per Phase 1 doc |
| `scripts/regenerate_ontology.py` | Regenerate `phase1_ontology.yaml` v1.1 from corpus + case data |

### 3.5 Validation Reports (7 files in `validation/`)

| File | Purpose |
|------|---------|
| `validation/LINT_REPORT_BEFORE.md` | Fase de Especificação 0 baseline lint (6/6 pass, 31W) |
| `validation/LINT_REPORT_AFTER_RECONCILE.md` | Fase de Especificação 1 post-reconcile lint (6/6 pass, 10W) |
| `validation/CORPUS_AUGMENTATION_REPORT.md` | Corpus augmentation (38/38 sub-domains + 48 manifests + 38 sidecars + 623 articles) |
| `validation/SPRINT1_REPORT.md` | Fase de Especificação 1 completion report |
| `validation/SPRINT2_ENRICHMENT_REPORT_EXISTING.md` | Fase de Especificação 2 enrichment of 4 existing docs (04a/04b/04c/04d) |
| `validation/SPRINT2_ENRICHMENT_REPORT_NEW.md` | Fase de Especificação 2 enrichment of 2 NEW docs (05b + Citation_Index) |
| `validation/VALIDATOR_SPRINT0.md` | Fase de Especificação 0 Validator verdict |
| `validation/VALIDATOR_SPRINT3.md` | Fase de Especificação 3 Validator verdict (NEW) |
| `validation/SPRINT3_REPORT.md` | Fase de Especificação 3 final report (NEW) |

## 4. Quick-Start for Reviewers

1. **Start here:** this README.md (orientation + dashboard + navigation)
2. **Diff vs legacy:** `RICH_VS_LEGACY.md` (side-by-side file inventory + corpus linkage)
3. **Project state:** `PROJECT_STATE.md` (Rich version status, deliverables, branch info)
4. **Field mapping:** `corpus_field_map.md` §2 (case ↔ corpus field mapping per doc)
5. **Top ambiguity cards:** `05b_Ambiguity_Register.md` §3 (top 20 severity-sorted with R1/R2/R3 readings)
6. **Verbatim quotes:** `04c_ThirdParty_Landscape.md` §4.1 + §5.1 + §5.2 (GDPR Art. 28 + CRA Art. 7 + CRA Art. 13(5)/(6))
7. **Citations:** `Citation_Index.md` (18 unique (reg, ref) pairs + 3 coverage gaps)
8. **Proportionality:** `07b_Proportionality_Profile.md` §4 (37-row tier table) + §11 (Fase de Especificação 3 corpus cross-check)
9. **Validation:** `validation/SPRINT3_REPORT.md` (final lint status + Validator verdict PASS)

## 5. Lint Status

| Phase | Sprint | Lint result |
|-------|--------|-------------|
| Fase de Especificação 0 baseline | 0 | 6/6 PASS, 31 warnings |
| Fase de Especificação 1 post-reconcile | 1 | 6/6 PASS, 10 warnings (−68%) |
| Fase de Especificação 2 post-enrichment | 2 | 6/6 PASS, 44 warnings (+34 from new content — all in legacy meta-docs not introduced by enrichment) |
| Fase de Especificação 3 final | 3 | 6/6 PASS, 44 warnings, 0 errors |

**Lint command:**

```bash
python3 01_IMPLEMENTATION_TOOLS/lints/run_phase1_lints.py --case "Case_01_TinyTask_SaaS" --quiet
```

Latest report: `01_IMPLEMENTATION_TOOLS/lints/reports/lint_report_phase1_20260806_120303.md`

## 6. Corpus Linkage Summary

| Layer | Source | Used in |
|-------|--------|---------|
| L1 — Domain Manifests | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-XX_<Domain>/D-XX.manifest.json` (10 files) | Taxonomy overview (not per-row) |
| L2 — Sub-domain Manifests | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-XX_Y/D-XX.Y.manifest.json` (38 files) | Doc 04a (Corpus Manifest Path, NIST CSF Anchors), Doc 04d (Corpus Manifest Path) |
| L3 — JSON Sidecars | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-XX_Y/D-XX.Y.json` (38 files) | Doc 04b (Target fit_criterion, Verification Method), Doc 05b (ambiguity cards) |
| L4 — Verbatim Articles | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-XX_Y/articles/<REG>_Art_<N>.md` (623 files) | Doc 04c (Art. 28, Art. 7, Art. 13(5)/(6) quotes), Citation_Index |

**Total corpus linkage cells added across Fase de Especificação 2:** 135 cells in 4 existing docs + 18 unique citations + 417 ambiguity cards + 4 corpus-field-map sections.

## 7. Migration Notes — GDPR-C → GDPR-CL Clause IDs

Legacy Phase 1 uses clause IDs like `GDPR-C-001`. The corpus uses **GDPR-CL-001** (the `-CL` suffix distinguishes corpus-level clause IDs from case-level ones). Fase de Especificação 1 added a **cross-reference shim** to Doc 06 §8 (not a find-replace) — both forms coexist. The canonical case-form is preserved for Phase 2/3 backward compatibility; the corpus-form is added as a parallel reference.

```
GDPR-C{NN} ↔ GDPR-CL/CP/RT{xx}  (semantic, not numerical)
```

## 8. Cross-references to Corpus (Example Paths)

| Layer | Pattern | Example |
|-------|---------|---------|
| L1 (domain manifest) | `…/PREPROCESSING_by_domain/domains/D-XX_<Domain>/D-XX.manifest.json` | `…/domains/D-01_Data-Protection/D-01.manifest.json` |
| L2 (sub-domain manifest) | `…/PREPROCESSING_by_domain/domains/D-XX.Y/D-XX.Y.manifest.json` | `…/domains/D-01.1/D-01.1.manifest.json` |
| L3 (JSON sidecar) | `…/PREPROCESSING_by_domain/domains/D-XX.Y/D-XX.Y.json` | `…/domains/D-01.1/D-01.1.json` |
| L4 (verbatim articles) | `…/PREPROCESSING_by_domain/domains/D-XX.Y/articles/<REG>_Art_<N>.md` | `…/domains/D-01.1/articles/GDPR_Art_5.md` |

## 9. Outstanding Items (post-Fase de Especificação 3)

1. (Optional) Update Doc 06 Clause Mapping to use GDPR-CL corpus form as canonical (semantic remap, not renumbering)
2. (Optional) Extend Doc 05b with full ambiguity card set (currently top 20 of 417)
3. (Optional) Add corpus field map per-doc sections for 7b (Track B proportionality)
4. Subagente Validator final review — DONE in Fase de Especificação 3 (`validation/VALIDATOR_SPRINT3.md`)
5. Git branch + merge prep — handled by orchestrator (branch: `feature/aegis-p1-case01-rich`)