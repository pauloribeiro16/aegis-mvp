---
document_id: AEGIS-EVAL-GUIDE
title: 'Guia de Avaliação — como a pipeline está organizada e o que é um bom resultado em cada parte'
version: 1.1.0
created: 2026-11-02
status: ACTIVE
upstream:
  - AGENTS.md
  - docs/experiments/METRICS.md
  - docs/pipeline/10_PHASE_ORIENTATION.md
  - docs/experiments/L2_RUBRIC.md
  - docs/experiments/L2_RUBRIC_F3.md
---

# Guia de Avaliação

**Para quem é.** Para qualquer pessoa ou agente que chega a este repositório sem
contexto e precisa de responder a uma pergunta: *esta corrida da pipeline deu um
bom resultado, ou não?*

**Como ler.** A secção 1 mostra a pipeline inteira. A secção 2 explica as quatro
perguntas com que se avalia qualquer parte dela. A secção 3 aplica essas quatro
perguntas a cada etapa, fase a fase. A secção 4 diz como se declara o resultado
de uma corrida inteira. A secção 5 é o dicionário: traduz cada código que vais
encontrar no repositório (`G-P1-A`, `M-27`, `T6`, `D3`…) para o seu significado
por extenso.

**Regra de ouro.** *"A etapa terminou sem erro" não quer dizer "a etapa deu um
bom resultado".* Na corrida `run_seqall_1793479203_2173045` (registo P2-03 em
`docs/experiments/00_RESULTS.md`) a Fase 2 terminou com estado `ok` e tinha
falhado 37 de 37 chamadas ao modelo, produzindo zero regras. Um resultado só é
bom quando passa as quatro perguntas da secção 2.

**Onde se vê.** A mesma informação está na página *Pipeline AEGIS* do
inspector (`~/Work/aegis-inspector`, rota `/pipeline`): secção "Como se
avalia", o bloco "Bom resultado desta fase" em cada fase, e "Como se verifica"
em cada cartão de passo (dados em `frontend/src/lib/pipeline-evaluation.ts`).
Quem mudar uma verificação aqui muda-a lá na mesma sessão.

**Onde vivem os números.** Este guia explica e aponta; **não é dono de nenhum
limiar**. O valor oficial de cada limiar, e a base que o justifica, está em
`docs/experiments/METRICS.md` (identificadores `M-nn`) ou no pré-registo da
experiência que o fixou. Se um número aqui divergir dessa fonte, a fonte ganha e
este guia está desatualizado.

---

## 1. A pipeline num relance

A pipeline transforma a descrição de uma empresa em requisitos de segurança e
privacidade, em quatro fases encadeadas. Cada fase consome **apenas** o que a
fase anterior produziu (ADR-004, `AGENTS.md` §6.0).

| Fase | Pergunta que responde | Entra | Sai (unidade de troca) | Formato dos identificadores |
|---|---|---|---|---|
| **Fase 0 — Base metodológica** (congelada, não corre) | O que exige cada lei, em termos neutros? | Texto das leis + análise de ambiguidade | Objetivos de base, por subdomínio e por lei | `SO-D-XX.Y.HL`, `SO-D-XX.Y.<LEI>` |
| **Fase 1 — Definição contextual** | Que leis se aplicam a esta empresa, que áreas são ativadas, e o que cada objetivo de base passa a exigir *desta* empresa? | Descrição da empresa (`company_input.md`) + Fase 0 | Metas ajustadas à empresa | `AG-D-XX.Y-NNN` |
| **Fase 2 — Operacionalização** | Como se verifica, na prática, cada meta ajustada? | Metas ajustadas | Objetivos operacionais (com método de verificação, critério e responsável) + regras de engenharia + princípios de desenho seguro | `PO-D-XX.Y-NNN` (privacidade), `SO-D-XX.Y-NNN` (segurança), `RULE-…` |
| **Fase 3, Parte 1 — Especificação** | Que requisitos o produto e a organização têm de cumprir, aceites pelo cliente item a item? | Objetivos operacionais + regras + cartões funcionais da empresa | Requisitos de produto, requisitos organizacionais, casos de uso reforçados | `REQ-D-XX.Y-NNN` (na prática `R<n>`/`RN<n>`), `ORG-D-XX.Y-NNN` |
| **Fase 3, Parte 2 — Ameaças e risco** | Que ameaças sobram depois desses requisitos, e que risco a empresa aceita? | Requisitos aceites na Parte 1 | Modelo do sistema, análise de ameaças de segurança e de privacidade, árvores de ataque, registo de risco assinado | `TM-D-XX.Y-NNN`, fluxos `DF-…`, fronteiras `TB-…` |

