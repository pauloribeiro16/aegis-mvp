# D-09.2 — AI Act module

> Regulation-specific layer: applies when `AI_Act` is in scope
> (activation: `if AI_Act in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| AI_Act | SO-AIACT-001 | Continuous, iterative risk-management system across AI lifecycle (Art. 9(1) `established, implemented, documented and maintained`) with 4-step process (Art. 9(2)(a) identify/analyse known + reasonably foreseeable risks; (b) estimate/evaluate reasonably-foreseeable-misuse risks; (c) evaluate post-market-monitoring-data risks; (d) adopt appropriate and targeted risk-management measures); cross-coupled with Art. 27 FRIA for certain Annex III categories. | AI-system pre-market + post-market risk-management system; Art. 9 risk management as the FRIA-equivalent; **subject to CRA Art. 13(4) sentence 2 consolidation rule** with CRA Art. 13(3) risk assessment. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **AI_Act** | AI-system risk (high-risk AI system lifecycle dimension) — continuous iterative risk-management system | high-risk AI system lifecycle (continuous + iterative per Art. 9(1) `established, implemented, documented and maintained in relation to high-risk AI systems`) | 4-step Art. 9(2) closed list: (a) the identification and analysis of the known and the reasonably foreseeable risks to health, safety and fundamental rights; (b) the estimation and evaluation of the risks emerging from use under conditions of reasonably foreseeable misuse; (c) the evaluation of other risks arising from analysis of post-market monitoring data; (d) the adoption of appropriate and targeted risk-management measures; cross-coupled with Art. 27 FRIA for certain Annex III categories | continuous + iterative across AI lifecycle per Art. 9(1) `established, implemented, documented and maintained` | provider + MSA + AI Office — Art. 9(1) `established, implemented, documented and maintained` + Art. 9(2) 4-step documentation + Art. 27 FRIA documentation for certain Annex III categories + cross-coupling with deployer measures per Art. 26(1) | Art. 9(1) `established, implemented, documented and maintained` + Art. 9(2) 4-step closed list (a)-(d) `known and the reasonably foreseeable risks to health, safety and fundamental rights` + `reasonably foreseeable misuse` + `post-market monitoring data` + `appropriate and targeted risk-management measures` + Art. 27 FRIA for certain Annex III categories + Art. 26(1) deployer measures aligned with provider instructions |

## Sub-SO (AI Act)

#### D-09.2.5 — Sub-SO for AI Act

```yaml
id: SO-D-09.2.AI_Act
subdomain: D-09.2
applies_to: [AI_Act]
inherits_from: SO-AIACT-001
source_SR: SR-AIACT-001 + SR-AIACT-002
activation: if AI_Act in applicable_regs
phase_1A_role: 1_of_5
```

**Objective.** A risk management system is **established, implemented, documented and maintained** in relation to high-risk AI systems (Art. 9(1) AI Act), comprising the four Art. 9(2)(a)-(d) steps: identify and analyse known and reasonably foreseeable risks; estimate and evaluate reasonably-foreseeable-misuse risks; evaluate post-market-monitoring-data risks; and adopt appropriate and targeted risk-management measures.

**CSF anchors (from `SR-AIACT-001` + `SR-AIACT-002` v0.3 security_rationale):**
GV.RM-01, GV.RM-06, ID.RA-03, ID.RA-04, ID.RA-06.
**AI RMF anchors (from `SR-AIACT-001`, `SR-AIACT-002` — dashboard `00_VISUALISATIONS/AI_Act/AI_Act_Dashboard.html`, mechanical uniformization):**
GOVERN-1.1, GOVERN-1.3, GOVERN-1.5, MAP-5.1, MAP-3.1, MAP-3.2, MANAGE-1.2.

---


## Security Requirements (AI Act)

#### 9.2.5 — Provider-side continuous iterative Art. 9 risk-management system with 4-step process + Art. 27 FRIA; subject to CRA Art. 13(4) sentence 2 consolidation rule

```yaml
- req_id: 9.2.5
  volere_section: 15
  volere_subtype: integrity

  title: "Provider establishes, implements, documents, and maintains a continuous iterative risk-management system across the AI lifecycle with the four Art. 9(2)(a)-(d) steps, cross-coupled with Art. 27 FRIA for certain Annex III categories"

  derives_from:
    hso_sub_so: SO-9.2.AI_Act
    per_reg_so: SO-AIACT-001
    source_sr: SR-AIACT-001 + SR-AIACT-002
    hso_file: ../../HierarchicalSecurityObjectives/D-09_Governance-Documentation/9.2.md
    objective_ref_section: "### 9.2.5"

  description: |
    The product shall ensure that the provider of a high-risk AI system establishes, implements, documents, and maintains a continuous iterative risk-management system across the AI lifecycle (per AI Act Art. 9(1)) running the four Art. 9(2)(a)-(d) steps (identify/analyse known + reasonably foreseeable risks; estimate/evaluate reasonably-foreseeable-misuse risks; evaluate post-market-monitoring-data risks; adopt appropriate and targeted risk-management measures), cross-coupled with Art. 27 FRIA documentation for certain Annex III categories.

  fit_criterion: |
    A continuous iterative risk-management system is established, implemented, documented, and maintained across the AI lifecycle under Art. 9(1) `established, implemented, documented and maintained` (SR-AIACT-001) with ID.RA-05 threats-vulnerabilities-likelihoods-impacts dimension (Art. 9(2)(a) `the identification and analysis of the known and the reasonably foreseeable risks to health, safety and fundamental rights` + Art. 9(2)(b) `the estimation and evaluation of the risks emerging from use under conditions of reasonably foreseeable misuse` + Art. 9(2)(c) `the evaluation of other risks arising from analysis of post-market monitoring data`) + GV.RM-04 strategic-direction-and-review-coupling dimension (Art. 9(2)(d) `the adoption of appropriate and targeted risk-management measures` with documented feedback into the AI lifecycle); the risk-management system runs the **4-step Art. 9(2)(a)-(d) process**: (a) identify and analyse known and reasonably foreseeable risks to health, safety and fundamental rights; (b) estimate and evaluate risks emerging from use under conditions of reasonably foreseeable misuse (adversarial use + out-of-scope use + accidental misuse); (c) evaluate other risks arising from analysis of post-market monitoring data per Art. 72 + Art. 73 incident reporting; (d) adopt appropriate and targeted risk-management measures (elimination first where reasonably practicable, then engineering controls + protective + information measures); the system is **continuous iterative** across the AI lifecycle (design → development → placement on market → operation → post-market monitoring → significant modification → decommissioning) with documented iteration triggers and review cadences; the system is **cross-coupled** with Art. 27 FRIA for certain Annex III categories (deployer-side Fundamental Rights Impact Assessment) where the high-risk AI system is in Annex III and deployed by public authorities + private actors providing public services + banking + insurance + employment + law enforcement + migration + justice + democratic-process use cases — the FRIA documents the fundamental-rights risk dimension that complements the Art. 9 risk-management system on the deployer side; **CRITICAL consolidation rule** — CRA Art. 13(4) sentence 2 unification: for AI-enabled CRA-regulated products (the SAME product is both CRA-regulated and AI-Act high-risk), a unified AI Act Art. 9 risk-management system substitutes for the CRA Art. 13(3) cybersecurity risk assessment (per SR-CRA-066 ambiguity_notes); this is the ONLY OJ-level cross-regulation consolidation rule in 9.2; the unified artefact must satisfy BOTH Art. 9(2)(a)-(d) + Art. 13(3) sentence 1-3 content (intended purpose + reasonably foreseeable use + Annex I Part I (2) applicability mapping); the provider can demonstrate ex post, against the market surveillance authority + AI Office, that the Art. 9(1) risk-management system was carried out across the AI lifecycle with the 4-step Art. 9(2)(a)-(d) process documented and integrated with Art. 27 FRIA documentation for certain Annex III categories; the provider coordinates with deployer measures per Art. 26(1) `use of the high-risk AI system in accordance with the instructions for use accompanying the system` with the deployer-side Art. 4(5) + Art. 26(1) human-oversight measures layered on the provider-side risk-management measures; **AI Act risk management does NOT address data-subject rights** (per CRDA flag DomainAnalysis §9.2 line 175): the GDPR DPIA on data-subject rights must be a separate artefact even when the AI Act Art. 9 risk-management system is in place; AI Act Recital 78 explicit GDPR preservation.

  priority: MUST
  verification_method: TEST
  dependencies: [9.2.3 (when product is both CRA-regulated and AI-Act high-risk — CRA Art. 13(4) sentence 2 consolidation rule permits AI Act Art. 9 risk-management system to substitute for CRA Art. 13(3) cybersecurity risk assessment on a single artefact; the ONLY OJ-level cross-regulation consolidation rule in 9.2), 9.2.1 (when high-risk AI processes personal data — AI Act Art. 9 continuous iterative + GDPR DPIA pre-launch on-change; DIFFERENT-PERSPECTIVE, distinct artefacts, **no OJ-level consolidation rule**; AI Act Recital 78 explicit GDPR preservation), 9.2.2 (when NSIE deploys high-risk AI — NIS 2 entity-level operational + AI Act AI-system-level continuous iterative; COMPLEMENTARY), 9.2.4 (when DORA FE deploys high-risk AI — DORA entity-level operational + AI Act AI-system-level continuous iterative; COMPLEMENTARY, **no OJ-level consolidation rule** — DORA has no equivalent to CRA Art. 13(4) sentence 2)]

  nist_csf: [GV.RM-01, GV.RM-06]
  nist_airmf: [GOVERN-1.1, GOVERN-1.3, GOVERN-1.5, MAP-5.1]

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

**AI_Act article (verbatim, Art. 9(1) + Art. 9(2)):**
> "A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems." — Art. 9(1) AI Act (per SR-AIACT-001)
> "The risk management system shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks to health, safety and fundamental rights; (b) the estimation and evaluation of the risks emerging from use under conditions of reasonably foreseeable misuse; (c) the evaluation of other risks arising from analysis of post-market monitoring data; (d) the adoption of appropriate and targeted risk management measures …" — Art. 9(2)(a)–(d) AI Act (per SR-AIACT-002)

**AI_Act article (verbatim, Art. 9(1) + Art. 9(2)):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/AI_Act.md body — field `verified_relationship`

```yaml
verified_relationship: DIFFERENT-PERSPECTIVE / COMPLEMENTARY (CRDA-deep, D-09.2: GDPR↔AI_Act = DIFFERENT-PERSPECTIVE (SAME — pre-launch DPIA on data-subject rights vs continuous iterative AI Act Art. 9 risk management; AI Act Recital 78 explicit GDPR preservation; **no OJ-level consolidation**); NIS2↔AI_Act = COMPLEMENTARY (SAME — NIS 2 entity-level operational + AI Act AI-system-level continuous iterative); **CRA↔AI_Act = COMPLEMENTARY (SAME) — CRITICAL CONSOLIDATION RULE**: CRA Art. 13(4) sentence 2 unification rule permits the AI Act Art. 9 risk-management system to substitute for the CRA Art. 13(3) cybersecurity risk assessment when both apply to the same product; **only OJ-level cross-regulation consolidation rule in D-09.2**; DORA↔AI_Act = COMPLEMENTARY (SAME — DORA entity-level operational + AI Act AI-system-level continuous iterative; **no OJ-level consolidation**))
```

### from regs/AI_Act.md body

*(ID.RA-05 — Threats, vulnerabilities, likelihoods, impacts used to understand inherent risk and inform risk response — anchors the AI Act Art. 9(1) + Art. 9(2)(a)-(d) continuous iterative risk-management system across AI lifecycle mapped to NIST CSF 2.0 ID.RA-05. GV.RM-04 — Strategic direction for risk response — anchors the continuous-iterative dimension per DomainAnalysis §D-09.2 line 180 cross-validation. The 4-step Art. 9(2)(a)-(d) process — (a) identify/analyse known + reasonably foreseeable risks to health, safety and fundamental rights; (b) estimate/evaluate reasonably-foreseeable-misuse risks; (c) evaluate post-market-monitoring-data risks; (d) adopt appropriate and targeted risk-management measures — defines the AI-system-level continuous iterative assessment methodology. **CRITICAL CONSOLIDATION RULE — CRA Art. 13(4) sentence 2 unification**: for AI-enabled CRA-regulated products, a unified AI Act Art. 9 risk-management system substitutes for the CRA Art. 13(3) cybersecurity risk assessment (per SR-CRA-066 ambiguity_notes); this is the only OJ-level cross-regulation consolidation rule in D-09.2. The two subcategories together enable the AI Act provider / deployer to demonstrate ex post, against the MSA / AI Office + Art. 27 FRIA documentation for certain Annex III categories, that the Art. 9(1) `established, implemented, documented and maintained` risk-management system was carried out across the AI lifecycle with the 4-step Art. 9(2)(a)-(d) process documented and applied to the high-risk AI system, with post-market monitoring integrated per Art. 9(2)(c) and reasonable foreseeability scoping per Art. 9(2)(a) + (b). **Note — AI Act risk management does NOT address data-subject rights**: per CRDA flag (DomainAnalysis §D-09.2 line 175), the GDPR DPIA on data-subject rights must be a separate artefact even when the AI Act Art. 9 risk-management system is in place; AI Act Recital 78 explicit GDPR preservation.)*

### from regs/AI_Act.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # AI_Act↔GDPR = Y (high-risk AI processes personal data; AI Act Recital 78 explicit GDPR preservation; **no OJ-level consolidation rule**); AI_Act↔NIS2 = Y (NSIE deploys high-risk AI; NIS 2 entity-level operational + AI Act AI-system-level continuous iterative); AI_Act↔CRA = Y (**CRITICAL CONSOLIDATION RULE** — CRA Art. 13(4) sentence 2 unification rule; AI Act Art. 9 risk-management system substitutes for CRA Art. 13(3) cybersecurity risk assessment when both apply to the same product; only OJ-level cross-regulation consolidation rule in 9.2); AI_Act↔DORA = Y (DORA FE deploys high-risk AI; DORA entity-level operational + AI Act AI-system-level continuous iterative; **no OJ-level consolidation rule**); HL engages on overlap

```

### from regs/AI_Act.md body — field `considerations`

```yaml
  considerations: |
    The AI Act impact-and-risk-assessment obligation at 9.2 is the **continuous iterative risk-management system** under Art. 9(1) `established, implemented, documented and maintained` with the **4-step Art. 9(2)(a)-(d) process** and Art. 27 FRIA for certain Annex III categories. The risk object is **AI-system risk** (health, safety, fundamental rights). Art. 9(1) `established, implemented, documented and maintained` carries S2 features — `continuously iterative across the AI lifecycle` (chosen reading: ongoing operational frequency with documented iteration triggers); the 4-step Art. 9(2)(a)-(d) closed list is a **full content template** with sub-steps (a) known + reasonably foreseeable risks (b) reasonably foreseeable misuse risks (c) post-market-monitoring-data risks (d) appropriate + targeted risk-management measures — elimination first + engineering controls + protective + information measures per Recital 95; the 4-step process is a COORD-2 with sequencing implications — step (a) feeds (b) + (c) which together inform (d); the iterative loop feeds post-market monitoring back into step (a) per Art. 72 incident + serious-incident reporting. **Art. 27 FRIA cross-coupling** for certain Annex III categories: deployer-side Fundamental Rights Impact Assessment (Art. 27(1)) documented `before first use of the system` (Art. 27(3)) with content per Art. 27(4) — categories of data subjects + relevant fundamental-rights implications + reasonably foreseeable risks + measures to address them; cross-coupled with the provider-side Art. 9 risk-management system on the deployer side. **CRITICAL consolidation rule — CRA Art. 13(4) sentence 2**: for AI-enabled CRA-regulated products (the SAME product is both CRA-regulated and AI-Act high-risk), a unified AI Act Art. 9 risk-management system substitutes for the CRA Art. 13(3) cybersecurity risk assessment (per SR-CRA-066 ambiguity_notes); the unified artefact must satisfy BOTH Art. 9(2)(a)-(d) + Art. 13(3) sentence 1-3 content. This is the **ONLY OJ-level cross-regulation consolidation rule in 9.2** and no other cross-regulation substitution is OJ-permitted. **AI Act risk management does NOT address data-subject rights** (per CRDA flag DomainAnalysis §9.2 line 175): the GDPR DPIA on data-subject rights must be a separate artefact even when the AI Act Art. 9 risk-management system is in place; AI Act Recital 78 explicit GDPR preservation. The recipient is the **provider-supervised + market surveillance authority (MSA) + AI Office** on Art. 9(1) `established, implemented, documented and maintained` + Art. 9(2) 4-step documentation + Art. 27 FRIA documentation for certain Annex III categories + Art. 26(1) deployer-measures alignment per provider instructions for use (cross to D-13 deployer instructions). For a DORA financial entity deploying CRA-conformant high-risk AI (a vertically-integrated 5-reg stack), the high-level SO surfaces the 5-assessment architecture (GDPR pre-launch DPIA + NIS 2 continuous operational risk-analysis policy + CRA pre-market + support-period cybersecurity risk assessment consolidated with AI Act Art. 9 on a single artefact per Art. 13(4) sentence 2 + DORA continuous + at-least-yearly ICT risk framework = 4 artefacts with 1 consolidation, not 5; AI Act Art. 9 + CRA Art. 13(3) collapse onto one artefact).
```

<!-- aegis:purity: own_reg=AI_Act; demoted=4; core_cross_mentions=2 -->
