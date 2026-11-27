from datetime import date
from typing import Optional
from src.pessoa import Cliente, Vendedor
from src.veiculo import Veiculo


class Pagamento:
    def __init__(self, tipo: str, valor: float):
        self.__tipo = tipo
        self.__valor = valor

    def get_tipo(self) -> str:
        return self.__tipo

    def get_valor(self) -> float:
        return self.__valor

    def exibir_recibo(self) -> str:
        return f"Pagamento via {self.__tipo} | Valor Total: R$ {self.__valor:.2f}"


class Locacao:
    """Gerencia o contrato de aluguel, devolução e composição do pagamento."""

    def __init__(
        self,
        cliente: Cliente,
        veiculo: Veiculo,
        vendedor: Vendedor,
        data_locacao: date,
        data_devolucao_prevista: date,
        tipo_pagamento: str,
    ):
        self.__cliente = cliente
        self.__veiculo = veiculo
        self.__vendedor = vendedor
        self.__data_locacao = data_locacao
        self.__data_devolucao_prevista = data_devolucao_prevista
        self.__data_devolucao_real: Optional[date] = None
        self.__status = "Ativa"
        self.__pagamento = Pagamento(tipo_pagamento, self.calcular_valor_total())

    def get_veiculo(self) -> Veiculo:
        return self.__veiculo

    def get_data_locacao(self) -> date:
        return self.__data_locacao

    def get_status(self) -> str:
        return self.__status

    def get_pagamento(self) -> Pagamento:
        return self.__pagamento

    def calcular_valor_total(self) -> float:
        # Locação no mesmo dia cobra no mínimo 1 diária
        dias = max(1, (self.__data_devolucao_prevista - self.__data_locacao).days)
        return dias * self.__veiculo.get_preco_diaria()

    def calcular_multa(self, data_real: date) -> float:
        # Regra de negócio: multa de 150% da diária por dia de atraso
        if data_real > self.__data_devolucao_prevista:
            dias_atraso = (data_real - self.__data_devolucao_prevista).days
            return dias_atraso * (self.__veiculo.get_preco_diaria() * 1.5)
        return 0.0

    def finalizar_devolucao(self, data_real: date) -> float:
        self.__data_devolucao_real = data_real
        multa = self.calcular_multa(data_real)
        self.__status = "Finalizada"
        self.__veiculo.set_disponivel(True)
        return multa