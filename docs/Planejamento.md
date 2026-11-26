Tema escolhido: Locadora de veículos:

* Informações do sistema: 
* Veiculos (Marca, Modelo, Cor, Placa, Preço, disponível)
* Pessoas (Nome, Idade, Telefone, Email)
** Pessoas->Vendedores (CTPS)
** Pessoas->Clientes (CPF)
* Pagamento (Tipo, Valor)
  
* Funcionalidades:
** Cadastro Cliente
** Cadastro Veiculo
** Consulta de veiculo
*** Dados veiculo, disponibilidade
** Alugar
*** data locação, data devolução
** Devolver
*** Status Veiculo

## Organização proposta

- `src/models/`: `Pessoa` (abstrata), `Cliente`, `Vendedor`, `Veiculo`, `Locacao` e `Pagamento`.
- `src/services/locadora_service.py`: regras para cadastro, consulta, locação e devolução.
- `src/repositories/arquivo_json.py`: carregamento e salvamento dos dados em JSON.
- `src/exceptions.py`: exceções de validação e de regras de negócio.
- `src/main.py`: menu CLI e interação com a pessoa usuária.
- `docs/diagramas/`: fontes PlantUML dos diagramas UML.

`Cliente` e `Vendedor` herdam de `Pessoa` e especializam `exibir_dados()`. Uma locação associa cliente, vendedor e veículo; pagamentos pertencem à locação. A locação tem um pagamento inicial e pode ter um pagamento adicional de multa.

## Decisões pendentes

- Definir como calcular a multa (valor fixo ou taxa por dia de atraso) antes de implementar a devolução.
- Definir quais formas de pagamento o menu aceitará.
- Confirmar se o grupo fará a entrega regular ou a etapa ampliada da 3ª VA. Os diagramas já incluem dois fluxos de sequência; abstração, exceção personalizada e persistência também estão previstas na arquitetura, mas ainda não implementadas.
