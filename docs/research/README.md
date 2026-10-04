---
document_id: AEGIS-RES-IDX
title: 'AI pipeline & agent orchestration research — folder index'
version: 0.1.0
created: 2026-10-03
status: ACTIVE
---

# AI pipeline & agent orchestration research (`docs/research/`)

External survey of **AI pipeline patterns** and **agent orchestration patterns**,
and a mapping of both against the implementation in `pipeline/`. The purpose is
to let an approach be chosen on evidence rather than on intuition, and to keep
the reasoning attached to its sources over time.

## What this folder is — and is not

- **It is** the *external evidence* layer: an annotated catalogue of named
  patterns, a verdict on what this repo has already done and what it has not,
  and a ranked backlog of experiments.
- **It is not** the design layer. That is [`docs/pipeline/`](../pipeline/README.md)
  — what the pipeline is and why. This folder supplies the evidence the design
  layer is measured against, and where the two disagree, it says so.
- **It is not** the methodology layer. `SPEC.md`, `AGENTS.md`, `templates/`,
  `baseline/` and case deliverables stay frozen and technology-neutral (R5, R13).
  Nothing here may be cited as a methodology requirement.
- **It contains no runnable code and no results.** Every experiment in the
  backlog is unrun. This is a design, not a record.

## Index

