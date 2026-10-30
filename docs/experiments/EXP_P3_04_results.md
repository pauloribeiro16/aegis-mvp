---
prereg: PREREG_P3_04.md
prereg_version: 1.2.0
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

## A revisão estrutural (job 2166542): medida INERTE, com diagnóstico

A guarda de reparo L0 foi implementada (Adenda 1.1.0) e medida no job
2166542: routing **bit-idêntico** ao run sem guarda (68%; D-05 4/7; D-07 4/5)
e **zero re-pedidas L0** na trace — a guarda nunca disparou. Duas causas,
ambas medidas:

1. **Granularidade.** A chamada de veredicto é por **sub-domínio**
   (`verdicts_D-07_1.json` tem 2 linhas, `_2` tem 1); o colapso é um padrão
   de **domínio** (D-07 é 4/5 across D-07.1..4). A guarda via 1–2 linhas e
   o seu mínimo de 3 nunca era atingido.
2. **Limiar.** 65% ficava **acima** do D-05 colapsado (57%) — nunca o
   desafiava.

As duas correcções (a guarda passa a ver o domínio; limiar novo de 40% com
base medida nos seis braços — ver M-27 e a Adenda 1.2.0 do PREREG_P3_04) vão
para a terceira e última tentativa sobre este instrumento: se o routing não
mover, a conclusão é que o encaminhamento é um **juízo prévio estável** do
modelo e o instrumento tem de mudar o **procedimento de decisão** (exemplar
no pack, ou routing derivado), não a prosa.

## A terceira tentativa (job 2167313, `run_p304d_qwen38_c1`): A GUARDA MOVE

Com a granularidade por domínio e o limiar de 40% (Adenda 1.2.0), a guarda
**disparou** — a trace regista **3 re-pedidas L0** (D-05.2, D-07.2, D-07.3) —
e o modelo cedeu parcialmente:

| | global `ROUTE_ORG` | D-05 | D-07 | M-26 (D-02..D-07) |
|---|---|---|---|---|
| v1.4.0 (sem guarda) | 68% | 4/7 (57%) | 4/5 (80%) | 68% — **alerta dispara** |
| **C-3 (guarda)** | **62%** | **2/7 (29%)** | **2/5 (40%)** | **58% — alerta cala** |

**H4 (parcialmente suportado).** A predição era "D-05 ≤ 29%, D-07 ≤ 35% e
global ≤ 60%": o **D-05 cumpre o alvo exactamente** (2/7 = 29%), o D-07
melhora de 80% para 40% mas fica acima dos 35%, e o global desce 6 pontos
(68% → 62%) mas mantém-se acima do tecto de 60%. O falsificador do §H4
("D-05 ou D-07 inalterados ⇒ o modelo ignora a instrução") **não dispara**:
ambos mudaram, e mudaram para metade.

**Consequências honestas:**
- A guarda **funciona**: é a primeira intervenção em três tentativas que move
  o encaminhamento. A lição das tentativas anteriores — a prosa não move um
  juízo prévio — fica confirmada: o que moveu foi um desafio **mecânico e
  específico**, ao nível onde a decisão é tomada (o domínio).
- O mecanismo é visível na trace: a guarda disparou nos sub-domínios onde o
  domínio colapsava, e o modelo re-evaluou.
- O M-26 (o alerta registado) **passa a calar** neste braço.
- O que fica: 2 pontos no global e 5 pontos no D-07. A guarda dispara **uma
  vez por sub-domínio** e o modelo cede onde cede; fechar o resto exige
  uma segunda ronda de desafio (ou um limiar por domínio, com base no
  gabarito) — é a decisão seguinte, e é do investigador.

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
