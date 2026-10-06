---
document_id: AEGIS-LAB-PREREG-01B
title: 'Pré-registo LAB01b — E-01: saída restringida por schema no p2 (qwen3.5:27b)'
version: 1.0.0
created: 2026-10-05
status: REGISTERED — before any run
upstream: 'lab/README.md · lab/LAB01_PREREG.md §H-L1 · docs/research/04_EXPERIMENT_BACKLOG.md:96-136 (E-01)'
---

# Pré-registo LAB01b — E-01 no lab

## Questão (do backlog E-01, escopado ao p2)

A constrainção da geração no schema elimina a classe de falha de formato L0 no
p2 — e o que custa em latência e qualidade?

## Porquê este braço e não mais texto

O qwen3.5 falha o p2 em 7/7 corridas: emite a **tabela de veredictos perfeita e
sem cerca de código**. Duas formas de instrução diferentes (fence-first ao nível
do carácter; demo de formato) falharam de forma idêntica — o pré-registo
`LAB01_PREREG.md` §H-L1 previa exactamente esta leitura ("se ambos falharem ⇒ é
de capacidade e o caminho é o E-01"). A forma deixa de ser pedida em prosa e passa
a ser imposta no serving layer (`format:` com JSON schema, Ollama 0.32.13); um
conversor determinístico renderiza o artefacto markdown exacto que o `parse_p2`
consome.

## Desenho

| Parcela | Valor |
|---|---|
| Braço | `lab01-qwen35-schema` |
| Modelo | `qwen3.5:27b` |
| Caso | `Case_01_TinyTask_SaaS` (o caso onde a classe é 7/7) |
| Variável isolada | p2: schema-constrained decoding vs. parse-com-repair |
| Restrito a | p2 (p1/p3/p3f/p4/p4t inalterados) — como o backlog define |
| Constantes | gates/parsers/thresholds byte-idênticos (verificado por diff); seed 42, temperature 0.2, n=1 |
| Custo | ~1 GPU-h (a classe morre cedo se falhar) |

## Hipótese, predição, falsificador

**H.** A constrainção no serving elimina a falha de formato L0 no p2.
**Predição:** o p2 passa no **primeiro** attempt (zero repair-retry) e a corrida
avança para o p3.
**Falsificador:** (a) p2 continua a abortar por formato → nem o serving layer
resolve a classe e o qwen3.5 fica de fora até outro serving; (b) p2 passa mas
por repair-retry → o formato melhorou mas o mecanismo não é o que o modelo usa.
**Custo a registar:** latência por chamada e `eval_count` vs. a corrida da M07
(mesmo caso, mesmo modelo, instrução-only) — [S-045] e o caminho llama.cpp
carregam custo por token, é para isso que o backlog pede a medição.

## O que este braço NÃO faz

Não toca a pipeline de produção (regra 1 da constituição). Não altera o prompt
das outras etapas. Não substitui o repair-retry: se o JSON vier inválido, o
`parse_p2` recusa — o conversor não decide, o gate decide.