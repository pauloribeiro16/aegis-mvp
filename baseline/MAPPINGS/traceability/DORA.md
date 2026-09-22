# Traceability — DORA

> Chain: regulation -> article(s) -> ambiguity clause(s) -> HSO -> SO-DORA -> Sub-SO -> requirement -> controls. Generated from the modular corpus + `sr_control_mappings` (dashboard-uniformized).

## D-01.1 — Data at Rest Encryption

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 1.1.4 — ICT-supported data of financial entity maintained at high standards of CIA at rest | `SR-DORA-001` | Art. 9(2) — CIA+A 4-way AND + at-rest/in-use/in-transit 3-way OR; Art. 9(2) — in-transit dimension (same locus, explicit in OJ); Art. 9(2) — integrity dimension (same locus, explicit in OJ) | DORA-C09, DORA-C10, DORA-C11 | SO-D-01.1.HL -> SO-DORA-001 -> SO-D-01.1.DORA | PR.DS-01, PR.DS-02, PR.DS-10, ID.AM-08 | — | — |

## D-01.2 — Data in Transit Encryption

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 1.2.3 — ICT-supported data of financial entity maintained at high standards of CIA in transit | `SR-DORA-001` | Art. 9(2) — CIA+A 4-way AND + at-rest/in-use/in-transit 3-way OR; Art. 9(2) — in-transit dimension (same locus, explicit in OJ); Art. 9(2) — integrity dimension (same locus, explicit in OJ) | DORA-C09, DORA-C10, DORA-C11 | SO-D-01.2.HL -> SO-DORA-001 -> SO-D-01.2.DORA | PR.DS-01, PR.DS-02, PR.DS-10, ID.AM-08 | — | — |

## D-01.3 — Cryptographic Key Management

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 1.3.3 — Financial-entity cryptographic keys protected with classification-driven cipher strength and depth | `SR-DORA-002` | Art. 9(4)(d) — strong authentication mechanisms based on relevant standards and dedicated control systems; Art. 9(4)(d) same locus — T4 reads `Multi-Factor Authentication`; OJ says `strong authentication mechanisms`; Art. 9(4)(d) same locus — `protection measures of cryptographic keys` | DORA-C15, DORA-C16, DORA-C17 | SO-D-01.3.HL -> SO-DORA-002 -> SO-D-01.3.DORA | PR.AA-03, PR.AA-04 | — | — |

## D-01.4 — Data Integrity Mechanisms

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 1.4.3 — ICT-system data integrity maintained at high standards across all data states | `SR-DORA-001` | Art. 9(2) — CIA+A 4-way AND + at-rest/in-use/in-transit 3-way OR; Art. 9(2) — in-transit dimension (same locus, explicit in OJ); Art. 9(2) — integrity dimension (same locus, explicit in OJ) | DORA-C09, DORA-C10, DORA-C11 | SO-D-01.4.HL -> SO-DORA-001 -> SO-D-01.4.DORA | PR.DS-01, PR.DS-02, PR.DS-10, ID.AM-08 | — | — |

## D-02.1 — Vulnerability Identification

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 2.1.4 — Continuous ICT-risk identification + at-least-yearly scenario review (hard anchor) | `SR-DORA-004` | Art. 7(2) — `on a continuous basis, identify all sources of ICT risk`; Art. 8(2) — `identify all sources of ICT risk … and assess cyber threats and ICT vulnerabilities relevant to their ICT supported business functions` | DORA-C06, DORA-C08 | SO-D-02.1.HL -> SO-DORA-003 -> SO-D-02.1.DORA | ID.RA-01, ID.RA-03 | — | — |

## D-02.2 — Patch Management & Updates

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 2.2.2 — Appropriate and comprehensive documented patch policy + automated blast-radius isolation of affected information assets | `SR-DORA-006` | Art. 9(4)(b) — `sound network and infrastructure management structure using appropriate techniques, methods and protocols that may include implementing automated mechanisms to isolate affected information assets in the event of cyber-attacks` | DORA-C13 | SO-D-02.2.HL -> SO-DORA-004 -> SO-D-02.2.DORA | PR.PS-01, PR.IR-01, PR.IR-03 | — | — |

