# Decisão pendente (G-c) — os seis deveres SCALE da via organizacional (Caso 01)

Data: 2026-10-10 · Para: investigador (a decisão é tua — ADR-008/audit) ·
Fontes: [PROPORTIONALITY_AUDIT_ORGANIZATIONAL_LANE.md](../cases/Case_01_TinyTask_SaaS/03_PHASE3_SPEC/part1_security_privacy/analysis_v0_to_v1/PROPORTIONALITY_AUDIT_ORGANIZATIONAL_LANE.md) §3–§4 ·
Doc 08 onda 5 (`pending-scale`) · [PREREG_P3_01](../experiments/PREREG_P3_01.md) §3

**O que se decide:** os 6 deveres que a auditoria classificou **SCALE** — o dever
mantém-se, mas a *forma* que o objectivo implica (um programa empresarial) é
desproporcionada numa empresa de 8 pessoas. Para cada um: escrever o requisito
ORG na forma proporcional (o estágio `p3a_org` fica desbloqueado para ele), ou
aceitar o risco explicitamente (fica no registo de resíduos, nunca silencioso).

## 1. Resiliência/CIA contínuos — `SO-D-04.4-001`, `SO-D-10.1-001`, carve-out `PO-D-01.1-001`

- **Forma empresarial:** programa de gestão de resiliência com avaliação de
  riscos periódica e capacidade própria de recuperação.
- **Forma proporcional (audit):** responsabilidade partida do cloud gerido +
  o RPO já transportado por `RN5`.
- **Opções:** (a) requisito ORG "rever anualmente a repartição de
  responsabilidades do fornecedor e o RPO declarado"; (b) aceitar o risco.
- **Recomendação: (a)** — é uma revisão anual de um documento que já existe;
  custo quase nulo, fecha 3 linhas da matriz.

## 2. Testar regularmente a eficácia das medidas — `SO-D-02.1-001`, `SO-D-10.3-001`

- **Forma empresarial:** programa permanente de testes de segurança com
  relatórios.
- **Forma proporcional (audit):** auto-revisão anual escrita pelos fundadores.
- **Opções:** (a) requisito ORG da auto-revisão anual; (b) aceitar o risco.
- **Recomendação: (a)** — nota: fusível natural com o dever 1 (uma revisão
  anual pode cobrir ambos com um único requisito, se assim o decidires).

## 3. Distribuição segura de actualizações e avisos — `SO-D-02.2-002`, `SO-D-05.2-002`, `SO-D-07.3-002`

- **Forma empresarial:** processo formal de gestão de vulnerabilidades com SLA
  de distribuição.
- **Forma proporcional (audit):** já resolvido pelo intake `ORG-INT-02` — um
  fluxo de pull-requests gerido satisfaz o dever para SaaS B2B.
- **Opções:** (a) requisito ORG curto que referencia `ORG-INT-02` como decisão
  de caso; (b) fechar sem escrever (já decidido no intake).
- **Recomendação: (b)** — escrever um requisito para citar outro é duplicação;
  o fecho contra `ORG-INT-02` é a forma que o caso já usa (precedente
  `ORG-INT-03` no DPO).

## 4. Disponibilidade das funções essenciais após incidente — `SO-D-04.2-002`

- **Forma empresarial:** capacidade de resiliência com postura de redundância
  permanente.
- **Forma proporcional (audit):** redundância da plataforma gerida + o RPO
  transportado por `RN5`.
- **Opções:** (a) requisito ORG "as funções essenciais (autenticação, tarefas,
  facturação) ficam disponíveis após incidente, com RPO declarado"; (b) risco.
- **Recomendação: (a)** — funde naturalmente com o dever 1 no mesmo documento.

## 5. Testes ao produto com relatórios escritos — `SO-D-10.3-002`

- **Forma empresarial:** regime de QA com relatórios de teste escritos por
  versão.
- **Forma proporcional (audit):** funde com a auto-revisão anual (dever 2).
- **Opções:** (a) absorver no requisito do dever 2; (b) risco.
- **Recomendação: (a) absorvido no dever 2** — mesmo artefacto, mesmo cadência.

## 6. Documentação técnica e avaliação de conformidade — `SO-D-09.3-002`, `SO-D-09.4-002`

- **Forma empresarial:** documentação técnica Annex II + procedimento de
  avaliação de conformidade antes da colocação no mercado.
- **Forma proporcional (audit):** para SaaS o produto É o serviço; a forma
  proporcional é uma nota de arquitectura curta, não o Annex II.
- **Opções:** (a) requisito ORG "manter uma nota de arquitectura e a declaração
  de conformidade CRA actualizadas a cada release maior"; (b) risco.
- **Recomendação: (a)** — a nota de arquitectura é o que a Parte 2 (threat
  model) vai precisar de qualquer forma; escrevê-la agora paga-se à frente.

## Resumo da recomendação

| Dever | Recomendação | Requisitos novos |
|---|---|---|
| 1. CIA/resiliência | escrever (a) | 1 |
| 2. Testar eficácia | escrever (a) | 1 |
| 3. Actualizações | fechar contra `ORG-INT-02` (b) | 0 |
| 4. Disponibilidade pós-incidente | escrever (a), fundido com 1 | 0 (partilha) |
| 5. Testes ao produto | absorver no dever 2 | 0 (partilha) |
| 6. Documentação técnica | escrever (a) | 1 |

Aceitando as recomendações: **+3 requisitos ORG** (Doc03 passa de 10 para ~13),
os 6 deveres saem de `pending-scale`, e a onda 5 fica totalmente desbloqueada
para o ensaio. As decisões registam-se aqui com data e vão ao registo da ronda
(`ROUND1_REGISTER` ou adenda do Doc03 §5→§3).