Não existe Fase 4 (decisão do investigador, 2026-10-18).

### As etapas, por ordem de execução

A ordem é fixada no código em `pipeline/src/aegis_pipeline/phases/phase1/runner.py`
(`P3A_ORDER`, `P3B_ORDER`). Na Parte 2 a tabela mostra as chamadas ao modelo
(`p3b_stride`, `p3b_linddun`, `p3b_k3`, `p3b_tree`), que o executor agrupa nas
etapas `p3b_threats` e `p3b_trees`; são os nomes que o inspector usa.

"Modelo" = a etapa chama o modelo de linguagem; "código" = a etapa é
determinística.

| Fase | Etapa (nome no código) | O que faz, por extenso | Quem a faz |
|---|---|---|---|
| 1 | `p1` | Extrair os factos da empresa para uma ficha | Modelo |
| 1 | `p2` | Decidir, lei a lei, se se aplica (cinco leis candidatas: GDPR, CRA, NIS2, DORA, AI Act) | Modelo |
| 1 | `p3` | Selecionar os subdomínios ativados (de 38 possíveis, `D-01.1` a `D-10.3`) | Modelo |
| 1 | `p3f` | Enquadrar a proporcionalidade da empresa | Modelo |
| 1 | `p4` | Escrever as metas ajustadas, um subdomínio de cada vez | Modelo |
| 1 | `p4t` | Resolver tensões entre leis (só com duas ou mais leis aplicáveis) | Modelo |
| 1 | `p5` | Montar o documento final da Fase 1 | Código |
| 2 | `phase2` (chamadas internas `p2o` e `p2d`) | Para cada objetivo: método de verificação, critério, responsável e regras (`p2o`); princípios de desenho seguro (`p2d`) | Modelo + código |
| 3.1 | `p3a_cards` | Construir os cartões funcionais de partida (linha de base V0) | Modelo |
| 3.1 | `p3a_map` | Triar cada objetivo: já está coberto por um cartão? vai para o produto? vai para a organização? | Modelo |
| 3.1 | `p3a_org_cluster` | Agrupar os deveres organizacionais | Modelo |
| 3.1 | `p3a_propose` / `p3a_prin` | Propor requisitos novos para as lacunas (a partir de objetivos / de princípios) | Modelo |
| 3.1 | `p3a_round` / `p3a_repropose` | Ronda de aceitação: o cliente aceita, rejeita ou pede ajuste a cada proposta; repete até convergir | Código + pessoa |
| 3.1 | `p3a_org` | Escrever os requisitos organizacionais | Modelo |
| 3.1 | `p3a_weave` | Integrar os requisitos aceites nos cartões e casos de uso | Modelo |
| 3.1 | `p3a_gate` | Portão de saída da Parte 1 | Código |
| 3.2 | `p3b_model` | Modelar o sistema em activos, fluxos de dados e fronteiras de confiança | Modelo |
| 3.2 | `p3b_stride` | Levantar ameaças de segurança (método STRIDE), por fluxo de dados | Modelo |
| 3.2 | `p3b_linddun` | Levantar ameaças de privacidade (método LINDDUN) | Modelo |
| 3.2 | `p3b_k3` | Mapear cada ameaça para os catálogos CWE / CAPEC / ATT&CK / D3FEND | Modelo |
| 3.2 | `p3b_tree` | Construir árvores de ataque-defesa | Modelo |
| 3.2 | `p3b_risk_round` | Ronda de risco: uma pessoa assina a decisão sobre cada ameaça | Código + pessoa |
| 3.2 | `p3b_gate` | Portão de saída da Parte 2 | Código |

---

## 2. As quatro perguntas de avaliação

Qualquer saída da pipeline é avaliada com as mesmas quatro perguntas, por esta
ordem. Cada pergunta só faz sentido se a anterior passou.

