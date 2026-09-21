# D-09.3 — NIS 2 module

> Regulation-specific layer: applies when `NIS2` is in scope
> (activation: `if NIS2 in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| NIS2 | SO-NIS2-003 (primary, partial) + SO-NIS2-021 (cross) | Entity-level asset-management sub-domain coordinated with access control (Art. 21(2)(i) `human resources security, access control policies and asset management`) + management-body oversight of Art. 21 measures (Art. 20(1)). | Partial coverage via access-control coordination; no dedicated asset-inventory mandate; NIS 2 does not impose a dedicated asset-inventory mandate (NIS 2 participant note: "NIS 2 does not impose a dedicated asset-inventory mandate"). |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **NIS 2** | entity-level asset-management sub-domain coordinated with access control — partial coverage via access-control coordination; asset-management is one of three coordinated sub-domains of access control (HR security + access control + asset management) | Art. 21(2)(i) `human resources security, access control policies and asset management` | management body (Art. 20(1) sentence 1 `management bodies … approve the cybersecurity risk-management measures … oversee their implementation and can be held liable`) — NIS 2 sub-SO inherits the management-body approve/oversee/liable architecture from D-09.1 | management body + competent authority — Art. 21(2)(i) asset-management sub-domain + Art. 20(1) management-body approval records | Art. 21(2)(i) partial-coverage asset-management sub-domain + Art. 20(1) sentence 1 management-body approve/oversee/liable + Art. 21(1) chapeau `appropriate and proportionate` proportionality hook + Recital 56 proportionality |

## Sub-SO (NIS 2)

#### D-09.3.1 — Sub-SO for NIS 2

```yaml
id: SO-D-09.3.NIS2
subdomain: D-09.3
applies_to: [NIS2]
inherits_from: SO-NIS2-003 + SO-NIS2-021 (cross)
source_SR: SR-NIS2-005
activation: if NIS2 in applicable_regs
phase_1A_role: 1_of_3
```

**Objective.** Essential and important entities adopt **access control policies coordinated with human resources security and asset management** (Art. 21(2)(i) NIS 2), with the management body approving, overseeing, and being liable for the cybersecurity risk-management measures (Art. 20(1) sentence 1 NIS 2).

**CSF anchors (from `SR-NIS2-005` v0.3 security_rationale):**
PR.PS-01 (primary), ID.AM-01, ID.AM-02.
*(PR.PS-01 — Configuration management practices established — anchors the NIS 2 Art. 21(2)(i) asset-management coordinated-with-access-control sub-domain mapped to NIST CSF 2.0 PR.PS-01 per CRDA DomainAnalysis §D-09.3 line 86 cross-validation; ID.AM-01 — Inventories of hardware managed within the system — and ID.AM-02 — Inventories of software, services, and systems managed — are the convergent NIST CSF 2.0 subcategories for the entity-level hardware + software + services + systems inventory per CRDA DomainAnalysis §D-09.3 line 86. The three subcategories together enable the NSIE to demonstrate ex post, against the Member State competent authority, that the Art. 21(2)(i) asset-management sub-domain — coordinated with access control — is established, reviewed, and updated in light of the proportionality factors (degree of exposure; likelihood of incidents; severity per Recital 56).)*


---


## Security Requirements (NIS 2)

#### 9.3.1 — Entity-level partial asset-management sub-domain coordinated with access control (no dedicated asset-inventory mandate)

```yaml
- req_id: 9.3.1
  volere_section: 15
  volere_subtype: audit

  title: "Essential and important entities adopt asset-management sub-domain coordinated with access control under NIS 2 Art. 21(2)(i), approved and overseen by the management body"

  derives_from:
    hso_sub_so: SO-9.3.NIS2
    per_reg_so: SO-NIS2-003 + SO-NIS2-021 (cross)
    source_sr: SR-NIS2-005
    hso_file: ../../HierarchicalSecurityObjectives/D-09_Governance-Documentation/9.3.md
    objective_ref_section: "### 9.3.1"

  description: |
    The product shall ensure that the essential or important entity adopts access control policies coordinated with human resources security and asset management (per NIS 2 Art. 21(2)(i)), with the management body approving the Art. 21 cybersecurity risk-management measures and overseeing their implementation (per Art. 20(1) sentence 1).

  fit_criterion: |
    The Art. 21(2)(i) sub-domain `human resources security, access control policies and asset management` (SR-NIS2-005) is established as one of three coordinated sub-domains of access control (HR security + access control + asset management) with PR.PS-01 configuration-management dimension (the entity demonstrates ex post that asset-management is established, reviewed, and updated in light of the proportionality factors — degree of exposure + likelihood of incidents + severity per Recital 56) + ID.AM-01 hardware-inventory dimension (entity demonstrates that inventories of hardware managed within the system are maintained, classified, and reviewed) + ID.AM-02 software-services-systems-inventory dimension (entity demonstrates that inventories of software, services, and systems managed are maintained, classified, and reviewed); the depth is entity-discretionary under Recital 56 proportionality + Art. 21(1) chapeau `appropriate and proportionate` + state-of-the-art floor (Art. 21(1) sentence 2) + cost factor; the management body formally approves the Art. 21(2)(i) sub-domain through a documented approval minute (cross to 9.1 NIS 2 sub-SO 9.1.2 for the management-body approve/oversee/liable architecture); for DORA financial entities under DORA's direct scope, the **DORA Art. 7(1) `3-way AND` inventory obligation is the dominant authority** and discharges both DORA's dedicated Art. 7(1) obligation and NIS 2's Art. 21(2)(i) partial-coverage asset-management dimension (cross-coupled via access-control) — DORA-dominant stack with EQUAL classification on entity-level asset inventory; for non-financial NSIEs, NIS 2 Art. 21(2)(i) partial coverage stands alone (no DORA Art. 7(1) obligation); the Art. 21(2)(i) sub-domain does NOT impose a dedicated asset-inventory mandate (per CRDA `NIS 2 does not impose a dedicated asset-inventory mandate`); the recipient is the **management body + competent authority (national NIS 2 supervisory authority)** on Art. 21(2)(i) asset-management sub-domain + Art. 20(1) management-body approval records.

  priority: MUST
  verification_method: TEST
  dependencies: [9.1.2 (Art. 20(1) management-body approve/oversee/liable architecture as the upstream policy-architecture governance hook), 9.3.3 (when DORA-NSIE — DORA Art. 7(1) `3-way AND` discharges both; EQUAL, DORA-dominant stack for financial entities), 9.3.2 (when NSIE is not manufacturer — substantively scope-disjoint per CRDA `N (typically)` on the NIS 2 ↔ CRA pair; different objects — entity asset register vs. product architecture documentation — meeting at supplier-customer interface only)]

  nist_csf: [PR.PS-01, ID.AM-01, ID.AM-02]

  applicable_if:
    regs: [NIS2]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (NIS 2)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**NIS2 article (verbatim, Art. 21(2)(i)):**
> "[Member States shall ensure that essential and important entities take appropriate and proportionate technical, operational and organisational measures to … ] (i) human resources security, access control policies and asset management." — Art. 21(2)(i) NIS 2 (per SR-NIS2-005)

**NIS2 article (verbatim, Art. 21(2)(i)):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/NIS2.md body — field `verified_relationship`

```yaml
verified_relationship: PARTIAL (CRDA-deep, D-09.3: NIS2↔CRA = SAME — COMPLEMENTARY (substantively scope-disjoint per CRDA `N (typically)` — different objects, entity asset register vs. product architecture documentation; substantively scope-disjoint; CRDA `complementary` is a taxonomy artifact); NIS2↔DORA = SAME — EQUAL (DORA Art. 7(1) sole authority with explicit OJ-literal anchor; both entity-level asset inventory; DORA-dominant for financial entities); CRA↔DORA = SAME — COMPLEMENTARY (Conditional-Y when DORA entity procures CRA-conformant products; CRA Annex VII §1-§2 architecture documentation feeds DORA asset register; DORA-led stack with CRA Annex VII §1-§2 as upstream product-level sub-register))
```

### from regs/NIS2.md body

**Considerations.** For DORA financial entities under DORA's direct scope, the DORA Art. 7(1) `3-way AND` inventory obligation is the dedicated authority and discharges both DORA's dedicated Art. 7(1) obligation and NIS 2's Art. 21(2)(i) partial-coverage asset-management dimension — DORA-dominant stack with EQUAL classification on the entity-level asset inventory.

### from regs/NIS2.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # NIS2↔DORA = Y (DORA financial entity is also an NSIE; DORA Art. 7(1) `3-way AND` is dominant authority; EQUAL on entity-level asset inventory; DORA-dominant stack discharges both); NIS2↔CRA = **N (typically)** — substantively scope-disjoint per CRDA — different objects (entity asset register vs. product architecture documentation); substantively scope-disjoint; CRDA `complementary` is a taxonomy artifact; HL does NOT engage on this pair alone; the two regimes meet at the supplier-customer interface only (CRA-conformant product is an input to the NIS 2 entity's asset register); HL engages on overlap

```

### from regs/NIS2.md body — field `considerations`

```yaml
  considerations: |
    The NIS 2 asset-inventory obligation at 9.3 is the **entity-level partial asset-management sub-domain coordinated with access control** under Art. 21(2)(i) `human resources security, access control policies and asset management` — **partial coverage only**, via access-control coordination; **NIS 2 does not impose a dedicated asset-inventory mandate**. Asset-management is one of three coordinated sub-domains of access control under the Art. 21(2)(i) chapeau (HR security + access control + asset management). The depth is entity-discretionary under Recital 56 proportionality + Art. 21(1) chapeau `appropriate and proportionate` + state-of-the-art floor + cost factor; the OJ does not codify the content template. The **NIS 2 ↔ CRA substantive scope-disjoint flag** (per CRDA-deep §9.3 line 66) is structurally significant — the pair operates on **different objects** (entity asset register vs. product architecture documentation) serving different audit purposes (entity-level NCA review vs. product-level MSA review); CRDA `complementary` is a taxonomy artifact and the two regimes meet at the **supplier-customer interface** only (CRA-conformant product is an input to the NIS 2 entity's asset register). The **NIS 2 ↔ DORA EQUAL pair** discharges both obligations on the DORA-dominant stack for financial entities; the explicit OJ-literal `3-way AND` mandate in DORA Art. 7(1) is the dominant authority on entity-level asset inventory. The **management-body approve/oversee/liable architecture** is the governance body (cross to 9.1 NIS 2 sub-SO 9.1.2). For a DORA financial entity that is also an NSIE, the DORA Art. 7(1) `3-way AND` discharges both DORA's dedicated Art. 7(1) obligation and NIS 2's Art. 21(2)(i) partial-coverage asset-management dimension (cross-coupled via access-control); for a non-financial NSIE that is not a manufacturer (no CRA Annex VII §1-§2 documentation duty), the NIS 2 partial-coverage stands alone. The recipient is the **management body + competent authority (national NIS 2 supervisory authority)** on Art. 21(2)(i) asset-management sub-domain + Art. 20(1) management-body approval records (cross to 9.1). **Important — NIS 2 partial coverage**: NIS 2 Art. 21(2)(i) does NOT impose the `classify` dimension (DORA's Art. 7(1) classify dimension is unique among the 3 participating regs), does NOT impose hardware-and-software-and-services-and-systems inventory codification (DORA's 3-way AND is more prescriptive), and does NOT impose a documented architecture description (CRA Annex VII §1-§2 partial coverage).
```

<!-- aegis:purity: own_reg=NIS2; demoted=4; core_cross_mentions=2 -->

