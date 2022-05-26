import datetime

from models.dados_pessoais import DadosPessoais


class Funcionario(object):

    def __init__(self, dados_pessoais: DadosPessoais):
        self.__dados_pessoais = dados_pessoais
        self.__data_ultimo_reajuste = None

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
    def data_ultimo_reajuste(self):
        return self.__data_ultimo_reajuste

    @data_ultimo_reajuste.setter
    def data_ultimo_reajuste(self, data_ultimo_reajuste):
        self.__data_ultimo_reajuste = data_ultimo_reajuste

    def atualizar_salario(self, novo_salario: float):
        self.__dados_pessoais.salario = novo_salario
        self.data_ultimo_reajuste = datetime.date.today()

    def promover(self, novo_cargo):
        self.__dados_pessoais.cargo = novo_cargo
