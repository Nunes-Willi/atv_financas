from financeiro.lancamento import Lancamento

class Conciliacao:
    def __init__(
        self,
        lancamentos_sistema: list[Lancamento],
        lancamentos_banco: list[Lancamento]
    ) -> None:

        self.lancamentos_sistema = lancamentos_sistema
        self.lancamentos_banco = lancamentos_banco

        self._total_sistema = 0.0
        self._total_banco = 0.0
        self._diferenca = 0.0

    @property
    def total_sistema(self) -> float:
        return self._total_sistema

    @property
    def total_banco(self) -> float:
        return self._total_banco

    @property
    def diferenca(self) -> float:
        return self._diferenca

    def calcular_total_sistema(self) -> float:
        self._total_sistema = sum(
            lancamento.valor for lancamento in self.lancamentos_sistema
        )
        return self._total_sistema

    def calcular_total_banco(self) -> float:
        self._total_banco = sum(
            lancamento.valor for lancamento in self.lancamentos_banco
        )
        return self._total_banco

    def conciliar(self) -> bool:
        self.calcular_total_sistema()
        self.calcular_total_banco()

        self._diferenca = self._total_sistema - self._total_banco

        if self._diferenca != 0:
            raise ValueError(
                f"Conciliação falhou! Sistema: R$ {self._total_sistema:.2f} | "
                f"Banco: R$ {self._total_banco:.2f} | "
                f"Diferença: R$ {self._diferenca:.2f}"
            )

        return True