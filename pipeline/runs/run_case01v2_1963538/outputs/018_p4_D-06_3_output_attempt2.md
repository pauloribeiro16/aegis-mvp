```markdown
### D-06.3 — High-level Security Objective (regulation-neutral)

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-06.3-001 | Controller/processor DPA contracts for TinyTask's two processing roles (controller for customer-account data; processor for customer task data) contain the Art. 28(3)(a)–(h) eight-element closed list, including documented instructions, confidentiality, Art. 32 measures, sub-processor authorisation with change-notification, data-subject-rights assistance, incident-assistance, end-of-service return-or-deletion, and audit/inspection access; the single external sub-processor (payment provider) is covered by a written prior-authorisation regime. | achieve | Accountability | SO-D-06.3.HL | Art. 28(3)(a)–(h) GDPR; Art. 28(2) GDPR | GV.SC-03 | Restated for an 8-employee B2B SaaS with one external sub-processor; the 8-element DPA applies bidirectionally (TinyTask-as-controller → payment sub-processor; TinyTask-as-processor → business-customer controllers) rather than a multi-processor enterprise matrix. |
| AG-D-06.3-002 | Where personal data is transferred to a third country without an adequacy decision, an Art. 46 appropriate-safeguards instrument (SCCs, BCRs, code of conduct, certification, or ad-hoc contractual clauses) is in place for each transfer pathway, with a transfer-mapping and supplementary-measures assessment maintained. | maintain | Confidentiality | SO-D-06.3.HL | Art. 46(1) GDPR; Art. 46(2)(a)–(f) GDPR | GV.SC-03 | Restated for a single managed-cloud hosting pathway and one payment sub-processor; the safeguard obligation is conditional on the absence of an adequacy decision for the hosting or sub-processor jurisdiction. |
| AG-D-06.3-003 | Third-country court or administrative requests for disclosure of personal data are recognised only through an international-agreement basis; any such request not meeting that filter is refused or routed through the appropriate legal channel before disclosure. | avoid | Accountability | SO-D-06.3.HL | Art. 48 GDPR | GV.OC-03 | Restated for a single-entity, 8-employee operator; the filter applies to any third-country legal-process pressure on data held in the managed cloud or by the payment sub-processor, with no dedicated legal-ops team assumed. |
| AG-D-06.3-004 | Upon identifying a vulnerability in a component integrated in TinyTask's product with digital elements, the manufacturer reports the vulnerability to the person or entity manufacturing or maintaining that component and addresses and remediates it in accordance with Annex I Part II; where an open-source component is affected, code and documentation are shared with the OSS maintainer. | achieve | Integrity | SO-D-06.3.HL | Art. 13(6) sentence 1 CRA; Art. 13(6) sentence 2 CRA | GV.SC-04 | Restated for TinyTask's manufacturer role (default class, self-assessment conformity); Art. 19 importer and Art. 20 distributor duties in the same requirement apply to downstream economic operators in the supply chain, not to TinyTask, and are therefore not restated as a TinyTask obligation. |

## §4.1 Control Anchor Mapping

| ID | Regulation | CSF 2.0 | NIST PF 1.1 | NIST AI RMF | Source |
|---|---|---|---|---|---|
| AG-D-06.3-001 | GDPR | GV.SC-03 | ID.DE-P3 | — | SR-GDPR-034 |
| AG-D-06.3-002 | GDPR | GV.SC-03; GV.SC-04 | ID.DE-P3 | — | SR-GDPR-056 |
| AG-D-06.3-003 | GDPR | GV.OC-03; GV.SC-03 | GV.PO-P5; ID.DE-P3 | — | SR-GDPR-059 |
| AG-D-06.3-004 | CRA | GV.SC-04; RS.MI-02 | — | — | SR-CRA-051 |

## §5

> ASSUMPTION: The managed-cloud hosting location is assumed to be within the EEA. If the cloud provider or the payment sub-processor operates from a third country without an adequacy decision, AG-D-06.3-002 (Art. 46 appropriate-safeguards instrument) becomes unconditionally applicable rather than conditional, and the transfer-mapping obligation extends to that specific pathway.

> ASSUMPTION: TinyTask does not act as importer or distributor of products with digital elements; its CRA role in this sub-domain is limited to manufacturer obligations under Art. 13(6). If TinyTask were to resell or redistribute a third-party product with digital elements, Art. 19/20 duties would additionally apply and require a separate goal.
```