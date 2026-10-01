```markdown
### D-06.1 — Vendor Risk Assessment

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-06.1-001 | Before engaging any processor — including the external payment provider acting as sub-processor for payment metadata — TinyTask verifies that the processor provides sufficient guarantees to implement appropriate technical and organisational measures ensuring processing meets GDPR requirements and protects data-subject rights; the Art. 28(3) closed-list DPA clauses (a)–(h) are documented in the processor contract and the Art. 28(2) sub-processor authorisation chain is maintained and inspectable. | achieve | accountability | SO-D-06.1.HL | Art. 28(1); Art. 28(2); Art. 28(3)(a)–(h); Art. 4(7)/(8) | GV.SC-02 | Scope narrowed from the general controller-processor engagement duty to TinyTask's single external payment-provider sub-processor relationship and any future processors; the EDPB Guidelines 07/2020 4-factor calibration is retained as the proportionality test appropriate to an 8-employee B2B SaaS controller. |
| AG-D-06.1-002 | When integrating components sourced from third parties — including free and open-source software components not made available on the market in the course of a commercial activity — TinyTask exercises documented due diligence (procedural and substantive) so that those components do not compromise the cybersecurity of the product with digital elements; on becoming aware of a component vulnerability, TinyTask addresses and remediates it without delay and shares relevant information with the component supplier. | achieve | integrity | SO-D-06.1.HL | Art. 13(5); Art. 13(6); Art. 3(48) | GV.SC-02; ID.RA-02 | Scope calibrated to TinyTask's 8-employee SaaS manufacturer role with self-assessment conformity; the component universe is the software libraries, frameworks, and managed-cloud dependencies integrated into the product; non-commercial OSS inclusion per Art. 3(48) is retained as the CRA-specific extension beyond the commercial-supplier framework. |

## §4.1 Control Anchor Mapping

| ID | Regulation | CSF 2.0 | NIST PF 1.1 | NIST AI RMF | Source |
|---|---|---|---|---|---|
| AG-D-06.1-001 | GDPR | GV.SC-02, GV.SC-03 | ID.DE-P5, ID.IM-P2 | — | SR-GDPR-033 |
| AG-D-06.1-002 | CRA | GV.SC-01, GV.SC-02, ID.RA-02 | — | — | SR-CRA-050 |

## §5

> ASSUMPTION: The fact sheet records `data_scale: rough figure not stated in the intake`. The GDPR Art. 28(1) `sufficient guarantees` calibration (EDPB Guidelines 07/2020 4-factor test) does not require a quantitative data-volume threshold, but the proportionality of the due-diligence depth (e.g. frequency of processor re-assessment, granularity of the Art. 30(2) RoPA processor record) may be informed by data scale. This is flagged as an open input for Phase 2 refinement; no goal is relaxed on this basis.

> ASSUMPTION: The CRA module's considerations note two items remain open: (a) whether implementing acts under Art. 13(24) will specify minimum due-diligence evidentiary content (e.g. signed attestations of CVE-monitoring posture, vulnerability-handling SLA disclosure); (b) the operational status of due diligence for indirect dependencies (transitive depth beyond the SBOM top-level floor) where the manufacturer has no visibility. Both are recorded as open questions for Phase 2; the adjusted goal AG-D-06.1-002 is stated at the level the current regulation text supports and is not pre-emptively narrowed or broadened.
```