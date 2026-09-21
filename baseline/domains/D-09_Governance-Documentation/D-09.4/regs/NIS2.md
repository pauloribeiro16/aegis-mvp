# D-09.4 — NIS 2 module

> Regulation-specific layer: applies when `NIS2` is in scope
> (activation: `if NIS2 in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| NIS2 | SO-NIS2-024 (partial) | Member States shall encourage the use of European or internationally accepted standards and specifications relevant to the security of network and information systems (Art. 24(1)); Commission delegated acts under Art. 24(2); ENISA candidate scheme request under Art. 24(3). | Certification-driven recordkeeping (Art. 24(1)/(2)/(3)), not a RoPA-equivalent; substantively scope-disjoint from GDPR per CRDA `N (typically)` (different record types, different triggers). |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **NIS 2** | certification-driven recordkeeping — Member-State-driven use of certified ICT products, ICT services, and ICT processes per Art. 24 | Art. 24(1) sentence 1 `Member States shall encourage the use of European or internationally accepted standards and specifications relevant to the security of network and information systems` + Art. 24(1) sentence 2 qualified trust services encouragement + Art. 24(2) Commission delegated acts + Art. 24(3) ENISA candidate scheme request — **not codified at OJ level for content — entity-discretionary under Member State transposition** | management body + Member State — Art. 24(1)/(2)/(3) per Member State | management body + competent authority — Art. 24(1)/(2)/(3) certification-driven records per Member State | Art. 24(1) sentence 1 + Art. 24(1) sentence 2 + Art. 24(2) + Art. 24(3) |

## Sub-SO (NIS 2)

#### D-09.4.2 — Sub-SO for NIS 2

```yaml
id: SO-D-09.4.NIS2
subdomain: D-09.4
applies_to: [NIS2]
inherits_from: SO-NIS2-024
source_SR: SR-NIS2-043
activation: if NIS2 in applicable_regs
phase_1A_role: 2_of_5
```

**Objective.** Member States shall **encourage the use of European or internationally accepted standards and specifications relevant to the security of network and information systems** (Art. 24(1) sentence 1 NIS 2) and of qualified trust services (Art. 24(1) sentence 2); the Commission may adopt delegated acts specifying entities that must use certified ICT products, services and processes (Art. 24(2) NIS 2), and ENISA may be requested to prepare a candidate European cybersecurity certification scheme (Art. 24(3) NIS 2).

**CSF anchors (from `SR-NIS2-043` v0.3 security_rationale):**
ID.AM-08 (primary), PR.DS-12.

---


## Security Requirements (NIS 2)

#### 9.4.2 — Member-State-driven certification-driven recordkeeping under Art. 24(1)/(2)/(3) for certified ICT products, services, and processes

```yaml
- req_id: 9.4.2
  volere_section: 15
  volere_subtype: audit

  title: "Member States encourage use of European or internationally accepted standards and specifications for the security of network and information systems, with Commission delegated acts under Art. 24(2) and ENISA candidate scheme request under Art. 24(3)"

  derives_from:
    hso_sub_so: SO-9.4.NIS2
    per_reg_so: SO-NIS2-024
    source_sr: SR-NIS2-043
    hso_file: ../../HierarchicalSecurityObjectives/D-09_Governance-Documentation/9.4.md
    objective_ref_section: "### 9.4.2"

  description: |
    The product shall record the use of certified ICT products, ICT services, and ICT processes under Member-State-driven standards and specifications relevant to the security of network and information systems (per NIS 2 Art. 24(1) sentence 1) and of qualified trust services (per Art. 24(1) sentence 2), with the Commission empowered to adopt delegated acts specifying entities required to use certified ICT products/services/processes (per Art. 24(2)) and ENISA empowered to be requested to prepare a candidate European cybersecurity certification scheme (per Art. 24(3)).

  fit_criterion: |
    Certification-driven records are maintained per Art. 24(1) sentence 1 `Member States shall encourage the use of European or internationally accepted standards and specifications relevant to the security of network and information systems` (SR-NIS2-043) verified by ID.AM-08 lifecycle-management dimension (the NSIE demonstrates ex post that certified ICT products/services/processes are inventoried and managed throughout their life cycle per CRDA DomainAnalysis §9.4 line 113 cross-validation) + PR.DS-12 risk-strategy-consistent data management (the certification-driven records are consistent with the entity's risk strategy); Art. 24(1) sentence 2 `Member States shall also encourage, without prejudice to paragraph 1, the use of any qualified trust service` extends the certification-driven records to qualified trust services; Art. 24(2) `The Commission may adopt delegated acts … to specify which categories of essential and important entities shall be required to use certain certified ICT products, ICT services and ICT processes` — the certification-driven records are conditional on the Commission adopting such delegated acts; Art. 24(3) `ENISA may be requested to prepare a candidate European cybersecurity certification scheme` — the certification-driven records may feed ENISA candidate scheme preparation. The content is **not codified at OJ level** — entity-discretionary under Member State transposition. The recipient is the **management body + competent authority (national NIS 2 supervisory authority)** on the Art. 24(1)/(2)/(3) certification-driven records per Member State. **IMPORTANT — NIS 2 partial coverage at 9.4**: the NIS 2 Art. 24(1)/(2)/(3) certification-driven recordkeeping is **partial coverage** — Member-State-driven use of certified ICT products/services/processes, not a RoPA-equivalent; substantively scope-disjoint from GDPR per CRDA `N (typically)` (different record types, different triggers, different audit purposes). Phase 1 entities with NIS 2 + GDPR applicability must maintain both GDPR Art. 30 RoPA + NIS 2 Art. 24 certification-driven records on distinct artefacts that are not substitutable. For NSIEs that are CRA-conformant product procurers, the CRA Art. 27(8)/(9) CSA-certification presumption-of-conformity machinery is the upstream gate for NIS 2 procurements — Phase 1 must verify that procured CRA products hold CSA certification at the assurance level required by the Commission's delegated act under Art. 24(2). The **NIS 2 → CRA certification link** is the only cross-regulation link at 9.4 involving NIS 2.

  priority: MUST
  verification_method: TEST
  dependencies: [9.4.1 (when controller = NSIE — RoPA + certification-driven records on distinct artefacts; substantively scope-disjoint per CRDA `N (typically)`; CRDA `different-perspective` is a taxonomy artifact), 9.4.3 (when NSIE procures CSA-certified CRA products — CRA Art. 27(8)/(9) CSA-certification presumption-of-conformity machinery is the upstream gate for NIS 2 procurements; certification boundary), 9.4.4 (when DORA-NSIE — DORA Art. 9(4)(a) IS-policy documentation + NIS 2 Art. 24 certification-driven records on distinct artefacts; CRDA-recommended COMPLEMENTARY), 9.4.5 (when NSIE deploys high-risk AI — NIS 2 Art. 24 certification-driven records + AI Act Art. 17(1) QMS documentation on distinct artefacts; CRDA-recommended COMPLEMENTARY)]

  nist_csf: [ID.AM-08, PR.DS-12]

  applicable_if:
    regs: [NIS2]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (NIS 2)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**NIS2 article (verbatim, Art. 24(1)/(2)/(3)):**
> "Member States shall encourage the use of European or internationally accepted standards and specifications relevant to the security of network and information systems …" — Art. 24(1) NIS 2 (per SR-NIS2-043)

**NIS2 article (verbatim, Art. 24(1)/(2)/(3)):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/NIS2.md body — field `verified_relationship`

```yaml
verified_relationship: DIFFERENT-PERSPECTIVE (CRDA-deep, D-09.4: GDPR↔NIS2 = DIFFERENT-PERSPECTIVE (SAME — substantively scope-disjoint per CRDA `N (typically)`); NIS2↔CRA = COMPLEMENTARY (SAME — Conditional-Y when NSIE procures CSA-certified CRA products; NIS 2 Art. 24 + CRA Art. 27(8)/(9) CSA-certification presumption-of-conformity machinery as upstream gate for NSIE procurements); NIS2↔DORA = COMPLEMENTARY RECOMMENDED-by-CRDA (Conditional-Y when DORA financial entity is also an NSIE); NIS2↔AI_Act = COMPLEMENTARY RECOMMENDED-by-CRDA (Conditional-Y when NSIE deploys high-risk AI))
```

### from regs/NIS2.md body

*(ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycle — anchors the NIS 2 Art. 24(1)/(2)/(3) certification-driven recordkeeping mapped to NIST CSF 2.0 ID.AM-08 per CRDA DomainAnalysis §D-09.4 line 113 cross-validation; PR.DS-12 — Data managed consistent with risk strategy — anchors the NIS 2 Art. 24(1) use of certified ICT products/services/processes per CRDA DomainAnalysis §D-09.4 line 113. The two subcategories together enable the NSIE to demonstrate ex post, against the Member State competent authority, that the Art. 24(1)/(2)/(3) certification-driven records were established for the certified ICT products/services/processes procured. **IMPORTANT — NIS 2 partial coverage at D-09.4**: the NIS 2 Art. 24(1)/(2)/(3) certification-driven recordkeeping is **partial coverage** — Member-State-driven use of certified ICT products/services/processes, not a RoPA-equivalent; substantively scope-disjoint from GDPR per CRDA `N (typically)` (different record types, different triggers). Phase 1 entities with NIS 2 + GDPR applicability must maintain both GDPR Art. 30 RoPA + NIS 2 Art. 24 certification-driven records on distinct artefacts that are not substitutable. For NSIEs that are CRA-conformant product procurers, the CRA Art. 27(8)/(9) CSA-certification presumption-of-conformity machinery is the upstream gate for NIS 2 procurements — Phase 1 must verify that procured CRA products hold CSA certification at the assurance level required by the Commission's delegated act under Art. 24(2). The **NIS 2 → CRA certification link** is the only cross-regulation link at D-09.4 involving NIS 2.)*

### from regs/NIS2.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # NIS2↔GDPR = N (typically) — substantively scope-disjoint (certification-driven records vs. RoPA; different record types, different audit purposes; CRDA `different-perspective` is a taxonomy artifact); NIS2↔CRA = Conditional (Y when NSIE procures CSA-certified CRA products; certification boundary); NIS2↔DORA = Conditional (Y when DORA financial entity is also NSIE; CRDA-recommended COMPLEMENTARY); NIS2↔AI_Act = Conditional (Y when NSIE deploys high-risk AI; CRDA-recommended COMPLEMENTARY); HL engages when the NIS 2 sub-SO activates AND ≥1 other sub-SO activates on Y or Conditional-Y overlap.

```

### from regs/NIS2.md body — field `considerations`

```yaml
  considerations: |
    The NIS 2 records-of-processing obligation at 9.4 is the **Member-State-driven certification-driven recordkeeping** under Art. 24(1) sentence 1 (European or internationally accepted standards and specifications) + Art. 24(1) sentence 2 (qualified trust services) + Art. 24(2) (Commission delegated acts specifying which categories of essential and important entities must use certified ICT products/services/processes) + Art. 24(3) (ENISA candidate scheme request). The content is **not codified at OJ level** — entity-discretionary under Member State transposition. Art. 24(1) `Member States shall encourage the use of European or internationally accepted standards and specifications relevant to the security of network and information systems` (per SR-NIS2-043) — the `encourage` verb is VAG-3 (Berry §5.1 — no OJ-anchored threshold); the entity-discretionary reading is dominant since OJ does not enumerate specific record content. The **NIS 2 → CRA certification link** is the only cross-regulation link at 9.4 involving NIS 2 — CRA Art. 27(8) `A product with digital elements and the processes put in place by the manufacturer for which the manufacturer has obtained an EU statement of conformity or an EU certificate under a European cybersecurity certification scheme adopted pursuant to Regulation (EU) 2019/881, at assurance level at least 'substantial', shall be presumed to be in conformity with the essential cybersecurity requirements` + Art. 27(9) provides the **CSA-certification presumption-of-conformity machinery** as the upstream gate for NSIE procurements. The **NIS 2 partial coverage** at 9.4 is structurally significant — substantively scope-disjoint from GDPR per CRDA `N (typically)` (different record types, different triggers, different audit purposes); Phase 1 entities with NIS 2 + GDPR applicability must maintain both GDPR Art. 30 RoPA + NIS 2 Art. 24 certification-driven records on distinct artefacts. The recipient is the **management body + competent authority (national NIS 2 supervisory authority)** on the Art. 24(1)/(2)/(3) certification-driven records per Member State. Member State transposition divergence may apply on documentation expected to evidence the certification-driven records.
```

<!-- aegis:purity: own_reg=NIS2; demoted=4; core_cross_mentions=2 -->

