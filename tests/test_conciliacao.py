from datetime import date
import pytest

from financeiro.categoria import Categoria
from financeiro.lancamento import Lancamento
from financeiro.conciliacao import Conciliacao


class TestConciliacao:

    def test_conciliacao_com_sucesso(self):
        sistema = [
            Lancamento("Salário", 2000, date.today(), Categoria("Receita")),
            Lancamento("Mercado", -300, date.today(), Categoria("Alimentação"))
        ]

        banco = [
            Lancamento("Salário", 2000, date.today(), Categoria("Receita")),
            Lancamento("Mercado", -300, date.today(), Categoria("Alimentação"))
        ]

        conciliacao = Conciliacao(sistema, banco)

        assert conciliacao.conciliar() is True
        assert conciliacao.total_sistema == 1700
        assert conciliacao.total_banco == 1700
        assert conciliacao.diferenca == 0

    def test_conciliacao_com_diferenca(self):
        sistema = [
            Lancamento("Salário", 2000, date.today(), Categoria("Receita"))
        ]

        banco = [
            Lancamento("Salário", 1800, date.today(), Categoria("Receita"))
        ]

        conciliacao = Conciliacao(sistema, banco)

        with pytest.raises(ValueError):
            conciliacao.conciliar()