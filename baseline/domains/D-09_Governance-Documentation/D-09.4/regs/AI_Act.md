# D-09.4 — AI Act module

> Regulation-specific layer: applies when `AI_Act` is in scope
> (activation: `if AI_Act in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| AI_Act | SO-AIACT-009 (partial, primary) + SO-AIACT-010 (cross) + SO-AIACT-008 (logs) | Technical documentation (Annex IV via Art. 11/12) per Art. 19(1) `Providers of high-risk AI systems shall keep the logs referred to in Article 12(1) … to the extent that such logs are under their control` + QMS documentation of 13 enumerated aspects (Art. 17(1) `systematic and orderly manner in the form of written policies, procedures and instructions`). | AI-system-specific technical documentation mandate (Annex IV) + QMS documentation + provider logs; partial coverage; GDPR Art. 30 is the dedicated authority for RoPA. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **AI Act** | AI-system-specific technical documentation (Annex IV via Art. 11/12 traceability) + QMS documentation of 13 enumerated aspects (Art. 17(1) `systematic and orderly manner in the form of written policies, procedures and instructions`) + high-risk-AI-system logs per Art. 19(1) `Providers of high-risk AI systems shall keep the logs referred to in Article 12(1) … to the extent that such logs are under their control` | Art. 11 technical documentation + Art. 12(1) automatic recording of events + Art. 12(2) traceability + Art. 17(1) 13-element QMS closed list (a)-(m) + Art. 19(1) log retention (per SR-AIACT-008) | provider (high-risk AI system provider with Art. 17(1) QMS + Art. 11 technical documentation + Art. 19(1) log retention) — distinct from MSA / AI Office oversight | provider + deployer + MSA + AI Office — Art. 11 + Art. 12(1)/(2) + Art. 17(1) 13-element QMS + Art. 19(1) log retention | Art. 11 + Art. 12(1) + Art. 12(2) + Art. 17(1) + Art. 19(1) + Art. 13(1)+(3) transparency-to-deployers (cross) |

## Sub-SO (AI Act)

#### D-09.4.5 — Sub-SO for AI Act

```yaml
id: SO-D-09.4.AI_Act
subdomain: D-09.4
applies_to: [AI_Act]
inherits_from: SO-AIACT-009 + SO-AIACT-010 + SO-AIACT-008 (logs)
source_SR: SR-AIACT-008 + SR-AIACT-009 + SR-AIACT-010 + SR-AIACT-017
activation: if AI_Act in applicable_regs
phase_1A_role: 5_of_5
```

**Objective.** Providers of high-risk AI systems **draw up and keep up-to-date the technical documentation of the high-risk AI system in accordance with Annex IV before that system is placed on the market or put into service** (Art. 11(1) AI Act), **keep the logs automatically recorded by the high-risk AI system to the extent under their control** (Art. 19(1) AI Act), and document the **quality management system** in written policies, procedures, and instructions covering at least the 13 enumerated aspects (a)-(m) (Art. 17(1) AI Act).

**CSF anchors (from `SR-AIACT-008` + `SR-AIACT-009` + `SR-AIACT-010` + `SR-AIACT-017` v0.3 security_rationale):**
ID.AM-08 (primary), ID.AM-08, GV.PO-01.

---


## Security Requirements (AI Act)

#### 9.4.5 — Provider-side Annex IV technical documentation + Art. 17(1) 13-element QMS documentation + Art. 19(1) provider logs (MSA + AI Office audit)

```yaml
- req_id: 9.4.5
  volere_section: 15
  volere_subtype: audit

  title: "Provider of high-risk AI system draws up and keeps up-to-date the Annex IV technical documentation before placing on market or putting into service, the 13-element QMS documentation, and the Art. 19(1) provider logs under their control"

  derives_from:
    hso_sub_so: SO-9.4.AI_Act
    per_reg_so: SO-AIACT-009 + SO-AIACT-010 + SO-AIACT-008
    source_sr: SR-AIACT-008 + SR-AIACT-009 + SR-AIACT-010 + SR-AIACT-017
    hso_file: ../../HierarchicalSecurityObjectives/D-09_Governance-Documentation/9.4.md
    objective_ref_section: "### 9.4.5"

  description: |
    The product shall draw up and keep up-to-date the technical documentation of the high-risk AI system in accordance with Annex IV before that system is placed on the market or put into service (per AI Act Art. 11(1)), keep the logs automatically recorded by the high-risk AI system to the extent under the provider's control (per Art. 19(1) `Providers of high-risk AI systems shall keep the logs referred to in Article 12(1) … to the extent that such logs are under their control`), and document the quality management system in written policies, procedures, and instructions in a systematic and orderly manner covering at least the 13 enumerated aspects (a)-(m) of Art. 17(1) closed list, with AI Act Recital 78 explicit GDPR preservation.

  fit_criterion: |
    Technical documentation is drawn up and kept up-to-date per Art. 11(1) `Providers of high-risk AI systems shall draw up and keep up-to-date the technical documentation of the high-risk AI system in accordance with Annex IV before that system is placed on the market or put into service` (SR-AIACT-009) verified by ID.AM-08 lifecycle-management dimension (the provider demonstrates ex post that the Annex IV technical documentation + Art. 19(1) logs + Art. 17(1) QMS documentation are managed throughout the AI-system life cycle per CRDA DomainAnalysis §9.4 line 113 cross-validation) + ID.AM-08 risk-strategy-consistent data management (the Art. 17(1)(d) `data quality` + Art. 17(1)(g) `risk-management-system documentation cross-reference to Art. 9` are consistent with the entity's risk strategy per CRDA DomainAnalysis §9.4 line 113) + GV.PO-01 cybersecurity-policy substrate (the Art. 17(1) QMS `systematic and orderly manner in the form of written policies, procedures and instructions` is an organisational policy under the QMS — cross to 9.1 AI Act sub-SO); the Annex IV technical documentation is drawn up before placing on the market or putting into service per Art. 11(1); the Art. 19(1) `Providers of high-risk AI systems shall keep the logs referred to in Article 12(1) … to the extent that such logs are under their control` (SR-AIACT-008) covers the automatic recording of events over the high-risk AI system's life cycle per Art. 12(1) + traceability per Art. 12(2); the Art. 17(1) QMS documentation covers the 13 enumerated aspects (a) compliance strategy; (b) design, development, and verification techniques; (c) design, design control, design verification of the high-risk AI system; (d) post-market monitoring (cross to 10.1 AI Act sub-SO); (e) data quality; (f) ... (m) — full content codification (vs GDPR's entity-discretionary content under Art. 24(2) or NIS 2's entity-discretionary content under Recital 56 proportionality); the recipient is the **MSA (market surveillance authority) + AI Office + provider** on the Art. 11 Annex IV technical documentation + Art. 12(1)/(2) automatic recording + Art. 17(1) 13-element QMS + Art. 19(1) logs; verified by MSA + AI Office audit pack (Annex IV technical documentation extract, QMS documentation extract, Art. 19(1) log retention evidence) + automated Annex IV field-completeness test + automated 13-element QMS field-completeness test. **IMPORTANT — AI Act Recital 78 GDPR preservation**: AI Act Recital 78 explicitly preserves GDPR for personal-data processing — `protection of natural persons in relation to the processing of personal data … is governed by Regulation (EU) 2016/679`; providers that are also controllers maintain **parallel artefacts** (GDPR RoPA + AI Act Annex IV + AI Act Art. 17(1) QMS) on distinct artefacts that are not substitutable. **IMPORTANT — CRA Art. 13(4) sentence 2 risk-assessment consolidation does NOT extend to documentation**: the CRA Art. 13(4) sentence 2 unification rule at 9.2 covers the *risk-assessment object*; there is no equivalent documentation-level consolidation rule at 9.4; the two regimes maintain **parallel artefacts** (CRA Annex VII + AI Act Annex IV + AI Act Art. 17(1) QMS).

  priority: MUST
  verification_method: TEST
  dependencies: [9.4.1 (when provider/deployer = controller — GDPR RoPA + AI Act Annex IV + AI Act Art. 17(1) QMS on three parallel artefacts; AI Act Recital 78 explicit GDPR preservation; no OJ-level consolidation rule for documentation), 9.4.2 (when NSIE deploys high-risk AI — NIS 2 Art. 24 certification-driven records + AI Act Art. 17(1) QMS on distinct artefacts; CRDA-recommended COMPLEMENTARY), 9.4.3 (when CRA-regulated product is also high-risk AI system — CRA Annex VII + AI Act Annex IV + AI Act Art. 17(1) QMS on three parallel artefacts; no OJ-level consolidation rule for documentation at 9.4 — the CRA Art. 13(4) sentence 2 risk-assessment consolidation rule at 9.2 covers the *risk-assessment object* not the *documentation object*), 9.4.4 (when DORA financial entity deploys high-risk AI — DORA Art. 9(4)(a) IS-policy + AI Act Art. 17(1) QMS on distinct artefacts; CRDA-recommended COMPLEMENTARY)]

  nist_csf: [ID.AM-08, GV.PO-01]

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

**AI_Act article (verbatim, Art. 11 + Art. 12 + Art. 17(1)):**
> "Providers of high-risk AI systems shall keep the logs referred to in Article 12(1) … to the extent that such logs are under their control." — Art. 19(1) AI Act (per SR-AIACT-008/009)
> "The quality management system shall be documented in a systematic and orderly manner in the form of written policies, procedures and instructions …" — Art. 17(1) AI Act (per SR-AIACT-017)

**AI_Act article (verbatim, Art. 17(1)):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/AI_Act.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-09.4: GDPR↔AI_Act = COMPLEMENTARY (SAME — Conditional-Y when provider/deployer is controller processing personal data via high-risk AI; GDPR RoPA + AI Act Annex IV + AI Act Art. 17 QMS stack on three parallel artefacts; AI Act Recital 78 explicit GDPR preservation; **no OJ-level consolidation rule for documentation**); NIS2↔AI_Act = COMPLEMENTARY RECOMMENDED-by-CRDA (Conditional-Y when NSIE deploys high-risk AI); CRA↔AI_Act = COMPLEMENTARY (SAME — Y when CRA-regulated product is also a high-risk AI system; CRA Annex VII + AI Act Annex IV + AI Act Art. 17 QMS stack on three parallel artefacts; **no OJ-level consolidation rule for documentation at D-09.4** — unlike the CRA Art. 13(4) sentence 2 risk-assessment consolidation rule at D-09.2, that rule covers the *risk-assessment object* not the *documentation object*); DORA↔AI_Act = COMPLEMENTARY RECOMMENDED-by-CRDA (Conditional-Y when DORA financial entity deploys high-risk AI))
```

### from regs/AI_Act.md body

*(ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycle — anchors the AI Act Art. 11 + Art. 19(1) `logs referred to in Article 12(1)` + Art. 17(1) QMS documentation of 13 enumerated aspects mapped to NIST CSF 2.0 ID.AM-08 per CRDA DomainAnalysis §D-09.4 line 113 cross-validation; ID.AM-08 — Data managed consistent with risk strategy — anchors the AI Act Art. 17(1)(d) `data quality` + Art. 17(1)(g) `risk-management-system documentation cross-reference to Art. 9` per CRDA DomainAnalysis §D-09.4 line 113; GV.PO-01 — Organizational cybersecurity policy established, communicated, enforced — anchors the AI Act Art. 17(1) QMS `systematic and orderly manner in the form of written policies, procedures and instructions` mapped to NIST CSF 2.0 GV.PO-01 (cross to D-09.1 AI Act sub-SO). The three subcategories together enable the provider to demonstrate ex post, against the MSA + AI Office supervisory baseline, that the Annex IV technical documentation (Art. 11) + Art. 12(2) traceability + Art. 17(1) 13-element QMS documentation + Art. 19(1) provider logs were established before placing on the market and kept up-to-date during the AI lifecycle. **IMPORTANT — AI Act Recital 78 GDPR preservation**: AI Act Recital 78 explicitly preserves GDPR for personal-data processing — `protection of natural persons in relation to the processing of personal data … is governed by Regulation (EU) 2016/679`; providers that are also controllers maintain **parallel artefacts** (GDPR RoPA + AI Act Annex IV + AI Act Art. 17 QMS). **IMPORTANT — CRA Art. 13(4) sentence 2 risk-assessment consolidation does NOT extend to documentation**: the CRA Art. 13(4) sentence 2 unification rule at D-09.2 covers the *risk-assessment object*; there is no equivalent documentation-level consolidation rule at D-09.4; the two regimes maintain **parallel artefacts** (CRA Annex VII + AI Act Annex IV + AI Act Art. 17 QMS). The **T5 mapping error on AIA-C11 (Art. 12(4) does not exist in the OJ) is surfaced in SR-AIACT-009 `ambiguity_notes` without silent reinterpretation** — the AI Act Art. 12(4) reference is a mapping-error trap; the OJ only has Art. 12(1)/(2)/(3) (per SR-AIACT-009 ambiguity_notes).)*

### from regs/AI_Act.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # AI_Act↔GDPR = Conditional (Y when provider/deployer is controller processing personal data via high-risk AI; GDPR RoPA + AI Act Annex IV + Art. 17(1) QMS on three parallel artefacts; AI Act Recital 78 explicit GDPR preservation; no OJ-level consolidation rule for documentation); AI_Act↔NIS2 = Conditional (Y when NSIE deploys high-risk AI; CRDA-recommended COMPLEMENTARY); AI_Act↔CRA = Y (CRA-regulated product is also high-risk AI system; CRA Annex VII + AI Act Annex IV + Art. 17(1) QMS on three parallel artefacts; no OJ-level consolidation rule for documentation at 9.4); AI_Act↔DORA = Conditional (Y when DORA financial entity deploys high-risk AI; CRDA-recommended COMPLEMENTARY); HL engages when the AI Act sub-SO activates AND ≥1 other sub-SO activates on Y or Conditional-Y overlap.

```

### from regs/AI_Act.md body — field `considerations`

```yaml
  considerations: |
    The AI Act records-of-processing obligation at 9.4 is the **AI-system-specific technical documentation** (Annex IV via Art. 11/12 traceability) + **QMS documentation of 13 enumerated aspects** (Art. 17(1) `systematic and orderly manner in the form of written policies, procedures and instructions`) + **high-risk-AI-system provider logs** (Art. 19(1)) with the provider as governance body. Art. 11(1) `Providers of high-risk AI systems shall draw up and keep up-to-date the technical documentation of the high-risk AI system in accordance with Annex IV before that system is placed on the market or put into service` (per SR-AIACT-009); Art. 12(1) automatic recording of events + Art. 12(2) traceability; Art. 17(1) 13-element QMS closed list (a)-(m) with the `systematic and orderly manner` formality (VAG-2 per SR-AIACT-017 ambiguity_notes); Art. 19(1) `Providers of high-risk AI systems shall keep the logs referred to in Article 12(1) … to the extent that such logs are under their control` (per SR-AIACT-008) — the `to the extent that such logs are under their control` qualifier carries VAG-3 (Berry §5.1 — OJ does not anchor the extent of provider control; chosen reading: provider control extends to the high-risk AI system itself and the immediate environment under the provider's operational control). **AI Act Recital 78 GDPR preservation**: AI Act Recital 78 explicitly preserves GDPR — `protection of natural persons in relation to the processing of personal data by Union institutions, bodies, offices and agencies … is governed by Regulation (EU) 2018/1725`; explicit Regulation (EU) 2016/679 preservation. **CRA Art. 13(4) sentence 2 risk-assessment consolidation does NOT extend to documentation**: the CRA Art. 13(4) sentence 2 unification rule at 9.2 covers the *risk-assessment object*; there is no equivalent documentation-level consolidation rule at 9.4. The 13-element QMS closed list is fully content-codified (vs GDPR's entity-discretionary content under Art. 24(2) or NIS 2's entity-discretionary content under Recital 56 proportionality). The recipient is the **MSA (market surveillance authority) + AI Office + provider** on the Art. 11 Annex IV technical documentation + Art. 12(1)/(2) automatic recording + Art. 17(1) 13-element QMS + Art. 19(1) logs. No OJ-quantified retention period for the technical documentation or QMS — entity-discretionary under Member State transposition + AI Office supervisory baseline.
```

<!-- aegis:purity: own_reg=AI_Act; demoted=4; core_cross_mentions=3 -->