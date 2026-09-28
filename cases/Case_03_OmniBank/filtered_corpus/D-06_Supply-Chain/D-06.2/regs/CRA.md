# D-06.2 — CRA module

> Regulation-specific layer: applies when `CRA` is in scope
> (activation: `if CRA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| CRA | SG-CRA-038 | Manufacturer draws up and maintains an SBOM covering the components and dependencies contained in the product with digital elements in a commonly used and machine-readable format that includes, at minimum, the top-level dependencies; on a reasoned request from a market surveillance authority, the SBOM is provided where necessary for the authority to check compliance with the Annex I cybersecurity requirements | Product with digital elements; manufacturer SBOM; Art. 3(39) SBOM definition + Annex I Part II (1) SBOM + Art. 13(24) Commission implementing acts on SBOM format + Annex II §9 SBOM optional user access + Annex VII §2(b) SBOM in technical documentation + Annex VII §8 SBOM on MSA reasoned request; ID.AM-02 + GV.SC-02 + GV.SC-03 |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **CRA (optional, no separate sub-SO)** | user-facing access (Annex II §9) | manufacturer's discretion under Annex II §9 `if the manufacturer decides to make available` | (same format as authoring) | (manufacturer's discretion on depth — typically mirrors the authoring depth) | user / integrator (optional disclosure) | Annex II §9 + Art. 13(18) 10-year information accessibility + Art. 13(1) design-time |

## Sub-SO (CRA)

#### D-06.2.1 — Sub-SO for CRA

```yaml
id: SG-D-06.2.CRA
subdomain: D-06.2
applies_to: [CRA]
inherits_from: SG-CRA-038
source_SR: SR-CRA-008, SR-CRA-052, SR-CRA-053
activation: if CRA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** The manufacturer draws up and maintains an SBOM covering the components and dependencies contained in the product with digital elements in a commonly used and machine-readable format that includes, at minimum, the top-level dependencies (Annex I Part II (1)).

**CSF anchors (from `SR-CRA-008` + `SR-CRA-052` + `SR-CRA-053`
v0.3 security_rationale):**
ID.AM-02, GV.SC-02, GV.SC-03.
*(`SR-CRA-008` covers the Annex I Part II (1) SBOM format
operationalised in NIST CSF 2.0 through **ID.AM-02 (inventories of
software platforms and applications maintained)** and **GV.SC-02
(suppliers and other third parties known, prioritised, and assessed
using a cybersecurity supply-chain risk-management process)**.
ID.AM-02 captures the format-side leg — the inventory must be
queryable and automatable; a `commonly used and machine-readable
format` is the structural requirement that turns the SBOM from a
static artefact into an input to vulnerability-management
automation, CVE matching, and downstream supply-chain risk
assessment. GV.SC-02 anchors the supply-chain dimension — the
format must encode supplier and supply-chain relationships (per the
Art. 3(39) definition), so that the SBOM supports both
vulnerability lookup and supplier-prioritisation under the broader
cybersecurity supply-chain risk-management process. `SR-CRA-052`
covers the Annex I Part II (1) top-level-dependencies floor
operationalised through **ID.AM-02** — the SBOM is the most specific
operational expression of the software-inventory principle in the
product-side cybersecurity domain, with the machine-readable format
qualifier supplying the queryable interface that defenders use to
correlate upstream CVEs against the product's dependency surface.
`SR-CRA-053` covers the Annex VII §2(b) + Annex II §9 + Annex VII
§8 retention-and-disclosure architecture operationalised through
**ID.AM-02 + GV.SC-03 (contracts with suppliers and other third
parties used to implement appropriate measures designed to meet
the objectives of an organisation's cybersecurity programme and the
Cybersecurity Supply Chain Risk Management Plan)**. GV.SC-03
captures the user-facing dimension and the supply-chain
coordination — the Annex II §9 user-facing SBOM access is the
contractual-equivalent transparency lever for voluntary disclosure,
and the SBOM-internal record is the contractual coordination point
with downstream integrators who depend on the SBOM for their own
SR-CRA-050 due-diligence work. Together the three subcategories
enable the manufacturer to demonstrate ex post, through the
documented SBOM in the technical documentation under Annex VII
§2(b), the versioning record, the MSA-request response log under
Annex VII §8, and the optional Annex II §9 user-access record,
that the Annex I Part II (1) SBOM duty has been discharged across
the support period and through the 10-year tail.)*

---


## Security Requirements (CRA)

#### 6.2.1 — Three-anchored SBOM architecture (authoring + retention + regulatory disclosure + optional user access) under Annex I Part II (1) + Annex VII §2(b) + Annex VII §8 + Annex II §9

```yaml
- req_id: 6.2.1
  volere_section: 15
  volere_subtype: audit

  title: "Three-anchored SBOM architecture: machine-readable format covering at least top-level dependencies authored at release + retained in technical documentation under Annex VII §2(b) + disclosed to MSAs on reasoned request under Annex VII §8 + optional user access under Annex II §9"

  derives_from:
    hso_sub_so: SG-D-06.2.CRA
    per_reg_so: SG-CRA-038
    source_sr: SR-CRA-008, SR-CRA-052, SR-CRA-053
    hso_file: ../../HierarchicalSecurityObjectives/D-06_Supply-Chain/D-06.2.md
    objective_ref_section: "### D-06.2.1"

  description: |
    The product shall draw up and maintain an SBOM covering the components and dependencies contained in the product with digital elements in a commonly used and machine-readable format that includes, at minimum, the top-level dependencies (Annex I Part II (1)); the SBOM is included in the technical documentation under Annex VII §2(b) surviving the Annex VII §4 retention period (10 years or support period, whichever is longer) per Art. 13(13) + Art. 13(9); on a reasoned request from a market surveillance authority, the SBOM is provided where necessary for the authority to check compliance with the Annex I cybersecurity requirements (Annex VII §8); the manufacturer may, where it decides to make available an SBOM externally, identify where it is located under Annex II §9 (manufacturer's discretion, no obligation to publish); the format and elements of the SBOM may be further specified by Commission implementing acts under Art. 13(24); the SBOM is the upstream component-identification artefact that feeds the SR-CRA-050 component due diligence in 6.1 and the SR-CRA-007 + SR-CRA-008 + SR-CRA-010 vulnerability identification + remediation in D-02.x (CRA Art. 3(39) SBOM definition + Annex I Part II (1) authoring + Annex VII §2(b) technical-documentation retention + Annex II §9 optional user access + Art. 13(24) Commission implementing acts + Annex VII §8 MSA reasoned request + Art. 13(1) design-time + Art. 13(7) all-cybersecurity-aspects documentation + Art. 13(8) sentence 1 support-period handling + Art. 13(13) 10-year retention + Annex VII §4 retention).

  fit_criterion: |
    A manufacturer-side three-anchored SBOM architecture is operated via ID.AM-02 software-inventory substrate (the SBOM is the most specific operational expression of the software-inventory principle in the product-side cybersecurity domain, with the machine-readable format qualifier supplying the queryable interface that defenders use to correlate upstream CVEs against the product's dependency surface — a `commonly used and machine-readable format` is the structural requirement that turns the SBOM from a static artefact into an input to vulnerability-management automation, CVE matching, and downstream supply-chain risk assessment) + GV.SC-02 supply-chain encoding (the format encodes supplier and supply-chain relationships per the Art. 3(39) definition, so the SBOM supports both vulnerability lookup and supplier-prioritisation under the broader cybersecurity supply-chain risk-management process) + GV.SC-03 retention-and-disclosure architecture (the Annex VII §2(b) technical-documentation layer survives the Annex VII §4 retention period and ties to the type-examination record for Class II products under Annex IV, and the Annex II §9 user-facing SBOM access is the contractual-equivalent transparency lever for voluntary disclosure, with the SBOM-internal record as the contractual coordination point with downstream integrators who depend on the SBOM for their own SR-CRA-050 due-diligence work); the authoring anchor (Annex I Part II (1)) produces an SBOM in a commonly used and machine-readable format covering at minimum the top-level dependencies (POLY-S2 R1 reading per SR-CRA-052 — first-level direct dependencies with depth-1 look-through; depth-discretionary beyond the floor) with the format choice (POLY-S3 R3 reading per SR-CRA-008 — any commonly-used machine-readable format that supports automated component identification, pending the Commission implementing acts under Art. 13(24)) documented in the conformity dossier; the retention anchor (Annex VII §2(b) + Annex VII §4) includes the SBOM in the technical documentation surviving the Annex VII §4 retention period (10 years or support period, whichever is longer) per Art. 13(13) + Art. 13(9) 10-year tail; the regulatory-disclosure anchor (Annex VII §8) provides the SBOM on reasoned request from an MSA with the `where necessary` scope (POLY-S2 R1 reading per SR-CRA-053 — necessary subset directly relevant to the compliance question under investigation, not a comprehensive dump of every component) documented in the MSA-request log; the optional Annex II §9 user-facing access is at the manufacturer's discretion (POLY-S2 R1 reading per SR-CRA-053 — no obligation to publish the SBOM externally; the obligation is only to include it in the technical documentation); the format-migration posture when the Commission implementing acts under Art. 13(24) specify a binding format is documented with versioning evidence across the support period; the SBOM is continuously updated through the support period under Art. 13(8); the three-anchored SBOM architecture operates as the upstream component-identification artefact feeding 6.1 (component due diligence under SR-CRA-050), 2.1 (vulnerability identification under SR-CRA-007), 2.2 (vulnerability remediation under SR-CRA-008 + SR-CRA-010), and 9.4 (technical documentation under SR-CRA-059); verified by Annex VII §2(b) technical-documentation SBOM inclusion review + ID.AM-02 software-inventory substrate audit (format supports automated CVE matching) + GV.SC-02 supplier-relationship encoding review + SBOM versioning records audit + Annex VII §4 retention compliance review + Annex VII §8 MSA-request response log inspection + Annex II §9 user-access posture documentation review + Art. 13(8) continuous-update evidence review + MSA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [6.1.3 (SBOM feeds component-tier inventory substrate under SR-CRA-050 due diligence — the manufacturer integrates the SBOM-derived component inventory into the Art. 13(5) due-diligence procedure)]

  nist_csf: [ID.AM-02, GV.SC-02]

  applicable_if:
    regs: [CRA]
    scope_overlap: N/A   # single-participant sub-domain; CRA is SOLE AUTHORITY for D-06.2 per AEGIS taxonomy §4.1

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

### from regs/CRA.md body — field `verified_relationship`

```yaml
verified_relationship: SOLE-AUTHORITY (CRDA-deep, D-06.2: CRA is the SOLE AUTHORITY for the manufacturer-side SBOM obligation per AEGIS taxonomy §4.1; GDPR, NIS 2, DORA, AI Act are out-of-scope; the Annex I Part II (1) SBOM authoring + Annex VII §2(b) technical-documentation retention + Annex VII §8 MSA reasoned-request disclosure + Annex II §9 optional user access compose the three-anchored (+ optional fourth) SBOM architecture; no CORRECTED, no SCOPE-DISJOINT, no CONTRADICTORY classifications by construction)
```

### from regs/CRA.md body — field `considerations`

```yaml
  considerations: |
    The CRA SBOM obligation is the three-anchored (+ optional fourth) SBOM architecture composed of (1) authoring (Annex I Part II (1)) — manufacturer draws up the SBOM at product release and continuously updates through the support period; (2) retention (Annex VII §2(b) + Annex VII §4) — the SBOM is included in the technical documentation surviving the Annex VII §4 retention period (10 years or support period, whichever is longer) per Art. 13(13) + Art. 13(9) 10-year tail; (3) regulatory disclosure (Annex VII §8) — on reasoned request from an MSA, the SBOM is provided where necessary for compliance checking; (4) optional user-facing access (Annex II §9) — at manufacturer's discretion under `if the manufacturer decides to make available`. The format-floor POLY-S3 (Annex I Part II (1) `commonly used and machine-readable format`) is resolved to R3 per SR-CRA-008 — any commonly-used machine-readable format that supports automated component identification, pending the Commission implementing acts under Art. 13(24); R1 (specific sector format such as SPDX) and R2 (different specific sector format) are currently common in the market but neither is OJ-mandated; R5 (domain-agnostic cryptographic manifest) is admitted as long-run consensus direction but rejected for current OJ reading. The depth-floor POLY-S2 (Annex I Part II (1) `top-level dependencies`) is resolved to R1 per SR-CRA-052 — first-level direct dependencies with depth-1 look-through, honouring the OJ literal `at the very least the top-level dependencies` without forbidding deeper SBOMs at the manufacturer's discretion; R2 (transitive closure) is operationally heavier and rejected as exceeding the literal text; R3 (critical-path-only) is preserved as the rationale behind future implementing-acts expansion. The `where necessary` MSA-disclosure scope POLY-S2 (Annex VII §8) is resolved to R1 per SR-CRA-053 — necessary subset directly relevant to the compliance question under investigation, not a comprehensive dump of every component; R2 (full SBOM disclosure without scope filter) would over-disclose proprietary supply-chain relationships and create an IP tension that Annex VII §8 does not require. The format-choice-must-remain-operational scope caveat is critical: the SBOM must be operational across the support period + 10-year tail, and the format choice must remain machine-readable in tooling that survives the support period; formats depending on proprietary tooling without an open parser are not `commonly used and machine-readable` (the R3 reading per SR-CRA-008 excludes single-vendor or single-tool formats that lack a published specification). The SBOM is the upstream component-identification artefact feeding 6.1 (component due diligence under SR-CRA-050), 2.1 (vulnerability identification under SR-CRA-007), 2.2 (vulnerability remediation under SR-CRA-008 + SR-CRA-010), and 9.4 (technical documentation under SR-CRA-059). For a 5-FTE SaaS startup with CRA applicability, the three anchors are discharged with a documented Annex VII §2(b) artefact bundle + an MSA-request log + an updated SBOM across the support period; the optional Annex II §9 user-facing access is at manufacturer's discretion (typically NOT enabled for B2B products but enabled for consumer products as a trust-signal lever); the format choice defaults to the Annex I Part II (1) `top-level dependencies` floor with a documented R3 format choice (any commonly-used machine-readable format that supports the build-system toolchain). The soft-touch cross-pollination with SR-GDPR-032 `commonly used` ambiguity in Art. 15(3) is an architectural support at the format-selection layer where the manufacturer's CRA-side SBOM format choice and the controller-side GDPR Art. 15(3) portability format choice may share infrastructure (e.g. a single data-catalog machinery) — but the GDPR obligation is data-subject-right-bound and the CRA obligation is manufacturer-side-bound, and the two are not the same obligation; the architectural support does not generate a D-06.2 sub-SO on the GDPR side and does not generate an emergent tension. (Copied from the HSO Considerations block of `### D-06.2.1`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=CRA; demoted=2; core_cross_mentions=0 -->
