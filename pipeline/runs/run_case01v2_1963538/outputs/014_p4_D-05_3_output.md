```markdown
### D-05.3 — Erasure and Secure Removal

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-05.3-001 | Personal data concerning a data subject is erased without undue delay upon the data subject's request where any of the six Art. 17(1) grounds applies, and the controller confirms the action taken to the data subject. | achieve | privacy-right | SO-D-05.3.HL | Art. 17(1)(a)–(f); Art. 17(2) | PR.DS-10, ID.AM-08 | Restated for an 8-person B2B SaaS controller over customer account data (names, emails, passwords); "without undue delay" retained as VAG per corpus; no sensitive data in scope narrows the operational surface; Art. 17(3) carve-outs apply as exception structure without relaxing the duty. |
| AG-D-05.3-002 | Upon end of processing services, the processor deletes or returns all personal data to the controller and deletes existing copies, unless Union or Member State law requires storage, with evidentiary confirmation available to the controller. | achieve | accountability | SO-D-05.3.HL | Art. 28(3)(g) | PR.DS-10, GV.SC-04 | Restated for TinyTask's processor role over customer task data; the deletion-or-return obligation activates at contract end; GV.SC-04 evidentiary confirmation (audit, test result, or independent inspection) retained so the controller can discharge Art. 5(2) accountability. |
| AG-D-05.3-003 | The product exposes a discoverable user-interface affordance allowing the user to securely and easily remove, on a permanent basis, all data and settings of the product, with decommissioning instructions supplied; where data can be transferred to other products or systems, the transfer is done in a secure manner. | achieve | accountability | SO-D-05.3.HL | Annex I Part I (2)(m); Annex II §8(d) | PR.DS-10, ID.AM-08 | Restated for a default-class SaaS product with self-assessment conformity; "securely and easily" retained as VAG (both required via discoverable affordance); "permanent basis" = recovery-infeasible; the second limb (secure cross-product transfer) is structurally relevant to D-03.3 per corpus and is included here as part of the Sub-SO objective; the affordance is independent of GDPR Art. 17(3) carve-outs. |

## §4.1 Control Anchor Mapping

| ID | Regulation | CSF 2.0 | NIST PF 1.1 | NIST AI RMF | Source |
|---|---|---|---|---|---|
| AG-D-05.3-001 | GDPR | PR.DS-10, ID.AM-08 | CT.DM-P4, CT.DM-P5 | — | SR-GDPR-030 |
| AG-D-05.3-002 | GDPR | PR.DS-10, GV.SC-04 | CT.DM-P4, CT.DM-P5, ID.DE-P3 | — | SR-GDPR-031 |
| AG-D-05.3-003 | CRA | PR.DS-10, ID.AM-08 | — | — | SR-CRA-048 |

## §5

> ASSUMPTION: TinyTask's dual role (controller for customer account data; processor for customer task data) means both the Art. 17(1) controller-side erasure (AG-D-05.3-001) and the Art. 28(3)(g) processor-side mirror (AG-D-05.3-002) are operative on the same party; the processor mirror applies to the task-data processing relationship with business customers, and the controller-side Art. 17 path executes through the manufacturer's (2)(m) affordance at the architectural layer per the corpus layer-stacking pattern.

> ASSUMPTION: The CRA Annex I Part I (2)(m) second limb (secure cross-product transfer, SR-CRA-049) is included in AG-D-05.3-003 as part of the Sub-SO objective, but its dedicated requirement is not present in the D-05.3 CRA module; the corpus notes it is "structurally relevant to D-03.3 as well." No separate goal is emitted here for the second limb to avoid double-counting; the D-03.3 module is expected to carry its own requirement.

Open question: data_scale is not stated in the intake (fact_sheet.yaml); the operational calibration of the erasure procedure (backup retention windows, replica count, query-cache purge scope) depends on this figure and cannot be fixed at Phase 1A altitude.
```