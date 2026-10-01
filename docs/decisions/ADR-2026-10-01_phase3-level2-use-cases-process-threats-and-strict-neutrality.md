---
id: 'AEGIS-MVP-ADR-009'
date: 2026-10-01
status: ACCEPTED
decided_by: researcher (working session)
amends: 'ADR-2026-09-24_phase4-threat-analysis-and-iterative-risk-acceptance.md (ADR-005, feedback loop operationalization) · ADR-2026-09-28_phase3-two-part-structure.md (ADR-006, Part 1/Part 2 interaction) · templates/phase3_functional_spec_guidelines.md (Level-2 use case criteria)'
---

# ADR-009 — Phase 3 Specification Architecture: Level-2 Security Use Cases, Process Threat Evaluation, Part 2 Feedback Loop, Dual Anchoring, and Absolute Technology Agnosticism

## 1. Status

**ACCEPTED** — decided by the researcher on 2026-10-01. Normative across all AEGIS Phase 3 specifications and downstream pipeline increments.

---

## 2. Context & Questions Stated Precisely

During the architectural review and practical execution of Phase 3 for target systems, five interconnected questions were identified regarding requirements granularity, threat modeling scope, feedback mechanics, and abstraction boundaries:

1. **Use Case Granularity & Level-2 Decompositions (`{U.C. x.y.z}`):**  
   Earlier guidelines enforced an exclusive anchor at Cockburn Level 1 (Sea Level / `{U.C. x.y}`), prohibiting leaf nodes to avoid micro-UI clutter. However, complex security transactions (such as multi-zone cryptographic challenges, file decontamination, asynchronous webhook signature verification, and multi-tenant cryptographic erasure) cannot be adequately expressed as simple one-line steps in a Sea-Level flow without losing essential failure modes and guarantees. What are the formal criteria governing when a Level-2 use case is legitimate and when it is prohibited?

2. **The Feedback Loop from Part 2 (Threats & Risks) to Part 1 (Specification):**  
   ADR-005 and ADR-006 established that Part 2 (Threat & Risk Analysis) validates the baseline produced by Part 1 (Security & Privacy Specification). However, the concrete operational mechanics of the reverse feedback loop — how threats identified in Part 2 re-enter, refine, and evolve Part 1 requirements and use cases — remained unspecified. Does Part 1 evolve into a new version (e.g., `v3`), and how is this closure traced?

3. **Risk Evaluation on Operational and Business Processes (`Doc00`):**  
   With the modular extraction of operational workflows into `Doc00_Process_and_Operational_Workflows.md`, how does security and privacy risk evaluation apply to human and business workflows as opposed to technical Data Flow Diagrams (DFDs)? What does scientific literature dictate?

4. **100% Phase 2 Objective Coverage & The "Dual Anchoring" Principle:**  
   How is complete coverage of upstream regulatory objectives (`PO-` and `SO-`) verified, and can a non-functional security constraint (NFR / EARS) exist in isolation without a concrete functional requirement (`R...`) to operationalize it?

5. **Absolute Technology Agnosticism (Rule R13 Reinforcement):**  
   How must functional specifications, requirements cards, and behavioral flows be written to guarantee 100% independence from commercial vendors, software libraries, database engines, and proprietary protocols across Fases 1 to 3?

---

## 3. Decisions

### D1 — Cockburn Goal Hierarchy & Strict Criteria for Level-2 Use Cases (`{U.C. x.y.z}`)

System specifications operate under Alistair Cockburn's classical goal levels, supplemented by strict security decomposition criteria:
- **Level 0 (Sky / Cloud / Summary Level):** Product Use Cases (PUC) from Volere methodology (`PUC 1.1`, `PUC 2.1`), bounding business events and organizational scope.
- **Level 1 (Sea Level / User Goal):** Core user goals completed by a single primary actor in a single session to achieve measurable business outcomes (`{U.C. 1.1}`, `{U.C. 2.1}`). **By default, >85% of all system use cases must remain at Level 1.**
- **Level 2 (Fish / Subfunction Level — `{U.C. x.y.z}`):** Subordinate use cases decomposing specific high-risk transactional steps, invoked via `<<include>>` or formal refinement.

