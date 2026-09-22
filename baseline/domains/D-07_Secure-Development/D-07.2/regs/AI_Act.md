# D-07.2 — AI Act module

> Regulation-specific layer: applies when `AI_Act` is in scope
> (activation: `if AI_Act in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| AI_Act | SO-AIACT-009 (partial via Art. 15(4)–(5)) | High-risk AI systems … be designed and developed with appropriate technical and organisational measures to … (b) enable the AI systems to effectively resist, as appropriate to the AI system's purpose and conditions of use, attempts to manipulate the training data set (data poisoning) or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws — Art. 15(4)–(5) per the SR-AIACT-016 reading. | **AI/ML-focused secure-coding dimension** — 6 AI-attack-defence categories enumerated (data poisoning + model poisoning + adversarial examples + model evasion + confidentiality attacks + model flaws). The AI-Act-side participation at D-07.2 is **partial** in the SR sense (AI-attack-defence categories do not map to conventional secure-coding mandates). |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **AI_Act** | AI-system attack-defence (6 AI/ML-specific attack categories) at the AI-system-provider side | high-risk AI system design/development (Art. 15(4)–(5)) | Art. 15(4) `enable the AI systems to effectively resist, as appropriate to the AI system's purpose and conditions of use` + Art. 15(4)(b) 6-category AI-attack-defence: data poisoning + model poisoning + adversarial examples + model evasion + confidentiality attacks + model flaws — qualitative; the Art. 15(4) `as appropriate to the AI system's purpose and conditions of use` is a proportionality qualifier at the AI-system-purpose level | provider + market surveillance authority + AI Office — QMS design-control + Annex IV technical documentation + Art. 15(4)–(5) attack-defence measures (SR-AIACT-016) | Art. 15(4) + Art. 15(5) + Art. 17(1)(c) QMS design/design-control/design-verification + Recital 78 GDPR preservation |

## Sub-SO (AI Act)

#### D-07.2.3 — Sub-SO for AI Act

```yaml
id: SO-D-07.2.AIACT
subdomain: D-07.2
applies_to: [AI_Act]
inherits_from: SO-AIACT-009 (partial via Art. 15(4)–(5))
source_SR: SR-AIACT-016
activation: if AI_Act in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** High-risk AI systems are designed and developed with appropriate technical and organisational measures to enable the AI systems to effectively resist, as appropriate to the AI system's purpose and conditions of use, attempts to manipulate the training data set (data poisoning) or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws (Art. 15(4)–(5) AI Act).

**Considerations.**
- The 6 AI-attack-defence categories are: (1) data poisoning — manipulation of the training data set; (2) model poisoning — manipulation of pre-trained components; (3) adversarial examples — inputs designed to cause the AI model to make a mistake; (4) model evasion — adversarial-example-induced evasion; (5) confidentiality attacks — attacks on confidentiality of training data, parameters, or outputs; (6) model flaws — vulnerabilities or weaknesses inherent in model architecture or training process.
- The `as appropriate to the AI system's purpose and conditions of use` is a proportionality qualifier at the AI-system-purpose level — calibration is informed by the intended purpose (cross to D-09.2 — SO-AIACT-001 Art. 9 risk-management-system) and the conditions of use (operational environment + reasonably foreseeable use).
- The AI-Act-side participation at D-07.2 is partial in the SR sense: Art. 15(4)–(5) AI-attack-defence categories are AI/ML-specific and do NOT map to conventional secure-coding mandates (no general coding-standards prescription in AI Act — the AI Act addresses AI-attack-defence, not conventional coding practices).
- AI-Act-side attack-defence is documented in QMS design-control records (Art. 17(1)(c) design/design-control/design-verification) + Annex IV technical documentation + Art. 9 risk-management-system documentation (cross to D-09.1 — SO-AIACT-010 + SO-AIACT-001).
- For a high-risk AI system provider, the AI-attack-defence coding-practices baseline is built from AI/ML-specific frameworks (NIST AI RMF, ISO/IEC 23894, MITRE ATLAS) and demonstrated against the 6 Art. 15(4)–(5) attack-defence categories via the QMS + Annex IV documentation.
**CSF anchors (from `SR-AIACT-016` v0.3 security_rationale):**
ID.RA-04, PR.PS-06, RS.MI-01, RS.MA-03.
**AI RMF anchors (from `SR-AIACT-016` — dashboard `00_VISUALISATIONS/AI_Act/AI_Act_Dashboard.html`, mechanical uniformization):**
MEASURE-2.7, MAP-3.2, MANAGE-1.3.
*(PR.PS-06 anchors the secure-software-development lifecycle dimension — secure software development practices are integrated, and their performance is monitored throughout the SDLC; the AI Act Art. 15(4)–(5) AI-attack-defence categories with the Art. 17(1)(c) QMS design/design-control/design-verification are realised through the SDLC with AI/ML-specific calibration. ID.RA-01 anchors the vulnerabilities-identified-validated-recorded dimension — vulnerabilities in assets are identified, validated, and recorded; the AI Act Art. 15(4)–(5) 6-category AI-attack-defence + Art. 9(2) foreseeable-risk identification map to ID.RA-01 directly. The two subcategories together enable the AI system provider to demonstrate ex post, through the documented Art. 15(4)–(5) AI-attack-defence measures + Art. 17(1)(c) QMS design/design-control/design-verification record + Art. 9 risk-management-system documentation + Annex IV technical documentation, that the AI-attack-defence duty has been exercised with the 6-category AI/ML-specific attack resistance.)*

---


## Security Requirements (AI Act)

#### 7.2.3 — High-risk AI system attack-defence across 6 AI/ML-specific categories

```yaml
- req_id: 7.2.3
  volere_section: 15
  volere_subtype: immunity

  title: "High-risk AI systems designed and developed to effectively resist, as appropriate to purpose and conditions of use, attempts at training-data poisoning, model poisoning, adversarial examples, model evasion, confidentiality attacks or model flaws"

  derives_from:
    hso_sub_so: SO-D-07.2.AIACT
    per_reg_so: SO-AIACT-009 (partial via Art. 15(4)–(5))
    source_sr: SR-AIACT-016
    hso_file: ../../HierarchicalSecurityObjectives/D-07_Secure-Development/D-07.2.md
    objective_ref_section: "### D-07.2.3"

  description: |
    The product shall ensure that high-risk AI systems are designed and developed with appropriate technical and organisational measures to enable the AI systems to effectively resist, as appropriate to the AI system's purpose and conditions of use, attempts to manipulate the training data set (data poisoning) or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws (AI Act Art. 15(4)–(5)).

  fit_criterion: |
    A documented Art. 15(4) attack-defence baseline is maintained for the 6 AI/ML-specific attack categories: (1) **data poisoning** — defence against manipulation of the training data set, including input-validation + data-provenance checks + training-data sanitisation + anomaly-detection on training-set distribution; (2) **model poisoning** — defence against manipulation of pre-trained components, including supply-chain integrity for pre-trained components + signed-model checksums + pre-training-component provenance verification; (3) **adversarial examples** — defence against inputs designed to cause the AI model to make a mistake, including adversarial-input detection + input-preprocessing hardening + adversarial-robustness training; (4) **model evasion** — defence against adversarial-example-induced evasion, including evasion-aware model-update cadence + detection-of-evasion-attempt signals; (5) **confidentiality attacks** — defence against attacks on confidentiality of training data, parameters, or outputs, including differential-privacy training + model-parameter access controls + output-redaction discipline + membership-inference resistance; (6) **model flaws** — defence against vulnerabilities or weaknesses inherent in model architecture or training process, including architecture-review discipline + known-flaw catalogue + flaw-driven model-update cadence; the baseline is calibrated to `appropriate to the AI system's purpose and conditions of use` (Art. 15(4) proportionality qualifier) — informed by intended purpose (cross to D-09.2 — SO-AIACT-001 Art. 9 risk-management-system) and conditions of use (operational environment + reasonably foreseeable use); the Art. 15(4)–(5) AI-attack-defence categories are AI/ML-specific and do NOT map to conventional secure-coding mandates (no general coding-standards prescription in AI Act — the AI Act addresses AI-attack-defence, not conventional coding practices); the AI-attack-defence coding-practices baseline is built from AI/ML-specific frameworks (NIST AI RMF, ISO/IEC 23894, MITRE ATLAS) and demonstrated against the 6 Art. 15(4)–(5) attack-defence categories via the QMS + Annex IV documentation; AI-Act-Recital 78 GDPR preservation operates at the AI-system side for high-risk AI systems processing personal data — the AI-Act-side AI-attack-defence does NOT substitute for the GDPR Art. 25(1) data-protection by-design; the GDPR-side by-design is layered on top via the controller-means-determination + processing-time by-default; for AI-enabled CRA products (CRA-regulated product that embeds a high-risk AI system), AI Act Art. 15(4)–(5) AI-attack-defence stacks with CRA Annex I Part I (2)(j) attack-surface + (2)(k) exploitation-mitigation — the two regimes DO NOT substitute (AI Act defence categories do not substitute for CRA's outcome-level obligations, and vice versa); **no OJ-level consolidation rule exists** for the coding-practices dimension (unlike CRA Art. 13(4) sentence 2 unified-risk-assessment carve-out for AI Act Art. 9 risk assessment, which does NOT extend to coding practices); verified by Art. 15(4) 6-category AI-attack-defence measures record review + Art. 15(4) proportionality calibration records (purpose + conditions of use) + QMS design-control record (Art. 17(1)(c) — design/design-control/design-verification) + Annex IV technical-documentation audit + Art. 9 risk-management-system documentation cross-reference + provider + MSA + AI Office inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [7.2.1 (when AI-enabled CRA product — CRA Annex I Part I (2)(j)+(k) outcome-level obligations + AI Act Art. 15(4)–(5) AI-attack-defence categories stack vertically with no OJ-level consolidation rule; CRA-side outcomes + AI Act AI-attack-defence categories are complementary with non-substitution)]

  nist_csf: [ID.RA-04, PR.PS-06, RS.MI-01, RS.MA-03]
  nist_airmf: [MEASURE-2.7, MAP-3.2, MANAGE-1.3]

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

