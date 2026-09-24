# Phase 3 — Risk Acceptance Register (TinyTask SaaS)

> **Purpose:** Authoritative record of the iterative synthesis rounds (ADR-005): every proposed security/privacy constraint, the risk it addresses, and the client's per-item verdict. No `Doc01`/`Doc02` version evolves before the register reaches convergence.
> **Normative basis:** `../PHASE3_PROCESS_AND_METHODOLOGY.md` Step 3 (Iterative Synthesis & Risk-Acceptance Rounds); ADR-005.
> **Template:** `templates/phase3_risk_acceptance_register.md`.

---

## Round rules

1. **One proposal per item**: an EARS constraint carrying (a) the risk it addresses, (b) its altitude level (L2 verifiable constraint / L3 mechanism category — guidelines §2.5), (c) its full regulatory chain (`regulation article → Phase 2 rule → PRIN-ENG → candidate anchor`), (d) a Volere Fit Criterion and Verification Method.
2. **Client verdict per item**, recorded verbatim per round: **Accept** · **Reject** · **Adjust** (wording, level, or scope → re-proposed next round).
3. **A rejection is an explicit risk acceptance**: the item stays registered as `Risk-accepted (client decision)` — it is never silently dropped.
4. **Convergence**: a round with no new rejections, or an explicit client decision to close the baseline. Only then do the deliverable versions evolve; control selection (Step 4) follows.
5. Functional refinement-pass items (Step 5b, taxonomy D1–D4) enter the cycle as round proposals like any other.

---

## Round 1 — 2026-09-24 — Proposal (objective-mapping conformance, STEP7)

Derived from [`OBJECTIVE_MAPPING.md`](OBJECTIVE_MAPPING.md): 9 re-drives of existing chains to their natural objectives (ADJ) + 4 new constraints (P). All published control sets cited from the Phase 2 deliverable.