**Strict Eligibility Criteria (All Three Must Apply):**
A Level-2 use case is permitted **only** when a step in a Level-1 use case satisfies all three conditions:
1. *Trust Boundary Crossing:* The transaction crosses distinct trust zones (e.g., untrusted public network to application backend; application backend to external isolated processing engine).
2. *Autonomous Behavioral Protocol & Multiple Failure Modes:* The transaction possesses its own security preconditions, multiple exception/attack branches (e.g., rate-limit breach, clock drift, signature mismatch, format spoofing), and distinct minimal guarantees.
3. *Cross-Cutting Reusability or Direct Regulatory Imperative:* The subfunction is invoked across multiple Level-1 use cases or directly implements a non-negotiable regulatory mandate requiring formal proof of non-repudiation or cryptographic erasure.

**Prohibition (Anti-Patterns):**
Level-2 use cases are **strictly prohibited** for procedural micro-UI interactions (e.g., clicking buttons, entering form fields, client-side syntax checks, rendering dropdowns).

### D2 — The Operationalized Reverse Feedback Loop (ADR-005 Closure)

Threat modeling in Part 2 is not a terminal artifact; it operates as an active validation engine over Part 1. When Part 2 discovers a threat where inherent or residual risk is evaluated as Medium or High:
1. **Derivation of Mitigating Action:** The risk must be addressed via one of three Part 1 specification vehicles:
   - *EARS Non-Functional Constraint (`RN`):* If the threat demands a quality, temporal, or behavioral boundary condition.
   - *Derived Functional Requirement (D1 / `R<n.m>`):* If the threat demands a new user-visible operational capability (e.g., active session revocation, account unlock flow, emergency export).
   - *Level-2 Subfunction Use Case (`{U.C. x.y.z}`):* If the threat requires multi-step interactive defense sequences.
2. **Evolution Traceability:**
   - Where iterative rounds are active, changes are absorbed into the current working baseline (`v2` or `v3_threat_informed_synthesis`), with every change classified in the D1–D4 taxonomy.
   - Every case risk register (`05_RISK_REGISTER_AND_GOVERNANCE.md`) must include a **Feedback Reconciliation Matrix** mapping:
     `Threat ID (STRIDE/LINDDUN) -> Inherent Risk -> ADR-005 Mitigating Requirement (RN / R / Level-2 UC) -> Verified Residual Risk (Low)`.

### D3 — Threat Modeling on Operational & Business Processes (`Doc00`)

Security and privacy risk analysis must evaluate socio-technical and operational workflows (`Doc00`) alongside technical architecture (DFD). Grounded in authoritative literature:
- **SecBPMN2 (Security-Annotated BPMN):** Operational processes (`PROC-01` to `PROC-05`) are evaluated against:
  - *Segregation of Duties (SoD) / Four-Eyes Principle:* Ensuring conflicting sensitive roles (e.g., billing configuration vs. task execution) cannot be performed by the same operational actor.
  - *Binding of Duties (BoD):* Ensuring sequential steps initiated by a verified actor cannot be intercepted or completed by a different identity without re-authentication.
  - *Non-Repudiation across Trust Boundaries (`TZ-01` to `TZ-05`):* Ensuring handoffs between humans, internal workflows, and third-party processors carry verifiable provenance.
- **PA-BPMN & Process LINDDUN:** Business workflows are analyzed for organizational privacy failure modes:
  - *Unawareness:* Workflows that capture subject data without prior presentation of lawful processing notices.
  - *Linkability across Roles:* Unnecessary exposure of internal staff or customer operational data to unrelated business participants.
