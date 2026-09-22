# aegis-mvp

Minimal viable pipeline for **AEGIS Phase 1 — Contextual Definition**: a reduced,
self-contained contract that bootstraps a **new** company/project with the least
information possible, then grows by absorbing artefacts from the full methodology
repo (`Methodology_compact`).

## The idea in one line

> One company input file → one Phase 1 output file (profile + applicable regulations
> + adjusted goals per applicable sub-domain), with regulatory and control
> knowledge **inherited by reference** from the frozen AEGIS baseline corpus.

## The three natures of Phase 1 information

| Nature | What it covers | Where it lives |
|---|---|---|
| **Inherited (free)** | 38 sub-domains `D-XX.Y` (10 domains) in **modular per-regulation layout**, verbatim regulation article copies, 7 NIST/OWASP control referentials, ambiguity baseline | `baseline/` (working modular corpus, derived from `Methodology_compact`; see `baseline/domains/_migration_report.md`) |
| **Company input** | 1 prose file, 5 short sections (profile, product, data, systems, regulations) | `input/<company>/company_input.md` |
| **Generated** | 1 all-in-one output document | `output/<company>/phase1_output.md` |

## How to run (no code — LLM-assisted procedure)

1. Copy `templates/company_input.md` → `input/<company>/company_input.md` and fill
   the 5 sections in plain prose.
2. Ask any LLM agent: *"Execute `SPEC.md` on `input/<company>/company_input.md`,
   writing the result to `output/<company>/phase1_output.md`."*
3. Validate the run with the checklist in `SPEC.md` §8.

A complete worked example (fictional company, real corpus anchors) lives in `example/`.

## Layout

```
aegis-mvp/
├── AGENTS.md            operational contract & guidelines for agents
├── README.md            this file
├── SPEC.md              the contract: input schema, procedure, output schema, rules
├── config.yaml          corpus paths (reference, not copy)
├── baseline/            Phase 0 Baseline (frozen taxonomy, ambiguity registry, generic objectives)
│   ├── 00_Taxonomy_Reference.md
│   ├── 01_Ambiguity_Registry.md
│   ├── 02_Regulatory_Mapping_and_Generic_Objectives.md
│   ├── CONTROLS/        NIST CSF 2.0 / PF 1.1 / AI RMF referentials (anchor resolvability)
│   ├── MAPPINGS/        sr_control_mappings/<REG>.json — complete SR↔CSF/PF/AI-RMF store
│   │                    extracted from the frozen dashboards; traceability/ — full chain
│   │                    regulation → article → clause → objective → requirement → control
│   └── domains/         canonical 38 sub-domains, MODULAR per-regulation layout:
│                         D-XX.Y/{_index.md, objective.md, regs/<REG>.md,
│                         regs/<REG>.ambiguity.md, cross/<R1>-<R2>.md,
│                         cross/_interactions.md, articles/}
├── templates/
│   ├── company_input.md     blank input template + filling instructions
│   └── phase1_output.md     blank output skeleton
├── input/<company>/     one directory per company run
├── output/<company>/    one output per company run
├── cases/               benchmark reference cases from Methodology_compact
│   └── Case_01_TinyTask_SaaS/
│       ├── 01_PHASE1_CONTEXT/  Phase 1 contextual deliverables (Doc01 to Doc06)
│       └── filtered_corpus/    deterministic composed case slice (active-reg modules verbatim, zero summaries)
├── example/             golden example: fictional company, real anchors
└── scripts/             automation utilities
    ├── modularize_domains.py          merged Parts 1-4 → modular per-regulation layout (deterministic)
    └── generate_case_corpus_slice.py  deterministic slice composer for company cases
```

## Relation to `Methodology_compact`

- **Provenance, read-only.** This repo never writes into the methodology corpus.
  `baseline/` is the working modular copy, derived deterministically from
  `Methodology_compact` (`reorg_by_domain_md.py` → `annotate_baseline_domains.py`
  → `modularize_domains.py`; audit: `baseline/domains/_migration_report.md`).
  Each `regs/<REG>.md` is independent of every other regulation — applying any
  single regulation never requires loading the others; cross-regulation analysis
  lives in `cross/`.
- **ID-compatible.** Adjusted goals reuse the AEGIS `AG-D-XX.Y-NNN` scheme and
  sub-domain codes (`D-01.1` … `D-10.3`) so later increments can absorb outputs into
  the canonical document chain (Doc08/Doc10/Doc11/Doc12/Doc13) without rework.
- **Interpretation is frozen.** Cross-regulation analysis, hierarchical objectives
  and ambiguity resolutions are already done in the baseline; this pipeline
  *applies* them to a company, it does not re-derive them.
- **Control mappings are uniformized.** The NIST CSF 2.0 / PF 1.1 / AI RMF mappings
  cited on the modules, the ambiguity cards and the registry are extracted from the
  frozen per-regulation dashboards (`Methodology_compact/00_METHODOLOGY/
  00_VISUALISATIONS`, read-only) and verified contradiction-free by
  `scripts/verify_no_loss.py` (checks G/H). Ledger:
  `baseline/MAPPINGS/_control_uniformization.md`. Every security requirement
  carries its full chain — regulation, articles, ambiguity clauses, objectives
  (HSO → SO-REG → Sub-SO), and all mapped controls — in
  `baseline/MAPPINGS/traceability/` (regenerate with `scripts/build_traceability.py`).

## Status — Increment 0 (MVP)

The absorption roadmap (what gets added next, in which order) is in `SPEC.md` §9.
