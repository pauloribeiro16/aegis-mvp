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
   - Every requirement must have a clear behavioral scope, origin, interfaces, and testable **Fit Criterion** (how to verify objectively whether a delivered functionality satisfies the requirement).
5. **The Quality Gateway:**
   - Every elicited requirement must pass a rigorous filter before entering the baseline:
     - Is it unambiguous?
     - Is it strictly functional (free from implementation and technological design)?
     - Is it atomic and testable?
     - Is it necessary and scoped to real organizational scale?

### 1.2 Goal-Driven Use Case Architecture (Cockburn, 2000)
Alistair Cockburn's *Writing Effective Use Cases* establishes the precision levels and boundaries of system use cases:

1. **Goal Altitude Hierarchy:**
   - **Sky / Cloud Level (Summary — Level 0):** High-level organizational goals or core functional groupings (e.g., "Manage Tasks", "Manage Projects").
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

### 2.5 Specificity Matching (Altitude Control)

Specificity is not a virtue to maximize — it is a debt that must be **warranted**. When a stakeholder says *"the platform must authenticate users securely"* (vague), the specification may not answer with a concrete mechanism unless the anchored context descends first. Every statement's altitude is matched against its source: **output specificity ≤ source specificity + documented descents**. This is the general rule behind §2.1 (technology neutrality is its L4 extreme) and it binds every artifact in this guide — V0 cards, V1 absorbed constraints, derived requirements (§3.4), and use case flows.

**The specificity scale:**

| Level | Kind | Examples |
|---|---|---|
| **L0 — Property** | Qualitative value word | "secure", "reliable", "user-friendly" |
| **L1 — Goal / capability** | User or business goal (Cockburn Sea-Level, `AG-`) | "authenticate users", "export data" |
| **L2 — Verifiable constraint** | Technology-neutral behavioral rule, EARS-shaped, quantifiable — where `PO-`/`SO-` objectives and synthesized `RN` requirements belong | "the system shall deny authentication after 5 consecutive failed attempts" |
| **L3 — Mechanism category** | A family of implementations that constrains design | "salted one-way hashing", "webhook signature verification", "output encoding" |
| **L4 — Technology / implementation** | Named technology, protocol, library | "TLS 1.3", "Argon2id", "HttpOnly cookies" — **banned** (§2.1) |

**The matching rule:** a downstream statement may not exceed the specificity level of its source unless each level descent carries a **warrant** — a cited, dated document in the anchored context that itself descends:

| Warrant | Source | Example |
|---|---|---|
| **W1 — Source statement** | The input itself is already at that level | company input names a system; a stakeholder asks for a signature check |
| **W2 — Regulation verbatim** | The cited article's own text names the mechanism | GDPR Art. 32(1)(a) names "encryption" and "pseudonymisation" → authorizes L3 "encryption at rest", not "AES-256" |
| **W3 — Anchored objective / corpus module** | The Phase 2 objective or `regs/<REG>.md` requirement text descends | `SO-D-01.1-002` "state-of-the-art mechanisms" stays L2 — it does **not** authorize "salted" |
| **W4 — Admitted good practice** | A T2/T3 source per ADR-001 (conditional on ratification; ambiguity registry R2 = ceiling/minimum), cited tier + source + version | ENISA Art. 32 catalogue names the measure family |
| **W5 — Company statement** | The company input text itself descends | "we process payments via an external gateway" |

- **Quantitative precision is level-neutral but not warrant-free.** A number never causes a mechanism descent ("deny after 5 failed attempts" is L2, not L3), and verifiability demands measurable fit criteria (ISO 29148; Anti-Pattern 8) — but the *values themselves* must be derived from the regulation, a risk assessment, or a cited source, never invented (Anti-Pattern 11). Specificity without a warrant is unwarranted at every level, numeric or lexical.
- **One level at a time.** A chain that warrants L2 does not authorize L3 wording; each descent step cites its own warrant.
- **No warrant → stay at the source's level.** State the property or constraint; leave the mechanism open to Phase 4 / design. "This mechanism sounds right" is not a warrant.

- ✅ `**NFR-RN10**` named "Credential Confidentiality Protection (State of the Art)" when the chain ends at a state-of-the-art clause (L2 = warranted level).
- ❌ `**NFR-RN10**` named "Credential Hardening & **Salted** Hashing" when no anchored document mentions salt (unwarranted L2→L3 descent).
- ✅ "encrypted at rest" under GDPR Art. 32(1)(a) (W2 — the article names encryption).
- ❌ "AES-256-GCM at rest" anywhere in Phases 0–3 (L4; §2.1).
- ✅ "blocks authentication after 5 failed attempts" (quantified L2 fit criterion — no mechanism descent; the *value* must still carry a derivation warrant, Anti-Pattern 11).

**Composition with existing rules:** §2.1 is the L4 ban; Anti-Pattern 1 keeps security out of V0 (V1 absorbed constraints and §3.4-derived requirements obey *this* rule instead); Anti-Pattern 8 demands the quantitative fit criteria this rule explicitly does not restrict; **Anti-Pattern 11 is this rule's numeric twin** — it governs unwarranted *parameter values* while §2.5 governs unwarranted *mechanism vocabulary*. When a constraint genuinely needs an L3 category that only a good-practice source warrants, record it as `W4-pending` until ADR-001 is ratified — do not silently absorb general knowledge into the specification.

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
  5. Key Features (Functional pillars)
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

