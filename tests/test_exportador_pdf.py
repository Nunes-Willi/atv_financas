from datetime import date

from financeiro.exportador_pdf import ExportadorPDF
from financeiro.lancamento import Lancamento
from financeiro.categoria import Categoria


class TestExportadorPDF:

    def criar_lancamento(self):
        categoria = Categoria("Salário")

        return Lancamento(
            "Pagamento",
            500.0,
            date(2026, 11, 7),
            categoria
        )

    def test_criar_doc(self):
        exportador = ExportadorPDF()

        documento = exportador.criar_doc([])

        assert documento == []

    def test_add_cabecalho(self):
        exportador = ExportadorPDF()
        documento = []

        exportador.add_cabecalho(documento, [])

        assert "RELATÓRIO FINANCEIRO" in documento
        assert "Data | Descrição | Valor" in documento

    def test_add_corpo(self):
        exportador = ExportadorPDF()
        documento = []

        lancamento = self.criar_lancamento()

        exportador.add_corpo(documento, [lancamento])

        assert (
            f"{lancamento.data} | "
            f"{lancamento.descricao} | "
            f"{lancamento.valor}"
        ) in documento

    def test_add_rodape(self):
        exportador = ExportadorPDF()
        documento = []

        exportador.add_rodape(documento, [])

        assert "FIM DO RELATÓRIO" in documento

    def test_salvar(self):
        exportador = ExportadorPDF()
        documento = []

        resultado = exportador.salvar(documento)

        assert resultado is None