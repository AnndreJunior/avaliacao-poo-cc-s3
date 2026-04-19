from .conta import Conta
from app.modules.clientes.models.cliente import Cliente
from app.modules.movimentacoes import Operacao


class ContaCorrente(Conta):
    def __init__(self, cliente: Cliente):
        super().__init__(cliente)

    def sacar(self, valor: float) -> None:
        TAXA_SAQUE = 5.50

        self._validar_valor_saque(valor)

        valor_saque = valor + TAXA_SAQUE
        self._saldo -= valor_saque
        self._historico.adicionar(Operacao("saque", valor_saque))
