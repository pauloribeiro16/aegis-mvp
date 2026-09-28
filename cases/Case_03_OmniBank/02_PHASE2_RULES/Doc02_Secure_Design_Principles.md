---
document_id: AEGIS-P2-DOC02
title: Secure Design & Systems Engineering Principles (Case 02 — OmniBank Financial Systems)
phase: 2
version: 1.0
date: 2026-09-23
case: Case_02_SecureBorder_Solutions
tier: MEDIUM
status: APPROVED
categories: [Architectural Modeling, Core Security, Requirements Engineering, Privacy by Design]
total_principles: 7
realization_class: TECHNOLOGY
---

# Secure Design & Systems Engineering Principles — Case 02 (OmniBank Financial Systems)

> **Document Purpose:** Establishes the 7 foundational, technology-agnostic engineering principles that govern architectural diagramming, data flow modeling, requirements engineering, and privacy by design for OmniBank Financial Systems. While `Doc01` structures the regulatory obligations across the 35 active sub-domains, `Doc02` defines the universal engineering code of practice that constrains the solution space before specific technologies and use cases are chosen in Phase 3. Every principle in this document corresponds 1:1 to an autonomous multi-agent verification skill in `baseline/skills/`.

---

## §1 Architectural Role of Principles in AEGIS

### 1.1 Dual-Spine Architecture: Regulatory vs Engineering
AEGIS Phase 2 separates the problem space into two complementary, non-overlapping pillars:
1. **The Regulatory Spine (`Doc01_Operational_Objectives.md`):** Balizes European regulations (GDPR, CRA, NIS 2, AI Act) across canonical sub-domains (`D-01` to `D-10`), formulating what the law proportionally requires as verifiable Operational Objectives (`PO-` and `SO-`).
2. **The Engineering Spine (`Doc02_Secure_Design_Principles.md`):** Establishes 7 universal, technology-agnostic engineering principles (Saltzer & Schroeder, Shostack, ISO 29148, Cavoukian). These principles are transversal to all domains and dictate how software must be modeled, diagrammed, and specified.

### 1.2 Technology Neutrality & The Boundary with Phase 3
In accordance with ISO/IEC/IEEE 29148:2018 (clause 5.2.4), these principles specify **verifiable architectural constraints** (*what* boundaries, invariants, and failure modes must be respected) without prematurely prescribing *how* (concrete database engines, web frameworks, protocol implementations, or software libraries). Specific technologies and use-case allocations (`UC-*`) are strictly introduced in Phase 3.

---

## §2 Principles Category 1 — Architectural & Data Flow Modeling

> **Governing Domain:** System Architecture, Data Flow Diagrams (DFD), Component Topology, and Network Boundaries.  
> **Foundational Literature:** Adam Shostack (2014, *Threat Modeling: Designing for Security*); Jerome Saltzer & Michael Schroeder (1975).

| Principle ID | Principle Name | Academic Source | Architectural Definition | Diagrammatic & Modeling Constraint | Verification Method & Lead |
|---|---|---|---|---|---|
| `PRIN-ENG-01` | **Explicit Trust Boundaries & Complete Mediation** | Shostack (2014) / Saltzer & Schroeder (1975) | Every interface separating zones of differing privilege must be visually demarcated, and every crossing flow must be authenticated and validated with zero unmediated bypasses. | Diagrams must explicitly draw dashed trust boundaries separating Traveller-Facing Edge (eGate), Government Integration, Cloud Back-Office, and Administration tiers. No external actor — including airport-site networks — may directly address internal data stores; government authority and airport operator boundaries are first-class trust boundaries. | `INSPECT`: Verification that all cross-zone flows terminate at an authenticating gateway. (Lead Developer) |
| `PRIN-ENG-02` | **Attack Surface Minimization & Peripheral Resilience** | Howard & LeBlanc (2003) / Schneier (2000) | Accessible entry points, communication channels, and active interfaces must be reduced to the minimum necessary, and auxiliary ingress hooks must match core security intensity. | Deployment diagrams must depict zero unmediated service ports or diagnostic consoles on field-deployed eGate units. Per-airport physical isolation boundaries, update-ingest channels, and monitoring feeds must enforce equal security rigor as primary operational interfaces. | `ANALYZE`: Audit of exposed interfaces and auxiliary listeners confirming zero unauthenticated public routes across all deployments. (CISO + Lead Developer) |

---

