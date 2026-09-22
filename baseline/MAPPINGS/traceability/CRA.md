# Traceability — CRA

> Chain: regulation -> article(s) -> ambiguity clause(s) -> baseline goal -> SO-CRA -> Sub-SO -> requirement -> controls. Generated from the modular corpus + `sr_control_mappings` (dashboard-uniformized).

## D-01.1 — Data at Rest Encryption

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 1.1.3 — Product-stored data is encrypted using state-of-the-art mechanisms | `SR-CRA-002` | Annex I Part I (2)(e) — at-rest encryption; Annex I Part I (1) — chapeau | CRA-CL134, CRA-CL129 | SO-D-01.1.HL -> SO-CRA-002 -> SO-D-01.1.CRA | PR.DS-01 | — | — |

## D-01.2 — Data in Transit Encryption

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 1.2.2 — Product-transmitted data is encrypted with state-of-the-art mechanisms and exposed interfaces are minimised | `SR-CRA-003` | Annex I Part I (2)(e) — in-transit encryption; Annex I Part I (2)(j) — limit attack surfaces incl. external interfaces | CRA-CL134, CRA-CL139 | SO-D-01.2.HL -> SO-CRA-003 -> SO-D-01.2.CRA | PR.DS-02, PR.IR-01 | — | — |

## D-01.3 — Cryptographic Key Management

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 1.3.2 — Cryptographic keys of product with digital elements separated from operational environment | `SR-CRA-004` | Annex I Part I (2)(e) — `and by using other technical means`; Annex I Part I (2)(d) — access control; Art. 6(a) proviso — installation/conditions | CRA-CL134, CRA-CL133, CRA-CL2 | SO-D-01.3.HL -> SO-CRA-004 -> SO-D-01.3.CRA | PR.DS-01, PR.AA-05, GV.OV-01 | — | — |

## D-01.4 — Data Integrity Mechanisms

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 1.4.2 — Integrity of stored/transmitted/processed data + commands + programs + configuration protected against unauthorised manipulation | `SR-CRA-005` | Annex I Part I (2)(f) — integrity + report on corruptions; Annex I Part I (2)(l) — logging + monitoring | CRA-CL135, CRA-CL141 | SO-D-01.4.HL -> SO-CRA-005 -> SO-D-01.4.CRA | PR.DS-01, PR.DS-10, PR.PS-04 | — | — |

## D-02.1 — Vulnerability Identification

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 2.1.3 — Product made available without known exploitable vulnerabilities; SBOM-backed identification throughout support period | `SR-CRA-006` | Annex I Part I (2)(a) — no known exploitable vulnerabilities; Annex I Part I (1) — chapeau | CRA-CL130, CRA-CL129 | SO-D-02.1.HL -> SO-CRA-006 -> SO-D-02.1.CRA | ID.RA-01, PR.PS-02 | — | — |

## D-02.2 — Patch Management & Updates

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 2.2.1 — Vulnerabilities remediated without delay; separated secure update distribution; 5-year support + 10-year availability tail | `SR-CRA-010` | Annex I Part II (2) — address and remediate without delay; Annex I Part I (2)(c) — vulnerabilities addressed through security updates; Art. 13(6) sentence 1 — component vulnerability address + remediate | CRA-CL144, CRA-CL132, CRA-CL24 | SO-D-02.2.HL -> SO-CRA-008 -> SO-D-02.2.CRA | PR.PS-02, ID.RA-06 | — | — |

## D-02.3 — Coordinated Vulnerability Disclosure

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 2.3.1 — Manufacturer puts in place, documents and enforces CVD policy for products with digital elements; publicly identifiable contact address; SPOC; public disclosure of fixed vulnerabilities with `duly justified` delay exception | `SR-CRA-019` | Annex I Part II (5) — CVD policy; Art. 13(8) sentence 6 — CVD policy; Art. 24(3) — OSS steward Art. 14 extension cross-ref to CVD | CRA-CL147, CRA-CL32, CRA-CL103 | SO-D-02.3.HL -> SO-CRA-012 -> SO-D-02.3.CRA | GV.PO-01, GV.SC-04 | — | — |

