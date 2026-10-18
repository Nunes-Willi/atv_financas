from financeiro.estrategia_juros import (
    JurosSimples,
    JurosCompostos
)


def test_juros_simples():
    estrategia = JurosSimples()

    assert estrategia.calcular(1000, 2, 3) == 60


def test_juros_compostos():
    estrategia = JurosCompostos()

    resultado = estrategia.calcular(1000, 2, 3)

    assert round(resultado, 2) == 61.21


def test_juros_simples_sem_capital():
    estrategia = JurosSimples()

    assert estrategia.calcular(0, 2, 3) == 0


def test_juros_compostos_sem_capital():
    estrategia = JurosCompostos()

    assert estrategia.calcular(0, 2, 3) == 0


def test_juros_simples_sem_taxa():
    estrategia = JurosSimples()

    assert estrategia.calcular(1000, 0, 3) == 0


def test_juros_compostos_sem_taxa():
    estrategia = JurosCompostos()

    assert estrategia.calcular(1000, 0, 3) == 0
