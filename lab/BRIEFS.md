# Briefs por modelo — a falha medida e o ajuste proposto

Assinaturas extraídas da M07 (`steps/stage_result.json` + `manifest.json` de cada
corrida sincronizada). Cada braço do LAB01 aponta UMA assinatura.

## qwen3.5:27b — colapso de formato no p2 (3/3 células)

- **Sintoma:** `no ```markdown fenced block found in answer`, primeiro attempt e
  repair — o modelo escreve a tabela mas sem a cerca, ou prosa à volta. Nunca
  passa do p2 (7/7 histórico).
- **Leitura:** o contrato de saída ("return ONLY one fenced block") não está a
  ser seguido — ou não é compreendido como *delimitadores literais*.
- **Braços:** `qwen35-fence` (o primeiro carácter da resposta é a abertura da
  cerca; o último é o fecho) e `qwen35-demo` (demo do formato com empresa
  fictícia — a forma correcta sem ditar veredictos).

## glm-4.7-flash:latest — sobre-compressão + §5 em falta (20/38 no C1)

- **Sintoma misto:** (a) muitas respostas sem a secção `## §5`
  (`P4 answer missing the '## §5' section`), (b) near-verbatim 96% nos rows que
  escreve.
- **Leitura:** o modelo trunca a estrutura de cauda (§5) e comprime o corpo.
  Ambos são instruções de forma: o §5 tem de ser obrigatório mesmo vazio, e a
  restatement tem de levar as pernas do dever (quem, o quê, medida, limiar).
- **Braço:** `glm47-substance`.

## nemotron-3.5-lightning:30b — compressão + alucinação de quantidades + formato (31/38 no C1)

- **Sintoma misto:** near-verbatim 98%, quantidades não rastreáveis (R6: "2020"),
  cerca em falta, implicações duplicadas entre linhas.
- **Leitura:** três lapsos de forma: cópia do objectivo, números inventados,
  estrutura da tabela a fugir (10 colunas já vista antes).
- **Braço:** `nemotron-substance` (o do glm + quantidades só do fact sheet +
  9 células exactas por linha).

## gemma4:31b — quase lá (37/38 no C3, 35/37 no C2)

- **Sintoma:** falhas residuais distintas por caso: ordem canónica violada
  (`got NIS2 before …`), R8 (linha AI_Act em módulo stub), R6 (quantidade 56
  fora do intake). O resto do run está limpo.
- **Leitura:** não é capacidade — são lapsos pontuais de precisão. Ênfase
  explícita nas três regras já existentes.
- **Braço:** `gemma4-precision` (no C3, onde a falha é 1/38).

## Os sobreviventes (não têm braço)

- **qwen3.8:27b (referência)** e **muse-glimmer:30b** entregam 3/3 casos sob o
  instrumento badge (M07). Registados no ledger. Qualquer overlay que os toque
  só por toque é desperdício — e confunde o instrumento.
- ornith-1.5: runtime-incompatible (CUDA, 2 nós) — fora por PREREG-M02.
