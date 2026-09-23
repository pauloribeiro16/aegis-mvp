# Phase 3 Functional Specification Guidelines (GPTools E1.1 / E1.2 Standard)

> **Scope:** Theoretical foundations, mandatory rules, and operational process for authoring AEGIS Phase 3 pure functional baseline deliverables (`Doc01` and `Doc02`).
> **Authority:** Derived from `AGENTS.md` Rule R13, the reference project standard (`E1.1 – GPTools_ModeloASIS_TOBE V2.0` and `E1.2 – GPTools_AnáliseRequisitos_CasosDeUso_V4.0`), and foundational software requirements engineering literature (Robertson & Robertson, Cockburn, Wiegers & Beatty, Leffingwell & Widrig).

---

## 1. Theoretical & Methodological Foundations

The specification of pure functional requirements and use cases within AEGIS Phase 3 is not an arbitrary drafting exercise. It is grounded in established requirements engineering literature:

### 1.1 The Volere Requirements Process (Robertson & Robertson, 2012)
Suzanne and James Robertson's *Mastering the Requirements Process: Getting Requirements Right* (3rd ed.) provides the core methodology for deriving, framing, and structuring functional specifications:

1. **Project Blastoff & Context of Work:**
   - Establishes the operational boundary of the organization before designing software.
   - The *Context of Work Diagram* identifies the adjacent systems, business stakeholders, and information flows entering and exiting the organization.
2. **Event-Driven Elicitation (Business Events $\rightarrow$ Business Use Cases):**
   - Work does not occur randomly; it is triggered by **Business Events** originating from external actors (e.g., customer registers, member uploads deliverable, billing cycle arrives).
   - Each business event triggers a **Business Use Case (BUC)** within the operational environment.
3. **Product Boundary & Product Use Cases (PUC):**
   - The **Product Use Case (PUC)** represents the specific automated partition of the business use case that the planned software application will perform.
   - A PUC is strictly delimited by its input data flows (`(in)`) and output data deliverables (`(out)`).
4. **The Requirement Snow Card & Fit Criteria:**
   - Volere formalizes atomic requirements into standardized specification shells (*Snow Cards*).
   - Every requirement must have a clear behavioral scope, origin, interfaces, and testable **Fit Criterion** (how to verify objectively whether a delivered capability satisfies the requirement).
5. **The Quality Gateway:**
   - Every elicited requirement must pass a rigorous filter before entering the baseline:
     - Is it unambiguous?
     - Is it strictly functional (free from implementation and technological design)?
     - Is it atomic and testable?
     - Is it necessary and scoped to real organizational scale?

### 1.2 Goal-Driven Use Case Architecture (Cockburn, 2000)
Alistair Cockburn's *Writing Effective Use Cases* establishes the precision levels and boundaries of system use cases:

1. **Goal Altitude Hierarchy:**
   - **Sky / Cloud Level (Summary — Level 0):** High-level organizational goals or core capability groupings (e.g., "Manage Tasks", "Manage Projects").
   - **Sea Level (User Goal — Level 1):** A discrete operational task undertaken by a single primary actor in a single sitting to achieve a meaningful business outcome (e.g., "Create and Assign Task", "Transition Task State").
   - **Underwater / Clam Level (Sub-function — Leaf Nodes / Level 2+):** Procedural, micro-interaction UI details (e.g., "Click submit button", "Select dropdown item 3", "Validate string length").
2. **The AEGIS Level-1 Scoping Boundary:**
   - In accordance with the GPTools standard and Cockburn's sea-level principle, AEGIS functional use cases **anchor strictly at Level 1 (`{U.C.n.m}`)**.
   - **Zero leaf nodes (`{U.C.n.m.k}`) and zero step-by-step procedural execution sequences** are written in the functional baseline. Micro-steps and procedural steps belong to interactive design and UI prototyping, not to the baseline functional architecture.

### 1.3 Requirements Quality Attributes (Wiegers & Beatty, 2013)
Karl Wiegers and Joy Beatty's *Software Requirements* (3rd ed.) defines the essential quality attributes enforced in our specification:
- **Complete:** Each card contains all necessary operational properties (origin, interfaces, dependencies).
- **Correct:** Accurately reflects stakeholder needs extracted from the Intake Form without invention.
- **Feasible:** Realistic within the operational and human capacity of the organization.
- **Necessary:** Directly traces to customer expectations or business workflow viability.
- **Prioritized:** Formally classified via MoSCoW based on essential business viability.
- **Unambiguous:** Expressed in direct active voice with universal business meaning.
- **Verifiable:** Formulated so that functional acceptance testing can yield a binary pass/fail result.