Every functional requirement card must follow this exact single-column markdown table structure. In the **V1 security & privacy synthesis**, an additional optional row — `Security & Privacy Constraints:` — is inserted between `Requirement Origin` and `Interfaces` (see §3.3); the pure functional baseline (V0) uses exactly these 7 rows:

```markdown
| Requirement |
|---|
| **ID:** R... **Name:** <Active Verb Phrase> |
| **Description:** ... |
| **Requirement Origin:** ... |
| **Security & Privacy Constraints:** ... |   <- V1 synthesis only (optional; see §3.3)
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
   - Traces the real business or stakeholder origin of the requirement (e.g., "Founders Business Case & Onboarding Workflow", "Team Lead Operational Intake", "Collaborator Sprint Feedback", "Customer Invoicing & Subscription Policy").
   - **Never cite self-referential internal system modules** (e.g., do NOT write "TinyTask SaaS / Identity Management" — see Anti-Pattern 6 in Section 7).
4. **Row 4 — `Interfaces:`**
   - The **concrete interaction surfaces** through which the requirement is exercised: user-facing screens, forms, panels, flows, and external system interfaces (e.g., "Registration screen; Login screen; Password recovery flow; Transactional email interface").
   - **Never a list of actors.** Actor names ("Workspace Admin", "Registered User") belong in the Actors table and in `Dependencies: Stakeholders`, not here — see Anti-Pattern 9 in Section 7.
5. **Row 5 — `Dependencies:`:**
   - Structured sub-fields:
     - `Stakeholders:` Key business beneficiaries (e.g., "Executive Leadership, Team Contributors").
     - `Data Sources:` Operational origin of the data payload, specific to what this requirement actually consumes (e.g., "Registration form submissions; Credential verification requests; Payment failure events").
     - `Extraction Periodicity:` The operational tempo this requirement genuinely runs at — vary it when behavior dictates: "on demand", "on event", "daily digest", "per recurrence schedule", "continuous". Do not default to "on demand" when the functionality is event- or schedule-driven.
     - `Information Systems / Databases:` The functionally-specific repository this requirement reads/writes, named by role ("Identity and Credential Store", "Internal Application Database (task state records)", "File Storage Service", "External Payment Gateway"). Never paste the same generic value into every card — see Anti-Pattern 10 in Section 7. Never cite commercial engines.
     - `Preceding Requirements:` **Empty by default!** Only populate when a strict, hard business prerequisite exists between requirements.
6. **Row 6 — `Identified Problems:`:**
   - **Empty by default** (or `—`), matching GPTools E1.1. Used only to record known business ambiguities or unresolved process conflicts.
7. **Row 7 — `Priority:`:**
   - Strict MoSCoW classification: `Must`, `Should`, `Could`, or `Won't`.

### 3.3 Card Field-Filling Standard (per-field rules, examples & anti-patterns)

This subsection is the **canonical filling guide** for every card row. Whenever a filling style is corrected — in review or in conversation — the correction is codified here in the same session, so filling is always reproduced the same way.

**Row `Description:`**
- ✅ "The system must allow prospective users to create an account with email verification, authenticate using valid credentials to establish an active session, and autonomously request password reset assistance via email."
- ❌ "Handles user management and auth flows." (nominalized, vague, no behavioral contract)

**Row `Requirement Origin:`**
- ✅ "Founders Business Case & User Onboarding Workflow"
- ❌ "TinyTask SaaS / Identity Management module" (self-referential — Anti-Pattern 6)

**Row `Security & Privacy Constraints:` (V1 synthesis only)**
- Purpose: carry the absorbed security/privacy NFRs with their full tracing chain, so nothing "falls from the sky".
- ✅ One condensed line per NFR, ids only:
  `**NFR-RN10** Credential Hardening & Salted Hashing — CRA Annex I Part I (2)(d)+(2)(j) → SO-D-02.1-002 → PRIN-ENG-04 → CSF PR.AA-03, PR.DS-01`
- **High-Level Control Abstraction Mandate:** NFRs must be expressed as **High-Level Control Objectives** anchored in the control referential (NIST CSF 2.0 / NIST PF 1.1 / ISO). They must **NEVER invent premature implementation parameters** (e.g., exact timeout minutes, request quotas, byte sizes, response latencies). Parameterization belongs to Phase 4 design (Anti-Pattern 11).
- Only NFRs **genuinely applicable to this card's function** (typically 1–3). Cards with no security surface carry no row at all — do not pad.
- **Never** repeat cross-cutting NFRs (rate limiting, audit logging, transport encryption) card by card; they live once as standalone rows in the Quality Attributes table.
- ❌ Dumping every NFR into the biggest card "for coverage"; ❌ listing an NFR without its four-link chain; ❌ prescribing arbitrary operational numbers (Anti-Pattern 11).

