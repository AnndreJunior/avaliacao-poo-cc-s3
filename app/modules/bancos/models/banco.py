from app.modules.contas import Conta


class Banco:
    def __init__(self):
        self.__contas: list[Conta] = []

    def adicionar_conta(self, conta: Conta):
        self.__contas.append(conta)

    def listar_contas(self) -> list[Conta]:
        return self.__contas
