# Company Input — OmniBank Financial Systems S.A.

## §1 Company Profile

OmniBank Financial Systems S.A. is a société anonyme incorporated in Germany
(Frankfurt-registered, ECB-supervised) operating in the banking and financial
services sector. It has 5,000 employees and approximately €1.5B annual revenue,
making it a LARGE-scale institution. It is a credit institution under CRR
Art. 4(1)(1) and a payment service provider; as a banking-sector entity with more
than 250 employees it is an Essential Entity under NIS 2 (Annex I). It keeps a
dedicated security organisation of about 100 security FTE, a 24/7 Security
Operations Center, and a certified information security management system.

## §2 Product / Service

OmniBank operates four product lines across the EU market: a consumer mobile
banking application (account management, payments, card services), a full-service
web banking platform for retail customers, payment processing services for
retail customers and merchants, and OmniScore — an in-house developed and
in-house operated machine-learning platform producing credit-access decisions on
applicants. For OmniScore the bank acts as both provider and deployer: it
develops the models on its own AI/ML platform and operates them in production
decision flows.

## §3 Data Handled

The bank processes customer identity, contact, account and transaction data at
scale, plus balances and payment histories; credit data including applications,
repayment histories, defaults and the credit scores produced by OmniScore; and
applicant behavioural data feeding those models. It also processes employee data
for its 5,000-strong workforce, acting as controller in the employment context.
**No special-category data under Art. 9 is processed by design.** Retention and
erasure follow statutory financial-records floors; decision records are kept in
token-only form under the longest applicable floor, while direct identifiers are
not retained beyond purpose.

## §4 Systems & Cloud

An on-premise mainframe core banking system anchors the estate, with EU-region
cloud for customer-facing services, a custom AI/ML platform for OmniScore
training and serving, a relational database estate, and HSM-based cryptographic
key custody operated in-house. A signed-release pipeline covers the mobile/web
estate, and the model registry is versioned for OmniScore. Critical ICT systems
include the core banking system, AML screening, payments and OmniScore (DORA
Art. 6 critical functions). Third parties are managed-cloud and market-data
providers, tracked in a maintained register of ICT third-party providers.

## §5 Regulations Assumed

- **GDPR** — controller for customer and applicant data, processor in the
  employer context for the 5,000-person workforce; no Art. 9 data by design.
- **CRA** — manufacturer placing the mobile application and web platform on the
  EU market; Class I/important products handling financial data.
- **NIS2** — banking is an Annex I essential sector and the entity is an
  Essential Entity.
- **DORA** — financial entity per Art. 2(1) as a credit institution and payment
  service provider, with ICT third-party register duties.
- **AI Act** — provider and deployer of OmniScore, a high-risk credit-scoring
  system, carrying conformity-assessment and registration duties.

Known constraints recorded at intake: ECB supervision; statutory
financial-record retention floors that interact with erasure duties; DORA ICT
third-party register duties overlapping processor contracts; and four
incident-notification regimes with distinct clocks (GDPR 72 h; NIS 2 24 h/72 h/1
month; DORA initial/intermediate/final; AI Act serious-incident matrix).
