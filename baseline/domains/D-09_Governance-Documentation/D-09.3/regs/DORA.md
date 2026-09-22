# D-09.3 — DORA module

> Regulation-specific layer: applies when `DORA` is in scope
> (activation: `if DORA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| DORA | SO-DORA-017 (sole authority) | Identify, classify, and adequately document ICT supported business functions + roles and responsibilities + information assets + ICT assets + their roles and dependencies in relation to ICT risk (Art. 7(1)). | Entity-level formal asset inventory; **the dedicated authority per AEGIS taxonomy §4.1** (OJ-literal Art. 7(1) 3-way AND); DORA-dominant for DORA financial entities. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **DORA** | financial-entity dedicated asset inventory: ICT supported business functions + roles and responsibilities + information assets + ICT assets + their roles and dependencies in relation to ICT risk — **entity-level formal asset inventory with explicit OJ-literal `3-way AND`** — **the dedicated authority per AEGIS taxonomy §4.1** | Art. 7(1) `Financial entities shall identify, classify and adequately document all ICT supported business functions, the roles and responsibilities supporting those functions, the information assets and ICT assets supporting those functions, and their roles and dependencies in relation to ICT risk` (per SR-DORA-029) + Art. 6(4) three-lines-of-defence model | management body (Art. 5(2) four-verb coordination: define/approve/oversee/be responsible — cross to D-09.1) + control function with appropriate level of independence per three-lines-of-defence (Art. 6(4)) | competent authority (NCA — national financial supervisory authority) + management body — Art. 7(1) ICT asset register + Art. 6(4) three-lines-of-defence + EBA Guidelines on ICT and security risk management supervisory baseline | Art. 7(1) `identify, classify, adequately document` 3-verb + `3-way AND` of ICT supported business functions + information assets + ICT assets + roles and dependencies (per SR-DORA-029) + Art. 6(4) three-lines-of-defence (per SR-DORA-017 cross) + Art. 5(2) management-body oversight (cross to D-09.1) + Art. 4 proportionality `in relation to the size, nature, scale and complexity of the financial entity's activities` |

## Sub-SO (DORA)

#### D-09.3.3 — Sub-SO for DORA

```yaml
id: SO-D-09.3.DORA
subdomain: D-09.3
applies_to: [DORA]
inherits_from: SO-DORA-017 (sole authority per AEGIS taxonomy §4.1)
source_SR: SR-DORA-029
activation: if DORA in applicable_regs
phase_1A_role: 3_of_3
```

**Objective.** Financial entities **identify, classify and adequately document all ICT supported business functions, the roles and responsibilities supporting those functions, the information assets and ICT assets supporting those functions, and their roles and dependencies in relation to ICT risk** (Art. 7(1) DORA — the dedicated authority with explicit OJ-literal `3-way AND`); responsibility for managing and overseeing ICT risk is assigned to a control function with appropriate independence per the three lines of defence model (Art. 6(4) DORA).

**CSF anchors (from `SR-DORA-029` v0.3 security_rationale):**
ID.AM-01, ID.AM-02, ID.AM-03, ID.AM-05.

---


## Security Requirements (DORA)

#### 9.3.3 — Financial-entity dedicated Art. 7(1) `3-way AND` asset inventory as the sole authority per AEGIS taxonomy §4.1 (OJ-literal)

```yaml
- req_id: 9.3.3
  volere_section: 15
  volere_subtype: audit

  title: "Financial entity identifies, classifies, and adequately documents ICT supported business functions + roles and responsibilities + information assets + ICT assets + dependencies in relation to ICT risk under three-lines-of-defence and management-body governance"

  derives_from:
    hso_sub_so: SO-9.3.DORA
    per_reg_so: SO-DORA-017 (sole authority per AEGIS taxonomy §4.1)
    source_sr: SR-DORA-029
    hso_file: ../../HierarchicalSecurityObjectives/D-09_Governance-Documentation/9.3.md
    objective_ref_section: "### 9.3.3"

  description: |
    The product shall ensure that the financial entity identifies, classifies, and adequately documents all ICT supported business functions, the roles and responsibilities supporting those functions, the information assets and ICT assets supporting those functions, and their roles and dependencies in relation to ICT risk (per DORA Art. 7(1)) — with the inventory operated under the three-lines-of-defence model (per Art. 6(4)) and approved by the management body under the Art. 5(2) four-verb coordination.

  fit_criterion: |
    The financial entity maintains a dedicated entity-level asset inventory under Art. 7(1) `Financial entities shall identify, classify and adequately document all ICT supported business functions, the roles and responsibilities supporting those functions, the information assets and ICT assets supporting those functions, and their roles and dependencies in relation to ICT risk` (per SR-DORA-029) (per CRDA DomainAnalysis §9.3 line 80 — **DORA Art. 7(1) is the dedicated authority with explicit OJ-literal anchor**) with ID.AM-01 hardware-inventory dimension (Art. 7(1) `information assets` + `ICT assets` dimension mapped to NIST CSF 2.0 ID.AM-01) + ID.AM-02 software-services-systems-inventory dimension (Art. 7(1) `ICT supported business functions` + software-inventory dimension mapped to NIST CSF 2.0 ID.AM-02) + **ID.AM-05 assets-prioritised-by-criticality dimension** (Art. 7(1) `classify` dimension mapped to NIST CSF 2.0 ID.AM-05 — **classification dimension unique to DORA** among the 3 participating regs; NIS 2 does not impose the classify dimension; CRA does not impose the classify dimension); the inventory demonstrates the **3-way AND** chain of (1) ICT supported business functions + (2) information assets + (3) ICT assets, with the **+ roles and responsibilities + dependencies** extensions per Art. 7(1) (the OJ-literal chain includes ICT supported business functions, roles and responsibilities, information assets, ICT assets, and their roles and dependencies — 3 primary + 2 extensions); the inventory is operated under the **three-lines-of-defence model** per Art. 6(4) (operational-management as first line, risk-management and compliance as second line, internal-audit as third line) with responsibility for managing and overseeing ICT risk assigned to a control function with appropriate level of independence; the inventory is approved and overseen by the management body under the **Art. 5(2) four-verb coordination** `define, approve, oversee and be responsible for` (cross to 9.1 DORA sub-SO 9.1.4 for the four-verb coordination); the depth and granularity are calibrated by Art. 4 proportionality `in relation to the size, nature, scale and complexity of the financial entity's activities`; for DORA financial entities that are also NSIEs, the **DORA Art. 7(1) `3-way AND` discharges both the NIS 2 Art. 21(2)(i) partial-coverage asset-management dimension and DORA's dedicated Art. 7(1) obligation** — DORA-dominant stack with EQUAL classification on entity-level asset inventory; for DORA financial entities that procure CRA-conformant products, the CRA Annex VII §1-§2 architecture documentation is an upstream **product-level sub-register** feeding the DORA entity-level master record — DORA-led stack with CRA as upstream product-level sub-register (per CRDA-deep §9.3 line 146); the **classification dimension** (Art. 7(1) `classify`) is **unique to DORA** among the 3 participating regs — NIS 2 and CRA provide partial coverage only with no classify dimension; the recipient is the **competent authority (NCA — national financial supervisory authority) + management body** on Art. 7(1) ICT asset register + Art. 6(4) three-lines-of-defence + Art. 5(2) management-body define/approve/oversee/be responsible + EBA Guidelines on ICT and security risk management supervisory baseline.

  priority: MUST
  verification_method: TEST
  dependencies: [8.3.2 (Art. 5(4) management-body training as literacy prerequisite for Art. 5(2) define/approve/oversee/be-responsible), 9.1.4 (Art. 5(2) four-verb coordination as upstream policy-architecture governance hook), 9.3.1 (when DORA-NSIE — DORA Art. 7(1) `3-way AND` discharges both; EQUAL, DORA-dominant stack for financial entities), 9.3.2 (when DORA entity procures CRA-conformant — CRA Annex VII §1-§2 as upstream product-level sub-register feeding the DORA entity-level master record; COMPLEMENTARY, Conditional-Y scope overlap)]

  nist_csf: [ID.AM-01, ID.AM-02, ID.AM-03, ID.AM-05]

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

**DORA article (verbatim, Art. 7(1) per SR-DORA-029; OJ-literal locus Art. 8(1) per the v0.2 audit):**
> "Financial entities shall identify, classify and adequately document all ICT supported business functions, the roles and responsibilities supporting those functions, the information assets and ICT assets supporting those functions, and their roles and dependencies in relation to ICT risk." — DORA Art. 7(1) per SR-DORA-029

**DORA article (verbatim, Art. 7(1) per SR-DORA-029; OJ-literal locus Art. 8(1) per the v0.2 audit):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/DORA.md body — field `verified_relationship`

```yaml
verified_relationship: PARTIAL (CRDA-deep, D-09.3: NIS2↔DORA = SAME — EQUAL (DORA Art. 7(1) sole authority with explicit OJ-literal anchor; both entity-level asset inventory; DORA-dominant for financial entities under DORA's direct scope); NIS2↔CRA = SAME — COMPLEMENTARY (substantively scope-disjoint per CRDA `N (typically)`); CRA↔DORA = SAME — COMPLEMENTARY (Conditional-Y when DORA entity procures CRA-conformant products; CRA Annex VII §1-§2 architecture documentation feeds DORA asset register; DORA-led stack with CRA Annex VII §1-§2 as upstream product-level sub-register))
```

### from regs/DORA.md body

*(ID.AM-01 — Inventories of hardware managed within the system — anchors the DORA Art. 7(1) `information assets` + `ICT assets` dimensions mapped to NIST CSF 2.0 ID.AM-01; ID.AM-02 — Inventories of software, services, and systems managed — anchors the DORA Art. 7(1) `ICT supported business functions` + software-inventory dimensions; ID.AM-05 — Assets are prioritized based on classification, criticality, and business value — anchors the DORA Art. 7(1) `classify` dimension per CRDA DomainAnalysis §D-09.3 line 86 cross-validation. The three subcategories together (ID.AM-01 + ID.AM-02 + ID.AM-05) are the convergent NIST CSF 2.0 subcategories for DORA's entity-level asset inventory with the **classification dimension unique to DORA** (NIS 2 does not impose the classify dimension; CRA does not impose the classify dimension). The three subcategories together enable the financial entity to demonstrate ex post, against the national competent authority + EBA supervisory baseline, that the Art. 7(1) `3-way AND` ICT asset register + Art. 6(4) three-lines-of-defence were established, reviewed, and updated in light of the proportionality factors (size, nature, scale, complexity per Art. 4). For DORA financial entities that are also NSIEs, the DORA Art. 7(1) `3-way AND` discharges both the NIS 2 partial-coverage asset-management dimension and DORA's dedicated Art. 7(1) obligation — **DORA is the dedicated authority with OJ-literal `3-way AND`** distinct from the D-07.2 OJ-text-unsupported sole-authority assignment.)*

### from regs/DORA.md body — field `scope_overlap`

```yaml
    scope_overlap: Y   # DORA↔NIS2 = Y (DORA financial entity is NSIE; DORA Art. 7(1) is dominant authority with explicit OJ-literal anchor; EQUAL on entity-level asset inventory; DORA-dominant stack for financial entities discharges both DORA's dedicated Art. 7(1) obligation and NIS 2's Art. 21(2)(i) partial-coverage asset-management dimension); DORA↔CRA = Conditional (Y when DORA entity procures CRA-conformant; same; reciprocal — CRA Annex VII §1-§2 architecture documentation as upstream product-level sub-register feeding the DORA entity-level master record); HL engages on overlap

```

### from regs/DORA.md body — field `considerations`

```yaml
  considerations: |
    The DORA asset-inventory obligation at 9.3 is the **financial-entity dedicated asset inventory** under Art. 7(1) `Financial entities shall identify, classify and adequately document all ICT supported business functions, the roles and responsibilities supporting those functions, the information assets and ICT assets supporting those functions, and their roles and dependencies in relation to ICT risk` — **the dedicated authority per AEGIS taxonomy §4.1** with explicit OJ-literal anchor (distinct from D-07.2 where the sole-authority assignment is OJ-text-unsupported). Art. 7(1) carries S2 features — 3-way AND chain of ICT supported business functions + information assets + ICT assets + roles and responsibilities + dependencies; the 3-verb `identify, classify and adequately document` (3-way COORD) and the 3-way AND asset chain are both COORD-2 (per SR-DORA-029 ambiguity_notes). The three-lines-of-defence model per Art. 6(4) provides the governance architecture with responsibility for managing and overseeing ICT risk assigned to a control function with appropriate level of independence (chosen reading: operational-management as first line, risk-management and compliance as second line, internal-audit as third line — per EBA Guidelines on ICT and security risk management). The **Art. 5(2) four-verb coordination** `define, approve, oversee and be responsible for` is the management-body define/approve/oversee/be-responsible architecture (cross to 9.1 DORA sub-SO). The **NIS 2 ↔ DORA EQUAL classification** discharges both obligations on the DORA-dominant stack for financial entities under DORA's direct scope; for non-financial NSIEs, NIS 2 Art. 21(2)(i) partial coverage stands alone (no DORA Art. 7(1) obligation). The **CRA ↔ DORA COMPLEMENTARY** is DORA-led with CRA Annex VII §1-§2 as upstream product-level sub-register feeding the DORA entity-level master record; the DORA ICT asset inventory is the entity-level master record; the CRA Annex VII §1-§2 is the product-level sub-register (per CRDA-deep §9.3 line 146). **DORA's classify dimension is unique** among the 3 participating regs — the ID.AM-05 `Assets are prioritised based on classification, criticality, and business value` anchor is unique to DORA; NIS 2 does not impose the classify dimension; CRA does not impose the classify dimension. The **3 subcategories** (ID.AM-01 + ID.AM-02 + ID.AM-05) together enable the financial entity to demonstrate ex post, against the national competent authority + EBA supervisory baseline, that the Art. 7(1) `3-way AND` ICT asset register + Art. 6(4) three-lines-of-defence + Art. 4 proportionality calibration were established, reviewed, and updated. The recipient is the **competent authority (NCA — national financial supervisory authority) + management body** on Art. 7(1) ICT asset register + Art. 6(4) three-lines-of-defence + EBA Guidelines on ICT and security risk management supervisory baseline. The Art. 7(1) inventory coordinates with the Art. 7(2) ICT risk identification register (cross to 9.2 DORA sub-SO 9.2.4 for the continuous + at-least-yearly ICT risk framework). For a DORA financial entity that is also an NSIE + deploys CRA-conformant products (a vertically-integrated 3-reg stack), the DORA Art. 7(1) entity-level master record + NIS 2 Art. 21(2)(i) partial-coverage discharged on the DORA stack + CRA Annex VII §1-§2 as upstream product-level sub-register = 2 effective artefacts (DORA + CRA sub-register), not 3, with the NIS 2 partial-coverage discharged on the DORA Art. 7(1) `3-way AND`.
```

<!-- aegis:purity: own_reg=DORA; demoted=4; core_cross_mentions=2 -->
