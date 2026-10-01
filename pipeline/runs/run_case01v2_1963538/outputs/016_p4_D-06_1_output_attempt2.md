```markdown
### D-06.1 — Vendor Risk Assessment (Supply-Chain Due Diligence)

> TinyTask Lda. is an 8-employee B2B SaaS productivity-tools company (Portugal, EU) that develops and places a rule-based task-management platform on the EU market as **manufacturer** (CRA default class, self-assessment conformity) and acts as **controller** for customer-account personal data and **processor** for customers' task data (GDPR). One external payment provider operates as a sub-processor for payment metadata only. NIS 2, DORA, and AI Act are excluded per the fact sheet. No AI/ML systems are developed, deployed, or integrated.

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-06.1-001 | Before engaging the external payment provider as a sub-processor, the controller verifies that the provider offers sufficient guarantees to implement appropriate technical and organisational measures so that processing meets GDPR requirements and protects data-subject rights; the Art. 28(3) closed-list DPA clauses (a)–(h) are documented in the processor contract and the Art. 28(2) sub-processor authorisation chain is maintained in the Art. 30(2) RoPA processor record. | achieve | accountability | SO-D-06.1.HL | Art. 28(1); Art. 28(2); Art. 28(3)(a)–(h) | GV.SC-02, GV.SC-03 | Proportionally scoped to the single external payment-provider sub-processor relationship at 8-employee SaaS scale; the EDPB Guidelines 07/2020 4-factor assessment operationalises the qualitative `sufficient guarantees` threshold for that one processor engagement rather than a multi-processor portfolio. |
| AG-D-06.1-002 | When integrating components sourced from third parties — including components of free and open-source software not made available on the market in the course of a commercial activity — the manufacturer exercises due diligence (procedural and substantive) so that those components do not compromise the cybersecurity of the product with digital elements; on becoming aware of a component vulnerability, the manufacturer addresses and remediates it without delay and shares relevant information with the component supplier. | achieve | I | SO-D-06.1.HL | Art. 13(5); Art. 13(6); Art. 3(48) | GV.SC-01, GV.SC-02 | Proportionally scoped to the self-assessment-class SaaS platform's third-party component set (commercial libraries and non-commercial OSS) at 8-employee manufacturer scale; the R3 procedural + substantive due-diligence reading applies with OSS-specific calibration (stewardship, CVD policy, vulnerability-disclosure channel) rather than a multi-tier enterprise supply-chain programme. |

## §4.1 Control Anchor Mapping

| ID | Regulation | CSF 2.0 | NIST PF 1.1 | NIST AI RMF | Source |
|---|---|---|---|---|---|
| AG-D-06.1-001 | GDPR | GV.SC-02, GV.SC-03 | ID.DE-P5, ID.IM-P2 | — | SR-GDPR-033 |
| AG-D-06.1-002 | CRA | GV.SC-01, GV.SC-02, ID.RA-02 | — | — | SR-CRA-050 |

## §5

> ASSUMPTION: The fact sheet states one external payment provider as the sole sub-processor; no additional processor engagements are assumed. If further processors are added, AG-D-06.1-001 extends to each new engagement without structural change.

> ASSUMPTION: The CRA component set is assumed to comprise the third-party libraries and non-commercial OSS dependencies declared in the product's build manifest; no transitive-depth-beyond-SBOM-top-level obligation is assumed beyond what Art. 13(5) sentence 1 requires for components the manufacturer integrates.

> OPEN QUESTION: The fact sheet does not state a rough data-scale figure; the proportionality calibration of the Art. 28(1) `sufficient guarantees` assessment (EDPB 4-factor) may shift if the customer base or task-data volume grows materially beyond the current 8-employee SaaS baseline.
```