---
document_id: AEGIS-PIPE-01
title: 'Phase 1 Pipeline — Contextual Definition (P1–P5)'
version: 0.1.0
created: 2026-10-01
status: ACTIVE
upstream:
  - SPEC.md
  - templates/company_input.md
  - templates/doc02_adjusted_goals.md
  - example/
fichas:
  - prompts/PROM-P1-01_EXTRACT_FACTS.md
  - prompts/PROM-P1-02_CONFIRM_REGULATIONS.md
  - prompts/PROM-P1-03_SELECT_SUBDOMAINS.md
  - prompts/PROM-P1-06_BUILD_FRAMING.md
  - prompts/PROM-P1-04_DERIVE_ADJUSTED_GOALS.md
  - prompts/PROM-P1-05_RENDER_VALIDATE.md
---

# Phase 1 Pipeline — Contextual Definition

## 1. Scope & contracts

- **Input contract (SPEC §4):** `input/<company>/company_input.md`, 5 plain-prose sections; §5 must list ≥1 regulation with a one-line justification; regulation identifiers `GDPR | CRA | NIS2 | DORA | AI_Act`.
- **Output contract (SPEC §6):** `output/<company>/doc02_adjusted_goals.md`, Doc02 case format — §0 purpose, §1 regulatory floor, §2 framing table, §3 adjusted goals (+ derived anchors), §4 tensions resolved, §5 Track B decision trail, §6 NIST controls mapping.
- **Normative procedure:** SPEC §5 (P1–P5); rules R1–R8 (SPEC §7); checklist §8. This document organizes the same procedure into executable steps; the fichas are the executable artifacts.

## 2. Step sequence

| Step | Ficha | Pattern | Consumes | Produces | Gate after |
|---|---|---|---|---|---|
| P1 | [PROM-P1-01](prompts/PROM-P1-01_EXTRACT_FACTS.md) | single structured call | company_input §1–§4 (+ §5 read) | internal fact sheet | G-P1-A |
| P2 | [PROM-P1-02](prompts/PROM-P1-02_CONFIRM_REGULATIONS.md) | routing per regulation | fact sheet + §5 assumptions | §2 verdict table (applies / does not apply / flagged) | G-P1-B |
| P3 | [PROM-P1-03](prompts/PROM-P1-03_SELECT_SUBDOMAINS.md) | deterministic pre-filter + LLM trigger judgment | verdicts + domains index | §3 subset table + exclusion list | G-P1-C |
| P3f | [PROM-P1-06](prompts/PROM-P1-06_BUILD_FRAMING.md) | single structured call | fact sheet + verdicts | `steps/framing.md` (§2 framing table) | (reviewed at G-P1-D) |
| P4 | [PROM-P1-04](prompts/PROM-P1-04_DERIVE_ADJUSTED_GOALS.md) | parallelization per D-XX.Y | subset + framing + context packs | goal fragments (8 columns; anchors derived by code) + assumptions | G-P1-D |
| P4t | [PROM-P1-07](prompts/PROM-P1-07_RESOLVE_TENSIONS.md) | one call per selected sub-domain, merged (multi-regulation only) | corpus tensions + fact sheet | `steps/tensions.json` (§4 resolutions) | G-P1-D |
| P5 | [PROM-P1-05](prompts/PROM-P1-05_RENDER_VALIDATE.md) | deterministic assembly (zero LLM) + layered validation | all step outputs + code derivations | `doc02_adjusted_goals.md` (DRAFT→ACTIVE) + `RUN_NOTES.md`, exported to `output/<company>/` | sign-off |

## 3. Step cards (summary — full execution detail lives in the fichas)

### P1 — Extract facts
Fact sheet with fixed fields (sector, size, jurisdictions, legal form, product summary, `develops_software`, data categories, subjects, sensitive data, scale, hosting, access model, third parties, assumed regulations) + `open_questions`. Every field traces to input text (R6); gaps become `open_questions`, never guesses. Input §5 is read but **not judged** here (that is P2).

### P2 — Confirm applicable regulations
Evaluate each of the 5 candidate regulations against the fact sheet using the scope criteria embedded in the ficha (GDPR establishment/processing; CRA products with digital elements placed on the market; NIS2 sector+size essential/important entity; DORA financial entity; AI Act placing on the market / deploying high-risk AI). Verdicts: `**applies**`, `does not apply`, `flagged` (assumed in §5 but failing the scope test — flagged, never silently dropped). All 5 rows are rendered; every §5 assumption appears.

