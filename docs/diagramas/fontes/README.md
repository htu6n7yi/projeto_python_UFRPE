# Fontes dos diagramas UML

Esta pasta contém os arquivos `.puml`, que são os arquivos editáveis usados para gerar os diagramas.

| Arquivo | Diagrama |
|---|---|
| `casos-de-uso.puml` | Casos de uso |
| `classes.puml` | Diagrama de classes |
| `sequencia-locacao-sucesso.puml` | Sequência da locação realizada com sucesso |
| `sequencia-locacao-indisponivel.puml` | Sequência da locação com veículo indisponível |
| `atividades-devolucao.puml` | Atividades da devolução |

## Compilação

Com o PlantUML instalado, execute na raiz do projeto:

```bash
plantuml -tpng -o ../imagens docs/diagramas/fontes/*.puml
```

As imagens serão geradas em `docs/diagramas/imagens/`.

Para recompilar um único diagrama:

```bash
plantuml -tpng -o ../imagens docs/diagramas/fontes/classes.puml
```
