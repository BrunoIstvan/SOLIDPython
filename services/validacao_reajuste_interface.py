from abc import ABC

from models.funcionario import Funcionario


class IValidacaoReajuste(ABC):

    def validar(self, funcionario: Funcionario, **kwargs):
        pass
