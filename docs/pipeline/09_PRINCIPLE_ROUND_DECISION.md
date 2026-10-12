# Ronda dos princípios — 7 propostas à espera de veredicto

> Gerado por `p3a_prin` (job 2023699, run `run_p2enr_c1`). As sete chamadas
> produziram sete restrições, uma por princípio. Este ficheiro diz o que cada uma
> faz, o que Recommendamos, e onde achamos defeito.

**O que tens de fazer:** escrever `Accept` / `Reject` / `Adjust` por item em
`steps/phase3/round1_verdicts.json`, sob a chave do **princípio** (não do
objectivo — a razão está no §3). Aceitar tudo em bloco é legítimo; aprovar sem
ler torna a ronda decorativa.

---

## 1. O que a corrida mediu

| Medição pré-registada | Resultado |
|---|---|
| O `PO-D-01.2-001` (protecção em trânsito) volta ao lane de produto? | **Sim** — pelo `PRIN-ENG-01`, como `also_carries` |
| A contagem organizacional desce das 52? | **Sim** — 52 → 37 (15 objectivos movem) |
| Zero âncoras inventadas? | **Sim** — as 11 âncoras distintas resolvem em ficheiros reais do NIST CSF 2.0, verificados um a um em `baseline/CONTROLS/` |
| Zero rejeições de formato? | A ronda ainda não correu |

Contagem por princípio: **7 proposing, 0 silences.** O pass diz que silêncio é
resposta válida; o modelo não usou essa saída uma única vez, e o `PRIN-ENG-05`
abaixo mostra que havia pelo menos um caso em que devia ter usado.

---

## 2. Os sete itens

### PRIN-ENG-01 — *Explicit Trust Boundaries & Complete Mediation* → `SO-D-01.2-002`, também `PO-D-01.2-001`

> Where the system exposes interfaces across distributed SaaS instances, the system shall authenticate and validate every crossing flow between zones of differing privilege, ensuring zero unmediated bypasses.

**Recomendação: Ajustar.** É a restrição que responde ao teu exemplo, e é a
única sobre a qual tens uma objecção de fundo:

- O objectivo `PO-D-01.2-001` pede que os dados **permanecem confidenciais em
  trânsito**. A restrição diz *autenticar e validar* cada fluxo. Um fluxo pode
  ser autenticado, validado, e transported em claro — a restrição não obriga a
  canal cifrado.
- O `SO-D-01.2-002` tem duas pernas: *cifrar em trânsito* **e** *restringir a
  superfície exposta*. A restrição só implementa a segunda, mas o veredicto
  diria "descarregado".
- Com a formulação actual, a protecção em trânsito volta ao lane de produto com
  um portador que não pede canal cifrado. O exemplo que levantaste ficaria
  tecnicamente coberto e materialmente por fazer.

O que pedir: que a restrição nomeie a **propriedade de confidencialidade do
canal**, não só a sua mediação. A formulação neutra da tabela D5 é
*"authenticated and encrypted end-to-end communication channel"* — sem
protocolo, com a propriedade. Tu conheces o caso escrito à mão: a RN24 é
exactamente isto.

---

### PRIN-ENG-02 — *Complete Mediation* → `SO-D-07.2-001`, também `SO-D-01.2-002`

> Where the system exposes network interfaces, API endpoints, or auxiliary ingress hooks (e.g., webhooks, debug ports, admin consoles), the system shall restrict active interfaces to the minimum necessary for the intended purpose and enforce that any auxiliary ingress hook implements the same security intensity (authentication, authorization, and integrity checks) as the core data processing interfaces.

**Recomendação: Aceitar.** É a melhor das sete: implementa o princípio em vez de
o repetir, o critério de conformidade é decidível por auditoria estática, e o
risco é concreto para uma plataforma SaaS. Sem objecção de conteúdo.

Nota: este item e o PRIN-ENG-01 reclamam ambos o `SO-D-01.2-002`. A matriz
credita só um (o PRIN-ENG-01, por ordem de ficheiro) — determinístico, mas
saber que o objectivo fica com um portador só.

---

### PRIN-ENG-03 — *Least Privilege* → `SO-D-01.3-002`, também `PO-D-01.3-001`

> Where the system manages cryptographic keys for data at rest, the system shall enforce access controls that restrict key management operations to roles distinct from the operational environment custodian, ensuring that no single principal holds both key management and operational execution privileges.

**Recomendação: Aceitar.** Corresponde ao objectivo (separação de papéis na
gestão de chaves), o critério é uma auditoria de acessos, e as âncoras
(`PR.DS-01`, `PR.AA-05`, `GV.OV-01`) são as do conjunto publicado.

Ponto menor: o critério de conformidade inventa dois nomes de permissão
(`key_management`, `operational_execution`). Aceitável como vocabulário
funcional, mas não são nomes que venham da empresa.

---

### PRIN-ENG-04 — *Secure by Default* → `SO-D-03.4-002`, também `PO-D-03.4-001`, `SO-D-07.2-001`

