# AGENTS.md — Cases Subsystem Operational Guidelines

> **Scope:** Guidelines for AI agents and human operators inspecting, evaluating, or extending benchmark cases within `cases/`.
> **Inheritance:** Inherits all top-level invariants, scientific-conduct contracts (§-2), and rules (R1–R12) from [`../AGENTS.md`](../AGENTS.md).

---

## 1. Mission & Role of `cases/`

The `cases/` directory contains the **reference benchmark cases** for the AEGIS methodology.
It serves as the **immutable ground truth / golden standard** against which:
1. Automated pipeline stages (Phase 1, Phase 2, Phase 3) are evaluated.
2. Scientific experiments (EXP-01 through EXP-05, and future registered experiments) measure extraction accuracy, retention, calibration health, and compliance fidelity.
3. Quality gates (`validate.py`, `doc_lint.py`, `check_traceability.py`) are calibrated.

Every benchmark case in this directory represents a complete, hand-authored, verified operationalization of AEGIS Phase 1, Phase 2, and (where developed) Phase 3 deliverables.

---

## 2. Directory Layout & Existing Cases

```text
cases/
├── AGENTS.md                         # (This file) Operational contract for the cases subsystem
├── Case_01_TinyTask_SaaS/            # Micro-SaaS benchmark (8 employees; GDPR + CRA)
│   ├── 01_PHASE1_CONTEXT/            # Phase 1 context deliverables
│   │   ├── Doc01_INTAKE_FORM.md      # Ground truth intake facts (§1–§5 plain prose)
│   │   ├── Doc02_Adjusted_Goals.md   # Golden adjusted goals (AG-D-XX.Y-NNN)
│   │   └── README.md                 # Case profile & context summary
│   ├── 02_PHASE2_RULES/              # Phase 2 operationalization deliverables
│   │   ├── Doc01_Operational_Objectives.md  # 62 operational objectives (PO/SO)
│   │   └── Doc02_Secure_Design_Principles.md # 7 universal engineering principles
│   ├── 03_PHASE3_SPEC/               # Phase 3 technical specifications
│   │   ├── Doc01_Requirements_Elicitation_and_PUC.md # V0 functional cards (RXX.YY)
│   │   └── Doc02_System_Use_Cases.md # Primary and misuse use-cases
│   └── filtered_corpus/              # Deterministic case slice (composed from baseline/)
│       └── index.md                  # Verbatim module index for active regulations
├── Case_02_SecureBorder_Solutions/   # Mid-market physical security benchmark (GDPR + CRA + NIS2 + AI_Act)
│   ├── 01_PHASE1_CONTEXT/            # Doc01 intake + Doc02 adjusted goals (35 active sub-domains)
│   ├── 02_PHASE2_RULES/              # Doc01 (100 objectives) + Doc02 principles
│   ├── 03_PHASE3_SPEC/               # Doc01 PUC + Doc02 system use cases
│   └── filtered_corpus/              # Composed slice (GDPR, CRA, NIS2, AI_Act)
└── Case_03_OmniBank/                 # Financial enterprise benchmark (DORA + GDPR + NIS2)
    ├── 01_PHASE1_CONTEXT/            # Doc01 intake + Doc02 adjusted goals (38 sub-domains)
    ├── 02_PHASE2_RULES/              # Doc01 (134 objectives) + Doc02 principles
    └── filtered_corpus/              # Composed slice (DORA, GDPR, NIS2)
```

---

## 3. Strict Non-Negotiable Invariants — What MUST NOT Be Altered

The following items are **strictly frozen** and **MUST NEVER be modified without explicit, written instruction from the user**:

1. **Frozen Hand-Authored Deliverables:**
   - Any document under `cases/<Case>/01_PHASE1_CONTEXT/`, `02_PHASE2_RULES/`, or `03_PHASE3_SPEC/` is a historical scientific ground truth.
   - **DO NOT** edit, reformat, overwrite, or "fix" these deliverables during normal agent tasks or pipeline runs.
   - Modifying a ground-truth document silently invalidates all previous experiment metrics, breaks deterministic regression assertions (e.g. `test_every_objective_gets_exactly_one_row` asserting 62, 100, 134 objectives), and constitutes scientific misconduct (AGENTS.md §-2).

