# Round 1 Register — Iterative Risk-Acceptance Synthesis (OmniBank Financial Systems)

> **Round window:** opened 2026-09-28 · verdicts 2026-09-29 · **Status: CONVERGED — 16/16 constraint accepts + 92/92 chain-binding accepts by client directive** ("coloca o v2" with the evolution plan; the five plain-language batches stand accepted in full); 0 Rejects, 0 Adjusts.
> **Inputs:** [`OBJECTIVE_MAPPING.md`](OBJECTIVE_MAPPING.md) (134/134 placed) · [`PRINCIPLE_MAPPING.md`](PRINCIPLE_MAPPING.md) · `../v0_functional_baseline/`.
> **Control selection rule (ADR-005 Step 4):** anchors copied only from pre-verified surfaces — the driver objective’s published control set (Phase 2 final column) and the mapping store (`baseline/MAPPINGS/sr_control_mappings/<REG>.json`); PF accompanies GDPR-derived constraints; AI RMF accompanies AI-Act-derived constraints.

## §1 New Constraint Proposals (RN11–RN26)

### RN11 — OmniScore Decision & Model Integrity at Serving (MUST)
- **Risk addressed:** A forged model version or manipulated command at the serving estate could produce wrongful credit decisions at scale.
- **EARS:** When a credit decision is produced, the system shall serve it only from a model version whose integrity has been verified, and shall refuse any model artefact or command whose integrity verification fails.
- **Altitude:** L2 (verifiable control objective; mechanism left to design)
- **Fit criterion:** Every served decision verifiable against a verified model version; unauthorized modification detected and refused.
- **Verification:** `TEST`.
- **Chain:** GDPR Art. 5(1)(f) · CRA (2)(f)+(l) · AI Act Art. 15 · DORA Art. 9 → PRIN-ENG-07 → CSF PR.DS-01, PR.DS-10, PR.PS-04.
- **Carriers:** `R1.2`, `R8.4`.

### RN12 — Scoring Data Minimization & Purpose Binding (MUST)
- **Risk addressed:** Scope creep into applicant profiling beyond the declared basis.
- **EARS:** When the scoring flow is invoked, the system shall consume only the applicant fields bound to the declared processing purposes, and shall record any declared field withheld as out of scope.
- **Altitude:** L2
- **Fit criterion:** Scoring consumes only purpose-bound fields; field inventory reconciles to the declared processing basis.
- **Verification:** `TEST`.
- **Chain:** GDPR Art. 5(1)(c)+Art. 6 · AI Act Art. 10 → PRIN-ENG-06 → CSF PR.PS-01, ID.AM-08.
- **Carriers:** `R1.2`, `R6.1`.

### RN13 — Data-in-Transit Protection (MUST)
- **Risk addressed:** Interception or alteration of customer, inter-service, or authority flows in transit.
- **EARS:** When data crosses a customer, inter-service, third-party, or authority channel, the system shall protect it with state-of-the-art encryption and integrity verification, and shall refuse unauthenticated channels.
- **Altitude:** L2
- **Fit criterion:** 100% of boundary flows authenticated, encrypted, integrity-verified; unauthenticated channels refused.
- **Verification:** `TEST`.
- **Chain:** GDPR Art. 32(1)(b)+32(2) · CRA (2)(e)+(j) · NIS 2 Art. 21(2)(h) · DORA Art. 9 → PRIN-ENG-01 → CSF PR.DS-02, PR.IR-01.
- **Carriers:** `ALL`.

### RN14 — Data-at-Rest Encryption with Field-Level Protection (MUST)
- **Risk addressed:** Storage compromise exposing customer PII, financial data, or AI datasets.
- **EARS:** When personal, financial, or AI-related data is stored, the system shall hold it under at-rest encryption, applying field-level protection to the most sensitive categories, and shall expose no plaintext retrieval.
- **Altitude:** L2
- **Fit criterion:** All stored estates encrypted at rest; sensitive categories field-level protected; no plaintext retrieval.
- **Verification:** `TEST`.
- **Chain:** GDPR Art. 32(1)(a)+5(1)(f) · CRA (2)(e) · NIS 2 Art. 21(2)(h) · DORA Art. 9 → PRIN-ENG-01 → CSF PR.DS-01, PR.DS-10.
- **Carriers:** `R2.1`.

