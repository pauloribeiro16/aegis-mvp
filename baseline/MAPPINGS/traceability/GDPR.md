# Traceability — GDPR

> Chain: regulation -> article(s) -> ambiguity clause(s) -> HSO -> SO-GDPR -> Sub-SO -> requirement -> controls. Generated from the modular corpus + `sr_control_mappings` (dashboard-uniformized).

## D-01.1 — Data at Rest Encryption

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 1.1.1 — Personal data at rest is protected by appropriate technical measures | `SR-GDPR-001` | Art. 5(1)(f); Art. 32(1)(b); Art. 4(1) — personal data definition | GDPR-CL06, GDPR-CP15, GDPR-C01 | SO-D-01.1.HL -> SO-GDPR-001 -> SO-D-01.1.GDPR | PR.DS-01, PR.DS-10 | PR.DS-P1, PR.PO-P3 | — |

## D-01.2 — Data in Transit Encryption

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 1.2.1 — Personal data in transit remains confidential and unaltered | `SR-GDPR-002` | Art. 32(1)(b); Art. 32(2) — risk enumeration; Art. 4(1) — personal data | GDPR-CP15, GDPR-CP16, GDPR-C01 | SO-D-01.2.HL -> SO-GDPR-001 -> SO-D-01.2.GDPR | PR.DS-02, PR.IR-01 | PR.DS-P2, PR.AC-P5 | — |

## D-01.3 — Cryptographic Key Management

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 1.3.1 — Personal-data key material kept separately to prevent re-attribution (de-attribution test) | `SR-GDPR-003` | Art. 32(1)(a); Art. 4(5) — pseudonymisation definition; Art. 4(1) — personal data | GDPR-CP15, GDPR-C02, GDPR-C01 | SO-D-01.3.HL -> SO-GDPR-002 -> SO-D-01.3.GDPR | PR.DS-01 | PR.DS-P1, CT.DP-P2 | — |

## D-01.4 — Data Integrity Mechanisms

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 1.4.1 — Personal data accurate, up to date, and protected against unauthorised modification | `SR-GDPR-005` | Art. 5(1)(d) — accuracy; Art. 5(1)(f) — integrity (cross-reference); Art. 4(1) — personal data | GDPR-CL04, GDPR-CL06, GDPR-C01 | SO-D-01.4.HL -> SO-GDPR-003 -> SO-D-01.4.GDPR | PR.DS-01, ID.AM-08 | CT.DM-P1, CT.DM-P3 | — |

## D-02.1 — Vulnerability Identification

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 2.1.1 — Periodic testing of security measures + DPIA review on material change | `SR-GDPR-007` | Art. 32(1)(d); Art. 5(1)(f) — appropriate security | GDPR-CP15, GDPR-CL06 | SO-D-02.1.HL -> SO-GDPR-004 -> SO-D-02.1.GDPR | ID.RA-01, PR.PS-02 | GV.MT-P3, CT.DM-P10 | — |

## D-02.2 — Patch Management & Updates

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-02.3 — Coordinated Vulnerability Disclosure

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-02.4 — Threat-Led Penetration Testing

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-03.1 — Identity Lifecycle Management

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 3.1.1 — Data-subject identity verified using reasonable means proportionate to risk (rights-exercise endpoint) | `SR-GDPR-009` | Art. 12(6) — identity verification; Art. 11(2) — identification exemption; Art. 4(1) — personal data (cross) | GDPR-RT04, GDPR-CL26, GDPR-C01 | SO-D-03.1.HL -> SO-GDPR-005 -> SO-D-03.1.GDPR | PR.AA-03, PR.AA-02 | PR.AC-P6, PR.AC-P3 | — |

## D-03.2 — Multi-Factor Authentication

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 3.2.1 — Authentication governed by instructions + confidentiality + minimisation (no OJ authentication-strength threshold) | `SR-GDPR-011` | Art. 29 — processing under authority; Art. 32(4); Art. 28(3)(a)/(b); Art. 4(7)/(8) — controller/processor definitions | GDPR-CP11, GDPR-CP15, GDPR-CP09, GDPR-C03 | SO-D-03.2.HL -> SO-GDPR-006 -> SO-D-03.2.GDPR | PR.AA-05, PR.AA-06 | PR.AC-P1, PR.AC-P2, CT.PO-P1 | — |

## D-03.3 — Authorisation & Least Privilege

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 3.3.1 — Authorisation in personal-data scope operates through documented instructions and confidentiality undertakings (chain of authority controller → processor → authorised persons) | `SR-GDPR-011` | Art. 29 — processing under authority; Art. 32(4); Art. 28(3)(a)/(b); Art. 4(7)/(8) — controller/processor definitions | GDPR-CP11, GDPR-CP15, GDPR-CP09, GDPR-C03 | SO-D-03.3.HL -> SO-GDPR-006 -> SO-D-03.3.GDPR | PR.AA-05, PR.AA-06 | PR.AC-P1, PR.AC-P2, CT.PO-P1 | — |

