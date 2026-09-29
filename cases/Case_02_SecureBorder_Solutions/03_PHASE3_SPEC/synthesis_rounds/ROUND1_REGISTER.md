# Round 1 Register — Iterative Risk-Acceptance Synthesis (SecureBorder eGate)

> **Round window:** opened 2026-09-28 · verdicts collected 2026-09-28 · **Status: CONVERGED — 20/20 constraint accepts + 51/51 chain-binding accepts; 0 Rejects, 0 Adjusts; no Round 2 required.**
> **Inputs:** [`OBJECTIVE_MAPPING.md`](OBJECTIVE_MAPPING.md) (100/100 objectives placed) · [`../analysis_v0_to_v1/STEP2_REGULATORY_CROSS_CUTTING_ANALYSIS.md`](../analysis_v0_to_v1/STEP2_REGULATORY_CROSS_CUTTING_ANALYSIS.md) (derivation) · `../v0_functional_baseline/` (locked baseline).
> **Effect on acceptance:** accepted items are absorbed into `Doc01`/`Doc02` → V1 (`v1_security_privacy_synthesis/`); rejections stay recorded as explicit risk acceptances; `v0_functional_baseline/` remains untouched.
> **Control selection rule (ADR-005 Step 4):** anchors copied only from pre-verified surfaces — the driver objective's published control set (Phase 2 `Doc01` final column) and the mapping store (`baseline/MAPPINGS/sr_control_mappings/<REG>.json`). PF 1.1 accompanies GDPR-derived obligations; AI RMF accompanies AI-Act-derived obligations (R2/R8).

---

## §1 New Constraint Proposals (RN11–RN30)

Each proposal: EARS constraint (altitude L2), risk addressed, Volere fit criterion, verification method, full chain, selected control anchors (published sets; store-sourced anchors flagged).

### RN11 — Biometric Template Protection at Rest (MUST)
- **EARS:** When a biometric verification template or a passage decision record is stored at rest, the system shall protect it with state-of-the-art encryption calibrated to the five Art. 32(1) factors.
- **Risk:** extracted biometric templates are special-category personal data; a storage compromise re-identifies travellers.
- **Fit criterion:** 100% of stored templates and decision records encrypted at rest; no plaintext representation retrievable. **Verification:** `TEST`.
- **Chain:** GDPR Art. 32(1)(a)+(b)+5(1)(f) → `PO-D-01.1-001`; CRA Annex I (2)(e) → `SO-D-01.1-002` → PRIN-ENG-01 → CSF PR.DS-01, PR.DS-10.
- **Carriers:** `R1.1`, `R1.3`.

### RN12 — Cryptographic Key Custody Separation (MUST)
- **EARS:** Where biometric templates are de-linked or personal data encrypted, the system shall hold the re-identification information (keys, seeds, mapping tables) under custody separated from the operational environment that uses the data.
- **Risk:** bundled key custody converts a strong-encryption compromise into full re-identification.
- **Fit criterion:** no single role or environment holds both data and re-identification material. **Verification:** `TEST`.
- **Chain:** GDPR Art. 4(5)+32(1)(a) → `PO-D-01.3-001`; CRA (2)(d)+(2)(e) → `SO-D-01.3-002` → PRIN-ENG-03 → CSF PR.DS-01, PR.AA-05.
- **Carriers:** `R1.1`, `R1.2`.

### RN13 — Data-in-Transit Protection (MUST; cross-cutting, Table 7)
- **EARS:** When data crosses the gate↔back-office, back-office↔authority, or fleet↔update channels, the system shall protect it with state-of-the-art transit encryption and integrity verification, refusing unauthenticated channels.
- **Risk:** interception or alteration of biometric flows, decision records, notifications, or update packages in transit.
- **Fit criterion:** 100% of external-boundary flows authenticated and encrypted; unencrypted attempts refused. **Verification:** `TEST`.
- **Chain:** GDPR Art. 32(1)(b)+32(2) → `PO-D-01.2-001`; CRA (2)(e)+(j) → `SO-D-01.2-002` → PRIN-ENG-01 → CSF PR.DS-02, PR.IR-01.
- **Carriers:** all UC preconditions; `R1.2`, `R6.1`, `R7.2`, `R9.x`.

