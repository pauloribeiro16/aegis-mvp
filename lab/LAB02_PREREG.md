---
document_id: AEGIS-LAB-PREREG-02
title: 'Pré-registo LAB02 — decomposição do p4 por cartão Sub-SO (orquestração)'
version: 0.2.0
created: 2026-10-05
status: DRAFT — NÃO SUBMETIDO; bloqueado numa decisão de contrato (ver §Bloqueio)
upstream: 'lab/LAB01_PREREG.md · lab/LAB01B_PREREG.md · docs/experiments/00_RESULTS.md §M07'
---

# Pré-registo LAB02 — p4 por cartão Sub-SO

## Questão

Dar a cada modelo **um cartão Sub-SO de cada vez** (em vez de todos os cartões do
sub-domínio numa só resposta) elimina a classe de sobre-compressão que trava
glm-4.7-flash (20/38) e nemotron-3.5 (31/38) na matriz M07?

O falsificador do LAB01 já apontou para aqui: os dois braços de instrução
deixaram os conjuntos de falha **idênticos** aos da M07 (18/18 e 7/7 de
intersecção). A classe não é de instrução.

## Desenho (proposto)

| Parcela | Valor |
|---|---|
| Braços | `lab02-glm47-cardsplit` · `lab02-nemotron-cardsplit` (e gemma4 como controlo) |
| Caso | `Case_01_TinyTask_SaaS` (2 regulações confirmadas → 1–2 cartões por sub-domínio) |
| Variável isolada | p4: uma chamada por cartão vs. uma chamada por sub-domínio |
| Constantes | gates/parsers/thresholds byte-idênticos; seed 42; n=1 |
| Semântica de falha | conservadora: um cartão que falhe faz falhar o sub-domínio (como hoje) |

## Verificação feita antes de qualquer submissão

- O patch aplica e compila; os blocos guardados (parse_p1/p2/p3/p3f/p4t,
  check_p4_quality, _validate, assemble_doc, store_parsed, thresholds) ficam
  **byte-idênticos** — verificado por diff de blocos, não por promessa.
- O **merge** foi testado isoladamente: renumeração sequencial
  `AG-<sd>-001..N`, ordem canónica das regulações preservada, 9 células por linha,
  assumptions concatenadas. Correcto.

## BLOQUEIO (2026-10-05) — porque este braço não foi submetido

A verificação end-to-end (pipeline completa contra Ollama falso) revelou que a
chave-por-cartão é **uma alteração de contrato no gate, não um detalhe de
implementação**:

- `store_parsed` sanitiza o sub-domínio com `replace(".", "_")`, portanto um
  cartão `D-01.1.GDPR` grava como `D-01_1` — colide com o sub-domínio, e os
  cartões sobrescrevem-se uns aos outros.
- Para evitar a colisão, o `subdomain` teria de chegar card-qualified
  (`D-01.1.GDPR`) — mas `compose.py:227` valida o **sub-domínio canónico** e
  rejeita-o (`not a canonical sub-domain id: D-01.1.GDPR`).

Ou seja: fazer uma chamada por cartão **exige** uma chave de artefacto nova
(`<sd>__<REG>`), o que toca `store_parsed` e a validação de id canónico — dois
locais que são gates. Isso já não é "ajustar a orquestração sem mexer nos
gates"; é mexer nos gates.

## Decisão que o investigador tem de tomar

1. **Uma chave nova para cartões** (ex. `D-01_1__GDPR.json`), com
   `compose.py`/`store_parsed` a aceitarem a forma qualificada **apenas** para o
   p4-per-cartão, mantendo o gate de sub-domínio canónico intacto para o resto. É
   a opção limpa, mas toca dois gates e precisa de review do investigador.
2. **Cartões por sub-domínio, não por ficheiro**: fazer as chamadas por cartão
   mas escrever todas as respostas num único artefacto temporário por
   sub-domínio (sem mudar a chave) — mais simples, sem tocar gates, mas obriga a
   um buffer em memória e perde a rastreabilidade por cartão no disco.
3. **Abandonar a alavanca de orquestração** para estes modelos e aceitar que a
   compressão é um limite de capacidade — registando isso no resultado e
   redirigindo o esforço (E-01 já cobre o qwen3.5; para glm/nemotron resta
   reduzir o tamanho do trabalho por outro caminho).

**Até haver decisão, LAB02 não é submetido.** Isto é o princípio de constitutição
do lab a funcionar: o braço não entra no cluster sem passar pelos guards.