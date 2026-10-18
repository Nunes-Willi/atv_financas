from financeiro.estrategia_correcao import (
    SemCorrecao,
    CorrecaoTaxaFixa
)


def test_sem_correcao():
    estrategia = SemCorrecao()

    assert estrategia.calcular(1000, 4) == 1000


def test_correcao_taxa_fixa():
    estrategia = CorrecaoTaxaFixa()

    assert estrategia.calcular(1000, 4) == 1040


def test_correcao_sem_taxa():
    estrategia = CorrecaoTaxaFixa()

    assert estrategia.calcular(1000, 0) == 1000


def test_correcao_valor_zero():
    estrategia = CorrecaoTaxaFixa()

    assert estrategia.calcular(0, 4) == 0


def test_correcao_taxa_negativa():
    estrategia = CorrecaoTaxaFixa()

    assert estrategia.calcular(1000, -4) == 960