## D-03.4 — Secure System Defaults

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 3.4.1 — Personal-data processing systems implement by-default measures across amount, extent, period, and accessibility (Art. 25(2) four-dimension AND) | `SR-GDPR-013` | Art. 25(2) — privacy by default; Art. 25(1) — privacy by design (cross); Art. 5(1)(c) — data minimisation (cross) | GDPR-CP03, GDPR-CP02, GDPR-CL03 | SO-D-03.4.HL -> SO-GDPR-007 -> SO-D-03.4.GDPR | PR.PS-01, ID.AM-08 | CT.DP-P4, CT.PO-P4 | — |

## D-04.1 — Incident Detection & Triage

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 4.1.1 — Personal-data breaches detected at the controller data-flow boundary with documented `becoming aware` moment anchoring the 72h clock | `SR-GDPR-014` | Art. 33(1) — 72-hour notification trigger; Art. 32(1)(b) — confidentiality of processing systems; Art. 4(12) — personal data breach definition | GDPR-CP17, GDPR-CP15, GDPR-C06 | SO-D-04.1.HL -> SO-GDPR-008 -> SO-D-04.1.GDPR | DE.CM-01, DE.CM-09, RS.MA-02 | GV.MT-P5, GV.MT-P3, CM.AW-P7 | — |

## D-04.2 — Incident Containment & Response

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 4.2.1 — Personal-data breaches contained and mitigated through TOMs incl. unintelligibility rendering; Art. 33(3)(d) measures description in supervisory-authority notification | `SR-GDPR-015` | Art. 33(3)(d) — measures taken or proposed; Art. 34(3)(a)/(b) — measures to render data unintelligible / subsequent measures; Art. 32(1)(d) — testing | GDPR-CP18, GDPR-CP20, GDPR-CP15 | SO-D-04.2.HL -> SO-GDPR-009 -> SO-D-04.2.GDPR | RS.MI-01, RS.MI-02, PR.DS-01 | PR.PO-P7, CT.DM-P10 | — |

## D-04.3 — Incident Notification & Reporting

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 4.3.1 — Personal-data breach notified to supervisory authority within 72 hours `where feasible` of becoming aware, with `unlikely risk` carve-out documented | `SR-GDPR-016` | Art. 33(1) — 72-hour notification; Art. 4(12) — personal data breach; Art. 32(2) — risk enumeration; Art. 4(22) — supervisory authority concerned | GDPR-CP17, GDPR-C06, GDPR-CP16, GDPR-C09 | SO-D-04.3.HL -> SO-GDPR-010 -> SO-D-04.3.GDPR | RS.CO-02, RS.MA-04, RS.MA-03 | CM.AW-P7, CM.PO-P2 | — |

## D-04.4 — Incident Recovery & Lessons Learned

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 4.4.1 — Personal data availability and access restored in `timely manner` after physical or technical incident, with tested recovery-exercise evidence discharging Art. 5(2) accountability | `SR-GDPR-024` | Art. 32(1)(c) — timely restore; Art. 5(1)(f) — integrity & confidentiality (cross); Art. 32(2) — risk enumeration | GDPR-CP15, GDPR-CL06, GDPR-CP16 | SO-D-04.4.HL -> SO-GDPR-014 -> SO-D-04.4.GDPR | PR.IR-04, PR.DS-11, RC.RP-04 | PR.PO-P3 | — |

## D-05.1 — Data Minimisation

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 5.1.1 — Personal data limited to what is adequate, relevant, and necessary for the processing purpose, with Art. 6(4) compatibility assessment on change of purpose and Art. 9(1) special-category prohibition honoured | `SR-GDPR-025` | Art. 5(1)(c) — data minimisation; Art. 6(4) — compatibility test; Art. 5(1)(b) — purpose limitation (cross) | GDPR-CL03, GDPR-CL14, GDPR-CL02 | SO-D-05.1.HL -> SO-GDPR-015 -> SO-D-05.1.GDPR | ID.AM-08, ID.AM-03 | CT.PO-P4, CT.DP-P4, ID.RA-P3 | — |

## D-05.2 — Retention & Archiving

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 5.2.1 — Personal data retained no longer than necessary for the processing purpose; longer retention only where lawful and subject to Art. 89(1) safeguards; Art. 30(1)(f) RoPA time-limits documented per category | `SR-GDPR-029` | Art. 5(1)(e) — storage limitation; Art. 30(1)(f) — retention time limits; Art. 5(1)(c) — data minimisation (cross) | GDPR-CL05, GDPR-CP12, GDPR-CL03 | SO-D-05.2.HL -> SO-GDPR-017 -> SO-D-05.2.GDPR | ID.AM-08, ID.AM-03 | CT.PO-P4, CT.DM-P5 | — |

