# D-01.3 — Pair analysis: GDPR ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ CRA

**GDPR article (verbatim — SR-GDPR-003 + SR-GDPR-004, Art. 4(5) + Art. 32(1)(a) + Art. 34(3)(a)):**
> Art. 4(5) pseudonymisation … the personal data can no longer be attributed to a specific data subject without the use of additional information, provided that such additional information is kept separately and is subject to appropriate technical and organisational measures. Art. 34(3)(a) … render the personal data unintelligible to any person who is not authorised to access it, such as encryption.

**CRA article (verbatim — SR-CRA-004, Annex I Part I (2)(d) + (2)(e)):**
> Annex I Part I (2)(e) … by encrypting … and by using other technical means. Annex I Part I (2)(d) protect from unauthorised access by appropriate control mechanisms.

**Scope comparison:**
- GDPR: personal-data pseudonymisation/encryption with separate-storage test (Art. 4(5)); unintelligibility carve-out (Art. 34(3)(a)).
- CRA: cryptographic key separation from operational environment (custodian ≠ consumer), anchored via the (2)(d) RBAC + (2)(e) "other technical means" reading.
- Scope overlap: Y when the CRA product protects personal data.

**Trigger comparison:**
- GDPR: continuous + breach-context (Art. 34(3)(a) carve-out triggered by breach).
- CRA: design-time invariant (separation is a property of the product).
- Trigger alignment: PARTIAL — GDPR's Art. 34(3)(a) is breach-triggered; CRA's separation is continuous. The trigger alignment is partial because one obligation is breach-triggered (the carve-out) and the other is design-time.

**Threshold/timeline comparison:**
- GDPR: "appropriate technical and organisational measures" + unintelligibility "render … unintelligible to any person who is not authorised" (Art. 34(3)(a) "such as encryption").
- CRA: functional-RBAC separation (R2 reading per SR-CRA-004 ambiguity_notes).
- Tension: NONE — the two converge on key separation as the technical property and "unauthorised party cannot access" as the operational test.

**Recipient comparison:**
- GDPR: SA on inspection.
- CRA: MSA.

**Content template comparison:**
- GDPR: Art. 5(2) accountability burden + Art. 32(1)(a) documented measure.
- CRA: Annex VII §2/§3 technical documentation + Annex VII §6 test evidence.

**Classified relationship (from CRDA):** COMPLEMENTARY.

**Verified relationship (after OJ-text analysis):** SAME (CORRECTED — wording only).

**Reasoning:** Both impose key separation (GDPR Art. 4(5) de-attribution test + Art. 34(3)(a) unintelligibility carve-out ↔ CRA Annex I (2)(d)+(e) functional-RBAC separation) as the technical property; they differ on the trigger (breach-context carve-out vs design-time invariant) and on the documentation artefact (Art. 32 documentation vs Annex VII conformity dossier). On a single product that handles personal data, both are met by the same key-separation architecture; the documentation is the only difference.

**Scope-disjoint test:** Y on the same product; disjoint in baseline.

**Downstream implication:** Stack-merge with documentation. A single key-custody architecture (HSM-anchored, RBAC-separated) plus the dual documentation pack (Art. 32 + Annex VII) discharges both.

---


## Summary (Domain Analysis)

<!-- pair: GDPR,CRA -->
| GDPR ↔ CRA | **Complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-003 + SR-GDPR-004, Art. 4(5) + Art. 32(1)(a) + Art. 34(3)(a)) | Pseudonymisation/encryption with key separation; Art. 4(5) de-attribution test; unintelligibility as Art. 34(3)(a) carve-out from data-subject notification | Controller/processor; personal-data scope; key separation is the carve-out anchor; PR.DS-01 |
| **CRA** (SR-CRA-004, Annex I Part I (2)(d)+(e)) | Cryptographic key separation from operational environment (custodian ≠ consumer) | Manufacturer; product-level; "personal or other"; functional role-based access-control separation (T2-vs-text gap reading) |

**Why Complementary**: GDPR's key-separation obligation is the mechanism that earns the Art. 34(3)(a) data-subject-notification carve-out: if the cryptographic key is unavailable to the adversary, the breached data is unintelligible, and notification is not required. CRA's key-separation obligation is a product-design invariant: the custodian holding the key material is not the same role as the operator consuming the data. The two converge on key separation as the technical property; they differ on the trigger (GDPR's breach-context carve-out vs CRA's design-time invariant). → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-003 + SR-GDPR-004; `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-004



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
43 lines — see ../../_migration_report.md)_

