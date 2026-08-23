from financeiro.fechamento import Fechamento

class Extrato:
    def __init__(self, mes: int, ano: int, fechamentos: list[Fechamento]) -> None:
        self.mes = mes
        self.ano = ano
        self.fechamentos = fechamentos

        self._total_lancamentos = 0
        self._total_creditos = 0.0
        self._total_debitos = 0.0
        self._saldo_final = 0.0

    @property
    def total_lancamentos(self) -> int:
        return self._total_lancamentos

    @property
    def total_creditos(self) -> float:
        return self._total_creditos

    @property
    def total_debitos(self) -> float:
        return self._total_debitos

    @property
    def saldo_final(self) -> float:
        return self._saldo_final

    def gerar_extrato(self) -> None:
        fechamentos_periodo = [
            fechamento for fechamento in self.fechamentos
            if fechamento.data.month == self.mes
            and fechamento.data.year == self.ano
        ]

        self._total_lancamentos = sum(
            len(fechamento.lancamentos)
            for fechamento in fechamentos_periodo
        )

        self._total_creditos = sum(
            fechamento.total_receitas
            for fechamento in fechamentos_periodo
        )

        self._total_debitos = sum(
            abs(fechamento.total_despesas)
            for fechamento in fechamentos_periodo
        )

        self._saldo_final = sum(
            fechamento.total_saldo
            for fechamento in fechamentos_periodo
        )

        print("====== EXTRATO ======")
        print(f"Período: {self.mes}/{self.ano}")
        print(f"Total de lançamentos: {self._total_lancamentos}")
        print(f"Total de créditos: R$ {self._total_creditos:.2f}")
        print(f"Total de débitos: R$ {self._total_debitos:.2f}")
        print(f"Saldo final: R$ {self._saldo_final:.2f}")