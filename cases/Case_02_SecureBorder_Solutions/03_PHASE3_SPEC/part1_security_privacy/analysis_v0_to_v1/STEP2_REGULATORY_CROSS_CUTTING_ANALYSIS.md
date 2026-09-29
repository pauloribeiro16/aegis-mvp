# Step 2 — Regulatory Cross-Cutting Analysis & Constraint Derivation (SecureBorder eGate)

> **Inputs:** Phase 2 spine — 100 objectives (29 `PO-` GDPR / 71 `SO-` across CRA 34, NIS 2 22, AI Act 15) + 7 principles · V0 functional audit (STEP1) · harmonized tensions T-001..T-004.
> **Method:** per functional area, every applicable objective is juxtaposed against the area's cards; gaps become `RN` candidates (EARS, altitude L2, chain `article → objective → PRIN-ENG → anchor`); objectives already realized by existing V0 functions become chain bindings on those carriers. Threat analysis is out of Part 1 (ADR-006).

## 1. The Four Regulatory Ambits over One Fleet

| Ambit | Objective family | Binds on |
|---|---|---|
| **GDPR** (personal data: traveller biometrics + employee data) | `PO-D-01..10` | R1 (biometric lifecycle), R4 (rights, RoPA), R3 (authorized actors), R5/R6 (breach), R10 (assessments, vendors), R11 (awareness) |
| **CRA** (product security: eGate fleet & release artefacts) | `SO-D-* -002` | R1 (data protection in product), R3 (product identity/access), R5 (activity recording, resilience), R6 (exploited-vuln notification), R7 (vuln handling, updates, CVD, testing), R8 (pipeline, SBOM), R9 (support-period docs), R10 (risk assessment) |
| **NIS 2** (essential entity: network & information systems) | `SO-D-* -003` | R3 (workforce identity, MFA, access policy), R5 (incident handling, continuity), R7 (CVD, maintenance), R10 (risk analysis, management-body approval), R11 (training) |
| **AI Act** (high-risk AI: border-control verification) | `SO-D-* -004` | R1 (robustness, logging), R2 (human oversight), R8 (model versioning/rollback), R9 (risk management, accuracy/drift/bias, adversarial testing, transparency, post-market monitoring) |

## 2. New Constraint Candidates (RN11–RN30)

All constraints are altitude L2 (technology-neutral control objectives), with binary fit criteria and ISO 29148 methods. Full formulations and control selections are recorded in [`../synthesis_rounds/ROUND1_REGISTER.md`](../synthesis_rounds/ROUND1_REGISTER.md).

