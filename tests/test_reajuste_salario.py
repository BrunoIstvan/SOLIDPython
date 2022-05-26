import datetime
from unittest import TestCase

from exceptions.custom_exceptions import ValidacaoException
from models.cargo import Cargo
from models.funcionario import Funcionario
from services.reajuste_service import ReajusteService
from services.validacao_percentual_reajuste import ValidacaoPercentualReajuste
from services.validacao_periodicidade_entre_reajustes import ValidacaoPeriodicidadeReajustes


class ReajusteServiceTest(TestCase):

    def test_reajustar_salario(self):

        funcionario = Funcionario(nome='B', cpf='4', salario=1000.0, cargo=Cargo.ANALISTA)

        assert funcionario.salario == 1000.0
        assert funcionario.data_ultimo_reajuste is None

        validacoes = [ValidacaoPercentualReajuste(), ValidacaoPeriodicidadeReajustes()]

        reajuste_service = ReajusteService(validacoes=validacoes)

        # valida se o valor do reajuste é maior que 40% e lança uma exceção
        with self.assertRaises(ValidacaoException):
            reajuste_service.reajustar_salario(funcionario, 410)

        # realiza um ajuste de 20%
        reajuste_service.reajustar_salario(funcionario, 200)

        # valida se tudo foi atualizado
        assert funcionario.salario == 1200
        assert funcionario.data_ultimo_reajuste == datetime.date.today()

        # tenta realizar um novo ajuste...
        # deve tomar uma exceção por conta do período do novo reajuste ser menor que 6 meses
        with self.assertRaises(ValidacaoException):
            reajuste_service.reajustar_salario(funcionario, 200)

        # valida se nada foi atualizado
        assert funcionario.salario == 1200
        assert funcionario.data_ultimo_reajuste == datetime.date.today()