2. **No Manual Edits to `filtered_corpus/`:**
   - Files in `filtered_corpus/` are generated deterministically by [`scripts/generate_case_corpus_slice.py`](../scripts/generate_case_corpus_slice.py) from `baseline/domains/`.
   - Never hand-edit, delete, or summarize text in `filtered_corpus/` (Rule R9: composed, not filtered; zero summaries, zero text omissions).

3. **No Fact Invention (Rule R6):**
   - Intake facts in `Doc01_INTAKE_FORM.md` are the single source of truth for each case. Never add ungrounded assumptions to a case unless prefixed with `> ASSUMPTION:`.

4. **No Editorial Meta-Commentary (Rule R11):**
   - Never insert changelogs, commit messages, agent notes, or conversational text into case deliverables.

---

## 4. Conventions & Schemas in Cases

When reading or referencing case content, strictly respect the following conventions:

| Element | Format / Regex | Examples | Notes |
|---|---|---|---|
| **Sub-domain** | `D-XX.Y` (`D-01.1` to `D-10.3`) | `D-01.1`, `D-03.2` | 38 canonical sub-domains; never merge or invent (Rule R1). |
| **Adjusted Goal** | `AG-D-XX.Y-NNN` | `AG-D-01.1-001` | Tailored proportionately to company scale; technology neutral (Rules R3, R4, R5). |
| **Operational Objective** | `(PO\|SO)-D-XX.Y-NNN` | `PO-D-01.1-001`, `SO-D-03.1-002` | `PO-` strictly for GDPR obligations; `SO-` for CRA, NIS2, DORA, AI Act. |
| **Operational Rule** | `RULE-D-XX.Y-NNN` | `RULE-D-01.1-001` | Imperative operational requirement enforcing the parent objective. |
| **Engineering Principle** | `PRIN-ENG-01` to `PRIN-ENG-07` | `PRIN-ENG-01` | 7 universal principles from Phase 2 Doc02. |
| **Carrier Card (V0)** | `RXX.YY` | `R01.01`, `R02.04` | Functional capability card from Phase 3 Doc01 PUC. |
| **Organizational Item** | `ORG-D-XX.Y-NNN` | `ORG-D-06.3-001` | Obligations routed to the organizational/process lane. |
| **Coverage Verdict** | ADR-007 D4 Enum | `Fully covered (anchored)` | Pure 5-value enum; never hybrid `enum: reason` (R10b Invariant 2). |

---

## 5. How to Add a New Case (Operator & Agent Guide)

When instructed by the user to introduce a new benchmark case (e.g. `Case_04_IoT_Medical`):

### Step 1: Create Case Intake & Context
1. Create `cases/Case_XX_<Name>/01_PHASE1_CONTEXT/Doc01_INTAKE_FORM.md` based on [`templates/company_input.md`](../templates/company_input.md).
2. Ensure sections §1 (Profile), §2 (Product/Service), §3 (Data Handled), §4 (Infrastructure), and §5 (Assumed Regulations) are completely filled with concrete, unambiguous facts.

### Step 2: Configure Pipeline Binding
1. Create `pipeline/cases/Case_XX_<Name>/case.yaml` specifying:
   - `case_id`: `Case_XX_<Name>`
   - `company_name`: Official legal and brand name
   - `input_file`: Path to the intake form
   - `scope`: Assumed candidate regulations (`GDPR`, `CRA`, `NIS2`, `DORA`, `AI_Act`)

### Step 3: Compose Deterministic Corpus Slice
Run the deterministic composer to generate the case's slice:
```bash
python3 scripts/generate_case_corpus_slice.py --case Case_XX_<Name>
```
Verify that `cases/Case_XX_<Name>/filtered_corpus/index.md` is populated and all active modules resolve.

### Step 4: Run the Pipeline to Generate Deliverables
Execute the pipeline stages to generate output in the run directory (outside the case directory):
```bash
python3 pipeline/src/run_pipeline.py new-run --case Case_XX_<Name> --run-dir ~/Work/aegis-runs/run_new_001 --model qwen3.8:27b
python3 pipeline/src/run_pipeline.py run --stage all --run-dir ~/Work/aegis-runs/run_new_001
```

### Step 5: Promotion to Benchmark (Requires User Approval)
Only copy generated deliverables from `output/<Company>/phase1/<run_id>/` into `cases/Case_XX_<Name>/` if the human operator explicitly approves the baseline promotion following human gate reviews (G-P1-A through G-P1-D).
