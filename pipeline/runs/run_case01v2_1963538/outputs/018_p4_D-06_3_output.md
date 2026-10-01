```markdown
### D-06.3 — High-level Security Objective (regulation-neutral)

> **Framing.** TinyTask Lda. is an 8-employee B2B SaaS company in Portugal (EU) that develops and places a rule-based task-management product with digital elements on the EU market as **manufacturer** (CRA default class, self-assessment conformity). It acts as **controller** for customer-account personal data (names, emails, passwords) and as **processor** for customer task data containing personal data of the customers' own users. One external sub-processor (payment provider) handles payment metadata. Hosting is managed cloud. No AI/ML systems. NIS2, DORA, and AI Act are excluded per the fact sheet. The sub-domain D-06.3 engages because ≥2 confirmed regulations (GDPR, CRA) apply to the same supply-chain artefact (the product and its processing relationships).

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-06.3-001 | Each controller–processor relationship in which TinyTask acts as controller (customer-account data) or as processor (customer task data) is governed by a written contract containing the Art. 28(3)(a)–(h) eight mandatory clauses: documented instructions, confidentiality, Art. 32 security measures, sub-processor authorisation conditions, data-subject-rights assistance, incident-assistance, deletion-or-return at contract end, and audit/inspection access. | maintain | accountability | SO-D-06.3.HL | Art. 28(3)(a)–(h) | GV.SC-03 | Split from corpus requirement 6.3.1 (which bundles Art. 28(3), Art. 46, Art. 48) to the DPA-specific obligation; scoped to TinyTask's two processor relationships (external payment provider as sub-processor; business-customer controllers for task data) at 8-employee scale. |
| AG-D-06.3-002 | Where personal data (customer account metadata or task data) is transferred to a third country without an adequacy decision, an Art. 46 appropriate-safeguards instrument is in place for each such transfer, with a maintained transfer mapping and supplementary-measures assessment. | maintain | privacy-right | SO-D-06.3.HL | Art. 46(1); Art. 46(2)(a)–(f) | GV.SC-03, GV.SC-04 | Split from corpus requirement 6.3.1 to the transfer-safeguard obligation; scoped to TinyTask's managed-cloud hosting context where personal data may be processed in a third country; no adequacy decision assumed for the hosting jurisdiction. |
| AG-D-06.3-003 | A third-country court or administrative request for disclosure of personal data is recognised only where it is based on an international agreement between the requesting third country and the Union or a Member State; requests not meeting this criterion are not honoured. | avoid | privacy-right | SO-D-06.3.HL | Art. 48 | GV.OC-03 | Split from corpus requirement 6.3.1 to the legal-request filter obligation; scoped to TinyTask's managed-cloud exposure to third-country legal-process pressure; no mechanism prescribed beyond the recognition criterion. |
| AG-D-06.3-004 | Upon identifying a vulnerability in a component integrated in TinyTask's product with digital elements, the vulnerability is reported to the person or entity manufacturing or maintaining that component, and the vulnerability is addressed and remediated in accordance with Annex I Part II vulnerability-handling requirements. | achieve | integrity | SO-D-06.3.HL | Art. 13(6) sentence 1 | GV.SC-04, RS.MI-02 | Narrowed from corpus requirement 6.3.3 (which bundles Art. 19 importer, Art. 20 distributor, and Art. 13(6) manufacturer duties) to the manufacturer-applicable obligation only; TinyTask is the manufacturer, not an importer or distributor, so Art. 19/20 duties apply to downstream economic operators, not to TinyTask. |

## §4.1 Control Anchor Mapping

| ID | Regulation | CSF 2.0 | NIST PF 1.1 | NIST AI RMF | Source |
|---|---|---|---|---|---|
| AG-D-06.3-001 | GDPR | GV.SC-03 | ID.DE-P3 | — | SR-GDPR-034 |
| AG-D-06.3-002 | GDPR | GV.SC-03, GV.SC-04 | ID.DE-P3 | — | SR-GDPR-056 |
| AG-D-06.3-003 | GDPR | GV.OC-03, GV.SC-03 | GV.PO-P5, ID.DE-P3 | — | SR-GDPR-059 |
| AG-D-06.3-004 | CRA | GV.SC-04, RS.MI-02 | — | — | SR-CRA-051 |

## §5

> ASSUMPTION: The managed-cloud hosting jurisdiction is assumed to be a third country without an EU adequacy decision for the purposes of Art. 46 applicability (AG-D-06.3-002). If an adequacy decision exists for the hosting jurisdiction, the Art. 46 safeguard obligation is satisfied by the adequacy basis under Art. 45 and the goal reduces to maintaining the adequacy assessment.

> ASSUMPTION: TinyTask's role as manufacturer (not importer or distributor) means CRA Art. 19 and Art. 20 obligations in corpus requirement 6.3.3 are not directly applicable to TinyTask; they bind downstream economic operators in the supply chain. Only Art. 13(6) (manufacturer component-vulnerability reporting) is retained as TinyTask's own obligation in D-06.3.
```