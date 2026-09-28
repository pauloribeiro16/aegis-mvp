# Doc01 — Intake Form: OmniBank Financial Systems S.A.

> **Case Study:** Case 03 — OmniBank Financial Systems (Consumer Banking with In-House High-Risk Credit-Scoring AI)  
> **Lifecycle Phase:** AEGIS Phase 1 — Contextual Definition  
> **Source:** company-provided intake (5 sections, plain prose). Every Phase 1 fact traces here (R6).

---

## 1. Company Profile

OmniBank Financial Systems S.A. is a Société Anonyme incorporated in Germany (Frankfurt-registered, ECB-supervised), operating in the banking & financial services sector with 5,000 employees and approximately €1.5B annual revenue — a LARGE-scale institution with a dedicated security organization of ~100 security FTE, a 24/7 Security Operations Center, and a certified information security management system. The bank is a credit institution under CRR Art. 4(1)(1) and a payment service provider; as a banking-sector entity with more than 250 employees it is an Essential Entity under NIS 2 (Annex I). It maintains in-house HSM-based cryptographic key custody and per-business-line isolation of its core platforms.

## 2. Products and Services

- **Consumer mobile banking application** (EU market) — account management, payments, card services.
- **Web banking platform** (EU market) — full-service online banking for retail customers.
- **OmniScore AI credit-scoring platform** — an in-house developed and in-house operated machine-learning platform producing credit-access decisions on applicants (AI Act Annex III §5(b): access to credit). OmniBank acts as **provider and deployer** of this high-risk AI system: it develops the models on its custom AI/ML platform and operates them in production decision flows.
- Payment processing services (PSP) for retail customers and merchants.

## 3. Data Handled

- **Customer personal data:** identity data, contact data, account and transaction data (financial transactions at scale), balances and payment histories.
- **Credit data:** credit applications, repayment histories, defaults, and **credit scores** produced by OmniScore; applicant behavioral data feeding the models.
- **Employee data:** HR records of the 5,000-strong workforce (controller in the employment context).
- **No special-category data** under Art. 9 is processed by design.
- Retention and erasure follow statutory financial-records floors; decision records are retained in token-only form under the longest applicable floor while biometric-like direct identifiers are not retained beyond purpose.

## 4. Infrastructure and Technology Context

- On-premise mainframe core banking system; EU-region cloud for customer-facing services; custom AI/ML platform (training and serving of OmniScore); relational database estate; HSM-based key custody operated in-house; signed-release pipeline for the mobile/web estate and model registry with versioning for OmniScore. Critical ICT systems include the core banking system (CBS), AML screening, payments, and OmniScore (DORA Art. 6 critical/important functions). Third parties include managed cloud and market data providers; a register of ICT third-party providers is maintained.

## 5. Assumed Regulations and Known Constraints

The bank self-assesses as subject to **GDPR** (controller; processor for employer data), **CRA** (manufacturer placing the mobile app and web platform on the EU market — Class I/important product handling financial data), **NIS 2** (Essential Entity, banking), **DORA** (financial entity per Art. 2(1) — credit institution and PSP), and the **AI Act** (provider and deployer of the high-risk OmniScore credit-scoring system). Known constraints: ECB supervision; statutory financial-record retention floors that interact with erasure duties; DORA ICT third-party register duties overlapping processor contracts; the AI Act conformity and registration duties for OmniScore; four incident-notification regimes with distinct clocks (GDPR 72 h, NIS 2 24 h/72 h/1 month, DORA initial/intermediate/final, AI Act serious-incident matrix).

---

*Prepared from the company context records of the methodology case library; technology mentions are company facts from this intake (R6) and do not enter downstream technology-neutral deliverables (R5).*
