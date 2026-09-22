# D-06.4 — NIS 2 module

> Regulation-specific layer: applies when `NIS2` is in scope
> (activation: `if NIS2 in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| NIS2 | SO-NIS2-012; SO-NIS2-014 (partial); SO-NIS2-016 (partial) | Cross-MS notification routing through CSIRTs/competent authorities/SPOCs/ENISA; direct-supplier scope-limiter and EU-level supply-chain-risk propagation provide entity-boundary hooks | Entity-level boundary and cross-border information flow; Member-State-transposition-sensitive |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **NIS2** | cross-border incident flow and direct supplier/service-provider boundary | significant incident with two or more affected Member States; direct supplier/service-provider relationship | SPOC forwarding; CSIRT/competent-authority routing; supplier-scope register | SPOC; ENISA; affected Member States; CSIRT/competent authority | Art. 23(6); Art. 23(8); Art. 21(2)(d) |

## Sub-SO (NIS 2)

#### D-06.4.2 — Sub-SO for NIS 2

```yaml
id: SO-D-06.4.NIS2
subdomain: D-06.4
applies_to: [NIS2]
inherits_from: [SO-NIS2-012, SO-NIS2-014, SO-NIS2-016]
source_SR: [SR-NIS2-018, SR-NIS2-020, SR-NIS2-025]
activation: if NIS2 in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** NIS 2 boundary management is split across cross-border notification routing and entity-side supplier-scope control: for incidents affecting two or more Member States, CSIRTs, competent authorities, and SPOCs route information to other affected Member States and ENISA; for supply-chain boundaries, the Art. 21(2)(d) `direct` supplier/service-provider scope-limiter defines which third parties sit inside the entity's NIS 2 supplier-security perimeter, and Art. 22 coordinated supply-chain risk-assessment outputs feed into supplier decisions where available.

**CSF anchors (from NIS 2 SRs):** RS.MA-04, GV.SC-05, GV.SC-02, GV.SC-03, ID.RA-02.

---


## Security Requirements (NIS 2)

#### 6.4.2 — Art. 23(6)/(8) cross-MS notification routing + Art. 21(2)(d) `direct` supplier/service-provider scope boundary

```yaml
- req_id: 6.4.2
  volere_section: 15
  volere_subtype: audit

  title: "Art. 23(6)/(8) cross-MS SPOC / CSIRT / ENISA notification routing + Art. 21(2)(d) `direct` supplier/service-provider scope register + Art. 22 coordinated supply-chain risk-assessment ingestion"

  derives_from:
    hso_sub_so: SO-D-06.4.NIS2
    per_reg_so: SO-NIS2-012, SO-NIS2-014, SO-NIS2-016
    source_sr: SR-NIS2-018, SR-NIS2-020, SR-NIS2-025
    hso_file: ../../HierarchicalSecurityObjectives/D-06_Supply-Chain/D-06.4.md
    objective_ref_section: "### D-06.4.2"

  description: |
    The product shall split NIS 2 third-party boundary management across two boundary mechanisms — (a) cross-border incident-flow routing for significant incidents affecting two or more Member States per Art. 23(6) (SPOC designation, CSIRT/competent-authority routing, notification to other affected Member States and ENISA where appropriate) and Art. 23(8) (single-window notification and cooperation); and (b) entity-level direct-supplier/service-provider boundary under Art. 21(2)(d) `direct` scope-limiter (with R1 Tier-1 contractual as minimum + R2 technically integrated + R3 operationally dependent per Recital 56), with Art. 22 EU-level coordinated supply-chain risk-assessment outputs ingested where available — NIS 2 `direct` scope determines entity liability; DORA CIF audit rights (Art. 30(3)(e)) extend the boundary layer for financial entities.

  fit_criterion: |
    A two-track NIS 2 boundary matrix is maintained with explicit separation of (Track-1) cross-MS routing and (Track-2) direct-supplier-scope register: Track-1 cross-MS routing covers each significant incident affecting 2+ Member States via SPOC designation per Art. 23(6)/(8), CSIRT-and-competent-authority notification forwarding, ENISA notification where Art. 23(8)(b) cooperation framework applies, and recorded affected-MS notification routing with timestamps; Track-2 direct-supplier scope covers each in-scope direct supplier / service-provider under Art. 21(2)(d) `direct` scope-limiter with R1 Tier-1 contractual as minimum + R2 technically integrated + R3 operationally dependent per Recital 56 risk-management-precaution principle (the THREE materially distinct readings R1/R2/R3 are PRESERVED with R1 as minimum + R2/R3 added per Recital 56; Member-State-transposition divergence: German BSI favours R1+R3, French ANSSI favours R2+R3, both may signal forthcoming n-hop obligations in critical sectors), with Art. 22 coordinated supply-chain risk-assessment outputs (Cooperation Group + Commission + ENISA under Art. 22(1)) ingested in supplier-scope decisions; the two tracks feed the cross-domain D-06.3 supplier-contract matrix (Art. 21(2)(d) supplier contracts) and the cross-domain risk-assessment record; in DORA overlap, DORA Art. 30(3)(e) CIF audit-rights extend the boundary layer for financial entities beyond the direct-supplier floor (DORA-exceeds-NIS 2 in audit-rights depth); in CRA overlap, CRA Art. 22 substantial-modification and Art. 23 economic-operator identification operate at distinct boundaries (CRA determines manufacturer-status; NIS 2 determines entity supplier liability); verified by SPOC routing log review + CSIRT-and-competent-authority notification forwarding record audit + cross-MS routing timestamps inspection + direct-supplier-scope register audit + Art. 22 EU-level coordinated-assessment inputs integration evidence + CSIRT-or-competent-authority inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [6.1.2 (vendor-risk-assessment four-tier discipline provides tier-1 supplier-register input to direct-supplier-scope register), 6.3.2 (Art. 21(2)(d) supplier contracts materialise the direct-supplier-scope register boundary decisions into contractual instruments)]

  nist_csf: [RS.MA-04, GV.SC-05]

  applicable_if:
    regs: [NIS2]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (NIS 2)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**NIS 2 article (verbatim, Art. 23(6) + Art. 23(8)):**
> "The competent authorities or the CSIRTs shall inform the other affected Member States and ENISA about the incident. The competent authorities or the CSIRTs shall, in accordance with Union or national law, provide the relevant information to the recipients of the services of the entity concerned." — NIS 2 Art. 23(6)
>
> "Single points of contact shall forward the notifications referred to in this Article to the single points of contact of other affected Member States and to ENISA." — NIS 2 Art. 23(8)

**NIS 2 article (verbatim, Art. 21(2)(d)):**
> "… supply chain security including security-related aspects concerning the relationships between each entity and its direct suppliers or service providers." — NIS 2 Art. 21(2)(d)

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/NIS2.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-06.4: GDPR↔NIS2 = COMPLEMENTARY; NIS2↔CRA = DIFFERENT-PERSPECTIVE; NIS2↔DORA = COMPLEMENTARY with DORA exceeding NIS 2 in audit-rights depth)
```

### from regs/NIS2.md body

**Considerations.**

- In overlap with DORA, DORA audit rights add a deeper CIF-provider verification layer; they do not erase NIS 2's direct-supplier scope record.

### from regs/NIS2.md body

- In overlap with CRA, NIS 2 `direct` supplier scope determines who the entity is liable for; CRA Art. 22/23 determines who becomes the manufacturer after substantial modification and who must identify upstream/downstream economic operators — the two regimes operate at different boundaries.


### from regs/NIS2.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # NIS2↔GDPR = Conditional (N in baseline because SPOC routing vs Art. 27 representative are distinct mechanisms; Y when non-EU controller operates across multiple MS and an incident route crosses borders); NIS2↔CRA = Conditional (N in baseline because direct-supplier scope vs Art. 22 substantial-modification / Art. 23 economic-operator identification are distinct boundary mechanisms; Y when NIS 2 entity deploys CRA product substantially modified by third party); NIS2↔DORA = Y (DORA-exceeds-NIS 2 in audit-rights depth; financial entity is also NIS 2 entity; DORA CIF audit-rights extend beyond direct-supplier floor)

```

### from regs/NIS2.md body — field `considerations`

```yaml
  considerations: |
    The NIS 2 third-party-boundary obligation is split across two boundary mechanisms — Track-1 cross-MS notification routing (Art. 23(6)/(8)) and Track-2 direct-supplier-scope register (Art. 21(2)(d) + Art. 22 coordinated-assessment ingestion); the operational substrate is the two-track NIS 2 boundary matrix keyed by incident-routing scope / supplier-role / CIF overlap / CRA-product deployment. The `direct` scope-limiter is the single most consequential scope ambiguity in Chapter IV — three materially distinct readings (R1 contractually bound Tier-1, R2 technically integrated, R3 operationally dependent SPOF); CRDA-deep preserves the SAME taxonomy label because the obligations layer within the same supply-chain sub-domain, with R1 as the minimum + R2/R3 per Recital 56; Member-State-transposition divergence may apply. In DORA overlap, DORA CIF audit/access rights extend beyond the direct-supplier floor (DORA-exceeds-NIS 2 in audit-rights depth); the financial entity is also NIS 2 entity and DORA provides the sharper audit-rights layer without erasing the NIS 2 direct-supplier scope record. In CRA overlap, NIS 2 `direct` supplier scope determines who the entity is liable for, while CRA Art. 22 substantial-modification / Art. 23 economic-operator identification determines manufacturer-status and upstream/downstream traceability — the two regimes operate at different boundaries (NIS 2=entity-side liability scope; CRA=product-side traceability scope). The two NIS 2 boundary tracks feed cross-domain Phase 1C Doc 07 (contractual-security matrix for Track-2 + incident-routing governance for Track-1). (Copied from the HSO Considerations block of `### D-06.4.2`; preserved here for self-containment per Volere shell `considerations` field definition.)
```

<!-- aegis:purity: own_reg=NIS2; demoted=5; core_cross_mentions=2 -->
