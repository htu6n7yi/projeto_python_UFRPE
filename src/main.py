"""Interface CLI de backoffice para operação da locadora."""

from datetime import datetime, date
from typing import Optional
from src.pessoa import Vendedor, Cliente
from src.veiculo import Veiculo
from src.locacao import Locacao


def ler_texto_obrigatorio(mensagem: str) -> str:
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("Este campo não pode ficar vazio.")


def ler_inteiro(mensagem: str, minimo: int = 0) -> int:
    while True:
        try:
            valor = int(input(mensagem).strip())
            if valor < minimo:
                print(f"Valor inválido! Informe um número maior ou igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")


def ler_float(mensagem: str, minimo: float = 0.01) -> float:
    while True:
        try:
            texto = input(mensagem).strip().replace(",", ".")
            valor = float(texto)
            if valor < minimo:
                print(f"Valor inválido! O mínimo permitido é R$ {minimo:.2f}.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida! Digite um valor numérico válido (ex: 120.50).")


def ler_data(mensagem: str, data_minima: Optional[date] = None) -> date:
    while True:
        texto = input(mensagem).strip()
        try:
            data_informada = datetime.strptime(texto, "%d/%m/%Y").date()
            if data_minima and data_informada < data_minima:
                print(
                    f"Data incoerente! Informe uma data igual ou posterior a "
                    f"{data_minima.strftime('%d/%m/%Y')}."
                )
                continue
            return data_informada
        except ValueError:
            print("Data inválida! Use o formato DD/MM/AAAA (ex: 26/11/2026).")


def main() -> None:
    vendedor_ativo = Vendedor(
        "Carlos Silva", 30, "(81) 99999-0000", "carlos@locadora.com", "CTPS-12345"
    )

    clientes: list[Cliente] = []
    veiculos: list[Veiculo] = []
    locacoes: list[Locacao] = []

    print("\n=== Sistema de Locadora de Veículos (Backoffice) ===")
    print(f"Operador: {vendedor_ativo.exibir_dados()}")

    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Cadastrar Cliente")
        print("2. Cadastrar Veículo")
        print("3. Consultar Veículos")
        print("4. Realizar Locação")
        print("5. Registrar Devolução")
        print("0. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            print("\n-- Cadastrar Cliente --")
            cpf = ler_texto_obrigatorio("CPF: ")
            if any(c.get_cpf() == cpf for c in clientes):
                print("Já existe um cliente cadastrado com este CPF.")
                continue

            nome = ler_texto_obrigatorio("Nome: ")
            idade = ler_inteiro("Idade (mínimo 18): ", minimo=18)
            telefone = ler_texto_obrigatorio("Telefone: ")
            email = ler_texto_obrigatorio("E-mail: ")

            clientes.append(Cliente(nome, idade, telefone, email, cpf))
            print("Cliente cadastrado com sucesso!")

        elif opcao == "2":
            print("\n-- Cadastrar Veículo --")
            placa = ler_texto_obrigatorio("Placa: ").upper()
            if any(v.get_placa() == placa for v in veiculos):
                print("Já existe um veículo cadastrado com esta placa.")
                continue

            marca = ler_texto_obrigatorio("Marca: ")
            modelo = ler_texto_obrigatorio("Modelo: ")
            cor = ler_texto_obrigatorio("Cor: ")
            preco = ler_float("Preço da diária (R$): ", minimo=0.01)

            veiculos.append(Veiculo(marca, modelo, cor, placa, preco))
            print("Veículo cadastrado com sucesso!")

        elif opcao == "3":
            print("\n-- Consultar Veículos --")
            if not veiculos:
                print("Nenhum veículo cadastrado.")
                continue

            filtrar = input("Filtrar apenas disponíveis? (S/N): ").strip().upper()
            encontrados = False
            for v in veiculos:
                if filtrar == "S" and not v.is_disponivel():
                    continue
                print(v.exibir_dados())
                encontrados = True

            if not encontrados:
                print("Nenhum veículo disponível no momento.")

        elif opcao == "4":
            print("\n-- Realizar Locação --")
            cpf = ler_texto_obrigatorio("CPF do Cliente: ")
            cliente = next((c for c in clientes if c.get_cpf() == cpf), None)
            if not cliente:
                print("Cliente não encontrado. Cadastre-o primeiro.")
                continue

            placa = ler_texto_obrigatorio("Placa do Veículo: ").upper()
            veiculo = next((v for v in veiculos if v.get_placa() == placa), None)
            if not veiculo:
                print("Veículo não encontrado.")
                continue

            if not veiculo.is_disponivel():
                print("Veículo indisponível para locação.")
                continue

            data_loc = ler_data("Data da locação (DD/MM/AAAA): ", data_minima=date.today())
            data_prev = ler_data(
                "Data prevista de devolução (DD/MM/AAAA): ", data_minima=data_loc
            )
            tipo_pag = ler_texto_obrigatorio("Tipo de pagamento (PIX / Cartão / Dinheiro): ")

            locacao = Locacao(
                cliente, veiculo, vendedor_ativo, data_loc, data_prev, tipo_pag
            )
            veiculo.set_disponivel(False)
            locacoes.append(locacao)

            print("\nLocação confirmada com sucesso!")
            print(locacao.get_pagamento().exibir_recibo())

        elif opcao == "5":
            print("\n-- Registrar Devolução --")
            placa = ler_texto_obrigatorio("Placa do veículo devolvido: ").upper()
            locacao_ativa = next(
                (
                    loc
                    for loc in locacoes
                    if loc.get_veiculo().get_placa() == placa
                    and loc.get_status() == "Ativa"
                ),
                None,
            )

            if not locacao_ativa:
                print("Locação ativa não encontrada para esta placa.")
                continue

            data_real = ler_data(
                "Data real da devolução (DD/MM/AAAA): ",
                data_minima=locacao_ativa.get_data_locacao(),
            )
            multa = locacao_ativa.finalizar_devolucao(data_real)

            if multa > 0:
                print(f"Devolução com atraso! Multa aplicada: R$ {multa:.2f}")
            else:
                print("Devolução registrada no prazo (sem multa).")

            print(f"Status do veículo {placa} atualizado para: Disponível.")

        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Escolha um número de 0 a 5.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExecução interrompida pelo operador. Encerrando...")