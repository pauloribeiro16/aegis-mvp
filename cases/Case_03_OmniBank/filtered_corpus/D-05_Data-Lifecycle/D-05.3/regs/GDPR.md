# D-05.3 — GDPR module

> Regulation-specific layer: applies when `GDPR` is in scope
> (activation: `if GDPR in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SG-GDPR-018 + SG-GDPR-019 | Personal data erased without undue delay on the data subject's Art. 17(1) request + processor deletion or return of all personal data (Art. 28(3)(g)) after end of processing services, with existing copies deleted unless Union/Member State law requires storage | Personal data; controller + processor; Art. 17(1)(a)–(f) + Art. 17(2) + Art. 28(3)(g) + Art. 5(1)(c)/(e) cross-refs + Art. 19 cascade (cross to D-04.3 SG-GDPR-012); PR.DS-10 + ID.AM-08 + GV.SC-04 |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **GDPR** | controller-side policy execution on personal data (data-subject right + processor mirror) | data subject's Art. 17(1) request (6 grounds (a)–(f)) — TRIGGERED; processor's contract-end moment under Art. 28(3)(g) — PER-CONTRACT-END | cryptographic key-destruction (SR-GDPR-030 POLY-S3 → cryptographic-erasure reading) where the controller retains the key outside the data substrate and the data is encrypted at rest; secure overwrite where cryptographic-erasure is not feasible; physical-media destruction as ultimate fallback (rare, narrow) | Art. 5(2) accountability evidence (Art. 17(2) confirmation + Art. 12 transparency + Art. 30 RoPA record update + Art. 35(7) DPIA record where applicable) + processor-side Art. 28(3)(g) deletion-or-return record | supervisory authority (DPA) — Art. 58 inspection; downstream recipients per Art. 19 cascade (D-04.3 SG-GDPR-012) | Art. 17(1)(a)–(f) + Art. 17(2) + Art. 17(3)(a)–(e) exceptions + Art. 28(3)(g) + Art. 5(1)(c)/(e) cross + Art. 12 transparency + Art. 19 cascade |

## Sub-SO (GDPR)

#### D-05.3.1 — Sub-SO for GDPR

```yaml
id: SG-D-05.3.GDPR
subdomain: D-05.3
applies_to: [GDPR]
inherits_from: SG-GDPR-018, SG-GDPR-019
source_SR: SR-GDPR-030, SR-GDPR-031
activation: if GDPR in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Personal data are erased without undue delay on the data subject's Art. 17(1) request where one of the six Art. 17(1) grounds (a)–(f) applies: (a) no longer necessary for original purposes; (b) consent withdrawn (no other Art. 6(1) basis applies); (c) Art. 21(1) objection (no overriding compelling legitimate ground) or Art. 21(2) direct-marketing objection; (d) unlawful processing; (e) legal-obligation erasure; (f) information-society-service offers to a child (Art. 8(1)). On processor contract end, the processor deletes or returns all personal data and existing copies per Art. 28(3)(g).

- The Art. 19 cascade (rectification/erasure/restriction notification to recipients) is structurally in D-04.3 SG-GDPR-012 (notification, not erasure); the high-level SO surfaces the erasure itself, not the cascade.
- The `deletes` polysemy in Art. 28(3)(g) is resolved to the cryptographic-erasure reading per SR-GDPR-030 (key destruction scales across backups/replicas without per-copy destruction; aligns with EDPB Guidelines 5/2020).

**CSF anchors (from `SR-GDPR-030` + `SR-GDPR-031` v0.3
security_rationale):**
PR.DS-10, ID.AM-08, GV.SC-04.
*(`SR-GDPR-030` covers the Art. 17 + Art. 5(1)(c)/(e) + Art. 28(3)(g) erasure obligation anchored to **PR.DS-10** (Data-in-use protected — the runtime-protection layer that erasure must extend through: protection against residual exposure during query and join operations is the prerequisite for a defensible cryptographic-erasure posture, because if the in-use protections fail the controller cannot claim the additional information held under separate technical and organisational control was effective; the cryptographic-erasure reading relies on the in-use key-custody discipline) + **ID.AM-08** (Data managed consistent with risk strategy — the lifecycle-management layer: a documented deletion procedure keyed to the Art. 17 trigger conditions and the Art. 5(1)(e) purpose-end moment, with cryptographic key destruction as the operational realisation of `deletes` for any system where per-copy destruction is not feasible across backups and replicas). `SR-GDPR-031` covers the Art. 28(3)(g) processor-side mirror anchored to **PR.DS-10** + **GV.SC-04** (Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations — the contractual mechanism for the controller-processor deletion-cadence obligation; the contract-end deletion is the contractually-supplied trigger). The three subcategories together operationalise the GDPR erasure architecture: PR.DS-10 supplies the cryptographic-key-custody substrate for the cryptographic-erasure reading; ID.AM-08 supplies the lifecycle-management discipline (Art. 17 trigger procedure + Art. 5(1)(e) purpose-end procedure); GV.SC-04 supplies the contractual substrate for the Art. 28(3)(g) processor-side mirror. Art. 5(2) accountability closes the supervisory-authority evidence loop; the Art. 17(2) confirmation of action closes the data-subject-communication loop; the Art. 12 transparency obligation closes the procedural-information loop; ... (line truncated to 2000 chars)

---


## Security Requirements (GDPR)

#### 5.3.1 — Personal-data erasure per Art. 17 + Art. 28(3)(g) processor-side mirror, with cryptographic key-destruction deletion path

```yaml
- req_id: 5.3.1
  volere_section: 15
  volere_subtype: privacy

  title: "Personal data erased without undue delay on the data subject's Art. 17(1) request where one of the 6 grounds applies; processor deletes or returns all personal data on contract end per Art. 28(3)(g); cryptographic key destruction as deletion path"

  derives_from:
    hso_sub_so: SG-D-05.3.GDPR
    per_reg_so: SG-GDPR-018, SG-GDPR-019
    source_sr: SR-GDPR-030, SR-GDPR-031
    hso_file: ../../HierarchicalSecurityObjectives/D-05_Data-Lifecycle/D-05.3.md
    objective_ref_section: "### D-05.3.1"

  description: |
    The product shall erase personal data without undue delay on the data subject's Art. 17(1) request where one of the six grounds (a)–(f) applies: (a) no longer necessary for original purposes; (b) consent withdrawn; (c) Art. 21 objection; (d) unlawful processing; (e) legal-obligation erasure; (f) information-society-service offers to a child; on processor contract end, the processor deletes or returns all personal data and deletes existing copies per Art. 28(3)(g), operationalised through cryptographic key destruction where the controller holds the key outside the data substrate (per SR-GDPR-030 POLY-S3 → cryptographic-erasure reading).

  fit_criterion: |
    A controller-side erasure architecture is operated under PR.DS-10 in-use key-custody discipline (the runtime-protection prerequisite that erasure must extend through — active replicas, query caches, processing pipelines) + ID.AM-08 documented deletion procedure keyed to the Art. 17 trigger conditions and Art. 5(1)(e) purpose-end moment (the lifecycle-management substrate); cryptographic key destruction is the operational realisation of `deletes` per SR-GDPR-030 POLY-S3 → cryptographic-erasure reading — key held outside the data substrate, key destruction scales across backups and replicas without per-copy destruction, aligned with EDPB Guidelines 5/2020; backup copies are in scope per SR-GDPR-031 SCOPE-Q R1 unless protected by a separate Union/Member State law storage obligation; audit logs are out of scope to the extent needed for legal-accountability purposes (SR-GDPR-031 R1); the 6 Art. 17(1) grounds (a)–(f) are evaluated on every request; the Art. 17(3) carve-outs (freedom of expression, legal obligation, public-interest public-health, archiving per Art. 89(1), establishment-exercise-defence of legal claims) are honoured as exception structure without relaxing the erasure duty beyond what they permit; Art. 17(2) confirmation of action is delivered to the data subject; Art. 12(1) transparency on the right is provided; the Art. 19 cascade to downstream recipients (rectification/erasure/restriction notification) is executed (handled structurally in D-04.3 SG-GDPR-012 — not duplicated here); Art. 30(1)(f) RoPA envisages-time-limits-for-erasure are documented per category; Art. 5(2) accountability evidence is inspection-ready; for a processor, the Art. 28(3)(g) contract-end deletion-or-return obligation is documented with GV.SC-04 evidentiary confirmation (audit, test result, or independent inspection so the controller can demonstrate, against Art. 5(2), that on the day any supervisory inspection occurs the personal data under the processor's custody no longer ex... (line truncated to 2000 chars)

  priority: MUST
  verification_method: TEST
  dependencies: [5.3.2 (when CRA-classified product processes personal data — the controller-side Art. 17 path is executed through the manufacturer's (2)(m) affordance at the architectural layer; the manufacturer enables the deletion affordance, the controller operationalises the data-subject right through that affordance)]

  nist_csf: [PR.DS-10, ID.AM-08]
  nist_pf: [CT.DM-P4, CT.DM-P5]

  applicable_if:
    regs: [GDPR]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (GDPR)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**GDPR article (verbatim, Art. 17(1) + Art. 5(1)(c)/(e) + Art. 28(3)(g)):**
> "The data subject shall have the right to obtain from the controller the erasure of personal data concerning him or her without undue delay and the controller shall have the obligation to erase personal data without undue delay where one of the following grounds applies: (a) the personal data are no longer necessary in relation to the purposes for which they were collected or otherwise processed; (b) the data subject withdraws consent …; (c) the data subject objects …; (d) the personal data have been unlawfully processed; (e) the personal data have to be erased for compliance with a legal obligation …; (f) the personal data have been collected in relation to the offer of information society services …" — Art. 17(1) GDPR
>
> "Processing by a processor … be governed by a contract … that sets out … the obligation to … delete or return all the personal data to the controller after the end of the provision of services relating to processing … and delete existing copies." — Art. 28(3)(g) GDPR

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/GDPR.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-05.3: GDPR↔CRA = COMPLEMENTARY (SAME — controller-side Art. 17 policy execution stacks with the manufacturer-side Annex I Part I (2)(m) user-facing removal affordance; CRDA initial classification held); no SCOPE-DISJOINT, no CONTRADICTORY, no CORRECTED)
```

### from regs/GDPR.md body

**Considerations.**

- The CRA Annex I Part I (2)(m) affordance is the manufacturer-side architectural companion — when a CRA-classified product processes personal data, the controller-side Art. 17 path is executed through the manufacturer's deletion affordance; for an integrated manufacturer-controller, the controller's Art. 5(2) accountability evidence is discharged via the Annex VII technical documentation.

### from regs/GDPR.md body

- Art. 17(3) carve-outs (freedom of expression, legal obligation, public-interest public-health, archiving/research/statistical, establishment-exercise-defence of legal claims) do not relax the erasure duty beyond what they permit; the manufacturer-side CRA (2)(m) obligation is independent of the GDPR-side Art. 17(3) exceptions (the user retains the product-side removal affordance even when the controller-side obligation is lawfully suspended).

### from regs/GDPR.md body — field `scope_overlap`

```yaml
    scope_overlap: Y   # GDPR activates whenever GDPR in applicable_regs; the CRA layer (5.3.2) activates separately when CRA-classified product processes personal data — when both activate, they stack on the same party

```

### from regs/GDPR.md body — field `considerations`

```yaml
  considerations: |
    The GDPR erasure obligation is the controller-side personal-data erasure anchored on Art. 17(1) `without undue delay` on the data subject's request (6 grounds (a)–(f)) with Art. 17(2) confirmation + Art. 12 transparency + Art. 19 cascade (cross to D-04.3 SG-GDPR-012 — notification is structurally distinct from erasure and is not duplicated here) + Art. 28(3)(g) processor-side mirror on contract end. The CRA Annex I Part I (2)(m) affordance is the manufacturer-side architectural companion — when a CRA-classified product processes personal data, the controller-side Art. 17 path is executed through the manufacturer's deletion affordance; for an integrated manufacturer-controller, the controller's Art. 5(2) accountability evidence is discharged via the Annex VII technical documentation. The Art. 17(3) carve-outs (freedom of expression, legal obligation, public-interest public-health, archiving per Art. 89(1), establishment-exercise-defence of legal claims) do not relax the erasure duty beyond what they permit; the manufacturer-side CRA (2)(m) obligation is independent of the GDPR-side Art. 17(3) exceptions — the user retains the product-side removal affordance even when the controller-side obligation is lawfully suspended. The `deletes` polysemy in Art. 28(3)(g) is resolved to the cryptographic-erasure reading per SR-GDPR-030 (key destruction scales across backups/replicas without per-copy destruction; aligns with EDPB Guidelines 5/2020). The processor-side Art. 28(3)(g) mirror requires GV.SC-04 evidentiary confirmation (audit, test result, or independent inspection) so the controller can demonstrate, against Art. 5(2), that the post-contract data residue on processor systems was actually removed on the documented date. (Copied from the HSO Considerations block of `### D-05.3.1`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=GDPR; demoted=5; core_cross_mentions=1 -->
