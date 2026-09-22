# D-01.1 — GDPR module

> Regulation-specific layer: applies when `GDPR` is in scope
> (activation: `if GDPR in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-001 | CIA + resilience for personal data processing | Controller/processor; Art. 5(1)(f) + Art. 32(1)(a)/(b); personal-data scope; risk-anchored `appropriate` |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **GDPR** | continuous risk-anchored | personal data | supervisory authority (DPA) | Art. 5(1)(f) + Art. 32(1)(a)/(b) |

## Sub-SO (GDPR)

#### D-01.1.1 — Sub-SO for GDPR

```yaml
id: SO-D-01.1.GDPR
subdomain: D-01.1
applies_to: [GDPR]
inherits_from: SO-GDPR-001
source_SR: SR-GDPR-001
activation: if GDPR in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Personal data at rest is processed in a manner that ensures
appropriate security — including protection against unauthorised or
unlawful processing and against accidental loss, destruction or damage —
using appropriate technical or organisational measures, with the ability
to ensure the ongoing confidentiality, integrity, availability and
resilience of processing systems and services (Art. 5(1)(f) + Art.
32(1)(b); the `appropriate` threshold is anchored by the five Art. 32(1)
preamble factors — state of the art, costs of implementation, nature,
scope, context, purposes, risks).

**CSF anchors (from `SR-GDPR-001` v0.3 security_rationale):**
PR.DS-01, PR.DS-10.
**PF 1.1 anchors (from `SR-GDPR-001` — dashboard `00_VISUALISATIONS/GDPR/GDPR_Dashboard.html`, mechanical uniformization):**
PR.DS-P1, PR.PO-P3.

---


## Security Requirements (GDPR)

#### 1.1.1 — Personal data at rest

```yaml
- req_id: 1.1.1
  volere_section: 15
  volere_subtype: integrity

  title: "Personal data at rest is protected by appropriate technical measures"

  derives_from:
    hso_sub_so: SO-D-01.1.GDPR
    per_reg_so: SO-GDPR-001
    source_sr: SR-GDPR-001
    hso_file: ../../HierarchicalSecurityObjectives/D-01_Data-Protection/D-01.1.md
    objective_ref_section: "### D-01.1.1"

  description: |
    The product shall protect personal data held at rest in storage against unauthorised or unlawful processing and against accidental loss, destruction or damage, using appropriate technical measures — primarily encryption with appropriate key custody — anchored to the five Art. 32(1) preamble factors (state of the art, costs of implementation, nature, scope, context, purposes, risks) (GDPR Art. 5(1)(f) + Art. 32(1)(a)/(b)).

  fit_criterion: |
    AES-256 (or stronger) symmetric encryption is applied to all personal-data storage volumes; key custody is logically or physically separated from data access; the controller/processor risk-assessment artefact cites the five Art. 32(1) preamble factors and selects cipher strength accordingly; verified by automated configuration audit + manual key-custody review + DPA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: ["1.3 (Key Management — pending generation)"]

  nist_csf: [PR.DS-01, PR.DS-10]

  applicable_if:
    regs: [GDPR]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (GDPR)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**GDPR article (verbatim from SR-GDPR-001, Art. 5(1)(f) + Art. 32(1)(a)/(b)):**
> Art. 5(1)(f) integrity and confidentiality … processed in a manner that ensures appropriate security of the personal data … protection against unauthorised or unlawful processing and against accidental loss, destruction or damage, using appropriate technical or organisational measures. Art. 32(1)(b) the ability to ensure the ongoing confidentiality, integrity, availability and resilience of processing systems and services.

**GDPR article (verbatim from SR-GDPR-001, Art. 5(1)(f) + Art. 32(1)(a)):**
> Art. 32(1)(a) pseudonymisation and encryption of personal data … as appropriate technical measures.

**GDPR article (verbatim — SR-GDPR-001, Art. 5(1)(f) + Art. 32(1)(b) "ongoing confidentiality, integrity, availability and resilience"):**
> Art. 5(1)(f) integrity and confidentiality … appropriate security of the personal data. Art. 32(1)(b) the ongoing confidentiality, integrity, availability and resilience of processing systems and services.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/GDPR.md body — field `verified_relationship`

```yaml
verified_relationship: SAME (CRDA-deep, D-01.1: GDPR↔NIS2 CORRECTED from COMPLEMENTARY; GDPR↔CRA CORRECTED from COMPLEMENTARY; GDPR↔DORA CORRECTED from COMPLEMENTARY)
```

### from regs/GDPR.md body

**Considerations.**

- GDPR's anchor is the strictest for personal data on the at-rest dimension
  even where CRA state-of-the-art is the strictest in absolute terms — the
  GDPR scope (personal data) is narrower and the obligation is unconditional
  (no `where appropriate` hedge).


### from regs/GDPR.md body — field `scope_overlap`

```yaml
    scope_overlap: Y   # GDPR↔NIS2 = Y (controller is also NSIE — typical); HL engages on overlap

```

### from regs/GDPR.md body — field `considerations`

```yaml
  considerations: |
    GDPR's anchor is the strictest for personal data on the at-rest dimension
    even where CRA state-of-the-art is the strictest in absolute terms — the
    GDPR scope (personal data) is narrower and the obligation is unconditional
    (no `where appropriate` hedge). (Copied from the HSO Considerations block
    of `### D-01.1.1`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=GDPR; demoted=4; core_cross_mentions=0 -->
