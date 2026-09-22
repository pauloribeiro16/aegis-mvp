# D-09.3 — CRA module

> Regulation-specific layer: applies when `CRA` is in scope
> (activation: `if CRA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| CRA | SO-CRA-061 (partial) | Annex VII §1 `general description` (intended purpose + software versions affecting compliance) + Annex VII §2 `design, development, production and vulnerability-handling processes` (system architecture description documenting how software components build on or feed into each other). | Documentation-centric, not a formal asset register in the DORA sense; **partial coverage only**; **substantively scope-disjoint from NIS 2** per CRDA `N (typically)` (per CRDA-deep `§D-09.3 line 66`). |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **CRA** | product-level technical documentation: Annex VII §1 `general description` (intended purpose + software versions affecting compliance + hardware external features where applicable + user information and instructions per Annex II) + Annex VII §2 `design, development, production, and vulnerability-handling processes` (system architecture description documenting how software components build on or feed into each other) — **partial coverage, documentation-centric, not a formal asset register in the DORA sense** | Annex VII §1 `general description` + Annex VII §2 `design, development, production, and vulnerability-handling processes` (per SR-CRA-087) | manufacturer (Art. 13(8) manufacturer policies/processes/procedures owner — cross to D-09.1) — distinct from data-protection governance body | market surveillance authority (MSA) — Annex VII §1 `general description` + Annex VII §2 `design, development, production, and vulnerability-handling processes` + 10-year technical-documentation retention per Art. 13(13) (cross to D-09.4) + conformity-assessment records per Art. 27 + Article 31(2) `drawn up before placing on the market and updated during the support period` | Annex VII §1 + Annex VII §2 (per SR-CRA-087) + Art. 31(1) `technical documentation … contain Annex I compliance evidence` + Art. 31(2) `drawn up before placing and updated during the support period` + Art. 13(13) `10-year documentation retention` + Art. 27(1)/(2)/(5)/(8)/(9) presumption-of-conformity machinery (cross to D-09.1) |

## Sub-SO (CRA)

#### D-09.3.2 — Sub-SO for CRA

```yaml
id: SO-D-09.3.CRA
subdomain: D-09.3
applies_to: [CRA]
inherits_from: SO-CRA-061
source_SR: SR-CRA-087 + SR-CRA-088
activation: if CRA in applicable_regs
phase_1A_role: 2_of_3
```

**Objective.** Manufacturers of products with digital elements draw up **technical documentation** containing at least a **general description** of the product (Annex VII §1) and a **description of the design, development, production and vulnerability-handling processes** including the system architecture description (Annex VII §2); the technical documentation is drawn up before placing on the market and updated during the support period (Art. 31(2) CRA), and kept at the disposal of market surveillance authorities for at least 10 years or the support period, whichever is longer (Art. 13(13) CRA).

**CSF anchors (from `SR-CRA-087` + `SR-CRA-088` v0.3 security_rationale):**
GV.PO-02, ID.AM-02, GV.OC-03, ID.RA-04, GV.SC-04.

---


## Security Requirements (CRA)

#### 9.3.2 — Manufacturer-side product-level architecture documentation as Annex VII §1-§2 (partial coverage, documentation-centric)

```yaml
- req_id: 9.3.2
  volere_section: 15
  volere_subtype: audit

  title: "Manufacturer draws up product-level technical documentation containing at least the general description and the design/development/production/vulnerability-handling-processes architecture description per Annex VII §1-§2"

  derives_from:
    hso_sub_so: SO-9.3.CRA
    per_reg_so: SO-CRA-061
    source_sr: SR-CRA-087 + SR-CRA-088
    hso_file: ../../HierarchicalSecurityObjectives/D-09_Governance-Documentation/9.3.md
    objective_ref_section: "### 9.3.2"

  description: |
    The product shall ensure that the manufacturer of a product with digital elements draws up technical documentation containing at least a general description of the product (Annex VII §1) and a description of the design, development, production, and vulnerability-handling processes including the system architecture description (Annex VII §2), with the technical documentation drawn up before placing on the market and updated during the support period.

  fit_criterion: |
    The technical documentation is drawn up under Annex VII §1 `general description` (intended purpose + software versions affecting compliance + hardware external features where applicable + user information and instructions per Annex II) + Annex VII §2 `design, development, production and vulnerability-handling processes` (system architecture description documenting how software components build on or feed into each other) (per SR-CRA-087 + SR-CRA-088) with ID.AM-01 hardware-inventory dimension (the documentation identifies the software versions affecting compliance + hardware external features supporting compliance with Annex I) + ID.AM-02 software-services-systems-inventory dimension (the documentation identifies how the system architecture components build on or feed into each other, providing the upstream sub-register for the entity-level master record); the technical documentation is **drawn up before placing on the market and updated during the support period** per Art. 31(2) `drawn up before placing on the market and updated during the support period` (SR-CRA-087 + Art. 13(8) support period); the technical documentation is **retained at the disposal of market surveillance authorities for at least 10 years after placement on the market or the support period, whichever is longer** per Art. 13(13) `made available to the market surveillance authorities for at least 10 years after the placement on the market of the product with digital elements or for the support period, whichever is longer`; the manufacturer acts as governance body per Art. 13(8) (cross to 9.1 CRA sub-SO 9.1.3 for the manufacturer policies/processes/procedures owner), distinct from the data-protection governance body under GDPR; for AI Act high-risk components of the product, the Annex VII §1-§2 documentation cross-references the AI Act Art. 9 risk-management-system records (which serve as the cybersecurity evidence layer for both CRA + AI Act under CRA Art. 13(4) sentence 2 consolidation); the documentation is subject to the presumption-of-conformity machinery per Art. 27(1)/(2)/(5)/(8)/(9) where harmonised standards / common specifications / European cybersecurity certification scheme under Regulation (EU) 2019/881 cover the Annex VII content; **CRA partial coverage**: CRA Annex VII §1-§2 is documentation-centric (general description + architecture), NOT a formal asset register in the DORA sense; **partial coverage only**; the partial coverage does NOT substitute for the NIS 2 entity-level asset-management sub-domain (substantively scope-disjoint per CRDA `N (typically)`) or the DORA entity-level `3-way AND` inventory (different audit purposes — product-level MSA review vs. entity-level NCA review); the recipient is the **market surveillance authority (MSA)** on Annex VII §1 `general description` + Annex VII §2 `design, development, production and vulnerability-handling processes` + 10-year technical-documentation retention per Art. 13(13) (cross to 9.4 for the records-of-processing layer) + conformity-assessment records per Art. 27 + Article 31(2) `drawn up before placing on the market and updated during the support period`.

  priority: MUST
  verification_method: TEST
  dependencies: [9.1.3 (Art. 13(8) manufacturer policies/processes/procedures as upstream governance hook), 9.3.3 (when DORA entity procures CRA-conformant — DORA-led stack with CRA Annex VII §1-§2 as upstream product-level sub-register feeding the DORA entity-level master record; COMPLEMENTARY, Conditional-Y scope overlap), 9.3.1 (when entity is not manufacturer — substantively scope-disjoint per CRDA `N (typically)` on the NIS 2 ↔ CRA pair; different objects — entity asset register vs. product architecture documentation — meeting at supplier-customer interface only)]

  nist_csf: [ID.AM-01, ID.AM-02]

  applicable_if:
    regs: [CRA]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (CRA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**CRA article (verbatim, Annex VII §1-§2):**
> "The technical documentation shall contain: (1) a general description of the product with digital elements … (2) a description of the design, development, production and vulnerability-handling processes of the product with digital elements …" — CRA Annex VII §1-§2 (per SR-CRA-087)

**CRA article (verbatim, Annex VII §1-§2):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/CRA.md body — field `verified_relationship`

```yaml
verified_relationship: PARTIAL (CRDA-deep, D-09.3: NIS2↔CRA = SAME — COMPLEMENTARY (substantively scope-disjoint per CRDA `N (typically)` — different objects, entity asset register vs. product architecture documentation; substantively scope-disjoint; CRDA `complementary` is a taxonomy artifact); NIS2↔DORA = SAME — EQUAL (DORA Art. 7(1) sole authority; DORA-dominant for financial entities); CRA↔DORA = SAME — COMPLEMENTARY (Conditional-Y when DORA entity procures CRA-conformant products; CRA Annex VII §1-§2 architecture documentation feeds DORA asset register; DORA-led stack with CRA Annex VII §1-§2 as upstream product-level sub-register))
```

### from regs/CRA.md body

*(ID.AM-01 — Inventories of hardware managed within the system — and ID.AM-02 — Inventories of software, services, and systems managed — are the convergent NIST CSF 2.0 subcategories per CRDA DomainAnalysis §D-09.3 line 86 cross-validation; the CRA Annex VII §1-§2 mandate covers the software-versions + system-architecture dimensions of these subcategories at the product level (intended purpose + software versions affecting compliance + architecture description). The two subcategories together enable the manufacturer to demonstrate ex post, against the market surveillance authority, that the Annex VII §1-§2 general description + architecture description were drawn up before placing on the market (Art. 31(2)) and kept up to date during the support period with the 10-year retention per Art. 13(13). **IMPORTANT — CRA partial coverage**: CRA Annex VII §1-§2 is documentation-centric (general description + architecture), not a formal asset register in the DORA sense; the partial coverage does not substitute for the NIS 2 entity-level asset-management sub-domain (substantively scope-disjoint per CRDA `N (typically)`) or the DORA entity-level `3-way AND` inventory (different audit purposes — product-level MSA review vs. entity-level NCA review). **CRA presumption of conformity per Art. 27(1)/(2)/(5)/(8)/(9)** discharges the CRA conformity-assessment obligation only; it does not substitute for the NIS 2 entity-level asset-management sub-domain or the DORA Art. 7(1) `3-way AND` inventory obligation.)*

### from regs/CRA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # CRA↔DORA = Conditional (Y when DORA entity procures CRA-conformant products; DORA-led stack with CRA Annex VII §1-§2 architecture documentation as upstream product-level sub-register feeding the DORA entity-level master record); CRA↔NIS2 = **N (typically)** — substantively scope-disjoint per CRDA — different objects (entity asset register vs. product architecture documentation); substantively scope-disjoint; CRDA `complementary` is a taxonomy artifact; HL does NOT engage on this pair alone; the two regimes meet at the supplier-customer interface only (CRA-conformant product is an input to the NIS 2 entity's asset register); HL engages on overlap

```

### from regs/CRA.md body — field `considerations`

```yaml
  considerations: |
    The CRA asset-inventory obligation at 9.3 is the **product-level technical documentation** under Annex VII §1 `general description` (intended purpose + software versions affecting compliance + hardware external features where applicable + user information and instructions per Annex II) + Annex VII §2 `design, development, production and vulnerability-handling processes` (system architecture description documenting how software components build on or feed into each other) — **partial coverage only**, documentation-centric, **NOT a formal asset register in the DORA sense**. The content template is partial content codification via Annex VII §1-§2. The **NIS 2 ↔ CRA substantive scope-disjoint flag** (per CRDA-deep §9.3 line 66) is structurally significant — the pair operates on **different objects** (entity asset register vs. product architecture documentation) serving different audit purposes (entity-level NCA review vs. product-level MSA review); the two regimes meet at the **supplier-customer interface** only (CRA-conformant product is an input to the NIS 2 entity's asset register). **No OJ-level consolidation rule** between NIS 2 and CRA exists at 9.3 (distinct from 9.2 where CRA Art. 13(4) sentence 2 permits AI Act Art. 9 risk-management system to substitute for CRA cybersecurity risk assessment — that rule covers the assessment object not the asset-inventory object). The **CRA ↔ DORA COMPLEMENTARY** is DORA-led with CRA Annex VII §1-§2 as upstream product-level sub-register feeding the DORA Art. 7(1) entity-level master record; CRA architecture documentation does NOT cover the classify dimension (DORA's Art. 7(1) classify dimension is unique) and does NOT cover the roles-and-dependencies dimension (DORA's `roles and dependencies in relation to ICT risk` is unique). The **manufacturer** is the governance body per Art. 13(8) (cross to 9.1 CRA sub-SO 9.1.3 for the manufacturer policies/processes/procedures owner), distinct from the data-protection governance body under GDPR; the **10-year technical-documentation retention** per Art. 13(13) + 10-year or support-period retention (whichever is longer) applies to the Annex VII content. The recipient is the **market surveillance authority (MSA)** on Annex VII §1-§2 + Art. 31(2) `drawn up before placing on the market and updated during the support period` + Art. 13(13) retention + Art. 27(1)/(2)/(5)/(8)/(9) conformity-assessment records (cross to 9.1 + 9.4). **For an NSIE + manufacturer (non-DORA)**: the NIS 2 entity-level asset register + CRA Annex VII §1-§2 architecture documentation stack on the supplier-customer interface without OJ-level consolidation; the manufacturer produces the CRA Annex VII §1-§2 documentation; the NSIE ingests it into the entity-level asset register on its side; **CRITICAL — the two artefacts are not substitutable** because they serve different audit purposes (entity-level NCA review vs. product-level MSA review). **For an entity that is not a manufacturer and not a DORA financial entity**: only the NIS 2 partial-coverage sub-SO activates on its own.
```

<!-- aegis:purity: own_reg=CRA; demoted=4; core_cross_mentions=2 -->