| RN | Candidate constraint (essence) | Chain (article → objectives) | Carrier | Skill |
|---|---|---|---|---|
| RN11 | Biometric templates and decision records encrypted at rest with state-of-the-art mechanisms | GDPR Art. 32(1)(a)+(b)+5(1)(f) → `PO-D-01.1-001` · CRA (2)(e) → `SO-D-01.1-002` | `R1.1`, `R1.3` | TB |
| RN12 | De-linking keys and template seeds held under separated custody, never bundled with the operational environment | GDPR Art. 4(5)+32(1)(a) → `PO-D-01.3-001` · CRA (2)(d)+(e) → `SO-D-01.3-002` | `R1.1`, `R1.2` | LP |
| RN13 | All gate↔back-office↔authority flows cryptographically protected in transit (cross-cutting) | GDPR Art. 32(1)(b)+32(2) → `PO-D-01.2-001` · CRA (2)(e)+(j) → `SO-D-01.2-002` | all UC preconditions; `R1.2`, `R6.1`, `R7.2`, `R9.x` | TB |
| RN14 | Passage decisions, decision records, and notification dossiers integrity-protected; corruption detected and reported | CRA (2)(f)+(l) → `SO-D-01.4-002` | `R1.2`, `R1.3`, `R6.1` | V |
| RN15 | Verification AI resilient to errors/faults with technical redundancy and fail-safe reversion to a safe state | AI Act Art. 15(3) → `SO-D-01.4-004` | `R1.2`, `R8.3`, `R9.2` | FS |
| RN16 | Rights-requester identity verified proportionately before executing Art. 15–22 requests | GDPR Art. 12(6)+11(2)+5(1)(c) → `PO-D-03.1-001` | `R4.1` | TB |
| RN17 | Operator identities and entitlements lifecycle-managed (provisioning, review, revocation) with verified product-side identity handling | NIS 2 Art. 21(2)(i) → `SO-D-03.1-003` · CRA (2)(d)+13(15) → `SO-D-03.1-002` | `R3.1`, `R3.3` | LP |
| RN18 | Operators authenticated with strong/multi-factor mediation per access policy | NIS 2 → `SO-D-03.2-003` · CRA (2)(d) → `SO-D-03.2-002` | `R3.2` | TB |
| RN19 | Authorized actors act under documented instructions and role-mediated entitlements only | GDPR Art. 29+32(4) → `PO-D-03.2-001`, `PO-D-03.3-001` · CRA (2)(d) → `SO-D-03.3-002` · NIS 2 → `SO-D-03.3-003` | `R3.3`, `R2.1` | LP |
| RN20 | New deployments/artifacts born with secure-by-default configuration, resettable to that state | GDPR Art. 25(2) → `PO-D-03.4-001` · CRA 2(b)+(c) → `SO-D-03.4-002` | `R1.2`, `R8.1` | FS |
| RN21 | One unified notification pipeline enforcing the four statutory timelines from a single clock-start discipline (T-001) | GDPR Art. 33(1) → `PO-D-04.3-001` · CRA Art. 14 → `SO-D-04.3-002` · NIS 2 Art. 23 → `SO-D-04.3-003` · AI Act Art. 73 → `SO-D-04.3-004` | `R6.1` | V |
| RN22 | Fleet/gate internal activity recorded and monitored with tamper-evident storage | CRA (2)(l) → `SO-D-04.1-002`, `SO-D-10.1-002` | `R5.1`, `R1.2` | V |
| RN23 | Incident handling closed across the full lifecycle (prevent/detect/analyse/contain/respond/recover) | NIS 2 Art. 21(2)(c) → `SO-D-04.1-003`, `SO-D-04.2-003` | `R5.2`, `R5.3` | AS |
| RN24 | AI system automatically logs events over its lifetime; logs supplied to authorities on demand (T-002 leg) | AI Act Art. 12(1)+19 → `SO-D-10.2-004`, `SO-D-05.2-004` | `R1.2`, `R9.2` | V |
| RN25 | Post-market monitoring data feeds the risk-management system continuously | AI Act Art. 72 → `SO-D-10.1-004` | `R9.2`, `R5.1` | AS |
| RN26 | Breach awareness moment documented and containment measures recorded against the 72 h clock | GDPR Art. 33(1)+33(5) → `PO-D-04.1-001`, `PO-D-04.2-001` | `R5.2`, `R6.1` | V |
| RN27 | Security updates distributed via a secure, separated channel with advisories across the support period | CRA (2)(c)+Part II (7)(8) → `SO-D-07.3-002`, `SO-D-02.2-002`, `SO-D-05.2-002` | `R7.2` | AS |
| RN28 | Traveller erasure without undue delay and structured portability delivery (T-002 leg: token-only records survive) | GDPR Art. 17+20+15(3) → `PO-D-05.3-001`, `PO-D-05.4-001` | `R4.1` | LE |
| RN29 | Human oversight effective: overseers competent, empowered, and able to interpret and override (incl. training leg) | AI Act Art. 14 → `SO-D-08.2-004` | `R2.1`, `R11.2` | TB |
| RN30 | AI operation sufficiently transparent for deployers to interpret a system's output and use it appropriately | AI Act Art. 13 → `SO-D-09.1-004` | `R9.3` | V |

