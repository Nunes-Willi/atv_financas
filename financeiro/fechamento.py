from financeiro.lancamento import Lancamento
from datetime import date

class Fechamento:
    def __init__(self, data: date, lancamentos: list[Lancamento]):
        self.data = data
        self.lancamentos = lancamentos
        
        self._total_receitas = 0.0
        self._total_despesas = 0.0
        self._total_saldo = 0.0

    @property
    def total_receitas(self) -> float:
        return self._total_receitas    
    
    @property
    def total_despesas(self) -> float:
        return self._total_despesas

    @property
    def total_saldo(self) -> float:
        return self._total_saldo
    
    def calcular_receitas(self) -> float:
        self._total_receitas = sum(
            lancamento.valor
            for lancamento in self.lancamentos
            if lancamento.valor > 0
        )
        return self._total_receitas
    
    def calcular_despesas(self) -> float:
        self._total_despesas = sum(
            lancamento.valor
            for lancamento in self.lancamentos
            if lancamento.valor < 0
        )
        return self._total_despesas

    def realizar_fechamento(self) -> float:
        self.calcular_receitas()
        self.calcular_despesas()

        self._total_saldo = (
            self._total_receitas + self._total_despesas
        )
        return self._total_saldo

    def gerar_resumo(self) -> None:
        print("=== FECHAMENTO ===")
        print(f"Data: {self.data}")
        print(f"Receitas: R$ {self.total_receitas:.2f}")
        print(f"Despesas: R$ {self.total_despesas:.2f}")
        print(f"Saldo Final: R$ {self.total_saldo:.2f}")