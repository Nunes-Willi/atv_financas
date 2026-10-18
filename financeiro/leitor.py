from abc import ABC, abstractmethod

from financeiro.lancamento import Lancamento

class Leitor(ABC):
    @abstractmethod
    def ler(self, caminho: str) -> list[Lancamento]:
        ...