| # | Pergunta | Quando se faz | Quem responde | O que acontece se falha | Nome antigo no repositório |
|---|---|---|---|---|---|
| **1** | **A resposta do modelo tem a forma certa?** Campos obrigatórios presentes, valores dentro das listas permitidas, identificadores que existem, gramática exigida (por exemplo "WHEN … the system SHALL …"). | Em cada chamada ao modelo | Código | O código devolve ao modelo uma mensagem de correção e pede uma segunda tentativa (são duas tentativas no total, `runner.py`, ciclo `for attempt in (1, 2)`). Se a segunda falha, a parte fica marcada como falhada. | "L0", "contrato", "validação de esquema" |
| **2** | **O conjunto produzido pela fase é íntegro?** As cadeias de identificadores fecham, os totais somam, não há tecnologia proibida, nenhum objetivo se perdeu, o modelo não colapsou numa resposta por defeito. | No fim de cada etapa e no portão de saída de cada fase | Código | Bloqueia (a fase não é declarada concluída) **ou** apenas avisa — a secção 3 diz qual, em cada caso. | "L1", "gate", "guarda", "checker" |
| **3** | **Uma pessoa responsável aprova?** | Em pontos fixos entre etapas | O investigador / o cliente | A etapa seguinte recusa-se a correr enquanto não existir o ficheiro de aprovação em `steps/gates/`. | "portão humano", "L4", `G-P1-A`…, `G-P3-A`, `G-P3-B` |
| **4** | **O conteúdo é boa engenharia para esta empresa?** Não é texto genérico com o nome da empresa colado; preserva a obrigação legal; um auditor consegue testar o que está escrito. | Por amostragem, depois das corridas, em sessão de pontuação cega | Pessoa, com uma grelha de pontuação | Não bloqueia uma corrida. Decide se os limiares das perguntas 1 e 2 estão bem calibrados (é assim que um limiar passa de "convenção" a "medido" em `METRICS.md`). | "L2", "rubrica", "pontuação cega" |

**O que cada pergunta não consegue ver.** A pergunta 1 e a 2 só verificam forma e
coerência; não sabem se o conteúdo é bom (`AGENTS.md` R10b). A pergunta 4 é a
única que julga substância, mas só vê uma amostra. Por isso um "verde" das
perguntas 1 e 2 nunca chega para afirmar qualidade.

**Atenção a uma colisão de nomes.** "L0…L4" aparece no repositório com **dois
significados diferentes**: (a) as camadas de validação acima, e (b) a escala de
**altitude** de um requisito (L0 propriedade → L1 objetivo → L2 restrição
verificável → L3 categoria de mecanismo → L4 tecnologia concreta;
`templates/phase3_functional_spec_guidelines.md` §2.5). Neste guia usam-se só as
palavras por extenso.

### Como ler a coluna "Quem verifica" na secção 3

| Valor | Significado |
|---|---|
| **Código — bloqueia** | Se falha, a fase não fica concluída. |
| **Código — avisa** | Fica registado como aviso, a corrida continua. |
| **Código — só reporta** | O número é calculado e escrito, mas nada o compara com um limiar. Um mau valor passa despercebido se ninguém olhar. |
| **Critério de experiência** | O limiar existe apenas no pré-registo de uma experiência; a pipeline não o aplica. |
| **Pessoa** | Decisão humana (pergunta 3) ou pontuação (pergunta 4). |

---

## 3. O que é um bom resultado, fase a fase

Em cada tabela: o que a etapa tem de garantir, quem verifica, e o sinal típico
de mau resultado (com o registo onde já aconteceu, quando existe).

### 3.1 Fase 1 — Definição contextual

**Um bom resultado da Fase 1:** as leis certas estão ativadas com a razão
ligada a um facto da empresa; só os subdomínios que a operação real ativa estão
selecionados; e cada meta ajustada preserva todas as partes da obrigação
legal *e* diz algo que só é verdade para esta empresa, sem nomear tecnologias.