## D-02.4 — Threat-Led Penetration Testing

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 2.4.1 — Effective and regular tests and reviews of product security across the support period with Annex VII §6 test-report evidence + Annex VIII Part II (8) Module B periodic audits | `SR-CRA-022` | Annex I Part II (3) — effective and regular tests and reviews; Annex VII §6 — test reports in technical documentation; Annex VIII Part II (8) — Module B periodic audits of vuln handling | CRA-CL145, CRA-CL165, CRA-CL174 | SO-D-02.4.HL -> SO-CRA-014 -> SO-D-02.4.CRA | ID.RA-01, PR.PS-06, DE.CM-09 | — | — |

## D-03.1 — Identity Lifecycle Management

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 3.1.3 — Product users, services, and integrated components identities managed in verifiable manner throughout operational lifetime | `SR-CRA-023` | Annex I Part I (2)(d) — appropriate control mechanisms incl. authentication, identity or access management; Art. 13(15) — type/batch/serial number or other element; Annex II §3 — name and type and unique identification | CRA-CL133, CRA-CL40, CRA-CL153 | SO-D-03.1.HL -> SO-CRA-015 -> SO-D-03.1.CRA | PR.AA-01, ID.AM-01 | — | — |

## D-03.2 — Multi-Factor Authentication

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 3.2.3 — Appropriate control mechanisms for protection from unauthorised access, which may include authentication | `SR-CRA-023` | Annex I Part I (2)(d) — appropriate control mechanisms incl. authentication, identity or access management; Art. 13(15) — type/batch/serial number or other element; Annex II §3 — name and type and unique identification | CRA-CL133, CRA-CL40, CRA-CL153 | SO-D-03.2.HL -> SO-CRA-016 -> SO-D-03.2.CRA | PR.AA-01, ID.AM-01 | — | — |

## D-03.3 — Authorisation & Least Privilege

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 3.3.3 — Access to product with digital elements limited to authenticated and authorised users, services, and hardware; possible unauthorised access reported; attack surfaces including external interfaces limited (multi-leg product-side authorisation framework) | `SR-CRA-024` | Annex I Part I (2)(d) — report on possible unauthorised access; Annex I Part I (2)(j) — limit attack surfaces | CRA-CL133, CRA-CL139 | SO-D-03.3.HL -> SO-CRA-017 -> SO-D-03.3.CRA | PR.AA-05, PR.AA-06, DE.CM-09 | — | — |

## D-03.4 — Secure System Defaults

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 3.4.2 — Products with digital elements made available with secure-by-default configuration + reset-to-original-state capability + auto-update default + opt-out + postponement (Annex I Part I (2)(b) + (2)(c) multi-leg product default) | `SR-CRA-025` | Annex I Part I (2)(b) — secure by default configuration; Art. 6(a) proviso — properly installed, intended purpose, reasonably foreseeable; Art. 3(23) — intended purpose | CRA-CL131, CRA-CL2, CRA-CL3 | SO-D-03.4.HL -> SO-CRA-018 -> SO-D-03.4.CRA | PR.PS-01, ID.AM-08 | — | — |

## D-04.1 — Incident Detection & Triage

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 4.1.3 — Product-internal activity recorded and monitored with user opt-out where appropriate; corruption / unauthorised modification reported | `SR-CRA-027` | Annex I Part I (2)(l) — recording + monitoring + user opt-out; Annex II §8 — detailed instructions | CRA-CL141, CRA-CL158 | SO-D-04.1.HL -> SO-CRA-020 -> SO-D-04.1.CRA | PR.PS-04, DE.AE-08 | — | — |

## D-04.2 — Incident Containment & Response

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 4.2.3 — Product availability preserved after incident via resilience + DoS resistance + cross-product impact minimisation + exploitation mitigation; Art. 13(21) corrective measures on non-conformity | `SR-CRA-043` | Annex I Part I (2)(h) — availability + resilience + DoS; Annex I Part I (2)(k) — exploitation mitigation | CRA-CL137, CRA-CL140 | SO-D-04.2.HL -> SO-CRA-021 -> SO-D-04.2.CRA | PR.IR-03, ID.AM-08 | — | — |

