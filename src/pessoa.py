class Pessoa:
    """Superclasse base para perfis cadastrais do sistema."""

    def __init__(self, nome: str, idade: int, telefone: str, email: str):
        self._nome = nome
        self._idade = idade
        self._telefone = telefone
        self._email = email

    def get_nome(self) -> str:
        return self._nome

    def exibir_dados(self) -> str:
        return (
            f"Nome: {self._nome} | Idade: {self._idade} | "
            f"Tel: {self._telefone} | E-mail: {self._email}"
        )


class Vendedor(Pessoa):
    def __init__(self, nome: str, idade: int, telefone: str, email: str, ctps: str):
        super().__init__(nome, idade, telefone, email)
        self.__ctps = ctps

    def get_ctps(self) -> str:
        return self.__ctps

    def exibir_dados(self) -> str:
        return f"[Vendedor] {super().exibir_dados()} | CTPS: {self.__ctps}"


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int, telefone: str, email: str, cpf: str):
        super().__init__(nome, idade, telefone, email)
        self.__cpf = cpf

    def get_cpf(self) -> str:
        return self.__cpf

    def exibir_dados(self) -> str:
        return f"[Cliente] {super().exibir_dados()} | CPF: {self.__cpf}"