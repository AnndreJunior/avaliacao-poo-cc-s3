from app.utils import show_message, clean
from app.modules.bancos import Banco
from app.modules.clientes import Cliente
from app.modules.contas import ContaCorrente, ContaPoupanca, Conta


def main():
    banco = Banco()
    conta: Conta | None = None

    while True:
        try:
            print("1. Criar conta")
            print("2. Depositar")
            print("3. Sacar")
            print("4. Consultar saldo")
            print("5. Histórico")
            print("0. Sair")
            print("")

            opcao = input("Selecione uma opção: ")

            if not opcao:
                raise Exception("Selecione uma opção válida")

            clean()

            match int(opcao):
                case 1:
                    while True:
                        nome = input("Informe o seu nome: ")
                        senha = input("Crie uma senha: ")

                        try:
                            cliente = Cliente(nome, senha)
                            break
                        except Exception as e:
                            show_message(e)

                    while True:
                        tipo = input(
                            "Informe o tipo da conta [Corrente/Poupança]: "
                        ).lower()

                        if tipo in ["corrente", "poupança"]:
                            conta = (
                                ContaCorrente(cliente)
                                if tipo == "corrente"
                                else ContaPoupanca(cliente)
                            )
                            banco.adicionar_conta(conta)

                            show_message("Conta criada com sucesso!")

                            break

                        show_message("A conta deve ser do tipo corrente ou poupança")

                case 2:
                    pass

                case 3:
                    pass

                case 4:
                    pass

                case 5:
                    pass

                case 0:
                    break

                case _:
                    raise Exception("Selecione uma opção válida")

        except Exception as e:
            show_message(e)


main()
