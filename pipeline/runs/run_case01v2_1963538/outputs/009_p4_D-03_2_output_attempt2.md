```markdown
### D-03.2 — Authentication of users, services, and hardware

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-03.2-001 | The 8-person internal team and the external payment sub-processor act only on documented instructions from TinyTask as controller (or as processor for customer task data) and remain bound by a confidentiality obligation; no authentication-strength threshold is imposed by this obligation — the surrounding instruction-and-confidentiality architecture is the operative duty. | maintain | C | SO-D-03.2.HL | GDPR Art. 28(3)(b); Art. 29; Art. 32(4) | PR.AA-05, PR.AA-06 | Restated from the GDPR Sub-SO staff-side obligation for an 8-employee SaaS controller/processor with one external sub-processor; the "documented instructions" chain is scoped to the internal team plus the payment sub-processor rather than a large enterprise hierarchy; the absence of an authentication-strength threshold is preserved verbatim from the OJ. |
| AG-D-03.2-002 | When a customer's own user (data subject) exercises a GDPR right through the customer (controller), TinyTask as processor verifies the requester's identity using reasonable means proportionate to the risk of mis-identification, given the non-sensitive, small-scale B2B data context. | achieve | privacy-right | SO-D-03.2.HL | GDPR Art. 12(6); Art. 11(2) | PR.AA-06, PR.AT-02 | Restated from the GDPR Sub-SO data-subject-side verification obligation; proportionality is anchored to the fact-sheet context (non-sensitive data, B2B SaaS, 8 employees) rather than a generic enterprise scale; the verification trigger is "reasonable doubt" per Art. 12(6), not a blanket MFA mandate. |
| AG-D-03.2-003 | The TinyTask SaaS product (web and mobile interface, default class, self-assessment conformity) protects against unauthorised access through appropriate control mechanisms — which may include authentication, identity, or access-management systems — commensurate with the identified cybersecurity risk of the product; the mechanism choice is at the manufacturer's discretion under the 3-way OR. | maintain | C | SO-D-03.2.HL | CRA Annex I Part I (2)(d) | PR.AA-01, ID.AM-01 | Restated from the CRA Sub-SO for a default-class SaaS product with individual customer logins; the "may include" permissive language is preserved verbatim from the OJ; no MFA or continuous-authentication phrase is imposed; the risk-assessment anchor is scoped to the product's default-class self-assessment conformity procedure. |

## §4.1 Control Anchor Mapping

| ID | Regulation | CSF 2.0 | NIST PF 1.1 | NIST AI RMF | Source |
|---|---|---|---|---|---|
| AG-D-03.2-001 | GDPR | PR.AA-05, PR.AA-06 | PR.AC-P1, PR.AC-P2, CT.PO-P1 | — | SR-GDPR-011, SR-GDPR-012 |
| AG-D-03.2-002 | GDPR | PR.AA-06, PR.AT-02 | PR.AC-P1, PR.AC-P2, CT.PO-P1 | — | SR-GDPR-011, SR-GDPR-012 |
| AG-D-03.2-003 | CRA | PR.AA-01, ID.AM-01 | — | — | SR-CRA-023, SR-CRA-024 |

## §5

> ASSUMPTION: The external payment provider is treated as a sub-processor under GDPR Art. 28(3)(b) for payment metadata only, per the fact-sheet `third_party_processing` entry; no additional sub-processor chain is assumed.

> ASSUMPTION: The product's "individual logins" access model (fact-sheet `access_model`) is the authentication substrate to which the CRA Annex I Part I (2)(d) "appropriate control mechanisms" obligation attaches; no service-to-service or machine-identity authentication is in scope for this 8-employee SaaS product.

**Open question:** `data_scale` is not stated in the intake (fact-sheet `open_questions`); the proportionality calibration of AG-D-03.2-002 (Art. 12(6) verification means) and the risk-assessment depth of AG-D-03.2-003 (CRA Annex I Part I (2)(d)) cannot be quantitatively refined until a rough record-volume or user-count figure is provided.
```