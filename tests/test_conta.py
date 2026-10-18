from datetime import date
import pytest

from financeiro.conta import Conta
from financeiro.categoria import Categoria
from financeiro.lancamento import Lancamento
from financeiro.estrategia_rendimento import (
    SemRendimento,
    PercentualRendido
)


class TestConta:
    def test_criar_conta(self):
        usuario = Conta("William", 20, 0.0)

        assert usuario.abrir_conta() is True

    def test_conta_sem_nome(self):
        usuario = Conta("", 20, 0.0)

        with pytest.raises(ValueError):
            usuario.abrir_conta()

    def test_menor_de_idade(self):
        usuario = Conta("João", 17, 0.0)

        with pytest.raises(ValueError):
            usuario.abrir_conta()

    def test_adicionar_lancamento(self):
        conta = Conta("William", 20, 100)

        categoria = Categoria("Salário")
        lancamento = Lancamento("Pagamento", 500, date.today(), categoria)

        conta.adicionar_lancamento(lancamento)

        assert len(conta.lancamentos) == 1
        assert conta.lancamentos[0] == lancamento

    def test_remover_lancamento(self):
        conta = Conta("William", 20, 100)

        categoria = Categoria("Transporte")
        lancamento = Lancamento("Ônibus", -10, date.today(), categoria)

        conta.adicionar_lancamento(lancamento)
        conta.remover_lancamento(lancamento)

        assert len(conta.lancamentos) == 0

    def test_calcular_saldo(self):
        conta = Conta("William", 20, 1000)

        salario = Lancamento(
            "Salário", 2000, date.today(), Categoria("Receita")
        )
        mercado = Lancamento(
            "Mercado", -300, date.today(), Categoria("Alimentação")
        )

        conta.adicionar_lancamento(salario)
        conta.adicionar_lancamento(mercado)

        assert conta.calcular_saldo(SemRendimento()) == 2700

    def test_calcular_saldo_sem_rendimento(self):
        conta = Conta("William", 20, 1000)

        assert conta.calcular_saldo(SemRendimento()) == 1000

    def test_calcular_saldo_com_rendimento(self):
        conta = Conta("William", 20, 1000)

        assert conta.calcular_saldo(PercentualRendido(10)) == 1100

    def test_calcular_saldo_com_lancamentos_e_rendimento(self):
        conta = Conta("William", 20, 1000)

        salario = Lancamento(
            "Salário", 200, date.today(), Categoria("Receita")
        )
        conta.adicionar_lancamento(salario)
        
        assert conta.calcular_saldo(PercentualRendido(10)) == 1320

    def test_calcular_saldo_com_rendimento_zero(self):
        conta = Conta("William", 20, 1000)

        assert conta.calcular_saldo(PercentualRendido(0)) == 1000

    def test_remover_lancamento_e_calcular_saldo(self):
        conta = Conta("William", 20, 1000)

        mercado = Lancamento(
            "Mercado", -200, date.today(), Categoria("Alimentação")
        )

        conta.adicionar_lancamento(mercado)
        conta.remover_lancamento(mercado)

        assert conta.calcular_saldo(SemRendimento()) == 1000
