```yaml
company: TinyTask Lda.
sector: Technology / Software (B2B SaaS productivity tools)
size_employees: 8
jurisdictions: [Portugal (EU), HQ in Lisbon]
legal_form: Private Limited Company (Lda.)
product_summary: >
  TinyTask develops and operates B2B SaaS productivity tools: a rule-based task
  management platform sold by commercial subscription to clinics. The company
  develops the software itself and places the product, with its web and mobile
  interface, on the EU market as the manufacturer; the product falls in the
  default class with internal-production-control (self-assessment) conformity.
  There are no AI/ML systems developed, deployed or integrated — the platform is
  rule-based.
develops_software: true
data_categories:
  - customer account metadata (names, emails, passwords)
  - clinic task data containing personal data of the clinics' own users
data_subjects:
  - clinic customers (controller role)
  - clinics' own users (processor role, on behalf of clinics under DPAs)
sensitive_data: []
data_scale: not stated in the intake
hosting: managed cloud (hosted SaaS service)
access_model: customer accounts with individual logins
third_party_processing:
  - external payment provider (sub-processor for payment metadata only)
assumed_regulations:
  - GDPR — commercial B2B SaaS processing EU personal data (names, emails, passwords, task notes); TinyTask acts as controller for customer accounts and processor for clinic task data.
  - CRA — TinyTask develops and places products with digital elements (SaaS + web/mobile interface) on the EU market as manufacturer, default product class.
  - NIS2 — considered and excluded: technology sector but non-critical service, 8 employees (<50) and <€2M (<€10M), not in Annex I/II essential sectors.
  - DORA — considered and excluded: not a financial entity and not an ICT provider to financial entities.
  - AI_Act — considered and excluded: rule-based task management; zero AI/ML systems developed, deployed or integrated.
open_questions:
  - data_scale: "Rough scale is not stated in the intake."
```