# Projeto Prático de POO e UML

Repositório inicial do projeto prático da disciplina. O tema e as regras de negócio ainda serão definidos pela equipe; por enquanto, o projeto contém apenas a estrutura-base em Python.

## Clonar o repositório

```bash
git clone git@github.com:htu6n7yi/projeto_python_UFRPE.git
cd projeto_python_UFRPE
```

Se o repositório for privado, sua conta precisa ter acesso. Para SSH, configure sua chave no GitHub antes de clonar.

## Estado atual

- Tema e escopo do sistema: ainda serão definidos.
- Código funcional e menu de terminal: ainda não implementados.
- Não há dependências externas definidas até o momento.
- A pasta `docs/instrucoes-projeto/` contém as instruções recebidas em Markdown e PDF. Os diagramas UML e o PDF final do trabalho serão adicionados quando forem produzidos.

## Estrutura inicial

```text
.
├── .gitignore
├── README.md
├── docs/
│   └── instrucoes-projeto/
│       ├── instrucoes.md
│       └── instrucoes.pdf
└── src/
    ├── __init__.py
    ├── main.py
    ├── models/
    │   └── __init__.py
    └── services/
        └── __init__.py
```

- `src/models/`: local para as classes e entidades do domínio.
- `src/services/`: local para regras de negócio e operações do sistema.
- `src/main.py`: ponto de entrada previsto para a aplicação e o menu CLI.
- `docs/instrucoes-projeto/`: instruções originais da atividade em Markdown e PDF.
- `docs/`: local para os diagramas UML e documentos finais do projeto.

Os arquivos Python são apenas marcadores da estrutura neste momento. Quando houver uma aplicação implementada, a execução poderá ser feita a partir da raiz com `python -m src.main`.

## Requisitos da atividade

Consulte as [instruções em Markdown](docs/instrucoes-projeto/instrucoes.md) ou baixe a [versão PDF](docs/instrucoes-projeto/instrucoes.pdf) para ver os requisitos, entregas e critérios de avaliação da 2ª VA e da 3ª VA.
