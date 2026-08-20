from datetime import date
from financeiro.categoria import Categoria

class Lancamento:
    def __init__(self, descricao: str, valor: float, data: date, categoria: Categoria) -> None:
        self.descricao = descricao
        self.valor = valor
        self.data = data.today()
        self.categoria: categoria