# Traceability — AI_Act

> Chain: regulation -> article(s) -> ambiguity clause(s) -> baseline goal -> SO-AI_Act -> Sub-SO -> requirement -> controls. Generated from the modular corpus + `sr_control_mappings` (dashboard-uniformized).

## D-01.1 — Data at Rest Encryption

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-01.2 — Data in Transit Encryption

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-01.3 — Cryptographic Key Management

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-01.4 — Data Integrity Mechanisms

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 1.4.4 — High-risk AI system resilient to errors, faults, or inconsistencies via technical redundancy | `SR-AIACT-015` | Art. 15(3) — `High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment … The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans` | AIA-C17 | SG-AIACT-009 | PR.IR-03, PR.IR-04, PR.DS-11 | — | MEASURE-2.6, MEASURE-2.7, MANAGE-2.3 |

## D-02.1 — Vulnerability Identification

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 2.1.5 — Continuous iterative AI risk-identification (Art. 9(2) 4-step cycle) + AI-specific attack-taxonomy register (Art. 15(4)–(5)) | `SR-AIACT-001` | Art. 9(1) — `A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems` | AIA-C01 | SG-AIACT-001 | GV.RM-01, GV.RM-06 | — | GOVERN-1.1, GOVERN-1.3, GOVERN-1.5, MAP-5.1 |

## D-02.2 — Patch Management & Updates

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-02.3 — Coordinated Vulnerability Disclosure

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-02.4 — Threat-Led Penetration Testing

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 2.4.3 — High-risk AI systems tested to perform consistently for intended purpose (Art. 9(6)) and tested in real-world conditions per Art. 60 (Art. 9(7)) | `SR-AIACT-003` | Art. 9(6) — `High-risk AI systems shall be tested for the purpose of identifying the most appropriate and targeted risk management measures. Testing shall ensure that high-risk AI systems perform consistently for their intended purpose`; Art. 9(7) — `Testing procedures may include testing in real-world conditions in accordance with Article 60` | AIA-C03, AIA-C04 | SG-AIACT-002 | ID.RA-01, ID.RA-04, PR.PS-06, GV.SC-04 | — | MEASURE-1.1, MEASURE-2.1, MEASURE-2.3, MAP-3.3 |

## D-03.1 — Identity Lifecycle Management

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-03.2 — Multi-Factor Authentication

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-03.3 — Authorisation & Least Privilege

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-03.4 — Secure System Defaults

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-04.1 — Incident Detection & Triage

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-04.2 — Incident Containment & Response

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-04.3 — Incident Notification & Reporting

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 4.3.5 — Serious incident involving high-risk AI reported to market surveillance authorities under 4-trigger × 4-timeline matrix (15d default / 10d death / 2d widespread / 15d causal-link-anchor); GPAI systemic-risk report separately to AI Office under Art. 55 | `SR-AIACT-022` | Art. 73(1)–(4) — `report any serious incident`; `not later than 15 days after … becomes aware`; `not later than two days` (widespread infringement); `not later than 10 days` (death) | AIA-C26 | SG-AIACT-013 | RS.CO-02, RS.MA-04, RS.MA-03, RS.MA-01 | — | MANAGE-2.3, MANAGE-4.3, GOVERN-1.1 |

## D-04.4 — Incident Recovery & Lessons Learned

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-05.1 — Data Minimisation

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 5.1.3 — High-risk AI training/validation/testing datasets meet Art. 10(3) quality criteria and Art. 10(2) 8-element data-governance practice; Art. 10(5) special-category 6-cumulative-condition gateway documented when applicable | `SR-AIACT-003` | Art. 9(6) — `High-risk AI systems shall be tested for the purpose of identifying the most appropriate and targeted risk management measures. Testing shall ensure that high-risk AI systems perform consistently for their intended purpose`; Art. 9(7) — `Testing procedures may include testing in real-world conditions in accordance with Article 60` | AIA-C03, AIA-C04 | SG-AIACT-002 | ID.RA-01, ID.RA-04, PR.PS-06, GV.SC-04 | — | MEASURE-1.1, MEASURE-2.1, MEASURE-2.3, MAP-3.3 |

## D-05.2 — Retention & Archiving

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 5.2.3 — High-risk AI system logs retained ≥6 months per Art. 19(1); upward adjustment justified by intended purpose; floor-within-ceiling layering with GDPR when logs contain personal data | `SR-AIACT-008` | Art. 12(4) per T5 — **T5 mapping error**: Art. 12 has only paragraphs 1, 2, 3 in the OJ; the substance is in Art. 19(1); Art. 19(1) — `the logs shall be kept for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in the applicable Union or national law` | AIA-C11, AIA-C19 | SG-AIACT-006 | PR.PS-04, GV.PO-02 | — | MEASURE-2.4, MEASURE-4.2, GOVERN-1.4 |

## D-05.3 — Right to Erasure

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-05.4 — Data Portability

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-06.1 — Vendor Risk Assessment

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-06.2 — Software Bill of Materials (SBOM)

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-06.3 — Contractual Security Obligations

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-07.1 — Secure-by-Design Principles

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 7.1.5 — High-risk AI systems designed and developed to achieve appropriate level of accuracy, robustness, and cybersecurity, performing consistently throughout their lifecycle, with QMS covering design/design-control/design-verification | `SR-AIACT-014` | Art. 15(1) — `High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle` | AIA-C16 | SG-AIACT-009 | PR.PS-06, PR.IR-03, ID.RA-04 | — | MEASURE-2.5, MEASURE-2.6, MEASURE-2.7, GOVERN-1.2 |

