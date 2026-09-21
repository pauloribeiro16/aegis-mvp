# D-04.3 — Relevant Ambiguity (AI Act)

> Part 4 ambiguity analysis for AI Act, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## AI_Act
#### 2.26 AIA-C26 — Art. 73(1)-(4) Serious incident reporting
**Source loci:** Art. 73(1) `report any serious incident`; Art. 73(2) `not later than 15 days after … becomes aware`; Art. 73(3) `not later than two days` (widespread infringement); Art. 73(4) `not later than 10 days` (death).
* **VAG — S3** — `serious incident` — defined in Art. 3(49) via three sub-categories (a)/(b)/(c) with distinct triggers. The three sub-categories use different severity thresholds without specifying their interaction.
* **POLY — S2** — `reasonable likelihood of a causal link` (Art. 73(2)) — distinct from `established causal link`; the two thresholds trigger the same 15-day clock.
* **COORD — S3** — Four differentiated timelines (immediate / 15 days / 10 days / 2 days) AND-coordinated with four distinct triggers (causal link / awareness / death / widespread infringement). Berry §5.7: the cross-product admits ≥16 distinct reporting-obligation shapes.
**Berry anchor:** §5.1 (`serious`, `reasonable likelihood`), §5.7 (4-timeline coordination), §3.3.1 (`serious incident`).
#### 2.29 AIA-C29 — Art. 55(1)(c) GPAI serious incident reporting
**Source locus:** `keep track of, document, and report, without undue delay, to the AI Office and, as appropriate, to national competent authorities, relevant information about serious incidents and possible corrective measures to address them`.
* **VAG — S3** — `without undue delay`, `relevant information`, `as appropriate`.
* **POLY — S3** — `serious incidents` for GPAI models — distinct from `serious incidents` for high-risk AI systems (Art. 73) but the cross-reference is implicit. The boundary (when does a GPAI incident trigger Art. 55 reporting vs. Art. 73 reporting vs. both?) is undefined.
* **COORD — S2** — `keep track of, document, AND report` (3-way verb AND); `serious incidents AND possible corrective measures` (AND).
**Berry anchor:** §5.1 (`undue`, `relevant`, `as appropriate`), §3.3.1 (`serious incidents` cross-article polysemy).
---
### 3. Synthesis

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/AI_Act.ambiguity.md

* **SCOPE-Q — S3** — `becomes aware of the serious incident` — same awareness-trigger ambiguity as GDPR/CRA/NIS 2/DORA. Compounded here by the multi-timeline structure.

<!-- aegis:purity: own_reg=AI_Act; demoted=1; core_cross_mentions=0 -->