### RN14 — Record & Command Integrity Protection (MUST)
- **EARS:** If any stored record, transmitted message, command, or configuration of the gate system is modified without authorization, the system shall detect the corruption, report it, and refuse to act on the affected data.
- **Risk:** forged passage decisions or notification dossiers; manipulated gate commands.
- **Fit criterion:** every unauthorized modification detected and reported; corrupted inputs never acted upon. **Verification:** `TEST`.
- **Chain:** CRA (2)(f)+(l) → `SO-D-01.4-002` → PRIN-ENG-07 → CSF PR.DS-01, PR.DS-10, PR.PS-04.
- **Carriers:** `R1.2`, `R1.3`, `R6.1`.

### RN15 — AI Model Resilience & Fail-Safe Reversion (MUST)
- **EARS:** If the verification AI enters an error, fault, or inconsistent state, the system shall keep the gate in a safe closed state and shall revert to the last verified model version through the rollback mechanism.
- **Risk:** a degraded or corrupted model produces wrongful passage decisions at a critical-infrastructure boundary.
- **Fit criterion:** 100% of fault states end in a safe closed state; rollback restores the last verified version. **Verification:** `TEST`.
- **Chain:** AI Act Art. 15(3) → `SO-D-01.4-004` → PRIN-ENG-04 → CSF PR.IR-03, PR.IR-04, PR.DS-11.
- **Carriers:** `R1.2`, `R8.3`, `R9.2`.

### RN16 — Rights-Requester Identity Verification (MUST)
- **EARS:** If a traveller or employee submits a data-subject request (Art. 15–22), the system shall verify the requester's identity with means proportionate to the mis-identification risk before executing it.
- **Risk:** rights executed by unauthorized third parties over biometric data.
- **Fit criterion:** every executed request preceded by a recorded successful verification. **Verification:** `TEST`.
- **Chain:** GDPR Art. 12(6)+11(2)+5(1)(c) → `PO-D-03.1-001` → PRIN-ENG-01 → CSF PR.AA-03, PR.AA-02.
- **Carriers:** `R4.1`.

### RN17 — Operator Identity Lifecycle Management (MUST)
- **EARS:** When an operator is inducted, changes role, or separates, the system shall provision, review, or revoke the operator's identities and entitlements accordingly, including the product-side unique identification of services and integrated components.
- **Risk:** orphaned or over-privileged operator identities on a border-control system.
- **Fit criterion:** 100% of lifecycle events produce the matching entitlement state within the policy window. **Verification:** `TEST`.
- **Chain:** NIS 2 Art. 21(2)(i) → `SO-D-03.1-003`; CRA (2)(d)+13(15) → `SO-D-03.1-002` → PRIN-ENG-03 → CSF PR.AA-01, PR.AA-05.
- **Carriers:** `R3.1`, `R3.3`.

### RN18 — Strong Operator Authentication (MUST)
- **EARS:** When an operator or integrated service authenticates to the back-office, the system shall require multi-factor or continuous authentication per the entity access policy, and shall refuse weaker modalities.
- **Risk:** single-factor compromise of an oversight or administration function.
- **Fit criterion:** 100% of privileged accesses via the policy-mandated authentication strength. **Verification:** `TEST`.
- **Chain:** NIS 2 → `SO-D-03.2-003`; CRA (2)(d) → `SO-D-03.2-002` → PRIN-ENG-01 → CSF PR.AA-03, PR.AA-05, PR.AA-06.
- **Carriers:** `R3.2`.

### RN19 — Authorized-Actor Instruction Mediation (MUST)
- **EARS:** Before an actor processes personal data or performs an access-controlled action, the system shall verify that the actor is authorized for that action under documented instructions and role assignments, refusing all else.
- **Risk:** processing outside documented instructions (processor duty) or role overreach.
- **Fit criterion:** 100% of actions mediated by the role/instruction check; denials logged. **Verification:** `TEST`.
- **Chain:** GDPR Art. 29+32(4) → `PO-D-03.2-001`, `PO-D-03.3-001`; CRA (2)(d) → `SO-D-03.3-002`; NIS 2 → `SO-D-03.3-003` → PRIN-ENG-03 → CSF PR.AA-05, PR.AA-06.
- **Carriers:** `R3.3`, `R2.1`.

### RN20 — Secure-by-Default Configuration & Reset (MUST)
- **EARS:** When a gate deployment, verification configuration, or pipeline artifact is created, the system shall initialize it with the most restrictive supported configuration, and the system shall allow an authorized user to reset to that default.
- **Risk:** per-airport deployments born permissive; configuration drift across the fleet.
- **Fit criterion:** every new deployment/artifact starts at the restrictive default; reset restores it exactly. **Verification:** `TEST`.
- **Chain:** GDPR Art. 25(2) → `PO-D-03.4-001`; CRA 2(b)+(c) → `SO-D-03.4-002` → PRIN-ENG-04 → CSF PR.PS-01.
- **Carriers:** `R1.2`, `R8.1`.

