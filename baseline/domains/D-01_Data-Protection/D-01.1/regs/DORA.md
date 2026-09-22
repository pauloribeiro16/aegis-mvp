# D-01.1 — DORA module

> Regulation-specific layer: applies when `DORA` is in scope
> (activation: `if DORA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| DORA | SO-DORA-001 | CIA+A maintained across data states (at-rest, in-use, in-transit) | Financial entity; Art. 9(2); ICT-system-level; `high standards` anchor |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **DORA** | continuous + annual scenario review | ICT-supported data of financial entity | national CA + ESAs | Art. 9(2) |

## Sub-SO (DORA)

#### D-01.1.4 — Sub-SO for DORA

```yaml
id: SO-D-01.1.DORA
subdomain: D-01.1
applies_to: [DORA]
inherits_from: SO-DORA-001
source_SR: SR-DORA-001
activation: if DORA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Data confidentiality, integrity, authenticity and
availability are maintained at high standards across all data states,
including at rest, through ICT security policies, procedures, protocols
and tools designed to ensure ICT-system resilience, continuity and
availability (Art. 9(2)).

**CSF anchors (from `SR-DORA-001` v0.3 security_rationale):**
PR.DS-01, PR.DS-02, PR.DS-10, ID.AM-08.
*(The PR.DS-02 / PR.DS-10 / ID.AM-05 anchors are inherited from the 4×3
matrix context; D-01.1 is the at-rest cell, which is anchored
specifically by PR.DS-01.)*

---


## Security Requirements (DORA)

#### 1.1.4 — Financial-entity ICT data at rest

```yaml
- req_id: 1.1.4
  volere_section: 15
  volere_subtype: integrity

  title: "ICT-supported data of financial entity maintained at high standards of CIA at rest"

  derives_from:
    hso_sub_so: SO-D-01.1.DORA
    per_reg_so: SO-DORA-001
    source_sr: SR-DORA-001
    hso_file: ../../HierarchicalSecurityObjectives/D-01_Data-Protection/D-01.1.md
    objective_ref_section: "### D-01.1.4"

  description: |
    The product shall maintain data confidentiality, integrity, authenticity and availability at high standards across data states including at rest, through ICT security policies, procedures, protocols and tools designed to ensure ICT-system resilience, continuity and availability (DORA Art. 9(2)).

  fit_criterion: |
    High-standards symmetric encryption (AES-256 or stronger, EBA/ESMA/EIOPA RTS-conformant under DORA Art. 15 where applicable) is applied to financial-entity ICT-supported data at rest; the DORA Art. 9(4)(d) classification-driven cipher-strength overlay (per SR-DORA-003 / GV.RM-04) is documented for ICT risk-classification mapping; key-custody architecture is documented; verified by configuration audit + classification-driven cipher-strength overlay review + national-CA + ESA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: ["1.3 (Key Management — pending generation)"]

  nist_csf: [PR.DS-01]

  applicable_if:
    regs: [DORA]
  satisfaction:
    controls: []
    nodes: []

```


---


## Verbatim regulatory basis (DORA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**DORA article (verbatim from SR-DORA-001, Art. 9(2)):**
> Art. 9(2) ICT security policies, procedures, protocols and tools that aim to ensure the resilience, continuity and availability of ICT systems and to maintain high standards of availability, authenticity, integrity and confidentiality of data, whether at rest, in use or in transit.

**DORA article (verbatim — SR-DORA-001, Art. 9(2)):**
> Art. 9(2) ICT security policies, procedures, protocols and tools … to maintain high standards of availability, authenticity, integrity and confidentiality of data, whether at rest, in use or in transit.

**DORA article (verbatim — SR-DORA-001, Art. 9(2)):**
> Art. 9(2) … high standards of availability, authenticity, integrity and confidentiality of data, whether at rest, in use or in transit.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/DORA.md body — field `verified_relationship`

```yaml
verified_relationship: SAME (CRDA-deep, D-01.1: GDPR↔DORA CORRECTED from COMPLEMENTARY; NIS2↔DORA CORRECTED from EQUAL; CRA↔DORA CORRECTED from COMPLEMENTARY)
```

### from regs/DORA.md body

**Considerations.**

- DORA is OJ-explicit on the at-rest dimension (unlike GDPR's scope-imposed
  split or NIS 2's silence on in-use); the DORA classification-driven
  cipher-strength overlay (Art. 9(4)(d) + SR-DORA-003 per `GV.RM-04`) sits
  on top of the joint at-rest encryption for a DORA financial entity that
  is also a GDPR controller.

### from regs/DORA.md body

- The `high standards` anchor is qualitatively softer than CRA's `state of
  the art`; the OJ text defers the measurement criterion to EBA / ESMA /
  EIOPA RTS under Art. 15.


### from regs/DORA.md body — field `scope_overlap`

```yaml
    scope_overlap: Y   # DORA↔GDPR = Y (DORA financial entity is GDPR controller — typical); DORA↔NIS2 = Conditional (lex specialis in financial sector); HL engages on overlap

```

### from regs/DORA.md body — field `considerations`

```yaml
  considerations: |
    DORA is OJ-explicit on the at-rest dimension (unlike GDPR's scope-imposed
    split or NIS 2's silence on in-use); the DORA classification-driven
    cipher-strength overlay (Art. 9(4)(d) + SR-DORA-003 per `GV.RM-04`) sits
    on top of the joint at-rest encryption for a DORA financial entity that
    is also a GDPR controller. The `high standards` anchor is qualitatively
    softer than CRA's `state of the art`; the OJ text defers the measurement
    criterion to EBA / ESMA / EIOPA RTS under Art. 15. (Copied from the HSO
    Considerations block of `### D-01.1.4`; preserved here for self-contained
    traceability.)
```

<!-- aegis:purity: own_reg=DORA; demoted=5; core_cross_mentions=0 -->