> Where the system initializes a new customer account or task workspace, the system shall configure all security-relevant parameters to a secure-by-default state that denies access and restricts data visibility until explicitly authorized by the user, and shall not expose any functional interface or data store in an open or permissive state during initialization or failure.

**Recomendação: Aceitar com uma nota.** O trigger está bem posto (o momento de
criação da conta é onde o secure-by-default se decide) e o risco é concreto.
Uma objecção leve: o critério de conformidade diz *"all security controls (e.g.,
MFA, encryption, access restrictions) enabled by default"* — isso nomeia
controlos dentro do critério, e um critério não deve prescrever o que verificar.
Não é violação da tabela D5 (MFA e "encryption" são classes de controlo, não
tecnologias), mas é mais fraco do que devia ser.

---

### PRIN-ENG-05 — *Fail-Safe Defaults* → `PO-D-02.1-001`, também `SO-D-02.1-002`, `SO-D-10.3-002`

> Where the organization initiates a test or evaluation of technical and organizational security measures, the system shall produce a single, atomic verification record that contains exactly one condition, one expected response, and a deterministic automated pass/fail result, without requiring manual interpretation of ambiguous outputs.

**Recomendação: Rejeitar.** Esta não é uma restrição de segurança:

- O que ela impõe é o **formato do nosso próprio registo de verificação** — uma
  condição, uma resposta esperada, um resultado determinístico. Isso é a
  convenção EARS/Volere deste projecto, vestida de risco de segurança. O campo
  "risco" acusa *"revisões de segurança manuais, subjectivas ou de multi-condição"* —
  está a criticar o nosso estilo de escrita, não uma falha de segurança da
  empresa.
- E tem um efeito nocivo: puxaria `PO-D-02.1-001` (testes de segurança),
  `SO-D-02.1-002` e `SO-D-10.3-002` do lane organizacional para o lane de
  produto, por causa de uma restrição sobre registos de teste. Esses três são
  organizacionais por natureza; aqui por causa de uma regra de escrita.

É também o item onde o modelo **devia** ter usado a saída de silêncio que a ficha
lhe dá.

---

### PRIN-ENG-06 — *Data Minimization* → `PO-D-03.4-001`, também `PO-D-05.1-001`, `SO-D-05.1-002`, `PO-D-07.1-001`

> Where the system processes customer account metadata or task data, the system shall restrict the collection, transmission, and retention of personal data fields to only those strictly indispensable for the specific declared service purpose, and shall project data views to authorized roles that exclude any personal data fields not required for that role's function.

**Recomendação: Aceitar.** É a mais bem construída das sete: implementa a
minimização com as duas pernas que a tornam verificável (o que se recolhe e o
que se projecta), o risco é concreto e cita a base legal correcta.

---

### PRIN-ENG-07 — *Right to Erasure* → `PO-D-05.2-001`, também `PO-D-04.4-001`

> Where a data subject request for erasure is received or a retention period expires, the system shall permanently destroy the associated personal data across all primary stores, edge caches, archives, and disaster-recovery copies, ensuring no recoverable copies remain.

**Recomendação: Aceitar.** Cobre as camadas onde um produto SaaS pequeno
efectivamente perde dados (cache, arquivo, cópias de recuperação), o critério
é uma inspecção forense, e o risco cita o artigo certo.

---

## 3. Porquê que o veredicto se escreve sob a chave do princípio

O `SO-D-07.2-001` tem **duas** restrições nesta ronda: o cartão vindo do
objectivo (que já tinhas aceite) e a restrição do `PRIN-ENG-02`. Se a chave fosse
o objectivo, um único veredicto governaria as duas — e não tinhas forma de ficar
com uma e rejeitar a outra.

Por isso: `PRIN-ENG-01` … `PRIN-ENG-07` são chaves próprias. Os 18 veredictos que
já puseste mantêm-se como estão.

```json
{
  "verdicts": {
    "SO-D-07.2-001": "Accept",
    "PRIN-ENG-01": "Adjust",
    "PRIN-ENG-02": "Accept",
    "PRIN-ENG-03": "Accept",
    "PRIN-ENG-04": "Accept",
    "PRIN-ENG-05": "Reject",
    "PRIN-ENG-06": "Accept",
    "PRIN-ENG-07": "Accept"
  },
  "rationale": {
    "PRIN-ENG-01": "",
    "PRIN-ENG-02": "",
    "PRIN-ENG-03": "",
    "PRIN-ENG-04": "",
    "PRIN-ENG-05": "",
    "PRIN-ENG-06": "",
    "PRIN-ENG-07": ""
  }
}
```

A `rationale` dos 18 veredictos anteriores fica como está; estas sete chaves são
novas. Este bloco é o que Recommendamos, não um bloco pré-preenchido: o Adjust
do PRIN-ENG-01 é uma pergunta para ti, não um texto pronto.

Depois: `p3a_round` re-converge, o weave re-aloca os cartões novos, re-encaminha
os 15 objectivos e re-renderiza a matriz e a `PRINCIPLE_MAPPING`. Nada do que
já está verde volta a correr.