### RN15 — Key Custody Separation & Cryptographic Destruction (MUST)
- **Risk addressed:** Bundled key custody converts a storage compromise into full re-identification.
- **EARS:** When personal data is encrypted or de-linked, the system shall hold the re-identification material under custody separated from the environment that uses the data, and shall evidence every destruction event.
- **Altitude:** L2
- **Fit criterion:** No single role/environment holds data and re-identification material; destruction events evidenced.
- **Verification:** `TEST`.
- **Chain:** GDPR Art. 4(5)+32(1)(a) · CRA (2)(d)+(e) · NIS 2 Art. 21(2)(h) · DORA Art. 9 → PRIN-ENG-03 → CSF PR.DS-01, PR.AA-05.
- **Carriers:** `R2.3`.

### RN16 — Rights-Requester Identity Verification (MUST)
- **Risk addressed:** Rights executed by unauthorized third parties over financial data.
- **EARS:** If a data-subject request to access, rectify, export, or erase personal data is submitted, the system shall verify the requester identity with means proportionate to the mis-identification risk before executing it.
- **Altitude:** L2
- **Fit criterion:** Every executed request preceded by a recorded proportionate identity verification.
- **Verification:** `TEST`.
- **Chain:** GDPR Art. 12(6)+11(2)+5(1)(c) → PRIN-ENG-01 → CSF PR.AA-03, PR.AA-02 / PF PR.AC-P6.
- **Carriers:** `R6.3`.

### RN17 — Token-Only Decision-Record Retention (MUST)
- **Risk addressed:** Biometric-like direct identifiers surviving erasure vs statutory retention floors.
- **EARS:** If a data subject exercises erasure, the system shall permanently destroy the direct identifiers including the de-linking key material, retaining only token-only decision records under the longest applicable statutory floor.
- **Altitude:** L2
- **Fit criterion:** Erasure destroys direct identifiers incl. key material; decision records token-only under the longest statutory floor.
- **Verification:** `TEST`.
- **Chain:** GDPR Art. 17+5(1)(e) · AI Act Art. 12 retention leg · statutory floors → PRIN-ENG-07 → CSF PR.DS-10, ID.AM-08 / PF CT.DM-P4.
- **Carriers:** `R6.3`, `R11.2`.

### RN18 — Unified Notification Clock Enforcement (MUST)
- **Risk addressed:** Missed statutory clocks across five notification regimes on one incident.
- **EARS:** When an incident meets a statutory notification criterion, the system shall dispatch the notifications required by each applicable regime from one recorded clock-start, within that regime deadline.
- **Altitude:** L2
- **Fit criterion:** 100% of notifiable incidents dispatched per each regime deadline from one recorded clock-start.
- **Verification:** `TEST`.
- **Chain:** GDPR Art. 33(1) · NIS 2 Art. 23 · DORA Art. 19 · CRA Art. 14 · AI Act Art. 73 → PRIN-ENG-05 → CSF RS.MA-04, RS.MA-02, RS.CO-02.
- **Carriers:** `R5.2`.

### RN19 — Strong Privileged-Access Authentication (MUST)
- **Risk addressed:** Single-factor compromise of privileged banking functions.
- **EARS:** When a privileged or administrative session is established, the system shall require the authentication strength mandated by the entity access policy and shall refuse weaker modalities.
- **Altitude:** L2
- **Fit criterion:** 100% of privileged access via policy-strength multi-factor; weaker modalities refused.
- **Verification:** `TEST`.
- **Chain:** NIS 2 Art. 21(2)(j) · CRA (2)(d) · DORA Art. 9 → PRIN-ENG-01 → CSF PR.AA-03, PR.AA-05, PR.AA-06.
- **Carriers:** `R4.2`.

### RN20 — Secure-by-Default Configuration & Reset (MUST)
- **Risk addressed:** Deployments and artifacts born permissive; configuration drift.
- **EARS:** When a deployment, artifact, or configuration is created, the system shall initialize it with the most restrictive supported configuration, and shall allow an authorized user to reset it to that state.
- **Altitude:** L2
- **Fit criterion:** New deployments/artifacts born restrictive; reset restores exactly the default state.
- **Verification:** `TEST`.
- **Chain:** CRA 2(b)+(c) · NIS 2 Art. 21(2)(i)-(j) · GDPR Art. 25(2) → PRIN-ENG-04 → CSF PR.PS-01.
- **Carriers:** `R4.4`, `R8.2`.

