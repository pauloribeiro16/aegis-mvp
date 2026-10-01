```markdown
### D-01.2 — Data in transit (confidentiality and integrity)

**Framing (company context):** TinyTask Lda. is an 8-employee B2B SaaS company in Portugal (EU) developing and operating a rule-based task-management platform. It acts as GDPR controller for customer account data (names, emails, passwords) and processor for customer task data containing personal data of the customers' own users, and as CRA manufacturer (default product class, self-assessment conformity) placing the product with digital elements on the EU market. Hosting is managed cloud; no AI/ML systems are present. DORA, NIS 2, and AI Act are out of scope.

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-01.2-001 | Personal data transmitted across the company's network paths, inter-service channels, and third-party API connections remains confidential and unaltered in transit, with the level of protection proportionate to the risk of the five Art. 32(2) event classes (accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to, personal data transmitted). | maintain | C | SO-D-01.2.HL | Art. 32(1)(b); Art. 32(2) | PR.DS-02, PR.IR-01 | Scope narrowed from all data in transit to personal data (Art. 4(1)); protection level anchored to GDPR's risk-based "appropriate" standard with the five-event risk enumeration as the assessment frame; applies to an 8-person controller/processor operating managed-cloud channels. |
| AG-D-01.2-002 | Data transmitted by the product with digital elements is rendered unintelligible to any person not authorised to access it via state-of-the-art encryption in transit, and the product's exposed interfaces through which such data could leak are minimised. | maintain | C | SO-D-01.2.HL | Annex I Part I (2)(e); Annex I Part I (2)(j) | PR.DS-02, PR.IR-01 | Threshold raised from GDPR's risk-anchored "appropriate" to CRA's "state-of-the-art" (harmonised-standards-conformant); attack-surface-limitation leg (2)(j) added as a distinct manufacturer obligation; scope is product-level (all data the product transmits, not only personal data); applies to a default-class manufacturer with self-assessment conformity. |

## §4.1 Control Anchor Mapping

| ID | Regulation | CSF 2.0 | NIST PF 1.1 | NIST AI RMF | Source |
|---|---|---|---|---|---|
| AG-D-01.2-001 | GDPR | PR.DS-02, PR.IR-01 | PR.DS-P2, PR.AC-P5 | — | `SR-GDPR-002` |
| AG-D-01.2-002 | CRA | PR.DS-02, PR.IR-01 | — | — | `SR-CRA-003` |

## §5

> ASSUMPTION: The cross-regulation corpus (CRDA-deep, all 3 pairs verified SAME) states that a CRA-compliant in-transit configuration discharges the GDPR Art. 32(1)(b)/(2) in-transit obligation on the same channel. Both goals are retained independently because TinyTask's GDPR obligation (controller/processor on its own deployment channels) and CRA obligation (manufacturer on the product) are separate compliance tracks per the scope caveat in `cross/_interactions.md`; the discharge relationship is noted for Phase 2 verification design but does not eliminate either goal.

> Open question (from fact sheet): `data_scale` is not stated in the intake. This does not alter the goal wording (the obligation is risk-anchored, not volume-anchored) but will affect the Phase 2 risk-assessment evidence pack under GDPR Art. 32(2).
```