**Row `Interfaces:`**
- ✅ "Registration screen; Login screen; Password recovery flow; Transactional email interface" — the surfaces where the functionality is exercised.
- ❌ "Workspace Admin and Workspace Owner" — an actor list, not interfaces (Anti-Pattern 9). Actors already live in the Actors table and `Stakeholders`.

**Row `Dependencies: Data Sources:`**
- ✅ "Registration form submissions; Credential verification requests; Password reset requests" — the real operational origins for THIS requirement.
- ❌ Copying the same generic source list into every card.

**Row `Dependencies: Extraction Periodicity:`**
- ✅ "on demand" for user-initiated actions; "on event" for failure/status-driven flows; "daily digest" for scheduled digests; "per recurrence schedule" for scheduler-driven functionalities.
- ❌ Automatic "on demand" everywhere, including event- and schedule-driven requirements.

**Row `Dependencies: Information Systems / Databases:`**
- ✅ "Identity and Credential Store"; "Internal Application Database (task state records)"; "File Storage Service"; "Internal Application Database (subscription records); External Payment Gateway" — the functional repository role this requirement touches.
- ❌ The identical "Internal Application Database" on 16 of 18 cards with no differentiation (Anti-Pattern 10). ❌ Commercial engines or products (Anti-Pattern 2).

**Rows `Preceding Requirements:`, `Identified Problems:`, summary-table `Restrictions:`**
- ✅ Empty by default; populated only with genuine, evidenced content.
- ❌ Synthetic filler to look complete (Anti-Patterns 4 and 5).

**Standing meta-rule:** every user correction to a filling style is codified into this §3.3 (with a ✅/❌ pair) in the same working session, so future filling is deterministic and never drifts back to the rejected style.

### 3.4 V1 Functional Evolution (Refinement Pass)

The V0 baseline is locked to protect elicitation from pre-baked security (§2.3) — not to freeze the functional model forever. The V1 security & privacy synthesis legitimately reveals functional gaps that pure business elicitation cannot see: a brute-force lockout creates the new user goal *recover a locked account*; irreversible erasure creates the obligation to offer a final export before data loss. A V1 that only appends constraint rows leaves such gaps undiscovered until implementation. V1 therefore applies a controlled **Functional Refinement Pass** with an exhaustive change taxonomy:

| Type | Change | Rule | ✅ / ❌ |
|---|---|---|---|
| **D1 — Derived requirement** | New card `Rn.x` for user-visible, Cockburn Sea-Level functionality demanded by an obligation (`RN` / `PO-` / `SO-` / regulation article) not covered by any V0 card | Continues the package numbering; generates the matching PUC and fully dressed use case in `Doc02`; all R13 standards apply (active verb, technology neutrality, scale discipline) | ✅ `R1.3 Recover access to a locked user account` (derived from the NFR-RN10/RN11 lockout behavior) · ❌ `R1.3 Session Management Module` (nominalized, pseudo-origin) |
| **D2 — Description refinement** | `Description` rewritten so an absorbed constraint can actually bind | ID, origin and scope preserved; targeted use cases gain steps or extensions only — their Main Success Scenario is otherwise preserved | ✅ `R8.2` gains "presents a final personal data export option before irreversible erasure" · ❌ rewriting the card into a different functionality |
| **D3 — Priority re-evaluation** | MoSCoW priority elevation driven by a confirmed regulation | The regulatory driver (article + Phase 2 objective) is cited in the register; summary table, card, and traceability matrix are updated together | ✅ `R1.2` SHOULD → MUST (GDPR Art. 5(1)(d) + Art. 16 rectification via `PO-D-01.4-001`) · ❌ "this feels mandatory" |
| **D4 — Card split** | One V0 card bundles functionalities with distinct security surfaces needing separate lifecycle or priority | Highest ceremony; old→new renumbering recorded; only when D1–D3 demonstrably cannot express the change | ✅ (rare) · ❌ splitting `R4.2` into "move card left" + "move card right" (clam-level, Anti-Pattern 3) |

**Prohibited in the pass:** deleting or silently shrinking V0 scope; inventing functionality without a traceable driver; technology leakage in any new or refined text (§2.1 still applies); clam-level derived cards (§1.2).

**Change Register (mandatory):** every functional change — including `evaluated, no change` rows — is recorded as `type → from/to → driving RN/PO/SO/article → rationale`, and the V1 document's Version History documents the pass in one row. Reference application: `cases/Case_01_TinyTask_SaaS/03_PHASE3_SPEC/analysis_v0_to_v1/STEP5_FUNCTIONAL_EVOLUTION_REGISTER.md`.

**Relationship to Anti-Pattern 1 (§7):** the Pre-Baked Security/Privacy Trap bans security mechanisms in **V0 authoring**. A V1 *derived* functional requirement is legitimate precisely because it carries its regulatory lineage (`RN` → regulation article) and stays in pure functional terms at Sea Level: "Recover access to a locked account" is a user goal; "store passwords with bcrypt" is not.

---

### 3.5 Objective Fulfillment Semantics & the Organizational Lane (ADR-007 / ADR-008)

Mapping a Phase 2 objective to a carrier requirement is a **fulfillment claim**, not a bookkeeping link. Three rules make the claim verifiable; a fourth routes what no product requirement can carry.

