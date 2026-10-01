# RUN_NOTES — run_case01v2_1963538

## Run meta

| Field | Value |
|---|---|
| Case | Case_01_TinyTask_SaaS |
| Model | qwen3.8:27b |
| LLM calls (trace.jsonl) | 30 |
| Fichas | p1=PROM-P1-01 v1.0.0, p2=PROM-P1-02 v1.0.0, p3=PROM-P1-03 v1.0.0, p4=PROM-P1-04 v1.1.0, p5=PROM-P1-05 v1.0.0 |
| Deliverable | phase1_output.md (DRAFT) |

## SPEC §8 evidence

| # | Item | How verified | Result |
|---|---|---|---|
| 1 | Input contract (5 sections) | validated at P1 (L0 stop condition) | PASS |
| 2 | §2 covers every input §5 regulation | validate.py item 2 | run locally post-sync |
| 3 | §3 codes exist in corpus | validate.py item 3 | run locally post-sync |
| 4 | AG IDs unique, match §3 | validate.py item 4 | run locally post-sync |
| 5 | Regulatory sources resolve (R2a) | validate.py item 5 | run locally post-sync |
| 6 | Control anchors resolve (R2b) | validate.py item 6 | run locally post-sync |
| 7 | No statement without input trace | L0 parsers + gate review | human check |
| 8 | Frontmatter complete; DRAFT | assembly (deterministic) | PASS (DRAFT until G-P1-D) |
| 9 | Pattern/property/parent/adjustment | validate.py item 9 | run locally post-sync |
| 10 | Document hygiene (R11/R12) | validate.py R12-hygiene + doc_lint scope note | run locally post-sync |

## Human gates

| Gate | State | Note |
|---|---|---|
| G-P1-A | approved | reviewer note: Fact sheet approved: faithful to generalized input (business cust |
| G-P1-B | approved | reviewer note: All 5 verdicts confirmed: GDPR+CRA apply; NIS2/DORA/AI_Act do not |
| G-P1-C | approved | reviewer note: 22 sub-domains approved (completeness over 4-10 signal; below Doc |