## §3 Principles Category 2 — Core Systems & Access Security

> **Governing Domain:** System-wide access control, failure state handling, and resource isolation.  
> **Foundational Literature:** Jerome Saltzer & Michael Schroeder (1975, *The Protection of Information in Computer Systems*); OWASP.

| Principle ID | Principle Name | Academic Source | Security Definition | Architectural & Operational Constraint | Verification Method & Lead |
|---|---|---|---|---|---|
| `PRIN-ENG-03` | **Least Privilege & Mechanism Isolation** | Saltzer & Schroeder (1975) | Every principal (user, service, background worker) must operate with the minimum privileges necessary, and distinct tenants or sensitivity levels must not share unisolated execution mechanisms. | Access grants must be action-scoped (no wildcards or superuser roles in runtime services); edge workloads must execute with minimal privilege; per-airport deployments and per-authority data must be isolated by deployment boundary and cryptographic separation. | `TEST`: Automated assertion that runtime identities cannot execute unauthorized privileged actions or cross-deployment access. (CISO + Lead Developer) |
| `PRIN-ENG-04` | **Fail-Safe Defaults & Closed Failure States** | Saltzer & Schroeder (1975) / OWASP | Access decisions and state transitions must default to refusal, and unexpected failures or exceptions must terminate in a secure closed state without state corruption or data leakage. | Gate-control decisions must fail toward the manual lane (officer referral), never toward unverified passage; authentication evaluators must default to denial; exceptions must emit opaque error responses; decision-state mutations must execute within atomic rollback boundaries. | `TEST`: Fault injection verifying that authorization outages and unhandled errors fail closed toward the manual lane. (Lead Developer) |

---

## §4 Principles Category 3 — Requirements Engineering & Verifiability

> **Governing Domain:** Specification of system behaviors, verification criteria, and lifecycle traceability.  
> **Foundational Literature:** ISO/IEC/IEEE 29148:2018; INCOSE Guide to Writing Requirements; EARS (Mavin et al., 2009).

| Principle ID | Principle Name | Academic Source | Requirements Engineering Definition | Specification Constraint | Verification Method & Lead |
|---|---|---|---|---|---|
| `PRIN-ENG-05` | **Requirement Verifiability & Atomicity** | ISO/IEC/IEEE 29148:2018 / EARS (2009) | Every security and privacy requirement must be atomic (one single condition and response) and possess a deterministic, automated pass/fail verification method. | Requirements must conform to EARS syntax patterns (*When... SHALL*); subjective adjectives ('appropriate', 'fast', 'secure') are prohibited unless bound to quantified numerical thresholds. | `INSPECT`: Validation that 100% of requirements map to an empirical test or automated linter rule. (Compliance Analyst) |

---

## §5 Principles Category 4 — Privacy by Design & Data Lifecycle

> **Governing Domain:** Personal data lifecycle, data-subject sovereignty, and purpose-bound processing.  
> **Foundational Literature:** Ann Cavoukian (2009, *Privacy by Design: 7 Foundational Principles*); GDPR Art. 5, 17, 25; ISO/IEC 27701:2019.

| Principle ID | Principle Name | Academic Source | Privacy Engineering Definition | Operational & Diagrammatic Constraint | Verification Method & Lead |
|---|---|---|---|---|---|
| `PRIN-ENG-06` | **Proactive Data Minimization & Scoped Projection** | Cavoukian (2009) / GDPR Art. 5(1)(c) | Only data strictly indispensable for fulfilling the declared service purpose may be collected, transmitted, or retained, and egress models must project strictly scoped data views. | Ingest schemas must reject undeclared fields; raw biometric captures must be discarded immediately after template extraction; monitoring and diagnostic channels must strip or tokenize personal identifiers; cross-authority data flows must project decision-scoped views only. | `INSPECT`: Data dictionary and interface-schema audit proving zero collection or exposure of unjustified personal fields. (DPO + Lead Developer) |
| `PRIN-ENG-07` | **End-to-End Lifecycle Security & Irreversible Erasure** | Cavoukian (2009) / GDPR Art. 17 | Protection covers the entire data lifecycle; data subject to erasure must be permanently destroyed across edge caches, primary stores, archives, and disaster-recovery copies. | Traveller-data erasure must cascade across on-device caches, cloud stores, and recovery copies through irreversible de-linking; token-only decision records remain retainable under the longest applicable regulatory floor without preserving biometric material; recovery restores must replay erasure state. | `TEST`: End-to-end integration test verifying that an erasure request purges biometric material across all storage layers while preserving lawful token-only records. (Lead Developer + DPO) |