## D-02.3 — Coordinated Vulnerability Disclosure

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-02.4 — Threat-Led Penetration Testing

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 2.4.2 — Sound and comprehensive testing programme (12-modality portfolio under Art. 25(1)) + advanced TLPT every 3 years under Art. 26(1) where Art. 26(8) significant-entity criteria are met | `SR-DORA-008` | Art. 24(1) — `establish, maintain and review a sound and comprehensive digital operational resilience testing programme as an integral part of the ICT risk-management framework`; Art. 25(1) — testing modalities portfolio (12-way open list) | DORA-C32, DORA-C33 | SO-D-02.4.HL -> SO-DORA-005 -> SO-D-02.4.DORA | GV.OV-02, ID.RA-01, PR.PS-06 | — | — |

## D-03.1 — Identity Lifecycle Management

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 3.1.4 — Staff + service identities managed with assertion-conveyance integrity under strong-authentication discipline | `SR-DORA-002` | Art. 9(4)(d) — strong authentication mechanisms based on relevant standards and dedicated control systems; Art. 9(4)(d) same locus — T4 reads `Multi-Factor Authentication`; OJ says `strong authentication mechanisms`; Art. 9(4)(d) same locus — `protection measures of cryptographic keys` | DORA-C15, DORA-C16, DORA-C17 | SO-D-03.1.HL -> SO-DORA-002 -> SO-D-03.1.DORA | PR.AA-03, PR.AA-04 | — | — |

## D-03.2 — Multi-Factor Authentication

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 3.2.4 — Strong authentication mechanisms based on relevant standards (Art. 9(4)(d); dominant EBA MFA reading) | `SR-DORA-002` | Art. 9(4)(d) — strong authentication mechanisms based on relevant standards and dedicated control systems; Art. 9(4)(d) same locus — T4 reads `Multi-Factor Authentication`; OJ says `strong authentication mechanisms`; Art. 9(4)(d) same locus — `protection measures of cryptographic keys` | DORA-C15, DORA-C16, DORA-C17 | SO-D-03.2.HL -> SO-DORA-002 -> SO-D-03.2.DORA | PR.AA-03, PR.AA-04 | — | — |

## D-03.3 — Authorisation & Least Privilege

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 3.3.4 — Financial-entity ICT security policies limit physical or logical access to information assets and ICT assets to what is required for legitimate and approved functions and activities only (literal `only` qualifier) | `SR-DORA-010` | Art. 9(4)(c) — `implement policies that limit the physical or logical access to information assets and ICT assets to what is required for legitimate and approved functions and activities only` | DORA-C14 | SO-D-03.3.HL -> SO-DORA-006 -> SO-D-03.3.DORA | PR.AA-05, PR.AA-06 | — | — |

## D-03.4 — Secure System Defaults

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-04.1 — Incident Detection & Triage

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 4.1.4 — Multi-class anomalous-activity detection with SPOF identification, alert thresholds, automatic escalation, and Art. 17(1) `detect` leg of incident management process | `SR-DORA-011` | Art. 10(1) — `mechanisms to promptly detect anomalous activities … including ICT network performance issues and ICT-related incidents, and to identify potential material single points of failure` | DORA-C20 | SO-D-04.1.HL -> SO-DORA-007 -> SO-D-04.1.DORA | DE.CM-01, DE.CM-09, DE.AE-02 | — | — |

## D-04.2 — Incident Containment & Response

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 4.2.4 — Financial-entity BC arrangements: dedicated, appropriate and documented response/recovery plans + backup policies + restoration procedures; independent internal audit for non-microenterprises | `SR-DORA-013` | Art. 11(1) — `comprehensive ICT business continuity policy, which may be adopted as a dedicated specific policy, forming an integral part of the overall business continuity policy of the financial entity` | DORA-C22 | SO-D-04.2.HL -> SO-DORA-010 -> SO-D-04.2.DORA | RC.RP-01, PR.IR-03 | — | — |

