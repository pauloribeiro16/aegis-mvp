```markdown
### D-04.1 — Incident Detection & Triage

> TinyTask Lda. is an 8-employee B2B SaaS company (Portugal, EU) developing and operating a rule-based task management platform. Regulatory roles: controller for customer account data (names, emails, passwords); processor for customer task data; manufacturer of products with digital elements (CRA default product class, self-assessment). Hosting: managed cloud. Explicit exclusions: no AI/ML systems developed, deployed, or integrated; NIS 2 and DORA not applicable; AI Act not applicable.

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-04.1-001 | Personal-data breaches affecting customer account data and task data are detected at the data-flow boundary of the managed-cloud environment, and the moment of "becoming aware" by a designated breach-handling role is documented to anchor the Art. 33(1) 72-hour notification clock. | maintain | C | SO-D-04.1.HL | Art. 32(1)(b); Art. 33(1); Art. 4(12) | DE.CM-01, RS.MA-02 | Scope narrowed from a generic controller to TinyTask's two data categories (customer account metadata as controller; task data as processor) at the managed-cloud data-flow boundary; the "becoming aware" documentation obligation and 72-hour clock anchor are retained in full per the corpus. |
| AG-D-04.1-002 | Relevant internal activity of the TinyTask SaaS platform — including access to or modification of task data, services, or functions — is recorded and monitored on a continuing basis throughout the product support period, with a user-visible opt-out for non-security-critical events, and any corruption or unauthorised modification is reported to the user. | maintain | I | SO-D-04.1.HL | Annex I Part I (2)(l); Annex I Part II (6); Art. 13(8) | PR.PS-04, DE.CM-09 | Scope narrowed from a generic manufacturer to TinyTask's B2B SaaS platform (web + mobile interface) under the CRA default product class; the user opt-out is limited to non-security-critical events; the product-internal detection layer is distinct from and does not substitute for the GDPR data-flow detection layer (DIFFERENT-PERSPECTIVE per CRDA-deep). |

## §4.1 Control Anchor Mapping

| ID | Regulation | CSF 2.0 | NIST PF 1.1 | NIST AI RMF | Source |
|---|---|---|---|---|---|
| AG-D-04.1-001 | GDPR | DE.CM-01, DE.CM-09, RS.MA-02 | GV.MT-P5, GV.MT-P3, CM.AW-P7 | — | SR-GDPR-014 |
| AG-D-04.1-002 | CRA | PR.PS-04, DE.AE-08, DE.CM-09, DE.CM-01 | — | — | SR-CRA-027; SR-CRA-100 |

## §5

> ASSUMPTION: The managed-cloud hosting environment constitutes the "data-flow boundary" for GDPR Art. 32(1)(b) detection purposes; the corpus does not further specify the boundary topology, and the fact sheet states only "managed cloud" without naming a provider or architecture.

> OPEN QUESTION (from fact sheet): `data_scale` — rough figure not stated in the intake. This does not alter the detection obligation but may affect the proportionality of monitoring coverage and the evidence-pack scope for the "becoming aware" timestamp records.
```