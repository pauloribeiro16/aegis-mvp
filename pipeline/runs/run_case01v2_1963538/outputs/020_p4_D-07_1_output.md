```markdown
### D-07.1 — Secure-by-Design Principles

**Framing (company context conditioning every goal below):**

> TinyTask Lda. is an 8-employee B2B SaaS company in Portugal (EU) developing and operating a rule-based task-management platform sold by commercial subscription. It acts as **controller** for customer account data (names, emails, passwords) and **processor** for customer task data. It develops the software itself and places the product (web + mobile interface) on the EU market as a **CRA manufacturer** in the default product class with self-assessment (internal-production-control) conformity. No AI/ML systems are developed, deployed, or integrated. Hosting is managed cloud. NIS2, DORA, and AI Act are not applicable to this entity.

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-07.1-001 | The controller implements appropriate technical and organisational measures — such as pseudonymisation — designed to implement data-protection principles (data minimisation) in an effective manner and to integrate the necessary safeguards into the processing at the time of means-determination and at the time of processing, and ensures that by default only personal data necessary for each specific purpose are processed, calibrated to the state of the art, cost of implementation, nature/scope/context/purposes of processing, and risks of varying likelihood and severity for an 8-person SaaS platform on managed cloud. | achieve | privacy-right | SO-D-07.1.HL | Art. 25(1) GDPR; Art. 25(2) GDPR | PR.PS-06, ID.AM-08 | Restated from the corpus controller-side by-design + by-default obligation (req 7.1.1) to the company's scale: the 4-factor qualitative proportionality is applied to a small SaaS controller/processor on managed cloud; by-default limits (amount, extent, storage period, accessibility) are operationalised through the platform's minimal-data-collection and minimal-access design; no mechanism prescribed beyond the OJ text. |
| AG-D-07.1-002 | The manufacturer ensures that the product with digital elements (SaaS platform + web/mobile interface) has been designed, developed and produced in accordance with the essential cybersecurity requirements set out in Annex I Part I, with the cybersecurity risk assessment taken into account across the planning, design, development, production, delivery and maintenance phases, with a view to minimising cybersecurity risks, preventing incidents, and minimising their impact including in relation to the health and safety of users, at the scale of a default-class self-assessment manufacturer. | achieve | I | SO-D-07.1.HL | Art. 13(1) CRA; Art. 13(2) CRA | PR.PS-06, GV.PO-02 | Restated from the corpus manufacturer-side product by-design + 6-phase risk-assessment-propagation obligation (req 7.1.3) to the company's scale: the 6-phase propagation applies to the SaaS + web/mobile product lifecycle; Annex I Part I essential requirements are applied at the default-class self-assessment conformity level; no AI/ML components are present, so AI-Act-specific attack categories do not apply. |

## §4.1 Control Anchor Mapping

| ID | Regulation | CSF 2.0 | NIST PF 1.1 | NIST AI RMF | Source |
|---|---|---|---|---|---|
| AG-D-07.1-001 | GDPR | PR.PS-06, ID.AM-08 | GV.PO-P2, CT.PO-P4 | — | SR-GDPR-039 |
| AG-D-07.1-002 | CRA | PR.PS-06, GV.PO-02 | — | — | SR-CRA-064 |

## §5

> ASSUMPTION: The company's dual GDPR role (controller for customer account data; processor for customer task data) means Art. 25(1) by-design obligations attach to the controller-side processing (account data). The processor-side obligation for customer task data is governed by Art. 28 and the controller's instructions; the adjusted goal AG-D-07.1-001 is scoped to the controller role as stated in the corpus baseline.

> ASSUMPTION: The data scale (volume of personal data processed) is not stated in the intake. The 4-factor proportionality under Art. 25(1) includes "nature, scope, context and purposes of processing" as a calibration factor; the absence of a stated data volume does not alter the obligation but may affect the depth of the documented necessity assessment. This is recorded as an open intake item, not a goal modification.

> ASSUMPTION: The CRA default-class self-assessment conformity path means the manufacturer performs its own conformity assessment (no notified body). The 6-phase risk-assessment propagation and Annex I Part I essential-requirement conformance are self-documented and retained in the Annex VII §2/§3 technical documentation for market-surveillance-authority inspection.
```