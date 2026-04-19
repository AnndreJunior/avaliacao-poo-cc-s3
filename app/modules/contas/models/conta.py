import random
from abc import ABC, abstractmethod
from app.modules.clientes.models.cliente import Cliente
from app.modules.movimentacoes import Historico, Operacao


class Conta(ABC):
    def __init__(self, cliente: Cliente):
        self._numero = self.__gerar_numero_da_conta()
        self._saldo = 0.0
        self._cliente = cliente
        self._historico = Historico()

    @property
    def numero(self):
        return self._numero

    @property
    def saldo(self):
        return self._saldo

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def depositar(self, valor: float):
        if valor <= 0:
            raise Exception("O valor para depósito deve ser maior que zero")

        self._saldo += valor
        self._historico.adicionar(Operacao("depósito", valor))

    @abstractmethod
    def sacar(self, valor: float) -> None:
        pass

    def _validar_valor_saque(self, valor: float) -> None:
        if valor <= 0:
            raise Exception("O valor de saque deve ser maior que zero")

        if valor > self._saldo:
            raise Exception("Saldo insuficiente para saque")

    def __gerar_numero_da_conta(self):
        numero_str = "".join([str(random.randint(1, 9)) for _ in range(8)])

        return int(numero_str)
