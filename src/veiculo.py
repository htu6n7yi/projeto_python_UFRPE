class Veiculo:
    """Entidade de veículo com controle de disponibilidade na frota."""

    def __init__(
        self, marca: str, modelo: str, cor: str, placa: str, preco_diaria: float
    ):
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__placa = placa.upper()
        self.__preco_diaria = preco_diaria
        self.__disponivel = True

    def get_placa(self) -> str:
        return self.__placa

    def get_preco_diaria(self) -> float:
        return self.__preco_diaria

    def is_disponivel(self) -> bool:
        return self.__disponivel

    def set_disponivel(self, status: bool) -> None:
        self.__disponivel = status

    def exibir_dados(self) -> str:
        status_txt = "Disponível" if self.__disponivel else "Alugado"
        return (
            f"{self.__marca} {self.__modelo} ({self.__cor}) | "
            f"Placa: {self.__placa} | Diária: R$ {self.__preco_diaria:.2f} | "
            f"Status: {status_txt}"
        )