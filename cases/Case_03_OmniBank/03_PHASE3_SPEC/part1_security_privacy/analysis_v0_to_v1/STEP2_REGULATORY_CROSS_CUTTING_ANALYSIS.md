# Step 2 — Regulatory Cross-Cutting Analysis & Constraint Derivation (OmniBank Financial Systems)

> **Inputs:** Phase 2 spine — 134 objectives (29 `PO-` GDPR · 36 `SO-` CRA · 24 `SO-` NIS 2 · 30 `SO-` DORA · 15 `SO-` AI Act) + 7 principles · V0 functional audit (STEP1) · harmonized tensions T-001..T-005.
> **Method:** per functional area, every applicable objective is juxtaposed against the area's cards; gaps become `RN` candidates (EARS, altitude L2, chain `article → objective → PRIN-ENG → anchor`); objectives already realized by existing V0 functions become chain bindings on those carriers. Threat analysis is out of Part 1 (ADR-006).

## 1. The Five Regulatory Ambits over One Platform

| Ambit | Objective rows | Binds on |
|---|---|---|
| **GDPR** (customer PII, transactions, credit scores) | 29 | R1 (biometric-free but personal data), R4 (rights, RoPA), R3 (authorized actors), R5/R6 (breach, erasure, retention), R7 (processors), R10 (DPIA), R11 (awareness) |
| **CRA** (product security: mobile app, web platform, releases) | 36 | R1 (data protection in product), R3 (product identity/access), R5 (activity recording, resilience), R6 (permanent removal), R7 (SBOM, CVD), R8 (pipeline, attack surface), R9 (advisories/instructions), R10 (risk assessment) |
| **NIS 2** (essential entity — banking) | 24 | R3 (workforce identity, MFA, access policy), R5 (incident handling, continuity), R7 (vuln handling, maintenance), R9/R11 (training, testing), R10 (management-body approval, risk analysis) |
| **DORA** (financial entity — credit institution + PSP) | 30 | R5 (ICT incident management), R7 (**register of ICT third-party providers**, contractual arrangements), R8 (**ICT change management**), R10 (ICT risk-management framework), R11 (**resilience testing incl. TLPT**), R2 (ICT protection) |
| **AI Act** (OmniScore — **provider and deployer**) | 15 | R1 (decision & model integrity), R2/R6 (data governance), R8 (AI pipeline integrity, model versioning), R9 (**risk management, accuracy/drift/bias, adversarial testing, transparency, post-market monitoring**), R11 (explainability) |

## 2. New Constraint Candidates (RN11–RN26)

All constraints are altitude L2 (technology-neutral control objectives), with binary fit criteria and ISO 29148 methods. Full EARS formulations and control selections: [`../synthesis_rounds/ROUND1_REGISTER.md`](../synthesis_rounds/ROUND1_REGISTER.md) §1 and §3.