| Etapa | O que tem de garantir | Quem verifica | Limiar e fonte | Sinal de mau resultado |
|---|---|---|---|---|
| Extrair factos (`p1`) | Ficha com os campos do perfil; nada inventado (regra R6) | Código — bloqueia (forma); Pessoa (portão de aprovação dos factos, `G-P1-A`) | — | Infraestrutura ou dados que a empresa não declarou |
| Decidir leis (`p2`) | Uma decisão sim/não por lei, com razão ligada ao papel legal da empresa | Código — bloqueia (forma); Pessoa (portão de confirmação das leis, `G-P1-B`) | — | Ativar NIS2 ou DORA numa micro-empresa sem critério setorial |
| Selecionar subdomínios (`p3`, `p3f`) | Cada um dos 38 candidatos fica selecionado **ou** excluído, nunca omitido; só identificadores canónicos (regra R1) | Código — bloqueia (partição completa, `phase1/selection.py`); Pessoa (portão de aceitação da seleção, `G-P1-C`); Pessoa — pontuação, dimensão `D7` da grelha da Fase 1 | — | Selecionar todos os 38 "por precaução" num caso simples |
| Escrever metas ajustadas (`p4`) | Mantém os termos da obrigação | Código — bloqueia | retenção ≥ 0,30 — `M-02` (convenção) | Perna da obrigação perdida |
| | É uma reformulação, não uma cópia | Código — bloqueia | semelhança ao texto de base ≤ 0,88 — `M-03` (convenção) | Cópia quase literal do objetivo de base |
| | A implicação para a empresa é específica e não se repete entre linhas | Código — bloqueia | ≥ 5 palavras — `M-05`; semelhança entre implicações < 0,95 — `M-07` (convenções) | A mesma frase em todas as linhas |
| | Sem nomes de tecnologia, produto ou fornecedor (regra R5) | Código — bloqueia (lista de palavras, `quality_gates.py`) | — | "usar PostgreSQL", "AWS" |
| | Âncoras de controlo existem e pertencem ao objetivo (regra R2) | Código — as âncoras são derivadas pelo código, não pelo modelo (`guards/controls.py`) | — | — |
| | O modelo não se refugiou na classificação por defeito | Código — avisa | `(inalterado + literal) / n > 0,70` — `M-14` (convenção) | Mais de 70 % das linhas marcadas "unchanged" |
| | A narrativa e a classificação não se contradizem | Código — avisa | lista de palavras — `M-15` (convenção) | Implicação fala em delegar a um fornecedor, classificação diz "unchanged" |
| | **Substância:** o objetivo passaria o teste da invariância — não se leria igual para outra empresa | Pessoa — pontuação 1–5, grelha `docs/experiments/L2_RUBRIC.md` §2a | 4–5 = bom; 3 = "legalmente completo, analiticamente preguiçoso"; ≤ 2 = defeito | Nome da empresa colado à frase da lei (pontuação 3) |
| Resolver tensões (`p4t`) | Cada conflito entre leis tem uma regra única e auditável | Código — a etapa só corre com ≥ 2 leis (`M-11`); Pessoa — dimensões `D5`, `D6` da grelha da Fase 1 | — | "monitorizar e rever periodicamente" |
| Montar documento (`p5`) | O documento diz o mesmo que os artefactos; subdomínio que falhou fica marcado como rascunho não validado, nunca omitido | Código — bloqueia (validador diferencial, `guards/l1_validation.py`) | — | Subdomínio desaparecido do documento |
| Fim da fase | Aprovação final | Pessoa (portão de assinatura final, `G-P1-D`) — **documentado mas o código não o exige** (`10_PHASE_ORIENTATION.md` §3) | — | — |

### 3.2 Fase 2 — Operacionalização

**Um bom resultado da Fase 2:** todos os objetivos da Fase 1 continuam
presentes; cada um tem um método de verificação que corresponde à natureza do
dever, um critério que diz *que evidência* aprova ou chumba, e uma a duas regras
de engenharia testáveis, específicas desta empresa.

