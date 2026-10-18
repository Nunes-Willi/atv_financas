import pytest

from financeiro.estrategia_rendimento import (
    SemRendimento,
    PercentualRendido
)


def test_sem_rendimento():
    estrategia = SemRendimento()

    assert estrategia.calcular(1000) == 1000


def test_percentual_rendido():
    estrategia = PercentualRendido(10)

    assert estrategia.calcular(1000) == 1100


def test_percentual_rendido_zero():
    estrategia = PercentualRendido(0)

    assert estrategia.calcular(1000) == 1000


def test_percentual_rendido_cem():
    estrategia = PercentualRendido(100)

    assert estrategia.calcular(1000) == 2000


def test_percentual_negativo():
    with pytest.raises(ValueError):
        PercentualRendido(-1)


def test_percentual_acima_de_cem():
    with pytest.raises(ValueError):
        PercentualRendido(101)
