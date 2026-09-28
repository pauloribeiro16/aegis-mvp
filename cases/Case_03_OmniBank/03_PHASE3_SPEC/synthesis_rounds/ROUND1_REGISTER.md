# Round 1 Register — Iterative Risk-Acceptance Synthesis (OmniBank Financial Systems)

> **Round window:** opened 2026-09-28 · **Status: OPEN — awaiting client verdicts** (presented in plain business language; this register holds the formulations, chains and IDs).
> **Inputs:** [`OBJECTIVE_MAPPING.md`](OBJECTIVE_MAPPING.md) (134/134 placed) · [`PRINCIPLE_MAPPING.md`](PRINCIPLE_MAPPING.md) · `../v0_functional_baseline/`.
> **Control selection rule (ADR-005 Step 4):** anchors copied only from pre-verified surfaces — the driver objective’s published control set (Phase 2 final column) and the mapping store (`baseline/MAPPINGS/sr_control_mappings/<REG>.json`); PF accompanies GDPR-derived constraints; AI RMF accompanies AI-Act-derived constraints.

## §1 New Constraint Proposals (RN11–RN26)

### RN11 — OmniScore Decision & Model Integrity at Serving (MUST)
- **Risk addressed:** A forged model version or manipulated command at the serving estate could produce wrongful credit decisions at scale.
- **Fit criterion:** Every served decision verifiable against a verified model version; unauthorized modification detected and refused.
- **Verification:** `TEST`.
- **Chain:** GDPR Art. 5(1)(f) · CRA (2)(f)+(l) · AI Act Art. 15 · DORA Art. 9 → PRIN-ENG-07 → CSF PR.DS-01, PR.DS-10, PR.PS-04.
- **Carriers:** `R1.2`, `R8.4`.

### RN12 — Scoring Data Minimization & Purpose Binding (MUST)
- **Risk addressed:** Scope creep into applicant profiling beyond the declared basis.
- **Fit criterion:** Scoring consumes only purpose-bound fields; field inventory reconciles to the declared processing basis.
- **Verification:** `TEST`.
- **Chain:** GDPR Art. 5(1)(c)+Art. 6 · AI Act Art. 10 → PRIN-ENG-06 → CSF PR.PS-01, ID.AM-08.
- **Carriers:** `R1.2`, `R6.1`.

### RN13 — Data-in-Transit Protection (MUST)
- **Risk addressed:** Interception or alteration of customer, inter-service, or authority flows in transit.
- **Fit criterion:** 100% of boundary flows authenticated, encrypted, integrity-verified; unauthenticated channels refused.
- **Verification:** `TEST`.
- **Chain:** GDPR Art. 32(1)(b)+32(2) · CRA (2)(e)+(j) · NIS 2 Art. 21(2)(h) · DORA Art. 9 → PRIN-ENG-01 → CSF PR.DS-02, PR.IR-01.
- **Carriers:** `ALL`.

### RN14 — Data-at-Rest Encryption with Field-Level Protection (MUST)
- **Risk addressed:** Storage compromise exposing customer PII, financial data, or AI datasets.
- **Fit criterion:** All stored estates encrypted at rest; sensitive categories field-level protected; no plaintext retrieval.
- **Verification:** `TEST`.
- **Chain:** GDPR Art. 32(1)(a)+5(1)(f) · CRA (2)(e) · NIS 2 Art. 21(2)(h) · DORA Art. 9 → PRIN-ENG-01 → CSF PR.DS-01, PR.DS-10.
- **Carriers:** `R2.1`.

### RN15 — Key Custody Separation & Cryptographic Destruction (MUST)
- **Risk addressed:** Bundled key custody converts a storage compromise into full re-identification.
- **Fit criterion:** No single role/environment holds data and re-identification material; destruction events evidenced.
- **Verification:** `TEST`.
- **Chain:** GDPR Art. 4(5)+32(1)(a) · CRA (2)(d)+(e) · NIS 2 Art. 21(2)(h) · DORA Art. 9 → PRIN-ENG-03 → CSF PR.DS-01, PR.AA-05.
- **Carriers:** `R2.3`.

### RN16 — Rights-Requester Identity Verification (MUST)
- **Risk addressed:** Rights executed by unauthorized third parties over financial data.
- **Fit criterion:** Every executed request preceded by a recorded proportionate identity verification.
- **Verification:** `TEST`.
- **Chain:** GDPR Art. 12(6)+11(2)+5(1)(c) → PRIN-ENG-01 → CSF PR.AA-03, PR.AA-02 / PF PR.AC-P6.
- **Carriers:** `R6.3`.

### RN17 — Token-Only Decision-Record Retention (MUST)
- **Risk addressed:** Biometric-like direct identifiers surviving erasure vs statutory retention floors.
- **Fit criterion:** Erasure destroys direct identifiers incl. key material; decision records token-only under the longest statutory floor.
- **Verification:** `TEST`.
- **Chain:** GDPR Art. 17+5(1)(e) · AI Act Art. 12 retention leg · statutory floors → PRIN-ENG-07 → CSF PR.DS-10, ID.AM-08 / PF CT.DM-P4.
- **Carriers:** `R6.3`, `R11.2`.

### RN18 — Unified Notification Clock Enforcement (MUST)
- **Risk addressed:** Missed statutory clocks across five notification regimes on one incident.
- **Fit criterion:** 100% of notifiable incidents dispatched per each regime deadline from one recorded clock-start.
- **Verification:** `TEST`.
- **Chain:** GDPR Art. 33(1) · NIS 2 Art. 23 · DORA Art. 19 · CRA Art. 14 · AI Act Art. 73 → PRIN-ENG-05 → CSF RS.MA-04, RS.MA-02, RS.CO-02.
- **Carriers:** `R5.2`.