## D-04.3 — Incident Notification & Reporting

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 4.3.3 — Actively-exploited vulnerability notified on three-tier pattern — 24h early warning + 72h vulnerability notification + 14d final report — to CSIRT + ENISA, with severe-incident (SI) parallel pathway at 24h/72h/1m | `SR-CRA-029` | Art. 14(2)(a) — AEV early warning 24h; Art. 14(1) sentence 1 — awareness trigger | CRA-CL53, CRA-CL51 | SO-D-04.3.HL -> SO-CRA-024 -> SO-D-04.3.CRA | RS.MA-02, RS.CO-02 | — | — |

## D-04.4 — Incident Recovery & Lessons Learned

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 4.4.3 — Product with digital elements preserves essential and basic functions `also after an incident` through resilience and exploitation-mitigation architecture (intra-product recovery, layered not substituted) | `SR-CRA-043` | Annex I Part I (2)(h) — availability + resilience + DoS; Annex I Part I (2)(k) — exploitation mitigation | CRA-CL137, CRA-CL140 | SO-D-04.4.HL -> SO-CRA-021 -> SO-D-04.4.CRA | PR.IR-03, ID.AM-08 | — | — |

## D-05.1 — Data Minimisation

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 5.1.2 — Product data limited to what is adequate, relevant, and necessary in relation to the intended purpose of the product, with risk-assessment proportionality calibration | `SR-CRA-046` | Annex I Part I (2)(g) — adequate, relevant, necessary = data minimisation; Art. 13(3) sentence 2 — intended purpose + reasonably foreseeable use; Art. 3(23) — intended purpose | CRA-CL136, CRA-CL19, CRA-CL3 | SO-D-05.1.HL -> SO-CRA-034 -> SO-D-05.1.CRA | ID.AM-08, ID.AM-03 | — | — |

## D-05.2 — Retention & Archiving

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 5.2.2 — Security updates available across support period and the 10-year-or-remainder tail; Annex II information accessible for ≥10 years from placing on market; support-period end-date communicated at purchase | `SR-CRA-016` | Art. 13(9) — 10-year update availability | CRA-CL33 | SO-D-05.2.HL -> SO-CRA-035 -> SO-D-05.2.CRA | PR.PS-02, GV.OV-02 | — | — |

## D-05.3 — Right to Erasure

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 5.3.2 — User of a product with digital elements can securely and easily remove, on a permanent basis, all data and settings of the product via a discoverable user-interface affordance, with Annex II §8(d) decommissioning instructions | `SR-CRA-048` | Annex I Part I (2)(m) — secure and easily remove on a permanent basis all data and settings; Annex II §8(d) — secure decommissioning including how user data can be securely removed | CRA-CL142, CRA-CL158 | SO-D-05.3.HL -> SO-CRA-036 -> SO-D-05.3.CRA | PR.DS-10, ID.AM-08 | — | — |

## D-05.4 — Data Portability

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-06.1 — Vendor Risk Assessment

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 6.1.3 — Third-party-component due diligence procedural + substantive including non-commercial OSS per Art. 3(48), with Art. 13(6) vulnerability reporting and Annex VII §2 technical-documentation record | `SR-CRA-050` | Art. 13(5) — due diligence on third-party components; Art. 3(48) — free and open-source software definition | CRA-CL23a, CRA-CL48 | SO-D-06.1.HL -> SO-CRA-037 -> SO-D-06.1.CRA | GV.SC-01, GV.SC-02, ID.RA-02 | — | — |

## D-06.2 — Software Bill of Materials (SBOM)

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 6.2.1 — Three-anchored SBOM architecture: machine-readable format covering at least top-level dependencies authored at release + retained in technical documentation under Annex VII §2(b) + disclosed to MSAs on reasoned request under Annex VII §8 + optional user access under Annex II §9 | `SR-CRA-008` | Annex I Part II (1) — SBOM format; Art. 3(39) — SBOM definition (details and supply chain relationships) | CRA-CL143, CRA-CL39 | SO-D-06.2.HL -> SO-CRA-038 -> SO-D-06.2.CRA | ID.AM-02, GV.SC-02 | — | — |

## D-06.3 — Contractual Security Obligations

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 6.3.3 — Importer pre-market verification (Art. 19) + distributor due-care + non-conformity escalation (Art. 20) + component-vulnerability reporting (Art. 13(6)) — regulatory economic-operator duties, NOT DPA-style contracts | `SR-CRA-051` | Art. 13(6) sentence 1 — report + address + remediate component vulnerabilities; Art. 13(6) sentence 2 — share with component supplier | CRA-CL24, CRA-CL25 | SO-D-06.3.HL -> SO-CRA-037 -> SO-D-06.3.CRA | GV.SC-04, RS.MI-02 | — | — |