| Doc | Purpose | Status |
|---|---|---|
| [01_PIPELINE_PATTERNS.md](01_PIPELINE_PATTERNS.md) | Catalogue `PP-001`..`PP-021`: architecture and decomposition, structured output, resource management, context and retrieval, evaluation, reliability, cost routing, anti-patterns | ACTIVE |
| [02_AGENT_ORCHESTRATION_PATTERNS.md](02_AGENT_ORCHESTRATION_PATTERNS.md) | Catalogue `AO-001`..`AO-013`: the workflow/agent boundary, topologies, context and memory, tools and protocols, multi-agent failure modes, false success, benchmarks, observability, security | ACTIVE |
| [03_PATTERN_MAPPING.md](03_PATTERN_MAPPING.md) | The verdict: architecture supported by the evidence; 22 patterns already implemented; **6 gaps**; 7 places the implementation is ahead of the literature; 4 contradictions stated | ACTIVE |
| [04_EXPERIMENT_BACKLOG.md](04_EXPERIMENT_BACKLOG.md) | **22 experiments** (`E-01`..`E-22`), each with one isolated variable, a primary metric, a GPU cost, a success criterion, and what changes if it wins and if it loses. `E-13`..`E-18` added 2026-10-04 from the KG survey; `E-19`..`E-22` are the robustness lane (mutation testing, pack measurement, matcher-pinned equivalence, metamorphic input tests), preregistration discipline stated per entry; most cost 0 GPU-h | ACTIVE — **nothing run** |
| [05_KNOWLEDGE_GRAPH_CONSTRUCTION.md](05_KNOWLEDGE_GRAPH_CONSTRUCTION.md) | Catalogue `KG-001`..`KG-010` + `KG-023`: standards as substrate (STIX 2.1/TAXII 2.1, ATT&CK's 81% edge-to-node ratio), attack graphs as Datalog, why taxonomy chaining produces artefacts, the four-stage CTI pipeline, entity resolution, and the reproducibility audit showing the *matcher* determines the number | ACTIVE |
| [06_GRAPH_QUERY_PATTERNS.md](06_GRAPH_QUERY_PATTERNS.md) | Catalogue `KG-011`..`KG-019` + `KG-033`, `KG-036`, `KG-037`: validity vs correctness, schema grounding (0.08 → 76.59 F1), emit-a-plan-not-a-query, tool surfaces, mode routing, curated vs LLM-built graphs | ACTIVE |
| [07_GRAPH_EVALUATION.md](07_GRAPH_EVALUATION.md) | Catalogue `KG-020`..`KG-026` + `KG-034`, `KG-035`: benchmarks wrong 57% of the time, answer-entity coverage as a gate, abstention collapse, judge noise floors, cheap deterministic proxies, and 13 negative results | ACTIVE |
| [08_GRAPH_IN_AI_PIPELINES.md](08_GRAPH_IN_AI_PIPELINES.md) | Catalogue `KG-027`..`KG-032`: five architectural slots, provenance and the derivation DAG, graph-as-memory with its budget-controlled negative results, the cost ledger and break-even, the graph as an attack surface, and 14 consolidated anti-patterns | ACTIVE |
| [09_KG_PATTERN_MAPPING.md](09_KG_PATTERN_MAPPING.md) | The KG verdict: **the three questions answered** (what to experiment with, how to build, how to evaluate), ADR-011 strengthened with a mechanism, **6 new gaps** (`G7`–`G12`), **5 contradictions** (`C-01`–`C-05`), and the one place the implementation is ahead of the literature | ACTIVE |
| [sources.yaml](sources.yaml) | The source registry: 204 entries, each with URL, publication and retrieval dates, evidence grade, and the verbatim quote that supports the claim | ACTIVE |

## Source anchoring — how this stays attached to its sources

Every factual claim in the four documents carries an `[S-nnn]` token that must
resolve to an entry in [`sources.yaml`](sources.yaml). The registry is the single
place a source is described, and it records *how well it was read*, not merely
that it was cited.

Three fields carry the anti-drift weight:

- **`retrieved`** — the date of the pass that actually opened the source. Sources
  carried over from the 2026-10-01 literature review keep that date. It is never
  bumped without a re-read.
- **`recheck_after`** — when the source must be re-read. Six months for living
  vendor documentation, twelve for preprints and blogs, `never` for a frozen
  specification or peer-reviewed paper. This is the alarm that fires when a
  claim has aged past its source.
- **`evidence`** — `PRIMARY`, `PEER`, `PRACTITIONER`, `CONTESTED`, `UNVERIFIED`.
  A source that could not be opened is recorded as `UNVERIFIED`, carries no
  quote, and is barred from being cited as evidence.

### Verifying

```bash
python scripts/check_research_refs.py            # report
python scripts/check_research_refs.py --strict   # exit 1 on any error
```

Seven checks: every citation resolves (**R1**); every registry entry is cited or
explicitly `unused` (**R2**); every cited repo path exists (**R3**); no source
is past its `recheck_after` date (**R4**); every entry is well-formed (**R5**);
every superseded entry names a live replacement (**R6**); and no `UNVERIFIED`
entry carries a quote (**R7**).

**R7 is the one that matters most.** It is what stops a source that could not be
opened from acquiring the authority of a citation simply by being written down.

## Conventions

- **Pattern IDs.** `PP-nnn` for pipeline patterns, `AO-nnn` for agent
  orchestration, `E-nn` for experiments, `G-n` for gaps and `C-n` for
  contradictions. Stable and never reused.
- **Evidence grades.** `PRIMARY` (vendor or standards documentation read
  directly), `PEER` (preprint; peer status not established), `PRACTITIONER`
  (named expert writing from experience), `CONTESTED` (credible sources
  disagree — both sides recorded, not smoothed).
- **Contested claims are recorded as contested.** Where the literature disagrees
  with itself, the catalogue names both readings rather than picking the
  convenient one.
- **Absence is recorded.** What the survey could not establish has its own
  section in each catalogue, and the two sources that could not be opened are in
  the registry as `UNVERIFIED` rather than silently dropped.
- **This folder is inside the `docs/` governance layer**, which
  `scripts/doc_lint.py` deliberately excludes from R11/R12 scanning. That is
  why these documents carry "honesty notes" and rationale narrative — the
  convention `docs/pipeline/04_LITERATURE_REVIEW.md` already follows.

## Relationship to the 2026-10-01 literature review

[`docs/pipeline/04_LITERATURE_REVIEW.md`](../pipeline/04_LITERATURE_REVIEW.md)
covers RAG versus knowledge graphs, security-requirements elicitation, and
threat-modelling LLM work. This folder **extends** it to pipeline architecture
and agent orchestration, and supersedes its coverage of those two topics. The
RAG/KG and security-RE sections of the older review remain current and are not
reproduced here; their sources are carried in the registry with
`retrieved: 2026-10-01` and `kind: prior-review`, so the two documents are
cross-referenced rather than divergent.

## Status

- **Survey:** 2026-10-03, two independent passes (pipeline architecture; agent
  orchestration), 123 registered sources.
- **Next:** E-04 and E-05, which are prerequisites for reading any future A/B
  result scored by an LLM judge.
- **Maintenance:** when a source is re-read, bump `retrieved` and push
  `recheck_after` in the same edit, and re-run the checker in `--strict` mode.
