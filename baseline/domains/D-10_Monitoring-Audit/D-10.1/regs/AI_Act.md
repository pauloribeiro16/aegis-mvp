# D-10.1 — AI Act module

> Regulation-specific layer: applies when `AI_Act` is in scope
> (activation: `if AI_Act in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| AI_Act | SO-AIACT-012 | A post-market monitoring system is established and documented in a manner that is proportionate to the nature of the AI technologies and the risks of the high-risk AI system, actively and systematically collecting, documenting and analysing relevant data to evaluate continued compliance; market-surveillance cooperation under Regulation (EU) 2019/1020 applies (Art. 72(1)–(2) + Art. 74(1)). | AI-system post-market monitoring (lifecycle monitoring of high-risk AI); `proportionate to the nature of the AI technologies and the risks` (qualitative); `actively and systematically collect, document and analyse` (3-way verb AND). |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **AI_Act** | AI-system-level post-market monitoring system + market-surveillance cooperation | Art. 72(1) `Providers shall establish and document a post-market monitoring system in a manner that is proportionate to the nature of the AI technologies and the risks of the high-risk AI system` + Art. 72(2) `The post-market monitoring system shall actively and systematically collect, document and analyse relevant data` + Art. 74(1) market-surveillance cooperation under Regulation (EU) 2019/1020 | AI-system (high-risk AI system per Art. 6) | MSA + AI Office + provider — Art. 72(1)–(2) post-market monitoring system + Art. 74(1) market-surveillance cooperation | Art. 72(1) + Art. 72(2) `actively and systematically collect, document and analyse` 3-way verb AND + Art. 72(3) post-market monitoring plan + Art. 74(1) market-surveillance cooperation + Art. 6 high-risk classification + Art. 9 risk-management-system documentation (cross to D-09.1) |

## Sub-SO (AI Act)

#### D-10.1.5 — Sub-SO for AI Act

```yaml
id: SO-D-10.1.AI_Act
subdomain: D-10.1
applies_to: [AI_Act]
inherits_from: SO-AIACT-012
source_SR: SR-AIACT-021 + SR-AIACT-022
activation: if AI_Act in applicable_regs
phase_1A_role: 5_of_5
```

**Objective.** Providers of high-risk AI systems **establish and document a post-market monitoring system in a manner that is proportionate to the nature of the AI technologies and the risks of the high-risk AI system** (Art. 72(1) AI Act), with the system **actively and systematically collecting, documenting and analysing relevant data** (Art. 72(2) AI Act); market-surveillance cooperation under Regulation (EU) 2019/1020 applies (Art. 74(1) AI Act).

**CSF anchors (from `SR-AIACT-021` + `SR-AIACT-022` v0.3 security_rationale):**
DE.CM-09 (primary), ID.IM-04, GV.OV-03, RS.CO-02, RS.MA-04, RS.MA-03, RS.MA-01.
**AI RMF anchors (from `SR-AIACT-021`, `SR-AIACT-022` — dashboard `00_VISUALISATIONS/AI_Act/AI_Act_Dashboard.html`, mechanical uniformization):**
MANAGE-4.1, MEASURE-3.1, MEASURE-4.1, GOVERN-1.5, MANAGE-2.3, MANAGE-4.3, GOVERN-1.1.
*(DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored — anchors the AI Act Art. 72(2) `actively and systematically collect, document and analyse relevant data` mapped to NIST CSF 2.0 DE.CM-09; ID.IM-04 — Adequate resource capacity to ensure availability is maintained — anchors the post-market monitoring system per DomainAnalysis cross-validation; GV.OV-03 — Cybersecurity risk management strategy outcomes are reviewed and inform changes — anchors the Art. 72 analysis-to-risk-management feedback loop. The three subcategories together enable the AI Act provider to demonstrate ex post, against the MSA + AI Office supervisory baseline, that the Art. 72(1)–(2) post-market monitoring system was operational with the `proportionate to the nature of the AI technologies and the risks` proportionality calibration, and that the `actively and systematically collect, document and analyse` 3-way verb AND was operational across the AI-system lifecycle. The Art. 74(1) market-surveillance cooperation under Regulation (EU) 2019/1020 provides the MSA + AI Office recipient channel.)*

---


## Security Requirements (AI Act)

#### 10.1.5 — AI-system post-market monitoring `proportionate to the nature of the AI technologies and the risks` + analysis-to-risk-management feedback loop

```yaml
- req_id: 10.1.5
  volere_section: 15
  volere_subtype: audit

  title: "Provider of high-risk AI system establishes and documents a post-market monitoring system proportionate to the nature of the AI technologies and the risks, actively and systematically collecting, documenting and analysing relevant data across the AI lifecycle"

  derives_from:
    hso_sub_so: SO-10.1.AI_Act
    per_reg_so: SO-AIACT-012
    source_sr: SR-AIACT-021 + SR-AIACT-022
    hso_file: ../../HierarchicalSecurityObjectives/D-10_Monitoring-Audit/10.1.md
    objective_ref_section: "### 10.1.5"

  description: |
    The product shall establish and document a post-market monitoring system in a manner that is proportionate to the nature of the AI technologies and the risks of the high-risk AI system (per AI Act Art. 72(1) `Providers shall establish and document a post-market monitoring system in a manner that is proportionate to the nature of the AI technologies and the risks of the high-risk AI system`), with the system actively and systematically collecting, documenting and analysing relevant data (per Art. 72(2) `The post-market monitoring system shall actively and systematically collect, document and analyse relevant data`), and market-surveillance cooperation under Regulation (EU) 2019/1020 applying (per Art. 74(1)).

  fit_criterion: |
    A post-market monitoring system is established and documented per Art. 72(1) + Art. 72(2) + Art. 74(1) (SR-AIACT-021 + SR-AIACT-022) verified by DE.CM-09 primary (Computing hardware and software, runtime environments, and their data are monitored — anchors the AI Act Art. 72(2) `actively and systematically collect, document and analyse relevant data` mapped to NIST CSF 2.0 DE.CM-09) + ID.IM-04 (Adequate resource capacity to ensure availability is maintained — anchors the post-market monitoring system per DomainAnalysis cross-validation) + GV.OV-03 (Cybersecurity risk management strategy outcomes are reviewed and inform changes — anchors the Art. 72 analysis-to-risk-management feedback loop); the post-market monitoring system is documented in a manner that is `proportionate to the nature of the AI technologies and the risks` (qualitative proportionality — per SR-AIACT-021 ambiguity_notes, the OJ does not quantify the proportionality; the chosen reading is: a documented proportionality assessment that calibrates the depth of monitoring to the AI technology class and risk category); the Art. 72(2) `actively and systematically collect, document and analyse` 3-way verb AND is operational across the AI-system lifecycle (collection channels + documentation layer + analysis layer + feedback loop); the analysis-to-risk-management feedback loop feeds back into the provider's risk-management-system documentation (Art. 9 — cross to 9.1 AI Act sub-SO) and the AI-system quality management system (Art. 17 — cross to 9.1 AI Act sub-SO); the Art. 72(3) post-market monitoring plan is documented and operational; the Art. 74(1) market-surveillance cooperation under Regulation (EU) 2019/1020 provides the MSA + AI Office recipient channel; the recipient is the **MSA (market surveillance authority) + AI Office + provider** on the Art. 72(1)-(3) post-market monitoring + Art. 74(1) market-surveillance cooperation; verified by MSA + AI Office audit pack (post-market monitoring system documentation, Art. 72 proportionality assessment, Art. 72(2) 3-way verb AND evidence, Art. 72(3) post-market monitoring plan, analysis-to-risk-management feedback loop evidence, Art. 74(1) market-surveillance cooperation evidence) + automated Art. 72(2) 3-way verb AND test (collection channels operational + documentation layer operational + analysis layer operational) + automated analysis-to-risk-management feedback loop test (post-market monitoring analysis feeds back into Art. 9 risk-management-system documentation + Art. 17 QMS). **IMPORTANT — AI Act post-market monitoring feedback loop** (Art. 72(2) `actively and systematically collect, document and analyse` → analysis-to-risk-management loop feeding Art. 9 + Art. 17) is AI-Act-specific and is preserved in this sub-SO. The AI Act Art. 72 monitoring is provider-side and is NOT subject to user opt-out (unlike CRA Annex I Part I (2)(l) opt-out); the CRA opt-out tension does NOT extend to the AI Act pair.

  priority: MUST
  verification_method: TEST
  dependencies: [10.1.1 (when provider/deployer = controller — GDPR pre-breach detection + AI Act lifecycle monitoring on different trigger alignment; pre-breach vs. lifecycle; the two regimes stack without overlap), 10.1.2 (when NSIE deploys high-risk AI — NIS 2 entity-level operational monitoring + AI Act AI-system lifecycle monitoring; different trigger alignment; the two regimes stack without overlap), 10.1.3 (when CRA-regulated product is also high-risk AI system — CRA Annex I conformity + AI Act post-market monitoring stack for AI-enabled products; the AI Act adds the feedback-loop dimension; the CRA opt-out tension does NOT extend to the AI Act pair — the AI Act Art. 72 monitoring is provider-side, not subject to user opt-out), 10.1.4 (when DORA financial entity deploys high-risk AI — DORA continuous monitoring + AI Act post-market monitoring stack; DORA-led stack with AI Act as AI-system-level overlay; the two regimes stack without overlap)]

  nist_csf: [DE.CM-09, ID.IM-04, GV.OV-03]
  nist_airmf: [MANAGE-4.1, MEASURE-3.1, MEASURE-4.1, GOVERN-1.5]

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

**AI_Act article (verbatim, Art. 72(1)–(2)):**
> "Providers shall establish and document a post-market monitoring system in a manner that is proportionate to the nature of the AI technologies and the risks of the high-risk AI system. The post-market monitoring system shall actively and systematically collect, document and analyse relevant data …" — Art. 72(1)–(2) AI Act (per SR-AIACT-021)

**AI_Act article (verbatim, Art. 72(1)–(2)):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/AI_Act.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-10.1: GDPR↔AI_Act = COMPLEMENTARY (SAME — pre-breach detection vs. lifecycle; different trigger alignment); NIS2↔AI_Act = COMPLEMENTARY (SAME — entity-level operational vs. AI-system lifecycle); CRA↔AI_Act = COMPLEMENTARY (SAME — CRA Annex I conformity + AI Act post-market monitoring stack for AI-enabled products; AI Act adds feedback-loop dimension); DORA↔AI_Act = COMPLEMENTARY (SAME — DORA continuous monitoring + AI Act post-market monitoring stack for DORA financial entities deploying high-risk AI))
```

### from regs/AI_Act.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # AI_Act↔GDPR = Conditional (Y when high-risk AI processes personal data — provider is controller; pre-breach vs. lifecycle; different trigger alignment); AI_Act↔NIS2 = Conditional (Y when NSIE deploys high-risk AI; entity-level operational vs. AI-system lifecycle); AI_Act↔CRA = Conditional (Y when CRA-regulated product is also high-risk AI; CRA Annex I conformity + AI Act Art. 72 post-market monitoring stack; AI Act adds feedback-loop dimension; the CRA opt-out tension does NOT extend to the AI Act pair); AI_Act↔DORA = Y (DORA financial entity deploys high-risk AI; DORA continuous monitoring + AI Act post-market monitoring stack; DORA-led stack with AI Act as AI-system-level overlay); HL engages when the AI Act sub-SO activates AND ≥1 other sub-SO activates on Y or Conditional-Y overlap.

```

