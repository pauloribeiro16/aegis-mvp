# Pacote de decisão — ronda 1, as 7 constraints de princípio (run_p2enr_c1)

**Estado:** à tua espera. A ronda não converge sem os teus veredictos, e por isso a
gate de saída está em `PROPOSED` (G1 e G2 OPEN) desde 2026-10-12.

**O que precisas de fazer:** responder **Aceitar em bloco** (as 6 recomendações) ou
**por excepção** (indicar quaisitm). Os veredictos vão para
`~/Work/aegis-runs/run_p2enr_c1/steps/phase3/round1_verdicts.json`, e a ronda
volta a correr com `p3a_all`.

> **Aviso, porque é o que este ficheiro existe para evitar:** se responderes sem
> ler, a ronda torna-se decorativa — fica registado que decidiste, não o que
> decidiste. O registo passa a dizer "Aceite" sobre um texto que ninguém
> sustentou. O custo não é o veredicto errado; é a rastreabilidade.

---

## Medição mecânica (feita antes de te pedir nada)

Corri o guard de contaminação R5 sobre os 7 itens (constraint, critério de
verificação e risco): **0 ocorrências de vocabulário de tecnologia em 21 campos**.

Isto importa porque o precedente `duty_20` falhou duas vezes exactamente assim: o
teu warrant dizia "Enforce TLS 1.3", o pack levou-o verbatim e o modelo copiou a
auditoria. Não se repetiu aqui, porque estes textos são gerados, não teus.

**Mas o guard é cego para três defeitos que a leitura encontrou.** O `L4_TERMS` é
uma lista de tecnologia *nomeada* (fornecedores, frameworks, protocolos). Ele não
modela segurança pré-farcada, prescrição de método, nem identificadores
inventados — que são regras diferentes (R13 anti-padrão 1, mandato de abstracção
de controlo, R6). **Não é um defeito do guard; é um limite do que ele mede.** Os
três pontos estão assinalados abaixo.

---

## As 7 recomendações

Legenda: **A** = Aceitar · **Aj** = Aceitar com ajuste de redacção (o sentido
mantém-se, a formulação muda) · **R** = Reject (= aceitação explícita do risco).

### PRIN-ENG-01 — Fronteiras de confiança explícitas e mediação completa → **Aj**
> *Onde o sistema expõe interfaces através de instâncias SaaS distribuídas,
> shall autenticar e validar cada fluxo entre zonas de privilégio distinto,
> garantindo zero bypasses não mediados.*

**Porque não aceitar como está:** "cada fluxo" e "zero bypasses" não são
verificáveis e pedem autenticação entre serviços internos — uma descida de nível
(L2 → L3) sem warrant, que presume uma arquitectura que a TinyTask pode não ter.
**Ajuste sugerido:** limitar às fronteiras que existem no produto (externas e
entre níveis de privilégio reais), e trocar o absoluto por "nenhuma fronteira
exposta sem mediação".
**Riscos de não fazer nada:** a SO-D-01.2-002 e a PO-D-01.2-001 ficam sem
constraint que as descarregue.

### PRIN-ENG-02 — Minimização da superfície de ataque → **Aj**
> *Onde o sistema expõe interfaces de rede, pontos de acesso ou ganchos de
> entrada auxiliares (webhooks, portas de depuração, consolas de administração),
> shall restringir as interfaces activas ao mínimo necessário…*

