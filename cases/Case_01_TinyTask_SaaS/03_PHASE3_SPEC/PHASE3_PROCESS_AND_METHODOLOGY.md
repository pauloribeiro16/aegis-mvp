# AEGIS Phase 3 — Requirements Engineering & Security/Privacy Synthesis Methodology

> **Document Type:** Methodological Manual & Practical Process Guide  
> **Lifecycle Phase:** AEGIS Phase 3 — Specification  
> **Target Audience:** Systems Architects, Requirements Engineers, Security Officers, AI Agents  
> **Status:** Normative Methodology Reference  

---

## Executive Summary

This document establishes the formal, repeatable methodology for conducting **Phase 3 (Specification)** within the AEGIS Framework. It provides both the theoretical foundations drawn from classical requirements engineering literature and the concrete, step-by-step operational process required to take a pure functional software baseline (**Version 0**) and systematically synthesize it with upstream regulatory and secure design obligations (**Phase 2**) to generate an augmented, verifiable, and secure specification (**Version 1**).

By segregating functional elicitation from security synthesis across distinct versioned baselines, AEGIS eliminates the common pitfalls of requirements engineering: premature technology lock-in, unverified architectural constraints, and polluted functional user stories.

---

## 1. Foundational Theoretical Frameworks & Literature Grounding

The AEGIS Phase 3 methodology synthesizes four authoritative standards and theoretical frameworks from software engineering literature:

```text
+-----------------------------------------------------------------------------------+
|                            THEORETICAL FOUNDATIONS                                |
+-----------------------------------------------------------------------------------+
|  Suzanne & James Robertson (Volere)     |  Karl Wiegers & Joy Beatty               |
|  - Work Context & Business Events       |  - 3-Level Requirements Architecture     |
|  - Product Use Cases (PUC)              |  - EARS Syntax for Precise Constraints   |
|  - Snow Cards & Non-Functional Criteria |  - Quality Attributes vs Functionality   |
+-----------------------------------------+------------------------------------------+
|  Alistair Cockburn                      |  ISO/IEC/IEEE 29148:2018                 |
|  - Sea-Level (User Goal) Granularity    |  - Characteristics of Good Requirements  |
|  - Fully Dressed Behavioral Flows       |  - Complete Bidirectional Traceability   |
|  - Extension Points for Failure/Threats |  - Empirical Verification Methods        |
+-----------------------------------------------------------------------------------+
```

### 1.1 Suzanne & James Robertson: The Volere Approach
*Source: Suzanne Robertson & James Robertson, "Mastering the Requirements Process: Getting Requirements Right", 3rd ed., Addison-Wesley.*

The Volere methodology establishes that requirements do not exist in a vacuum; they stem from the **business context** and **business events**:
1. **The Work Context Model:** Defines the boundaries of the business domain being studied, identifying external adjacent systems, human business actors, and information flows entering and leaving the work.
2. **Business Events & Product Use Cases (PUC):** When a business event occurs (e.g., *Customer signs up*, *Member logs billable hours*), the organization responds. The portion of that response performed by software constitutes a **Product Use Case (PUC)**.
3. **Purity of Functional Scope:** Functional requirements define *what the system must do to support the business work*, completely decoupled from technological choices or non-functional constraints. Conflating functional requirements with security rules at the initial elicitation stage corrupts the baseline and hides true business needs.
4. **Non-Functional Fit Criteria:** Non-functional requirements (including security and privacy) must have an unambiguous, measurable **Fit Criterion** that allows engineers to objectively determine whether an implementation satisfies the requirement.

### 1.2 Karl Wiegers & Joy Beatty: Software Requirements Architecture
*Source: Karl Wiegers & Joy Beatty, "Software Requirements", 3rd ed., Microsoft Press.*

Wiegers and Beatty formalize the distinction between three hierarchical levels of requirements:
1. **Business Requirements:** The high-level objectives and business rationale of the enterprise sponsoring the product (captured in Phase 1 / Phase 3 Scope).
2. **User Requirements:** Tasks and goals that users must be able to accomplish with the product (captured via Sea-Level Use Cases).
3. **Functional vs. Non-Functional Requirements:**
   - *Functional Requirements:* Describe observable system behaviors and calculations under specific conditions.
   - *Non-Functional Requirements (Quality Attributes & Constraints):* Specify how well the system performs, detailing security, privacy, availability, and performance characteristics.
4. **EARS (Easy Approach to Requirements Syntax):** To eliminate ambiguity, Wiegers advocates the EARS syntax (developed by Alistair Mavin et al.), enforcing precise sentence templates for specifying constraints and unwanted behaviors:
   - *Ubiquitous:* `The <system> shall <system response>.`
   - *Event-Driven:* `When <trigger>, the <system> shall <system response>.`
   - *State-Driven:* `While <state>, the <system> shall <system response>.`
   - *Unwanted Behavior:* `If <condition/threat>, then the <system> shall <system response>.`
   - *Optional Feature:* `Where <feature is present>, the <system> shall <system response>.`