**Rule 1 — Congruence (when objectives may share one requirement).** A requirement (one EARS condition→response pair) may cite multiple Phase 2 objectives as drivers **only if every cited objective is satisfied by that same condition→response**. Objectives demanding different system responses get separate requirements. ✅ One requirement carries the GDPR and CRA twins for the transport-encryption leg, with the CRA twin's attack-surface leg discharged by the attack-surface carriers (cross-reference in the matrix). ❌ Absorbing a co-driver "by twin symmetry" because both objectives publish identical control anchors — identical anchors constrain the fourth chain link (controls), never the first (behavior).

**Rule 2 — Discharge (what "covered" means).** An objective is **fully covered** only when the union of its carriers' Volere fit criteria reconstitutes the objective's Phase 2 Verification Criteria **and** every demand leg of its Operational Statement is carried, out-of-scale-recorded (with warrant), or explicitly carved out. ❌ Naming an RN next to an objective and writing "Covered".

**Rule 3 — The matrix is the discharge graph; card chains cite primary drivers.** Cross-carrier fulfillment is recorded in the case's `synthesis_rounds/OBJECTIVE_MAPPING.md` (`VC discharge` column), not by stuffing every card chain (§3.3 economy: typically 1–3 constraints per card). Re-anchoring a chain to a different driver objective is a baseline change (round verdict, ADR-005) and **must re-examine the frozen wording/fit criterion against the new driver's demands** — wording is never grandfathered across a driver swap.

**Verdict vocabulary (matrix State column):** `Fully covered` · `Partially covered (functional leg + explicit carve-out)` · `No functional carrier (organizational)` · `Design guidance` · `N/A`. A partial verdict names the carried legs, the discharging fit criteria, and the carve-out route of every uncarried leg.

**Rule 4 — Explicit carve-outs; the organizational lane is the sink.** A leg no product requirement carries is routed to exactly one of: (a) the organizational lane → `Doc03_Organizational_Requirements.md` (ADR-008); (b) out-of-scale, with a company-scale warrant (§2.4 / R13); (c) design guidance (Phase 4 context); (d) a round proposal — a new or adjusted requirement, pending the client verdict (ADR-005).

**Round proposal payload addition:** each proposal carries a **discharge statement** — which legs of each cited driver this requirement's fit criterion discharges.

#### 3.5.1 Organizational Requirements (Doc03, PROCESS lane — ADR-008)

Objectives and legs whose realization class is PROCESS/CAPABILITY (ADR-003) derive into the case's `03_PHASE3_SPEC/Doc03_Organizational_Requirements.md` — same derivation machinery, organizational subject:

- **EARS organizational templates:** `The organization shall <response>.` · `When <trigger>, the organization shall <response>.` · `While <state>, the organization shall <response>.` · `If <condition>, then the organization shall <response>.` · `Where <activity exists>, the organization shall <response>.` — one congruent demand set per requirement (Rule 1 unchanged).
- **Card anatomy (per requirement):** ID `ORG-D-XX.Y-NNN` + active-verb name; EARS statement; Requirement Origin (real stakeholder/business/regulatory event — never internal categories); Volere fit criterion; verification method (`INSPECT`/`DEMONSTRATE`/`ANALYZE` dominate; `TEST` where automated evidence exists); Dependencies (Stakeholders, Owner — from the Phase 2 Governance & Stakeholder Matrix, Cadence, Information Systems [technology-neutral or empty], Preceding Requirements [empty by default]); Priority (MoSCoW from regulatory priority).
- **Chain:** `regulation article → Phase 2 objective → (principle) → organizational control anchor`. Primary anchors: NIST CSF 2.0 GOVERN function (`baseline/CONTROLS/NIST_CSF_2.0/GOVERN/`) and organizational categories of the other CSF functions; advisory under R2b agent discretion: ISO/IEC 27001:2022 Annex A organizational controls (`baseline/CONTROLS/ISO_27001_2022/A5_ORGANIZATIONAL/`), ENISA NIS2 baseline (`baseline/CONTROLS/ENISA/NIS2_BASELINE/`), BSI IT-Grundschutz OPS layer. PF 1.1 accompanies GDPR-derived obligations only. No invented anchors (R2).
- **Specificity stays at L2** (§2.5): no invented operational parameters — values come from the regulation, a cited source, or a risk assessment.
- **Doc03 blueprint:** Executive summary → per-domain sections `D-01`…`D-10` (one card per requirement) → coverage linkage table (objective / carve-out leg → ORG requirement → verification method → owner) → MoSCoW summary → Version History. Content enters through the ADR-005 round cycle; the Part 1 Exit Gate G1 evidence surface extends to the organizational mapping (ADR-008 D7).
- ✅ `ORG-D-04.3-001` **Notify the supervisory authority of personal-data breaches within 72 hours** · ❌ `Breach Notification Process` (nominalization, §2.2) · ❌ `The system shall notify the authority` (product subject — an organizational duty).

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

### 4.2 Use Case Granularity & Literature Best Practices (Cockburn & Larman Standard)