**AI_Act article (verbatim, Art. 15(4)–(5)):**
> "High-risk AI systems shall … be designed and developed with appropriate technical and organisational measures to … (a) … (b) enable the AI systems to effectively resist, as appropriate, to the AI system's purpose and conditions of use, attempts to manipulate the training data set (data poisoning) or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws." — Art. 15(4) AI Act (per the SR-AIACT-016 reading)

**AI_Act article (verbatim, Art. 15(4)–(5)):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/AI_Act.md body — field `verified_relationship`

```yaml
verified_relationship: DIFFERENT-PERSPECTIVE-AT-AI-VS-CONVENTIONAL (CRDA-deep, D-07.2: CRA↔AI_Act = SAME — COMPLEMENTARY with Conditional Y scope overlap on AI-enabled CRA products — CRA Annex I Part I (2)(j) + (2)(k) conventional outcome mandate + AI Act Art. 15(4)–(5) AI/ML-specific attack-defence mandate stack with no OJ-level consolidation rule; DORA↔AI_Act = SAME — COMPLEMENTARY with scope-disjoint qualifier per OJ-literal reading — entity-side change-mgmt process mandate vs AI-system-side attack-defence mandate; substantively scope-disjoint in baseline; the AI-Act-side attack-defence categories do not substitute for conventional coding-practices baselines)
```

