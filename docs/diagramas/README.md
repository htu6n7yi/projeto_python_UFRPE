# Diagramas UML

Esta pasta reúne os arquivos-fonte, as imagens finais e as instruções dos diagramas do projeto.

## Estrutura

```text
docs/diagramas/
├── fontes/       # arquivos editáveis .puml
├── imagens/      # diagramas finais em PNG
├── apresentacao/ # apresentação visual e descrição dos diagramas
└── README.md     # instruções de uso e compilação
```

## Fontes editáveis

Os arquivos `.puml` ficam em [`fontes/`](fontes/):

1. `casos-de-uso.puml` — operações do vendedor e relacionamentos `include`/`extend`.
2. `classes.puml` — classes de domínio, serviço, persistência e exceção.
3. `sequencia-locacao-sucesso.puml` — fluxo principal de locação.
4. `sequencia-locacao-indisponivel.puml` — fluxo alternativo quando o veículo não está disponível.
5. `atividades-devolucao.puml` — decisão de atraso e finalização da devolução.

## Imagens finais

As versões prontas para visualização ficam em [`imagens/`](imagens/). A apresentação com imagens, descrições e legenda dos símbolos está em [`apresentacao/README.md`](apresentacao/README.md).

## Compilar os diagramas

### Com PlantUML instalado

Na raiz do projeto, execute:

```bash
plantuml -tpng -o ../imagens docs/diagramas/fontes/*.puml
```

O argumento `-o ../imagens` salva as imagens em `docs/diagramas/imagens/`.

Para gerar um único diagrama:

```bash
plantuml -tpng -o ../imagens docs/diagramas/fontes/classes.puml
```

### Com VS Code

Instale uma extensão PlantUML, abra um arquivo `.puml` dentro de `fontes/` e use o comando de exportação configurado pela extensão.

## Observações

- `Cliente` possui um CPF público.
- `Vendedor` possui uma CTPS pública.
- Atualize a fonte `.puml` e recompile o PNG correspondente sempre que o modelo mudar.
