from datetime import date
import pytest

from financeiro.categoria import Categoria
from financeiro.lancamento import Lancamento

class TestLancamento:
    def test_criar_lancamento(self):
        categoria = Categoria("Transporte")
        lancamento = Lancamento("Uber", -25.0, date.today(), categoria)

        assert lancamento.descricao == "Uber"
        assert lancamento.valor == -25.0
        assert lancamento.categoria.nome == "Transporte"

    def test_validar_valor(self):
        categoria = Categoria("Mercado")
        lancamento = Lancamento("Compras", 0, date.today(), categoria)

        with pytest.raises(ValueError):
            lancamento.validar_valor()

    def test_validar_descricao(self):
        categoria = Categoria("Lazer")
        lancamento = Lancamento("", 50, date.today(), categoria)

        with pytest.raises(ValueError):
            lancamento.validar_descricao()