1. **Refinement Stops at Level 1 (Cockburn Sea-Level Discipline):**
   - Every use case must be expressed at **Level 1 (`{U.C.n.m}`)** — Cockburn's "User Goal / Sea Level". A Sea-Level use case represents an elementary business task completed by a single actor in a single sitting that delivers measurable value to the user.
2. **Absolute Ban on Leaf Nodes and Micro-UI Procedural Scripts:**
   - Never decompose into `{U.C.n.m.k}`.
   - Never write micro-UI procedural scripts ("Step 1: User navigates to URL; Step 2: User clicks blue button; Step 3: User focuses input..."). Step sequences in use cases must represent *functional actor intent and black-box system validation/commit*, not UI layout instructions.
3. **Literature-Grounded Use Case Anatomy (Cockburn Fully Dressed Format):**
   - Each `{U.C.n.m}` specification must adhere to the standard literature template (Cockburn, 2000; Larman, 2004; Wiegers & Beatty, 2013):
     - **ID & Name:** Canonical identifier (`{U.C. n.m}`) and active verb phrase denoting the user goal.
     - **Traceability:** Direct bidirectional mapping to underlying Functional Requirement (`R...`) and Product Use Case (`PUC...`) from `Doc01`.
     - **Primary Actor:** The principal human user or external system initiating the interaction.
     - **Supporting Actors:** Auxiliary services or external systems participating in the execution (e.g., Payment Gateway, Email Service).
     - **Scope & Level:** System Boundary / Sea Level (User Goal / Level 1).
     - **Stakeholders & Interests:** Key organizational beneficiaries and what they need guaranteed.
     - **Preconditions:** The mandatory state of the system and actors before execution can trigger.
     - **Trigger:** The business event that initiates execution.
     - **Main Success Scenario (Happy Path):** Numbered sequence of operational interactions between Actor and System, describing business intent, input submission, system validation, state transition, and output delivery.
     - **Extensions (Alternative & Exception Flows):** Branching conditions, business rule variations, and error recovery paths (e.g., `2a`, `3a`), ensuring comprehensive exception handling.
     - **Success Guarantees (Postconditions):** What the system guarantees upon successful completion.
     - **Minimal Guarantees:** What the system guarantees even if the goal fails (data integrity, rollback, audit recording).
4. **Macro UML Use Case Diagrams:**
   - Each macro use case group (`{U.C. 1}` to `{U.C. N}`) must be preceded by an error-free Mermaid UML Use Case Diagram (`flowchart LR`), linking human actors and external services to oval user goal nodes in standard UML style, avoiding reserved bracket characters inside labels.

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
| **Identified Problems & Constraints** | Informs downstream threat modeling (Phase 4, ADR-005) and exception handling under **Skill 5 (Secure Defaults)** and **Skill 6 (Defensive Design)**. |

---

## 6. Authoring & Validation Checklist

Before declaring any Phase 3 functional baseline deliverable complete, verify:

- [ ] **Technology Check:** Run a text search for `PostgreSQL`, `MySQL`, `Dotnet`, `Angular`, `React`, `Stripe`, `AWS`, `S3`, `WebSockets`. Zero matches must be returned.
- [ ] **Verb Phrasing Check:** Verify that every requirement group (`R1`), sub-requirement (`R1.1`), and use case (`{U.C. 1.1}`) starts with an active verb in the infinitive/imperative.
- [ ] **Table Format Check:** Verify that each individual requirement card uses the exact 7-row single-column format with `| Requirement |` header.
- [ ] **Dependencies Check:** Verify that `Preceding Requirements:` is empty by default (>90% blank) and `Information Systems / Databases:` contains only technology-neutral terms.
- [ ] **Restrictions Check:** Verify that the `Restrictions` column in the MoSCoW summary table is empty by default.
- [ ] **Granularity Check:** Verify that `Doc02` contains zero leaf nodes (`{U.C.n.m.k}`) and zero procedural execution steps.
- [ ] **UML Diagram Check:** Verify that every macro use case has a valid, error-free Mermaid UML Use Case Diagram (`flowchart LR`) depicting actors and user goals.
- [ ] **Anti-Pattern Check:** Review all cards against Section 7 to ensure none of the 8 anti-patterns are present.
- [ ] **doc_lint Check:** Run `python scripts/doc_lint.py --strict` and ensure 0 findings are returned.

---

## 7. Lessons Learned: Anti-Patterns in Requirements Engineering (How NOT to Write Requirements)

This section documents critical anti-patterns identified during the authoring and refinement of functional baselines. Grounded in established Requirements Engineering literature (Robertson & Robertson / Volere, Alistair Cockburn, Karl Wiegers & Joy Beatty), these represent common traps that compromise specification quality, bias architectural choices, or prematurely couple business goals with technical mechanisms.