| O que tem de garantir | Quem verifica | Limiar e fonte | Sinal de mau resultado |
|---|---|---|---|
| Nenhum objetivo da Fase 1 se perde; nenhum subdomínio selecionado fica sem objetivos; prefixos `PO-`/`SO-` coerentes com a lei; identificadores únicos | Código — bloqueia (cinco verificações do documento 1, códigos `G0`–`G4`, `phase2/derivation.py` `check`) | contagem igual — `P2M1`, zero achados — `P2M2` (`PREREG_P2_02.md`) | Objetivo da Fase 1 sem objetivo da Fase 2 |
| Cada objetivo recebe método, critério e responsável do modelo | **Código — só reporta** (`seams_filled` no resultado da etapa) | ≥ 95 % — `P2M5`, **critério de experiência** | **Degradação silenciosa:** 0 de 37 chamadas passaram e a etapa saiu `ok` (registo P2-03) |
| Os métodos de verificação não colapsam num só | Código — bloqueia (`phase2/parsers.py`) | nenhum método > 60 % — `P2M7` (regra R10b) | 90 % dos objetivos como "INSPECT" |
| Cada objetivo tem pelo menos uma regra `RULE-…` | Critério de experiência | ≥ 1 por objetivo, média 1–2,5 — `P2M8` | Zero regras (registo P2-03); regras que repetem o objetivo em maiúsculas |
| As regras e traduções diferem entre empresas | Critério de experiência | semelhança média entre casos ≤ 0,60 — `P2M10` | O mesmo texto para três empresas diferentes |
| Princípios de desenho: completos, sem tecnologia, ancorados nos factos desta empresa | Código — bloqueia (verificações do documento 2, códigos `G5`–`G7`) | proporção ancorada ≥ 0,50 — `P2M9` | Princípios de manual, sem relação com o produto; vocabulário de outra empresa |
| Todas as âncoras de controlo existem no referencial | Código — bloqueia | zero não resolvidas — `P2M4` (regra R2b) | — |
| **Substância:** o método e o critério servem um auditor real | Pessoa — **ainda sem grelha própria para a Fase 2** | — | — |

### 3.3 Fase 3, Parte 1 — Especificação de requisitos

**Um bom resultado da Parte 1:** cada objetivo operacional tem um destino honesto
(já coberto por um cartão, novo requisito de produto, ou requisito
organizacional); os deveres técnicos ficam no produto e não são empurrados para
"política"; cada requisito novo está à altitude certa e tem um critério que um
engenheiro de testes transforma num teste passa/falha; e o cliente aceitou ou
rejeitou explicitamente cada proposta.

| Etapa | O que tem de garantir | Quem verifica | Limiar e fonte | Sinal de mau resultado |
|---|---|---|---|---|
| Triagem e cobertura (`p3a_map`) | Cada objetivo recebe um de cinco veredictos (totalmente coberto / parcialmente coberto / sem portador funcional, isto é, organizacional / orientação de desenho / não aplicável) e nomeia o que o cobre | Código — bloqueia (`M-19`, lista fechada de veredictos) | coluna de descarga não vazia — `M-19` | "Totalmente coberto" sem dizer por quem |
| | As âncoras escolhidas pertencem ao objetivo | Código — bloqueia (`M-20`, verificação `T6`) — **verificação fraca: compara o conjunto consigo próprio** (`10_PHASE_ORIENTATION.md` falha S5) | — | — |
| | Os deveres técnicos não fogem para a organização | Código — avisa e desafia o modelo uma vez | > 40 % organizacional em D-01, D-03, D-05, D-07 — `M-27` (medido); > 65 % em D-02..D-07 — `M-26` | 70–80 % dos deveres técnicos enviados para "política" (registo P3-02) |
| | **Substância:** o veredicto é honesto | Pessoa — grelha da Fase 3 (`L2_RUBRIC_F3.md`), dimensão `D6` | 0–2 | "Totalmente coberto" com exceções escondidas |
| Propor requisitos (`p3a_propose`, `p3a_prin`, `p3a_org`) | Gramática EARS; as leis citadas têm um objetivo de origem dessa lei (`T2`); sem vocabulário de tecnologia | Código — bloqueia | — | Lei citada que não pertence ao objetivo |
| | **Substância:** altitude certa; critério binário; cadeia de âncoras válida; ligado à empresa | Pessoa — grelha da Fase 3, dimensões `D1`–`D5` | 0–2 cada | Critério vago ou duplo ("rápido e seguro"); biblioteca nomeada sem justificação |
| Ronda de aceitação (`p3a_round`) | Cada proposta tem decisão explícita: aceitar / rejeitar (= aceitação de risco registada) / ajustar | Pessoa (portão da ronda, `G-P3-A`) | — | Proposta sem decisão |
| Integrar nos casos de uso (`p3a_weave`) | Os requisitos aceites entram como passos reais de validação ou exceção nos casos de uso | Pessoa — leitura | — | Regra colada como texto solto |
| **Portão de saída** (`p3a_gate`) | `G1` todos os objetivos e princípios têm destino; `G2` ronda concluída com aprovação humana e pelo menos um item; `G3` âncoras publicadas; `G4` documentos sem defeitos de formato (`doc_lint --strict`); `G5` avaliação de suficiência por lei; `G6` uma linha de absorção por requisito aceite; mais as verificações de rastreabilidade `T1`–`T6` sobre a corrida | Código — bloqueia (`phase3/weave.py`) | todos fechados | Estado `PROPOSED` (ronda aberta) ou `FAILED` |

