## 1. Objetivo Geral

Desenvolver uma aplicação em **Python** aplicando os paradigmas da **Programação Orientada a Objetos (POO)**, acompanhada da respectiva modelagem arquitetural utilizando a **Linguagem de Modelagem Unificada (UML)**. O tema do sistema é de livre escolha da equipe (exemplos: sistema de gestão bibliotecária, locadora de veículos, clínica médica, e-commerce, controle acadêmico ou sistema bancário), desde que atenda integralmente aos requisitos técnicos exigidos.

## 2. Regras de Organização e Entrega

- **Formação das Equipes:** Grupos de **até 04 integrantes** (trabalhos individuais são permitidos apenas mediante justificativa prévia).
- **Data de Apresentação:** Encontro síncrono do dia **01/12/2026** (a ordem de apresentação será definida no início da aula, tempo de apresentação de cada grupo = 10 minutos no máximo).
- **Avaliação Individual:** Embora o desenvolvimento seja em grupo, **a nota será atribuída individualmente**. Durante a apresentação, todos os membros deverão demonstrar domínio sobre o código e os diagramas entregues, respondendo a arguições técnicas do docente.
- **Formato de Entrega (via AVA antes do início da aula de 01/12):**
  1. Arquivo compactado (`.zip`) contendo todos os arquivos-fonte em Python (`.py`) organizados e comentados, **ou** link para repositório público no GitHub.
  2. Documento único em formato **PDF** contendo a identificação dos integrantes, breve descrição do escopo do sistema e os **04 diagramas UML** legíveis.

## 3. Requisitos Técnicos Obrigatórios (Avaliação Regular 2ª VA — Máximo 7,0 pontos)

### A. Modelagem UML

O documento em PDF deve conter, obrigatoriamente, os seguintes diagramas coerentes entre si e com o código implementado:

1. **Diagrama de Casos de Uso:** Identificando atores, casos de uso principais e relacionamentos (`<<include>>` e/ou `<<extend>>`).
2. **Diagrama de Classes:** Representando todas as classes do sistema, seus atributos, métodos, visibilidade (`+`, `-`, `#`), multiplicidades e relacionamentos (associação, agregação/composição e herança).
3. **Diagrama de Sequência:** Ilustrando a troca de mensagens entre objetos em, pelo menos, **01 fluxo principal** do sistema (ex: realizar venda, efetuar empréstimo).
4. **Diagrama de Atividades:** Mapeando o fluxo de trabalho/decisões de um processo de negócio relevante do sistema.

### B. Implementação em Python (OO)

O código-fonte deve ser estruturado aplicando boas práticas de POO:

1. **Estrutura Mínima:** Possuir, no mínimo, **03 classes** distintas e funcionais (além do arquivo principal de execução `main.py`).
2. **Herança:** Implementar pelo menos **01 relação de herança** (superclasse e subclasse(s)) fazendo uso adequado do método `super()`.
3. **Encapsulamento:** Utilizar atributos privados/protegidos (convenção `_` ou `__`) com métodos de acesso/modificação (`@property` e `@setter` ou métodos *getters/setters* explícitos).
4. **Polimorfismo:** Sobrescrever (*override*) ao menos **01 método** da superclasse em uma classe filha, alterando ou especializando seu comportamento.
5. **Relacionamento entre Objetos:** Demonstrar associação, agregação ou composição entre classes (ex: um objeto `Pedido` contendo uma lista de objetos `Item`).
6. **Interface de Execução:** Menu interativo via terminal (CLI) que permita testar todas as funcionalidades cadastrais e operacionais em tempo de execução.

## 4. Critérios de Avaliação (Avaliação Regular — Total: 7,0 pontos)

A composição da nota regular da disciplina será dada por: **Exercícios no AVA (3,0 pts) + Projeto Prático (7,0 pts) = 10,0 pontos**.

| Critério Avaliado | Descrição detalhada | Pontuação Máxima |
|---|---|---:|
| **1. Modelagem UML** | Coerência entre os 4 diagramas (Casos de Uso, Classes, Sequência e Atividades), uso correto da notação UML e alinhamento com o código entregue. | **2,0 pts** |
| **2. Estrutura OO e Pilares** | Implementação correta das classes (mín. 3), encapsulamento, herança (`super()`), polimorfismo e associação/composição entre objetos. | **2,5 pts** |
| **3. Funcionamento e Execução** | Sistema executando sem erros de sintaxe ou exceções não tratadas, com menu funcional cobrindo o fluxo proposto. | **1,0 pt** |
| **4. Arguição Individual** | Domínio técnico demonstrado pelo aluno ao explicar trechos do código, decisões de modelagem e responder às perguntas do professor. | **1,5 pts** |
| **TOTAL** |  | **7,0 pts** |

> **Observação:** Caso o grupo entregue o projeto, mas um integrante falte à apresentação síncrona sem justificativa legal, ou não consiga explicar o funcionamento básico do código entregue, sua nota individual no critério de Arguição será zerada e os demais critérios poderão sofrer redução proporcional.

## 5. Diretrizes para 3ª VA (Total: 10,0 pontos)

Para os estudantes que realizarem a **2ª Chamada (3ª VA)**, o projeto será individual e valerá **10,0 pontos** (substituindo integralmente a nota da avaliação). Além de cumprir **todos os requisitos da etapa regular**, o projeto deverá incorporar os seguintes incrementos obrigatórios:

### Requisitos Adicionais Obrigatórios

1. **Ampliação de Classes:** Mínimo de **05 classes** funcionais.
2. **Abstração:** Utilização obrigatória do módulo `abc` (`ABC` e `@abstractmethod`) para definir ao menos **01 classe abstrata** na hierarquia de herança.
3. **Tratamento de Exceções:** Implementação de blocos `try / except` para validação de entradas do usuário e criação de pelo menos **01 exceção personalizada** herdando de `Exception`.
4. **Persistência de Dados:** Salvamento e carregamento automático dos dados do sistema em arquivos externos (`.json`, `.csv` ou `.txt`), garantindo que as informações não sejam perdidas ao encerrar o programa.
5. **UML Expandida:** Inclusão de **02 Diagramas de Sequência** (um para fluxo de sucesso e outro contemplando fluxo alternativo/exceção).
