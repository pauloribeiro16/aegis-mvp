# V0 → V1 → V2 Analysis Tables — TinyTask SaaS

> **Document Purpose:** Tabular view of the three baseline versions. In V1, every security & privacy NFR is **absorbed into the functional requirement card it applies to** under `Security & Privacy Constraints`, one condensed tracing line per NFR: `<Regulation Article> → <Phase 2 rule> → <PRIN-ENG principle> → <control anchor>`. Cross-cutting NFRs (RN17, RN18, RN24) stay standalone in the Quality Attributes table.

> **Source of Truth:** `v0_functional_baseline/` (V0, LOCKED) · top-level `Doc01`/`Doc02` (V2, ACTIVE) · `v1_security_privacy_synthesis/Doc01` (V1, APPROVED).

---

## §1 Version Ladder

| Version | Path | Role | R | RN | Status |
|---|---|---|---|---|---|
| **V0** | `v0_functional_baseline/` | Pure functional snapshot (8 packages, 18 cards, 18 PUCs, 18 UCs). | 18 | 0 | LOCKED |
| **V1** | `v1_security_privacy_synthesis/` | V0 + synthesis absorbed + Functional Refinement Pass (Step 4b): 15 security/privacy NFRs embedded in R cards; RN17/RN18/RN24 cross-cutting standalone; RN1–RN8 operational standalone; +1 derived requirement (`R1.3`), 2 descriptions refined, 1 re-prioritized (register: STEP5). | 19 | 26 (`RN1`–`RN26`) | APPROVED |
| **V2** | top-level `Doc01`/`Doc02` | Consolidated functional baseline (v2.2); security traceability via Doc02 matrix. | 19 | 26 | ACTIVE |

## §2 Per-Requirement Absorption (R1.1–R8.2)

