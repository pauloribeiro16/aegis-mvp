---
document_id: AEGIS-MVP-ASSUMPTIONS
title: 'Assumption register — load-bearing assumptions with signposts'
version: 1.2.0
created: 2026-10-04
updated: 2026-10-09
status: ACTIVE
upstream: 'AGENTS.md §-2 (rule 5), AEGIS-RES-10 §1 SM-008, ADR-2026-10-05_pack-budget-and-context-policy'
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
| A1 | **Um caso só** (Case_01 TinyTask) — nenhum resultado generaliza para outro perfil de empresa | PREREG_01 limitação 1; PREREG_02 limitação 1 | Case_02/Case_03 entrarem no programa experimental | Re-correr EXP-05b/c (coverage/equivalence) nos novos casos antes de qualquer alegação transferida | **DISPARADO — 2026-10-05** (ver nota A1 abaixo) |
| A2 | **Um modelo só** (qwen3.8:27b num A100) — os números do piso de ruído são do modelo+stack | PREREG_01 limitação 2 | Um novo model matrix arrancar (M01/M02) | Re-correr os preregistos activos sob o novo modelo; comparar pisos | **DISPARADO — 2026-10-05** (ver nota A2 abaixo) |
| A3 | **Um rater só** (rubrica L2, o investigador) — sem inter-rater reliability; intra-rater test-retest substitui | PREREG_01 limitação 3; L2_RUBRIC.md | Um 2.º humano disponível para scoring | Correr κ inter-rater sobre a mesma tuple set; até lá, E-04 (validador determinístico vs judge) | ABERTO |
| A4 | **Determinismo do juiz L3 não provado** — o piso de ruído do judge nunca foi medido neste conteúdo | PREREG_02 E-17; AEGIS-RES-09 §4.1 | E-17 correr (auditoria de temperature/seed + re-judging) | Declarar o piso no METRICS.md; gatear todo A/B judged nesse piso | **FECHADO — 2026-10-05, contingência CADUCADA** (ver nota A4 abaixo) |
| A5 | **O corpus congelado é ground truth** — a verdade normativa vive no baseline verbatim | SPEC §2/§3; R5/R6 | Qualquer mutação do baseline (modularização, admissão K2/K3, ADR-001) | Re-correr `scripts/verify_no_loss.py` + EXP-05b (coverage 100%) antes de novos resultados | ABERTO |
| A6 | **ADR-011 D2** — schema desenhado, grafo materializado "on demand"; os packs servem as perguntas das Fases 1–3 | ADR-2026-10-01_knowledge-representation.md D2/D4 | E-13 dispara (T6 / pergunta relacional que os packs não respondem) | Materializar o grafo (builder determinístico) e revisitar a ADR — revê-se, não se defende | ABERTO |
| A7 | **O forward pass do juiz não-determinístico não é alcançável por seed** — mesmo temperature=0 + greedy deixa items a inverter [S-241] | AEGIS-RES-09 §4.1; PREREG_02 E-17 caveat | Um provider retirar o parâmetro temperature (Claude Opus 4.7/4.8 já rejeita, HTTP 400) | Re-medir o piso do judge com o protocolo E-17; nenhum A/B judged sem piso válido | **FECHADO — 2026-10-05, contingência CADUCADA** (ver nota A7 abaixo) |
| A8 | **O orçamento de contexto é uma restrição, não uma conveniência** — a escada de `num_ctx` existe porque os packs precisam de mais do que cabe, e por isso valeria a pena subi-la | ADR-2026-10-05_pack-budget-and-context-policy.md §1.1–§1.3, D1/D6 | (a) E-15 achar retenção da cadeia **igual** nos orçamentos current / 0.75× / 0.5× — o orçamento nunca foi a restrição; **ou** (b) um pack real ultrapassar 50 k tokens de prompt depois de D1; **ou** (c) uma célula `context-fail` registada (`PLANO_FECHO.md:124`) persistir depois de D1 | E-15 corre (0 GPU-h, já preregistrado); se (a) sem (b)/(c), o contexto sai da lista de restrições e a energia vai para onde os abortos estão de facto — as L0 quality gates | ABERTO |
| A9 | **A F2 não emite o tail `RULE-*` porque nenhum artefacto do corpus define a linha RULE** (colunas, derivação de âncoras, método de verificação) — a omissão nos 3 casos manuais é evidência de forma indeterminada, não de um artefacto forgotten | ADR-2026-10-09_phase2-objective-bridge.md D1; ledger §1 finding 2, §4.1 | (a) um schema de linha RULE ser definido na metodologia; **ou** (b) a F3 declarar que não consegue citar um artefacto de nível regra; **ou** (c) a restrição Doc02 gerada para uma 4.ª empresa estruturalmente diferente sair genérica | Definir a linha RULE e re-emitir Doc01; revê-se a decisão, não se defende | ABERTO |

