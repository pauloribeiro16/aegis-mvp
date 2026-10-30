---
prereg: PREREG_P3_04.md
prereg_version: 1.1.0
status: H1 FALSIFIER FIRED · H2 FALSIFIER FIRED · H3 SUPPORTED — a revisão estrutural (adenda v1.1.0) é o próximo passo
---

# EXP_P3_04 results — a revisão da ficha v1.4.0 NÃO moveu o colapso (resultado negativo)

Prereg: [PREREG_P3_04.md](PREREG_P3_04.md) **v1.2.0 → v1.1.0** (a Adenda
1.1.0 desta sessão é a revisão estrutural que este resultado obriga; o
resultado abaixo é o do instrumento v1.4.0, congelado antes da corrida).

Job **2165434**, `run_p304_qwen38_c1`, upstream idêntico ao do braço v1.3.0
(fork limpo: só o upstream fixado, `v0_source=frozen`, seed 42, temp 0.2),
mesmo modelo (qwen3.8:27b), mesmo caso. Control intra-braço: o v1.3.0 do
mesmo braço já medido.

## Run inventory (antes de qualquer veredicto)

| Job | Run | Ficha | Outcome |
|---|---|---|---|
| 2165434 | `run_p304_qwen38_c1` | PROM-P3A-01 v1.4.0 | COMPLETED — 65/65 objectivos com veredicto, 31+13 propostas |

## As três hipóteses

| | Critério (pré-registado) | Medido | Juízo |
|---|---|---|---|
| **H1** | `ROUTE_ORG` global ≤ 60% | **68%** (v1.3.0: 66%) | **FALSIFICADOR DISPARADO** |
| **H2** | D-05 ≤ 29% org (≤2/7) e D-07 ≤ 35% (≤5/15) | D-05 **4/7 (57%)**, D-07 **4/5 (80%)** | **FALSIFICADOR DISPARADO** (idêntico ao v1.3.0) |
| **H3** | L0 1.ª tentativa ≥ 90% e 65/65 objectivos com veredicto | **95% (53/56)**, 65/65 | **SUPORTADA** |

## O que a medição mostra: a extensão de vocabulário não foi o mecanismo

Comparação domínio a domínio entre v1.3.0 e v1.4.0 (mesmo braço, mesma seed,
mesmo upstream — a única diferença é a ficha):

| Domínio | v1.3.0 | v1.4.0 | Gabarito manual (D-01) |
|---|---|---|---|
| D-01 | 2/8 | **2/8** | 0% |
| D-02 | 4/5 | 5/5 | 100% |
| D-03 | 1/8 | 1/8 | 25% |
| D-04 | 6/8 | 6/8 | 75% |
| D-05 | 4/7 | **4/7** | 14% |
| D-06 | 7/7 | 7/7 | 80% |
| D-07 | 4/5 | **4/5** | 20% |
| D-08 | 4/4 | 4/4 | 67% |
| D-09 | 7/7 | 7/7 | 100% |
| D-10 | 4/6 | 4/6 | 83% |

A v1.4.0 não mudou uma única linha de routing nos domínios-alvo (D-05, D-07) e
**piorou o global em 2 pontos** (D-02). Ou seja: **a prosa da regra de
acoplamento não é o mecanismo** — o modelo não reavalia o encaminhamento
porque a lista de produto ficou mais longa; ele tem um juízo prévio sobre que
obrigações são organizacionais, e uma frase mais longa não o move.

Isto cumpre a condição que o próprio pré-registo escrevera
(§H1, falsificador): *"se `ROUTE_ORG` > 60% de novo ⇒ a lacuna NÃO é
vocabulário da regra de acoplamento; a revisão seguinte é estrutural
(exemplar no pack ou guard L0 na coluna Action), não mais uma extensão de
lista"*. A revisão estrutural é a Adenda 1.1.0 do PREREG_P3_04 (guarda de
reparo L0 com âmbito nos domínios onde o gabarito manda produto), congelada
**antes** da re-submissão.

## H3 — o contrato não regride

L0 à 1.ª tentativa 95% (53/56) e 65/65 objectivos com veredicto: a ficha maior
não fragilizou o contrato (o padrão de P3_02 repete-se). Este é o único
resultado positivo da corrida e vale registado — o instrumento está sólido;
o que falha é a *decisão de encaminhamento*, não o formato.

## O que este NÃO reclama

- Não diz que a regra de acoplamento é irrelevante — diz que **prosa** não a
  moveu; um guard mecânico pode (e é o que a Adenda 1.1.0 testa).
- Não generaliza para os outros modelos: o braço é o qwen38/Caso 01 (o único
  com falsificador disparado).
- Não mede a qualidade das propostas (é a ronda e o L2).

## Estado

`run_p302_muse_c1` (muse, 58% — dentro da banda) está a percorrer o ciclo
pós-ronda (Bloco 1.2) em paralelo, com a assinatura mecânica delegada no
handoff do investigador. O ciclo prova que a máquina multi-ronda fecha até
CONCLUDED; a Adenda 1.1.0 testa se um guard L0 fecha a lacuna de
encaminhamento no braço que a disparou.