## 3. Chain Bindings on Existing Functional Carriers (51 objectives)

The V0 already elicits the operational capabilities; 51 objectives bind onto those cards directly (chain rows in the cards' `Security & Privacy Constraints` block, no new RN needed):

- **R4.2** carries `PO-D-09.4-001` (RoPA — the card *is* the records function). **R8.2** carries `SO-D-06.2-002` (SBOM). **R7.3** carries `SO-D-02.3-002`/`SO-D-02.3-003` (CVD). **R10.1** carries the unified-assessment family (`PO-D-09.2-001`, `SO-D-09.2-002/003/004`, `SO-D-09.1-003`, `PO-D-09.1-001`, `SO-D-01.1-003`). **R10.2** carries the vendor family (`PO-D-06.1-001`, `SO-D-06.1-002/003`, `PO-D-06.3-001`, `SO-D-06.3-003`, `SO-D-07.1-003`). **R9.1** carries the AI documentation family (`SO-D-02.1-004`, `SO-D-05.1-004`, `SO-D-07.1-004`, `SO-D-09.4-004`, `SO-D-09.2-004` co-driver). **R7.1** carries the vulnerability/testing family (`PO-D-02.1-001`, `SO-D-02.1-002/003`, `SO-D-02.4-002`, `SO-D-07.3-003`, `SO-D-10.3-002` co). **R5.3** carries the resilience/continuity family (`SO-D-04.2-002`, `SO-D-04.4-002/003`, `PO-D-04.4-001`, `PO-D-10.1-001`). **R10.3** carries the documentation/compliance family (`SO-D-09.4-002`, `PO-D-10.2-001`, `SO-D-10.2-002`, `SO-D-10.3-003`, `PO-D-10.3-001`). **R11.1** carries `SO-D-08.1-003`, `SO-D-08.2-003`. **R9.3** carries `SO-D-02.4-004`, `SO-D-07.2-004`, `SO-D-10.3-002/004`. **R1.1** carries `PO-D-05.1-001`, `SO-D-05.1-002`, `PO-D-05.2-001` (retention slices). **R4.1** carries `PO-D-01.4-001`, `SO-D-05.3-002`. **R6.1** carries `SO-D-06.4-003` (cross-border routing). **R7.2** carries `SO-D-08.1-002` (advisories/instructions).
- **Transversal umbrellas:** `PO-D-07.1-001` (DPbD — realized by RN11/RN20 slices) and `SO-D-07.1-002` (CRA Annex I umbrella — realized by RN14/RN27/R8.1 chains).

## 4. Tension Application

1. **T-001 → RN21:** one triage pipeline, one clock-start, four timelines (24 h early warnings; 72 h GDPR/CSIRT; AI Act matrix).
2. **T-002 → RN24 + RN28:** biometric content purged on erasure; token-only decision records retained under the longest statutory floor (V0 RN6).
3. **T-003 → R10.1 chain family:** one evidence pass feeds DPIA + fundamental-rights leg + AI risk file + CRA assessment + NIS 2 analysis.
4. **T-004 → R10.2 chain family:** one due-diligence pass yields processor docs, component records, NIS 2 three-prong assessment.

## 5. Explicit Non-Carriers

- **No functional carrier (organizational, recorded):** `PO-D-08.1-001` (DPO advisory), `PO-D-08.2-001` (DPO compliance monitoring).
- **N/A (recorded):** `SO-D-06.3-002` (importer/distributor duties — the manufacturer places its own product), `PO-D-06.4-001` (EU-established), `SO-D-06.4-002` (EU manufacturer), `SO-D-08.2-002` (product not offered for integration into other products), `SO-D-09.1-002` (not an open-source steward), `SO-D-09.4-003` (addressee: Member States).

## 6. Output

39 objective rows carried by the 20 RN candidates · 51 chain rows on functional carriers · 2 transversal · 2 organizational · 6 N/A = **100/100 placed**. The candidates go to Round 1 for per-item client verdicts.
