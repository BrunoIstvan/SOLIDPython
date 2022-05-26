from models.reajuste_tributavel import ReajusteTributavel


class AumentoPromocao(ReajusteTributavel):

    def __init__(self, valor, data):
        self.__valor = valor
        self.__data = data

    def valor_imposto(self):
        return self.__valor * 0.1

    def valor(self):
        return self.__valor

    def data(self):
        return self.__data
