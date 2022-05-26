from exceptions.custom_exceptions import ValidacaoException
from models.cargo import Cargo
from models.funcionario import Funcionario


class PromocaoService:

    def promover(self, funcionario: Funcionario, meta_batida: bool):

        cargo_atual = funcionario.cargo

        if cargo_atual == Cargo.GERENTE:
            raise ValidacaoException('Gerentes não podem ser promovidos')

        if meta_batida:
            novo_cargo = Cargo.proximo_cargo(cargo_atual)
            funcionario.promover(novo_cargo)
        else:
            raise ValidacaoException('Funcionário não bateu a meta')