| RN | Candidate constraint (essence) | Chain (articles → objectives) | Carrier | Skill |
|---|---|---|---|---|
| RN11 | OmniScore decision & model integrity at serving | GDPR 5(1)(f) · CRA (2)(f)+(l) · AI Act 15 → D-01.4 | `R1.2`, `R8.4` | V |
| RN12 | Scoring data minimization & purpose binding | GDPR 5(1)(c)+6 · AI Act 10 → D-05.1 | `R1.2`, `R6.1` | DM |
| RN13 | Data-in-transit protection (cross-cutting) | GDPR 32(1)(b)+32(2) · CRA (2)(e)+(j) · NIS 2 21(2)(h) · DORA 9 → D-01.2 | all UC preconditions | TB |
| RN14 | Data-at-rest encryption, field-level for sensitive categories | GDPR 32(1)(a)+5(1)(f) · CRA (2)(e) · NIS 2 21(2)(h) · DORA 9 → D-01.1 | `R2.1` | TB |
| RN15 | Key custody separation & cryptographic destruction | GDPR 4(5)+32(1)(a) · CRA (2)(d)+(e) · NIS 2 21(2)(h) · DORA 9 → D-01.3 | `R2.3` | LP |
| RN16 | Rights-requester identity verification | GDPR 12(6)+11(2)+5(1)(c) → `PO-D-03.1-001` | `R6.3` | TB |
| RN17 | Token-only decision-record retention (T-002) | GDPR 17+5(1)(e) · AI Act 12(1)+19 → D-05.3 | `R6.3`, `R11.2` | LE |
| RN18 | Unified notification clock enforcement (T-001) | GDPR 33(1) · CRA 14 · NIS 2 23 · DORA 19 · AI Act 73 → D-04.3 | `R5.2` | V |
| RN19 | Strong privileged-access authentication | NIS 2 21(2)(j) · CRA (2)(d) · DORA 9 → D-03.2 | `R4.2` | TB |
| RN20 | Secure-by-default configuration & reset | CRA 2(b)+(c) · NIS 2 21(2)(i)-(j) · GDPR 25(2) → D-03.4 | `R4.4`, `R8.2` | FS |
| RN21 | AI platform access mediation & least privilege | CRA (2)(d) · AI Act 15 · NIS 2 21(2)(i)-(j) → D-03.1 | `R4.1` | LP |
| RN22 | Human oversight effectiveness (Art. 14) | AI Act 14 → `SO-D-08.2-004` | `R1.3`, `R9.2` | TB |
| RN23 | AI event logging over lifetime | AI Act 12(1)+19 → D-10.2 | `R1.2`, `R11.2` | V |
| RN24 | Post-market monitoring integration | AI Act 72 · DORA 6(3), 8 → D-10.1, D-09.2 | `R10.2` | AS |
| RN25 | AI adversarial robustness measures | AI Act 9(6)-(7)+15(1),(4)-(5) · CRA (2)(l) → D-02.1, D-02.4, D-07.1, D-07.2, D-10.3 | `R11.4` | AS |
| RN26 | ICT third-party register completeness & criticality | DORA 28-30 · GDPR 28 · NIS 2 21(3) → D-06.1, D-06.4 | `R7.1` | V |

## 3. Chain Bindings on Existing Functional Carriers (92 rows)

The V0 already elicits the operating functions; 92 objectives bind onto those cards directly as `Security & Privacy Constraints` chain rows (rows marked *chain row* in [`../synthesis_rounds/OBJECTIVE_MAPPING.md`](../synthesis_rounds/OBJECTIVE_MAPPING.md)), including the DORA legs: **ICT change management** (`R8.3` → `SO-D-07.4-002`), **resilience testing incl. TLPT** (`R3.4`/`R11.3` → D-02.4 / D-10.3 DORA rows), **register of information on ICT third-party providers** (`R7.1` → RN26), and **ICT risk-management framework** (`R10.2` → D-09.2 DORA row).

## 4. Tension Application

1. **T-001 → RN18:** one incident triage record, one clock-start, five regimes' timelines (GDPR 72 h; NIS 2 24 h/72 h/1 month; DORA initial 4 h / intermediate 72 h / final 1 month; CRA three-tier; AI Act serious-incident matrix) — realized in `{U.C. 5.2}`.
2. **T-002 → RN17 + RN24:** erasure destroys direct identifiers including key material; token-only decision records retained under the longest statutory floor — realized in `{U.C. 6.3}` and `{U.C. 6.2}`.
3. **T-003 → R10.2 chain family:** one evidence pass feeds the DPIA, the CRA assessment, the NIS 2 analysis, the DORA ICT-risk framework output, and the AI risk-management leg.
4. **T-004 → R7.1 + R10.2 chain families:** one due-diligence pass yields processor documentation, component records, the NIS 2 three-prong assessment, and the DORA register entries.
5. **T-005 → R10.2 + R9.1/R11.4:** one AI compliance file evidences both the provider duty set (Art. 16, conformity, registration) and the deployer duty set (Art. 26, oversight, monitoring) for OmniScore.

## 5. Explicit Non-Carriers

- **No functional carrier (organizational, recorded):** `PO-D-08.1-001` (DPO advisory), `PO-D-08.2-001` (DPO compliance monitoring) — routed to the organizational lane (ADR-008) at its activation.
- **N/A (recorded):** `PO-D-06.4-001` (EU representative — EU-established), `SO-D-06.4-002` (non-EU manufacturer boundary), `SO-D-07.4-001` (series production — software product), `SO-D-08.2-002` (integration information — product not offered for integration).

## 6. Output

36 objective rows carried by the 16 RN candidates · 92 chain rows on functional carriers · 2 organizational (recorded) · 4 N/A (recorded) = **134/134 placed**. The candidates went to Round 1 for per-batch client verdicts.
