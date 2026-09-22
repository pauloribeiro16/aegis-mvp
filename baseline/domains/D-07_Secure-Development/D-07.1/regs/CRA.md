# D-07.1 — CRA module

> Regulation-specific layer: applies when `CRA` is in scope
> (activation: `if CRA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| CRA | SO-CRA-045 | A product with digital elements is designed, developed, and produced in accordance with the essential cybersecurity requirements set out in Annex I Part I, with the cybersecurity risk assessment propagated across the planning, design, development, production, delivery, and maintenance phases (Art. 13(1)+(2)). | Product-level by-design; essential-requirement conformance with health-and-safety of users as a cross-cutting objective; risk-assessment propagation across 6 lifecycle phases per Art. 13(2); Annex VII §3 risk-assessment record. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **CRA** | product cybersecurity via Annex I Part I essential requirements | manufacturer places product on market (Art. 13(1)) + planning/design/development/production/delivery/maintenance phases (6 lifecycle phases per Art. 13(2) chapeau) + ongoing during support period per Art. 13(8) | `essential cybersecurity requirements set out in Part I of Annex I` (Art. 13(1)) + risk-assessment propagation across 6 phases (Art. 13(2)) + support period ≥ 5 years (Art. 13(8) sentence 3) + 10-year Annex II information accessibility (Art. 13(18)); no quantitative threshold | market surveillance authority (MSA) — Annex VII §3 risk-assessment record + Annex VII §2 design/development documentation + Annex I Part I (2) sub-point evidence | Art. 13(1) + Art. 13(2) chapeau + sentence 1 + sentence 2 + Art. 13(3) sentence 1 + Art. 13(7) + Art. 13(8) + Art. 13(18) + Annex I Part I chapeau + Annex VII §2 + Annex VII §3 |

## Sub-SO (CRA)

#### D-07.1.3 — Sub-SO for CRA

```yaml
id: SO-D-07.1.CRA
subdomain: D-07.1
applies_to: [CRA]
inherits_from: SO-CRA-045
source_SR: SR-CRA-064
activation: if CRA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** When placing a product with digital elements on the market, the manufacturer ensures that it has been designed, developed and produced in accordance with the essential cybersecurity requirements set out in Part I of Annex I (Art. 13(1) CRA), with the cybersecurity risk assessment propagated across the 6 lifecycle phases (planning, design, development, production, delivery, maintenance) per Art. 13(2) chapeau + sentence 1, with a view to minimising cybersecurity risks, preventing incidents, and minimising their impact (Art. 13(2) sentence 2).

**Considerations.**
- The Annex I Part I chapeau establishes the cybersecurity-by-design baseline across 11 sub-points (a)–(k) including attack-surface limitation (2)(j) + exploitation mitigation (2)(k) + automatic security updates (2)(c) + integrity protection (2)(f) + data-minimisation (2)(g) + resilience+availability (2)(h) + cascading-impact minimisation (2)(i) + recording-and-monitoring (2)(l).
- The risk-assessment propagation across 6 phases is a continuous obligation, not a one-shot pre-launch activity — risk assessment is documented (Art. 13(3) sentence 1) and updated when there is a change of risk represented by the product.
- Annex VII §3 risk-assessment record + Annex VII §2 design/development documentation form the technical-documentation evidence base (cross to D-09.4).
- Support period ≥ 5 years (Art. 13(8) sentence 3); 10-year Annex II information accessibility (Art. 13(18)).
**CSF anchors (from `SR-CRA-064` v0.3 security_rationale):**
PR.PS-06, GV.PO-02.
*(PR.PS-06 anchors the secure-software-development lifecycle dimension — secure software development practices are integrated, and their performance is monitored throughout the SDLC; the CRA Art. 13(2) 6-phase coordinated risk-assessment-propagation architecture maps to PR.PS-06 directly. PR.PS-01 anchors the configuration-management dimension — configuration management practices are established, documented, and applied; the CRA Annex I Part I (2) sub-points (a)–(k) including attack-surface limitation (j) + exploitation mitigation (k) + automatic security updates (c) + integrity protection (f) + recording-and-monitoring (l) + secure-by-default (b) form the configuration-management baseline of the product by-design. The two subcategories together enable the manufacturer to demonstrate ex post, through the documented Annex VII §3 risk-assessment record + Annex VII §2 design/development documentation + Annex I Part I (2) sub-point evidence + Art. 13(3) sentence 1 update-on-change-of-risk record + Art. 13(7) documentation record, that the Art. 13(1)+(2) by-design + 6-phase-risk-assessment-propagation duty has been exercised with the Annex I Part I essential-requirements anchor.)*

---


## Security Requirements (CRA)

#### 7.1.3 — Product cybersecurity via Annex I Part I across 6 lifecycle phases

```yaml
- req_id: 7.1.3
  volere_section: 15
  volere_subtype: integrity

  title: "Product with digital elements designed, developed and produced in accordance with Annex I Part I essential cybersecurity requirements with risk assessment propagated across planning, design, development, production, delivery and maintenance"

  derives_from:
    hso_sub_so: SO-D-07.1.CRA
    per_reg_so: SO-CRA-045
    source_sr: SR-CRA-064, SR-CRA-066
    hso_file: ../../HierarchicalSecurityObjectives/D-07_Secure-Development/D-07.1.md
    objective_ref_section: "### D-07.1.3"

  description: |
    The product shall be designed, developed and produced in accordance with the essential cybersecurity requirements set out in Annex I Part I, with the cybersecurity risk assessment taken into account across the planning, design, development, production, delivery and maintenance phases of the product, with a view to minimising cybersecurity risks, preventing incidents, and minimising their impact including in relation to the health and safety of users (CRA Art. 13(1) + Art. 13(2) chapeau + sentence 1 + sentence 2 + Annex I Part I chapeau + Annex VII §2 + Annex VII §3).

  fit_criterion: |
    The product by-design discipline conforms to Annex I Part I essential cybersecurity requirements across the 11 sub-points (a)–(k) including attack-surface limitation (2)(j) + exploitation mitigation (2)(k) + automatic security updates (2)(c) + integrity protection (2)(f) + data-minimisation (2)(g) + resilience+availability (2)(h) + cascading-impact minimisation (2)(i) + recording-and-monitoring (2)(l); a documented cybersecurity risk assessment per Art. 13(2) is propagated across the 6 lifecycle phases (planning / design / development / production / delivery / maintenance) with the assessment comprising at least the analysis of risks based on intended purpose and reasonably foreseeable use (including operational environment, assets to be protected, expected lifetime) per Art. 13(3) sentence 2, indicating whether and in what manner the Annex I Part I (2) requirements apply and how they are implemented per Art. 13(3) sentence 3; the risk assessment is documented in the Annex VII §3 technical documentation and updated when there is a change of risk represented by the product per Art. 13(3) sentence 1; Annex VII §2 design/development documentation forms the technical-documentation evidence base; the support period is determined in accordance with Art. 13(8) with ≥ 5 years expected per sentence 3; Annex II information accessibility is maintained for 10 years per Art. 13(18); for an integrated manufacturer-controller-deployer, the CRA-side Annex I Part I product by-design discharges the engineering substrate while GDPR Art. 25(1) controller-side by-design discharges the personal-data overlay; for an AI-enabled CRA product, CRA Art. 13(4) sentence 2 explicit AI-Act-substitution for risk assessment permits a unified risk assessment under AI Act Art. 9 to substitute for the CRA risk assessment when both apply (per SR-CRA-066); verified by Annex I Part I (2) sub-point evidence per product class + Annex VII §2 design/development documentation review + Annex VII §3 risk-assessment record audit + 6-phase risk-assessment-propagation records inspection + Art. 13(3) sentence 1 update-on-change-of-risk record + Art. 13(8) support-period record + Art. 13(18) 10-year information-accessibility record + MSA / ENISA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [7.1.1 (when integrated manufacturer-controller — CRA Annex I Part I engineering substrate + GDPR Art. 25(1) personal-data overlay), 7.1.2 (when NIS 2 entity deploys / manufactures CRA product — supplier-customer boundary; NIS 2 supplier-assessment references CRA Annex VII technical documentation), 7.1.4 (when DORA FE deploys CRA product — DORA design-procurement baseline satisfied by CRA-conformant-product selection; CRA Annex VII §3 risk-assessment record feeds DORA Art. 6(1) ICT risk-management framework), 7.1.5 (when AI-enabled CRA product — CRA Art. 13(4) sentence 2 explicit AI-Act-substitution for risk assessment unifies Art. 9 + Art. 13 risk-assessment documentation)]

  nist_csf: [PR.PS-06, PR.PS-01]

  applicable_if:
    regs: [CRA]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (CRA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**CRA article (verbatim, Art. 13(1) + Art. 13(2)):**
> "When placing a product with digital elements on the market, manufacturers shall ensure that it has been designed, developed and produced in accordance with the essential cybersecurity requirements set out in Part I of Annex I." — Art. 13(1) CRA
> "The manufacturer shall undertake an assessment of the cybersecurity risks associated with a product with digital elements … and take the outcome of that assessment into account during the planning, design, development, production, delivery and maintenance phases of the product with digital elements …" — Art. 13(2) CRA


**CRA article (verbatim, Art. 13(1) + Art. 13(4) sentence 2):**
> [as quoted above, plus]
> "The cybersecurity risk assessment referred to in paragraph 2 shall be part of, or combined with, the risk assessment required by other Union legal acts applicable to the product with digital elements." — Art. 13(4) sentence 2 CRA

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/CRA.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-07.1: GDPR↔CRA = COMPLEMENTARY (SAME — controller-side data-protection by-design overlay on manufacturer-side product by-design); NIS2↔CRA = COMPLEMENTARY (SAME — entity-side NIS-lifecycle security stacks with maker-side product by-design at supplier-customer boundary); CRA↔DORA = COMPLEMENTARY (SAME — DORA-entity-side infrastructure management operationalised via upstream CRA-conformant-product procurement); CRA↔AI_Act = COMPLEMENTARY (SAME — CRA Art. 13(4) sentence 2 explicit AI-Act-substitution for risk assessment on AI-enabled-CRA-product))
```

### from regs/CRA.md body

- For an integrated manufacturer-controller-deployer, CRA-side Annex I Part I product-cybersecurity by-design discharges the engineering substrate; GDPR Art. 25(1) data-protection by-design discharges the personal-data overlay; the two stack vertically on the same product-lifecycle.

### from regs/CRA.md body

- For an AI-enabled CRA product, CRA Art. 13(4) sentence 2 explicit AI-Act-substitution for risk assessment permits a unified risk assessment under AI Act Art. 9 to substitute for the CRA risk assessment when both apply (SR-CRA-066) — the by-design risk-assessment obligation is satisfied by the AI Act Art. 9 + Art. 17 risk-management-system documentation that covers both regimes' risk-assessment content.

### from regs/CRA.md body

- For a CRA manufacturer that is also a DORA financial entity, CRA-side Annex VII §3 risk-assessment record feeds the DORA-side Art. 6(1) ICT risk-management framework + Art. 9(4)(e) change-management six-step + Art. 24 testing programme — the upstream CRA-side by-design discipline documents the product cybersecurity for procurement by the downstream DORA-side deployer.


### from regs/CRA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # CRA↔GDPR = Y (integrated manufacturer-controller-deployer); CRA↔NIS2 = Y (NIS 2 entity deploys / manufactures CRA product); CRA↔DORA = Y (DORA FE deploys CRA product — CRA-conformant-product selection discharges DORA design-procurement baseline); CRA↔AI_Act = Conditional Y (AI-enabled CRA product — CRA Art. 13(4) sentence 2 explicit AI-Act-substitution carve-out for risk assessment); HL engages on overlap

```

### from regs/CRA.md body — field `considerations`

```yaml
  considerations: |
    The CRA secure-by-design obligation is the product-level by-design with risk-assessment propagation across 6 lifecycle phases per Annex I Part I; the operational substrate is the Annex VII §2 design/development documentation + Annex VII §3 risk-assessment record + Annex I Part I (2) sub-point evidence + Art. 13(3) sentence 1 update-on-change-of-risk record + Art. 13(7) documentation record + Art. 13(8) support-period record (≥ 5 years) + Art. 13(18) 10-year Annex II information-accessibility record. The Annex I Part I (2) sub-points (a)–(k) form the configuration-management baseline of the product by-design (mapped to PR.PS-01). The 6-phase CRA lifecycle is not 1:1 aligned with the 3-phase NIS 2 lifecycle — the two regimes stack at the supplier-customer boundary. CRA Art. 13(4) sentence 2 explicit AI-Act-substitution carve-out for risk assessment permits a unified risk assessment under AI Act Art. 9 on AI-enabled CRA products. (Copied from the HSO Considerations block of `### D-07.1.3`; preserved here for self-contained traceability.)
```

### from regs/CRA.md body

**CRA article (verbatim, Art. 13(1)):**

> [as quoted in GDPR ↔ CRA above]

<!-- aegis:purity: own_reg=CRA; demoted=7; core_cross_mentions=2 -->
