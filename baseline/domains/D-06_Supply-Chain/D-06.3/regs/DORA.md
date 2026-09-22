# D-06.3 — DORA module

> Regulation-specific layer: applies when `DORA` is in scope
> (activation: `if DORA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| DORA | SO-DORA-012; SO-DORA-011 (standards link) | ICT third-party contractual arrangements clearly allocate rights and obligations in writing, include the Art. 30(2) minimum elements, and comply with Art. 28(5) information-security standards; CIF contracts add Art. 30(3) clauses | Financial-entity ICT third-party contractual layer; competent-authority-facing evidence; CIF escalator |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **DORA** | ICT third-party contractual arrangement | per-ICT-service contract; CIF support; standards compliance | Art. 30(2) 9-element contract; Art. 28(5) standards record; CIF clauses under Art. 30(3) | competent authority; financial entity; resolution authorities where applicable | Art. 28(1); Art. 28(5); Art. 30(1)–(3) |

## Sub-SO (DORA)

#### D-06.3.4 — Sub-SO for DORA

```yaml
id: SO-D-06.3.DORA
subdomain: D-06.3
applies_to: [DORA]
inherits_from: [SO-DORA-011, SO-DORA-012]
source_SR: [SR-DORA-019, SR-DORA-020, SR-DORA-021, SR-DORA-022]
activation: if DORA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Financial entities structure ICT third-party contractual arrangements so that rights and obligations are clearly allocated and set out in writing, the Art. 30(2)(a)–(i) minimum elements are present, Art. 28(5) information-security standards are contractually evidenced, and contractual arrangements supporting critical or important functions include the additional CIF clauses required under Art. 30(3) (including unrestricted access/inspection/audit rights where applicable).

**CSF anchors (from DORA SRs):** GV.SC-01, GV.SC-02, GV.SC-03, GV.SC-04, ID.AM-04, DE.CM-06.

---


## Security Requirements (DORA)

#### 6.3.4 — Art. 30(1)+(2) 9-element ICT-contract + Art. 28(5) standards + Art. 30(3) CIF-only clauses

```yaml
- req_id: 6.3.4
  volere_section: 15
  volere_subtype: immunity

  title: "Art. 30(1)+(2) 9-element ICT-contract closed-list + Art. 28(5) standards record + Art. 30(3) CIF-only clauses (audit/access/exit) — clause-list union with GDPR Art. 28(3) when same ICT provider is processor"

  derives_from:
    hso_sub_so: SO-D-06.3.DORA
    per_reg_so: SO-DORA-011, SO-DORA-012
    source_sr: SR-DORA-019, SR-DORA-020, SR-DORA-021, SR-DORA-022
    hso_file: ../../HierarchicalSecurityObjectives/D-06_Supply-Chain/D-06.3.md
    objective_ref_section: "### D-06.3.4"

  description: |
    The product shall structure ICT third-party contractual arrangements so that rights and obligations are clearly allocated and set out in writing per Art. 30(1), incorporate the Art. 30(2)(a)–(i) 9-element minimum ICT-contract list, evidence Art. 28(5) information-security standards contractually (most up-to-date and highest quality for CIF per Art. 28(5) sentence 2; appropriate standards for non-CIF per Art. 28(5) sentence 1), and add Art. 30(3)(a)–(f) CIF-only clauses for critical or important functions (including audit rights, exit-strategy provisions, and concentration-risk identification per Art. 28(4)) — the CORRECTED CRDA pair resolves to clause-list union with GDPR Art. 28(3) when same ICT provider is processor; DORA-exceeds-NIS 2 in financial-services subset.

  fit_criterion: |
    A financial-entity ICT-contract matrix is maintained for each ICT third-party service-provider relationship, with Art. 30(1) clear written allocation of rights and obligations and the Art. 30(2)(a)–(i) 9-element closed-list minimum clauses present in each contract: (a) clear description of functions / ICT services / objectives + (b) effective date + duration + notice periods + (c) locations (data processing, storage, support, service performance) + (d) termination / exit-strategy provisions + (e) financial-entity and competent-authority access/inspection/audit rights per Art. 30(3)(e)(i)/(ii) + alternative-assurance exception only where other clients' rights are affected + (f) SLA + monitoring + reporting + (g) partial/full-substitution provisions + (h) cost allocation + (i) contingency arrangements; Art. 28(5) sentence 1 `appropriate information security standards` applies to non-CIF contracts; Art. 28(5) sentence 2 `most up-to-date and highest quality information security standards` is the CIF escalator for arrangements supporting critical or important functions; Art. 30(3)(a)–(f) CIF-only clauses are added for CIF support (audit-rights framework, on-site documentation-copy right, exit-strategy + transition support, sub-outsourcing restrictions, termination triggers for non-performance); Art. 28(4) concentration-risk identification accompanies CIF support (alternative ICT providers, re-internalisation feasibility); in GDPR overlap (same ICT provider is processor), the contract applies the **clause-list union** of GDPR Art. 28(3) 8-element DPA + DORA Art. 30 9-element ICT-contract list, with GDPR-specific processor terms retained whenever the ICT provider processes personal data (CORRECTED CRDA pair from CONTRADICTORY to COMPLEMENTARY — UNION, NOT substitution); in NIS 2 overlap (financial entity is also NIS 2 essential entity), DORA Art. 30 satisfies NIS 2 `security-related contractual aspects` floor (DORA-exceeds-NIS 2 discharge) — NIS 2 chapeau extends to physical + operational hazards via lex specialis analysis; verified by ICT-contract matrix inspection + Art. 30(2)(a)–(i) 9-element closed-list clause-inventory attestation review + Art. 28(5) standards record review + Art. 30(3) CIF-clause review when CIF support + clause-list union attestation when GDPR overlap + concentration-risk identification record review + national-financial-supervisory-authority-or-competent-authority inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [6.1.4 (ICT-third-party risk assessment + four-factor proportionality shapes contract depth and CIF designation), 6.3.1 (clause-list union when same ICT provider is processor — GDPR-specific clauses retained; this is the operative effect of the CORRECTED CRDA pair), 6.4.4 (CIF audit/access rights are the boundary-side handle that backs up the contractual CIF clauses; per Art. 30(3)(e)(i)/(ii))]

  nist_csf: [GV.SC-01, GV.SC-02, GV.SC-03, GV.SC-04, ID.AM-04, DE.CM-06]

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

**DORA article (verbatim, Art. 30(1)+(2)):**
> "The rights and obligations of the financial entity and of the ICT third-party service provider shall be clearly allocated and set out in writing … The contractual arrangements shall include, at least, the following elements: (a) a clear description of all functions and ICT services to be provided by the ICT third-party service provider … (b) the locations where the contracted and subcontracted functions and ICT services are to be provided and where the data are to be processed, including the storage location, and an obligation for the ICT third-party service provider to notify the financial entity in advance if it intends to change those locations; (c)) provisions on the availability, authenticity, integrity and confidentiality of the data, including the protection of data during transmission and processing; (d) provisions on ensuring access, recovery and return of the personal and non-personal data of the financial entity in the case of insolvency, resolution or termination of the ICT third-party service provider; (e) service level descriptions, including updates and revisions thereto; (f) the obligation of the ICT third-party service provider to provide assistance to the financial entity in the event of an ICT-related incident … at no extra cost or at a cost determined ex ante; (g) the obligation of the ICT third-party service provider to cooperate fully with the competent authority and the resolution authorities of the financial entity; (h) termination rights and related minimum notice periods for the financial entity … (i) conditions for participation of the ICT third-party service provider in the ICT security awareness programmes and digital operational resilience training of the financial entity …" — DORA Art. 30(1)+(2)(a)–(i)


## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/DORA.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-06.3: GDPR↔DORA = CORRECTED — COMPLEMENTARY clause-list union; NIS2↔DORA = EQUAL with DORA exceeding NIS 2; CRA↔DORA = DIFFERENT-PERSPECTIVE)
```

### from regs/DORA.md body

**Considerations.**

- In overlap with GDPR, the contract must contain the union of GDPR Art. 28(3) and DORA Art. 30 clauses; DORA does not erase the GDPR-specific data-processing terms (the CORRECTED CRDA pair from CONTRADICTORY to COMPLEMENTARY is resolved as clause-list union).

### from regs/DORA.md body

- In overlap with NIS 2, DORA operationalises the NIS 2 open-textured supplier-contract requirement for financial entities, while NIS 2 remains the floor outside that subset.

### from regs/DORA.md body

- CRA importer/distributor economic-operator duties and DORA ICT-service contracts operate at different supply-chain layers (market-access vs ICT service); the two obligations compose when a CRA-classified product is procured by a financial entity through importer/distributor channels.


### from regs/DORA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # DORA↔GDPR = Y (clause-list union — CORRECTED CRDA pair — same ICT provider can be processor and DORA ICT third party); DORA↔NIS2 = Y (DORA-exceeds-NIS 2 discharge in financial-services subset; NIS 2 chapeau extends to physical + operational hazards); DORA↔CRA = Conditional (N in baseline because CRA is market-access and DORA is contract; Y when CRA product procured as financial-entity ICT service)

```

### from regs/DORA.md body — field `considerations`

```yaml
  considerations: |
    The DORA contractual-security obligation is the financial-entity ICT-contract structure under Art. 30(1) + Art. 30(2) 9-element minimum list + Art. 28(5) standards compliance + Art. 30(3) CIF-only clauses; the operational substrate is a financial-entity ICT-contract matrix keyed by ICT provider relationship / CIF status / processor-overlap / NIS 2-overlap. The `critical or important functions` undefined distinction is the central DORA ambiguity — appears in 18 of 38 DORA clauses without ever being defined; the chosen reading is that both categories are in scope and distinct obligations may attach to each, pending EBA RTS clarity. The Art. 28(5) CIF escalator — `most up-to-date and highest quality information security standards` — is the DORA-unique strictness floor applying only to CIFs; non-CIF contracts apply Art. 28(5) sentence 1 `appropriate information security standards`. In GDPR overlap, the CORRECTED CRDA pair (CONTRADICTORY → COMPLEMENTARY) is the central resolution: the contract applies clause-list union of GDPR Art. 28(3) 8-element DPA + DORA Art. 30 9-element ICT-contract list, with GDPR-specific processor terms retained whenever the ICT provider processes personal data (UNION, NOT substitution). In NIS 2 overlap (financial entity is also NIS 2 essential entity), DORA Art. 30 satisfies NIS 2 `security-related contractual aspects` floor (DORA-exceeds-NIS 2 discharge in financial-services subset) — NIS 2 chapeau extends to physical + operational hazards via lex specialis analysis. CRA importer/distributor economic-operator duties and DORA ICT-service contracts operate at different supply-chain layers (market-access vs ICT service); the two obligations compose when a CRA-classified product is procured by a financial entity through importer/distributor channels. (Copied from the HSO Considerations block of `### D-06.3.4`; preserved here for self-containment per Volere shell `considerations` field definition.)
```

### from regs/DORA.md body

**DORA article (verbatim, Art. 30(1)+(2)):**

> (See GDPR↔DORA pair above for the verbatim 9-element list.)

<!-- aegis:purity: own_reg=DORA; demoted=7; core_cross_mentions=4 -->