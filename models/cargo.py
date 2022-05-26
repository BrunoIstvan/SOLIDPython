from enum import Enum


class CallableEnum(Enum):
    """
    Inherit this class to create a Callable Enum
    """

    def __call__(self, *args, **kwargs):
        return self.value[0](*args, **kwargs)


def register(func):
    """
    Decorator to easily define tuples that contain functions
    """
    return func,


class Cargo(CallableEnum):
    ASSISTENTE = 1
    ANALISTA = 2
    ESPECIALISTA = 3
    GERENTE = 4

    @staticmethod
    def proximo_cargo(cargo):
        if cargo == Cargo.GERENTE:
            return Cargo.GERENTE

        novo_cargo = cargo.value + 1
        return Cargo(novo_cargo)
