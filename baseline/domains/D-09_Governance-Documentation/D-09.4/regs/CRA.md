# D-09.4 — CRA module

> Regulation-specific layer: applies when `CRA` is in scope
> (activation: `if CRA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| CRA | SG-CRA-055 to SG-CRA-067 (many — D-09.4 is the densest CRA sub-domain) | Single point of contact (Art. 13(17)) + product identification (Art. 13(15)/(16) + Annex II §1/§3) + 10-year technical-documentation retention (Art. 13(13) + Art. 19(6) + Art. 23(2)) + EU declaration + CE marking (Art. 13(12) + Art. 28 + Art. 30) + Annex VII 8-item technical documentation + support-period determination (Art. 13(8) sentence 2 + Art. 13(19) + Annex II §7) + EU declaration provision (Art. 13(20) + Annex II §6) + immediate corrective measures (Art. 13(21)) + MSA cooperation (Art. 13(22) + Art. 13(4) sentence 2) + cessation of operations notification (Art. 13(23)) + conformity-assessment procedure selection (Art. 32) + Commission implementing/delegated acts (Art. 13(24)/(25) + Art. 14(9)/(10) + Art. 7(3)/(4) + Art. 30(6)). | Product-level technical documentation regime; Annex VII 8-item content list; 10-year retention or support period (whichever longer); substantively scope-disjoint from GDPR per CRDA `N (typically)` (different record types, different triggers). |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **CRA** | product-level technical documentation: Annex VII 8-item content list (general description + design/development/vulnerability-handling processes + risk assessment + support-period determination + standards applied + test reports + EU declaration copy + SBOM on MSA reasoned request) + pre-market documentation + EU declaration + CE marking + product identification + manufacturer contact info + support-period end-date + EU declaration provision + immediate corrective measures + MSA cooperation + cessation-of-operations notification + Commission implementing/delegated acts + conformity-assessment procedure selection | Art. 13(12) sentence 1 `the manufacturer shall draw up the technical documentation referred to in Article 31` + Art. 13(12) sentence 2 EU declaration + CE marking + Art. 13(13) `10 years … or for the support period, whichever is longer` + Annex VII §1-§8 8-item content list (per SR-CRA-087 + SR-CRA-088) | manufacturer (Art. 13 manufacturer obligations owner — cross to D-09.1) + MSA oversight — distinct from data-protection governance body | market surveillance authority (MSA) — Art. 13(12)/(13) + Annex VII §1-§8 + Art. 13(15)/(16) + Art. 13(17) SPOC + Art. 13(19) + Art. 13(20) + Art. 13(21) + Art. 13(22) + Art. 13(23) + Art. 13(24)/(25) + Art. 28 EU declaration + Art. 30 CE marking + Art. 31 technical-documentation drawing-up-before-placing + Art. 32 conformity-assessment procedure selection | Art. 13(12) + Art. 13(13) 10-year retention + Art. 13(15)/(16) + Art. 13(17) SPOC + Art. 13(19) + Art. 13(20) + Art. 13(21) + Art. 13(22) + Art. 13(23) + Art. 13(24)/(25) Commission acts + Annex II §1/§2/§3/§6/§7 + Annex VII §1-§8 + Art. 28 EU declaration + Art. 30 CE marking + Art. 31 drawing-up-before-placing + Art. 32 conformity-assessment procedure |

## Sub-SO (CRA)

#### D-09.4.3 — Sub-SO for CRA

```yaml
id: SG-D-09.4.CRA
subdomain: D-09.4
applies_to: [CRA]
inherits_from: SG-CRA-055 + SG-CRA-056 + SG-CRA-057 + SG-CRA-058 + SG-CRA-059 + SG-CRA-061 + SG-CRA-062 + SG-CRA-063 + SG-CRA-064 + SG-CRA-065 + SG-CRA-066 + SG-CRA-067
source_SR: SR-CRA-085 + SR-CRA-087 + SR-CRA-088 + SR-CRA-078
activation: if CRA in applicable_regs
phase_1A_role: 3_of_5
```

**Objective.** The manufacturer **draws up before placing a product with digital elements on the market the technical documentation referred to in Art. 31** (Art. 13(12) sentence 1 CRA), carries out the conformity assessment procedure referred to in Art. 32, draws up the EU declaration of conformity under Art. 28, and affixes the CE marking under Art. 30 (Art. 13(12) sentence 2); the manufacturer keeps the technical documentation and the EU declaration of conformity at the disposal of market surveillance authorities for at least 10 years or the support period, whichever is longer (Art. 13(13) CRA).

**CSF anchors (from `SR-CRA-085` + `SR-CRA-087` + `SR-CRA-088` + `SR-CRA-078` v0.3 security_rationale):**
GV.PO-02, GV.OC-03, ID.AM-02, ID.RA-04, GV.SC-04.

---


## Security Requirements (CRA)

#### 9.4.3 — Product-level technical documentation per Annex VII §1-§8 8-item content list, 10-year or support-period retention, MSA audit

```yaml
- req_id: 9.4.3
  volere_section: 15
  volere_subtype: audit

  title: "Manufacturer draws up before placing on market the technical documentation per Annex VII §1-§8 8-item content list, keeps it at MSA disposal for at least 10 years or the support period (whichever longer), and provides the EU declaration + CE marking"

  derives_from:
    hso_sub_so: SO-9.4.CRA
    per_reg_so: SG-CRA-055 + SG-CRA-056 + SG-CRA-057 + SG-CRA-058 + SG-CRA-059 + SG-CRA-061 + SG-CRA-062 + SG-CRA-063 + SG-CRA-064 + SG-CRA-065 + SG-CRA-066 + SG-CRA-067
    source_sr: SR-CRA-085 + SR-CRA-087 + SR-CRA-088 + SR-CRA-078
    hso_file: ../../HierarchicalSecurityObjectives/D-09_Governance-Documentation/9.4.md
    objective_ref_section: "### 9.4.3"

  description: |
    The product shall draw up before placing a product with digital elements on the market the technical documentation referred to in Art. 31 (per CRA Art. 13(12) sentence 1), carry out the conformity assessment procedure referred to in Art. 32, draw up the EU declaration of conformity under Art. 28, and affix the CE marking under Art. 30 (per Art. 13(12) sentence 2), with the technical documentation and the EU declaration of conformity kept at the disposal of market surveillance authorities for at least 10 years or the support period, whichever is longer (per Art. 13(13)), and the Annex VII §1-§8 8-item content list (general description; design, development, production, and vulnerability-handling processes; cybersecurity risk assessment; support-period determination; harmonised standards applied; reports of tests carried out; copy of the EU declaration of conformity; SBOM on MSA reasoned request) maintained throughout the support period.

  fit_criterion: |
    Technical documentation is drawn up before placing on market per Art. 13(12) sentence 1 `the manufacturer shall draw up the technical documentation referred to in Article 31` (SR-CRA-085) verified by ID.AM-08 lifecycle-management dimension (manufacturer demonstrates ex post that the Annex VII §1-§8 8-item content list is managed throughout the product life cycle per CRDA DomainAnalysis §9.4 line 113 cross-validation) + ID.AM-08 risk-strategy-consistent data management (the Annex VII §1 `general description` + §3 `cybersecurity risk assessment` dimensions are consistent with the entity's risk strategy per CRDA DomainAnalysis §9.4 line 113) + ID.RA-05 risk-priority-response dimension (the Annex VII §3 `cybersecurity risk assessment` documentation is mapped to the priority risk responses per CRDA DomainAnalysis §9.4 line 113); the Annex VII §1-§8 8-item content list is fully content-codified (§1 general description; §2 design, development, production, and vulnerability-handling processes; §3 cybersecurity risk assessment; §4 support-period determination; §5 harmonised standards applied; §6 reports of tests carried out; §7 copy of the EU declaration of conformity; §8 SBOM on MSA reasoned request — per SR-CRA-087 + SR-CRA-088); the technical documentation is drawn up before placing on the market per Art. 31(2); the manufacturer carries out the conformity assessment procedure referred to in Art. 32 (selection of internal production control per Annex VI or third-party assessment per Annex VII depending on criticality class); the manufacturer draws up the EU declaration of conformity per Art. 28 + CE marking per Art. 30 (per Art. 13(12) sentence 2); the technical documentation + EU declaration of conformity are kept at MSA disposal for at least 10 years or the support period, whichever longer, per Art. 13(13) `10 years … or for the support period, whichever is longer` (SR-CRA-085); the manufacturer is identified per Art. 13(15) (single point of contact per Art. 13(17) + Art. 13(16) for product-identification where applicable); the support-period end-date is displayed per Art. 13(19) (cross to D-06.3 Contractual Security Obligations); the EU declaration is provided per Art. 13(20) + Annex II §6; immediate corrective measures are taken per Art. 13(21); MSA cooperation per Art. 13(22); cessation-of-operations notification per Art. 13(23); Commission implementing/delegated acts per Art. 13(24)/(25) + Art. 14(9)/(10) + Art. 7(3)/(4) + Art. 30(6). The recipient is the **MSA (market surveillance authority)** on the Annex VII §1-§8 8-item content list + Art. 13(12)/(13)/(15)-(25) + Art. 28 EU declaration + Art. 30 CE marking. Verified by MSA technical-file audit pack (Annex VII §1-§8 content list extract, EU declaration copy, CE marking documentation, 10-year or support-period retention evidence, SBOM on MSA reasoned request) + automated Annex VII §1-§8 field-completeness test. **IMPORTANT — CRA full content codification**: CRA Annex VII §1-§8 is fully content-codified — the 8-item content list is explicit (vs GDPR's Art. 30(1)(a)-(g) RoPA content list with entity-discretionary fields such as `where possible`). **IMPORTANT — CRA Annex VII does NOT cross-substitute for GDPR RoPA**: substantively scope-disjoint per CRDA `N (typically)` (different record types, different triggers, different audit purposes). **IMPORTANT — CRA + AI Act for AI-enabled products do NOT have OJ-level consolidation for documentation**: unlike the CRA Art. 13(4) sentence 2 risk-assessment consolidation rule at 9.2 (which substitutes AI Act Art. 9 risk-management for CRA risk-assessment), no equivalent documentation-level consolidation rule exists at 9.4.

  priority: MUST
  verification_method: TEST
  dependencies: [9.4.1 (when controller-manufacturer — RoPA + Annex VII 8-item technical documentation on distinct artefacts; substantively scope-disjoint per CRDA `N (typically)`; CRDA `different-perspective` is a taxonomy artifact), 9.4.2 (when NSIE procures CSA-certified CRA products — CRA Art. 27(8)/(9) CSA-certification presumption-of-conformity machinery is the upstream gate for NIS 2 procurements; certification boundary), 9.4.4 (when DORA entity procures CRA-conformant products — CRA Annex VII 8-item technical documentation + DORA Art. 9(4)(a) IS-policy documentation on distinct artefacts; CRDA-recommended COMPLEMENTARY), 9.4.5 (when CRA-regulated product is also high-risk AI system — CRA Annex VII + AI Act Annex IV + AI Act Art. 17(1) QMS on three parallel artefacts; no OJ-level consolidation rule for documentation at 9.4)]

  nist_csf: [GV.PO-02, GV.OC-03]

  applicable_if:
    regs: [CRA]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (CRA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**CRA article (verbatim, Art. 13(12) + Art. 13(13) + Annex VII §1-§8):**
> "Where, prior to placing a product with digital elements on the market, the manufacturer has carried out a conformity assessment procedure … the manufacturer shall draw up the technical documentation … and draw up the EU declaration of conformity." — Art. 13(12) CRA (per SR-CRA-085)
> "The manufacturer shall keep the technical documentation and the EU declaration of conformity at the disposal of the market surveillance authorities for at least 10 years after the product has been placed on the market, or for the support period, whichever is longer." — Art. 13(13) CRA (per SR-CRA-084)

**CRA article (verbatim, Art. 27(8)/(9)):**
> "A product with digital elements and the processes put in place by the manufacturer for which the manufacturer has obtained an EU statement of conformity or an EU certificate under a European cybersecurity certification scheme adopted pursuant to Regulation (EU) 2019/881, at assurance level at least 'substantial', shall be presumed to be in conformity with the essential cybersecurity requirements …" — Art. 27(8) CRA (per SR-CRA-078)

**CRA article (verbatim, Annex VII §1-§8):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/CRA.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-09.4: GDPR↔CRA = DIFFERENT-PERSPECTIVE (SAME — substantively scope-disjoint per CRDA `N (typically)` — different record types, RoPA vs. CRA Annex VII 8-item technical documentation; substantively scope-disjoint); NIS2↔CRA = COMPLEMENTARY (SAME — Conditional-Y when NSIE procures CSA-certified CRA products; CRA Art. 27(8)/(9) CSA-certification presumption-of-conformity machinery as upstream gate for NSIE procurements; CERTIFICATION LINK); CRA↔DORA = COMPLEMENTARY RECOMMENDED-by-CRDA (Conditional-Y when DORA entity procures CRA-conformant products); CRA↔AI_Act = COMPLEMENTARY (SAME — Y when CRA-regulated product is also a high-risk AI system; CRA Annex VII + AI Act Annex IV + AI Act Art. 17 QMS stack on three parallel artefacts; **no OJ-level consolidation rule for documentation at D-09.4** — unlike the CRA Art. 13(4) sentence 2 risk-assessment consolidation rule at D-09.2, that rule covers the *risk-assessment object* not the *documentation object*))
```

### from regs/CRA.md body

*(ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycle — anchors the CRA Annex VII §1-§8 8-item content list mapped to NIST CSF 2.0 ID.AM-08 per CRDA DomainAnalysis §D-09.4 line 113 cross-validation; ID.AM-08 — Data managed consistent with risk strategy — anchors the CRA Annex VII §1 `general description` + §3 `cybersecurity risk assessment` dimensions per CRDA DomainAnalysis §D-09.4 line 113; ID.RA-05 — Threats, vulnerabilities, likelihoods, and impacts are used to determine the priority risk responses — anchors the CRA Annex VII §3 `cybersecurity risk assessment` documentation per CRDA DomainAnalysis §D-09.4 line 113 (CRA specifically maps ID.RA-05 for the risk-assessment documentation). The three subcategories together enable the manufacturer to demonstrate ex post, against the market surveillance authority, that the Annex VII §1-§8 8-item content list + Art. 13(12)/(13)/(15)/(16)/(17)/(19)/(20)/(21)/(22)/(23) documentation were established before placing on the market and kept up to date during the support period with the 10-year retention per Art. 13(13). **IMPORTANT — CRA full content codification**: CRA Annex VII §1-§8 is **fully content-codified** — the 8-item content list is explicit. The CRA sub-SO is the densest documentation regime of the 5 (covering product identification + manufacturer contact + SPOC + support-period + EU declaration + CE marking + conformity assessment + MSA cooperation + cessation-of-operations + Commission implementing/delegated acts). **IMPORTANT — CRA Annex VII does NOT cross-substitute for GDPR RoPA**: substantively scope-disjoint per CRDA `N (typically)` (different record types, different triggers, different audit purposes). **IMPORTANT — CRA + AI Act for AI-enabled products do NOT have OJ-level consolidation for documentation**: unlike the CRA Art. 13(4) sentence 2 risk-assessment consolidation rule at D-09.2 (which substitutes AI Act Art. 9 risk-management for CRA risk-assessment), there is no equivalent documentation-level consolidation rule at D-09.4; the two regimes maintain parallel artefacts (CRA Annex VII + AI Act Annex IV + AI Act Art. 17 QMS). **CRA Art. 27(8)/(9) CSA-certification presumption-of-conformity**: the CRA Art. 27(8)/(9) `A product with digital elements and the processes put in place by the manufacturer for which the manufacturer has obtained an EU statement of conformity or an EU certificate under a European cybersecurity certification scheme adopted pursuant to Regulation (EU) 2019/881, at assurance level at least 'substantial', shall be presumed to be in conformity with the essential cybersecurity requirements` is the upstream gate for NIS 2 procurements of CRA-conformant products; Phase 1 entities with NIS 2 + CRA applicability that procure CSA-certified CRA products discharge the Conditional-Y scope overlap at the certification boundary.)*

### from regs/CRA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # CRA↔GDPR = N (typically) — substantively scope-disjoint (CRA Annex VII 8-item technical documentation vs. RoPA; different record types, different audit purposes; CRDA `different-perspective` is a taxonomy artifact); CRA↔NIS2 = Conditional (Y when NSIE procures CSA-certified CRA products; certification boundary via CRA Art. 27(8)/(9)); CRA↔DORA = Conditional (Y when DORA entity procures CRA-conformant products; CRDA-recommended COMPLEMENTARY); CRA↔AI_Act = Y (CRA-regulated product is also high-risk AI system; CRA Annex VII + AI Act Annex IV + Art. 17(1) QMS on three parallel artefacts; no OJ-level consolidation rule for documentation); HL engages when the CRA sub-SO activates AND ≥1 other sub-SO activates on Y or Conditional-Y overlap.

```

### from regs/CRA.md body — field `considerations`

```yaml
  considerations: |
    The CRA records-of-processing obligation at 9.4 is the **product-level technical documentation** per Annex VII §1-§8 8-item content list (fully content-codified), with 10-year or support-period retention (whichever longer) per Art. 13(13), drawn up before placing on the market per Art. 31(2) + Art. 13(12) sentence 1, and the manufacturer as governance body per Art. 13. The Annex VII §1-§8 8-item content list is the densest documentation regime of the 5 (covering product identification + manufacturer contact + SPOC + support-period + EU declaration + CE marking + conformity assessment + MSA cooperation + cessation-of-operations + Commission implementing/delegated acts). Art. 13(12) sentence 2 requires the manufacturer to carry out the conformity assessment procedure per Art. 32 + draw up the EU declaration of conformity per Art. 28 + affix the CE marking per Art. 30. Art. 13(13) `10 years … or for the support period, whichever is longer` — the retention period is the maximum of 10 years or the support period. Art. 13(15) + Art. 13(16) + Art. 13(17) cover product identification + manufacturer contact + single point of contact. Art. 13(19) + Art. 13(20) + Art. 13(21) + Art. 13(22) + Art. 13(23) cover support-period end-date display + EU declaration provision + immediate corrective measures + MSA cooperation + cessation-of-operations notification. Art. 13(24) + Art. 13(25) + Art. 14(9) + Art. 14(10) + Art. 7(3) + Art. 7(4) + Art. 30(6) cover Commission implementing/delegated acts. Art. 28 + Art. 30 + Art. 31 + Art. 32 cover EU declaration of conformity + CE marking + technical-documentation drawing-up-before-placing + conformity-assessment procedure selection. **CRA + AI Act for AI-enabled products do NOT have OJ-level consolidation for documentation**: the CRA Art. 13(4) sentence 2 unification rule at 9.2 covers the *risk-assessment object*; there is no equivalent documentation-level consolidation rule at 9.4; the two regimes maintain parallel artefacts (CRA Annex VII + AI Act Annex IV + AI Act Art. 17(1) QMS). The recipient is the **MSA (market surveillance authority)** on the Annex VII §1-§8 8-item content list + Art. 13(12)-(25) + Art. 28 EU declaration + Art. 30 CE marking.
```

<!-- aegis:purity: own_reg=CRA; demoted=4; core_cross_mentions=2 -->
