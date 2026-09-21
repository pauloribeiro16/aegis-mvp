# D-06.4 — GDPR module

> Regulation-specific layer: applies when `GDPR` is in scope
> (activation: `if GDPR in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-023 | Non-EU controllers/processors falling under Art. 3(2) designate a representative in writing in the Union, subject to narrow occasional/low-risk/public-authority exceptions | Legal-address anchor for non-EU personal-data actors; DPA/data-subject-facing representative |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **GDPR** | non-EU controller/processor under Art. 3(2) | offering goods/services to EU data subjects or monitoring behaviour, unless Art. 27(2) exception applies | written Union representative designation | DPA; data subjects; representative | Art. 27(1)/(2) |

## Sub-SO (GDPR)

#### D-06.4.1 — Sub-SO for GDPR

```yaml
id: SO-D-06.4.GDPR
subdomain: D-06.4
applies_to: [GDPR]
inherits_from: SO-GDPR-023
source_SR: SR-GDPR-038
activation: if GDPR in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Non-EU controllers and processors falling under GDPR Art. 3(2) designate a representative in writing in the Union unless the Art. 27(2) exception applies; the representative is the legal-address and accountability anchor for supervisory-authority and data-subject contact.

**CSF anchors (from GDPR SR-GDPR-038):** GV.OC-02, GV.RR-02.

---


## Security Requirements (GDPR)

#### 6.4.1 — Art. 27(1)/(2) written Union representative for non-EU controllers/processors

```yaml
- req_id: 6.4.1
  volere_section: 15
  volere_subtype: audit

  title: "Art. 27(1) written Union representative designation for non-EU controllers/processors under Art. 3(2), subject to Art. 27(2) occasional / low-risk / public-authority exceptions"

  derives_from:
    hso_sub_so: SO-D-06.4.GDPR
    per_reg_so: SO-GDPR-023
    source_sr: SR-GDPR-038
    hso_file: ../../HierarchicalSecurityObjectives/D-06_Supply-Chain/D-06.4.md
    objective_ref_section: "### D-06.4.1"

  description: |
    The product shall ensure that non-EU controllers and processors falling under GDPR Art. 3(2) (offering goods/services to EU data subjects or monitoring behaviour in the Union) designate in writing a representative in the Union, subject only to the narrow Art. 27(2) occasional / low-risk / public-authority exceptions — the representative is the legal-address and accountability anchor for supervisory-authority and data-subject contact; in CRA overlap (same non-EU entity is also CRA manufacturer), the GDPR representative does NOT replace the CRA authorised representative — single legal entity may perform both roles only if both mandates and recipient channels are separately documented.

  fit_criterion: |
    An Art. 27 written-Union-representative discipline is operated per non-EU controller/processor falling under Art. 3(2) with no Art. 27(2) exception; each designated representative maintains a written mandate, a Union address, an establishment-on-Union-territory-of-business record, a designated data-subject and supervisory-authority contact function, and a documented articulation of representative obligations (Art. 30(2) RoPA reference, Art. 58(1) DPA cooperation, Art. 13/14 information-clause identification); the Art. 27(2) occasional / low-risk / public-authority exception is applied per non-EU controller/processor only with documented exception-eligibility assessment (processing occasional + low-risk + no special-category data + no large-scale systematic monitoring — typically meets all four limbs cumulatively to engage the exception; an Art. 27(2)(a)–(c) reading is rejected as insufficient, the exception requires the exceptional-low-risk threshold); the GDPR representative designation does NOT replace the CRA authorised representative — in CRA overlap, the single legal entity may perform both roles only if both mandates and recipient channels are separately documented (data-protection correspondence vs product-compliance technical-documentation/MSA cooperation); in DORA overlap (non-EU ICT provider is CIF-supporting for a financial entity and falls under Art. 3(2)), the GDPR representative address coexists with DORA contractual audit/access rights, not substitute; verified by representative designation register review + Art. 27(2) exception-eligibility assessment audit + representative written-mandate inspection + DPA inspection-ready evidence pack on request + CRA-AR-mandate separate-documentation attestation when CRA overlap (or single-entity dual-role mandate split with separately documented recipient channels).

  priority: MUST
  verification_method: TEST
  dependencies: [6.3.1 (Art. 28(3) DPA contracts coexist with Art. 27 representative; representative receives DPA-related supervisory-authority correspondence but does not perform DPA negotiation — different actor roles)]

  nist_csf: [GV.OC-02, GV.RR-02]

  applicable_if:
    regs: [GDPR]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (GDPR)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**GDPR article (verbatim, Art. 27(1)/(2)):**
> "Where Article 3(2) applies, the controller or the processor shall designate in writing a representative in the Union." — Art. 27(1) GDPR
>
> "The obligation set out in paragraph 1 shall not apply to: (a) processing which is occasional, does not include, on a large scale, processing of special categories of data as referred to in Article 9(1) or of personal data relating to criminal convictions as referred to in Article 10, and is unlikely to result in a risk to the rights and freedoms of natural persons, taking into account the nature, context, scope and purposes of the processing; or (b) a public authority or body." — Art. 27(2)(a)/(b) GDPR


## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/GDPR.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-06.4: GDPR↔NIS2 = COMPLEMENTARY; GDPR↔CRA = EQUAL (different objects); GDPR↔DORA = DIFFERENT-PERSPECTIVE)
```

### from regs/GDPR.md body

**Considerations.**

- In overlap with CRA, the GDPR representative does not replace the CRA authorised representative — one handles data-protection correspondence and one handles product-compliance technical-documentation/MSA cooperation; a single legal entity may perform both roles only if both mandates and recipient channels are separately documented.

### from regs/GDPR.md body

- In overlap with DORA, GDPR's representative address coexists with DORA contractual audit rights where the non-EU ICT provider supports critical or important functions for a financial entity.


### from regs/GDPR.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # GDPR↔NIS2 = Conditional (N in baseline because Art. 27 representative vs SPOC routing are distinct mechanisms; Y when non-EU controller operates across multiple MS and an incident route crosses borders); GDPR↔CRA = Y (same non-EU entity can be both GDPR controller/processor and CRA manufacturer; two written EU-side representatives or mandates coexist with single-entity dual-role requiring separately documented mandates and recipient channels); GDPR↔DORA = Conditional (N in baseline because Art. 27 representative vs DORA Art. 30(3)(e) audit-rights are distinct mechanisms; Y when non-EU ICT provider is critical/important for financial entity and falls under Art. 3(2))

```

### from regs/GDPR.md body — field `considerations`

```yaml
  considerations: |
    The GDPR third-party-boundary obligation is the Art. 27(1) written Union representative designation for non-EU controllers/processors falling under Art. 3(2), subject to Art. 27(2) exception; the operational substrate is a representative designation register with written mandates per non-EU entity, an exception-eligibility assessment discipline for Art. 27(2), and a recipient-channel separation when the same entity also has CRA / DORA boundary roles. The representative's scope-of-authority is the Art. 30(2) RoPA / Art. 58(1) DPA cooperation / Art. 13/14 information-clause identification fields — the representative is the legal-address anchor, NOT a delegate of data-protection responsibility (controller/processor remain legally accountable). The Art. 27(2) exception is narrow: occasional + low-risk + no special-category + no large-scale systematic monitoring all required cumulatively; the exception does not apply to public-authority or large-scale processing and is rejected as reading-route that would self-apply the exception. In CRA overlap, the GDPR representative does NOT replace the CRA authorised representative — one handles data-protection correspondence (DPA, data subjects) and the other handles product-compliance technical-documentation/MSA cooperation; a single legal entity may perform both roles only if both mandates and recipient channels are separately documented; otherwise two representatives or two mandates coexist. In DORA overlap, the GDPR representative address coexists with DORA contractual audit/access rights, NOT substitute — the CORRECTED CRDA pair is N/A in D-06.4 (no corrected pairs in this sub-domain) but role-and-recipient allocation governs. (Copied from the HSO Considerations block of `### D-06.4.1`; preserved here for self-containment per Volere shell `considerations` field definition.)
```

### from regs/GDPR.md body

**GDPR article (verbatim, Art. 27(1)):**

> (See GDPR↔CRA pair above for the verbatim text.)

<!-- aegis:purity: own_reg=GDPR; demoted=6; core_cross_mentions=2 -->

