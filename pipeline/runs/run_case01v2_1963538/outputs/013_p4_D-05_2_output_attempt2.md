```markdown
### D-05.2 — Retention & Archiving

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-05.2-001 | Personal data held by the company (customer account metadata and task data containing personal data of customers' users) is retained for no longer than is necessary for its declared processing purpose; any retention beyond purpose end is lawful and subject to Art. 89(1) safeguards (pseudonymisation, aggregation, access limitation); the RoPA documents the envisaged time limits for erasure per data category. | maintain | privacy-right | SO-D-05.2.HL | Art. 5(1)(e); Art. 30(1)(f); Art. 89(1) | ID.AM-08, ID.AM-03 | Narrowed to the company's two data classes (customer account metadata; task data with personal data of customers' users); no sensitive-data categories; processor role for customer task data acknowledged; no AI/ML logs in scope. |
| AG-D-05.2-002 | Security updates and supporting advisory messages for the company's SaaS product remain available to users across the support period (≥ 5 years) and the 10-year-or-remainder-of-support-period update-availability tail; Annex II information remains accessible for at least 10 years from placing on market; the support-period end-date is communicated clearly and understandably at the time of purchase. | maintain | A | SO-D-05.2.HL | Art. 13(8); Art. 13(9); Art. 13(18); Art. 13(19); Annex I Part II (7); Annex I Part II (8) | PR.PS-02, GV.OV-02 | Narrowed to the company's SaaS product (web + mobile interface) as a default-class product with self-assessment conformity; no AI/ML systems; the 10-year tail applies to update artefacts and Annex II information, not to personal data. |

## §4.1 Control Anchor Mapping

| ID | Regulation | CSF 2.0 | NIST PF 1.1 | NIST AI RMF | Source |
|---|---|---|---|---|---|
| AG-D-05.2-001 | GDPR | ID.AM-08, ID.AM-03 | CT.PO-P4, CT.DM-P5 | — | SR-GDPR-029 |
| AG-D-05.2-002 | CRA | PR.PS-02, GV.OV-02 | — | — | SR-CRA-016; SR-CRA-047 |

## §5

> ASSUMPTION: The company's SaaS platform (web + mobile interface) is treated as a single "product with digital elements" under CRA for the purposes of the support-period and update-availability obligations; no separate hardware or embedded-component retention duties arise.

**Open question (from fact sheet):** data_scale — rough volume figure not stated in the intake; the retention architecture must be scalable, but no specific volume threshold can be derived for the Art. 30(1)(f) RoPA time-limit documentation or the CRA Annex II information-accessibility evidence.
```