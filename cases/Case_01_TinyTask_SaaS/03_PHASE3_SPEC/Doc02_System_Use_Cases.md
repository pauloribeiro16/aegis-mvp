# E1.2 – TinyTask SaaS: Análise de Requisitos e Casos de Uso de Sistema

## Sumário Executivo

O presente documento constitui o relatório técnico de análise de requisitos e especificação de casos de uso de sistema para a plataforma **TinyTask SaaS**. Este documento complementa o modelo AS-IS / TO-BE (*Doc01*) e formaliza o desenho funcional da aplicação, estruturando a interação entre os diferentes atores operacionais e os serviços da plataforma.

A abordagem metodológica adotada baseia-se na decomposição funcional e na especificação formal de casos de uso até ao nível 1 de refinamento (`{U.C.n.m}`), omitindo deliberadamente passos sequenciais de execução e decomposição em nós folha (*leaf nodes*), em estrito alinhamento com a diretiva de engenharia de requisitos estabelecida no projeto de referência.

As funcionalidades aqui especificadas refletem exclusivamente os requisitos de negócio e a experiência de utilização da aplicação, servindo de base funcional neutra para a subsequente aplicação das regras de segurança, privacidade e conformidade regulamentar da metodologia AEGIS.

---

## Índice

- [1. Introdução](#1-introdução)
- [2. Abordagem aos Requisitos do Sistema](#2-abordagem-aos-requisitos-do-sistema)
  - [2.1 A Abordagem Volere e Decomposição Triangular](#21-a-abordagem-volere-e-decomposição-triangular)
  - [2.2 Fronteira de Refinamento (Sem Nós Folha / Leaf Nodes)](#22-fronteira-de-refinamento-sem-nós-folha--leaf-nodes)
  - [2.3 Requisitos Não-Funcionais](#23-requisitos-não-funcionais)
- [3. Análise de Requisitos](#3-análise-de-requisitos)
  - [3.1 Modelo de Contexto de Trabalho](#31-modelo-de-contexto-de-trabalho)
  - [3.2 Tabela de Casos de Uso do Produto (PUC)](#32-tabela-de-casos-de-uso-do-produto-puc)
- [4. Casos de Uso da Aplicação de Domínio](#4-casos-de-uso-da-aplicação-de-domínio)
  - [4.1 Atores do Sistema](#41-atores-do-sistema)
  - [4.2 Casos de Uso de Sistema](#42-casos-de-uso-de-sistema)
    - [4.2.1 Caso de Uso 1 – Autenticação e Gestão de Identidade](#421-caso-de-uso-1--autenticação-e-gestão-de-identidade)
    - [4.2.2 Caso de Uso 2 – Administração de Espaços de Trabalho e Membros](#422-caso-de-uso-2--administração-de-espaços-de-trabalho-e-membros)
    - [4.2.3 Caso de Uso 3 – Gestão de Projetos](#423-caso-de-uso-3--gestão-de-projetos)
    - [4.2.4 Caso de Uso 4 – Gestão e Execução de Tarefas](#424-caso-de-uso-4--gestão-e-execução-de-tarefas)
    - [4.2.5 Caso de Uso 5 – Gestão de Anexos e Documentos de Suporte](#425-caso-de-uso-5--gestão-de-anexos-e-documentos-de-suporte)
    - [4.2.6 Caso de Uso 6 – Comunicação Colaborativa e Alertas](#426-caso-de-uso-6--comunicação-colaborativa-e-alertas)
    - [4.2.7 Caso de Uso 7 – Gestão Comercial e Faturação](#427-caso-de-uso-7--gestão-comercial-e-faturação)
    - [4.2.8 Caso de Uso 8 – Gestão do Ciclo de Vida da Conta e Dados](#428-caso-de-uso-8--gestão-do-ciclo-de-vida-da-conta-e-dados)
- [5. Requisitos Não-Funcionais](#5-requisitos-não-funcionais)
- [6. Conclusões](#6-conclusões)
- [7. Bibliografia](#7-bibliografia)
- [Histórico de Versões](#histórico-de-versões)

---

## 1. Introdução

A plataforma **TinyTask SaaS** destina-se a simplificar a colaboração operacional de equipas distribuídas, unificando a gestão de projetos, a atribuição de tarefas e o controlo de prazos num ambiente acessível e intuitivo.

O presente documento formaliza a arquitetura funcional da plataforma, apresentando o modelo de contexto, os atores e o refinamento dos Casos de Uso do Sistema correspondentes aos requisitos identificados no documento *Doc01*.

---

## 2. Abordagem aos Requisitos do Sistema

### 2.1 A Abordagem Volere e Decomposição Triangular

A especificação de requisitos baseia-se nos princípios de engenharia de software da abordagem Volere, combinando:
1. **Identificação da Fronteira do Produto:** Determinação rigorosa dos dados que entram (*inputs*) e que saem (*outputs*) do sistema através dos Casos de Uso do Produto (*Product Use Cases* — PUC).
2. **Decomposição Triangular de Casos de Uso:** Estruturação hierárquica partindo do nível macro (Nível 0) para sub-casos de nível 1, assegurando rastreabilidade direta com os requisitos funcionais priorizados por MoSCoW.

### 2.2 Fronteira de Refinamento (Sem Nós Folha / Leaf Nodes)

De acordo com a diretriz metodológica explícita deste projeto:
- **Limite Superior de Granularidade:** Os casos de uso são refinados até ao **Nível 1** (`{U.C.n.m}`).
- **Omissão Estrita de Nós Folha:** O documento **não decompõe** os casos de uso em sub-sub-casos de nível folha (`{U.C.n.m.k}`) nem descreve passos procedimentais sequenciais (passo 1, passo 2, etc.).
- **Foco Funcional Puro:** As descrições centram-se nas capacidades de negócio que o sistema coloca ao dispor dos atores, mantendo total neutralidade relativamente a tecnologias ou mecanismos físicos de segurança.

### 2.3 Requisitos Não-Funcionais

Os requisitos não-funcionais (NFR) enquadram o desempenho, disponibilidade e usabilidade do sistema, garantindo tempos de resposta céleres e isolamento rigoroso entre inquilinos (*tenants*).

---

## 3. Análise de Requisitos

### 3.1 Modelo de Contexto de Trabalho

O modelo de contexto descreve as fronteiras de comunicação entre o sistema TinyTask e os atores externos intervenientes:

```mermaid
flowchart TD
    subgraph Atores_Humanos["Atores Humanos"]
        UA["Utilizador Não Autenticado"]
        WM["Workspace Member"]
        WA["Workspace Admin"]
        WO["Workspace Owner"]
        WV["Workspace Viewer"]
    end

    subgraph Plataforma_TinyTask["Plataforma TinyTask SaaS"]
        Core["Núcleo Operacional e Base de Dados"]
    end

    subgraph Sistemas_Externos["Sistemas e Serviços Externos"]
        Stripe["Gateway Stripe (Pagamentos)"]
        MailService["Serviço de Correio Transacional"]
    end

    UA -- "Formulário de Registo / Login" --> Core
    WM -- "Criação de Tarefas, Comentários e Anexos" --> Core
    WA -- "Gestão de Membros e Projetos" --> Core
    WO -- "Subscrição Comercial e Faturação" --> Core
    WV -- "Consulta de Leitura" --> Core

    Core -- "Despacho de Notificações e Confirmações" --> MailService
    Core <--> "Sessões Checkout e Webhooks" --> Stripe
```

### 3.2 Tabela de Casos de Uso do Produto (PUC)

A tabela seguinte estabelece a correspondência entre os PUC e os dados de entrada e saída:

*Tabela 1 - Tabela sumária de Casos de Uso do Produto (PUC)*

| PUC | Nome do PUC | Atores/Utilizadores | Input e Output |
|---|---|---|---|
| **1.1** | Registar e Ativar Conta de Utilizador | Utilizador Não Autenticado, Serviço de Email | **(in)** Nome, email e palavra-passe<br>**(out)** Email com hiperligação de verificação de conta |
| **1.2** | Autenticar Utilizador e Gerir Sessão | Utilizador Registado | **(in)** Email e palavra-passe<br>**(out)** Sessão autenticada e lista de workspaces autorizados |
| **1.3** | Recuperar Palavra-passe de Acesso | Utilizador Registado, Serviço de Email | **(in)** Endereço de email do utilizador<br>**(out)** Hiperligação temporária para redefinição de credenciais |
| **2.1** | Criar Espaço de Trabalho (Workspace) | Workspace Owner | **(in)** Nome do workspace e slug de identificação<br>**(out)** Workspace instanciado com o criador no papel de Owner |
| **2.2** | Convidar e Administrar Membros de Equipa | Workspace Admin, Workspace Owner, Serviço de Email | **(in)** Email do convidado e papel pretendido (Admin, Member, Viewer)<br>**(out)** Notificação de convite e membro associado ao workspace |
| **2.3** | Personalizar Definições do Workspace | Workspace Admin, Workspace Owner | **(in)** Nome atualizado e ficheiro de logótipo (até 2 MB)<br>**(out)** Perfil visual do workspace atualizado para a equipa |
| **3.1** | Criar e Parametrizar Novo Projeto | Workspace Admin, Workspace Member | **(in)** Título, descrição do âmbito e visibilidade do projeto<br>**(out)** Projeto inicializado e acessível na barra de projetos |
| **3.2** | Arquivar Projeto Concluído | Workspace Admin, Workspace Owner | **(in)** Seleção do projeto a arquivar<br>**(out)** Projeto em estado de só de leitura oculto da vista diária |
| **4.1** | Criar e Atribuir Nova Tarefa | Workspace Member, Workspace Admin | **(in)** Título, descrição, prioridade, membro responsável e prazo<br>**(out)** Cartão de tarefa criado na coluna "To-Do" e notificação ao membro |
| **4.2** | Atualizar Estado da Tarefa no Kanban | Workspace Member, Workspace Admin | **(in)** Arrastamento do cartão de tarefa para nova coluna de estado<br>**(out)** Estado da tarefa atualizado e evento registado no histórico |
| **4.3** | Pesquisar e Filtrar Tarefas | Todos os Utilizadores | **(in)** Critérios de pesquisa (responsável, estado, prioridade, texto livre)<br>**(out)** Vista do quadro Kanban e listas filtradas em tempo real |
| **5.1** | Anexar Documento a Cartão de Tarefa | Workspace Member, Workspace Admin | **(in)** Seleção de ficheiro local (até 25 MB)<br>**(out)** Ficheiro armazenado e associado à lista de anexos da tarefa |
| **5.2** | Descarregar e Eliminar Anexo | Workspace Member, Workspace Admin | **(in)** Ordem de descarregamento ou eliminação de anexo<br>**(out)** Ficheiro transferido para o posto local ou removido do registo |
| **6.1** | Publicar Comentário e Mencionar Colaboradores | Workspace Member, Workspace Admin | **(in)** Texto formatado em Markdown com menções (@membro)<br>**(out)** Comentário publicado e notificação emitida aos visados |
| **6.2** | Consultar Centro de Notificações | Utilizador Autenticado | **(in)** Acesso ao painel de alertas do utilizador<br>**(out)** Lista de notificações de menções e atribuições não lidas |
| **7.1** | Subscrever e Atualizar Plano Comercial | Workspace Owner, Gateway de Pagamento (Stripe) | **(in)** Seleção de plano Pro/Enterprise e dados de faturação<br>**(out)** Confirmação de subscrição e quota de membros atualizada |
| **7.2** | Processar Notificação de Cobrança | Gateway de Pagamento (Stripe), Backend TinyTask | **(in)** Mensagem assíncrona de webhook com estado do pagamento<br>**(out)** Estado do plano reconciliado na base de dados do workspace |
| **8.1** | Exportar Dados Pessoais e do Workspace | Utilizador Autenticado, Workspace Owner | **(in)** Pedido de exportação (JSON pessoal ou ZIP de workspace)<br>**(out)** Ficheiro compactado disponibilizado para descarregamento |
| **8.2** | Encerrar Conta de Utilizador | Utilizador Autenticado, Serviço de Email | **(in)** Confirmação de encerramento da conta de utilizador<br>**(out)** Conta desativada, nome anonimizado e email de confirmação |

---

## 4. Casos de Uso da Aplicação de Domínio

### 4.1 Atores do Sistema

Os utilizadores e sistemas externos intervenientes são:
- **Workspace Owner:** Responsável contratual e administrativo supremo do espaço de trabalho.
- **Workspace Admin:** Gestor operacional que administra membros, projetos e permissões.
- **Workspace Member:** Colaborador que cria tarefas, anexa ficheiros e publica comentários.
- **Workspace Viewer:** Convidado externo ou auditor com privilégios exclusivos de leitura.
- **Gateway de Pagamentos (Stripe):** Entidade externa encarregada das transações de subscrição.
- **Serviço de Email:** Subsistema encarregado do envio de notificações transacionais.

### 4.2 Casos de Uso de Sistema

#### 4.2.1 Caso de Uso 1 – Autenticação e Gestão de Identidade

Este caso de uso abrange as funcionalidades de entrada na plataforma e gestão de credenciais:

- **{U.C. 1.1} Registar Nova Conta:** O utilizador não autenticado submete os dados de inscrição (nome, email e palavra-passe). O sistema valida a unicidade do endereço e envia uma ligação de confirmação para ativação da conta.
- **{U.C. 1.2} Autenticar Credenciais:** O utilizador introduz o seu email e palavra-passe. O sistema valida as credenciais e fornece uma sessão autenticada, carregando a lista de workspaces associados.
- **{U.C. 1.3} Recuperar Credenciais:** O utilizador solicita a recuperação de acesso fornecendo o email de registo, recebendo uma hiperligação temporária para redefinir a palavra-passe.

#### 4.2.2 Caso de Uso 2 – Administração de Espaços de Trabalho e Membros

Este caso de uso agrupa a gestão organizacional e de equipa:

- **{U.C. 2.1} Criar Espaço de Trabalho:** Qualquer utilizador registado pode criar um novo workspace, tornando-se o seu proprietário primário (*Workspace Owner*).
- **{U.C. 2.2} Convidar e Gerir Membros:** Permite aos administradores emitir convites por email e gerir a atribuição de papéis (Admin, Member, Viewer), respeitando a lotação do plano comercial contratado.
- **{U.C. 2.3} Parametrizar Workspace:** Permite a edição do nome da organização e o carregamento do logótipo corporativo (ficheiro de imagem até 2 MB).

#### 4.2.3 Caso de Uso 3 – Gestão de Projetos

Este caso de uso organiza o portfólio de trabalho do workspace:

- **{U.C. 3.1} Criar e Parametrizar Projeto:** O administrador ou membro cria novos projetos, configurando o nome, descrição do âmbito e restrições de visibilidade interna.
- **{U.C. 3.2} Arquivar Projeto:** Permite colocar um projeto concluído no arquivo histórico da organização, bloqueando novas edições e mantendo os dados para consulta.

#### 4.2.4 Caso de Uso 4 – Gestão e Execução de Tarefas

Este caso de uso constitui o núcleo operacional da plataforma:

- **{U.C. 4.1} Criar e Atribuir Tarefa:** Permite registar tarefas com título obrigatório, descrição em texto livre, prazo de conclusão, prioridade visual e responsável pela execução.
- **{U.C. 4.2} Gerir Estados no Kanban:** O utilizador visualiza e transita tarefas entre as fases do fluxo de trabalho ("To-Do", "In-Progress", "Under-Review", "Done") através de arrastamento interativo.
- **{U.C. 4.3} Filtrar e Pesquisar Tarefas:** Permite pesquisar tarefas e filtrar listas por responsável, estado e prioridade, atualizando os dados dinamicamente.

#### 4.2.5 Caso de Uso 5 – Gestão de Anexos e Documentos de Suporte

Este caso de uso rege o repositório documental associado às tarefas:

- **{U.C. 5.1} Carregar Anexo para Tarefa:** Permite anexar documentos, folhas de cálculo ou imagens diretamente a um cartão de tarefa, com limite estrito de 25 MB por anexo.
- **{U.C. 5.2} Descarregar e Remover Anexo:** Permite descarregar ficheiros para o posto local e autoriza o membro que enviou ou o administrador a eliminar anexos.

#### 4.2.6 Caso de Uso 6 – Comunicação Colaborativa e Alertas

Este caso de uso centraliza a discussão operacional e a notificação de equipa:

- **{U.C. 6.1} Publicar Comentários em Tarefas:** Permite a troca de mensagens em fio de discussão contextual dentro de cada tarefa com suporte para sintaxe Markdown.
- **{U.C. 6.2} Notificar e Mencionar Colaboradores:** Reconhece menções com "@" nos comentários e gera notificações no centro de alertas e resumos por email.

#### 4.2.7 Caso de Uso 7 – Gestão Comercial e Faturação

Este caso de uso gere as subscrições comerciais e a integração com a gateway Stripe:

- **{U.C. 7.1} Subscrever e Alterar Plano:** O Workspace Owner seleciona o plano comercial pretendido e é direcionado para a plataforma de pagamento seguro Stripe Checkout.
- **{U.C. 7.2} Processar Cobrança e Quotas:** O sistema recebe notificações assíncronas da Stripe via webhooks, atualizando as quotas de membros do workspace.

#### 4.2.8 Caso de Uso 8 – Gestão do Ciclo de Vida da Conta e Dados

Este caso de uso garante a transparência, portabilidade e encerramento de conta:

- **{U.C. 8.1} Exportar Dados:** O utilizador pode gerar um ficheiro JSON com os seus dados pessoais e o Workspace Owner pode gerar um ficheiro ZIP completo do workspace.
- **{U.C. 8.2} Desativar e Encerrar Conta:** O utilizador pode encerrar a sua conta de forma autónoma, ficando as credenciais invalidadas, o nome anonimizado nas tarefas e recebendo um comprovativo por correio eletrónico.

---

## 5. Requisitos Não-Funcionais

Conforme especificado no documento *Doc01*, a aplicação obedece aos seguintes parâmetros não-funcionais:
- **Desempenho (RN1):** Carregamento de quadros com até 200 tarefas em tempo inferior a 500 ms.
- **Disponibilidade (RN2):** Disponibilidade mínima de serviço de 99,5%.
- **Usabilidade (RN3):** Desenho responsivo para ecrãs móveis e desktop a partir de 375 px.
- **Escalabilidade (RN4):** Capacidade para 50 000 tarefas por workspace sem quebra de resposta.
- **Recuperabilidade (RN5):** Cópias de segurança diárias com RPO inferior a 24 horas.
- **Internacionalização (RN6):** Suporte de interface em Português e Inglês.
- **Interoperabilidade (RN7):** Integração Stripe via chamadas HTTPS autenticadas.
- **Multi-Tenancy (RN8):** Segregação lógica integral de dados entre diferentes workspaces.

---

## 6. Conclusões

A presente especificação formaliza a totalidade dos requisitos funcionais e dos casos de uso de sistema para a plataforma **TinyTask SaaS**, fornecendo uma base sólida, rigorosa e puramente funcional.

Com este documento concluído, fica plenamente delimitado o âmbito funcional sobre o qual a metodologia AEGIS aplicará subsequentemente as suas camadas de análise de ameaças, superfícies de ataque e objetivos operacionais de segurança e privacidade (Fase 2 e Fase 3).

---

## Bibliografia

1. Cockburn, A. (2000). *Writing Effective Use Cases*. Addison-Wesley Professional.
2. Robertson, S., & Robertson, J. (2012). *Mastering the Requirements Process: Getting Requirements Right* (3rd ed.). Addison-Wesley Professional.
3. Fowler, M. (2003). *UML Distilled: A Brief Guide to the Standard Object Modeling Language* (3rd ed.). Addison-Wesley Professional.

---

## Histórico de Versões

| Versão | Data | Autor | Notas de Modificação |
|---|---|---|---|
| **1.0.0** | 2026-09-23 | Equipa Técnica AEGIS | Criação inicial da especificação de Casos de Uso de Sistema (Doc02) em conformidade com o padrão E1.2 do GPTools, contemplando o diagrama de contexto, a tabela sumária de PUC e o refinamento até ao nível 1 sem nós folha. |
