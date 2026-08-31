from abc import ABC, abstractmethod


class EstrategiaRendimento(ABC):
    @abstractmethod
    def calcular(self, total: float) -> float:
        ...
        
class SemRendimento(EstrategiaRendimento):
    def calcular(self, total: float) -> float:
        return total
    
class PercentualRendido(EstrategiaRendimento):
    def __init__(self, percentual: float) -> None:
        if not 0 <= percentual <= 100:
            raise ValueError("Percentual deve estar entre 0 e 100")
        self.__percentual = percentual
        
    def calcular(self, total: float) -> float:
        return total - (total * self.__percentual /100)