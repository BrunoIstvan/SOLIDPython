from models.reajuste import Reajuste


class AumentoAnuenio(Reajuste):

    def __init__(self, valor, data):
        self.__valor = valor
        self.__data = data

    def valor(self):
        return self.__valor

    def data(self):
        return self.__data
