# Locadora de Veículos — Projeto Prático de POO e UML

Projeto prático da disciplina para modelar uma locadora de veículos em Python, aplicando Programação Orientada a Objetos e UML.

## Clonar o repositório

```bash
git clone git@github.com:htu6n7yi/projeto_python_UFRPE.git
cd projeto_python_UFRPE
```

Se o repositório for privado, sua conta precisa ter acesso. Para SSH, configure sua chave no GitHub antes de clonar.

## Escopo

Sistema de backoffice operado via terminal (CLI) pelo vendedor. O vendedor cadastra clientes e veículos, consulta a disponibilidade da frota, registra locações e devoluções.

Regras de negócio implementadas:

- Não permite CPF de cliente nem placa de veículo duplicados.
- O cliente precisa ter no mínimo 18 anos.
- Só é possível alugar veículos disponíveis, com data de locação a partir de hoje e devolução prevista igual ou posterior à locação.
- A locação cobra no mínimo 1 diária.
- Uma devolução após a data prevista gera multa de 150% do valor da diária por dia de atraso.

## Como executar

Requer Python 3.9 ou superior, sem dependências externas. A partir da raiz do projeto:

```bash
python -m src.main
```

## Estado atual

- Classes de domínio e menu CLI implementados, atendendo aos requisitos da 2ª VA.
- Os quatro diagramas UML (Casos de Uso, Classes, Sequência e Atividades) estão em `images/`.
- Itens exclusivos da 3ª VA (classe abstrata com `abc`, exceção personalizada e persistência em arquivo) não foram implementados.

## Estrutura

```text
.
├── .gitignore
├── README.md
├── docs/
│   └── instrucoes-projeto/
│       └── instrucoes.md
├── images/
│   ├── 01 - Diagrama de Casos de Uso.drawio.png
│   ├── 02 - Diagrama de Classes.drawio.png
│   ├── 03 - Diagrama de Sequencia.drawio.png
│   └── 04 - Diagrama de Atividades.drawio.png
└── src/
    ├── __init__.py
    ├── main.py
    ├── pessoa.py
    ├── veiculo.py
    └── locacao.py
```

- `src/main.py`: menu interativo e ponto de entrada da aplicação.
- `src/pessoa.py`: superclasse `Pessoa` e subclasses `Vendedor` e `Cliente`.
- `src/veiculo.py`: classe `Veiculo`, com controle de disponibilidade.
- `src/locacao.py`: classes `Locacao` e `Pagamento`, com cálculo de valor total e multa.
- `images/`: diagramas UML exportados do draw.io.
- `docs/instrucoes-projeto/`: instruções originais da atividade.

## Aplicação dos pilares de POO

- **Herança:** `Vendedor` e `Cliente` herdam de `Pessoa` e usam `super()`.
- **Encapsulamento:** atributos protegidos (`_`) em `Pessoa` e privados (`__`) nas demais classes, acessados por métodos `get_`/`set_`.
- **Polimorfismo:** `exibir_dados()` é sobrescrito em `Vendedor` e `Cliente`.
- **Associação e composição:** `Locacao` associa `Cliente`, `Vendedor` e `Veiculo`, e cria internamente o seu `Pagamento` (composição).

## Diagramas UML

![Diagrama de Casos de Uso](images/01%20-%20Diagrama%20de%20Casos%20de%20Uso.drawio.png)

![Diagrama de Classes](images/02%20-%20Diagrama%20de%20Classes.drawio.png)

![Diagrama de Sequência — Realizar Locação](images/03%20-%20Diagrama%20de%20Sequencia.drawio.png)

![Diagrama de Atividades — Registrar Devolução](images/04%20-%20Diagrama%20de%20Atividades.drawio.png)

## Requisitos da atividade

Consulte as [instruções da atividade](docs/instrucoes-projeto/instrucoes.md) para ver os requisitos, entregas e critérios de avaliação da 2ª VA e da 3ª VA.
