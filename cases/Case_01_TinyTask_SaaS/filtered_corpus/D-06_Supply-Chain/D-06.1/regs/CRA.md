# D-06.1 — CRA module

> Regulation-specific layer: applies when `CRA` is in scope
> (activation: `if CRA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| CRA | SO-CRA-037 | Manufacturer exercises due diligence when integrating components sourced from third parties — including components of free and open-source software not made available on the market in the course of a commercial activity — so that those components do not compromise the cybersecurity of the product with digital elements (Art. 13(5) + Art. 13(6) + Art. 3(48) FOSS definition) | Product component integration; manufacturer-driven; `due diligence` procedural + substantive (VAG+POLY-S3, R3 reading); entities up to Art. 3(40) dealer / Art. 3(11) importer responsibilities; GV.SC-01 + GV.SC-02 + ID.RA-02 |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **CRA** | third-party component as technical artefact (manufacturer's component list, including non-commercial OSS per Art. 3(48)) | per-component integration (continuous during support period under Art. 13(8)) + on-becoming-aware of component vulnerability (Art. 13(6) sentence 1) + sharing with component supplier (Art. 13(6) sentence 2) | `due diligence` (VAG+POLY-S3, R3 procedural + substantive per `SR-CRA-050`) + Art. 13(2) risk-assessment propagation across 6 lifecycle phases + Art. 3(48) FOSS inclusion (non-commercial OSS not made available in commercial activity is in scope) + Annex I Part II (1) component identification (SBOM is D-06.2) | market surveillance authority (MSA) — Annex VII §2 technical documentation + Annex VII §3 risk-assessment record + Annex I Part II (1) component identification + Annex II information deliverable | Art. 13(5) + Art. 13(6) + Art. 3(48) FOSS definition + Art. 13(2) risk assessment + Art. 13(8) support-period handling + Annex VII §2 + Annex VII §3 |

## Sub-SO (CRA)

#### D-06.1.3 — Sub-SO for CRA

```yaml
id: SO-D-06.1.CRA
subdomain: D-06.1
applies_to: [CRA]
inherits_from: SO-CRA-037
source_SR: SR-CRA-050
activation: if CRA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** The manufacturer exercises due diligence when integrating components sourced from third parties — including components of free and open-source software not made available on the market in the course of a commercial activity (Art. 3(48) FOSS definition) — so that those components do not compromise the cybersecurity of the product with digital elements (Art. 13(5) sentence 1); on becoming aware of a component vulnerability (Art. 13(6) sentence 1), the manufacturer addresses and remediates it without delay and shares relevant information with the component supplier (Art. 13(6) sentence 2).

**Considerations.**
- The `due diligence` POLY-S3 is resolved to R3 (procedural + substantive) per Annex VII §2 conformity-assessment evidentiary requirements (both documented vetting process and positive verification of security posture).
**CSF anchors (from `SR-CRA-050` v0.3 security_rationale):**
GV.SC-01, GV.SC-02, ID.RA-02.
*(GV.SC-01 anchors the cybersecurity-supply-chain governance
dimension — a cybersecurity supply-chain risk-management plan is
established, implemented, and maintained; the manufacturer's overall
CRA-side supply-chain governance under Art. 13(5) discharges
GV.SC-01 at the product level. GV.SC-02 anchors the supplier-
prioritisation dimension — suppliers (here: third-party component
suppliers) are prioritised by criticality (the component's attack-
surface exposure + the component's exposure to known
vulnerabilities). ID.RA-02 anchors the supplier-risk-intelligence
dimension — threat intelligence is received from and shared with
suppliers and other third parties; the Art. 13(6) component
vulnerability-reporting + sharing leg maps to ID.RA-02 directly.
The three subcategories together enable the manufacturer to
demonstrate ex post, through documented component due-diligence
records, Annex VII §2 / §3 technical-documentation evidence, and
CRA-side CVD-policy + component-vulnerability-sharing records, that
the Art. 13(5) `due diligence` duty has been exercised on each
third-party component (including non-commercial OSS) and that the
Art. 13(6) component-vulnerability-handling leg has been
operationalised.)*

---


## Security Requirements (CRA)

#### 6.1.3 — Third-party-component due diligence including non-commercial OSS per Art. 3(48)

```yaml
- req_id: 6.1.3
  volere_section: 15
  volere_subtype: immunity

  title: "Third-party-component due diligence procedural + substantive including non-commercial OSS per Art. 3(48), with Art. 13(6) vulnerability reporting and Annex VII §2 technical-documentation record"

  derives_from:
    hso_sub_so: SO-6.1.CRA
    per_reg_so: SO-CRA-037
    source_sr: SR-CRA-050
    hso_file: ../../HierarchicalSecurityObjectives/D-06_Supply-Chain/6.1.md
    objective_ref_section: "### 6.1.3"

  description: |
    The product shall exercise due diligence — procedural + substantive R3 reading — when integrating components sourced from third parties, including components of free and open-source software not made available on the market in the course of a commercial activity per Art. 3(48) FOSS definition, so that those components do not compromise the cybersecurity of the product with digital elements; on becoming aware of a vulnerability in a component (including OSS), the vulnerability is reported to the component maintainer and addressed + remediated in the product per Annex I Part II, with code and documentation shared with the OSS maintainer per Art. 13(6) sentence 2; the due-diligence discipline operates across the support period under Art. 13(8) and is documented in the Annex VII §2 technical documentation (CRA Art. 13(5) `due diligence` R3 + Art. 13(6) component vulnerability reporting + Art. 3(48) FOSS definition + Art. 13(2) risk assessment + Art. 13(8) support-period handling + Annex VII §2).

  fit_criterion: |
    A manufacturer-side third-party-component due-diligence discipline is operated via GV.SC-01 documented programme-governance layer (cybersecurity supply chain risk management programme, strategy, objectives, policies, and processes established and agreed by organisational stakeholders, covering commercial and non-commercial OSS components) + GV.SC-02 component inventory + prioritisation by criticality + assessment against documented cybersecurity criteria + ID.RA-02 threat-intelligence loop (CVE feeds, advisories, OSS-security mailing lists); each integrated third-party component — commercial or non-commercial OSS per Art. 3(48) — undergoes the R3 procedural + substantive due diligence reading (documented vetting process evidenced in Annex VII §2, plus positive verification of supplier / component security posture), with OSS-specific calibration (stewardship assessment, CVD policy review, vulnerability disclosure channel, governance-transparency review) per SR-CRA-050 ambiguity_notes; the Art. 13(6) sentence 1 vulnerability-reporting address-and-remediate duty operates on becoming-aware of a component vulnerability, with the Art. 13(6) sentence 2 OSS-sharing limb applying when an OSS component is integrated (code and documentation shared with the OSS maintainer for fix development); the SBOM under Annex I Part II (1) (D-06.2 cross-ref) feeds the component-inventory substrate; the component-tier due-diligence discipline operates at the product-internal boundary only, with the tier hand-off to processor-tier (GDPR leg), supplier-tier (NIS 2 leg), and ICT-provider-tier (DORA leg) documented as the controlled interfaces; verified by GV.SC-01 programme-governance documentation review + GV.SC-02 component-prioritisation records audit + ID.RA-02 threat-intelligence-feed evidence review + Annex VII §2 component-due-diligence rationale review + Annex VII §3 risk-assessment record review + Art. 13(6) component-vulnerability reporting log inspection + MSA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [6.1.1 (when manufacturer is also controller — component-tier feeds processor-tier for personal-data subset), 6.1.2 (when NIS 2 entity deploys/manufactures CRA product — component-tier feeds supplier-tier on the manufacturer-entity relationship), 6.1.4 (when DORA FE deploys CRA product — typically scope-disjoint because distinct actors handle distinct objects; conditional when integrated manufacturer-financial-entity controller), 6.2.1 (SBOM feeds component-tier inventory substrate per Annex I Part II (1))]

  nist_csf: [GV.SC-01, GV.SC-02, ID.RA-02]

  applicable_if:
    regs: [CRA]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (CRA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**CRA article (verbatim, Art. 13(5) + Art. 3(48)):**
> "Manufacturers shall exercise due diligence when integrating components sourced from third parties — including components of free and open-source software not made available on the market in the course of a commercial activity — so that those components do not compromise the cybersecurity of the product with digital elements." — CRA Art. 13(5) sentence 1
>
> "'free and open-source software' means software the source code of which is openly shared and which is made available under a free and open-source licence … for the study, modification and distribution by its users …" — CRA Art. 3(48)

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/CRA.md body — field `verified_relationship`

```yaml
verified_relationship: DIFFERENT-PERSPECTIVE (CRDA-deep, D-06.1: GDPR↔CRA = DIFFERENT-PERSPECTIVE (SAME — entity-level processor vs product-level component); NIS2↔CRA = DIFFERENT-PERSPECTIVE (SAME — entity-level supplier vs product-level component); CRA↔DORA = DIFFERENT-PERSPECTIVE (SAME — upstream product-level vs midstream entity-level ICT provider))
```

### from regs/CRA.md body

- The Art. 3(48) FOSS inclusion is the CRA-specific operational handle that GDPR / NIS 2 / DORA do not separately replicate; non-commercial OSS components are in scope where the OSS becomes a component of the product with digital elements placed on the Union market.

### from regs/CRA.md body

- CRA ↔ DORA = DIFFERENT-PERSPECTIVE (typically scope-disjoint in baseline): CRA is upstream (manufacturer's inputs), DORA is midstream (deployer's ICT providers); the manufacturer and the financial entity are typically different parties.

### from regs/CRA.md body

- GDPR ↔ CRA = DIFFERENT-PERSPECTIVE: GDPR processor due diligence is on the entity; CRA third-party component due diligence is on the components; the two layers stack vertically on the integrated manufacturer-controller-deployer.


### from regs/CRA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # CRA↔GDPR = Conditional (Y integrated manufacturer-controller stack; disjoint baseline: product-component ↔ data-processing-counterparty); CRA↔NIS2 = Conditional (Y NIS 2 entity deploys/manufactures CRA product; disjoint baseline: product-component ↔ supplier-relationship); CRA↔DORA = Conditional (typically N — distinct actors at different supply-chain levels; Y when integrated manufacturer-financial-entity controller); HL engages on overlap

```

### from regs/CRA.md body — field `considerations`

```yaml
  considerations: |
    The CRA vendor-risk-assessment obligation is the third-party-component due diligence procedural + substantive on the manufacturer's component list, including non-commercial OSS per Art. 3(48) FOSS definition; the operational substrate is an intra-product component due-diligence discipline that covers commercial and non-commercial OSS components alike. The `due diligence` POLY-S3 ambiguity is resolved to R3 (procedural + substantive) per SR-CRA-050 ambiguity_notes — R1 (procedural only) and R2 (substantive only) are both rejected as insufficient. The OSS-inclusion limb is CRA-unique among the four 6.1 regulators and the key CRA-specific operational handle that GDPR / NIS 2 / DORA do not separately replicate: a non-commercial OSS maintainer is typically not a processor in the GDPR sense, may not be a `direct supplier` in the NIS 2 sense, and may not be an ICT third-party service provider in the DORA sense — the CRA Art. 13(5) due diligence applies with OSS-specific calibration (stewardship assessment, CVD policy review, vulnerability disclosure channel, governance-transparency review). The third-party-component target object is distinct from the GDPR processor-as-legal-entity, the NIS 2 direct-supplier-as-relationship, and the DORA ICT-third-party-as-financial-entity-counterparty — the four target objects are layered not collapsed (CRA is upstream — manufacturer's inputs; DORA is midstream — deployer's ICT providers; GDPR / NIS 2 are downstream — deployer's own supplier due diligence). The Art. 13(6) component-vulnerability reporting limb (sentence 1) and the OSS-sharing limb (sentence 2) are CRA-unique feedback-loop duties; the upstream feedback path feeds component-maintainer fixes and the in-product remediation addresses the component vulnerability in the manufacturer's product per Annex I Part II. Remain open: (a) whether the implementing acts under Art. 13(24) will specify minimum due-diligence evidentiary content (e.g. signed attestations of CVE-monitoring posture, vulnerability-handling SLA disclosure); (b) the operational status of due diligence for indirect dependencies (transitive depth beyond the SBOM top-level floor) where the manufacturer has no visibility. (Copied from the HSO Considerations block of `### 6.1.3`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=CRA; demoted=6; core_cross_mentions=2 -->