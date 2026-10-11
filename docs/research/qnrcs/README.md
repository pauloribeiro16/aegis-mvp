# QNRCS — Quadro Nacional de Referência de Cibersegurança (extracção)

Fonte: dashboard construído pelo investigador (`Methodology_compact` no GitHub,
`00_METHODOLOGY/00_VISUALISATIONS/QNRCS/QNRCS_Reg756_2026_Dashboard.html`).
Extraído para JSON a 2026-10-11 e verificado: 6 objectivos, 22 categorias, 107 controlos.

- **Fonte legal:** Regulamento n.º 756/2026 — DR 2.ª série n.º 118, 22-06-2026 — base: DL 125/2025 (RJC) — transposição NIS 2
- **Estrutura:** objectivos (ID/GR/PR/DE/RS/RC) → categorias → controlos, com
  medidas escalonadas por tipo de entidade (básico/substancial/elevado) e matriz
  de risco com limiares de conformidade.
- **Estado:** material de trabalho — NÃO é referencial citável em cadeias até ser
  acrescentado como consultivo em `baseline/CONTROLS/QNRCS/` (decisão do
  investigador; o baseline está congelado e protegido).
- **Encaixe natural:** o nível "básico" das medidas é a forma proporcional
  nacional para uma entidade de 8 pessoas — candidato ao anexo de boas práticas
  não vinculativas do Doc03 e a âncoras dos deveres organizacionais de
  governança (D-09).


## Verificação contra a fonte primária (2026-10-11)

O extract foi conferido contra o texto publicado no Diário da República
(Regulamento n.º 756/2026, `diariodarepublica.pt/dr/detalhe/regulamento/756-2026-1134399056`,
252 343 caracteres renderizados — o sítio é uma app cliente, o texto não vem em
`curl`).

**Medidas por tier — coincidência exacta, conjunto a conjunto:**

| Tier | ANEXO III | extract | diferença |
|---|---|---|---|
| Básico | 43 | 43 | 0 ids |
| Substancial | 59 | 59 | 0 ids |
| Elevado | 51 | 51 | 0 ids |

Consequência directa: **o DE.AE-1 não tem medida básica** — a tabela do Básico
do ANEXO III não o lista. Não é lacuna da extracção.

**Estrutura do regulamento (o que a extracção tem de apanhar):** a secção 7.x
lista os controlos com **Descrição** + **Referências**; o **ANEXO III** lista,
por tier, uma tabela de *Controlo de Cibersegurança · Medida de Cibersegurança ·
Critério de Verificação*. São dois sítios diferentes — a medida de um tier não
está junto do controlo.

**Os 107 controlos estão todos definidos na secção 7.x** — a verificação
inicial deu os dois por faltantes, e estava errada: os ids aparecem com
variações de formatação que um leitor por expressão regular apanha mal.

| variante | exemplo |
|---|---|
| espaço-hífen-espaço | `DE.AE-1 - Os eventos…` |
| sem espaço antes do hífen | `ID.MC-1- As melhorias…` · `PR.GA-4- As afirmações…` |
| espaço depois do ponto | `GR. SP-1 - Os resultados…` · `GR. SP-2 - A estratégia…` |

Um leitor que exija `XX.YY-N - ` choca com as duas últimas variantes e reporta
falsos controlos em falta — foi o que aconteceu na primeira comparação, e é o
mesmo defeito que a extracção original já tinha registado nas suas `warnings`.
A lição fica: **quando um verificador acusa a fonte, confirmar a acusação com
os olhos antes de a publicar** — a segunda vez que um padrão de id derruba uma
conclusão.

`GR.SP-1` e `GR.SP-2` não são referências penduradas: têm descrição e, no
caso de `GR.SP-2`, medida de nível elevado.
