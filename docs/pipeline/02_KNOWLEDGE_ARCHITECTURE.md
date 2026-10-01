---
document_id: AEGIS-PIPE-02
title: 'Knowledge Architecture — layers, graph schema, threat knowledge'
version: 0.1.0
created: 2026-10-01
status: ACTIVE
adrs:
  - docs/decisions/ADR-2026-10-01_knowledge-representation.md
  - docs/decisions/ADR-2026-10-01_threat-knowledge-layer.md
---

# Knowledge Architecture

## 1. Layer model

| Layer | Content | Format / where | Consumed by | Source of truth |
|---|---|---|---|---|
| **K1 — Regulatory & control knowledge** | 38 sub-domains (`D-XX.Y`): neutral Baseline Goals, per-regulation modules, ambiguity cards, cross-regulation pairs, verbatim articles; 14 control referentials; SR↔control mapping store; full traceability chain | `baseline/domains/` (modular markdown + YAML + `aegis:` tags); `baseline/MAPPINGS/`; `baseline/CONTROLS/`; `baseline/01_Ambiguity_Registry.md` + `baseline/registry.csv` | Phases 1–3 | frozen baseline (read-only, by reference) |
| **K2 — Best-practice knowledge** | Good-practice statements, context-conditioned (ADR-001 tiers: law → ENISA/EDPB → control catalogs) | to be `baseline/BEST_PRACTICES/` (advisory pattern) — **not created yet** | Phase 2 onward | pending ADR-001 ratification |
| **K3 — Threat knowledge** | CWE, CAPEC (core); ATT&CK (consultive); ATLAS, EMB3D (per case). CVE/KEV/EPSS **excluded** | to be `baseline/THREATS/` (advisory pattern: manifest + ID list + per-entry JSON) — **not created yet** | Phase 3 Part 2 | external MITRE/OAS catalogs, ingested verbatim |
| **K4 — Company & case state** | intake, fact sheets, verdicts, versioned case artifacts, registers, run notes | `input/<company>/`, `output/<company>/`, `cases/<case>/` | all phases, own case only | the case tree itself |

One external dependency is inherited from the baseline: the canonical ambiguity registry lives in the sibling frozen repo (`config.yaml` → `../Methodology_compact/.../AMBIGUITY_REGISTRY/registry.md`); the in-repo mirror (`baseline/01_Ambiguity_Registry.md`, `baseline/registry.csv`, 49 clause cards) is the working surface.

## 2. K1 machine-readable inventory (what can be indexed today)

| Surface | Granularity | Fields available |
|---|---|---|
| `baseline/MAPPINGS/sr_control_mappings/<REG>.json` (5 files) | one Security Requirement (`SR-<REG>-NNN`) | `sr_id`, `title`, `sub_domain[]`, `linked_objectives[]`, `source_clauses[]` (clause_id + article_ref), `nist_csf[]`, `nist_pf[]`, `nist_airmf[]`, full `source_record` |
| `baseline/MAPPINGS/traceability/traceability.csv` | one chain row | regulation, sub_domain, hso_id, so_reg_id, subso_id, req_id, sr_id, articles, ambiguity_clauses, nist_csf/pf/airmf |
| `baseline/registry.csv` + `01_Ambiguity_Registry.md` | one clause card | clause_id, regulation, article, verbatim_phrase, sub_domain, berry_flag, severity, card_variant, recommended_variant/source, nist anchors |
| `baseline/CONTROLS/<FW>/**` (14 frameworks) | one control per JSON | `control_id`, `subcategory_text`, `informative_references[]`, `implementation_examples[]`; `_MANIFEST.json` (advisory flag, enforced flag) |
| `regs/<REG>.md` YAML blocks | one requirement per block | `req_id`, `derives_from`, `fit_criterion`, `priority`, `verification_method`, `nist_csf/pf/airmf`, `applicable_if.regs` |
| `regs/<REG>.ambiguity.md` | one clause per `#####` section | clause id/type, `**Control anchors:**`, Berry anchor, instance variant readings |
| `aegis:` HTML comment tags (`aegis:pair`, `aegis:subso`, `aegis:req`) | structural boundaries | deterministic module parsing |
| `objective.md` YAML | one Baseline Goal per module | `id` (`SG-D-XX.Y.HL`), applies_to, derivation_source, tensions |

Consequence: **every entity and edge the pipeline needs already exists in a parseable surface**; the knowledge graph is a reorganization, not new knowledge work.

