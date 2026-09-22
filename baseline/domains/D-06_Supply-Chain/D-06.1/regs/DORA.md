# D-06.1 — DORA module

> Regulation-specific layer: applies when `DORA` is in scope
> (activation: `if DORA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| DORA | SG-DORA-011 | ICT third-party risk is managed taking into account the nature, scale, complexity and importance of ICT-related dependencies and the risks arising from contractual arrangements on the use of ICT services (Art. 28(1) four-factor AND); contractual arrangements comply with appropriate information security standards; for critical or important functions (CIF), the most up-to-date and highest quality information security standards are used (Art. 28(5) escalator) | Financial entity ICT third-party; multi-factor proportionality; `critical or important functions` undefined distinction (POLY-S2 across 18 clauses); continuous risk-management; GV.SC-02 + ID.AM-04 |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **DORA** | ICT third-party service provider as financial-entity counterparty (broader than GDPR's processor) | continuous ICT third-party risk management (Art. 28(1)) + contractual arrangement entry (Art. 28(5) standards compliance) + concentration-risk identification (Art. 28(4) on the critical-ICT third-party register under Art. 28(4) → Art. 29 designation) | Art. 28(1) four-factor proportionality — nature, scale, complexity, importance — explicit AND + service / process / function criticality + Art. 28(5) CIF escalator (`most up-to-date and highest quality information security standards`) + Art. 30(2) 9-element closed contract list (a)–(i) | competent authority (national financial supervisory authority) — Art. 28 proportionality record + Art. 30(2) contract + Art. 28(5) standards compliance for CIFs | Art. 28(1) + Art. 28(4) concentration + Art. 28(5) CIF + Art. 30(1) clearly-allocated obligations + Art. 30(2) closed list (a)–(i) |

## Sub-SO (DORA)

#### D-06.1.4 — Sub-SO for DORA

```yaml
id: SG-D-06.1.DORA
subdomain: D-06.1
applies_to: [DORA]
inherits_from: SG-DORA-011
source_SR: SR-DORA-019
activation: if DORA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Financial entities manage ICT third-party risk taking into account four-factor proportionality — nature, scale, complexity and importance of ICT-related dependencies (Art. 28(1) four-way AND) — and the risks arising from contractual arrangements on the use of ICT services; the Art. 28(5) CIF escalator ("most up-to-date and highest quality information security standards") applies to contractual arrangements concerning critical or important functions.

**Considerations.**
- The Art. 28(5) `appropriate information security standards` POLY-S3 is resolved by SR-DORA-020 to R1 (entity-selected) with R2 (supervisory-recognised) as the EU-acceptable floor.
- The `critical or important functions` POLY-S2 ambiguity (no OJ definition; 18 of 38 clauses use the term) propagates through D-06.3 + D-06.4; chosen reading is the EBA/ESMA/EIOPA RTS-supplied definition (the regulator-level RTS on critical or important functions per Art. 28(13)).

**CSF anchors (from `SR-DORA-019` v0.3 security_rationale):**
GV.SC-02, ID.AM-04.
*(GV.SC-02 anchors the supplier-prioritisation dimension — ICT
third-party service providers are prioritised by criticality (the
Art. 28(1) four-factor AND is the proportionality test, with the
`importance` factor mapping to the criticality dimension). ID.AM-04
anchors the resource-prioritised dimension — resources (here: ICT
third-party dependencies) are prioritised based on classification
(the Art. 28(4) critical-ICT third-party register maps to ID.AM-04
directly). The two subcategories together enable the financial
entity to demonstrate ex post, through documented four-factor
proportionality assessment, Art. 28(4) register records, and Art.
28(5) CIF escalator records, that the Art. 28(1) ICT third-party
risk-management duty has been exercised with the proportionality
calibration anchored in the nature, scale, complexity, and
importance of the ICT-related dependencies.)*

---


## Security Requirements (DORA)

#### 6.1.4 — ICT-third-party-as-financial-entity-counterparty risk under four-factor proportionality with Art. 28(5) CIF escalator

```yaml
- req_id: 6.1.4
  volere_section: 15
  volere_subtype: immunity

  title: "ICT-third-party-as-financial-entity-counterparty risk under Art. 28(1) four-factor proportionality (nature, scale, complexity, importance) with Art. 28(5) CIF escalator"

  derives_from:
    hso_sub_so: SO-6.1.DORA
    per_reg_so: SG-DORA-011
    source_sr: SR-DORA-019, SR-DORA-020
    hso_file: ../../HierarchicalSecurityObjectives/D-06_Supply-Chain/6.1.md
    objective_ref_section: "### 6.1.4"

  description: |
    The product shall manage ICT third-party risk taking into account the nature, scale, complexity and importance of ICT-related dependencies and the risks arising from contractual arrangements on the use of ICT services, including the criticality or importance of the respective service, process or function — with the four factors informing risk assessment cumulatively and the criticality-or-importance judgement applying to all three artefact categories; contractual arrangements with ICT third-party service providers comply with appropriate information security standards, and for contractual arrangements concerning critical or important functions, the most up-to-date and highest quality information security standards are used (DORA Art. 28(1) four-factor AND + service/process/function OR + Art. 28(5) CIF escalator + Art. 28(4) concentration-risk identification + Art. 30(1)+(2) closed-list 9-element contract + Art. 30(3)(e)(i)+(ii) audit-rights architecture).

  fit_criterion: |
    A financial-entity ICT-third-party-risk-management discipline is operated via GV.SC-02 prioritisation and assessment engine stratified by the Art. 28(1)(i) four-factor AND proportionality (nature, scale, complexity, importance — all four factors informing risk assessment cumulatively per COORD-S2 R1) + Art. 28(1)(ii) criticality-or-importance of the respective service/process/function (cumulative per COORD-S2 across all three artefacts) + ID.AM-04 supplier inventory substrate (the proportionality judgement is grounded in the actual supplier inventory, not ad-hoc case-by-case reasoning); each ICT third-party service-provider relationship is assessed against a documented supply-chain risk-management process aligned with EBA Guidelines on outsourcing arrangements; for contractual arrangements concerning critical or important functions (CIF), the Art. 28(5) CIF escalator is applied — the most up-to-date and highest quality information security standards are used (with the `critical or important` distinction POLY-S2 propagated to 18 of 38 DORA clauses per SR-DORA-019 ambiguity_notes — both categories in scope with distinct obligations attached, pending EBA RTS clarity); the Art. 30(1)+(2) 9-element closed-list contract (a)–(i) materialises the assessment into the contractual instrument + the Art. 30(3)(e)(i)+(ii) universal unrestricted rights of access, inspection and audit (with the alternative-assurance-levels qualification when other clients' rights are affected) closes the audit loop; the DORA four-factor test operationalises GDPR Art. 28(1) `sufficient guarantees` and NIS 2 Art. 21(1) chapeau with sharper factors in the financial-services subset (DORA-dominant stack where applicable); the ICT-third-party-as-financial-entity-counterparty risk discipline operates at the financial-entity ICT-dependency boundary only, with the tier hand-off to processor-tier (GDPR leg), supplier-tier (NIS 2 leg), and component-tier (CRA leg) documented as the controlled interfaces; verified by GV.SC-02 supplier-prioritisation records audit + ID.AM-04 supplier-inventory review + Art. 28(1) four-factor proportionality record inspection + Art. 28(5) CIF-standards compliance evidence review + Art. 30(2) 9-element contract attestation review + Art. 30(3)(e) audit-rights architecture documentation review + national-financial-supervisory-authority + ESA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [6.1.1 (when financial entity is also controller — DORA four-factor satisfies GDPR `sufficient guarantees` with GDPR-specific Art. 28(3) clauses appended on controller side), 6.1.2 (when financial entity = NIS 2 essential entity — DORA Art. 28(1) satisfies NIS 2 supply-chain-security chapeau in the financial-services subset via lex specialis; NIS 2 chapeau extends to physical + operational hazards)]

  nist_csf: [GV.SC-02, ID.AM-04]

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

**DORA article (verbatim, Art. 28(1)):**
> "Financial entities shall manage ICT third-party risk … taking into account: (i) the nature, scale, complexity and importance of ICT-related dependencies; (ii) the risks arising from contractual arrangements on the use of ICT services … taking into account the criticality or importance of the respective service, process or function." — DORA Art. 28(1)
>
> "Financial entities may only enter into contractual arrangements with ICT third-party service providers that comply with appropriate information security standards. When those contractual arrangements concern critical or important functions, financial entities shall … take due consideration of the use, by ICT third-party service providers, of the most up-to-date and highest quality information security standards." — DORA Art. 28(5)

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/DORA.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-06.1: GDPR↔DORA = COMPLEMENTARY (SAME — DORA exceeds GDPR, Art. 28(1) four-factor proportionality operationalises GDPR `sufficient guarantees` with sharper factors; GDPR-specific Art. 28(3) DPA clauses appended on controller side); NIS2↔DORA = EQUAL (SAME — DORA exceeds NIS 2, four-factor operationalises `appropriate and proportionate` chapeau with sharper factors; DORA satisfies NIS 2 in the financial-services subset); CRA↔DORA = DIFFERENT-PERSPECTIVE (SAME — upstream product-level vs midstream entity-level ICT provider))
```

### from regs/DORA.md body

- DORA's four-factor operationalises GDPR `sufficient guarantees` and NIS 2 `appropriate and proportionate` chapeau with sharper factors — a financial entity implementing DORA Art. 28(1) discharges GDPR Art. 28(1) in the financial-services subset (with GDPR-specific Art. 28(3) DPA clauses appended on controller side where the ICT provider is also a processor) and exceeds NIS 2's supply-chain-security requirement.

### from regs/DORA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # DORA↔GDPR = Conditional (Y financial-entity-controller; disjoint baseline: ICT-third-party ↔ data-processing-counterparty); DORA↔NIS2 = Conditional (Y cross-sector; N pure-financial via lex specialis — DORA Art. 28(1) four-factor operationalises NIS 2 chapeau with sharper factors); DORA↔CRA = Conditional (typically N — distinct actors at different supply-chain levels; Y when integrated manufacturer-financial-entity controller); HL engages on overlap

```

### from regs/DORA.md body — field `considerations`

```yaml
  considerations: |
    The DORA vendor-risk-assessment obligation is the ICT-third-party-as-financial-entity-counterparty risk management under the Art. 28(1) four-factor proportionality test; the operational substrate is a financial-entity ICT-third-party-risk-management discipline stratified by the four-factor AND (nature, scale, complexity, importance — all four factors cumulatively per COORD-S2 R1) with the criticality-or-importance judgement applying to all three artefact categories (service, process, function per COORD-S2 cumulative R1). The `critical or important functions` undefined distinction is the central DORA POLY-S2 — appears in 18 of 38 DORA clauses per `../Regulation/DORA/Ambiguity/05_DORA.md` §3.4 without ever being defined; DORA Art. 18(3) gives factors but does not fix the boundary; the chosen reading is that both categories are in scope and that distinct obligations may attach to each, pending EBA RTS clarity. The Art. 28(5) CIF escalator — `most up-to-date and highest quality information security standards` — is the DORA-unique strictness floor that applies only to CIFs; for non-CIF contractual arrangements, the `appropriate information security standards` POLY-S2 in Art. 28(5) sentence 1 applies. The DORA four-factor test exceeds both GDPR `sufficient guarantees` and NIS 2 `appropriate and proportionate` chapeau — DORA is lex specialis in the financial-services subset and a financial entity implementing DORA discharges both GDPR Art. 28(1) (with GDPR-specific Art. 28(3) clauses appended on controller side) and NIS 2 Art. 21(1) chapeau in the supply-chain-security dimension. The ICT-third-party-as-financial-entity-counterparty target object is distinct from the GDPR processor-as-legal-entity, the NIS 2 direct-supplier-as-relationship, and the CRA third-party-component-as-technical-artefact — the four target objects are layered not collapsed (DORA is midstream — deployer's ICT providers; CRA is upstream — manufacturer's inputs; GDPR / NIS 2 are downstream — deployer's own supplier due diligence). Remain open: how to operationalise the OR-coordination between `critical` and `important` remains a documented entity-policy matter awaiting EBA RTS clarity. (Copied from the HSO Considerations block of `### 6.1.4`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=DORA; demoted=4; core_cross_mentions=2 -->