### 1.3 Alistair Cockburn: Writing Effective Use Cases
*Source: Alistair Cockburn, "Writing Effective Use Cases", Addison-Wesley.*

Cockburn establishes the standard for behavioral user requirements:
1. **Goal Granularity (The Sea-Level Standard):**
   - *Sky Level / Cloud Level:* Enterprise or summary goals (e.g., "Run SaaS Operations").
   - *Sea Level (User Goal):* A task completed by a primary actor in a single session to achieve a measurable business objective (e.g., "Log Billable Hours", "Create Project Workspace"). **Phase 3 operates strictly at this level.**
   - *Underwater / Clam Level:* Procedural micro-UI actions (clicking a button, entering text, validating email format). Cockburn warns against clam-level use cases as they clutter specifications with transient UI implementation details.
2. **The Fully Dressed Use Case Anatomy:**
   - *Primary & Supporting Actors:* Who initiates and who assists.
   - *Preconditions & Trigger:* The exact state required before execution and the event initiating it.
   - *Main Success Scenario (MSS):* The clean, happy-path sequence of actor action and system response.
   - *Extensions (Alternative & Exception Flows):* Explicit branches handling failures, edge cases, and unauthorized access attempts. This is the **primary functional anchor for security controls**.
   - *Postconditions (Minimal & Success Guarantees):* Guarantees maintained by the system, even when an extension fails (e.g., "Minimal Guarantee: No partial transaction is committed and security audit log records the failure").

### 1.4 ISO/IEC/IEEE 29148:2018 Requirements Engineering Standard
*Source: ISO/IEC/IEEE 29148:2018 Systems and software engineering — Life cycle processes — Requirements engineering.*

ISO 29148 dictates the mandatory quality characteristics of well-formed requirements:
- **Unambiguous:** Has only one possible interpretation.
- **Verifiable:** Can be validated through an objective, empirical method: Inspection (`INSPECT`), Demonstration (`DEMONSTRATE`), Analysis (`ANALYZE`), or Test (`TEST`).
- **Traceable:** Maintains bidirectional lineage from upstream regulatory mandates down to test procedures.
- **Necessary:** Essential to meet operational, stakeholder, or regulatory objectives.
- **Feasible:** Technically achievable within known organizational and technological constraints.

---

## 2. The AEGIS Methodological Synthesis: From Phase 2 to Phase 3

### 2.1 The Upstream Contract
In the AEGIS lifecycle, Phase 3 does not invent security or regulatory requirements from scratch. It consumes the formal outputs of **Phase 2 (Operationalization)**:
1. **Operational Objectives (`Doc01_Operational_Objectives.md`):**
   - Privacy Objectives (`PO-D-XX.Y-NNN`): Derived from GDPR articles (consent, data minimization, right to erasure, storage limitation).
   - Security Objectives (`SO-D-XX.Y-NNN`): Derived from EU Cyber Resilience Act (CRA) Annex I requirements (vulnerability handling, attack surface reduction, cryptographic protection, integrity monitoring).
2. **Secure Design Principles (`Doc02_Secure_Design_Principles.md`):**
   - 7 Engineering Principles (`PRIN-ENG-01` to `PRIN-ENG-07`): Least Privilege, Defense in Depth, Secure Defaults, Fail-Securely, Complete Mediation, Data Minimization, and Auditability.

### 2.2 The Separation of Concerns: Why Version 0 Must Be Purely Functional
Attempting to author functional requirements and security requirements simultaneously results in **The Pre-Baked Security/Privacy Trap**:
- An engineer writing a "User Login" requirement might write: *"The user must log in using 2FA, bcrypt password hashing, and session tokens stored in secure HttpOnly cookies."*
- **Why this fails:**
  - It specifies implementation technology (`bcrypt`, `HttpOnly cookies`), violating technology neutrality (Rule R13).
  - It prematurely dictates architecture without analyzing the actual risk profile or threat model.
  - It pollutes the business user goal with non-functional security controls.

**The AEGIS Solution:** 
1. Build **Version 0 (V0)** as a **100% pure functional baseline** representing only what the business and users need to accomplish.
2. Formally synthesize Phase 2 rules against V0 to produce **Version 1 (V1)**, which defines the testable security constraints, fit criteria, and use case extension points without distorting the underlying functional model.
3. Where the synthesis reveals a genuine functional gap — an obligation that requires user-visible, goal-level functionality absent from V0 — evolve the functional model through the controlled **Functional Refinement Pass (Step 5b)**: every change classified in the D1–D4 taxonomy, proposed through the Step 3 risk-acceptance rounds, with `part1_security_privacy/v0_functional_baseline/` left untouched as the locked reference.

