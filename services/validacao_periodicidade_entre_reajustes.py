import datetime

from dateutil import relativedelta
from exceptions.custom_exceptions import ValidacaoException
from models.funcionario import Funcionario
from services.validacao_reajuste_interface import IValidacaoReajuste


class ValidacaoPeriodicidadeReajustes(IValidacaoReajuste):

    def validar(self, funcionario: Funcionario, **kwargs):
        """
        Valida se o periodo do reajuste e' menor que 6 meses compadada a data do ultimo reajuste

            Parameters:
                funcionario: Funcionario a ser validado
                kwargs: Inutilizado
            Returns:
                Nada em caso de sucesso.
            Raises:
                ValidacaoException em caso de reajuste antes de 6 meses
        """

        data_ultimo_reajuste = funcionario.data_ultimo_reajuste
        data_atual = datetime.date.today()
        delta = relativedelta.relativedelta(data_atual, data_ultimo_reajuste)
        if data_ultimo_reajuste is not None and delta.months < 6:
            raise ValidacaoException("Data do último reajuste deve ser no mínimo de 6 meses")
