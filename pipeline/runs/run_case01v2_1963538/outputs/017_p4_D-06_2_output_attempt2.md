```markdown
### D-06.2 — Software Bill of Materials (SBOM)

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-06.2-001 | The manufacturer draws up and maintains a software bill of materials (SBOM) covering the components and dependencies in the product with digital elements, in a commonly used and machine-readable format including at minimum the top-level dependencies; the SBOM is retained in the technical documentation through the support period and the 10-year retention tail; on a reasoned request from a market surveillance authority, the SBOM is provided where necessary for the authority to check compliance with the Annex I cybersecurity requirements. | maintain | accountability | SO-D-06.2.HL | Annex I Part II (1); Annex VII §2(b); Annex VII §8; Art. 3(39) | ID.AM-02, GV.SC-02 | Restated from the corpus baseline for TinyTask's 8-employee B2B SaaS scale — the three-anchored SBOM architecture (authoring, retention, MSA disclosure) is discharged with a documented technical-documentation artefact bundle and an MSA-request log; the optional Annex II §9 user-facing access is at manufacturer's discretion and not enabled by default for B2B products; GDPR confirmed in pack but carries no SBOM obligation in this sub-domain (CRA sole authority per AEGIS taxonomy §4.1). |

## §4.1 Control Anchor Mapping

| ID | Regulation | CSF 2.0 | NIST PF 1.1 | NIST AI RMF | Source |
|---|---|---|---|---|---|
| AG-D-06.2-001 | GDPR | — | — | — | — |
| AG-D-06.2-001 | CRA | ID.AM-02, GV.SC-02 | — | — | SR-CRA-008 |

## §5

> ASSUMPTION: GDPR is confirmed in the pack for sub-domain D-06.2 but the module explicitly states "no GDPR Sub-SO or requirements in this sub-domain" and "No SBOM mandate in GDPR; CRA sole authority per AEGIS taxonomy §4.1." The GDPR row in §4.1 therefore carries no anchors and no source; no GDPR-derived goal is emitted.

> ASSUMPTION: The optional Annex II §9 user-facing SBOM access is at the manufacturer's discretion ("if the manufacturer decides to make available"). For TinyTask's B2B SaaS product, this optional anchor is assumed not to be enabled by default; it does not generate a separate obligation or goal.
```