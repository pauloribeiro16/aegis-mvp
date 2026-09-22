# D-09.1 — AI Act module

> Regulation-specific layer: applies when `AI_Act` is in scope
> (activation: `if AI_Act in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| AI_Act | SO-AIACT-007 + SO-AIACT-010 | High-risk AI systems are designed and developed so their operation is sufficiently transparent to enable deployers to interpret output and use it appropriately, accompanied by concise, complete, correct and clear instructions for use (Art. 13(1)+(3)); a quality management system documented in a systematic and orderly manner in the form of written policies, procedures and instructions covering at least 13 enumerated aspects including design/design control/design verification and risk-management-system documentation (Art. 17(1)). | AI-system-specific policy carrier via QMS; transparency-to-deployers as policy content. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **AI_Act** | provider-side QMS documented in a systematic and orderly manner in the form of written policies, procedures, instructions, covering at least 13 enumerated aspects ((a) compliance strategy; (b) design/development/verification; (c) post-market monitoring; (d) data quality; (e) risk management; (f) … (m)) + transparency-to-deployers via instructions-for-use | Art. 17(1) `The quality management system shall be documented in a systematic and orderly manner in the form of written policies, procedures and instructions, and shall include at least the following aspects: (a) … (m)` + Art. 13(1) `sufficiently transparent to enable deployers to interpret a system's output and use it appropriately` + Art. 13(3) `concise, complete, correct and clear` instructions for use | provider (high-risk AI system provider with Art. 17(1) QMS + Art. 13(1) transparency-to-deployers + Art. 26(1) deployer measures aligned with instructions) — distinct from MSA / AI Office oversight | provider, deployer, MSA, AI Office — Art. 17(1) QMS documented policies/procedures/instructions + Art. 13(1)+(3) transparency instructions-for-use + Art. 26(1) deployer measures aligned with instructions | Art. 17(1) + Art. 17(1)(c) design/design control/verification + Art. 17(1)(g) risk-management-system documentation cross-reference to Art. 9 + Art. 13(1) + Art. 13(3) + Art. 26(1) |

## Sub-SO (AI Act)

#### D-09.1.5 — Sub-SO for AI Act

```yaml
id: SO-D-09.1.AI_Act
subdomain: D-09.1
applies_to: [AI_Act]
inherits_from: SO-AIACT-007 + SO-AIACT-010
source_SR: SR-AIACT-010 + SR-AIACT-011 + SR-AIACT-017 + SR-AIACT-019
activation: if AI_Act in applicable_regs
phase_1A_role: 1_of_5
```

**Objective.** High-risk AI systems are **designed and developed to ensure that their operation is sufficiently transparent to enable deployers to interpret a system's output and use it appropriately** (Art. 13(1) AI Act), accompanied by **concise, complete, correct and clear instructions for use** (Art. 13(3) AI Act); a provider **puts a quality management system in place** documented in written policies, procedures and instructions covering at least the 13 enumerated aspects (a)-(m) (Art. 17(1) AI Act).

**CSF anchors (from `SR-AIACT-010` + `SR-AIACT-017` v0.3 security_rationale):**
GV.PO-01 (primary), GV.OC-03, GV.OC-04, GV.RM-01, GV.RM-04.
**AI RMF anchors (from `SR-AIACT-010`, `SR-AIACT-017` — dashboard `00_VISUALISATIONS/AI_Act/AI_Act_Dashboard.html`, mechanical uniformization):**
GOVERN-1.4, MAP-1.1, MEASURE-2.8, MEASURE-2.9, GOVERN-1.1, GOVERN-1.3, GOVERN-1.6.

---


## Security Requirements (AI Act)

#### 9.1.5 — Provider-side QMS documented in a systematic and orderly manner with 13-element closed list and transparency-to-deployers instructions-for-use

```yaml
- req_id: 9.1.5
  volere_section: 15
  volere_subtype: integrity

  title: "Provider of high-risk AI system operates a documented quality management system with at least 13 enumerated aspects and instructions for use enabling deployer-interpretable transparency"

  derives_from:
    hso_sub_so: SO-9.1.AI_Act
    per_reg_so: SO-AIACT-007 + SO-AIACT-010
    source_sr: SR-AIACT-010 + SR-AIACT-017
    hso_file: ../../HierarchicalSecurityObjectives/D-09_Governance-Documentation/9.1.md
    objective_ref_section: "### 9.1.5"

  description: |
    The product shall operate a documented quality management system (QMS) ensuring compliance with the AI Act, documented in a systematic and orderly manner in the form of written policies, procedures, and instructions covering at least the 13 enumerated aspects of Art. 17(1) closed list (a)-(m), with high-risk AI systems designed and developed to ensure sufficiently transparent operation enabling deployers to interpret a system's output and use it appropriately, accompanied by concise, complete, correct and clear instructions for use (per AI Act Art. 17(1) + Art. 13(1) + Art. 13(3)).

  fit_criterion: |
    A QMS is documented under Art. 17(1) (SR-AIACT-017) in a systematic and orderly manner in the form of written policies, procedures, and instructions (POLY on `quality management system` — R1 ISO 9001 / R2 ISO/IEC 23053 / R3 internal bespoke; chosen reading: R3 literal since the OJ does not name any specific standard — Recital 67 characterises the QMS as inspired by established quality standards but does not mandate a specific standard); the QMS covers at least the 13 enumerated aspects (a)-(m) of the Art. 17(1) closed list with GV.PO-01 policy arm (the top-level written cybersecurity policy that operationalises the 13-element list including the policies, procedures, and instructions anchor) + GV.PO-02 process-and-procedure arm (the policies accompanied by documented processes and procedures, also documented, communicated, and enforced — the systematic-and-orderly requirement of Art. 17(1)) + GV.RM-01 risk-management-objectives binding (the QMS bound to risk-management objectives agreed by organisational stakeholders, satisfying sub-point (g)'s cross-reference to Art. 9 risk-management system) + GV.RM-04 strategic-direction layer (risk appetite, response posture, escalation criteria that connect policy formulation and risk-objective setting to operational risk-treatment decisions) + GV.OC-03 legal-and-regulatory obligations register (the QMS understands and manages the full set of legal, regulatory, and contractual obligations that the AI Act adds on top of CRA, NIS 2, GDPR, and DORA); high-risk AI systems are designed and developed to ensure sufficiently transparent operation enabling deployers to interpret a system's output and use it appropriately under Art. 13(1) (SR-AIACT-010) with GV.PO-01 cybersecurity-policy substrate (transparency must be policy-bound and enforced to be supervisory-auditable) + GV.OC-03 legal-and-regulatory understanding substrate (distinguishing the high-risk-specific Art. 13(1) transparency duty from the Art. 50 user-facing and Art. 70 deployer-information duties, ensuring the cumulative AND of explainability, disclosure, and interpretability senses is operationalised against an understood regulatory baseline) + GV.OC-04 stakeholder-communication dimension (deployers are the principal stakeholders for AI-system transparency, operationalising the `interpret a system's output AND use it appropriately` opening through understood capabilities and limitations); the chosen reading for `sufficiently transparent` + `appropriate type and degree of transparency` is cumulative (explainability + disclosure + interpretability) because the `interpret a system's output AND use it appropriately` opening implicates each sense (per SR-AIACT-010 ambiguity_notes — central S3 ambiguity on `sufficiently transparent` admits three AI-governance senses: explainability / disclosure / interpretability, each implying different technical implementations — explainable-AI tooling / system documentation / model-architecture disclosure respectively); Art. 13(3) instructions-for-use are `concise, complete, correct and clear` (4-way AND) + `relevant, accessible and comprehensible` (3-way AND) + `characteristics, capabilities and limitations of performance` (POLY triple) — the high-risk-system transparency instructions-for-use accompanying the system; the QMS is documented under Art. 17(1) systematic-and-orderly QMS + Art. 9 risk-management cross-reference + Art. 43/47 conformity-assessment accountability chain; the QMS becomes a sub-policy of the integrated policy architecture on the GDPR↔AI_Act SAME — COMPLEMENTARY pair (AI Act Recital 78 explicit GDPR preservation — AI Act QMS as sub-policy of GDPR data-protection policies for providers/deployers that are controllers processing personal data via high-risk AI, per CRDA-deep §9.1 GDPR↔AI_Act verified relationship); for an NSIE that deploys high-risk AI, the AI Act QMS becomes a sub-policy of the entity-level NIS 2 governance framework on the NIS2↔AI_Act SAME — COMPLEMENTARY pair (the AI Act layer adds the AI-specific 13-element QMS to the NIS 2 risk-analysis policy, per CRDA-deep §9.1 NIS2↔AI_Act verified relationship); for AI-enabled products that are both CRA-regulated and AI-Act high-risk, the CRA Annex I conformity stack coexists with the AI Act QMS stack on the CRA↔AI_Act SAME — COMPLEMENTARY pair (CRA on the product cybersecurity requirements + AI Act on the AI-system quality-management system — no OJ-level consolidation rule at 9.1, unlike 9.2 where CRA Art. 13(4) sentence 2 permits AI Act Art. 9 risk management to substitute for CRA risk assessment, that rule covers the *risk-assessment object* not the *policy object*, per CRDA-deep §9.1 CRA↔AI_Act verified relationship); for a DORA financial entity that deploys high-risk AI, the DORA ICT risk-management framework + AI Act QMS + Art. 26(1) deployer measures stack on the DORA↔AI_Act SAME — COMPLEMENTARY pair (three-lines-of-defence + QMS compatible governance architectures; DORA-led stack with AI Act QMS as sub-component, per CRDA-deep §9.1 DORA↔AI_Act verified relationship); verified by Art. 17(1) QMS documentation review + Art. 13(1) sufficiently-transparent design-and-development evidence + Art. 13(3) `concise, complete, correct and clear` instructions-for-use documentation review + Art. 17(1)(g) Art. 9 risk-management-system cross-reference documentation + Art. 43/47 conformity-assessment records + Art. 50 user-facing transparency records (when applicable) + MSA / AI Office / provider / deployer inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [9.1.1 (when provider/deployer = controller — AI Act QMS as sub-policy of GDPR data-protection policies; AI Act Recital 78 explicit GDPR preservation), 9.1.2 (when NSIE deploys high-risk AI — AI Act QMS as sub-policy of NIS 2 entity-level governance framework), 9.1.3 (when product is both CRA-regulated and AI-Act high-risk — CRA Annex I conformity + AI Act QMS stack; no OJ-level consolidation rule at 9.1), 9.1.4 (when DORA FE deploys high-risk AI — DORA ICT risk-management framework + AI Act QMS + Art. 26(1) deployer measures stack; three-lines-of-defence + QMS compatible governance architectures; DORA-led stack with AI Act QMS as sub-component)]

  nist_csf: [GV.PO-01, GV.OC-03, GV.OC-04]
  nist_airmf: [GOVERN-1.4, MAP-1.1, MEASURE-2.8, MEASURE-2.9]

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

**AI_Act article (verbatim, Art. 13(1) + Art. 17(1) + Art. 26(1)):**
> "The quality management system shall be documented in a systematic and orderly manner in the form of written policies, procedures and instructions, and shall include at least the following aspects: (a) … (m)" — Art. 17(1) AI Act (per SR-AIACT-017)
> "Deployers of high-risk AI systems shall take appropriate technical and organisational measures to ensure they use such systems in accordance with the instructions for use accompanying the systems." — Art. 26(1) AI Act (per SR-AIACT-019)

**AI_Act article (verbatim, Art. 17(1)):**
> "Providers of high-risk AI systems shall put a quality management system in place that ensures compliance with this Regulation. That system shall be documented in a systematic and orderly manner in the form of written policies, procedures and instructions, and shall include at least the following aspects: (a) … (m)" — Art. 17(1) AI Act (per SR-AIACT-017)

**AI_Act article (verbatim, Art. 17(1)):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/AI_Act.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-09.1: GDPR↔AI_Act = COMPLEMENTARY (SAME — AI Act Recital 78 explicit GDPR preservation; AI Act QMS as sub-policy of GDPR controller policies for providers/deployers that are controllers processing personal data via high-risk AI); NIS2↔AI_Act = COMPLEMENTARY (SAME — NIS 2 entity-level governance + AI Act QMS as sub-policy for NSIEs deploying high-risk AI); CRA↔AI_Act = COMPLEMENTARY (SAME — CRA Annex I conformity + AI Act QMS stack for products that are both CRA-regulated and AI-Act high-risk; **no OJ-level consolidation rule at D-09.1**); DORA↔AI_Act = COMPLEMENTARY (SAME — DORA ICT risk-management framework + AI Act QMS + Art. 26(1) deployer measures stack for DORA financial entities deploying high-risk AI; three-lines-of-defence + QMS compatible governance architectures))
```

### from regs/AI_Act.md body

*(GV.PO-01 — Organizational cybersecurity policy established, communicated, enforced — anchors the AI Act Art. 17(1) QMS documented `in a systematic and orderly manner in the form of written policies, procedures and instructions` mapped to NIST CSF 2.0 GV.PO-01. The 13-element closed list (a)-(m) is the most content-codified of the 5 regulators: it specifies strategies, procedures, and instructions across compliance, design/design control/design verification (per (c)), risk-management-system documentation cross-reference to Art. 9 (per (g)), data quality (per (d) — cross to D-05 Data-Lifecycle), post-market monitoring (per (k) — cross to D-10.1 Continuous Security Monitoring), and other AI-specific controls. The Art. 13(1)+(3) transparency-to-deployers instructions-for-use is the deployer-side policy content delivered alongside the high-risk AI system. The two subcategories together enable the AI Act provider to demonstrate ex post, against the MSA / AI Office supervisory baseline, that the Art. 17(1) QMS documented `written policies, procedures and instructions` were adopted, reviewed, and updated across the AI lifecycle, with the Art. 9 risk-management-system documentation cross-reference operationalising the continuous-iterative risk dimension (cross to D-09.2 — `SR-CRA-066 ambiguity_notes` notes the CRA Art. 13(4) sentence 2 unification rule applies at D-09.2 but not at D-09.1). AI Act Recital 78 explicitly preserves GDPR for personal-data processing, so providers that are also controllers stack the GDPR data-protection policies with the AI Act QMS as a sub-policy.)*

### from regs/AI_Act.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # AI_Act↔GDPR = Y (provider/deployer = controller; AI Act QMS as sub-policy of GDPR data-protection policies; AI Act Recital 78 explicit GDPR preservation); AI_Act↔NIS2 = Y (NSIE deploys high-risk AI; AI Act QMS as sub-policy of NIS 2 entity-level governance framework); AI_Act↔CRA = Y (same product is both CRA-regulated and AI-Act high-risk; CRA Annex I conformity + AI Act QMS stack — no OJ-level consolidation rule at 9.1); AI_Act↔DORA = Y (DORA FE deploys high-risk AI; DORA ICT risk-management framework + AI Act QMS + Art. 26(1) deployer measures stack; three-lines-of-defence + QMS compatible governance architectures); HL engages on overlap

```

### from regs/AI_Act.md body — field `considerations`

```yaml
  considerations: |
    The AI Act information-security-policy obligation at 9.1 is the **provider-side QMS** documented in a systematic and orderly manner in the form of written policies, procedures, and instructions (Art. 17(1)) with the **transparency-to-deployers instructions-for-use** (Art. 13(1)+(3)) as policy-content dimension. Art. 17(1) carries S2 features — `systematic and orderly manner` is VAG-2 (Berry §5.1 — the OJ does not anchor the sense); `quality management system` is POLY-2 with R1 ISO 9001 / R2 ISO/IEC 23053 / R3 internal bespoke — chosen reading: R3 literal (OJ does not name any specific standard); the 3-way AND of `written policies, procedures AND instructions` and the 13-element closed list (a)-(m) are both COORD-2 (per SR-AIACT-017 ambiguity_notes). The 13 enumerated aspects include (a) compliance strategy; (b) design, development, and verification techniques; (c) design, design control, design verification of the high-risk AI system; (d) post-market monitoring; (e) data quality; (f) ... (m) — full content codification (vs GDPR's entity-discretionary content under Art. 24(2) or NIS 2's entity-discretionary content under Recital 56 proportionality). Art. 13(1) `sufficiently transparent` + `appropriate type and degree of transparency` is the central S3 ambiguity (per SR-AIACT-010 ambiguity_notes) — admits three AI-governance senses (explainability / disclosure / interpretability) with different technical implementations — chosen reading: cumulative covering all three senses because the `interpret a system's output AND use it appropriately` opening implicates each. Art. 13(3) `concise, complete, correct and clear` (4-way AND) + `relevant, accessible and comprehensible` (3-way AND) + `characteristics, capabilities and limitations of performance` (POLY triple) — twin 4-way and 3-way adjective coordinations. Art. 17(1)(g) cross-refers to Art. 9 risk-management system, so the QMS is the governance substrate for the substantive Title III obligations. The recipient is the **provider, deployer, MSA, AI Office** on Art. 17(1) QMS documented policies/procedures/instructions + Art. 13(1)+(3) transparency instructions-for-use + Art. 26(1) deployer measures aligned with instructions. For a provider/deployer that is a controller, the AI Act QMS becomes a sub-policy of the GDPR data-protection policies on the GDPR↔AI_Act SAME — COMPLEMENTARY pair (AI Act Recital 78 explicit GDPR preservation). For an NSIE that deploys high-risk AI, the AI Act QMS becomes a sub-policy of the entity-level NIS 2 governance framework on the NIS2↔AI_Act SAME — COMPLEMENTARY pair (the AI Act layer adds the AI-specific 13-element QMS to the NIS 2 risk-analysis policy). For AI-enabled products that are both CRA-regulated and AI-Act high-risk, the CRA Annex I conformity stack coexists with the AI Act QMS stack on the CRA↔AI_Act SAME — COMPLEMENTARY pair (CRA on the product cybersecurity requirements + AI Act on the AI-system quality-management system — no OJ-level consolidation rule at 9.1, unlike 9.2 where CRA Art. 13(4) sentence 2 permits AI Act Art. 9 risk management to substitute for CRA risk assessment). For a DORA financial entity that deploys high-risk AI, the DORA ICT risk-management framework + AI Act QMS + Art. 26(1) deployer measures stack on the DORA↔AI_Act SAME — COMPLEMENTARY pair (three-lines-of-defence + QMS compatible governance architectures). (Copied from the HSO Considerations block of `### 9.1.5`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=AI_Act; demoted=4; core_cross_mentions=2 -->