## D-07.2 — Secure Coding Practices

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 7.2.3 — High-risk AI systems designed and developed to effectively resist, as appropriate to purpose and conditions of use, attempts at training-data poisoning, model poisoning, adversarial examples, model evasion, confidentiality attacks or model flaws | `SR-AIACT-016` | Art. 15(4)–(5) — `measures to prevent, detect, respond to, resolve and control for attacks trying to manipulate the training data set (data poisoning), or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws` | AIA-C18 | SG-AIACT-009 | ID.RA-04, PR.PS-06, RS.MI-01, RS.MA-03 | — | MEASURE-2.7, MAP-3.2, MANAGE-1.3 |

## D-07.3 — CI/CD Pipeline Security

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-07.4 — Change Management

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-08.1 — General Security Awareness

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-08.2 — Role-Specific Competence

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 8.2.5 — High-risk AI system human overseers enabled with the 5 cumulative oversight abilities (provider) and assigned with competence, training, authority, and support (deployer) | `SR-AIACT-013` | Art. 14(4) — `natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate: (a) to properly understand … (b) to remain aware … (c) to correctly interpret … (d) to decide … (e) to intervene …` | AIA-C15 | SG-AIACT-008 | PR.AT-02, PR.AT-01, GV.RR-02 | — | MAP-3.5, GOVERN-2.1, GOVERN-2.2 |

## D-08.3 — Management Board Training

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-09.1 — Information Security Policies

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 9.1.5 — Provider of high-risk AI system operates a documented quality management system with at least 13 enumerated aspects and instructions for use enabling deployer-interpretable transparency | `SR-AIACT-010` | Art. 13(1) — `High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system's output and use it appropriately. An appropriate type and degree of transparency shall be ensured` | AIA-C12 | SG-AIACT-007 | GV.PO-01, GV.OC-03, GV.OC-04 | — | GOVERN-1.4, MAP-1.1, MEASURE-2.8, MEASURE-2.9 |

## D-09.2 — Impact & Risk Assessments

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 9.2.5 — Provider establishes, implements, documents, and maintains a continuous iterative risk-management system across the AI lifecycle with the four Art. 9(2)(a)-(d) steps, cross-coupled with Art. 27 FRIA for certain Annex III categories | `SR-AIACT-001` | Art. 9(1) — `A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems` | AIA-C01 | SG-AIACT-001 | GV.RM-01, GV.RM-06 | — | GOVERN-1.1, GOVERN-1.3, GOVERN-1.5, MAP-5.1 |

## D-09.3 — Asset Inventories

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-09.4 — Records of Processing

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 9.4.5 — Provider of high-risk AI system draws up and keeps up-to-date the Annex IV technical documentation before placing on market or putting into service, the 13-element QMS documentation, and the Art. 19(1) provider logs under their control | `SR-AIACT-008` | Art. 12(4) per T5 — **T5 mapping error**: Art. 12 has only paragraphs 1, 2, 3 in the OJ; the substance is in Art. 19(1); Art. 19(1) — `the logs shall be kept for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in the applicable Union or national law` | AIA-C11, AIA-C19 | SG-AIACT-006 | PR.PS-04, GV.PO-02 | — | MEASURE-2.4, MEASURE-4.2, GOVERN-1.4 |

## D-10.1 — Continuous Security Monitoring

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 10.1.5 — Provider of high-risk AI system establishes and documents a post-market monitoring system proportionate to the nature of the AI technologies and the risks, actively and systematically collecting, documenting and analysing relevant data across the AI lifecycle | `SR-AIACT-021` | Art. 72(1)–(2) — `Providers shall establish and document a post-market monitoring system in a manner that is proportionate to the nature of the AI technologies and the risks of the high-risk AI system. The post-market monitoring system shall actively and systematically collect, document and analyse relevant data`; Art. 74(1) — `Regulation (EU) 2019/1020 shall apply to AI systems covered by this Regulation` | AIA-C25, AIA-C27 | SG-AIACT-012 | DE.CM-09, ID.IM-04, GV.OV-03 | — | MANAGE-4.1, MEASURE-3.1, MEASURE-4.1, GOVERN-1.5 |

## D-10.2 — Audit Logging & Traceability

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 10.2.4 — High-risk AI system technically allows automatic recording of events (logs) over the lifetime of the system with traceability appropriate to the intended purpose; provider keeps logs under their control for at least six months | `SR-AIACT-007` | Art. 12(1) — `High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system`; Art. 12(2) — `In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) … (b) … (c) …` | AIA-C09, AIA-C10 | SG-AIACT-005 | PR.PS-04, DE.CM-09, DE.AE-03 | — | MEASURE-2.4, MEASURE-3.1, GOVERN-1.6 |

## D-10.3 — Compliance Testing

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 10.3.5 — Provider ensures high-risk AI system is tested for the purpose of identifying risk management measures, performs consistently for intended purpose, may be tested in real-world conditions per Article 60, and achieves appropriate accuracy/robustness/cybersecurity throughout the AI-system lifecycle | `SR-AIACT-003` | Art. 9(6) — `High-risk AI systems shall be tested for the purpose of identifying the most appropriate and targeted risk management measures. Testing shall ensure that high-risk AI systems perform consistently for their intended purpose`; Art. 9(7) — `Testing procedures may include testing in real-world conditions in accordance with Article 60` | AIA-C03, AIA-C04 | SG-AIACT-002 | ID.RA-01, ID.RA-04, PR.PS-06, GV.SC-04 | — | MEASURE-1.1, MEASURE-2.1, MEASURE-2.3, MAP-3.3 |

