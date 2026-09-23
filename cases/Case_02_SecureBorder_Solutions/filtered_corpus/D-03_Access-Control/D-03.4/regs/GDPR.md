# D-03.4 — GDPR module

> Regulation-specific layer: applies when `GDPR` is in scope
> (activation: `if GDPR in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SG-GDPR-007 | Personal-data processing systems implement appropriate technical and organisational measures ensuring that, by default, only personal data which are necessary for each specific purpose are processed — across amount, extent, period, and accessibility | Controller; Art. 25(2); data-protection by default; scope = personal data; "by default" across 4 dimensions (amount, extent, period, accessibility); PR.PS-01 + ID.AM-08 + GV.PO-01 |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **GDPR** | data-centric by-default (processing systems) | continuous (Art. 25(2) four-dimension AND) | `by default, only personal data which are necessary for each specific purpose of the processing are processed` (Art. 25(2)) + four AND-coordinated dimensions (amount, extent, period, accessibility) | `appropriate technical and organisational measures` + Art. 5(1)(c) data minimisation + `without the individual's intervention` opt-in gate | supervisory authority (four-dimension by-default audit) | by-default settings across four Art. 25(2) dimensions + Art. 5(1)(c) minimisation register + opt-in-gate evidence + per-system minimisation evidence, on PR.PS-01 + ID.AM-08 + GV.PO-01 anchors |

## Sub-SO (GDPR)

#### D-03.4.1 — Sub-SO for GDPR

```yaml
id: SG-D-03.4.GDPR
subdomain: D-03.4
applies_to: [GDPR]
inherits_from: SG-GDPR-007
source_SR: SR-GDPR-013
activation: if GDPR in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Personal-data processing systems implement appropriate
technical and organisational measures ensuring that, by default, only
personal data which are necessary for each specific purpose of the
processing are processed — across the four AND-coordinated dimensions
of amount of data collected, extent of their processing, period of their
storage, and their accessibility — with the additional constraint that
personal data are not made accessible without the individual's
intervention to an indefinite number of natural persons (Art. 25(2) +
Art. 25(1) privacy-by-design cross-anchor + Art. 5(1)(c) data
minimisation underlying principle).

**Considerations.**
- The four-dimensional AND is preserved from `SR-GDPR-013` `ambiguity_notes` (all four dimensions must individually be minimised and AND-coordinated per EDPB Guidelines 04/2019 on Article 25; an alternative reading allowing some dimensions to be relaxed if others are tightened would weaken the default and is rejected; the AND reading is the chosen one).
- On `without the individual's intervention`, the chosen reading treats the intervention requirement as the opt-in gate: the controller must not bypass the data subject's affirmative action to expose data.
- The downstream notification cascade (Art. 33 personal-data-breach notification) is part of D-04.3, not D-03.4.

**CSF anchors (from `SR-GDPR-013` v0.3 security_rationale):**
PR.PS-01, ID.AM-08.
**PF 1.1 anchors (from `SR-GDPR-013` — dashboard `00_VISUALISATIONS/GDPR/GDPR_Dashboard.html`, mechanical uniformization):**
CT.DP-P4, CT.PO-P4.
*(`SR-GDPR-013` covers the Art. 25(2) + Art. 25(1) + Art. 5(1)(c)
privacy-by-default obligation anchored to PR.PS-01 (configuration
management practices established and applied) + ID.AM-08 (data
managed consistent with risk strategy). PR.PS-01 anchors the
configuration-management baseline that sets the four default
dimensions — amount collected, extent processed, retention period,
accessibility — to their minimum-necessary values, satisfying the
Art. 25(2) AND-coordinated default and ensuring the minimum is
enforced as a system property rather than left to operator
judgement. ID.AM-08 captures the policy-level data-management
strategy that the defaults express: a documented risk-strategy
positioning opt-in collection, opt-out for out-of-purpose operations,
minimum-necessary retention and no public access unless explicitly
granted.)* GV.PO-01 (organisational cybersecurity policy) is the
governance-side anchor.

---


## Security Requirements (GDPR)

#### 3.4.1 — Data-centric by-default on processing systems (four AND-coordinated Art. 25(2) dimensions)

```yaml
- req_id: 3.4.1
  volere_section: 15
  volere_subtype: access

  title: "Personal-data processing systems implement by-default measures across amount, extent, period, and accessibility (Art. 25(2) four-dimension AND)"

  derives_from:
    hso_sub_so: SG-D-03.4.GDPR
    per_reg_so: SG-GDPR-007
    source_sr: SR-GDPR-013
    hso_file: ../../HierarchicalSecurityObjectives/D-03_Access-Control/D-03.4.md
    objective_ref_section: "### D-03.4.1"

  description: |
    The product shall ensure that personal-data processing systems implement appropriate technical and organisational measures such that, by default, only personal data which are necessary for each specific purpose of the processing are processed — across the four AND-coordinated dimensions of amount of personal data collected, extent of their processing, period of their storage, and their accessibility — with the additional constraint that by default personal data are not made accessible without the individual's intervention to an indefinite number of natural persons (GDPR Art. 25(2) + Art. 25(1) privacy-by-design + Art. 5(1)(c) data minimisation underlying principle).

  fit_criterion: |
    A by-default configuration operates at the processing-system level with the four Art. 25(2) dimensions minimised independently and AND-coordinated — amount of personal data collected limited to what is necessary for the specific purpose (no over-collection); extent of processing limited to operations necessary for the specific purpose (no out-of-purpose processing); period of storage limited to retention necessary for the specific purpose (no indefinite retention); accessibility limited to recipients intended by the specific purpose (no exposure to an indefinite number of natural persons without the individual's intervention); PR.PS-01 configuration-management baseline establishes the four default values as system properties rather than operator judgement; ID.AM-08 data-management risk strategy governs opt-in collection, opt-out for out-of-purpose operations, minimum-necessary retention, and no public access unless explicitly granted; GV.PO-01 organisational cybersecurity policy is the governance-side anchor; the EDPB Guidelines 04/2019 four-independent-minima reading is preserved — any reading allowing some dimensions to be relaxed if others are tightened is rejected as it would weaken the default and is not supported by EDPB; the `without the individual's intervention` opt-in gate closes the accessibility dimension — the controller must not bypass the data subject's affirmative action to expose data; the data-centric by-default discipline operates at the processing-system layer only, with the layer hand-off to CRA product-centric secure-by-default (when the processing system is a CRA-regulated product) documented as the controlled layer interface at which the GDPR data-centric four-dimension AND ends; the CRA tailor-made carve-out does NOT propagate into GDPR scope — even a CRA tailor-made product configuration does not exempt the controller from GDPR Art. 25(2); verified by four-dimension by-default settings audit + Art. 5(1)(c) minimisation register review + opt-in-gate evidence + DPA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [3.1.1 (data-subject identity verification feeds the opt-in-gate evidence on the accessibility dimension)]

  nist_csf: [PR.PS-01, ID.AM-08]
  nist_pf: [CT.DP-P4, CT.PO-P4]

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
> Art. 25(2) obliges the controller to implement appropriate technical and organisational measures for ensuring that, by default, only personal data which are necessary for each specific purpose of the processing are processed. That obligation applies to the amount of personal data collected, the extent of their processing, the period of their storage and their accessibility. In particular, such measures shall ensure that by default personal data are not made accessible without the individual's intervention to an indefinite number of natural persons.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/GDPR.md body — field `verified_relationship`

```yaml
verified_relationship: SAME DIFFERENT-PERSPECTIVE (CRDA-deep, D-03.4: GDPR↔CRA same DIFFERENT-PERSPECTIVE confirmed after OJ-text analysis)
```

### from regs/GDPR.md body

- The data-centric by-default is distinct from the CRA product-centric secure-by-default — the data-processing layer is system/configuration-of-data-side, and the four-dimension AND discipline operates at that layer only.

### from regs/GDPR.md body

- The CRA tailor-made carve-out does NOT propagate into GDPR scope: a CRA tailor-made product configuration does not exempt the controller from GDPR Art. 25(2).

### from regs/GDPR.md body

- For an organisation across both regulators, the GDPR leg documents the data-side leg of the two-layer default posture rather than imposing a separate framework; the boundary hand-off to CRA product-secure-by-default is documented as the controlled layer interface at which the data-centric four-dimension AND ends.

### from regs/GDPR.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # GDPR↔CRA = Conditional (Y when CRA product processes personal data; tailor-made carve-out does NOT exempt); HL engages on overlap; for parties that deploy a CRA product that does NOT process personal data, only the CRA sub-requirement activates

```

### from regs/GDPR.md body — field `considerations`

```yaml
  considerations: |
    The data-centric by-default is distinct from the CRA product-centric secure-by-default — the data-processing layer is system/configuration-of-data-side, and the four-dimension AND discipline operates at that layer only. The four-dimensional AND (R1 all four dimensions must individually be minimised and AND-coordinated; alternative reading allowing some dimensions to be relaxed if others are tightened rejected as it would weaken the default and is not supported by EDPB Guidelines 04/2019 on Article 25 which treats the four dimensions as independent minima) is preserved verbatim from `SR-GDPR-013` `ambiguity_notes`. The `without the individual's intervention` interpretation treats the intervention requirement as the opt-in gate: the controller must not bypass the data subject's affirmative action to expose data. The CRA tailor-made carve-out (Annex I Part I (2)(b) `unless otherwise agreed between manufacturer and business user in relation to a tailor-made product with digital elements`) does NOT propagate into GDPR scope — even a bespoke CRA tailor-made product configuration does not exempt the controller from GDPR Art. 25(2) on the data side. For an organisation across both regulators, the GDPR leg documents the data-side leg of the two-layer default posture rather than imposing a separate framework. The downstream notification cascade (Art. 33 personal-data-breach notification) is part of D-04.3, not D-03.4. (Copied from the HSO Considerations block of `### D-03.4.1`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=GDPR; demoted=6; core_cross_mentions=1 -->
