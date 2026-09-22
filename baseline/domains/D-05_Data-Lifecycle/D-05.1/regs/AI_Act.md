# D-05.1 — AI Act module

> Regulation-specific layer: applies when `AI_Act` is in scope
> (activation: `if AI_Act in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| AI_Act | SO-AIACT-003 + SO-AIACT-004 | High-risk AI training/validation/testing datasets meet quality criteria (relevant/representative/free of errors/complete) + bias-detection data governance (8-element list) + exceptional special-category processing for bias correction (6 cumulative conditions (a)–(f)) | Training data; provider-driven; Art. 10(1)/(2)/(3)/(5); ID.AM-03 + ID.AM-08 + PR.PS-06 + PR.DS-01 + GV.OC-03 |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **AI_Act** | training data (high-risk AI training/validation/testing datasets) | training of high-risk AI systems with data; bias detection and correction in those datasets | dataset quality criteria `relevant, sufficiently representative, and to the best extent possible, free of errors and complete` (Art. 10(3)) + 8-element data-governance practice (Art. 10(2) (a)–(h)) + special-category 6-cumulative-condition gateway (Art. 10(5) (a)–(f)) | training pipeline (upstream of runtime) | national competent authority + MSA — Annex IV technical documentation + Art. 10(2) data-governance records + Art. 10(5) safeguard records | Art. 10(1) + Art. 10(2) 8-element list (a)–(h) + Art. 10(3) 4-criterion quality + Art. 10(5) 6-cumulative-condition gateway |

## Sub-SO (AI Act)

#### D-05.1.3 — Sub-SO for AI_Act

```yaml
id: SO-D-05.1.AIACT
subdomain: D-05.1
applies_to: [AI_ACT]
inherits_from: SO-AIACT-003, SO-AIACT-004
source_SR: SR-AIACT-003, SR-AIACT-004, SR-AIACT-005, SR-AIACT-006
activation: if AI_ACT in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** High-risk AI systems which make use of techniques involving the training of AI models with data are developed on the basis of training, validation and testing data sets that meet the quality criteria — relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose (Art. 10(3)) — supported by data governance practices that detect, prevent and mitigate possible biases (Art. 10(1) + Art. 10(2) 8-element closed list (a)–(h)).

- `biases` carries POLY ambiguity (statistical / algorithmic / societal); chosen reading is cumulative with all three senses in scope (per SR-AIACT-004 ambiguity_notes); the 8-element closed list is AND-coordinated so partial compliance with six of eight does not satisfy Art. 10.

**CSF anchors (from `SR-AIACT-003` + `SR-AIACT-004` + `SR-AIACT-005`
+ `SR-AIACT-006` v0.3 security_rationale):**
ID.AM-03, ID.AM-08, PR.PS-06, PR.DS-01, GV.OC-03.

---


## Security Requirements (AI Act)

#### 5.1.3 — High-risk AI training-data quality per Art. 10(1)/(2)/(3) with Art. 10(5) 6-cumulative-condition special-category gateway

```yaml
- req_id: 5.1.3
  volere_section: 15
  volere_subtype: privacy

  title: "High-risk AI training/validation/testing datasets meet Art. 10(3) quality criteria and Art. 10(2) 8-element data-governance practice; Art. 10(5) special-category 6-cumulative-condition gateway documented when applicable"

  derives_from:
    hso_sub_so: SO-D-05.1.AIACT
    per_reg_so: SO-AIACT-003, SO-AIACT-004
    source_sr: SR-AIACT-003, SR-AIACT-004, SR-AIACT-005, SR-AIACT-006
    hso_file: ../../HierarchicalSecurityObjectives/D-05_Data-Lifecycle/D-05.1.md
    objective_ref_section: "### D-05.1.3"

  description: |
    The product shall develop high-risk AI systems on the basis of training, validation and testing data sets that meet the quality criteria of being relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose (Art. 10(3)), supported by data governance practices that detect, prevent and mitigate possible biases per the Art. 10(2) 8-element closed list (a)–(h); exceptional special-category processing for bias detection and correction is permitted only when all 6 cumulative Art. 10(5) conditions (a)–(f) are satisfied (Art. 10(1) + Art. 10(2) + Art. 10(3) + Art. 10(5)).

  fit_criterion: |
    A provider-side training-pipeline data-governance architecture is operated under ID.AM-03 datasets and corresponding metadata inventory (data sources through preparation operations to deployed model, with bias-detection (f) and bias-detection/prevention/mitigation (g) records) + ID.AM-08 data managed consistent with the provider's risk strategy (the upstream control that (f) and (g) operationalise) + PR.PS-06 secure software development practices integrated (the secure engineering pipeline into which data-collection, preparation and bias-mitigation practices are embedded) + PR.DS-01 data-at-rest CIA protected (the pseudonymisation, differential-privacy and federated-learning techniques that constitute the state-of-the-art privacy-preserving measures referenced by the Art. 10(5) safeguards clause) + GV.OC-03 legal/regulatory/contractual requirements regarding cybersecurity understood and managed (the legal-and-regulatory understanding substrate that the cross-regulation GDPR Art. 9 interaction requires); the Art. 10(2) 8-element closed list (a)–(h) is AND-coordinated so partial compliance with six of eight does not satisfy Art. 10; the Art. 10(3) 4-criterion quality benchmark (relevant, sufficiently representative, free of errors, complete) is verified per dataset; when special-category personal data is processed for bias detection and correction, the Art. 10(5) 6-cumulative-condition gateway is documented: (a) bias detection and correction cannot be effectively achieved by processing other data, (b) special categories are strictly necessary and limited to the bias detection and correction, (c) effective technical and organisational safeguards in place, (d) datasets subject to enhanced data governance, (e) safeguards documented, (f) special-category data deleted after the bias detection and correction; `biases` is read cumulatively across statistical / algorithmic / societal senses; outside the narrow Art. 10(5) window, the AI Act does not trigger special-categor... (line truncated to 2000 chars)

  priority: MUST
  verification_method: TEST
  dependencies: [5.1.1 (when high-risk AI provider processes personal data — AI Act Art. 10(5) operates as a narrow permission into the GDPR Art. 9(1) prohibition, conditioned on 6 cumulative safeguards (a)–(f); outside the Art. 10(5) window, GDPR Art. 9(1) binds and the AI Act gateway does not extend the controller-side processing basis), 5.1.2 (when CRA-classified high-risk AI product — upstream AI Act training-data quality feeds downstream CRA runtime minimisation; 3-track matrix applies with explicit upstream-to-downstream minimisation hand-off)]

  nist_csf: [ID.AM-03, ID.AM-08, PR.PS-06, PR.DS-01, GV.OC-03]

  applicable_if:
    regs: [AI_ACT]
  satisfaction:
    controls: []
    nodes: []

```

---


## Verbatim regulatory basis (AI Act)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**AI_Act article (verbatim, Art. 10(2)(f)/(g) + Art. 10(5)):**
> "Training, validation and testing data sets shall be relevant, representative and, to the best extent possible, free of errors and complete. They shall have the appropriate statistical properties, including where applicable, as regards the persons or groups of persons on which the high-risk AI system is intended to be used. These properties of the data sets can be met at the level of individual data sets or a combination thereof … The data sets shall take into account, to the extent required by their intended purpose, the characteristics or elements that are particular to the specific geographical, behavioural or functional setting within which the high-risk AI system is intended to be used." — AI Act Art. 10(3)
>
> "Where it is not possible to fully comply with paragraph 4 in order to detect and prevent biases in relation to the training, validation and testing datasets of high-risk AI systems referred to in points (a) and (b) of Article 6(2), the providers of such systems may exceptionally process special categories of personal data referred to in Article 9(1) of Regulation (EU) 2016/679 … insofar as the following conditions are fulfilled: (a) the bias detection and correction cannot be effectively achieved by processing other data; (b) the special categories of personal data are processed strictly necessary and limited to the bias detection and correction; (c) the providers have put in place effective technical and organisational safeguards to protect the data; (d) the datasets used for bias detection and correction are subject to enhanced data governance; (e) the safeguards are documented; (f) the special-category data are deleted after the bias detection and correction." — AI Act Art. 10(5)

**AI_Act article (verbatim, Art. 10(1)–(3)):**
> "High-risk AI systems which make use of techniques involving the training of AI models with data shall be developed on the basis of training, validation and testing data sets that meet the quality criteria referred to in paragraphs 2 to 5 whenever such data sets are used." — AI Act Art. 10(1)
>
> "Training, validation and testing data sets shall be relevant, representative and, to the best extent possible, free of errors and complete." — AI Act Art. 10(3)

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/AI_Act.md body — field `verified_relationship`

```yaml
verified_relationship: NON-SAME (CRDA-deep, D-05.1: GDPR↔AI_Act = CORRECTED from CONTRADICTORY to SCOPE-DISJOINT with Art. 10(5) carve-out; CRA↔AI_Act = COMPLEMENTARY (SAME — runtime vs training lifecycle stages))
```

### from regs/AI_Act.md body

**Considerations.**

- The Art. 10(5) special-category exception is the single overlap point with GDPR Art. 9(1) in D-05.1; outside the narrow Art. 10(5) window (high-risk AI provider training a system with bias-detection needs that cannot be met by non-special-category data, all 6 cumulative conditions (a)–(f) satisfied), the AI Act does not trigger special-category processing and the GDPR ↔ AI_Act pair is scope-disjoint in baseline.

### from regs/AI_Act.md body

- CRA-side coverage of training data quality is sequential not concurrent — CRA Annex I Part I (2)(g) operates at runtime on product data; AI Act Art. 10 operates upstream on the training pipeline; the two obligations compose into a 3-track matrix when training data flows into a CRA-classified runtime product.

### from regs/AI_Act.md body

*(`SR-AIACT-003` covers the Art. 10(1)/(2) 8-element data-governance
practice anchored to ID.AM-03 (inventories of data and corresponding
metadata for designated data types — the dataset-inventory substrate
for traceability from data sources through preparation operations to
deployed model) + ID.AM-08 (data managed consistent with the
organisation's risk strategy — the upstream control that the
bias-examination (f) and bias-detection/prevention/mitigation (g)
duties operationalise) + PR.PS-06 (secure software development
practices integrated, performance monitored throughout the SDLC —
the secure engineering pipeline into which data-collection,
preparation and bias-mitigation practices are embedded). `SR-AIACT-004`
covers the Art. 10(5) 6-cumulative-condition special-category
gateway anchored to ID.AM-08 + PR.DS-01 (data-at-rest CIA protected
— including the pseudonymisation, differential-privacy and
federated-learning techniques that constitute the state-of-the-art
privacy-preserving measures referenced by the safeguards clause) +
GV.OC-03 (legal/regulatory/contractual requirements regarding
cybersecurity — including privacy and civil-liberties obligations —
understood and managed — the legal-and-regulatory understanding
substrate that the cross-regulation GDPR Art. 9 interaction requires).
`SR-AIACT-005` covers the Art. 10(3) 4-criterion dataset quality
benchmark anchored to ID.AM-08 + PR.DS-01. `SR-AIACT-006` covers the
Art. 10(5) exceptional special-category processing anchored to
ID.AM-08 + PR.DS-01 + GV.OC-03. The five subcategories together
operationalise the AI Act training-pipeline upstream data quality +
data-governance + special-category gateway architecture.)*

### from regs/AI_Act.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # AI_Act↔GDPR = Conditional (Y in the Art. 10(5) window only — high-risk AI provider processing special-category data for bias correction with all 6 conditions (a)–(f) satisfied; N outside the window; the AI Act provider is also a controller when the training data is personal); AI_Act↔CRA = Conditional (Y sequential — training data flows into runtime CRA product; disjoint in baseline — different lifecycle stages, runtime vs training pipeline); HL engages on overlap

```

### from regs/AI_Act.md body — field `considerations`

```yaml
  considerations: |
    The AI Act data-minimisation obligation is the high-risk AI training-pipeline data-governance architecture anchored on the Art. 10(3) 4-criterion quality benchmark plus the Art. 10(2) 8-element closed list plus the Art. 10(5) 6-cumulative-condition special-category gateway. The Art. 10(5) provision is the single overlap point with GDPR Art. 9(1) in D-05.1; outside the narrow Art. 10(5) window (high-risk AI provider training a system with bias-detection needs that cannot be met by non-special-category data, all 6 cumulative conditions (a)–(f) satisfied), the AI Act does not trigger special-category processing and the GDPR ↔ AI_Act pair is scope-disjoint in baseline. CRA-side coverage of training data quality is sequential not concurrent — CRA Annex I Part I (2)(g) operates at runtime on product data; AI Act Art. 10 operates upstream on the training pipeline; the two obligations compose into a 3-track matrix when training data flows into a CRA-classified runtime product. `biases` carries POLY ambiguity (statistical / algorithmic / societal); the chosen reading is cumulative with all three senses in scope; the 8-element closed list is AND-coordinated so partial compliance with six of eight does not satisfy Art. 10. (Copied from the HSO Considerations block of `### D-05.1.3`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=AI_Act; demoted=6; core_cross_mentions=2 -->