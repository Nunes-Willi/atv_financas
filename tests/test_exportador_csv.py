from datetime import date

from financeiro.exportador_csv import ExportarCSV
from financeiro.lancamento import Lancamento


class TestExportarCSV:

    def test_criar_doc(self):
        exportador = ExportarCSV()

        relatorio = []

        documento = exportador.criar_doc(relatorio)

        assert documento == []

    def test_add_cabecalho(self):
        exportador = ExportarCSV()

        documento = []
        relatorio = []

        exportador.add_cabecalho(documento, relatorio)

        assert documento == [
            ["Data", "Descrição", "Valor"]
        ]

    def test_add_corpo(self):
        exportador = ExportarCSV()

        lancamento = Lancamento(
            "Salário",
            5000,
            date.today(),
            None
        )

        relatorio = [lancamento]
        documento = []

        exportador.add_corpo(documento, relatorio)

        assert documento == [[
            lancamento.data,
            lancamento.descricao,
            lancamento.valor
        ]]

    def test_add_corpo_com_varios_lancamentos(self):
        exportador = ExportarCSV()

        lancamento1 = Lancamento(
            "Salário",
            5000,
            date.today(),
            None
        )

        lancamento2 = Lancamento(
            "Mercado",
            -300,
            date.today(),
            None
        )

        relatorio = [lancamento1, lancamento2]
        documento = []

        exportador.add_corpo(documento, relatorio)

        assert len(documento) == 2

        assert documento[0] == [
            lancamento1.data,
            lancamento1.descricao,
            lancamento1.valor
        ]

        assert documento[1] == [
            lancamento2.data,
            lancamento2.descricao,
            lancamento2.valor
        ]

    def test_add_rodape(self):
        exportador = ExportarCSV()

        documento = []
        relatorio = []

        resultado = exportador.add_rodape(documento, relatorio)

        assert resultado is None

    def test_salvar(self):
        exportador = ExportarCSV()

        documento = [
            ["Data", "Descrição", "Valor"]
        ]

        resultado = exportador.salvar(documento)

        assert resultado is None

    def test_exportar(self):
        exportador = ExportarCSV()

        lancamento = Lancamento(
            "Salário",
            5000,
            date.today(),
            None
        )

        relatorio = [lancamento]

        exportador.exportar(relatorio)