### RN19 — Strong Privileged-Access Authentication (MUST)
- **Risk addressed:** Single-factor compromise of privileged banking functions.
- **Fit criterion:** 100% of privileged access via policy-strength multi-factor; weaker modalities refused.
- **Verification:** `TEST`.
- **Chain:** NIS 2 Art. 21(2)(j) · CRA (2)(d) · DORA Art. 9 → PRIN-ENG-01 → CSF PR.AA-03, PR.AA-05, PR.AA-06.
- **Carriers:** `R4.2`.

### RN20 — Secure-by-Default Configuration & Reset (MUST)
- **Risk addressed:** Deployments and artifacts born permissive; configuration drift.
- **Fit criterion:** New deployments/artifacts born restrictive; reset restores exactly the default state.
- **Verification:** `TEST`.
- **Chain:** CRA 2(b)+(c) · NIS 2 Art. 21(2)(i)-(j) · GDPR Art. 25(2) → PRIN-ENG-04 → CSF PR.PS-01.
- **Carriers:** `R4.4`, `R8.2`.

### RN21 — AI Platform Access Mediation & Least Privilege (MUST)
- **Risk addressed:** Unauthorized mutation of models, datasets, or serving configuration.
- **Fit criterion:** AI platform roles least-privileged; mutations restricted to authorized roles; denials logged.
- **Verification:** `TEST`.
- **Chain:** CRA (2)(d) · AI Act Art. 15 cybersecurity leg · NIS 2 Art. 21(2)(i)-(j) → PRIN-ENG-03 → CSF PR.AA-05, PR.AA-06.
- **Carriers:** `R4.1`.

### RN22 — Human Oversight Effectiveness (OmniScore) (MUST)
- **Risk addressed:** Rubber-stamp oversight of high-risk credit decisions (AI Act Art. 14).
- **Fit criterion:** Every oversight shift covered by trained, authorized overseers; overrides recorded; oversight cannot be bypassed.
- **Verification:** `DEMONSTRATE`.
- **Chain:** AI Act Art. 14 (provider & deployer duties) → PRIN-ENG-01 → CSF PR.AT-02, PR.AT-01, GV.RR-02.
- **Carriers:** `R1.3`, `R9.2`.

### RN23 — AI Event Logging over Lifetime (MUST)
- **Risk addressed:** Inability to reconstruct AI decisions after the fact (authorities/applicants).
- **Fit criterion:** Automatic logging of decision events over the system lifetime; logs supplied on authority request.
- **Verification:** `TEST`.
- **Chain:** AI Act Art. 12(1)+Art. 19 → PRIN-ENG-07 → CSF PR.PS-04, DE.CM-09, DE.AE-03.
- **Carriers:** `R1.2`, `R11.2`.

### RN24 — Post-Market Monitoring Integration (MUST)
- **Risk addressed:** Field-degraded model behaviour undetected by the risk-management system.
- **Fit criterion:** Monitoring data ingested into the AI risk file with traceable updates; serious-incident triggers escalate.
- **Verification:** `INSPECT`.
- **Chain:** AI Act Art. 72 · DORA ICT-risk feedback loop → PRIN-ENG-02 → CSF DE.CM-09, ID.IM-04.
- **Carriers:** `R10.2`.

### RN25 — AI Adversarial Robustness Measures (MUST)
- **Risk addressed:** Poisoning, evasion, or model-theft success against the scoring estate.
- **Fit criterion:** Adversarial testing covers poisoning/evasion/confidentiality classes; findings drive targeted measures.
- **Verification:** `TEST`.
- **Chain:** AI Act Art. 15(1),(4)-(5) · CRA (2)(l) → PRIN-ENG-02 → CSF ID.RA-04, PR.PS-06, RS.MI-01.
- **Carriers:** `R11.4`.

### RN26 — ICT Third-Party Register Completeness & Criticality (MUST)
- **Risk addressed:** Register gaps on critical ICT third parties (DORA supervisory exposure).
- **Fit criterion:** Register entries complete with criticality classification and kept current.
- **Verification:** `INSPECT`.
- **Chain:** DORA Art. 28-30 · GDPR Art. 28 · NIS 2 Art. 21(3) → PRIN-ENG-05 → CSF GV.SC-04, GV.SC-07, ID.AM-05.
- **Carriers:** `R7.1`.

## §2 Chain-Binding Proposals (92 objectives on existing cards)

Each is a `Security & Privacy Constraints` chain row on the named card — no new RN; the V0 function realizes the objective and the chain makes the derivation explicit (see [`OBJECTIVE_MAPPING.md`](OBJECTIVE_MAPPING.md) rows marked *chain row*).

## §3 Control Selection (Step 4, executed with the proposals)

Per-constraint anchors are selected as subsets of the cited objectives’ published sets (final column of Phase 2 `Doc01`) plus store-flagged selections where the driver publishes none; PF axes from `GDPR.json` (e.g. `SR-GDPR-009` for RN16, `SR-GDPR-030` for RN17) and AI RMF axes from `AI_Act.json` where the verification tooling requires them. Full per-item table fixed at absorption.

## §4 Convergence & Effect

- **Status:** OPEN — client verdicts pending per batch.

- **On convergence:** accepted set absorbed → `Doc01`/`Doc02` V1 (2.0.0) in `v1_security_privacy_synthesis/`; the 43 use cases elaborated to the fully-dressed Cockburn anatomy with the accepted security behavior; coverage totals finalize in `OBJECTIVE_MAPPING.md`.
