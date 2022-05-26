from typing import List

from models.funcionario import Funcionario
from services.validacao_reajuste_interface import IValidacaoReajuste


class ReajusteService(object):

    def __init__(self, validacoes: List[IValidacaoReajuste]):
        """
        Construtor que recebe lista de validacoes

            Parameters:
                validacoes: Lista de validacoes do tipo IValidacaoReajuste
        """
        self.validacoes = validacoes

    def reajustar_salario(self, funcionario: Funcionario, aumento: float):
        """
        Realiza a chamada das validacoes antes de aplicar o reajuste do salario

            Parameters:
                funcionario: Funcionario a ter o salario reajustado
                aumento: Valor do aumento
            Returns:
                Nada
            Raises:
                ValidacaoException
        """

        for val in self.validacoes:
            val.validar(funcionario, aumento=aumento)

        funcionario.atualizar_salario(funcionario.salario + aumento)
