from .pessoa import Pessoa


class Vendedor(Pessoa):
    def __init__(self, nome: str, idade: int,salario:int) -> None:
        super().__init__(nome, idade)
        self.salario = salario