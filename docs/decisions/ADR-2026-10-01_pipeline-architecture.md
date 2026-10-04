---
document_id: AEGIS-MVP-ADR-010
title: 'AI pipeline architecture — prompt-chaining workflow with deterministic guards and human gates'
status: 'ACCEPTED — decided by the researcher, 2026-10-01'
date: 2026-10-01
phase: 'Cross-phase (0–3), pipeline layer'
author: 'Decision: PhD researcher; formalization + record: Executor session'
---

# ADR-010 — AI pipeline architecture

> Registered decision (2026-10-01), stated by the researcher when commissioning the pipeline design: *"quero que tu me digas como é que nós vamos organizar esta pipeline … quero uma organização completa do início ao fim. Mas primeiro vamos começar pela fase 1."* — with the execution format settled as prompt fichas in markdown executed by an agent (option selected explicitly from three offered, including a runnable orchestrator).

## 1. Context

- The methodology is fully specified on paper (SPEC §5 P1–P5, ADR-004 I/O contract, ADR-005 rounds, ADR-006 two-part Phase 3) and has been executed case-by-case by an LLM agent following prose instructions. No prompt catalog or orchestration tooling exists (`README.md` frames Phase 1 as "no code — LLM-assisted procedure").
- Literature consensus (docs/pipeline/04_LITERATURE_REVIEW.md): for predefined, auditable procedures, prompt-chaining workflows with programmatic gates outperform autonomous agents on predictability and traceability; Anthropic's guidance is explicitly "simplest solution first; workflows for predictable tasks".

## 2. Decisions

- **D1 — Workflow, not agent.** The pipeline is a fixed sequence of LLM steps (prompt chains) with deterministic gates between them and explicit human gates on decisions. No LLM-directed control flow, no cross-phase autonomous loops.
- **D2 — Prompts as versioned markdown fichas.** One step = one ficha (fixed anatomy, docs/pipeline/03_PROMPT_CATALOG.md) under `docs/pipeline/prompts/`. Fichas are executed by any LLM agent; no runtime dependency is introduced (Increment 0 ethos preserved).
- **D3 — Deterministic context packs.** Every step's retrieval is an explicit, deterministic file list (heir of `generate_case_corpus_slice.py`); the agent does not freelance retrieval.
- **D4 — Orchestration runtime deferred.** A script that invokes a model API is registered as an optional future increment (docs/pipeline/00 §9); it would reuse the same fichas unchanged.
- **D5 — State on disk.** All intermediates (fact sheets, verdicts, registers, run notes) are files; any step re-enters from its recorded predecessor.

## 3. Alternatives considered

- **Autonomous agent across phases** — rejected: unpredictable control flow is incompatible with evidence-grade traceability (R12b) and exit gates; harder to audit for a PhD evidence chain.
- **Runnable orchestrator now** — rejected for this increment: adds runtime/model/cost decisions before the fichas exist; the design doc + fichas deliver the same execution discipline.

## 4. Consequences

- **C1:** `docs/pipeline/` becomes the executable specification of *how* the methodology is run; SPEC/AGENTS remain the specification of *what*.
- **C2:** every executed run records the ficha versions it used (in `RUN_NOTES.md`), enabling the eval loop.
- **C3:** ficha bodies are the single place carrying execution instructions; case deliverables never absorb them (R11).

> Previsto (falsificável): a workflow arm completa corridas a uma fracção do
> custo do agente, com saída estruturalmente estável sob seed fixa.
> Sinal: um experimento registado (padrão EXP-03/EXP-04) mostrar o braço
> alternativo a superar o workflow em qualidade com custo comparável.
> Revisar: quando esse resultado existir (ver docs/decisions/ASSUMPTIONS.md).

## 5. Ratification checklist (P7)

1. D1 (workflow, not agent) — **decided by researcher** (2026-10-01).
2. D2/D3 (fichas + deterministic packs) — **decided by researcher** (2026-10-01).
3. D4 (defer orchestrator) — confirm: ______
