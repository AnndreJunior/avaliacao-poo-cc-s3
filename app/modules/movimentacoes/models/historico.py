from .operacao import Operacao


class Historico:
    def __init__(self):
        self.__operacoes: list[Operacao] = []

    def adicionar(self, operacao: Operacao):
        self.__operacoes.append(operacao)

    def listar(self):
        return self.__operacoes
