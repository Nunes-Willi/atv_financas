import pytest

from financeiro.exportador_relatorio import ExportRelatorio


class ExportRelatorioTeste(ExportRelatorio):
    def criar_doc(self, relatorio):
        return {
            "relatorio": relatorio
        }

    def add_cabecalho(self, documento, relatorio):
        documento["cabecalho"] = True

    def add_corpo(self, documento, relatorio):
        documento["corpo"] = True

    def add_rodape(self, documento, relatorio):
        documento["rodape"] = True

    def salvar(self, documento):
        self.documento_salvo = documento


class TestExportRelatorio:

    def test_criar_documento(self):
        exportador = ExportRelatorioTeste()
        relatorio = ["lancamento 1", "lancamento 2"]

        documento = exportador.criar_doc(relatorio)

        assert documento["relatorio"] == relatorio

    def test_exportar(self):
        exportador = ExportRelatorioTeste()
        relatorio = ["lancamento 1"]

        exportador.exportar(relatorio)

        assert exportador.documento_salvo["relatorio"] == relatorio
        assert exportador.documento_salvo["cabecalho"] is True
        assert exportador.documento_salvo["corpo"] is True
        assert exportador.documento_salvo["rodape"] is True

    def test_classe_e_abstrata(self):
        with pytest.raises(TypeError):
            ExportRelatorio()