### 3.4 Fase 3, Parte 2 — Ameaças e risco

**Um bom resultado da Parte 2:** cada ameaça está ligada a um fluxo real do
sistema e aos requisitos da Parte 1 que a mitigam; segurança e privacidade estão
ambas cobertas; o risco residual nunca é menor do que os factos justificam; e
cada decisão de risco tem assinatura humana.

| O que tem de garantir | Quem verifica | Limiar e fonte | Sinal de mau resultado |
|---|---|---|---|
| Os mitigadores citados são requisitos aceites da Parte 1 | Código — bloqueia (`phase3b/threats.py`) | — | Inventar identificadores de mitigadores (fez cair a análise de privacidade do modelo qwen3.8, registo P3-03) |
| Identificadores CWE / CAPEC / LINDDUN existem no catálogo `baseline/THREATS/` | Código — bloqueia (`G12`, verificação `T8`) | 100 % | Identificador inventado |
| O risco residual é calculado pelo código a partir da avaliação de mitigação, nunca escolhido pelo modelo | Código (`residual_from_mitigation`) | — | — |
| Um caminho de ataque não mitigado na árvore impede risco residual "Baixo" | Código — sobe o residual (`phase3b/adtrees.py`) | hipótese H3 de `PREREG_P3_03.md` | Residual "Baixo" com caminho aberto |
| Ameaças analisadas = ameaças no registo | Código — bloqueia (`G11`, verificação `T7`) | — | Ameaça analisada que não chega ao registo |
| Nenhum risco residual "Crítico" | Código — bloqueia (`G8`) | zero | — |
| Ameaça com obrigação legal e sem mitigação não pode ser aceite nem transferida | Código — bloqueia (`G9`) | zero | Aceitar risco ilegal |
| Cada ameaça tem decisão humana assinada | Pessoa (portão da ronda de risco, `G-P3-B`); Código verifica a assinatura (`G7`) | todas | Estado `PROPOSED` |
| Cada rejeição volta à Parte 1 e é absorvida numa ronda assinada | Código — bloqueia (`G10`) | — | Rejeição sem retrabalho |
| **Substância:** as ameaças e árvores são plausíveis para esta arquitetura | Pessoa — **ainda sem grelha própria para a Parte 2** | — | — |

---

## 4. Como se declara o resultado de uma corrida

Ler por esta ordem. Parar no primeiro "não".

1. **Todas as etapas correram?** `manifest.json` da corrida, estado de cada
   etapa. Atenção: hoje uma etapa que registou `partial` pode aparecer como `ok`
   (`10_PHASE_ORIENTATION.md`, falha S13). Confirmar também os números que só
   são reportados (por exemplo `seams_filled` da Fase 2).
2. **Os portões de código fecharam?** O relatório de portão de cada fase tem um
   de três estados:
   - `CONCLUDED` — todos os portões fechados, zero achados. Único estado que
     conta como resultado completo.
   - `PROPOSED` — falta uma decisão humana (ronda aberta ou ameaças por
     assinar). Não é falha; é trabalho por fazer.
   - `FAILED` — um portão de código está aberto. Ler a mensagem `OPEN — …`.
3. **As pessoas aprovaram?** Os ficheiros de aprovação existem em
   `steps/gates/`.
4. **A substância está boa?** Só se sabe por amostragem com as grelhas da
   pergunta 4. Enquanto não houver pontuação, a afirmação honesta é "passou a
   forma e a integridade; a substância não foi medida".

