# Documentação de Arquitetura e Modelagem UML
## Sistema de Gestão para Locadora de Veículos (Backoffice CLI)

**Instituição:** Universidade Federal Rural de Pernambuco (UFRPE) — Bacharelado em Sistemas de Informação (BSI)  
**Avaliação:** 2ª VA  
**Equipe:**  
Jose Carlos Cavalcanti  
Orquídea
Raphael Almeida da Silva

---

## 1. Escopo do Sistema e Arquitetura POO

O projeto consiste em um sistema de *backoffice* operado via terminal (CLI) para o gerenciamento operacional de uma locadora de veículos. O software é controlado exclusivamente pelo ator **Vendedor** no balcão de atendimento, centralizando o cadastro de clientes e da frota, a consulta de catálogo, a efetivação de contratos de locação e o encerramento de devoluções.

### Regras de Negócio Implementadas
* **Controle de Frota e Cadastros:** Impede duplicidade de CPF entre clientes e de placas entre veículos, além de exigir idade mínima de 18 anos para locatários. Todo veículo recém-cadastrado ingressa automaticamente com status disponível.
* **Contratualização e Pagamento:** A locação só é permitida para veículos disponíveis e datas vigentes (bloqueando locações retroativas ou devoluções anteriores à retirada), garantindo a cobrança mínima de 1 diária.
* **Devolução e Multa:** No retorno do veículo, caso a data real de entrega ultrapasse a data prevista em contrato, o sistema aplica automaticamente uma multa equivalente a 150% do valor da diária por dia de atraso e restabelece a disponibilidade do automóvel na frota.

### Aplicação dos Pilares de Orientação a Objetos
* **Herança:** A superclasse `Pessoa` concentra os dados cadastrais comuns e os transmite às subclasses `Vendedor` e `Cliente`.
* **Encapsulamento:** Atributos protegidos (`#` / `_`) na superclasse `Pessoa` permitem reutilização controlada na hierarquia, enquanto atributos privados (`-` / `__`) nas demais classes protegem o estado interno dos objetos, expondo apenas métodos públicos (`+`) de leitura e atualização.
* **Polimorfismo:** O método `exibir_dados()` definido em `Pessoa` é sobrescrito (*override*) em `Vendedor` (exibindo a CTPS) e em `Cliente` (exibindo o CPF).
* **Associação e Composição:** `Locacao` associa-se a `Cliente`, `Vendedor` e `Veiculo`, e estabelece uma relação de **composição** estrita com `Pagamento` — o registro financeiro é instanciado internamente pela locação e não existe de forma isolada no sistema.

---

## 2. Diagrama de Casos de Uso

Representa as funcionalidades expostas no menu principal ao operador (`Vendedor`), destacando as inclusões obrigatórias (`«include»`) de verificação de catálogo e registro de pagamento ao alugar um veículo, bem como as extensões condicionais (`«extend»`) para filtragem de veículos disponíveis e cálculo de multa em devoluções com atraso.

![Diagrama de Casos de Uso](images/01%20-%20Diagrama%20de%20Casos%20de%20Uso.drawio.png)

---

## 3. Diagrama de Classes

Estrutura estática do sistema com tipagem de atributos, assinaturas de métodos, modificadores de visibilidade oficiais da UML (`+`, `-`, `#`), relações de herança, associações com multiplicidades e composição entre `Locacao` e `Pagamento`.

![Diagrama de Classes](images/02%20-%20Diagrama%20de%20Classes.drawio.png)

---

## 4. Diagrama de Sequência — Fluxo: Realizar Locação

Demonstra a troca cronológica de mensagens entre o ator `Vendedor`, o controlador `:Sistema` (`main.py`) e as instâncias de `Veiculo`, `Locacao` e `Pagamento`, contemplando o bloco condicional (`alt`) para validação prévia de disponibilidade do veículo antes da instanciação do contrato.

![Diagrama de Sequência](images/03%20-%20Diagrama%20de%20Sequencia.drawio.png)

---

## 5. Diagrama de Atividades — Fluxo: Registrar Devolução

Mapeia o fluxo de trabalho entre as raias `Vendedor` e `Sistema` durante a devolução de um veículo, detalhando os nós de decisão para localização do contrato ativo, apuração condicional de atraso com cálculo de multa e liberação final do automóvel no pátio.

![Diagrama de Atividades](images/04%20-%20Diagrama%20de%20Atividades.drawio.png)