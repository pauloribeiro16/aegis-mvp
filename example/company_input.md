# Company Input — VetCare Connect, Lda.

<!-- Filled example for the aegis-mvp golden run (fictional company, real corpus). -->

## §1 Company Profile

- Name: VetCare Connect, Lda.
- Sector: veterinary care (chain of 4 clinics)
- Size: 15 employees
- Jurisdiction(s): Portugal
- Legal form: Lda. (private limited company)

## §2 Product / Service

VetCare Connect runs 4 veterinary clinics in the Porto area. Clients book
consultations through a web and mobile appointment app, which also sends
vaccination and check-up reminders. The app was commissioned from and is
operated by an external software house as a hosted service; VetCare does not
develop software itself. Each clinic additionally uses a cloud
practice-management system for consultations and invoices.

## §3 Data Handled

Client (pet owner) personal data: name, contacts, address, payment data, and
appointment/clinical history of the animal linked to the owner — about 12,000
client records in total. The clinical notes concern animals, not people, but
the owner identity, contact and payment data are personal data. Employee
administrative data is not processed in-house (external accountant runs
payroll).

## §4 Systems & Cloud

- Appointment web + mobile app — developed and hosted by the software house
  (SaaS, EU cloud provider); VetCare has an admin console for staff.
- Practice-management SaaS (EU hosting) for consultations and invoicing.
- Card payments via a payment services provider.
- Email/SMS reminders sent through the software house's messaging service.
- Clinic staff access the app admin console with individual logins; the admin
  console currently has no multi-factor authentication.

## §5 Regulations Assumed

- GDPR — VetCare is the controller of ~12,000 data subjects' personal data
  (identity, contact, payment, appointment history).
- CRA — considered and excluded: VetCare commissions and uses the app but does
  not manufacture or place products with digital elements on the market.
- NIS2 — considered and excluded: veterinary care is not an Annex I/II sector
  and the company is far below the size thresholds.
- DORA — considered and excluded: not a financial entity.
- AI_Act — considered and excluded: reminders are rule-based scheduling; no AI
  system is placed on the market or deployed.