## D-04.3 — Incident Notification & Reporting

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 4.3.4 — Major ICT-related incident reported to competent authority `without undue delay`; affected clients informed `without undue delay` as soon as financial entity becomes aware — pending EBA/ESMA/EIOPA RTS (4h pending) | `SR-DORA-017` | Art. 19(1) — `Financial entities shall report major ICT-related incidents to the relevant competent authority`; Art. 19(3) — `financial entities shall, without undue delay as soon as they become aware of it, inform their clients about the major ICT-related incident` | DORA-C31 | SO-D-04.3.HL -> SO-DORA-008 -> SO-D-04.3.DORA | RS.CO-02, RS.MA-04 | — | — |

## D-04.4 — Incident Recovery & Lessons Learned

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 4.4.4 — Comprehensive ICT BC policy with dedicated appropriate documented arrangements + response/recovery plans + backup-scoping on criticality/confidentiality + restoration procedures; OJ-corrected Art. 11(2)(a)–(e) BC-policy objectives preserved verbatim | `SR-DORA-013` | Art. 11(1) — `comprehensive ICT business continuity policy, which may be adopted as a dedicated specific policy, forming an integral part of the overall business continuity policy of the financial entity` | DORA-C22 | SO-D-04.4.HL -> SO-DORA-010 -> SO-D-04.4.DORA | RC.RP-01, PR.IR-03 | — | — |

## D-05.1 — Data Minimisation

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-05.2 — Retention & Archiving

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-05.3 — Right to Erasure

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-05.4 — Data Portability

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-06.1 — Vendor Risk Assessment

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 6.1.4 — ICT-third-party-as-financial-entity-counterparty risk under Art. 28(1) four-factor proportionality (nature, scale, complexity, importance) with Art. 28(5) CIF escalator | `SR-DORA-019` | Art. 28(1) — `manage ICT third-party risk … taking into account: (i) the nature, scale, complexity and importance of ICT-related dependencies; (ii) the risks arising from contractual arrangements on the use of ICT services … taking into account the criticality or importance of the respective service, process or function` | DORA-C35 | SO-D-06.1.HL -> SO-DORA-011 -> SO-D-06.1.DORA | GV.SC-02, ID.AM-04 | — | — |

## D-06.2 — Software Bill of Materials (SBOM)

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-06.3 — Contractual Security Obligations

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 6.3.4 — Art. 30(1)+(2) 9-element ICT-contract closed-list + Art. 28(5) standards record + Art. 30(3) CIF-only clauses (audit/access/exit) — clause-list union with GDPR Art. 28(3) when same ICT provider is processor | `SR-DORA-019` | Art. 28(1) — `manage ICT third-party risk … taking into account: (i) the nature, scale, complexity and importance of ICT-related dependencies; (ii) the risks arising from contractual arrangements on the use of ICT services … taking into account the criticality or importance of the respective service, process or function` | DORA-C35 | SO-D-06.3.HL -> SO-DORA-011 -> SO-D-06.3.DORA | GV.SC-02, ID.AM-04 | — | — |

