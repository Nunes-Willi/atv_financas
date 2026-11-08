import pytest

from financeiro.importador_banco import ImportadorBancoX, ImportadorBancoY, CriadorImportador

from financeiro.leitor import LeitorCSV, LeitorJSON

class TestImportadorBanco:

    def test_importador_banco_x(self):
        leitor = LeitorCSV()
        importador = ImportadorBancoX(leitor)

        assert isinstance(importador.leitor, LeitorCSV)

    def test_importador_banco_y(self):
        leitor = LeitorJSON()
        importador = ImportadorBancoY(leitor)

        assert isinstance(importador.leitor, LeitorJSON)

    def test_criar_banco_x(self):
        criador = CriadorImportador()

        importador = criador.criar("BANCO_X")

        assert isinstance(importador, ImportadorBancoX)
        assert isinstance(importador.leitor, LeitorCSV)

    def test_criar_banco_y(self):
        criador = CriadorImportador()

        importador = criador.criar("BANCO_Y")

        assert isinstance(importador, ImportadorBancoY)
        assert isinstance(importador.leitor, LeitorJSON)

    def test_banco_desconhecido(self):
        criador = CriadorImportador()

        with pytest.raises(ValueError, match="Banco desconhecido"):
            criador.criar("BANCO_Z")