---

## 2. Non-Negotiable Core Principles

### 2.1 Strict Technology Neutrality (ABSOLUTE BAN on Technologies)
Under **NO circumstances** may any requirement, table, card, or description mention specific technology products, database engines, software frameworks, cloud vendors, or technical protocols:
- **Banned Technical Terms:**
  - Database engines: `PostgreSQL`, `MySQL`, `MongoDB`, `SQLite`, `Oracle`, `Redis`.
  - Frameworks & libraries: `Dotnet`, `Dotnet Core`, `Angular`, `React`, `Vue`, `Express`, `Spring`.
  - Cloud providers & vendors: `AWS`, `AWS S3`, `Google Cloud`, `Azure`, `Stripe`, `Sendgrid`, `Twilio`.
  - Protocols & standards: `WebSockets`, `SAML 2.0`, `OIDC`, `REST`, `GraphQL`, `gRPC`.
- **Mandatory Functional Terms:**
  - Database $\rightarrow$ `Internal Application Database` or leave empty (`—`).
  - File storage $\rightarrow$ `File Storage Service` or `Attachment Storage`.
  - Payment/Billing $\rightarrow$ `External Payment Gateway` or `Payment Processing Service`.
  - Notifications/Email $\rightarrow$ `Transactional Email Service` or `Notification / Email Service`.
  - Real-time communication $\rightarrow$ `Real-Time Message Stream` or `Real-Time Push Channel`.

### 2.2 Action Verb Phrasing (No Nominalizations)
All requirement group titles (`R1`, `R2`, ...), sub-requirement names (`R1.1`, `R1.2`, ...), and use case names (`{U.C. 1}`, `{U.C. 1.1}`, ...) **MUST** use active verbs in the infinitive/imperative form:
- **Correct Examples:**
  - "Manage User Accounts and Identity" (NOT "User Account and Identity Management")
  - "Manage Workspaces and Teams" (NOT "Workspace and Team Administration")
  - "Create and Assign Tasks" (NOT "Task Creation and Attribution")
  - "Manage Task States and Kanban Boards" (NOT "Task State Management")
  - "Upload and Manage Task Attachments" (NOT "Task Attachment Management")
  - "Collaborate via In-Task Comments" (NOT "In-Task Collaboration")
  - "Gerir Tarefas" (NOT "Gestão de Tarefas")

### 2.3 Pure Functional Baseline (Zero Pre-Baked Security/Privacy)
The functional specification represents pure business and user operational capabilities:
- **Never pre-bake security, cryptography, or privacy mechanisms** (such as Argon2, bcrypt, TLS 1.3, AES encryption, GDPR articles, audit hash chains, or presigned URLs) into functional cards.
- Security and privacy controls belong strictly to the downstream AEGIS Phase 3 synthesis layer driven by Phase 2 Operational Objectives and automated skills.

### 2.4 Company Scale Discipline (No Enterprise Scope Inflation)
Tailor the functional scope strictly to the target organization's operational profile and size:
- An 8-person micro-SaaS does not get enterprise SSO SAML/OIDC federation, multi-tenant billing splits, or complex custom permission matrix editors.
- Keep requirements lean, focused, and realistic for the company's real context from the Intake Form.

---

## 3. Deliverable Doc01: Requirements Elicitation & PUC (E1.1 Standard)

### 3.1 Structural Blueprint
Deliverable `Doc01` mirrors `E1.1 – GPTools_ModeloASIS_TOBE V2.0`:
- **Executive Summary / Resumo**
- **Table of Contents / Índice**
- **Part I – Scope:**
  1. Objective (Business mission of the product)
  2. Problem Description (Pain points of current operations)
  3. Product Position Statement (For / Who / The product is / That allows / Unlike / Our product distinguishes itself)
  4. Expected Impact (Measurable business outcomes)
  5. Key Features (Functional capability pillars)
  6. Stakeholders (Table 1: Stakeholder, Representatives, Role and Interest)
  7. System Users (Table 2: System User Role, Description and Responsibilities)
  8. Constraints (Operational, team size, and architectural constraints)
