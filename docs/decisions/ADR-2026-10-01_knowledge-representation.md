---
document_id: AEGIS-MVP-ADR-011
title: 'Knowledge representation — corpus + JSON as source of truth; knowledge graph as designed schema, materialized on demand'
status: 'ACCEPTED — decided by the researcher, 2026-10-01'
date: 2026-10-01
phase: 'Cross-phase (0–3), pipeline layer'
author: 'Decision: PhD researcher; formalization + record: Executor session'
---

# ADR-011 — Knowledge representation for the pipeline

> Registered decision (2026-10-01): asked how to treat the knowledge graph of regulations and best practices, the researcher selected *"Schema agora, build depois"* — design the graph schema in this pass, keep the corpus + JSON as source of truth, materialize later as a deterministic, regenerable view.

## 1. Context

- The Fase 0 baseline is already graph-shaped: requirement → Sub-SO → SO-REG → HL chains with typed edges (`derives_from`, `inherits_from`, `source_sr`), clause-level ambiguity nodes, and control nodes validated against referentials. A machine-readable layer exists today: `sr_control_mappings/<REG>.json`, `traceability/traceability.csv`, `registry.csv`, `CONTROLS/**/*.json`, plus `aegis:` structural tags in module markdown.
- SPEC §9 already anticipated graph infrastructure (`build_p1_graph.py`) for a later increment.
- Literature (docs/pipeline/04 §3): graphs win on relational/multi-hop questions; plain retrieval wins on factual lookup; no published head-to-head exists for EU-regulation compliance QA — a KG is a reasoned bet, not settled science.

## 2. Decisions

- **D1 — Source of truth unchanged.** The modular corpus + JSON mappings remain authoritative. Nothing in the baseline is reorganized for the graph.
- **D2 — Schema designed now, materialization deferred.** The node/edge schema and the surface→graph build map are recorded in docs/pipeline/02_KNOWLEDGE_ARCHITECTURE.md §3. Materialization is a future deterministic script emitting `node_link.json` + GraphML.
- **D3 — Regenerable derived view.** The graph is never hand-edited; consistency is checked by node/edge counts against source records (anti-circular spirit of `verify_no_loss.py`).
- **D4 — Retrieval stays deterministic.** Pipeline steps consume context packs (ADR-010 D3); the graph adds query power where packs are weak — T6 anchor-provenance analysis (58 out-of-set anchors debt), impact analysis, coverage debugging.
- **D5 — No vector DB, no vendor lock.** Plain files; loading into any graph tool is optional and out of scope.

## 3. Alternatives considered

- **Build the KG now** — rejected for this pass: the retrieval needs of Phases 1–2 are served by deterministic packs; building now would delay the prompt catalogs (the researcher's stated priority).
- **Vector RAG only** — rejected: loses the relational queries the traceability debt needs, and the corpus is already graph-shaped at zero extra curation cost.
- **GraphRAG-style community summarization now** — rejected: depends on materialization (D2) and adds LLM-derived summaries into a corpus whose integrity depends on verbatim-only content.

## 4. Consequences

- **C1:** docs/pipeline/02 §3 is the authoritative schema; the future builder script implements it, not the reverse.
- **C2:** when materialized, T6 provenance analysis gets a direct tool (which objective/test cited each out-of-set anchor).
- **C3:** if a hybrid retrieval experiment is ever run, it benchmarks against the pack baseline (LegalBench-RAG-style snippet metrics) before any ficha changes.

## 5. Ratification checklist (P7)

1. D1/D2 (source of truth; schema now, build later) — **decided by researcher** (2026-10-01).
2. D4 (packs first, graph for relational queries) — confirm: ______
