from exceptions.custom_exceptions import ValidacaoException
from models.funcionario import Funcionario
from services.validacao_reajuste_interface import IValidacaoReajuste


class ValidacaoPercentualReajuste(IValidacaoReajuste):

    def validar(self, funcionario: Funcionario, **kwargs):
        """
        Valida se o percentual de reajuste e' maior que o previsto pelo empregador

            Parameters:
                funcionario: Funcionario a ser validado
                kwargs: É esperado o parametro 'aumento'
            Returns:
                Nada em caso de sucesso.
            Raises:
                ValidacaoException em caso de percentual maior que o previsto
        """

        percentual_reajuste: float = kwargs.get('aumento') / funcionario.salario
        if percentual_reajuste > 0.4:
            raise ValidacaoException("Reajuste nao pode ser superior a 40% do salario!")
