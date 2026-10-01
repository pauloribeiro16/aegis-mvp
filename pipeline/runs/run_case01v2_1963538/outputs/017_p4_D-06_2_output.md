```markdown
### D-06.2 — High-level Security Objective (regulation-neutral)

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-06.2-001 | The manufacturer draws up and maintains a software bill of materials covering the components and dependencies of the product with digital elements in a commonly used and machine-readable format that includes, at minimum, the top-level dependencies, and keeps the SBOM updated throughout the support period. | maintain | Integrity | SO-D-06.2.HL | Annex I Part II (1); Art. 3(39); Art. 13(24) | ID.AM-02, GV.SC-02 | Restated from CRA Sub-SO SG-D-06.2.CRA for an 8-employee B2B SaaS manufacturer in default (self-assessment) class; format is any commonly-used machine-readable format supporting automated component identification pending Art. 13(24) implementing acts; depth floor is first-level direct dependencies with depth-1 look-through; continuous update through the support period per Art. 13(8). |
| AG-D-06.2-002 | The SBOM is included in the technical documentation and retained for the duration of the support period and the 10-year post-market-surveillance tail. | maintain | Accountability | SO-D-06.2.HL | Annex VII §2(b); Annex VII §4; Art. 13(13) | ID.AM-02, GV.SC-03 | Restated from requirement 6.2.1 retention anchor for a self-assessment manufacturer; the SBOM forms part of the Annex VII §2(b) technical documentation bundle surviving the Annex VII §4 retention period (10 years or support period, whichever is longer) per Art. 13(13). |
| AG-D-06.2-003 | On a reasoned request from a market surveillance authority, the manufacturer provides the subset of the SBOM necessary for the authority to check compliance with the Annex I cybersecurity requirements. | achieve | Accountability | SO-D-06.2.HL | Annex VII §8 | ID.AM-02, GV.SC-03 | Restated from requirement 6.2.1 regulatory-disclosure anchor; the `where necessary` scope is the subset of the SBOM directly relevant to the compliance question under investigation, not a comprehensive component dump; the scope decision is documented in the MSA-request log. |
| AG-D-06.2-004 | Where the manufacturer decides to make the SBOM available to users, the location of the SBOM is identified in the product documentation. | achieve | Accountability | SO-D-06.2.HL | Annex II §9 | ID.AM-02 | Restated from requirement 6.2.1 optional user-access anchor; this is a conditional obligation activated only if the manufacturer decides to make the SBOM available externally; for TinyTask Lda.'s B2B SaaS model, external publication is not the default posture and no obligation to publish is created. |

## §4.1 Control Anchor Mapping

| ID | Regulation | CSF 2.0 | NIST PF 1.1 | NIST AI RMF | Source |
|---|---|---|---|---|---|
| AG-D-06.2-001 | CRA | ID.AM-02, GV.SC-02 | — | — | SR-CRA-008 |
| AG-D-06.2-002 | CRA | ID.AM-02, GV.SC-03 | — | — | SR-CRA-053 |
| AG-D-06.2-003 | CRA | ID.AM-02, GV.SC-03 | — | — | SR-CRA-009 |
| AG-D-06.2-004 | CRA | ID.AM-02 | — | — | SR-CRA-109 |

## §5

> ASSUMPTION: GDPR is confirmed as an applicable regulation for TinyTask Lda. in this pack, but the D-06.2 GDPR module explicitly states "No SBOM mandate in GDPR; CRA sole authority per AEGIS taxonomy §4.1" and contains no Sub-SO or requirements. No GDPR-derived goal is produced for this sub-domain; CRA is the sole authority for the manufacturer-side SBOM obligation.

> ASSUMPTION: The Annex II §9 user-facing SBOM access (AG-D-06.2-004) is a conditional obligation at the manufacturer's discretion. For TinyTask Lda.'s B2B SaaS model, external publication of the SBOM is not the default posture; the goal is stated conditionally and does not create an obligation to publish the SBOM externally.
```