- **Part II – As-Is:**
  1. Business Roles in Context (Informal roles before system adoption)
  2. Workflow Processes for Work Management:
     - Detailed operational narrative of manual procedures.
     - Manual data tables with exact 3 columns: `['Data Field', 'Data Type', 'Mandatory']` (or `['Dados', 'Tipo de Dados', 'Obrigatoriedade']`).
  3. IT Support (Unstructured tools, spreadsheets, emails, shared drives)
- **Part III – To-Be:**
  1. Customer Initial Expectations (Table 8: `['Initial Expectations', 'Description']`)
  2. Functional and Non-Functional Requirements:
     - 2.1 Actors (Table 9: `['Actor', 'Description']`)
     - 2.2 Functional Requirements:
       - 2.2.1 MoSCoW Prioritization Method
       - 2.2.2 Summary Table of Functional Requirements (Table 10: `['ID', 'ID', 'Requirement', 'Priority', 'Restrictions']`)
         - **Discipline for Restrictions:** The `Restrictions` column is **empty by default** for most requirements (matching GPTools Table 20). Only record genuine business constraints; never force synthetic text into every cell.
       - 2.2.3 Detailed Specification Cards for Functional Requirements (Exact 7-row single-column format below)
     - 2.3 Non-Functional Requirements (Table 11: `['ID', 'Requirement', 'Priority', 'Type']`)
  3. Business Product Use Cases (PUC) Definition (Table 12: `['PUC', 'PUC Name', 'Actors / Users', 'Input and Output']`)
  4. System Use Case Model:
     - Level-0 System Use Case Diagram (Mermaid)
     - Level-1 System Use Cases descriptions
- **Bibliography**
- **Version History**

---

### 3.2 Exact 7-Row Single-Column Requirement Card Anatomy

Every functional requirement card must follow this exact single-column markdown table structure:

```markdown
| Requirement |
|---|
| **ID:** R... **Name:** <Active Verb Phrase> |
| **Description:** ... |
| **Requirement Origin:** ... |
| **Interfaces:** ... |
| **Dependencies:**<br>• **Stakeholders:** ...<br>• **Data Sources:** ...<br>• **Extraction Periodicity:** on demand<br>• **Information Systems / Databases:** Internal Application Database<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must / Should / Could / Won't |
```

#### Detailed Derivation Rules for Each Card Row:

1. **Row 1 — `ID: R... Name: <Active Verb Phrase>`:**
   - Canonical hierarchical ID (`R1`, `R1.1`, `R1.2`, ...).
   - Name must start with an active verb (e.g., "Register user account with email verification", "Archive completed project to read-only state").
2. **Row 2 — `Description:`:**
   - Precise behavioral contract specifying what the system must perform from the user's perspective.
   - Follows the template: *"The system must allow [authorized actor] to [action/behavior], automatically [resulting system response or deliverable]."*
   - Written in active voice, free from jargon, unambiguous, and completely technology-neutral.
3. **Row 3 — `Requirement Origin:`:**
   - Traces the business origin of the requirement (e.g., "TinyTask SaaS / Identity Management", "TinyTask SaaS / Task Management", "TinyTask SaaS / Customer Billing").
4. **Row 4 — `Interfaces:`:**
   - Identifies the human users and external services crossing the boundary of this requirement (e.g., "Workspace Member, Workspace Admin", "Unauthenticated User and Notification / Email Service").
5. **Row 5 — `Dependencies:`:**
   - Structured sub-fields:
     - `Stakeholders:` Key business beneficiaries (e.g., "Executive Leadership, Team Contributors").
     - `Data Sources:` Operational origin of the data payload (e.g., "User Registration Form", "Task Card Details").
     - `Extraction Periodicity:` Operational tempo (e.g., "on demand", "daily").
     - `Information Systems / Databases:` Must be generic (`Internal Application Database`, `File Storage Service`) or empty (`—`). Never cite commercial engines.
     - `Preceding Requirements:` **Empty by default!** Only populate when a strict, hard business prerequisite exists between requirements.
6. **Row 6 — `Identified Problems:`:**
   - **Empty by default** (or `—`), matching GPTools E1.1. Used only to record known business ambiguities or unresolved process conflicts.
7. **Row 7 — `Priority:`:**
   - Strict MoSCoW classification: `Must`, `Should`, `Could`, or `Won't`.

---

## 4. Deliverable Doc02: System Use Cases (E1.2 Standard)