| Req ID | Name | Priority | Absorbed NFRs (tracing chain in card) |
|---|---|---|---|
| `R1.1` | Register and authenticate user accounts | Must | **NFR-RN10** Credential Confidentiality Protection (State of the Art) — `CRA Annex I Part I (2)(d) + (2)(j)` → `SO-D-02.1-002, SO-D-01.1-002` → `PRIN-ENG-04` → CSF PR.DS-01, PR.PS-02, PR.PS-01<br>**NFR-RN11** Session Management & Invalidation — `CRA Annex I Part I (2)(d) + (2)(j)` → `SO-D-02.2-002` → `PRIN-ENG-04` → CSF PR.AA-01, PR.AA-05, PR.AA-06<br>**NFR-RN19** Registration Data Minimization by Default — `GDPR Art. 5(1)(c)` → `PO-D-05.1-001` → `PRIN-ENG-06` → CSF PR.DS-10, GV.OC-03 / PF CT.DP-P2 |
| `R1.2` | Manage user profile and account preferences | Must | **NFR-RN23** Personal Data Cryptographic Protection at Rest — `GDPR Art. 32(1)(a) + Art. 5(1)(f)` → `PO-D-01.1-001` → `PRIN-ENG-01` → CSF PR.DS-01, PR.DS-10 / PF PR.DS-P1<br>**NFR-RN26** Privacy Audit Trail for Personal Data Modifications — `GDPR Art. 30` → `PO-D-09.4-001` → `PRIN-ENG-07` → CSF ID.AM-08, PR.DS-10, DE.CM-01 / PF CM.AW-P2<br>*D3 (STEP5 CH-04): Should → Must (GDPR Art. 5(1)(d) + Art. 16, `PO-D-01.4-001`)* |
| `R1.3` | Recover access to a locked user account | Must | **NFR-RN10** Credential Confidentiality Protection (State of the Art) — `CRA Annex I Part I (2)(d) + (2)(j)` → `SO-D-02.1-002, SO-D-01.1-002` → `PRIN-ENG-04` → CSF PR.DS-01, PR.PS-02, PR.PS-01<br>**NFR-RN11** Session Management & Invalidation — `CRA Annex I Part I (2)(d) + (2)(j)` → `SO-D-02.2-002` → `PRIN-ENG-04` → CSF PR.AA-01, PR.AA-05, PR.AA-06<br>*D1 (STEP5 CH-01): derived in the V1 Refinement Pass* |
| `R2.1` | Create and configure workspace | Must | **NFR-RN9** Multi-Tenant Data Isolation & Mediation — `CRA Annex I Part I (2)(d)` → `SO-D-02.1-002` → `PRIN-ENG-03` → CSF PR.PS-02, PR.PS-01, ID.RA-01 |
| `R2.2` | Invite workspace members and manage access roles | Must | **NFR-RN12** Role-Based Access Control & Action Mediation — `CRA Annex I Part I (2)(d)` → `SO-D-02.1-002` → `PRIN-ENG-03` → CSF PR.PS-02, ID.RA-01, PR.PS-01 |
| `R2.3` | Monitor workspace activity and operational metrics | Could | **NFR-RN22** Purpose Limitation & Activity Metrics Segregation — `GDPR Art. 5(1)(b) + Art. 6(4)` → `PO-D-05.1-001` → `PRIN-ENG-03` → CSF GV.OC-03, PR.DS-10 / PF CM.PO-P2 |
| `R3.1` | Create and configure projects | Must | **NFR-RN9** Multi-Tenant Data Isolation & Mediation — `CRA Annex I Part I (2)(d)` → `SO-D-02.1-002` → `PRIN-ENG-03` → CSF PR.PS-02, PR.PS-01, ID.RA-01 |
| `R3.2` | Archive completed projects | Should | — |
| `R4.1` | Create and assign tasks | Must | — |
| `R4.2` | Track and transition task workflow states on visual boards | Must | — |
| `R4.3` | Configure recurring automated tasks | Could | — |
| `R5.1` | Manage task deliverable attachments | Must | **NFR-RN13** File Upload Strict Validation & Content Isolation — `CRA Annex I Part I (2)(j)` → `SO-D-07.1-002` → `PRIN-ENG-02` → CSF PR.PS-06, PR.PS-01<br>**NFR-RN25** Automated Orphan File Asset Cleanup & Expiration — `GDPR Art. 5(1)(e)` → `PO-D-05.2-001` → `PRIN-ENG-07` → CSF PR.DS-10, ID.AM-03 / PF CT.DM-P3 |
| `R5.2` | Post in-task discussion comments and mention collaborators | Must | **NFR-RN14** Untrusted Content Neutralization — `CRA Annex I Part I (2)(l)` → `SO-D-07.1-002` → `PRIN-ENG-04` → CSF PR.PS-06 |
| `R6.1` | Consult chronological audit history on task cards | Must | **NFR-RN22** Purpose Limitation & Activity Metrics Segregation — `GDPR Art. 5(1)(b) + Art. 6(4)` → `PO-D-05.1-001` → `PRIN-ENG-03` → CSF GV.OC-03, PR.DS-10 / PF CM.PO-P2 |
| `R6.2` | Receive workspace alerts and daily task digests | Should | **NFR-RN16** Cryptographic Webhook Origin Verification — `CRA Annex I Part I (2)(l)` → `SO-D-05.1-002, SO-D-08.1-002` → `PRIN-ENG-01` → CSF PR.DS-10, ID.AM-03, PR.AT-01 |
| `R7.1` | Subscribe and manage workspace commercial plans | Must | **NFR-RN15** Cryptographic Billing Invariant Protection — `CRA Annex I Part I (2)(l)` → `SO-D-01.1-002, SO-D-08.1-002` → `PRIN-ENG-01` → CSF PR.DS-01, PR.AT-01 |
| `R7.2` | Enforce operational grace period upon payment failure | Must | **NFR-RN15** Cryptographic Billing Invariant Protection — `CRA Annex I Part I (2)(l)` → `SO-D-01.1-002, SO-D-08.1-002` → `PRIN-ENG-01` → CSF PR.DS-01, PR.AT-01 |
| `R8.1` | Export personal and workspace data archives | Must | **NFR-RN20** Structured Personal Data Portability & Export — `GDPR Art. 20 + Art. 15(3) + Art. 12(3)` → `PO-D-05.4-001` → `PRIN-ENG-06` → CSF PR.DS-10 / PF CT.DM-P1 |
| `R8.2` | Close user accounts and terminate workspace access | Must | **NFR-RN21** Irreversible Data Subject Erasure & Pseudonymization — `GDPR Art. 17 + Art. 28(3)(g)` → `PO-D-05.3-001` → `PRIN-ENG-07` → CSF PR.DS-10 / PF CT.DM-P1 |