```mermaid
flowchart TD
    subgraph P2["AEGIS Phase 2 — Operationalization"]
        PO["Privacy Objectives<br>(PO-D-XX.Y-NNN / GDPR)"]
        SO["Security Objectives<br>(SO-D-XX.Y-NNN / CRA)"]
        ENG["Secure Design Principles<br>(PRIN-ENG-01 .. 07)"]
    end

    subgraph P3_V0["Phase 3 — Version 0 (Pure Functional Baseline)"]
        R_V0["Business Requirements (R1.1 .. R8.2)<br>Pure Functional GPTools Table 22 Cards"]
        PUC_V0["Product Use Cases (PUC 1.1 .. 8.2)<br>Volere Work Context Boundary"]
        UC_V0["Sea-Level Use Cases ({U.C. 1.1} .. {U.C. 8.2})<br>Cockburn Main Success Scenarios"]
    end

    subgraph Synth["Synthesis Process (Steps 2–5b)"]
        Matrix["Cross-Cutting Matrix & Asset Mapping"]
        EARS["EARS Formulation of Security & Privacy NFRs (RN)"]
    end

    subgraph P3_V1["Phase 3 — Version 1 (Synthesized Baseline)"]
        Doc01_V1["Doc01: Requirements Elicitation<br>(+ Non-Functional Requirements & P2 Trace)"]
        Doc02_V1["Doc02: System Use Cases<br>(+ Security Preconditions, Extensions, Guarantees)"]
        Round_Notes["Round Documentation<br>(part1_security_privacy/synthesis_rounds/ — client verdicts per item)"]
    end

    P2 --> Synth
    P3_V0 --> Synth
    Synth --> P3_V1
    P3_V1 --> P3P2["Phase 3 — Part 2<br>Threat & Risk Analysis<br>(gated by the Part 1 Exit Gate, ADR-006)"]
```

---

## 3. The Progressive Synthesis Process (Iterative Risk-Acceptance Cycle)

### The Part 1 Loop: Engine and Inputs

Part 1 (Security & Compliance) runs an iterative loop with two internal roles:

1. **The engine — Iterative Evolution Loop.** A permanent cycle between requirements and use cases, always improving them on two axes:
   - **Compliance:** every Phase 2 objective is checked against the functional model via `part1_security_privacy/synthesis_rounds/OBJECTIVE_MAPPING.md` (objective-centric) and `UC_OBJECTIVE_CORRESPONDENCE.md` (use-case-centric, regulation-tagged).
   - **Principles:** every secure-design principle (`PRIN-ENG-01..07`) is checked via `part1_security_privacy/synthesis_rounds/PRINCIPLE_MAPPING.md` (principle-centric) — the same review discipline as objectives, so "are all principles followed?" has a recorded, auditable answer.
   Each loop iteration: **reveal** use cases and requirements → **check** objectives and principles (both mappings) → **propose** constraints/adjustments for the gaps → **client verdict** per item, recorded in the round documentation → **converge**. Only after convergence do `Doc01`/`Doc02` versions evolve. The transition from assessment to improvement **is** the round itself: the mappings produce proposals, the round documentation turns verdicts into baseline changes.
2. **The inputs — Requirement Derivation.** The derivation machinery that feeds the loop: the V0 functional baseline, the Phase 2 objectives and principles, the EARS formulation with fit criteria, and the absorption rules (§3.3 of the guidelines). Derivation produces the *candidates*; the loop decides what enters the baseline.

**Threat modulation is not a Part 1 activity.** Threat analysis and modeling belong to **Phase 3 Part 2 — Threat & Risk Analysis** (ADR-006, superseding the separate-Fase-4 placement of ADR-005): Part 1 delivers a risk-accepted, control-anchored baseline whose asset and trust-boundary statements seed Part 2. No threat catalog, attack modeling, or abuse-case derivation appears in Part 1 deliverables.

### Step 1: Elicitation and Freezing of Functional Baseline (V0)
- **Goal:** Capture the complete operational scope of the product in purely functional terms.
- **Process:**
  1. Identify Business Roles and Contextual Information Flows (Volere Work Context Model).
  2. Define the Business Expectations and Customer Goals.
  3. Formulate Atomic Business Requirements using the standardized GPTools Table 22 card format. Every requirement title MUST use an active verb in the infinitive (e.g., *Manage User Accounts*, *Log Billable Hours*).
  4. Ensure zero technology leakage (no references to specific databases, cloud services, or protocols).
  5. Derive Product Use Cases (PUC) mapping business events to boundary inputs and outputs.
  6. Author Cockburn Sea-Level Use Cases (`{U.C. n.m}`) focusing on the Main Success Scenario (MSS).
- **Result:** Locked `part1_security_privacy/v0_functional_baseline/` containing `Doc01` and `Doc02`.

