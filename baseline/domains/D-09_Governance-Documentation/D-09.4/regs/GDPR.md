# D-09.4 — GDPR module

> Regulation-specific layer: applies when `GDPR` is in scope
> (activation: `if GDPR in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SG-GDPR-029 (primary) + SG-GDPR-038 (data-subject transparency) | Records of processing activities per Art. 30(1)/(2); in writing or electronic form (Art. 30(3)); 250-employee exception per Art. 30(5); supervisory-authority on-request (Art. 30(4)); transparency to data subjects (Art. 12-14). | Controller/processor RoPA mandate; data-subject-rights + DPA audit purposes; substantively scope-disjoint from NIS 2 + CRA per CRDA `N (typically)` (different record types). |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **GDPR** | controller/processor records of processing activities (RoPA) + transparency to data subjects on processing operations (Art. 12-14) | Art. 30(1) `record of processing activities under its responsibility` + Art. 30(2) processor RoPA + Art. 30(3) `in writing, including in electronic form` + Art. 30(4) on-supervisory-authority-request + Art. 30(5) 250-employee exception + Art. 12-14 transparency | controller (Art. 4(7) `the natural or legal person, public authority, agency or other body which, alone or jointly with others, determines the purposes and means of the processing of personal data`) + processor (Art. 4(8)) + DPO (Art. 37-39) | supervisory authority (DPA) + data subjects — Art. 30(1) content items (name/contact details of controller; purposes; categories of data subjects and of personal data; categories of recipients; transfers to third country; envisaged time limits for erasure; general description of technical and organisational security measures) + Art. 30(4) on-DPA-request + Art. 12-14 transparency | Art. 30(1) `(a) … (g)` 7-item content + Art. 30(2) processor RoPA content + Art. 30(3) `in writing, including in electronic form` + Art. 30(4) on-supervisory-authority-request + Art. 30(5) 250-employee exception + Art. 5(2) accountability |

## Sub-SO (GDPR)

#### D-09.4.1 — Sub-SO for GDPR

```yaml
id: SG-D-09.4.GDPR
subdomain: D-09.4
applies_to: [GDPR]
inherits_from: SG-GDPR-029 + SG-GDPR-038
source_SR: SR-GDPR-048 + SR-GDPR-050 + SR-GDPR-065 + SR-GDPR-066 + SR-GDPR-067 + SR-GDPR-068
activation: if GDPR in applicable_regs
phase_1A_role: 1_of_5
```

**Objective.** Each controller and processor **maintains a record of processing activities under its responsibility** (Art. 30(1) GDPR), in writing or electronic form (Art. 30(3) GDPR), containing the Art. 30(1) 7-item content list; the processor maintains a parallel record under Art. 30(2) GDPR; records are made available to the supervisory authority on request (Art. 30(4) GDPR), subject to the Art. 30(5) 250-employee exception.

**CSF anchors (from `SR-GDPR-048` + `SR-GDPR-050` + `SR-GDPR-065-068` v0.3 security_rationale):**
ID.AM-03, GV.PO-02, PR.PS-04, DE.AE-03, RS.AN-07, PR.AA-02.
**PF 1.1 anchors (from `SR-GDPR-048`, `SR-GDPR-050`, `SR-GDPR-065` — dashboard `00_VISUALISATIONS/GDPR/GDPR_Dashboard.html`, mechanical uniformization):**
ID.IM-P1, ID.IM-P4, ID.IM-P6, ID.IM-P8, CT.DM-P9, CM.PO-P1, CM.AW-P1, CM.AW-P3.

---


## Security Requirements (GDPR)

#### 9.4.1 — Controller/processor records of processing activities (RoPA) with the Art. 30(1) 7-item content list, in writing/electronic form, on-supervisory-authority-request

```yaml
- req_id: 9.4.1
  volere_section: 15
  volere_subtype: audit

  title: "Controller and processor maintain a record of processing activities (RoPA) under Art. 30(1)/(2)/(3)/(4)/(5) GDPR with the 7-item content list, on-DPA-request, subject to the 250-employee exception"

  derives_from:
    hso_sub_so: SO-9.4.GDPR
    per_reg_so: SG-GDPR-029 + SG-GDPR-038
    source_sr: SR-GDPR-048 + SR-GDPR-050 + SR-GDPR-065 + SR-GDPR-066 + SR-GDPR-067 + SR-GDPR-068
    hso_file: ../../HierarchicalSecurityObjectives/D-09_Governance-Documentation/9.4.md
    objective_ref_section: "### 9.4.1"

  description: |
    The product shall maintain a record of processing activities under the controller's or processor's responsibility (per GDPR Art. 30(1) + Art. 30(2) processor RoPA), in writing or electronic form (per Art. 30(3) `in writing, including in electronic form`), with the Art. 30(1) (a)-(g) 7-item content list (name/contact details of controller; purposes of processing; categories of data subjects and personal data; categories of recipients; transfers to third country; envisaged time limits for erasure; general description of technical and organisational security measures), made available to the supervisory authority on request (per Art. 30(4)), subject to the Art. 30(5) 250-employee exception, and operationalising the Art. 5(2) accountability burden (per Art. 12-14 transparency to data subjects).

  fit_criterion: |
    A RoPA is maintained per Art. 30(1) `record of processing activities under its responsibility` with the 7-item content list (SR-GDPR-048) verified by ID.AM-08 lifecycle-management dimension (controller demonstrates ex post that systems, hardware, software, services, and data are managed throughout their life cycle — the RoPA records the processing activities supporting that life cycle per CRDA DomainAnalysis §9.4 line 113 cross-validation) + ID.AM-08 risk-strategy-consistent data management (the Art. 30(1)(g) `general description of the technical and organisational security measures` is consistent with the entity's risk strategy) + GV.PO-02 process-and-procedure demonstrable-compliance (the Art. 30(3) `in writing, including in electronic form` form-factor is documented and demonstrable to the DPA on request); the processor maintains a parallel record per Art. 30(2) `record of processing activities carried out on behalf of the controller` with the (a)-(e) content (name/contact details of processor + controller; categories of processing; transfers to third country; TOMs; audit enablement to the extent necessary); records are made available to the supervisory authority on request per Art. 30(4) (SR-GDPR-050); the Art. 30(5) 250-employee exception is read at the R1 literal — `an undertaking or organisation employing fewer than 250 persons` is exempt from the RoPA obligation UNLESS processing is likely to result in a risk to the rights and freedoms of data subjects, the processing is not occasional, OR the processing includes special categories of data or criminal-conviction data; the RoPA operationalises Art. 5(2) accountability burden with Art. 12-14 transparency to data subjects cross-referenced (SR-GDPR-065-068); the recipient is the **DPA (supervisory authority)** on the Art. 30(1) RoPA content items + Art. 30(4) on-DPA-request + Art. 30(5) 250-employee exception + Art. 12-14 transparency; verified by DPA audit pack (RoPA extract, on-DPA-request retrieval procedure, accountability burden evidence, Art. 5(2) continuous compliance evidence) + automated RoPA field-completeness test (all 7 Art. 30(1)(a)-(g) fields populated for each processing activity) + Art. 30(3) form-factor inspection (writing or electronic form). **IMPORTANT — DORA-absence flag**: per CRDA-deep §9.4 line 29, DORA is fully absent for RoPA-equivalent — for DORA financial entities, the GDPR RoPA remains the dedicated authority for processing-activities documentation. The GDPR RoPA does NOT substitute for the CRA Annex VII 8-item technical documentation (substantively scope-disjoint per CRDA `N (typically)`), the NIS 2 Art. 24 certification-driven records (substantively scope-disjoint per CRDA `N (typically)`), the DORA Art. 9(4)(a) IS-policy documentation (different record type, different audit purpose), or the AI Act Annex IV + Art. 17(1) QMS documentation (parallel artefacts; no OJ-level consolidation rule for documentation at 9.4).

  priority: MUST
  verification_method: TEST
  dependencies: [9.4.2 (when controller = NSIE — RoPA + certification-driven records on distinct artefacts; substantively scope-disjoint per CRDA `N (typically)`), 9.4.3 (when controller = manufacturer — RoPA + Annex VII 8-item technical documentation on distinct artefacts; substantively scope-disjoint per CRDA `N (typically)`), 9.4.4 (when DORA-controller — DORA Art. 9(4)(a) IS-policy is different record type from RoPA; for DORA financial entities, the GDPR RoPA remains the dedicated authority for processing-activities documentation per CRDA-absence flag), 9.4.5 (when provider/deployer = controller — RoPA + AI Act Annex IV + Art. 17 QMS on three parallel artefacts; AI Act Recital 78 explicit GDPR preservation; no OJ-level consolidation rule for documentation)]

  nist_csf: [ID.AM-03, GV.PO-02]
  nist_pf: [ID.IM-P1, ID.IM-P4, ID.IM-P6, ID.IM-P8]

  applicable_if:
    regs: [GDPR]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (GDPR)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**GDPR article (verbatim, Art. 30(1)–(4) + Art. 12-14):**
> "Each controller … shall maintain a record of processing activities under its responsibility … Such record shall contain … where possible, the envisaged time limits for erasure of the different categories of data …" — Art. 30(1) GDPR
> "Each processor … shall maintain a record of all categories of processing activities carried out on behalf of a controller …" — Art. 30(2) GDPR
> "The records referred to in paragraphs 1 and 2 shall be maintained in writing, including in electronic form …" — Art. 30(3) GDPR

**GDPR article (verbatim, Art. 30(1)–(4)):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/GDPR.md body — field `verified_relationship`

```yaml
verified_relationship: DIFFERENT-PERSPECTIVE (CRDA-deep, D-09.4: GDPR↔NIS2 = DIFFERENT-PERSPECTIVE (SAME — substantively scope-disjoint per CRDA `N (typically)` — different record types, RoPA vs. certification-driven Art. 24; substantively scope-disjoint); GDPR↔CRA = DIFFERENT-PERSPECTIVE (SAME — substantively scope-disjoint per CRDA `N (typically)` — different record types, RoPA vs. CRA Annex VII 8-item technical documentation; substantively scope-disjoint); GDPR↔DORA = DIFFERENT-PERSPECTIVE RECOMMENDED-by-CRDA (substantively scope-disjoint per CRDA `N (typically)`-recommended; RoPA vs. DORA Art. 9(4)(a) IS-policy documentation; DORA fully absent for RoPA per CRDA explicit note); GDPR↔AI_Act = COMPLEMENTARY (SAME — Conditional-Y when provider/deployer is controller processing personal data via high-risk AI; GDPR RoPA + AI Act Annex IV + AI Act Art. 17 QMS stack on three parallel artefacts; AI Act Recital 78 explicit GDPR preservation; no OJ-level consolidation rule for documentation))
```

### from regs/GDPR.md body

*(ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycle — anchors the GDPR Art. 30 RoPA `record of processing activities under its responsibility` mapped to NIST CSF 2.0 ID.AM-08 per CRDA DomainAnalysis §D-09.4 line 113 cross-validation; ID.AM-08 — Data managed consistent with risk strategy — anchors the GDPR Art. 30(1)(g) `general description of the technical and organisational security measures` per CRDA DomainAnalysis §D-09.4 line 113; GV.PO-02 — Cybersecurity processes and procedures established, communicated, enforced — anchors the GDPR Art. 30(3) `in writing, including in electronic form` per CRDA DomainAnalysis §D-09.4 line 113 cross-validation (GDPR specifically maps GV.PO-02 for the demonstrable-compliance dimension). The three subcategories together enable the controller or processor to demonstrate ex post, against the Art. 5(2) accountability burden, that the Art. 30(1) RoPA 7-item content list + Art. 30(3) in-writing-or-electronic-form + Art. 30(4) on-DPA-request records were established, reviewed, and updated as processing activities changed (Art. 30(1) `shall maintain`). **IMPORTANT — DORA-absence flag**: per CRDA-deep §D-09.4 line 29, **DORA is fully absent for RoPA-equivalent**; for DORA financial entities, the GDPR RoPA remains the dedicated authority for processing-activities documentation. The GDPR RoPA does **NOT** substitute for the CRA Annex VII 8-item technical documentation (substantively scope-disjoint per CRDA `N (typically)`), the NIS 2 Art. 24 certification-driven records (substantively scope-disjoint per CRDA `N (typically)`), the DORA Art. 9(4)(a) IS-policy documentation (different record type), or the AI Act Annex IV + Art. 17(1) QMS documentation (parallel artefacts). Phase 1 entities with GDPR + CRA applicability must maintain both GDPR RoPA + CRA Annex VII technical documentation on distinct artefacts that are not substitutable.)*

### from regs/GDPR.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # GDPR↔NIS2 = N (typically) — substantively scope-disjoint (RoPA vs. certification-driven records; different record types, different audit purposes; CRDA `different-perspective` is a taxonomy artifact); GDPR↔CRA = N (typically) — substantively scope-disjoint (RoPA vs. CRA Annex VII 8-item technical documentation; different record types, different audit purposes); GDPR↔DORA = N (typically) RECOMMENDED — substantively scope-disjoint (RoPA vs. DORA Art. 9(4)(a) IS-policy documentation; DORA fully absent for RoPA per CRDA explicit note); GDPR↔AI_Act = Conditional (Y when provider/deployer is controller processing personal data via high-risk AI); HL engages when the GDPR sub-SO activates AND ≥1 other sub-SO activates on Conditional-Y overlap.

```

### from regs/GDPR.md body — field `considerations`

```yaml
  considerations: |
    The GDPR records-of-processing obligation at 9.4 is the **controller/processor RoPA** with **DPO as governance anchor** under Art. 30(1) + Art. 30(2) + Art. 30(3) + Art. 30(4) + Art. 30(5) + Art. 5(2) accountability + Art. 12-14 transparency to data subjects. Art. 30(1) `record of processing activities under its responsibility` (per SR-GDPR-048); Art. 30(1) (a)-(g) 7-item content list is the formal codification — `(a) name and contact details of the controller, any joint controller, the controller's representative and the data protection officer; (b) purposes of the processing; (c) a description of the categories of data subjects and of the categories of personal data; (d) the categories of recipients to whom personal data have been or will be disclosed including recipients in third countries or international organisations; (e) transfers of personal data to a third country or an international organisation …; (f) where possible, the envisaged time limits for erasure of the different categories of data; (g) where possible, a general description of the technical and organisational security measures`. Art. 30(2) processor RoPA content — `the name and contact details of the processor or processors, of each controller on behalf of which the processor is acting, the categories of processing carried out on behalf of the controller, transfers to a third country … and the technical and organisational security measures`. Art. 30(3) `in writing, including in electronic form` — entity-discretionary on form factor. Art. 30(4) on-DPA-request — the records are made available to the supervisory authority on request. Art. 30(5) 250-employee exception — `an undertaking or organisation employing fewer than 250 persons is not obliged to keep records of processing activities, unless … (a) the processing is likely to result in a risk to the rights and freedoms of data subjects; (b) the processing is not occasional; or (c) the processing includes special categories of data as referred to in Article 9(1) or personal data relating to criminal convictions and offences`. Art. 12-14 transparency to data subjects — the RoPA is upstream of the data-subject-facing privacy notice (cross to 9.1 GDPR sub-SO). **DORA-absence flag** (per CRDA-deep §9.4 line 29): for DORA financial entities, the GDPR RoPA remains the dedicated authority for processing-activities documentation; the DORA Art. 9(4)(a) IS-policy documentation is a separate artefact. The recipient is the **DPA (supervisory authority)** on the Art. 30(1) RoPA content items + Art. 30(4) on-DPA-request + Art. 30(5) 250-employee exception + Art. 12-14 transparency.
```

<!-- aegis:purity: own_reg=GDPR; demoted=4; core_cross_mentions=2 -->