### RN21 — AI Platform Access Mediation & Least Privilege (MUST)
- **Risk addressed:** Unauthorized mutation of models, datasets, or serving configuration.
- **EARS:** When an actor acts on the AI platform (datasets, training jobs, model artefacts, serving configuration), the system shall enforce least-privilege role mediation and record every denial.
- **Altitude:** L2
- **Fit criterion:** AI platform roles least-privileged; mutations restricted to authorized roles; denials logged.
- **Verification:** `TEST`.
- **Chain:** CRA (2)(d) · AI Act Art. 15 cybersecurity leg · NIS 2 Art. 21(2)(i)-(j) → PRIN-ENG-03 → CSF PR.AA-05, PR.AA-06.
- **Carriers:** `R4.1`.

### RN22 — Human Oversight Effectiveness (OmniScore) (MUST)
- **Risk addressed:** Rubber-stamp oversight of high-risk credit decisions (AI Act Art. 14).
- **EARS:** While the scoring AI operates, the system shall ensure that natural-person overseers are trained and authorized for the decision class and able to interpret, intervene in, and reverse a decision, recording every override.
- **Altitude:** L2
- **Fit criterion:** Every oversight shift covered by trained, authorized overseers; overrides recorded; oversight cannot be bypassed.
- **Verification:** `DEMONSTRATE`.
- **Chain:** AI Act Art. 14 (provider & deployer duties) → PRIN-ENG-01 → CSF PR.AT-02, PR.AT-01, GV.RR-02.
- **Carriers:** `R1.3`, `R9.2`.

### RN23 — AI Event Logging over Lifetime (MUST)
- **Risk addressed:** Inability to reconstruct AI decisions after the fact (authorities/applicants).
- **EARS:** While the scoring AI operates, the system shall automatically record decision events over the system lifetime at a level sufficient to reconstruct a decision on authority request, and shall supply the logs within the statutory deadline.
- **Altitude:** L2
- **Fit criterion:** Automatic logging of decision events over the system lifetime; logs supplied on authority request.
- **Verification:** `TEST`.
- **Chain:** AI Act Art. 12(1)+Art. 19 → PRIN-ENG-07 → CSF PR.PS-04, DE.CM-09, DE.AE-03.
- **Carriers:** `R1.2`, `R11.2`.

### RN24 — Post-Market Monitoring Integration (MUST)
- **Risk addressed:** Field-degraded model behaviour undetected by the risk-management system.
- **EARS:** While the scoring AI operates in the field, the system shall feed post-market monitoring data into the AI risk-management file with traceable updates, and shall escalate on serious-incident triggers.
- **Altitude:** L2
- **Fit criterion:** Monitoring data ingested into the AI risk file with traceable updates; serious-incident triggers escalate.
- **Verification:** `INSPECT`.
- **Chain:** AI Act Art. 72 · DORA ICT-risk feedback loop → PRIN-ENG-02 → CSF DE.CM-09, ID.IM-04.
- **Carriers:** `R10.2`.

### RN25 — AI Adversarial Robustness Measures (MUST)
- **Risk addressed:** Poisoning, evasion, or model-theft success against the scoring estate.
- **EARS:** When a model version enters validation, the system shall test it against the mandated manipulation classes (poisoning, evasion, confidentiality) and shall file every finding with a targeted measure in the risk file.
- **Altitude:** L2
- **Fit criterion:** Adversarial testing covers poisoning/evasion/confidentiality classes; findings drive targeted measures.
- **Verification:** `TEST`.
- **Chain:** AI Act Art. 15(1),(4)-(5) · CRA (2)(l) → PRIN-ENG-02 → CSF ID.RA-04, PR.PS-06, RS.MI-01.
- **Carriers:** `R11.4`.

### RN26 — ICT Third-Party Register Completeness & Criticality (MUST)
- **Risk addressed:** Register gaps on critical ICT third parties (DORA supervisory exposure).
- **EARS:** When an ICT third-party arrangement is established, changed, or reviewed, the system shall maintain the register entry complete, with criticality classification, and keep it current.
- **Altitude:** L2
- **Fit criterion:** Register entries complete with criticality classification and kept current.
- **Verification:** `INSPECT`.
- **Chain:** DORA Art. 28-30 · GDPR Art. 28 · NIS 2 Art. 21(3) → PRIN-ENG-05 → CSF GV.SC-04, GV.SC-07, ID.AM-05.
- **Carriers:** `R7.1`.

