# D-01.4 — DORA module

> Regulation-specific layer: applies when `DORA` is in scope
> (activation: `if DORA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| DORA | SO-DORA-001 (cross-ref) | Integrity is one dimension of the 4×3 CIA+A matrix (at rest, in use, in transit) | Financial entity; Art. 9(2) CIA+A 4-way AND + 3-way OR of data states; ICT-system-level; `high standards`; OJ-explicit integrity dimension |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **DORA** | continuous + annual scenario review (Art. 7(2)) | ICT-system CIA+A (4×3 matrix; integrity cell) | national CA + ESAs | Art. 9(2) |

## Sub-SO (DORA)

#### D-01.4.3 — Sub-SO for DORA

```yaml
id: SO-D-01.4.DORA
subdomain: D-01.4
applies_to: [DORA]
inherits_from: SO-DORA-001
source_SR: SR-DORA-001
activation: if DORA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Data confidentiality, integrity, authenticity and availability
are maintained at high standards across all data states — at rest, in use,
or in transit — through ICT security policies, procedures, protocols and
tools designed to ensure ICT-system resilience, continuity and availability
(Art. 9(2)).

**CSF anchors (from `SR-DORA-001` v0.3 security_rationale):**
PR.DS-01, PR.DS-02, PR.DS-10, ID.AM-08.
*(The PR.DS-01 / PR.DS-02 / PR.DS-10 / ID.AM-05 anchors are inherited from
the 4×3 matrix context; D-01.4 is the integrity cell, which is anchored
specifically by PR.DS-01 (at-rest integrity) + PR.DS-10 (in-use integrity),
with PR.DS-02 (in-transit integrity) + ID.AM-05 (data managed consistent
with risk strategy) as the supplementary cell anchors.)*

---


## Security Requirements (DORA)

#### 1.4.3 — ICT-system integrity cell of the 4×3 CIA+A matrix

```yaml
- req_id: 1.4.3
  volere_section: 15
  volere_subtype: integrity

  title: "ICT-system data integrity maintained at high standards across all data states"

  derives_from:
    hso_sub_so: SO-D-01.4.DORA
    per_reg_so: SO-DORA-001
    source_sr: SR-DORA-001
    hso_file: ../../HierarchicalSecurityObjectives/D-01_Data-Protection/D-01.4.md
    objective_ref_section: "### D-01.4.3"

  description: |
    The product shall maintain data confidentiality, integrity, authenticity and availability at high standards across all data states — at rest, in use, or in transit — through ICT security policies, procedures, protocols and tools designed to ensure ICT-system resilience, continuity and availability, with the integrity cell of the 4×3 CIA+A × data-states matrix as the binding property on the DORA side (DORA Art. 9(2)).

  fit_criterion: |
    ICT-system-level integrity controls cover at-rest integrity (PR.DS-01 — cryptographic hashes / MACs on stored data), in-transit integrity (PR.DS-02 — signed-protocol integrity on data in motion), in-use integrity (PR.DS-10 — runtime integrity controls such as signed firmware, control-flow integrity, tamper-detection instrumentation), and risk-strategy-managed data integrity (ID.AM-05 — data managed consistent with risk strategy per DORA Art. 6 chapeau); the integrity cell of the DORA Art. 9(2) 4×3 matrix is documented and discharged; verified by configuration audit of all four integrity anchors + classification-driven cipher-strength overlay (per DORA Art. 9(4)(d) + SR-DORA-003 GV.RM-04) + national-CA + ESAs inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: []

  nist_csf: [PR.DS-01, PR.DS-02, PR.DS-10, ID.AM-08]

  applicable_if:
    regs: [DORA]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (DORA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**DORA article (verbatim — SR-DORA-001, Art. 9(2)):**
> Art. 9(2) … high standards of availability, authenticity, integrity and confidentiality of data, whether at rest, in use or in transit.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/DORA.md body — field `verified_relationship`

```yaml
verified_relationship: SAME (CRDA-deep, D-01.4: GDPR↔DORA CORRECTED from COMPLEMENTARY; CRA↔DORA CORRECTED from EQUAL; DORA↔AI_Act CORRECTED from DIFFERENT PERSPECTIVE)
```

### from regs/DORA.md body

**Considerations.**

- DORA is OJ-explicit on the integrity dimension (unlike NIS 2's silence on
  the standalone integrity dimension or AI Act's resilience-not-integrity
  framing); the integrity cell of the 4×3 CIA+A matrix is the ICT-system-
  level integrity property, layered above CRA's product-side technical
  integrity.

### from regs/DORA.md body

- For a DORA financial entity processing personal data on a CRA-regulated
  product, DORA's ICT-system-level integrity covers the storage-integrity leg
  (typically the strictest operational surface on the integrity dimension),
  with GDPR's accuracy workflow + CRA's universal-quantifier protection
  layered as the personal-data-side and product-side sub-legs.

### from regs/DORA.md body

- The `high standards` anchor is qualitatively softer than CRA's `state of
  the art`; the OJ text defers the measurement criterion to EBA / ESMA /
  EIOPA RTS under Art. 15.


### from regs/DORA.md body — field `scope_overlap`

```yaml
    scope_overlap: Y   # DORA↔GDPR = Y; DORA↔CRA = Y; DORA↔AI_Act = Y (DORA financial entity deploys high-risk AI — typical); HL engages on overlap

```

### from regs/DORA.md body — field `considerations`

```yaml
  considerations: |
    DORA is OJ-explicit on the integrity dimension (unlike NIS 2's silence
    on the standalone integrity dimension or AI Act's resilience-not-
    integrity framing); the integrity cell of the 4×3 CIA+A matrix is the
    ICT-system-level integrity property, layered above CRA's product-side
    technical integrity. For a DORA financial entity processing personal
    data on a CRA-regulated product, DORA's ICT-system-level integrity
    covers the storage-integrity leg (typically the strictest operational
    surface on the integrity dimension), with GDPR's accuracy workflow +
    CRA's universal-quantifier protection layered as the personal-data-side
    and product-side sub-legs. The `high standards` anchor is qualitatively
    softer than CRA's `state of the art`; the OJ text defers the measurement
    criterion to EBA / ESMA / EIOPA RTS under Art. 15. (Copied from the HSO
    Considerations block of `### D-01.4.3`; preserved here for self-contained
    traceability.)
```

<!-- aegis:purity: own_reg=DORA; demoted=6; core_cross_mentions=0 -->