### Anti-Pattern 1: The Pre-Baked Security & Privacy Trap
- **Description:** Injecting concrete security, cryptographic, or privacy controls directly into the functional requirement baseline (e.g., specifying Two-Factor Authentication (2FA/TOTP), session termination timeouts, password hashing algorithms like bcrypt/Argon2, TLS encryption, or GDPR right-to-be-forgotten anonymization).
- **Literature Grounding:** Robertson & Robertson (*Mastering the Requirements Process*, Volere) strictly separate *functional requirements* (the business functionality the product must deliver) from *security non-functional requirements* and *operational constraints*. Pre-baking security mechanisms into functional cards blinds the engineering process to alternative threat mitigations.
- **Why it breaks AEGIS:** AEGIS is specifically engineered to derive security and privacy requirements (`REQ-D-XX.Y-NNN`) systematically from regulatory anchors (GDPR, NIS2, CRA, DORA, AI Act) and control referentials (NIST CSF 2.0, NIST PF 1.1, NIST AI RMF) through specialized skills (Attack Surface, Trust Boundaries, Least Privilege, Data Minimization). If security is pre-baked into the functional cards, AEGIS cannot perform genuine derivation, resulting in circular reasoning or redundant controls.
- **❌ INCORRECT (Anti-Pattern):**
  > "The system must enforce Two-Factor Authentication (TOTP via Google Authenticator or SMS) and invalidate inactive sessions after 15 minutes of inactivity."
- **✔ CORRECT (Pure Functional):**
  > "The system must allow registered users to authenticate into their assigned workspace and access active projects."
  > *(Security synthesis downstream will determine whether TOTP, WebAuthn, SSO, or session limits are mandated based on Phase 2 operational rules).*

---

### Anti-Pattern 2: The Technology Leakage Trap
- **Description:** Referencing concrete software products, programming frameworks, database engines, cloud providers, or technical protocols in functional requirements or dependency cards (e.g., "PostgreSQL", "MySQL", "AWS S3", "Stripe", "Dotnet", "Angular", "WebSockets", "OAuth2").
- **Literature Grounding:** Robertson & Robertson emphasize the *Essence of the System*—the pure policy and business functionality free of implementation technologies. Wiegers & Beatty (*Software Requirements*, 3rd Ed.) warn that stating technologies in functional specifications prematurely constrains solution design and turns business requirements into legacy design decisions.
- **Why it breaks AEGIS:** Phase 3 functional specifications define *what* the system provides to users. Technical architecture and component selection occur during Phase 3 solution synthesis. Early vendor lock-in violates AEGIS Rule R5.
- **❌ INCORRECT (Anti-Pattern):**
  > "Description: Store uploaded deliverable attachments in an AWS S3 bucket and record metadata in PostgreSQL. Payment is processed via Stripe Checkout."
  > "Information Systems / Databases: AWS S3, PostgreSQL 15, Stripe API."
- **✔ CORRECT (Technology-Neutral):**
  > "Description: The system must allow collaborators to attach deliverable files directly to task cards, storing file content in the file storage service and recording metadata in the internal application database. External payments are completed via the external payment gateway."
  > "Information Systems / Databases: Internal Application Database, File Storage Service."

---

### Anti-Pattern 3: The Clam-Level Decomposition Trap (Micro-UI Fragmentation)
- **Description:** Decomposing user actions into micro-level user interface widgets or separate requirement cards for individual UI interactions (e.g., creating separate requirements for: "Upload file button", "Drag and drop file into box", "Support PNG format", "Support PDF format", "Generate file thumbnail").
- **Literature Grounding:** Alistair Cockburn (*Writing Effective Use Cases*) defines goal levels: *Summary Level* (Kite/Cloud), *User Goal Level* (Sea Level), and *Subfunction Level* (Fish/Clam Level). Use cases and functional requirements must sit at **Sea Level** (Level 1)—an atomic interaction that provides measurable business value to the user and can be completed in a single uninterrupted sitting. Clam-level interactions are UI design choices, not functional requirements.
- **Why it breaks AEGIS:** Micro-fragmentation inflates the requirement count, clutters traceability matrices, and makes security threat modeling unmanageable by scattering a single logical operation across dozens of trivial cards.
- **❌ INCORRECT (Anti-Pattern):**
  - `R4.1`: Allow user to click file upload button.
  - `R4.2`: Allow user to drag and drop file into dropzone.
  - `R4.3`: Support PDF attachment format.
  - `R4.4`: Support PNG and JPG attachment format.
  - `R4.5`: Render attachment preview thumbnail.
- **✔ CORRECT (Consolidated Sea-Level):**
  - `R4.1`: "Attach and manage task deliverable files" (allows uploading deliverable files up to 25 MB in common documentation and image formats, rendering inline previews and permitting authorized download and deletion).

---

### Anti-Pattern 4: The Artificial Chaining Trap (Preceding Requirements Abuse)
- **Description:** Forcing artificial sequential dependencies into the `Preceding Requirements:` field of every requirement card (e.g., setting `R1.1` as preceding for `R1.2`, `R1.2` for `R1.3`, or chaining every feature to user login).
- **Literature Grounding:** Volere Snow Cards specify dependencies only when a strict, indispensable logical constraint exists. GPTools E1.1 reference model leaves `Preceding Requirements` **empty** (>90% blank), as requirements exist concurrently within the functional scope. Chaining is a workflow scheduling artifact, not a fundamental system dependency.
- **Why it breaks AEGIS:** Chaining creates false dependency graphs in architectural modeling, preventing modular implementation, parallel test engineering, and clean microservice boundary definition.
- **❌ INCORRECT (Anti-Pattern):**
  > Card R2.3: `Preceding Requirements: R2.2, R2.1, R1.3, R1.2, R1.1` (every previous card listed).