### 4.1 Structural Blueprint
Deliverable `Doc02` mirrors `E1.2 – GPTools_AnáliseRequisitos_CasosDeUso_V4.0`:
- **Executive Summary**
- **Table of Contents**
- **1. Introduction**
- **2. System Requirements Approach:**
  - 2.1 Volere Approach and Triangular Functional Decomposition
  - 2.2 Refinement Boundary (No Leaf Nodes)
  - 2.3 Non-Functional Requirements
- **3. Requirements Analysis:**
  - 3.1 Work Context Model (Mermaid Diagram)
  - 3.2 Summary Table of Product Use Cases (PUC)
- **4. Domain Application Use Cases:**
  - 4.1 System Actors
  - 4.2 System Use Cases:
    - `{U.C. 1}` to `{U.C. N}` Macro Use Cases (Level 0)
    - Level-1 System Use Cases (`{U.C.n.m}`)
- **5. Non-Functional Requirements**
- **6. Conclusions**
- **7. Bibliography**
- **Version History**

### 4.2 Use Case Granularity Rules (Cockburn Sea-Level Discipline)
1. **Refinement Stops at Level 1:**
   - Every use case must be expressed at **Level 1 (`{U.C.n.m}`)** — Cockburn's "User Goal / Sea Level".
2. **Absolute Ban on Leaf Nodes:**
   - Never decompose into `{U.C.n.m.k}`.
   - Never write step-by-step procedural execution sequences ("Step 1: User navigates to page; Step 2: User clicks input field; Step 3: ...").
3. **Use Case Narrative Structure:**
   - Each `{U.C.n.m}` describes:
     - The triggering primary actor.
     - The operational business intent.
     - The system's processing response and output deliverable.

---

## 5. Downstream Bridge: How AEGIS Evaluates Functional Requirements

A critical reason for maintaining this rigorous standard is that Phase 3 functional requirements serve as the **Anchor Canvas** for AEGIS security and privacy synthesis:

| Functional Card Property | Downstream AEGIS Evaluation & Synthesis Hook |
|---|---|
| **Interfaces (Actors & Services)** | Directly feeds **Skill 1 (Attack Surface Analysis)** and **Skill 2 (Trust Boundary Analysis)** to identify exposed endpoints and boundary crossings. |
| **Dependencies: Data Sources** | Directly feeds **Skill 4 (Data Minimization Analysis)** and **Skill 7 (Privacy by Design)** to scrutinize data fields against GDPR Art. 5 principles. |
| **Dependencies: Stakeholders & Roles** | Directly feeds **Skill 3 (Least Privilege Analysis)** to enforce RBAC authorization checks and prevent privilege escalation. |
| **Dependencies: Information Systems** | Informs architectural component placement and tenant isolation (multi-tenancy) in Phase 3 design. |
| **Requirement Description & Verb** | Forms the primary functional contract upon which security assertions (`RULE-*`) and security requirements (`REQ-D-XX.Y-NNN`) are synthesized. |
| **Identified Problems & Constraints** | Informs threat modeling and exception handling under **Skill 5 (Secure Defaults)** and **Skill 6 (Defensive Design)**. |

---

## 6. Authoring & Validation Checklist

Before declaring any Phase 3 functional baseline deliverable complete, verify:

- [ ] **Technology Check:** Run a text search for `PostgreSQL`, `MySQL`, `Dotnet`, `Angular`, `React`, `Stripe`, `AWS`, `S3`, `WebSockets`. Zero matches must be returned.
- [ ] **Verb Phrasing Check:** Verify that every requirement group (`R1`), sub-requirement (`R1.1`), and use case (`{U.C. 1.1}`) starts with an active verb in the infinitive/imperative.
- [ ] **Table Format Check:** Verify that each individual requirement card uses the exact 7-row single-column format with `| Requirement |` header.
- [ ] **Dependencies Check:** Verify that `Preceding Requirements:` is empty by default (>90% blank) and `Information Systems / Databases:` contains only technology-neutral terms.
- [ ] **Restrictions Check:** Verify that the `Restrictions` column in the MoSCoW summary table is empty by default.
- [ ] **Granularity Check:** Verify that `Doc02` contains zero leaf nodes (`{U.C.n.m.k}`) and zero procedural execution steps.
- [ ] **doc_lint Check:** Run `python scripts/doc_lint.py --strict` and ensure 0 findings are returned.
