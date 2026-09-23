# Phase 3 Functional Specification Guidelines (GPTools E1.1 / E1.2 Standard)

> **Scope:** Mandatory rules and structural blueprint for authoring AEGIS Phase 3 pure functional baseline deliverables (`Doc01` and `Doc02`).
> **Authority:** Derived from `AGENTS.md` Rule R13 and the reference project standard (`E1.1 – GPTools_ModeloASIS_TOBE V2.0` and `E1.2 – GPTools_AnáliseRequisitos_CasosDeUso_V4.0`).

---

## 1. Core Principles

1. **Strict Technology Neutrality:**
   - Under **NO circumstances** may any requirement, table, card, or description mention specific technology products, database engines, software frameworks, cloud vendors, or protocols.
   - **Banned examples:** "PostgreSQL", "MySQL", "MongoDB", "Dotnet Core", "Angular", "React", "Vue", "Stripe", "AWS S3", "WebSockets", "SAML 2.0", "Redis".
   - **Mandatory functional equivalents:** 
     - Database $\rightarrow$ `Internal Application Database` or leave empty (`—`)
     - File storage $\rightarrow$ `File Storage Service` or `Attachment Storage`
     - Billing/Payments $\rightarrow$ `External Payment Gateway` or `Payment Processing Service`
     - Notifications $\rightarrow$ `Transactional Email Service` or `Notification Service`
     - Real-time communication $\rightarrow$ `Real-time messaging channel` or `Real-time push`

2. **Action Verb Phrasing (No Nominalizations):**
   - All requirement group titles (`R1`, `R2`, ...), sub-requirement names (`R1.1`, `R1.2`, ...), and use case names (`{U.C. 1}`, `{U.C. 1.1}`, ...) **MUST** use active verbs in the infinitive/imperative form.
   - **Correct:** "Manage User Accounts and Identity", "Manage Projects", "Create and Assign Tasks", "Gerir Tarefas".
   - **Prohibited:** "User Account and Identity Management", "Project Lifecycle", "Task Creation and Attribution", "Gestão de Tarefas".

3. **Pure Functional Baseline (Zero Pre-Baked Security/Privacy):**
   - The functional specification represents pure business and user operational capabilities.
   - Never pre-bake security, cryptography, or privacy mechanisms (such as Argon2, TLS, AES encryption, GDPR articles, or audit hash chains) into functional cards. Security and privacy controls belong strictly to the downstream AEGIS Phase 3 synthesis layer driven by Phase 2 Operational Objectives.

4. **Company Scale Discipline (No Enterprise Inflation):**
   - Tailor the functional scope strictly to the target organization's operational profile and size (e.g., an 8-person micro-SaaS does not get enterprise SSO federation, multi-tenant billing splits, or complex custom permission matrix editors).

---

## 2. Deliverable Doc01: Requirements Elicitation & PUC (E1.1 Standard)

### 2.1 Structural Blueprint
- **Resumo / Executive Summary**
- **Índice / Table of Contents**
- **Part I – Scope:**
  1. Objective
  2. Problem Description
  3. Product Position Statement
  4. Expected Impact
  5. Key Features
  6. Stakeholders (Table 1)
  7. System Users (Table 2)
  8. Constraints
- **Part II – As-Is:**
  1. Business Roles in Context
  2. Workflow Processes for Work Management:
     - Manual data tables with exact 3 columns: `['Data Field', 'Data Type', 'Mandatory']` (or `['Dados', 'Tipo de Dados', 'Obrigatoriedade']`).
  3. IT Support (unstructured tools, spreadsheets, emails)
- **Part III – To-Be:**
  1. Customer Initial Expectations (Table: `['Initial Expectations', 'Description']`)
  2. Functional and Non-Functional Requirements:
     - 2.1 Actors (Table: `['Actor', 'Description']`)
     - 2.2 Functional Requirements:
       - 2.2.1 MoSCoW Prioritization Method
       - 2.2.2 Summary Table of Functional Requirements:
         - Columns: `['ID', 'ID', 'Requirement', 'Priority', 'Restrictions']`
         - **Discipline for Restrictions:** The `Restrictions` column is **empty by default** for most requirements (matching GPTools Table 20). Only record genuine business constraints; never force synthetic text into every cell.
       - 2.2.3 Detailed Specification Cards for Functional Requirements (7-row format below)
     - 2.3 Non-Functional Requirements:
       - Table: `['ID', 'Requirement', 'Priority', 'Type']`
  3. Business Product Use Cases (PUC) Definition:
     - Summary Table: `['PUC', 'PUC Name', 'Actors / Users', 'Input and Output']`
  4. System Use Case Model:
     - Level-0 System Use Case Diagram (Mermaid)
     - Level-1 System Use Cases descriptions
- **Bibliography**
- **Version History**

### 2.2 Exact 7-Row Single-Column Requirement Card Format

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

**Field Rules:**
- **ID & Name:** Must start with an active verb.
- **Information Systems / Databases:** Technology-neutral (e.g. `Internal Application Database`) or empty (`—`). Never cite vendor engines.
- **Preceding Requirements:** **Empty by default**. Only populate if a genuine, strict business prerequisite dependency exists.
- **Identified Problems:** **Empty by default** (or `—`), matching GPTools E1.1.

---

## 3. Deliverable Doc02: System Use Cases (E1.2 Standard)

### 3.1 Structural Blueprint
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
    - `{U.C. 1}` to `{U.C. N}` Macro Use Cases
    - Level-1 System Use Cases (`{U.C.n.m}`)
- **5. Non-Functional Requirements**
- **6. Conclusions**
- **7. Bibliography**
- **Version History**

### 3.2 Granularity Rule (No Leaf Nodes)
- Refinement stops strictly at **Level 1** (`{U.C.n.m}`).
- **Zero leaf nodes** (`{U.C.n.m.k}`).
- **Zero procedural execution step sequences** (Step 1, Step 2, etc.) in the functional baseline.
- Focus strictly on actors, business intent, input payloads, and output deliverables.
