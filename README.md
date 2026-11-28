# Locadora de Veículos

Sistema de locação de veículos em Python, desenvolvido com Programação Orientada a Objetos e modelado em UML.

## Clonar o repositório

```bash
git clone git@github.com:htu6n7yi/projeto_python_UFRPE.git
cd projeto_python_UFRPE
```

## Escopo

Sistema de backoffice operado via terminal (CLI) pelo vendedor. O vendedor cadastra clientes e veículos, consulta a disponibilidade da frota, registra locações e devoluções.

Regras de negócio implementadas:

- Não permite CPF de cliente nem placa de veículo duplicados.
- O cliente precisa ter no mínimo 18 anos.
- Só é possível alugar veículos disponíveis, com data de locação a partir de hoje e devolução prevista igual ou posterior à locação.
- A locação cobra no mínimo 1 diária.
- Uma devolução após a data prevista gera multa de 150% do valor da diária por dia de atraso.

## Como executar

Requer Python 3.9+.

```bash
python -m src.main
```

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

## POO

- Herança: `Vendedor` e `Cliente` herdam de `Pessoa`.
- Encapsulamento: atributos protegidos e privados com getters e setters.
- Polimorfismo: `exibir_dados()` sobrescrito nas subclasses.
- Composição: `Locacao` cria e mantém o seu `Pagamento`.

## Diagramas UML

### Diagrama de Casos de Uso

![Diagrama de Casos de Uso](images/01%20-%20Diagrama%20de%20Casos%20de%20Uso.drawio.png)

### Diagrama de Classes

![Diagrama de Classes](images/02%20-%20Diagrama%20de%20Classes.drawio.png)

### Diagrama de Sequência

![Diagrama de Sequência](images/03%20-%20Diagrama%20de%20Sequencia.drawio.png)

### Diagrama de Atividades

![Diagrama de Atividades](images/04%20-%20Diagrama%20de%20Atividades.drawio.png)

## Requisitos da atividade

Consulte as [instruções da atividade](docs/instrucoes-projeto/instrucoes.md) para ver os requisitos, entregas e critérios de avaliação da 2ª VA e da 3ª VA.