### Step 2: Cross-Cutting Regulatory Analysis
- **Goal:** Determine which Phase 2 objectives apply to which functional requirements and areas.
- **Process:**
  1. **Asset Identification:** Identify all business assets, user data, credentials, and system artifacts handled by each requirement `R...` and use case `{U.C. ...}`.
  2. **Trust Boundary Mapping:** Identify where data crosses organizational or system boundaries (e.g., user browser to application service, application service to external payment gateway, internal tenant to internal tenant).
  3. **Regulatory Rule Juxtaposition:**
     - For personal data processing (identity, contact details, logs), apply GDPR Operational Objectives (`PO-D-XX.Y-NNN`).
     - For software components, endpoints, storage, and interfaces, apply CRA Operational Objectives (`SO-D-XX.Y-NNN`).
     - For overall architectural behavior, apply Engineering Principles (`PRIN-ENG-01` to `PRIN-ENG-07`).
  4. **Exhaustive Coverage Matrix (mandatory output):** **every** Phase 2 objective (`PO-`/`SO-` — all of them) and every `PRIN-ENG-*` principle receives an explicit verdict against the functional model: **applies** (naming the functional carrier `R...`/`{U.C. ...}` and the **skill** from `baseline/skills/` used as the analysis lens) or **no functional carrier** (a recorded decision: organizational/process control per ADR-002, design guidance, or Phase 4 scope). No objective may be left unmapped — this matrix is what makes the synthesis reviewable, and it is what the client sees in the Step 3 rounds. Stored per case as `part1_security_privacy/synthesis_rounds/OBJECTIVE_MAPPING.md`.
- **Result:** Cross-cutting Traceability Matrix linking `R...` and `{U.C. ...}` to `PO-*`, `SO-*`, and `PRIN-ENG-*`, plus the Exhaustive Coverage Matrix covering 100% of the objective set. Asset and trust-boundary statements are kept here — they drive proposal derivation and later seed Phase 3 Part 2 (ADR-006). Formal threat modeling is **out of Part 1 scope** (it lives in Part 2).

### Step 3: Iterative Synthesis & Risk-Acceptance Rounds
- **Goal:** Negotiate the synthesized constraints with the client until the risk posture converges — no constraint enters the baseline without an explicit client decision (ADR-005).
- **Process (per round):**
  1. **Formulate candidate proposals** from the juxtaposition matrix using EARS sentence templates. Each proposal carries: the EARS constraint, the **risk it addresses**, its **altitude level** (L2/L3, with the Specificity Matching check — guidelines §2.5), an unambiguous **Volere Fit Criterion**, an empirical **Verification Method** (`TEST`, `INSPECT`, `DEMONSTRATE`, `ANALYZE`), and its full regulatory chain (`regulation article → Phase 2 rule → PRIN-ENG → candidate anchor`).
     - Security & privacy requirements continue the existing `RN` numbering (e.g. `RN9` onwards, after the base NFR table), with the regulatory driver carried as data — never as an ID prefix. CRA-derived: integrity, authentication, access control, audit, cryptography, vulnerability management. GDPR-derived: consent tracking, data minimization, right to erasure, purpose limitation, subject export.
     - **Anchor integrity:** the chain's control anchors must belong to the **published control set of the cited objective** (final column of the Phase 2 deliverable — the controls that objective already maps to). An anchor outside that set requires an explicit rationale and a W4 admission (ADR-001); anchors are never chosen ad hoc. The proposal cites the objective's published set as context, so the client can see which controls the requirement is built from — requirements are thereby informed by the existing control mapping without prescribing any technology.
  2. **Present the round** to the client stakeholders.
  3. **Record the client verdict per item** in the round documentation (the part1_security_privacy/synthesis_rounds notes): **Accept** · **Reject** (= explicit risk acceptance — the item remains recorded as accepted-by-decision, never silently dropped) · **Adjust** (wording, level, or scope; re-proposed next round).
  4. **Iterate** until convergence: a round with no new rejections, or an explicit client decision to close.
- **Result:** The **accepted constraint set** plus a fully traced round documentation. No `Doc01`/`Doc02` version evolves before convergence.

### Step 4: Control Identification & Selection
- **Goal:** Select the best-matching controls for every accepted constraint, completing the derivation chain `regulation → article → objective → requirement → control` as a deliberate act.
- **Process:**
  1. For each accepted item, identify candidate controls in `baseline/CONTROLS/` (enforced: NIST CSF 2.0, PF 1.1, AI RMF; advisory referentials per ADR-001 tiers).
  2. Copy anchors only from pre-verified surfaces (module anchor blocks, requirement YAML keys, the `MAPPINGS/sr_control_mappings/` store) — never re-derive (rules R2/R2b).
  3. Record the selection rationale per item in the round documentation: which control, from which referential/tier, and why it is the best fit.
- **Result:** The accepted set carrying its selected control anchors, ready for absorption.

