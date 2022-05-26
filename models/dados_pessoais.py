from models.cargo import Cargo


class DadosPessoais:

    def __init__(self, nome, cpf, cargo: Cargo, salario):
        self.__nome = nome
        self.__cpf = cpf
        self.__cargo = cargo
        self.__salario = salario

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo: Cargo):
        self.__cargo = cargo

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario: float):
        self.__salario = salario