## 3. Knowledge-graph schema (designed now; materialization = later increment — ADR-011)

### 3.1 Node types

| Node | Key properties | Primary source |
|---|---|---|
| `Regulation` | id (`GDPR`, `CRA`, `NIS2`, `DORA`, `AI_Act`), anchor axes | module `regs/` dirs, mappings `meta` |
| `Article` | regulation, number, verbatim path | `articles/<REG>_Art_N.md` frontmatter |
| `Clause` (ambiguity card) | clause_id, berry_flag, severity, variant readings | `registry.csv`, `regs/<REG>.ambiguity.md` |
| `SubDomain` | `D-XX.Y`, canonical name | `domains/D-XX.Y/_index.md` |
| `BaselineGoal` | id (`SO-D-XX.Y.HL` / `SO-D-XX.Y.<REG>`; corpus YAML alias `SG-`), pattern, property | `objective.md`, Sub-SO YAML |
| `AdjustedGoal` | `AG-D-XX.Y-NNN`, pattern, property, adjustment | case Phase 1 output |
| `OperationalObjective` | `PO-/SO-D-XX.Y-NNN`, verification criteria | case Phase 2 Doc01 |
| `Requirement` | case `REQ/RN/ORG` ids; corpus `req_id` | Part 1 cards; corpus YAML |
| `SecurityReq` | `SR-<REG>-NNN` | mappings store |
| `Control` | framework, control_id | `CONTROLS/**/*.json` |
| `CompanyFact` | field, value, input trace | P1 fact sheet |
| `CaseArtifact` | path, phase, version | case tree |
| `ThreatEntry` (future, K3) | framework, entry_id | `baseline/THREATS/` |

### 3.2 Edge types

| Edge | From → To | Derived from |
|---|---|---|
| `applies_to` | Regulation → SubDomain | module participant rows |
| `article_of` | Article → Regulation | article frontmatter |
| `has_clause` | Article → Clause | ambiguity modules |
| `derives_from` | Goal→Goal, AG→BaselineGoal, OO→AG, Req→OO | YAML `derives_from`/`inherits_from`, case chains |
| `anchored_to` | BaselineGoal / AG / OO / SR / Req → Control | YAML anchor surfaces, `**Control anchors:**` lines, mapping store |
| `cited_by` | Article → Goal / Requirement | R2a citations |
| `resolves` | Clause → Goal / Requirement | R7 citations, §5, constraint rows |
| `triggers` | CompanyFact → SubDomain | §3 trigger rationale |
| `covers` | Requirement → OperationalObjective | coverage matrix (ADR-007) |
| `maps_to` | ThreatEntry → ThreatEntry (weakness→pattern→technique); Req/Threat → ThreatEntry | K3 mapping pass (ADR-012) |

### 3.3 Surface → graph build map

| Source row/record | Produces |
|---|---|
| `traceability.csv` row | full F0 chain edges (SubDomain→BaselineGoal→SR) + SR→Control edges + Article/Clause links |
| `sr_control_mappings` entry | `SecurityReq` node + `anchored_to` edges + `linked_objectives`/`source_clauses` edges |
| `registry.csv` row | `Clause` node + anchor edges |
| `CONTROLS` JSON | `Control` node |
| `regs/<REG>.md` YAML requirement block | corpus `Requirement` node + `derives_from` + anchor edges |
| `aegis:req` / `aegis:subso` / `aegis:pair` tags | parse boundaries (no semantic nodes) |

### 3.4 Materialization strategy (future increment)

- Deterministic builder script (the SPEC §9-anticipated graph builder; candidate name `scripts/build_knowledge_graph.py`): reads the surfaces above, emits `docs/pipeline/graph/node_link.json` + GraphML export.
- The graph is a **regenerable derived view**: never hand-edited; consistency check = node/edge counts vs source record counts (same anti-circular spirit as `verify_no_loss.py`).
- No vendor lock: plain JSON/GraphML files; loading into any graph tool (or none) is optional.
- Retrieval in the pipeline stays **context packs** (deterministic); the graph adds query power where packs are weak: T6 anchor-provenance analysis (the 58 out-of-set anchor debt), impact analysis ("which goals cite this article?"), coverage debugging.
- Justification for deferring: the systematic RAG-vs-GraphRAG evidence favors graphs for relational/multi-hop questions and packs already cover factual lookup; no published head-to-head exists for EU-regulation compliance QA — build when a concrete query need hurts (ADR-011).

