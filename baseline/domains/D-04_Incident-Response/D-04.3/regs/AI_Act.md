# D-04.3 — AI Act module

> Regulation-specific layer: applies when `AI_Act` is in scope
> (activation: `if AI_Act in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| AI Act | SO-AIACT-013 | 15d / 10d / 2d tiered serious incident reporting | High-risk AI serious incident; provider / deployer → MSA |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **AI Act** | serious incident (Art. 3(49), 3 sub-categories) | high-risk AI system (or GPAI for Art. 55) | market surveillance authorities (or AI Office for GPAI) | Art. 73(1)–(4) | 15d default; 10d (death); 2d (widespread infringement) |

## Sub-SO (AI Act)

#### D-04.3.5 — Sub-SO for AI Act

```yaml
id: SO-D-04.3.AI_Act
subdomain: D-04.3
applies_to: [AI_Act]
inherits_from: SO-AIACT-013
source_SR: SR-AIACT-022
activation: if AI_Act in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** A serious incident involving a high-risk AI system is reported to the market surveillance authorities of the Member States where the incident occurred under a differentiated 4-timeline × 4-trigger matrix (Art. 73(1)–(4)): 15 days after the provider becomes aware (default); 10 days if the incident results in death; 2 days for widespread infringement; 15 days from reasonable likelihood of causal link (whichever is later with the awareness trigger, per Art. 73(2)).

- GPAI providers of systemic-risk models separately report under `SR-AIACT-024` / `SO-AIACT-014` to the AI Office without undue delay — distinct recipient, separate clock. The AI Act therefore introduces two distinct recipient classes (MSAs for high-risk AI serious incidents, AI Office for GPAI systemic-risk incidents), each with its own clock pattern.

**CSF anchors (from `SR-AIACT-022` v0.3 security_rationale):**
RS.CO-02, RS.CO-04, RS.MA-03, RS.MA-01.

---


## Security Requirements (AI Act)

#### 4.3.5 — 4-trigger × 4-timeline serious incident reporting to MSAs (high-risk) / AI Office (GPAI)

```yaml
- req_id: 4.3.5
  volere_section: 15
  volere_subtype: audit

  title: "Serious incident involving high-risk AI reported to market surveillance authorities under 4-trigger × 4-timeline matrix (15d default / 10d death / 2d widespread / 15d causal-link-anchor); GPAI systemic-risk report separately to AI Office under Art. 55"

  derives_from:
    hso_sub_so: SO-4.3.AI_Act
    per_reg_so: SO-AIACT-013
    source_sr: SR-AIACT-022
    hso_file: ../../HierarchicalSecurityObjectives/D-04_Incident-Response/4.3.md
    objective_ref_section: "### 4.3.5"

  description: |
    The product shall report any serious incident — per the Art. 3(49) three-sub-category definition ((a) death; (b) serious harm to health; (c) serious infringement of fundamental rights) — involving a high-risk AI system to the market surveillance authorities of the Member States where the incident occurred under the differentiated 4-timeline × 4-trigger matrix of Art. 73(1)–(4): 15 days after the provider becomes aware (default, Art. 73(1)/(4)); 10 days if the incident results in death (Art. 73(2)); 2 days for widespread infringement (Art. 73(3)); 15 days from reasonable likelihood of causal link, whichever is later with the awareness trigger (Art. 73(2) causal-link-anchor); additionally, GPAI providers of systemic-risk models separately report under Art. 55 (GPAI Article 55) / `SR-AIACT-024` / `SO-AIACT-014` to the AI Office without undue delay — distinct recipient, separate clock, two recipient classes in total (MSA for high-risk AI serious incidents; AI Office for GPAI systemic-risk incidents) (AI Act Art. 3(49) sub-categories (a)/(b)/(c) + Art. 73(1)–(4) 4-trigger × 4-timeline matrix + Art. 55 GPAI).

  fit_criterion: |
    An MSA-notification pipeline is operated with 4-trigger × 4-timeline matrix discipline: the default 15d timeline fires upon provider awareness (per Art. 73(1)/(4) — `15 days after the date on which the provider becomes aware`); the 10d timeline fires when the serious incident results in death (per Art. 73(2)); the 2d timeline fires when the serious incident constitutes widespread infringement (per Art. 73(3)); the causal-link-anchor 15d fires from the reasonable likelihood of causal link, whichever is later with the awareness trigger (per Art. 73(2) literal); the provider classifies the incident against the Art. 3(49) three-sub-category definition ((a) death; (b) serious harm to health; (c) serious infringement of fundamental rights) before the timeline is selected; the MSAs of the Member States where the incident occurred receive the report via the MS-determined routing channel; the report contains at minimum: a description of the incident; the category of serious incident (death / serious harm / fundamental rights infringement); the impact and consequences; the AI system's identification; the corrective measures taken; the planned follow-up; for GPAI systemic-risk models, a separate Art. 55 report to the AI Office fires without undue delay; for events overlapping with GDPR (personal data breach) / NIS 2 (significant incident) / CRA (AEV) / DORA (major ICT incident) on a single underlying event, parallel clocks run — e.g. 2d AI Act widespread + 10d AI Act death + 15d AI Act default + 24h NIS 2 early warning + 72h GDPR/NIS 2/CRA + 14d CRA AEV + 1m NIS 2 final — up to 6 distinct deadlines; the binding-procedure principle (shortest clock binds per recipient, but parallel recipients each get their own deadline) is documented in the notification playbook (Doc 07 downstream); the Art. 73 obligation is the most temporally complex notification clause in the AEGIS corpus; verified by MSA-notification logs review + Art. 3(49) sub-category classification records inspection + 4-trigger × 4-timeline matrix coverage audit + MSA-of-where-occurred routing documentation + parallel-clock binding-principle records inspection (on multi-reg overlap) + AI Office (GPAI Art. 55) notification logs review (when GPAI in scope) + AI Office + MSA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [4.1.5 (notification clock depends on 4.1 awareness event from 4.1 detection leg; AI Act detection obligations are coupled to the Art. 73/55 reporting triggers and not standalone — 4.1 AI Act out-of-scope, but 4.3 AI Act pulls awareness from 4.1 detection capabilities operated at the AI-system boundary), 4.2.5 (notification content requires prior incident-classification feeding Art. 73 content template)]

  nist_csf: [RS.CO-02, RS.CO-04, RS.MA-03, RS.MA-01]

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

**AI_Act article (verbatim):**
> Art. 73(1)–(4) of Regulation (EU) 2024/1689 requires providers of high-risk AI systems, and deployers where applicable, to report any serious incident to the market surveillance authorities of the Member States where the incident occurred. The reporting timeline depends on the severity: 15 days after the provider becomes aware (default), 10 days if the incident results in death, 2 days for widespread infringement.

**AI_Act article (verbatim):**
> Art. 55(1)(c) of Regulation (EU) 2024/1689 requires providers of general-purpose AI models with systemic risk to keep track of, document, and report, without undue delay, to the AI Office and, as appropriate, to national competent authorities, relevant information about serious incidents and possible corrective measures to address them.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/AI_Act.md body — field `verified_relationship`

```yaml
verified_relationship: CONDITIONAL (CRDA-deep, D-04.3 GDPR↔AI_Act: SCOPE-DISJOINT baseline / CONTRADICTORY; NIS2↔AI_Act: SCOPE-DISJOINT baseline / CONTRADICTORY; CRA↔AI_Act: SCOPE-DISJOINT baseline / CONTRADICTORY; DORA↔AI_Act: SCOPE-DISJOINT baseline / CONDITIONAL-CONTRADICTORY)
```

### from regs/AI_Act.md body

**Considerations.**

- The Art. 73 obligation is the most temporally complex notification clause in the AEGIS corpus; the 4-trigger × 4-timeline matrix exceeds any other regulator's single-clock pattern. Operationally, an entity subject to AI Act + GDPR + NIS 2 + CRA + DORA on a single serious AI incident must discharge up to 6 distinct deadlines (2d AI Act widespread-infringement + 10d AI Act death + 15d AI Act default + 24h NIS 2 early warning + 72h GDPR / NIS 2 / CRA + 14d CRA AEV + 1m NIS 2 / CRA final).

### from regs/AI_Act.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # AI_Act↔GDPR = Conditional (Y high-risk AI processes personal data; parallel clocks — AI Act 15d default + GDPR 72h DPA); AI_Act↔NIS2 = Conditional (Y NSIE deploys high-risk AI; parallel clocks — AI Act 15d + NIS 2 24h/72h/1m); AI_Act↔CRA = Conditional (Y CRA product embeds high-risk AI; parallel clocks — AI Act 15d + CRA AEV 24h/72h/14d on different recipient track); AI_Act↔DORA = Conditional (Y FE deploys high-risk AI; parallel clocks — AI Act 15d + DORA `without undue delay` CA, both fire from same awareness moment)

```

### from regs/AI_Act.md body — field `considerations`

```yaml
  considerations: |
    The AI Act notification obligation is the high-risk AI serious-incident MSA notification (Art. 73) + the GPAI systemic-risk AI Office notification (Art. 55); the operational substrate is an MSA-notification pipeline with 4-trigger × 4-timeline matrix discipline. The Art. 73 obligation is the most temporally complex notification clause in the AEGIS corpus; the 4-trigger × 4-timeline matrix exceeds any other regulator's single-clock pattern. Operationally, an entity subject to AI Act + GDPR + NIS 2 + CRA + DORA on a single serious AI incident must discharge up to 6 distinct deadlines (2d AI Act widespread-infringement + 10d AI Act death + 15d AI Act default + 24h NIS 2 early warning + 72h GDPR/NIS 2/CRA + 14d CRA AEV + 1m NIS 2/CRA final). GPAI providers of systemic-risk models separately report under Art. 55 / `SR-AIACT-024` / `SO-AIACT-014` to the AI Office without undue delay — distinct recipient, separate clock. The AI Act therefore introduces two distinct recipient classes (MSAs for high-risk AI serious incidents, AI Office for GPAI systemic-risk incidents), each with its own clock pattern. The Art. 3(49) three-sub-category definition ((a) death; (b) serious harm to health; (c) serious infringement of fundamental rights) is the gating classification test before the timeline is selected. The MSA-of-Member-State-where-the-incident-occurred routing means the report may go to multiple MSAs when the incident spans jurisdictions. (Copied from the HSO Considerations block of `### 4.3.5`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=AI_Act; demoted=4; core_cross_mentions=1 -->

