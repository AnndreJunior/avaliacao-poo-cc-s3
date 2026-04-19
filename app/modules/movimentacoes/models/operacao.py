class Operacao:
    def __init__(self, tipo: str, valor: float):
        self.__tipo = tipo
        self.__valor = valor

    @property
    def tipo(self) -> str:
        return self.__tipo

    @property
    def valor(self) -> float:
        return self.__valor
