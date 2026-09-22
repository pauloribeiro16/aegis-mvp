# D-06.3 — NIS 2 module

> Regulation-specific layer: applies when `NIS2` is in scope
> (activation: `if NIS2 in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| NIS2 | SO-NIS2-015; SO-NIS2-016 | Direct suppliers and service providers are assessed on supplier-specific vulnerabilities, product/service quality, cybersecurity practices, secure-development procedures, and EU-level coordinated supply-chain risk-assessment outputs | Entity-side direct-supplier contractual and assessment layer; Member-State-transposition-sensitive `direct` scope-limiter |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **NIS2** | direct supplier/service-provider relationship | continuous supply-chain security; per-supplier assessment; availability of Art. 22 coordinated assessment | supplier-risk register; security-related contract terms; three-prong assessment evidence | CSIRT or competent authority | Art. 21(2)(d); Art. 21(3); Art. 22 |

## Sub-SO (NIS 2)

#### D-06.3.2 — Sub-SO for NIS 2

```yaml
id: SO-D-06.3.NIS2
subdomain: D-06.3
applies_to: [NIS2]
inherits_from: [SO-NIS2-015, SO-NIS2-016]
source_SR: [SR-NIS2-020, SR-NIS2-021, SR-NIS2-022, SR-NIS2-023, SR-NIS2-024, SR-NIS2-025]
activation: if NIS2 in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Essential and important entities manage contractual security for direct supplier and service-provider relationships by documenting the supplier universe under the `direct` scope-limiter, embedding security-related contractual aspects into supplier relationships, and assessing each direct supplier against the Art. 21(3) three-prong supplier-assessment structure (supplier-specific vulnerabilities + overall quality of products/services and cybersecurity practices + supplier secure-development procedures); Art. 22 coordinated supply-chain risk assessments are taken into account where available.

**CSF anchors (from NIS 2 SRs):** GV.SC-02, GV.SC-03, GV.SC-04, ID.AM-04, ID.RA-01, ID.RA-02, PR.PS-06.

---


## Security Requirements (NIS 2)

#### 6.3.2 — Art. 21(2)(d) direct-supplier contracts + Art. 21(3) three-prong assessment evidence + Art. 22 coordinated-assessment inputs

```yaml
- req_id: 6.3.2
  volere_section: 15
  volere_subtype: immunity

  title: "Art. 21(2)(d) direct-supplier contractual-security embedding + Art. 21(3) three-prong assessment evidence + Art. 22 coordinated-assessment ingestion"

  derives_from:
    hso_sub_so: SO-D-06.3.NIS2
    per_reg_so: SO-NIS2-015, SO-NIS2-016
    source_sr: SR-NIS2-020, SR-NIS2-021, SR-NIS2-022, SR-NIS2-023, SR-NIS2-024, SR-NIS2-025
    hso_file: ../../HierarchicalSecurityObjectives/D-06_Supply-Chain/D-06.3.md
    objective_ref_section: "### D-06.3.2"

  description: |
    The product shall embed security-related contractual aspects into each direct supplier/service-provider relationship under Art. 21(2)(d) (with R1 Tier-1 contractual as minimum + R2 technically integrated + R3 operationally dependent per Recital 56), maintain documented Art. 21(3) sentence 1 three-prong supplier-assessment evidence per direct supplier (supplier-specific vulnerabilities + overall quality of products/services and cybersecurity practices + supplier secure-development procedures), and ingest Art. 22 EU-level coordinated supply-chain risk-assessment outputs where available — NIS 2 remains separate operational handle from GDPR DPA and from DORA Art. 30, with CRA Art. 13(6) component-vulnerability reporting as the upstream feedback path.

  fit_criterion: |
    A direct-supplier contractual-security matrix is maintained covering each in-scope direct supplier via Art. 21(2)(d) `direct` scope-limiter with R1 Tier-1 contractual as minimum + R2 technically integrated + R3 operationally dependent per Recital 56 risk-management-precaution principle; security-related contractual aspects are embedded via documented contract clauses or schedules covering incident notification, audit cooperation, security-measure commitments, vulnerability disclosure, and termination-for-cause; Art. 21(3) sentence 1 three-prong supplier-assessment evidence is maintained per supplier covering (i) supplier-specific vulnerabilities via ID.RA-01 + ID.RA-02 + CVE feeds + vendor advisories + sectoral CSIRT notifications, (ii) overall quality of products/services and cybersecurity practices via GV.SC-04 audit/test-result/certification records, (iii) supplier secure-development procedures via externally-assessable interpretation (questionnaire / contract clause / third-party attestation); Art. 21(3) sentence 2 EU-level coordinated assessment outputs (Cooperation Group + Commission + ENISA under Art. 22(1)) are ingested in supplier-risk decisions; in DORA overlap (financial entity = NIS 2 essential entity), DORA Art. 30 9-element ICT-contract list satisfies NIS 2 contractual-security floor (DORA-exceeds-NIS 2); the GDPR DPA layer adds data-protection-specific clauses when controller-NSIE combined; CRA Art. 13(6) component-vulnerability reporting provides the upstream post-contract feedback path (NIS2↔CRA lifecycle hinge) without converting CRA into DPA-style contract; verified by supplier-contractual-security matrix review + Art. 21(3) three-prong per-supplier assessment evidence inspection + GV.SC-04 audit/test-result records review + Art. 22 EU-level coordinated-assessment inputs integration evidence + CSIRT-or-competent-authority inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [6.1.2 (supplier-register and three-prong assessment feeds direct-supplier contractual-security matrix; the assessment object is preserved across assessment-arch and contract-arch layers)]

  nist_csf: [GV.SC-02, GV.SC-03]

  applicable_if:
    regs: [NIS2]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (NIS 2)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**NIS 2 article (verbatim, Art. 21(2)(d) + Art. 21(3) sentence 1):**
> "… supply chain security including security-related aspects concerning the relationships between each entity and its direct suppliers or service providers." — NIS 2 Art. 21(2)(d)
>
> "When considering which of the measures referred to in the first subparagraph are appropriate, essential and important entities shall take into account the vulnerabilities specific to each direct supplier and service provider, the overall quality of products and cybersecurity practices of their suppliers and service providers, including their secure development procedures, and the results of coordinated security risk assessments of critical supply chains …" — NIS 2 Art. 21(3)

**NIS 2 article (verbatim, Art. 21(3) sentence 1):**
> "When considering which of the measures referred to in the first subparagraph are appropriate, essential and important entities shall take into account the vulnerabilities specific to each direct supplier and service provider, the overall quality of products and cybersecurity practices of their suppliers and service providers, including their secure development procedures …" — NIS 2 Art. 21(3)

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/NIS2.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-06.3: GDPR↔NIS2 = COMPLEMENTARY; NIS2↔CRA = COMPLEMENTARY; NIS2↔DORA = EQUAL with DORA exceeding NIS 2 in the financial-services subset)
```

### from regs/NIS2.md body

**Considerations.**

- In overlap with DORA, DORA's Art. 30 contract list may satisfy the NIS 2 open-textured contractual-security floor for financial entities, but the NIS 2 `direct` scope-limiter and Member-State-transposition evidence remain separate operational handles.

### from regs/NIS2.md body

- CRA component-vulnerability reporting under Art. 13(6) provides the post-contract upstream feedback path (the NIS2↔CRA lifecycle hinge); CRA does not convert into a DPA-style contract.


### from regs/NIS2.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # NIS2↔GDPR = Y (controller-NSIE; supplier-contract and DPA coexist); NIS2↔CRA = Conditional (Y NIS 2 entity deploys CRA product; supplier-contract coexists with CRA market-access duties — lifecycle hinge via Art. 13(6)); NIS2↔DORA = Y (DORA-exceeds-NIS 2 discharge in financial-services subset; NIS 2 supply-chain-security chapeau extends to physical + operational hazards via lex specialis analysis)

```

### from regs/NIS2.md body — field `considerations`

```yaml
  considerations: |
    The NIS 2 contractual-security obligation is the direct-supplier-as-relationship security embedding + Art. 21(3) sentence 1 three-prong supplier-assessment evidence chain; the operational substrate is a direct-supplier contractual-security matrix anchored on the Art. 21(2)(d) `direct` scope-limiter, security-related contract clauses, and the three-prong assessment record per supplier. The `direct` scope-limiter is the single most consequential SCOPE-Q ambiguity in Chapter IV — three materially distinct readings (R1 contractually bound Tier-1, R2 technically integrated, R3 operationally dependent SPOF); chosen reading is R1 as the minimum + R2/R3 per Recital 56. Member-State transposition divergence may apply (German BSI favours R1+R3; French ANSSI favours R2+R3; both may signal forthcoming n-hop obligations in critical sectors). In DORA overlap, DORA Art. 30 9-element ICT-contract list satisfies the NIS 2 open-textured contractual-security floor for financial entities (DORA-exceeds-NIS 2 discharge); the NIS 2 `direct` scope-limiter and Member-State-transposition evidence remain separate operational handles. CRA Art. 13(6) component-vulnerability reporting provides the upstream post-contract feedback path (NIS2↔CRA lifecycle hinge) — CRA does not convert to DPA-style contract. (Copied from the HSO Considerations block of `### D-06.3.2`; preserved here for self-containment per Volere shell `considerations` field definition.)
```

<!-- aegis:purity: own_reg=NIS2; demoted=5; core_cross_mentions=2 -->
