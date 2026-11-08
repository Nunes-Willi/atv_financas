import pytest
from datetime import date

from financeiro.categoria import Categoria
from financeiro.lancamento import Lancamento

from financeiro.exportador import ExportarRelatorio, ExportarCSV, ExportarHTML, ExportarPDF

#! Testes Class ExportarRelatorio(Abstrata)
class ExportRelatorioTeste(ExportarRelatorio):
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
            ExportarRelatorio()
     
            
#! Testes Class ExportarCSV(Concreto)
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
        

#! Testes Class ExportarHTML(Concreto)
class TestExportarHTML:

    def criar_lancamento(self):
        categoria = Categoria("Salário")

        return Lancamento(
            "Pagamento",
            500.0,
            date(2026, 11, 7),
            categoria
        )

    def test_criar_doc(self):
        exportador = ExportarHTML()

        documento = exportador.criar_doc([])

        assert documento == []

    def test_add_cabecalho(self):
        exportador = ExportarHTML()
        documento = []

        exportador.add_cabecalho(documento, [])

        assert "<html>" in documento
        assert "<body>" in documento
        assert "<h1> Extrato </h1>" in documento

    def test_add_corpo(self):
        exportador = ExportarHTML()
        documento = []

        lancamento = self.criar_lancamento()

        exportador.add_corpo(documento, [lancamento])

        assert "<table>" in documento
        assert f"<td> {lancamento.data} </td>" in documento
        assert f"<td> {lancamento.descricao} </td>" in documento
        assert f"<td> {lancamento.valor} </td>" in documento

    def test_add_rodape(self):
        exportador = ExportarHTML()
        documento = []

        exportador.add_rodape(documento, [])

        assert "</body>" in documento
        assert "</html>" in documento

    def test_salvar(self):
        exportador = ExportarHTML()
        documento = []
        resultado = exportador.salvar(documento)

        assert resultado is None
        

#! Testes Class ExportarPDF(Concreto)
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
        exportador = ExportarPDF()

        documento = exportador.criar_doc([])

        assert documento == []

    def test_add_cabecalho(self):
        exportador = ExportarPDF()
        documento = []

        exportador.add_cabecalho(documento, [])

        assert "RELATÓRIO FINANCEIRO" in documento
        assert "Data | Descrição | Valor" in documento

    def test_add_corpo(self):
        exportador = ExportarPDF()
        documento = []

        lancamento = self.criar_lancamento()

        exportador.add_corpo(documento, [lancamento])

        assert (
            f"{lancamento.data} | "
            f"{lancamento.descricao} | "
            f"{lancamento.valor}"
        ) in documento

    def test_add_rodape(self):
        exportador = ExportarPDF()
        documento = []

        exportador.add_rodape(documento, [])

        assert "FIM DO RELATÓRIO" in documento

    def test_salvar(self):
        exportador = ExportarPDF()
        documento = []

        resultado = exportador.salvar(documento)

        assert resultado is None