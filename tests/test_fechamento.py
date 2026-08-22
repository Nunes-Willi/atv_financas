import pytest
from datetime import date

from financeiro.categoria import Categoria
from financeiro.lancamento import Lancamento
from financeiro.fechamento import Fechamento


class TestFechamento:

    def test_calcular_receitas(self):
        lancamentos = [
            Lancamento("Salário", 3000, date.today(), Categoria("Receita")),
            Lancamento("Mercado", -200, date.today(), Categoria("Alimentação")),
            Lancamento("Freela", 500, date.today(), Categoria("Receita")),
        ]
        
        fechamento = Fechamento(date.today(), lancamentos)
        assert fechamento.calcular_receitas() == 3500

    def test_calcular_despesas(self):
        lancamentos = [
            Lancamento("Salário", 3000, date.today(), Categoria("Receita")),
            Lancamento("Uber", -50, date.today(), Categoria("Transporte")),
            Lancamento("Mercado", -150, date.today(), Categoria("Alimentação")),
        ]

        fechamento = Fechamento(date.today(), lancamentos)
        assert fechamento.calcular_despesas() == -200

    def test_realizar_fechamento(self):
        lancamentos = [
            Lancamento("Salário", 2500, date.today(), Categoria("Receita")),
            Lancamento("Internet", -100, date.today(), Categoria("Contas")),
            Lancamento("Mercado", -400, date.today(), Categoria("Alimentação")),
        ]

        fechamento = Fechamento(date.today(), lancamentos)
        saldo = fechamento.realizar_fechamento()

        assert saldo == 2000
        assert fechamento.total_receitas == 2500
        assert fechamento.total_despesas == -500
        assert fechamento.total_saldo == 2000

    def test_fechamento_sem_lancamentos(self):
        fechamento = Fechamento(date.today(), [])

        assert fechamento.realizar_fechamento() == 0
        assert fechamento.total_receitas == 0
        assert fechamento.total_despesas == 0