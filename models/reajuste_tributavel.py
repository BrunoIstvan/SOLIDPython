from abc import abstractmethod

from models.reajuste import Reajuste


class ReajusteTributavel(Reajuste):

    @abstractmethod
    def valor_imposto(self):
        pass
