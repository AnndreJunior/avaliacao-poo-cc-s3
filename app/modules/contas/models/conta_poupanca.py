from .conta import Conta
from app.modules.clientes.models.cliente import Cliente
from app.modules.movimentacoes import Operacao


class ContaPoupanca(Conta):
    def __init__(self, cliente: Cliente):
        super().__init__(cliente)

    def sacar(self, valor: float) -> None:
        self._validar_valor_saque(valor)

        self._saldo -= valor
        self._historico.adicionar(Operacao("saque", valor))
