# D-06.4 — CRA module

> Regulation-specific layer: applies when `CRA` is in scope
> (activation: `if CRA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| CRA | SO-CRA-041; SO-CRA-042; SO-CRA-043; SO-CRA-044 | Non-EU manufacturer authorised representative; importer/distributor manufacturer-equivalent trigger; third-party substantial-modification trigger; economic-operator identification and 10-year retention | Product-compliance boundary; MSA-facing authorised representative and supply-chain traceability |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **CRA** | non-EU manufacturer, importer/distributor/modifier, and economic-operator chain | written AR mandate; own-name placement; substantial modification; MSA reasoned request | authorised representative mandate; manufacturer-equivalent status; substantial-modification record; 10-year identification log | MSA; manufacturer; economic operators | Art. 18; Art. 21; Art. 22; Art. 23 |

## Sub-SO (CRA)

#### D-06.4.3 — Sub-SO for CRA

```yaml
id: SO-D-06.4.CRA
subdomain: D-06.4
applies_to: [CRA]
inherits_from: [SO-CRA-041, SO-CRA-042, SO-CRA-043, SO-CRA-044]
source_SR: [SR-CRA-059, SR-CRA-060, SR-CRA-061, SR-CRA-062, SR-CRA-063]
activation: if CRA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** CRA third-party boundary management preserves product-compliance accountability across EU/non-EU and supply-chain actor boundaries: a non-EU manufacturer may appoint an authorised representative by written mandate, but core manufacturer obligations remain non-delegable; an importer or distributor that places a product under its own name/trademark or substantially modifies it becomes manufacturer-equivalent; a third party that substantially modifies a product becomes the manufacturer for the affected part (or the entire product if the modification affects the whole product's cybersecurity); economic operators maintain upstream/downstream identification records and provide them to MSAs on reasoned request, retaining the supply-chain information for 10 years.

**CSF anchors (from CRA SRs):** GV.RR-02, GV.SC-03, GV.SC-04, GV.OC-03, GV.SC-02.

---


## Security Requirements (CRA)

#### 6.4.3 — Art. 18 authorised representative + Art. 21 manufacturer-equivalent + Art. 22 substantial-modification + Art. 23 10-year economic-operator identification

```yaml
- req_id: 6.4.3
  volere_section: 15
  volere_subtype: audit

  title: "Art. 18 written authorised representative mandate + Art. 21 own-name/trademark manufacturer-equivalent + Art. 22 third-party substantial-modification manufacturer-status + Art. 23 10-year upstream/downstream economic-operator identification log"

  derives_from:
    hso_sub_so: SO-D-06.4.CRA
    per_reg_so: SO-CRA-041, SO-CRA-042, SO-CRA-043, SO-CRA-044
    source_sr: SR-CRA-059, SR-CRA-060, SR-CRA-061, SR-CRA-062, SR-CRA-063
    hso_file: ../../HierarchicalSecurityObjectives/D-06_Supply-Chain/D-06.4.md
    objective_ref_section: "### D-06.4.3"

  description: |
    The product shall preserve CRA product-compliance accountability across EU/non-EU and supply-chain actor boundaries — Art. 18 written authorised representative mandate (non-EU manufacturer may appoint AR in writing, with non-delegable manufacturer obligations remaining on the manufacturer; single-entity may also be GDPR Art. 27 representative only with separately documented mandates and recipient channels); Art. 21 own-name/trademark manufacturer-equivalent trigger (importer or distributor placing a product under own name/trademark, or modifying it in a way that may affect compliance with the CRA, becomes manufacturer-equivalent); Art. 22 substantial-modification rule (third party that substantially modifies a product becomes the manufacturer for the affected part, or for the entire product if the modification affects the whole product's cybersecurity); Art. 23 10-year upstream/downstream economic-operator identification log (economic operators maintain identification records and provide them to MSAs on reasoned request, retaining supply-chain information for 10 years) — CRA AR mandate is NOT a GDPR Art. 27 representative or a DORA Art. 30(3)(e) audit-right.

  fit_criterion: |
    A CRA economic-operator boundary matrix is maintained per non-EU manufacturer / importer / distributor / substantial-modifier with explicit boundary-mechanism separation: Art. 18 authorised representative mandate is documented per non-EU manufacturer with written mandate text, AR establishment-on-Union-territory record, AR delegation-by-manufacturer scope (NOT core manufacturer obligations), AR obligation-set (Art. 30 RoPA leg + Annex VII technical-documentation access + MSA cooperation on reasoned request); Art. 21 own-name/trademark manufacturer-equivalent trigger is operated as an own-name-placement event log + intended-purpose-modification assessment + manufacturer-equivalent-status register per importer or distributor; Art. 22 substantial-modification rule is operated as a substantial-modification event log with criterion criteria (consequence-not-considered-in-initial-assessment + obliges-the-manufacturer-to-ensure-the-product-remains-compliant-with-CRA + may-affect-the-whole-product-cybersecurity) per substantial modifier, with affected-part OR entire-product manufacturer-status designation per substantial-modification scope; Art. 23 10-year upstream/downstream economic-operator identification log is maintained with economic-operator records (name, contact, role, identification details, supply-chain position) and is provided to MSAs on reasoned request with 10-year retention; non-delegable manufacturer obligations (per Art. 18 carve-out in the AR-mandate standard text — typically conformance-assessment responsibilities, technical-documentation-keeping, incident-handling under Art. 14, vulnerability-handling under Art. 13) remain on the manufacturer regardless of AR mandate; the CRA AR does NOT replace the GDPR Art. 27 representative — one handles data-protection correspondence (DPA, data subjects) and one handles product-compliance technical-documentation/MSA cooperation; the CRA AR does NOT replace the DORA CIF audit-rights — CRA is upstream traceability; DORA is downstream audit; verified by AR-mandate register review + own-name-placement event log audit + substantial-modification event log audit + 10-year economic-operator identification log spot-check + non-delegable-obligations retention attestation + MSA inspection-ready evidence pack on request + GDPR-DPA-recipient separation attestation when AR-and-GDPR-representative dual-role.

  priority: MUST
  verification_method: TEST
  dependencies: [6.3.3 (economic-operator compliance matrix provides Art. 19/20 + Art. 13(6) records that feed Art. 21/22/23 boundary operations), 6.1.3 (third-party-component due diligence shapes component-vulnerability inputs to substantial-modification assessments; OSS stewardship assessment is part of the substantial-modification analysis), 6.4.1 (single-entity dual-role handling — AR can be GDPR Art. 27 representative ONLY with separately documented mandates and recipient channels)]

  nist_csf: [GV.RR-02, GV.SC-03]

  applicable_if:
    regs: [CRA]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (CRA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**CRA article (verbatim, Art. 18(1)–(3)):**
> "A manufacturer established outside the Union may, by written mandate, appoint an authorised representative established in the Union to perform specified tasks on behalf of the manufacturer." — CRA Art. 18(1)
>
> "The mandate of the authorised representative shall not cover the obligations laid down in Article 13(1) to (11), Article 13(12) first subparagraph, point (a), and Article 13(14)." — CRA Art. 18(2)
>
> "The authorised representative shall perform the tasks specified in the mandate. The mandate shall allow the authorised representative to perform at least the following tasks: (a) keeping a copy of the EU declaration of conformity and the technical documentation at the disposal of the market surveillance authorities for the period referred to in Article 13(13); (b) providing the market surveillance authorities, on reasoned request, with all the information and documentation necessary to demonstrate the conformity of a product with digital elements with the essential cybersecurity requirements set out in Annex I; (c) cooperating with the market surveillance authorities, at their request, on any action taken to address non-compliance with the essential cybersecurity requirements set out in Annex I presented by a product with digital elements covered by the mandate of the authorised representative." — CRA Art. 18(3)

**CRA article (verbatim, Art. 22(1)/(2) + Art. 23(1)/(2)):**
> "A natural or legal person, other than the manufacturer, the importer or the distributor, that carries out a substantial modification of a product with digital elements and makes that product available on the market shall be considered to be the manufacturer for the purposes of this Regulation." — CRA Art. 22(1)
>
> "The manufacturer obligations referred to in paragraph 1 shall apply to the affected part of the product with digital elements or, where the substantial modification has an impact on the cybersecurity of the product with digital elements as a whole, to the entire product with digital elements." — CRA Art. 22(2)
>
> "Economic operators shall, on a reasoned request from a market surveillance authority, identify: (a) any economic operator that has supplied them with a product with digital elements; (b) any economic operator to which they have supplied a product with digital elements." — CRA Art. 23(1)
>
> "Economic operators shall keep the information referred to in paragraph 1 for a period of 10 years after they have been supplied with the product with digital elements and after they have supplied the product with digital elements." — CRA Art. 23(2)


## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/CRA.md body — field `verified_relationship`

```yaml
verified_relationship: DIFFERENT-PERSPECTIVE (CRDA-deep, D-06.4: GDPR↔CRA = EQUAL (different objects); NIS2↔CRA = DIFFERENT-PERSPECTIVE; CRA↔DORA = DIFFERENT-PERSPECTIVE)
```

### from regs/CRA.md body

**Considerations.**

- In overlap with GDPR, the CRA authorised representative does not replace the GDPR Union representative — the two mandates differ (data-protection correspondence vs product-compliance technical-documentation/MSA cooperation) and must be documented separately.

### from regs/CRA.md body

- In overlap with DORA, economic-operator identification and DORA CIF audit rights point in different directions but compose where a CRA-classified product is supplied to a financial entity through an economic-operator chain.


### from regs/CRA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # CRA↔GDPR = Y (same non-EU entity; data-protection representative and product-compliance AR coexist with single-entity dual-role requiring separate documentation); CRA↔NIS2 = Conditional (N in baseline because substantial-modification manufacturer-status and economic-operator identification vs direct-supplier scope are distinct mechanisms; Y when NIS 2 entity deploys CRA product substantially modified by third party); CRA↔DORA = Conditional (N in baseline because economic-operator identification vs financial-entity audit-rights are distinct mechanisms; Y when CRA product is supplied to financial entity through economic-operator chain)

```

### from regs/CRA.md body — field `considerations`

```yaml
  considerations: |
    The CRA third-party-boundary obligation is the product-compliance accountability structure across EU/non-EU and supply-chain actor boundaries, materialised as four boundary mechanisms: Art. 18 AR mandate + Art. 21 manufacturer-equivalent + Art. 22 substantial-modification + Art. 23 10-year economic-operator identification log; the operational substrate is the CRA economic-operator boundary matrix keyed by EU/non-EU status / actor role (manufacturer / importer / distributor / substantial-modifier) / modification status / supply-chain position. The non-delegable-manufacturer-obligations carve-out (per Art. 18 AR-mandate standard text) is the boundary-protection layer that prevents the AR from becoming a de-facto manufacturer — the AR is technical-documentation custodian and MSA cooperation anchor, NOT a replacement for the manufacturer. The substantial-modification rule (Art. 22) has a non-trivial criterion set — consequence-not-considered-in-initial-assessment + obliges-the-manufacturer-to-ensure-the-product-remains-compliant-with-CRA + may-affect-the-whole-product-cybersecurity (typically all three criteria cumulatively to engage the substantial-modification manufacturer-status trigger); the third-party substantial modifier becomes manufacturer-equivalent for the affected part OR the entire product if the modification scope reaches the whole product's cybersecurity. The 10-year retention (Art. 23) applies to upstream/downstream economic-operator identification records; the log is provided on MSA reasoned request. The CRA AR does NOT replace the GDPR Art. 27 representative (different objects / different recipient channels); a single legal entity may perform both roles only with separately documented mandates. The CRA economic-operator identification does NOT replace DORA CIF audit-rights (different direction — upstream traceability vs downstream audit). (Copied from the HSO Considerations block of `### D-06.4.3`; preserved here for self-containment per Volere shell `considerations` field definition.)
```

### from regs/CRA.md body

**CRA article (verbatim, Art. 23(1)/(2)):**

> (See NIS2↔CRA pair above for the verbatim text.)

<!-- aegis:purity: own_reg=CRA; demoted=6; core_cross_mentions=3 -->