### Step 5: Absorption & Traceability Weaving (V1)
- **Goal:** Embed security and privacy constraints into the functional model without disrupting functional purity.
- **Process:**
  1. **Update Use Cases (`Doc02` in V1):**
     - Add **Security Preconditions** (e.g., *Actor must possess an authenticated, valid session token authorized for the target tenant*).
     - Add **Cockburn Extensions (Alternative Flows)** for accepted security behavior (e.g., *3a. Invalid credentials provided: System increments failure counter, logs event, and rejects authentication without indicating which field failed*).
     - Add **Minimal Guarantees** to Postconditions (e.g., *Minimal Guarantee: No unauthorized data modification occurs; all access rejections are recorded in immutable audit logs*).
     - Add cross-reference tags to the corresponding security & privacy NFR cards (`RN9` onwards).
  2. **Update Functional Cards (`Doc01` in V1):**
     - Absorb each applicable NFR into its `R<n.m>` card as a **`Security & Privacy Constraints:` row** carrying the full `regulation article → Phase 2 rule → PRIN-ENG → control anchor` chain; keep cross-cutting NFRs standalone in the Quality Attributes table.
     - Add security and privacy dependency references to the `Dependencies` block of individual requirement cards.
- **Result:** Updated `part1_security_privacy/v1_security_privacy_synthesis/` containing augmented `Doc01` and `Doc02`, plus the analysis dossier.

### Step 5b: Functional Refinement Pass (V1 Functional Evolution)
- **Goal:** Let the synthesis legitimately evolve the functional model where it revealed genuine gaps — without corrupting V0 and without re-opening elicitation. Refinement items (D1 derived requirements, D2 refinements, D3 re-prioritizations) **enter the Step 3 round cycle as proposals** before absorption — the client accepts or rejects them like any other constraint.
- **Rationale:** Freezing V0 protects elicitation from premature security pre-baking, not functional progress. Security and privacy synthesis routinely exposes user-visible functionality that pure business elicitation could not see (e.g., a brute-force lockout creates the new user goal of recovering a locked account; irreversible erasure creates the obligation to offer a final export). A V1 that only appends constraint rows leaves those gaps undiscovered until implementation.
- **Allowed change types (exhaustive taxonomy):**
  - **D1 — Derived requirement:** an obligation (`RN` / `PO-` / `SO-` / regulation article) requires user-visible, Cockburn Sea-Level functionality not covered by any V0 card. Adds a new card continuing the canonical package numbering (`Rn.x`) and generates the matching PUC and fully dressed use case in `Doc02`. All R13 standards apply (active verb, technology neutrality, company-scale discipline).
  - **D2 — Description refinement:** the synthesis reveals ambiguity or omission in a V0 card's `Description` that prevents an absorbed constraint from binding. Rewrites only the `Description` (ID, origin, and scope preserved); targeted use cases gain steps or extensions — their Main Success Scenario is otherwise preserved.
  - **D3 — Priority re-evaluation:** a confirmed regulation converts a MoSCoW priority (typically `Should`/`Could` → `Must`). Requires the regulatory driver (article + Phase 2 objective) cited in the round documentation; summary table, card, and traceability matrix are updated together.
  - **D4 — Card split:** distinct security surfaces within one V0 card demand separate lifecycle or priority. Highest ceremony; old→new renumbering is recorded; use only when D1–D3 demonstrably cannot express the change.
- **Prohibited:** deleting or silently shrinking V0 scope; inventing functionality without a traceable driver; technology leakage in any new or refined text; clam-level derived cards.
- **Change Register (mandatory):** every functional change — including `evaluated, no change` rows — is recorded as `type → from/to → driving RN/PO/SO/article → rationale` in the analysis dossier (`STEP5_FUNCTIONAL_EVOLUTION_REGISTER.md`), and the V1 document's Version History documents the pass in one row.
- **Result:** An evolved V1 whose functional set is a registered, traceable refinement of V0; `part1_security_privacy/v0_functional_baseline/` untouched.

### Objective Fulfillment Record & the Organizational Lane (ADR-007 / ADR-008)

- **Fulfillment semantics (ADR-007):** a coverage verdict is a fulfillment claim, not a bookkeeping link. One EARS condition→response may carry several Phase 2 objectives only under the **congruence rule** — every cited objective must be satisfied by that same condition→response; identical control-anchor sets never evidence demand equivalence. An objective is **fully covered** only when the union of its carriers' Volere fit criteria reconstitutes the objective's Phase 2 Verification Criteria and every statement leg is carried, out-of-scale-recorded (with warrant), or explicitly carved out. The coverage matrix (`part1_security_privacy/synthesis_rounds/OBJECTIVE_MAPPING.md`, `VC discharge` column) is the authoritative discharge graph; delivered card chains cite primary drivers only. Re-anchoring a driver re-opens the wording/fit-criterion check — wording is never grandfathered across a driver swap. Round proposals carry a **discharge statement**.
- **Verdict vocabulary:** `Fully covered` / `Partially covered (functional leg + explicit carve-out)` / `No functional carrier (organizational)` / `Design guidance` / `N/A`.
- **Organizational lane (ADR-008):** uncarried PROCESS/CAPABILITY legs route to `part1_security_privacy/Doc03_Organizational_Requirements.md` in this folder — EARS with organizational subject (`The organization shall …`), Volere fit criterion, `INSPECT`/`DEMONSTRATE`/`ANALYZE` method, owner from the Phase 2 Governance & Stakeholder Matrix, IDs `ORG-D-XX.Y-NNN`, chain terminating in organizational anchors (NIST CSF 2.0 GOVERN; advisory ISO 27001 A.5.x / ENISA NIS2 / BSI OPS per R2b). Doc03 content enters through the same round cycle and is covered by the Part 1 Exit Gate (G1 extends to the organizational mapping).