### from regs/AI_Act.md body

- For an AI-enabled CRA product, AI Act Art. 15(4)–(5) AI-attack-defence stacks with CRA Annex I Part I (2)(j) + (2)(k) attack-surface + exploitation-mitigation — the two regimes DO NOT substitute (AI Act defence categories do not substitute for CRA's outcome-level obligations, and vice versa); **no OJ-level consolidation rule exists for the coding-practices dimension** (unlike CRA Art. 13(4) sentence 2 unified-risk-assessment carve-out for AI Act Art. 9, which does not extend to coding practices).

### from regs/AI_Act.md body

- AI-Act-Recital 78 GDPR preservation operates at the AI-system side for high-risk AI systems processing personal data — the AI-Act-side AI-attack-defence does NOT substitute for the GDPR Art. 25(1) data-protection by-design; the GDPR-side by-design is layered on top via the controller-means-determination + processing-time by-default.


### from regs/AI_Act.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # AI_Act↔CRA = Conditional Y on AI-enabled CRA products; AI_Act↔DORA = N typically (scope-disjoint in baseline); HL engages only on the Conditional Y integrated stack

```

### from regs/AI_Act.md body — field `considerations`

```yaml
  considerations: |
    The AI Act secure-coding obligation is the high-risk AI system attack-defence mandate with 6 AI/ML-specific attack categories: data poisoning + model poisoning + adversarial examples + model evasion + confidentiality attacks + model flaws. The Art. 15(4) `as appropriate to the AI system's purpose and conditions of use` is a proportionality qualifier at the AI-system-purpose level. The AI-Act-side participation at D-07.2 is **partial** in the SR sense: Art. 15(4)–(5) AI-attack-defence categories are AI/ML-specific and do NOT map to conventional secure-coding mandates (no general coding-standards prescription in AI Act — the AI Act addresses AI-attack-defence, not conventional coding practices). The AI-attack-defence coding-practices baseline is built from AI/ML-specific frameworks (NIST AI RMF, ISO/IEC 23894, MITRE ATLAS) and demonstrated against the 6 Art. 15(4)–(5) attack-defence categories via the QMS + Annex IV documentation. For AI-enabled CRA products, AI Act Art. 15(4)–(5) AI-attack-defence stacks with CRA Annex I Part I (2)(j) + (2)(k) attack-surface + exploitation-mitigation — **no OJ-level consolidation rule exists** for the coding-practices dimension (unlike CRA Art. 13(4) sentence 2 unified-risk-assessment carve-out for AI Act Art. 9 risk assessment, which does NOT extend to coding practices). AI-Act-Recital 78 GDPR preservation operates at the AI-system side for high-risk AI systems processing personal data — the AI-Act-side AI-attack-defence does NOT substitute for the GDPR Art. 25(1) data-protection by-design. (Copied from the HSO Considerations block of `### D-07.2.3`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=AI_Act; demoted=5; core_cross_mentions=2 -->
