from unittest import TestCase

from models.cargo import Cargo
from models.funcionario import Funcionario
from services.promocao_service import PromocaoService


class TestPromocaoService(TestCase):

    def test_promover(self):

        funcionario = Funcionario(nome='B', cpf='4', salario=1000.0, cargo=Cargo.ASSISTENTE)

        promocao_service = PromocaoService()

        promocao_service.promover(funcionario, meta_batida=True)

        assert funcionario.cargo == Cargo.ANALISTA
