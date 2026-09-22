# D-08.1 — CRA module

> Regulation-specific layer: applies when `CRA` is in scope
> (activation: `if CRA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| CRA | SO-CRA-048 (partial) | Detailed user-facing instructions (Annex II §8(a)–(f)) for product secure use over lifetime. | User instructions with the product, not workforce awareness; partial-coverage. AEGIS taxonomy §4.1 marks NIS 2 / DORA / GDPR as the authorities for full staff awareness. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **CRA** | end-user (external user with the product) — partial coverage per AEGIS taxonomy §4.1; workforce-side limited to Annex II §8(f) integrator information | manufacturer places product on market (Art. 13(1) trigger); Annex II §8(a)–(f) instructions accompany the product throughout the lifetime; Art. 13(18) 10-year Annex II information accessibility | support period ≥ 5 years (Art. 13(8) sentence 3) + 10-year Annex II information accessibility (Art. 13(18)) — qualitative support-period framing; the `detailed` content threshold is harmonised-standards-pending | end-user (B2C/user-facing) + market surveillance authority (MSA) — Annex II §8(a)–(f) instructions on the product; Annex II §8(f) integrator information discharge the workforce-side partial dimension for B2B integrators | Art. 13(1) + Annex II §8(a) + Annex II §8(b) + Annex II §8(c) + Annex II §8(d) + Annex II §8(e) + Annex II §8(f) + Art. 13(18) support-period accessibility + Recital 25 (Annex II scope) |

## Sub-SO (CRA)

#### D-08.1.3 — Sub-SO for CRA (partial)

```yaml
id: SO-D-08.1.CRA
subdomain: D-08.1
applies_to: [CRA]
inherits_from: SO-CRA-048 (partial)
source_SR: SR-CRA-071
activation: if CRA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** A product with digital elements is accompanied by detailed instructions — or an internet address referring to such detailed instructions — covering the necessary measures during initial commissioning and throughout the lifetime of the product to ensure its secure use (Annex II §8(a)–(e) CRA), and — where the product is intended for integration into other products — the information necessary for the integrator to comply with the essential cybersecurity requirements set out in Part I of Annex I and the documentation requirements set out in Annex VII (Annex II §8(f) CRA).

**Considerations.**
- Annex II §8(a) covers necessary measures during initial commissioning and throughout the lifetime of the product; §8(b) covers how changes to the product can affect the security of data; §8(c) covers how security-relevant updates can be installed; §8(d) covers secure decommissioning of the product including user data removal; §8(e) covers how the default setting enabling automatic installation of security updates can be turned off.
- Art. 13(18) extends this to a duty to provide the instructions in paper or electronic form, accessible for the support period (10-year Annex II information accessibility; cross to D-09.4).
- The Annex II §8(f) integrator information is the workforce-side partial dimension — integrators who incorporate the product into a downstream system are informed of the cybersecurity measures required to maintain Annex I compliance (B2B integrators are the closest workforce-side dimension at D-08.1).
- The chosen PR.AT-01 mapping at SR-CRA-071 anchors the workforce-side (integrator) dimension; the user-side is marked UNMAPPED_CSF per SR-CRA-071 unmapped_csf_justification (NIST CSF 2.0 PR.AT-01 trains the workforce, not the end-user; no direct CSF 2.0 Subcategory for end-user instructions on secure product use).
**CSF anchors (from `SR-CRA-071` v0.3 security_rationale):**
PR.AT-01 (with UNMAPPED_CSF on the user-side).
*(PR.AT-01 captures the workforce-side awareness function for the Annex II §8(f) integrator dimension: integrators who incorporate the product into a downstream system are informed of the cybersecurity measures required to maintain Annex I compliance, with the awareness channel being the Annex II §8(f) information deliverable. The downside — flagged in the unmapped_csf_justification — is that PR.AT-01 scopes the workforce, not the end user; the SR retains the mapping for the workforce-side (integrator) of Annex II §8(f) and marks the user-side as UNMAPPED_CSF. The Annex II §8(a)–(e) user-side instructions remain documented as the device-side analogue of workforce awareness, with the support-period accessibility of Article 13(18) ensuring the information deliverable is durable. PR.AT-01 — applied to the integrator scope — enables the manufacturer to demonstrate ex post, through the documented Annex II §8(f) integrator information, that the workforce-awareness dimension of the instructions duty has been discharged.)*

---


## Security Requirements (CRA)

#### 8.1.3 — Manufacturer-shipped detailed user-facing secure-use instructions with 10-year support-period accessibility

```yaml
- req_id: 8.1.3
  volere_section: 15
  volere_subtype: immunity

  title: "Product with digital elements accompanied by detailed user-facing secure-use instructions covering the lifetime of the product"

  derives_from:
    hso_sub_so: SO-8.1.CRA
    per_reg_so: SO-CRA-048 (partial)
    source_sr: SR-CRA-071
    hso_file: ../../HierarchicalSecurityObjectives/D-08_Human-Factors/8.1.md
    objective_ref_section: "### 8.1.3"

  description: |
    The product with digital elements shall be accompanied by detailed instructions — or an internet address referring to such detailed instructions — covering the necessary measures during initial commissioning and throughout the lifetime of the product to ensure its secure use (Annex II §8(a)–(e) CRA), and — where the product is intended for integration into other products — the information necessary for the integrator to comply with the essential cybersecurity requirements set out in Part I of Annex I and the documentation requirements set out in Annex VII (Annex II §8(f) CRA), with a duty to provide the instructions in paper or electronic form accessible for the support period under Art. 13(18).

  fit_criterion: |
    The product with digital elements is accompanied by detailed secure-use instructions under Annex II §8(a) initial-commissioning + lifetime measures, §8(b) how changes to the product affect data security, §8(c) how security-relevant updates are installed, §8(d) secure decommissioning including user-data removal, §8(e) how the default automatic-update setting can be turned off, and §8(f) — where intended for integration — the information necessary for the integrator to comply with Annex I + Annex VII; the instructions are provided in paper or electronic form and remain accessible for the support period ≥ 5 years under Art. 13(8) sentence 3 + 10-year Annex II information accessibility under Art. 13(18); the CRA participation at 8.1 is partial — Annex II §8(a)–(f) addresses the end-user audience with the product (not workforce) per AEGIS taxonomy §4.1; the workforce-side partial dimension is the Annex II §8(f) integrator information for B2B integrators who incorporate the product into a downstream system (information counterpart to a contractually-anchored SCRM commitment per SR-CRA-108 security_rationale — Annex II §8(f) integrates at the 8.2 layer); the `detailed` content threshold is harmonised-standards-pending (no OJ definition of `detailed`); the chosen reading of `Throughout the lifetime of the product` is the entire supported lifetime + 10-year update tail (per SR-CRA-071 ambiguity reading); verified by Annex II §8(a)–(f) instruction-set review + Art. 13(18) support-period accessibility audit + Annex II §8(f) integrator-information review (B2B integrators) + support-period ≥ 5 years + Annex VII §2(b) + §3 + §6 + §8 technical-documentation inspection + market surveillance authority (MSA) / ENISA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [8.2.3 (Annex II §8(f) integrator information integrates at the 8.2 role-specific layer — integrator-B2B audience)]

  nist_csf: [PR.AT-01]

  applicable_if:
    regs: [CRA]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (CRA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**CRA article (verbatim, Annex II §8(a)–(f)):**
> "The product shall be accompanied by detailed instructions and information … including: (a) the necessary measures during initial commissioning and throughout the lifetime of the product to ensure its secure use; (b) how changes to the product can affect the security of data; (c) how security-relevant updates can be installed; (d) the secure decommissioning of the product, including, where applicable, information on how user data can be securely removed; (e) how the default setting enabling the automatic installation of security updates, as required by point (c) of Part I, can be turned off; (f) where the product is intended for integration into other products, the information necessary for the integrator to comply with the essential cybersecurity requirements set out in Part I of Annex I and the documentation requirements set out in Annex VII." — CRA Annex II §8(a)–(f) (per SR-CRA-071)

**CRA article (verbatim, Annex II §8):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/CRA.md body — field `verified_relationship`

```yaml
verified_relationship: DIFFERENT-PERSPECTIVE (CRDA-deep, D-08.1: GDPR↔CRA = DIFFERENT-PERSPECTIVE (SAME — substantively scope-disjoint; workforce vs end-user audiences; no consolidation rule); NIS2↔CRA = DIFFERENT-PERSPECTIVE (SAME — substantively scope-disjoint; workforce vs end-user audiences); CRA↔DORA = DIFFERENT-PERSPECTIVE (SAME — substantively scope-disjoint; end-user instructions vs internal staff training))
```

### from regs/CRA.md body

- The CRA participation at D-08.1 is partial: Annex II §8(a)–(f) addresses the end-user audience with the product — not the manufacturer's or operator's workforce. AEGIS taxonomy §4.1 marks NIS 2 / DORA / GDPR as the authorities for full staff awareness.

### from regs/CRA.md body

- For an integrated manufacturer-controller-deployer, the CRA-side user-facing instructions are independent of the GDPR workforce awareness programme (DPO-catalysed workforce) and the NIS 2 hygiene baseline on the manufacturer workforce (substantively scope-disjoint audiences — workforce vs end-user).

### from regs/CRA.md body

- For a CRA-regulated manufacturer, the workforce awareness obligation is discharged via NIS 2 / DORA / GDPR; the parallel tracks coexist on substantively scope-disjoint audiences.


### from regs/CRA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # CRA↔GDPR = N (typically) substantively scope-disjoint (workforce vs end-user audiences); CRA↔NIS2 = N (typically) substantively scope-disjoint (workforce vs end-user); CRA↔DORA = N (typically) substantively scope-disjoint (end-user vs internal staff); HL engages only on Y-pairs (none of the CRA-involving pairs engage the workforce-side HL)

```

### from regs/CRA.md body — field `considerations`

```yaml
  considerations: |
    The CRA general-awareness obligation at 8.1 is the **product-side Annex II §8 detailed-instructions package** — user-facing (Annex II §8(a)–(e)) + integrator-facing B2B (Annex II §8(f)). The Annex II §8(a)–(e) user-side addresses the end-user with the product — not the manufacturer's or operator's workforce. The Annex II §8(f) integrator information is the **workforce-side partial dimension** — integrators who incorporate the product into a downstream system are informed of the cybersecurity measures required to maintain Annex I compliance (B2B integrators are the closest workforce-side dimension at 8.1). The CRA participation at 8.1 is partial: Annex II §8 is user-facing not workforce; AEGIS taxonomy §4.1 marks NIS 2 / DORA / GDPR as the authorities for full staff awareness. Art. 13(18) extends this to a duty to provide the instructions in paper or electronic form, accessible for the support period (10-year Annex II information accessibility; cross to 9.4). The 3 CRA-involving pairs (GDPR↔CRA, NIS2↔CRA, CRA↔DORA) are substantively scope-disjoint (workforce vs end-user audiences) — the parallel tracks coexist on different audiences with no consolidation rule; the high-level SO does NOT collapse the audience boundaries. **8.2 layer (8.2.3)** adds the role-specific depth for the integrator-B2B audience via Annex II §8(f) (integrator-facing information on threat model + configuration constraints + vulnerability-handling interface). The recipient is the end-user (B2C/user-facing) + market surveillance authority (MSA) — Annex II §8(a)–(f) instructions on the product; Annex II §8(f) integrator information discharge the workforce-side partial dimension for B2B integrators. (Copied from the HSO Considerations block of `### 8.1.3`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=CRA; demoted=6; core_cross_mentions=0 -->