# D-09.2 — DORA module

> Regulation-specific layer: applies when `DORA` is in scope
> (activation: `if DORA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| DORA | SO-DORA-017 + SO-DORA-003 | Three-lines-of-defence model + ICT supported business functions / information assets / ICT assets identification, classification, documentation (Art. 6(4) + Art. 7(1) — cross to D-09.3); ICT risk identification register on a continuous basis with at-least-yearly risk-scenario review (Art. 7(2) sentence 1 + sentence 2). | Financial-entity operational ICT risk framework; continuous + yearly review; no pre-launch DPIA-equivalent. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **DORA** | financial-entity ICT operational risk (ICT-supported business functions dimension) — continuous + at-least-yearly review | financial-entity establishment / on-going operational | ICT risk identification register (sources of ICT risk, exposure to/from other financial entities, cyber threats, ICT vulnerabilities relevant to ICT supported business functions / information assets / ICT assets per Art. 7(2) sentence 1) + risk-scenario register (reviewed at-least-yearly per Art. 7(2) sentence 2) | continuous + at-least-yearly per Art. 7(2) sentence 1 + sentence 2 `review on a regular basis, and at least yearly, the risk scenarios impacting them` | competent authority (NCA — national financial supervisory authority) — Art. 7(2) sentence 1 continuous ICT risk identification register + sentence 2 at-least-yearly risk-scenario review + Art. 6(4) three-lines-of-defence documentation + EBA Guidelines on ICT and security risk management supervisory baseline | Art. 6(4) `three lines of defence model` (or internal risk management and control model) + Art. 7(1) `identify, classify and adequately document` ICT supported business functions + information assets + ICT assets + Art. 7(2) sentence 1 `continuously … identify all sources of ICT risk` + sentence 2 `review on a regular basis, and at least yearly, the risk scenarios impacting them` + EBA Guidelines on ICT and security risk management supervisory baseline |

## Sub-SO (DORA)

#### D-09.2.4 — Sub-SO for DORA

```yaml
id: SO-D-09.2.DORA
subdomain: D-09.2
applies_to: [DORA]
inherits_from: SO-DORA-017 + SO-DORA-003
source_SR: SR-DORA-028 + SR-DORA-004 + SR-DORA-005
activation: if DORA in applicable_regs
phase_1A_role: 1_of_5
```

**Objective.** Financial entities shall, on a continuous basis, **identify all sources of ICT risk** including risk exposure to and from other financial entities, and **assess cyber threats and ICT vulnerabilities relevant to ICT supported business functions, information assets and ICT assets** (Art. 7(2) sentence 1 DORA); risk scenarios are reviewed on a regular basis, and at least yearly (Art. 7(2) sentence 2), under a three-lines-of-defence model (Art. 6(4) DORA).

**CSF anchors (from `SR-DORA-028` + `SR-DORA-004` + `SR-DORA-005` v0.3 security_rationale):**
GV.RR-02, GV.RM-02, ID.RA-01, ID.RA-03, ID.RA-05, ID.IM-04, GV.OV-02, PR.PS-02.

---


## Security Requirements (DORA)

#### 9.2.4 — Financial-entity continuous ICT risk identification register + at-least-yearly risk-scenario review under three-lines-of-defence

```yaml
- req_id: 9.2.4
  volere_section: 15
  volere_subtype: integrity

  title: "Financial entity continuously identifies ICT risks and reviews risk scenarios at least yearly under the three-lines-of-defence model with classification and documentation per Art. 7(1)-(2)"

  derives_from:
    hso_sub_so: SO-9.2.DORA
    per_reg_so: SO-DORA-017 + SO-DORA-003
    source_sr: SR-DORA-028 + SR-DORA-004 + SR-DORA-005
    hso_file: ../../HierarchicalSecurityObjectives/D-09_Governance-Documentation/9.2.md
    objective_ref_section: "### 9.2.4"

  description: |
    The product shall ensure that the financial entity, on a continuous basis, identifies all sources of ICT risk and assesses cyber threats and ICT vulnerabilities relevant to its ICT supported business functions, information assets, and ICT assets (per DORA Art. 7(2) sentence 1), with risk scenarios reviewed on a regular basis and at least yearly (per Art. 7(2) sentence 2), under a three-lines-of-defence model (per Art. 6(4)) and with identification / classification / documentation per Art. 7(1).

  fit_criterion: |
    The financial entity's ICT risk identification register is maintained on a continuous basis under Art. 7(2) sentence 1 `continuously … identify all sources of ICT risk … including the risk exposure to and from other financial entities, and assess cyber threats and ICT vulnerabilities relevant to ICT supported business functions, information assets and ICT assets` (SR-DORA-028) with ID.RA-05 threats-vulnerabilities-likelihoods-impacts dimension (the register identifies ICT risk sources + exposure to/from other financial entities + cyber threats + ICT vulnerabilities, mapped to the ICT supported business functions / information assets / ICT assets identified and classified per Art. 7(1) `identify, classify and adequately document all ICT supported business functions … the information assets and ICT assets` cross-ref 9.3) + GV.RR-02 management-body approve/oversee dimension (the register is management-body-overseen per Art. 5(2) four-verb coordination `define, approve, oversee and be responsible for`); the register is operated under the **three-lines-of-defence model** per Art. 6(4) (operational-management as first line, risk-management and compliance as second line, internal-audit as third line) with responsibility for managing and overseeing ICT risk assigned to a control function with appropriate level of independence; the risk-scenario review is conducted on a regular basis and at least yearly per Art. 7(2) sentence 2 `review on a regular basis, and at least yearly, the risk scenarios impacting them`, with the depth calibrated to Art. 4 proportionality `in relation to the size, nature, scale and complexity of the financial entity's activities`; the register and review records are retained per EBA Guidelines on ICT and security risk management supervisory baseline; the register coordinates with Art. 7(1) ICT asset inventory (cross to 9.3 DORA sub-SO) and the Art. 6(1) ICT risk-management framework (cross to 9.1 DORA sub-SO); for financial entities under DORA's direct scope, the **continuous + at-least-yearly ICT risk framework** discharges both DORA's dedicated risk-identification obligation and NIS 2's Art. 21(2)(a) continuous operational risk-analysis policy on the DORA-dominant stack — EQUAL classification (per CRDA flag DomainAnalysis §9.2 line 110-114); the management body's Art. 5(4) `actively keep up to date` training obligation (cross-ref 8.3.2) is the literacy prerequisite for the Art. 5(2) define/approve/oversee/be-responsible architecture; **DORA ICT risk framework does NOT extend to data-subject rights** (per CRDA flag DomainAnalysis §9.2 line 175): the GDPR DPIA on data-subject rights must be a separate artefact even when the DORA ICT risk framework is in place; **DORA has no equivalent to CRA Art. 13(4) sentence 2** — the DORA ↔ AI_Act pair has no OJ-level consolidation rule.

  priority: MUST
  verification_method: TEST
  dependencies: [8.3.2 (Art. 5(4) management-body training as literacy prerequisite for Art. 5(2) define/approve/oversee/be-responsible), 9.2.2 (when DORA-NSIE — DORA continuous + yearly discharges both; EQUAL, DORA-dominant stack for financial entities), 9.2.1 (when DORA-controller — DPIA pre-launch + DORA continuous + yearly; DIFFERENT-PERSPECTIVE, distinct artefacts, **no OJ-level consolidation rule**), 9.2.3 (when DORA entity procures CRA-conformant — DORA entity-level operational + CRA product-level pre-market; COMPLEMENTARY, Conditional-Y scope overlap), 9.2.5 (when DORA FE deploys high-risk AI — DORA entity-level operational + AI Act AI-system-level continuous iterative; COMPLEMENTARY, **no OJ-level consolidation rule**)]

  nist_csf: [GV.RR-02, GV.RM-02]

  applicable_if:
    regs: [DORA]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (DORA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**DORA article (verbatim, Art. 6(4) + Art. 7(2)):**
> "Financial entities shall assign the responsibility for managing and overseeing ICT risk to a control function and ensure an appropriate level of independence … in accordance with the three lines of defence model, or an internal risk management and control model." — Art. 6(4) DORA (per SR-DORA-028)
> "Financial entities shall, on a continuous basis, identify all sources of ICT risk, in particular the risk exposure to and from other financial entities, and assess cyber threats and ICT vulnerabilities relevant to their ICT supported business functions, information assets and ICT assets." — Art. 7(2) sentence 1 DORA (per SR-DORA-004; the OJ-literal locus is Art. 8(2) per the v0.2 audit note)
> "Financial entities shall review on a regular basis, and at least yearly, the risk scenarios impacting them." — Art. 7(2) sentence 2 DORA (per SR-DORA-005; the OJ-literal locus is Art. 8(2) per the v0.2 audit note)

**DORA article (verbatim, Art. 6(4) + Art. 7(2)):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/DORA.md body — field `verified_relationship`

```yaml
verified_relationship: DIFFERENT-PERSPECTIVE / COMPLEMENTARY / EQUAL (CRDA-deep, D-09.2: GDPR↔DORA = DIFFERENT-PERSPECTIVE (SAME — pre-launch DPIA vs continuous + at-least-yearly DORA risk framework; **no OJ-level consolidation**); NIS2↔DORA = EQUAL (SAME — both regulations impose continuous operational risk-identification obligations; DORA-dominant for financial entities under DORA's direct scope; EQUAL on continuous operational risk identification); CRA↔DORA = COMPLEMENTARY (SAME — CRA product-level pre-market + DORA entity-level operational; Conditional-Y scope overlap when DORA entity procures CRA-conformant); DORA↔AI_Act = COMPLEMENTARY (SAME — DORA entity-level operational + AI Act AI-system-level continuous iterative; **no OJ-level consolidation** — DORA has no equivalent to CRA Art. 13(4) sentence 2))
```

### from regs/DORA.md body

*(ID.RA-05 — Threats, vulnerabilities, likelihoods, impacts used to understand inherent risk and inform risk response — anchors the DORA Art. 7(2) sentence 1 continuous ICT risk identification + sentence 2 at-least-yearly risk-scenario review mapped to NIST CSF 2.0 ID.RA-05. The three-lines-of-defence model (Art. 6(4)) provides the governance architecture for the ICT risk identification + asset classification + risk-scenario review chain. The two subcategories together enable the financial entity to demonstrate ex post, against the national competent authority + EBA Guidelines on ICT and security risk management supervisory baseline, that the Art. 7(2) sentence 1 continuous ICT risk identification register + sentence 2 at-least-yearly risk-scenario review records + Art. 6(4) three-lines-of-defence documentation + Art. 7(1) asset identification/classification/documentation chain are maintained on the entity-level operational continuous + at-least-yearly cadence per Art. 4 proportionality. **Note — DORA ICT risk framework does NOT extend to data-subject rights**: per CRDA flag (DomainAnalysis §D-09.2 line 175), the GDPR DPIA on data-subject rights must be a separate artefact even when the DORA ICT risk framework is in place; **DORA has no equivalent to CRA Art. 13(4) sentence 2** — DORA ↔ AI Act pair has no OJ-level consolidation rule. **Note — DORA OJ-literal locus**: the OJ-literal locus for Art. 7(2) sentence 1 + sentence 2 is Art. 8(2) per the SR-DORA-004 / SR-DORA-005 v0.2 audit note; the SR preserves the substantive content of the risk-identification-on-a-continuous-basis + at-least-yearly risk-scenario review obligation.)*

### from regs/DORA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # DORA↔NIS2 = Y (DORA financial entity is NSIE; EQUAL on continuous operational risk identification; DORA-dominant stack for financial entities); DORA↔GDPR = Y (DORA financial entity is controller; **no OJ-level consolidation rule** — DPIA pre-launch vs DORA continuous + yearly; distinct artefacts); DORA↔CRA = Conditional (Y when DORA entity procures CRA-conformant; CRA product-level + DORA entity-level operational); DORA↔AI_Act = Y (DORA FE deploys high-risk AI; **no OJ-level consolidation rule** — DORA has no equivalent to CRA Art. 13(4) sentence 2); HL engages on overlap

```

### from regs/DORA.md body — field `considerations`

```yaml
  considerations: |
    The DORA impact-and-risk-assessment obligation at 9.2 is the **continuous + at-least-yearly ICT risk identification + risk-scenario review** under Art. 6(4) three-lines-of-defence + Art. 7(2) sentence 1 + sentence 2. The risk object is **financial-entity ICT operational risk** (sources of ICT risk + exposure to/from other financial entities + cyber threats + ICT vulnerabilities relevant to ICT supported business functions + information assets + ICT assets per Art. 7(2) sentence 1 + Art. 7(1) identify/classify/adequately document chain, cross to 9.3 DORA sub-SO). Art. 7(2) sentence 1 `continuously … identify all sources of ICT risk` carries S2 VAG on `continuously` (chosen reading: ongoing operational frequency, not project-end); Art. 7(2) sentence 2 `review on a regular basis, and at least yearly, the risk scenarios` carries a 2-way `regular basis AND at least yearly` COORD — `at least yearly` is the OJ-minimum cadence with `regular basis` permitting additional reviews on material-change triggers. The EBA Guidelines on ICT and security risk management operationalise the supervisory baseline for the register + review records. The **NIS 2 ↔ DORA EQUAL pair** (per CRDA DomainAnalysis §9.2 line 110-114) discharges both continuous operational risk-identification obligations on the DORA-dominant stack for financial entities under DORA's direct scope; for non-financial NSIEs, NIS 2 is the authority. **DORA has no equivalent to CRA Art. 13(4) sentence 2** — the DORA ↔ AI_Act pair has no OJ-level consolidation rule, so a DORA financial entity deploying a CRA-conformant high-risk AI system discharges three separate assessment artefacts (DORA continuous + yearly + CRA pre-market + support-period + AI Act Art. 9 continuous iterative — with CRA Art. 13(4) sentence 2 permitting CRA + AI Act consolidation on a single artefact, leaving DORA separate). **DORA ICT risk framework does NOT extend to data-subject rights** (per CRDA flag DomainAnalysis §9.2 line 175): the GDPR DPIA on data-subject rights must be a separate artefact even when the DORA ICT risk framework is in place; the 4 SAME — DIFFERENT-PERSPECTIVE pairs (all 4 GDPR pairs) preserve this structural pre-launch DPIA vs operational-continuous asymmetry. The recipient is the **competent authority (NCA — national financial supervisory authority)** + EBA Guidelines supervisory baseline on Art. 7(2) sentence 1 continuous ICT risk identification register + sentence 2 at-least-yearly risk-scenario review + Art. 6(4) three-lines-of-defence documentation + Art. 7(1) asset chain.
```

<!-- aegis:purity: own_reg=DORA; demoted=4; core_cross_mentions=2 -->