## D-06.4 — Third-Party Boundary Management

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 6.4.4 — Art. 30(3)(e)(i)/(ii) unrestricted access / inspection / audit rights (including on-site documentation copy right) for financial entity / appointed third party / competent authority over CIF-supporting ICT third-party providers, with narrowly bounded alternative-assurance exception only where other clients' rights are affected | `SR-DORA-022` | Art. 30(3)(e)(i)+(ii) — `unrestricted rights of access, inspection and audit by the financial entity, or an appointed third party, and by the competent authority … the right to take copies of relevant documentation on-site … the right to agree on alternative assurance levels if other clients' rights are affected` | DORA-C38 | SO-D-06.4.HL -> SO-DORA-012 -> SO-D-06.4.DORA | GV.SC-03, DE.CM-06 | — | — |

## D-07.1 — Secure-by-Design Principles

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 7.1.4 — Sound network and infrastructure management structure with appropriate techniques/methods/protocols, patch and update policies, and secure-by-design operationalised via change-management six-step + testing programme (DORA partial — no OJ dedicated by-design mandate) | `SR-DORA-004` | Art. 7(2) — `on a continuous basis, identify all sources of ICT risk`; Art. 8(2) — `identify all sources of ICT risk … and assess cyber threats and ICT vulnerabilities relevant to their ICT supported business functions` | DORA-C06, DORA-C08 | SO-D-07.1.HL -> SO-DORA-004 -> SO-D-07.1.DORA | ID.RA-01, ID.RA-03 | — | — |

## D-07.2 — Secure Coding Practices

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 7.2.2 — ICT change-management six-step (recorded/tested/assessed/approved/implemented/verified) with implicit coding-dimension inference through tested/assessed legs and Art. 25 testing modalities (DORA partial — no OJ-mandated secure-coding-standards prescription; SR-DORA-023 partial at D-07.2 by inference only, D-07.4 primary) | `SR-DORA-023` | Art. 9(4)(e) — `implement documented policies, procedures and controls for ICT change management, including changes to software, hardware, firmware components, systems or security parameters … that are based on a risk assessment approach … in order to ensure that all changes to ICT systems are recorded, tested, assessed, approved, implemented and verified in a controlled manner` | DORA-C18 | SO-D-07.2.HL -> SO-DORA-013 -> SO-D-07.2.DORA | PR.PS-01, PR.PS-02, PR.PS-06 | — | — |

## D-07.3 — CI/CD Pipeline Security

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-07.4 — Change Management

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 7.4.2 — Entity-side ICT change records demonstrate controlled, risk-based change execution | `SR-DORA-023` | Art. 9(4)(e) — `implement documented policies, procedures and controls for ICT change management, including changes to software, hardware, firmware components, systems or security parameters … that are based on a risk assessment approach … in order to ensure that all changes to ICT systems are recorded, tested, assessed, approved, implemented and verified in a controlled manner` | DORA-C18 | SO-D-07.4.HL -> SO-DORA-013 -> SO-D-07.4.DORA | PR.PS-01, PR.PS-02, PR.PS-06 | — | — |

## D-08.1 — General Security Awareness

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 8.1.4 — ICT security awareness programmes and digital operational resilience training as compulsory modules in financial-entity staff training schemes | `SR-DORA-025` | Art. 13(6) — `ICT security awareness programmes and digital operational resilience training as compulsory modules in their staff training schemes`; Art. 13(6) same locus — `level of complexity commensurate to the remit of their functions`; Art. 13(6) same locus — T4 mapping mismatch per `../Regulation/DORA/Ambiguity/05_DORA.md` §2.26 | DORA-C27, DORA-C28, DORA-C26 | SO-D-08.1.HL -> SO-DORA-015 -> SO-D-08.1.DORA | PR.AT-01, PR.AT-02 | — | — |

## D-08.2 — Role-Specific Competence

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 8.2.4 — Financial-entity staff training modules with level of complexity commensurate to the remit of staff functions | `SR-DORA-025` | Art. 13(6) — `ICT security awareness programmes and digital operational resilience training as compulsory modules in their staff training schemes`; Art. 13(6) same locus — `level of complexity commensurate to the remit of their functions`; Art. 13(6) same locus — T4 mapping mismatch per `../Regulation/DORA/Ambiguity/05_DORA.md` §2.26 | DORA-C27, DORA-C28, DORA-C26 | SO-D-08.2.HL -> SO-DORA-015 -> SO-D-08.2.DORA | PR.AT-01, PR.AT-02 | — | — |

## D-08.3 — Management Board Training

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 8.3.2 — Members of the management body of financial entities actively keep up to date with sufficient knowledge and skills to understand and assess ICT risk, commensurate to the ICT risk being managed | `SR-DORA-024` | Art. 5(4) — `Members of the management body … shall actively keep up to date with sufficient knowledge and skills … including by following specific training on a regular basis, commensurate to the ICT risk being managed` | DORA-C02 | SO-D-08.3.HL -> SO-DORA-014 -> SO-D-08.3.DORA | PR.AT-02, GV.RR-01 | — | — |

## D-09.1 — Information Security Policies

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 9.1.4 — Financial entity operates a sound, comprehensive, well-documented ICT risk-management framework with three-lines-of-defence and identified, classified, documented ICT supported business functions and assets | `SR-DORA-026` | Art. 5(2) — `the management body of the financial entity shall define, approve, oversee and be responsible for the implementation of all arrangements related to the ICT risk management framework` | DORA-C01 | SO-D-09.1.HL -> SO-DORA-016 -> SO-D-09.1.DORA | GV.RR-01, GV.RR-02 | — | — |

## D-09.2 — Impact & Risk Assessments

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 9.2.4 — Financial entity continuously identifies ICT risks and reviews risk scenarios at least yearly under the three-lines-of-defence model with classification and documentation per Art. 7(1)-(2) | `SR-DORA-028` | Art. 6(4) — `assign the responsibility for managing and overseeing ICT risk to a control function and ensure an appropriate level of independence … according to the three lines of defence model, or an internal risk management and control model` | DORA-C04 | SO-D-09.2.HL -> SO-DORA-017 -> SO-D-09.2.DORA | GV.RR-02, GV.RM-02 | — | — |

## D-09.3 — Asset Inventories

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 9.3.3 — Financial entity identifies, classifies, and adequately documents ICT supported business functions + roles and responsibilities + information assets + ICT assets + dependencies in relation to ICT risk under three-lines-of-defence and management-body governance | `SR-DORA-029` | Art. 7(1) — `identify, classify and adequately document all ICT supported business functions, roles and responsibilities, the information assets and ICT assets supporting those functions, and their roles and dependencies in relation to ICT risk` | DORA-C05 | SO-D-09.3.HL -> SO-DORA-017 -> SO-D-09.3.DORA | ID.AM-01, ID.AM-02, ID.AM-03, ID.AM-05 | — | — |

## D-09.4 — Records of Processing

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 9.4.4 — Financial entity develops and documents an information security policy defining rules to protect availability, authenticity, integrity and confidentiality of data, information assets and ICT assets, including those of customers where applicable (Art. 9(4)(a) DORA) | `SR-DORA-031` | Art. 9(4)(a) — `develop and document an information security policy defining rules to protect the availability, authenticity, integrity and confidentiality of data, information assets and ICT assets, including those of their customers, where applicable` | DORA-C12 | SO-D-09.4.HL -> SO-DORA-018 -> SO-D-09.4.DORA | GV.PO-01, ID.AM-08, GV.OC-03 | — | — |

## D-10.1 — Continuous Security Monitoring

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 10.1.4 — Financial entity continuously monitors and controls the security and functioning of ICT systems and tools, with prompt anomalous-activity detection through multi-layered controls and continuous ICT risk identification | `SR-DORA-030` | Art. 8(1) — `continuously monitor and control the security and functioning of ICT systems and tools and shall minimise the impact of ICT risk on ICT systems through the deployment of appropriate ICT security tools, policies and procedures` | DORA-C07 | SO-D-10.1.HL -> SO-DORA-018 -> SO-D-10.1.DORA | DE.CM-01, DE.CM-09, PR.PS-04 | — | — |

## D-10.2 — Audit Logging & Traceability

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 10.2.3 — Financial entity develops and documents an information security policy defining rules to protect the availability, authenticity, integrity and confidentiality of data, information assets and ICT assets, with logging implicit in CIA+A monitoring | `SR-DORA-031` | Art. 9(4)(a) — `develop and document an information security policy defining rules to protect the availability, authenticity, integrity and confidentiality of data, information assets and ICT assets, including those of their customers, where applicable` | DORA-C12 | SO-D-10.2.HL -> SO-DORA-031 -> SO-D-10.2.DORA | GV.PO-01, ID.AM-08, GV.OC-03 | — | — |

## D-10.3 — Compliance Testing

| Requisito | SR | Artigos | Cláusulas | Objetivos (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 10.3.4 — Financial entity establishes, maintains and reviews a sound and comprehensive digital operational resilience testing programme with a 12-way testing modalities portfolio and TLPT for significant entities on a regular basis | `SR-DORA-008` | Art. 24(1) — `establish, maintain and review a sound and comprehensive digital operational resilience testing programme as an integral part of the ICT risk-management framework`; Art. 25(1) — testing modalities portfolio (12-way open list) | DORA-C32, DORA-C33 | SO-D-10.3.HL -> SO-DORA-019 -> SO-D-10.3.DORA | GV.OV-02, ID.RA-01, PR.PS-06 | — | — |

