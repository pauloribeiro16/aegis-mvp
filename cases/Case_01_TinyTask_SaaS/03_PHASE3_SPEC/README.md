# Phase 3 — Specification Baseline (TinyTask SaaS)

> **Case Study:** Case 01 — TinyTask SaaS (B2B Task Management Multi-Tenant Platform)  
> **Lifecycle Phase:** AEGIS Phase 3 — Specification  
> **Reference Standard:** Volere Requirements Process & GPTools Standards (E1.1 / E1.2)  
> **Status:** Functional Baseline Active  

---

## 1. Overview & Directory Structure

This directory houses the formal **Functional Requirements and System Use Cases Baseline** for TinyTask SaaS, structured following the proven methodology of GPTools:

```text
cases/Case_01_TinyTask_SaaS/03_PHASE3_SPEC/
├── README.md                                    # (This file) Overview and roadmap for Phase 3
├── Doc01_Requirements_Elicitation_and_PUC.md    # GPTools E1.1 standard: Context, Data, Actors, PUCs, & MoSCoW Requirements
└── Doc02_System_Use_Cases.md                    # GPTools E1.2 standard: Level-0 & Level-1 System Use Cases ({U.C.1} .. {U.C.6})
```

---

## 2. Document Map

### 2.1 [`Doc01_Requirements_Elicitation_and_PUC.md`](file:///c:/Users/paulo.ribeiro/OneDrive%20-%20Instituto%20CCG%20ZGDV/Ambiente%20de%20Trabalho/Projetos_PhD/aegis-mvp/cases/Case_01_TinyTask_SaaS/03_PHASE3_SPEC/Doc01_Requirements_Elicitation_and_PUC.md)
*Estrutura 1:1 com o padrão **GPTools E1.1 — Modelo AS-IS / TO-BE & Levantamento de Requisitos***:
- **Parte I – Âmbito:** Objetivo, descrição do problema, posição do produto, impacto esperado, características principais, stakeholders, utilizadores do sistema e restrições.
- **Parte II – As-Is:** Papéis em contexto empresarial, fluxos de processos manuais com tabelas de dados (`['Dados', 'Tipo de Dados', 'Obrigatoriedade']`) e suporte de TI.
- **Parte III – To-Be:**
  - Expectativas do cliente (`['Expectativas Iniciais', 'Descrição']`).
  - Atores do sistema (`['Ator', 'Descrição']`).
  - Tabela sumária de Requisitos Funcionais MoSCoW (`['ID', 'ID', 'Requisito', 'Prioridade', 'Restrições']`).
  - **Tabelas de especificação detalhada de requisitos (R1 a R12)** com a estrutura exata de 7 linhas e 1 coluna do Word:
    `ID / Nome`, `Descrição`, `Origem do Requisito`, `Interfaces`, `Dependências`, `Problemas Identificados`, `Prioridade`.
  - Requisitos Não Funcionais (`['ID', 'Requisito', 'Prioridade', 'Tipo']`).
  - Tabela sumária de Casos de Uso do Produto (PUC) (`['PUC', 'Nome do PUC', 'Atores/Utilizadores', 'Input e Output']`).
  - Modelo de Casos de Uso com diagrama Mermaid de Nível 0 e descrição dos Casos de Uso de Nível 1.

### 2.2 [`Doc02_System_Use_Cases.md`](file:///c:/Users/paulo.ribeiro/OneDrive%20-%20Instituto%20CCG%20ZGDV/Ambiente%20de%20Trabalho/Projetos_PhD/aegis-mvp/cases/Case_01_TinyTask_SaaS/03_PHASE3_SPEC/Doc02_System_Use_Cases.md)
*Estrutura 1:1 com o padrão **GPTools E1.2 — Análise de Requisitos & Casos de Uso***:
- **Enquadramento Metodológico:** Abordagem Volere e Decomposição Triangular.
- **Modelo de Contexto de Trabalho:** Diagrama Mermaid de contexto com atores humanos, núcleo da aplicação e serviços externos.
- **Tabela Sumária de Casos de Uso do Produto (PUC):** Entradas (`in`) e saídas (`out`) para cada interação.
- **Casos de Uso de Sistema (`{U.C. 1}` a `{U.C. 8}`):** Detalhamento até ao **Nível 1** (`{U.C.n.m}`), puramente funcional.
- **Disciplina de Granularidade:** Estritamente até ao Nível 1. **Sem nós folha (*leaf nodes*)** (`{U.C.n.m.k}`) nem sequências passo-a-passo de execução.

---

## 3. Downstream Phase 3 Synthesis

Once the functional baseline is locked, the next step in Phase 3 is synthesizing **Security & Privacy Requirements** (`Doc03_Security_Privacy_Requirements.md`). 

This synthesis will cross-cut these functional capabilities with:
1. **Phase 2 Operational Objectives (`Doc01_Operational_Objectives.md`):** Dual GDPR/CRA operational rules (`PO-D-XX.Y-NNN` and `SO-D-XX.Y-NNN`).
2. **Phase 2 Secure Design Principles (`Doc02_Secure_Design_Principles.md`):** 7 foundational engineering principles (`PRIN-ENG-01` through `PRIN-ENG-07`).
3. **AEGIS Autonomous Skills (`baseline/skills/`):** Automated auditing across Attack Surface Analysis, Trust Boundary Analysis, Least Privilege, Data Minimization, and Secure Defaults.
