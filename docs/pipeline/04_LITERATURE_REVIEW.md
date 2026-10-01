---
document_id: AEGIS-PIPE-04
title: 'Literature Review — LLM pipeline patterns grounding the AEGIS pipeline'
version: 0.1.0
created: 2026-10-01
status: ACTIVE
search_date: 2026-10-01
---

# Literature Review — grounding for the AEGIS pipeline

Research method: web survey (2026-10-01) across four topics — (1) canonical LLM workflow patterns, (2) RAG vs knowledge-graph augmentation for regulatory corpora, (3) LLM for security requirements engineering and threat modeling, (4) guardrails and evals for multi-step generation pipelines. Preference for 2023–2026 sources; primary sources opened and read are marked [V] in the notes below.

## 1. Consensus stage model of a production LLM pipeline

| Stage | Supporting sources |
|---|---|
| 1. Ingest & preprocess | GraphRAG indexing (LLM-derived entity graph over a corpus) — [arXiv 2404.16130](https://arxiv.org/abs/2404.16130); PromptChainer: realistic applications need data transformation between chain steps — [arXiv 2203.06566](https://arxiv.org/abs/2203.06566) |
| 2. Represent / index | GraphRAG entity graph → communities → summaries ([Microsoft Research](https://www.microsoft.com/en-us/research/publication/from-local-to-global-a-graph-rag-approach-to-query-focused-summarization)); KG-RAG over a curated KG — [Soman et al., Bioinformatics 2024](https://academic.oup.com/bioinformatics/article/40/9/btae560/7759620) |
| 3. Retrieve / assemble context | Routing pattern — [Anthropic](https://www.anthropic.com/engineering/building-effective-agents) [V]; retrieval must be benchmarked separately from generation — [LegalBench-RAG, arXiv 2408.10343](https://arxiv.org/abs/2408.10343) |
| 4. Generate | Prompt chaining / parallelization — [Anthropic](https://www.anthropic.com/engineering/building-effective-agents) [V]; schema-constrained decoding — [OpenAI Structured Outputs](https://openai.com/index/introducing-structured-outputs-in-the-api/) [V] |
| 5. Validate / guardrail | Programmatic gates between steps; guardrails with human escalation — [OpenAI agent guide](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents); evaluator–optimizer — [Anthropic [V]](https://www.anthropic.com/engineering/building-effective-agents) |
| 6. Human-in-the-loop | Expert checkpoints on high-stakes artifacts — [Anthropic [V]](https://www.anthropic.com/engineering/building-effective-agents); empirical: LLM-elicited security requirements weak on testability (44.4%) — [Takaronis et al., arXiv 2609.00886](https://arxiv.org/abs/2609.00886) [V] |
| 7. Iterate / state | Eval-driven development from error analysis of traces — [Hamel Husain, "Your AI Product Needs Evals"](https://hamel.dev/blog/posts/evals/index.html); benchmark-then-optimize loop — [ThreatModeling-LLM, arXiv 2411.17058](https://arxiv.org/abs/2411.17058) [V] |

## 2. Topic 1 — Canonical workflow patterns

[Anthropic — Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) [V] defines workflows vs agents and five named patterns: **augmented LLM** (building block), **prompt chaining** (fixed sequence with programmatic gates), **routing** (classify → specialized path), **parallelization** (sectioning / voting), **orchestrator-workers** (dynamic decomposition), **evaluator–optimizer** (generator–critic loop). Advice: find the simplest solution first; workflows for predictable tasks; agents only where model-driven decisions are needed.

[OpenAI — A Practical Guide to Building Agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents): agent = model + tools + instructions; orchestration as manager vs decentralized handoffs; guardrails and human escalation from day one.

Academic antecedents: [PromptChainer (CHI 2022)](https://arxiv.org/abs/2203.06566); surveys of agentic workflows ([arXiv 2508.01186](https://arxiv.org/abs/2508.01186), [arXiv 2406.05804](https://www.alphaxiv.org/overview/2406.05804v1)).

**AEGIS reading:** the methodology is a predefined, auditable procedure → **prompt-chaining workflow, not an autonomous agent** (ADR-010). Routing maps naturally to regulation-specific branches (R8); parallelization to per-sub-domain and per-objective steps; evaluator–optimizer to the ADR-005 acceptance rounds.

## 3. Topic 2 — RAG vs knowledge graphs for regulatory corpora

- [GraphRAG — From Local to Global (arXiv 2404.16130)](https://arxiv.org/abs/2404.16130): vector RAG fails at corpus-level "sensemaking" questions; LLM-built entity graph + hierarchical community summaries wins on comprehensiveness/diversity — exactly the "what does the regulation require of a company like ours" question class.
- [RAG vs GraphRAG: A Systematic Evaluation (arXiv 2502.11371)](https://arxiv.org/abs/2502.11371) [V]: neither paradigm dominates — RAG better at factual/detail QA, GraphRAG at relationship-dependent reasoning; **hybrids win consistently**.
- [KG-RAG (Soman et al., Bioinformatics 2024)](https://academic.oup.com/bioinformatics/article/40/9/btae560/7759620): grounding prompts in a *curated* KG consistently improves answers in a high-stakes domain — evidence that curation quality, not graph-ness alone, drives the gain.
- [LegalBench-RAG (arXiv 2408.10343)](https://arxiv.org/abs/2408.10343): in legal RAG, snippet-level retrieval precision is the bottleneck — argues for precise, structured sources over bigger chunk stores.
- Vendor claims for compliance GraphRAG ([GraphWise](https://graphwise.ai/blog/the-advantages-of-graphrag-for-enhanced-regulatory-compliance-and-understanding), [Neo4j](https://neo4j.com/blog/developer/from-legal-documents-to-knowledge-graphs)) are not peer-reviewed evidence.

**AEGIS reading:** our baseline is a *curated* graph-shaped corpus (typed edges, unique control IDs) — the strongest precondition for KG value. But the pipeline's questions are mostly served by deterministic packs; KG value concentrates in relational queries (anchor provenance/T6, impact analysis). → **Design the schema now, materialize on demand** (ADR-011); revisit when a hybrid retrieval experiment is warranted.

## 4. Topic 3 — LLM for security requirements & threat modeling

- [ThreatModeling-LLM (arXiv 2411.17058)](https://arxiv.org/abs/2411.17058) [V]: banking threat modeling pipeline — benchmark dataset from an existing threat-modeling tool → prompt optimization (CoT/OPRO) → LoRA fine-tuning; threats + mitigations aligned to NIST 800-53.
- [LLMs' suitability for STRIDE categorization (arXiv 2505.04101)](https://arxiv.org/html/2505.04101v2): quantifies LLM threat-categorization quality (accuracy/precision/recall/F1).
- [Using LLMs to elicit security requirements (Takaronis et al., arXiv 2609.00886)](https://arxiv.org/abs/2609.00886) [V]: 5 LLMs, 84 requirements, 5 expert raters — necessity 98.5%, clarity 87.4%, completeness 85.2%, feasibility 78.5%, **testability 44.4%** → early elicitation support, mandatory human review; testability is the weak flank.
- [Automated NFR generation (arXiv 2503.15248)](https://arxiv.org/html/2503.15248v1): promising only with human oversight and iterative feedback.
- MITRE chain pipelines (CVE→CWE→CAPEC→ATT&CK): [NEXUS (NDSS 2026)](https://www.ndss-symposium.org/wp-content/uploads/2026-f2926-paper.pdf); [CIRCL gold set + classifier + LLM for CVE→ATT&CK (arXiv 2607.25572)](https://arxiv.org/html/2607.25572v1); [Vuln2Action](https://www.sciencedirect.com/science/article/abs/pii/S2214212626000505). The chain works as an **auditable mapping step** against standard KBs.

**AEGIS reading:** (a) human review of LLM-elicited requirements is non-negotiable and testability deserves its own gate — already embodied in ADR-005 rounds and fit-criteria discipline; (b) the threat-KB enrichment belongs as a **mapping pass with ledger columns**, not free-text generation — adopted as PROM-P3B-05 and ADR-012.

## 5. Topic 4 — Guardrails & evals

- [A Survey on LLM-as-a-Judge (arXiv 2411.15594)](https://arxiv.org/abs/2411.15594) [V]: reliability is the central open question; position, verbosity, self-enhancement and preference biases are documented (companion study: [arXiv 2406.07791](https://arxiv.org/html/2406.07791v9)); mitigate with order swapping, rubrics, and validation against human agreement.
- [OpenAI Structured Outputs](https://openai.com/index/introducing-structured-outputs-in-the-api/) [V]: constrained decoding gives ~100% schema conformance — and OpenAI's own caveat: **conformance ≠ correctness**.
- Format-vs-reasoning debate: [Let Me Speak Freely? (arXiv 2408.02442)](https://arxiv.org/abs/2408.02442) vs [dottxt rebuttal](https://blog.dottxt.ai/say-what-you-mean.html) — practical resolution: keep a reasoning field in the schema; prefer constrained decoding over prompt-only JSON.
- [Hamel Husain — Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/index.html): build domain test sets from error analysis of real traces; validate any judge against human agreement before trusting it.
- Guardrail frameworks survey: [Guardrails AI vs NeMo Guardrails](https://genai.qa/blog/guardrails-ai-vs-nemo-guardrails).

**AEGIS reading:** our L1 deterministic guards (`doc_lint.py`, `check_traceability.py`, §8) are the strong layer; LLM-as-judge is demoted to advisory L3 and only where calibrated; the eval loop starts from the golden example's `RUN_NOTES.md` convention.

## 6. Takeaways adopted by the design

1. Workflow (prompt chaining + gates), not an autonomous agent → ADR-010.
2. Deterministic context packs as retrieval; KG designed now, materialized when relational queries hurt → ADR-011.
3. Threat-KB enrichment as a match-only mapping pass with ledger columns; CWE/CAPEC core, ATT&CK consultive, ATLAS/EMB3D routed by profile, CVE/KEV excluded → ADR-012.
4. Layered validation: schema → deterministic guards → self-checks → (calibrated) judge → human gates; testability gets explicit attention in Phase 3 fichas.
5. Eval loop as a first-class stage: trace every run in `RUN_NOTES.md`; golden example as test set; failures feed ficha versions.

## 7. Honesty notes (evidence gaps)

- No peer-reviewed 2023–2026 head-to-head of KG-augmented vs vector RAG on GDPR/CRA/NIS2/DORA-style compliance QA was found; evidence is indirect (general QFS, biomedical, legal QA) plus vendor claims. KG-vs-pack here is a reasoned design bet, not settled science.
- HITL "best practices" rest on practitioner guidance plus one rigorous security-RE study; there is no canonical HITL-for-RE-pipeline paper.
- Some secondary sources (NEXUS PDF, arXiv 2505.04101, 2503.15248, 2508.01186) were read via search-result summaries rather than opened in full.

## 8. Source list

Core: Anthropic *Building Effective Agents* · OpenAI *A Practical Guide to Building Agents* · OpenAI *Structured Outputs* · GraphRAG (arXiv 2404.16130) · RAG vs GraphRAG systematic evaluation (arXiv 2502.11371) · KG-RAG (Bioinformatics 2024) · LegalBench-RAG (arXiv 2408.10343) · ThreatModeling-LLM (arXiv 2411.17058) · Takaronis et al. security-RE elicitation (arXiv 2609.00886) · LLM-as-a-Judge survey (arXiv 2411.15594).

Secondary: Hamel Husain evals · PromptChainer (arXiv 2203.06566) · NEXUS (NDSS 2026) · CIRCL CVE→ATT&CK (arXiv 2607.25572) · Vuln2Action · STRIDE benchmark (arXiv 2505.04101) · NFR generation (arXiv 2503.15248) · position-bias study (arXiv 2406.07791) · Let Me Speak Freely? (arXiv 2408.02442) + dottxt rebuttal · Guardrails AI vs NeMo Guardrails · agent-workflow surveys (arXiv 2508.01186, 2406.05804) · GraphWise / Neo4j compliance blogs.

(Full URLs inline in the sections above.)
