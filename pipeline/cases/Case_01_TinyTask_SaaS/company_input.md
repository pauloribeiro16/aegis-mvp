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