### Phase 3 Part 2 (Gated): Threat & Risk Analysis
- **Goal:** Model threats formally — STRIDE/LINDDUN, attack-surface analysis, abuse scenarios — over the **accepted, control-informed baseline**, and maintain the case risk register (treat / accept / defer, with rationale).
- **Location:** `part2_threat_risk/` inside the Phase 3 folder; outputs carry `TM-D-XX.Y-NNN` IDs (ADR-006).
- **Trigger:** the **Part 1 Exit Gate (G1–G6)** below, plus the researcher's order to launch.
- **Scope boundary:** Part 1 performs **zero formal threat modeling**. Asset identification and trust-boundary statements (Step 2) remain in Part 1 and seed Part 2. Use-case security extensions describe *accepted security behavior*, not threat models.
- **Contract:** ADR-006 — Fase 3 [Part 1 Security & Compliance + Part 2 Threat & Risk] → **Fase 4 Verification & Implementation** (the former "Fase 5"; ADR-005's separate-Fase-4 placement is superseded).

### Part 1 Exit Gate (Critérios de Paragem)

Part 2 launches only when every criterion is **GREEN** and evidenced in the transition dossier (`analysis_v<N>_to_v<N+1>/README.md`):

| # | Criterion | Evidence surface |
|---|---|---|
| **G1** | Exhaustive mapping 100% verdicted — every Phase 2 objective and every principle placed, zero silent/pending | `part1_security_privacy/synthesis_rounds/OBJECTIVE_MAPPING.md` totals + `PRINCIPLE_MAPPING.md` |
| **G2** | Rounds converged — zero open verdicts; every rejection recorded as an explicit risk acceptance | `part1_security_privacy/synthesis_rounds/ROUND<n>_REGISTER.md` |
| **G3** | Control selection complete — every accepted constraint carries selected anchors from pre-verified surfaces, within published sets | register §3 |
| **G4** | Deliverables at the current version — Phase 3 Quality Checklist (§6) green; `doc_lint.py --strict` = 0 | version folder + lint run |
| **G5** | Sufficiency assessment produced — per-regulation compliance verdict + security verdict + explicit residual list | `part1_security_privacy/synthesis_rounds/SUFFICIENCY_ASSESSMENT.md` |
| **G6** | Transition dossier complete — steps documented like `part1_security_privacy/analysis_v0_to_v1/` | `analysis_v<N>_to_v<N+1>/` |

---

## 4. Version Evolution & Artifact Directory Architecture

To ensure strict configuration management and prevent confusing mixed revisions, Phase 3 is organised in its two parts (ADR-006) and, inside Part 1, in versioned folders:

```text
cases/Case_01_TinyTask_SaaS/03_PHASE3_SPEC/
├── README.md                                    # Master Phase 3 Navigation & Executive Index
├── PHASE3_PROCESS_AND_METHODOLOGY.md            # (This file) Complete normative methodology manual
│
├── part1_security_privacy/                      # [PART 1] Security & Compliance — versioned baseline + rounds
│   ├── Doc01_Requirements_Elicitation_and_PUC.md# Active Doc01 (working copy, synced to the current version folder)
│   ├── Doc02_System_Use_Cases.md                # Active Doc02 (working copy, synced to the current version folder)
│   │
│   ├── v0_functional_baseline/                  # [VERSION 0] Locked Pure Functional Baseline
│   │   ├── README.md                            # V0 Scope, Rationale, and Architecture
│   │   ├── Doc01_Requirements_Elicitation_and_PUC.md
│   │   └── Doc02_System_Use_Cases.md
│   │
│   ├── v1_security_privacy_synthesis/           # [VERSION 1] Synthesized & functionally evolved baseline (APPROVED)
│   │   ├── README.md                            # V1 Synthesis Scope, absorbed constraints, refinement pass
│   │   ├── Doc01_Requirements_Elicitation_and_PUC.md
│   │   └── Doc02_System_Use_Cases.md
│   │
│   ├── v2_security_privacy_synthesis/           # [VERSION 2] Round-1 convergence (APPROVED, ACTIVE)
│   │   ├── README.md                            # V2 Scope, re-anchored chains, new constraints, round register
│   │   ├── Doc01_Requirements_Elicitation_and_PUC.md
│   │   └── Doc02_System_Use_Cases.md
│   │
│   ├── analysis_v0_to_v1/                       # STEP1-STEP5 dossiers + V0/V1/V2 analysis tables
│   │   ├── README.md
│   │   ├── STEP1_V0_FUNCTIONAL_AUDIT_AND_BOUNDARY_ANALYSIS.md
│   │   ├── STEP2_REGULATORY_CROSS_CUTTING_ANALYSIS.md
│   │   ├── STEP3_EARS_REQUIREMENT_FORMULATION_AND_FIT_CRITERIA.md
│   │   ├── STEP4_FUNCTIONAL_AUGMENTATION_AND_TRACEABILITY_WEAVING.md
│   │   ├── STEP5_FUNCTIONAL_EVOLUTION_REGISTER.md
│   │   └── V0_V1_V2_ANALYSIS_TABLES.md
│   │
│   ├── analysis_v1_to_v2/                       # [V1 → V2 TRANSITION] Round-2 dossier + Part 1 Exit Gate record
│   │   ├── README.md
│   │   └── STEP1..STEP5
│   │
│   └── synthesis_rounds/                        # [ROUND CYCLE] Objective/principle/UC mappings + round registers
│       ├── README.md
│       ├── OBJECTIVE_MAPPING.md
│       ├── PRINCIPLE_MAPPING.md
│       ├── UC_OBJECTIVE_CORRESPONDENCE.md
│       ├── ROUND1_REGISTER.md
│       ├── ROUND2_REGISTER.md
│       └── SUFFICIENCY_ASSESSMENT.md
│
└── part2_threat_risk/                           # [PART 2] Threat & Risk Analysis (entry gate: G1–G6, ADR-006)
    └── README.md
```

Top-level `Doc01`/`Doc02` inside `part1_security_privacy/` are the active working copies, synced to the current version folder (V2).

### Comparative Evolution Matrix

| Dimension | Version 0 (Functional Baseline) | Version 1/2 (Security & Privacy Synthesis) | Phase 3 Part 2 (Threat & Risk, gated) → Phase 4 (Verification / Impl.) |
|---|---|---|---|
| **Primary Focus** | What the business & user need to achieve | How the system protects assets & complies with law; functional gaps revealed by the synthesis are closed (Step 4b) | How the implementation is built and verified |
| **Input Sources** | Stakeholder goals, As-Is workflows, Product scope | V0 Functional Baseline + Phase 2 `PO-` and `SO-` | V1 Specification + Architecture Decisions |
| **Security Controls** | Zero (strictly excluded) | Fully specified via EARS (security & privacy NFRs `RN9`+) | Implemented as code, tests, CI/CD gates |
| **Use Case Content** | Main Success Scenario (Sea-Level) | MSS + Security Preconditions + Security Extensions + derived use cases (D1) | Concrete UI/API procedural execution scripts |
| **Traceability** | Business Event -> Requirement -> PUC -> Use Case | Phase 2 Rules <-> Functional Scope <-> Security Reqs <-> Functional Change Register | Specification <-> Test Cases <-> Code Units |
| **Technology Neutrality**| Absolute (zero vendors, frameworks, protocols)| Absolute (pure functional security constraints) | Concrete technology stack selections |
| **Threat Modeling** | Zero (deferred by design) | Zero — assets & trust boundaries mapped, ready to seed Part 2 | Part 2: STRIDE/LINDDUN + risk register over the accepted baseline |

---

## 5. Practical Guidelines & Anti-Pattern Catalog

To maintain the highest professional standard of requirements engineering, authors and agents must avoid the 8 canonical anti-patterns documented below:

### 1. The Pre-Baked Security/Privacy Trap
- **Anti-Pattern:** Writing *"User enters password which is encrypted using Argon2id"* in a functional requirement card.
- **Remedy:** Keep functional cards focused on the business functionality (*"Authenticate User Identity"*). Specify the cryptographic strength and algorithm constraints in the card's **`Security & Privacy Constraints:` row** under the absorbed security & privacy NFR IDs (or the Quality Attributes table for cross-cutting NFRs).

### 2. The Technology Leakage Trap
- **Anti-Pattern:** Writing *"Store task records in PostgreSQL database hosted in AWS Frankfurt"*.
- **Remedy:** Use technology-neutral conceptual designations: *"Internal Application Database"*, *"Encrypted Relational Storage"*.

### 3. The Clam-Level Decomposition Trap
- **Anti-Pattern:** Creating separate requirement cards for *"Click Submit Button"*, *"Validate Email Regex"*, or *"Display Error Banner"*.
- **Remedy:** Maintain Cockburn's Sea-Level granularity. Group these micro-actions into a single meaningful business transaction (*"Register Organization Account"*).

### 4. The Artificial Chaining Trap
- **Anti-Pattern:** Populating `Preceding Requirements` sequentially so that every card depends on the previous one.
- **Remedy:** Leave `Preceding Requirements` empty by default. Only record true operational prerequisites (e.g., you cannot log billable hours on a project before the project workspace exists).

### 5. The Phantom Restriction Trap
- **Anti-Pattern:** Inventing arbitrary narrative restrictions for every cell in the MoSCoW summary table.
- **Remedy:** Leave restrictions empty by default. Only record genuine business constraints (e.g., regulatory deadlines or contractual limits).

### 6. The Pseudo-Origin Trap
- **Anti-Pattern:** Listing internal software modules as requirement origins (e.g., *"Origin: TinyTask / User Module"*).
- **Remedy:** State the real business event, stakeholder, or operational intake (e.g., *"Founder Business Case & Multi-Tenant Onboarding Operational Intake"*).

### 7. The Passive Nominalization Trap
- **Anti-Pattern:** Using noun phrases for titles (e.g., *"User Account Management"*, *"Project Metadata Configuration"*).
- **Remedy:** Use active verb conjugations in the infinitive (e.g., *"Manage User Accounts"*, *"Configure Project Metadata"*).

### 8. The Vague Adjective Trap
- **Anti-Pattern:** Stating that the system must be *"fast"*, *"secure"*, *"intuitive"*, or *"reliable"*.
- **Remedy:** Use Volere Fit Criteria and EARS templates with testable, verifiable assertions (e.g., verifying that stored credentials cannot be recovered from any stored representation, or that unauthenticated access requests fail closed).

### 9. The Premature Solution Design & Over-Specific Parameter Trap
- **Anti-Pattern:** Prescribing arbitrary low-level operational numbers (*"30-minute idle session timeout"*, *"100 req/min rate limit"*, *"128-bit entropy"*, *"salt >= 16 bytes"*, *"export within 24 hours"*) into Phase 3 non-functional requirements.
- **Remedy:** Maintain high-level control abstraction. Non-functional requirements must follow the chain `Regulation → Article/Clause → Control Framework (NIST CSF 2.0 / NIST PF 1.1 / ISO) → High-Level Control Objective`. Define the defensive boundary and control state at high level; reserve fine-grained operational parameterization and algorithm tuning for Phase 4 (Verification & Implementation).

---

## 6. Phase 3 Quality Checklist (Verification Gate)

Before declaring Phase 3 complete, verify that:
- [ ] **V0 Functional Integrity:** `part1_security_privacy/v0_functional_baseline/` contains only pure functional requirements and use cases, with zero pre-baked security or vendor names.
- [ ] **Granularity Standard:** Every use case is at Cockburn Sea-Level (Level 1). Zero clam-level UI sequences.
- [ ] **Verbal Phrasing:** 100% of requirement titles, sub-requirements, and use case names use active verbs in the infinitive.
- [ ] **EARS Compliance:** 100% of security and privacy NFRs (`RN9` onwards) follow the EARS syntax templates.
- [ ] **High-Level Control Abstraction:** 100% of security and privacy NFRs express high-level control objectives anchored in regulatory clauses and NIST/ISO controls, without premature operational parameters.
- [ ] **Functional Evolution Control:** Every V1 functional change is classified in the D1–D4 taxonomy and recorded in the Functional Evolution Register with its `RN`/`PO-`/`SO-`/article driver; `part1_security_privacy/v0_functional_baseline/` files are untouched.
- [ ] **Specificity Matching:** Every security & privacy NFR's wording stays within the altitude warranted by its cited chain (L0–L4 scale, warrants W1–W5 — guidelines §2.5); zero L4 vocabulary anywhere in Phase 3 deliverables.
- [ ] **Exhaustive Mapping:** 100% of Phase 2 objectives and principles carry an explicit verdict in the Objective Mapping (applies — with skill — or no functional carrier); zero unmapped objectives.
- [ ] **Risk-Acceptance Control:** Every synthesized constraint's client verdict (Accept / Reject = risk accepted / Adjust) is recorded in the round documentation with round trace; no baseline version evolves before round convergence.
- [ ] **Control Selection:** Every accepted constraint carries its selected control anchor copied from the pre-verified surfaces (module anchor blocks, requirement YAML keys, mapping store).
- [ ] **Phase Boundary (Threats):** Zero formal threat modeling (STRIDE/LINDDUN, attack-scenario catalogs) inside Part 1 deliverables — confined to Phase 3 Part 2 (`part2_threat_risk/`, ADR-006).
- [ ] **Part 1 Exit Gate:** G1–G6 all GREEN and evidenced in the transition dossier before Part 2 starts (§3).
- [ ] **Empirical Verification:** Every security requirement defines an unambiguous Fit Criterion and specifies one of the four ISO 29148 verification methods (`TEST`, `INSPECT`, `DEMONSTRATE`, `ANALYZE`).
- [ ] **Bidirectional Traceability:** A complete traceability matrix connects Phase 2 `PO-` and `SO-` objectives to functional requirements `R...`, use cases `{U.C. ...}`, and the security & privacy NFRs (`RN9` onwards).
- [ ] **Tooling Integrity:** Running `python scripts/doc_lint.py --strict` passes with 0 findings across the entire repository.


> **Absorption rule (2026-09-23):** the standalone security/privacy NFR catalog (former `Doc03`) is dissolved; NFRs are absorbed into the relevant R<n.m> cards with the full regulation → Phase 2 → PRIN-ENG → control anchor chain.
