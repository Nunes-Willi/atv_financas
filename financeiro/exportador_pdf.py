from financeiro.exportador_relatorio import ExportRelatorio

class ExportadorPDF(ExportRelatorio):

    def criar_doc(self, relatorio):
        return []

    def add_cabecalho(self, documento, relatorio):
        documento.append("RELATÓRIO FINANCEIRO")
        documento.append("Data | Descrição | Valor")

    def add_corpo(self, documento, relatorio):
        for lancamento in relatorio:
            documento.append(
                f"{lancamento.data} | "
                f"{lancamento.descricao} | "
                f"{lancamento.valor}"
            )

    def add_rodape(self, documento, relatorio):
        documento.append("FIM DO RELATÓRIO")

    def salvar(self, documento):
        pass