- **NIST SP 800-160 Vol. 1 (Process Bypassing):** Validating that technical software interfaces do not allow users to bypass the organizational sequence defined in `Doc00`.

### D4 — 100% Phase 2 Coverage & The "Dual Anchoring" Principle

1. **Exhaustive Objective Coverage:** 100% of Phase 2 objectives (`PO-` and `SO-`) and principles (`PRIN-ENG-01` to `07`) must be accounted for in the case's `OBJECTIVE_MAPPING.md` (Exit Gate G1).
2. **The Dual Anchoring Principle:**
   - A non-functional security/privacy requirement (NFR / EARS constraint `RN`) **must never exist as an unattached, floating rule**.
   - Every NFR must have a **Functional Carrier Anchor (`R...`)** in `Doc01` that provides the concrete operational context where the constraint applies.
   - Conversely, every functional capability handling sensitive data or assets must carry its corresponding security and privacy constraints in its card specification.

### D5 — Absolute Technology Agnosticism (Rule R13 Reinforcement)

In Phases 0, 1, 2, and 3, all specifications, models, requirements, and use cases must remain 100% technology-agnostic. Concrete technologies, database engines, vendor names, protocols, and proprietary algorithms are strictly prohibited:

| Prohibited Specific Technology | Mandatory Agnostic Functional Phrasing |
|---|---|
| *Argon2id, PBKDF2, Bcrypt* | Memory-hard adaptive cryptographic key derivation function |
| *HMAC-SHA256, HMAC* | Keyed cryptographic message authentication code |
| *JWT, Session Cookies, Bearer Token* | Cryptographically signed, time-bound session authentication token |
| *PostgreSQL, MySQL, SQLite, MongoDB* | Internal Application Database / Relational transactional datastore |
| *AWS S3, Google Cloud Storage, Azure Blob* | External Object Storage Service / Distributed file repository |
| *Stripe, PayPal, Adyen* | External Payment Gateway / Hosted billing processor |
| *AES-256-GCM, RSA-4096* | Authenticated high-assurance symmetric / asymmetric encryption |
| *TLS 1.3, HTTPS, SSH* | Authenticated and encrypted end-to-end communication channel |
| *OAuth 2.0, OIDC, SAML* | Federated identity and authorization assertion protocol |

---

## 4. Consequences

- **Methodology & Guidelines:** `templates/phase3_functional_spec_guidelines.md` and `cases/Case_01_TinyTask_SaaS/03_PHASE3_SPEC/PHASE3_PROCESS_AND_METHODOLOGY.md` are updated to incorporate D1 through D5.
- **Case Execution:** 
  - Case 01 integrates the 4 justified Level-2 use cases (`{U.C. 1.1.1}`, `{U.C. 5.1.1}`, `{U.C. 7.2.1}`, `{U.C. 8.3.1}`) into `Doc02_System_Use_Cases.md`.
  - Part 2 risk register establishes the bidirectional Feedback Reconciliation Matrix back to Part 1.
  - All occurrences of technology leaks across diagrams, tables, and cards are sanitized.
- **Linters:** `scripts/check_traceability.py` and `scripts/doc_lint.py` continue to enforce zero findings.

---

## 5. References

- Cockburn, A. (2000). *Writing Effective Use Cases*. Addison-Wesley.
- Robertson, S., & Robertson, J. (2012). *Mastering the Requirements Process: Getting Requirements Right* (3rd ed.). Addison-Wesley.
- Wiegers, K., & Beatty, J. (2013). *Software Requirements* (3rd ed.). Microsoft Press.
- Wolter, C., Menzel, M., & Meinel, C. (2009). *Modeling Security Requirements in Business Processes with SecBPMN*.
- Salnitri, M., Dalpiaz, F., & Giorgini, P. (2015). *Modeling and Verifying Security Policies in Business Processes*.
- NIST SP 800-160 Vol. 1 Rev. 1 (2022). *Engineering Trustworthy Secure Systems*.
