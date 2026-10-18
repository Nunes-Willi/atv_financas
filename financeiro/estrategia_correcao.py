from abc import ABC, abstractmethod

class EstrategiaCorrecao(ABC):
    @abstractmethod
    def calcular(self, valor: float, taxa: float) -> float:
        ...

class SemCorrecao(EstrategiaCorrecao):
    def calcular(self, valor: float, taxa: float) -> float:
        return valor

class CorrecaoTaxaFixa(EstrategiaCorrecao):
    def calcular(self, valor: float, taxa: float) -> float:
        return valor * (1 + taxa / 100)