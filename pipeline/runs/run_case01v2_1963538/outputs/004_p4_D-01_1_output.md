```markdown
### D-01.1 — Data at rest: encryption and key custody

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-01.1-001 | Personal data at rest in TinyTask's managed-cloud storage (customer account metadata and customer task data) is maintained under encryption with key custody logically separated from data access, calibrated to the five Art. 32(1) preamble factors in the company's risk assessment. | maintain | C | SO-D-01.1.HL | GDPR Art. 5(1)(f); Art. 32(1)(a); Art. 32(1)(b) | PR.DS-01, PR.DS-10 | Restated from the corpus "appropriate technical measures" to TinyTask's 8-person managed-cloud deployment where the company acts as both controller (customer accounts) and processor (customer task data); the "appropriate" threshold is operationalised through the five Art. 32(1) preamble factors in the company's risk assessment, and managed-cloud hosting means technical implementation is partly delegated while the obligation remains with TinyTask. |
| AG-D-01.1-002 | The TinyTask SaaS product (web and mobile interface) maintains state-of-the-art encryption of all stored data — personal or other — at the product level, rendering data unintelligible to any person not authorised to access it, with key custody functionally separated by role-based access control. | maintain | C | SO-D-01.1.HL | CRA Annex I Part I (1); Annex I Part I (2)(e) | PR.DS-01 | Restated from the corpus baseline to TinyTask's role as manufacturer of a default-class product with digital elements under self-assessment conformity; the state-of-the-art floor is a product-level obligation distinct from the GDPR deployment-level obligation, and the "render unintelligible" test applies to all data stored by the product (not only personal data). |

## §4.1 Control Anchor Mapping

| ID | Regulation | CSF 2.0 | NIST PF 1.1 | NIST AI RMF | Source |
|---|---|---|---|---|---|
| AG-D-01.1-001 | GDPR | PR.DS-01, PR.DS-10 | PR.DS-P1, PR.PO-P3 | — | SR-GDPR-001 |
| AG-D-01.1-002 | CRA | PR.DS-01 | — | — | SR-CRA-002 |

## §5

> ASSUMPTION: The cross-regulation analysis (CRDA-deep, all 6 pairs SAME) confirms that meeting the CRA state-of-the-art floor discharges the GDPR "appropriate" obligation on the at-rest dimension for the same product artefact; however, the GDPR controller's deployment-side risk assessment and cipher-strength selection remain TinyTask's own obligation independent of the CRA product-level baseline (scope caveat in cross/_interactions.md).

> ASSUMPTION: TinyTask's managed-cloud hosting arrangement means the physical encryption implementation is partly delegated to the cloud provider; the obligation to ensure "appropriate technical measures" (GDPR) and "state-of-the-art mechanisms" (CRA) remains with TinyTask as controller/processor and manufacturer respectively, and the company's risk assessment must evidence that the delegated implementation meets the applicable threshold.

> OPEN QUESTION: Data scale (rough figure) is not stated in the intake (fact_sheet open_questions); the "appropriate" threshold under the Art. 32(1) preamble factors (costs of implementation, nature, scope, context, purposes, risks) may be affected by data volume, and the company's risk assessment should record the scale assumption.
```