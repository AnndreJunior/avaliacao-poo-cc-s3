class Cliente:
    def __init__(self, nome: str, senha: str):
        self.__set_nome(nome)
        self.__set_senha(senha)

    @property
    def nome(self):
        return self.__nome

    @property
    def senha(self):
        return self.__senha

    def __set_nome(self, nome: str):
        if not nome:
            raise Exception("O nome deve ser informado")

        if len(nome) > 80:
            raise Exception("O nome deve conter até 80 caracteres")

        self.__nome = nome

    def __set_senha(self, senha: str):
        if not senha:
            raise Exception("A senha deve ser informada")

        if len(senha) < 8 or len(senha) > 30:
            raise Exception("A senha deve conter entre 8 e 30 caracteres")

        self.__senha = senha
