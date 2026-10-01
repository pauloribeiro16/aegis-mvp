```markdown
### D-03.1 — Identity Lifecycle Management

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-03.1-001 | When a natural person (business customer or end-user of a customer) submits a data-subject rights request (Art. 15–22) to TinyTask as controller, the identity of the requester is verified using reasonable means proportionate to the risk of mis-identification before the request is actioned; the controller may request additional information necessary to confirm identity, and the verification scope is limited to the minimum information required (Art. 5(1)(c) minimisation), with a documented graduated-verification standard and proportionality justification per request class. | achieve | privacy-right | SO-D-03.1.HL | GDPR Art. 12(6); Art. 11(2); Art. 5(1)(c) | PR.AA-03, PR.AA-02 | Restated for an 8-employee B2B SaaS controller handling low-volume rights requests from business customers and their end-users; graduated verification and minimisation register scaled to the company's data categories (customer account metadata, task data) and managed-cloud hosting context. |
| AG-D-03.1-002 | Identities, credentials, and access entitlements for product users, service identities, and integrated components of TinyTask's SaaS platform are managed in a verifiable manner throughout the product's operational lifetime, with type/batch/serial unique identification backing the identity register and a documented single point of contact for identity-related queries (Art. 13(17)). | maintain | accountability | SO-D-03.1.HL | CRA Annex I Part I (2)(d); Art. 13(15); Art. 13(17); Annex II §3 | PR.AA-01, ID.AM-01 | Restated for an 8-employee manufacturer of a default-class B2B SaaS product; verifiable-manner obligation applied to the product's user accounts, internal service identities, and third-party integrated components (e.g., external payment provider); operational-lifetime scope aligned with the SaaS subscription model and self-assessment conformity path. |

## §4.1 Control Anchor Mapping

| ID | Regulation | CSF 2.0 | NIST PF 1.1 | NIST AI RMF | Source |
|---|---|---|---|---|---|
| AG-D-03.1-001 | GDPR | PR.AA-03, PR.AA-02, ID.AM-08 | PR.AC-P6, PR.AC-P3, CT.DP-P4 | — | SR-GDPR-009, SR-GDPR-010 |
| AG-D-03.1-002 | CRA | PR.AA-01, ID.AM-01, PR.AA-05, PR.AA-06, DE.CM-09 | — | — | SR-CRA-023, SR-CRA-024 |

## §5

> ASSUMPTION: Per the cross-regulation aggregation logic (cross/_interactions.md), the CRA "verifiable manner" floor discharges the GDPR "reasonable means proportionate to risk" on the identity-management dimension when TinyTask operates both manufacturer-side and controller-side roles on the same identity substrate; the evidence layer must document which artefacts support which regulatory role.

> ASSUMPTION: The boundary between the GDPR data-subject verification discipline (AG-D-03.1-001) and the CRA product-user identity-management discipline (AG-D-03.1-002) is a controlled hand-off at the rights-exercise endpoint; the two goals are layered, not collapsed, and the identity-subject divergence (external data subjects vs. product users/services/components) is preserved in separate evidence templates.

> OPEN QUESTION: Data scale (rough volume of rights requests and records) is not stated in the intake; the proportionality calibration of the graduated-verification standard in AG-D-03.1-001 (e.g., which request classes trigger document verification vs. strong authentication) depends on this figure and should be confirmed before Phase 2 objective refinement.
```