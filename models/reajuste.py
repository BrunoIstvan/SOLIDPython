from abc import ABC, abstractmethod


class Reajuste(ABC):

    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def data(self):
        pass
