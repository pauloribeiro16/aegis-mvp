# D-09.4 — DORA module

> Regulation-specific layer: applies when `DORA` is in scope
> (activation: `if DORA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| DORA | (out-of-scope as RoPA-equivalent — partial via DORA Art. 9(4)(a) information-security policy) | DORA does **NOT** impose a RoPA obligation (no GDPR Art. 30 analogue). The DORA Art. 9(4)(a) information security policy defines rules to protect availability, authenticity, integrity and confidentiality of data, information assets and ICT assets — different record type serving a different audit purpose than RoPA. DORA BC/DR logging obligations (Art. 12) are operational continuity artefacts, not RoPA-equivalents. | Entity-level IS-policy documentation serving NCA audit purposes — **partial coverage at D-09.4 (different record type, not RoPA-equivalent)**; CRDA explicitly classifies DORA as "fully absent" for D-09.4 per CRDA-deep §D-09.4 line 29. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **DORA** | entity-level information security policy defining rules to protect availability, authenticity, integrity and confidentiality of data, information assets and ICT assets — **different record type from GDPR RoPA; DORA is fully absent for RoPA-equivalent per CRDA explicit note** | Art. 9(4)(a) `Financial entities shall … develop and document an information security policy defining rules to protect the availability, authenticity, integrity and confidentiality of data, information assets and ICT assets, including those of their customers, where applicable` (per SR-DORA-031) | management body (Art. 5(2) four-verb coordination: define/approve/oversee/be responsible — cross to D-09.1) + control function with appropriate level of independence per three-lines-of-defence (Art. 6(4) — cross to D-09.3) | competent authority (NCA — national financial supervisory authority) + management body — Art. 9(4)(a) IS-policy documentation serving NCA audit purposes | Art. 9(4)(a) (per SR-DORA-031) + Art. 6(4) three-lines-of-defence + Art. 5(2) management-body oversight + Art. 4 proportionality `in relation to the size, nature, scale and complexity of the financial entity's activities` |

## Sub-SO (DORA)

#### D-09.4.4 — Sub-SO for DORA

```yaml
id: SO-D-09.4.DORA
subdomain: D-09.4
applies_to: [DORA]
inherits_from: (out-of-scope as RoPA-equivalent — partial via DORA Art. 9(4)(a) SO-DORA-018 cross)
source_SR: SR-DORA-031
activation: if DORA in applicable_regs
phase_1A_role: 4_of_5
```

**Objective.** Financial entities **develop and document an information security policy defining rules to protect the availability, authenticity, integrity and confidentiality of data, information assets and ICT assets, including those of their customers, where applicable** (Art. 9(4)(a) DORA); this is entity-level IS-policy documentation serving NCA audit purposes and is a **different record type from the GDPR RoPA**.

**CSF anchors (from `SR-DORA-031` v0.3 security_rationale):**
ID.AM-08 (primary), ID.AM-08, GV.PO-01.

---


## Security Requirements (DORA)

#### 9.4.4 — Entity-level information security policy per Art. 9(4)(a) defining rules to protect availability, authenticity, integrity and confidentiality of data, information assets and ICT assets (different record type from RoPA)

```yaml
- req_id: 9.4.4
  volere_section: 15
  volere_subtype: audit

  title: "Financial entity develops and documents an information security policy defining rules to protect availability, authenticity, integrity and confidentiality of data, information assets and ICT assets, including those of customers where applicable (Art. 9(4)(a) DORA)"

  derives_from:
    hso_sub_so: SO-9.4.DORA
    per_reg_so: SO-DORA-018 (cross to 9.1 DORA sub-SO)
    source_sr: SR-DORA-031
    hso_file: ../../HierarchicalSecurityObjectives/D-09_Governance-Documentation/9.4.md
    objective_ref_section: "### 9.4.4"

  description: |
    The product shall develop and document an information security policy defining rules to protect the availability, authenticity, integrity and confidentiality of data, information assets, and ICT assets, including those of their customers, where applicable (per DORA Art. 9(4)(a)), under the management-body define/approve/oversee/be-responsible architecture per Art. 5(2) four-verb coordination, the three-lines-of-defence model per Art. 6(4), and the proportionality factors per Art. 4 (size, nature, scale, and complexity of the financial entity's activities); this is entity-level IS-policy documentation serving NCA audit purposes and is a **different record type from the GDPR RoPA**.

  fit_criterion: |
    An information security policy is developed and documented per Art. 9(4)(a) `Financial entities shall … develop and document an information security policy defining rules to protect the availability, authenticity, integrity and confidentiality of data, information assets and ICT assets, including those of their customers, where applicable` (SR-DORA-031) verified by ID.AM-08 lifecycle-management dimension (the financial entity demonstrates ex post that the IS-policy is managed throughout the life cycle of data, information assets, and ICT assets per CRDA DomainAnalysis §9.4 line 113 cross-validation) + ID.AM-08 risk-strategy-consistent data management (the IS-policy CIA+A 4-way + customer-where-applicable dimension is consistent with the entity's risk strategy per CRDA DomainAnalysis §9.4 line 113) + GV.PO-01 cybersecurity-policy substrate (the IS-policy is an organisational policy under the management-body define/approve/oversee/be-responsible architecture per Art. 5(2) — cross to 9.1 DORA sub-SO); the management body discharges the Art. 5(2) four-verb coordination `define, approve, oversee and be responsible for` (per SR-DORA-026); the three-lines-of-defence model is operationalised per Art. 6(4) (operational-management as first line, risk-management and compliance as second line, internal-audit as third line); the proportionality factors per Art. 4 `in relation to the size, nature, scale and complexity of the financial entity's activities` calibrate the IS-policy depth; no OJ-quantified retention period — entity-discretionary under Member State transposition; the recipient is the **competent authority (NCA — national financial supervisory authority) + management body** on the Art. 9(4)(a) IS-policy documentation serving NCA audit purposes. Verified by NCA audit pack (IS-policy extract, Art. 5(2) management-body approval minute, three-lines-of-defence documentation, Art. 4 proportionality calibration evidence) + automated CIA+A field-completeness test (availability, authenticity, integrity, confidentiality of data + information assets + ICT assets, customer-where-applicable). **IMPORTANT — DORA-absence flag**: per CRDA-deep §9.4 line 29, DORA is fully absent for RoPA-equivalent — DORA does not impose a RoPA obligation (no analogue to GDPR Art. 30). The DORA Art. 9(4)(a) IS-policy documentation is a **different record type** (entity-level IS-policy documentation) serving a **different audit purpose** (NCA audit on IS policy) than the GDPR RoPA (DPA audit on processing activities). For DORA financial entities, the GDPR RoPA remains the dedicated authority for processing-activities documentation; the DORA Art. 9(4)(a) IS-policy documentation is a separate artefact. **DORA BC/DR logging obligations (Art. 12) are operational continuity artefacts, not RoPA-equivalents** — covered separately under D-10 Monitoring & Audit. Phase 1 entities with GDPR + DORA applicability must maintain both GDPR RoPA + DORA Art. 9(4)(a) IS-policy documentation on distinct artefacts that are not substitutable (no cross-substitution OJ-permitted).

  priority: MUST
  verification_method: TEST
  dependencies: [9.4.1 (when DORA-controller — DORA Art. 9(4)(a) IS-policy is different record type from RoPA; for DORA financial entities, the GDPR RoPA remains the dedicated authority for processing-activities documentation per CRDA-absence flag; the two artefacts are not substitutable), 9.4.2 (when DORA-NSIE — DORA Art. 9(4)(a) IS-policy documentation + NIS 2 Art. 24 certification-driven records on distinct artefacts; CRDA-recommended COMPLEMENTARY), 9.4.3 (when DORA entity procures CRA-conformant products — DORA Art. 9(4)(a) IS-policy documentation + CRA Annex VII 8-item technical documentation on distinct artefacts; CRDA-recommended COMPLEMENTARY), 9.4.5 (when DORA financial entity deploys high-risk AI — DORA Art. 9(4)(a) IS-policy + AI Act Art. 17(1) QMS on distinct artefacts; CRDA-recommended COMPLEMENTARY)]

  nist_csf: [ID.AM-08, GV.PO-01]

  applicable_if:
    regs: [DORA]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (DORA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**DORA article (verbatim, Art. 9(4)(a) per SR-DORA-031):**
> "Financial entities shall … develop and document an information security policy defining rules to protect the availability, authenticity, integrity and confidentiality of data, information assets and ICT assets, including those of their customers, where applicable." — Art. 9(4)(a) DORA

**DORA article (verbatim, Art. 9(4)(a)):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/DORA.md body — field `verified_relationship`

```yaml
verified_relationship: PARTIAL (CRDA-deep, D-09.4: GDPR↔DORA = DIFFERENT-PERSPECTIVE RECOMMENDED-by-CRDA (substantively scope-disjoint per CRDA `N (typically)`-recommended; RoPA vs. DORA Art. 9(4)(a) IS-policy documentation; **DORA fully absent for RoPA-equivalent per CRDA explicit note** — for DORA financial entities, the GDPR RoPA remains the dedicated authority for processing-activities documentation); NIS2↔DORA = COMPLEMENTARY RECOMMENDED-by-CRDA (Conditional-Y when DORA financial entity is also an NSIE); CRA↔DORA = COMPLEMENTARY RECOMMENDED-by-CRDA (Conditional-Y when DORA entity procures CRA-conformant products); DORA↔AI_Act = COMPLEMENTARY RECOMMENDED-by-CRDA (Conditional-Y when DORA financial entity deploys high-risk AI))
```

### from regs/DORA.md body

*(ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycle — anchors the DORA Art. 9(4)(a) `data, information assets and ICT assets` dimension mapped to NIST CSF 2.0 ID.AM-08 per CRDA DomainAnalysis §D-09.4 line 113 cross-validation; ID.AM-08 — Data managed consistent with risk strategy — anchors the DORA Art. 9(4)(a) `availability, authenticity, integrity and confidentiality of data, information assets and ICT assets, including those of their customers, where applicable` CIA+A 4-way + customer-where-applicable dimension per CRDA DomainAnalysis §D-09.4 line 113; GV.PO-01 — Organizational cybersecurity policy established, communicated, enforced — anchors the DORA Art. 9(4)(a) IS-policy as an organisational policy (cross to D-09.1 DORA sub-SO). The three subcategories together enable the financial entity to demonstrate ex post, against the national competent authority + EBA supervisory baseline, that the Art. 9(4)(a) IS-policy documentation was developed and documented in light of the proportionality factors (size, nature, scale, complexity per Art. 4). **IMPORTANT — DORA-absence flag**: per CRDA-deep §D-09.4 line 29, **DORA is fully absent for RoPA-equivalent** — DORA does not impose a RoPA obligation (no analogue to GDPR Art. 30). The DORA Art. 9(4)(a) IS-policy documentation is a **different record type** (entity-level IS-policy documentation) serving a **different audit purpose** (NCA audit on IS policy) than the GDPR RoPA (DPA audit on processing activities). For DORA financial entities, the GDPR RoPA remains the dedicated authority for processing-activities documentation; the DORA Art. 9(4)(a) IS-policy documentation is a separate artefact. **DORA BC/DR logging obligations (Art. 12) are operational continuity artefacts, not RoPA-equivalents** — covered separately under D-10 Monitoring & Audit. Phase 1 entities with GDPR + DORA applicability must maintain both GDPR RoPA + DORA Art. 9(4)(a) IS-policy documentation on distinct artefacts that are not substitutable.)*

### from regs/DORA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # DORA↔GDPR = N (typically) RECOMMENDED — substantively scope-disjoint (DORA Art. 9(4)(a) IS-policy documentation vs. RoPA; DORA fully absent for RoPA per CRDA explicit note; different record types, different audit purposes; CRDA `different-perspective` is a taxonomy artifact); DORA↔NIS2 = Conditional (Y when DORA financial entity is also NSIE; CRDA-recommended COMPLEMENTARY); DORA↔CRA = Conditional (Y when DORA entity procures CRA-conformant products; CRDA-recommended COMPLEMENTARY); DORA↔AI_Act = Conditional (Y when DORA financial entity deploys high-risk AI; CRDA-recommended COMPLEMENTARY); HL engages when the DORA sub-SO activates AND ≥1 other sub-SO activates on Y or Conditional-Y overlap.

```

### from regs/DORA.md body — field `considerations`

```yaml
  considerations: |
    The DORA records-of-processing obligation at 9.4 is the **entity-level information security policy** per Art. 9(4)(a), with **management-body define/approve/oversee/be-responsible** per Art. 5(2) + **three-lines-of-defence** per Art. 6(4) + **proportionality factors** per Art. 4 as governance anchor. **DORA-absence flag (CRDA-deep §9.4 line 29)**: DORA is fully absent for RoPA-equivalent — DORA does not impose a RoPA obligation (no analogue to GDPR Art. 30). The DORA Art. 9(4)(a) IS-policy documentation is a **different record type** (entity-level IS-policy documentation) serving a **different audit purpose** (NCA audit on IS policy) than the GDPR RoPA (DPA audit on processing activities). For DORA financial entities, the GDPR RoPA remains the dedicated authority for processing-activities documentation; the DORA Art. 9(4)(a) IS-policy documentation is a separate artefact (cross to 9.1 DORA sub-SO). **DORA BC/DR logging obligations (Art. 12) are operational continuity artefacts, not RoPA-equivalents** — covered separately under D-10 Monitoring & Audit. The CIA+A 4-way `availability, authenticity, integrity and confidentiality` (VAG + COORD per SR-DORA-031 ambiguity_notes) + customer-where-applicable dimension is the IS-policy coverage anchor. The recipient is the **competent authority (NCA — national financial supervisory authority) + management body** on the Art. 9(4)(a) IS-policy documentation serving NCA audit purposes. No OJ-quantified retention period for the IS-policy — entity-discretionary under Member State transposition + EBA Guidelines supervisory baseline.
```

<!-- aegis:purity: own_reg=DORA; demoted=4; core_cross_mentions=4 -->