## §3 NFR Catalogue (RN1–RN26)

| RN | Name | Kind | Where it lives |
|---|---|---|---|
| `RN1` | Page load under 500 ms on boards/lists with up to 200 items | Operational | Quality Attributes table (standalone) |
| `RN2` | Monthly availability at least 99.5% excluding announced maintenance | Operational | Quality Attributes table (standalone) |
| `RN3` | Responsive interface down to 375 px viewport | Operational | Quality Attributes table (standalone) |
| `RN4` | Storage scales to 50,000 active tasks per workspace without degradation | Operational | Quality Attributes table (standalone) |
| `RN5` | Daily automated backups with RPO under 24 hours | Operational | Quality Attributes table (standalone) |
| `RN6` | Interface localized in English and Portuguese | Operational | Quality Attributes table (standalone) |
| `RN7` | Payment gateway communication over authenticated channels with webhook signature verification | Operational | Quality Attributes table (standalone) |
| `RN8` | Strict logical data segregation across workspaces (multi-tenancy) | Operational | Quality Attributes table (standalone) |
| `RN17` | Inbound API Token Mediation & Rate Limiting | Security — cross-cutting | Quality Attributes table (standalone, full tracing chain in row) |
| `RN18` | Non-Repudiable Security Audit Logging | Security — cross-cutting | Quality Attributes table (standalone, full tracing chain in row) |
| `RN24` | Cryptographic Protection of Data in Transit | Security — cross-cutting | Quality Attributes table (standalone, full tracing chain in row) |
| `RN10` | Credential Confidentiality Protection (State of the Art) | Security/Privacy | Absorbed in `R1.1`, `R1.3` cards |
| `RN11` | Session Management & Invalidation | Security/Privacy | Absorbed in `R1.1`, `R1.3` cards |
| `RN19` | Registration Data Minimization by Default | Security/Privacy | Absorbed in `R1.1` card |
| `RN23` | Personal Data Cryptographic Protection at Rest | Security/Privacy | Absorbed in `R1.2` card |
| `RN26` | Privacy Audit Trail for Personal Data Modifications | Security/Privacy | Absorbed in `R1.2` card |
| `RN9` | Multi-Tenant Data Isolation & Mediation | Security/Privacy | Absorbed in `R2.1` card |
| `RN12` | Role-Based Access Control & Action Mediation | Security/Privacy | Absorbed in `R2.2` card |
| `RN22` | Purpose Limitation & Activity Metrics Segregation | Security/Privacy | Absorbed in `R2.3` card |
| `RN9` | Multi-Tenant Data Isolation & Mediation | Security/Privacy | Absorbed in `R3.1` card |
| `RN13` | File Upload Strict Validation & Content Isolation | Security/Privacy | Absorbed in `R5.1` card |
| `RN25` | Automated Orphan File Asset Cleanup & Expiration | Security/Privacy | Absorbed in `R5.1` card |
| `RN14` | Untrusted Content Neutralization | Security/Privacy | Absorbed in `R5.2` card |
| `RN22` | Purpose Limitation & Activity Metrics Segregation | Security/Privacy | Absorbed in `R6.1` card |
| `RN15` | Cryptographic Billing Invariant Protection | Security/Privacy | Absorbed in `R7.1` card |
| `RN15` | Cryptographic Billing Invariant Protection | Security/Privacy | Absorbed in `R7.2` card |
| `RN20` | Structured Personal Data Portability & Export | Security/Privacy | Absorbed in `R8.1` card |
| `RN21` | Irreversible Data Subject Erasure & Pseudonymization | Security/Privacy | Absorbed in `R8.2` card |

