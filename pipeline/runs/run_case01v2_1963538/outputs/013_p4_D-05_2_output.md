```markdown
### D-05.2 — Retention & Archiving

**Framing (company context conditioning every goal below):**

> TinyTask Lda. is an 8-employee B2B SaaS company (Portugal, EU) developing and operating a rule-based task-management platform sold by commercial subscription. It acts as GDPR controller for customer account metadata (names, emails, passwords) and GDPR processor for customer task data. It places its product (web + mobile interface) on the EU market as a CRA manufacturer in the default product class (self-assessment conformity). No AI/ML systems are developed, deployed, or integrated; AI Act is not applicable. Hosting is managed cloud. No sensitive-data categories are in scope. Data scale is not stated in the intake.

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-05.2-001 | Personal data (customer account metadata and customer task data) is retained in a form permitting identification of data subjects for no longer than is necessary for the declared processing purpose; where retention extends beyond purpose end for archiving, scientific or historical research, or statistical purposes, Art. 89(1) safeguards (pseudonymisation, aggregation, access limitation) are applied; the record of processing activities documents the envisaged time limits for erasure per data category, and the retention clock resets when the underlying purpose changes. | maintain | privacy-right | SO-D-05.2.HL | Art. 5(1)(e); Art. 30(1)(f); Art. 89(1) | ID.AM-08, ID.AM-03 | Restated from corpus Sub-SO SG-D-05.2.GDPR to reflect TinyTask's dual role (controller for account metadata, processor for task data) at 8-FTE scale; the Art. 89(1) carve-out is retained as a conditional obligation (no current public-interest or research processing identified in the fact sheet); no mechanism prescribed beyond the regulatory safeguard categories. |
| AG-D-05.2-002 | Security updates and supporting advisory messages for the TinyTask platform remain available to users across the support period (≥ 5 years or expected use time if shorter) and the 10-year-or-remainder-of-support-period update-availability tail (the longer of the two applies per update); Annex II information remains accessible for at least 10 years from placing on market; the support-period end-date is communicated clearly and understandably at the time of purchase. | maintain | Availability | SO-D-05.2.HL | Art. 13(8); Art. 13(9); Art. 13(18); Art. 13(19); Annex I Part II (7); Annex I Part II (8) | PR.PS-02, GV.OC-04 | Restated from corpus Sub-SO SG-D-05.2.CRA to reflect TinyTask's role as sole manufacturer of a default-class SaaS product at 8-FTE scale; the twin-anchor pattern (10-year floor vs. support-period remainder, whichever is longer, per the R2 reading) is preserved; no mechanism prescribed beyond the regulatory availability and user-communication obligations. |

## §4.1 Control Anchor Mapping

| ID | Regulation | CSF 2.0 | NIST PF 1.1 | NIST AI RMF | Source |
|---|---|---|---|---|---|
| AG-D-05.2-001 | GDPR | ID.AM-08, ID.AM-03 | CT.PO-P4, CT.DM-P5 | — | SR-GDPR-029 |
| AG-D-05.2-002 | CRA | PR.PS-02, GV.OV-02 | — | — | SR-CRA-016 |
| AG-D-05.2-002 | CRA | PR.PS-02, GV.OC-04 | — | — | SR-CRA-047 |

## §5

> ASSUMPTION: The CRA module's verbatim-quotes section labels the Art. 13(9) excerpt as "vulnerability disclosure — adjacent but distinct from update availability," yet the module's axis table, requirement 5.2.2 description, fit criterion, and the anchor_slice.json (SR-CRA-016: "Art. 13(9) — 10-year update availability") all treat Art. 13(9) as the 10-year update-availability tail. This step follows the module's operative requirement and the mapping store; the verbatim-quote label is treated as a secondary context provision within the same article.

> ASSUMPTION: AI Act is not confirmed for TinyTask (fact sheet: "rule-based task management; zero AI/ML systems developed, deployed or integrated"). All AI Act material in cross/_interactions.md (floor-within-ceiling, Art. 19(1) ≥ 6-month log floor, SR-AIACT-008) is excluded from this sub-domain's adjusted goals per R8.

> OPEN QUESTION: The fact sheet does not state a rough data-scale figure ("data_scale: rough figure not stated in the intake"). Proportionality of the retention-review cadence (e.g., quarterly vs. annual) cannot be calibrated until this is supplied; the goals above are stated at the regulatory altitude without a frequency prescription.
```