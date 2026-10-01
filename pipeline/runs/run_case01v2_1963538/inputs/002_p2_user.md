# Task — PROM-P1-02 (ficha PROM-P1-02 v1.0.0)

You are a regulatory scope analyst. Using the fact sheet, evaluate each of the five candidate regulations against its scope test and produce the §2 verdict table.

Scope tests:
- **GDPR** — applies when the company is established in a jurisdiction covered by the input and processes personal data (establishment + processing).
- **CRA** — applies when the company develops or supplies products with digital elements that are placed on the market; use `develops_software` from the fact sheet. A company that only uses software does not, by that fact alone, place products with digital elements on the market.
- **NIS2** — applies when the company falls in an essential/important entity sector and meets the size threshold; state sector and size explicitly.
- **DORA** — applies to financial entities; check the sector field.
- **AI_Act** — applies when the company places AI systems on the market or deploys high-risk AI systems; an ordinary product without AI functionality does not trigger it.

Rules:
1. Every rationale cites the fact-sheet field(s) it rests on.
2. Every regulation listed in input §5 must appear in the table. If an assumed regulation fails its scope test, verdict = `flagged` with the failing criterion — it is flagged, never silently dropped.
3. Do not derive any obligation here; this step only decides scope (R8).
4. If a scope test cannot be decided from the fact sheet, verdict = `flagged` + `open question`, never a guess.

# Output schema

```
| Regulation | Verdict | Rationale |
|---|---|---|
| GDPR | `**applies**` / `does not apply` / `flagged` | one line, citing fact-sheet fields |
| CRA | … | … |
| NIS2 | … | … |
| DORA | … | … |
| AI_Act | … | … |
```

Wrap your answer: return ONLY one ```markdown fenced block containing the 5-row §2 verdict table (header + 5 rows, nothing else).

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


----- BEGIN FILE: pipeline/cases/Case_01_TinyTask_SaaS/company_input.md §5 -----
## §5 Regulations Assumed

- GDPR — commercial B2B SaaS processing EU personal data (names, emails,
  passwords, task notes); TinyTask acts as controller for customer accounts
  and processor for customer task data.
- CRA — TinyTask develops and places products with digital elements (SaaS +
  web/mobile interface) on the EU market as manufacturer, default product
  class.
- NIS2 — considered and excluded: technology sector but non-critical service,
  8 employees (<50) and <€2M (<€10M), not in Annex I/II essential sectors.
- DORA — considered and excluded: not a financial entity and not an ICT
  provider to financial entities.
- AI_Act — considered and excluded: rule-based task management; zero AI/ML
  systems developed, deployed or integrated.
----- END FILE: pipeline/cases/Case_01_TinyTask_SaaS/company_input.md §5 -----


----- BEGIN FILE: templates/phase1_output.md §2 -----
## §2 Applicable Regulations

| Regulation | Verdict | Rationale |
|---|---|---|
| GDPR | applies / does not apply | <one line> |
| CRA | applies / does not apply | <one line> |
| NIS2 | applies / does not apply | <one line> |
| DORA | applies / does not apply | <one line> |
| AI_Act | applies / does not apply | <one line> |

<!-- Every regulation from input §5 must appear here: applied or flagged
     non-applicable with rationale. Never silently dropped. -->
----- END FILE: templates/phase1_output.md §2 -----
