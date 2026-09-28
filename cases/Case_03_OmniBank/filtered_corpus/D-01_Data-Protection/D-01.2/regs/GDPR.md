# D-01.2 — GDPR module

> Regulation-specific layer: applies when `GDPR` is in scope
> (activation: `if GDPR in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SG-GDPR-001 (cross-ref) | Confidentiality, integrity, resilience of processing systems — covers in-transit via Art. 32(2) "transmitted" | Controller/processor; Art. 32(1)(b) + Art. 32(2); personal-data scope; risk-anchored; PR.DS-02 + PR.IR-01 substrate |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **GDPR** | continuous + on material change | personal data transmitted across networks | supervisory authority (DPA) | Art. 32(1)(b) + Art. 32(2) |

## Sub-SO (GDPR)

#### D-01.2.1 — Sub-SO for GDPR

```yaml
id: SG-D-01.2.GDPR
subdomain: D-01.2
applies_to: [GDPR]
inherits_from: SG-GDPR-001  # cross-ref — D-01.2 is covered by SG-GDPR-001 (D-01.1) per per-reg SO file
source_SR: SR-GDPR-002
activation: if GDPR in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Personal data transmitted across networks, inter-service
channels, and third-party infrastructure remains confidential and
unaltered in transit, with the in-transit protection anchored to the
five-event Art. 32(2) risk enumeration (accidental or unlawful
destruction, loss, alteration, unauthorised disclosure of, or access
to, personal data transmitted) (Art. 32(1)(b) + Art. 32(2)).

**CSF anchors (from `SR-GDPR-002` v0.3 security_rationale):**
PR.DS-02, PR.IR-01.
**PF 1.1 anchors (from `SR-GDPR-002` — dashboard `00_VISUALISATIONS/GDPR/GDPR_Dashboard.html`, mechanical uniformization):**
PR.DS-P2, PR.AC-P5.

---


## Security Requirements (GDPR)

#### 1.2.1 — Personal data in transit

```yaml
- req_id: 1.2.1
  volere_section: 15
  volere_subtype: integrity

  title: "Personal data in transit remains confidential and unaltered"

  derives_from:
    hso_sub_so: SG-D-01.2.GDPR
    per_reg_so: SG-GDPR-001  # cross-ref — D-01.2 is covered by SG-GDPR-001 (D-01.1) per per-reg SO file
    source_sr: SR-GDPR-002
    hso_file: ../../HierarchicalSecurityObjectives/D-01_Data-Protection/D-01.2.md
    objective_ref_section: "### D-01.2.1"

  description: |
    The product shall ensure that personal data transmitted across networks, inter-service channels, and third-party infrastructure remains confidential and unaltered in transit, with the in-transit protection anchored to the five-event Art. 32(2) risk enumeration (accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to, personal data transmitted) (GDPR Art. 32(1)(b) + Art. 32(2)).

  fit_criterion: |
    TLS 1.3 (or stronger) is applied to all in-transit channels carrying personal data; the five-event Art. 32(2) risk enumeration is addressed by technical measures on each event class (encryption for confidentiality, integrity verification for alteration, network segmentation for destruction/loss/access); cipher-suite selection is documented; verified by automated network scan + configuration audit + DPA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: ["1.3 (Key/Certificate Management — pending generation)", "3.x (Mutual Authentication — pending generation)"]

  nist_csf: [PR.DS-02, PR.IR-01]
  nist_pf: [PR.DS-P2, PR.AC-P5]

  applicable_if:
    regs: [GDPR]
  satisfaction:
    controls: []
    nodes: []

  considerations: |
    HSO D-01.2.1 carries no separate Considerations block — the GDPR in-transit
    sub-SO is cross-referenced to SG-GDPR-001 (the D-01.1 SO) and inherits the
    D-01.1 GDPR Considerations by reference via SR-GDPR-002. (Recorded here
    as a traceability note; no per-reg perspective was omitted.)
```


## Verbatim regulatory basis (GDPR)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**GDPR article (verbatim — SR-GDPR-002, Art. 32(1)(b) + Art. 32(2)):**
> Art. 32(1)(b) the ongoing confidentiality, integrity, availability and resilience of processing systems and services. Art. 32(2) in assessing the appropriate level of security account shall be taken in particular of the risks … from accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to, personal data transmitted, stored or otherwise processed.

**GDPR article (verbatim — SR-GDPR-002, Art. 32(1)(b)):**
> Art. 32(1)(b) the ongoing confidentiality, integrity, availability and resilience of processing systems and services.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/GDPR.md body — field `verified_relationship`

```yaml
verified_relationship: SAME (CRDA-deep, D-01.2: GDPR↔CRA CORRECTED from COMPLEMENTARY; GDPR↔DORA CORRECTED from COMPLEMENTARY)
```

### from regs/GDPR.md body — field `scope_overlap`

```yaml
    scope_overlap: Y   # GDPR↔CRA = Y (CRA product transmits personal data — typical); GDPR↔DORA = Y (DORA FE transmits personal data — typical); HL engages on overlap

```

<!-- aegis:purity: own_reg=GDPR; demoted=2; core_cross_mentions=0 -->
