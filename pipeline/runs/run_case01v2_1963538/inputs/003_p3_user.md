# Task — PROM-P1-03 (ficha PROM-P1-03 v1.0.0)

You are a solution-scope architect. Work only from the candidate set (sub-domains whose module contains a regulation confirmed at G-P1-B).

For each candidate sub-domain:
1. Read its participant rows (which confirmed regulations are present) and the sub-domain's subject matter.
2. Decide: does an obligation of a confirmed regulation match the sub-domain subject matter AND trigger on a company fact? Write the decision as a one-line trigger rationale in "company fact → regulation duty" form (example: "client PII stored on managed cloud → GDPR Art. 32 security of processing").
3. If no company fact triggers it, move the sub-domain to the exclusion list with a why-not line.

Rules:
1. Canonical IDs only, exactly as in `baseline/domains/index.md` — never invent, merge, or reformat (R1).
2. Only confirmed regulations generate triggers (R8).
3. Target 4–10 sub-domains for a small company — use it as a proportionality signal, not as a hard rule; completeness over the candidate set wins.
4. Do not read goal content or requirements yet — selection only.

# Output schema

```
§3 table: `Sub-domain | Name | Trigger rationale` — plus an exclusion list:

```text
Excluded candidates: <D-XX.Y> — <one-line why-not (no company fact triggers it)>
```
```