- **✔ CORRECT (Clean Dependency):**
  > Card R2.3: `Preceding Requirements: —` (empty by default; only filled when an absolute logical dependency exists, e.g., transitioning a task requires a task to exist).

---

### Anti-Pattern 5: The Phantom Restriction Trap
- **Description:** Forcing synthetic narrative commentary into every cell of the `Restrictions` column in the MoSCoW summary table (e.g., inventing banal notes like "Requires user to have keyboard", "Limited to web browser", or repeating the requirement description).
- **Literature Grounding:** GPTools E1.1 Table 20 explicitly leaves the `Restrictions` column **empty by default** for standard requirements. A restriction should only be stated when a genuine, non-trivial operational or business constraint limits the requirement (e.g., external legal restriction, statutory deadline, or legacy hardware ceiling).
- **Why it breaks AEGIS:** Noise in restriction columns dilutes real architectural constraints, causing automated analyzers and human auditors to miss genuine project risks.
- **❌ INCORRECT (Anti-Pattern):**
  > Filling all 30 rows with repetitive fluff: "Subject to standard web browser availability", "Requires internet access", "User must be logged in".
- **✔ CORRECT (Clean Table):**
  > Leaving cells empty (`—`) by default, populating only genuine restrictions (e.g., "Subject to payment provider jurisdiction eligibility" or "Restricted to authorized organization owners").

---

### Anti-Pattern 6: The Pseudo-Origin / Self-Referential Trap
- **Description:** Specifying the `Requirement Origin:` as an internal system module, category name, or document section (e.g., "TinyTask SaaS / Task Management", "System Architecture / Auth Module").
- **Literature Grounding:** Robertson & Robertson define requirement origin as the *originating business event, stakeholder request, or operational reality* that justifies why the requirement exists. Requirements do not originate from their own functional category; they originate from human actors, operational problems, or business strategies.
- **Why it breaks AEGIS:** AEGIS needs to trace business intent back to real organizational stakeholders to assess proportionality, risk appetite, and regulatory liability. Self-referential origins sever this traceability chain.
- **❌ INCORRECT (Anti-Pattern):**
  > `Requirement Origin: TinyTask SaaS / Identity Management`
- **✔ CORRECT (Stakeholder & Operational Context):**
  > `Requirement Origin: Founders Business Case & User Onboarding Workflow`
  > `Requirement Origin: Team Lead Operational Intake & Work Coordination Feedback`
  > `Requirement Origin: Customer Subscription & Commercial Billing Policy`

---

### Anti-Pattern 7: The Passive Nominalization Trap
- **Description:** Titling requirements, sub-requirements, and use cases with noun phrases and nominalizations instead of active verbs in the infinitive or imperative (e.g., "User Account Management", "Task Lifecycle", "Gestão de Utilizadores", "Criação de Tarefas").
- **Literature Grounding:** Standard software engineering guidelines (Cockburn, Wiegers, IEEE 830 / ISO/IEC/IEEE 29148) mandate active verb phrases for functional requirements and use cases. Systems do not provide "concepts"; they perform actions that allow users to achieve goals.
- **Why it breaks AEGIS:** Nominalized names obscure the actor-action relationship, complicating automated extraction of operational functionalities and blurring authorization boundaries.
- **❌ INCORRECT (Anti-Pattern):**
  > `R1: User Account and Workspace Management`
  > `R2.1: Task Creation and Lifecycle`
  > `U.C. 1: Gestão de Projetos`
- **✔ CORRECT (Active Verb Conjugation):**
  > `R1: Manage User Accounts and Workspaces`
  > `R2.1: Create and transition collaborative tasks`
  > `U.C. 1: Gerir Projetos` / `Manage Projects`

---

### Anti-Pattern 8: The Vague Adjective / Unverifiable Quality Trap
- **Description:** Using subjective, non-measurable adjectives in requirement descriptions (e.g., "The system must be fast", "The UI must be intuitive and user-friendly", "Support common attachment formats", "Handle high traffic").
- **Literature Grounding:** Robertson & Robertson define the *Fit Criterion*—an unambiguous, quantifiable metric by which a tester can verify whether an implementation satisfies the requirement. Wiegers & Beatty identify unverifiable adjectives as the single most frequent cause of requirement ambiguity and customer-developer disputes.
- **Why it breaks AEGIS:** Security and compliance verification requires binary or measurable assertions (`RULE-*`). Vague quality statements cannot be translated into automated tests, static checks, or audit evidence.
- **❌ INCORRECT (Anti-Pattern):**
  > "The system must quickly upload attachments in common formats and display them in a user-friendly manner."
- **✔ CORRECT (Verifiable Behavioral Contract):**
  > "The system must allow users to upload file attachments up to 25 MB in PDF, PNG, JPEG, and CSV formats, rendering previews within 2 seconds under standard broadband conditions."

---

