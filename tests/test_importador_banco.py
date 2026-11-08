import pytest

from financeiro.importador_banco import ImportadorBancoX, ImportadorBancoY, CriadorImportador

from financeiro.leitor import LeitorCSV, LeitorJSON


class TestImportadorBanco:

    def test_importador_banco_x(self):
        importador = ImportadorBancoX()

        assert isinstance(importador.leitor, LeitorCSV)

    def test_importador_banco_y(self):
        importador = ImportadorBancoY()

        assert isinstance(importador.leitor, LeitorJSON)

    def test_importar_banco_x(self, tmp_path):
        arquivo = tmp_path / "extrato.csv"

        arquivo.write_text(
            "data,descricao,valor,categoria\n"
            "2026-11-08,Salário,3000.0,Salário\n"
        )

        importador = ImportadorBancoX()
        lancamentos = importador.importar(arquivo)

        assert len(lancamentos) == 1
        assert lancamentos[0].descricao == "Salário"

    def test_importar_banco_y(self, tmp_path):
        arquivo = tmp_path / "extrato.json"

        arquivo.write_text(
            '[{"data": "2026-11-08", '
            '"descricao": "Salário", '
            '"valor": 3000.0, '
            '"categoria": "Salário"}]'
        )

        importador = ImportadorBancoY()
        lancamentos = importador.importar(arquivo)

        assert len(lancamentos) == 1
        assert lancamentos[0].descricao == "Salário"


class TestCriadorImportador:

    def test_criar_banco_x(self):
        criador = CriadorImportador()

        importador = criador.criar("BANCO_X")

        assert isinstance(importador, ImportadorBancoX)

    def test_criar_banco_y(self):
        criador = CriadorImportador()

        importador = criador.criar("BANCO_Y")

        assert isinstance(importador, ImportadorBancoY)

    def test_banco_desconhecido(self):
        criador = CriadorImportador()

        with pytest.raises(ValueError, match="Banco desconhecido"):
            criador.criar("BANCO_Z")