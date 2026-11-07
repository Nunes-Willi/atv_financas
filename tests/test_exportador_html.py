from datetime import date

from financeiro.exportador_html import ExportadorHTML
from financeiro.lancamento import Lancamento
from financeiro.categoria import Categoria


class TestExportadorHTML:

    def criar_lancamento(self):
        categoria = Categoria("Salário")

        return Lancamento(
            "Pagamento",
            500.0,
            date(2026, 11, 7),
            categoria
        )

    def test_criar_doc(self):
        exportador = ExportadorHTML()

        documento = exportador.criar_doc([])

        assert documento == []

    def test_add_cabecalho(self):
        exportador = ExportadorHTML()
        documento = []

        exportador.add_cabecalho(documento, [])

        assert "<html>" in documento
        assert "<body>" in documento
        assert "<h1> Extrato </h1>" in documento

    def test_add_corpo(self):
        exportador = ExportadorHTML()
        documento = []

        lancamento = self.criar_lancamento()

        exportador.add_corpo(documento, [lancamento])

        assert "<table>" in documento
        assert f"<td> {lancamento.data} </td>" in documento
        assert f"<td> {lancamento.descricao} </td>" in documento
        assert f"<td> {lancamento.valor} </td>" in documento

    def test_add_rodape(self):
        exportador = ExportadorHTML()
        documento = []

        exportador.add_rodape(documento, [])

        assert "</body>" in documento
        assert "</html>" in documento

    def test_salvar(self):
        exportador = ExportadorHTML()
        documento = []
        resultado = exportador.salvar(documento)

        assert resultado is None