## §4 Use Case ↔ NFR Coverage ({U.C. 1.1}–{U.C. 8.2})

| UC | Bound R | NFR-RN |
|---|---|---|
| `{U.C. 1.1}` | `R1.1` | NFR-RN10, NFR-RN11, NFR-RN19 |
| `{U.C. 1.2}` | `R1.2` | NFR-RN23, NFR-RN26 |
| `{U.C. 1.3}` | `R1.3` | NFR-RN10, NFR-RN11 |
| `{U.C. 2.1}` | `R2.1` | NFR-RN9 |
| `{U.C. 2.2}` | `R2.2` | NFR-RN12 |
| `{U.C. 2.3}` | `R2.3` | NFR-RN22 |
| `{U.C. 3.1}` | `R3.1` | NFR-RN9 |
| `{U.C. 3.2}` | `R3.2` | — |
| `{U.C. 4.1}` | `R4.1` | — |
| `{U.C. 4.2}` | `R4.2` | — |
| `{U.C. 4.3}` | `R4.3` | — |
| `{U.C. 5.1}` | `R5.1` | NFR-RN13, NFR-RN25 |
| `{U.C. 5.2}` | `R5.2` | NFR-RN14 |
| `{U.C. 6.1}` | `R6.1` | NFR-RN22 |
| `{U.C. 6.2}` | `R6.2` | NFR-RN16 |
| `{U.C. 7.1}` | `R7.1` | NFR-RN15 |
| `{U.C. 7.2}` | `R7.2` | NFR-RN15 |
| `{U.C. 8.1}` | `R8.1` | NFR-RN20 |
| `{U.C. 8.2}` | `R8.2` | NFR-RN21 |

## §5 Coverage Totals

| Surface | Count | Notes |
|---|---|---|
| Functional requirements | 19 | 15 MUST / 2 SHOULD / 2 COULD (18 elicited + derived `R1.3`). |
| NFRs total | 26 | 8 operational + 3 cross-cutting security (standalone) + 15 absorbed in R cards. |
| Cards with absorbed NFRs | 15 | 1–3 NFRs each; 4 elicited cards have no security surface (R3.2, R4.1, R4.2, R4.3). |
| NFRs without home | 0 | Every NFR is either absorbed (with chain) or standalone (with chain). |
| Functional evolution (V0→V1) | 4 entries | 1×D1, 2×D2, 1×D3 + evaluated-no-change rows — see §6 and STEP5 register; V0 untouched. |

## §6 Functional Evolution Register (V0 → V1, Step 4b)

Full register with rationale and evaluated-no-change rows: [`STEP5_FUNCTIONAL_EVOLUTION_REGISTER.md`](STEP5_FUNCTIONAL_EVOLUTION_REGISTER.md).

| # | Type | Change | Driving obligation |
|---|---|---|---|
| CH-01 | D1 — Derived requirement | New `R1.3` Recover access to a locked user account (+ `PUC 1.3`, `{U.C. 1.3}`) | NFR-RN10, NFR-RN11 (lockout in `{U.C. 1.1}` ext. 5c) |
| CH-02 | D2 — Description refinement | `R8.2`: final personal data export offered before irreversible erasure (+ `{U.C. 8.2}` step 3 / ext. 3a) | NFR-RN21 (Art. 17), NFR-RN20 (Art. 20) |
| CH-03 | D2 — Description refinement | `R7.2`: post-grace restricted state defined (read-only consultation + export preserved; modifications + invitations suspended) | NFR-RN15 + PRIN-ENG-04 |
| CH-04 | D3 — Priority re-evaluation | `R1.2` Should → Must | GDPR Art. 5(1)(d) + Art. 16 via `PO-D-01.4-001` |