### Anti-Pattern 9: The Actor-Dump Interfaces Trap
- **Description:** Filling the `Interfaces:` row of a requirement card with actor names ("Workspace Admin and Workspace Owner", "Authenticated User and Notification / Email Service") instead of the concrete interaction surfaces through which the functionality is exercised.
- **Why it breaks AEGIS:** Actors are already defined in the Actors table and in `Dependencies: Stakeholders`; duplicating them under "Interfaces" adds zero information and hides the real integration points. AEGIS downstream skills (trust-boundary analysis, attack-surface analysis) need the *surfaces* — screens, forms, flows, external system interfaces — to locate where mediation and validation must occur.
- **❌ INCORRECT (Anti-Pattern):**
  > `Interfaces: Workspace Admin and Workspace Owner`
  > `Interfaces: Unauthenticated Visitor, Registered User, and Notification / Email Service`
- **✔ CORRECT (Interaction Surfaces):**
  > `Interfaces: Registration screen; Login screen; Password recovery flow; Transactional email interface`
  > `Interfaces: Plan selection screen; Hosted checkout interface`

---

### Anti-Pattern 10: The Copy-Paste Databases Trap
- **Description:** Pasting the same generic `Information Systems / Databases:` value (typically "Internal Application Database") into every requirement card regardless of what the requirement actually touches.
- **Why it breaks AEGIS:** The IS/Databases field is a functional inventory signal: it tells downstream phases which repository roles each functionality reads and writes (identity store vs task state vs audit records vs external gateway). A uniform value erases that signal, breaks data-flow analysis, and makes the field noise instead of data.
- **❌ INCORRECT (Anti-Pattern):**
  > 16 of 18 cards carrying `Information Systems / Databases: Internal Application Database` unchanged.
- **✔ CORRECT (Functionally specific, technology-neutral):**
  > `Information Systems / Databases: Identity and Credential Store` (registration/authentication)
  > `Information Systems / Databases: Internal Application Database (task state records)` (board transitions)
  > `Information Systems / Databases: File Storage Service; Internal Application Database (attachment metadata)` (attachments)

---

### Anti-Pattern 11: The Premature Solution Design & Over-Specific Parameter Trap (Conditioning the Implementation Architecture)
- **Description:** Injecting arbitrary low-level operational parameters, implementation metrics, or solution mechanics into non-functional requirements and security constraints (e.g., prescribing "30-minute idle session timeout", "minimum 128 bits of entropy", "rate limit of 100 requests per minute with Retry-After header", "salt lengths >= 16 bytes", "data export delivered within 24 hours", or "files purged in 14 days").
- **Literature Grounding:** Robertson & Robertson (*Mastering the Requirements Process*, Volere) and ISO/IEC/IEEE 29148:2018 emphasize that requirements must define *what* system quality or protective boundary must be achieved, not prematurely fix quantitative design parameters without stakeholder validation or empirical benchmarking. Karl Wiegers (*Software Requirements*, 3rd ed.) warns against "presupposing design in requirements", which narrows the solution space and blinds system architects to contextual trade-offs.
- **Why it breaks AEGIS:** At Phase 3, the client/user has not yet specified low-level operational numbers. When an agent invents concrete parameters ("30 min", "100 req/min"), it **conditions the solution without knowledge of the operational reality** (*sem conhecimento de causa*). The proper AEGIS derivation lineage is:
  $$\text{Applicable Regulation} \longrightarrow \text{Article / Clause} \longrightarrow \text{Control Framework Mapping (NIST CSF 2.0 / NIST PF 1.1 / ISO)} \longrightarrow \text{High-Level Control Objective}$$
  Phase 3 defines the **High-Level Control Objective** anchored directly in the mapped control. Fine-grained numerical parameterization and algorithm tuning belong strictly to Phase 4 (Architecture & Implementation) or subsequent detailed design passes with stakeholder concurrence.
- **❌ INCORRECT (Anti-Pattern - Premature Parameterization):**
  > "While a user is authenticated, the system shall maintain session tokens with a minimum of 128 bits of entropy and terminate sessions after 30 minutes of inactivity, rejecting post-logout requests within 100 milliseconds."
  > "The system shall throttle API clients exceeding 100 requests per minute per tenant, returning HTTP 429 Too Many Requests."
  > "When an account termination request is submitted, the system shall permanently purge personal data within 30 days."
- **✔ CORRECT (High-Level Control Objective Anchored in Regulation & Framework):**
  > "The system shall manage authenticated user sessions through secure, non-predictable session identifiers, terminating and invalidating session state upon explicit user logout and following an established period of user inactivity, ensuring session state cannot be resumed without re-authentication."
  > *(Anchored in CRA Annex I Part I (2)(j) → NIST CSF 2.0 PR.AA-03)*
  > "The system shall monitor and throttle inbound external API requests to protect system availability against resource exhaustion and denial of service, enforcing request rate limitations commensurate with operational capacity."
  > *(Anchored in CRA Annex I Part I (2)(e) → NIST CSF 2.0 PR.IR-01, PR.PS-02)*
  > "When an account closure or data subject erasure request is executed, the system shall irreversibly erase personal identifiers and credentials from active operational stores, applying cryptographic pseudonymization or anonymization to historical records where retention is required for legal or organizational audit integrity."
  > *(Anchored in GDPR Art. 17 → NIST PF CT.PO-P3)*


