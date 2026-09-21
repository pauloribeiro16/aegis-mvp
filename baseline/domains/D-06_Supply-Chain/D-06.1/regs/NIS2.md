# D-06.1 — NIS 2 module

> Regulation-specific layer: applies when `NIS2` is in scope
> (activation: `if NIS2 in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| NIS2 | SO-NIS2-014 | Supply chain security is managed across direct supplier and service-provider relationships, including security-related aspects of those relationships (Art. 21(2)(d) + Art. 21(1) chapeau) | Entity supplier relationships; `direct` scope-limiter (Tier-1 + operationally-dependent sub-tier scope is calibrated by Member State transposition); continuous risk-management; GV.SC-02 + ID.AM-04 + GV.OC-03 |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **NIS2** | direct supplier / service provider as relationship (entity-level supplier list) | continuous supply-chain security (Art. 21(2)(d)) + per-supplier assessment three-prong (Art. 21(3) sentence 1: vulnerabilities + quality + secure-development procedures) + EU-level coordinated risk propagation (Art. 21(3) sentence 2 → Art. 22) | `appropriate and proportionate` (Art. 21(1) chapeau) + `direct` scope-limiter (Art. 21(2)(d)) + state-of-the-art (Art. 21(1) sentence 2) | CSIRT or competent authority | Art. 21(1) chapeau + Art. 21(2)(d) + Art. 21(3) sentence 1 + Art. 22 + Art. 21(1) sentence 2 state-of-the-art |

## Sub-SO (NIS 2)

#### D-06.1.2 — Sub-SO for NIS 2

```yaml
id: SO-D-06.1.NIS2
subdomain: D-06.1
applies_to: [NIS2]
inherits_from: SO-NIS2-014
source_SR: SR-NIS2-020
activation: if NIS2 in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Essential and important entities take appropriate and proportionate technical, operational and organisational measures across direct supplier and service-provider relationships, including security-related aspects of those relationships (Art. 21(2)(d)), taking into account state of the art (Art. 21(1) sentence 2) and the risks posed to the security of network and information systems; the Art. 21(3) sentence 1 three-prong supplier assessment (supplier-specific vulnerabilities + overall quality of products and cybersecurity practices + supplier secure-development procedures) is performed per direct supplier, with EU-level coordinated risk-propagation inputs (Art. 21(3) sentence 2 → Art. 22) taken into account where available.

**Considerations.**
- The `direct` scope-limiter is POLY-S3 with three materially distinct readings per SR-NIS2-020: R1 (Tier-1 strict), R2 (Tier-1 + technically integrated), R3 (Tier-1 + operationally dependent). Chosen reading is R2 (risk-management-precaution principle — technical integration is the primary attack-surface handle on supply-chain risk).
**CSF anchors (from `SR-NIS2-020` v0.3 security_rationale):**
GV.SC-02, ID.AM-04, GV.OC-03.
*(GV.SC-02 anchors the supplier-prioritisation dimension — direct
suppliers are prioritised by criticality (the R1/R2/R3 `direct`
reading determines which suppliers are within the prioritisation
scope). ID.AM-04 anchors the resource-prioritised dimension —
resources (here: NIS dependencies on direct suppliers) are
prioritised based on classification (the criticality of the
service, process, or function to the entity's mission). GV.OC-03
anchors the legal/regulatory/contractual-understanding dimension —
legal, regulatory, and contractual requirements regarding
cybersecurity (including supply-chain) are understood and managed.
The three subcategories together enable the essential / important
entity to demonstrate ex post, through documented supplier-risk
register, per-supplier vulnerability-intelligence records, and
Member-State-transposition-supplied proportionality decisions, that
the Art. 21(2)(d) direct-supplier security duty has been exercised
across the `direct` scope and the Art. 21(3) three-prong supplier
assessment has been documented for each direct supplier.)*

---


## Security Requirements (NIS 2)

#### 6.1.2 — Direct-supplier-as-relationship security with `appropriate and proportionate` chapeau and Art. 21(3) three-prong assessment

```yaml
- req_id: 6.1.2
  volere_section: 15
  volere_subtype: immunity

  title: "Direct-supplier-as-relationship security with Art. 21(2)(d) `direct` scope-limiter, Art. 21(1) `appropriate and proportionate` chapeau, and Art. 21(3) three-prong supplier assessment"

  derives_from:
    hso_sub_so: SO-6.1.NIS2
    per_reg_so: SO-NIS2-014
    source_sr: SR-NIS2-020, SR-NIS2-021
    hso_file: ../../HierarchicalSecurityObjectives/D-06_Supply-Chain/6.1.md
    objective_ref_section: "### 6.1.2"

  description: |
    The product shall operate direct-supplier-as-relationship security covering security-related aspects concerning the relationships between each entity and its direct suppliers or service providers (Art. 21(2)(d) `direct` scope-limiter, with the chosen reading R1 Tier-1 contractual as the minimum + R2 technically integrated + R3 operationally dependent per Recital 56), calibrated to state of the art (Art. 21(1) sentence 2) and the risks posed, with the Art. 21(3) sentence 1 three-prong supplier assessment performed per direct supplier — supplier-specific vulnerabilities (vulnerabilities specific to each direct supplier per SR-NIS2-022) + overall quality of products and cybersecurity practices + supplier secure-development procedures — and EU-level coordinated risk-assessment inputs (Art. 21(3) sentence 2 → Art. 22 Cooperation Group) taken into account where available (NIS 2 Art. 21(2)(d) + Art. 21(1) chapeau + Art. 21(3) sentence 1 three-prong + Art. 21(1) sentence 2 state-of-the-art + Recital 56).

  fit_criterion: |
    A direct-supplier-risk-management discipline is operated covering each in-scope direct supplier via GV.SC-02 supplier register and prioritisation methodology (with R1 Tier-1 contractual as the minimum `direct` scope + R2 technical-integration + R3 operationally-dependent per Recital 56 risk-management-precaution principle); the Art. 21(3) three-prong supplier assessment is performed per direct supplier covering (a) supplier-specific vulnerabilities via ID.RA-01 vulnerabilities-identified leg + ID.RA-02 threat-intelligence-collected leg (CVE feeds, vendor advisories, sectoral CSIRT notifications, threat-intelligence subscriptions) + ID.AM-04 supplier-inventory substrate, (b) overall quality of products and cybersecurity practices via GV.SC-04 audits/test-results/certifications leg (chosen R4 composite reading of `overall quality` per SR-NIS2-022 ambiguity_notes), (c) supplier secure-development procedures via the externally-assessable interpretation (questionnaire / contract clause / third-party attestation) per SR-NIS2-023; the Art. 21(1) `appropriate and proportionate` chapeau and Art. 21(1) sentence 2 state-of-the-art qualifier calibrate the assessment depth to risk profile and cost; the Art. 21(3) sentence 2 EU-level coordinated risk-assessment inputs (Cooperation Group + Commission + ENISA under Art. 22(1)) are taken into account in supplier-risk decisions; the direct-supplier-as-relationship security discipline operates at the entity-level supplier boundary only, with the tier hand-off to processor-tier (GDPR leg), component-tier (CRA leg), and ICT-provider-tier (DORA leg) documented as the controlled interfaces; verified by supplier-register audit + Art. 21(3) three-prong per-supplier assessment records inspection + GV.SC-04 audit/test-result records review + ID.RA-02 threat-intelligence-feed evidence review + Art. 22 EU-level coordinated-assessment inputs integration review + CSIRT-or-competent-authority inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [6.1.1 (when controller-NSIE combined — processor-tier feeds supplier-tier for data-processing supplier), 6.1.3 (when NIS 2 entity deploys/manufactures CRA product — supplier-tier on manufacturer stacks with component-tier), 6.1.4 (when financial entity = NIS 2 essential entity — DORA Art. 28(1) satisfies NIS 2 ICT-hazard subset; NIS 2 chapeau extends to physical + operational hazards via lex specialis analysis)]

  nist_csf: [GV.SC-02, GV.SC-03, GV.SC-04, ID.AM-04, ID.RA-01, ID.RA-02]

  applicable_if:
    regs: [NIS2]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (NIS 2)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**NIS 2 article (verbatim, Art. 21(2)(d)):**
> "Member States shall ensure that essential and important entities take appropriate and proportionate technical, operational and organisational measures to manage the risks posed to the security of network and information systems which those entities use for their activities or for the provision of their services, and to prevent or minimise the impact of incidents on recipients of their services and on other services. Taking into account the state of the art … those measures shall include, in particular … supply chain security including security-related aspects concerning the relationships between each entity and its direct suppliers or service providers." — NIS 2 Art. 21(1) + Art. 21(2)(d)

**NIS 2 article (verbatim, Art. 21(2)(d)):**
> "… supply chain security including security-related aspects concerning the relationships between each entity and its direct suppliers or service providers." — NIS 2 Art. 21(2)(d)

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/NIS2.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-06.1: GDPR↔NIS2 = COMPLEMENTARY (SAME — sharper-qualitative-on-shared-risk-substrate); NIS2↔CRA = DIFFERENT-PERSPECTIVE (SAME — entity-level supplier vs product-level component); NIS2↔DORA = EQUAL (SAME — DORA exceeds NIS 2, four-factor operationalises `appropriate and proportionate` chapeau with sharper factors; DORA satisfies NIS 2 in the financial-services subset))
```

### from regs/NIS2.md body

- DORA Art. 28(1) four-factor proportionality operationalises the NIS 2 `appropriate and proportionate` chapeau with explicit factors in the financial-services subset; a financial entity implementing DORA exceeds NIS 2's supply-chain-security requirement.

### from regs/NIS2.md body

- NIS 2 ↔ CRA = DIFFERENT-PERSPECTIVE: entity-level supplier (NIS 2) vs product-level component (CRA); the lists overlap when the deployer is the entity AND the manufacturer supplies a CRA-compliant product — the deployer does NIS 2-level supplier due diligence on the manufacturer (entity-to-entity), while the manufacturer does CRA-level component due diligence on its third-party components (product-internal).


### from regs/NIS2.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # NIS2↔GDPR = Conditional (Y controller-NSIE); NIS2↔CRA = Conditional (Y NIS 2 entity deploys/manufactures CRA product; disjoint baseline: supplier-relationship ↔ product-component); NIS2↔DORA = Conditional (Y cross-sector; N pure-financial via lex specialis — DORA Art. 28(1) four-factor operationalises NIS 2 chapeau with sharper factors; NIS 2 chapeau extends to physical + operational hazards); HL engages on overlap

```

### from regs/NIS2.md body — field `considerations`

```yaml
  considerations: |
    The NIS 2 vendor-risk-assessment obligation is the direct-supplier-as-relationship security covering security-related aspects of supplier relationships; the operational substrate is a direct-supplier-risk-management discipline anchored on the Art. 21(2)(d) `direct` scope-limiter, the Art. 21(1) `appropriate and proportionate` chapeau, and the Art. 21(3) sentence 1 three-prong supplier assessment (vulnerabilities + quality + secure-development procedures, all three required per COORD-S2 across three AND-coordinated limbs per SR-NIS2-022 + SR-DORA-019 Propagated). The `direct` scope-limiter is the single most consequential SCOPE-Q S3 in Chapter IV — three materially distinct readings: R1 contractually bound Tier-1, R2 technically integrated, R3 operationally dependent SPOF; chosen reading is R1 as the minimum + R2/R3 per Recital 56. Member State transposition divergence may apply (German BSI favours R1+R3; French ANSSI favours R2+R3; both may signal forthcoming n-hop obligations in critical sectors). DORA Art. 28(1) four-factor proportionality operationalises the NIS 2 `appropriate and proportionate` chapeau with explicit factors (nature, scale, complexity, importance) in the financial-services subset; a financial entity implementing DORA exceeds NIS 2's supply-chain-security requirement. The direct-supplier-as-relationship target object is distinct from the GDPR processor-as-legal-entity, the CRA third-party-component-as-technical-artefact, and the DORA ICT-third-party-as-financial-entity-counterparty — the four target objects are layered not collapsed. For a NIS 2 essential entity that is not a financial entity, the NIS 2 chapeau applies with Member-State-transposition-supplied detail on the proportionality calibration; for a financial entity that is also a NIS 2 essential entity, the DORA four-factor test discharges the NIS 2 chapeau in the supply-chain-security dimension. (Copied from the HSO Considerations block of `### 6.1.2`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=NIS2; demoted=5; core_cross_mentions=2 -->

