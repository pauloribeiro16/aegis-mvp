---
document_id: AEGIS-PIPE-IDX
title: 'AI Pipeline Design — folder index'
version: 0.1.0
created: 2026-10-01
status: ACTIVE
---

# AEGIS AI Pipeline Design (`docs/pipeline/`)

Design layer for the **LLM-assisted pipeline that executes the AEGIS methodology** on a company: which steps run, in which order, with which prompts, consuming which knowledge, guarded by which deterministic checks, and where humans decide.

## What this folder is — and is not

- **It is** the pipeline *design* layer: end-to-end organization, knowledge architecture, prompt catalog, and executable prompt fichas (cards) per phase. Executed by any LLM agent following the runbooks — no code to deploy (Increment 0 ethos; ADR-010).
- **It is not** part of the methodology layer. `SPEC.md`, `AGENTS.md`, `templates/`, `baseline/` and case deliverables remain frozen and technology-neutral (R5, R13). This folder may reference tooling; methodology deliverables still may not.
- **It ends at Phase 3.** No Phase 4 exists (researcher ruling, 2026-09-30).

## Index

| Doc | Purpose | Status |
|---|---|---|
| [00_PIPELINE_MASTER_DESIGN.md](00_PIPELINE_MASTER_DESIGN.md) | End-to-end pipeline organization (Phases 0–3): reference model from the literature, workflow patterns, per-phase steps/guards/gates, validation layers, roadmap | ACTIVE |
| [01_PHASE1_PIPELINE.md](01_PHASE1_PIPELINE.md) | Phase 1 deep dive: step sequence P1–P5, context packs, guards vs the SPEC §8 checklist, human gates, runbook, context-pack builder spec | ACTIVE |
| [02_KNOWLEDGE_ARCHITECTURE.md](02_KNOWLEDGE_ARCHITECTURE.md) | Knowledge layers K1–K4, machine-readable inventory, knowledge-graph schema design, threat-knowledge policy, knowledge requirements matrix | ACTIVE |
| [03_PROMPT_CATALOG.md](03_PROMPT_CATALOG.md) | Prompt ficha anatomy + full catalog (Phase 1 detailed; Phases 2–3 skeleton) | ACTIVE |
| [04_LITERATURE_REVIEW.md](04_LITERATURE_REVIEW.md) | Literature grounding: canonical LLM pipeline stage model, RAG vs KG evidence, security-RE/threat-modeling LLM work, guardrails & evals (annotated sources) | ACTIVE |
| [prompts/](prompts/) | Executable prompt fichas. Phase 1: `PROM-P1-01` … `PROM-P1-05` | Phase 1 detailed |

**External evidence layer:** [`../research/`](../research/README.md) carries the
2026-10-03 survey of pipeline and agent-orchestration patterns, the mapping of
both against this implementation (22 patterns adopted, 6 gaps, 4 contradictions),
and a ranked experiment backlog. It is the yardstick this folder's design
decisions are measured against.

## Governing decisions (ADRs in `docs/decisions/`)

| ADR | Decision |
|---|---|
| [ADR-010](../decisions/ADR-2026-10-01_pipeline-architecture.md) | Pipeline = prompt-chaining **workflow** with deterministic gates + human gates; not an autonomous agent. Prompts live as versioned markdown fichas executed by an agent. |
| [ADR-011](../decisions/ADR-2026-10-01_knowledge-representation.md) | Corpus + JSON mappings remain the source of truth; knowledge-graph schema designed now, materialization later as a regenerable derived view; retrieval via deterministic context packs; no vector DB / vendor lock. |
| [ADR-012](../decisions/ADR-2026-10-01_threat-knowledge-layer.md) | Threat knowledge for Phase 3 Part 2: CWE + CAPEC (core), MITRE ATT&CK (consultive), ATLAS + EMB3D (per case). CVE/KEV/EPSS excluded (instance level, below design altitude). |

## Conventions

- **Prompt IDs:** `PROM-<PHASE>-<NN>` (`P1`, `P2`, `P3A` = Phase 3 Part 1, `P3B` = Phase 3 Part 2). Ficha anatomy in [03_PROMPT_CATALOG.md](03_PROMPT_CATALOG.md).
- **Context packs** are deterministic file lists over the corpus — the direct heir of `filtered_corpus/` composition (`scripts/generate_case_corpus_slice.py`). The agent never freelances its retrieval.
- **Validation in layers:** L0 output schema → L1 deterministic guards (`doc_lint.py`, `check_traceability.py`, SPEC §8) → L2 prompt self-checks → L3 LLM-as-judge (only calibrated) → L4 human gates.
- **Flag-not-drop:** anything that fails a check is recorded and flagged, never silently dropped (SPEC P2 convention, generalized).
- **No editorial meta-commentary, no placeholders** in these docs (R11, R12) — rationale lives in the ADRs and the literature review.

## Status & next steps

- **Done (2026-10-01):** master design, Phase 1 pipeline + fichas, knowledge architecture, prompt catalog, literature review, ADR-010/011/012.
- **Next passes:** Phase 2 fichas → Phase 3 Part 1 fichas → Phase 3 Part 2 fichas (after K3 ingestion).
- **Registered increments (not started):** KG materialization script (ADR-011); K3 ingestion into `baseline/THREATS/` (ADR-012); optional orchestration runtime (ADR-010 explicitly defers).