---

## §6 Operationalization via Specialized Agentic Skills (1:1 Symmetry)

To translate these 7 transversal principles into continuous, automated engineering governance during Phase 3 and delivery pipelines, AEGIS specifies a dedicated skill layer stored in `baseline/skills/`. Each skill adheres to the Anthropic Skill Standard (rich, self-contained `SKILL.md` orchestrator with heuristics, anti-patterns, case studies, and checklists in `references/`), enabling autonomous sub-agents to evaluate diagrams and specifications against individual principles with zero ambiguity:

| Principle ID | Principle Name | Specialized Autonomous Skill | Path in Repository | Primary Evaluation Scope |
|---|---|---|---|---|
| `PRIN-ENG-01` | Explicit Trust Boundaries & Complete Mediation | `trust-boundary-analysis` | [`baseline/skills/trust-boundary-analysis/`](file:///c:/Users/paulo.ribeiro/OneDrive%20-%20Instituto%20CCG%20ZGDV/Ambiente%20de%20Trabalho/Projetos_PhD/aegis-mvp/baseline/skills/trust-boundary-analysis/) | Architectural DFDs, inter-service tokens, multi-authority database scoping, per-airport isolation |
| `PRIN-ENG-02` | Attack Surface Minimization & Peripheral Resilience | `attack-surface-analysis` | [`baseline/skills/attack-surface-analysis/`](file:///c:/Users/paulo.ribeiro/OneDrive%20-%20Instituto%20CCG%20ZGDV/Ambiente%20de%20Trabalho/Projetos_PhD/aegis-mvp/baseline/skills/attack-surface-analysis/) | Field-unit interfaces, update-ingest routes, diagnostic endpoints, monitoring-feed authentication |
| `PRIN-ENG-03` | Least Privilege & Mechanism Isolation | `least-privilege-analysis` | [`baseline/skills/least-privilege-analysis/`](file:///c:/Users/paulo.ribeiro/OneDrive%20-%20Instituto%20CCG%20ZGDV/Ambiente%20de%20Trabalho/Projetos_PhD/aegis-mvp/baseline/skills/least-privilege-analysis/) | Service identity policies, edge workload privilege, scoped data roles, per-deployment key context |
| `PRIN-ENG-04` | Fail-Safe Defaults & Closed Failure States | `fail-safe-defaults-analysis` | [`baseline/skills/fail-safe-defaults-analysis/`](file:///c:/Users/paulo.ribeiro/OneDrive%20-%20Instituto%20CCG%20ZGDV/Ambiente%20de%20Trabalho/Projetos_PhD/aegis-mvp/baseline/skills/fail-safe-defaults-analysis/) | Manual-lane failover, fail-closed authentication timeouts, sanitized errors, atomic decision state |
| `PRIN-ENG-05` | Requirement Verifiability & Atomicity | `verifiability-analysis` | [`baseline/skills/verifiability-analysis/`](file:///c:/Users/paulo.ribeiro/OneDrive%20-%20Instituto%20CCG%20ZGDV/Ambiente%20de%20Trabalho/Projetos_PhD/aegis-mvp/baseline/skills/verifiability-analysis/) | EARS requirement syntax, quantified metrics, deterministic test bindings |
| `PRIN-ENG-06` | Proactive Data Minimization & Scoped Projection | `data-minimization-analysis` | [`baseline/skills/data-minimization-analysis/`](file:///c:/Users/paulo.ribeiro/OneDrive%20-%20Instituto%20CCG%20ZGDV/Ambiente%20de%20Trabalho/Projetos_PhD/aegis-mvp/baseline/skills/data-minimization-analysis/) | Inbound schema strictness, raw-capture discard discipline, telemetry identifier tokenization |
| `PRIN-ENG-07` | End-to-End Lifecycle Security & Irreversible Erasure | `lifecycle-erasure-analysis` | [`baseline/skills/lifecycle-erasure-analysis/`](file:///c:/Users/paulo.ribeiro/OneDrive%20-%20Instituto%20CCG%20ZGDV/Ambiente%20de%20Trabalho/Projetos_PhD/aegis-mvp/baseline/skills/lifecycle-erasure-analysis/) | GDPR Art. 17 right to erasure, edge-to-cloud cascades, recovery replay of erasure state |
