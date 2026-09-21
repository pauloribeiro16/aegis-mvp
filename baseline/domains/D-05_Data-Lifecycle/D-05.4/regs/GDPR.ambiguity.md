# D-05.4 — Relevant Ambiguity (GDPR)

> Part 4 ambiguity analysis for GDPR, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## GDPR
##### Art. 15(1) — Access content
**Clause: GDPR-RT09** | type: data subject right (access) | obligatedParty: CONTROLLER | obligationType: PER-REQUEST
**Berry anchor:** §5.4.7 (8-element list), §5.1.
**Instance 1 — COORD+VAG / S3 / `(h) meaningful information about the logic involved`**
Same as Art. 13(2)(f) — partial repetition; the ADM-logic disclosure question is central here.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Logic = categories of input and decision tree structure. | EDPB Guidelines on ADM. |
| R2 | Logic = model weights and training procedure. | Strict reading. |
R1 vs R2 yield materially distinct explainability engineering scope.
---
##### Art. 15(3) — Copy provision and format
**Clause: GDPR-RT10** | type: data subject right (copy) | obligatedParty: CONTROLLER | obligationType: PER-REQUEST
**Berry anchor:** §5.1 (`commonly used electronic form`), §5.1 (`reasonable fee`).
**Instance 1 — VAG / S3 / `commonly used electronic form`**
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Common form = structured interoperable format (JSON, CSV, XML). | EDPB Guidelines on data portability 06/2020. |
| R2 | Common form = whatever the data subject requests. | Industry reading. |
| R3 | Common form = PDF or printable document. | Loose reading. |
R1 vs R3 yield materially distinct data-export engineering.
---

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/GDPR.ambiguity.md

`commonly used` is undefined (cf. CRA Art. 13(c) on SBOM — same open-list pattern). Common for whom — data subject, sector, jurisdiction?

<!-- aegis:purity: own_reg=GDPR; demoted=1; core_cross_mentions=0 -->

