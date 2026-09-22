# D-03.3 — GDPR module

> Regulation-specific layer: applies when `GDPR` is in scope
> (activation: `if GDPR in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-006 | Persons authorised to process personal data act only on documented instructions from the controller (or processor) and are bound by confidentiality | Controller/processor; Art. 29 + Art. 32(4) + Art. 28(3)(a)/(b); personal-data-scope chain of authority controller → processor → authorised persons; PR.AA-05 + PR.AA-06 + PR.AT-02 |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **GDPR** | personal-data-scope chain of authority (controller → processor → authorised persons) | continuous (instruction-bound processing) | `chain of authority controller → processor → authorised persons` (Art. 29 + Art. 32(4) + Art. 28(3)(a)/(b)) | `documented instructions` + confidentiality undertakings + Art. 5(1)(c) necessity on identified-purpose scope | supervisory authority (instruction register + processor contract inspection) | instruction register + processor Art. 28(3)(a)/(b) contract + confidentiality undertaking register + technical enforcement per PR.AA-05 + PR.AA-06 |

## Sub-SO (GDPR)

#### D-03.3.1 — Sub-SO for GDPR

```yaml
id: SO-D-03.3.GDPR
subdomain: D-03.3
applies_to: [GDPR]
inherits_from: SO-GDPR-006
source_SR: SR-GDPR-011, SR-GDPR-012
activation: if GDPR in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Persons authorised to process personal data act only on
documented instructions from the controller (or processor), and are
bound by confidentiality or an appropriate statutory obligation of
confidentiality, with documented instructions binding the controller →
processor → authorised-persons chain of authority under Art. 29 +
Art. 32(4) + Art. 28(3)(a)/(b) and Art. 4(7) + Art. 4(8) anchoring
controller and processor definitions.

**Considerations.**
- The `instructions` polysemy (R1 documented in contract with operational instructions recorded contemporaneously; R2 verbal with contemporaneous recording acceptable; R3 workflow-implied rejected) is preserved verbatim from `SR-GDPR-011` `ambiguity_notes`.
- The `appropriate statutory obligation of confidentiality` polysemy (R1 equivalent-scope NDA; R2 pre-existing statutory professional-secrecy; R3 public-sector employee secrecy under Member State law in narrow contexts) is preserved from `SR-GDPR-012` `ambiguity_notes`.
- The downstream notification cascade (Art. 33 personal-data-breach notification) is part of D-04.3, not D-03.3.

**CSF anchors (from `SR-GDPR-011` + `SR-GDPR-012` v0.3 security_rationale):**
PR.AA-05, PR.AA-06, PR.AT-02.
**PF 1.1 anchors (from `SR-GDPR-011`, `SR-GDPR-012` — dashboard `00_VISUALISATIONS/GDPR/GDPR_Dashboard.html`, mechanical uniformization):**
PR.AC-P1, PR.AC-P2, CT.PO-P1, GV.AT-P2.
*(`SR-GDPR-011` covers the Art. 29 + Art. 32(4) + Art. 28(3)(a)/(b)
instruction-bound authorisation under least-privilege authorisation
anchored to PR.AA-05 (access permissions managed per least privilege)
+ PR.AA-06 (access limited to authorised users/services/hardware). The
two anchors together operationalise the chain-of-authority pattern
(controller to processor to authorised persons) that Arts. 29 and
28(3) establish, with Union or Member State law as the only exception.
`SR-GDPR-012` covers the Art. 28(3)(b) + Art. 29 + Art. 32(4)
confidentiality undertakings for authorised personnel anchored to
PR.AA-05 + PR.AT-02 (workforce understands role-specific security
responsibilities). The two anchors together operationalise the
confidentiality ring that Arts. 28(3)(b) and 32(4) create around any
natural person handling personal data, combining the legal-policy
lever with the technical-enforcement lever.)*

---


## Security Requirements (GDPR)

#### 3.3.1 — Personal-data-scope chain of authority (controller → processor → authorised persons)

```yaml
- req_id: 3.3.1
  volere_section: 15
  volere_subtype: access

  title: "Authorisation in personal-data scope operates through documented instructions and confidentiality undertakings (chain of authority controller → processor → authorised persons)"

  derives_from:
    hso_sub_so: SO-D-03.3.GDPR
    per_reg_so: SO-GDPR-006
    source_sr: SR-GDPR-011, SR-GDPR-012
    hso_file: ../../HierarchicalSecurityObjectives/D-03_Access-Control/D-03.3.md
    objective_ref_section: "### D-03.3.1"

  description: |
    The product shall ensure that persons authorised to process personal data act only on documented instructions from the controller (or processor), with the controller → processor → authorised-persons chain of authority binding each link and authorised persons bound by confidentiality or an appropriate statutory obligation of confidentiality, anchored to PR.AA-05 + PR.AA-06 + PR.AT-02 on the personal-data-scope chain-of-authority pattern that Arts. 29 + 28(3)(a)/(b) + 32(4) establish (GDPR Art. 29 + Art. 32(4) + Art. 28(3)(a)/(b) + Art. 4(7)/(8)).

  fit_criterion: |
    A documented-instructions register records, for each processing operation, the controller-issued instruction, the processor-contract Art. 28(3)(a)/(b) clause that anchors it, and the operational instructions issued under it; an Art. 28(3)(b) confidentiality-undertaking register binds each authorised natural person (controller staff, processor staff, sub-processor staff) to either an equivalent-scope NDA, a pre-existing statutory professional-secrecy, or a Member-State-law public-sector employee-secrecy; technical enforcement under PR.AA-05 + PR.AA-06 prevents processing outside documented authority and surfaces it as observable events; the personal-data-scope chain-of-authority discipline operates at the staff-side / processor-boundary only, with the boundary hand-off to NIS 2 workforce-side lifecycle (D-03.1) and to CRA product-side authenticated-and-authorised boundary documented as the controlled interfaces at which the GDPR instruction-bound discipline ends; verified by documented-instructions register audit + Art. 28(3)(a)/(b) processor-contract inspection + confidentiality-undertaking register review + PR.AA-05/PR.AA-06 access-enforcement evidence + boundary hand-off-protocol documentation + DPA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [3.1.1 (data-subject identity feeds the verification event at the controller-facing rights-exercise endpoint)]

  nist_csf: [PR.AA-05, PR.AA-06]
  nist_pf: [PR.AC-P1, PR.AC-P2, CT.PO-P1]

  applicable_if:
    regs: [GDPR]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (GDPR)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**GDPR article (verbatim):**
> Art. 29 requires the processor and any person acting under the authority of the controller or of the processor, who has access to personal data, not to process those data except on instructions from the controller, unless required to do so by Union or Member State law. Art. 32(4) reinforces this for natural persons acting under controller or processor authority by requiring the controller and processor to take steps to ensure that any such natural person does not process the data except on instructions.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/GDPR.md body — field `verified_relationship`

```yaml
verified_relationship: SAME — COMPLEMENTARY (CRDA-deep, D-03.3: GDPR↔NIS2 SAME — COMPLEMENTARY; GDPR↔CRA SAME — COMPLEMENTARY; GDPR↔DORA SAME — COMPLEMENTARY)
```

### from regs/GDPR.md body

- The personal-data-scope chain of authority is distinct from the NIS 2 entity-side access-control policy, the CRA product-side authenticated-and-authorised boundary, and the DORA financial-entity-side legitimate-and-approved-only ICT-asset access — the personal-data-scope boundary is staff-side / processor-bound, and the chain-of-authority discipline operates at that boundary only.

### from regs/GDPR.md body

- For an organisation across multiple regulators, the GDPR leg documents the personal-data-scope leg of the multi-boundary authorisation architecture rather than imposing a separate authorisation framework; the boundary hand-off to NIS 2 workforce-side lifecycle (D-03.1) and to CRA product-side authorisation is documented as the controlled interface at which the GDPR instruction-bound discipline ends.

### from regs/GDPR.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # GDPR↔NIS2 = N (data subjects vs workforce are distinct identity objects); GDPR↔CRA = Conditional (Y when CRA product hosts data-subject rights endpoints); GDPR↔DORA = Conditional (Y when DORA financial entity is also controller); HL engages on overlap

```

### from regs/GDPR.md body — field `considerations`

```yaml
  considerations: |
    The personal-data-scope chain of authority is distinct from the NIS 2 entity-side access-control policy, the CRA product-side authenticated-and-authorised boundary, and the DORA financial-entity-side legitimate-and-approved-only ICT-asset access — the staff-side / processor-boundary is its own surface, and the instruction-bound discipline operates at that surface only. The `instructions` polysemy (R1 documented in the Art. 28(3)(a) contract with operational instructions recorded contemporaneously, R2 verbal with contemporaneous recording acceptable, R3 workflow-implied rejected) is preserved verbatim from `SR-GDPR-011` `ambiguity_notes`. The `appropriate statutory obligation of confidentiality` polysemy (R1 equivalent-scope NDA, R2 pre-existing statutory professional-secrecy, R3 Member-State-law public-sector employee-secrecy in narrow contexts) is preserved from `SR-GDPR-012` `ambiguity_notes`. For an organisation across multiple regulators, the GDPR leg documents the personal-data-scope leg of the multi-boundary authorisation architecture rather than imposing a separate authorisation framework. The downstream notification cascade (Art. 33 personal-data-breach notification) is part of D-04.3, not D-03.3. (Copied from the HSO Considerations block of `### D-03.3.1`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=GDPR; demoted=5; core_cross_mentions=1 -->
