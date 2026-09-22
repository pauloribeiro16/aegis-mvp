# D-06.3 — GDPR module

> Regulation-specific layer: applies when `GDPR` is in scope
> (activation: `if GDPR in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-022; SO-GDPR-033; SO-GDPR-035 | Processor contracts contain the eight Art. 28(3)(a)–(h) mandatory clauses; third-country transfers use Art. 46 safeguards where no adequacy decision exists; third-country court or administrative requests are recognised only through an international-agreement basis | Controller/processor personal-data contract; transfer-safeguard contractual layer; DPA-facing accountability |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **GDPR** | processor and transfer recipient handling personal data | per-processor contract; per-transfer safeguard; per-third-country legal request | Art. 28(3) DPA 8-element list; Art. 46 safeguards; Art. 48 legal-request filter | DPA; controller; processor | Art. 28(3)(a)–(h); Art. 46; Art. 48 |

## Sub-SO (GDPR)

#### D-06.3.1 — Sub-SO for GDPR

```yaml
id: SO-D-06.3.GDPR
subdomain: D-06.3
applies_to: [GDPR]
inherits_from: [SO-GDPR-022, SO-GDPR-033, SO-GDPR-035]
source_SR: [SR-GDPR-034, SR-GDPR-035, SR-GDPR-036, SR-GDPR-037, SR-GDPR-056, SR-GDPR-059]
activation: if GDPR in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Controller/processor contracts and related transfer instruments include the GDPR-specific contractual security obligations required for personal-data processing: the Art. 28(3)(a)–(h) eight-element DPA floor, sub-processor authorisation and change-notification, processor Art. 32 security-measure commitments, audit/inspection access, and contract-end return/deletion; the Art. 46 appropriate-safeguards mechanism and the Art. 48 international-agreement filter apply where personal data leaves the EEA or is exposed to third-country legal-process pressure.

**CSF anchors (from GDPR SRs):** GV.SC-03, GV.SC-04, GV.SC-02, GV.OC-03, ID.AM-08.

---


## Security Requirements (GDPR)

#### 6.3.1 — Art. 28(3) 8-element DPA + Art. 46 transfer safeguards + Art. 48 international-agreement filter

```yaml
- req_id: 6.3.1
  volere_section: 15
  volere_subtype: immunity

  title: "Art. 28(3)(a)–(h) 8-element DPA closed-list contracts + Art. 46 transfer safeguards + Art. 48 international-agreement filter for third-country legal-process exposure"

  derives_from:
    hso_sub_so: SO-D-06.3.GDPR
    per_reg_so: SO-GDPR-022, SO-GDPR-033, SO-GDPR-035
    source_sr: SR-GDPR-034, SR-GDPR-035, SR-GDPR-036, SR-GDPR-037, SR-GDPR-056, SR-GDPR-059
    hso_file: ../../HierarchicalSecurityObjectives/D-06_Supply-Chain/D-06.3.md
    objective_ref_section: "### D-06.3.1"

  description: |
    The product shall materialise controller/processor contractual security obligations as Art. 28(3)(a)–(h) 8-element DPA contracts, Art. 46 appropriate-safeguards instruments for third-country transfers without adequacy decisions, and an Art. 48 international-agreement filter for third-country court/administrative requests, with sub-processor authorisation under Art. 28(2), Art. 32 processor security-measure commitments, audit/inspection access, and contract-end return/deletion — GDPR layer is additive on DORA Art. 30, never substituted (the CORRECTED CRDA pair is clause-list union).

  fit_criterion: |
    A controller-processor DPA matrix is maintained covering each in-scope processor via Art. 28(3)(a)–(h) 8 closed-list clauses — (a) documented instructions + (b) confidentiality + (c) Art. 32 measures + (d) sub-processor conditions + (e) data-subject-rights assistance + (f) Art. 33/34 incident-assistance + (g) deletion-or-return + (h) audit/inspection — attested in each DPA contract; Art. 28(2) sub-processor authorisation chain is materialised as a written prior-authorisation regime with a maintained processor list per Art. 30(2) RoPA; Art. 46 safeguards operate for each transfer (SCCs, BCRs, codes of conduct, certification, ad-hoc contractual clauses) where no adequacy decision exists, with transfer-mapping per Schrems II / EDPB Recommendations 01/2020 supplementary-measures assessment; Art. 48 international-agreement filter rejects or routes through an international-agreement basis any third-country court/administrative request for personal-data disclosure; in DORA overlap, Art. 28(3) 8-element DPA clauses + Art. 46/48 safeguards ADD to DORA Art. 30(2) ICT-contract elements (clause-list union, NOT substitution) with GDPR-specific processor terms retained whenever the ICT provider processes personal data; verified by DPA matrix inspection + Art. 28(3)(a)–(h) closed-list clause-inventory attestation review + Art. 28(2) sub-processor chain inspection + Art. 46 transfer-mapping review + Art. 48 international-agreement filter log review + DPA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [6.1.1 (processor-selection discipline feeds DPA party-list and sub-processor chain), 6.3.4 (clause-list union when same ICT provider is processor — GDPR-specific clauses retained)]

  nist_csf: [GV.SC-02, GV.SC-03, GV.SC-04, GV.OC-03, ID.AM-08]

  applicable_if:
    regs: [GDPR]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (GDPR)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**GDPR article (verbatim, Art. 28(3)(a)–(h)):**
> "Processing by a processor … be governed by a contract … that sets out … the subject-matter and duration of the processing, the nature and purpose of the processing, the type of personal data and categories of data subjects, and the obligations and rights of the controller. That contract or other legal act shall stipulate, in particular, that the processor: (a) processes the personal data only on documented instructions from the controller …; (b) ensures that persons authorised to process the personal data have committed themselves to confidentiality …; (c) implements all the measures required pursuant to Article 32; (d) engages another processor only with the prior specific or general written authorisation of the controller …; (e) assists the controller in fulfilling its obligation to respond to requests for exercising the data subject's rights …; (f) assists the controller in ensuring compliance with the obligations pursuant to Articles 32 to 36; (g) at the choice of the controller, deletes or returns all the personal data to the controller after the end of the provision of services relating to processing … and deletes existing copies; (h) makes available to the controller all information necessary to demonstrate compliance with the obligations laid down in this Article and allow for and contribute to audits, including inspections, conducted by the controller or another auditor mandated by the controller." — Art. 28(3)(a)–(h) GDPR


## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/GDPR.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-06.3: GDPR↔NIS2 = COMPLEMENTARY; GDPR↔CRA = DIFFERENT-PERSPECTIVE; GDPR↔DORA = CORRECTED — COMPLEMENTARY clause-list union)
```

### from regs/GDPR.md body

**Considerations.**

- In overlap with DORA, the GDPR layer is additive: the DORA Art. 30(2) list does not remove instruction-bound processing (Art. 28(3)(a)), Art. 28(2) sub-processor authorisation, Art. 28(3)(h) audit contribution, or Chapter V transfer controls.

### from regs/GDPR.md body

- The CRA importer/distributor economic-operator duties are market-surveillance-facing, not DPA-style negotiated contracts; the two regimes do not duplicate on the same instrument.


### from regs/GDPR.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # GDPR↔NIS2 = Conditional (Y controller-NSIE; DPA clauses layer with NIS 2 supplier-security contract clauses); GDPR↔CRA = Conditional (Y integrated manufacturer-controller deployer; DPA clauses coexist with CRA economic-operator duties); GDPR↔DORA = Y (clause-list union applies — CORRECTED pair — same ICT provider can be processor and DORA ICT third party)

```

### from regs/GDPR.md body — field `considerations`

```yaml
  considerations: |
    The GDPR contractual-security obligation is the controller-processor DPA materialised through the Art. 28(3)(a)–(h) 8-element closed-list clauses, the Art. 46 transfer-safeguards instrument set, and the Art. 48 international-agreement filter; the operational substrate is a DPA matrix + transfer register + third-country request filter. In DORA overlap, the GDPR layer is additive: DORA Art. 30(2) list does NOT remove instruction-bound processing (Art. 28(3)(a)), Art. 28(2) sub-processor authorisation, Art. 28(3)(h) audit-contribution, or Chapter V transfer controls — this is the operative effect of the CORRECTED CRDA pair (CONTRADICTORY → COMPLEMENTARY clause-list union). The CRA importer/distributor economic-operator duties are market-surveillance-facing, NOT DPA-style negotiated contracts; the two regimes do not duplicate on the same instrument and coexist at distinct supply-chain layers. The CRA Art. 13(6) component-vulnerability reporting limb is the post-contract upstream feedback path connecting CRA-side escalation with the NIS 2 supplier-security assessment (lifecycle hinge), and operates at a different actor than the DPA. (Copied from the HSO Considerations block of `### D-06.3.1`; preserved here for self-containment per Volere shell `considerations` field definition.)
```

### from regs/GDPR.md body

**GDPR article (verbatim, Art. 28(3)(a)–(h)):**

> (See GDPR↔NIS2 pair above for the verbatim 8-element list.)

<!-- aegis:purity: own_reg=GDPR; demoted=6; core_cross_mentions=2 -->