## Notes on the state changes (2026-10-05)

**A1 — DISPARADO.** O sinal era "Case_02/Case_03 entrarem no programa
experimental" e os três casos estão no programa: a matriz M02 está fechada em
6 modelos × 3 casos com todas as células resolvidas (`00_RESULTS.md` §M02,
commit `7289d7f`). **Seguimento, e o que falta dele:** a contingência foi
cumprida **para o Case 01** — EXP-05b mediu cobertura 100 % (570/570 ids de
selecção, 1,350/1,350 citações de artigo) e 86,4 % de utilização em 15 runs
`arm-B`. **Não** foi cumprida para o Case 02 nem para o Case 03: não existe
medição de cobertura/utilização de pack nesses dois casos, e o que existe para
eles é a matriz M02 (retenção por célula), que é um resultado diferente. A
linha fica `DISPARADO` com a lacuna escrita, não `FECHADO`. O pressuposto
**também não se torna verdadeiro** por o sinal ter disparado: há três perfis de
empresa, não uma população, e é assim que fica escrito.

**A2 — DISPARADO.** O sinal era "um novo model matrix arrancar (M01/M02)" e
M01 e M02 correram. **Seguimento:** os pisos de ruído por modelo estão em
`docs/experiments/PLANO_FECHO.md` e as células em `aegis-models/MODELS.yaml` +
`results/*.tsv`; o que a contingência exige — re-correr os preregistos activos
sob cada modelo novo antes de comparar pisos — foi feito para EXP-02 (a
amostra de reprodutibilidade) mas **não** para o resto. A linha fica
`DISPARADO`, não `FECHADO`: os números do pipeline são de agora multi-modelo e
qualquer piso herdado de qwen3.8 tem de ser lido como piso *desse* modelo.

**A4 e A7 — FECHADOS por contingência caducada, não por refutação.** Ambas as
contingências apontam para **E-17**, que está **CADUCADO**: não há juiz L3 em
`pipeline/src` para auditar — a camada foi despromovida a L1 determinístico + L2
(`docs/experiments/PLANO_FECHO.md:94`). Não há piso para medir e não há A/B
judged a gatear, porque o instrumento que os produziria não existe no pipeline
actual. Isto **não** é evidência contra [S-241] nem contra o pressuposto de A7:
é uma mudança de instrumento, não uma resposta ao pressuposto. Se um juiz L3
for reposto, ambas reabrem com o sinal original e o texto de E-17 reposto
como item de backlog.

**A8 — nova.** É o pressuposto load-bearing desta ADR e o primeiro que se
registra **antes** da mudança de código que o pressupõe (ADR-012 D1/D6), não
depois. A anchor é a medição, não a intenção: o maior prompt já enviado é de
**50,054 tokens reais**, o rung 65,536 absorveu o p4t aos 46,978
(`run_sec03_p1_1979371`, job 1979371), e os abortos actuais do Case 03 são
falhas L0 a 19,659–29,808 tokens de prompt com `done_reason=stop`
(ADR-012 §1.7) — ou seja, o sinal (a) já tem o seu primeiro candidato em dados
que ninguém tinha lido como sendo sobre contexto.


## Convention note (A6, in prose for precision)

A6 é a única linha que aponta para uma decisão em vez de um pressuposto de
fundo — mantém-se aqui porque o sinal dela (E-13) é o mesmo mecanismo: o
ADR-011 adiou a materialização sem critério de conclusão, e E-13 é esse
critério. Se E-13 correr e responder à dívida T6 sem dor relacional nova, o
estado passa a `FECHADO — materialização não justificada (data)`; se houver
dor, `DISPARADO`.
