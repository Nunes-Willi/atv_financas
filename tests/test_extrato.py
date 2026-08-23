from datetime import date

from financeiro.categoria import Categoria
from financeiro.lancamento import Lancamento
from financeiro.fechamento import Fechamento
from financeiro.extrato import Extrato


class TestExtrato:

    def test_gerar_extrato(self):
        lancamentos = [
            Lancamento("Salário", 3000, date(2026, 8, 5), Categoria("Receita")),
            Lancamento("Mercado", -500, date(2026, 8, 5), Categoria("Alimentação"))
        ]

        fechamento = Fechamento(date(2026, 8, 5), lancamentos)
        fechamento.realizar_fechamento()

        extrato = Extrato(8, 2026, [fechamento])
        extrato.gerar_extrato()

        assert extrato.total_lancamentos == 2
        assert extrato.total_creditos == 3000
        assert extrato.total_debitos == 500
        assert extrato.saldo_final == 2500

    def test_extrato_sem_fechamentos(self):
        extrato = Extrato(8, 2026, [])

        extrato.gerar_extrato()

        assert extrato.total_lancamentos == 0
        assert extrato.total_creditos == 0
        assert extrato.total_debitos == 0
        assert extrato.saldo_final == 0