Quando se escreve sobre uma corrida, cada afirmação leva âncora verificável:
identificador de experiência (`EXP-nn`, `P3-03`…), identificador de limiar
(`M-nn`), ou o veredicto de um verificador (`AGENTS.md` §-2 regra 1).

---

## 5. Dicionário de códigos

### 5.1 Pontos de verificação e portões

| Código | Significado por extenso | Fase | Onde está definido |
|---|---|---|---|
| `G-P1-A` | Portão humano: a ficha de factos é fiel à descrição da empresa | 1 | `pipeline/README.md`; exigido por `runner.py` antes de `p2` |
| `G-P1-B` | Portão humano: as decisões sobre que leis se aplicam estão confirmadas | 1 | idem; exigido antes de `p3`/`p3f` |
| `G-P1-C` | Portão humano: a seleção de subdomínios e as exclusões estão aceites | 1 | idem; exigido antes de `p4` |
| `G-P1-D` | Portão humano: assinatura final do documento da Fase 1 (passa de rascunho a ativo) | 1 | documentado; **não exigido pelo código** |
| `G0`–`G4` (Fase 2) | Verificações do documento de objetivos operacionais: fase anterior completa (`G0`), sem marcação crua da base (`G1`), prefixo coerente com a lei (`G2`), identificadores únicos (`G3`), nenhum objetivo perdido (`G4`) | 2 | `phase2/derivation.py` `check` |
| `G5`–`G7` (Fase 2) | Verificações do documento de princípios: completude (`G5`), sem tecnologia (`G6`), ancoragem nos factos da empresa (`G7`) | 2 | `phase2/derivation.py` `check_doc02` |
| `G-P3-A` | Portão humano: a ronda de aceitação de requisitos foi decidida | 3.1 | `phase3/weave.py` |
| `G1`–`G6` (Fase 3, Parte 1) | Portão de saída da Parte 1 — ver tabela 3.3 | 3.1 | `phase3/weave.py` |
| `G-P3-B` | Portão humano: cada ameaça do registo de risco tem decisão assinada | 3.2 | `runner.py`, `steps/phase3b/risk_verdicts.json` |
| `G7`–`G12` (Fase 3, Parte 2) | Portão de saída da Parte 2 — ver tabela 3.4 | 3.2 | `phase3b/threat_gate.py` |
| `T1`–`T8` | Verificações de rastreabilidade: identificadores resolvem (`T1`), lei citada tem objetivo dessa lei (`T2`), totais somam (`T3`), evidência citada existe (`T4`), simetria entre matriz e portadores (`T5`), âncoras pertencem ao objetivo (`T6`), registo de ameaças reconciliado (`T7`), identificadores de ameaça existem no catálogo (`T8`) | 3 | `scripts/check_traceability.py` |

**Cuidado:** `G1`–`G7` da Fase 2, `G1`–`G6` da Fase 3 Parte 1 e `G7`–`G12` da
Fase 3 Parte 2 **são famílias diferentes** com números sobrepostos. Escrever
sempre a fase junto do código.

### 5.2 Limiares e métricas

| Código | Significado | Onde está o valor oficial |
|---|---|---|
| `M-01`…`M-27` | Limiares aplicados pelo código, cada um com a sua base: **medido** (resultado de experiência), **calibrado por incidente** (corrida concreta), ou **convenção** (escolha não medida — não pode ser citada como prova de qualidade) | `docs/experiments/METRICS.md` |
| `P2M1`…`P2M11` | Medidas da experiência da Fase 2 | `docs/experiments/PREREG_P2_02.md` §métricas |
| `H1`, `H2`, `H3` | Hipóteses de uma experiência (o número só tem sentido junto do pré-registo, por exemplo `PREREG_P3_03.md`) | o pré-registo respetivo |

### 5.3 Grelhas de pontuação humana

