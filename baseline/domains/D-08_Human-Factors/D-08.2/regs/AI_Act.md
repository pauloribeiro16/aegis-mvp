# D-08.2 — AI Act module

> Regulation-specific layer: applies when `AI_Act` is in scope
> (activation: `if AI_Act in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| AI_Act | SO-AIACT-008 + SO-AIACT-011 | Built-in human-oversight capability (Art. 14) + deployer assignment of competent human overseers (Art. 26(2)). | AI-system-specific competence: human overseers must have competence, training, authority. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **AI_Act** | high-risk AI system human overseers (provider-side Art. 14 design + deployer-side Art. 26(2) assignment) — AI-system-specific competence | provider design (Art. 14(1) `High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons`) + deployer assignment (Art. 26(2) `Deployers shall assign human oversight to natural persons who have the necessary competence, training and authority, as well as the necessary support`) — provider-design-by-design + deployer-assignment-on-deployment twin trigger | `as appropriate and proportionate` (Art. 14(4) qualitative) — 5 cumulative abilities must be enabled (Art. 14(4)(a)–(e)); Art. 26(2) 4-element AND: `competence, training AND authority AND support`; no quantitative threshold | provider (QMS design-control documented) + deployer (assignment documented) + market surveillance authority (MSA) (Annex IV technical documentation + Art. 17(1) QMS documented in `systematic and orderly manner`) + AI Office (for GPAI on systemic-risk tracking) | Art. 14(1) + Art. 14(2)–(5) — provider design + Art. 26(2) deployer assignment — competence, training, authority, support 4-element AND; Art. 17(1)(c) QMS design/design-control/design-verification cross to D-07.1; Recital 78 GDPR preservation |

## Sub-SO (AI Act)

#### D-08.2.5 — Sub-SO for AI Act

```yaml
id: SO-D-08.2.AIACT
subdomain: D-08.2
applies_to: [AI_Act]
inherits_from: SO-AIACT-008 + SO-AIACT-011
source_SR: SR-AIACT-013 + SR-AIACT-020
activation: if AI_Act in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** High-risk AI systems are designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use (Art. 14(1) AI Act) — the provider-side design obligation for the human-oversight capability.

**Considerations.**
- The natural persons assigned to human oversight are enabled, as appropriate and proportionate, to discharge the 5 cumulative abilities of Art. 14(4): (a) properly understand the relevant capacities and limitations of the high-risk AI system and foreseeable misuse; (b) remain aware of automation bias; (c) correctly interpret the output; (d) decide not to use the high-risk AI system or to disregard, override or reverse its output; (e) intervene on the operation or interrupt the system through a stop button or similar procedure.
- The 5-element closed list is AND-coordinated (all five must be enabled cumulatively — partial compliance is non-compliance per SR-AIACT-013 ambiguity_notes).
- On the deployer-side assignment obligation, deployers of high-risk AI systems assign human oversight to natural persons who have the necessary competence, training and authority, as well as the necessary support (Art. 26(2) AI Act) — the 4-element AND `competence, training AND authority AND support` (all four required per SR-AIACT-020 ambiguity_notes).
- The provider-design-by-design + deployer-assignment-on-deployment twin-trigger is the AI-Act-specific competence architecture.
- PR.AT-02 anchors the role-understanding dimension — the workforce-supplier analog of `properly understand` (Art. 14(4)(a)) and `correctly interpret` (Art. 14(4)(c)).
- PR.AT-01 anchors the awareness-and-training substrate — `remain aware of automation bias` (Art. 14(4)(b)) + `decide` (Art. 14(4)(d)) + `intervene` (Art. 14(4)(e)) require overseers to detect and respond to AI-specific failure modes including the cognitive-bias correction that `automation bias` operationalises.
- GV.RR-02 supplies the RACI substrate — overseers must hold formal authority to override and interrupt the system.
**CSF anchors (from `SR-AIACT-013` v0.3 + `SR-AIACT-020` v0.3 security_rationale):**
PR.AT-02, PR.AT-01, GV.RR-02.
*(PR.AT-02 covers the role-understanding dimension that sub-points (a) `properly understand` and (c) `correctly interpret` require. PR.AT-01 anchors the awareness-and-training substrate that sub-point (b) `remain aware of automation bias` and sub-points (d) `decide` and (e) `intervene` require, ensuring overseers detect and respond to AI-specific failure modes including the cognitive-bias correction that `automation bias` operationalises. GV.RR-02 supplies the RACI substrate that sub-points (d) and (e) require — overseers must hold formal authority to override and interrupt the system. A provider evidencing PR.AT-02 role understanding, PR.AT-01 awareness training and GV.RR-02 RACI definition demonstrates ex post that the five-element Art. 14(4) oversight-abilities list — cumulative AND of all five abilities plus the last-resort sub-point (e) intervention safety net — is operationalised in the provider's training and tooling programme. The Art. 26(2) deployer-side 4-element AND `competence, training AND authority AND support` adds the deployer's personnel-qualification anchor (PR.AT-02) + the deployer's formal RACI definition (GV.RR-02) + the deployer's HR-practices integration (GV.RR-04 — supplementary).)*

---


## Security Requirements (AI Act)

#### 8.2.5 — AI Act human-overseer 5-element + 4-element AND competence set (provider-design + deployer-assignment twin-trigger)

```yaml
- req_id: 8.2.5
  volere_section: 15
  volere_subtype: immunity

  title: "High-risk AI system human overseers enabled with the 5 cumulative oversight abilities (provider) and assigned with competence, training, authority, and support (deployer)"

  derives_from:
    hso_sub_so: SO-8.2.AIACT
    per_reg_so: SO-AIACT-008 + SO-AIACT-011
    source_sr: SR-AIACT-013 + SR-AIACT-020
    hso_file: ../../HierarchicalSecurityObjectives/D-08_Human-Factors/8.2.md
    objective_ref_section: "### 8.2.5"

  description: |
    The product shall, on the provider-side, be designed and developed in such a way, including with appropriate human-machine interface tools, that the high-risk AI system can be effectively overseen by natural persons during the period in which it is in use (Art. 14(1) AI Act), with the natural persons assigned to human oversight enabled, as appropriate and proportionate, to discharge five cumulative oversight abilities (Art. 14(4)(a)–(e): properly understand; remain aware of automation bias; correctly interpret; decide not to use / disregard / override / reverse; intervene on the operation or interrupt the system); and on the deployer-side, deployers shall assign human oversight to natural persons who have the necessary competence, training and authority, as well as the necessary support (Art. 26(2) AI Act — 4-element AND `competence, training AND authority AND support`).

  fit_criterion: |
    For an AI-Act-scope high-risk AI system, the provider-side Art. 14(4) 5-element closed-list AND-coordinated design obligation is operationalised in NIST CSF 2.0 through PR.AT-02 (Workforce understands role-specific responsibilities — covers sub-points (a) `properly understand` and (c) `correctly interpret`) + PR.AT-01 (User awareness and training — covers sub-points (b) `remain aware of automation bias`, (d) `decide`, (e) `intervene`) + GV.RR-02 (RACI substrate — overseers must hold formal authority to override and interrupt the system per sub-points (d) and (e)) — the 5-element list is AND-coordinated and all five abilities must be enabled cumulatively (partial compliance is non-compliance per SR-AIACT-013 ambiguity_notes); the design-by-design substrate includes the human-machine interface tools that enable the oversight-abilities under Art. 14(1); on the deployer-side Art. 26(2) 4-element AND, the deployer maintains a personnel file per overseer documenting each of the four elements (competence, training, authority, support) per SR-AIACT-020 ambiguity_notes, with GV.RR-02 (Roles, responsibilities, authorities, accountabilities established, communicated, understood, enforced — the four-way AND that the deployer must evidence for each overseer) + GV.RR-04 (Cybersecurity in HR practices — screening, onboarding, training, awareness, offboarding operationalises the `necessary support` element) + PR.AT-02 (the deployer's personnel-qualification anchor — competence, training) + supplementary PR.AT-01 + PR.AT-02 + GV.RR-01; the provider-design + deployer-assignment twin-trigger is the AI-Act-specific competence architecture (provider-side Art. 14 design-by-design substrate + deployer-side Art. 26(2) assignment-on-deployment substrate); for an AI Act deployer-controller with the same natural person as both data-processing staff and AI human overseer, the AI Act Art. 14(4) + Art. 26(2) layer is the additional competence dimension on top of the GDPR Art. 39(1)(b) DPO-catalysed role-specific training (Conditional Y per CRDA-deep §8.2 GDPR↔AI_Act verified DIFFERENT-PERSPECTIVE pair on the same-natural-person operator); for NSIEs deploying high-risk AI and assigning human oversight, the NIS 2 Art. 20(2) sentence 2 employee risk-identification training stacks with the AI Act Art. 14(4) + Art. 26(2) human-overseer 5-element + 4-element AND competence (per CRDA-deep §8.2 NIS2↔AI_Act verified relationship — NIS 2 risk-identification baseline + AI Act 5-element + 4-element AND stack); for DORA financial entities deploying high-risk AI, the DORA Art. 13(6) `commensurate to the remit` programme is the carrier and the AI Act Art. 14(4) + Art. 26(2) human-overseer 5-element + 4-element AND competence is a sub-component (per CRDA-deep §8.2 DORA↔AI_Act verified relationship); for a CRA-regulated manufacturer that is also an AI Act provider, the CRA Annex II §8(f) integrator-facing information is independent of the AI Act Art. 14(4) + Art. 26(2) human-overseer competence (substantively scope-disjoint audiences — B2B integrator vs AI-overseer role within deployer organization — per CRDA-deep §8.2 CRA↔AI_Act Executor-recommended SCOPE-DISJOINT pair); verified by 5-element + 4-element AND personnel-file inspection per overseer + provider QMS design-control documentation (Art. 17(1) QMS documented in `systematic and orderly manner`) + Annex IV technical-documentation review + post-market monitoring Art. 72 + provider / deployer / MSA / AI Office inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [8.2.1 (Conditional Y on AI Act deployer-controller with same natural person as both data-processing staff and AI human overseer — AI Act layer is the additional competence dimension on top of GDPR role-specific), 8.2.2 (when NSIE deploys high-risk AI and assigns human oversight — NIS 2 risk-identification baseline + AI Act 5-element + 4-element AND stack), 8.2.4 (when DORA FE deploys high-risk AI — DORA `commensurate to the remit` carrier + AI Act 5-element sub-component)]

  nist_csf: [PR.AT-02, PR.AT-01, GV.RR-02, GV.RR-04, GV.RR-01]

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

**AI_Act article (verbatim, Art. 14(4)(a)–(e) + Art. 26(2)):**
> "Natural persons to whom human oversight is assigned shall be enabled, as appropriate and proportionate, to: (a) properly understand the relevant capacities and limitations of the high-risk AI system and foreseeable misuse; (b) remain aware of automation bias; (c) correctly interpret the output; (d) decide not to use the high-risk AI system or to disregard, override or reverse its output; (e) intervene on the operation or interrupt the system through a stop button or similar procedure." — Art. 14(4)(a)–(e) AI Act (per SR-AIACT-013)
> "Deployers shall assign human oversight to natural persons who have the necessary competence, training and authority, as well as the necessary support." — Art. 26(2) AI Act (per SR-AIACT-020)

**AI_Act article (verbatim, Art. 14(4)(a)–(e) + Art. 26(2)):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/AI_Act.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-08.2: GDPR↔AI_Act = DIFFERENT-PERSPECTIVE (SAME — Conditional Y on same natural person as both data-processing staff and AI human overseer); NIS2↔AI_Act = COMPLEMENTARY (SAME — NIS 2 risk-identification baseline + AI Act 5-element competence on NSIE deploying high-risk AI); DORA↔AI_Act = COMPLEMENTARY (SAME — DORA `commensurate to the remit` carrier + AI Act 5-element sub-component on DORA financial entity deploying high-risk AI); CRA↔AI_Act = SCOPE-DISJOINT (recommended — integrator-B2B vs AI-overseer role within deployer organization; different objects))
```

### from regs/AI_Act.md body

- For an integrated GDPR-controller deployer with the same natural person as both data-processing staff and AI human overseer, the AI Act Art. 14(4) + Art. 26(2) layer is the additional competence dimension on top of the GDPR role-specific training (Conditional Y per CRDA-deep §D-08.2 GDPR↔AI_Act verified relationship).

### from regs/AI_Act.md body

- For NSIEs deploying high-risk AI and assigning human oversight, the NIS 2 Art. 20(2) sentence 2 employee risk-identification training stacks with the AI Act Art. 14(4) + Art. 26(2) human-overseer 5-element + 4-element AND competence (per CRDA-deep §D-08.2 NIS2↔AI_Act verified relationship).

### from regs/AI_Act.md body

- For DORA financial entities deploying high-risk AI, the DORA Art. 13(6) `commensurate to the remit` programme is the carrier and the AI Act Art. 14(4) + Art. 26(2) human-overseer 5-element + 4-element AND competence is the sub-component (per CRDA-deep §D-08.2 DORA↔AI_Act verified relationship).

### from regs/AI_Act.md body

- For a CRA-regulated manufacturer that is also an AI Act provider, the CRA Annex II §8(f) integrator-facing information is independent of the AI Act Art. 14(4) + Art. 26(2) human-overseer competence (substantively scope-disjoint audiences — B2B integrator vs AI-overseer role within deployer organization — per CRDA-deep §D-08.2 CRA↔AI_Act Executor-recommended SCOPE-DISJOINT classification — no consolidation rule applies).


### from regs/AI_Act.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # AI_Act↔GDPR = Y (Cond on same natural person as both data-processing staff and AI human overseer); AI_Act↔NIS2 = Y (NSIE deploys high-risk AI and assigns human oversight); AI_Act↔DORA = Y (DORA FE deploys high-risk AI; DORA carrier + AI Act 5-element sub-component); AI_Act↔CRA = N substantively scope-disjoint (AI-overseer role within deployer organization vs B2B integrator); HL engages on overlap

```

### from regs/AI_Act.md body — field `considerations`

```yaml
  considerations: |
    The AI Act role-specific competence obligation is the **provider-design-by-design + deployer-assignment-on-deployment twin-trigger human-overseer competence architecture** — Art. 14(1) `High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use` (provider design), Art. 14(4) 5-element closed-list AND `as appropriate and proportionate` `(a) to properly understand the relevant capacities and limitations of the high-risk AI system and foreseeable misuse scenarios; (b) to remain aware of automation bias; (c) to correctly interpret the output; (d) to decide not to use the high-risk AI system or to disregard, override or reverse its output; (e) to intervene on the operation or interrupt the system through a stop button or similar procedure` (provider design-by-design) + Art. 26(2) `Deployers shall assign human oversight to natural persons who have the necessary competence, training and authority, as well as the necessary support` (deployer assignment — 4-element AND `competence, training AND authority AND support`). The 5-element closed list is AND-coordinated (all five must be enabled cumulatively — partial compliance is non-compliance per SR-AIACT-013 ambiguity_notes). The `as appropriate and proportionate` soft hedge is Berry-classic; the chosen reading is that the technical term `automation bias` carries its established human-factors meaning, which encompasses both the cognitive tendency to defer to automated outputs and the related tendency to under-detect automation errors (per SR-AIACT-013 ambiguity_notes). The Art. 26(2) deployer-side 4-element AND is COORD-2 (4-element AND — `competence, training AND authority AND support` — all four required per SR-AIACT-020 ambiguity_notes). The provider-design-by-design + deployer-assignment-on-deployment twin-trigger is the AI-Act-specific competence architecture (provider-side Art. 14 design + deployer-side Art. 26(2) assignment). PR.AT-02 anchors the role-understanding dimension that sub-points (a) `properly understand` and (c) `correctly interpret` require. PR.AT-01 anchors the awareness-and-training substrate that sub-point (b) `remain aware of automation bias` and sub-points (d) `decide` and (e) `intervene` require, ensuring overseers detect and respond to AI-specific failure modes including the cognitive-bias correction that `automation bias` operationalises. GV.RR-02 supplies the RACI substrate — overseers must hold formal authority to override and interrupt the system per sub-points (d) and (e). GV.RR-04 binds the overseer assignment to the deployer's HR practices (screening, onboarding, training, awareness, offboarding) so the `necessary support` element is operationalised across the employment lifecycle. For an integrated GDPR-controller deployer with the same natural person as both data-processing staff and AI human overseer, the AI Act Art. 14(4) + Art. 26(2) layer is the additional competence dimension on top of the GDPR role-specific training (Conditional Y per CRDA-deep §8.2 GDPR↔AI_Act verified relationship). For NSIEs deploying high-risk AI and assigning human oversight, the NIS 2 Art. 20(2) sentence 2 employee risk-identification training stacks with the AI Act Art. 14(4) + Art. 26(2) human-overseer 5-element + 4-element AND competence (per CRDA-deep §8.2 NIS2↔AI_Act verified relationship). For DORA financial entities deploying high-risk AI, the DORA Art. 13(6) `commensurate to the remit` programme is the carrier and the AI Act Art. 14(4) + Art. 26(2) human-overseer 5-element + 4-element AND competence is a sub-component (per CRDA-deep §8.2 DORA↔AI_Act verified relationship). For a CRA-regulated manufacturer that is also an AI Act provider, the CRA Annex II §8(f) integrator-facing information is independent of the AI Act Art. 14(4) + Art. 26(2) human-overseer competence (substantively scope-disjoint audiences — B2B integrator vs AI-overseer role within deployer organization — per CRDA-deep §8.2 CRA↔AI_Act Executor-recommended SCOPE-DISJOINT pair). The recipient is the provider (QMS design-control documented Art. 17(1) QMS documented in `systematic and orderly manner`) + deployer (assignment documented) + market surveillance authority (MSA) (Annex IV technical documentation) + AI Office (for GPAI on systemic-risk tracking). (Copied from the HSO Considerations block of `### 8.2.5`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=AI_Act; demoted=7; core_cross_mentions=2 -->