### P3 — Select the sub-domain subset
**Deterministic pre-filter:** candidate set = sub-domains whose `regs/` directory contains ≥1 confirmed regulation (from `baseline/domains/index.md` module maps). **LLM judgment:** for each candidate, does an obligation of a confirmed regulation match the sub-domain subject matter AND trigger on company facts? One-line trigger rationale per selection (fact → duty form). Excluded candidates are recorded with a why-not line. Canonical IDs only (R1).

### P4 — Derive adjusted goals
One invocation per selected sub-domain (parallelizable), after the p3f framing exists. Context pack per D-XX.Y (exact paths in the ficha): `objective.md`, `regs/<REG>.md` for each confirmed regulation present in the module, `cross/<R1>-<R2>.md` + `cross/_interactions.md` (operative sections) only when ≥2 confirmed regulations apply, `templates/doc02_adjusted_goals.md` §3, `steps/framing.md`, and the fact sheet. Output: an 8-column goal fragment per sub-domain (`ID | Adjusted goal | Pattern | Property | Parent goal | Baseline source | Regulatory source | Adjustment`; one row per Sub-SO of each confirmed regulation in canonical order; `Baseline source` = corpus Sub-SO id; closed decision vocabulary in Adjustment) + §5 assumption entries. The model emits NO control anchors and no §4.1 table: Regulation and Control Anchors are derived by `controls.py` (`Baseline source → source_SR → mapping store → CONTROLS`, R2b by construction). Ambiguity cards do **not** enter Phase 1 (researcher ruling 2026-10-01).

### P4t — Resolve strategic tensions
One call per selected sub-domain, multi-regulation runs only (single-regulation runs write an empty `tensions.json` deterministically). Pack per call: the Emergent-tensions sections of that sub-domain's `cross/_interactions.md` + the fact sheet. The per-call answers are merged in canonical sub-domain order and `T-NNN` is renumbered at merge. Output: a `T-NNN | Sub-domains | Tension | Conflict | Resolution` table — the §4 Tensions Resolved block of the deliverable (max-SLA routing convention). A double-L0 failure costs one sub-domain, not the run: the failure is recorded per sub-domain and the stage reports `carried=n/selected` (see ADR-012 D1 and D5).

### P5 — Deterministic assembly + validate (zero LLM)
The Doc02 deliverable is assembled by `assemble_doc`: §0/§1 static template text; §2 the p3f framing table; §3 per selected sub-domain the HL paragraph verbatim from `objective.md` + the goal JSONs with Regulation and Control Anchors derived by code; §4 the p4t resolutions; §5 the deterministic Track B matrix (`controls.track_b_rows`, per-case overrides); §6 the NIST control tables (`controls.sd_control_sections`: union of the mapping-store SRs bound to the sub-domain + the Sub-SO `source_SR`s, resolved against `CONTROLS/`). After assembly, `validate.py` runs **in-process** (every table diffed against its artifact/derivation, §0–§6 order, §8 items 2–6, 9, R12 hygiene, trace/manifest consistency) — any finding aborts the stage before G-P1-D. On success the deliverable is exported to `output/<company>/`. `RUN_NOTES.md` is built deterministically (run meta, §8 evidence plan, gate ledger). Status becomes `ACTIVE` only after the human signs off (G-P1-D).

## 4. SPEC §8 checklist → guard mapping

| §8 item | Check | Guard layer |
|---|---|---|
| 1. Input: 5 sections present; §5 ≥1 regulation + justification | stop condition at P1 | L2 (ficha 01) + human |
| 2. Confirmed regulation set covers every input §5 regulation, none silently missing | verdicts.json row-coverage check | L2 (ficha 02) + L1 scriptable |
| 3. §3 codes exist in the corpus | `grep -r "D-XX.Y" baseline/domains` / index | L1 deterministic |
| 4. AG IDs unique; sub-domain part matches the P3 selection | ID table diff | L1 deterministic (simple parse) |
| 5. Regulatory sources resolve in `articles/` (R2a) | `ls <subdomain>/articles/ \| grep <REG>` spot-check | L1 deterministic |
| 6. Control anchors resolve in the referential (R2b) | derived by `controls.py` from the mapping store + CONTROLS; diff-checked in the doc | L1 deterministic (by construction) |
| 7. No company statement without input trace or ASSUMPTION mark | trace-back pass | L2 (fichas 01/02/04) + L4 human |
| 8. Frontmatter complete; `status: ACTIVE` only after pass | render rule | L2 (ficha 05) + L4 gate G-P1-D |
| 9. Every goal: valid pattern, property, parent `SO-D-XX.Y.HL`, Baseline source, non-empty Adjustment | enum + field check | L1 deterministic (parseable) |
| 10. `doc_lint.py --strict` zero findings | run the script | L1 deterministic |
| — | Assembled doc == artifacts + code derivations (§2/§3/§4/§5/§6 cell diff); §0–§6 order; HL paragraphs verbatim | L1 (`validate.py`, runs automatically post-assembly) |