### RN21 — Unified Regulatory Notification Timeline Enforcement (MUST; T-001)
- **EARS:** When an incident record reaches the notification stage, the system shall route it to the competent authorities under the four applicable timelines from one clock-start discipline — early warnings within 24 hours, supervisory/CSIRT notifications within 72 hours, and serious-incident reports per the AI Act matrix.
- **Risk:** missed statutory clocks across four regimes on one incident (multi-regulation notification).
- **Fit criterion:** 100% of notifiable incidents dispatched within the tightest applicable deadline; one clock-start recorded per incident. **Verification:** `TEST`.
- **Chain:** GDPR Art. 33(1) → `PO-D-04.3-001`; CRA Art. 14 → `SO-D-04.3-002`; NIS 2 Art. 23 → `SO-D-04.3-003`; AI Act Art. 73 → `SO-D-04.3-004` → PRIN-ENG-05 → CSF RS.MA-04, RS.MA-02, RS.CO-02.
- **Carriers:** `R6.1`.

### RN22 — Product Activity Recording & Tamper Evidence (MUST)
- **EARS:** When gate or back-office internal activity relevant to security occurs (access to or modification of data, services, or functions), the system shall record it in tamper-evident storage and make it available for monitoring.
- **Risk:** undetectable manipulation of gate activity or decision data.
- **Fit criterion:** 100% of relevant events recorded; tamper attempts detectable. **Verification:** `TEST`.
- **Chain:** CRA (2)(l) → `SO-D-04.1-002`, `SO-D-10.1-002` → PRIN-ENG-07 → CSF DE.CM-01, DE.CM-09.
- **Carriers:** `R5.1`, `R1.2`.

### RN23 — Incident-Handling Lifecycle Closure (MUST)
- **EARS:** When an incident is handled, the system shall support and record closure across all six lifecycle actions — prevention, detection, analysis, containment, response, and recovery — with CSIRT-ready evidence.
- **Risk:** partial incident handling leaves root causes unaddressed; evidence gaps vs CSIRT.
- **Fit criterion:** 100% of closed incidents have evidence for all six actions. **Verification:** `INSPECT`.
- **Chain:** NIS 2 Art. 21(2)(b) + Art. 6(8) → `SO-D-04.1-003`, `SO-D-04.2-003` → PRIN-ENG-02 → CSF RS.MA-01, RS.AN-03.
- **Carriers:** `R5.2`, `R5.3`.

### RN24 — AI Event Logging over Lifetime (MUST; T-002 leg)
- **EARS:** While the verification AI operates, the system shall automatically record events over the system lifetime at a level of detail sufficient for authority requests, keeping logs for at least the statutory floor.
- **Risk:** inability to reconstruct AI decisions after the fact (authorities/travellers).
- **Fit criterion:** 100% of decision events logged; logs supplied on authority request within the statutory deadline. **Verification:** `TEST`.
- **Chain:** AI Act Art. 12(1)+19 → `SO-D-10.2-004`, `SO-D-05.2-004` → PRIN-ENG-07 → CSF PR.PS-04, DE.CM-09, DE.AE-03.
- **Carriers:** `R1.2`, `R9.2`.

### RN25 — AI Post-Market Monitoring Integration (MUST)
- **EARS:** While the verification AI operates in the field, the system shall feed post-market monitoring data into the AI risk-management system continuously and on serious-incident triggers.
- **Risk:** field-degraded model behaviour undetected by the provider's risk system.
- **Fit criterion:** 100% of monitoring data ingested into the risk-management file with traceable updates. **Verification:** `INSPECT`.
- **Chain:** AI Act Art. 72 → `SO-D-10.1-004` → PRIN-ENG-02 → CSF DE.CM-09, ID.IM-04.
- **Carriers:** `R9.2`, `R5.1`.

### RN26 — Breach Awareness & Containment Record (MUST)
- **EARS:** If a personal-data breach is detected, the system shall record the awareness moment and the containment/mitigation measures taken, anchoring the 72-hour notification clock.
- **Risk:** undocumented clock-start invalidates the breach defence; unrecorded containment gaps.
- **Fit criterion:** 100% of breaches carry a recorded awareness timestamp and containment record. **Verification:** `INSPECT`.
- **Chain:** GDPR Art. 33(1)+33(5) → `PO-D-04.1-001`, `PO-D-04.2-001` → PRIN-ENG-07 → CSF DE.CM-01, RS.MI-01, RS.MA-02.
- **Carriers:** `R5.2`, `R6.1`.

