# aegis-mvp

Minimal viable pipeline for **AEGIS Phase 1 — Contextual Definition**: a reduced,
self-contained contract that bootstraps a **new** company/project with the least
information possible, then grows by absorbing artefacts from the full methodology
repo (`Methodology_compact`).

## The idea in one line

> One company input file → one Phase 1 output file (profile + applicable regulations
> + adjusted objectives per applicable sub-domain), with regulatory and control
> knowledge **inherited by reference** from the frozen AEGIS baseline corpus.

## The three natures of Phase 1 information

| Nature | What it covers | Where it lives |
|---|---|---|
| **Inherited (free)** | 38 sub-domains `D-XX.Y` (10 domains), verbatim regulation article copies, 7 NIST/OWASP control referentials, ambiguity baseline | `Methodology_compact/00_METHODOLOGY/PREPROCESSING_by_domain/` + `00_METHODOLOGY/AMBIGUITY_REGISTRY/` — referenced via `config.yaml`, never copied |
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
├── README.md            this file
├── config.yaml          corpus paths (reference, not copy)
├── SPEC.md              the contract: input schema, procedure, output schema, rules
├── templates/
│   ├── company_input.md     blank input template + filling instructions
│   └── phase1_output.md     blank output skeleton
├── input/<company>/     one directory per company run
├── output/<company>/    one output per company run
├── example/             golden example: fictional company, real anchors
└── scripts/             (empty in Inc.0 — procedure is LLM-assisted, no code)
```

## Relation to `Methodology_compact`

- **Read-only by reference.** This repo never writes into the methodology corpus and
  never duplicates it. Paths are configured in `config.yaml`.
- **ID-compatible.** Adjusted objectives reuse the AEGIS `AG-D-XX.Y-NNN` scheme and
  sub-domain codes (`D-01.1` … `D-10.3`) so later increments can absorb outputs into
  the canonical document chain (Doc08/Doc10/Doc11/Doc12/Doc13) without rework.
- **Corpus is frozen.** Interpretation work (cross-regulation analysis, hierarchical
  objectives, ambiguity resolutions) is already done in the baseline; this pipeline
  *applies* it to a company, it does not re-derive it.

## Status — Increment 0 (MVP)

The absorption roadmap (what gets added next, in which order) is in `SPEC.md` §9.