## 4. K2 — best-practice layer (gated)

- Enters the pipeline **only after ADR-001 (PROPOSED) is ratified**. Until then, no ficha cites good-practice sources.
- Planned shape: `baseline/BEST_PRACTICES/` following the advisory-framework pattern (`_MANIFEST.json` + ID list + per-entry JSON), with ADR-001's three source tiers and admission gate A1–A4 recorded per entry.
- Pipeline touchpoints when live: Phase 2 design principles (engineering spine) and Phase 3 Part 1 proposal rounds may cite K2 entries as **advisory anchors** (R2b discretion), never as regulation-derived obligations.

## 5. K3 — threat knowledge layer (Phase 3 Part 2)

### 5.1 Adopted set and altitude

| Catalog | Role | Feeds |
|---|---|---|
| **CWE** — Common Weakness Enumeration | core; weakness categories at mechanism altitude | `02_TECHNICAL_THREATS_STRIDE.md` (threat identification), weakness classing of findings |
| **CAPEC** — Common Attack Pattern Enumeration | core; attacker patterns at mechanism altitude | `04_ATTACK_VECTORS_AND_DEFENSE_TREES.md` (vector naming, tree pruning) |
| **ATT&CK** | consultive; adversary TTPs (detection-leaning vocabulary) | defense trees, governance discussions — optional per case |
| **ATLAS** (ML threats) / **EMB3D** (embedded) | per-case routing: only when the case profile includes AI/ML or embedded components | corresponding threat catalogs |
| CVE / KEV / EPSS | **excluded** — instance-level vulnerabilities; below the design altitude of Phase 3 deliverables (R13 specificity discipline); risk-register likelihood stays a reasoned estimate | — |

### 5.2 Ingestion & anchoring rules

- Ingest into `baseline/THREATS/<CATALOG>/` following the advisory-framework pattern (manifest with `advisory: true`, source URLs, fetch date; flat ID list; per-entry JSON). Generation precedent: `scripts/generate_advisory_framework.py`.
- **Only-cite-what-resolves:** every cited threat ID must resolve to a JSON under `baseline/THREATS/`; an unresolvable ID is dropped or replaced with `—`, never marked with `?` (R12 discipline). Guard T8 (new, with ingestion): same check automated in `check_traceability.py`.
- **Chain as mapping pass, not free text:** threat → CWE weakness → CAPEC pattern → (optional) ATT&CK technique is a dedicated enrichment step (PROM-P3B-05) with explicit ledger columns (`cwe_id`, `capec_id`, `attack_id`) — the NEXUS/CIRCL pattern. IDs are matched, never generated.
- **Scope discipline (R8 analog):** K3 feeds Part 2 artifacts only; it never becomes an anchor of Part 1 requirements. ATLAS/EMB3D activate only via case-profile routing.

## 6. Knowledge requirements matrix (which knowledge each step needs)

| Pipeline step | K1 corpus | K1 mappings | K1 ambiguity | K2 practices | K3 threats | K4 company/case |
|---|---|---|---|---|---|---|
| P1 facts | — | — | — | — | — | input §1–§4 |
| P2 regulations | scope criteria (SPEC §5, embedded in ficha) | — | — | — | — | fact sheet, §5 |
| P3 sub-domains | `domains/index.md`, `_index.md` participant rows | — | — | — | — | fact sheet, verdicts |
| P4 goals | `objective.md`, `regs/<REG>.md`, `cross/`, `articles/` | `sr_control_mappings/<REG>.json` | `regs/<REG>.ambiguity.md`, `registry.csv` | (ADR-001: not yet) | — | fact sheet |
| P5 render | output template | — | — | — | — | all step outputs |
| Phase 2 | regs + AG set | mappings | registry | PRIN sources (when K2 live) | — | AG set |
| Phase 3 Part 1 | full chain | mappings + `traceability.csv` | registry | ADR-001 tiers (when ratified) | — | objectives, v0 baseline, round registers |
| Phase 3 Part 2 | chain refs (citations only) | — | — | — | CWE, CAPEC, ATT&CK (+ ATLAS/EMB3D routed) | system model, requirements, coverage matrix |

Reading: Phases 1–2 are knowledge-light by design (the user's premise holds — the heavy lifting is K1 lookup + company facts); the knowledge burden concentrates in Phase 3 Part 1 (chains + K2) and Part 2 (K3). The KG materialization (§3.4) pays off exactly where the matrix is densest.
