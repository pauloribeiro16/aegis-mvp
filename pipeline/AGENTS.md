# AGENTS.md — Pipeline Subsystem Operational Guidelines & Best Practices

> **Scope:** Guidelines for AI agents and human operators developing, refactoring, extending, or executing the AEGIS execution pipeline.
> **Inheritance:** Inherits all top-level invariants, scientific-conduct contracts (§-2), and rules (R1–R12) from [`../AGENTS.md`](../AGENTS.md).

---

## 1. Mission & Architecture of the Pipeline

The AEGIS pipeline is the automated orchestration engine that executes the phased AEGIS methodology (Phase 1 Contextual Definition, Phase 2 Operationalization, Phase 3 Coverage & Specification).

### Key Architectural Decisions:
- **Workflow, not Agent (ADR-010 D1, D4):** The production pipeline executes a staged sequence of deterministic and prompt-driven steps. The agentic arm is kept only as an experimental baseline (ADR-010, EXP-03).
- **State on Disk (ADR-010 D5):** Every stage reads its inputs from disk and writes its outputs to disk. No in-memory state survives across stages. A job re-enters cleanly from predecessor stage artifacts.
- **Human Gates (G-P1-A..D):** Stages stop at formal review gates represented by marker files (`steps/gates/G-P1-X.approved`). Unattended execution requires explicit `--preapprove-gates`.
- **Bit-Reproducibility (§-1, EXP-02):** Every run is seeded by default (`seed=42`, `temperature=0.2`). All sampling parameters are frozen into `config.json` and `manifest.json`.
- **Supercomputer (HPC) Isolation:** The pipeline runs on compute nodes (Deucalion) with zero outbound network egress. It uses Python 3.10+ standard library HTTP clients; heavy framework dependencies are strictly prohibited.

---

## 2. Directory Layout

The pipeline follows a modular, package-based architecture (`aegis_pipeline`) with thin, backward-compatible shims at `pipeline/src/`:

```text
pipeline/
├── AGENTS.md                         # (This file) Operational guidelines and developer guide
├── README.md                         # Supercomputer runbook and stage overview
├── cases/                            # Case bindings
│   ├── Case_01_TinyTask_SaaS/        # case.yaml + company_input.md binding
│   ├── Case_02_SecureBorder_Solutions/
│   └── Case_03_OmniBank/
├── deucalion/                        # HPC execution layer (SLURM + sync)
│   ├── phase1.sbatch                 # Hardened SLURM job script
│   ├── submit.sh                     # Stage job submission wrapper
│   ├── sync_up.sh                    # Workstation -> cluster payload sync
│   ├── sync_down.sh                  # Cluster -> workstation artifacts sync
│   └── gate.sh                       # Local gate marker review & push
├── src/                              # Legacy roots & backward-compatible shims
│   ├── run_pipeline.py               # Thin CLI entrypoint (new-run, run --stage)
│   ├── phase2.py                     # Backward-compatible shim for Phase 2
│   ├── phase3.py                     # Backward-compatible shim for Phase 3
│   ├── phase3_schemas.py             # Backward-compatible shim for Phase 3 schemas
│   ├── steps.py                      # Backward-compatible shim for StepRunner & helpers
│   ├── compose.py                    # Prompt ficha parser & context pack composer
│   ├── runconfig.py                  # Backward-compatible shim for config
│   ├── trace.py                      # Backward-compatible shim for trace ledger
│   ├── llm.py                        # Backward-compatible shim for stdlib LLM client
│   ├── validate.py                   # Backward-compatible shim for L1 validator
│   ├── quality.py                    # Backward-compatible shim for quality gates
│   ├── controls.py                   # Backward-compatible shim for control referential
│   │
│   └── aegis_pipeline/               # Core modular package (Production architecture)
│       ├── core/                     # Foundational engine primitives
│       │   ├── config.py             # Run configuration & sampling defaults
│       │   ├── trace.py              # trace.jsonl call ledger & manifest.json updater
│       │   └── llm_client.py         # Resilient stdlib Ollama HTTP client
│       ├── observability/            # Telemetry & diagnostics
│       │   ├── logging.py            # Structured stage & call logger
│       │   └── metrics.py            # Latency, token accounting, and run timers
│       ├── guards/                   # Deterministic checks & validation gates
│       │   ├── controls.py           # NIST/ISO/OWASP control resolver & R2b checker
│       │   ├── l1_validation.py      # L1 document and directory integrity validator
│       │   └── quality_gates.py      # Content gates (retention, anti-drift, R10b)
│       ├── phases/                   # Methodological phase implementations
│       │   ├── phase1/               # Phase 1 — Contextual Definition
│       │   │   ├── common.py         # Markdown table parsers & normalization
│       │   │   ├── facts.py          # P1 Fact sheet extractor & parser
│       │   │   ├── regulations.py    # P2 Regulation scope confirmation
│       │   │   ├── selection.py      # P3 Sub-domain subset selector
│       │   │   ├── framing.py        # P3f §2 4-dimension framing table
│       │   │   ├── goals.py          # P4 Adjusted goals table & quality gates
│       │   │   ├── tensions.py       # P4t Strategic tensions extractor & merger
│       │   │   ├── assembly.py       # P5 Deterministic Doc02 deliverable assembler
│       │   │   └── runner.py         # StepRunner orchestrator for P1–P5
│       │   ├── phase2/               # Phase 2 — Operational Objectives & Rules
│       │   │   ├── principles.py     # 7 universal engineering design principles
│       │   │   ├── parsers.py        # P2o rule parser & tension loader
│       │   │   ├── derivation.py     # Deterministic objective derivation & gates
│       │   │   ├── renderers.py      # Doc01 & Doc02 markdown renderers
│       │   │   └── runner.py         # Phase 2 CLI entrypoint & orchestrator
│       │   └── phase3/               # Phase 3 — Coverage Matrix & Skeleton
│       │       ├── schemas.py        # Matrix columns, ADR-007 D4 verdicts, skills
│       │       ├── skeleton.py       # Coverage matrix & principles skeleton builder
│       │       ├── verdicts.py       # Model verdict table parser & verification gates
│       │       ├── v0_cards.py       # V0 functional carrier card loader
│       │       └── runner.py         # Phase 3 CLI entrypoint & orchestrator
│       └── cli/                      # CLI dispatch
│           └── commands.py           # new-run, run --stage dispatch logic
└── tests/                            # Automated test battery
    ├── local_e2e_test.py             # Local mock-Ollama E2E pipeline test
    ├── agent_e2e_test.py             # Agent loop E2E test
    ├── assemble_real_test.py         # Real prose deliverable assembly test
    ├── quality_gate_test.py          # Adversarial red-team test for quality gates
    ├── phase2_test.py                # Phase 2 derivation, parsing & gate tests
    └── phase3_test.py                # Phase 3 skeleton, verdict & anchor tests
```

---

## 3. Strict Non-Negotiable Invariants — What MUST NOT Be Altered

1. **Sampling Defaults (§-1):**
   - Default sampling: `seed=42`, `temperature=0.2`.
   - **DO NOT** change default temperature, seed, top-p, or top-k in `config.py` or `run_pipeline.py` without a registered experiment in `docs/experiments/`.
   - Running unseeded requires explicit `--seed none`.

2. **Quality Gate Thresholds (METRICS.md):**
   - P4 Lexical retention floor: `0.30` (measured: EXP-02).
   - P4 Verbatim copy ceiling: `0.88` (measured: EXP-02).
   - Method distribution mode-collapse ceiling: `0.60` (R10b Invariant 3).
   - **DO NOT** loosen, bypass, or change these thresholds without calibrated evidence and user approval.

3. **External Runs Location (§0):**
   - Run directories (`manifest.json`, `trace.jsonl`, `steps/`, `logs/`) live outside the repository at `~/Work/aegis-runs/<run_id>/` (workstation) or `../aegis-runs/<run_id>/` (cluster).
   - Deliverables are exported to `<repo>/output/<company>/<phase>/<run_id>/`.
   - **NEVER** write ad-hoc run folders inside the repository root.

4. **Backward Compatibility & Existing Shims:**
   - Shims at `pipeline/src/` (`run_pipeline.py`, `phase2.py`, `phase3.py`, `steps.py`, etc.) are consumed by cluster SLURM scripts and existing test suites.
   - **DO NOT** delete or break the symbol exports in these shims.

5. **Technology Neutrality (Rule R5):**
   - Phase 1 and Phase 2 generators must strictly specify *what* is required without prescribing concrete tools, cloud vendors, or specific programming libraries.

---

## 4. How to Add Features and New Stages (Developer Guide)

Follow this step-by-step workflow when extending the pipeline:

### A. Adding a New Stage to an Existing Phase (e.g. adding `p3b` in Phase 1)
1. **Define the Prompt Ficha:**
   - Create `docs/pipeline/prompts/FICHA_PX_NAME.md` following the immutable prompt contract.
   - Register the file in `compose.py:FICHA_FILES`.
2. **Build the Deterministic Context Pack:**
   - Add a pack composer in `compose.py` (e.g. `compose_p3b_pack(...)`) reading strictly from prior stage outputs on disk.
3. **Implement the Parsing and Gate Validation:**
   - In `aegis_pipeline/phases/phase1/`, create the dedicated module (e.g. `aegis_pipeline/phases/phase1/stage_p3b.py`) with parsing and L0 gate validation.
4. **Register Step Execution in `StepRunner`:**
   - In `aegis_pipeline/phases/phase1/runner.py`, add `stage_p3b()` to `StepRunner`.
   - Implement retry-on-L0-failure and store output in `run_dir / "steps" / ...`.
5. **Update CLI Dispatch:**
   - In `aegis_pipeline/cli/commands.py`, add the stage identifier to `--stage` choices.
6. **Add Automated Regression Tests:**
   - Add test cases in `pipeline/tests/local_e2e_test.py` verifying stage execution, gate enforcement, and retry behavior.

### B. Adding a New Phase (e.g. Phase 4 Technical Architecture)
1. **Create the Phase Package:**
   - Create `pipeline/src/aegis_pipeline/phases/phase4/`:
     - `schemas.py`: Pure enums, regexes, and data models.
     - `parsers.py`: Structured output parsers.
     - `derivation.py`: Deterministic derivation rules.
     - `renderers.py`: Markdown deliverable formatting.
     - `runner.py`: Phase orchestrator and CLI entrypoint.
     - `__init__.py`: Clean public API export.
2. **Create Top-Level Shim (if standalone CLI needed):**
   - Create `pipeline/src/phase4.py` re-exporting symbols and dispatching `main()`.
3. **Add Deterministic Control & Validation Gates:**
   - Register any phase-specific control referentials in `aegis_pipeline/guards/controls.py`.
   - Extend `aegis_pipeline/guards/l1_validation.py` to validate Phase 4 outputs.
4. **Export Path Convention:**
   - Ensure deliverable exports route to `output/<company>/phase4/<run_id>/`.
5. **Write Unit and E2E Tests:**
   - Create `pipeline/tests/phase4_test.py` covering 100% of derivations, seam declarations, and gates.

---

## 5. Best Practices Guide for Pipeline Manipulation

When modifying or maintaining the pipeline, adhere to these production best practices:

### 1. Deterministic vs. Probabilistic Separation
- Keep code that can be computed deterministically (anchor lookups, matrix slicing, table formatting, ID allocation) **100% separated** from LLM calls.
- Never ask an LLM to allocate sequential IDs (`AG-D-XX.Y-001`, `RULE-D-XX.Y-001`, `ORG-D-XX.Y-001`) or format markdown tables if the code can assemble them deterministically.

### 2. Defensive Parsing & Atomic Writes
- Never write partial or unvalidated LLM output to final stage artifact paths.
- Write raw model output to `outputs/` first, parse and validate against gates, and only write to `steps/` upon gate passing.
- If a gate fails, keep the failed attempt artifact in `steps/` (e.g. `fact_sheet_attempt1.yaml`) for debugging forensics before retrying or aborting.

### 3. Trace & Manifest Accounting
- Every single LLM call must write a line to `trace.jsonl` via `trace.log_call(...)`.
- `manifest.json` must be updated after each stage with call counts, timestamps, job IDs, and stage status (`ok`, `aborted`, or `dry-run`).
- `inputs/` must capture the exact prompt sent (`001_P1_...`), and `outputs/` the raw response.

### 4. Zero Egress & Standard Library First
- Compute nodes have no internet access. Do not introduce dependencies that require `pip install` at runtime.
- Use standard library modules (`urllib.request`, `json`, `re`, `argparse`, `pathlib`, `hashlib`) wherever possible.

### 5. Local Pre-Flight Verification
Before syncing code to the cluster or submitting sbatch jobs, always run the full local test battery:
```bash
python3 pipeline/tests/local_e2e_test.py
python3 pipeline/tests/phase2_test.py
python3 pipeline/tests/phase3_test.py
python3 pipeline/tests/quality_gate_test.py
```
A commit or sync is only permitted if all test suites pass with **0 failures**.
