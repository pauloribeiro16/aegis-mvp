# D-07.1 — DORA module

> Regulation-specific layer: applies when `DORA` is in scope
> (activation: `if DORA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| DORA | SO-DORA-004 (partial) | Sound network and infrastructure management structure using appropriate techniques, methods and protocols + patch and update policies (Art. 9(4)(b)+(f)) — **secure-by-design is implicit, not an OJ-mandate standalone**; operationalised through Art. 9(4)(e) change-management six-step (SR-DORA-023). | Financial-entity operational resilience; no dedicated by-design clause in OJ; the security-in-design dimension is operationalised through change-management (Art. 9(4)(e)) and the testing programme (Art. 24); SR-DORA-004 routes Art. 9(4)(b) and Art. 9(4)(f) into D-07.1 partial coverage. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **DORA** | ICT-infrastructure management structure + change-management six-step + patch policies (financial-entity side) | establishment of ICT infrastructure (continuous per Art. 9(4)(b)) + ICT change event (Art. 9(4)(e) six-step) + patch update event (Art. 9(4)(f)) | no OJ dedicated by-design mandate; `appropriate techniques, methods and protocols` (Art. 9(4)(b) qualitative) + Art. 9(4)(e) six-step mandatory (recorded/tested/assessed/approved/implemented/verified) + Art. 4 proportionality under Recital 56; no quantitative threshold for design cadence | competent authority (national financial supervisory authority) + management body — Art. 6(1) ICT risk-management framework + Art. 9(4)(b) infrastructure record + Art. 9(4)(e) change-mgmt policy + Art. 24 testing programme | Art. 9(4)(b) + Art. 9(4)(e) + Art. 9(4)(f) + Art. 6(1) ICT risk-management framework + Art. 24 testing programme (no dedicated by-design OJ clause — partial at D-07.1) |

## Sub-SO (DORA)

#### D-07.1.4 — Sub-SO for DORA

```yaml
id: SO-D-07.1.DORA
subdomain: D-07.1
applies_to: [DORA]
inherits_from: SO-DORA-004
source_SR: SR-DORA-004
activation: if DORA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Financial entities establish a sound network and infrastructure management structure using appropriate techniques, methods and protocols (Art. 9(4)(b) DORA) with appropriate and comprehensive documented policies for patches and updates maintained (Art. 9(4)(f)).

**Considerations.**
- DORA does not impose a dedicated secure-by-design mandate as such — the security-in-design dimension for the financial-entity side is operationalised through Art. 9(4)(e) ICT change-management six-step (recorded/tested/assessed/approved/implemented/verified in a controlled manner) and Art. 24 ICT risk-management testing programme (12-way open list including vulnerability assessments, scans, source-code reviews where feasible, scenario-based tests, penetration testing, etc.).
- Art. 9(4)(b) network-and-infrastructure-management baseline + Art. 9(4)(f) patch-policies baseline are the standing instruments; change-mgmt six-step (SR-DORA-023) + testing programme (SR-DORA-005) are the by-design operationalisation instruments.
- DORA-side by-design obligations propagate downstream to D-07.2 (Secure Coding Practices) as the code-level instruction in the change-management gate, D-07.3 (CI/CD Pipeline Security) as the delivery-path instruction in the testing programme, and D-07.4 (Change Management) as the explicit change-management six-step that operationalises by-design at the entity side.
- Art. 5(2)+(4) management-body `define, approve, oversee and is responsible for the implementation of all arrangements related to the ICT risk management framework` is the upstream governance instrument for the by-design architecture on the DORA side.

**CSF anchors (from `SR-DORA-004` v0.3 security_rationale):**
ID.RA-01, ID.RA-03.

---


## Security Requirements (DORA)

#### 7.1.4 — Financial-entity infrastructure management with change-management six-step + testing programme (partial — no OJ dedicated by-design mandate)

```yaml
- req_id: 7.1.4
  volere_section: 15
  volere_subtype: integrity

  title: "Sound network and infrastructure management structure with appropriate techniques/methods/protocols, patch and update policies, and secure-by-design operationalised via change-management six-step + testing programme (DORA partial — no OJ dedicated by-design mandate)"

  derives_from:
    hso_sub_so: SO-D-07.1.DORA
    per_reg_so: SO-DORA-004 (partial)
    source_sr: SR-DORA-004, SR-DORA-023
    hso_file: ../../HierarchicalSecurityObjectives/D-07_Secure-Development/D-07.1.md
    objective_ref_section: "### D-07.1.4"

  description: |
    The product shall establish a sound network and infrastructure management structure using appropriate techniques, methods and protocols with appropriate and comprehensive documented policies for patches and updates, with the secure-by-design dimension operationalised through documented ICT change-management policies, procedures and controls for software, hardware, firmware components, systems or security parameters that are recorded, tested, assessed, approved, implemented and verified in a controlled manner, based on a risk assessment approach, supported by the Art. 24 ICT risk-management testing programme (DORA Art. 9(4)(b) + Art. 9(4)(f) + Art. 9(4)(e) + Art. 24 — partial at D-07.1; no OJ-mandated dedicated by-design clause).

  fit_criterion: |
    A documented Art. 9(4)(b) network-and-infrastructure-management structure is maintained using appropriate techniques, methods and protocols; documented Art. 9(4)(f) patch-and-update policies are maintained appropriate and comprehensive per the risk profile; the secure-by-design dimension is operationalised through the Art. 9(4)(e) ICT change-management six-step (recorded / tested / assessed / approved / implemented / verified in a controlled manner, based on a risk assessment approach) covering all change targets (software / hardware / firmware components / systems / security parameters) per SR-DORA-023; the Art. 24 ICT risk-management testing programme is operated with the 12-way open testing-modality list including vulnerability assessments, scans, source-code reviews where feasible, scenario-based tests, penetration testing, end-to-end testing, performance testing, compatibility testing, etc.; the by-design architecture integrates with Art. 6(1) ICT risk-management framework + Art. 5(2)+(4) management-body responsibility for the ICT risk-management framework; for a DORA-only entity that is not a CRA manufacturer and does not process personal data via high-risk AI, by-design compliance is demonstrated through the change-management six-step + testing programme outputs, with no standalone OJ-mandated by-design obligation; for a DORA FE that is also a CRA manufacturer, the upstream CRA-side Annex I Part I product by-design feeds the downstream DORA-side change-management six-step + testing; for a DORA FE that is also a controller processing personal data, the controller-side GDPR Art. 25(1) data-protection by-design sits on top of the DORA-side change-management six-step + testing; verified by Art. 9(4)(b) infrastructure-management structure records review + Art. 9(4)(f) patch-policy records audit + Art. 9(4)(e) change-management six-step records inspection (each ICT change shows recorded / tested / assessed / approved / implemented / verified) + Art. 24 testing-programme records review (each of the 12 modalities documented) + Art. 6(1) ICT risk-management-framework record + Art. 5(2)+(4) management-body responsibility record + national CA + ESA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [7.1.1 (when DORA FE is also controller — GDPR Art. 25(1) data-protection overlay on DORA change-mgmt), 7.1.2 (when DORA FE is also NSIE — DORA Art. 9(4)(e) change-mgmt operationalises NIS 2 maintenance phase for ICT-hazard subset; NIS 2 chapeau extends to physical + operational hazards), 7.1.3 (when DORA FE deploys / manufactures CRA product — CRA-conformant-product procurement feeds DORA design-procurement baseline), 7.1.5 (when DORA FE deploys high-risk AI — DORA change-mgmt six-step operational gate + AI Act QMS governance gate stack)]

  nist_csf: [PR.PS-06]

  applicable_if:
    regs: [DORA]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (DORA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**DORA article (verbatim, Art. 9(4)(b)):**
> "Financial entities shall … (b) establish a sound network and infrastructure management structure using appropriate techniques, methods and protocols that may include implementing automated mechanisms to isolate affected information assets in the event of cyber-attacks." — Art. 9(4)(b) DORA

**DORA article (verbatim, Art. 9(4)(e)):**
> "Financial entities shall … (e) implement documented policies, procedures and controls for ICT change management, including changes to software, hardware, firmware components, systems or security parameters … that are based on a risk assessment approach … in order to ensure that all changes to ICT systems are recorded, tested, assessed, approved, implemented and verified in a controlled manner." — Art. 9(4)(e) DORA


**DORA article (verbatim, Art. 9(4)(b)):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/DORA.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-07.1: GDPR↔DORA = COMPLEMENTARY (SAME — controller-side data-protection by-design overlay on financial-entity change-mgmt six-step + testing); NIS2↔DORA = COMPLEMENTARY (SAME — NSIE maintenance-phase operationalised through DORA change-mgmt six-step); CRA↔DORA = COMPLEMENTARY (SAME — DORA-entity-side infrastructure management operationalised via upstream CRA-conformant-product procurement); DORA↔AI_Act = COMPLEMENTARY (SAME — DORA change-mgmt operational gate + AI Act QMS governance gate))
```

### from regs/DORA.md body

- For a DORA-only entity that is not a CRA manufacturer and does not process personal data via high-risk AI, D-07.1 by-design compliance is demonstrated through the change-management six-step + testing programme outputs, with no standalone OJ-mandated by-design obligation.

### from regs/DORA.md body

- For a financial entity that is also a CRA manufacturer, upstream CRA-side Annex I Part I product by-design feeds the downstream DORA-side change-management six-step + testing programme — the by-design architecture stacks with the product-side Annex I Part I essential-requirements providing the by-design output, and the deployer-side Art. 9(4)(e) + Art. 24 providing the by-design operationalisation.

### from regs/DORA.md body

- For a financial entity that is also a controller processing personal data, controller-side GDPR Art. 25(1) data-protection by-design sits on top of the DORA-side change-mgmt six-step + testing programme — the by-design architecture stacks with the data-protection overlay on top of the financial-entity infrastructure-management baseline.

### from regs/DORA.md body

*(PR.PS-06 anchors the secure-software-development lifecycle dimension — secure software development practices are integrated, and their performance is monitored throughout the SDLC; the DORA Art. 9(4)(e) change-management six-step (recorded/tested/assessed/approved/implemented/verified) + Art. 24 testing programme (12-way open list of testing modalities including source-code reviews and penetration testing) + Art. 9(4)(b) network-and-infrastructure-management + Art. 9(4)(f) patch policies are the DORA-side by-design operational mechanisms that map to PR.PS-06. The DORA-side PR.PS-06 anchor is operationalised through the change-management + testing instruments rather than through a dedicated by-design OJ clause — this is the structural Layer 2 review item (no OJ dedicated by-design clause; SR-DORA-004 partial mapping at D-07.1). For a DORA-only entity that is not a CRA manufacturer and does not process personal data via high-risk AI, the PR.PS-06 anchor is demonstrated through the change-management six-step + testing programme outputs without an OJ-mandated dedicated by-design obligation.)*

### from regs/DORA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # DORA↔GDPR = Conditional Y (DORA-controller combined stack); DORA↔NIS2 = Y (DORA FE = NSIE; lex specialis — DORA Art. 9(4)(e) operationalises NIS 2 maintenance for ICT-hazard subset); DORA↔CRA = Y (DORA FE deploys CRA product; CRA-conformant-product procurement); DORA↔AI_Act = Y (DORA FE deploys high-risk AI); HL engages on overlap

```

### from regs/DORA.md body — field `considerations`

```yaml
  considerations: |
    The DORA secure-by-design obligation is the financial-entity-side infrastructure management + change-management + testing — **no OJ-mandated dedicated by-design clause** is present in DORA; Art. 9(4)(b) is `sound network and infrastructure management structure using appropriate techniques, methods and protocols`; Art. 9(4)(f) is `patches and updates`; the secure-by-design dimension is operationalised through Art. 9(4)(e) change-management six-step + Art. 24 testing programme — this is the structural Layer 2 review item (SR-DORA-004 partial mapping at D-07.1). For a DORA-only entity that is not a CRA manufacturer and does not process personal data via high-risk AI, by-design compliance is demonstrated through the change-management six-step + testing programme outputs, with no standalone OJ-mandated by-design obligation. The DORA-side by-design architecture integrates with Art. 6(1) ICT risk-management framework + Art. 5(2)+(4) management-body responsibility. For pure-financial entities, DORA is lex specialis over NIS 2 for the ICT-hazard subset (NIS 2 chapeau extends to physical + operational hazards). (Copied from the HSO Considerations block of `### D-07.1.4`; preserved here for self-contained traceability.)
```

### from regs/DORA.md body

**DORA article (verbatim, Art. 9(4)(b)):**

> [as quoted in GDPR ↔ DORA above]

<!-- aegis:purity: own_reg=DORA; demoted=8; core_cross_mentions=2 -->
