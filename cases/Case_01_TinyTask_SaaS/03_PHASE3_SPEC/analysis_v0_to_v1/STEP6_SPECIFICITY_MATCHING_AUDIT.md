# STEP 6 — Specificity Matching Audit (V1)

> **Case Study:** Case 01 — TinyTask SaaS  
> **Lifecycle Phase:** AEGIS Phase 3 — Specification  
> **Purpose:** Audit every synthesized requirement's wording against the altitude warranted by its anchored context, and register the corrections applied. Principle: **output specificity ≤ source specificity + documented descents** — a vague statement may not receive a concrete answer, and every mechanism-category descent needs a warrant in the corpus.  
> **Normative basis:** `templates/phase3_functional_spec_guidelines.md` §2.5 (scale L0–L4, warrants W1–W5); `../PHASE3_PROCESS_AND_METHODOLOGY.md` Step 3 item 5 + checklist gate.  
> **Scope:** the 26 RNs of the V1 baseline, notable V1 statements (use case flows, README), and the analysis dossier itself. V0 is the locked input layer: its own wording defines the source altitude (W1) and is not rewritten.

---

## 1. Method

1. **Source altitude:** for each RN, identify its cited chain (regulation article → Phase 2 objective → PRIN-ENG → anchor) and take the *highest specificity level* that chain literally warrants (W1 source statement / W2 regulation verbatim / W3 anchored objective / W4 admitted good practice (ADR-001, pending ratification) / W5 company statement).
2. **Output altitude:** classify the RN's name + EARS formulation on the L0–L4 scale. Quantitative fit criteria (5 attempts, 15 minutes, 14 days) are level-neutral and never counted as descents — though their *values* themselves need derivation warrants (Anti-Pattern 11; §7.3).
3. **Verdict:** `warranted` (wording ≤ warranted level), `demoted` (wording exceeded the warrant and was rewritten), or `warranted — chain observation` (wording fine; the *chain's* citation is stale/wrong and goes to the recalibration backlog, §7).

## 2. Corpus warrant register (verbatim basis)

| Warrant source | Verbatim (from the anchored corpus) | Level it warrants |
|---|---|---|
| CRA Annex I Part I (2)(d) | "protection from unauthorised access through appropriate control mechanisms" (+ reporting of "possible unauthorised access") | L2 access control |
| CRA Annex I Part I (2)(e) | "encrypting relevant data at rest using state-of-the-art mechanisms" | L3 **encryption** (named), state-of-the-art |
| CRA Annex I Part I (2)(j) | attack-surface limitation | L2 |
| CRA Annex I Part I (2)(l) | recording-and-monitoring | L2 |
| GDPR Art. 32(1)(a) | "pseudonymisation and encryption of personal data" | L3 **encryption / pseudonymisation** (named) |
| GDPR Art. 32(2) | "ongoing confidentiality, integrity, availability and resilience of processing systems" | L2 properties |
| GDPR Art. 30 | records of processing activities (accountability) | L2 records |
| GDPR Art. 5(1)(b)/(c)/(e), Art. 6(4), Art. 12(3), 15(3), 17, 20, 28(3)(g) | principles and data-subject rights (purpose limitation, minimization, storage limitation, erasure, portability) | L2 |
| `SO-D-01.1-002` (Phase 2) | "…confidentiality of that data is protected by encrypting relevant data at rest using state-of-the-art mechanisms" | L3 encryption at rest |
| V0 RN7 (locked baseline) | "…enforce cryptographic webhook signature verification" (payment gateway) | L3 signature verification (payment scope) |

Key negative finding: **no anchored document mentions salt, memory-hardness, or any hashing scheme.** The word "salt" appears in the case lane only inside "Saltzer & Schroeder" (author names).

## 3. Operational NFRs (RN1–RN8)

All eight are native to the locked V0 baseline (elicitation/company context, W1) and stay at their source altitude — quantitative constraints (500 ms, 99.5%, 375 px, 50 000 tasks, RPO < 24 h) with no unwarranted mechanism vocabulary. **Verdict: warranted (W1), no action.**

## 4. Synthesized security & privacy NFRs (RN9–RN26)

| RN | Wording audited | Level | Warrant (quote basis) | Warranted | Verdict | Action |
|---|---|---|---|---|---|---|
| RN9 | Multi-Tenant Data Isolation & Mediation | L2 | (2)(d) access control + W5 multi-tenant product | L2 | **Warranted** | — |
| RN10 | Credential Hardening & **Salted Hashing** | L3 (mechanism selection) | (2)(d)/(2)(e) + `SO-D-01.1-002`: state-of-the-art protection; **no corpus text names salt or any hashing scheme** | L2 | **DEMOTED** | Renamed → "Credential Confidentiality Protection (State of the Art)"; EARS + fit criterion rewritten without mechanism selection |
| RN11 | **Cryptographic** Session Management & Invalidation | L3 | (2)(d): "appropriate control mechanisms"; no corpus text names cryptography for sessions | L2 | **DEMOTED** | Renamed → "Session Management & Invalidation"; "unpredictable session identifiers" kept as L2 property |
| RN12 | Role-Based Access Control & Action Mediation | L2/L3 | (2)(d) access control + W5: the product's own Owner/Admin/Member/Viewer role model | L3 | **Warranted** | — |
| RN13 | File Upload Strict Validation & Content Isolation | L2 | (2)(j) attack-surface limitation | L2 | **Warranted** (name); EARS wording demoted | "declared MIME type / magic bytes" → "declared file type / content signature" |
| RN14 | Context-Aware **Output Encoding & Sanitization** | L3 | cited (2)(l) = recording-and-monitoring (see §7); no corpus text names encoding/sanitization | L2 | **DEMOTED** | Renamed → "Untrusted Content Neutralization"; EARS + fit criterion reworded (no "output encoding", "HTML", "XSS") |
| RN15 | Cryptographic Billing Invariant Protection | L3 | W1: V0 RN7 names cryptographic webhook signature verification (payment scope) | L3 | **Warranted** | — |
| RN16 | Cryptographic Webhook Origin Verification | L3 | W1: V0 RN7 names it | L3 | **Warranted** | — |
| RN17 | Inbound API Token Mediation & Rate Limiting | L2 behavioral | (2)(d)+(2)(j); quantified rule is a fit criterion, not a descent | L2 | **Warranted** (wording) | Parameter value flagged by Anti-Pattern 11 — see §7.3 |
| RN18 | Non-Repudiable Security Audit Logging | L2 | (2)(l) recording-and-monitoring | L2 | **Warranted** | — |
| RN19 | Registration Data Minimization by Default | L2 | Art. 5(1)(c) | L2 | **Warranted** | — (chain PO missing, §7) |
| RN20 | Structured Personal Data Portability & Export | L2 | Art. 20 + 15(3) + 12(3) | L2 | **Warranted** | — (chain PO missing, §7) |
| RN21 | Irreversible Data Subject Erasure & Pseudonymization | L2/L3 | Art. 17 erasure; "pseudonymisation" named by Art. 32(1)(a) | L2/L3 | **Warranted** (W2 cross-citation pending) | — (chain PO missing, §7) |
| RN22 | Purpose Limitation & **Time Log** Segregation | L2 | Art. 5(1)(b) + Art. 6(4) | L2 | **DEMOTED** (ghost reference) | Renamed → "Purpose Limitation & Activity Metrics Segregation" — "time log" references functionality that no longer exists in the functional model |
| RN23 | Personal Data Cryptographic Protection at Rest | L3 | Art. 32(1)(a) names encryption | L3 | **Warranted** | — |
| RN24 | **End-to-End Transport Layer** Cryptographic Protection | L3+ (protocol-stack vocabulary) | Art. 32(1)(a) names encryption; Art. 32(2)/`PO-D-01.2-001` warrant "in transit" | L3 | **DEMOTED** | Renamed → "Cryptographic Protection of Data in Transit" |
| RN25 | Automated Orphan File Asset Cleanup & Expiration | L2 behavioral | Art. 5(1)(e) storage limitation; automation = behavioral rule with quantified fit criterion | L2 | **Warranted** | — (chain PO missing, §7) |
| RN26 | Privacy Audit Trail for Personal Data Modifications | L2 | Art. 30 records duty | L2 | **Warranted** | — (chain PO missing, §7) |

## 5. Notable V1 statements audited

| Location | Statement | Verdict | Action |
|---|---|---|---|
| v1 README §1 | "memory-hard credential hashing, token-based session expiration, strict MIME validation, context-aware output encoding" | **DEMOTED** — implementation properties beyond warrant | Reworded to state-of-the-art credential protection, session expiration, file-type validation, untrusted content neutralization |
| `{U.C. 4.1}` ext. 3b1 / `{U.C. 5.2}` ext. 3c1 + minimal guarantee (v1 + top-level Doc02) | "HTML-encodes", "embedded script tags", "stored XSS" | **DEMOTED** — implementation/attack-class jargon beyond warrant | Reworded to "neutralizes… inert text", "embedded active payloads", "executable payloads" |
| STEP1/STEP2/STEP3 dossier rows for RN10/RN13/RN14 | "memory-hard, salted cryptographic hashing algorithm"; "MIME type / magic bytes"; "output encoding… stored XSS" | **DEMOTED** | Reworded at warranted levels; STEP2's warrant claim that `SO-D-02.1-002` "requires memory-hard salted password hashing" corrected — the objective requires vulnerability handling and names no hashing scheme |
| All UC preconditions of the form "secure encrypted channel (RN24)" | "encrypted channel" | **Warranted** (W2: Art. 32(1)(a) names encryption) | — |

## 6. Corrections applied (register)

IDs are unchanged; only wording was demoted to the warranted altitude. Mechanical replacements across the case lane (per-file diff in the commit):

| # | Before | After | Reason |
|---|---|---|---|
| C-01 | "Credential Hardening & Salted Hashing" | "Credential Confidentiality Protection (State of the Art)" | No anchored document names salt or a hashing scheme (§2); chain warrants state-of-the-art protection (L2) |
| C-02 | "Cryptographic Session Management & Invalidation" | "Session Management & Invalidation" | (2)(d) warrants control mechanisms (L2), not a cryptography category for sessions |
| C-03 | "Context-Aware Output Encoding & Sanitization" | "Untrusted Content Neutralization" | No corpus warrant for encoding/sanitization categories; cited (2)(l) is recording-and-monitoring (§7) |
| C-04 | "Purpose Limitation & Time Log Segregation" | "Purpose Limitation & Activity Metrics Segregation" | "Time log" references functionality absent from the functional model (ghost wording) |
| C-05 | "Mandatory End-to-End Transport Layer Cryptographic Protection" | "Cryptographic Protection of Data in Transit" | Art. 32(1)(a) warrants encryption (L3); "end-to-end"/"transport layer" is protocol-stack vocabulary without warrant |
| C-06 | RN10 EARS + fit criterion (STEP3): "memory-hard, salted cryptographic hashing algorithm…"; "verified salted cryptographic one-way derivation formats with unique per-credential salt parameters" | "…state-of-the-art mechanisms such that the original value cannot be recovered from any stored representation…"; "one-way verifiable representations, unique per credential, zero recoverable credential values in logs or data stores" | Mechanism selection demoted; verifiability preserved (TEST stays possible) |
| C-07 | RN13 EARS: "declared MIME type and file signature (magic bytes)"; "MIME/magic-byte spoofing test suite" | "declared file type and actual content signature"; "file-type spoofing test suite" | MIME/magic-byte = implementation vocabulary |
| C-08 | RN14 EARS + fit criterion (STEP3): "context-aware output encoding… HTML tags…"; "stored XSS test vectors" | "neutralize embedded active content… rendered as inert text"; "stored script-injection test vectors" | Implementation/attack-class jargon demoted |
| C-09 | v1 README §1 feature list | state-of-the-art credential protection, session expiration, file-type validation, untrusted content neutralization | Implementation properties beyond warrant |
| C-10 | UC 4.1 ext. 3b1, UC 5.2 ext. 3c1 + minimal guarantee (v1 + top-level Doc02): "script tags", "HTML-encodes", "stored XSS" | neutralized/disarmed wording ("embedded active payloads", "executable payloads") | Implementation/attack-class jargon beyond warrant |
| C-11 | STEP2: "`SO-D-02.1-002`: Requires memory-hard salted password hashing and credential hardening." | Corrected to `SO-D-01.1-002` + CRA (2)(d) requiring state-of-the-art credential protection, mechanism selection deferred to design | **Fabricated warrant removed** — the cited objective is about vulnerability handling and names no hashing scheme |

## 7. Residual observations (chain recalibration backlog — outside this wording pass)

1. **Missing Phase 2 POs cited by absorbed chains:** `PO-D-06.1-001`/`PO-D-06.2-001` (RN19, RN20, RN21, RN22, RN25) and `PO-D-03.1-001` (RN26) do not exist in this case's Phase 2 deliverable (D-06 there is Supply Chain, SO-only; D-03 objectives are absent). The data-subject-rights POs that exist are `PO-D-05.1`–`PO-D-05.4` (+ `PO-D-01.4` for accuracy/rectification, correctly cited by STEP5 CH-04).
2. **CRA sub-point mismatches:** RN14, RN15, RN16 cite Annex I Part I (2)(l), which the corpus reads as *recording-and-monitoring* — the constraints' subjects (content neutralization, billing invariant, webhook verification) map to other sub-points ((2)(k) exploitation mitigation / W1 V0 RN7); RN10 cites (2)(d)+(2)(j) for credential protection whose natural home is (2)(e) state-of-the-art data protection. Requires a dedicated chain recalibration.
3. **Parameter-value warrants (Anti-Pattern 11):** quantified values not derived from a cited source — RN17's "100 requests per minute", `{U.C. 1.1}`'s 15-minute lockout window, RN25's 14-day expiration — need an explicit derivation (regulation, risk assessment, or cited practice) in the recalibration pass; they may stand as documented defaults only where the Intake or Phase 2 supports them.
4. **W4-pending:** any future constraint that genuinely needs a mechanism category beyond W1–W3 (e.g., a mandated hashing family) waits for ADR-001 ratification (T2/T3 sources) instead of absorbing general knowledge.