| Código | Grelha | Escala | Onde |
|---|---|---|---|
| pontuação 1–5 por linha | Metas ajustadas da Fase 1 | 5 excelente … 1 falha o dever; 0 indeterminado | `L2_RUBRIC.md` §2a |
| `D1`–`D7` (Fase 1) | Itens do documento da Fase 1: dimensão da empresa, área de operação, papéis legais, capacidades herdadas, conjunto de tensões, qualidade das resoluções, seleção de subdomínios | 1–5 | `L2_RUBRIC.md` §2b |
| `D1`–`D6` (Fase 3) | Altitude, forma, critério de aceitação, validade da cadeia, ligação à empresa, honestidade do veredicto | 0–2 | `L2_RUBRIC_F3.md` §2 |

**Cuidado:** `D1`–`D7` da Fase 1 e `D1`–`D6` da Fase 3 **são grelhas diferentes**
(e `D-01`…`D-10` são domínios da taxonomia, outra coisa ainda).

### 5.4 Identificadores de conteúdo

| Código | Significado |
|---|---|
| `D-XX.Y` | Subdomínio canónico da taxonomia (38, de `D-01.1` a `D-10.3`) |
| `SO-D-XX.Y.HL` / `SO-D-XX.Y.<LEI>` | Objetivo de base da Fase 0 (neutro / por lei) |
| `AG-D-XX.Y-NNN` | Meta ajustada à empresa (Fase 1) |
| `PO-D-XX.Y-NNN` / `SO-D-XX.Y-NNN` | Objetivo operacional de privacidade / de segurança (Fase 2) |
| `RULE-…` | Regra de engenharia testável (Fase 2) |
| `R<n>`, `RN<n>`, `REQ-D-XX.Y-NNN` | Requisito de produto (Fase 3, Parte 1) |
| `ORG-D-XX.Y-NNN` | Requisito organizacional (Fase 3, Parte 1) |
| `TM-D-XX.Y-NNN`, `DF-…`, `TB-…` | Ameaça, fluxo de dados, fronteira de confiança (Fase 3, Parte 2) |
| `R1`–`R13` | Regras obrigatórias para agentes (`AGENTS.md` §5) |
| `W1`–`W5` | Justificações aceites para descer de altitude (`templates/phase3_functional_spec_guidelines.md` §2.5) |

### 5.5 Termos técnicos

| Termo | Significado |
|---|---|
| EARS | Gramática de requisitos "WHEN/IF/WHILE … the system SHALL …" |
| STRIDE | Método de levantamento de ameaças de segurança (falsificação, adulteração, repúdio, divulgação, negação de serviço, elevação de privilégio) |
| LINDDUN | Método de levantamento de ameaças de privacidade |
| CWE / CAPEC | Catálogos públicos de fraquezas de software / padrões de ataque |
| V0 | Linha de base funcional da empresa, antes de qualquer requisito de segurança |
| Altitude | Grau de concretude de uma afirmação (propriedade → objetivo → restrição verificável → categoria de mecanismo → tecnologia) |
| Teste da invariância | "Este texto leria igual para outra empresa?" Se sim, é teatro de conformidade (`AGENTS.md` R10b) |
| Degradação silenciosa | Etapa termina `ok` mas a parte gerada pelo modelo está vazia |
| Colapso para o valor por defeito | O modelo escolhe a mesma classificação para quase tudo |

---

## 6. Manutenção deste guia

- Novo portão, verificação ou limiar ⇒ uma linha na tabela da secção 3 da fase
  respetiva e, se for um limiar, uma linha em `METRICS.md` (§-2 regra 2).
- Uma verificação que passa de "só reporta" ou "critério de experiência" a
  "bloqueia" ⇒ atualizar a coluna "Quem verifica" na mesma sessão.
- Nova grelha de pontuação (Fase 2, Fase 3 Parte 2) ⇒ substituir a célula
  "ainda sem grelha própria".
- As falhas conhecidas das próprias verificações estão em
  `docs/pipeline/10_PHASE_ORIENTATION.md` §4; este guia só assinala as que mudam
  a leitura de um resultado.

## Histórico de versões

| Versão | Data | Alteração |
|---|---|---|
| 1.0.0 | 2026-11-02 | Primeira versão: mapa único da pipeline, das quatro perguntas de avaliação, do bom resultado por etapa e do dicionário de códigos. |
| 1.1.0 | 2026-11-02 | Alinhado com a página `/pipeline` do inspector: "metas" na Fase 1, as chamadas da Parte 2 por nome, e a ligação à página. |