**Porque não aceitar como está:** o critério de verificação exige **análise
estática** — isso é um mecanismo, não um objectivo de controlo, e é exactamente o
que o mandato de abstracção de alto nível proíbe numa requisito não-funcional. A
enumeração de exemplos ("debug ports") é um convite a technology leakage dentro
do cartão.
**Ajuste sugerido:** manter o objectivo ("nenhuma interface activa sem
justificação documentada; nenhuma interface auxiliar mais fraca que as
principais") e retirar "análise estática" e a lista de exemplos.

### PRIN-ENG-03 — Menor privilégio e isolamento de mecanismos → **Aj + decisão tua de proporcionalidade**
> *Onde o sistema gere chaves criptográficas… shall restringir as operações de
> gestão de chaves a papéis distintos do custodiante operacional…*

**Porque não aceitar como está:** o critério de verificação nomeia
**`key_management` e `operational_execution`** — dois identificadores que não
existem em lado nenhum. São inventados (R6), e um critério que verifica permissões
que ninguém definiu não verifica nada.
**E há uma decisão tua dentro disto:** exigir que os dois conjuntos de papéis sejam
disjuntos, numa empresa de 8 pessoas, é uma decisão de proporcionalidade (é a
mesma família do G-c, as seis duties SCALE). Se as chaves vivem num serviço
gerido, a segregação já é estrutural e a obrigação deve dizer isso, não exigir
uma separação de cargos que a dimensão da empresa não suporta.

### PRIN-ENG-04 — Defaults fail-safe e estados de falha fechados → **Aj**
> *Onde o sistema inicializa uma nova conta… shall configurar todos os
> parâmetros relevantes para um estado seguro por omissão…*

**Porque não aceitar como está:** o critério de verificação lista **"MFA,
encriptação, restrições de acesso"** como coisas a verificar por omissão. É o
anti-padrão 1 do R13 por nome: segurança pré-farcada numa requisito. A
requirement tem de dizer o efeito (uma conta nova não expõe dados nem concede
acesso antes de autorização), não enumerar controlos.
**Nota:** é a constraint mais bem fundamentada das sete no que toca a
conformidade (CRA secure-by-default) — o problema é só a redacção do critério.

### PRIN-ENG-05 — Verificabilidade e atomicidade dos requisitos → **R**
> *Onde a organização inicia um teste ou avaliação de medidas… shall produzir um
> registo de verificação atómico com exactamente uma condição, uma resposta
> esperada e um resultado automático de passa/falha…*

**Porque rejeitar:** isto é uma regra de redacção da AEGISvestida de obrigação
da TinyTask. "Uma condição EARS por cartão" é o nosso método, não uma exigência
do GDPR ou do CRA. A justificação no próprio texto ("para uma empresa de 8
pessoas, revisões manuais criam risco") descreve um risco real mas não cria uma
obrigação — e pior, obriga a que *toda* a verificação seja automática, o que
contradiz a coluna Method da Fase 2 (que inclui INSPECT, DEMONSTRATE e ANALYZE,
não só TEST).
É o exemplo mais limpo de *compliance theater* do lote: uma regra de instrumento
mascarada de obrigação do cliente. **Aceitar isto seria o erro mais caro dos
sete**, porque o registo de conformidade passaria a citar um requisito que não
existe. A rejeição fica registada como aceitação explícita do risco, que é
exactamente o que a regra de dois estados pretende.

### PRIN-ENG-06 — Minimização proactiva de dados → **A**
> *Onde o sistema processa metadados de conta ou dados de tarefa, shall
> restringir a recolha, transmissão e retenção aos campos estritamente
> indispensáveis…*

**A mais bem fundamentada das sete.** Âncora correcta (GDPR Art. 5(1)(c)),
ancorada na dimensão real da empresa ("8-employee team"), e o critério de
verificação é verificável sem mecanismo. **Um único corte:** "camadas de resposta
API" é vocabulário de tecnologia — trocar por "as respostas do sistema".

### PRIN-ENG-07 → **A**
> *Onde um pedido de apagamento é recebido… shall destruir permanentemente os
> dados pessoais em todas as cópias, incluindo cópias de recuperação…*

Juridicamente sólida (Art. 17 + Art. 5(1)(e)) e o critério ("zero instâncias
recuperáveis") é verificável. **Ressalva de proporcionalidade, não de redacção:**
as cópias de recuperação/desastre numa SaaS alojada não são necessariamente da
TinyTask. Se a obrigação não é executável na dimensão da empresa, diz isso
explicitamente em vez de prometer o que não se cumpre.

---

## Resumo

| Princípio | Recomendação | Razão em uma linha |
|---|---|---|
| PRIN-ENG-01 | **Aj** | absolutos não verificáveis; presume arquitectura |
| PRIN-ENG-02 | **Aj** | "análise estática" é mecanismo, não objectivo |
| PRIN-ENG-03 | **Aj + decisão** | permissões inventadas + segregação de cargos ≠ 8 pessoas |
| PRIN-ENG-04 | **Aj** | MFA e controlo enumerado = segurança pré-farcada |
| PRIN-ENG-05 | **R** | regra nossa, vestida de obrigação da empresa |
| PRIN-ENG-06 | **A** | sólida; um corte de vocabulário |
| PRIN-ENG-07 | **A** | sólida; ressalva de proporcionalidade |

**Aceitar em bloco** = A, A, R, A, A e os ajustes de redacção em 01–04 aplicados
por mim. **Por excepção** = indica os que mudam.

## O que fica bloqueado até responderes

1. A ronda não converge ⇒ **G2 OPEN** ⇒ a gate não fecha (correcto: é isto que
   estava a acontecer em silêncio).
2. **G1 OPEN** — os 7 princípios contam como "por colocar" e a
   `PRINCIPLE_MAPPING.md` fica em esqueleto.
3. A Fase 4 (o `v1 Doc01` como especificação a sério) e o segundo caso dependem
   desta ronda.

## Se preferires despachar

Responde "**bloco**" e eu aplico os quatro ajustes de redacção e corro
`p3a_all`. Responde "**bloco, excepto o 5**" ou "**bloco, excepto 3 e 4**" e
trato as excepções uma a uma.