### from regs/AI_Act.md body — field `considerations`

```yaml
  considerations: |
    The AI Act continuous-monitoring obligation at 10.1 is the **AI-system post-market monitoring system** per Art. 72(1) + Art. 72(2) + Art. 72(3) + Art. 74(1). Art. 72(1) `Providers shall establish and document a post-market monitoring system in a manner that is proportionate to the nature of the AI technologies and the risks of the high-risk AI system` (per SR-AIACT-021) — the `proportionate to the nature of the AI technologies and the risks` proportionality is qualitative (S3 VAG per SR-AIACT-021 ambiguity_notes — OJ does not quantify the proportionality; chosen reading: documented proportionality assessment calibrating depth to AI technology class + risk category). Art. 72(2) `The post-market monitoring system shall actively and systematically collect, document and analyse relevant data` (per SR-AIACT-022) — the 3-way verb AND `actively and systematically collect, document and analyse` is S2 COORD (per SR-AIACT-022 ambiguity_notes). Art. 72(3) post-market monitoring plan; Art. 74(1) market-surveillance cooperation under Regulation (EU) 2019/1020. The analysis-to-risk-management feedback loop feeds back into the provider's risk-management-system documentation (Art. 9 — cross to 9.1 AI Act sub-SO) and the AI-system quality management system (Art. 17 — cross to 9.1 AI Act sub-SO). The recipient is the **MSA + AI Office + provider** on the Art. 72(1)-(3) post-market monitoring + Art. 74(1) market-surveillance cooperation. The AI Act Art. 72 monitoring is provider-side and is **NOT subject to user opt-out** (unlike CRA Annex I Part I (2)(l) opt-out); the CRA opt-out tension does NOT extend to the AI Act pair.
```

<!-- aegis:purity: own_reg=AI_Act; demoted=3; core_cross_mentions=2 -->
