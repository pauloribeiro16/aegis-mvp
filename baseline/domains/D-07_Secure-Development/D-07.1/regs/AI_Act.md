# D-07.1 — AI Act module

> Regulation-specific layer: applies when `AI_Act` is in scope
> (activation: `if AI_Act in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| AI_Act | SO-AIACT-009 + SO-AIACT-010 | High-risk AI systems achieve appropriate level of accuracy, robustness, and cybersecurity with lifecycle consistency (Art. 15(1) + Art. 15(4)–(5)) + a QMS with 13 enumerated aspects including design/design control/design verification (Art. 17(1)+(1)(c)). | AI-system-specific design discipline; QMS as formal carrier of design controls; lifecycle-consistency clause as qualitative cross-cutting requirement; SR-AIACT-014 (Art. 15(1)) + SR-AIACT-018 (Art. 17(1)(c)). |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **AI_Act** | AI-system accuracy / robustness / cybersecurity (lifecycle-consistent) + QMS design/design-control/design-verification | provider places high-risk AI system on market (Art. 6 + Art. 15(1)) + design/development activity (Art. 17(1)(c)) + design-control sub-process in QMS | `appropriate level of accuracy, robustness, and cybersecurity` (Art. 15(1) qualitative) + `perform consistently … throughout their lifecycle` (Art. 15(1) lifecycle-consistency qualitative) + Art. 15(4)–(5) AI-attack defence (6 attack categories) + Art. 17(1) QMS documented in `systematic and orderly manner` + 13-element closed list (a)–(m); no quantitative threshold | provider (QMS design-control documented) + market surveillance authority (QMS + Annex IV technical documentation) + AI Office (for GPAI on systemic-risk tracking) | Art. 15(1) + Art. 15(4)–(5) + Art. 17(1) + Art. 17(1)(c) + Recital 78 GDPR preservation + Annex IV technical documentation |

## Sub-SO (AI Act)

#### D-07.1.5 — Sub-SO for AI Act

```yaml
id: SO-D-07.1.AIACT
subdomain: D-07.1
applies_to: [AI_Act]
inherits_from: SO-AIACT-009 + SO-AIACT-010
source_SR: SR-AIACT-014
activation: if AI_Act in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** High-risk AI systems are designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle (Art. 15(1) AI Act).

- The Quality Management System (QMS) under Art. 17(1) is the AI-Act-side by-design operationalisation mechanism — documented in systematic and orderly manner covering at least 13 enumerated aspects including Art. 17(1)(c) design/design-control/design-verification (3-way AND).
- Annex IV technical documentation (per Art. 11 + Art. 12(2)) is the technical-documentation evidence base for the by-design outputs.
- The by-design architecture propagates downstream to D-07.2 (Secure Coding Practices) via the AI Act Art. 15(4)–(5) AI-attack-defence categories as the AI/ML-specific secure-coding baseline (cross to D-07.2 — SR-AIACT-016).

**CSF anchors (from `SR-AIACT-014` v0.3 security_rationale):**
PR.PS-06, PR.IR-03, ID.RA-04.
**AI RMF anchors (from `SR-AIACT-014` — dashboard `00_VISUALISATIONS/AI_Act/AI_Act_Dashboard.html`, mechanical uniformization):**
MEASURE-2.5, MEASURE-2.6, MEASURE-2.7, GOVERN-1.2.
*(PR.PS-06 anchors the secure-software-development lifecycle dimension — secure software development practices are integrated, and their performance is monitored throughout the SDLC; the AI Act Art. 15(1) accuracy+robustness+cybersecurity with lifecycle consistency + Art. 17(1)(c) QMS design/design-control/design-verification map to PR.PS-06 directly. ID.RA-01 anchors the vulnerabilities-identified-validated-recorded dimension — vulnerabilities in assets are identified, validated, and recorded; the AI Act Art. 9(2) foreseeable-risk identification + Art. 15(4)–(5) AI-attack-defence categories map to ID.RA-01 directly. The two subcategories together enable the AI system provider to demonstrate ex post, through the documented Art. 15(1) accuracy+robustness+cybersecurity baseline + Art. 17(1) QMS systematic-and-orderly-manner documentation + Art. 17(1)(c) design/design-control/design-verification sub-record + Art. 11 + 12(2) Annex IV technical documentation + Art. 9 risk-management-system documentation, that the Art. 15(1) + 17(1)(c) by-design + QMS duty has been exercised with the lifecycle-consistency + AI-attack-defence calibration.)*

---


## Security Requirements (AI Act)

#### 7.1.5 — High-risk AI system accuracy, robustness, cybersecurity with lifecycle consistency + QMS

```yaml
- req_id: 7.1.5
  volere_section: 15
  volere_subtype: integrity

  title: "High-risk AI systems designed and developed to achieve appropriate level of accuracy, robustness, and cybersecurity, performing consistently throughout their lifecycle, with QMS covering design/design-control/design-verification"

  derives_from:
    hso_sub_so: SO-D-07.1.AIACT
    per_reg_so: SO-AIACT-009, SO-AIACT-010
    source_sr: SR-AIACT-014, SR-AIACT-018
    hso_file: ../../HierarchicalSecurityObjectives/D-07_Secure-Development/D-07.1.md
    objective_ref_section: "### D-07.1.5"

  description: |
    The product shall ensure that high-risk AI systems are designed and developed to achieve an appropriate level of accuracy, robustness, and cybersecurity, and perform consistently in those respects throughout their lifecycle, with a Quality Management System implemented in a systematic and orderly manner covering at least 13 enumerated aspects including techniques, procedures and systematic actions for the design, design control and design verification of the high-risk AI system (AI Act Art. 15(1) + Art. 17(1) + Art. 17(1)(c) + Art. 17(1)(g) cross-reference to Art. 9 risk-management-system documentation).

  fit_criterion: |
    A documented Art. 15(1) accuracy+robustness+cybersecurity baseline is maintained with lifecycle consistency (`perform consistently in those respects throughout their lifecycle`); the baseline is calibrated to `appropriate level` per the intended purpose + conditions of use; an Art. 17(1) Quality Management System is documented in `systematic and orderly manner` (POLY — ISO 9001 / ISO/IEC 23053 / internal bespoke) in the form of written policies, procedures and instructions; the QMS covers all 13 enumerated aspects (a)–(m) per Art. 17(1) including Art. 17(1)(c) `design, design control and design verification` 3-way AND; Art. 17(1)(g) cross-references Art. 9 risk-management-system documentation; the by-design outputs feed Annex IV technical documentation (per Art. 11 + Art. 12(2)) which is the technical-documentation evidence base; the Art. 15(4)–(5) AI-attack-defence categories (6 categories: data poisoning + model poisoning + adversarial examples + model evasion + confidentiality attacks + model flaws) are addressed as AI-specific attack-resistance obligations that do not substitute for CRA Annex I Part I (2)(j) attack-surface limitation or (2)(k) exploitation-mitigation outcomes on AI-enabled CRA products; AI Act Recital 78 explicitly preserves GDPR — for a high-risk AI system processing personal data, AI Act Art. 15(1) + QMS design/design-control/design-verification stacks with GDPR Art. 25(1) data-protection by-design as distinct design outputs (AI-system property vs privacy property); the by-design risk-assessment obligation on AI-enabled CRA products is satisfied by AI Act Art. 9 + Art. 17 risk-management-system documentation (per CRA Art. 13(4) sentence 2 explicit AI-Act-substitution carve-out for risk assessment); verified by Art. 15(1) accuracy+robustness+cybersecurity baseline documentation review + lifecycle-consistency evidence audit + Art. 17(1) QMS systematic-and-orderly-manner documentation inspection + Art. 17(1)(c) design/design-control/design-verification sub-record review + Art. 9 risk-management-system documentation cross-reference + Art. 15(4)–(5) AI-attack-defence measures record (for AI/ML-specific attacks) + Annex IV technical-documentation audit + provider + MSA + AI Office inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [7.1.1 (when high-risk AI system processes personal data — Recital 78 preservation; GDPR by-design overlay on AI Act by-design + QMS), 7.1.2 (when NIS embeds high-risk AI — NIS 2 procurement gate + AI Act QMS governance gate stack), 7.1.3 (when AI-enabled CRA product — CRA Art. 13(4) sentence 2 explicit AI-Act-substitution for risk assessment unifies Art. 9 + Art. 13 risk-assessment documentation), 7.1.4 (when DORA FE deploys high-risk AI — DORA Art. 9(4)(e) change-mgmt operational gate + AI Act QMS governance gate stack)]

  nist_csf: [PR.PS-06, ID.RA-01]

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

**AI_Act article (verbatim, Art. 15(1) + Art. 17(1)(c)):**
> "High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle." — Art. 15(1) AI Act
> "The quality management system shall include at least the following aspects: … (c) the techniques, procedures and systematic actions to be used for the design, design control and design verification of the high-risk AI system." — Art. 17(1)(c) AI Act


**AI_Act article (verbatim, Art. 15(1) + Art. 17(1)(c)):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/AI_Act.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-07.1: GDPR↔AI_Act = COMPLEMENTARY (SAME — privacy-by-design overlay on AI-system-accuracy+robustness+cybersecurity + QMS, Recital 78 preservation); NIS2↔AI_Act = COMPLEMENTARY (SAME — NIS 2 procurement gate on NIS-embedding-AI stacks with AI Act QMS governance gate); CRA↔AI_Act = COMPLEMENTARY (SAME — CRA Art. 13(4) sentence 2 explicit AI-Act-substitution for risk assessment on AI-enabled-CRA-product); DORA↔AI_Act = COMPLEMENTARY (SAME — DORA change-mgmt operational gate + AI Act QMS governance gate))
```

### from regs/AI_Act.md body

**Considerations.**

- Art. 15(4)–(5) AI-attack-defence categories (6 categories: data poisoning + model poisoning + adversarial examples + model evasion + confidentiality attacks + model flaws) are AI-specific attack categories that do not substitute for CRA Annex I Part I (2)(j) attack-surface limitation or (2)(k) exploitation-mitigation outcomes (cross to D-07.2).

### from regs/AI_Act.md body

- AI Act Recital 78 explicitly preserves the GDPR — for a high-risk AI system processing personal data, AI Act Art. 15(1) accuracy+robustness+cybersecurity + QMS design/design-control/design-verification stacks with GDPR Art. 25(1) data-protection by-design as distinct design outputs (AI-system property vs privacy property).

### from regs/AI_Act.md body

- For an AI-enabled CRA product, CRA Art. 13(4) sentence 2 explicit AI-Act-substitution for risk assessment permits a unified risk assessment under AI Act Art. 9 to substitute for the CRA risk assessment when both apply (SR-CRA-066) — the by-design risk-assessment obligation is satisfied by the AI Act Art. 9 + Art. 17 risk-management-system documentation that covers both regimes' risk-assessment content.

### from regs/AI_Act.md body

- For a financial entity deploying high-risk AI, DORA Art. 9(4)(e) change-management six-step is the operational gate; AI Act QMS design controls is the governance gate; the two stack with the change-mgmt six-step pre-empting the deployment and the QMS design controls governing the design-development activity.

### from regs/AI_Act.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # AI_Act↔GDPR = Y (provider/deployer-controller-processing-personal-data-via-AI; Recital 78 preservation); AI_Act↔NIS2 = Y (NIS-embedding-high-risk-AI; NIS 2 procurement gate + AI Act QMS); AI_Act↔CRA = Conditional Y (AI-enabled CRA product; CRA Art. 13(4) sentence 2 explicit AI-Act-substitution carve-out); AI_Act↔DORA = Y (DORA FE deploys high-risk AI; DORA change-mgmt operational gate + AI Act QMS governance gate); HL engages on overlap

```

### from regs/AI_Act.md body — field `considerations`

```yaml
  considerations: |
    The AI Act secure-by-design obligation is the high-risk AI system accuracy+robustness+cybersecurity with lifecycle consistency + QMS design/design-control/design-verification; the operational substrate is the Art. 15(1) baseline + Art. 17(1) QMS documented in `systematic and orderly manner` covering all 13 enumerated aspects (a)–(m) including Art. 17(1)(c) design/design-control/design-verification 3-way AND. The Art. 15(4)–(5) AI-attack-defence categories (6 categories: data poisoning + model poisoning + adversarial examples + model evasion + confidentiality attacks + model flaws) are AI-specific attack categories that do not substitute for CRA Annex I Part I (2)(j) attack-surface or (2)(k) exploitation-mitigation outcomes on AI-enabled CRA products. AI Act Recital 78 preserves GDPR — for high-risk AI processing personal data, AI Act Art. 15(1) accuracy+robustness+cybersecurity + QMS design/design-control/design-verification stacks with GDPR Art. 25(1) data-protection by-design as distinct design outputs (AI-system property vs privacy property). For an AI-enabled CRA product, CRA Art. 13(4) sentence 2 explicit AI-Act-substitution for risk assessment permits a unified risk assessment under AI Act Art. 9 to substitute for the CRA risk assessment when both apply (per SR-CRA-066). (Copied from the HSO Considerations block of `### D-07.1.5`; preserved here for self-contained traceability.)
```

### from regs/AI_Act.md body

**AI_Act article (verbatim, Art. 15(1) + Art. 17(1)(c)):**

> [as quoted in GDPR ↔ AI_Act above]

<!-- aegis:purity: own_reg=AI_Act; demoted=8; core_cross_mentions=2 -->
