from app.utils import show_message


def main():
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

            match int(opcao):
                case 1:
                    pass

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