Wrap your answer: return ONLY one ```markdown fenced block containing (a) the §3 selection table `| Sub-domain | Name | Trigger rationale |` and (b) a line `Excluded candidates:` followed by one line per excluded candidate in the form `<D-XX.Y> — <why-not>`. Nothing else.

# Attached context (verbatim files)


----- BEGIN FILE: steps/fact_sheet.yaml -----
company: TinyTask Lda.
sector: Technology / Software (B2B SaaS productivity tools)
size_employees: 8
jurisdictions: [Portugal (EU)]
legal_form: Private Limited Company (Lda.)
product_summary: >
  TinyTask develops and operates B2B SaaS productivity tools: a rule-based task
  management platform sold by commercial subscription to business customers.
  The company develops the software itself and places the product, with its web
  and mobile interface, on the EU market as the manufacturer; the product falls
  in the default class with internal-production-control (self-assessment)
  conformity. There are no AI/ML systems developed, deployed or integrated —
  the platform is rule-based.
develops_software: true
data_categories:
  - customer account metadata (names, emails, passwords)
  - task data containing personal data of the customers' own users
data_subjects:
  - business customers (controller role)
  - customers' own users (processor role)
sensitive_data: []
data_scale: not stated in the intake
hosting: managed cloud
access_model: customer accounts with individual logins
third_party_processing:
  - external payment provider (sub-processor for payment metadata only)
assumed_regulations:
  - GDPR — commercial B2B SaaS processing EU personal data (names, emails, passwords, task notes); TinyTask acts as controller for customer accounts and processor for customer task data.
  - CRA — TinyTask develops and places products with digital elements (SaaS + web/mobile interface) on the EU market as manufacturer, default product class.
  - NIS2 — considered and excluded: technology sector but non-critical service, 8 employees (<50) and <€2M (<€10M), not in Annex I/II essential sectors.
  - DORA — considered and excluded: not a financial entity and not an ICT provider to financial entities.
  - AI_Act — considered and excluded: rule-based task management; zero AI/ML systems developed, deployed or integrated.
open_questions:
  - data_scale: rough figure not stated in the intake
----- END FILE: steps/fact_sheet.yaml -----


----- BEGIN FILE: steps/verdicts.md -----
| Regulation | Verdict | Rationale |
|---|---|---|
| GDPR | `applies` | Established in Portugal (EU) per `jurisdictions`; processes personal data per `data_categories` (names, emails, passwords, task data with personal data). |
| CRA | `applies` | `develops_software: true`; `product_summary` states TinyTask develops the software and places the product (SaaS + web/mobile interface) on the EU market as manufacturer. |
| NIS2 | `does not apply` | `sector` is Technology/Software (B2B SaaS) — not an Annex I/II essential/important sector; `size_employees: 8` is below the NIS2 size threshold. |
| DORA | `does not apply` | `sector` is Technology/Software (B2B SaaS productivity tools); the company is not a financial entity nor an ICT provider to financial entities. |
| AI_Act | `does not apply` | `product_summary` states "no AI/ML systems developed, deployed or integrated — the platform is rule-based"; no AI system is placed on the market or deployed. |
----- END FILE: steps/verdicts.md -----


----- BEGIN FILE: baseline/domains/index.md -----
# Domains index (modular per-regulation layout)

- Domains: 10
- Sub-domains: 38
- Per-regulation modules: 189
- Ambiguity modules: 185
- Cross pair analyses: 200
- Article copies: 623

> Every sub-domain `D-XX.Y/` contains: `_index.md` (identity), `objective.md`
> (neutral high-level objective), `regs/<REG>.md` + `regs/<REG>.ambiguity.md`
> (independent per-regulation modules), `cross/<R1>-<R2>.md` +
> `cross/_interactions.md` (cross-regulation layer), `articles/` (verbatim
> article copies). Migration audit: [_migration_report.md](_migration_report.md).

| Domain | Sub-domains | Reg modules | Ambiguity | Cross pairs | Article copies |
|---|---|---|---|---|---|
| [D-01_Data-Protection](D-01_Data-Protection/_index.md) | 4 | 20 | 20 | 18 | 66 |
| [D-02_Vulnerability-Management](D-02_Vulnerability-Management/_index.md) | 4 | 20 | 20 | 15 | 57 |
| [D-03_Access-Control](D-03_Access-Control/_index.md) | 4 | 20 | 20 | 19 | 47 |
| [D-04_Incident-Response](D-04_Incident-Response/_index.md) | 4 | 20 | 20 | 28 | 108 |
| [D-05_Data-Lifecycle](D-05_Data-Lifecycle/_index.md) | 4 | 20 | 20 | 7 | 38 |
| [D-06_Supply-Chain](D-06_Supply-Chain/_index.md) | 4 | 19 | 15 | 18 | 55 |
| [D-07_Secure-Development](D-07_Secure-Development/_index.md) | 4 | 20 | 20 | 15 | 38 |
| [D-08_Human-Factors](D-08_Human-Factors/_index.md) | 3 | 15 | 15 | 20 | 34 |
| [D-09_Governance-Documentation](D-09_Governance-Documentation/_index.md) | 4 | 20 | 20 | 33 | 120 |
| [D-10_Monitoring-Audit](D-10_Monitoring-Audit/_index.md) | 3 | 15 | 15 | 27 | 60 |


----- END FILE: baseline/domains/index.md -----


----- BEGIN FILE: pack-p3/candidates.md -----
Deterministic pre-filter result: 38 candidate sub-domains contain at least one confirmed regulation (GDPR, CRA). These are the only candidates you may select from or exclude; everything else is out of scope.

### D-01.1 — Data at Rest Encryption
Confirmed regulations present in the module: GDPR, CRA
Participants (parsed): CRA, DORA, GDPR, NIS 2
Subject matter: Data held at rest in storage is protected against unauthorised access through appropriate technical measures — primarily encryption with appropriate key custody — calibrated to the risks identified in the entity's risk assessment and commensurate with the state of the art.

### D-01.2 — Data in Transit Encryption
Confirmed regulations present in the module: GDPR, CRA
Participants (parsed): CRA, DORA, GDPR
Subject matter: Data in transit — across network paths, inter-service calls, and third-party APIs — is protected against unauthorised disclosure and alteration through cryptographic confidentiality and integrity controls (mutual authentication, encryption, integrity verification).

### D-01.3 — Cryptographic Key Management
Confirmed regulations present in the module: GDPR, CRA
Participants (parsed): CRA, DORA, GDPR
Subject matter: Cryptographic keys and related authentication material are managed with separation of roles such that possession of the key material is not bundled with possession of the operational environment that uses it; the key custodian and the data consumer are distinct roles under distinct technical and organisational control, with the cryptographic key (not the storage medium) as the necessary condition for intelligibility of the protected data.

### D-01.4 — Data Integrity Mechanisms
Confirmed regulations present in the module: GDPR, CRA
Participants (parsed): AI Act, CRA, DORA, GDPR
Subject matter: Data integrity is preserved against unauthorised modification across the data lifecycle — at rest, in transit, and in use — with corruption detected, logged, and reported, and with semantic accuracy maintained as the workflow leg of the personal-data principle.

### D-02.1 — Vulnerability Identification
Confirmed regulations present in the module: GDPR, CRA
Participants (parsed): AI Act, CRA, DORA, GDPR, NIS 2
Subject matter: Vulnerabilities — including, where in scope, AI-system-specific attack surfaces (data poisoning, model poisoning, adversarial examples, model evasion, confidentiality attacks, model flaws) — are identified on a continuing basis across the system, product, ICT asset, or AI system that an entity operates, manufactures, deploys, or processes, with the resulting identification artefact (vulnerability register, risk-scenario catalogue, SBOM, or risk-management file) feeding the entity's testing, remediation, and notification cascades.

### D-02.2 — Patch Management & Updates
Confirmed regulations present in the module: GDPR, CRA
Participants (parsed): CRA, DORA
Subject matter: Vulnerabilities identified in the upstream identification pipeline are addressed and remediated through security updates that are distributed via a secure, separated channel, with the entity-side policy governing patch deployment (severity-classified deployment windows, automated isolation of affected information assets in the event of a cyber-attack) forming a layered patch-management workflow on the asset.

### D-02.3 — Coordinated Vulnerability Disclosure
Confirmed regulations present in the module: GDPR, CRA
Participants (parsed): CRA, NIS 2
Subject matter: A coordinated vulnerability disclosure (CVD) ecosystem is maintained, covering the manufacturer-side CVD policy (intake, triage, publication, post-disclosure verification), a publicly identifiable contact address for vulnerability reporting, and — when the manufacturer also operates as a NIS 2 essential entity in a Member State — the institutional CSIRT-coordinated pathway under Art. 12(1) that integrates the manufacturer-side CVD with the Member-State-level disclosure coordination.

### D-02.4 — Threat-Led Penetration Testing
Confirmed regulations present in the module: GDPR, CRA
Participants (parsed): AI Act, CRA, DORA
Subject matter: The security of the asset — product with digital elements, ICT-supported business functions / information assets / ICT assets, or high-risk AI system — is tested on a continuing basis, with a layered testing architecture combining conventional product-security testing, ICT defensive-capability testing (portfolio of testing modalities with periodic advanced TLPT), and AI-specific risk-management-measure testing plus real-world conditions.

### D-03.1 — Identity Lifecycle Management
Confirmed regulations present in the module: GDPR, CRA
Participants (parsed): CRA, DORA, GDPR, NIS 2
Subject matter: Identities of principals that interact with the entity's systems, products, services, components and data are managed in a verifiable, lifecycle-aware manner with documented boundaries between identity types and explicit hand-off protocols at boundary surfaces.

### D-03.2 — Multi-Factor Authentication
Confirmed regulations present in the module: GDPR, CRA
Participants (parsed): CRA, DORA, GDPR, NIS 2
Subject matter: Authentication of users, services, and hardware that interact with the entity's systems, products, services, components and data operates through an authentication mechanism of sufficient strength for the risk in scope, with the strictest applicable floor discharging the most permissive on the same authentication event when both apply.

### D-03.3 — Authorisation & Least Privilege
Confirmed regulations present in the module: GDPR, CRA
Participants (parsed): CRA, DORA, GDPR, NIS 2
Subject matter: The entitlement to perform actions on the entity's systems, products, services, components, and data is managed per least privilege with explicit authorisation-model choice, documented entitlements, attack-surface-limitation evidence, and boundary hand-offs between access surfaces.

### D-03.4 — Secure System Defaults
Confirmed regulations present in the module: GDPR, CRA
Participants (parsed): CRA, GDPR
Subject matter: The default disposition of the entity's data-centric processing systems and the product's product-centric configuration is managed so that the baseline state of every processing system and every product configuration is the minimum-necessary / secure configuration, with relaxation requiring affirmative data-subject or user intervention.

### D-04.1 — Incident Detection & Triage
Confirmed regulations present in the module: GDPR, CRA
Participants (parsed): CRA, DORA, GDPR, NIS 2
Subject matter: Security-relevant events affecting the entity's systems, products, services, components and data are detected and triaged with documented trigger moments that anchor the downstream notification and response pipelines.

### D-04.2 — Incident Containment & Response
Confirmed regulations present in the module: GDPR, CRA
Participants (parsed): CRA, DORA, GDPR, NIS 2
Subject matter: Security incidents affecting the entity's systems, products, services, components and data are contained and mitigated through appropriate measures that address the incident's impact and reduce the probability of further damage.

### D-04.3 — Incident Notification & Reporting
Confirmed regulations present in the module: GDPR, CRA
Participants (parsed): AI Act, CRA, DORA, GDPR, NIS 2
Subject matter: A major security incident is notified to the applicable recipients within the regulatory timelines applicable to the event's material scope.

### D-04.4 — Incident Recovery & Lessons Learned
Confirmed regulations present in the module: GDPR, CRA
Participants (parsed): CRA, DORA, GDPR, NIS 2
Subject matter: Systems, products, services, components and data are restored and recovered with documented recovery evidence applicable to the recovery dimensions of all four participating regulators on the same party.

### D-05.1 — Data Minimisation
Confirmed regulations present in the module: GDPR, CRA
Participants (parsed): AI Act, CRA, GDPR
Subject matter: Data collected or otherwise acquired is limited to what is adequate, relevant, and necessary in relation to the purpose for which it is processed, with a documented necessity assessment and, where the underlying purpose changes, a compatibility assessment confirming that the new use is consistent with the original. Special-category data is processed only where a narrow exception applies and is documented to that effect.

### D-05.2 — Retention & Archiving
Confirmed regulations present in the module: GDPR, CRA
Participants (parsed): AI Act, CRA, GDPR
Subject matter: Data — across the data classes in scope — is retained for the period required to satisfy its declared purpose, with documented retention rationale and, where the underlying purpose changes, a reset of the retention clock. Long-term archiving or research-only retention is paired with safeguards proportional to the residual identifiability.

### D-05.3 — Right to Erasure
Confirmed regulations present in the module: GDPR, CRA
Participants (parsed): CRA, GDPR
Subject matter: Data held about a person is rendered inaccessible to the controller on the data subject's election, and data held by a product with digital elements is rendered inaccessible to the manufacturer on the user's election, by whichever mechanism — the controller-side policy execution or the manufacturer-side product affordance — applies to the data object. Erasure is performed without undue delay and is documented to demonstrate compliance; where a processor is involved, the processor-side mirror ensures deletion-or-return at contract end.

### D-05.4 — Data Portability
Confirmed regulations present in the module: GDPR, CRA
Participants (parsed): GDPR
Subject matter: Personal data are exported to the data subject in a structured, commonly used, machine-readable format, and the data subject can transmit those data to another controller without hindrance, subject to the qualifying conditions and exclusions that scope the right.

### D-06.1 — Vendor Risk Assessment
Confirmed regulations present in the module: GDPR, CRA
Participants (parsed): CRA, DORA, GDPR, NIS 2
Subject matter: Vendors, suppliers, components, and ICT service providers undergo risk-anchored due diligence with proportionality documentation and ongoing monitoring before entry to the supply chain.

### D-06.2 — Software Bill of Materials (SBOM)
Confirmed regulations present in the module: GDPR, CRA
Participants (parsed): CRA
Subject matter: The manufacturer draws up and maintains a software bill of materials (SBOM) covering the components and dependencies contained in the product with digital elements, in a commonly used and machine-readable format that supports automated downstream consumption, with at minimum the top-level dependencies.

### D-06.3 — Contractual Security Obligations
Confirmed regulations present in the module: GDPR, CRA
Participants (parsed): CRA, DORA, GDPR, NIS 2
Subject matter: Third-party security obligations are made enforceable through contracts, transfer safeguards, written mandates, or market-access duties, as appropriate to the regulatory perspective and the actor involved.

### D-06.4 — Third-Party Boundary Management
Confirmed regulations present in the module: GDPR, CRA
Participants (parsed): CRA, DORA, GDPR, NIS 2
Subject matter: Third-party boundary responsibilities are explicitly allocated so that non-EU representatives, direct-supplier scope, cross-border routing, substantial-modification accountability, economic-operator identification, and audit/access rights remain traceable to the correct actor and recipient.

### D-07.1 — Secure-by-Design Principles
Confirmed regulations present in the module: GDPR, CRA
Participants (parsed): AI Act, CRA, DORA, GDPR, NIS 2
Subject matter: Security is integrated into the acquisition, design, development, production, deployment and maintenance of systems and products via documented by-design decisions, risk-assessment propagation, proportionate safeguards, and lifecycle consistency.

### D-07.2 — Secure Coding Practices
Confirmed regulations present in the module: GDPR, CRA
Participants (parsed): AI Act, CRA, DORA
Subject matter: Coding practices deliver attack-surface limitation, exploitation mitigation, and AI-system attack-defence under an appropriate coding-practice evidence base.

### D-07.3 — CI/CD Pipeline Security
Confirmed regulations present in the module: GDPR, CRA
Participants (parsed): CRA, NIS 2
Subject matter: CI/CD pipeline security delivers build-time control baselines (signed artefacts, build-agent integrity, ephemeral build environments) and update-distribution delivery-path security.

### D-07.4 — Change Management
Confirmed regulations present in the module: GDPR, CRA
Participants (parsed): CRA, DORA
Subject matter: Change management delivers documented change-management procedures (manufacturer-side series-production conformity + entity-side change-management six-step), risk-assessment-approach, controlled-manner, and substantial-modification assessment with manufacturer-equivalent status consequences where applicable.

### D-08.1 — General Security Awareness
Confirmed regulations present in the module: GDPR, CRA
Participants (parsed): AI Act, CRA, DORA, GDPR, NIS 2
Subject matter: General security awareness is established through a documented training programme with population-wide coverage, audience-routing, and governance hooks.

### D-08.2 — Role-Specific Competence
Confirmed regulations present in the module: GDPR, CRA
Participants (parsed): AI Act, CRA, DORA, GDPR, NIS 2
Subject matter: Role-specific competence is established through a function-specific depth, audience-routing, competence-criteria-anchored training, and governance hooks architecture.

### D-08.3 — Management Board Training
Confirmed regulations present in the module: GDPR, CRA
Participants (parsed): AI Act, DORA, NIS 2
Subject matter: Management bodies of essential and important entities (NIS 2) and financial entities (DORA) maintain an executive-literacy substrate with documented training records, governance competence, and personal-capacity threshold for approve+oversee+liable governance duties through a management-body training programme.

### D-09.1 — Information Security Policies
Confirmed regulations present in the module: GDPR, CRA
Participants (parsed): AI Act, CRA, DORA, GDPR, NIS 2
Subject matter: Information security policies are established through a **documented policy architecture** with **governance hooks** and an **accountability chain** that anchor the entity's cybersecurity posture.

### D-09.2 — Impact & Risk Assessments
Confirmed regulations present in the module: GDPR, CRA
Participants (parsed): AI Act, CRA, DORA, GDPR, NIS 2
Subject matter: Impact and risk assessments are established through a **documented assessment** of identified risks and mitigation measures, with a **review cadence** calibrated to the lifecycle phase of the assessment object.

### D-09.3 — Asset Inventories
Confirmed regulations present in the module: GDPR, CRA
Participants (parsed): AI Act, CRA, DORA, GDPR, NIS 2
Subject matter: Asset inventories are established through a **documented entity-level asset inventory** with **identification + classification + documentation** of ICT supported business functions, information assets, ICT assets, and their roles and dependencies.

### D-09.4 — Records of Processing
Confirmed regulations present in the module: GDPR, CRA
Participants (parsed): AI Act, CRA, DORA, GDPR, NIS 2
Subject matter: Records of processing activities are established through **parallel documentation regimes** that produce records of processing activities, technical documentation, certification records, information security policy documentation, and quality management system documentation serving distinct audit purposes.

### D-10.1 — Continuous Security Monitoring
Confirmed regulations present in the module: GDPR, CRA
Participants (parsed): AI Act, CRA, DORA, GDPR, NIS 2
Subject matter: Continuous security monitoring is established through a **layered detection-and-monitoring architecture** spanning personal-data processing systems, network and information systems, on-device product activity, ICT systems and tools, and high-risk AI systems, with detection capability feeding the incident-response chain.

### D-10.2 — Audit Logging & Traceability
Confirmed regulations present in the module: GDPR, CRA
Participants (parsed): AI Act, CRA, DORA, GDPR, NIS 2
Subject matter: Audit logging and traceability are established through a **layered audit-records architecture** spanning compliance records with integrity and traceability, product-level technical documentation traceability, entity-level information security policy documentation, and AI-system event logging with retention floors.

### D-10.3 — Compliance Testing
Confirmed regulations present in the module: GDPR, CRA
Participants (parsed): AI Act, CRA, DORA, GDPR, NIS 2
Subject matter: Compliance testing is established through a **5-parallel-testing-programme architecture** spanning effectiveness-evaluation of security measures, effectiveness-assessment of risk-management measures, product-level conformity-assessment, entity-level digital operational resilience testing with TLPT, and AI-system-level testing for risk management with real-world-conditions and accuracy/robustness/cybersecurity baseline testing.
----- END FILE: pack-p3/candidates.md -----
