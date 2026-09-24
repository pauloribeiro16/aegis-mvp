# Threat Analysis — Deferred to Phase 4 (TinyTask SaaS)

> **Status:** DEFERRED — Phase 4 (Threat Analysis) per ADR-005. Not part of the Phase 3 baseline; never consumed by `Doc01`/`Doc02`.
> **Purpose:** Seed material for the future Phase 4 threat-modeling engagement: the attack and privacy-threat hypotheses drafted during the 2026-09-23 synthesis, preserved verbatim per functional area.
> **Trigger:** Researcher judgment that the accepted baseline is robust and concrete (post risk-acceptance convergence, post control selection).
> **On activation:** every hypothesis below is re-validated against the *accepted* baseline and its selected controls — items whose risk was explicitly accepted by the client (`Risk-accepted` in the Risk Acceptance Register) are not re-litigated here; they are recorded as accepted posture.

---

## 1. Framing (carried from the original derivation)

- **Method grounding:** STRIDE Threat Modeling (Shostack, 2014), Privacy by Design (Cavoukian, 2009), Saltzer & Schroeder (1975).
- **Inputs at Phase 4 time:** the accepted, control-anchored F3 baseline (`v1_security_privacy_synthesis/`), the Risk Acceptance Register (`synthesis_rounds/`), and the asset/trust-boundary maps from Phase 3 Step 2.

---

## 2. Threat & Vulnerability Hypotheses by Functional Area

### Functional Area 1: User Accounts & Authentication (`R1.1`, `R1.2` | `{U.C. 1.1}`, `{U.C. 1.2}`)
- *Threat 1 (Credential Stuffing / Brute Force):* Attackers script automated login attempts against the public ingress.
- *Threat 2 (Plaintext Password Exposure):* Internal database dump reveals user credentials.
- *Threat 3 (Session Hijacking):* Session tokens intercepted over unencrypted channels or persisting after logout.
- *Privacy Threat 4 (Data Maximization):* Registration form unnecessarily demanding personal phone numbers or demographic data.

### Functional Area 2: Workspaces and Teams (`R2.1`, `R2.2`, `R2.3` | `{U.C. 2.1}`, `{U.C. 2.2}`, `{U.C. 2.3}`)
- *Threat 1 (Cross-Tenant Data Leakage):* An authenticated user belonging to Tenant A modifies their request parameters (IDOR) to access or modify Tenant B's workspace.
- *Threat 2 (Privilege Escalation):* Standard workspace member invokes administrative member-invitation or role-promotion APIs.

### Functional Area 3: Manage Projects (`R3.1`, `R3.2` | `{U.C. 3.1}`, `{U.C. 3.2}`)
- *Threat 1 (Unauthorized Project Mutation):* Guests or standard members modifying project settings or archiving active work.
- *Threat 2 (Unbounded Project Creation):* Malicious users generating millions of empty project containers to exhaust storage.

### Functional Area 4: Manage and Execute Tasks (`R4.1`, `R4.2`, `R4.3` | `{U.C. 4.1}`, `{U.C. 4.2}`, `{U.C. 4.3}`)
- *Threat 1 (API Resource Starvation):* Automated client firing 1,000 board transition requests per second, exhausting server connections.
- *Threat 2 (Cross-Tenant Task Tampering):* Injecting foreign task IDs into state transition endpoints.

### Functional Area 5: Collaborate on Deliverables (`R5.1`, `R5.2` | `{U.C. 5.1}`, `{U.C. 5.2}`)
- *Threat 1 (Malicious Binary Upload / Web Shell):* Attacker uploads `.php`, `.exe`, or HTML file masquerading as a PDF to achieve remote execution.
- *Threat 2 (Stored Cross-Site Scripting - XSS):* Attacker injects `<script>` or event handlers into task comment text to hijack session cookies of other team members.
- *Privacy Threat 3 (Indefinite Data Retention):* Deleted deliverable attachments remain stored on disk indefinitely.

### Functional Area 6: Track Activity History & Notifications (`R6.1`, `R6.2` | `{U.C. 6.1}`, `{U.C. 6.2}`)
- *Threat 1 (Audit Log Tampering / Erasure):* Malicious insider deleting historical records to cover up unauthorized actions.
- *Privacy Threat 2 (Employee Surveillance & Purpose Creep):* Management using task activity logs to monitor employee keystrokes or productivity metrics without consent.

### Functional Area 7: Manage Commercial Subscriptions (`R7.1`, `R7.2` | `{U.C. 7.1}`, `{U.C. 7.2}`)
- *Threat 1 (Forged Billing Webhooks):* Attacker sending mock HTTP POST requests to TinyTask's webhook endpoint claiming an enterprise plan was paid.
- *Threat 2 (Replay Attacks):* Re-submitting previous valid payment notifications to extend subscriptions fraudulently.

### Functional Area 8: Export Data and Close Accounts (`R8.1`, `R8.2` | `{U.C. 8.1}`, `{U.C. 8.2}`)
- *Threat 1 (Post-Closure Token Re-use):* Deactivated user account continues accessing APIs using previously issued session tokens.
- *Privacy Threat 2 (Incomplete Erasure):* Personal data remaining active in database backups and operational tables after account termination.
- *Privacy Threat 3 (Third-Party Data Contamination):* Exporting workspace archives exposing personal contact details of unrelated individuals.

---

## 3. Open items for the Phase 4 engagement

- Map each hypothesis to the accepted constraints (RN set) and their selected controls; identify coverage gaps and residual risks.
- Classify residual risks and bring any **new treatment proposals back through the Phase 3 round cycle** (`synthesis_rounds/RISK_ACCEPTANCE_REGISTER.md`) — Phase 4 does not modify the baseline unilaterally.
- Chain-recalibration backlog (STEP6 §7) should be resolved before or during this engagement so threat-to-requirement mapping anchors on correct chains.
