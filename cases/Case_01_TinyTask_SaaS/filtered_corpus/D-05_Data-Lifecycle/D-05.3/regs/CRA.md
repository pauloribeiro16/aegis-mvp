# D-05.3 — CRA module

> Regulation-specific layer: applies when `CRA` is in scope
> (activation: `if CRA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| CRA | SO-CRA-036 | User of a product with digital elements can securely and easily remove, on a permanent basis, all data and settings of the product; where such data can be transferred to other products or systems, the transfer is done in a secure manner | Product data (personal or other) + settings; manufacturer-bound; Annex I Part I (2)(m) first limb (terminal deletion) + second limb (cross-product secure transfer) + Annex II §8(d) decommissioning instructions; PR.DS-10 + ID.AM-08 (+ PR.DS-02 for the second limb) |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **CRA** | manufacturer-side user-facing removal affordance on product data + settings + secure cross-product transfer | user's product-initiated removal request — TRIGGERED; user's election to transfer to another product — TRIGGERED | secure permanent removal (SR-CRA-048 VAG+POLY-S2 → cryptographic-erase / secure-overwrite / physical-media-destruction R3 reading) + secure cross-product transfer (SR-CRA-049 VAG-S2 → confidentiality + integrity + destination-authentication R1) | Annex VII §2 technical documentation (data-class inventory + deletion-mechanism architecture) + Annex II §8(d) decommissioning instructions + Annex VII §6 test reports demonstrating verification of conformity with Annex I Part I (2)(m) | market surveillance authority (MSA) — Annex VII compliance demonstration on reasoned request; user as the direct recipient of the removal affordance | Annex I Part I (2)(m) first limb + second limb + Art. 13(1) design-time + Art. 13(18) + Annex II §8(d) + Art. 13(2) risk assessment underpinning the deletion-mechanism depth |

## Sub-SO (CRA)

#### D-05.3.2 — Sub-SO for CRA

```yaml
id: SO-D-05.3.CRA
subdomain: D-05.3
applies_to: [CRA]
inherits_from: SO-CRA-036
source_SR: SR-CRA-048, SR-CRA-049
activation: if CRA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** The user of a product with digital elements can securely and easily remove, on a permanent basis, all data and settings of the product; where such data can be transferred to other products or systems, the transfer is done in a secure manner (Annex I Part I (2)(m) first limb — terminal deletion on user election — and second limb — secure cross-product transfer).

**Considerations.**
- The CRA (2)(m) affordance is an architectural obligation addressed to the product, not a data-subject right — the user retains the product-side removal affordance even when the controller-side Art. 17 obligation is lawfully suspended under Art. 17(3). The two regimes do NOT override each other.
- `securely and easily` is VAG+COORD-S2 (both secure AND easy required — R1 reading via a discoverable user-interface affordance); `permanent basis` is POLY-VAG-S2 (R3 — cryptographic-erase, secure-overwrite, or physical-media destruction are all acceptable).
- The second-limb secure cross-product transfer is the architectural companion to the first-limb terminal deletion; both stack on the same product event when personal data is involved (the controller's Art. 17 path executes through the manufacturer's (2)(m) affordance).

**CSF anchors (from `SR-CRA-048` + `SR-CRA-049` v0.3 security_rationale):**
PR.DS-10, ID.AM-08 (+ PR.DS-02 for the second limb).
*(`SR-CRA-048` covers the Annex I Part I (2)(m) first-limb terminal-deletion duty anchored to **PR.DS-10** (Data-in-use protected — the cryptographic-erase and overwrite-erase controls applied during device shutdown: the data-in-use protection layer must provide the secure-removal affordance — secure enough to make recovery infeasible, easy enough that the user can execute it without specialist tooling) + **ID.AM-08** (Data managed consistent with the organisation's risk strategy — the architectural-decision layer: the manufacturer designs the product to retain no extraneous data that would survive disposal, with the data-class inventory in the technical documentation under Annex VII §2 evidencing that the deletion surface is comprehensive). `SR-CRA-049` covers the Annex I Part I (2)(m) second-limb secure-transfer duty anchored to **PR.DS-02** (Data-in-transit protected — the integration-side baseline: any in-band transfer path inherits the same confidentiality + integrity baseline as data-in-transit more generally, with destination authentication, content integrity, and in-flight confidentiality as the three constituent controls) + **ID.AM-08** (the risk-strategy dimension: the choice of binding mechanism for each interface class — paired-device authentication, signed transfer payloads, mutually-authenticated transport encryption, signed export manifests — is determined by the Art. 13(2) risk assessment for the relevant product class). Together PR.DS-10, ID.AM-08, and PR.DS-02 enable the manufacturer to demonstrate ex post, through documented deletion affordances, decommissioning instructions under Annex II §8(d), cross-product-transfer binding mechanisms, and the data-class inventory, that the (2)(m) first-limb + second-limb duties have been discharged and that users can exercise the permanent-removal + secure-transfer rights on discoverable user-interface paths.)*

---


## Security Requirements (CRA)

#### 5.3.2 — Manufacturer-side user-facing secure data and settings removal per Annex I Part I (2)(m) first limb, with discoverable affordance + Annex II §8(d) decommissioning instructions

```yaml
- req_id: 5.3.2
  volere_section: 15
  volere_subtype: privacy

  title: "User of a product with digital elements can securely and easily remove, on a permanent basis, all data and settings of the product via a discoverable user-interface affordance, with Annex II §8(d) decommissioning instructions"

  derives_from:
    hso_sub_so: SO-D-05.3.CRA
    per_reg_so: SO-CRA-036
    source_sr: SR-CRA-048
    hso_file: ../../HierarchicalSecurityObjectives/D-05_Data-Lifecycle/D-05.3.md
    objective_ref_section: "### D-05.3.2"

  description: |
    The product shall expose a discoverable user-interface affordance allowing the user to securely and easily remove, on a permanent basis, all data and settings of the product (Annex I Part I (2)(m) first limb — both secure AND easy; permanent = recovery-infeasible), supported by Annex II §8(d) decommissioning instructions and the Annex VII §2 data-class inventory demonstrating that the deletion surface is comprehensive.

  fit_criterion: |
    A manufacturer-side user-facing removal affordance is exposed through the product UI (per SR-CRA-048 VAG+COORD-S2 R1 — both secure AND easy via a discoverable user-interface affordance; a deletion mechanism that is easy but not secure (plain-delete of pointers without overwriting storage) fails, one that is secure but not easy (deep-wipe requiring specialist tooling the user does not have) fails); the deletion surface is comprehensive (ID.AM-08 data-class inventory per Annex VII §2 covers telematics, locally-cached cloud-synced state, paired-device records — SR-CRA-048 POLY-S2 R1 universal-quantifier reading); the deletion mechanism applies cryptographic-erase, secure-overwrite, or physical-media destruction as needed for recovery-infeasibility per SR-CRA-048 POLY-VAG-S2 R3 (any method that makes recovery infeasible is acceptable); PR.DS-10 in-use data-path coverage is documented (the runtime-protection layer that the secure-removal affordance extends through); ID.AM-08 data-class inventory is maintained (the architectural-decision layer — the manufacturer designs the product to retain no extraneous data that would survive disposal); Annex II §8(d) decommissioning instructions are supplied with the product (the information deliverable under Art. 13(18)); Annex VII §2 technical documentation + Annex VII §6 test reports demonstrate verification of conformity with Annex I Part I (2)(m); the (2)(m) affordance is independent of any GDPR-side Art. 17(3) carve-outs — the user retains the product-side removal affordance even when the controller-side obligation is lawfully suspended under Art. 17(3); for an integrated manufacturer-controller on a CRA-classified product processing personal data, the manufacturer's (2)(m) affordance is the architectural substrate through which the controller's Art. 17 path executes and the manufacturer's Annex VII documentation discharges the controller's Art. 5(2) accountability evidence; verified by UI affordance discoverability test + d... (line truncated to 2000 chars)

  priority: MUST
  verification_method: TEST
  dependencies: [5.3.1 (when CRA-classified product processes personal data — the manufacturer's (2)(m) affordance is the architectural substrate through which the controller-side Art. 17 path executes; the layer-segregated evidence architecture means both obligations are documented separately for compliance demonstration even when a unified deletion pipeline exists at the architectural layer)]

  nist_csf: [PR.DS-10, ID.AM-08]

  applicable_if:
    regs: [CRA]
  satisfaction:
    controls: []
    nodes: []

```

---


## Verbatim regulatory basis (CRA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**CRA article (verbatim, Annex I Part I (2)(m) + Annex II §8(d)):**
> "On the basis of the cybersecurity risk assessment referred to in Article 13(2) … the product with digital elements shall: … (m) allow users to securely and in a timely manner remove or transfer all of the data they have provided to, or generated through, the use of, the product with digital elements, and provide the user with information on how to do so, including for the purpose of switching to another product." — CRA Annex I Part I (2)(m)
>
> "The instructions and information referred to in paragraph 1 shall include … the secure decommissioning of the product with digital elements, including, where applicable, information on how user data can be securely removed." — CRA Annex II §8(d)

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/CRA.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-05.3: GDPR↔CRA = COMPLEMENTARY (SAME — manufacturer-side Annex I Part I (2)(m) user-facing removal affordance stacks with the controller-side Art. 17 policy execution; CRDA initial classification held); no SCOPE-DISJOINT, no CONTRADICTORY, no CORRECTED)
```

### from regs/CRA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # CRA activates whenever CRA in applicable_regs (the manufacturer-side (2)(m) affordance is an architectural obligation, not a data-subject right, and is independent of GDPR-side Art. 17(3) carve-outs); when the CRA-classified product processes personal data and the user is the data subject, the GDPR layer (5.3.1) also activates and the two stack on the same party in the personal-data subset

```

### from regs/CRA.md body — field `considerations`

```yaml
  considerations: |
    The CRA erasure obligation is the manufacturer-side user-facing removal affordance anchored on Annex I Part I (2)(m) first limb — terminal deletion on user election — supported by Annex II §8(d) decommissioning instructions and the Annex VII §2 data-class inventory. The (2)(m) affordance is an architectural obligation addressed to the product, NOT a data-subject right — the user retains the product-side removal affordance even when the controller-side Art. 17 obligation is lawfully suspended under Art. 17(3) (the layer-segregated exception structure: GDPR-side Art. 17(3) governs the controller; CRA-side (2)(m) governs the manufacturer; neither overrides the other). `securely and easily` is VAG+COORD-S2 R1 (both secure AND easy required via a discoverable user-interface affordance); `permanent basis` is POLY-VAG-S2 R3 (any method that makes recovery infeasible — cryptographic-erase, secure-overwrite, physical-media destruction — is acceptable); `all data and settings` is POLY-S2 R1 (universal — includes telematics, locally-cached cloud-synced state, paired-device records). The (2)(m) second-limb secure cross-product transfer (handled by SR-CRA-049, structurally relevant to D-03.3 as well) is the architectural companion to the first-limb terminal deletion and supports cross-controller portability (D-05.4) when portability-eligible data resides in a CRA-classified product — but is NOT a portability right on D-05.4. For an integrated manufacturer-controller where the manufacturer's cloud backend is also the controller's processor, the processor-side Art. 28(3)(g) mirror (in 5.3.1) is exercised through the manufacturer's (2)(m) affordance at the architectural level but the regulatory obligations remain distinct — the three obligations (Art. 17, Art. 28(3)(g), (2)(m)) are discharged with a single deletion pipeline but documented separately for compliance demonstration. (Copied from the HSO Considerations block of `### D-05.3.2`; preserved here for self-contained trace... (line truncated to 2000 chars)
```

<!-- aegis:purity: own_reg=CRA; demoted=3; core_cross_mentions=1 -->