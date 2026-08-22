from financeiro.lancamento import Lancamento
from datetime import date

class fechamento:
    def __init__(self, data: date, lancamento: Lancamento):
        self.data = date
        self.lancamentos: list[Lancamento] = []