### RN27 — Secure Update Distribution across Support Period (MUST)
- **EARS:** When a security update is released, the system shall distribute it to the fleet via a secure, separated channel without delay, accompanied by advisory messages, and shall keep updates and advisories available across the support period.
- **Risk:** fleet running vulnerable firmware/models; unsigned or mixed channels.
- **Fit criterion:** 100% of updates via the secure separated channel; availability window ≥ statutory floor. **Verification:** `TEST`.
- **Chain:** CRA (2)(c)+Part II (7)(8) → `SO-D-07.3-002`, `SO-D-02.2-002`, `SO-D-05.2-002` → PRIN-ENG-02 → CSF ID.AM-02, GV.SC-03.
- **Carriers:** `R7.2`.

### RN28 — Traveller Erasure & Portability Delivery (MUST; T-002 leg)
- **EARS:** If a traveller exercises the rights of erasure or portability, the system shall erase personal data without undue delay (templates and raw-capture derivatives permanently destroyed, including the de-linking key material) or deliver the structured, machine-readable export, keeping only token-only decision records under the longest statutory floor.
- **Risk:** biometric content surviving beyond the erasure duty; non-compliant export formats.
- **Fit criterion:** 100% of erasure requests remove biometric content including key material; exports validated as structured and machine-readable. **Verification:** `TEST`.
- **Chain:** GDPR Art. 17+20+15(3) → `PO-D-05.3-001`, `PO-D-05.4-001` → PRIN-ENG-07 → CSF PR.DS-10, ID.AM-08 / PF CT.DM-P4 (anchors from the objective's published set — `PO-D-05.4-001`: PR.DS-10, ID.AM-08 — and the mapping store `SR-GDPR-030` "Right-to-erasure with cryptographic key-destruction deletion path": nist_csf PR.DS-10, ID.AM-08; nist_pf CT.DM-P4, CT.DM-P5).
- **Carriers:** `R4.1`.

### RN29 — Human Oversight Effectiveness (MUST)
- **EARS:** When the verification AI operates, the system shall ensure that the natural-person overseers are able to effectively oversee its operation — competence maintained through training, authority to intervene/suspend/reverse, and an interface enabling interpretation of outputs — and shall treat override actions as first-class recorded decisions.
- **Risk:** rubber-stamp oversight (AI Act Art. 14 core risk) at an automated border boundary.
- **Fit criterion:** 100% of oversight shifts covered by trained overseers with intervention authority; overrides recorded. **Verification:** `DEMONSTRATE`.
- **Chain:** AI Act Art. 14 → `SO-D-08.2-004` → PRIN-ENG-01 → CSF PR.AT-02, PR.AT-01, GV.RR-02.
- **Carriers:** `R2.1`, `R11.2`.

### RN30 — AI Transparency & Deployer Interpretability (MUST)
- **EARS:** When an AI decision is produced or explained, the system shall provide the deployer with sufficiently transparent information to interpret the system's output and use it appropriately, per the instructions-for-use scope.
- **Risk:** deployers misreading gate decisions; Art. 13 conformity gap.
- **Fit criterion:** every decision class carries interpretability information per the documented scope. **Verification:** `INSPECT`.
- **Chain:** AI Act Art. 13 → `SO-D-09.1-004` → PRIN-ENG-05 → CSF GV.OC-03, GV.RM-01.
- **Carriers:** `R9.3`.

---

## §2 Chain-Binding Proposals (51 objectives on existing cards)

Each is a `Security & Privacy Constraints` chain row on the named card — no new RN; the card's existing functionality realizes the objective and the chain makes the derivation explicit. Full list in [`OBJECTIVE_MAPPING.md`](OBJECTIVE_MAPPING.md) (rows marked *chain row*); rationale: the V0 elicitation for a RIGOROUS-tier essential entity already carries the operational capabilities.

## §3 Control Selection (Step 4, executed with the proposals)

| Constraint | Selected anchors | Source surface | Rationale |
|---|---|---|---|
| RN11 | PR.DS-01, PR.DS-10 | Published sets: `PO-D-01.1-001` (PR.DS-01, PR.DS-10), `SO-D-01.1-002` (PR.DS-01) | at-rest confidentiality + data-in-use protection |
| RN12 | PR.DS-01, PR.AA-05 | `PO-D-01.3-001` (PR.DS-01, PR.IR-03), `SO-D-01.3-002` (PR.DS-01, PR.AA-05, GV.OV-01) | key material is data-at-rest + access-restricted asset |
| RN13 | PR.DS-02, PR.IR-01 | `PO-D-01.2-001` = `SO-D-01.2-002` published sets | transit protection — identical sets |
| RN14 | PR.DS-01, PR.DS-10, PR.PS-04 | `SO-D-01.4-002` published set | integrity of data + corruption reporting leg |
| RN15 | PR.IR-03, PR.IR-04, PR.DS-11 | `SO-D-01.4-004` published set | AI resilience/redundancy anchors as published |
| RN16 | PR.AA-03, PR.AA-02 | `PO-D-03.1-001` published set | requester authentication controls |
| RN17 | PR.AA-01, PR.AA-05 | `SO-D-03.1-003` (PR.AA-01, PR.AA-05, PR.AT-02), `SO-D-03.1-002` | identity provisioning + entitlement enforcement |
| RN18 | PR.AA-03, PR.AA-05, PR.AA-06 | `SO-D-03.2-003` + `SO-D-03.2-002` published sets | MFA + access enforcement |
| RN19 | PR.AA-05, PR.AA-06 | common set of the four drivers | instruction/role mediation enforcement |
| RN20 | PR.PS-01 | `SO-D-03.4-002` (PR.PS-01, ID.AM-08, GV.SC-03), `PO-D-03.4-001` (PR.PS-01, ID.AM-08) | secure-by-default protective measure |
| RN21 | RS.MA-04, RS.MA-02, RS.CO-02 | union of the four notification drivers' published sets | notification timing + coordination |
| RN22 | DE.CM-01, DE.CM-09 | `SO-D-04.1-002` + `SO-D-10.1-002` published sets | activity monitoring |
| RN23 | RS.MA-01, RS.AN-03 | `SO-D-04.1-003` + `SO-D-04.2-003` published sets | incident handling lifecycle |
| RN24 | PR.PS-04, DE.CM-09, DE.AE-03 | `SO-D-10.2-004` (PR.PS-04 (primary), DE.CM-09, DE.AE-03, ...), `SO-D-05.2-004` (PR.PS-04, GV.PO-02) | AI log recording + monitoring |
| RN25 | DE.CM-09, ID.IM-04 | `SO-D-10.1-004` (DE.CM-09 (primary), ID.IM-04, ...) | post-market monitoring |
| RN26 | DE.CM-01, RS.MI-01, RS.MA-02 | `PO-D-04.1-001` (DE.CM-01, DE.CM-09, RS.MA-02), `PO-D-04.2-001` (RS.MI-01, RS.MI-02, PR.DS-01) | awareness detection + containment + clock anchor |
| RN27 | ID.AM-02, GV.SC-03 | `SO-D-07.3-002` published set (ID.AM-02, GV.SC-03) | software asset identification + secure distribution governance |
| RN28 | PR.DS-10, ID.AM-08 / PF CT.DM-P4 | `PO-D-05.4-001` published set (PR.DS-10, ID.AM-08) + store `SR-GDPR-030` (nist_pf CT.DM-P4, CT.DM-P5) | erasure/destruction path (store-flagged selection: driver `PO-D-05.3-001` publishes no anchors) |
| RN29 | PR.AT-02, PR.AT-01, GV.RR-02 | `SO-D-08.2-004` published set | oversight competence + roles |
| RN30 | GV.OC-03, GV.RM-01 | `SO-D-09.1-004` published set (GV.PO-01 (primary), GV.OC-03, GV.OC-04, GV.RM-01, GV.RM-04) | transparency governance |

Integrity note: store-flagged selections (RN28) cite the exact SR record; all others are subsets of published sets — no out-of-set anchor.

## §4 Convergence & Effect

- **Convergence:** the client accepted all batches in plain business language on 2026-09-28 — 20/20 new constraints (RN11–RN30) and 51/51 chain bindings; zero rejections (no explicit risk-acceptance entries) and zero adjustments; the round closed with no Round 2.
- **Effect:** the accepted set is absorbed into `Doc01`/`Doc02` 2.0.0 in `v1_security_privacy_synthesis/` (top-level docs kept as synced active copies); coverage totals finalize in `OBJECTIVE_MAPPING.md` (92 covered / 2 organizational / 6 N/A = 100).
- **On convergence:** accepted set absorbed → `Doc01`/`Doc02` V1 (2.0.0) in `v1_security_privacy_synthesis/`; the 28 use cases are elaborated to the fully-dressed Cockburn anatomy with the accepted security preconditions/extensions; coverage totals finalize in `OBJECTIVE_MAPPING.md`.
