# D-06.4 — DORA module

> Regulation-specific layer: applies when `DORA` is in scope
> (activation: `if DORA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| DORA | SO-DORA-012 (partial) | Financial entities and competent authorities have unrestricted access, inspection, and audit rights over critical ICT third-party providers, with narrowly bounded alternative assurance where other clients' rights are affected | Financial-entity audit-rights boundary over CIF-supporting ICT providers |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **DORA** | CIF-supporting ICT third-party provider | contractual arrangement concerning critical or important function | unrestricted access/inspection/audit rights; on-site documentation copy right; alternative-assurance exception | financial entity; competent authority; appointed third party | Art. 30(3)(e)(i)/(ii) |

## Sub-SO (DORA)

#### D-06.4.4 — Sub-SO for DORA

```yaml
id: SO-D-06.4.DORA
subdomain: D-06.4
applies_to: [DORA]
inherits_from: SO-DORA-012
source_SR: SR-DORA-022
activation: if DORA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Contractual arrangements concerning critical or important functions grant the financial entity, an appointed third party, and the competent authority unrestricted rights of access, inspection, and audit over the ICT third-party service provider, including on-site copying of relevant documentation where critical to provider operations; those rights must not be impeded or limited by other contractual arrangements or implementation policies, and alternative assurance levels may be agreed only where other clients' rights are affected.

**CSF anchors (from DORA SR-DORA-022):** GV.SC-03, DE.CM-06.

---


## Security Requirements (DORA)

#### 6.4.4 — Art. 30(3)(e)(i)/(ii) unrestricted access / inspection / audit rights over CIF-supporting ICT third-party providers

```yaml
- req_id: 6.4.4
  volere_section: 15
  volere_subtype: audit

  title: "Art. 30(3)(e)(i)/(ii) unrestricted access / inspection / audit rights (including on-site documentation copy right) for financial entity / appointed third party / competent authority over CIF-supporting ICT third-party providers, with narrowly bounded alternative-assurance exception only where other clients' rights are affected"

  derives_from:
    hso_sub_so: SO-D-06.4.DORA
    per_reg_so: SO-DORA-012
    source_sr: SR-DORA-022
    hso_file: ../../HierarchicalSecurityObjectives/D-06_Supply-Chain/D-06.4.md
    objective_ref_section: "### D-06.4.4"

  description: |
    The product shall operate Art. 30(3)(e)(i)/(ii) unrestricted access / inspection / audit rights over ICT third-party service providers for contractual arrangements concerning critical or important functions, extending to financial entity / appointed third party / competent authority and including the on-site documentation-copy right where critical to provider operations; those rights must NOT be impeded or limited by other contractual arrangements or implementation policies; alternative-assurance levels may be agreed only where other clients' rights are affected; DORA CIF audit-rights extend beyond NIS 2 direct-supplier floor (DORA-exceeds-NIS 2 in audit-rights depth); CIF audit-rights do NOT replace CRA Art. 23 economic-operator identification (different direction).

  fit_criterion: |
    A CIF audit-rights framework is operated per CIF-supporting ICT third-party service-provider relationship covering (i) financial-entity access / inspection / audit right exercised directly or through an appointed third party, (ii) competent-authority access / inspection / audit right, (iii) on-site documentation-copy right where critical to provider operations, with (iv) alternative-assurance-levels qualification applied only where other clients' rights are affected — the alternative-assurance exception is narrowly bounded and does not replace the primary audit-right (alternative is documented justification for the affected scope only); the CIF audit-rights contractually anchored via the Art. 30(3)(e)(i) + (ii) clauses (D-06.3 DORA cross-ref), and must not be impeded or limited by other contractual arrangements (e.g., NDAs with shared providers, sub-outsourcing restrictions by upstream ICT providers) or by implementation policies (e.g., provider-internal audit-on-demand-only schedules); the CIF audit-rights are exercised through documented audit procedures covering audit-scope alignment, audit-finding artefact transport, audit-finding acceptance criteria, audit-finding remediation tracking per the financial entity's risk-management framework; in NIS 2 overlap (financial entity is also NIS 2 entity), the CIF audit-rights extend beyond the NIS 2 Art. 21(2)(d) direct-supplier floor (DORA-exceeds-NIS 2 in audit-rights depth) and reach into critical provider chains beyond direct providers; in CRA overlap, economic-operator identification (Art. 23, D-06.4 CRA leg) and CIF audit-rights (Art. 30(3)(e), DORA leg) point in different directions but compose where a CRA-classified product is supplied to a financial entity through importer/distributor channels; in GDPR overlap (non-EU CIF-supporting ICT provider falls under Art. 3(2)), the GDPR Art. 27 representative address coexists with the CIF audit-right, NOT substitute (the two mechanisms operate at distinct boundaries); verified by CIF audit-rights framework documentation review + Art. 30(3)(e)(i)/(ii) audit-exercise record audit + alternative-assurance-exception narrowly-bounded application review + on-site documentation-copy right exercise evidence + Art. 30(3) audit-clause contractual backing attestation + national-financial-supervisory-authority-or-competent-authority inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [6.3.4 (Art. 30(3) CIF-only clauses establish contractual basis for Art. 30(3)(e)(i)/(ii) audit-rights; the contractual-security matrix backstops the audit-rights invocation), 6.1.4 (four-factor proportionality + CIF designation determine which ICT providers fall in scope of CIF audit-rights; vendor-risk-assessment findings feed audit-rights prioritisation)]

  nist_csf: [GV.SC-03, DE.CM-06]

  applicable_if:
    regs: [DORA]
  satisfaction:
    controls: []
    nodes: []

```


---


## Verbatim regulatory basis (DORA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**DORA article (verbatim, Art. 30(3)(e)(i)+(ii)):**
> "Where the contractual arrangements concern critical or important functions, the contractual arrangements shall, in addition to the elements set out in paragraph 2, include the following: … (e) the rights of the financial entity and the competent authority to obtain, from the ICT third-party service provider, unrestricted rights of access, inspection and audit by the financial entity, or an appointed third party, and by the competent authority … including the right to take copies of relevant documentation on-site if critical to the operations of the ICT third-party service provider, the effective exercise of which is not impeded or limited by other contractual arrangements or implementation policies. The right to agree on alternative assurance levels if other clients' rights are affected shall be allowed." — DORA Art. 30(3)(e)(i)+(ii)


## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/DORA.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-06.4: GDPR↔DORA = DIFFERENT-PERSPECTIVE; NIS2↔DORA = COMPLEMENTARY with DORA exceeding NIS 2; CRA↔DORA = DIFFERENT-PERSPECTIVE)
```

### from regs/DORA.md body

**Considerations.**

- In overlap with NIS 2, the DORA CIF audit-rights layer exceeds the NIS 2 direct-supplier floor for financial entities; it extends into critical ICT third-party providers beyond direct providers through the critical provider chain.

### from regs/DORA.md body

- In overlap with CRA, DORA CIF audit rights coexist with CRA economic-operator identification rather than replacing it.


### from regs/DORA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # DORA↔GDPR = Conditional (N in baseline because legal-address representative vs audit-rights are distinct mechanisms; Y when non-EU ICT provider is critical/important for financial entity and falls under Art. 3(2)); DORA↔NIS2 = Y (DORA-exceeds-NIS 2 in audit-rights depth; financial entity is also NIS 2 entity; CIF audit-rights extend beyond NIS 2 direct-supplier floor); DORA↔CRA = Conditional (N in baseline because audit-rights vs economic-operator identification are distinct mechanisms; Y when CRA product is supplied through economic-operator chain to financial entity)

```

### from regs/DORA.md body — field `considerations`

```yaml
  considerations: |
    The DORA third-party-boundary obligation is the CIF audit/access/inspection rights framework for CIF-supporting ICT third-party providers under Art. 30(3)(e)(i)/(ii); the operational substrate is the CIF audit-rights framework keyed by CIF-supporting ICT provider / non-EU status / NIS 2 overlap / CRA product supply chain. The alternative-assurance exception is narrowly bounded — applied only where other clients' rights are affected and never as a wholesale substitution for the primary audit-right. The CIF audit-rights must NOT be impeded or limited by other contractual arrangements or implementation policies (the prohibition is a hard floor — a clause or policy that obstructs the Art. 30(3)(e) right is itself non-compliant). In NIS 2 overlap (financial entity is also NIS 2 entity), the CIF audit-rights extend beyond the Art. 21(2)(d) direct-supplier floor (DORA-exceeds-NIS 2 in audit-rights depth) and reach into critical provider chains beyond direct providers, including the provider's subcontractors where critical to ICT service; the NIS 2 direct-supplier scope record is preserved alongside the extended CIF audit-rights layer (the regimes layer, not collapse). In CRA overlap, the CIF audit-rights (downstream audit) and Art. 23 economic-operator identification (upstream traceability) point in different directions and compose where a CRA-classified product is supplied through an economic-operator chain to a financial entity. In GDPR overlap (non-EU CIF-supporting ICT provider falls under Art. 3(2)), the Art. 27 representative address coexists with CIF audit-rights — the two mechanisms operate at distinct boundaries (legal-address vs audit-rights). The `critical or important functions` undefined distinction is the central DORA ambiguity — appears in 18 of 38 DORA clauses without ever being defined; the chosen reading is that both categories are in scope with distinct obligations attached to each, pending EBA RTS clarity. (Copied from the HSO Considerations block of `### D-06.4.4`; preserved here for self-containment per Volere shell `considerations` field definition.)
```

### from regs/DORA.md body

**DORA article (verbatim, Art. 30(3)(e)(i)+(ii)):**

> (See GDPR↔DORA pair above for the verbatim text.)

<!-- aegis:purity: own_reg=DORA; demoted=6; core_cross_mentions=2 -->

