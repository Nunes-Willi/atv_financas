from abc import ABC, abstractmethod

class EstrategiaJuros(ABC):
    @abstractmethod
    def calcular(self, capital: float, taxa: float, periodos: int) -> float:
        ...

class JurosSimples(EstrategiaJuros):
    def calcular(self, capital: float, taxa: float, periodos: int) -> float:
        return capital * (taxa / 100) * periodos

class JurosCompostos(EstrategiaJuros):
    def calcular(self, capital: float, taxa: float, periodos: int) -> float:
        return capital * ((1 + taxa / 100) ** periodos) - capital
