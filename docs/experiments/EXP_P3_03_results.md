---
prereg: PREREG_P3_03.md
prereg_version: 1.0.0
status: H1 SUPPORTED · H2 SUPPORTED · H3 FALSIFIER FIRED · H4 holds structurally · H5 SUPPORTED — a Parte 2 corre nas duas armas; o registo fica PROPOSED até a ronda humana assinar
---

# EXP_P3_03 results — a Parte 1 da Onda E: ameaças, árvores e o registo que não fecha sem pessoas

Prereg: [PREREG_P3_03.md](PREREG_P3_03.md) **v1.0.0** (congelado 2026-10-27,
antes do primeiro `p3b_all`).

## O que correu

Dois braços sobre pacotes Parte 1 CONCLUDED (o `p3b_all` recusa o contrário —
two-states):

- **`run_p302_muse_c1`** (muse-glimmer:30b, Case 01): 21 ameaças (16 STRIDE +
  5 LINDDUN), 13 árvores Critical/High, registo PROPOSED. Gate G8–G12 CLOSED,
  G7 OPEN (as 21 assinaturas humanas).
- **`run_p302_qwen38_c1`** (qwen3.8:27b, Case 01): 31 ameaças (só STRIDE), 17
  árvores, registo PROPOSED. Gate G8–G12 CLOSED, G7 OPEN (31 assinaturas).
  **O LINDDUN deste braço falhou por CONTEÚDO** (L0 recusou duas vezes: o
  modelo citou `SO-D-01.1-001` como mitigador fora do conjunto aceite) — a via
  de privacidade falta no braço e fica registada como diferença real de
  qualidade entre modelos. 1 árvore falhou (`T-STR-013`), registada no stage
  result.

## H1 — L0 à primeira tentativa: SUPPORTED (com a base honesta)

100% das chamadas `p3b_*` que chegaram ao modelo com o ambiente certo passaram
L0 **à primeira tentativa** (muse 30/30, qwen3.8 27/27; zero tentativas de
reparo consumidas); **zero rejeições T8 com o catálogo presente**. O
falsificador formal (>15% de falhas L0 ou qualquer rejeição T8) disparou
APENAS enquanto o ambiente estava errado: o catálogo `baseline/THREATS` nunca
entrou no payload do `sync_up.sh` (job 2168367 — o fallback é um índice VAZIO
que recusa todos os ids, reais inclusive), e as restantes falhas run-level
foram contratos de código nunca antes exercitados (`domain_dir("DF-01")` no
despacho, `.get()` numa lista no renumerador, stores com ids locais pré-
renumeração, árvores com chave velha) — **cada um fixado em código com
commit e teste**; a cascata integral está registada em
[00_RESULTS.md](00_RESULTS.md) §P3-02/P3-04. A leitura de H1: o pack ensina o
contrato (a ficha LINDDUN sem esquema próprio foi o contra-exemplo — v1.2.0
inlineou-o e o mesmo modelo passou à primeira).

## H2 — a aritmética é do código: SUPPORTED

13 ameaças `UNMITIGATED_GAP` nas duas armas; **0** com residual diferente do
inerente. O registo não reduz um risco que nada mitiga.

## H3 — a árvore tem dentes: FALSIFICADOR DISPARADO (leitura honesta)

`residual_floored_by_tree` = **0** nas duas armas. O pré-registo distingue as
duas causas: (a) árvores desonestas, (b) o chão nunca tem nada para levantar.
A medição: **zero residuais "Baixo" em todo o lado** (muse e qwen3.8) e 14/21
árvores do muse com caminho aberto — nenhuma ameaça de caminho aberto tinha
residual Baixo para o chão corrigir. O chão **manteve-se vago** (held
vacuously): nenhum veredicto mudou porque nenhum precisava de mudar. Nota de
instrumento: o muse media o chão sobre árvores introuváveis (drift de ids
pré-renumeração — corrigido em `505ad90`; as árvores foram re-derivadas sob os
ids renumerados no job 2169496). A discriminação fina (o chão deve ALGUMA vez
corrigir? é sinal de honestidade ou de ameaças mal escolhidas?) fica para o
investigador — é decisão de método, não de código.

## H4 — a regra de ouro: mantém-se estrutural

Nenhum gate chegou a CLOSED sem `risk_verdicts.json`: ambos os gates ficaram
`state: PROPOSED` com G7 OPEN sobre as ameaças não assinadas. G9 (estatutário
não mitigado): fechou com 4 (muse) e 2 (qwen3.8) obrigações estatutárias sem
FULL_MITIGATION — registadas no registo para a decisão humana, nunca aceites
em silêncio.

## H5 — reconciliação e catálogo: SUPPORTED

G11 CLOSED nas duas armas depois do renumber-on-carry (`44f78bd`): o registo é
a união STRIDE ∪ LINDDUN e os mitigadores citados são ids reais. G12 CLOSED
(catálogo íntegro, 3315 ids no cluster desde `ee67af2`).

## O que falta para CONCLUDED (e é por desenho)

A ronda humana de risco (G-P3-B): 21 + 31 decisões, uma por ameaça, com nome,
papel, justificação e sinal de revisão — os endpoints do inspector
(`POST /runs/:id/phase3b/verdicts`) assinam pelo browser. Uma recusa reabre a
Parte 1 com a instrução escrita (o loop reverso G10, cuja fechadura já foi
exercida em teste). Só depois o gate fecha, o export Parte 2 aterra em
`output/`, e a comparação entre armas fica completa para a pontuação L2 cega
([`scoring/f3/`](../../scoring/f3/)).

## Armadilha de instrumento registada

O pack do K3 envia id + nome truncado (158k chars ≈ 39,5k tokens) — a
estimativa de tokens do pack mede-se no que o builder ENVIA, não no ficheiro
fonte (o 265 KB era o JSON em disco). A escada de contexto não subiu
(needed 55,7k < num_ctx 65536) e o H1 foi medido nesse pack.