## D-05.3 — Right to Erasure

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 5.3.1 — Personal data erased without undue delay on the data subject's Art. 17(1) request where one of the 6 grounds applies; processor deletes or returns all personal data on contract end per Art. 28(3)(g); cryptographic key destruction as deletion path | `SR-GDPR-030` | Art. 5(1)(e) — storage limitation (cross); Art. 5(1)(c) — data minimisation (cross); Art. 28(3)(g) — delete polysemy | GDPR-CL05, GDPR-CL03, GDPR-CP10 | SO-D-05.3.HL -> SO-GDPR-018 -> SO-D-05.3.GDPR | PR.DS-10, ID.AM-08 | CT.DM-P4, CT.DM-P5 | — |

## D-05.4 — Data Portability

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 5.4.1 — Data subject receives personal data in a structured, commonly used, machine-readable format (Art. 20(1) + Art. 15(3) companion copy), supplied by the controller without undue delay (Art. 12(3) ≤1 month, ≤2 months complex) and free of charge (Art. 12(5)); cross-controller direct transmission provided where technically feasible | `SR-GDPR-032` | Art. 15(1)/(3) — copy provision and format; Art. 15(3) — commonly used electronic form | GDPR-RT09, GDPR-RT10 | SO-D-05.4.HL -> SO-GDPR-020 -> SO-D-05.4.GDPR | PR.DS-10, ID.AM-08 | CT.DM-P1, CT.DM-P6 | — |

## D-06.1 — Vendor Risk Assessment

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 6.1.1 — Processor-as-legal-entity due diligence with documented `sufficient guarantees` and Art. 28(3) DPA closed-list clauses | `SR-GDPR-033` | Art. 28(1) — processor selection; Art. 28(2) — sub-processor authorisation; Art. 4(7)/(8) — controller/processor | GDPR-CP07, GDPR-CP08, GDPR-C03 | SO-D-06.1.HL -> SO-GDPR-021 -> SO-D-06.1.GDPR | GV.SC-02, GV.SC-03 | ID.DE-P5, ID.IM-P2 | — |

## D-06.2 — Software Bill of Materials (SBOM)

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-06.3 — Contractual Security Obligations

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 6.3.1 — Art. 28(3)(a)–(h) 8-element DPA closed-list contracts + Art. 46 transfer safeguards + Art. 48 international-agreement filter for third-country legal-process exposure | `SR-GDPR-034` | Art. 28(3)(a)–(h) — 8 mandatory clauses | GDPR-CP09 | SO-D-06.3.HL -> SO-GDPR-022 -> SO-D-06.3.GDPR | GV.SC-03 | ID.DE-P3 | — |

## D-06.4 — Third-Party Boundary Management

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 6.4.1 — Art. 27(1) written Union representative designation for non-EU controllers/processors under Art. 3(2), subject to Art. 27(2) occasional / low-risk / public-authority exceptions | `SR-GDPR-038` | Art. 27(1) — designate in writing; Art. 27(2)(a) — occasional exception | GDPR-CP06 | SO-D-06.4.HL -> SO-GDPR-023 -> SO-D-06.4.GDPR | GV.OC-02, GV.RR-02 | GV.PO-P3, GV.PO-P4 | — |

## D-07.1 — Secure-by-Design Principles

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 7.1.1 — Personal-data processing implements data-protection principles via appropriate technical and organisational measures designed into the means of processing, with by-default limits on amount, extent, storage period and accessibility | `SR-GDPR-039` | Art. 25(1) — privacy by design; Art. 25(2) — privacy by default (cross); Art. 5(1)(f) — integrity & confidentiality (cross); Art. 32(1) — security measures (cross) | GDPR-CP02, GDPR-CP03, GDPR-CL06, GDPR-CP15 | SO-D-07.1.HL -> SO-GDPR-024 -> SO-D-07.1.GDPR | PR.PS-06, ID.AM-08 | GV.PO-P2, CT.PO-P4 | — |

## D-07.2 — Secure Coding Practices

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-07.3 — CI/CD Pipeline Security

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-07.4 — Change Management

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-08.1 — General Security Awareness

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 8.1.1 — Personnel authorised to process personal data receive DPO-catalysed awareness-raising and training on GDPR obligations applicable to their role | `SR-GDPR-042` | Art. 39(1)(b) — awareness and training; Art. 39(1)(a) — inform and advise | GDPR-CP28 | SO-D-08.1.HL -> SO-GDPR-025 -> SO-D-08.1.GDPR | PR.AT-01, PR.AT-02 | GV.AT-P1, GV.AT-P2 | — |