## §2 Chain-Binding Proposals (92 objectives on existing cards)

Each is a `Security & Privacy Constraints` chain row on the named card — no new RN; the V0 function realizes the objective and the chain makes the derivation explicit (see [`OBJECTIVE_MAPPING.md`](OBJECTIVE_MAPPING.md) rows marked *chain row*).

## §3 Control Selection (Step 4, executed with the proposals)

Anchors are selected as subsets of the cited objectives’ published control sets (final column of Phase 2 `Doc01`); store-flagged selections cite the SR record explicitly. No anchor sits outside a published set (guard: `scripts/check_traceability.py`, R2).

| Constraint | Selected anchors | Source surface | Rationale |
|---|---|---|---|
| RN11 | PR.DS-01, PR.DS-10, PR.PS-04 | D-01.4 drivers (GDPR/CRA/AI Act) | integrity of stored data and of commands/config; corruption reporting leg |
| RN12 | PR.PS-01, ID.AM-08 | `PO-D-05.1-001` | minimization protective measure + data inventory |
| RN13 | PR.DS-02, PR.IR-01 | D-01.2 drivers (GDPR/CRA/NIS 2/DORA) | transit confidentiality and integrity (identical published sets) |
| RN14 | PR.DS-01, PR.DS-10 | D-01.1 drivers | at-rest confidentiality + data-in-use protection |
| RN15 | PR.DS-01, PR.AA-05 | D-01.3 drivers | key material is restricted data; access enforcement |
| RN16 | PR.AA-03, PR.AA-02 / PF PR.AC-P6 | `PO-D-03.1-001` + store `SR-GDPR-009` | requester authentication; PF axis from the store record |
| RN17 | PR.DS-10, ID.AM-08 / PF CT.DM-P4 | D-05.3/D-10.2 drivers + store `SR-GDPR-030` | erasure destruction path; PF axis from the store record |
| RN18 | RS.MA-04, RS.MA-02, RS.CO-02 | D-04.3 drivers (five regimes) | notification timing and coordination |
| RN19 | PR.AA-03, PR.AA-05, PR.AA-06 | D-03.2 drivers | strong authentication + access enforcement |
| RN20 | PR.PS-01 | D-03.4 drivers | secure-by-default protective measure |
| RN21 | PR.AA-05, PR.AA-06 | D-03.1 drivers | least-privilege entitlement enforcement |
| RN22 | PR.AT-02, PR.AT-01, GV.RR-02 | `SO-D-08.2-004` | oversight competence, roles, and responsibilities |
| RN23 | PR.PS-04, DE.CM-09, DE.AE-03 | D-10.2 drivers (CRA/AI Act) | log recording + monitoring + analysis |
| RN24 | DE.CM-09, ID.IM-04 | D-10.1/D-09.2 drivers | post-market monitoring into the risk loop |
| RN25 | ID.RA-04, PR.PS-06, RS.MI-01 | D-02.1/D-02.4/D-07.1/D-07.2/D-10.3 drivers | AI-specific vulnerability response + protective measure |
| RN26 | GV.SC-02, GV.SC-03, ID.AM-04 | D-06.1/D-06.4 drivers (GDPR/NIS 2/DORA) | supplier roles, communication, and ICT asset inventory |

Store-flagged selections: `SR-GDPR-009` (rights-request identity verification: nist_csf PR.AA-03, PR.AA-02; nist_pf PR.AC-P6, PR.AC-P3) and `SR-GDPR-030` (right-to-erasure with cryptographic key destruction: nist_csf PR.DS-10, ID.AM-08; nist_pf CT.DM-P4, CT.DM-P5), both in `baseline/MAPPINGS/sr_control_mappings/GDPR.json`.

## §4 Convergence & Effect

- **Convergence:** the client directed the completion ("coloca o v2"), accepting all five presented batches in full — 16/16 new constraints (RN11–RN26) and 92/92 chain bindings; zero rejections (no explicit risk-acceptance entries), zero adjustments; no Round 2 required for this item set.

- **On convergence:** accepted set absorbed → `Doc01`/`Doc02` V1 (2.0.0) in `v1_security_privacy_synthesis/`; the 43 use cases elaborated to the fully-dressed Cockburn anatomy with the accepted security behavior; coverage totals finalize in `OBJECTIVE_MAPPING.md`.
