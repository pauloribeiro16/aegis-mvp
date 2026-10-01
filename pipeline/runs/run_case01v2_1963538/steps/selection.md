| Sub-domain | Name | Trigger rationale |
|---|---|---|
| D-01.1 | Data at Rest Encryption | customer PII (names, emails, passwords, task data) stored on managed cloud → GDPR Art. 32 security of processing (encryption at rest) |
| D-01.2 | Data in Transit Encryption | PII transmitted via SaaS web/mobile interface and payment-provider API → GDPR Art. 32 security of processing (encryption in transit) |
| D-02.1 | Vulnerability Identification | TinyTask develops and places SaaS product on EU market as manufacturer → CRA Art. 13(1) vulnerability identification |
| D-02.3 | Coordinated Vulnerability Disclosure | TinyTask places product with digital elements on EU market as manufacturer → CRA Art. 13(1) coordinated vulnerability disclosure |
| D-03.1 | Identity Lifecycle Management | customer accounts with individual logins for business customers and their end-users → GDPR Art. 32 identity lifecycle management |
| D-03.2 | Multi-Factor Authentication | individual login accounts with stored passwords → GDPR Art. 32 authentication strength |
| D-04.1 | Incident Detection & Triage | processing of PII (names, emails, passwords, task data) on managed cloud → GDPR Art. 33 breach detection and triage |
| D-04.3 | Incident Notification & Reporting | personal data breach involving customer PII → GDPR Art. 33(1) 72-hour notification to supervisory authority |
| D-05.1 | Data Minimisation | collection of customer names, emails, passwords, and task data → GDPR Art. 5(1)(c) data minimisation |
| D-05.2 | Retention & Archiving | storage of customer PII and task data on managed cloud → GDPR Art. 5(1)(e) storage limitation |
| D-05.3 | Right to Erasure | customer and end-user PII stored in SaaS → GDPR Art. 17 right to erasure |
| D-05.4 | Data Portability | customer PII (names, emails, task data) held in structured format → GDPR Art. 20 data portability |
| D-06.1 | Vendor Risk Assessment | external payment provider as sub-processor + managed cloud hosting → GDPR Art. 28 processor due diligence |
| D-06.2 | Software Bill of Materials (SBOM) | TinyTask develops SaaS product and places on EU market as manufacturer → CRA Art. 13(1) SBOM |
| D-06.3 | Contractual Security Obligations | external payment provider and managed cloud as processors → GDPR Art. 28(3) contractual security obligations |
| D-07.1 | Secure-by-Design Principles | TinyTask develops SaaS product from scratch → GDPR Art. 25 data protection by design + CRA security by design |
| D-07.2 | Secure Coding Practices | in-house development of SaaS product with digital elements → CRA secure coding practices |
| D-09.1 | Information Security Policies | 8-person SaaS company processing PII → GDPR Art. 32 documented security measures |
| D-09.2 | Impact & Risk Assessments | processing of PII (names, emails, passwords, task data) → GDPR Art. 35 risk assessment |
| D-09.4 | Records of Processing | controller and processor roles for PII → GDPR Art. 30 records of processing activities |
| D-10.1 | Continuous Security Monitoring | SaaS product processing PII on managed cloud → GDPR Art. 32 continuous security monitoring |
| D-10.2 | Audit Logging & Traceability | processing of PII with individual logins → GDPR Art. 32 audit logging and traceability |

Excluded candidates:
D-01.3 — key custody separation is a sub-component of D-01.1/D-01.2; managed cloud provider handles key management; no distinct company fact triggers it independently
D-01.4 — data integrity is implied by D-01.1/D-01.2 encryption controls; no distinct company fact triggers it independently
D-02.2 — patch management is a sub-component of D-02.1 vulnerability identification; no distinct company fact triggers it independently
D-02.4 — "threat-led" and TLPT are disproportionate for 8-person company with self-assessment conformity; basic security testing is covered by D-02.1
D-03.3 — least privilege is a sub-component of D-03.1/D-03.2 identity management; no distinct company fact triggers it independently
D-03.4 — secure defaults are a sub-component of D-07.1 secure by design; no distinct company fact triggers it independently
D-04.2 — incident containment is a sub-component of D-04.1 incident detection; no distinct company fact triggers it independently
D-04.4 — incident recovery is a sub-component of D-04.1 incident detection; no distinct company fact triggers it independently
D-06.4 — third-party boundary management is a sub-component of D-06.1/D-06.3 vendor risk; no distinct company fact triggers it independently
D-07.3 — CI/CD pipeline security is a sub-component of D-07.1/D-07.2 secure development; no distinct company fact triggers it independently
D-07.4 — change management is a sub-component of D-07.1 secure by design; no distinct company fact triggers it independently
D-08.1 — general security awareness is a generic obligation not clearly triggered by a specific company fact
D-08.2 — role-specific competence is a generic obligation not clearly triggered by a specific company fact
D-08.3 — subject matter targets NIS2 essential/important entities and DORA financial entities; neither applies to TinyTask
D-09.3 — asset inventory is a sub-component of D-09.1 security policies; no distinct company fact triggers it independently
D-10.3 — compliance testing is a sub-component of D-02.1/D-07.1; no distinct company fact triggers it independently