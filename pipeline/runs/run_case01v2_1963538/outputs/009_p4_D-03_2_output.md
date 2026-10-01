```markdown
### D-03.2 — Authentication Mechanism Strength

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-03.2-001 | TinyTask's 8-employee workforce and its external payment sub-processor personnel, when authorised to process personal data (customer account metadata, task data), act only on documented instructions from TinyTask as controller or processor and remain bound by a confidentiality obligation; no authentication-strength threshold is imposed by this obligation. | maintain | Confidentiality | SO-D-03.2.HL | GDPR Art. 28(3)(b); Art. 29 | PR.AA-05, PR.AA-06 | Narrowed from the generic "persons authorised to process personal data" to TinyTask's 8-employee workforce plus its single external payment sub-processor; the obligation is the documented-instructions + confidentiality wrapper (silent around authentication strength), not an authentication-strength mandate. |
| AG-D-03.2-002 | When a data subject (business customer or the customer's end-user) exercises a rights request against TinyTask, the requester's identity is verified using reasonable means proportionate to the risk of mis-identification, calibrated to the 8-employee operational scale. | achieve | privacy-right | SO-D-03.2.HL | GDPR Art. 12(6); Art. 11(2) | PR.AA-06 | Scoped to TinyTask's B2B context where data subjects are business customers and their end-users; "reasonable means proportionate to risk" is interpreted at 8-employee scale (account-credential verification + contextual confirmation rather than a dedicated verification team); no authentication-strength threshold is imposed. |
| AG-D-03.2-003 | The TinyTask SaaS product (web and mobile interface) protects against unauthorised access through appropriate control mechanisms, which may include authentication, identity, or access-management systems, appropriate to the identified cybersecurity risk of the product; the mechanism selection is at TinyTask's discretion as manufacturer under the 3-way OR. | maintain | Confidentiality | SO-D-03.2.HL | CRA Annex I Part I (2)(d) | PR.AA-01, ID.AM-01 | Restated for TinyTask's 8-employee manufacturer role with default-class (self-assessment) conformity; the "appropriate control mechanisms" floor is calibrated to the B2B SaaS product's risk profile (individual logins, managed cloud hosting); CRA imposes no MFA mandate — the "may include authentication" language preserves mechanism discretion. |

## §4.1 Control Anchor Mapping

| ID | Regulation | CSF 2.0 | NIST PF 1.1 | NIST AI RMF | Source |
|---|---|---|---|---|---|
| AG-D-03.2-001 | GDPR | PR.AA-05, PR.AA-06 | PR.AC-P1, PR.AC-P2, CT.PO-P1 | — | SR-GDPR-011 |
| AG-D-03.2-002 | GDPR | PR.AA-05, PR.AA-06 | PR.AC-P1, PR.AC-P2, CT.PO-P1 | — | SR-GDPR-012 |
| AG-D-03.2-003 | CRA | PR.AA-01, ID.AM-01 | — | — | SR-CRA-023 |

## §5

> ASSUMPTION: The external payment provider (sub-processor for payment metadata only, per the fact sheet) is covered by the Art. 28(3)(b) processor-contract confidentiality obligation as a sub-processor under TinyTask's controller/processor role; no separate authentication-strength obligation attaches to that sub-processor under the confirmed regulations (GDPR, CRA).

> OPEN QUESTION: The fact sheet records "data_scale: rough figure not stated in the intake." The proportionality calibration of the Art. 12(6) verification means (AG-D-03.2-002) and the CRA risk-assessment baseline (AG-D-03.2-003) both depend on the volume of personal data processed; a rough figure is needed to confirm that the 8-employee-scale interpretation is adequate.
```