## 5. Human gates

| Gate | When | Reviewer decides | Record |
|---|---|---|---|
| **G-P1-A** | after P1 | fact sheet is faithful and complete; resolve `open_questions` | fact sheet approval note in `RUN_NOTES.md` |
| **G-P1-B** | after P2 | each of the 5 verdicts (confirm / correct); flagged assumptions accepted or input corrected | §2 review note |
| **G-P1-C** | after P3 | subset composition; exclusions accepted | §3 review note |
| **G-P1-D** | after P5 | sign-off → `status: ACTIVE` | `RUN_NOTES.md` final entry |

Gate reviews are business-language, per-item (the ADR-005 round convention, applied in miniature); IDs live in the artifacts, not in the questions.

## 6. Context-pack builder (spec)

In the pipeline runtime the packs are assembled in memory by `pipeline/src/compose.py` (pure function of case binding + verdicts + selection; verbatim file content only, ADR-010 D3). Conceptually, per step the exact file list the ficha declares:

  - P2 — fact sheet + input §5 + template §2 (no corpus files needed);
  - P3 — deterministic pre-filter block (candidates with participant rows + subject matter) + fact sheet + verdicts;
  - P3f — fact sheet + verdicts + template §4 framing contract;
  - P4-<D-XX.Y> — `objective.md` + `regs/<REG>.md` (confirmed regs present in module) + `cross/` pair files (both regs confirmed) + `cross/_interactions.md` (operative sections) + `templates/doc02_adjusted_goals.md` §3 + `steps/framing.md` + fact sheet (ambiguity files excluded per researcher ruling 2026-10-01; no anchor slice — anchors are code-derived);
  - P4t — fact sheet + the Emergent-tensions sections of every selected sub-domain's `cross/_interactions.md` (deterministic trim);
  - P5 — template + narrative sources + style excerpt of the golden example + SPEC §8.

- **Guarantees:** file list is a pure function of (company, verdicts, selection); no summarization, verbatim copies or references only; every path in a pack must resolve before the step starts (fail loudly, flag-not-drop).
- **Implementation:** `compose.py` (deterministic, stdlib-only for compute nodes); determinism matters, automation does not (ADR-010).

## 7. Runbook — executing one Phase 1 run

Each step is one `submit.sh` invocation on the Deucalion login node. Set `MVP_RUN_TAG`
for the first job; for every later job also set `MVP_RUN_ID=run_<tag>_<first-JOBID>` so the
stage re-enters the same run directory. Gate markers are pushed up by
`pipeline/deucalion/gate.sh <run_id> <gate> "<note>"` after local review, and results come
back down with `pipeline/deucalion/sync_down.sh`.

| # | Step | Command (login node) | Produces | Gate after |
|---|---|---|---|---|
| 1 | P1 | `bash pipeline/deucalion/submit.sh p1` | `steps/fact_sheet.yaml` | G-P1-A |
| 2 | P2 | `bash pipeline/deucalion/submit.sh p2` | `steps/verdicts.*` | G-P1-B |
| 3 | P3 | `bash pipeline/deucalion/submit.sh p3` | `steps/selection.*` | G-P1-C |
| 4 | P3f | `bash pipeline/deucalion/submit.sh p3f` | `steps/framing.md` | — |
| 5 | P4 → P5 | `bash pipeline/deucalion/submit.sh p4p5` | `steps/goals/*`, `steps/tensions.*`, `doc02_adjusted_goals.md`, `RUN_NOTES.md`, export to `output/<company>/` | G-P1-D |

Notes:

- **P3f must precede P4.** `stage_p4` and `stage_p5` both refuse to start without
  `steps/framing.md`; running `p4p5` before `p3f` aborts at the prerequisite check.
