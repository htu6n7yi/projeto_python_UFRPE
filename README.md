# Locadora de Veículos — Projeto Prático de POO e UML

Projeto prático da disciplina para modelar uma locadora de veículos em Python, aplicando Programação Orientada a Objetos e UML.

## Clonar o repositório

```bash
git clone git@github.com:htu6n7yi/projeto_python_UFRPE.git
cd projeto_python_UFRPE
```

Se o repositório for privado, sua conta precisa ter acesso. Para SSH, configure sua chave no GitHub antes de clonar.

## Escopo

O vendedor cadastra clientes e veículos, consulta a disponibilidade, registra locações e devoluções. Uma devolução após a data prevista gera uma multa; a regra de cálculo ainda precisa ser definida pela equipe.

## Estado atual

- O escopo e a arquitetura proposta estão documentados.
- Os cinco diagramas UML estão em `docs/diagramas/` como fontes PlantUML.
- As classes de domínio, a persistência JSON e o menu CLI ainda precisam ser implementados.
- Não há dependências externas definidas para a aplicação.

## Estrutura proposta

```text
.
├── .gitignore
├── README.md
├── docs/
│   ├── Planejamento.md
│   ├── diagramas/
│   │   ├── fontes/
│   │   │   ├── casos-de-uso.puml
│   │   │   ├── classes.puml
│   │   │   ├── sequencia-locacao-sucesso.puml
│   │   │   ├── sequencia-locacao-indisponivel.puml
│   │   │   ├── atividades-devolucao.puml
│   │   │   └── README.md
│   │   ├── imagens/
│   │   │   ├── casos-de-uso.png
│   │   │   ├── classes.png
│   │   │   ├── sequencia-locacao-sucesso.png
│   │   │   ├── sequencia-locacao-indisponivel.png
│   │   │   ├── atividades-devolucao.png
│   │   │   └── README.md
│   │   ├── apresentacao/
│   │   │   └── README.md
│   │   └── README.md
│   └── instrucoes-projeto/
│       ├── instrucoes.md
│       └── instrucoes.pdf
└── src/
    ├── __init__.py
    ├── main.py
    ├── exceptions.py
    ├── models/
    │   ├── pessoa.py
    │   ├── cliente.py
    │   ├── vendedor.py
    │   ├── veiculo.py
    │   ├── locacao.py
    │   └── pagamento.py
    ├── services/
    │   └── locadora_service.py
    └── repositories/
        └── arquivo_json.py
```

- `src/models/`: entidades; `Cliente` e `Vendedor` especializam `Pessoa`.
- `src/services/`: regras de negócio para cadastro, consulta, locação e devolução.
- `src/repositories/`: leitura e gravação do estado do sistema em JSON.
- `src/exceptions.py`: exceções próprias para erros de negócio.
- `src/main.py`: menu interativo e ponto de entrada (`python -m src.main`).
- `docs/diagramas/`: diagramas-fonte editáveis, incluindo os dois fluxos de sequência previstos para a etapa ampliada.
- `docs/instrucoes-projeto/`: instruções originais da atividade.

Essa é a organização planejada; os módulos listados ainda não foram implementados.

## Requisitos da atividade

Consulte as [instruções em Markdown](docs/instrucoes-projeto/instrucoes.md) ou baixe a [versão PDF](docs/instrucoes-projeto/instrucoes.pdf) para ver os requisitos, entregas e critérios de avaliação da 2ª VA e da 3ª VA.

Para visualizar ou exportar os diagramas, consulte as [instruções dos diagramas](docs/diagramas/README.md).
