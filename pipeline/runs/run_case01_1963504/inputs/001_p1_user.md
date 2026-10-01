# Task — PROM-P1-01 (ficha PROM-P1-01 v1.0.0)

You are a compliance requirements analyst. Read `input/<company>/company_input.md` — sections §1 Company Profile, §2 Product/Service, §3 Data Handled, §4 Operational & Service Model — and produce the fact sheet exactly in the schema above.

Rules:
1. Extract only what the text states. Do not infer, complete, or interpret (rule R6).
2. `develops_software` must be answered strictly from §2's statement of whether the company develops or only uses software; if §2 does not say, write `unclear` and add it to `open_questions`.
3. Copy §5 Regulations Assumed verbatim into `assumed_regulations` — list them, do not judge them (judging happens in the next step).
4. If any of §1–§4 is empty or unusable, STOP and report which section is empty — the input contract requires the executor to stop (SPEC §4). Do not fill gaps.
5. Every value that is not literally in the input becomes an `open_questions` entry, never a guess.

# Output schema

```
```yaml
company: <name>
sector: <text>
size_employees: <N>
jurisdictions: [<list>]
legal_form: <text>
product_summary: <2-5 sentences, verbatim-faithful>
develops_software: <true|false|unclear>   # decides CRA scope later
data_categories: [<list>]
data_subjects: [<list>]
sensitive_data: [<list>]                   # health, payment, minors...
data_scale: <rough figure as stated>
hosting: <in-house | managed cloud | mixed, as stated>
access_model: <as stated>
third_party_processing: [<list>]
assumed_regulations: [<REG, justification as written in §5>]
open_questions: [<field, what is missing>]
```
```

Wrap your answer: return ONLY one ```yaml fenced block with the fact sheet.

# Attached context (verbatim files)


----- BEGIN FILE: pipeline/cases/Case_01_TinyTask_SaaS/company_input.md -----
# Company Input — TinyTask Lda.

<!-- Derived from cases/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT/Doc01_INTAKE_FORM.md
     (v2.1) to satisfy the SPEC §4 five-section input contract. Every fact below
     traces to Doc01 §2 (Layer 0), §3 (Layer 1) or §4 (Layer 2); nothing added. -->

## §1 Company Profile

- Name: TinyTask Lda.
- Sector: Technology / Software (B2B SaaS productivity tools)
- Size: 8 employees (EU classification: micro-enterprise; revenue <€2M)
- Jurisdiction(s): Portugal (EU), HQ in Lisbon
- Legal form: Private Limited Company (Lda.)

## §2 Product / Service

TinyTask develops and operates B2B SaaS productivity tools: a rule-based task
management platform sold by commercial subscription to clinics. The company
develops the software itself and places the product, with its web and mobile
interface, on the EU market as the manufacturer; the product falls in the
default class with internal-production-control (self-assessment) conformity.
There are no AI/ML systems developed, deployed or integrated — the platform is
rule-based.

## §3 Data Handled

EU personal data processed in two roles. As controller: customer account
metadata (names, emails, passwords). As processor, on behalf of clinics under
standard Data Processing Agreements: clinic task data containing personal data
of the clinics' own users. No health, payment-card or minors' data is stated as
processed in-house; payments are handled by an external payment provider.
Rough scale is not stated in the intake.

## §4 Operational & Service Model

The platform is operated as a hosted SaaS service for clinic customers. Access
follows the product's own account model (customer accounts with individual
logins). Third-party processing flows: an external payment provider processes
payments (sub-processor for payment metadata only, per the intake's
interpretation). Third-party software dependencies are not yet tracked in a
formal SBOM; supplier security evaluations are conducted ad-hoc with reliance
on standard supplier contracts/DPAs; vulnerability remediation is a manual
review triggered during routine updates or security advisories. Mandatory DPO
appointment is not triggered (small-scale processing; core activity does not
require regular and systematic large-scale monitoring).

## §5 Regulations Assumed

- GDPR — commercial B2B SaaS processing EU personal data (names, emails,
  passwords, task notes); TinyTask acts as controller for customer accounts
  and processor for clinic task data.
- CRA — TinyTask develops and places products with digital elements (SaaS +
  web/mobile interface) on the EU market as manufacturer, default product
  class.
- NIS2 — considered and excluded: technology sector but non-critical service,
  8 employees (<50) and <€2M (<€10M), not in Annex I/II essential sectors.
- DORA — considered and excluded: not a financial entity and not an ICT
  provider to financial entities.
- AI_Act — considered and excluded: rule-based task management; zero AI/ML
  systems developed, deployed or integrated.

----- END FILE: pipeline/cases/Case_01_TinyTask_SaaS/company_input.md -----


----- BEGIN FILE: templates/company_input.md -----
# Company Input — <Company Name>

<!--
  aegis-mvp input template (Increment 0)
  ─────────────────────────────────────
  HOW TO FILL
  · Replace every <...> placeholder. Plain prose, 2-10 lines per section.
  · Brevity is a feature: this is NOT a questionnaire.
  · §5 must list at least one regulation, each with a one-line justification.
  · Do not leave sections empty — the executor will stop (SPEC.md rule R6).
  · Any language is accepted; the output will be in English.

  REGULATION IDENTIFIERS: GDPR | CRA | NIS2 | DORA | AI_Act
-->

## §1 Company Profile

- Name: <company name>
- Sector: <sector/activity>
- Size: <N> employees
- Jurisdiction(s): <countries where it operates>
- Legal form: <e.g. Lda. / Ltd / BV>

## §2 Product / Service

<What the company sells or operates, in 2-5 sentences. Include whether the
company *develops* software/products or only *uses* them — this decides CRA
applicability.>

## §3 Data Handled

<Categories of personal or otherwise regulated data; whose data (customers,
employees, patients...); anything specially sensitive (health, payment,
minors); rough scale.>

## §4 Operational & Service Model

<Operational context: whether services are hosted in-house or via managed cloud;
high-level access/authentication pattern (e.g. centralized access control, role-based);
main third-party data processing flows (e.g. external payment handling, outsourced messaging).
Note: Specify functional roles and operational model; specific vendor products or software tools
are not required and will be addressed in Phase 2. 5-10 lines.>

## §5 Regulations Assumed

<List the regulations the company (or its advisor) believes apply, each with
one line of why. Example:
- GDPR — processes client personal data (contacts, appointment history).
>

----- END FILE: templates/company_input.md -----