- `p4p5` chains p4 → p4t → p5 in one job. If p4 aborts part-way, resubmit `p4p5`: p4
  resumes at the first sub-domain without a validated artifact on disk, and p4t/p5 then
  run normally. This is the intended recovery path, not a defect.
- p5 is zero-LLM: assembly, L1 validation and the export to `output/<company>/` all
  happen in-process. A `p4p5` job that ends with `[p5] L1 validation PASS` has produced
  the deliverable; one that ends with `STAGE ABORTED: ... post-assembly L1 validation
  failed with N finding(s)` has left `doc02_adjusted_goals.md` in the run directory for
  forensics and exported nothing.
- Mono-regulation runs write `steps/tensions.json` as `{"tensions": []}` without a model
  call; §4 of the deliverable then reads "None — single-regulation run."
- Re-entry rule: any failed gate re-enters at the producing step with the gate's recorded
  corrections; earlier artifacts are amended in place with the document's own changelog
  entry (R11).

## 8. Artifacts written per run

```text
pipeline/runs/<run_id>/
├── doc02_adjusted_goals.md   # the assembled deliverable (Doc02 case format)
├── RUN_NOTES.md              # deterministic run meta + §8 evidence + gate ledger
├── steps/
│   ├── fact_sheet.yaml       # P1
│   ├── verdicts.md/.json     # P2
│   ├── selection.md/.json    # P3
│   ├── framing.md            # P3f (§2 framing table)
│   ├── tensions.md/.json     # P4t (§4 resolutions; empty for mono-regulation runs)
│   ├── goals/D-XX.Y.md       # P4 fragment per sub-domain (raw model markdown)
│   ├── goals/D-XX_Y.json     # P4 structured: goals + assumptions
│   └── gates/G-P1-*.approved # human gate marker files
├── inputs/ outputs/ logs/    # per-call forensics (system/user prompts, raw answers)
└── trace.jsonl + manifest.json

output/<company>/             # exported deliverable (after P5 validation PASS)
├── doc02_adjusted_goals.md
└── RUN_NOTES.md
```

## 9. Inspecting runs — the local inspector

Everything a run produced (stage history, per-call prompts/answers, artifacts,
the deliverable, live L1 validation) is browsable as a local web app. It lives
**outside** this repository, in `~/Work/aegis-inspector/` — a React 19 + Vite
frontend over an Express API that reads this repository's disk. It is not a
source of truth about the runs: everything it shows is read live from
`pipeline/runs/` and `output/`.

```bash
cd ~/Work/aegis-inspector && pnpm install && pnpm dev
#   API em :3000, app em http://localhost:5173
```

`AEGIS_REPO` (no `backend/.env`) is the absolute path to this repository's root.

Deliverables are exported **per run**, under `output/<company>/<run_id>/`.
Indexing them by company alone meant two runs of the same case overwrote each
other, with the newest silently winning.

## 10. Agent mode — the directed tool-calling runner (EXP-01 arm 2)

Same case, corpus, validators and zero-LLM render as the prompt pipeline; the
model instead drives a tool loop and decides the working granularity. The
submission tools feed the model's markdown through the SAME L0 parsers and
content gates (`parse_p1…parse_p4t`, `check_p4_quality`) and persist with the
SAME `store_parsed` — an agent artifact is indistinguishable from a pipeline
artifact. Anchors/§5/§6 stay code-derived (`controls.py`); the final document
is assembled by the SAME `assemble_doc`.

```bash
# one job runs the whole task as a conversation (resumable via checkpoint)
bash pipeline/deucalion/submit.sh agentic     # env: AEGIS_AGENT_TRANSPORT=tools|text,
                                              #      AEGIS_AGENT_MAX_TURNS (default 80)
```

Runner internals (`pipeline/src/agent/`): `tools.py` (the 17-tool surface:
read brief/contracts/modules, submit artifacts, derive anchors/Track B/§6,
`render_document`, `self_validate`, `finish` — finish is refused while L1
findings remain), `loop.py` (checkpoint per turn on `agent_conversation.jsonl`
→ re-entering stage `agentic` resumes; large old tool observations are elided
from the working history — disk state is authoritative), `prompt.py` (the
directed system brief + working order).

Honest-difference note for the experiment: the agent sees `self_validate` /
finish-gate findings and repairs them (the pipeline only gets the one L0
repair retry per call); the comparison reports this asymmetry explicitly.
