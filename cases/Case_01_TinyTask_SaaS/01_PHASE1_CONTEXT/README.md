---
document_id: AEGIS-CASE01-P1-README
title: Phase 1 Contextual Definition — Case 01 (TinyTask SaaS)
phase: 1
version: 2.0
created: 2026-08-06
updated: 2026-09-22
status: ACTIVE
case: Case_01_TinyTask_SaaS
inputs: [Doc01_INTAKE_FORM.md]
outputs: [Doc02_Adjusted_Goals.md]
---

# Phase 1 Contextual Definition — Case 01 (TinyTask SaaS)

This directory contains the Phase 1 deliverables for **Case 01 — TinyTask SaaS**, implementing the minimal, self-contained **AEGIS Phase 1 (Contextual Definition)** pipeline per `SPEC.md` and `AGENTS.md`.

## 1. Pipeline Artifacts

The Phase 1 case implementation strictly follows the Phase 1 pipeline I/O contract (ADR-004):

| File | Nature | Description |
|---|---|---|
| [`Doc01_INTAKE_FORM.md`](Doc01_INTAKE_FORM.md) | **Input** | Target company profile, operations, data categories, and regulatory scope assessments. Technology-neutral fact sheet without technical bloat. |
| [`Doc02_Adjusted_Goals.md`](Doc02_Adjusted_Goals.md) | **Output** | Phase 1 primary deliverable: 35 ACTIVE sub-domains mapped to company-proportional **Adjusted Goals** (`AG-D-XX.Y-NNN`), 4 strategic tensions resolved with max-SLA routing, Track B tier allocations, and NIST CSF 2.0 / PF 1.1 control anchors. |

All generic taxonomy, legal texts, clause mappings, ambiguity registries, and control definitions are inherited directly by reference from the repository baseline.

## 2. Baseline References (Inherited)

Phase 1 inherits the following baseline knowledge without local duplication:

- **Taxonomy:** [`baseline/00_Taxonomy_Reference.md`](../../../baseline/00_Taxonomy_Reference.md) (38 canonical sub-domains `D-01.1` to `D-10.3`).
- **Ambiguity Registry:** [`baseline/01_Ambiguity_Registry.md`](../../../baseline/01_Ambiguity_Registry.md) (regulatory ambiguity cards).
- **Baseline Goals & Modules:** [`baseline/domains/`](../../../baseline/domains/) (regulation-neutral `objective.md` and modular `regs/<REG>.md` per sub-domain).
- **Control Referentials:** [`baseline/CONTROLS/`](../../../baseline/CONTROLS/) (NIST CSF 2.0, NIST PF 1.1, NIST AI RMF, and advisory referentials).
- **Traceability Chains:** [`baseline/MAPPINGS/`](../../../baseline/MAPPINGS/) (SR-to-control stores and end-to-end traceability chains).

## 3. Case Corpus Slice

For deterministic, case-isolated inspection of the active regulations (GDPR and CRA), consult the composed slice:
- [`filtered_corpus/`](../filtered_corpus/) (generated deterministically by `scripts/generate_case_corpus_slice.py`).