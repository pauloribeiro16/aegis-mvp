---
ficha_id: PROM-P2-03
title: 'Synthesize Secure Design Principles'
phase_step: 'Phase 2 · P2d (after Doc01; one call per run)'
pattern: 'one structured call per run — the 7 principles are transversal, never per sub-domain'
version: 1.0.0
created: 2026-10-09
status: ACTIVE
normative_source:
  - 'docs/decisions/ADR-2026-10-09_phase2-objective-bridge.md D2 (the Constraint is the Phase 2 work)'
  - 'docs/pipeline/05_PHASE2_DETERMINISM_LEDGER.md §3.2, §3.3'
  - 'cases/*/02_PHASE2_RULES/Doc02_Secure_Design_Principles.md §2–§6 (table schema, category structure)'
  - 'AGENTS.md §5 R5, §5 R10b; templates/phase3_functional_spec_guidelines.md §2.5 (specificity matching)'
---

# PROM-P2-03 — Synthesize Secure Design Principles

## Metadata

| Field | Content |
|---|---|
| Role | Secure systems architect |
| Mission | Bind each of the 7 universal engineering principles to **this company's own architecture**, as a checkable architectural constraint that holds before any technology is chosen |
| Inputs | The 7 principle definitions (Context pack §1); `steps/fact_sheet.yaml`; the confirmed regulation set |
| Output | `steps/principles.json` — 7 rows × `{id, constraint, method_lead, eval_scope}` — rendered into `Doc02_Secure_Design_Principles.md` |
| Human gate | **G-P2-A** — reviewed against the rendered document, with the Invariance Test (§ Self-checks) applied row by row |
| Failure mode | A constraint that would read identically for a different architecture → the column has degenerated into the baseline definition restated, and Phase 2 has produced nothing (ledger §3.3) |

## Context pack (load exactly these)

| # | File | Use |
|---|---|---|
| 1 | `pack-p2d/principles.md` | the 7 universal principle definitions, academic sources and category structure — a baseline asset, **copied, never regenerated** (ledger §3.2) |
| 2 | `steps/fact_sheet.yaml` | the company: sector, size, jurisdictions, data categories, data subjects, hosting, third-party processing |

## Output schema

```json
{"principles": [
  {"id": "PRIN-ENG-01", "constraint": "<the architectural boundary this company must respect>",
   "method_lead": "<one of TEST | INSPECT | DEMONSTRATE | ANALYZE> (<role>)",
   "eval_scope": "<the artefact or surface this constraint is checked against>"}
]}
```

Exactly 7 objects, `PRIN-ENG-01` … `PRIN-ENG-07`, in order, no additions.

## Prompt body

> You are a secure systems architect working for one company. The seven
> principles below are universal and are given to you already written — do not
> restate them. Your job is the part that is **not** universal: for each
> principle, state the architectural constraint **this company's own systems**
> must respect, in terms of the zones, data stores, interfaces, principals and
> decision points that actually exist for it.
>
> Read the fact sheet. It is short and it is the only thing you know about the
> company. Do not invent a system it does not have: if the fact sheet does not
> tell you the shape of something, bound your constraint to what it does say.
>
> For each principle produce:
>
> 1. **`constraint`** — one or two sentences. It must name the concrete surfaces
>    this principle binds: the trust zones and their mediators, the data stores
>    and where data lives, the principals and what they may do, the decision
>    points that must fail closed. Write it so a reviewer could check it against
>    this company's systems.
> 2. **`method_lead`** — one of `TEST`, `INSPECT`, `DEMONSTRATE`, `ANALYZE`,
>    followed by the role accountable (use the fact sheet's vocabulary for
>    sizing; if the fact sheet names no roles, name the function, not a person).
> 3. **`eval_scope`** — the artefact or surface the constraint is checked
>    against: a diagram, an access-control matrix, an interface schema, a
>    deletion ledger, a build pipeline. Not "the system".
>
> Rules:
> 1. **Technology neutrality (R5/R13).** No database engine, framework, cloud
>    provider, protocol or product name. Name *roles* and *surfaces*
>    ("the internal application database", "the transactional email service"),
>    never implementations. `DTO`, `table`, `bucket` and `queue` are technology
>    terms in this phase — write "interface schema", "record", "store",
>    "message stream".
> 2. **Do not restate the principle.** The definition above is already the
>    principle. Your `constraint` is the company's instantiation of it.
> 3. **No fact about the company that is not in the fact sheet (R6).** Sizes,
>    counts, jurisdictions and data categories come from it or not at all.
> 4. **Seven rows, always.** If a principle does not activate for this company,
>    say so in the constraint (`not activated: <why, from the fact sheet>`) —
>    never drop the row.

## Self-checks (L2)

Apply before answering, and the reviewer applies them row by row:

- **The Invariance Test (R10b).** *Would this constraint read identically for a
  company of a completely different architecture?* If yes, it fails: it restates
  the principle instead of binding the company. This is the single failure mode
  this step exists to avoid (ledger §3.3, §4.6 — Case 03's Doc02 carried Case
  02's eGate architecture).
- **Specificity matching (§2.5).** Every level drop below the principle —
  naming a zone, a store, a principal, a decision point — needs a warrant from
  the fact sheet. If you cannot point at the warrant, stay at the principle's
  level and say the fact sheet does not settle it.
- Every `method_lead` method is one of the four published values; no fifth.
- Every `eval_scope` names an artefact a reviewer could be handed, not a
  property ("secure", "auditable").
- Technology blacklist (`quality.py` `L4_TERMS`) is clean in all three fields.

## Guard hooks (L0/L1)

- **L0** (`steps.py:parse_p2d`): one ` ```json ` block; `principles` is a list of
  exactly 7 objects; ids exactly `PRIN-ENG-01`…`-07`, in order, no duplicates;
  all three string fields present and non-empty. Anything else → repair round.
- **L1** (`phase2.py:check`): **G5** Doc02 completeness — 7 rows, every canonical
  id, no duplicate, no orphan. **G6** technology neutrality, via the existing
  `quality.check_no_technology`. **G7** grounding — the constraint must not
  contain a company proper noun absent from the fact sheet (ledger §4.6's
  contamination, mechanised).
- **Measured, not gated:** `grounding_ratio` — the share of constraints carrying
  company-specific content absent from the universal definitions — is written to
  the stage result and predicted in `PREREG_P2_01.md`. M11 established that
  *demanding* a named artefact does not make a column more company-specific, so
  this is a measurement with a falsifier, not a gate that would reject a 7-row
  document into uselessness.

## Failure handling

- Dry run (`--dry-run`): packs composed and written, no call; `principles.json`
  is not written and `Doc02` renders its constraints as `—` (a visible seam,
  not a fabricated one).
- Model call fails twice: the stage aborts with the Doc01 already written —
  Doc01 is deterministic and survives a Doc02 failure.
- An L0 failure is repaired by the existing multi-turn loop in
  `StepRunner._call`; the first-attempt error is recorded in `trace.jsonl`.