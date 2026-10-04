---
document_id: AEGIS-MVP-ASSUMPTIONS
title: 'Assumption register — load-bearing assumptions with signposts'
version: 1.0.0
created: 2026-10-04
status: ACTIVE
upstream: 'AGENTS.md §-2 (rule 5), AEGIS-RES-10 §1 SM-008'
---

# Assumption register — load-bearing assumptions with signposts

**What this is.** The register §-2 (rule 5) requires, on the RAND
Assumption-Based Planning pattern: a load-bearing assumption is not managed
until it has a pre-agreed **signpost** — a warning condition that, when it
fires, reopens the decision the assumption supports. A signpost firing means
the assumption is *revisited*, never silently defended.

**Maintenance rule.** Every entry carries its origin (where the assumption is
already written today). New load-bearing assumptions enter here in the same
session they are made. When a signpost fires: flip `Estado` to `DISPARADO`,
record the date and the follow-up in the same row, and open the contingency.

| ID | Pressuposto | Onde vive hoje | Sinal (signpost) | Contingência | Estado |
|---|---|---|---|---|---|
| A1 | **Um caso só** (Case_01 TinyTask) — nenhum resultado generaliza para outro perfil de empresa | PREREG_01 limitação 1; PREREG_02 limitação 1 | Case_02/Case_03 entrarem no programa experimental | Re-correr EXP-05b/c (coverage/equivalence) nos novos casos antes de qualquer alegação transferida | ABERTO |
| A2 | **Um modelo só** (qwen3.8:27b num A100) — os números do piso de ruído são do modelo+stack | PREREG_01 limitação 2 | Um novo model matrix arrancar (M01/M02) | Re-correr os preregistos activos sob o novo modelo; comparar pisos | ABERTO |
| A3 | **Um rater só** (rubrica L2, o investigador) — sem inter-rater reliability; intra-rater test-retest substitui | PREREG_01 limitação 3; L2_RUBRIC.md | Um 2.º humano disponível para scoring | Correr κ inter-rater sobre a mesma tuple set; até lá, E-04 (validador determinístico vs judge) | ABERTO |
| A4 | **Determinismo do juiz L3 não provado** — o piso de ruído do judge nunca foi medido neste conteúdo | PREREG_02 E-17; AEGIS-RES-09 §4.1 | E-17 correr (auditoria de temperature/seed + re-judging) | Declarar o piso no METRICS.md; gatear todo A/B judged nesse piso | ABERTO |
| A5 | **O corpus congelado é ground truth** — a verdade normativa vive no baseline verbatim | SPEC §2/§3; R5/R6 | Qualquer mutação do baseline (modularização, admissão K2/K3, ADR-001) | Re-correr `scripts/verify_no_loss.py` + EXP-05b (coverage 100%) antes de novos resultados | ABERTO |
| A6 | **ADR-011 D2** — schema desenhado, grafo materializado "on demand"; os packs servem as perguntas das Fases 1–3 | ADR-2026-10-01_knowledge-representation.md D2/D4 | E-13 dispara (T6 / pergunta relacional que os packs não respondem) | Materializar o grafo (builder determinístico) e revisitar a ADR — revê-se, não se defende | ABERTO |
| A7 | **O forward pass do juiz não-determinístico não é alcançável por seed** — mesmo temperature=0 + greedy deixa items a inverter [S-241] | AEGIS-RES-09 §4.1; PREREG_02 E-17 caveat | Um provider retirar o parâmetro temperature (Claude Opus 4.7/4.8 já rejeita, HTTP 400) | Re-medir o piso do judge com o protocolo E-17; nenhum A/B judged sem piso válido | ABERTO |

## Convention note (A6, in prose for precision)

A6 é a única linha que aponta para uma decisão em vez de um pressuposto de
fundo — mantém-se aqui porque o sinal dela (E-13) é o mesmo mecanismo: o
ADR-011 adiou a materialização sem critério de conclusão, e E-13 é esse
critério. Se E-13 correr e responder à dívida T6 sem dor relacional nova, o
estado passa a `FECHADO — materialização não justificada (data)`; se houver
dor, `DISPARADO`.