| Item | Proposal (EARS constraint) | Risk addressed | Level | Regulatory chain | Fit criterion / Verification | Client verdict | Notes / adjustment |
|---|---|---|---|---|---|---|---|
| ADJ-1 | Re-drive `RN9` (Multi-Tenant Data Isolation): driver `SO-D-02.1-002` → `SO-D-03.2-002` (protection from unauthorised access); anchors → CSF PR.AA-05, PR.AA-06, DE.CM-09 | Cross-tenant data leakage (IDOR) | L2 | CRA Annex I (2)(d) → `SO-D-03.2-002` → `PRIN-ENG-03` → CSF PR.AA-05, PR.AA-06, DE.CM-09 | 100% of synthetic cross-tenant probes return 403 with zero records leaked · TEST | — | Chain re-anchor (wording unchanged) |
| ADJ-2 | Re-drive `RN11` (Session Management & Invalidation): driver `SO-D-02.2-002` (security updates) → `SO-D-03.1-002` (identity/credential/entitlement management); anchors stay CSF PR.AA-01, PR.AA-05, PR.AA-06 | Session hijacking / replay after logout | L2 | CRA Annex I (2)(d) → `SO-D-03.1-002` → `PRIN-ENG-04` → CSF PR.AA-01, PR.AA-05, PR.AA-06 | Invalidated tokens rejected at protected endpoints · TEST | — | Driver correction |
| ADJ-3 | Re-drive `RN12` (RBAC & Action Mediation): driver `SO-D-02.1-002` → `SO-D-03.3-002` (access limited to authenticated/authorized); anchors → CSF PR.AA-05, PR.AA-06, DE.CM-09 | Privilege escalation | L2 | CRA Annex I (2)(d) → `SO-D-03.3-002` → `PRIN-ENG-03` → CSF PR.AA-05, PR.AA-06, DE.CM-09 | Unauthorized mutations get 403 + audit record · TEST | — | Driver correction |
| ADJ-4 | Re-drive `RN13` (File Upload Strict Validation): driver `SO-D-07.1-002` → `SO-D-07.2-002` (attack-surface limitation); anchors → CSF PR.PS-06, PR.PS-02 | Malicious binary upload / web shell | L2 | CRA Annex I (2)(j) → `SO-D-07.2-002` → `PRIN-ENG-02` → CSF PR.PS-06, PR.PS-02 | Spoofed executables rejected; zero temp files remain · TEST | — | Driver correction |
| ADJ-5 | Re-drive `RN18` (Non-Repudiable Security Audit Logging): driver `SO-D-03.1-002` → `SO-D-10.1-002` (records/monitors internal activity; co-driver `SO-D-04.1-002`); anchors → CSF DE.CM-01, DE.CM-09, ID.IM-04 | Audit tampering / erasure | L2 | CRA Annex I (2)(l) → `SO-D-10.1-002` → `PRIN-ENG-07` → CSF DE.CM-01, DE.CM-09, ID.IM-04 | Log entries immutable; deletion attempts blocked + logged · TEST | — | Driver correction |
| ADJ-6 | Re-base `RN14` (Untrusted Content Neutralization) co-driver: `SO-D-07.1-002` → `SO-D-07.2-002`; anchors → CSF PR.PS-06, PR.PS-02 | Stored script injection | L2 | CRA Annex I (2)(j) → `SO-D-07.2-002` → `PRIN-ENG-04` → CSF PR.PS-06, PR.PS-02 | 100% of stored script-injection vectors rendered inert · TEST | — | Driver correction |
| ADJ-7 | Re-drive `RN15` (Cryptographic Billing Invariant Protection): drivers `SO-D-01.1-002`/`SO-D-08.1-002` → `SO-D-01.4-002` (integrity of data and commands); anchors → CSF PR.DS-10, PR.PS-04 | Forged/fraudulent billing state | L2 | CRA Annex I (2)(l) → `SO-D-01.4-002` → `PRIN-ENG-01` → CSF PR.DS-10, PR.PS-04 | Quota changes occur only on verified receipts · TEST | — | Driver correction |
| ADJ-8 | Re-drive `RN16` (Cryptographic Webhook Origin Verification): drivers `SO-D-05.1-002`/`SO-D-08.1-002` → `SO-D-01.4-002` (message integrity); anchors → CSF PR.DS-10, PR.PS-04 | Forged webhook origin | L2 | CRA Annex I (2)(l) + W1 V0 RN7 → `SO-D-01.4-002` → `PRIN-ENG-01` → CSF PR.DS-10, PR.PS-04 | Unsigned/replayed webhooks rejected · TEST | — | Driver correction |
| ADJ-9 | Extend `RN24` (Cryptographic Protection of Data in Transit) with CRA twin driver `SO-D-01.2-002` alongside `PO-D-01.2-001`; anchors already ∈ both sets (PR.DS-02, PR.IR-01) | Unencrypted transport | L2 | GDPR Art. 32(1)(a)+32(2) + CRA Annex I (2)(e) → `PO-D-01.2-001`, `SO-D-01.2-002` → `PRIN-ENG-01` → CSF PR.DS-02, PR.IR-01 | Unencrypted connection attempts refused/upgraded · TEST | — | Completes the GDPR+CRA pair |
| P-01 | `SO-D-03.1-001` on `R8.1`/`R8.2` (NEW): "When a data-subject request (export or erasure) is submitted, the system shall verify the requester's identity using means proportional to the request before executing it." | Unauthorized exercise of another person's data rights | L2 | GDPR Art. 12(2)/15–22 → `SO-D-03.1-001` → `PRIN-ENG-03` → CSF PR.AA-03, PR.AA-02, PR.DS-10 | Rights requests execute only after identity re-verification · TEST | — | New constraint; adds re-verification step to {U.C. 8.1}/{U.C. 8.2} |
| P-02 | `SO-D-03.4-002` on `R2.1`/`R3.1` (NEW): "Where the product creates a configurable artifact (workspace or project), the system shall apply the restrictive secure-by-default configuration (restricted visibility), permitting later relaxation by authorized users." | Accidental exposure by insecure defaults | L2 | CRA Annex I (2) secure-by-default → `SO-D-03.4-002` → `PRIN-ENG-04` → CSF PR.PS-01, PR.DS-10, GV.SC-03 | New artifacts default to restricted visibility · DEMONSTRATE | — | New constraint; secure-by-default |
| P-03 | `SO-D-05.3-002` on `R8` package (NEW, D1 candidate): "The system must allow the Workspace Owner to permanently delete a workspace and all its data and settings, with confirmation and irreversible erasure." | Retention of organizational data after contract end | L1→L2 | CRA Annex I (2) user data removal → `SO-D-05.3-002` → `PRIN-ENG-07` → CSF PR.DS-10, PR.DS-02 | Deleted workspace data irrecoverable; zero residual records post-erasure · TEST | — | Derived functional requirement candidate (R8.3) + PUC/UC; company-scale reviewed |
| P-04 | `SO-D-08.1-002` on product documentation (NEW, SHOULD): "The system shall provide users and administrators with secure-use instructions (account security, data handling, erasure) via an in-product information address." | Users unaware of secure-use measures | L2 | CRA Annex I (2) instructions for secure use → `SO-D-08.1-002` → `PRIN-ENG-07` → CSF PR.AT-01 | Instructions cover account security, data handling, erasure; reachable in-product · INSPECT | — | SHOULD; light documentation coverage |

---

## Cumulative status

| Item | Final status | Rounds involved | Decision trace |
|---|---|---|---|
| ADJ-1…ADJ-9, P-01…P-04 | **Awaiting client verdicts (Round 1 open)** | R1 | — |

**Status legend:**
- **Accepted** — client accepted the proposal as formulated.
- **Risk-accepted (client decision)** — client rejected the proposal and formally accepts the associated risk; the risk and its owner stay on record.
- **Adjusted** — client required changes; the adjusted formulation re-enters the next round; final status recorded on acceptance.

---

## Convergence record

| Round | Date | New items | Rejections | Outcome |
|---|---|---|---|---|
| 0 (pre-cycle consolidation) | 2026-09-23/24 | 15 absorbed constraints (`RN9`–`RN26`) + 3 cross-cutting (`RN17`, `RN18`, `RN24`) | — | Grandfathered: V1 (19 cards) approved under the one-shot process before ADR-005; treated as the accepted starting position. |
| 1 | 2026-09-24 | 13 (9 adjustments ADJ-1…9 + 4 new P-01…04) | — | **Open — awaiting client verdicts.** |
