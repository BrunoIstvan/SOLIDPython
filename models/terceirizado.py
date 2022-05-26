from models.dados_pessoais import DadosPessoais


class Terceirizado(object):

    def __init__(self, dados_pessoais: DadosPessoais, empresa: str):
        self.__dados_pessoais = dados_pessoais
        self.__empresa = empresa

    @property
    def nome(self):
        return self.__dados_pessoais.nome

    @property
    def cpf(self):
        return self.__dados_pessoais.cpf

    @property
    def cargo(self):
        return self.__dados_pessoais.cargo

    @property
    def salario(self):
        return self.__dados_pessoais.salario

    @property
    def empresa(self):
        return self.__empresa

    @empresa.setter
    def empresa(self, empresa):
        self.__empresa = empresa