## D-06.4 — Third-Party Boundary Management

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 6.4.3 — Art. 18 written authorised representative mandate + Art. 21 own-name/trademark manufacturer-equivalent + Art. 22 third-party substantial-modification manufacturer-status + Art. 23 10-year upstream/downstream economic-operator identification log | `SR-CRA-059` | Art. 18(1) — AR appointment; Art. 18(2) — AR carve-out of non-delegable obligations | CRA-CL84, CRA-CL85 | SO-D-06.4.HL -> SO-CRA-041 -> SO-D-06.4.CRA | GV.RR-02, GV.SC-03 | — | — |

## D-07.1 — Secure-by-Design Principles

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 7.1.3 — Product with digital elements designed, developed and produced in accordance with Annex I Part I essential cybersecurity requirements with risk assessment propagated across planning, design, development, production, delivery and maintenance | `SR-CRA-064` | Art. 13(1) — design/development/production per Annex I Part I; Annex I Part I (1) — chapeau | CRA-CL14, CRA-CL129 | SO-D-07.1.HL -> SO-CRA-045 -> SO-D-07.1.CRA | PR.PS-06, GV.PO-02 | — | — |

## D-07.2 — Secure Coding Practices

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 7.2.1 — Product with digital elements designed, developed and produced to limit attack surfaces (including external interfaces) and to reduce incident impact via exploitation-mitigation mechanisms and techniques | `SR-CRA-067` | Annex I Part I (2)(j) — limit attack surfaces incl. external interfaces | CRA-CL139 | SO-D-07.2.HL -> SO-CRA-046 -> SO-D-07.2.CRA | PR.PS-01, PR.PS-02 | — | — |

## D-07.3 — CI/CD Pipeline Security

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 7.3.2 — Product-side secure-update delivery evidence for CRA-regulated products | `SR-CRA-009` | Annex I Part II (1) — SBOM contents; Annex VII §2(b) — SBOM in technical documentation; Annex VII §8 — SBOM on MSA request | CRA-CL143, CRA-CL161, CRA-CL167 | SO-D-07.3.HL -> SO-CRA-009 -> SO-D-07.3.CRA | ID.AM-02, GV.SC-03 | — | — |

## D-07.4 — Change Management

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 7.4.1 — Product-side change records preserve series-production conformity and substantial-modification decisions | `SR-CRA-069` | Art. 13(14) — series-of-production conformity | CRA-CL39 | SO-D-07.4.HL -> SO-CRA-047 -> SO-D-07.4.CRA | GV.OV-01, GV.PO-02 | — | — |

## D-08.1 — General Security Awareness

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 8.1.3 — Product with digital elements accompanied by detailed user-facing secure-use instructions covering the lifetime of the product | `SR-CRA-071` | Annex II §8(a)–(f) — detailed instructions; Art. 13(18) — accompany with Annex II info | CRA-CL158, CRA-CL43 | SO-D-08.1.HL -> SO-CRA-048 -> SO-D-08.1.CRA | PR.AT-01 | — | — |

## D-08.2 — Role-Specific Competence

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 8.2.3 — Where the product is intended for integration, information necessary for the integrator to comply with Annex I cybersecurity requirements and Annex VII documentation requirements is delivered | `SR-CRA-108` | Annex II §8(f) — information necessary for integrator to comply with Annex I + Annex VII | CRA-CL158 | SO-D-08.2.HL -> SO-CRA-048 -> SO-D-08.2.CRA | PR.AT-02, GV.SC-03 | — | — |

## D-08.3 — Management Board Training

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|

## D-09.1 — Information Security Policies

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 9.1.3 — Manufacturer and OSS-steward cybersecurity policies with verifiable documentation, CVD, support-period, and presumption of conformity via harmonised standards, common specifications, or CSA certification | `SR-CRA-072` | Art. 24(1) — OSS steward cybersecurity policy; Art. 3(14) — open-source software steward definition; Art. 3(48) — free and open-source software definition | CRA-CL101, CRA-CL14, CRA-CL48 | SO-D-09.1.HL -> SO-CRA-049 -> SO-D-09.1.CRA | GV.PO-01, GV.SC-01 | — | — |

