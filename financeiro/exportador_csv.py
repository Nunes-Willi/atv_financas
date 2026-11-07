from exportador_relatorio import ExportRelatorio

class ExportarCSV(ExportRelatorio):
    def criar_doc(self, relatorio):
        return []
    
    def add_cabecalho(self, documento, relatorio):
       documento.append(["Data", "Descrição", "Valor"])
       
    def add_corpo(self, documento, relatorio):
        for lancamento in relatorio:
            documento.append([
                lancamento.data,
                lancamento.descricao,
                lancamento.valor
            ])
            
    def add_rodape(self, documento, relatorio):
        pass
    
    def salvar(self, documento):
        ...