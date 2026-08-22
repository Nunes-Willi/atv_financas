from datetime import date
from financeiro.categoria import Categoria

class Lancamento:
    def __init__(self, descricao: str, valor: float, data: date, categoria: Categoria) -> None:
        self.descricao = descricao
        self.valor = valor
        self.data = data
        self.categoria = categoria
        
    def validar_valor(self) -> bool:
        if self.valor == 0:
            raise ValueError ("O valor do lançamento não pode ser zero.")
        return True
        
    def validar_descricao(self) -> bool:
        if self.descricao == "":
            raise ValueError("A descrição não pode estar vazia")
        return True