## D-09.2 — Impact & Risk Assessments

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 9.2.3 — Manufacturer documents the cybersecurity risk assessment referred to in Art. 13(2) covering intended purpose + reasonably foreseeable use + Annex I Part I (2) applicability, updated during support period and recorded in Annex VII §3 | `SR-CRA-064` | Art. 13(1) — design/development/production per Annex I Part I; Annex I Part I (1) — chapeau | CRA-CL14, CRA-CL129 | SO-D-09.2.HL -> SO-CRA-053 -> SO-D-09.2.CRA | PR.PS-06, GV.PO-02 | — | — |

## D-09.3 — Asset Inventories

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 9.3.2 — Manufacturer draws up product-level technical documentation containing at least the general description and the design/development/production/vulnerability-handling-processes architecture description per Annex VII §1-§2 | `SR-CRA-087` | Annex VII §1 — general description; Annex VII §2(a)–(c) — design + vuln handling processes; Annex VII §3 — risk assessment; Annex VII §4 — support-period determination info | CRA-CL160, CRA-CL161, CRA-CL162, CRA-CL163 | SO-D-09.3.HL -> SO-CRA-061 -> SO-D-09.3.CRA | GV.PO-02, ID.AM-02 | — | — |

## D-09.4 — Records of Processing

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 9.4.3 — Manufacturer draws up before placing on market the technical documentation per Annex VII §1-§8 8-item content list, keeps it at MSA disposal for at least 10 years or the support period (whichever longer), and provides the EU declaration + CE marking | `SR-CRA-085` | Art. 13(12) sentence 1 — technical documentation + conformity assessment before placing; Art. 13(12) sentence 2 — EU declaration + CE marking; Art. 28(1) — EU declaration content; Art. 28(2) — declaration format per Annex V/VI; Art. 28(4) — manufacturer responsibility | CRA-CL36, CRA-CL37, CRA-CL113, CRA-CL114, CRA-CL116 | SO-D-09.4.HL -> SO-CRA-055 -> SO-D-09.4.CRA | GV.PO-02, GV.OC-03 | — | — |

## D-10.1 — Continuous Security Monitoring

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 10.1.3 — Product with digital elements records and monitors relevant internal activity (access to or modification of data, services or functions) with a user opt-out mechanism, and enables vulnerability sharing through a single contact address | `SR-CRA-100` | Annex I Part I (2)(l) — recording + monitoring of relevant internal activity; Annex I Part II (6) — contact address for vulnerability reporting | CRA-CL141, CRA-CL148 | SO-D-10.1.HL -> SO-CRA-020 -> SO-D-10.1.CRA | DE.CM-09, DE.CM-01 | — | — |

## D-10.2 — Audit Logging & Traceability

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 10.2.2 — Manufacturer maintains technical documentation + risk-assessment documentation + test reports + SBOM on MSA reasoned request during the support period with effective/regular tests of the product | `SR-CRA-088` | Annex VII §5 — standards applied + alternatives adopted; Annex VII §6 — test reports; Annex VII §7 — EU declaration copy; Annex VII §8 — SBOM on MSA request | CRA-CL164, CRA-CL165, CRA-CL166, CRA-CL167 | SO-D-10.2.HL -> SO-CRA-069 -> SO-D-10.2.CRA | GV.OC-03, ID.RA-04, GV.SC-04 | — | — |

## D-10.3 — Compliance Testing

| Requisito | SR | Artigos | Cláusulas | Baseline goals (HSO -> SO-REG -> Sub-SO) | CSF 2.0 | PF 1.1 | AI RMF |
|---|---|---|---|---|---|---|---|
| 10.3.3 — Manufacturer carries out effective and regular tests of the product, demonstrates conformity via OJ-codified modules (Module A or Module B+C and H), and includes test reports in technical documentation | `SR-CRA-101` | Annex VII §6 — test reports; Annex I Part II (3) — effective and regular tests and reviews | CRA-CL165, CRA-CL145 | SO-D-10.3.HL -> SO-CRA-071 -> SO-D-10.3.CRA | ID.RA-04, GV.OV-01 | — | — |

