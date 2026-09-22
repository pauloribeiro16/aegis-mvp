# Partial-coverage patch ledger (M9 — M7 follow-up)

- Date: 2026-09-22
- Scope: strictly additive YAML `nist_csf:` array of the named Volere requirement cards, AND propagation of the same anchor to every Sub-SO card in the corpus that cites the same `source_SR` (so check H stays green).
- Idempotent: re-run = 0 changes.

## Primary patches (M7 audit findings)

| Sub | Reg | Req | Anchor added | Justification | File | Before | After |
|---|---|---|---|---|---|---|---|
| D-04.2 | DORA | 4.2.4 | `RS.MA-01` | Article basis cites 'incident' as a key action; RS.MA-01 is the CSF subcategory for incident-management-plan execution with third-party coordination, covering the BC arrangements dispatch dimension (Art. 11(2) + Art. 19(1) + Art. 19(3)). | `baseline/domains/D-04_Incident-Response/D-04.2/regs/DORA.md` | `nist_csf: [PR.IR-03, RC.RP-01, RS.MA-01]` | `nist_csf: [PR.IR-03, RC.RP-01, RS.MA-01]` |
| D-04.2 | NIS2 | 4.2.2 | `RS.MA-01` | Article basis cites 'incident' as a key action; RS.MA-01 covers incident management with third-party coordination per the Art. 6(8) six-action lifecycle. | `baseline/domains/D-04_Incident-Response/D-04.2/regs/NIS2.md` | `nist_csf: [RS.MA-01, RS.AN-03]` | `nist_csf: [RS.MA-01, RS.AN-03]` |
| D-07.1 | DORA | 7.1.4 | `PR.PS-02` | Article basis cites 'patch' as a key action; PR.PS-02 covers software maintenance commensurate with risk, operationalising Art. 9(4)(f) patch-and-update policies documented in the fit_criterion. | `baseline/domains/D-07_Secure-Development/D-07.1/regs/DORA.md` | `nist_csf: [ID.RA-01, ID.RA-03, PR.PS-02]` | `nist_csf: [ID.RA-01, ID.RA-03, PR.PS-02]` |

Total primary patches applied: **3**