## D-08.2 — Role-Specific Competence

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 8.2.1 — Role-specific training for processing staff with data-subject-facing, access-management, breach-response or DPO-deputy responsibilities | `SR-GDPR-042` | Art. 39(1)(b) — awareness and training; Art. 39(1)(a) — inform and advise | GDPR-CP28 | SO-D-08.2.HL -> SO-GDPR-025 -> SO-D-08.2.GDPR | PR.AT-02, PR.AT-01 | GV.AT-P1, GV.AT-P2 | — |

## D-08.3 — Management Board Training

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-09.1 — Information Security Policies

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 9.1.1 — Controller implements appropriate data-protection policies reviewed and updated where necessary, with DPO designation, independence, and Art. 5(2) accountability | `SR-GDPR-043` | Art. 24(1) — appropriate measures; Art. 24(2) — appropriate data-protection policies; Art. 5(2) — accountability (cross) | GDPR-CP01, GDPR-CL07 | SO-D-09.1.HL -> SO-GDPR-026 -> SO-D-09.1.GDPR | GV.PO-01, GV.PO-02, GV.RM-04 | GV.PO-P1, GV.PO-P6 | — |

## D-09.2 — Impact & Risk Assessments

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 9.2.1 — Controller carries out a pre-launch DPIA covering the four Art. 35(7) content items before high-risk personal-data processing, reviewed on change of risk per Art. 35(11) and submitted for prior consultation where residual risk is high | `SR-GDPR-045` | Art. 35(1) — DPIA trigger; Art. 35(7) — DPIA content; Art. 36(1) — prior consultation (cross); Art. 4(1) — personal data | GDPR-CP21, GDPR-CP22, GDPR-CP23, GDPR-C01 | SO-D-09.2.HL -> SO-GDPR-028 -> SO-D-09.2.GDPR | ID.RA-01, ID.RA-05, ID.RA-06 | ID.RA-P3, ID.RA-P4, ID.RA-P5 | — |

## D-09.3 — Asset Inventories

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-09.4 — Records of Processing

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 9.4.1 — Controller and processor maintain a record of processing activities (RoPA) under Art. 30(1)/(2)/(3)/(4)/(5) GDPR with the 7-item content list, on-DPA-request, subject to the 250-employee exception | `SR-GDPR-048` | Art. 30(1) — RoPA content; Art. 30(4) — supervisory authority access; Art. 30(5) — 250-employee exception | GDPR-CP12, GDPR-CP13 | SO-D-09.4.HL -> SO-GDPR-029 -> SO-D-09.4.GDPR | ID.AM-03, GV.PO-02 | ID.IM-P1, ID.IM-P4, ID.IM-P6, ID.IM-P8 | — |

## D-10.1 — Continuous Security Monitoring

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 10.1.1 — Controller and processor monitor personal-data processing systems for the 5 Art. 32(2) risk types, with breach-`becoming-aware` clock anchoring the Art. 33(1) 72-hour notification | `SR-GDPR-019` | Art. 34(1) — high-risk breach communication to data subject; Art. 34(2) — content of communication; Art. 32(2) — risk enumeration (cross) | GDPR-CP19, GDPR-CP16 | SO-D-10.1.HL -> SO-GDPR-030 -> SO-D-10.1.GDPR | RS.CO-03, RS.MA-04 | CM.AW-P7, CM.AW-P8 | — |

## D-10.2 — Audit Logging & Traceability

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 10.2.1 — Controller and processor maintain compliance records in writing or electronic form with integrity and traceability sufficient to demonstrate compliance and to support supervisory-authority inspections | `SR-GDPR-044` | Art. 5(2) — accountability; Art. 24(1) — demonstrate compliance (cross); Art. 30(1) — records of processing (cross) | GDPR-CL07, GDPR-CP01, GDPR-CP12 | SO-D-10.2.HL -> SO-GDPR-031 -> SO-D-10.2.GDPR | GV.PO-02, GV.OV-03 | GV.MT-P3, GV.PO-P5 | — |

## D-10.3 — Compliance Testing

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 10.3.1 — Controller and processor establish a process for regularly testing, assessing and evaluating the effectiveness of technical and organisational measures, with DPIA review at least when there is a change of the risk | `SR-GDPR-019` | Art. 34(1) — high-risk breach communication to data subject; Art. 34(2) — content of communication; Art. 32(2) — risk enumeration (cross) | GDPR-CP19, GDPR-CP16 | SO-D-10.3.HL -> SO-GDPR-032 -> SO-D-10.3.GDPR | RS.CO-03, RS.MA-04 | CM.AW-P7, CM.AW-P8 | — |

