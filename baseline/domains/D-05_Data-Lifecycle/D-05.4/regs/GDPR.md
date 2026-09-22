# D-05.4 — GDPR module

> Regulation-specific layer: applies when `GDPR` is in scope
> (activation: `if GDPR in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-020 | Data subject receives personal data in a structured, commonly used, machine-readable format and can transmit those data to another controller without hindrance; the Art. 15(3) `commonly used electronic form` copy is the operational companion obligation supplying the read-only copy at the data subject's request, and Art. 20 supplies the portability right to transmit to another controller | Personal data; data-subject right; Art. 20(1)/(2)/(3)/(4) + Art. 15(3) companion copy; PR.DS-10 + ID.AM-08 |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **GDPR** | controller-side data-subject right (Art. 20 portability) | data subject's Art. 20 request (Art. 20(3) conditions met — consent/contract basis + automated means; Art. 20(4) exclusions honoured) — TRIGGERED | `structured, commonly used and machine-readable format` (Art. 20(1)) — operationalised via SR-GDPR-032 structured-interoperable reading (JSON, CSV, XML per EDPB Guidelines 06/2020) | data subject (Art. 20(1) direct recipient); receiving controller (Art. 20(1) cross-controller transmission target); DPA (Art. 58 supervision on the export-pipeline documentation) | Art. 20(1)/(2)/(3)/(4) + Art. 15(3) companion copy + Art. 12(1) transparency + Art. 12(3) ≤1-month (≤2-month complex) service-level + Art. 12(5) free of charge + Art. 13(2)(b) / Art. 14(2)(c) information-supply + Art. 30(1)(b) RoPA record + Art. 35(7) DPIA where applicable + Art. 5(2) accountability |

## Sub-SO (GDPR)

#### D-05.4.1 — Sub-SO for GDPR

```yaml
id: SO-D-05.4.GDPR
subdomain: D-05.4
applies_to: [GDPR]
inherits_from: SO-GDPR-020
source_SR: SR-GDPR-032
activation: if GDPR in applicable_regs
phase_1A_role: 1_of_N (sole sub-SO; sub-domain is single-regulator)
```

**Objective.** The data subject receives personal data in a structured, commonly used, machine-readable format (Art. 20(1) + Art. 15(3) companion copy), supplied by the controller without undue delay (Art. 12(3) ≤1 month, extendable to ≤2 months for complex requests) and free of charge (Art. 12(5)). The data subject can transmit those data to another controller without hindrance (Art. 20(1)); where technically feasible, the originating controller transmits directly to the receiving controller (Art. 20(2) sentence 2). The right applies where processing is based on consent (Art. 6(1)(a)) or contract (Art. 6(1)(b)) AND processing is carried out by automated means (Art. 20(3)); the right does NOT apply to public-interest-task or legitimate-interest processing (Art. 20(4)), and the controller may refuse an export where it would adversely affect third-party rights.

**CSF anchors (from `SR-GDPR-032` v0.3 security_rationale):**
PR.DS-10, ID.AM-08.
**PF 1.1 anchors (from `SR-GDPR-032` — dashboard `00_VISUALISATIONS/GDPR/GDPR_Dashboard.html`, mechanical uniformization):**
CT.DM-P1, CT.DM-P6.

---


## Security Requirements (GDPR)

#### 5.4.1 — Personal-data portability export per Art. 20 + Art. 15(3) companion copy, with structured-interoperable format and Art. 12(3) service-level

```yaml
- req_id: 5.4.1
  volere_section: 15
  volere_subtype: privacy

  title: "Data subject receives personal data in a structured, commonly used, machine-readable format (Art. 20(1) + Art. 15(3) companion copy), supplied by the controller without undue delay (Art. 12(3) ≤1 month, ≤2 months complex) and free of charge (Art. 12(5)); cross-controller direct transmission provided where technically feasible"

  derives_from:
    hso_sub_so: SO-D-05.4.GDPR
    per_reg_so: SO-GDPR-020
    source_sr: SR-GDPR-032
    hso_file: ../../HierarchicalSecurityObjectives/D-05_Data-Lifecycle/D-05.4.md
    objective_ref_section: "### D-05.4.1"

  description: |
    The product shall, on the data subject's Art. 20(1) request, deliver a copy of the portability-eligible personal data (Art. 6(1)(a) consent or Art. 6(1)(b) contract basis + Art. 20(3) automated-means requirement) in a structured, commonly used, machine-readable format (Art. 15(3) companion copy), supplied by the controller without undue delay (Art. 12(3) ≤1 month, extendable to ≤2 months for complex requests) and free of charge (Art. 12(5)); where technically feasible, the originating controller transmits directly to the receiving controller (Art. 20(2) sentence 2).

  fit_criterion: |
    A controller-side Art. 20 portability export endpoint is operated under PR.DS-10 runtime integrity posture (the export must reflect current processing truth under controlled exposure rather than stale snapshot drift — partial views derived from the same in-use data set are properly handled) + ID.AM-08 format-quality substrate (the structured, machine-readable, downstream-tool-friendly formats are layered into the data-handling substrate rather than treated as ad-hoc report outputs, ensuring security-classification discipline is preserved); the structured-interoperable format (JSON, CSV, XML per EDPB Guidelines 06/2020 — the print-ready reading (PDF/scanned image) rejected as defeating the purpose, the controller-proprietary reading rejected as functionally obstructing) is supplied as the default per SR-GDPR-032 VAG-S3 structured-interoperable reading; the Art. 20(3) consent/contract-basis + automated-means conditions are checked before exporting (portability applies only when the processing is based on Art. 6(1)(a) consent OR Art. 6(1)(b) contract AND the processing is carried out by automated means); the Art. 20(4) exclusions (no public-interest-task processing, no legitimate-interest processing) are honoured without prejudice to the Art. 21 right to object; the Art. 20(3) third-party-rights carve-out is honoured (refusal on the rare-but-honest ground that the export would adversely affect third-party rights and freedoms); the Art. 12(3) service-level of ≤1 month (extendable to ≤2 months for complex requests with reasoned extension notice delivered to the data subject within the original ≤1-month period) is met; the export is free of charge per Art. 12(5); cross-controller direct transmission is provided where technically feasible per Art. 20(2) sentence 2 (mutually-authenticated transport encryption with destination authentication + signed export manifests); Art. 13(2)(b) / Art. 14(2)(c) information-supply notifies the data subject of the right at collection (... (line truncated to 2000 chars)

  priority: MUST
  verification_method: TEST
  dependencies: []

  nist_csf: [PR.DS-10, ID.AM-08]

  applicable_if:
    regs: [GDPR]
    scope_overlap: Y   # GDPR activates whenever GDPR in applicable_regs AND portability-eligible personal data exists; single-participant sub-domain — the GDPR sub-SO captures the full regulatory surface of D-05.4

  satisfaction:
    controls: []
    nodes: []

```

---


## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/GDPR.md body — field `verified_relationship`

```yaml
verified_relationship: N/A (single-participant sub-domain — no pairwise surface; CRDA-deep §D-05.4 has 0 pairwise cells; the CRA Annex I Part I (2)(m) second-limb is a *technical anchor* under SR-CRA-049 and is NOT a regulatory right; the GDPR sub-SO captures the full regulatory surface of D-05.4)
```

### from regs/GDPR.md body

*(`SR-GDPR-032` covers the Art. 15(1)/(3) + Art. 20 structured-electronic-access-copy export-pipeline obligation anchored to **PR.DS-10** (Data-in-use protected — the runtime integrity posture: any export pipeline must be able to read live data under controlled exposure so that the copy delivered reflects current processing truth rather than stale snapshot drift, with proper handling for partial-views derived from the same in-use data set; the runtime integrity posture is the prerequisite for a defensible export pipeline because the export-supplied record must reflect current processing truth under controlled exposure rather than stale snapshot drift) + **ID.AM-08** (Data managed consistent with risk strategy — the data-management posture: the export pipeline is governed by the same risk strategy as the data it is exposing, with structured, commonly used formats — JSON, CSV, XML per the structured-interoperable reading aligned with EDPB Guidelines 06/2020 — layered into the data-handling substrate rather than treated as ad-hoc report outputs, ensuring the copy is machine-readable and downstream-tool-friendly without sacrificing security classification discipline; the format-selection policy is the operational expression of the risk-strategy dimension). The two subcategories together operationalise the Art. 20 portability architecture: PR.DS-10 supplies the runtime integrity substrate for the export pipeline; ID.AM-08 supplies the format-quality substrate for the structured-and-machine-readable requirement. Art. 20(2) sentence 2 cross-controller direct transmission is the operational expression of the PR.DS-10 in-use export controls (mutually-authenticated transport encryption with destination authentication and signed export manifests under the structured-interoperable reading; cf. SR-CRA-049 PR.DS-02 + ID.AM-08 anchors when the data resides in a CRA-classified product); Art. 12(1) transparency + Art. 13(2)(b) / Art. 14(2)(c) information-supply close the data-subjec... (line truncated to 2000 chars)

### from regs/GDPR.md body — field `considerations`

```yaml
  considerations: |
    The GDPR portability obligation is the controller-side data-subject right anchored on Art. 20(1) portability right + Art. 20(2) format requirement (same format where technically feasible) + Art. 20(2) sentence 2 cross-controller direct transmission (where technically feasible) + Art. 20(3) qualifying conditions (consent/contract basis + automated means) + Art. 20(4) exclusions (no public-interest-task or legitimate-interest processing; without prejudice to Art. 21 right to object) + Art. 20(3) third-party-rights carve-out (rare-but-honest structural qualifier — the controller may refuse an export where it would infringe third-party rights) + Art. 15(3) companion copy (the operational companion supplying the read-only copy at the data subject's request) + Art. 12(1) transparency + Art. 12(3) ≤1-month (≤2-month complex) service-level + Art. 12(5) free of charge + Art. 13(2)(b) / Art. 14(2)(c) information-supply + Art. 30(1)(b) RoPA record + Art. 35(7) DPIA where applicable + Art. 5(2) accountability. The structured-interoperable reading of `commonly used electronic form` per SR-GDPR-032 ambiguity_notes (JSON, CSV, XML per EDPB Guidelines 06/2020) is the format-quality floor — print-ready rendering (PDF/scanned image) and controller-preferred proprietary format are both rejected as defeating the portability purpose; the choice between JSON, CSV, or XML is delegated to the controller (calibrated per the data subject's context) within the structural floor (machine-readable; structured; commonly used; interoperable downstream). The CRA Annex I Part I (2)(m) second-limb secure cross-product transfer (SR-CRA-049 PR.DS-02 + ID.AM-08 anchors) is the complementary technical anchor when the portability-eligible data resides in a CRA-classified product — NOT a portability right, NOT a sub-SO on D-05.4, but the architectural substrate (confidentiality + integrity + destination-authentication) that makes the Art. 20 cross-controller transmission operationally feasible. The reg... (line truncated to 2000 chars)
```

<!-- aegis:purity: own_reg=GDPR; demoted=3; core_cross_mentions=0 -->
