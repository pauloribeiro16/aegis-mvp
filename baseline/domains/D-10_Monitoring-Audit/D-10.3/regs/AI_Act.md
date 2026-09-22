# D-10.3 — AI Act module

> Regulation-specific layer: applies when `AI_Act` is in scope
> (activation: `if AI_Act in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| AI_Act | SO-AIACT-007 + SO-AIACT-008 | High-risk AI systems are tested for the purpose of identifying the most appropriate and targeted risk management measures, ensuring consistent performance for their intended purpose; testing procedures may include testing in real-world conditions in accordance with Article 60; high-risk AI systems achieve an appropriate level of accuracy, robustness and cybersecurity and perform consistently throughout their lifecycle (Art. 9(6) + Art. 9(7) + Art. 15(1) AI Act per `SR-AIACT-003`/`SR-AIACT-014`). | AI-system-level testing for risk management + real-world-conditions testing per Art. 60 + accuracy/robustness/cybersecurity baseline testing throughout AI-system lifecycle; `perform consistently ... throughout their lifecycle` lifecycle anchor. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **AI_Act** | AI-system-level testing for risk management + real-world-conditions testing + accuracy/robustness/cybersecurity baseline testing throughout AI-system lifecycle | Art. 9(6) `High-risk AI systems shall be tested for the purpose of identifying the most appropriate and targeted risk management measures. Testing shall ensure that high-risk AI systems perform consistently for their intended purpose` + Art. 9(7) `Testing procedures may include testing in real-world conditions in accordance with Article 60` + Art. 15(1) `High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle` | AI-system (high-risk AI system per Art. 6) | provider + MSA + AI Office — Art. 9(6) testing-for-risk-management outputs + Art. 9(7) real-world-conditions testing per Art. 60 + Art. 15(1) accuracy/robustness/cybersecurity baseline testing | cadence Art. 9(6) `perform consistently for their intended purpose` + Art. 15(1) `throughout their lifecycle` lifecycle anchor; content partially codified for testing-for-risk-management dimension + Art. 60 detailed rules; testing proportional to AI-system risk per Art. 9(6) |

## Sub-SO (AI Act)

#### D-10.3.5 — Sub-SO for AI Act

```yaml
id: SO-D-10.3.AI_Act
subdomain: D-10.3
applies_to: [AI_Act]
inherits_from: SO-AIACT-007 + SO-AIACT-008
source_SR: SR-AIACT-003 + SR-AIACT-014
activation: if AI_Act in applicable_regs
phase_1A_role: 5_of_5
```

**Objective.** Providers of high-risk AI systems ensure the systems are **tested for the purpose of identifying the most appropriate and targeted risk management measures**, and **testing shall ensure that high-risk AI systems perform consistently for their intended purpose** (Art. 9(6) AI Act); testing procedures may include **testing in real-world conditions in accordance with Article 60** (Art. 9(7) AI Act); high-risk AI systems are **designed and developed to achieve an appropriate level of accuracy, robustness, and cybersecurity, and to perform consistently in those respects throughout their lifecycle** (Art. 15(1) AI Act).

**CSF anchors (from `SR-AIACT-003` + `SR-AIACT-014` v0.3 security_rationale):**
ID.IM-03 (primary), ID.RA-05, PR.PS-04, GV.OV-03.
*(ID.IM-03 — Configuration change control processes are in place — anchors the AI Act Art. 9(6) `tested for the purpose of identifying the most appropriate and targeted risk management measures` mapped to NIST CSF 2.0 ID.IM-03; ID.RA-05 — Threats, vulnerabilities, likelihoods, and impacts are used to establish risk tolerances — anchors the Art. 9(6) testing-for-risk-management risk-input dimension + Art. 9(7) real-world-conditions testing risk-input dimension; PR.PS-04 — Software installation, operation, and updates are performed consistent with the security policy — anchors the Art. 15(1) `throughout their lifecycle` lifecycle-testing dimension + the AI-system operational dimension; GV.OV-03 — Cybersecurity risk management strategy outcomes are reviewed and inform changes — anchors the Art. 9(6) testing-for-risk-management feedback loop into the AI-Act provider's risk-management-system documentation (Art. 9 — cross to D-09.1). The four subcategories together enable the AI Act provider to demonstrate ex post, against the MSA + AI Office supervisory baseline, that the Art. 9(6) testing-for-risk-management + Art. 9(7) real-world-conditions testing per Art. 60 + Art. 15(1) accuracy/robustness/cybersecurity baseline testing `throughout their lifecycle` were operational on the AI-system layer with appropriate risk-management calibration.)*

---


## Security Requirements (AI Act)

#### 10.3.5 — AI-system-level testing for risk management + real-world-conditions testing + accuracy/robustness/cybersecurity baseline throughout AI-system lifecycle

```yaml
- req_id: 10.3.5
  volere_section: 15
  volere_subtype: audit

  title: "Provider ensures high-risk AI system is tested for the purpose of identifying risk management measures, performs consistently for intended purpose, may be tested in real-world conditions per Article 60, and achieves appropriate accuracy/robustness/cybersecurity throughout the AI-system lifecycle"

  derives_from:
    hso_sub_so: SO-D-10.3.AI_Act
    per_reg_so: SO-AIACT-007 + SO-AIACT-008
    source_sr: SR-AIACT-003 + SR-AIACT-014
    hso_file: ../../HierarchicalSecurityObjectives/D-10_Monitoring-Audit/D-10.3.md
    objective_ref_section: "### D-10.3.5"

  description: |
    The product shall be tested for the purpose of identifying the most appropriate and targeted risk management measures, with testing ensuring that the high-risk AI system performs consistently for its intended purpose (per AI Act Art. 9(6) `High-risk AI systems shall be tested for the purpose of identifying the most appropriate and targeted risk management measures. Testing shall ensure that high-risk AI systems perform consistently for their intended purpose`); testing procedures may include testing in real-world conditions in accordance with Article 60 (per Art. 9(7) `Testing procedures may include testing in real-world conditions in accordance with Article 60`); the high-risk AI system shall be designed and developed to achieve an appropriate level of accuracy, robustness, and cybersecurity, and to perform consistently in those respects throughout its lifecycle (per Art. 15(1) `High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle`).

  fit_criterion: |
    AI-system-level testing is operational per Art. 9(6) + Art. 9(7) + Art. 15(1) (SR-AIACT-003 + SR-AIACT-014) verified by ID.IM-03 primary (Configuration change control processes are in place — anchors the AI Act Art. 9(6) `tested for the purpose of identifying the most appropriate and targeted risk management measures` mapped to NIST CSF 2.0 ID.IM-03) + ID.RA-05 (Threats, vulnerabilities, likelihoods, and impacts are used to establish risk tolerances — anchors the Art. 9(6) testing-for-risk-management risk-input dimension + Art. 9(7) real-world-conditions testing risk-input dimension) + PR.PS-04 (Software installation, operation, and updates are performed consistent with the security policy — anchors the Art. 15(1) `throughout their lifecycle` lifecycle-testing dimension + the AI-system operational dimension) + GV.OV-03 (Cybersecurity risk management strategy outcomes are reviewed and inform changes — anchors the Art. 9(6) testing-for-risk-management feedback loop into the AI-Act provider's risk-management-system documentation (Art. 9 — cross to 9.1)); the Art. 9(6) testing-for-risk-management is operational with tests identifying the most appropriate and targeted risk management measures + tests ensuring consistent performance for the intended purpose; the Art. 9(7) real-world-conditions testing is operational per the Art. 60 detailed rules (testing in real-world conditions subject to the Art. 60 conditions); the Art. 15(1) `throughout their lifecycle` lifecycle-testing is operational with accuracy + robustness + cybersecurity baseline testing + consistent performance in those respects throughout the AI-system lifecycle; the testing regime is calibrated to (a) identify the most appropriate and targeted risk management measures (Art. 9(6) testing-for-risk-management), (b) potentially include real-world-conditions testing per Art. 60 (Art. 9(7)), AND (c) achieve an appropriate level of accuracy, robustness, and cybersecurity throughout the AI-system lifecycle (Art. 15(1) baseline); the recipient is the **provider + MSA (market surveillance authority) + AI Office** on the Art. 9(6) testing-for-risk-management outputs + Art. 9(7) real-world-conditions testing per Art. 60 + Art. 15(1) accuracy/robustness/cybersecurity baseline testing throughout AI-system lifecycle; verified by MSA + AI Office audit pack (Art. 9(6) testing-for-risk-management outputs + Art. 9(7) real-world-conditions testing outputs + Art. 15(1) baseline testing outputs + lifecycle-testing evidence + Art. 9 risk-management-system documentation feedback loop (cross to 9.1) + Art. 72 post-market monitoring plan alignment (cross to 10.1)) + automated testing-for-risk-management test (tests identify risk management measures + tests ensure consistent performance for intended purpose) + automated real-world-conditions test (Art. 60 conditions met when real-world-conditions testing is included) + automated lifecycle-baseline test (accuracy + robustness + cybersecurity baseline throughout AI-system lifecycle).

  priority: MUST
  verification_method: TEST
  dependencies: [10.3.1 (Conditional — Y when high-risk AI system processes personal data; GDPR Art. 32(1)(d) effectiveness-evaluation + AI Act Art. 9(6) testing for risk management + Art. 9(7) real-world-conditions testing + Art. 15(1) baseline testing; entity-level regular testing vs. AI-system-level testing; partial trigger alignment; the two regimes stack without consolidation), 10.3.2 (Conditional — Y when NSIE deploys high-risk AI; NIS 2 Art. 21(2)(f) effectiveness-assessment + AI Act Art. 9(6) testing for risk management + Art. 9(7) real-world-conditions testing + Art. 15(1) baseline testing; AI Act adds real-world-conditions dimension; the two regimes stack without consolidation), 10.3.3 (**Y — when CRA-regulated product is also high-risk AI; CRA Annex I Part II (3) + Annex VII §6 + Annex VIII modules + AI Act Art. 9(6) testing for risk management + Art. 9(7) real-world-conditions testing per Art. 60 + Art. 15(1) baseline testing `throughout their lifecycle` stack on the same product; NO OJ-level consolidation rule for testing** — CRDA-deep line 388: "Tension: NONE (no OJ-level consolidation rule for testing — unlike the CRA Art. 13(4) sentence 2 risk-assessment consolidation)"; Phase 1 entities implement both regimes in parallel — the AI Act testing does NOT substitute for CRA testing and vice versa), 10.3.4 (Y — when DORA financial entity deploys high-risk AI; DORA Art. 24(1) testing programme + Art. 25(1) 12-way modalities + Art. 26(1) TLPT + AI Act Art. 9(6) testing for risk management + Art. 9(7) real-world-conditions testing per Art. 60 + Art. 15(1) baseline testing `throughout their lifecycle`; the two regimes stack without consolidation)]

  nist_csf: [ID.IM-03, ID.RA-05, PR.PS-04, GV.OV-03]

  applicable_if:
    regs: [AI_Act]
  satisfaction:
    controls: []
    nodes: []

```


---


## Verbatim regulatory basis (AI Act)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**AI_Act article (verbatim, Art. 9(6)+(7) + Art. 15(1)):**
> "High-risk AI systems shall be tested for the purpose of identifying the most appropriate and targeted risk management measures. Testing shall ensure that high-risk AI systems perform consistently for their intended purpose." — Art. 9(6) AI Act (per SR-AIACT-003)
> "Testing procedures may include testing in real-world conditions in accordance with Article 60." — Art. 9(7) AI Act
> "High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle." — Art. 15(1) AI Act (per SR-AIACT-014)

**AI_Act article (verbatim, Art. 9(6)+(7) + Art. 15(1)):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/AI_Act.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-10.3: GDPR↔AI_Act = COMPLEMENTARY (SAME — entity-level regular testing vs. AI-system-level testing for risk management; partial trigger alignment); NIS2↔AI_Act = COMPLEMENTARY (SAME — effectiveness-assessment + AI Act real-world-conditions testing stack; AI Act adds real-world-conditions dimension); CRA↔AI_Act = COMPLEMENTARY (SAME — CRA Annex I conformity + AI Act Art. 9(6)+(7) + Art. 15(1) stack for AI-enabled products; **NO OJ-level consolidation rule for testing — unlike the CRA Art. 13(4) sentence 2 risk-assessment consolidation**); DORA↔AI_Act = COMPLEMENTARY (SAME — DORA testing programme + TLPT + AI Act real-world-conditions testing stack for DORA financial entities deploying high-risk AI))
```

### from regs/AI_Act.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # AI_Act↔GDPR = Conditional (Y when high-risk AI processes personal data); AI_Act↔NIS2 = Conditional (Y when NSIE deploys high-risk AI); AI_Act↔CRA = Y (when CRA-regulated product is also high-risk AI; **NO OJ-level consolidation rule for testing**); AI_Act↔DORA = Y (DORA financial entity deploys high-risk AI); HL engages when the AI Act sub-SO activates AND ≥1 other sub-SO activates on Y or Conditional-Y overlap.

```

### from regs/AI_Act.md body — field `considerations`

```yaml
  considerations: |
    The AI Act compliance-testing obligation at D-10.3 is the **AI-system-level testing for risk management** + **real-world-conditions testing per Art. 60** + **accuracy/robustness/cybersecurity baseline testing throughout AI-system lifecycle** per Art. 9(6) + Art. 9(7) + Art. 15(1) (per SR-AIACT-003 + SR-AIACT-014). Art. 9(6) `High-risk AI systems shall be tested for the purpose of identifying the most appropriate and targeted risk management measures. Testing shall ensure that high-risk AI systems perform consistently for their intended purpose` — the testing-for-risk-management dimension + the consistent-performance-for-intended-purpose dimension. Art. 9(7) `Testing procedures may include testing in real-world conditions in accordance with Article 60` — the real-world-conditions testing per Art. 60 detailed rules. Art. 15(1) `High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle` — the `throughout their lifecycle` lifecycle anchor; the 3-way AND (accuracy, robustness, cybersecurity) + the 2-way AND (perform consistently in those respects throughout their lifecycle). The `throughout their lifecycle` anchor (Art. 15(1)) is the lifecycle-testing dimension — distinct from the point-in-time testing of the other 4 regulators. The recipient is the **provider + MSA + AI Office** on the Art. 9(6) testing-for-risk-management outputs + Art. 9(7) real-world-conditions testing per Art. 60 + Art. 15(1) accuracy/robustness/cybersecurity baseline testing throughout AI-system lifecycle. **NO OJ-level consolidation rule for testing** — even on the CRA↔AI_Act pair (CRDA-deep line 388: "Tension: NONE (no OJ-level consolidation rule for testing — unlike the CRA Art. 13(4) sentence 2 risk-assessment consolidation)"), the CRA Annex I Part II (3) `effective and regular tests` + Annex VII §6 test reports + Annex VIII modules stack separately from the AI Act Art. 9(6) testing for risk management + Art. 9(7) real-world-conditions testing per Art. 60 + Art. 15(1) accuracy/robustness/cybersecurity baseline; Phase 1 entities must implement both regimes in parallel — the AI Act testing does NOT substitute for CRA testing and vice versa. The Art. 9(6) testing-for-risk-management feedback loop feeds into the AI-Act provider's risk-management-system documentation (Art. 9 — cross to 9.1) and the AI-system quality management system (Art. 17 — cross to 9.1).
```

<!-- aegis:purity: own_reg=AI_Act; demoted=3; core_cross_mentions=1 -->